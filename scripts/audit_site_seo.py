#!/usr/bin/env python3
"""Audit what search engines will actually receive.

The generators can succeed and still leave the site unfriendly to Google: a
sitemap URL with no file behind it, a page whose canonical points somewhere
else, a release page with no title or no structured data, or a generated page
that never made it into a sitemap. This check runs after the generators and
exits non-zero on any of those, so the hourly workflow cannot quietly publish
a broken crawl surface.

Usage:
    python scripts/audit_site_seo.py [--limit N]
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://innioasis.app"
LOC = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
DESC_RE = re.compile(
    r"<meta[^>]+name=[\"']description[\"'][^>]+content=[\"'](.*?)[\"']", re.I | re.S
)
CANONICAL_RE = re.compile(
    r"<link[^>]+rel=[\"']canonical[\"'][^>]+href=[\"']([^\"']+)[\"']", re.I
)
ROBOTS_RE = re.compile(
    r"<meta[^>]+name=[\"']robots[\"'][^>]+content=[\"']([^\"']*)[\"']", re.I
)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
LD_RE = re.compile(
    r"<script[^>]+type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>", re.I | re.S
)
LINK_RE = re.compile(r"<a\b[^>]*\bhref=[\"']([^\"']+)[\"']", re.I)
TAG_RE = re.compile(r"<[^>]+>")


def text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(TAG_RE.sub(" ", value or ""))).strip()


def page_key(url: str) -> str:
    """A URL without the two spellings of a directory index."""
    value = html.unescape(url).split("#", 1)[0].split("?", 1)[0].rstrip("/")
    if value.endswith("/index.html"):
        value = value[: -len("/index.html")]
    return value.rstrip("/")


def local_file(url: str) -> pathlib.Path | None:
    if not url.startswith(SITE + "/"):
        return None
    rel = urllib.parse.unquote(url[len(SITE) + 1:].split("#", 1)[0].split("?", 1)[0])
    if not rel or rel.endswith("/"):
        rel += "index.html"
    return ROOT / rel


def read_sitemaps() -> tuple[dict[str, set[str]], list[str]]:
    errors: list[str] = []
    urls: dict[str, set[str]] = {}
    for path in sorted(ROOT.glob("sitemap*.xml")):
        try:
            root = ET.fromstring(path.read_text(encoding="utf-8"))
        except (OSError, ET.ParseError) as exc:
            errors.append("%s is not readable XML: %s" % (path.name, exc))
            continue
        if root.tag.endswith("sitemapindex"):
            continue
        locs = {node.text.strip() for node in root.iter(LOC) if node.text}
        count = len(locs)
        if count > 50000:
            errors.append("%s lists %d URLs (limit 50000)" % (path.name, count))
        urls[path.name] = locs
    return urls, errors


def audit_page(page: pathlib.Path, url: str, localized: bool, limit: int) -> tuple[list[str], list[str]]:
    problems: list[str] = []
    warnings: list[str] = []
    try:
        markup = page.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        return (["cannot read %s: %s" % (page.relative_to(ROOT), exc)], [])
    label = str(page.relative_to(ROOT))
    generated = label.startswith(("release-notes/", "install/"))
    title = text(TITLE_RE.search(markup).group(1)) if TITLE_RE.search(markup) else ""
    desc = html.unescape(DESC_RE.search(markup).group(1)).strip() if DESC_RE.search(markup) else ""
    canonical = CANONICAL_RE.search(markup)
    robots = ROBOTS_RE.search(markup)
    if not title:
        problems.append("%s has no <title>" % label)
    elif len(title) > 110:
        # Google rewrites long titles; this is cosmetic, never a crawl error.
        warnings.append("%s has a %d-character title" % (label, len(title)))
    if not desc:
        # Older translations predate the description pass. A missing description
        # is a quality issue, not a reason to hold back a release build.
        (problems if generated else warnings).append("%s has no meta description" % label)
    elif len(desc) > 320:
        warnings.append("%s has a %d-character description" % (label, len(desc)))
    if not canonical:
        (problems if generated else warnings).append("%s has no canonical link" % label)
    elif not localized:
        value = page_key(canonical.group(1))
        if value != page_key(url):
            # A hand-written page may deliberately canonicalise elsewhere
            # (projects-supported.html points at credits.html). Generated pages
            # must always name themselves.
            (problems if generated else warnings).append(
                "%s is canonical to %s" % (label, value))
    if robots and "noindex" in robots.group(1).lower():
        problems.append("%s is noindex but listed in a sitemap" % label)
    if "/release-notes/" in "/" + label and page.name != "index.html":
        if not H1_RE.search(markup):
            problems.append("%s has no <h1>" % label)
        blocks = LD_RE.findall(markup)
        if not blocks:
            problems.append("%s has no JSON-LD" % label)
        for block in blocks:
            try:
                json.loads(block)
            except ValueError as exc:
                problems.append("%s has invalid JSON-LD: %s" % (label, exc))
        if "-windows.html" in label or "-macos.html" in label or "-linux.html" in label:
            if 'id="steps"' not in markup:
                problems.append("%s has no install steps" % label)
        # Internal links in the generated release pages must resolve on disk.
        # External links, fragments and query-only links are not this check's
        # business, and neither are the rest of the site's hand-written pages.
        for target in LINK_RE.findall(markup):
            if target.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
                continue
            clean = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not clean:
                continue
            resolved = (page.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if clean.endswith("/"):
                resolved = resolved / "index.html"
            if not resolved.exists():
                problems.append("%s links to missing %s" % (label, target))
    if limit:
        problems = problems[:limit]
    return problems, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit sitemaps and generated search metadata.")
    parser.add_argument("--limit", type=int, default=20, help="problems reported per page")
    args = parser.parse_args()

    sitemaps, problems = read_sitemaps()
    if not sitemaps:
        print("seo audit: no sitemap files found", file=sys.stderr)
        return 1
    seen: dict[str, str] = {}
    warnings: list[str] = []
    checked = 0
    release_files = {
        path for path in ROOT.glob("release-notes/**/*.html") if path.is_file()
    }
    listed_files: set[pathlib.Path] = set()
    for name, locs in sitemaps.items():
        for loc in sorted(locs):
            if loc in seen:
                problems.append("%s is listed in both %s and %s" % (loc, seen[loc], name))
                continue
            seen[loc] = name
            path = local_file(loc)
            if path is None:
                problems.append("%s is not on %s" % (loc, SITE))
                continue
            listed_files.add(path)
            if not path.exists():
                problems.append("%s is in %s but has no file" % (loc, name))
                continue
            checked += 1
            localized = name.startswith("sitemap-i18n")
            page_problems, page_warnings = audit_page(path, loc, localized, args.limit)
            problems.extend(page_problems)
            warnings.extend(page_warnings)
    for path in sorted(release_files - listed_files):
        problems.append("%s exists but is not in any sitemap" % path.relative_to(ROOT))
    for warning in warnings[:20]:
        print("seo audit: warning: " + warning, file=sys.stderr)
    if len(warnings) > 20:
        print("seo audit: warning: %d more metadata warnings" % (len(warnings) - 20),
              file=sys.stderr)

    if problems:
        for problem in problems[:200]:
            print("seo audit: " + problem, file=sys.stderr)
        print(
            "seo audit: %d problems across %d checked URLs" % (len(problems), checked),
            file=sys.stderr,
        )
        return 1
    print(
        "seo audit: %d URLs checked, %d release pages listed, no problems"
        % (checked, len(release_files))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
