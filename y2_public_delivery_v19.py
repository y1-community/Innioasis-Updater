"""Release-locked Windows-only delivery contract for the Y2 Class A update.

This module deliberately contains no network, UI, subprocess or device code.  The
three Updater CE entry sources import it so catalogue/download/install decisions
all use one fail-closed contract.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ASSET_NAME = "Y2-Rockbox-Beta-v0.2.0-Windows-UPDATE-ONLY.zip"
ASSET_SIZE = 361_774_260
ASSET_SHA256 = "409ddb4d2d18111fb8c3ab619f10f04b916b6b2a3fc04d1d38011324563f326a"
MODEL = "Y2"
PLATFORM = "Windows"
CATALOGUE_REPOSITORY = "y1-community/rockbox-y2-rom"
RELEASE_TAG = "v0.2.0-beta"
SUPPORTED_BASELINES = ("Stock 3.1.7", "Beta V2 P17 Centre Context V1")
MBR_SIZE = 512
MBR_SHA256 = "4be9c92be18ba4169d4b050e18811c6650eab27a487f1c67f4a49efa01cd32a1"
MBR_LOGICAL_START = 0x01400000
FORBIDDEN_OUTPUT = re.compile(
    r"(?i)(format\s*all|format-download|firmware\s*upgrade|\berase\b|download\s+failed|\berror\b)"
)


class DeliveryBlocked(RuntimeError):
    pass


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def asset_name_from_url(url: str) -> str:
    return unquote(urlparse(str(url)).path.rsplit("/", 1)[-1])


def classify_release_asset(asset: dict, platform_name: str) -> dict | None:
    """Recognize only the manifest-bound public Y2 Class A Windows asset."""
    if asset.get("name") != ASSET_NAME:
        return None
    if platform_name != PLATFORM:
        raise DeliveryBlocked("Y2 Class A Beta V2 is Windows-only; platform handoff refused")
    if int(asset.get("size", -1)) != ASSET_SIZE:
        raise DeliveryBlocked("Y2 Class A release asset size differs from the approved contract")
    digest = str(asset.get("digest", "")).lower()
    if digest != "sha256:" + ASSET_SHA256:
        raise DeliveryBlocked("Y2 Class A release asset digest is absent or differs")
    if not asset.get("browser_download_url"):
        raise DeliveryBlocked("Y2 Class A release asset has no immutable download URL")
    return {
        "asset": asset, "type": "A", "resolution": "native", "model": MODEL,
        "contract": "y2-class-a-windows", "sha256": ASSET_SHA256, "size": ASSET_SIZE,
    }


def select_release_asset(release: dict, platform_name: str, selected_model: str,
                         repository: str = CATALOGUE_REPOSITORY) -> dict:
    if repository.lower() != CATALOGUE_REPOSITORY:
        raise DeliveryBlocked("Y2 Class A asset came from an unapproved catalogue repository")
    if release.get("tag_name") != RELEASE_TAG:
        raise DeliveryBlocked("Y2 Class A release tag differs from the approved Beta V2 tag")
    if str(selected_model).upper() != MODEL:
        raise DeliveryBlocked("Y2 Class A asset cannot be selected for another model")
    accepted = []
    for asset in release.get("assets", []):
        if asset.get("name") == ASSET_NAME:
            accepted.append(classify_release_asset(asset, platform_name))
    if len(accepted) != 1:
        raise DeliveryBlocked("Release must contain exactly one approved Y2 Class A Windows asset")
    return accepted[0]


def validate_download(path: Path, url: str | None = None) -> Path:
    candidate = Path(path)
    if not candidate.is_absolute():
        raise DeliveryBlocked("Candidate path must remain absolute")
    candidate = candidate.resolve(strict=True)
    if candidate.name != ASSET_NAME:
        raise DeliveryBlocked("Downloaded candidate filename differs from release contract")
    if url and asset_name_from_url(url) != ASSET_NAME:
        raise DeliveryBlocked("Download URL does not name the approved release asset")
    if not candidate.is_file() or candidate.is_symlink():
        raise DeliveryBlocked("Candidate is not an ordinary file")
    if candidate.stat().st_size != ASSET_SIZE or sha256(candidate) != ASSET_SHA256:
        raise DeliveryBlocked("Downloaded candidate bytes differ from the approved release asset")
    return candidate


def require_windows(platform_name: str) -> None:
    if platform_name != PLATFORM:
        raise DeliveryBlocked("Y2 Class A updater path is qualified only on Windows")


def validate_prewrite_identity(mbr_path: Path, baseline: str) -> dict:
    if baseline not in SUPPORTED_BASELINES:
        raise DeliveryBlocked("Starting baseline is not explicitly supported")
    mbr = Path(mbr_path).resolve(strict=True)
    if not mbr.is_file() or mbr.is_symlink():
        raise DeliveryBlocked("MBR evidence is not an ordinary file")
    if mbr.stat().st_size != MBR_SIZE or sha256(mbr) != MBR_SHA256:
        raise DeliveryBlocked("Y2 MBR/layout identity mismatch")
    return {
        "status": "PASS", "model": MODEL, "soc": "MT6582", "project": "eastaeon82_wet_kk",
        "baseline": baseline, "storage": "EMMC_USER", "part_id": 8,
        "address_mode": "NUTL_ADDR_LOGICAL", "mbr_start": MBR_LOGICAL_START,
        "mbr_size": MBR_SIZE, "mbr_sha256": MBR_SHA256,
    }


def evaluate_write_completion(stdout: str, exit_code: int, natural_completion: bool) -> dict:
    text = stdout or ""
    if not natural_completion or exit_code != 0:
        raise DeliveryBlocked("Flash Tool did not complete naturally with exit code 0")
    if "Download Succeeded" not in text:
        raise DeliveryBlocked("Explicit Download Succeeded evidence is absent")
    percents = [int(x) for x in re.findall(r"(?<!\d)(\d{1,3})\s*%", text)]
    if not percents or max(percents) != 100:
        raise DeliveryBlocked("Observed write progress did not reach exactly 100%")
    if FORBIDDEN_OUTPUT.search(text):
        raise DeliveryBlocked("Forbidden error/format/erase output was observed")
    if "Disconnect!" in text and text.find("Disconnect!") < text.find("Download Succeeded"):
        raise DeliveryBlocked("USB disconnected before explicit write success")
    return {"status": "PASS-WRITE-COMPLETED", "exit_code": 0,
            "natural_completion": True, "positive_evidence": "Download Succeeded",
            "progress_max_percent": 100, "retry_performed": False}


def require_usb_cycle(observations: list[dict]) -> dict:
    """Require connected -> disconnected -> one fresh connected observation."""
    states = [bool(x.get("connected")) for x in observations]
    try:
        first_on = states.index(True)
        off = states.index(False, first_on + 1)
        second_on = states.index(True, off + 1)
    except ValueError as exc:
        raise DeliveryBlocked("Fresh disconnect/reconnect boundary was not observed") from exc
    if any(states[second_on + 1:]):
        raise DeliveryBlocked("More than one reconnect was observed")
    return {"status": "PASS", "disconnect_index": off, "reconnect_index": second_on}


def unique_evidence_dir(root: Path, session_id: str) -> Path:
    if not re.fullmatch(r"[0-9]{8}T[0-9]{6}Z-[0-9a-f]{12}", session_id):
        raise DeliveryBlocked("Invalid evidence session identity")
    path = Path(root).resolve() / ("Y2-Class-A-" + session_id)
    if path.exists():
        raise DeliveryBlocked("Evidence session already exists")
    return path
