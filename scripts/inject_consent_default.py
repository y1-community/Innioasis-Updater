#!/usr/bin/env python3
"""Insert a Consent Mode v2 default before Google Tag Manager on every page.

Google's consent mode must be set before the GTM container loads, otherwise the
first hits are measured under the wrong state. Every page in both sites loads
GTM in the head, so this script inserts one script block immediately before the
container and leaves pages that already declare a default alone.

    python3 scripts/inject_consent_default.py
    python3 scripts/inject_consent_default.py --root ../Innioasis-Updater
    python3 scripts/inject_consent_default.py --check
"""

from __future__ import annotations

import argparse
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SKIP_DIRS = {".git", "node_modules", "dist", "_site", ".cache", ".coord", ".github", "__pycache__"}
GTM_TAG = re.compile(
    r"""<script\b[^>]*\bsrc=["']https://www\.googletagmanager\.com/(?:gtm\.js|gtag/js)[^"']*["'][^>]*>\s*</script>""",
    re.I,
)
CONSENT_DEFAULT = re.compile(r"""gtag\s*\(\s*['"]consent['"]\s*,\s*['"]default['"]""")

SNIPPET = """<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'granted',
    functionality_storage: 'granted',
    security_storage: 'granted',
    wait_for_update: 500
  });
</script>
"""


def pages(root: str):
    for base, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        for name in files:
            # support_toolbar*.html are injected fragments, not standalone pages.
            if name.startswith("support_toolbar"):
                continue
            if name.lower().endswith((".html", ".htm")):
                yield os.path.join(base, name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=ROOT, help="Repository root to process")
    parser.add_argument("--check", action="store_true", help="Report pages without a default, change nothing")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    total = changed = already = missing = 0
    examples = []

    for path in pages(root):
        total += 1
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            markup = handle.read()
        if CONSENT_DEFAULT.search(markup):
            already += 1
            continue
        tag = GTM_TAG.search(markup)
        if not tag:
            missing += 1
            if len(examples) < 10:
                examples.append(os.path.relpath(path, root))
            continue
        if args.check:
            changed += 1
            continue
        updated = markup[: tag.start()] + SNIPPET + markup[tag.start() :]
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(updated)
        changed += 1

    print(f"Pages scanned            : {total}")
    print(f"Consent default present  : {already}")
    print(f"Consent default inserted : {changed}{' (would insert)' if args.check else ''}")
    print(f"Pages without a GTM tag  : {missing}")
    for example in examples:
        print(f"  no GTM: {example}")

    if args.check and (changed or missing):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
