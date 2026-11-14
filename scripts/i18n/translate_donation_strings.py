#!/usr/bin/env python3
"""Translate all donation, goal, and toolbar strings across all site catalogs."""

import argparse
import csv
import json
import os
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from translate import Masker
from multi_provider_translate import _translate_via_google_clients5, translate_single

CONFIG = ROOT / "i18n" / "config.json"
CATALOGS_DIR = ROOT / "i18n" / "catalogs"
THEMES_CATALOGS_DIR = ROOT.parent / "InnioasisY1Themes" / "i18n" / "catalogs"

with open(CONFIG, "r", encoding="utf-8") as f:
    cfg = json.load(f)
terms = cfg.get("protectedTerms", [])
masker = Masker(terms)

CANONICAL_STRINGS = [
    # Goal headings & titles
    "Monthly Running Costs",
    "Weekly Running Costs",
    "Daily Running Costs",
    "Running Costs",
    "Costs",
    "Thank you - this month's costs are covered",
    "Help us cover this month's running costs",
    "Help us cover this week's running costs",
    "Help us cover today's running costs",
    "Help us cover {period}'s running costs",
    "This month's costs are covered - thank you!",
    "This week's costs are covered - thank you!",
    "Today's costs are covered - thank you!",
    "We rely on your donations to keep running. Donate now",
    "All donations are appreciated.",
    "You've helped us raise {raised} of our {target} costs {period}.",
    "You've helped us raise {raised} of our {target} costs {period}. All donations are appreciated.",
    "Only {amount} left to raise for this month's costs.",
    "Only {amount} left to raise for this week's costs.",
    "Only {amount} left to raise for today's costs.",
    "Only {amount} left to raise for {period}'s costs.",

    # Periods, adjectives, adverbs
    "this month",
    "this week",
    "today",
    "for this month",
    "for this week",
    "for today",
    "this month's",
    "this week's",
    "today's",
    "month",
    "week",
    "day",
    "monthly",
    "weekly",
    "daily",
    "yesterday",
    "last week",
    "a year ago",
    "since {date}",
    "just now",
    "1 minute ago",
    "{count} minutes ago",
    "1 hour ago",
    "{count} hours ago",
    "1 day ago",
    "{count} days ago",
    "1 week ago",
    "{count} weeks ago",
    "1 month ago",
    "{count} months ago",
    "1 year ago",
    "{count} years ago",

    # Rotating phrases
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
    "No one has donated today, will you be the first?",
    "{count} supporter has helped us this week  -  join them to keep downloads free for everyone.",
    "{count} supporters have helped us this week  -  join them to keep downloads free for everyone.",
    "{count} supporter helped us this week  -  join them",
    "{count} supporters helped us this week  -  join them",
    "1 supporter has helped us this week  -  join them to keep downloads free for everyone.",
    "1 supporter helped us this week  -  join them",
    "If everyone visiting today donated, we'd be able to run for a year",

    # Supporters, contributions, coffees, credit templates
    "Supporter",
    "Supporters",
    "Top Supporter",
    "Top Supporters",
    "A supporter",
    "A top supporter",
    "contributions",
    "contribution",
    "{count} contributions",
    "1 contribution",
    "Free contribution",
    "Corporate Sponsorship",
    "Donation",
    "a coffee",
    "{count} coffees",
    "a coffee on Ko-Fi",
    "{count} coffees on Ko-Fi",
    "{supporter} has donated {amount}{time}",
    "{supporter} bought us {coffees}{time}",
    "{supporter} donated {amount} by {method}{time}",
    "{supporter} contributed {amount} for free by sharing 100MB on Honeygain{time}",
    "We donated {amount} to {project} on {method}{time}",
    "Contribution of {amount} from {innioasis} (Corporate Sponsorship){time}",
    "{supporter} donated {amount}",

    # Ledger & credits table headers
    "Supporters and donations ledger",
    "Innioasis commercial sponsorship ledger",
    "Our projects rely on donations",
    "Recent Contributions",
    "All Contributions",
    "Contribution",
    "No contributions recorded yet.",
    "Date",
    "Name",
    "Amount",
    "Method",
    "Notes",

    # Modal controls & General / Family appeals
    "Hide crypto options · BTC, ETH, SHIB",
    "Show crypto options · BTC, ETH, SHIB",
    "Copied!",
    "Close bottom toolbar",
    "Close donation options",
    "Close privacy notice",
    "Close toolbar",
    "Open the site toolbar",
    "Running costs and community contributions - click to support",
    "Donations are processed through Boosty",
    "Donations directly help me support my family and fund the test devices that make this free service possible for everyone. If this tool saved you time or rescued your player today, please consider a small donation, it truly means the world to us.",
    "The servers behind the downloads are paid for out of pocket. A coffee keeps them online for the next owner.",
    "Every release here is built in evenings and weekends. A small donation buys more of that time.",
    "Solely self- and donations-funded, with no paid tier. Mostly paid for out of pocket, with help from people this helped.",
    "Donations buy the test players and cables used to check each release before anyone installs it.",
    "Thousands of downloads go out every month. Donations pay for the servers that deliver them.",
    "Donations pay the running costs of Updater CE, the Themes Gallery and the community firmware archive. Whatever you can add helps.",
    "A few dollars goes a long way here: it covers hundreds of downloads.",
    "Bugs get fixed because someone stayed up testing your exact model. A donation keeps that going.",
    "No company behind this, just one developer, a workbench and a donation page. Everything goes to running costs.",
    "The tools, the guides and the archive are all free. A tip funds the next feature.",
    "If this worked for you, pass the kindness on. It keeps the project free for whoever comes next.",
    "Some of the players this supports were written off as broken. A donation keeps the rescue service running.",
    "No subscription, no deadline, just a page like this one. Give only if it helped.",
    "One person answers the questions, writes the guides and pays the bills. Donations make that sustainable.",
    "Files vanish when a hosting company shuts down. Donations keep the copies that rescued your player online.",
    "One coffee roughly covers the cost of a download. It keeps the next fix within reach.",
    "Ryan and his partner are expecting a baby. Donations towards the project's running costs and our new family are massively appreciated.",
    "There's a new arrival on the way in Ryan's house. Every donation towards the servers and our growing family means a great deal.",
    "Ryan and his partner are getting ready for their child. If this tool has been useful, a donation for the running costs and our growing family would help more than you know."
]

# ---------------------------------------------------------------------------
# Batches beyond the hand-written list
#
# The footer rotates appeals from two pools and the donate dialog picks one of
# them, while the credits screens print whatever the donor typed into the
# ledger. Those strings were never in this batch, so a translated page could
# still show them in English. Collect both at run time: the pools from the
# toolbar source, the messages from donors.csv (canonical here, mirrored to the
# gallery). A new pool entry or a new donor message is translated on the next
# run without anyone remembering to edit this file.
# ---------------------------------------------------------------------------

TOOLBAR_SOURCES = [
    ROOT / "support_toolbar.html",
    ROOT.parent / "InnioasisY1Themes" / "support_toolbar.html",
]
DONOR_LEDGERS = [
    ROOT / "donors.csv",
    ROOT.parent / "InnioasisY1Themes" / "donors.csv",
]

_T_LITERAL_RE = re.compile(r'_t\(\s*"((?:[^"\\]|\\.)*)"')
_JS_ESCAPE_RE = re.compile(r"\\(.)")
_JS_ESCAPES = {"n": "\n", "t": "\t", '"': '"', "\\": "\\", "'": "'"}


def _unescape_js(text: str) -> str:
    return _JS_ESCAPE_RE.sub(lambda m: _JS_ESCAPES.get(m.group(1), m.group(1)), text)


def _toolbar_strings() -> list[str]:
    """Every _t("...") literal the toolbar can put on screen."""
    found: list[str] = []
    for path in TOOLBAR_SOURCES:
        try:
            source = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for match in _T_LITERAL_RE.finditer(source):
            raw = match.group(1)
            # "for this " + _t(goal.periodWord) is a fragment, not a sentence.
            if raw != raw.strip():
                continue
            text = _unescape_js(raw)
            if text:
                found.append(text)
    return found


def _donor_strings() -> list[str]:
    """The messages donors wrote. They appear verbatim on the credits pages."""
    found: list[str] = []
    for path in DONOR_LEDGERS:
        if not path.exists():
            continue
        try:
            with path.open(encoding="utf-8", newline="") as handle:
                for row in csv.DictReader(handle):
                    message = (row.get("Message") or "").strip()
                    if message and "\n" not in message and len(message) <= 500:
                        found.append(message)
        except OSError:
            continue
    return found


def _unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


ALL_STRINGS = _unique(CANONICAL_STRINGS + _toolbar_strings() + _donor_strings())

PLACEHOLDER_RE = re.compile(r"\{[A-Za-z0-9_]+\}")

def mask_text(text: str):
    placeholders = []
    def ph_repl(m):
        placeholders.append(m.group(0))
        return f"[[PH{len(placeholders)-1}]]"
    ph_masked = PLACEHOLDER_RE.sub(ph_repl, text)
    b_masked, found_brands = masker.mask(ph_masked)
    return b_masked, found_brands, placeholders

def unmask_text(text: str, found_brands: list, placeholders: list):
    b_restored = masker.restore(text, found_brands)
    for i, ph in enumerate(placeholders):
        b_restored = re.sub(rf"\[\[\s*PH{i}\s*\]\]", ph, b_restored, flags=re.IGNORECASE)
    return b_restored

def translate_batch(batch: list[str], loc: str) -> list[str]:
    masked_items = []
    metadata = []
    for s in batch:
        masked, fb, ph = mask_text(s)
        masked_items.append(masked)
        metadata.append((fb, ph))

    combined = "\n".join(masked_items)
    batch_res = _translate_via_google_clients5(combined, loc)
    lines = batch_res.split("\n") if batch_res else []
    
    if len(lines) != len(batch):
        lines = []
        for masked in masked_items:
            tr = translate_single(masked, loc) or ""
            lines.append(tr)

    results = []
    for s, tr, (fb, ph) in zip(batch, lines, metadata):
        if tr:
            restored = unmask_text(tr, fb, ph)
            results.append(restored)
        else:
            results.append(s)
    return results

def process_locale(loc: str, write: bool = True):
    path = CATALOGS_DIR / f"{loc}.json"
    if not path.exists():
        return 0

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    strings = data.get("strings", {})

    missing = [s for s in ALL_STRINGS if s not in strings]
    if not missing:
        return 0

    if not write:
        print(f"[{loc}] {len(missing)} missing strings (check mode)")
        return len(missing)

    print(f"[{loc}] Translating {len(missing)} missing strings...")
    if loc == "en":
        for s in missing:
            strings[s] = s
    else:
        batch_size = 10
        for i in range(0, len(missing), batch_size):
            chunk = missing[i:i + batch_size]
            translated_chunk = translate_batch(chunk, loc)
            for s, tr in zip(chunk, translated_chunk):
                strings[s] = tr

    data["strings"] = strings
    data["count"] = len(strings)

    temp_path = str(path) + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(temp_path, path)

    # Sync to InnioasisY1Themes if it exists. Merge only the keys translated
    # here: writing this whole catalog over the gallery's copy would drop
    # strings the gallery has but this repository does not.
    themes_path = THEMES_CATALOGS_DIR / f"{loc}.json"
    if themes_path.exists():
        try:
            with open(themes_path, "r", encoding="utf-8") as f:
                themes_data = json.load(f)
        except (OSError, ValueError):
            themes_data = None
        if isinstance(themes_data, dict):
            merged = themes_data.get("strings")
            if not isinstance(merged, dict):
                merged = {}
            changed = False
            for key in missing:
                if key in strings and merged.get(key) != strings[key]:
                    merged[key] = strings[key]
                    changed = True
            if changed:
                themes_data["strings"] = merged
                themes_data["count"] = len(merged)
                temp_path = str(themes_path) + ".tmp"
                with open(temp_path, "w", encoding="utf-8") as f:
                    json.dump(themes_data, f, ensure_ascii=False, indent=1, sort_keys=True)
                    f.write("\n")
                os.replace(temp_path, themes_path)

    return len(missing)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locales", default="all", help="'all', 'core', or comma-separated")
    parser.add_argument("--check", action="store_true", help="Report missing without translating")
    args = parser.parse_args()

    # Always ensure en is updated first
    process_locale("en", write=not args.check)

    all_files = sorted(CATALOGS_DIR.glob("*.json"))
    locales = [p.stem for p in all_files if p.stem != "en"]

    core_locales = [
        "es", "fr", "de", "zh-CN", "zh-TW", "ja", "ru", "it", "ko", "pt", "ar",
        "hi", "vi", "th", "tr", "pl", "nl", "id", "sv", "cs", "el", "he", "uk", "ro", "hu", "da", "fi", "no"
    ]

    if args.locales == "core":
        locales = [loc for loc in core_locales if (CATALOGS_DIR / f"{loc}.json").exists()]
    elif args.locales != "all":
        wanted = {x.strip() for x in args.locales.split(",") if x.strip()}
        locales = [loc for loc in locales if loc in wanted]

    import concurrent.futures

    total_translated = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_loc = {executor.submit(process_locale, loc, not args.check): loc for loc in locales}
        for future in concurrent.futures.as_completed(future_to_loc):
            loc = future_to_loc[future]
            try:
                count = future.result()
                total_translated += count
            except Exception as e:
                print(f"[{loc}] Error: {e}")

    print(
        f"\nDone! Translated {total_translated} strings across {len(locales)} catalogs "
        f"({len(ALL_STRINGS)} keys in the batch: {len(CANONICAL_STRINGS)} curated, "
        f"{len(_toolbar_strings())} toolbar, {len(_donor_strings())} donor messages)."
    )

if __name__ == "__main__":
    main()
