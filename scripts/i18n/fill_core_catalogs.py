#!/usr/bin/env python3
"""
Fill missing core page strings into catalogs so the website / repo / CDN
already has all foreign language text pre-translated, avoiding client-side
dynamic Google Translate calls.
"""

import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from extract_strings import extract, candidate_pages
from prerender import load_json
from translate import Clients5, Masker, translate_texts

CONFIG_PATH = os.path.join(ROOT, "i18n", "config.json")
CATALOGS_DIR = os.path.join(ROOT, "i18n", "catalogs")
THEMES_ROOT = os.path.abspath(os.path.join(ROOT, "..", "InnioasisY1Themes"))
THEMES_CATALOGS_DIR = os.path.join(THEMES_ROOT, "i18n", "catalogs")

TARGET_LOCALES = [
    "de", "es", "fr", "it", "ja", "zh-CN", "zh-TW",
    "ru", "pt", "ko", "nl", "pl", "ar", "tr", "uk"
]

def is_code_or_garbage(text: str) -> bool:
    s = text.strip()
    if len(s) < 2:
        return True
    if s.startswith(("//", "/*", "<!", "<script", "http://", "https://", "mailto:")):
        return True
    if re.search(r"\b(var |const |let |function\s*\(|return |document\.|window\.|dataLayer\b|\.innerHTML|\.appendChild|\.getElementById)\b", s):
        return True
    if re.search(r"[{};][\s\S]*[{};]", s) and ("{" in s and "}" in s):
        return True
    if re.match(r"^[\d\s.,:%+\-–—/()×]+$", s):
        return True
    if re.match(r"^[*_~`#]+$", s):
        return True
    return False

def main():
    config = load_json(CONFIG_PATH)
    tier_config = dict(config)
    tier_config["tiers"] = {"core": config["tiers"]["core"]}
    pages = candidate_pages(tier_config)
    print(f"Scanning {len(pages)} core pages...")

    all_strings = set()
    for page in pages:
        path = os.path.join(ROOT, page)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        res = extract(content, config)
        for kind, s in res:
            clean = s.strip()
            if clean and not is_code_or_garbage(clean):
                all_strings.add(clean)

    print(f"Found {len(all_strings)} valid unique core strings.")
    masker = Masker(config.get("protectedTerms", []))
    provider = Clients5(config.get("providers", {}).get("clients5", {}))

    for loc in TARGET_LOCALES:
        cat_file = os.path.join(CATALOGS_DIR, f"{loc}.json")
        cat_data = {"locale": loc, "strings": {}}
        if os.path.exists(cat_file):
            with open(cat_file, "r", encoding="utf-8") as f:
                cat_data = json.load(f)
        
        existing = cat_data.get("strings", {})
        missing = [s for s in sorted(all_strings) if s not in existing and not masker.is_brand_only(s)]
        print(f"\n[{loc}] Existing: {len(existing)}, Missing: {len(missing)}")

        if not missing:
            continue

        print(f"Translating {len(missing)} strings for {loc} in batches...")
        # Translate in chunks of 100 strings
        chunk_size = 100
        for i in range(0, len(missing), chunk_size):
            batch = missing[i:i + chunk_size]
            try:
                translated_batch = translate_texts(provider, batch, loc, masker)
                for k, v in translated_batch.items():
                    if v and v != k:
                        existing[k] = v
                print(f"  Translated {min(i + chunk_size, len(missing))}/{len(missing)}...")
            except Exception as e:
                print(f"  Error translating batch: {e}")
            time.sleep(0.1)

        cat_data["strings"] = existing
        cat_data["count"] = len(existing)
        with open(cat_file, "w", encoding="utf-8") as f:
            json.dump(cat_data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"Saved {cat_file} with {len(existing)} strings.")

        # Sync to InnioasisY1Themes if repo exists
        if os.path.isdir(THEMES_CATALOGS_DIR):
            theme_cat_file = os.path.join(THEMES_CATALOGS_DIR, f"{loc}.json")
            with open(theme_cat_file, "w", encoding="utf-8") as f:
                json.dump(cat_data, f, ensure_ascii=False, indent=2)
                f.write("\n")

    print("\nAll core catalogs successfully updated and synced!")

if __name__ == "__main__":
    main()
