import json
import os
from pathlib import Path

ROOT = Path("/Users/ryan/Documents/GitHub")
NEO_I18N = ROOT / "updater-ce-neo/assets/i18n"
UPDATER_CATALOGS = ROOT / "Innioasis-Updater/i18n/catalogs"
THEMES_CATALOGS = ROOT / "InnioasisY1Themes/i18n/catalogs"
LANGUAGES_FILE = NEO_I18N / "languages.json"

languages = json.loads(LANGUAGES_FILE.read_text(encoding="utf-8"))

for lang_file in NEO_I18N.glob("*.json"):
    if lang_file.name == "languages.json":
        continue
    code = lang_file.stem
    try:
        raw_strings = json.loads(lang_file.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {lang_file.name}: {e}")
        continue

    lang_meta = languages.get(code, {})
    name = lang_meta.get("english", code)
    native = lang_meta.get("native", name)

    catalog_data = {
        "locale": code,
        "name": name,
        "native": native,
        "dir": "rtl" if code in ["ar", "fa", "he", "iw", "ur", "ps", "sd", "ug", "dv", "ckb", "yi", "arc", "bal"] else "ltr",
        "source": "en",
        "provider": "updater-ce-neo",
        "count": len(raw_strings),
        "strings": raw_strings
    }

    # Write to Innioasis-Updater
    dest1 = UPDATER_CATALOGS / f"{code}.json"
    if dest1.exists():
        existing = json.loads(dest1.read_text(encoding="utf-8"))
        merged = dict(existing.get("strings", {}))
        merged.update(raw_strings)
        existing["strings"] = merged
        existing["count"] = len(merged)
        dest1.write_text(json.dumps(existing, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        dest1.write_text(json.dumps(catalog_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    # Write to InnioasisY1Themes
    dest2 = THEMES_CATALOGS / f"{code}.json"
    dest2.write_text(json.dumps(catalog_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Seeded catalogs across both repositories from updater-ce-neo.")
