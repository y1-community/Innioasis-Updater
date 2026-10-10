#!/usr/bin/env python3
"""Onboard one stock firmware release for an Innioasis or Timmkoo model.

Maintainer script, not a GitHub Action: the inputs are multi-gigabyte
archives, the org repo create needs a maintainer's ``gh`` login, and a
workflow dispatch would be easy to fire against real repos by mistake.
It lives under ``scripts/`` because the repository already has mtkclient's
``Tools/`` directory, and ``tools/`` would collide with that name on macOS.
Dry-run is the default. ``--apply`` is what talks to GitHub.

Given a model, tag, title, notes, and a source zip/rar or URL, this:

1. Repacks to the y1-stock-rom layout (files at the zip root, ``__MACOSX``
   and ``.DS_Store`` removed, ``zip -9 -X``).
2. Refuses a zip that is not strictly under GitHub's 2 GiB asset limit.
3. Creates ``<org>/<model>-stock-rom`` when it is missing, with a short README.
4. Creates the release if needed and uploads ``rom_<model>.zip`` and
   ``updater.jpg``.
5. Inserts or updates the Original Software line in ``slidia_manifest.xml``.

Running it twice with the same tag and the same asset size is a no-op.
This file does not call GitHub unless ``--apply`` is passed.
"""

from __future__ import annotations

import argparse
import base64
import json
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import firmware_models as fm


JUNK_NAMES = {"__macosx", ".ds_store", "thumbs.db", "desktop.ini"}


class OnboardError(Exception):
    pass


class Gh:
    """Thin ``gh`` wrapper. Tests pass a fake with the same ``run`` method."""

    def __init__(self, binary="gh"):
        self.binary = binary

    def run(self, args, check=True, input_text=None):
        proc = subprocess.run(
            [self.binary, *args],
            input=input_text,
            text=True,
            capture_output=True,
        )
        if check and proc.returncode != 0:
            raise OnboardError(
                f"gh {' '.join(args)} failed ({proc.returncode}): "
                f"{proc.stderr.strip() or proc.stdout.strip()}"
            )
        return proc


def _is_junk(path: Path) -> bool:
    parts = [part.lower() for part in path.parts]
    if any(part in JUNK_NAMES or part.startswith("._") for part in parts):
        return True
    return path.name.lower() in JUNK_NAMES or path.name.startswith("._")


def _extract_archive(source: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    suffix = source.suffix.lower()
    if suffix == ".zip":
        with zipfile.ZipFile(source) as archive:
            for info in archive.infolist():
                name = info.filename.replace("\\", "/")
                if name.endswith("/") or _is_junk(Path(name)):
                    continue
                target = dest / name
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as src, open(target, "wb") as out:
                    shutil.copyfileobj(src, out)
        return
    if suffix == ".rar":
        tool = shutil.which("7z") or shutil.which("7zz") or shutil.which("unrar") or shutil.which("bsdtar")
        if not tool:
            raise OnboardError(
                "RAR sources need 7z, unrar, or bsdtar installed. None was found."
            )
        base = Path(tool).name
        if base in ("7z", "7zz"):
            cmd = [tool, "x", "-y", f"-o{dest}", str(source)]
        elif base == "unrar":
            cmd = [tool, "x", "-o+", str(source), str(dest)]
        else:
            cmd = [tool, "-xf", str(source), "-C", str(dest)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise OnboardError(proc.stderr.strip() or f"{base} failed to extract {source.name}")
        return
    raise OnboardError(f"Unsupported source type {source.suffix!r}. Use a .zip or .rar.")


def _flatten(directory: Path) -> None:
    """Lift a single top-level folder so images sit at the root."""
    for path in list(directory.rglob("*")):
        if path.is_file() and _is_junk(path.relative_to(directory)):
            path.unlink()
    for path in sorted([p for p in directory.rglob("*") if p.is_dir()], reverse=True):
        if path.name.lower() == "__macosx":
            shutil.rmtree(path, ignore_errors=True)

    entries = [p for p in directory.iterdir() if p.name not in (".", "..")]
    if len(entries) == 1 and entries[0].is_dir():
        inner = entries[0]
        for child in inner.iterdir():
            target = directory / child.name
            if target.exists():
                raise OnboardError(f"Cannot flatten {inner.name}: {target.name} already exists")
            child.rename(target)
        inner.rmdir()


def repack_firmware(source: Path, dest_zip: Path, work_root: Path = None) -> Path:
    """Flatten ``source`` and write a ``zip -9 -X`` archive at ``dest_zip``."""
    source = Path(source)
    dest_zip = Path(dest_zip)
    if not source.is_file():
        raise OnboardError(f"Source not found: {source}")
    own_tmp = work_root is None
    work_root = Path(work_root or tempfile.mkdtemp(prefix="onboard-fw-"))
    stage = work_root / "stage"
    if stage.exists():
        shutil.rmtree(stage)
    try:
        _extract_archive(source, stage)
        _flatten(stage)
        files = [p for p in stage.rglob("*") if p.is_file()]
        if not files:
            raise OnboardError(f"{source.name} contained no firmware files after cleanup")
        dest_zip.parent.mkdir(parents=True, exist_ok=True)
        if dest_zip.exists():
            dest_zip.unlink()
        zip_bin = shutil.which("zip")
        if not zip_bin:
            raise OnboardError("The Info-ZIP `zip` command is required (`zip -9 -X`).")
        proc = subprocess.run(
            [zip_bin, "-9", "-X", "-r", str(dest_zip.resolve()), "."],
            cwd=str(stage),
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise OnboardError(proc.stderr.strip() or "zip failed")
        assert_under_github_limit(dest_zip)
        return dest_zip
    finally:
        if own_tmp:
            shutil.rmtree(work_root, ignore_errors=True)


def assert_under_github_limit(path: Path) -> int:
    size = Path(path).stat().st_size
    if size >= fm.GITHUB_MAX_ASSET_BYTES:
        raise OnboardError(
            f"{path.name} is {size} bytes, which is not under GitHub's "
            f"2 GiB release-asset limit ({fm.GITHUB_MAX_ASSET_BYTES} bytes). "
            "The release was not created."
        )
    return size


def fetch_source(url: str, dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, dest)
    return dest


def upsert_manifest(manifest_path: Path, model: str, org: str = "y1-community") -> str:
    """Insert or refresh one Original Software line. Returns added|updated|unchanged."""
    path = Path(manifest_path)
    text = path.read_text(encoding="utf-8")
    line = fm.manifest_package_line(model, org=org)
    device = fm.profile_for(model).id
    parsed = ET.fromstring(text)
    existing = None
    for node in parsed.findall("package"):
        if node.get("device_type") is not None:
            continue
        if (node.get("device") or "").strip().upper() != device:
            continue
        if (node.get("name") or "").strip() == "Original Software":
            existing = node
            break
    if existing is not None:
        current = (
            f'<package name="{existing.get("name")}" repo="{existing.get("repo")}" '
            f'device="{existing.get("device")}" url="{existing.get("url")}" '
            f'type="{existing.get("type")}" handler="{existing.get("handler")}" />'
        )
        if current == line:
            return "unchanged"
        # Replace the single matching line, leaving every other entry alone.
        replaced = False
        new_lines = []
        for raw in text.splitlines(keepends=True):
            if (not replaced) and f'device="{device}"' in raw and 'name="Original Software"' in raw:
                indent = raw[: len(raw) - len(raw.lstrip())]
                newline = "\n" if raw.endswith("\n") else ""
                new_lines.append(f"{indent}{line}{newline}")
                replaced = True
            else:
                new_lines.append(raw)
        if not replaced:
            raise OnboardError(f"Found a {device} Original Software entry but could not replace its line")
        path.write_text("".join(new_lines), encoding="utf-8")
        return "updated"
    if "</slidia>" not in text:
        raise OnboardError("Manifest has no </slidia> closing tag")
    indent = "  "
    addition = f"{indent}{line}\n"
    path.write_text(text.replace("</slidia>", addition + "</slidia>", 1), encoding="utf-8")
    return "added"


def _repo(model, org) -> str:
    return f"{org}/{fm.profile_for(model).repo_name}"


def ensure_repo(gh: Gh, model: str, org: str, apply: bool) -> str:
    repo = _repo(model, org)
    profile = fm.profile_for(model)
    view = gh.run(["repo", "view", repo, "--json", "name"], check=False)
    if view.returncode == 0:
        return "exists"
    if not apply:
        return "would-create"
    gh.run(
        [
            "repo", "create", repo,
            "--public",
            "--description",
            f"Stock firmware mirror for the {profile.product} ({profile.chip})",
        ]
    )
    return "created"


def ensure_readme(gh: Gh, model: str, org: str, apply: bool) -> str:
    repo = _repo(model, org)
    body = fm.stock_readme(model, org=org)
    owner, name = repo.split("/", 1)
    api_path = f"repos/{owner}/{name}/contents/README.md"
    current = gh.run(["api", api_path], check=False)
    sha = ""
    existing = ""
    if current.returncode == 0 and current.stdout.strip():
        try:
            data = json.loads(current.stdout)
        except json.JSONDecodeError as exc:
            raise OnboardError(f"Could not parse README metadata: {exc}") from exc
        sha = data.get("sha") or ""
        encoded = data.get("content") or ""
        if encoded:
            existing = base64.b64decode(encoded).decode("utf-8")
    if existing == body:
        return "unchanged"
    if not apply:
        return "would-write" if not existing else "would-update"
    payload = {
        "message": f"Add stock firmware README for {fm.profile_for(model).product}",
        "content": base64.b64encode(body.encode("utf-8")).decode("ascii"),
    }
    if sha and existing:
        payload["sha"] = sha
        payload["message"] = f"Update stock firmware README for {fm.profile_for(model).product}"
    gh.run(
        ["api", "--method", "PUT", api_path, "--input", "-"],
        input_text=json.dumps(payload),
    )
    return "written" if not existing else "updated"


def ensure_release(gh: Gh, model, org, tag, title, notes, rom_zip: Path, image: Path, apply: bool) -> str:
    repo = _repo(model, org)
    asset = fm.profile_for(model).asset_name
    view = gh.run(
        ["release", "view", tag, "--repo", repo, "--json", "assets"],
        check=False,
    )
    assets = {}
    if view.returncode == 0:
        try:
            data = json.loads(view.stdout or "{}")
            for item in data.get("assets") or []:
                assets[item.get("name")] = int(item.get("size") or 0)
        except json.JSONDecodeError as exc:
            raise OnboardError(f"Could not parse existing release JSON: {exc}") from exc
        else:
            rom_size = rom_zip.stat().st_size
            image_size = image.stat().st_size
            if assets.get(asset) == rom_size and assets.get(image.name) == image_size:
                return "unchanged"
    if not apply:
        return "would-create" if view.returncode != 0 else "would-upload"
    if view.returncode != 0:
        gh.run(
            [
                "release", "create", tag,
                "--repo", repo,
                "--title", title,
                "--notes", notes or "",
                "--target", "main",
            ]
        )
    gh.run(
        [
            "release", "upload", tag,
            str(rom_zip), str(image),
            "--repo", repo,
            "--clobber",
        ]
    )
    return "uploaded"


def build_plan(model, tag, title, notes, source, image, manifest, org, output) -> dict:
    profile = fm.profile_for(model)
    if profile is None:
        raise OnboardError(
            f"Unknown model {model!r}. Known: {', '.join(fm.STOCK_MANIFEST_MODELS)}"
        )
    if profile.id not in fm.STOCK_MANIFEST_MODELS and profile.flash == "builtin_y1":
        raise OnboardError(f"{profile.id} already has its own stock archive layout")
    return {
        "model": profile.id,
        "repo": _repo(profile.id, org),
        "tag": tag,
        "title": title,
        "notes": notes,
        "asset": profile.asset_name,
        "source": str(source) if source else "",
        "image": str(image) if image else "",
        "manifest": str(manifest),
        "output": str(output),
        "line": fm.manifest_package_line(profile.id, org=org),
        "flash": profile.flash,
        "chip": profile.chip,
    }


def run(argv=None, gh: Gh = None) -> dict:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Q3, Q5, G1, G3, G5, R1, or SR1")
    parser.add_argument("--tag", required=True, help="Release tag, e.g. 3.27-en")
    parser.add_argument("--title", required=True, help="Release title")
    parser.add_argument("--notes", default="", help="Release notes")
    parser.add_argument("--notes-file", type=Path, help="Read notes from a file")
    parser.add_argument("--source", help="Local .zip/.rar or an http(s) URL")
    parser.add_argument("--image", type=Path, help="updater.jpg to attach")
    parser.add_argument("--org", default="y1-community")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "slidia_manifest.xml",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Where to write rom_<model>.zip (default: a temp file)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Create the repo, release, and manifest line. Default is dry-run.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Accepted for clarity; this is the default")
    args = parser.parse_args(argv)
    if args.apply and args.dry_run:
        raise OnboardError("Pass only one of --apply and --dry-run")
    apply = bool(args.apply)
    notes = args.notes
    if args.notes_file:
        notes = args.notes_file.read_text(encoding="utf-8")
    profile = fm.profile_for(args.model)
    if profile is None or profile.id not in fm.STOCK_MANIFEST_MODELS:
        raise OnboardError(
            f"--model must be one of: {', '.join(fm.STOCK_MANIFEST_MODELS)}"
        )
    output = args.output or Path(tempfile.mkdtemp(prefix="onboard-out-")) / profile.asset_name
    plan = build_plan(
        profile.id, args.tag, args.title, notes,
        args.source, args.image, args.manifest, args.org, output,
    )
    report = {"plan": plan, "apply": apply, "steps": []}

    if not args.source:
        raise OnboardError("--source is required (a local zip/rar or a URL)")
    source_path = Path(args.source)
    if args.source.startswith("http://") or args.source.startswith("https://"):
        suffix = Path(urlparse(args.source).path).suffix or ".zip"
        source_path = output.parent / f"source{suffix}"
        report["steps"].append("fetch-source")
        fetch_source(args.source, source_path)
    elif not source_path.is_file():
        raise OnboardError(f"--source is not a file: {source_path}")

    report["steps"].append("repack")
    repack_firmware(source_path, output)
    report["zip_bytes"] = output.stat().st_size
    report["zip"] = str(output)

    if not args.image or not args.image.is_file():
        if apply:
            raise OnboardError("--image must point at updater.jpg when using --apply")
        report["steps"].append("image-missing")
    else:
        report["image_bytes"] = args.image.stat().st_size

    if not apply:
        # Dry-run repacks locally and stops. It does not call gh or edit the manifest.
        report["steps"].append("dry-run")
        report["manifest"] = "not-written"
        report["release"] = "not-uploaded"
        report["repo"] = "not-contacted"
        return report

    client = gh or Gh()

    report["steps"].append(ensure_repo(client, profile.id, args.org, apply=True))
    report["steps"].append("readme:" + ensure_readme(client, profile.id, args.org, apply=True))
    report["steps"].append(
        "release:" + ensure_release(
            client, profile.id, args.org, args.tag, args.title, notes,
            output, args.image, apply=True,
        )
    )
    report["steps"].append(
        "manifest:" + upsert_manifest(args.manifest, profile.id, org=args.org)
    )
    return report


def main(argv=None) -> int:
    try:
        report = run(argv)
    except OnboardError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
