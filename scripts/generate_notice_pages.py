#!/usr/bin/env python3
"""Render one static HTML page per entry in notice.xml.

The notices page loads notice.xml at runtime; search engines and answer
engines only see that rendering if they execute scripts. This generator
writes an equivalent page per notice so each has a stable, crawlable URL:
    https://innioasis.app/notices/<id>.html
It also refreshes notices/index.html and the sitemap entries.
"""
import html
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://innioasis.app"
BRAND = "Innioasis Updater"

# The locales that get their own literal page, in the same order the rest of
# the static site uses (scripts/i18n/generate_multilingual_static_pages.py).
# A notice is safety copy: it must be readable without JavaScript in the same
# languages as every other page, and it must be regenerated when notice.xml
# changes instead of being left behind as an orphan.
LOCALES = [
    "de", "ja", "es", "fr", "it", "pt-BR", "pt-PT", "ru", "zh-CN", "zh-TW",
    "ko", "ar", "nl", "pl", "tr", "uk", "vi", "th", "id", "he",
    "hi", "cs", "el", "sv", "fa", "da", "fi", "hu", "no", "ro",
]
RTL_LOCALES = {"ar", "he", "fa", "ur", "ps", "sd", "ug", "dv", "ckb", "yi"}
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
HREFLANG_BLOCK_RE = re.compile(
    r"\s*<!-- i18n-hreflang-start -->.*?<!-- i18n-hreflang-end -->\s*", re.DOTALL
)
INTERNAL_LINK_RE = re.compile(r'\]\((https?://innioasis\.app/[^)\s]+)\)|href="(/[^"]+\.html)[^"]*"')

sys.path.insert(0, str(ROOT / "scripts" / "i18n"))
try:  # The generator still works if the translation tree is absent.
    from i18n_core import apply_catalog  # noqa: E402
except Exception:  # pragma: no cover - only when scripts/i18n is missing
    apply_catalog = None

_CATALOGS = {}


def catalog(code):
    """The translated strings for one locale, loaded once per run."""

    if code not in _CATALOGS:
        path = ROOT / "i18n" / "catalogs" / (code + ".json")
        try:
            _CATALOGS[code] = json.loads(path.read_text(encoding="utf-8")).get(
                "strings", {}
            )
        except (OSError, ValueError):
            _CATALOGS[code] = {}
    return _CATALOGS[code]


def set_language(markup, code, direction):
    match = HTML_TAG_RE.search(markup)
    if not match:
        return markup
    attrs = match.group(1)
    if LANG_ATTR_RE.search(attrs):
        attrs = LANG_ATTR_RE.sub('lang="%s"' % code, attrs, count=1)
    else:
        attrs = attrs.rstrip() + ' lang="%s"' % code
    if DIR_ATTR_RE.search(attrs):
        attrs = DIR_ATTR_RE.sub('dir="%s"' % direction, attrs, count=1)
    else:
        attrs = attrs.rstrip() + ' dir="%s"' % direction
    if "data-locale=" in attrs:
        attrs = re.sub(r'data-locale="[^"]*"', 'data-locale="%s"' % code, attrs)
    else:
        attrs = attrs.rstrip() + ' data-locale="%s"' % code
    return markup[: match.start()] + "<html" + attrs + ">" + markup[match.end():]


def set_canonical(markup, url):
    if CANONICAL_RE.search(markup):
        markup = CANONICAL_RE.sub(
            lambda m: m.group(1) + m.group(2) + url + m.group(2), markup, count=1
        )
    if OGURL_RE.search(markup):
        markup = OGURL_RE.sub(
            lambda m: m.group(1) + m.group(2) + url + m.group(2), markup, count=1
        )
    return markup


def hreflang_block(notice_id):
    """Alternates for one notice, English first and x-default on English."""

    base = "%s/notices/%s" % (SITE, notice_id)
    lines = [
        "<!-- i18n-hreflang-start -->",
        '  <link rel="alternate" hreflang="x-default" href="%s.html">' % base,
        '  <link rel="alternate" hreflang="en" href="%s.html">' % base,
    ]
    for code in LOCALES:
        lines.append(
            '  <link rel="alternate" hreflang="%s" href="%s_%s.html">'
            % (code, base, code)
        )
    lines.append("  <!-- i18n-hreflang-end -->")
    return "\n".join(lines)


def add_hreflang(markup, notice_id):
    markup = HREFLANG_BLOCK_RE.sub("\n", markup)
    block = hreflang_block(notice_id)
    return markup.replace("</head>", "  %s\n</head>" % block, 1)


def localize(markup, code, notice_id):
    """Translate one rendered notice page and point it at its locale copy."""

    strings = catalog(code)
    if apply_catalog is not None and strings:
        markup, _count = apply_catalog(markup, strings)
    markup = set_language(markup, code, "rtl" if code in RTL_LOCALES else "ltr")
    markup = set_canonical(
        markup, "%s/notices/%s_%s.html" % (SITE, notice_id, code)
    )
    markup = add_hreflang(markup, notice_id)
    # The back link follows the language when that notices index exists.
    local_index = ROOT / "notices" / ("index_%s.html" % code)
    if local_index.is_file():
        markup = markup.replace(
            'href="index.html"', 'href="index_%s.html"' % code
        )
    elif (ROOT / ("notices_%s.html" % code)).is_file():
        markup = markup.replace(
            'href="index.html"', 'href="../notices_%s.html"' % code
        )
    return markup


def audit_linked_pages(notices):
    """Warn when a page a notice sends the reader to has no site chrome.

    A notice is read by someone looking for help. Landing on a bare page that
    has no header, footer or language control is the defect this catches; the
    page itself is fixed in place rather than hidden from the notice.
    """

    problems = []
    for n in notices:
        text = "\n".join([n.get("full") or "", n.get("url") or ""])
        for match in INTERNAL_LINK_RE.finditer(text):
            raw = match.group(1) or match.group(2) or ""
            if not raw:
                continue
            if raw.startswith("http"):
                rel = raw[len(SITE):].split("#")[0].split("?")[0].lstrip("/")
            else:
                rel = raw.lstrip("/")
            path = ROOT / rel
            if not path.is_file():
                problems.append("%s -> %s (missing page)" % (n["id"], rel))
                continue
            body = path.read_text(encoding="utf-8", errors="replace")
            missing = [
                name
                for name, marker in (
                    ("header", 'id="nav-root"'),
                    ("header script", "nav.js"),
                    ("footer", 'id="footer-root"'),
                )
                if marker not in body
            ]
            if missing:
                problems.append(
                    "%s -> %s (no %s)" % (n["id"], rel, ", ".join(missing))
                )
    for problem in problems:
        print("warning: notice chrome: %s" % problem)
    return problems


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r'<img src="\2" alt="\1" loading="lazy">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def markdown_to_html(md):
    out, para, items, ordered, fence = [], [], [], False, False
    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []
    def flush_list():
        nonlocal items, ordered
        if items:
            tag = "ol" if ordered else "ul"
            out.append("<%s>" % tag + "".join("<li>" + inline(i) + "</li>" for i in items) + "</%s>" % tag)
            items = []
    for raw in md.replace("\r\n", "\n").split("\n"):
        line = raw.rstrip()
        if line.strip().startswith("```"):
            flush_para(); flush_list()
            if not fence:
                out.append("<pre><code>")
            else:
                out.append("</code></pre>")
            fence = not fence
            continue
        if fence:
            out.append(html.escape(line))
            continue
        if not line.strip():
            flush_para(); flush_list(); continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush_para(); flush_list()
            n = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n)); continue
        if re.match(r"^(-{3,}|\*{3,})$", line.strip()):
            flush_para(); flush_list(); out.append("<hr>"); continue
        if line.startswith(">"):
            flush_para(); flush_list()
            out.append("<blockquote><p>" + inline(line.lstrip("> ").strip()) + "</p></blockquote>"); continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            flush_para()
            if ordered or not items and ordered: pass
            if ordered: flush_list()
            items.append(m.group(1)); ordered = False; continue
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            flush_para()
            if items and not ordered: flush_list()
            items.append(m.group(1)); ordered = True; continue
        para.append(line.strip())
    flush_para(); flush_list()
    return "\n".join(x for x in out if x)


HEAD = """<!doctype html>
<html lang="en">
<head>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('consent', 'default', {{
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'granted',
    functionality_storage: 'granted',
    security_storage: 'granted',
    wait_for_update: 500
  }});
  dataLayer.push({{'gtm.start': new Date().getTime(), event: 'gtm.js'}});
</script>
<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-TNDGC37L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
</script>
  <meta charset="utf-8">
  <meta name="author" content="Ryan Specter &amp; Innioasis Community">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} - {brand}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title} - {brand}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="{brand}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} - {brand}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{site}/assets/og-image.png">
  <link rel="icon" href="{up}y1_illustration.png">
  <link rel="stylesheet" href="{up}site-theme.css?v=20261109theme">
  <link rel="stylesheet" href="{up}lumen.css?v=20261105hero">
  <link rel="stylesheet" href="{up}site-pages.css?v=20260818">
  <link rel="stylesheet" href="{up}site-toolbar.css?v=20261108hero">
  <script src="{up}site-init.js?v=20261113badge2" defer></script>
</head>
<body class="site-themes-app"><a class="lumen-skip-link" href="#main">Skip to content</a><div id="nav-root"></div>
"""

FOOT = """<div id="footer-root"></div><div id="support-toolbar-slot"></div>
<script src="{up}firmware-catalog.js?v=20261106mirror" defer></script>
<script src="{up}nav.js?v=20261105copyleft" defer></script>
<script src="{up}site-locale.js?v=20261108c" defer></script>
<script src="{up}lumen-site.js?v=20261105savename" defer></script>
<script src="{up}site-i18n.js?v=20260830" defer></script>
</body></html>
"""


def window(n):
    """Name every target a notice was written for, in the same order the
    website and the app show them. These pages are the unfiltered view, so a
    reader must be able to tell who a notice was addressed to."""
    parts = []
    if n.get("from"):
        parts.append("From " + n.get("from"))
    if n.get("until"):
        parts.append("until " + n.get("until"))
    platform = (n.get("platform") or n.get("os") or "").strip()
    if platform:
        names = {"windows": "Windows", "win": "Windows", "mac": "macOS", "macos": "macOS", "darwin": "macOS", "linux": "Linux"}
        labels = [names.get(part.strip().lower(), part.strip()) for part in platform.split(",") if part.strip()]
        if labels:
            parts.append("Platform: " + ", ".join(labels))
    if n.get("models"):
        parts.append("Models: " + n.get("models"))
    if n.get("device_type"):
        parts.append("Type " + n.get("device_type"))
    if n.get("firmware_repo"):
        repos = [repo.strip().split("/")[-1] for repo in n.get("firmware_repo").split(",") if repo.strip()]
        if repos:
            parts.append("Software: " + ", ".join(repos))
    if n.get("firmware_version"):
        parts.append("Version " + n.get("firmware_version"))
    return " · ".join(parts)


def prune_stale_notice_pages(noticees_dir, notice_ids):
    """Delete generated pages for notices that are no longer published.

    The directory only ever holds pages this script wrote, and an expired
    advisory is still linked from search results and the app, so leaving it on
    disk serves a withdrawn notice as if it were current.
    """

    removed = []
    for path in sorted(noticees_dir.glob("*.html")):
        # The notices index has its own localized copies; neither is a notice.
        if path.name.startswith("index"):
            continue
        if any(
            path.name == notice_id + ".html"
            or path.name.startswith(notice_id + "_")
            for notice_id in notice_ids
        ):
            continue
        path.unlink()
        removed.append(path.name)
    return removed


def build():
    tree = ET.parse(ROOT / "notice.xml")
    notices = []
    for n in tree.getroot().findall("notice"):
        title = (n.findtext("title") or "").strip()
        content = (n.findtext("content") or n.findtext("body") or "").strip()
        full = (n.findtext("full_content") or content).strip()
        url = (n.findtext("url") or n.findtext("link") or "").strip()
        if url.rstrip("/") == SITE:
            url = ""
        notices.append({"id": n.get("id"), "title": title, "content": content,
                        "full": full, "url": url, "meta": window(n),
                        "severity": (n.get("severity") or "info")})
    noticees_dir = ROOT / "notices"
    noticees_dir.mkdir(exist_ok=True)
    written = []
    for n in notices:
        desc = re.sub(r"\s+", " ", re.sub(r"[*_`#>\[\]]|\(([^)]*)\)", r"\1", n["content"]))[:180].strip()
        canonical = "%s/notices/%s.html" % (SITE, n["id"])
        body = [HEAD.format(title=html.escape(n["title"]), brand=BRAND, desc=html.escape(desc),
                            canonical=canonical, site=SITE, up="../")]
        body.append('<main id="main" class="lumen-guide">\n<header><p class="lumen-kicker">%s</p>'
                    '<h1>%s</h1><p class="lead">%s</p><p class="lumen-meta">%s</p></header>\n'
                    % (html.escape(n["meta"] or "Notice"), html.escape(n["title"]),
                       html.escape(n["content"]), html.escape(n["meta"])))
        body.append('<section class="lumen-guide-section lumen-notice-body">%s</section>\n'
                    % markdown_to_html(n["full"]))
        if n["url"]:
            body.append('<p class="lumen-actions"><a class="lumen-button lumen-button--primary" href="%s" rel="noopener">Open the linked page</a></p>\n' % html.escape(n["url"]))
        body.append('<p class="lumen-notice-back"><a href="index.html">← All notices</a></p>\n</main>\n')
        body.append(FOOT.format(up="../"))
        page = add_hreflang("".join(body), n["id"])
        (noticees_dir / (n["id"] + ".html")).write_text(page, encoding="utf-8")
        # One literal copy per supported language, so a notice is readable (and
        # indexable) without the JavaScript language switch.
        for code in LOCALES:
            (noticees_dir / (n["id"] + "_" + code + ".html")).write_text(
                localize(page, code, n["id"]), encoding="utf-8"
            )
        written.append(n)
    written_ids = [n["id"] for n in written]
    pruned = prune_stale_notice_pages(noticees_dir, written_ids)
    if pruned:
        print("removed %d stale notice page(s): %s" % (len(pruned), ", ".join(pruned)))
    audit_linked_pages(written)
    idx = [HEAD.format(title="Notices", brand=BRAND, desc="Current Innioasis Updater notices and device safety advisories.",
                       canonical=SITE + "/notices/index.html", site=SITE, up="../")]
    idx.append('<main id="main" class="lumen-guide">\n<header><p class="lumen-kicker">Notices</p><h1>Current notices</h1>'
               '<p class="lead">Device safety advisories and release notes shown in Innioasis Updater.</p></header>\n<section class="lumen-guide-section"><div class="lumen-grid">')
    for n in written:
        idx.append('<article class="lumen-card"><small>%s</small><h3><a href="%s.html">%s</a></h3><p>%s</p></article>'
                   % (html.escape(n["meta"]), n["id"], html.escape(n["title"]), html.escape(n["content"])))
    idx.append('</div></section></main>\n' + FOOT.format(up="../"))
    index_page = add_hreflang("".join(idx), "index")
    (noticees_dir / "index.html").write_text(index_page, encoding="utf-8")
    # The localized indexes are what the localized notice pages link back to.
    for code in LOCALES:
        localized = index_page
        strings = catalog(code)
        if apply_catalog is not None and strings:
            localized, _count = apply_catalog(localized, strings)
        localized = set_language(
            localized, code, "rtl" if code in RTL_LOCALES else "ltr"
        )
        localized = set_canonical(
            localized, "%s/notices/index_%s.html" % (SITE, code)
        )
        localized = add_hreflang(localized, "index")
        for n in written:
            localized = localized.replace(
                'href="%s.html"' % n["id"],
                'href="%s_%s.html"' % (n["id"], code),
            )
        (noticees_dir / ("index_" + code + ".html")).write_text(
            localized, encoding="utf-8"
        )
    # sitemap
    sp = ROOT / "sitemap.xml"
    if sp.exists():
        s = sp.read_text(encoding="utf-8")
        for n in written:
            locs = ["%s/notices/%s.html" % (SITE, n["id"])] + [
                "%s/notices/%s_%s.html" % (SITE, n["id"], code) for code in LOCALES
            ]
            for loc in locs:
                if loc not in s:
                    s = s.replace(
                        "</urlset>",
                        "  <url><loc>%s</loc><changefreq>weekly</changefreq></url>\n</urlset>"
                        % loc,
                    )
        if "%s/notices/" % SITE not in s:
            s = s.replace("</urlset>", "  <url><loc>%s/notices/index.html</loc><changefreq>weekly</changefreq></url>\n</urlset>" % SITE)
        sp.write_text(s, encoding="utf-8")
    print("generated %d notice pages" % len(written))


if __name__ == "__main__":
    build()
