#!/usr/bin/env python3
"""Build every sitemap for innioasis.app from the files on disk.

A sitemap is only useful when it lists pages that exist, at the URL they are
served from, in files Google will actually accept. The previous layout failed
all three: the translation run wrote a single 90,906-URL ``sitemap-i18n.xml``
(Google rejects a file over 50,000 URLs, so the whole localized site was
unsubmitted), it contained duplicate URLs and ``404.html`` in every language,
and robots.txt never mentioned it.

This script is now the single owner of all of them:

* ``sitemap.xml``          — every real page in the default language
* ``sitemap-i18n-*.xml``   — localized pages, at most 45,000 URLs per file
* ``sitemap-i18n.xml``     — index of those chunks (a urlset when there is one)
* ``sitemap-index.xml``    — what robots.txt points at

Existing ``lastmod`` values are preserved so a re-run is byte-identical, and
``--check`` exits non-zero when anything is stale, which is what the GitHub
Action runs.

Usage:
    python scripts/generate_sitemap.py [--check]
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://innioasis.app"
MAX_URLS = 45000

SKIP_DIRS = {
    "innioasis.app website archive",
    "node_modules",
    ".git",
    ".cache",
    ".github",
    "src",
    "scripts",
    "feeds",
    "assets",
    "dist",
    "functions",
}
SKIP_FILES = {
    "404.html", "support_toolbar.html", "firmware_info.html",
    "innioasis-embed.html", "leaving.html", "donate.html",
}
# Three-letter directories that are not languages.
NOT_LOCALES = {"img", "api", "app", "tmp", "www", "new", "old", "pdf", "css", "js", "log", "dat"}
LOCALE_FILE_RE = re.compile(
    r"^(?P<stem>.+)_(?P<code>[A-Za-z]{2,3}(?:-[A-Za-z0-9]{1,8})?)\.html$"
)
NOINDEX_RE = re.compile(
    r"<meta[^>]+name=[\"']robots[\"'][^>]+content=[\"'][^\"']*noindex", re.I
)
LAST_RE = re.compile(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>")


def rel_for(path: pathlib.Path) -> str:
    return path.relative_to(ROOT).as_posix()


def url_for(rel: str) -> str:
    if rel == "index.html":
        return SITE + "/"
    if rel.endswith("/index.html"):
        return SITE + "/" + rel[: -len("index.html")]
    return SITE + "/" + rel


def is_noindex(path: pathlib.Path) -> bool:
    try:
        return bool(NOINDEX_RE.search(path.read_text(encoding="utf-8", errors="ignore")[:6000]))
    except OSError:
        return False


def locale_dirs() -> set[str]:
    found = set()
    for child in ROOT.iterdir():
        if child.is_dir() and child.name.lower() not in NOT_LOCALES:
            if re.fullmatch(r"[a-z]{2,3}(?:-[A-Za-z0-9]{1,8})?", child.name):
                found.add(child.name)
    return found


def static_pages() -> list[str]:
    pages = []
    for path in ROOT.rglob("*.html"):
        rel = rel_for(path)
        parts = rel.split("/")
        if any(part in SKIP_DIRS for part in parts[:-1]):
            continue
        if rel in SKIP_FILES or rel.startswith("404") or parts[0].startswith("."):
            continue
        if path.name.startswith("theme_downloader"):
            continue
        if is_noindex(path):
            continue
        pages.append(rel)
    return sorted(pages)


def split_locale(rel: str, dirs: set[str]) -> tuple[str, str] | None:
    """``(stem, code)`` when this page is a translation, else None.

    ``jp`` and ``kr`` are not language codes. They are leftover filenames for
    Japanese and Korean, and listing them beside ``ja`` and ``ko`` makes
    Google throw the pair out.
    """
    head = rel.split("/", 1)[0]
    name = rel.rsplit("/", 1)[-1]
    if "/" in rel and head in dirs:
        if head.lower() in {"jp", "kr"}:
            return None
        return name, head
    match = LOCALE_FILE_RE.match(name)
    if not match:
        return None
    code = match.group("code")
    if code.lower() in {"jp", "kr"}:
        return None
    return match.group("stem"), code


def lastmod_map() -> dict[str, str]:
    found: dict[str, str] = {}
    for path in sorted(ROOT.glob("sitemap*.xml")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for loc, lastmod in LAST_RE.findall(text):
            found.setdefault(loc, lastmod.strip())
    return found


def file_date(rel: str) -> str:
    try:
        stamp = (ROOT / rel).stat().st_mtime
    except OSError:
        stamp = dt.datetime.now().timestamp()
    return dt.datetime.fromtimestamp(stamp, dt.timezone.utc).date().isoformat()


def priority_for(rel: str) -> str:
    if rel == "index.html":
        return "1.0"
    if rel == "install/index.html":
        return "0.9"
    if rel.startswith("install/"):
        return "0.8"
    if rel in ("firmware.html", "firmware-list.html"):
        return "0.9"
    if rel.startswith(("release-notes/", "post-install/", "firmware-info/",
                       "rockbox-y1/", "rockbox-y2/", "guides/")):
        return "0.6"
    return "0.7"


def changefreq_for(rel: str) -> str:
    if rel in ("index.html", "firmware.html", "firmware-list.html"):
        return "weekly"
    return "monthly"


def render_urlset(entries: list[tuple[str, str, str, str]], alternates: bool = False) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, lastmod, changefreq, priority in entries:
        lines += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{lastmod}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def name_is_alias(rel: str) -> bool:
    """jp and kr filenames repeat Japanese and Korean. They are not languages."""
    name = rel.rsplit("/", 1)[-1].lower()
    head = rel.split("/", 1)[0].lower()
    return name.endswith(("_jp.html", "_kr.html")) or head in {"jp", "kr"}


def render_index(children: list[tuple[str, str]]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, lastmod in children:
        lines += ["  <sitemap>", f"    <loc>{loc}</loc>"]
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("  </sitemap>")
    lines.append("</sitemapindex>")
    return "\n".join(lines) + "\n"


def build() -> dict[pathlib.Path, str]:
    dirs = locale_dirs()
    known = lastmod_map()
    pages = static_pages()

    main: list[tuple[str, str, str, str]] = []
    localized: list[tuple[str, str, str, str]] = []
    seen: set[str] = set()
    for rel in pages:
        loc = url_for(rel)
        if loc in seen:
            continue
        seen.add(loc)
        entry = (
            loc,
            known.get(loc, file_date(rel)),
            changefreq_for(rel),
            priority_for(rel),
        )
        locale = split_locale(rel, dirs)
        # jp/kr files are the same page as ja/ko. Leave them out of both lists.
        if name_is_alias(rel):
            continue
        if locale:
            localized.append(entry)
        else:
            main.append(entry)

    main.sort(key=lambda item: item[0])
    localized.sort(key=lambda item: item[0])

    outputs: dict[pathlib.Path, str] = {
        ROOT / "sitemap.xml": render_urlset(main),
    }

    chunks = [localized[i:i + MAX_URLS] for i in range(0, len(localized), MAX_URLS)] or [[]]
    chunk_files: list[tuple[str, str]] = []
    for index, chunk in enumerate(chunks, 1):
        name = "sitemap-i18n.xml" if len(chunks) == 1 else f"sitemap-i18n-{index}.xml"
        outputs[ROOT / name] = render_urlset(chunk)
        chunk_files.append((SITE + "/" + name, max((e[1] for e in chunk), default="")))

    if len(chunks) == 1:
        i18n_index = chunk_files[0][0]
    else:
        # Keep the old URL working, now as an index of the chunks.
        outputs[ROOT / "sitemap-i18n.xml"] = render_index(chunk_files)
        i18n_index = SITE + "/sitemap-i18n.xml"

    i18n_last = max((item[1] for item in chunk_files), default="")
    outputs[ROOT / "sitemap-index.xml"] = render_index(
        [
            (SITE + "/sitemap.xml", max((e[1] for e in main), default="")),
            (i18n_index, i18n_last),
        ]
    )
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Build and audit every sitemap.")
    parser.add_argument("--check", action="store_true", help="exit 1 when a sitemap is stale")
    args = parser.parse_args()

    outputs = build()
    stale: list[pathlib.Path] = []
    for path, content in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != content:
            stale.append(path)
    stale_files = [
        path for path in ROOT.glob("sitemap*.xml") if path not in outputs
    ]
    stale.extend(stale_files)
    total = sum(content.count("<loc>") for content in outputs.values())
    if not stale:
        print(f"sitemap: up to date ({len(outputs) - 1} files, {outputs[ROOT / 'sitemap.xml'].count('<url>')} main URLs)")
        return 0
    if args.check:
        for path in stale:
            print(f"sitemap: {path.name} is out of date", file=sys.stderr)
        return 1
    for path in stale:
        if path not in outputs:
            path.unlink()
            print(f"sitemap: removed stale {path.name}")
            continue
        path.write_text(outputs[path], encoding="utf-8")
        print(f"sitemap: wrote {path.name} ({outputs[path].count('<loc>')} URLs)")
    print(f"sitemap: {total} URLs across {len(outputs)} files")
    # A malformed file is worse than a stale one: refuse to leave it behind.
    for path in outputs:
        try:
            ET.fromstring(path.read_text(encoding="utf-8"))
        except ET.ParseError as exc:
            print(f"sitemap: {path.name} is not well-formed XML: {exc}", file=sys.stderr)
            return 1
    for path in outputs:
        if path.name.startswith("sitemap-i18n-") or path.name == "sitemap-i18n.xml":
            if path.read_text(encoding="utf-8").count("<url>") > 50000:
                print(f"sitemap: {path.name} exceeds the 50,000 URL limit", file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
