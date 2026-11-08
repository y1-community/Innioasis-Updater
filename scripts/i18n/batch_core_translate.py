#!/usr/bin/env python3
"""Batch translate core site locales that still have missing strings.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.parent

CATALOGS_DIR = ROOT / "i18n/catalogs"
CORE_LOCALES = ["zh-CN", "zh-TW", "ru", "it", "ko"]

def main():
    for loc in CORE_LOCALES:
        cat_file = CATALOGS_DIR / f"{loc}.json"
        count = 0
        if cat_file.exists():
            try:
                data = json.loads(cat_file.read_text(encoding="utf-8"))
                count = len(data.get("strings", {}))
            except Exception:
                pass

        if count >= 5500:
            print(f"[{loc}] Already has {count} strings. Skipping.")
            continue

        print(f"\n==========================================")
        print(f"Translating {loc} (currently {count} strings)...")
        print(f"==========================================")
        cmd = [sys.executable, str(HERE / "translate.py"), "--provider", "clients5", "--locales", loc]
        ret = subprocess.run(cmd, cwd=str(ROOT))
        print(f"[{loc}] finished with code {ret.returncode}")

if __name__ == "__main__":
    main()
