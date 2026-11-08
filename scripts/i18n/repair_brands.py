#!/usr/bin/env python3
"""Keep brand and model names exactly as written in every catalog.

Two rules:

1. A source string that is only brand names ("Discord", "Y1", "Timmkoo",
   "Innioasis") is never translated. Machine translation turns "Discord"
   into the German word for strife and "Y1" into "J1" or "Υ1", so those
   catalog values are reset to the source.
2. A source string that mentions a brand must still contain it in the
   translation. Those entries are reported; the translator masks brands
   before a request, so the next run rewrites them correctly.

    python scripts/i18n/repair_brands.py --check
    python scripts/i18n/repair_brands.py --write
    python scripts/i18n/repair_brands.py --write --locales de,fr,ja
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from translate import Masker  # noqa: E402
from multi_provider_translate import _translate_via_google_clients5, translate_single  # noqa: E402

CONFIG = os.path.join(ROOT, "i18n", "config.json")
CATALOGS = os.path.join(ROOT, "i18n", "catalogs")
MODALS = os.path.join(ROOT, "i18n", "worklists", "modals.json")


def load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save(path: str, data: dict) -> None:
    temporary = path + ".tmp"
    with open(temporary, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=1, sort_keys=True)
        handle.write("\n")
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the repairs")
    parser.add_argument("--check", action="store_true", help="report only (the default)")
    parser.add_argument("--retranslate", action="store_true", help="retranslate entries that lost a brand and fill in missing modals with brand protection")
    parser.add_argument("--forget", action="store_true", help="drop entries that lost a brand so the next translate run retries them")
    parser.add_argument("--locales", default="all", help="'all' or de,fr,ja")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    terms = load(CONFIG).get("protectedTerms") or []
    masker = Masker(terms)

    modals: list[str] = []
    if os.path.exists(MODALS):
        try:
            modals = load(MODALS).get("strings") or []
        except (ValueError, OSError):
            pass

    names = sorted(name for name in os.listdir(CATALOGS) if name.endswith(".json"))
    if args.locales != "all":
        wanted = {part.strip() for part in args.locales.split(",") if part.strip()}
        names = [name for name in names if name[:-5] in wanted]

    fixed_total = 0
    lost_total = 0
    retranslated_total = 0
    for name in names:
        path = os.path.join(CATALOGS, name)
        data = load(path)
        strings = data.get("strings") or {}
        loc = name[:-5]
        fixed = 0
        lost = 0
        retranslated = 0
        forgotten: list[str] = []

        # 1. Brand-only strings from modals and existing catalog must stay untranslated
        def get_brands(text: str) -> list[str]:
            if not masker.pattern:
                return []
            return [m.group(0) for m in masker.pattern.finditer(text)]

        for s in modals:
            if masker.is_brand_only(s):
                if strings.get(s) != s:
                    strings[s] = s
                    fixed += 1

        for source, value in list(strings.items()):
            if masker.is_brand_only(source):
                if value != source:
                    strings[source] = source
                    fixed += 1
                continue
            brands = get_brands(source)
            if brands and any(term not in value for term in brands):
                lost += 1
                if args.forget:
                    del strings[source]
                    forgotten.append(source)

        # 2. Retranslate entries that lost a brand or are missing from modals
        if args.retranslate:
            needed: list[str] = []
            for s in modals:
                if masker.is_brand_only(s):
                    continue
                if s not in strings:
                    needed.append(s)
                else:
                    brands = get_brands(s)
                    if brands and any(term not in strings[s] for term in brands):
                        needed.append(s)

            for s, v in list(strings.items()):
                if masker.is_brand_only(s):
                    continue
                brands = get_brands(s)
                if brands and any(term not in v for term in brands):
                    if s not in needed:
                        needed.append(s)

            if needed:
                # Process in batches of up to 10
                for i in range(0, len(needed), 10):
                    batch = needed[i:i + 10]
                    masked_batch = []
                    founds = []
                    for s in batch:
                        h, f = masker.mask(s)
                        masked_batch.append(h)
                        founds.append(f)

                    combined = "\n".join(masked_batch)
                    batch_res = _translate_via_google_clients5(combined, loc)
                    lines = batch_res.split("\n") if batch_res else []
                    if len(lines) != len(batch):
                        lines = []
                        for h in masked_batch:
                            tr = translate_single(h, loc) or ""
                            lines.append(tr)

                    for s, tr, fnd in zip(batch, lines, founds):
                        if tr:
                            restored = masker.restore(tr, fnd)
                            if masker.survives(restored, fnd):
                                strings[s] = restored
                                retranslated += 1

        if fixed or forgotten or retranslated:
            fixed_total += fixed
            retranslated_total += retranslated
            if args.write or args.forget or args.retranslate:
                data["strings"] = strings
                data["count"] = len(strings)
                save(path, data)
            if forgotten:
                cache_path = os.path.join(ROOT, "i18n", "cache", name)
                if os.path.exists(cache_path):
                    try:
                        cache = load(cache_path)
                        for key in forgotten:
                            cache.pop(key, None)
                        save(cache_path, cache)
                    except (ValueError, OSError):
                        pass
        lost_total += lost
        if (fixed or lost or retranslated) and not args.quiet:
            print(f"{name[:-5]:<9} brand-only fixed {fixed:>4}   retranslated {retranslated:>4}   lost a brand {lost:>4}")

    verb = "fixed" if (args.write or args.retranslate) else "would fix"
    print(
        f"\n{verb} {fixed_total} brand-only entries, retranslated {retranslated_total} entries across {len(names)} catalogs; "
        f"{lost_total} entries had lost a brand."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
