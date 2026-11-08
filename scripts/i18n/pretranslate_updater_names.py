#!/usr/bin/env python3
"""Pre-translate and localise 'Updater' and its variations across all i18n catalogs.

Rules:
- 'Innioasis' is a proper noun and stays untranslated.
- 'Updater' and variations ('Innioasis Updater', 'Updater CE', 'Innioasis Updater CE',
  'Get Innioasis Updater', 'Get Updater CE', etc.) are localised and pre-translated into each catalog.
"""

import glob
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from multi_provider_translate import translate_single
from translate import Masker

NEO_I18N = ROOT.parent / "updater-ce-neo/assets/i18n"
UPDATER_CATALOGS = ROOT / "i18n/catalogs"
THEMES_CATALOGS = ROOT.parent / "InnioasisY1Themes/i18n/catalogs"

masker = Masker(["Innioasis"])


def get_curated_updater_map():
    updater_map = {}
    if NEO_I18N.exists():
        for path in NEO_I18N.glob("*.json"):
            if path.name == "languages.json":
                continue
            code = path.stem
            try:
                d = json.loads(path.read_text(encoding="utf-8"))
                an = d.get("app_name")
                if an:
                    clean = an.replace(" CE", "").strip()
                    updater_map[code] = clean
            except Exception:
                pass
    return updater_map


def main():
    updater_map = get_curated_updater_map()
    print(f"Loaded {len(updater_map)} curated app names from updater-ce-neo.")

    catalog_files = sorted(UPDATER_CATALOGS.glob("*.json"))
    print(f"Found {len(catalog_files)} catalogs in Innioasis-Updater.")

    # Target phrases that use "Updater" or variations
    phrases_to_translate = [
        "Innioasis Updater",
        "Innioasis Updater CE",
        "Updater CE",
        "Updater",
        "Get Innioasis Updater",
        "Get Updater CE",
        "Start with Innioasis Updater",
        "Start with Updater CE",
        "Try Updater first.",
        "Using Innioasis Updater",
        "Install with Updater CE",
        "Download Updater CE",
        "What is Innioasis Updater CE?",
    ]

    # Pre-populate base updater for all catalogs
    for cat_file in catalog_files:
        code = cat_file.stem
        if code in updater_map:
            continue
        # Fall back to root lang
        root_code = code.split("-")[0]
        if root_code in updater_map:
            updater_map[code] = updater_map[root_code]

    print(f"Expanded curated map to {len(updater_map)} locales using root fallbacks.")

    # Key locales to run full phrases translation
    key_locales = [
        "fr", "fr-CA", "fr-BE", "fr-CH",
        "es", "es-ES", "es-MX", "es-AR",
        "de", "de-AT", "de-CH",
        "zh-CN", "zh-TW", "zh-HK",
        "ja", "ko", "it", "it-CH",
        "pt", "pt-BR", "pt-PT",
        "ru", "pl", "uk", "vi", "id", "nl", "nl-BE",
        "tr", "ar", "ar-SA", "he", "hi", "el", "cs", "sv", "th", "da", "fi", "no", "hu", "ro"
    ]

    for cat_file in catalog_files:
        code = cat_file.stem
        if code == "en":
            continue

        try:
            cat_data = json.loads(cat_file.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"Error reading {cat_file}: {e}")
            continue

        strings = cat_data.get("strings", {})

        # 1. Determine base 'Updater' translation
        base_updater = updater_map.get(code)
        if not base_updater:
            base_updater = translate_single("Updater", code)
            if base_updater:
                updater_map[code] = base_updater
                time.sleep(0.04)

        if not base_updater or base_updater.lower() == "updater":
            if code not in ["en", "de", "nl"]:
                # If translation is missing or identical, check root language
                root_code = code.split("-")[0]
                if root_code in updater_map:
                    base_updater = updater_map[root_code]

        if not base_updater:
            base_updater = "Updater"

        # Apply base variations
        strings["Updater"] = base_updater
        strings["Updater CE"] = f"{base_updater} CE"
        strings["Innioasis Updater"] = f"Innioasis {base_updater}"
        strings["Innioasis Updater CE"] = f"Innioasis {base_updater} CE"
        strings["Updater Community Edition"] = f"{base_updater} Community Edition"
        strings["Innioasis Updater Community Edition"] = f"Innioasis {base_updater} Community Edition"

        # 2. For key locales, translate extended phrases with brand masking
        if code in key_locales:
            for phrase in phrases_to_translate:
                if phrase in ["Updater", "Updater CE", "Innioasis Updater", "Innioasis Updater CE"]:
                    continue
                # If already translated and not equal to English, keep unless it failed brand preservation
                current_val = strings.get(phrase)
                if current_val and current_val != phrase and "Innioasis" in current_val:
                    continue

                hidden, found = masker.mask(phrase)
                trans = translate_single(hidden, code)
                if trans:
                    restored = masker.restore(trans, found)
                    if "Innioasis" in phrase and "Innioasis" not in restored:
                        # Ensure Innioasis brand preserved
                        restored = f"Innioasis {restored}"
                    strings[phrase] = restored
                    time.sleep(0.04)

        cat_data["strings"] = strings
        cat_data["count"] = len(strings)

        # Write to Innioasis-Updater
        cat_file.write_text(json.dumps(cat_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

        # Mirror to InnioasisY1Themes if catalog exists
        theme_cat = THEMES_CATALOGS / cat_file.name
        if theme_cat.exists():
            theme_cat.write_text(json.dumps(cat_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Successfully updated all catalogs with localized Updater variations.")


if __name__ == "__main__":
    main()
