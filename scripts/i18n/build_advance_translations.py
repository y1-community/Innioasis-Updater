#!/usr/bin/env python3
"""Advance translation build and prerender pipeline.

Ensures that our entire website is genuinely already i18n translated in advance
for all pages, with static fallback pages for each language.

Pipeline steps:
1. (Optional) Batch-translate missing strings for target locales using Clients5.
2. Propagate base translations to regional variants (e.g. fr -> fr-CA, es -> es-MX).
3. Enforce brand preservation and proper noun masking via repair_brands.py.
4. Pre-translate and localise 'Updater' and its variations while preserving 'Innioasis'.
5. Rebuild site-locales.json index for the language picker.
6. Pre-render static fallback pages for crawlers, fallbacks and static hosting into dist/.
7. Sync catalogs and assets to InnioasisY1Themes.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.parent
THEMES_ROOT = ROOT.parent / "InnioasisY1Themes"


def run_step(desc: str, cmd: list[str]) -> bool:
    print(f"\n=== {desc} ===")
    print(f"Command: {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=str(ROOT))
    if res.returncode != 0:
        print(f"ERROR: Step failed with code {res.returncode}")
        return False
    return True


def sync_to_themes():
    print("\n=== Syncing updated catalogs and site-locale files to InnioasisY1Themes ===")
    if not THEMES_ROOT.exists():
        print(f"Themes repo not found at {THEMES_ROOT}, skipping sync.")
        return

    # Sync catalogs
    src_cats = ROOT / "i18n/catalogs"
    dst_cats = THEMES_ROOT / "i18n/catalogs"
    dst_cats.mkdir(parents=True, exist_ok=True)
    count = 0
    for p in src_cats.glob("*.json"):
        target = dst_cats / p.name
        target.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
        count += 1
    print(f"Synced {count} catalogs to InnioasisY1Themes.")

    # Sync site-locale files
    for fname in ["site-locale.js", "site-locale.css", "support_toolbar.html", "i18n/site-locales.json", "i18n/config.json"]:
        src_f = ROOT / fname
        dst_f = THEMES_ROOT / fname
        if src_f.exists():
            dst_f.parent.mkdir(parents=True, exist_ok=True)
            dst_f.write_text(src_f.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"Synced {fname} to InnioasisY1Themes.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locales", default="core", help="'core', 'all', or specific comma-separated locales")
    parser.add_argument("--skip-translate", action="store_true", help="Skip remote network translation pass")
    parser.add_argument("--skip-prerender", action="store_true", help="Skip static page pre-rendering pass")
    args = parser.parse_args()

    # Step 1: Remote translation of missing strings (if requested)
    if not args.skip_translate:
        cmd = [sys.executable, str(HERE / "translate.py"), "--provider", "clients5", "--locales", args.locales]
        if not run_step("Translate missing strings for core locales", cmd):
            print("Translation step encountered errors, continuing with existing catalog strings...")

    # Step 2: Propagate base language translations to regional variants
    cmd = [sys.executable, str(HERE / "propagate_variants.py")]
    if not run_step("Propagate base language strings to variants", cmd):
        return 1

    # Step 3: Repair brands and preserve proper nouns
    cmd = [sys.executable, str(HERE / "repair_brands.py"), "--write"]
    if not run_step("Repair brands and proper nouns", cmd):
        return 1

    # Step 4: Pre-translate Updater names and variations
    cmd = [sys.executable, str(HERE / "pretranslate_updater_names.py")]
    if not run_step("Pre-translate Updater names and localise", cmd):
        return 1

    # Step 5: Rebuild picker index
    cmd = [sys.executable, str(HERE / "translate.py"), "--index-only"]
    if not run_step("Rebuild language picker index", cmd):
        return 1

    # Step 6: Sync to InnioasisY1Themes
    sync_to_themes()

    # Step 7: Pre-render static fallback pages
    if not args.skip_prerender:
        cmd = [sys.executable, str(HERE / "prerender.py"), "--locales", "all", "--tiers", "core", "--out", "dist"]
        if not run_step("Pre-render static fallback pages", cmd):
            return 1

    print("\nAll advance translation and static fallback generation complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
