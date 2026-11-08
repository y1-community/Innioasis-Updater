#!/usr/bin/env python3
"""
Translates notice.xml notices into catalogs and produces localized notice feeds / notice pages
using free no-auth translation fallbacks.
"""

import json
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from multi_provider_translate import translate_single

NOTICE_XML = ROOT / "notice.xml"
CATALOGS_DIR = ROOT / "i18n/catalogs"
LOCALES_FILE = ROOT / "i18n/site-locales.json"

def main():
    if not NOTICE_XML.exists():
        print("notice.xml not found.")
        return

    tree = ET.parse(NOTICE_XML)
    root = tree.getroot()

    notices = []
    for n in root.findall("notice"):
        title = (n.findtext("title") or "").strip()
        content = (n.findtext("content") or n.findtext("body") or "").strip()
        if title:
            notices.append(title)
        if content:
            notices.append(content)

    print(f"Found {len(notices)} notice strings to ensure translated across catalogs.")

    locales = [l["code"] for l in json.loads(LOCALES_FILE.read_text(encoding="utf-8")).get("locales", [])]

    # Key languages
    TARGETS = ["es", "fr", "de", "zh-CN", "ja", "ru", "pt-BR", "it", "ar", "hi", "ko", "tr", "pl", "uk", "vi", "id", "nl", "th", "el", "cs", "sv", "he", "fa"]

    for code in TARGETS:
        cat_file = CATALOGS_DIR / f"{code}.json"
        if not cat_file.exists():
            continue
        try:
            data = json.loads(cat_file.read_text(encoding="utf-8"))
            strings = data.get("strings", {})
            changed = False
            for text in notices:
                if text not in strings or strings[text] == text:
                    t = translate_single(text, code)
                    if t:
                        strings[text] = t
                        changed = True
            if changed:
                data["strings"] = strings
                data["count"] = len(strings)
                cat_file.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
                print(f"Notice translations added for [{code}]")
        except Exception as e:
            print(f"Error updating [{code}]: {e}")

if __name__ == "__main__":
    main()
