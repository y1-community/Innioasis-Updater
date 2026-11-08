import json
from pathlib import Path

ROOT = Path("/Users/ryan/Documents/GitHub")
UPDATER_LANG_FILE = ROOT / "updater-ce-neo/assets/i18n/languages.json"
SITE_LOCALES_FILE = ROOT / "Innioasis-Updater/i18n/locales.json"
OUT_LOCALES_FILE = ROOT / "Innioasis-Updater/i18n/locales.json"
OUT_SITE_LOCALES = ROOT / "Innioasis-Updater/i18n/site-locales.json"

neo_langs = json.loads(UPDATER_LANG_FILE.read_text(encoding="utf-8"))
site_locales_data = json.loads(SITE_LOCALES_FILE.read_text(encoding="utf-8"))

existing_locales = {loc["code"]: loc for loc in site_locales_data.get("locales", [])}

rtl_codes = {"ar", "fa", "he", "iw", "ur", "ps", "sd", "ug", "dv", "ckb", "yi", "arc", "bal"}

merged_locales = []
all_codes = set(neo_langs.keys()).union(set(existing_locales.keys()))

for code in sorted(list(all_codes)):
    if code in existing_locales:
        item = existing_locales[code]
    else:
        info = neo_langs.get(code, {})
        eng_name = info.get("english", code)
        nat_name = info.get("native", eng_name)
        base = code.split("-")[0] if "-" in code else None
        item = {
            "code": code,
            "name": eng_name,
            "native": nat_name,
            "dir": "rtl" if (code in rtl_codes or (base and base in rtl_codes)) else "ltr"
        }
        if base and base != code:
            item["base"] = base
    merged_locales.append(item)

site_locales_data["locales"] = merged_locales
SITE_LOCALES_FILE.write_text(json.dumps(site_locales_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

picker_locales = []
for loc in merged_locales:
    entry = {
        "code": loc["code"],
        "name": loc["name"],
        "native": loc.get("native", loc["name"]),
        "dir": loc.get("dir", "ltr")
    }
    if "base" in loc:
        entry["base"] = loc["base"]
    picker_locales.append(entry)

site_loc_out = {
    "generated": "2026-11-08T12:00:00+00:00",
    "locales": picker_locales
}
OUT_SITE_LOCALES.write_text(json.dumps(site_loc_out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Merged total of {len(merged_locales)} locales successfully.")
