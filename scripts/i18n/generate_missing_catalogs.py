import json
from pathlib import Path

ROOT = Path("/Users/ryan/Documents/GitHub")
UPDATER_CATALOGS = ROOT / "Innioasis-Updater/i18n/catalogs"
THEMES_CATALOGS = ROOT / "InnioasisY1Themes/i18n/catalogs"
SITE_LOCALES = ROOT / "Innioasis-Updater/i18n/locales.json"

locales_data = json.loads(SITE_LOCALES.read_text(encoding="utf-8"))
locales = locales_data.get("locales", [])

created = 0
for loc in locales:
    code = loc["code"]
    dest1 = UPDATER_CATALOGS / f"{code}.json"
    dest2 = THEMES_CATALOGS / f"{code}.json"

    if not dest1.exists():
        data = {
            "locale": code,
            "name": loc["name"],
            "native": loc.get("native", loc["name"]),
            "dir": loc.get("dir", "ltr"),
            "source": "en",
            "provider": "initial-stub",
            "count": 0,
            "strings": {}
        }
        dest1.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        created += 1

    if not dest2.exists():
        if dest1.exists():
            dest2.write_text(dest1.read_text(encoding="utf-8"), encoding="utf-8")

print(f"Generated {created} catalog stubs. Total catalogs: {len(list(UPDATER_CATALOGS.glob('*.json')))}")
