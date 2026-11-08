#!/usr/bin/env python3
"""
Extract every translatable string from the site into one source catalog.

    python scripts/i18n/extract_strings.py                 # core pages
    python scripts/i18n/extract_strings.py --tiers full    # every page

The output (i18n/strings/en.json) is the translation work list. It is keyed by
the normalised English string so the same sentence is never translated twice,
and it records how often each string appears so a reviewer can see which copy
actually matters.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Dict, List, Set

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from i18n_core import extract  # noqa: E402

CONFIG_PATH = os.path.join(ROOT, "i18n", "config.json")


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def glob_to_regex(pattern: str) -> "re.Pattern[str]":
    """Translate a glob where '**' crosses directories and '*' does not."""
    out: List[str] = []
    index = 0
    while index < len(pattern):
        char = pattern[index]
        if pattern.startswith("**/", index):
            out.append("(?:.*/)?")
            index += 3
            continue
        if pattern.startswith("**", index):
            out.append(".*")
            index += 2
            continue
        if char == "*":
            out.append("[^/]*")
        elif char == "?":
            out.append("[^/]")
        else:
            out.append(re.escape(char))
        index += 1
    return re.compile("^" + "".join(out) + "$")


def locale_codes() -> Set[str]:
    """Every locale code the site ships, including aliases.

    Pre-rendered copies of a page are stored beside the source as
    ``<page>_<locale>.html`` (``index_de.html``, ``404_ar.html``). They are
    output, not source: extracting them treated German, Portuguese and Japanese
    prose as English and inflated the work list by an order of magnitude, so
    the catalogs were never able to cover the real English pages.
    """
    codes: Set[str] = {"en"}
    for relative in ("i18n/locales.json", "i18n/site-locales.json"):
        path = os.path.join(ROOT, relative)
        if not os.path.exists(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, ValueError):
            continue
        for key in ("locales", "variants"):
            for entry in data.get(key) or []:
                if not isinstance(entry, dict):
                    continue
                for field in ("code", "base"):
                    value = str(entry.get(field) or "").strip().lower()
                    if value:
                        codes.add(value)
                for alias in entry.get("aliases") or []:
                    alias = str(alias or "").strip().lower()
                    if alias:
                        codes.add(alias)
    return codes


LOCALE_COPY_RE = re.compile(r"_([a-z]{2,3}(?:-[a-z0-9]{2,4})?)\.html?$", re.IGNORECASE)


def is_locale_copy(relative: str, codes: Set[str]) -> bool:
    match = LOCALE_COPY_RE.search(relative)
    if not match:
        return False
    tag = match.group(1).lower()
    if tag in codes:
        return True
    return tag.split("-")[0] in codes


def candidate_pages(config: dict) -> List[str]:
    """Return repo-relative HTML paths for every configured page."""
    tiers = config["tiers"]
    include: List[str] = []
    exclude: List[str] = []
    for tier in tiers.values():
        include.extend(tier.get("include", []))
        exclude.extend(tier.get("exclude", []))

    include_re = [glob_to_regex(pattern) for pattern in include]
    exclude_re = [glob_to_regex(pattern) for pattern in exclude]

    codes = locale_codes()
    selected: Set[str] = set()
    for directory, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [
            name
            for name in dirnames
            if name not in {".git", "node_modules", "dist", "_site", ".cache", "__pycache__"}
        ]
        for filename in filenames:
            if not filename.lower().endswith((".html", ".htm")):
                continue
            absolute = os.path.join(directory, filename)
            relative = os.path.relpath(absolute, ROOT).replace(os.sep, "/")
            if is_locale_copy(relative, codes):
                continue
            if any(pattern.match(relative) for pattern in exclude_re):
                continue
            if any(pattern.match(relative) for pattern in include_re):
                selected.add(relative)
    return sorted(selected)


def load_ui_strings() -> Dict[str, str]:
    """Shell copy rendered by nav.js and friends, harvested separately."""
    path = os.path.join(ROOT, "i18n", "strings", "ui.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle).get("strings", {})


# Units rendered as their own text node beside a live number (theme cards and
# theme pages). They are shorter than the harvester's literal floor, so they
# would otherwise never reach a catalog and every card would cost an API call.
EXTRA_UI_STRINGS = ["views", "downloads"]


SHELL_MARKUP_FILES = ["nav.js", "gallery-chrome.js", "site-init.js"]
LITERAL_RE = re.compile(r"""(['"])((?:\\.|(?!\1)[^\\\n]){4,400}?)\1""")
TAG_RE = re.compile(r"<[^>]*>")
ENTITY_MAP = {"&amp;": "&", "&rarr;": "\u2192", "&larr;": "\u2190", "&mdash;": "\u2014", "&ndash;": "\u2013", "&nbsp;": " ", "&quot;": '"', "&#39;": "'", "&lt;": "<", "&gt;": ">"}


def load_shell_markup_strings() -> Dict[str, str]:
    """Visible text inside the HTML fragments nav.js builds its chrome from.

    Those literals contain tags, so the plain literal harvester drops them and
    the dock/notices labels never reached a catalog; every page load then asked
    a translation API for "Auto" or "All notices " again.
    """
    out: Dict[str, str] = {}
    for name in SHELL_MARKUP_FILES:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            source = handle.read()
        for match in LITERAL_RE.finditer(source):
            literal = match.group(2)
            if "<" not in literal or ">" not in literal:
                continue
            text = TAG_RE.sub("\n", literal)
            for key, value in ENTITY_MAP.items():
                text = text.replace(key, value)
            for segment in text.split("\n"):
                line = " ".join(segment.split())
                if len(line) < 3 or not re.search(r"[A-Za-z]{2}", line):
                    continue
                if any(token in line for token in ("=", "{", "}", "//", "\\")):
                    continue
                out[line] = name
    return out


def load_theme_strings() -> Dict[str, str]:
    """Theme names and descriptions live in themes.json, not in page markup,
    so extraction never saw them and no catalog could cover a card."""
    path = os.path.join(ROOT, "themes.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    themes = data.get("themes") if isinstance(data, dict) else data
    out: Dict[str, str] = {}
    for theme in themes or []:
        if not isinstance(theme, dict):
            continue
        for field in ("name", "description", "author"):
            value = " ".join(str(theme.get(field) or "").split())
            if value:
                out[value] = field
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tiers",
        default="core",
        help="Comma-separated tier names from i18n/config.json (default: core)",
    )
    parser.add_argument("--out", default="", help="Output path, defaults to config stringsFile")
    parser.add_argument("--pages-out", default="", help="Optional per-page work list")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    config = load_config()
    wanted = [name.strip() for name in args.tiers.split(",") if name.strip()]
    known = set(config["tiers"].keys())
    unknown = [name for name in wanted if name not in known]
    if unknown:
        print(f"Unknown tier(s): {', '.join(unknown)}. Known: {', '.join(sorted(known))}", file=sys.stderr)
        return 2

    full_config = dict(config)
    full_config["tiers"] = {name: config["tiers"][name] for name in wanted}
    pages = candidate_pages(full_config)

    strings: Dict[str, dict] = {}
    per_page: Dict[str, int] = {}
    total = 0

    for relative in pages:
        with open(os.path.join(ROOT, relative), "r", encoding="utf-8", errors="replace") as handle:
            markup = handle.read()
        found = extract(markup, config.get("skipTags", []))
        per_page[relative] = len(found)
        for _kind, text in found:
            total += 1
            entry = strings.get(text)
            if entry is None:
                entry = {"n": 0, "pages": 0}
                strings[text] = entry
            entry["n"] += 1

    # Count distinct pages per string in a second pass so the work list can be
    # ordered by reach.
    for relative in pages:
        with open(os.path.join(ROOT, relative), "r", encoding="utf-8", errors="replace") as handle:
            markup = handle.read()
        seen = {text for _kind, text in extract(markup, config.get("skipTags", []))}
        for text in seen:
            strings[text]["pages"] += 1

    ordered = dict(sorted(strings.items(), key=lambda item: (-item[1]["pages"], -item[1]["n"], item[0])))

    # Copy that only exists inside the JS shell still has to be translated.
    ui_strings = load_ui_strings()
    for text, files in ui_strings.items():
        entry = ordered.get(text)
        if entry is None:
            ordered[text] = {"n": 1, "pages": max(1, len(files)), "script": True}
        else:
            entry["script"] = True

    for text in EXTRA_UI_STRINGS:
        entry = ordered.get(text)
        if entry is None:
            ordered[text] = {"n": 1, "pages": 1, "script": True}
        else:
            entry["script"] = True

    for text in load_shell_markup_strings():
        entry = ordered.get(text)
        if entry is None:
            ordered[text] = {"n": 1, "pages": 1, "script": True}
        else:
            entry["script"] = True

    # Theme names and descriptions are rendered by the gallery from themes.json.
    for text in load_theme_strings():
        entry = ordered.get(text)
        if entry is None:
            ordered[text] = {"n": 1, "pages": 1, "theme": True}
        else:
            entry["theme"] = True

    output = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tiers": wanted,
        "pages": len(pages),
        "occurrences": total,
        "count": len(ordered),
        "strings": ordered,
    }

    out_path = os.path.join(ROOT, args.out or config["stringsFile"])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=1)
        handle.write("\n")

    if args.pages_out:
        pages_path = os.path.join(ROOT, args.pages_out)
        os.makedirs(os.path.dirname(pages_path), exist_ok=True)
        with open(pages_path, "w", encoding="utf-8", newline="\n") as handle:
            json.dump({"pages": per_page}, handle, ensure_ascii=False, indent=1)
            handle.write("\n")

    if not args.quiet:
        print(f"Pages scanned : {len(pages)}")
        print(f"Strings found : {len(ordered)} ({total} occurrences)")
        print(f"Written to    : {os.path.relpath(out_path, ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
