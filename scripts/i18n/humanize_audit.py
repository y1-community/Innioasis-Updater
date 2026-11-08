#!/usr/bin/env python3
"""Find AI-writing tells in site-owned English copy and in key translations.

This is a review tool, not a rewriter. It marks the patterns in the humanizer
skills (contrastive "not just X but Y", one-line closers, forced triads, em
dashes, inflated significance, sales language, chatbot residue) so an editor
can rewrite the sentence instead of patching the word.

    python3 scripts/i18n/humanize_audit.py
    python3 scripts/i18n/humanize_audit.py --check
    python3 scripts/i18n/humanize_audit.py --fix-dashes
    python3 scripts/i18n/humanize_audit.py --json .coord/humanize.json

Scope:
  - English source pages in the repository root, plus the shell JS that renders
    navigation, footer, gallery chrome and the donation dock.
  - The zh-CN, zh-TW, fi and ko catalogs, checked against the language-specific
    patterns from the humanizer skills.

Deliberately out of scope: theme names and descriptions written by their
authors. Those are the creator's voice, not site copy. Pass --include-themes to
audit them anyway.

--check exits 1 when a high-severity tell remains in site-owned English copy.
--fix-dashes replaces em and en dashes with a plain hyphen in English source
pages only; it is a mechanical cleanup, not a substitute for a rewrite.
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import re
import sys
from collections import Counter
from typing import Dict, Iterable, List, Tuple

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LOCALE_SUFFIX = re.compile(r"_[a-z]{2,3}(?:-[A-Za-z0-9]{2,4})?\.html?$", re.I)
SKIP_DIRS = {".git", "node_modules", "dist", "_site", ".cache", ".coord", ".github", "i18n", "__pycache__"}
NO_TEXT_RE = re.compile(r"<(script|style|pre|code|kbd|samp|textarea)\b[^>]*>.*?</\1>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
SHELL_FILES = ["nav.js", "gallery-chrome.js", "support_toolbar.html", "site-init.js", "theme-analytics.js"]

# (label, pattern, severity). Severity "high" blocks --check in English source.
ENGLISH: List[Tuple[str, re.Pattern[str], str]] = [
    ("not just / not only ... but", re.compile(r"\bnot\s+(?:just|only|merely)\b[^.]{0,90}\bbut\b", re.I), "high"),
    ("not X, it is Y", re.compile(r"\b(?:this|that|it)\s+is\s+not\s+[^.]{0,70}[.;]\s*(?:it|this|that)\s+is\b", re.I), "high"),
    ("staged opener", re.compile(r"\b(?:let'?s dive|let'?s explore|here'?s what you need to know|without further ado|let'?s break this down)\b", re.I), "high"),
    ("closer / pause line", re.compile(r"\b(?:that is the real win|read that again|let that sink in|that distinction matters)\b", re.I), "high"),
    ("inflated significance", re.compile(r"\b(?:testament to|pivotal moment|critical moment|indelible mark|set the stage for|evolving landscape|future looks bright|exciting times ahead)\b", re.I), "high"),
    ("sales language", re.compile(r"\b(?:nestled in|in the heart of|breathtaking|must-visit|renowned for|groundbreaking|game-chang|cutting-edge|seamless(?:ly)?|effortless(?:ly)?|unlock|empower|elevate your)\b", re.I), "high"),
    ("pseudo-depth", re.compile(r"\b(?:the real question is|at its core|what really matters|the deeper issue|the heart of the matter)\b", re.I), "high"),
    ("broad promise", re.compile(r"\bwhether you(?:'re| are)\b", re.I), "high"),
    ("AI stock word", re.compile(r"\b(?:delve|testament|tapestry|meticulous(?:ly)?|garner|interplay|showcase|underscore|vibrant|profound)\b", re.I), "high"),
    ("chatbot residue", re.compile(r"\b(?:i hope this helps|great question|of course!|let me know if|want me to|shall i continue)\b", re.I), "high"),
    ("em/en dash", re.compile(r"[\u2014\u2013]"), "high"),
    ("triad marker", re.compile(r"\b(?:\w+,\s+\w+,\s+and\s+\w+)\b"), "low"),
]

CHINESE: List[Tuple[str, re.Pattern[str]]] = [
    ("不是X而是Y", re.compile(r"不是[^，。]{0,30}而是")),
    ("不仅/不但", re.compile(r"不仅|不但")),
    ("深入探讨", re.compile(r"深入探讨|深入剖析|深度解析")),
    ("赋能/助力", re.compile(r"赋能|助力|打造|引领")),
    ("至关重要", re.compile(r"至关重要|不可或缺|举足轻重")),
    ("无缝/闭环", re.compile(r"无缝|闭环|全链路")),
    ("值得注意的是", re.compile(r"值得注意的是|需要指出的是|值得一提的是")),
    ("总而言之", re.compile(r"总而言之|综上所述|让我们一起|敬请期待")),
    ("显著提升/全面升级", re.compile(r"显著提升|全面提升|全面升级|焕新|彰显|见证")),
    ("开启新篇章", re.compile(r"开启新篇章|开启新纪元|蓬勃发展")),
]

FINNISH: List[Tuple[str, re.Pattern[str]]] = [
    ("on tärkeää huomata", re.compile(r"on (?:tärkeää|syytä) huomata|on huomattava", re.I)),
    ("merkittävä/keskeinen", re.compile(r"merkittävä|keskeinen|ratkaiseva", re.I)),
    ("saumaton/robusti", re.compile(r"saumaton|robusti|kokonaisvaltainen", re.I)),
    ("hyödyntää/varmistaa", re.compile(r"hyödyntää|varmistaa|mahdollistaa", re.I)),
    ("lisäksi", re.compile(r"\blisäksi\b|\bkokonaisuutena\b|\bloppujen lopuksi\b", re.I)),
    ("passive reporting", re.compile(r"voidaan (?:todeta|huomata)|on todettu", re.I)),
]

KOREAN: List[Tuple[str, re.Pattern[str]]] = [
    ("또한/매우", re.compile(r"또한|매우|극히")),
    ("핵심적/필수적", re.compile(r"핵심적인|필수적|중요한 역할")),
    ("다양한/제공합니다", re.compile(r"다양한|제공합니다|가능하게 합니다")),
    ("결론적으로", re.compile(r"결론적으로|시사합니다|주목할 만")),
    ("완벽한/혁신적", re.compile(r"완벽한|혁신적인|차별화된|새로운 지평")),
    ("살펴보겠습니다", re.compile(r"알아보겠습니다|살펴보겠습니다|확인해 보겠습니다")),
    ("통해", re.compile(r"를 통해|을 통해")),
]

CATALOG_LOCALES = {"zh-CN": CHINESE, "zh-TW": CHINESE, "fi": FINNISH, "ko": KOREAN}


def source_pages(include_themes: bool) -> List[str]:
    found: List[str] = []
    if include_themes:
        for base, dirs, files in os.walk(ROOT):
            dirs[:] = [name for name in dirs if name not in SKIP_DIRS and not name.startswith(".")]
            for name in files:
                if name.lower().endswith((".html", ".htm")):
                    found.append(os.path.join(base, name))
        return found
    for name in os.listdir(ROOT):
        path = os.path.join(ROOT, name)
        if os.path.isfile(path) and name.lower().endswith((".html", ".htm")) and not LOCALE_SUFFIX.search(name):
            found.append(path)
    return sorted(found)


def visible_text(markup: str) -> str:
    text = NO_TEXT_RE.sub(" ", markup)
    text = TAG_RE.sub(" ", text)
    text = html_lib.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def snippet(text: str, pattern: re.Pattern[str], width: int = 90) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    start = max(0, match.start() - width)
    end = min(len(text), match.end() + width)
    return ("..." if start else "") + text[start:end].strip() + ("..." if end < len(text) else "")


def audit_english(include_themes: bool) -> Tuple[List[dict], int]:
    findings: List[dict] = []
    dash_pages = 0
    for path in source_pages(include_themes):
        relative = os.path.relpath(path, ROOT).replace(os.sep, "/")
        markup = open(path, "r", encoding="utf-8", errors="replace").read()
        text = visible_text(markup)
        dash_count = len(re.findall(r"[\u2014\u2013]", text))
        if dash_count:
            dash_pages += 1
        for label, pattern, severity in ENGLISH:
            if label == "em/en dash":
                continue
            match = pattern.search(text)
            if match:
                findings.append(
                    {
                        "file": relative,
                        "label": label,
                        "severity": severity,
                        "snippet": snippet(text, pattern),
                    }
                )
    # Shell strings are source copy too, even though they never appear in HTML.
    for name in SHELL_FILES:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            continue
        text = visible_text(open(path, "r", encoding="utf-8", errors="replace").read())
        for label, pattern, severity in ENGLISH:
            if label in {"em/en dash", "triad marker"}:
                continue
            if pattern.search(text):
                findings.append(
                    {
                        "file": name,
                        "label": label,
                        "severity": severity,
                        "snippet": snippet(text, pattern),
                    }
                )
    return findings, dash_pages


def audit_catalogs(limit: int) -> Dict[str, Counter]:
    summary: Dict[str, Counter] = {}
    for locale, patterns in CATALOG_LOCALES.items():
        path = os.path.join(ROOT, "i18n", "catalogs", locale + ".json")
        if not os.path.exists(path):
            continue
        strings = json.load(open(path, "r", encoding="utf-8")).get("strings", {})
        counter: Counter = Counter()
        examples: Dict[str, str] = {}
        for value in strings.values():
            if not isinstance(value, str):
                continue
            for label, pattern in patterns:
                if pattern.search(value):
                    counter[label] += 1
                    examples.setdefault(label, value[:160])
        summary[locale] = counter
        if counter:
            print(f"\n{locale} catalog: {sum(counter.values())} matches")
            for label, count in counter.most_common(limit):
                print(f"  {count:>5}  {label}: {examples.get(label, '')}")
    return summary


def fix_dashes() -> int:
    changed = 0
    for path in source_pages(include_themes=False):
        markup = open(path, "r", encoding="utf-8", errors="replace").read()
        # Keep code and pre blocks untouched; they may contain a literal dash.
        parts = re.split(r"(<(?:script|style|pre|code)\b[^>]*>.*?</(?:script|style|pre|code)>)", markup, flags=re.S | re.I)
        for index in range(0, len(parts), 2):
            parts[index] = parts[index].replace(" \u2014 ", " - ").replace("\u2014", "-")
            parts[index] = parts[index].replace(" \u2013 ", " - ").replace("\u2013", "-")
        updated = "".join(parts)
        if updated != markup:
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(updated)
            changed += 1
    print(f"Replaced em/en dashes in {changed} English source pages.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Exit 1 on a high-severity English finding")
    parser.add_argument("--fix-dashes", action="store_true", help="Replace em/en dashes in English source pages")
    parser.add_argument("--include-themes", action="store_true", help="Also audit theme submission pages")
    parser.add_argument("--json", default="", help="Write the report to this path")
    parser.add_argument("--limit", type=int, default=8, help="Examples per language")
    args = parser.parse_args()

    if args.fix_dashes:
        return fix_dashes()

    findings, dash_pages = audit_english(args.include_themes)
    high = [item for item in findings if item["severity"] == "high"]

    print(f"English source pages with a dash : {dash_pages}")
    print(f"English source findings          : {len(findings)} ({len(high)} high)")
    for item in findings[: args.limit * 4]:
        print(f"  [{item['severity']}] {item['file']}: {item['label']} :: {item['snippet']}")
    if len(findings) > args.limit * 4:
        print(f"  ... and {len(findings) - args.limit * 4} more")

    catalogs = audit_catalogs(args.limit)

    if args.json:
        target = os.path.join(ROOT, args.json)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as handle:
            json.dump(
                {
                    "english": findings,
                    "dash_pages": dash_pages,
                    "catalogs": {locale: dict(counter) for locale, counter in catalogs.items()},
                },
                handle,
                ensure_ascii=False,
                indent=1,
            )
            handle.write("\n")
        print(f"\nWrote {os.path.relpath(target, ROOT)}")

    if args.check and high:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
