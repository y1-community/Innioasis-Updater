---
title: "Y2Linux 1.0 Beta 4 (Baseline 53) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 4 Baseline 53 Status: PUBLISHED as GitHub release baseline-53 2026-10-15. Release 1.0.0-beta.4 , Reborn 1.0.0-beta.4 , kernel 6.18.56-y2linux-1.0.0-beta."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-4.html"
---

# Y2Linux 1.0 Beta 4 (Baseline 53) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 4 (Baseline 53)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 4 (Baseline 53)

Status: PUBLISHED as GitHub release `baseline-53` (2026-10-15). Release `1.0.0-beta.4`, Reborn `1.0.0-beta.4`, kernel `6.18.56-y2linux-1.0.0-beta.4`, update sequence 5300, Linux `d681990`, Reborn `94eae20`, git tag `baseline-53` in both repositories. Built with `tools/production/release.py` (`--public`) in 135 s: container suite 739 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-4 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 0964208b77cdcb09e07736df93214b6289dd20aecd63f7c3affdc3c4795ddf60 |
| Y2ROOT | cc2a44ece891b1c29b184cbc2f9525c18d0f928a766ae521c7a2f97d197afffc |
| RECOVERY | a4ad836472979afe7a8a32c83af3976c83b7f865287d9386a090a9dda64d82cf |
| Y2DATA (no SSH key) | b5ac22909e92d373c5351051eac0d04fcb7ce3e2369789679040323c3591b6a3 |

## Since Beta 3: internet radio (Reborn)

Owner request (2026-10-15): internet radio and FM radio for Beta 4; owner decisions: internet radio first, stations from the radio-browser.info directory plus the owner's own `.m3u`/`.pls` files; FM follows (next beta), hidden where a scan finds no station.``````````````````````

| Part | Detail |
| --- | --- |
| Screens | Home → Radio: Favorites, Popular, Countries, Genres, Search (wheel keyboard), My Stations (Radio folder on Internal Storage or the SD card). Hold Select on a station or on Now Playing: add/remove favorite. Now Playing: LIVE RADIO, the station's song (ICY StreamTitle) or connection state, listening time, LIVE. |
| Network | curl on the player (OpenSSL, CA bundle, redirects, .pls/.m3u indirection, 15-s stall limit); ICY metadata stripped in Reborn; reconnect after 1–30 s; the decoder waits up to 45 s. radio-browser mirrors via DNS; plays counted with /json/url/. |
| Decoder | Decoder::open_stream: a pipe as non-seekable FFmpeg input (rbpipe:<fd>, mp3/aac/ogg/flac). FFmpeg keeps --disable-network and its file-only protocol policy (verify-ffmpeg.py unchanged and passing). |
| Engine | Station never pre-opened for gapless playback, never seeked; storage changes never pause it; no artwork lookup. |
| Not supported | HLS/DASH-only stations (filtered out of directory lists, named when a playlist leads to one). |

Host evidence: 426 Reborn tests (17 new for radio, including a local server that drops the connection and is reconnected through the real `curl`); live, by hand: the real directory and two stations (France Info MP3, Europe 1 AAC) decoded through the playback path. On the player (Beta 3, read-only): `curl` reaches the directory over HTTPS, certificate verified.

## Device checks owed (after the owner's over-the-air install)

Home → Radio → Popular → play; song title updates; Favorites survive a restart; Search; a short Wi-Fi drop reconnects; My Stations from a `Radio` folder; CPU and battery while streaming; Bluetooth headphones while streaming (shared antenna).

## Known gaps

FM radio not yet (next beta); HLS stations; battery in sleep ≈9.4 mA vs stock ≈1.3 mA; Bluetooth range is hardware-limited (stock too); no headphone-jack detection; full install from stock run on one player only.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
