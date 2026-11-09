---
title: "Y2Linux 1.0 Beta 5.1 (Baseline 56) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 5.1 Baseline 56 Status: PUBLISHED as GitHub release baseline-56 2026-10-15. Release 1.0.0-beta.5.1 , Reborn 1.0.0-beta.5.1 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-5.1.html"
---

# Y2Linux 1.0 Beta 5.1 (Baseline 56) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 5.1 (Baseline 56)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 5.1 (Baseline 56)

Status: PUBLISHED as GitHub release `baseline-56` (2026-10-15). Release `1.0.0-beta.5.1`, Reborn `1.0.0-beta.5.1`, kernel `6.18.56-y2linux-1.0.0-beta.5.1`, update sequence 5500, Linux `e9ac2a5`, Reborn `35e333d`, git tag `baseline-56` in both repositories. Built with `tools/production/release.py` (`--public`) in 102 s: container suite 740 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-5.1 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 8409e71dffd65e5ac68837964e0427720c5a802cf4acf73d0d3f5226bad99205 |
| Y2ROOT | d643d7665c49c204903186aa3b4e7d7b65279dcf490bb60fef59238f57b6e898 |
| RECOVERY | 91f5b71b087cd4adcd52fbd0665a1cc51797de79ace46a1d182de2cf99d4fac3 |
| Y2DATA (no SSH key) | 59f8adc0ddb1ea492ce4625cc97aad80d5fde55f628c563ae12b8829e3a05dc0 |

## Since Beta 5 (Reborn)

Owner (2026-10-15): "search works great … performance pass … live search"; "rework the radio UI … premium … sort everything by alphabet … include picture and more metadata"; "top 10 radio stations for each country … on top".````````

| Part | Detail |
| --- | --- |
| Live search | Library search shows artists, albums and songs above a compact keyboard while typing; Back on the top key row enters the results, Select opens or plays, Back returns to the full results. |
| Search speed | Index folded and sorted once per library, narrowing from the previous search, cached searches for Delete. Synthetic 20 000 songs, host release build: per keystroke 6.2 → 0.05 ms mean, 7.5 → 0.42 ms worst; built when the keyboard opens. |
| Radio section | Radio home with an On Air card and category tiles; station rows with logo, details, favorite star and LIVE; Station Info; Now Playing with the logo, LIVE badge and the song as title and artist; Previous/Next between stations. |
| Station logos | Directory logos downloaded once each in the background (≤300 kB, PNG/JPEG/WebP, PNG from .ico; failures remembered three days), cached in /data/reborn/cache/radio-logos, decoded undistorted by a new native rb_media_logo_file and laid on tiles (art::logo_tile); initials tiles otherwise. Host live check: 21 of 24 popular stations. |
| Order | Lists A to Z; country, genre and popular lists keep their ten most listened stations on top, ranked. |
| Fix | Grouped numbers (Home with 1 000+ songs) used a thin space missing from the fonts. |
| Pipeline | release.py prune no longer fails in the build container (no Reborn checkout there). |

Host evidence: 446 Reborn tests (new: live search navigation, logo tiles, .ico logos, ranking, A-to-Z, song split, Station Info), strict Clippy, fmt; preview renders; real directory logos downloaded and tiled on the host.

## Device checks owed (after the owner's over-the-air install)

Logos appear in lists and on Now Playing (Wi-Fi on); a country list shows its top 10 then A to Z; Station Info; Previous/Next between stations; live search results and opening them; memory/CPU while lists with logos scroll.

## Known gaps

FM radio (next beta); HLS stations; logos in SVG/GIF show initials; sleep ≈9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
