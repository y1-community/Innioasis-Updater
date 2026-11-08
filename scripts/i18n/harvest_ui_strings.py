#!/usr/bin/env python3
"""
Harvest user-facing strings from the JavaScript shell.

Navigation, the footer, the dock and the directory UI are all rendered by
nav.js and lumen-site.js, so their copy never appears in the static HTML that
extract_strings.py reads. This pulls sentence-like string literals out of those
files into i18n/strings/ui.json, which extract_strings.py merges into the
source catalog.

    python scripts/i18n/harvest_ui_strings.py

The filter is deliberately conservative: a literal must contain a space, start
with a capital letter, and carry no URL, markup or code punctuation. Anything
that slips through is still visible in ui.json and can be dropped by hand.
"""

from __future__ import annotations

import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

SHELL_FILES = [
    "nav.js",
    "lumen-site.js",
    "site-init.js",
    "firmware-catalog.js",
    "tutorial-video.js",
    "portable-zip-links.js",
    "docs-viewer.js",
    "site-locale.js",
    "support_toolbar.html",
]

# Inline scripts inside a page render their own copy too, so they are scanned
# alongside the shared shell files.
INLINE_SCRIPT_RE = re.compile(
    r"<script\b(?![^>]*\bsrc\s*=)[^>]*>([\s\S]*?)</script>", re.IGNORECASE
)

LITERAL_RE = re.compile(r"""(['"])((?:\\.|(?!\1)[^\\\n]){6,240}?)\1""")
HAS_WORD_RE = re.compile(r"[A-Za-z]{2,}")
REJECT_FRAGMENTS = (
    "http",
    "://",
    "<",
    ">",
    "=",
    "{",
    "}",
    ";",
    "_",
    "/",
    "\\",
    "function",
    "px",
    "%",
    "#",
    "@",
    "(",
    ")",
    "[",
    "]",
)


# nav.js and lumen-site.js build their markup by string concatenation, so their
# copy sits in literals such as '">Installation Guide</a>'. Those fail the prose
# test on the tag punctuation alone, which is how the whole navigation and
# footer stayed English while the page body translated. The visible text runs
# are tested on their own instead.
MARKUP_RUN_RE = re.compile(r">([^<>]{2,240})<")

# Nav and footer links are often a single word - "Themes", "Credits",
# "Reddit" - which the two-word prose rule rejects. Inside a tag boundary the
# run is already known to be text, so a lone capitalised word is a label.
SINGLE_WORD_RE = re.compile(r"^[A-Z][A-Za-z'\u2019-]{2,29}$")


def looks_like_prose(value: str) -> bool:
    text = value.strip()
    if len(text) < 6 or len(text) > 220:
        return False
    if " " not in text:
        return False
    if not re.match(r"^[A-Z]", text):
        return False
    if not HAS_WORD_RE.search(text):
        return False
    if any(fragment in text for fragment in REJECT_FRAGMENTS):
        return False
    # A CSS rule or a selector is not copy.
    if text.count(",") > 3 or text.count(":") > 1:
        return False
    if re.fullmatch(r"[A-Z0-9 .&+-]+", text):
        return False
    # Copy already written in another script belongs to that edition.
    if re.search(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]", text):
        return False
    # Currency and symbol tables are data, not copy.
    if re.search(r"[\u20a0-\u20bf\u060b\u09f3\u0e3f\u17db\ufdfc]", text):
        return False
    # Prose is mostly letters; a list of three-letter codes is not.
    letters = len(re.findall(r"[A-Za-z]", text))
    if letters / max(1, len(text)) < 0.6:
        return False
    if len(re.findall(r"[A-Za-z]{3,}", text)) < 2:
        return False
    return True


KNOWN_TOOLBAR_STRINGS = [
    "Running Costs",
    "Help us cover today's running costs",
    "Running costs and community contributions - click to support",
    "You've helped us raise",
    "of our",
    "costs",
    "Only",
    "left to raise for",
    "'s costs.",
    "All donations are appreciated.",
    "We rely on your donations to keep running. Donate now",
    "No one has donated today, will you be the first?",
    "supporter has helped us this week",
    "supporters have helped us this week",
    "supporter helped us this week",
    "supporters helped us this week",
    "join them to keep downloads free for everyone.",
    "join them",
    "Solely self- and donations-funded, and still mostly paid for out of pocket  -  thank you to everyone who chipped in!",
    "Solely self- and donations-funded  -  thank you!",
    "Every extra coffee funds future tool mirrors and development.",
    "Extra donations fund future mirrors & development",
    "Small gifts of $3 to $5 cover about 15% of what this project really costs; most of the rest goes on players bought to test.",
    "Small $3–$5 gifts cover about 15% of real costs",
    "Saved your player with a free firmware download? Consider buying us a coffee.",
    "Saved your player? Buy us a coffee to keep us online",
    "The price of a coffee or two keeps our download servers online this month.",
    "A coffee or two keeps our servers online this month",
    "Solely self- and donations-funded, with no paywalls  -  chip in $3 towards test players and servers.",
    "Self- and donations-funded  -  chip in $3 to support us",
    "If 1 in 50 visitors bought us a coffee, we'd cover most of a test player this month.",
    "If 1 in 50 visitors bought a coffee, we'd cover a test player",
    "If everyone visiting today donated, we'd be able to run for a year",
    "This month's costs are covered - thank you!",
    "This week's costs are covered - thank you!",
    "Today's costs are covered - thank you!",
    "A top supporter",
    "A supporter",
    "Top Supporter",
    "Supporter",
    "Top Supporters",
    "Supporters",
    "has donated",
    "donated",
    "bought us",
    "a coffee",
    "coffees",
    "on Ko-Fi",
    "contributed",
    "for free by sharing 100MB on",
    "Free contribution",
    "Corporate Sponsorship",
    "We donated",
    "Contribution of",
    "contributions",
    "Costs",
    "covered",
    "today",
    "yesterday",
    "day ago",
    "days ago",
    "1 week ago",
    "week ago",
    "weeks ago",
    "1 month ago",
    "month ago",
    "months ago",
    "1 year ago",
    "year ago",
    "years ago",
    "month",
    "week",
    "day",
    "monthly",
    "weekly",
    "daily",
    "this month",
    "this week",
    "for this month",
    "for this week",
    "for today",
    "Loading supporters...",
    "Loading supporters…",
    "Waiting for supporters to appear.",
    "Our projects rely on donations",
    "Don't show donation appeals again",
    "Show community support & running costs",
    "Brings back toolbar goals and donation links.",
    "Every contribution, big or small, matters.",
    "This project is here because people chose to help. Thank you for keeping the archive, the tools, and the community moving.",
    "Thank you.",
    "Full Credits & Ledger →",
    "Support Updater and the Themes Gallery through Ko-fi, Buy Me a Coffee, PayPal, Revolut, or Patreon.",
    "View our full public donor ledger & money raised →",
    "Or help for free with Honeygain (earn $3 by sharing 100MB of bandwidth)",
    "Show crypto options · BTC, ETH, SHIB",
    "Bitcoin (BTC)",
    "Ethereum (ETH)",
    "Shiba Inu (SHIB)",
    "Copy",
    "Donate on Ko-fi",
    "Buy Me a Coffee",
    "Donate by PayPal",
    "Donate by Revolut",
    "Donate by Patreon",
    "Donate on Boosty",
    "Your privacy on Innioasis.app",
    "Analytics and privacy",
    "Close privacy notice",
    "Remember guide feedback answers",
    "Saves your \"was this useful?\" feedback on guides.",
    "Remember nightly builds selection",
    "Shows pre-release and nightly builds in the firmware list.",
    "Save choices"
]


def looks_like_label(value: str) -> bool:
    text = value.strip()
    if not SINGLE_WORD_RE.match(text):
        return False
    if text.upper() == text:
        return False
    if any(fragment in text for fragment in REJECT_FRAGMENTS):
        return False
    return True


def collect(source: str, origin: str, found: dict[str, list[str]]) -> None:
    for match in LITERAL_RE.finditer(source):
        # Markup carries entities - 'All notices &rarr;', 'Developer Guide &amp;
        # Tooling' - and the browser shows them decoded, so the catalog key has
        # to be the decoded text or the lookup misses and the label stays English.
        value = html.unescape(match.group(2))
        if looks_like_prose(value):
            found.setdefault(value.strip(), []).append(origin)
            continue
        for run in MARKUP_RUN_RE.findall(value):
            run = html.unescape(run).strip()
            if looks_like_prose(run) or looks_like_label(run):
                found.setdefault(run, []).append(origin)


def main() -> int:
    found: dict[str, list[str]] = {}
    for s in KNOWN_TOOLBAR_STRINGS:
        found.setdefault(s.strip(), []).append("support_toolbar.html")

    for relative in SHELL_FILES:
        path = os.path.join(ROOT, relative)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            collect(handle.read(), relative, found)

    inline_pages = 0
    for directory, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [
            name for name in dirnames
            if name not in {".git", "node_modules", "dist", "_site", ".cache", "__pycache__", "i18n"}
        ]
        for filename in filenames:
            if not filename.lower().endswith((".html", ".htm")):
                continue
            path = os.path.join(directory, filename)
            with open(path, "r", encoding="utf-8", errors="replace") as handle:
                markup = handle.read()
            blocks = INLINE_SCRIPT_RE.findall(markup)
            if not blocks:
                continue
            inline_pages += 1
            relative = os.path.relpath(path, ROOT).replace(os.sep, "/")
            for block in blocks:
                collect(block, relative, found)

    output = {
        "note": "Strings rendered by the JS shell. Merged into the source catalog by extract_strings.py.",
        "strings": {text: sorted(set(files)) for text, files in sorted(found.items())},
    }

    target = os.path.join(ROOT, "i18n", "strings", "ui.json")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=1)
        handle.write("\n")

    print(f"Harvested {len(found)} shell strings from {len(SHELL_FILES)} files "
          f"and {inline_pages} pages with inline scripts into {os.path.relpath(target, ROOT)}")
    if "--list" in sys.argv:
        for text in sorted(found, key=len, reverse=True):
            print(repr(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
