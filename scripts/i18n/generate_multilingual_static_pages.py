#!/usr/bin/env python3
"""
Generate literal static multilingual HTML pages for search engines, SEO, and lightning-fast loading.

Produces:
    <stem>_<locale>.html directly in root (e.g. index_de.html, index_jp.html, index_ja.html,
    firmware_de.html, guide_de.html, post_install_de.html, etc.)

Features:
    - Bakes translated text from catalogs into the HTML DOM.
    - Preserves and translates meta tags (og:title, og:description, description, twitter tags).
    - Sets <html lang="..." dir="..." data-locale="...">.
    - Rewrites internal page links from foo.html -> foo_<locale>.html.
    - Injects bidirectional hreflang alternate links into both translated pages and source English pages.
    - Updates sitemap.xml and sitemap-i18n.xml with all static multilingual URLs.
"""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import sys
from datetime import datetime, timezone
from typing import Dict, List, Set, Tuple
from xml.sax.saxutils import escape as xml_escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from i18n_core import apply_catalog, load_locales, strip_by_region  # noqa: E402

CONFIG_PATH = os.path.join(ROOT, "i18n", "config.json")
LOCALES_PATH = os.path.join(ROOT, "i18n", "locales.json")
REGIONS_PATH = os.path.join(ROOT, "i18n", "regions.json")

# Target core pages to generate static language versions for (if present in repo)
CORE_PAGE_STEMS = [
    "index",
    "privacy",
    "firmware",
    "guide",
    "firmware-guide",
    "drivers",
    "updater-comparison",
    "troubleshooting",
    "post_install",
    "release_notes",
    "firmware_info",
    "firmware-list",
    "credits",
    "support_devs",
    "notices",
    "universal-flash-tool",
    "sp-flash-tool",
    "sp-flash-tool-mac",
    "installguide",
    "rockbox",
    "rockbox-rom-download",
    "slidia",
    "all_versions",
    "developers",
    "firmware-faq",
    "firmware-benefits",
    "firmware-y1",
    "firmware-y2",
    "better-y-benefits",
    "better-y-y1-software",
    "inniclassic-benefits",
    "inniclassic-y1-software",
    "inniclassic-y2-software",
    "original-software-benefits",
    "original-software-y1",
    "original-software-y2",
    "reborn-y2linux-benefits",
    "reborn-y2linux-y2-software",
    "rockbox-benefits",
    "rockbox-for-y1",
    "rockbox-for-y2",
    "rockbox-y1-software",
    "rockbox-y2-software",
    "rondo-benefits",
    "rondo-y1-software",
    "solar-benefits",
    "solar-y1-software",
    "solar-y2-software",
    "y2player-benefits",
    "y2player-y2-software",
    "y2reborn_wifibt",
    "recover-non-booting-device",
    "rockbox-y1-themes",
    # Themes repo specific pages
    "solar",
    "upload",
    "y2-themes",
    "report-theme",
    "theme",
    "404",
]

# Major global locales to generate literal static pages for
DEFAULT_STATIC_LOCALES = [
    "de", "ja", "es", "fr", "it", "pt-BR", "pt-PT", "ru", "zh-CN", "zh-TW",
    "ko", "ar", "nl", "pl", "tr", "uk", "vi", "th", "id", "he",
    "hi", "cs", "el", "sv", "fa", "da", "fi", "hu", "no", "ro"
]

# Aliases to duplicate for convenience and search engine compatibility
# e.g. "jp" is universally recognized for Japanese alongside "ja"
LOCALE_ALIASES = {
    "ja": ["jp"],
    "zh-CN": ["zh", "zh-cn"],
    "zh-TW": ["zh-tw"],
    "pt-BR": ["pt", "pt-br"],
    "pt-PT": ["pt-pt"],
    "ko": ["kr"],
}

CANONICAL_RE = re.compile(
    r"""(<link\b[^>]*?\brel\s*=\s*["']canonical["'][^>]*?\bhref\s*=\s*)(["'])([^"']+)\2""",
    re.IGNORECASE,
)
OGURL_RE = re.compile(
    r"""(<meta\b[^>]*?\bproperty\s*=\s*["']og:url["'][^>]*?\bcontent\s*=\s*)(["'])([^"']+)\2""",
    re.IGNORECASE,
)
HTML_TAG_RE = re.compile(r"<html\b([^>]*)>", re.IGNORECASE)
LANG_ATTR_RE = re.compile(r"""\blang\s*=\s*(["'])([^"']*)\1""", re.IGNORECASE)
DIR_ATTR_RE = re.compile(r"""\bdir\s*=\s*(["'])([^"']*)\1""", re.IGNORECASE)
HREFLANG_BLOCK_RE = re.compile(r"\s*<!-- i18n-hreflang-start -->.*?<!-- i18n-hreflang-end -->\s*", re.DOTALL)
HREF_ATTR_RE = re.compile(r"""(<a\b[^>]*?\bhref\s*=\s*)(["'])([^"']+)\2""", re.IGNORECASE)


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def region_for_locale(code: str, regions: dict) -> str:
    for region_id, region in regions.get("regions", {}).items():
        if code in region.get("locales", []):
            return region_id
    for region_id, region in regions.get("regions", {}).items():
        if code in (region.get("autoLocales") or {}).values():
            return region_id
    return regions.get("default", "intl")


def merged_strings(catalog: dict, region: dict, code: str) -> Dict[str, str]:
    strings: Dict[str, str] = dict(catalog.get("strings", {}))
    language = code.split("-")[0]
    for source, by_locale in (region.get("copy") or {}).items():
        value = by_locale.get(code) or by_locale.get(language) or by_locale.get("en")
        if value:
            strings[source] = value
    return strings


def set_html_language_attrs(markup: str, code: str, direction: str) -> str:
    match = HTML_TAG_RE.search(markup)
    if not match:
        return markup
    attrs = match.group(1)
    if LANG_ATTR_RE.search(attrs):
        attrs = LANG_ATTR_RE.sub(f'lang="{code}"', attrs, count=1)
    else:
        attrs = attrs.rstrip() + f' lang="{code}"'
    if DIR_ATTR_RE.search(attrs):
        attrs = DIR_ATTR_RE.sub(f'dir="{direction}"', attrs, count=1)
    else:
        attrs = attrs.rstrip() + f' dir="{direction}"'
    if "data-locale=" not in attrs:
        attrs = attrs.rstrip() + f' data-locale="{code}"'
    else:
        attrs = re.sub(r'data-locale="[^"]*"', f'data-locale="{code}"', attrs)
    return markup[: match.start()] + "<html" + attrs + ">" + markup[match.end():]


def build_hreflang_block(stem: str, origin: str, target_codes: List[str]) -> str:
    lines = [
        "<!-- i18n-hreflang-start -->",
        f'  <link rel="alternate" hreflang="x-default" href="{origin}/{stem}.html">',
        f'  <link rel="alternate" hreflang="en" href="{origin}/{stem}.html">',
    ]
    for code in target_codes:
        lines.append(f'  <link rel="alternate" hreflang="{code}" href="{origin}/{stem}_{code}.html">')
        # Add alias hreflangs
        for alias in LOCALE_ALIASES.get(code, []):
            lines.append(f'  <link rel="alternate" hreflang="{alias}" href="{origin}/{stem}_{alias}.html">')
    lines.append("  <!-- i18n-hreflang-end -->")
    return "\n".join(lines)


def inject_seo_tags(markup: str, stem: str, code: str, origin: str, target_codes: List[str]) -> str:
    # 1. Canonical and OG URL
    canonical_url = f"{origin}/{stem}_{code}.html" if code != "en" else f"{origin}/{stem}.html"
    if CANONICAL_RE.search(markup):
        markup = CANONICAL_RE.sub(
            lambda m: m.group(1) + m.group(2) + canonical_url + m.group(2), markup, count=1
        )
    else:
        markup = markup.replace("</head>", f'  <link rel="canonical" href="{canonical_url}">\n</head>', 1)

    if OGURL_RE.search(markup):
        markup = OGURL_RE.sub(
            lambda m: m.group(1) + m.group(2) + canonical_url + m.group(2), markup, count=1
        )

    # 2. Hreflang alternates
    markup = HREFLANG_BLOCK_RE.sub("\n", markup)
    block = build_hreflang_block(stem, origin, target_codes)
    if "</head>" in markup:
        markup = markup.replace("</head>", f"  {block}\n</head>", 1)

    return markup


def rewrite_internal_links(markup: str, code: str, valid_stems: Set[str], partner_origin: str) -> str:
    """Rewrites hrefs inside static page so navigation stays in target language."""
    def replace_href(match: re.Match) -> str:
        prefix = match.group(1)
        quote = match.group(2)
        raw = match.group(3)

        # Ignore external / non-nav links
        if raw.startswith(("mailto:", "tel:", "javascript:", "#", "data:", "blob:")):
            return match.group(0)

        # Partner site cross-domain links: carry language
        if partner_origin and (raw.startswith(partner_origin) or "innioasis.app" in raw):
            clean = raw
            sep = "&" if "?" in clean else "?"
            if "lang=" not in clean:
                clean = clean + f"{sep}lang={code}"
            return f"{prefix}{quote}{clean}{quote}"

        # Relative .html links
        parts = raw.split("#", 1)
        path = parts[0]
        fragment = ("#" + parts[1]) if len(parts) > 1 else ""

        path_parts = path.split("?", 1)
        file_path = path_parts[0]
        query = ("?" + path_parts[1]) if len(path_parts) > 1 else ""

        if file_path.endswith(".html"):
            basename = os.path.basename(file_path)
            stem = basename[:-5]
            if stem in valid_stems and not stem.endswith(f"_{code}"):
                new_file = f"{stem}_{code}.html"
                new_path = posixpath.join(posixpath.dirname(file_path), new_file) if "/" in file_path else new_file
                return f"{prefix}{quote}{new_path}{query}{fragment}{quote}"

        return match.group(0)

    return HREF_ATTR_RE.sub(replace_href, markup)


def write_sitemaps(root_dir: str, pages_generated: List[Tuple[str, str]], target_codes: List[str], origin: str) -> None:
    """Writes both sitemap.xml and sitemap-i18n.xml with full multilingual URLs."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    stems = sorted(list({stem for stem, _ in pages_generated}))
    
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]

    # 1. Base English pages with alternates
    for stem in stems:
        if stem == "404" or stem.startswith("404_"):
            continue
        loc = f"{origin}/{stem}.html" if stem != "index" else f"{origin}/"
        priority = "1.0" if stem in ("index", "firmware", "guide") else "0.8"
        lines.append("  <url>")
        lines.append(f"    <loc>{xml_escape(loc)}</loc>")
        lines.append(f"    <lastmod>{today}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{xml_escape(origin + "/" + stem + ".html")}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{xml_escape(origin + "/" + stem + ".html")}"/>')
        for code in target_codes:
            lines.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{xml_escape(origin + "/" + stem + "_" + code + ".html")}"/>')
            for alias in LOCALE_ALIASES.get(code, []):
                lines.append(f'    <xhtml:link rel="alternate" hreflang="{alias}" href="{xml_escape(origin + "/" + stem + "_" + alias + ".html")}"/>')
        lines.append("  </url>")

    # 2. Literal static language pages
    for stem, code in pages_generated:
        if stem == "404" or stem.startswith("404_"):
            continue
        loc = f"{origin}/{stem}_{code}.html"
        priority = "0.9" if stem in ("index", "firmware", "guide") else "0.7"
        lines.append("  <url>")
        lines.append(f"    <loc>{xml_escape(loc)}</loc>")
        lines.append(f"    <lastmod>{today}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")

    lines.append("</urlset>")
    content = "\n".join(lines) + "\n"

    for sitemap_name in ("sitemap.xml", "sitemap-i18n.xml"):
        out_path = os.path.join(root_dir, sitemap_name)
        with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        print(f"Updated {sitemap_name} ({len(pages_generated) + len(stems)} entries)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locales", default=",".join(DEFAULT_STATIC_LOCALES), help="Comma-separated locale codes")
    args = parser.parse_args()

    config = load_json(CONFIG_PATH)
    locales_data = load_json(LOCALES_PATH)
    regions = load_json(REGIONS_PATH)
    bases = locales_data["locales"]
    variants = locales_data.get("variants", [])
    loc_by_code = {entry["code"]: entry for entry in bases + variants}

    catalog_dir = os.path.join(ROOT, config["catalogDir"])
    origin = config["prerender"]["siteOrigin"].rstrip("/")
    is_themes_repo = "themes" in origin or os.path.exists(os.path.join(ROOT, "themes.json"))
    partner_origin = "https://innioasis.app" if is_themes_repo else "https://themes.innioasis.app"

    target_locales = [c.strip() for c in args.locales.split(",") if c.strip() and c.strip() != "en"]
    available_codes = []
    for code in target_locales:
        cat_file = os.path.join(catalog_dir, code + ".json")
        if not os.path.exists(cat_file):
            entry = loc_by_code.get(code, {})
            base = entry.get("base")
            if base and os.path.exists(os.path.join(catalog_dir, base + ".json")):
                available_codes.append(code)
        else:
            available_codes.append(code)

    print(f"Generating literal static multilingual pages for {len(available_codes)} locales...")

    # Discover candidate pages existing in repository root
    valid_stems: Set[str] = set()
    for stem in CORE_PAGE_STEMS:
        src = os.path.join(ROOT, stem + ".html")
        if os.path.isfile(src):
            valid_stems.add(stem)

    print(f"Found {len(valid_stems)} candidate HTML pages in repository root: {sorted(valid_stems)}")

    # Update English source pages with hreflang alternates first
    for stem in sorted(valid_stems):
        src_path = os.path.join(ROOT, stem + ".html")
        with open(src_path, "r", encoding="utf-8", errors="replace") as h:
            src_markup = h.read()
        src_markup = inject_seo_tags(src_markup, stem, "en", origin, available_codes)
        with open(src_path, "w", encoding="utf-8", newline="\n") as h:
            h.write(src_markup)

    pages_generated: List[Tuple[str, str]] = []
    total_written = 0

    for idx, code in enumerate(available_codes, start=1):
        loc_entry = loc_by_code.get(code, {})
        direction = loc_entry.get("dir", "ltr")
        cat_path = os.path.join(catalog_dir, code + ".json")
        if not os.path.exists(cat_path):
            base = loc_entry.get("base") or code
            cat_path = os.path.join(catalog_dir, base + ".json")
        if not os.path.exists(cat_path):
            continue

        catalog = load_json(cat_path)
        region_id = region_for_locale(code, regions)
        region = regions.get("regions", {}).get(region_id, {})
        strings = merged_strings(catalog, region, code)
        availability = region.get("availability", {})

        aliases = LOCALE_ALIASES.get(code, [])

        for stem in sorted(valid_stems):
            src_path = os.path.join(ROOT, stem + ".html")
            with open(src_path, "r", encoding="utf-8", errors="replace") as handle:
                markup = handle.read()

            markup = strip_by_region(markup, region_id, availability)
            markup, replaced = apply_catalog(markup, strings, ())
            markup = set_html_language_attrs(markup, code, direction)
            markup = inject_seo_tags(markup, stem, code, origin, available_codes)
            markup = rewrite_internal_links(markup, code, valid_stems, partner_origin)

            target_filename = f"{stem}_{code}.html"
            target_path = os.path.join(ROOT, target_filename)
            with open(target_path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(markup)
            pages_generated.append((stem, code))
            total_written += 1

            # Also generate alias files (e.g. index_jp.html alongside index_ja.html)
            for alias in aliases:
                alias_markup = set_html_language_attrs(markup, alias, direction)
                alias_markup = inject_seo_tags(alias_markup, stem, alias, origin, available_codes)
                alias_filename = f"{stem}_{alias}.html"
                alias_path = os.path.join(ROOT, alias_filename)
                with open(alias_path, "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(alias_markup)
                pages_generated.append((stem, alias))
                total_written += 1

        print(f"[{idx}/{len(available_codes)}] {code:<6} generated {len(valid_stems)} pages (+ {len(aliases)} aliases)")

    # Write unified sitemaps
    write_sitemaps(ROOT, pages_generated, available_codes, origin)

    # Write manifest for client-side router
    manifest = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "locales": available_codes,
        "aliases": LOCALE_ALIASES,
        "pages": sorted(list(valid_stems)),
    }
    manifest_path = os.path.join(ROOT, "i18n", "prerendered.json")
    with open(manifest_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(f"\nSuccessfully generated {total_written} literal static multilingual HTML pages in repository root.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
