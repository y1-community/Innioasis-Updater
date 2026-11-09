#!/usr/bin/env python3
"""
Turn the strings the site saw missing into catalog entries.

The locale runtime queues a source string when a non-English page has no
catalog entry for it, and posts batches to ``/i18n-missing``. This script
drains an export of those batches and feeds them to the same translation pass
the rest of the site uses:

    python3 scripts/i18n/drain_missing.py --batch misses.json --dry-run
    python3 scripts/i18n/drain_missing.py --batch misses.json --translate

``--batch`` accepts one batch object, a JSON list of them, ``{"batches": [...]}``,
or newline-delimited JSON — whatever a KV export or the webhook log produces.

Only strings that exist in ``i18n/strings/en.json`` are kept. That is the guard
against translating author copy: a theme or app description was never in our
source catalogue, so it is dropped instead of being sent to a provider. Run
``--dry-run`` first; it prints exactly what would be kept and dropped and
touches nothing.

After a successful translation the index is rebuilt, so the language picker
reflects the new coverage.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

MIN_LENGTH = 4
MAX_LENGTH = 300


def load_batches(path: str) -> list:
    """Read every batch in the file, whatever shape the export took."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            raw = handle.read().strip()
    except OSError as error:
        print(f"Cannot read {path}: {error}", file=sys.stderr)
        return []

    if not raw:
        return []

    try:
        data = json.loads(raw)
    except ValueError:
        # Newline-delimited export: one batch per line.
        found = []
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                found.append(json.loads(line))
            except ValueError:
                continue
        return found

    if isinstance(data, dict):
        nested = data.get("batches")
        return nested if isinstance(nested, list) else [data]
    if isinstance(data, list):
        return data
    return []


def usable(text: str) -> bool:
    if not isinstance(text, str):
        return False
    cleaned = text.strip()
    if len(cleaned) < MIN_LENGTH or len(cleaned) > MAX_LENGTH:
        return False
    return any(character.isalpha() for character in cleaned)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--batch", required=True, help="Export of /i18n-missing batches")
    parser.add_argument("--out", default="", help="Worklist file to write")
    parser.add_argument("--translate", action="store_true", help="Run the translation pass")
    parser.add_argument("--locales", default="", help="Comma-separated locales to translate")
    parser.add_argument("--dry-run", action="store_true", help="Report only; write nothing")
    args = parser.parse_args()

    source_path = os.path.join(ROOT, "i18n", "strings", "en.json")
    if not os.path.exists(source_path):
        print("No source catalogue. Run: python3 scripts/i18n/extract_strings.py --tiers core,full", file=sys.stderr)
        return 2

    with open(source_path, "r", encoding="utf-8") as handle:
        known = json.load(handle).get("strings", {})

    batches = load_batches(args.batch)
    if not batches:
        print(f"No batches found in {args.batch}")
        return 2

    per_locale: dict[str, set] = {}
    wanted: set[str] = set()
    dropped_short = 0
    dropped_author = 0
    ignored_batches = 0

    for document in batches:
        if not isinstance(document, dict):
            ignored_batches += 1
            continue
        locale = str(document.get("locale") or "").strip()
        base = str(document.get("base") or locale.split("-")[0]).strip()
        strings = document.get("strings")
        if not locale or not isinstance(strings, list):
            ignored_batches += 1
            continue
        kept = []
        for item in strings:
            text = str(item or "").strip()
            if not usable(text):
                dropped_short += 1
                continue
            if text not in known:
                # Author copy, fetched release notes, or something a reader
                # typed: not ours to translate.
                dropped_author += 1
                continue
            kept.append(text)
        if not kept or not base or base.lower() == "en":
            continue
        wanted.update(kept)
        per_locale.setdefault(base, set()).update(kept)

    if not wanted:
        print("Nothing to translate: no collected string is in the source catalogue.")
        print(f"  batches read      : {len(batches)} ({ignored_batches} unusable)")
        print(f"  dropped, not ours : {dropped_author}")
        print(f"  dropped, unusable : {dropped_short}")
        return 0

    ordered = sorted(wanted)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = args.out or os.path.join(ROOT, "i18n", "worklists", f"missing-{stamp}.json")
    payload = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "batches": len(batches),
        "strings": ordered,
        "locales": {code: sorted(texts) for code, texts in sorted(per_locale.items())},
        "dropped": {"not_in_source": dropped_author, "unusable": dropped_short},
    }

    print(f"Batches read      : {len(batches)} ({ignored_batches} unusable)")
    print(f"Strings to add    : {len(ordered)}")
    print(f"Locales asking    : {len(per_locale)} ({', '.join(sorted(per_locale))[:120]})")
    print(f"Dropped, not ours : {dropped_author} (author copy or fetched text)")
    print(f"Dropped, unusable : {dropped_short} (too short, too long, no letters)")
    for code, texts in sorted(per_locale.items())[:8]:
        print(f"  {code:<8} {len(texts)} string(s)")

    if args.dry_run:
        print(f"\nDry run: {out_path} not written, no catalog touched.")
        return 0

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    print(f"\nWorklist written: {os.path.relpath(out_path, ROOT)}")

    if not args.translate:
        print("Translate it with:")
        print(f"  python3 scripts/i18n/translate.py --strings-from {os.path.relpath(out_path, ROOT)} --locales <codes>")
        return 0

    locales = args.locales or ",".join(sorted(per_locale))
    translate = os.path.join(HERE, "translate.py")
    for step in (
        [sys.executable, translate, "--strings-from", out_path, "--locales", locales],
        [sys.executable, translate, "--index-only"],
    ):
        print(f"\n$ {' '.join(step[:3])} ...")
        run = subprocess.run(step, cwd=ROOT)
        if run.returncode != 0:
            print("Translation step failed; catalogs were left as they are.", file=sys.stderr)
            return run.returncode
    print("\nDone. Review the diff before committing; catalogs are generated files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
