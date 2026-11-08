#!/usr/bin/env python3
"""Propagate base language catalog strings to regional variants.

When a base language (e.g. fr, de, pt, es) has a comprehensive catalog,
regional variants (e.g. fr-CA, de-AT, pt-BR, es-MX) inherit all strings
from the base language while preserving any variant-specific overrides.
This guarantees static fallback generation and catalog loading has full coverage.
"""

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.parent

LOCALES_FILE = ROOT / "i18n/locales.json"
CATALOGS_DIR = ROOT / "i18n/catalogs"
THEMES_CATALOGS_DIR = ROOT.parent / "InnioasisY1Themes/i18n/catalogs"

def propagate_variants():
    if not LOCALES_FILE.exists():
        print(f"Error: {LOCALES_FILE} not found.")
        return 1

    locales_data = json.loads(LOCALES_FILE.read_text(encoding="utf-8"))
    variants = locales_data.get("variants", [])

    print(f"Propagating base translations to {len(variants)} variants...")

    updated_count = 0
    for var in variants:
        code = var.get("code")
        base = var.get("base")
        if not code or not base or code == base:
            continue

        base_cat_path = CATALOGS_DIR / f"{base}.json"
        if not base_cat_path.exists():
            continue

        try:
            base_cat = json.loads(base_cat_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[{code}] Failed to read base catalog {base_cat_path}: {e}")
            continue

        base_strings = base_cat.get("strings", {})
        if not base_strings:
            continue

        var_cat_path = CATALOGS_DIR / f"{code}.json"
        if var_cat_path.exists():
            try:
                var_cat = json.loads(var_cat_path.read_text(encoding="utf-8"))
            except Exception:
                var_cat = {
                    "locale": code,
                    "name": var.get("name", code),
                    "native": var.get("native", var.get("name", code)),
                    "dir": var.get("dir", base_cat.get("dir", "ltr")),
                    "base": base,
                    "strings": {}
                }
        else:
            var_cat = {
                "locale": code,
                "name": var.get("name", code),
                "native": var.get("native", var.get("name", code)),
                "dir": var.get("dir", base_cat.get("dir", "ltr")),
                "base": base,
                "strings": {}
            }

        var_strings = var_cat.get("strings", {})
        initial_len = len(var_strings)

        # Merge base_strings into var_strings where missing or unchanged
        merged_strings = dict(base_strings)
        for k, v in var_strings.items():
            if v and v != k:
                # Keep specific variant override
                merged_strings[k] = v

        var_cat["strings"] = merged_strings
        var_cat["count"] = len(merged_strings)
        var_cat["base"] = base

        # Write to Innioasis-Updater
        var_cat_path.write_text(json.dumps(var_cat, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

        # Mirror to InnioasisY1Themes
        if THEMES_CATALOGS_DIR.exists():
            theme_cat_path = THEMES_CATALOGS_DIR / f"{code}.json"
            theme_cat_path.write_text(json.dumps(var_cat, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

        print(f"[{code}] (base {base}): inherited {len(merged_strings) - initial_len} strings (now {len(merged_strings)} total)")
        updated_count += 1

    print(f"Successfully propagated to {updated_count} variants.")
    return 0

if __name__ == "__main__":
    sys.exit(propagate_variants())
