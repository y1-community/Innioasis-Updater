#!/usr/bin/env python3
"""Ensure every HTML page carries the Google Tag Manager tag.

The site measures with GTM container GTM-TNDGC37L (override with
INNIOASIS_GTM_ID). A generated page that forgets the snippet is invisible in
analytics, and a future advertising integration (Raptive/AdSense) is loaded
from the same tag, so this check runs before pre-rendering.

    python scripts/i18n/check_ga.py --check    # exit 1 when a page is missing
    python scripts/i18n/check_ga.py --fix      # insert the tag, then report
"""

from __future__ import annotations

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

CONTAINER = os.environ.get("INNIOASIS_GTM_ID", "GTM-TNDGC37L")
SNIPPET = (
    '<script>\n'
    '  window.dataLayer = window.dataLayer || [];\n'
    '  function gtag(){dataLayer.push(arguments);}\n'
    '  gtag(\'consent\', \'default\', {\n'
    '    ad_storage: \'denied\',\n'
    '    ad_user_data: \'denied\',\n'
    '    ad_personalization: \'denied\',\n'
    '    analytics_storage: \'granted\',\n'
    '    functionality_storage: \'granted\',\n'
    '    security_storage: \'granted\',\n'
    '    wait_for_update: 500\n'
    '  });\n'
    '</script>\n'
    '<script async src="https://www.googletagmanager.com/gtm.js?id=' + CONTAINER + '"></script>\n'
    '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
    'gtag("js",new Date());</script>\n'
)

SKIP_DIRS = {".git", "dist", "node_modules", "i18n", "assets", ".github"}


def has_tag(html: str) -> bool:
    return "googletagmanager.com/gtm.js" in html or "gtag/js?id=" in html


def pages() -> list[str]:
    found: list[str] = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        for name in files:
            # support_toolbar*.html are injected fragments, not standalone pages.
            if name.startswith("support_toolbar"):
                continue
            if name.endswith(".html"):
                found.append(os.path.join(base, name))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    all_pages = pages()
    missing: list[str] = []
    for path in all_pages:
        with open(path, "r", encoding="utf-8", errors="ignore") as handle:
            if not has_tag(handle.read()):
                missing.append(path)

    print(f"{len(all_pages)} HTML pages, {len(missing)} without a GA/GTM tag")

    if args.fix and missing:
        fixed = 0
        for path in missing:
            with open(path, "r", encoding="utf-8", errors="ignore") as handle:
                html = handle.read()
            if "</head>" not in html:
                continue
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(html.replace("</head>", SNIPPET + "</head>", 1))
            fixed += 1
        print(f"inserted the tag into {fixed} pages")
        return 0

    if missing:
        for path in missing[:12]:
            print("  " + os.path.relpath(path, ROOT))
        if len(missing) > 12:
            print(f"  ... and {len(missing) - 12} more")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
