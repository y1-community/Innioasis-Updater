#!/usr/bin/env python3
"""
Automated batch translator for site pages and catalogs.
Extracts strings and updates catalogs for any target locales using multi-provider free fallbacks.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from multi_provider_translate import translate_single

CATALOGS_DIR = ROOT / "i18n/catalogs"
LOCALES_FILE = ROOT / "i18n/locales.json"

def get_target_locales():
    data = json.loads(LOCALES_FILE.read_text(encoding="utf-8"))
    return [loc["code"] for loc in data.get("locales", [])]

def update_catalog(locale_code: str, max_strings: int = 50):
    catalog_path = CATALOGS_DIR / f"{locale_code}.json"
    if not catalog_path.exists():
        return 0

    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    strings = catalog.get("strings", {})

    en_source_path = ROOT / "i18n/strings/en.json"
    if not en_source_path.exists():
        return 0
    en_source = json.loads(en_source_path.read_text(encoding="utf-8")).get("strings", {})

    count = 0
    # Process untranslated strings up to max_strings
    for key in list(en_source.keys()):
        if count >= max_strings:
            break
        if key not in strings or strings[key] == key:
            translated = translate_single(key, locale_code)
            if translated:
                strings[key] = translated
                count += 1
                time.sleep(0.05)

    catalog["strings"] = strings
    catalog["count"] = len(strings)
    catalog_path.write_text(json.dumps(catalog, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", default=None, help="Specific locale to update")
    parser.add_argument("--limit", type=int, default=20, help="Max strings per locale")
    args = parser.parse_args()

    locales = [args.locale] if args.locale else get_target_locales()
    print(f"Starting automatic translation update for {len(locales)} locales...")

    for code in locales:
        try:
            n = update_catalog(code, max_strings=args.limit)
            if n > 0:
                print(f"[{code}] translated {n} new strings.")
        except Exception as e:
            print(f"[{code}] error: {e}")

if __name__ == "__main__":
    main()
