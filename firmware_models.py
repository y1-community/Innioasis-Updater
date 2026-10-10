"""Model catalogue, release-asset matching, and flash safety for Innioasis Updater.

A new stock model is onboarded with one ``slidia_manifest.xml`` line plus a
GitHub release whose firmware asset is ``rom_<model>.zip``. This module is the
decision layer the updater calls before it writes anything to a device.

Flashing rules:

* Y1 and Y2 keep their existing, tested install paths.
* Q3, Q5, R1, and SR1 may use a generic scatter path, but only when the zip
  name, the selected model, and the scatter's platform line all agree, the
  images are unsigned, and there is no dynamic ``super`` partition. The
  package is extracted into its own directory so it cannot replace the Y1/Y2
  scatter. Q3 and Q5 packages ship a file named ``MT6580_Android_scatter.txt``
  whose platform line is MT6582. That is the same chip family as the Y2. The
  flash plan still comes from that package's own scatter and preloader, not
  from the Y2 partition layout.
* G1, G3, and G5 (and A5, which is recognised but has no tested profile) are
  downloadable only. G1 and G3 images are signed. Their ``-en-wm`` releases
  identify internally as S2 (G1) and S4 (G3) and are not interchangeable with
  the other G1/G3 builds. G5 images are signed and use ``super.img``.

Nothing in here opens a USB device or invokes SP Flash Tool.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional, Sequence
from xml.etree import ElementTree as ET


GITHUB_MAX_ASSET_BYTES = 2 * 1024 * 1024 * 1024
PAYLOAD_DIR_NAME = "firmware_payloads"
GENERIC_SPFLASH_XML = "install_rom_sp_generic.xml"
DA_FILENAME = "MTK_AllInOne_DA.bin"

# Legacy DA chips this tree already knows how to drive from a package scatter.
# Newer secure-boot parts are intentionally absent.
GENERIC_SCATTER_CHIPS = frozenset({"MT6572", "MT6580", "MT6582"})

_SIGNED_NAME = re.compile(r"(?i)(?:-sign\b|_sign\b|-verified\b|_verified\b)")
_ROM_MODEL = re.compile(r"(?i)(?:^|/)rom[_-]([a-z0-9]+)\.zip$")
_PLATFORM = re.compile(r"(?im)^\s*platform:\s*(MT\d+)\b")
_SCATTER_BLOCK = re.compile(r"(?m)^-\s*partition_index:")


@dataclass(frozen=True)
class ModelProfile:
    """One player or recorder the catalogue can name."""

    id: str
    brand: str
    chip: str
    flash: str
    reason: str
    power_button: str
    kind: str = "player"

    @property
    def product(self) -> str:
        return f"{self.brand} {self.id}"

    @property
    def asset_name(self) -> str:
        return f"rom_{self.id.lower()}.zip"

    @property
    def repo_name(self) -> str:
        return f"{self.id.lower()}-stock-rom"


# flash values: builtin_y1, builtin_y2, generic_scatter, download_only
PROFILES = {
    "Y1": ModelProfile(
        "Y1", "Innioasis", "MT6572", "builtin_y1",
        "Tested Y1 install path (named partitions / MT6572 scatter).",
        "centre button",
    ),
    "Y2": ModelProfile(
        "Y2", "Innioasis", "MT6582", "builtin_y2",
        "Tested Y2 install path (MT6582 scatter offsets).",
        "power/lock button",
    ),
    "A5": ModelProfile(
        "A5", "Timmkoo", "MT6572", "download_only",
        "A5 packages are recognised by name, but this updater has no tested "
        "flash profile for them. They are not written with the Y1 path.",
        "power button",
    ),
    "Q3": ModelProfile(
        "Q3", "Timmkoo", "MT6582", "generic_scatter",
        "The scatter file is named MT6580_Android_scatter.txt, but its "
        "platform line is MT6582 (same chip family as the Y2). Flashing uses "
        "this package's scatter and preloader only, not the Y2 partition "
        "layout. Q3 firmware identifies itself as Q3E. This path has not been "
        "run on Q3 hardware.",
        "power button",
    ),
    "Q5": ModelProfile(
        "Q5", "Timmkoo", "MT6582", "generic_scatter",
        "The scatter file is named MT6580_Android_scatter.txt, but its "
        "platform line is MT6582 (same chip family as the Y2). Flashing uses "
        "this package's scatter and preloader only, not the Y2 partition "
        "layout. This path has not been run on Q5 hardware.",
        "power button",
    ),
    "R1": ModelProfile(
        "R1", "Innioasis", "MT6572", "generic_scatter",
        "MT6572 voice recorder. Same chip family as the Y1, different project "
        "and images, so the Y1 partition list is not used.",
        "power button",
        kind="recorder",
    ),
    "SR1": ModelProfile(
        "SR1", "Innioasis", "MT6582", "generic_scatter",
        "MT6582 voice recorder. Same chip family as the Y2, different "
        "preloader, so the Y2 preloader is not used.",
        "power button",
        kind="recorder",
    ),
    "G1": ModelProfile(
        "G1", "Innioasis", "MT6753", "download_only",
        "G1 stock images are signed (secure boot, MT6753). Automatic flashing "
        "is not supported yet. English WM releases (tags such as 5.01-en-wm) "
        "identify internally as S2 and may be a different board from the other "
        "G1 builds. They are not interchangeable.",
        "power button",
    ),
    "G3": ModelProfile(
        "G3", "Innioasis", "MT6753", "download_only",
        "G3 stock images are signed (secure boot, MT6753). Automatic flashing "
        "is not supported yet. English WM releases (tags such as 6.01-en-wm) "
        "identify internally as S4 and may be a different board from the other "
        "G3 builds. They are not interchangeable.",
        "power button",
    ),
    "G5": ModelProfile(
        "G5", "Innioasis", "MT6765", "download_only",
        "G5 stock images are signed and use a dynamic super.img (Android 12) "
        "on a secure-boot MT6765. Automatic flashing is not supported yet. "
        "The published zip is 2,049,171,366 bytes, under GitHub's 2 GiB limit.",
        "power button",
    ),
}

# Measured size of the repacked G5 stock zip. It is under the GitHub asset limit.
G5_PUBLISHED_ZIP_BYTES = 2_049_171_366

# Tags such as 3.27-en, 5.01-en-wm, 3.03-multi, 1.48.
_STOCK_TAG = re.compile(
    r"^(?P<ver>\d+(?:\.\d+)+)(?:-(?P<suffix>en-wm|multi|en|de|es))?$",
    re.IGNORECASE,
)
_STOCK_TAG_LABELS = {
    "en": "English",
    "de": "German",
    "es": "Spanish",
    "multi": "Multi-language",
    "en-wm": "English · WM",
}

# Models this change adds to the stock manifest. Y1/Y2 already have entries.
STOCK_MANIFEST_MODELS = ("Q3", "Q5", "G1", "G3", "R1", "SR1", "G5")


@dataclass
class FlashAssessment:
    """What the updater is allowed to do with one package."""

    action: str
    model: str
    message: str
    chip: str = ""
    preloader: str = ""
    scatter_name: str = ""
    errors: list = field(default_factory=list)

    @property
    def ok_to_flash(self) -> bool:
        return self.action in ("builtin", "generic")


def profile_for(model) -> Optional[ModelProfile]:
    key = canonical_model(model)
    if not key:
        return None
    return PROFILES.get(key)


def canonical_model(model) -> str:
    text = str(model or "").strip().upper()
    if not text:
        return ""
    if text in PROFILES:
        return text
    return ""


def stock_release_variant(tag) -> Optional[tuple]:
    """``(version, label)`` for a stock tag, or None.

    ``3.27-en`` is ``("3.27", "English")``. ``1.48`` and ``1.11`` are
    ``("1.48", "")`` and ``("1.11", "")``. Other tag shapes return None so
    custom-firmware tags keep the existing parser.
    """
    match = _STOCK_TAG.match(str(tag or "").strip())
    if not match:
        return None
    suffix = (match.group("suffix") or "").lower()
    return match.group("ver"), _STOCK_TAG_LABELS.get(suffix, "")


def release_variant_warning(model, tag) -> str:
    """Extra list text when a regional build must not be mixed with another."""
    parsed = stock_release_variant(tag)
    if not parsed or parsed[1] != "English · WM":
        return ""
    key = canonical_model(model)
    if key == "G1":
        return (
            "WM build. This package identifies internally as S2 and is not "
            "interchangeable with the other G1 releases."
        )
    if key == "G3":
        return (
            "WM build. This package identifies internally as S4 and is not "
            "interchangeable with the other G3 releases."
        )
    return ""


def preferred_default_model(models: Iterable[str]) -> str:
    """Keep Y1 as the opening selection when the catalogue grows."""
    present = []
    for model in models:
        key = str(model or "").strip().upper()
        if key and key not in present:
            present.append(key)
    if "Y1" in present:
        return "Y1"
    return sorted(present)[0] if present else ""


def uses_isolated_payload(model) -> bool:
    profile = profile_for(model)
    return bool(profile and profile.flash == "generic_scatter")


def payload_directory(tool_dir, model) -> Path:
    key = canonical_model(model) or "unknown"
    return Path(tool_dir) / PAYLOAD_DIR_NAME / key


def model_from_zip_name(name_or_url_or_path) -> Optional[str]:
    """Return a catalogue model from ``rom_<model>.zip``, or None.

    ``rom_type_b.zip`` and ``rom_240p.zip`` do not match: the token would be
    ``type`` / ``240p`` or the name has more than one suffix segment.
    ``rom_g5.zip`` is G5, not A5. ``rom_sr1.zip`` is SR1, not Y2 or R1.
    """
    if not name_or_url_or_path:
        return None
    try:
        from urllib.parse import urlparse
        raw = urlparse(str(name_or_url_or_path)).path.rsplit("/", 1)[-1]
    except Exception:
        raw = str(name_or_url_or_path).replace("\\", "/").rsplit("/", 1)[-1]
    match = _ROM_MODEL.search(raw.strip())
    if not match:
        return None
    return canonical_model(match.group(1)) or None


def classify_rom_asset(name, tag_name="", repo="") -> str:
    """Classify a ``rom*.zip`` asset as a model id or ``dual`` (legacy Y1).

    ``dual`` keeps the historical meaning: a plain ``rom.zip`` may be offered
    to Y1. It is never offered to Q3/Q5/G1/G3/G5/R1/SR1.
    """
    explicit = model_from_zip_name(name)
    if explicit:
        return explicit

    lower = (name or "").lower()
    tag_lower = (tag_name or "").lower()
    repo_lower = (repo or "").lower()
    repo_name = repo_lower.split("/")[-1] if "/" in repo_lower else repo_lower

    if "_y2" in lower or lower.startswith("rom_y2") or lower.startswith("rom-y2"):
        return "Y2"
    if any(token in lower for token in ("mt6582", "eastaeon82", "6582")):
        return "Y2"
    if any(token in tag_lower for token in ("mt6582", "eastaeon82", "6582")):
        return "Y2"
    if "y2" in tag_lower and "y1" not in tag_lower:
        return "Y2"
    if "y2" in repo_name and "y1" not in repo_name.replace("y2", "", 1):
        return "Y2"
    return "dual"


def variant_matches(asset_model, selected_model, package_device="", repo="") -> bool:
    """True when one release asset may be listed for the selected device."""
    selected = canonical_model(selected_model) or str(selected_model or "").strip().upper()
    asset = asset_model or "dual"
    package = str(package_device or "").strip().upper()
    repo_name = (repo or "").lower().split("/")[-1]

    if selected and selected not in ("Y1", "Y2") and selected in PROFILES:
        return asset == selected

    if selected == "Y2":
        if asset == "Y2":
            return True
        if asset != "dual":
            return False
        if package == "Y1":
            return False
        if package == "Y2" and "y2" not in repo_name:
            return False
        return True

    if selected == "Y1":
        if package == "Y2" or asset == "Y2":
            return False
        if asset not in ("Y1", "dual"):
            return False
        return True
    return False


def manifest_package_line(model, org="y1-community", name="Original Software") -> str:
    profile = profile_for(model)
    if profile is None:
        raise ValueError(f"Unknown model {model!r}")
    repo = f"{org}/{profile.repo_name}"
    url = f"https://github.com/{repo}"
    return (
        f'<package name="{name}" repo="{repo}" device="{profile.id}" '
        f'url="{url}" type="img" handler="Custom Firmware" />'
    )


def devices_in_manifest(xml_text: str) -> list:
    """Device ids from a manifest, skipping legacy device_type entries."""
    root = ET.fromstring(xml_text)
    devices = []
    for node in root.findall("package"):
        if node.get("device_type") is not None:
            continue
        device = (node.get("device") or "").strip()
        if device and device not in devices:
            devices.append(device)
    return devices


def parse_scatter_platform(scatter_text: str) -> str:
    match = _PLATFORM.search(scatter_text or "")
    return match.group(1).upper() if match else ""


def parse_scatter_project(scatter_text: str) -> str:
    match = re.search(r"(?im)^\s*project:\s*(\S+)", scatter_text or "")
    return match.group(1) if match else ""


def parse_scatter_downloads(scatter_text: str) -> list:
    """Downloadable partitions: name, file, index, is_download."""
    parts = []
    for block in _SCATTER_BLOCK.split(scatter_text or "")[1:]:
        idx = re.match(r"\s*SYS(\d+)", block)
        name = re.search(r"partition_name:\s*(\S+)", block)
        file_name = re.search(r"file_name:\s*(\S+)", block)
        download = re.search(r"is_download:\s*(\S+)", block)
        fname = (file_name.group(1) if file_name else "NONE").strip()
        if not fname or fname.upper() == "NONE":
            continue
        enabled = True
        if download and download.group(1).strip().lower() in ("false", "0", "no"):
            enabled = False
        if not enabled:
            continue
        try:
            index = int(idx.group(1)) if idx else -1
        except ValueError:
            index = -1
        parts.append(
            {
                "name": name.group(1) if name else "",
                "file": fname,
                "index": index,
            }
        )
    return parts


def preloader_from_scatter(scatter_text: str) -> str:
    for part in parse_scatter_downloads(scatter_text):
        if part["name"].upper() == "PRELOADER":
            return part["file"]
    return ""


def is_signed_image_name(name: str) -> bool:
    return bool(_SIGNED_NAME.search(Path(name).name))


def is_dynamic_super_name(name: str) -> bool:
    stem = Path(name).name.lower()
    return stem.startswith("super.") or stem.startswith("super-") or stem.startswith("super_")


def top_level_scatters(directory) -> list:
    """Scatter files sitting at the payload root. Nested copies are ignored."""
    root = Path(directory)
    if not root.is_dir():
        return []
    return sorted(path for path in root.glob("*scatter*.txt") if path.is_file())


def find_scatter_file(directory, chip: str) -> Optional[Path]:
    """Scatter at the payload root whose platform line is ``chip``.

    The filename is not the chip. Q3 and Q5 ship ``MT6580_Android_scatter.txt``
    while the platform line inside it is MT6582. A nested scatter is ignored.
    Stock releases are flat; a top-level folder would make SP Flash Tool load
    the wrong relative paths.
    """
    chip = (chip or "").upper()
    matched = []
    for path in top_level_scatters(directory):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if parse_scatter_platform(text) == chip:
            matched.append(path)
    if len(matched) == 1:
        return matched[0]
    return None


def _zip_basename(name) -> str:
    if not name:
        return ""
    try:
        from urllib.parse import urlparse
        raw = urlparse(str(name)).path.rsplit("/", 1)[-1]
    except Exception:
        raw = str(name).replace("\\", "/").rsplit("/", 1)[-1]
    return raw.strip()


def assess_named_package(selected_model, zip_name=None, asset_url=None) -> FlashAssessment:
    """Decide from names only, before anything is extracted."""
    selected = canonical_model(selected_model)
    zip_model = model_from_zip_name(zip_name) or model_from_zip_name(asset_url)
    if zip_model and selected and zip_model != selected:
        return FlashAssessment(
            action="refuse",
            model=zip_model,
            chip=profile_for(zip_model).chip if profile_for(zip_model) else "",
            message=(
                f"Refusing to flash. The package is {zip_model} firmware "
                f"({_zip_basename(zip_name) or _zip_basename(asset_url)}), "
                f"but {selected} is selected. No data was sent to a device."
            ),
            errors=["model_mismatch"],
        )
    effective = zip_model or selected
    profile = profile_for(effective)
    if profile is None:
        if not effective:
            return FlashAssessment(
                action="builtin",
                model="",
                message="",
            )
        return FlashAssessment(
            action="refuse",
            model=str(effective),
            message=(
                f"Refusing to flash. {effective} is not a model this updater "
                "knows how to write. No data was sent to a device."
            ),
            errors=["unknown_model"],
        )
    if profile.flash == "download_only":
        return _download_only(profile)
    if profile.flash in ("builtin_y1", "builtin_y2"):
        return FlashAssessment(
            action="builtin",
            model=profile.id,
            chip=profile.chip,
            message="",
        )
    return FlashAssessment(
        action="generic",
        model=profile.id,
        chip=profile.chip,
        message="",
    )


def assess_payload_dir(model, directory, zip_name=None, selected_model=None) -> FlashAssessment:
    """Full check of an extracted package. Refuses rather than guessing."""
    named = assess_named_package(selected_model or model, zip_name=zip_name)
    if named.action in ("refuse", "download_only"):
        return named
    profile = profile_for(named.model or model)
    if profile is None or profile.flash != "generic_scatter":
        return named

    root = Path(directory)
    names = [p.name for p in root.iterdir() if p.is_file()] if root.is_dir() else []
    signed = [name for name in names if is_signed_image_name(name)]
    supers = [name for name in names if is_dynamic_super_name(name)]
    if signed or supers:
        reason = []
        if signed:
            reason.append("signed images (" + ", ".join(signed[:4]) + ")")
        if supers:
            reason.append("a dynamic super image (" + ", ".join(supers[:3]) + ")")
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=profile.chip,
            message=(
                f"{profile.product} firmware was saved, but automatic flashing "
                f"was refused because the package contains {' and '.join(reason)}. "
                "Those images are not written with the legacy scatter path. "
                "No data was sent to a device."
            ),
            errors=["signed_or_super"],
        )

    scatters = top_level_scatters(root)
    scatter = find_scatter_file(root, profile.chip)
    if scatter is None and scatters:
        described = []
        for path in scatters:
            try:
                seen = parse_scatter_platform(path.read_text(encoding="utf-8", errors="ignore"))
            except OSError:
                seen = ""
            described.append(f"{path.name} ({seen or 'unknown platform'})")
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=profile.chip,
            message=(
                f"Refusing to flash. {profile.product} must be {profile.chip}. "
                f"The package scatter does not say that: {', '.join(described)}. "
                "The filename is not used as the chip. "
                "No data was sent to a device."
            ),
            errors=["chip_mismatch"],
        )
    if scatter is None:
        nested = list(root.glob("*/*scatter*.txt")) if root.is_dir() else []
        extra = ""
        if nested:
            extra = " The archive still has a top-level folder; repack it so the scatter sits at the zip root."
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=profile.chip,
            message=(
                f"Refusing to flash {profile.product}. Expected a flat scatter "
                f"whose platform line is {profile.chip}.{extra} "
                "No data was sent to a device."
            ),
            errors=["scatter_missing"],
        )
    text = scatter.read_text(encoding="utf-8", errors="ignore")
    chip = parse_scatter_platform(text)
    if chip != profile.chip or chip not in GENERIC_SCATTER_CHIPS:
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=chip,
            message=(
                f"Refusing to flash. {profile.product} must be {profile.chip}, "
                f"but {scatter.name} says {chip or 'an unknown chip'}. "
                "No data was sent to a device."
            ),
            errors=["chip_mismatch"],
        )
    project = parse_scatter_project(text).upper()
    if profile.id == "Q5" and project in {"Q3", "Q3E"}:
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=chip,
            message=(
                "Refusing to flash. This package identifies itself as "
                f"{project}, which is Q3 firmware, but Q5 is selected. "
                "No data was sent to a device."
            ),
            errors=["model_mismatch"],
        )
    if profile.id == "Q3" and project == "Q5":
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=chip,
            message=(
                "Refusing to flash. This package identifies itself as Q5, "
                "but Q3 is selected. No data was sent to a device."
            ),
            errors=["model_mismatch"],
        )
    preloader = preloader_from_scatter(text)
    if not preloader or not (root / preloader).is_file():
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=chip,
            message=(
                f"Refusing to flash {profile.product}. The scatter names "
                f"preloader {preloader or '(none)'}, and that file is not in "
                "the package. Another model's preloader will not be substituted. "
                "No data was sent to a device."
            ),
            errors=["preloader_missing"],
        )
    missing = []
    for part in parse_scatter_downloads(text):
        if part["file"] and not (root / part["file"]).is_file():
            missing.append(part["file"])
    if missing:
        return FlashAssessment(
            action="refuse",
            model=profile.id,
            chip=chip,
            preloader=preloader,
            scatter_name=scatter.name,
            message=(
                f"Refusing to flash {profile.product}. The scatter lists images "
                f"that are not in the package: {', '.join(missing[:8])}. "
                "No data was sent to a device."
            ),
            errors=["images_missing"],
        )
    return FlashAssessment(
        action="generic",
        model=profile.id,
        chip=chip,
        preloader=preloader,
        scatter_name=scatter.name,
        message=generic_confirm_text(profile, project=parse_scatter_project(text)),
    )


def _download_only(profile: ModelProfile) -> FlashAssessment:
    return FlashAssessment(
        action="download_only",
        model=profile.id,
        chip=profile.chip,
        message=(
            f"{profile.product} firmware can be downloaded, but automatic "
            f"flashing is not supported yet.\n\n{profile.reason}\n\n"
            "The zip is kept for you. It was not extracted into the Y1/Y2 "
            "install folder, and Install / Restore will not write it to a "
            "player or recorder."
        ),
    )


def generic_confirm_text(profile: ModelProfile, project: str = "") -> str:
    detail = ""
    if profile.id in ("Q3", "Q5"):
        detail = (
            "\n\nThe scatter file may be named MT6580_Android_scatter.txt. "
            "Flashing follows the platform line inside it (MT6582) and the "
            "preloader that scatter names. That is the same chip family as "
            "the Y2. It is not the Y2 partition layout, and the Y2 preloader "
            "is not substituted."
        )
        if profile.id == "Q3":
            detail += " Q3 firmware identifies itself as Q3E."
            if project.upper() == "Q3E":
                detail += " This package's project name is Q3E."
    return (
        f"This will write {profile.product} firmware ({profile.chip}) using "
        f"the scatter file and preloader inside this package.\n\n"
        f"Connect only a {profile.product}. A different player on the same "
        "USB port can be bricked, because the tool cannot yet prove which "
        f"model answered on the wire.\n\n"
        "This is a full format-and-download, and it has not been tested on "
        f"every {profile.id} board. Continue only if this device is a "
        f"{profile.product}."
        f"{detail}"
    )


def write_generic_spflash_xml(directory, model, log_path: str = "") -> Optional[Path]:
    """Write a scatter-driven SP Flash Tool config next to the payload.

    Rom filenames are basenames. The tool must be started with this directory
    as its working directory so those names cannot resolve to a Y1/Y2 file.
    """
    root = Path(directory)
    assessment = assess_payload_dir(model, root)
    if assessment.action != "generic":
        return None
    parts = parse_scatter_downloads(
        (root / assessment.scatter_name).read_text(encoding="utf-8", errors="ignore")
    )
    rom_lines = []
    for part in parts:
        if part["index"] < 0:
            continue
        rom_lines.append(
            f'            <rom index="{part["index"]}" enable="true">{part["file"]}</rom>'
        )
    rom_xml = "\n".join(rom_lines) if rom_lines else ""
    log = log_path or str(root / "SP_FT_Logs")
    xml = f"""<?xml version="1.0" encoding="utf-8"?>
<flashtool-config version="2.0">
    <general>
        <chip-name>{assessment.chip}</chip-name>
        <storage-type>EMMC</storage-type>
        <download-agent>{DA_FILENAME}</download-agent>
        <scatter>{assessment.scatter_name}</scatter>
        <authentication></authentication>
        <certification></certification>
        <rom-list>
{rom_xml}
        </rom-list>
        <connection type="BromUSB" high-speed="true" power="AutoDetect" da_log_level="Info" da_log_channel="UART" timeout-count="3600000" com-port="" />
        <checksum-level>none</checksum-level>
        <log-info log_on="true" log_path="{log}" clean_hours="720" />
    </general>
    <commands>
        <format-download>
            <combo-format>
                <format validation="false" physical="true" erase-flag="NormalErase" auto-format="true" auto-format-flag="FormatAll" />
            </combo-format>
            <da-download-all />
        </format-download>
    </commands>
</flashtool-config>
"""
    path = root / GENERIC_SPFLASH_XML
    path.write_text(xml, encoding="utf-8")
    return path


def validate_generic_payload(model, directory) -> tuple:
    """SP Flash Tool preflight tuple: (ok, errors, warnings)."""
    assessment = assess_payload_dir(model, directory)
    if assessment.action == "generic" and assessment.scatter_name:
        return True, [], [
            f"{assessment.model} generic scatter flash is untested on hardware "
            f"({assessment.chip}, preloader {assessment.preloader})."
        ]
    return False, [assessment.message or "Generic payload is not flashable."], []


def device_label(model) -> str:
    profile = profile_for(model)
    if profile:
        return profile.id
    text = str(model or "").strip()
    return text or "Y1"


def product_name(model) -> str:
    profile = profile_for(model)
    if profile:
        return profile.product
    label = device_label(model)
    if label in ("Y1", "Y2", "A5"):
        return f"Innioasis {label}"
    return label


def power_button(model) -> str:
    profile = profile_for(model)
    if profile:
        return profile.power_button
    return "centre button"


def stock_readme(model, org="y1-community") -> str:
    profile = profile_for(model)
    if profile is None:
        raise ValueError(f"Unknown model {model!r}")
    repo = f"{org}/{profile.repo_name}"
    if profile.flash == "download_only":
        install = (
            f"Innioasis Updater can download these releases when {profile.id} "
            "is selected. Automatic flashing is not supported yet: "
            f"{profile.reason}"
        )
    elif profile.flash == "generic_scatter":
        install = (
            f"Innioasis Updater can install a release when {profile.id} is "
            f"selected. It drives SP Flash Tool or mtkclient from the "
            f"{profile.chip} scatter and preloader inside `rom_{profile.id.lower()}.zip`. "
            "That path checks the zip name and the scatter chip before writing, "
            "and it has not been verified on every board revision."
        )
    else:
        install = (
            "Install it from https://innioasis.app with Innioasis Updater. "
            f"Select {profile.id}, then Original Software."
        )
    kind = "voice recorder" if profile.kind == "recorder" else "player"
    return f"""# {profile.product} stock firmware

Mirror of official stock system software for the {profile.product} {kind} ({profile.chip}).

Each GitHub release is one build:

- `rom_{profile.id.lower()}.zip` — firmware images at the zip root, maximum deflate, no `__MACOSX` or `.DS_Store`
- `updater.jpg` — release image shown by Innioasis Updater

Tags look like `3.27-en`, `5.01-en-wm`, or `1.48` (version, then a lowercase variant suffix when the build is regional). Each variant is its own release. Updater lists them all; GitHub's "latest" is only the newest English build. The release title looks like `System Software <version> for {profile.product}`.

{install}

Source repository for the updater and the manifest: https://github.com/y1-community/Innioasis-Updater

This repository: https://github.com/{repo}

These files are redistributed so a {kind} can be restored. The firmware itself remains the manufacturer's.
"""
