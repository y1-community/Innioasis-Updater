#!/usr/bin/env python3
"""Write the Rockbox-Y1 themes page and the Rockbox tutorial pages.

    rockbox-y1-themes.html                         themes: Updater CE, 360p by hand, 240p
    rockbox-tutorials/index.html                   the tutorial hub
    rockbox-tutorials/<topic>-<os>.html            one page per topic and desktop OS

A tutorial gets a page per operating system only where the steps really
differ (Finder, File Explorer and the Linux file managers show hidden folders,
merge folders and eject drives differently). Everything else is one page, and
every page shares one layout and one set of CSS/JS files, so the pre-rendered
language copies stay the size of the English page.

Facts used here come from the repositories this site already tracks: the
rockbox-y1/themes release (themepack.zip, themes_individual.zip and its README
credits), the Rockbox-Y1 release notes in firmware-catalog.js, and Updater CE's
own theme stage (Settings, USB Storage Mode, Ctrl/Cmd+T).

Usage:
    python scripts/generate_rockbox_tutorials.py
"""
from __future__ import annotations

import datetime
import json
import pathlib
import sys
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from generate_rockbox_pages import (  # noqa: E402
    breadcrumb_ld,
    esc,
    faq_block,
    faq_ld,
    jsonld,
    ol,
    p,
    section,
    ul,
)

ROOT = HERE.parent
SITE = "https://innioasis.app"
TODAY = datetime.date.today().isoformat()
TUTORIAL_DIR = "rockbox-tutorials"

THEMES_RELEASE_TAG = "for_the_gays_and_the_theys"
THEMES_RELEASE = "https://github.com/rockbox-y1/themes/releases/download/%s/" % THEMES_RELEASE_TAG
FONTS_URL = "https://download.rockbox.org/release/4.0/rockbox-fonts-4.0.zip"
IPOD_CLASSIC_THEMES = "https://themes.rockbox.org/index.php?target=ipod6g"

WARNING_240P = (
    "240p builds can't be used on a Y1 bought new after May 2026, or on any Y1 that shipped "
    "with Original Software 3.0.7 or later. Flashing one there stops the player from starting."
)

#: Credits from the rockbox-y1/themes README: theme, original author, port author.
THEMES = [
    ("Adwaitapod", "Dook", "davidcharles283-collab & rockbox-y1"),
    ("Adwaitapod_Dark", "Dook", "davidcharles283-collab & rockbox-y1"),
    ("Adwaitapod_simplified", "Dook", "davidcharles283-collab & rockbox-y1"),
    ("Adwaitapod_simplified-dark", "Dook", "davidcharles283-collab & rockbox-y1"),
    ("Adwaitapod_simplified-arcticons-dark", "Dook", "joelchrono"),
    ("BONES", "CHUCK_LARDO", "rockbox-y1"),
    ("BunnyPod", "Monica G.", "u/Sphynx87"),
    ("crowPod", "Monica G.", "rockbox-y1"),
    ("die-bahn", "Jihoon Kim", "rockbox-y1"),
    ("entune_audio", "Monica G.", "rockbox-y1"),
    ("FreshOS-Y1_Dark", "yuuiko", "u/elinks59 & rockbox-y1"),
    ("FreshOS-Y1_Light", "yuuiko", "u/elinks59 & rockbox-y1"),
    ("Horizon", "Jihoon Kim", "rockbox-y1"),
    ("iClassic_v1.2", "Humberto Santana", "rockbox-y1"),
    ("iClassic_v1.4", "Humberto Santana", "u/CarlosPixel_"),
    ("iClassic_v1.4_Dark", "Humberto Santana", "u/CarlosPixel_"),
    ("iLike", "Alan Brito", "u/elinks59"),
    ("iLike 360 Dark", "Alan Brito", "u/elinks59"),
    ("iMMXX", "FCorp", "rockbox-y1"),
    ("InfoMatrix", "yuuiko", "rockbox-y1"),
    ("Interpod", "Christian Soffke", "rockbox-y1"),
    ("iris-dawn", "Rosé Pine", "rockbox-y1"),
    ("iris-morning", "Rosé Pine", "rockbox-y1"),
    ("iris-night", "Rosé Pine", "rockbox-y1"),
    ("MacClassic", "Billy Blair", "rockbox-y1"),
    ("minimal_RTCsync", "Monica G.", "rockbox-y1"),
    ("OneBit_OLED", "Jihoon Kim", "rockbox-y1"),
    ("Orbit", "Chris Soffke", "rockbox-y1"),
    ("Pixel_Computer", "Monica G.", "rockbox-y1"),
    ("PodOne", "Guillaume Cocatre-Zilgien", "rockbox-y1"),
    ("PodTwo", "Guillaume Cocatre-Zilgien", "rockbox-y1"),
    ("RatPod", "Jannis Bolzern", "rockbox-y1"),
    ("Retina Classic Dark", "rockbox-theme-maker", "rockbox-y1"),
    ("Retina Classic Light", "rockbox-theme-maker", "rockbox-y1"),
    ("Satellite", "Jihoon Kim", "rockbox-y1"),
    ("SKIDMARK", "Jihoon Kim", "rockbox-y1"),
    ("SNARTY", "Simon Andén", "rockbox-y1"),
    ("SnartyJPMod", "u/Sphynx87", ""),
    ("SNAZZ", "Jihoon Kim", "rockbox-y1"),
    ("SNAZZ2", "Jihoon Kim", "rockbox-y1"),
    ("SNAZZ3", "Vera B", "rockbox-y1"),
    ("SNAZZ3_i18n", "Vera B", "rockbox-y1, melianmiko"),
    ("SNAZZPKT", "Jihoon Kim, CHUCK_LARDO", "rockbox-y1"),
    ("SNAZZx90", "DillMillz", "rockbox-y1"),
    ("snespod", "Matthew Pelegrin", "rockbox-y1"),
    ("Snowoasis_Y1", "u/CarlosPixel_", ""),
    ("Snowoasis_Y1_DARK", "u/CarlosPixel_", ""),
    ("Snowoasis_Y1_Sports", "u/CarlosPixel_", ""),
    ("SPAZZ", "CHUCK_LARDO", "rockbox-y1"),
    ("Terminal320", "Dylan Westford", "rockbox-y1"),
    ("Themify", "Dook", "rockbox-y1"),
    ("Widepod", "Christian Soffke", "rockbox-y1"),
    ("Widepod 2", "Chris Soffke", "rockbox-y1"),
    ("yayPod", "Humberto Santana, Awwnigiri", "rockbox-y1"),
]

#: Concrete, repo-backed facts used for keywords and article tags.
BASE_KEYWORDS = [
    "Rockbox", "Rockbox-Y1", "Rockbox for Y1", "Rockbox-Y2", "Innioasis Y1", "Innioasis Y2",
    "Innioasis Y1 Rockbox themes", "Rockbox 360p themes", "Rockbox 240p themes",
    "Rockbox iPod classic themes", "rockbox-y1/rockbox", "rockbox-y1/themes", "spycemagic/y2-rockbox",
    "Updater CE", "Innioasis Updater CE 2.5", ".rockbox folder", "USB Storage Mode",
    "Rockbox-Y1 0.5", "Rockbox-Y1 0.6", "Y1 Type A", "Y1 Type B", "Original Software 3.0.7",
    "MediaTek MT6572", "Rockbox fonts 4.0", "PictureFlow", "album art", "theme pack",
    "dual boot Rockbox and Original Software", "lyrics lrc Rockbox", "Rockbox WPS",
]
FIRMWARE_KEYWORDS = [
    "Solar thesolarproject/solar", "Rondo jarvissax/rondo", "Better-Y Leska1337/better-Y",
    "Koensayr ryan-specter/koensayr-auto", "Inniclassic FabianZettl/inniclassic",
    "Inniclassic Y2 JonaszPotoniec/inniclassic-y2", "Reborn Y2Linux schulzcode/y2linux",
    "Y2Player schulzcode/Y2Player", "JJ Launcher ismileblue/y1_launcher",
]
THEME_AUTHORS = sorted({a for _t, author, _p in THEMES for a in author.split(", ")} - {""})


OS_INFO = {
    "macos": {"label": "macOS", "files": "Finder", "unzip": "Double-click the zip in Finder. Archive Utility unpacks it into a folder beside it."},
    "windows": {"label": "Windows", "files": "File Explorer", "unzip": "Right-click the zip in File Explorer, choose <strong>Extract All</strong>, then <strong>Extract</strong>."},
    "linux": {"label": "Linux", "files": "your file manager", "unzip": "Right-click the zip and choose <strong>Extract Here</strong>, or run <code>unzip</code> in a terminal."},
}
OS_ORDER = ("macos", "windows", "linux")


# ---------------------------------------------------------------- shared layout

ASSETS = {
    "site-theme.css": "20261108headerfix",
    "lumen.css": "20261109sharedheader",
    "site-pages.css": "20260818",
    "site-toolbar.css": "20261108hero",
    "site-init.js": "20260803",
    "nav.js": "20261109sharedheader",
    "site-locale.js": "20261109i18n",
    "site-i18n.js": "20260830",
}


def asset(up: str, name: str) -> str:
    return "%s%s?v=%s" % (up, name, ASSETS[name])


def head(title, description, canonical, up, keywords, tags) -> str:
    tag_meta = "".join('\n  <meta property="article:tag" content="%s">' % esc(tag) for tag in tags)
    return """<!doctype html>
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
  <meta name="creator" content="Ryan Specter &amp; Innioasis Community">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Innioasis Updater">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://innioasis.app/assets/og-image.png">
  <meta property="article:modified_time" content="{today}">
  <meta property="article:section" content="Rockbox">{tag_meta}
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://innioasis.app/assets/og-image.png">
  <link rel="icon" href="{up}y1_illustration.png">
  <link rel="stylesheet" href="{css_theme}">
  <link rel="stylesheet" href="{css_lumen}">
  <link rel="stylesheet" href="{css_pages}">
  <link rel="stylesheet" href="{css_toolbar}">
  <script src="{js_init}" defer></script>
""".format(
        title=esc(title), description=esc(description), canonical=esc(canonical), up=up,
        keywords=esc(", ".join(keywords)), today=TODAY, tag_meta=tag_meta,
        css_theme=asset(up, "site-theme.css"), css_lumen=asset(up, "lumen.css"),
        css_pages=asset(up, "site-pages.css"), css_toolbar=asset(up, "site-toolbar.css"),
        js_init=asset(up, "site-init.js"),
    )


def foot(up: str, extra_script: str = "") -> str:
    return (
        '<div id="footer-root"></div><div id="support-toolbar-slot"></div>\n'
        + extra_script
        + '<script src="%s" defer></script>\n' % asset(up, "nav.js")
        + '<script src="%s" defer></script>\n' % asset(up, "site-i18n.js")
        + '<script src="%s" defer></script>\n' % asset(up, "site-locale.js")
        + "</body>\n</html>\n"
    )


def article_ld(title, description, canonical, keywords) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": title,
        "description": description,
        "image": SITE + "/assets/og-image.png",
        "dateModified": TODAY,
        "inLanguage": "en",
        "keywords": ", ".join(keywords),
        "author": {"@type": "Organization", "name": "Innioasis Community"},
        "publisher": {"@type": "Organization", "name": "Innioasis Updater"},
        "mainEntityOfPage": canonical,
        "about": [{"@type": "Product", "name": "Innioasis Y1"}, {"@type": "SoftwareApplication", "name": "Rockbox-Y1"}],
    }


def howto_ld(title, description, steps, tools) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": title,
        "description": description,
        "tool": [{"@type": "HowToTool", "name": tool} for tool in tools],
        "step": [{"@type": "HowToStep", "position": i + 1, "text": _plain(step)} for i, step in enumerate(steps)],
    }


def _plain(text: str) -> str:
    import re
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def button(text, href, primary=False, attrs="") -> str:
    return '<a class="lumen-button%s" href="%s"%s>%s</a>' % (
        " lumen-button--primary" if primary else "", esc(href), attrs, text)


def actions(*buttons) -> str:
    return '<div class="lumen-actions">%s</div>' % "".join(buttons)


def proxied(asset_name: str, filename: str) -> str:
    return "/download-proxy?" + urllib.parse.urlencode({"url": THEMES_RELEASE + asset_name, "filename": filename})


def download_button(text, asset_name, filename, theme_id, primary=False) -> str:
    attrs = (
        ' data-download-what="theme" data-download-software="Rockbox" data-download-model="Y1"'
        ' data-download-brand="Innioasis" data-download-resolution="360p"'
        ' data-download-id="%s" data-download-version="%s" data-download-file="%s"'
        ' data-download-method="site" data-asset-url="%s" download="%s"'
        % (esc(theme_id), esc(THEMES_RELEASE_TAG), esc(filename), esc(THEMES_RELEASE + asset_name), esc(filename))
    )
    return button(text, proxied(asset_name, filename), primary, attrs)


def fonts_button(primary=False) -> str:
    attrs = (
        ' data-download-what="theme" data-download-software="Rockbox" data-download-model="Y1"'
        ' data-download-brand="Innioasis" data-download-id="rockbox-fonts" data-download-version="4.0"'
        ' data-download-file="rockbox-fonts-4.0.zip" data-download-method="site"'
    )
    return button("Rockbox fonts 4.0", FONTS_URL, primary, attrs)


#: The download proxy streams the release under our own address. If it does
#: not answer, the button falls back to the asset itself, so it still works.
PROXY_FALLBACK = """<script>
(function () {
  var links = document.querySelectorAll("a[data-asset-url]");
  if (!links.length || !window.fetch) return;
  fetch(links[0].getAttribute("href"), { method: "HEAD", cache: "no-store" })
    .then(function (res) { if (!res.ok) throw new Error(String(res.status)); })
    .catch(function () {
      Array.prototype.forEach.call(links, function (link) {
        link.setAttribute("href", link.getAttribute("data-asset-url"));
        link.setAttribute("data-download-method", "direct");
      });
    });
})();
</script>
"""

WRITTEN: list[tuple[str, str]] = []


def write(path: pathlib.Path, document: str, canonical: str, priority: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding="utf-8")
    WRITTEN.append((canonical, priority))


def page(path, canonical, up, title, description, keywords, tags, crumbs, main, ld_extra=(), priority="0.7",
         extra_script="") -> None:
    blocks = [article_ld(title, description, canonical, keywords), breadcrumb_ld(crumbs)] + list(ld_extra)
    document = (
        head(title, description, canonical, up, keywords, tags)
        + jsonld(blocks)
        + '\n</head>\n<body class="site-themes-app">\n<a class="lumen-skip-link" href="#main">Skip to content</a>\n'
        + '<div id="nav-root"></div>\n<main id="main" class="lumen-guide">'
        + main
        + "</main>\n"
        + foot(up, extra_script)
    )
    write(path, document, canonical, priority)


def header_block(back_href, back_text, kicker, h1, lead, buttons="") -> str:
    return (
        '<p class="lumen-doc-back"><a href="%s">← %s</a></p>'
        '<header><p class="lumen-kicker">%s</p><h1>%s</h1><p class="lead">%s</p>%s</header>'
        % (esc(back_href), back_text, kicker, h1, lead, buttons)
    )


# ---------------------------------------------------------------- tutorials

def tutorial_url(slug: str, os_key: str) -> str:
    return "%s-%s.html" % (slug, os_key)


def os_switch(slug: str, current: str) -> str:
    links = []
    for key in OS_ORDER:
        label = OS_INFO[key]["label"]
        if key == current:
            links.append('<strong aria-current="page">%s</strong>' % label)
        else:
            links.append('<a href="%s">%s</a>' % (tutorial_url(slug, key), label))
    return '<p class="lumen-meta">Using another computer? %s</p>' % " · ".join(links)


def connect_steps(os_key: str) -> list[str]:
    where = {
        "macos": "It shows up in the Finder sidebar under <strong>Locations</strong>.",
        "windows": "It shows up in File Explorer under <strong>This PC</strong> as a new drive.",
        "linux": "It mounts like any USB drive, usually under <code>/media/&lt;you&gt;/</code> or <code>/run/media/&lt;you&gt;/</code>.",
    }[os_key]
    return [
        "Start Rockbox on the Y1 once before you begin. Rockbox makes its <code>.rockbox</code> folder on the first start.",
        "Plug the Y1 into your computer with a USB data cable. When the player asks, choose <strong>USB Storage Mode</strong>. " + where,
    ]


def reveal_steps(os_key: str) -> list[str]:
    if os_key == "macos":
        return [
            "Open the Y1 in Finder.",
            "Press <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd> (the full stop key). Hidden items appear dimmed, and <code>.rockbox</code> is one of them.",
            "Open <code>.rockbox</code>. Press the same keys again later to hide hidden items.",
        ]
    if os_key == "windows":
        return [
            "Open the Y1's drive in File Explorer. Windows usually shows <code>.rockbox</code> straight away: a leading dot doesn't hide a folder on Windows.",
            "Can't see it? On Windows 11 choose <strong>View → Show → Hidden items</strong>. On Windows 10 open the <strong>View</strong> tab and tick <strong>Hidden items</strong>.",
            "Open <code>.rockbox</code>.",
        ]
    return [
        "Open the Y1's drive in your file manager.",
        "Press <kbd>Ctrl</kbd>+<kbd>H</kbd> to show hidden files in GNOME Files (Nautilus), Nemo and Thunar. In KDE Dolphin it's <kbd>Alt</kbd>+<kbd>.</kbd> or <kbd>Ctrl</kbd>+<kbd>H</kbd>.",
        "Open <code>.rockbox</code>. In a terminal, <code>ls -a</code> lists it too.",
    ]


def merge_steps(os_key: str) -> list[str]:
    if os_key == "macos":
        return [
            "Open the theme's own <code>.rockbox</code> folder on your Mac. It's hidden too, so keep <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd> on.",
            "Select everything inside it (<kbd>Cmd</kbd>+<kbd>A</kbd>).",
            "Hold <kbd>Option</kbd> and drag the selection into the Y1's <code>.rockbox</code> folder. When Finder asks about a folder that already exists, choose <strong>Merge</strong>, and choose <strong>Replace</strong> for single files.",
            "Never choose <strong>Replace</strong> for a whole folder such as <code>wps</code> or <code>themes</code>: in Finder that removes everything already in it. If <strong>Merge</strong> isn't offered, open that folder on both sides and copy its contents across instead.",
        ]
    if os_key == "windows":
        return [
            "Open the theme's own <code>.rockbox</code> folder.",
            "Select everything inside it (<kbd>Ctrl</kbd>+<kbd>A</kbd>) and copy it (<kbd>Ctrl</kbd>+<kbd>C</kbd>).",
            "Open the Y1's <code>.rockbox</code> folder and paste (<kbd>Ctrl</kbd>+<kbd>V</kbd>). File Explorer merges folders with the same name on its own.",
            "When it asks about files that already exist, choose <strong>Replace the files in the destination</strong>.",
        ]
    return [
        "Open the theme's own <code>.rockbox</code> folder. Keep hidden files showing.",
        "Select everything inside it and copy it into the Y1's <code>.rockbox</code> folder.",
        "GNOME Files asks to <strong>Merge</strong> folders that already exist: choose it, then <strong>Replace</strong> for files. In Dolphin the folder button is <strong>Write Into</strong>, then <strong>Overwrite</strong> for files.",
        "Prefer a terminal? <code>cp -r ~/Downloads/THEME/.rockbox/. /media/$USER/Y1/.rockbox/</code> merges and overwrites in one go. Use your own paths.",
    ]


def eject_step(os_key: str) -> str:
    return {
        "macos": "Click the eject button next to the Y1 in the Finder sidebar, wait for it to disappear, then unplug.",
        "windows": "Right-click the Y1's drive in File Explorer, choose <strong>Eject</strong>, then unplug.",
        "linux": "Click the eject icon next to the Y1 in your file manager, wait for it to finish, then unplug.",
    }[os_key]


def hidden_folder_page(os_key: str) -> None:
    info = OS_INFO[os_key]
    label = info["label"]
    slug = "show-hidden-rockbox-folder"
    title = "Find the hidden .rockbox folder on your Y1 from %s" % label
    description = (
        "Rockbox keeps themes, fonts and settings in a hidden .rockbox folder. Here's how to connect your "
        "Innioasis Y1 in USB Storage Mode and show that folder in %s on %s." % (info["files"], label)
    )
    steps = connect_steps(os_key) + reveal_steps(os_key)
    notes = []
    if os_key == "macos":
        notes.append(
            "macOS leaves small files whose names start with <code>._</code> on the player. They're "
            "harmless, and Rockbox doesn't need them.")
    if os_key == "linux":
        notes.append(
            "If the drive doesn't mount on its own, open your file manager and click it in the "
            "sidebar. It mounts on first click.")
    body = section("Show .rockbox, step by step", ol(steps))
    body += section("What's inside", ul([
        "<code>themes</code>: the small <code>.cfg</code> file that names each theme.",
        "<code>wps</code>, <code>backdrops</code>, <code>icons</code>, <code>fonts</code>: the parts a theme is made of.",
        "Your settings, playlists and the music database also live here, so copy into it rather than replacing it.",
    ]) + (p(*notes) if notes else ""))
    body += section("When you're done", p(eject_step(os_key)))
    faqs = [
        ("I can't see .rockbox at all, even with hidden items on.",
         "Start Rockbox on the Y1 once, then connect again. The folder only exists after Rockbox has started."),
        ("Can I delete .rockbox?",
         "Yes, if you want a clean start. Rockbox makes a new one with default settings on the next start, and "
         "the Rockbox-Y1 0.5 release notes suggest it as a fix for odd path problems. Your themes and settings go with it."),
    ]
    body += faq_block(faqs)
    body += related(slug, os_key)
    keywords = BASE_KEYWORDS + ["show hidden files %s" % label, "%s hidden folder" % info["files"],
                                ".rockbox %s" % label, "Rockbox USB Storage Mode %s" % label]
    main = header_block("index.html", "Rockbox tutorials", "Rockbox-Y1 · %s" % label, esc(title),
                        esc(description)) + os_switch(slug, os_key) + body
    canonical = "%s/%s/%s" % (SITE, TUTORIAL_DIR, tutorial_url(slug, os_key))
    page(ROOT / TUTORIAL_DIR / tutorial_url(slug, os_key), canonical, "../", title, description, keywords,
         ["Rockbox", "Innioasis Y1", label, ".rockbox"],
         [("Home", SITE + "/"), ("Rockbox tutorials", "%s/%s/" % (SITE, TUTORIAL_DIR)), (title, canonical)],
         main, [howto_ld(title, description, steps, [info["files"], "USB data cable"]), faq_ld(faqs)])


def install_themes_page(os_key: str) -> None:
    info = OS_INFO[os_key]
    label = info["label"]
    slug = "install-rockbox-y1-themes"
    title = "Install Rockbox-Y1 360p themes by hand on %s" % label
    description = (
        "Copy the 360p Rockbox-Y1 themes onto an Innioasis Y1 from %s: download the theme pack, unzip it, "
        "merge its .rockbox folder into the player's, then pick a theme. Works on Rockbox-Y1 0.5 or later." % label
    )
    steps = [
        "Download the theme pack below. It holds every theme as one merged <code>.rockbox</code> folder. "
        "The individual themes download has each theme in its own folder, each with its own <code>.rockbox</code> inside.",
        info["unzip"],
    ] + connect_steps(os_key) + [
        "Show hidden items and open the Y1's <code>.rockbox</code> folder (<a href=\"%s\">how to show it on %s</a>)."
        % (tutorial_url("show-hidden-rockbox-folder", os_key), label),
    ] + merge_steps(os_key) + [
        eject_step(os_key),
        "On the Y1, open <strong>Settings → Theme Settings → Browse Theme Files</strong> and pick a theme.",
    ]
    body = section("Faster: let Updater CE do it", p(
        "Updater CE 2.5 or later installs every 360p Rockbox-Y1 theme for you during a Rockbox-Y1 install. "
        "Already on Rockbox? Open Updater CE and choose <strong>Settings → Install Rockbox 360p Themes</strong>, "
        "or press <kbd>%s</kbd>+<kbd>T</kbd>." % ("Cmd" if os_key == "macos" else "Ctrl")
    ) + actions(button("Get Updater CE", "../guide.html", True), button("All Rockbox-Y1 theme options", "../rockbox-y1-themes.html")))
    body += section("Before you start", ul([
        "Rockbox-Y1 0.5 or later on any Y1. These are 360p themes; 0.5 and later is 360p only.",
        "A USB data cable. Charge-only cables don't show the player as a drive.",
        "About 400&nbsp;MB free on your computer for the theme pack and its unzipped copy.",
    ]))
    body += section("Download", actions(
        download_button("Theme pack (360p)", "themepack.zip", "rockbox-y1-360p-themepack.zip", "themepack", True),
        download_button("Individual themes (360p)", "themes_individual.zip", "rockbox-y1-360p-themes-individual.zip", "themes_individual"),
        fonts_button(),
    ) + p("Text looks wrong or missing after picking a theme? Unzip the Rockbox fonts pack and merge its "
          "<code>.rockbox</code> folder in the same way."))
    body += section("Install, step by step", ol(steps), "steps")
    body += section("On a Y2", p(
        "The same 360p files can be copied by hand onto a Y2 running Rockbox-Y2: merge them into the "
        "<code>.rockbox</code> folder Rockbox-Y2 made on the player. Rockbox-Y2 is a separate port, so read the "
        "release notes for your version first. Updater CE's automatic theme install is for Rockbox-Y1."
    ) + actions(button("Rockbox-Y2 hub", "../rockbox-y2/")))
    faqs = [
        ("A theme I used before 0.5 no longer works.",
         "Rockbox-Y1 0.5 moved its files. The release notes say to change paths inside old theme files from "
         "<code>/.rockbox</code> to <code>/sdcard/.rockbox</code>. The themes in this pack are already updated."),
        ("Can I use 240p themes?",
         "Not on Rockbox-Y1 0.5 or later, which is 360p only. 240p themes need a 240p build: " + WARNING_240P),
        ("Will this delete my settings?",
         "No, as long as you merge. Replacing the whole <code>.rockbox</code> folder would."),
    ]
    body += faq_block(faqs)
    body += related(slug, os_key)
    keywords = BASE_KEYWORDS + ["install Rockbox themes %s" % label, "Rockbox theme merge %s" % info["files"],
                                "themepack.zip", "themes_individual.zip"] + THEME_AUTHORS[:12]
    main = header_block("index.html", "Rockbox tutorials", "Rockbox-Y1 · %s" % label, esc(title),
                        esc(description)) + os_switch(slug, os_key) + body
    canonical = "%s/%s/%s" % (SITE, TUTORIAL_DIR, tutorial_url(slug, os_key))
    page(ROOT / TUTORIAL_DIR / tutorial_url(slug, os_key), canonical, "../", title, description, keywords,
         ["Rockbox", "Rockbox-Y1", "themes", "360p", label],
         [("Home", SITE + "/"), ("Rockbox tutorials", "%s/%s/" % (SITE, TUTORIAL_DIR)), (title, canonical)],
         main, [howto_ld(title, description, steps, [info["files"], "Innioasis Y1", "USB data cable"]), faq_ld(faqs)],
         priority="0.75", extra_script=PROXY_FALLBACK)


def pictureflow_page(os_key: str) -> None:
    info = OS_INFO[os_key]
    label = info["label"]
    slug = "pictureflow-album-art"
    if os_key == "windows":
        tool = "Mp3tag"
        title = "Add album art for Rockbox PictureFlow with Mp3tag on Windows"
        art_steps = [
            "Install Mp3tag for Windows from <a href=\"https://www.mp3tag.de/en/\" rel=\"noopener\">mp3tag.de</a>.",
            "Choose <strong>File → Change Directory</strong> and open one album's folder.",
            "Select every track of that album (<kbd>Ctrl</kbd>+<kbd>A</kbd>).",
            "In the Tag Panel on the left, right-click the cover box and choose <strong>Add cover</strong>, then pick the image. Dragging the image onto the box works too.",
            "Save with <kbd>Ctrl</kbd>+<kbd>S</kbd>. The cover is now inside every selected file.",
        ]
    elif os_key == "macos":
        tool = "Mp3tag"
        title = "Add album art for Rockbox PictureFlow with Mp3tag on macOS"
        art_steps = [
            "Get Mp3tag for Mac from the Mac App Store.",
            "Drag one album's folder onto the Mp3tag window.",
            "Select every track of that album (<kbd>Cmd</kbd>+<kbd>A</kbd>).",
            "Drag the cover image onto the artwork box in the editor panel.",
            "Save with <kbd>Cmd</kbd>+<kbd>S</kbd>. The cover is now inside every selected file.",
        ]
    else:
        tool = "a cover.jpg file"
        title = "Add album art for Rockbox PictureFlow on Linux"
        art_steps = [
            "Mp3tag has no Linux version, and you don't need one: Rockbox also reads a <code>cover.jpg</code> file in the album's folder.",
            "Save the album's cover as <code>cover.jpg</code> in the same folder as its tracks.",
            "Repeat for each album. A file manager or <code>cp</code> is all it takes.",
            "Prefer art inside the files? Tag editors packaged for Linux, such as Kid3, can embed a cover too.",
        ]
    description = (
        "Make PictureFlow on your Innioasis Y1 show every album cover: add the art with %s on %s, copy the "
        "music across, then let Rockbox build its database and PictureFlow cache." % (tool, label)
    )
    player_steps = connect_steps(os_key) + [
        "Copy your albums to the player in %s." % info["files"],
        eject_step(os_key),
        "On the Y1, open <strong>Settings → General Settings → Database</strong> and choose <strong>Initialize Now</strong>.",
        "Open <strong>Plugins → Demos → PictureFlow</strong>. The first start builds its cover cache, which takes a while with a big library.",
    ]
    body = section("Get the art right first", ul([
        "Use a square JPEG. Rockbox doesn't show progressive JPEGs; if a cover stays blank, re-save it as a standard JPEG.",
        "Big images aren't sharper on a 480×360 screen; they just make the cache slower to build. 500×500 is plenty.",
        "One cover per album: PictureFlow groups by the album tag, so tracks with matching album and artist tags stay together.",
    ]))
    body += section("Add the covers with %s" % tool, ol(art_steps), "art")
    body += section("Put them on the Y1", ol(player_steps), "player")
    faqs = [
        ("New albums don't show up in PictureFlow.",
         "Update the database again, then rebuild PictureFlow's cache from its own settings menu."),
        ("Some covers are blank.",
         "Check the image is a standard (baseline) JPEG and that every track of the album carries the same album tag."),
    ]
    body += faq_block(faqs)
    body += related(slug, os_key)
    keywords = BASE_KEYWORDS + ["PictureFlow album art", "Rockbox cover art", "Mp3tag Rockbox", "Mp3tag %s" % label,
                                "cover.jpg Rockbox", "embedded album art Rockbox", "Rockbox database Initialize Now"]
    main = header_block("index.html", "Rockbox tutorials", "Rockbox-Y1 · PictureFlow · %s" % label, esc(title),
                        esc(description)) + os_switch(slug, os_key) + body
    canonical = "%s/%s/%s" % (SITE, TUTORIAL_DIR, tutorial_url(slug, os_key))
    page(ROOT / TUTORIAL_DIR / tutorial_url(slug, os_key), canonical, "../", title, description, keywords,
         ["Rockbox", "PictureFlow", "album art", "Mp3tag" if os_key != "linux" else "cover.jpg", label],
         [("Home", SITE + "/"), ("Rockbox tutorials", "%s/%s/" % (SITE, TUTORIAL_DIR)), (title, canonical)],
         main, [howto_ld(title, description, art_steps + player_steps, [tool, "Innioasis Y1"]), faq_ld(faqs)])


TOPICS = [
    ("install-rockbox-y1-themes", "Install 360p themes by hand",
     "Download the theme pack, unzip it and merge it into the player."),
    ("show-hidden-rockbox-folder", "Find the hidden .rockbox folder",
     "Connect in USB Storage Mode and show hidden items."),
    ("pictureflow-album-art", "Album art for PictureFlow",
     "Add covers with Mp3tag, or a cover.jpg on Linux."),
]


def related(current_slug: str, os_key: str) -> str:
    cards = []
    for slug, name, _blurb in TOPICS:
        if slug == current_slug:
            continue
        cards.append('<article class="lumen-card"><h3><a href="%s">%s</a></h3><p class="lumen-meta">%s</p></article>'
                     % (tutorial_url(slug, os_key), esc(name), OS_INFO[os_key]["label"]))
    cards.append('<article class="lumen-card"><h3><a href="../rockbox-y1-themes.html">Rockbox-Y1 themes</a></h3></article>')
    cards.append('<article class="lumen-card"><h3><a href="../rockbox-y1/">Rockbox-Y1 hub</a></h3></article>')
    return '<section class="lumen-guide-section"><h2>More Rockbox tutorials</h2><div class="lumen-grid">%s</div></section>' % "".join(cards)


def hub_page() -> None:
    title = "Rockbox tutorials for the Innioasis Y1 and Y2"
    description = (
        "Short, practical Rockbox tutorials for the Innioasis Y1 and Y2 on macOS, Windows and Linux: install "
        "360p themes, find the hidden .rockbox folder, and add album art for PictureFlow."
    )
    rows = []
    for slug, name, blurb in TOPICS:
        cells = "".join('<td><a href="%s">%s</a></td>' % (tutorial_url(slug, key), OS_INFO[key]["label"]) for key in OS_ORDER)
        rows.append("<tr><th scope=\"row\">%s<br><span class=\"lumen-meta\">%s</span></th>%s</tr>" % (esc(name), esc(blurb), cells))
    table = (
        '<div class="lumen-table-wrap"><table class="lumen-doc-table"><thead><tr><th scope="col">Tutorial</th>'
        + "".join('<th scope="col">%s</th>' % OS_INFO[key]["label"] for key in OS_ORDER)
        + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>"
    )
    body = section("Pick a tutorial and your computer", table)
    body += section("Start here", ul([
        "New to Rockbox on the Y1? The <a href=\"../rockbox-y1/install.html\">install guide</a> walks through Updater CE.",
        "Want the themes without the steps? Updater CE 2.5 or later installs every 360p Rockbox-Y1 theme during the install.",
        "On a Y2? Rockbox-Y2 is its own port. The <a href=\"../rockbox-y2/\">Rockbox-Y2 hub</a> has its downloads and notes.",
    ]))
    body += section("Other firmware for the Y1 and Y2", p(
        "Rockbox isn't the only option. The <a href=\"../firmware.html?view=firmware\">firmware archive</a> lists "
        "every project with a released build, including Solar, Rondo, Koensayr, Better-Y, Inniclassic, "
        "JJ Launcher, Y2Player and Reborn (Y2Linux)."
    ))
    keywords = BASE_KEYWORDS + FIRMWARE_KEYWORDS + ["Rockbox tutorial macOS", "Rockbox tutorial Windows", "Rockbox tutorial Linux"]
    main = header_block("../rockbox-benefits.html", "Rockbox on Innioasis", "Rockbox · tutorials", esc(title), esc(description),
                        actions(button("Rockbox-Y1 themes", "../rockbox-y1-themes.html", True), button("Rockbox-Y1 hub", "../rockbox-y1/"))) + body
    canonical = "%s/%s/" % (SITE, TUTORIAL_DIR)
    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": "%s/%s/%s" % (SITE, TUTORIAL_DIR, tutorial_url(slug, key))}
            for i, (slug, key) in enumerate((s, k) for s, _n, _b in TOPICS for k in OS_ORDER)
        ],
    }
    page(ROOT / TUTORIAL_DIR / "index.html", canonical, "../", title, description, keywords,
         ["Rockbox", "tutorials", "macOS", "Windows", "Linux"],
         [("Home", SITE + "/"), ("Rockbox tutorials", canonical)], main, [item_list], priority="0.8")


# ---------------------------------------------------------------- themes page

def themes_page() -> None:
    title = "Rockbox-Y1 themes: install with Updater CE or by hand"
    description = (
        "Rockbox-Y1 themes for the Innioasis Y1. Updater CE 2.5 or later installs every 360p theme during a "
        "Rockbox-Y1 install. You can also download the 360p theme pack here, or get 240p themes from rockbox.org."
    )
    credits = "".join(
        "<tr><th scope=\"row\" translate=\"no\">%s</th><td translate=\"no\">%s</td><td translate=\"no\">%s</td></tr>"
        % (esc(name), esc(author), esc(port or "—")) for name, author, port in THEMES)
    tutorial_links = " · ".join(
        '<a href="%s/%s">%s</a>' % (TUTORIAL_DIR, tutorial_url("install-rockbox-y1-themes", key), OS_INFO[key]["label"])
        for key in OS_ORDER)
    hidden_links = " · ".join(
        '<a href="%s/%s">%s</a>' % (TUTORIAL_DIR, tutorial_url("show-hidden-rockbox-folder", key), OS_INFO[key]["label"])
        for key in OS_ORDER)
    body = section("Recommended: let Updater CE install them", p(
        "Installing Rockbox-Y1 with Updater CE 2.5 or later? It installs every 360p Rockbox-Y1 theme for you "
        "during the install. There's nothing to download or unzip.",
        "Already on Rockbox? Open Updater CE and choose <strong>Settings → Install Rockbox 360p Themes</strong>, "
        "or press <kbd>Cmd</kbd>+<kbd>T</kbd> on a Mac and <kbd>Ctrl</kbd>+<kbd>T</kbd> on Windows and Linux. "
        "If it can't reach the player on its own, it walks you through USB Storage Mode."
    ) + actions(button("Get Updater CE", "guide.html", True), button("Install Rockbox-Y1", "rockbox-y1/install.html")), "updater-ce")
    body += section("360p themes, by hand", p(
        "Recommended if you're copying themes yourself. They work on Rockbox-Y1 0.5 or later on every Y1, "
        "and you can copy them onto a Y2 by hand too.",
        "The theme pack is every theme merged into one <code>.rockbox</code> folder. The individual download "
        "has each theme in its own folder. Either way, you merge a <code>.rockbox</code> folder into the "
        "player's: copy what's inside, merge folders, and replace files that already exist."
    ) + actions(
        download_button("Theme pack (360p) · 90 MB", "themepack.zip", "rockbox-y1-360p-themepack.zip", "themepack", True),
        download_button("Individual themes (360p) · 294 MB", "themes_individual.zip", "rockbox-y1-360p-themes-individual.zip", "themes_individual"),
        fonts_button(),
    ) + p("Step-by-step: %s. Can't see <code>.rockbox</code>? %s." % (tutorial_links, hidden_links)), "360p")
    body += section("240p themes", p(
        "240p themes are the Rockbox iPod classic themes on rockbox.org. Download one there and copy it into "
        "<code>.rockbox</code> by hand, the same way. They need a 240p Rockbox-Y1 build, and those ended at 0.4."
    ) + '<div class="lumen-warning" role="note"><strong>Check your Y1 first</strong><p style="margin: 0.35rem 0 0;">%s</p></div>' % esc(WARNING_240P)
      + actions(button("iPod classic themes on rockbox.org", IPOD_CLASSIC_THEMES, False,
                       ' rel="noopener" data-download-what="theme" data-download-software="Rockbox" data-download-model="Y1"'
                       ' data-download-brand="Innioasis" data-download-resolution="240p" data-download-id="rockbox-ipod6g"'
                       ' data-download-method="rockbox.org"')), "240p")
    body += section("Pick a theme on the player", ol([
        "Unplug the Y1 once the files are on it.",
        "Open <strong>Settings → Theme Settings → Browse Theme Files</strong>.",
        "Choose a theme. It applies straight away.",
    ]))
    body += section("Themes in the 360p pack", p(
        "Ported to the Y1 by the rockbox-y1 project and the community. Thank the original authors if you "
        "enjoy their work: Dook (Themify, Adwaitapod), yuuiko (FreshOS) and CarlosPixel_ (Snowoasis_Y1) take donations."
    ) + '<div class="lumen-table-wrap"><table class="lumen-doc-table"><thead><tr><th scope="col">Theme</th>'
        '<th scope="col">Original author</th><th scope="col">Ported by</th></tr></thead><tbody>%s</tbody></table></div>' % credits,
        "credits")
    faqs = [
        ("Which Rockbox-Y1 version do 360p themes need?",
         "Rockbox-Y1 0.5 or later. Every release from 0.5 on is 360p only."),
        ("Do I need to unzip anything if I use Updater CE?",
         "No. Updater CE 2.5 or later installs every 360p theme during a Rockbox-Y1 install."),
        ("Can I use 240p themes on my Y1?",
         "Only with a 240p build, and those ended at 0.4. " + WARNING_240P),
        ("Do these themes work on a Y2?",
         "You can copy the 360p files onto a Y2 running Rockbox-Y2 by hand. Rockbox-Y2 is a separate port, so check its release notes."),
    ]
    body += faq_block(faqs)
    keywords = BASE_KEYWORDS + ["themepack.zip", "themes_individual.zip", "Rockbox-Y1 360p Theme Pack"] + [t[0] for t in THEMES] + THEME_AUTHORS
    main = header_block("rockbox-y1/", "Rockbox-Y1 hub", "Rockbox-Y1 · themes", "Rockbox-Y1 themes",
                        "Change how Rockbox looks on your Y1. The quickest way is to let Updater CE install the themes "
                        "for you. You can also copy them over yourself.",
                        actions(button("Theme pack (360p)", proxied("themepack.zip", "rockbox-y1-360p-themepack.zip"), True,
                                       ' data-download-what="theme" data-download-software="Rockbox" data-download-model="Y1"'
                                       ' data-download-brand="Innioasis" data-download-resolution="360p" data-download-id="themepack"'
                                       ' data-download-version="%s" data-download-file="rockbox-y1-360p-themepack.zip"'
                                       ' data-download-method="site" data-asset-url="%s" download="rockbox-y1-360p-themepack.zip"'
                                       % (esc(THEMES_RELEASE_TAG), esc(THEMES_RELEASE + "themepack.zip"))),
                                button("Rockbox tutorials", "%s/" % TUTORIAL_DIR),
                                button("Community themes gallery", "https://themes.innioasis.app/")))
    main += body
    canonical = SITE + "/rockbox-y1-themes.html"
    page(ROOT / "rockbox-y1-themes.html", canonical, "", title, description, keywords,
         ["Rockbox", "Rockbox-Y1", "themes", "360p", "240p", "Updater CE"],
         [("Home", SITE + "/"), ("Firmware Downloads", SITE + "/firmware.html"),
          ("Rockbox-Y1", SITE + "/rockbox-y1/"), ("Rockbox-Y1 themes", canonical)],
         main, [faq_ld(faqs)], priority="0.8", extra_script=PROXY_FALLBACK)


# ---------------------------------------------------------------- sitemap

def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    added = 0
    for loc, priority in WRITTEN:
        if "<loc>%s</loc>" % loc in text:
            continue
        text = text.replace(
            "</urlset>",
            '  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq>'
            "<priority>%s</priority></url>\n</urlset>" % (esc(loc), TODAY, priority),
        )
        added += 1
    if added:
        path.write_text(text, encoding="utf-8")
    print("sitemap: %d new URLs" % added)


def main() -> int:
    themes_page()
    hub_page()
    for os_key in OS_ORDER:
        install_themes_page(os_key)
        hidden_folder_page(os_key)
        pictureflow_page(os_key)
    update_sitemap()
    print(json.dumps([loc for loc, _ in WRITTEN], indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
