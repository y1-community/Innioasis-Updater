#!/usr/bin/env python3
"""Check that a Y1 (MT6572) package is never selected for, or flashed onto, a Y2.

Regression check for a Y2 user who picked Device Model "Y2" and Software
"inniclassic" (JonaszPotoniec/inniclassic-y2). That release ships rom.zip and
rom_y1_type_a.zip (Y1, MT6572) next to rom_y2.zip (Y2, MT6582). The repo name
made every asset look like Y2, "rom.zip" sorted first, and the MTKClient
install then wrote the MT6572 images at MT6582 scatter offsets.

Run with the app's Python environment (PySide6 must be importable):
    python3 check_platform_mismatch_guard.py
"""
from __future__ import annotations

import os
import shutil
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import firmware_downloader as fd  # noqa: E402

# Asset names of JonaszPotoniec/inniclassic-y2 release 20261017.
INNICLASSIC_Y2_ASSETS = [
    "index.html",
    "InniClassic-20261017.apk",
    "rom.zip",
    "rom_type_b.zip",
    "rom_y1_type_a.zip",
    "rom_y1_type_b.zip",
    "rom_y2.zip",
    "SHA256SUMS.txt",
    "update.json",
]


def pick(asset_names, repo, tag, model, hw_type, package_device):
    assets = [{"name": n, "browser_download_url": f"https://x/{n}"} for n in asset_names]
    variants = fd.extract_rom_variants_from_assets(assets, tag, repo)
    variant = fd.select_rom_asset_for_model_and_resolution(
        variants, model, hw_type, "native",
        package_device=package_device, repo=repo, tag_name=tag,
    )
    return variant["asset"]["name"] if variant else None


def check_asset_selection(problems: list[str]) -> None:
    cases = [
        # (assets, repo, tag, selected model, type, manifest device, expected)
        (INNICLASSIC_Y2_ASSETS, "JonaszPotoniec/inniclassic-y2", "20261017", "Y2", "A", "Y2", "rom_y2.zip"),
        (INNICLASSIC_Y2_ASSETS, "JonaszPotoniec/inniclassic-y2", "20261017", "Y2", "B", "Y2", "rom_y2.zip"),
        (["rom.zip", "rom_type_b.zip", "rom_y2.zip"], "ismileblue/y1_launcher", "launcher-v0.11.6hotfix4", "Y2", "A", "Y2", "rom_y2.zip"),
        (["rom.zip", "rom_type_b.zip", "rom_y2.zip"], "ismileblue/y1_launcher", "launcher-v0.11.6hotfix4", "Y1", "A", "Y1", "rom.zip"),
        (["rom.zip", "rom_type_b.zip", "update.zip"], "rockbox-y1/rockbox", "nightly-11d9072", "Y1", "A", "Y1", "rom.zip"),
        (["rom.zip", "rom_type_b.zip", "update.zip"], "rockbox-y1/rockbox", "nightly-11d9072", "Y1", "B", "Y1", "rom_type_b.zip"),
        (["rom.zip"], "FabianZettl/inniclassic", "v1.4.5", "Y1", "A", "Y1", "rom.zip"),
        (["rom_y2.zip"], "schulzcode/Y2Player", "Release2.5", "Y2", "A", "Y2", "rom_y2.zip"),
        # A Y2 selection must never fall back to a Y1-named asset.
        (["rom.zip", "rom_type_b.zip"], "JonaszPotoniec/inniclassic-y2", "20261017", "Y2", "A", "Y2", None),
    ]
    for assets, repo, tag, model, hw_type, package_device, expected in cases:
        got = pick(assets, repo, tag, model, hw_type, package_device)
        if got != expected:
            problems.append(
                f"{repo} {tag} (Device Model {model}, Type {hw_type}): "
                f"picked {got!r}, expected {expected!r}"
            )


def make_package(root: Path, chip: str) -> list[str]:
    """Write a package extract list with the shipped scatter for this chip."""
    if chip == "MT6572":
        name = "MT6572_Android_scatter.txt"
        shutil.copy(ROOT / "MT6572_Android_scatter.txt", root / name)
        return [name, "preloader_g368_nyx.bin", "lk.bin", "boot.img", "system.img"]
    name = "MT6582_Android_scatter.txt"
    shutil.copy(ROOT / "MT6582_Android_scatter_def.txt", root / name)
    return [name, "preloader_eastaeon82_wet_kk.bin", "lk.bin", "boot.img", "system.img"]


def expect_refused(problems, label, func):
    try:
        func()
    except fd.FirmwarePlatformMismatchError:
        return
    problems.append(f"{label}: not refused")


def expect_allowed(problems, label, func):
    try:
        func()
    except fd.FirmwarePlatformMismatchError as e:
        problems.append(f"{label}: refused ({e})")


def check_guard(problems: list[str]) -> None:
    check = fd.check_package_matches_device
    with tempfile.TemporaryDirectory() as tmp:
        y1_dir = Path(tmp) / "y1"
        y2_dir = Path(tmp) / "y2"
        y1_dir.mkdir()
        y2_dir.mkdir()
        y1_files = make_package(y1_dir, "MT6572")
        y2_files = make_package(y2_dir, "MT6582")
        # Stale MT6582 scatter left by an earlier install must not count.
        shutil.copy(ROOT / "MT6582_Android_scatter_def.txt", y1_dir / "MT6582_Android_scatter.txt")

        try:
            fd.set_install_target_device_model(None)
            if fd.package_scatter_family(y1_files, y1_dir) != "Y1":
                problems.append("MT6572 package not detected as Y1")
            if fd.package_scatter_family(y2_files, y2_dir) != "Y2":
                problems.append("MT6582 package not detected as Y2")

            expect_refused(problems, "Y1 package, Y2 install plan",
                           lambda: check("Y2", y1_files, y1_dir))
            expect_refused(problems, "Y2 package, Y1 install plan",
                           lambda: check("Y1", y2_files, y2_dir))
            expect_allowed(problems, "Y1 package, Y1 install plan",
                           lambda: check("Y1", y1_files, y1_dir))
            expect_allowed(problems, "Y2 package, Y2 install plan",
                           lambda: check("Y2", y2_files, y2_dir))
            expect_allowed(problems, "unknown package",
                           lambda: check("Y2", ["system.img"], y1_dir))

            # The reported case: Device Model Y2, package resolved as Y1 everywhere.
            fd.set_install_target_device_model("Y2")
            expect_refused(problems, "Device Model Y2, Y1 package and Y1 plan",
                           lambda: check("Y1", y1_files, y1_dir))
            expect_refused(problems, "MTKClient plan, Device Model Y2, Y1 package",
                           lambda: fd.build_mtk_named_staged_commands(
                               install_dir=y1_dir, device_model="Y1",
                               extracted_files=y1_files))
            ok, errors, _ = fd.validate_spflash_images_for_model(
                "Y1", app_dir=y1_dir, extracted_files=y1_files)
            if ok or not any("does not match device" in e for e in errors):
                problems.append(f"SP Flash Tool preflight did not refuse: {errors}")
            expect_allowed(problems, "Device Model Y2, Y2 package",
                           lambda: check("Y2", y2_files, y2_dir))
        finally:
            fd.set_install_target_device_model(None)


def main() -> None:
    problems: list[str] = []
    check_asset_selection(problems)
    check_guard(problems)
    if problems:
        print("Platform mismatch guard problems:")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)
    print("OK: Y2 selections get rom_y2.zip, and Y1/Y2 package mismatches are refused.")


if __name__ == "__main__":
    main()
