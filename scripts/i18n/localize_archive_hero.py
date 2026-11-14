#!/usr/bin/env python3
"""Translate the archive hero and the per-release download label in place.

The firmware archive is generated as English pages (firmware-list.html and the
firmware-list_<locale>.html copies), with the translated copy living in
i18n/catalogs/<locale>.json. The runtime translates a page as it loads, but a
visitor without JavaScript, and anything that reads the HTML, should get the
same copy, so this pass writes the catalog text into the page itself.

    python scripts/i18n/localize_archive_hero.py
    python scripts/i18n/localize_archive_hero.py --check

Only three pieces of copy are touched, and only by position inside the
archive's own structure, so the page cannot drift from the generator:

    <header class="lumen-directory-hero">  h1  and  the lead <p>
    <div class="lumen-meta" style="margin-top:6px">  per-release label

A locale whose catalog has no entry for a string keeps the English source,
which is exactly what the runtime falls back to as well.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

HEADLINE = "Every player's software, in one place"
LEAD = (
    "Pick your player, then the software you want. Each entry shows what it is, "
    "who made it, and the download for your computer."
)
ROW_LABEL = "Downloads for your computer:"

# The archive keeps the two legacy page suffixes the runtime also accepts.
LOCALE_ALIASES = {"jp": "ja", "kr": "ko"}

HERO_RE = re.compile(r'(<header class="lumen-directory-hero">)(.*?)(</header>)', re.S)
H1_RE = re.compile(r"<h1\b[^>]*>.*?</h1>", re.S)
LEAD_RE = re.compile(r"<p>.*?</p>", re.S)
ROW_RE = re.compile(r'(<div class="lumen-meta" style="margin-top:6px">)(.*?)(</div>)', re.S)


def escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def read_catalog(locale: str) -> dict:
    path = os.path.join(ROOT, "i18n", "catalogs", locale + ".json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle).get("strings", {})


def catalog(locale: str) -> dict:
    """The locale's strings, falling back to its base language.

    A regional variant (es-419, pt-BR, de-AT) carries only the handful of
    strings that differ from its base, so a missing entry has to resolve the
    way the runtime resolves it: through the base catalog, not to English.
    """
    locale = LOCALE_ALIASES.get(locale, locale)
    if locale == "en":
        return {HEADLINE: HEADLINE, LEAD: LEAD, ROW_LABEL: ROW_LABEL}
    strings = read_catalog(locale)
    base = locale.split("-")[0]
    if base != locale:
        for key, value in read_catalog(base).items():
            strings.setdefault(key, value)
    return strings


def locale_of(path: str) -> str:
    name = os.path.basename(path)
    match = re.match(r"firmware-list_(.+)\.html$", name)
    return match.group(1) if match else "en"


def rewrite(html: str, strings: dict) -> tuple[str, list[str]]:
    """Return the page with the three pieces of copy translated."""
    changed: list[str] = []
    hero = HERO_RE.search(html)
    if not hero:
        return html, changed

    body = hero.group(2)
    headline = strings.get(HEADLINE)
    if headline:
        new_body, count = H1_RE.subn(lambda m: "<h1>" + escape(headline) + "</h1>", body, count=1)
        if count and new_body != body:
            body = new_body
            changed.append("h1")

    lead = strings.get(LEAD)
    if lead:
        new_body, count = LEAD_RE.subn(lambda m: "<p>" + escape(lead) + "</p>", body, count=1)
        if count and new_body != body:
            body = new_body
            changed.append("lead")

    html = html[: hero.start(2)] + body + html[hero.end(2):]

    label = strings.get(ROW_LABEL)
    if label:
        def swap(match: re.Match[str]) -> str:
            inner = match.group(2)
            if inner.strip() == escape(label):
                return match.group(0)
            changed.append("row")
            return match.group(1) + escape(label) + match.group(3)

        html = ROW_RE.sub(swap, html)
    return html, changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report without writing")
    args = parser.parse_args()

    pages = sorted(glob.glob(os.path.join(ROOT, "firmware-list*.html")))
    written = 0
    residue: list[str] = []
    for page in pages:
        locale = locale_of(page)
        strings = catalog(locale)
        with open(page, "r", encoding="utf-8") as handle:
            html = handle.read()
        updated, changed = rewrite(html, strings)
        if args.check:
            if ROW_LABEL in updated and locale != "en":
                residue.append(os.path.basename(page))
            continue
        if updated != html:
            with open(page, "w", encoding="utf-8") as handle:
                handle.write(updated)
            written += 1

    if args.check:
        print(f"{len(pages)} archive pages checked")
        print("untranslated labels: " + (", ".join(residue) if residue else "none"))
        return 1 if residue else 0

    print(f"{written} archive pages updated of {len(pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
