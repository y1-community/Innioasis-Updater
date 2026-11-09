---
title: "Y2Linux 1.0 Beta 6.2 (Baseline 59) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 6.2 Baseline 59 Status: PUBLISHED as GitHub release baseline-59 2026-10-16. Release 1.0.0-beta.6.2 , Reborn 1.0.0-beta.6.2 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-6.2.html"
---

# Y2Linux 1.0 Beta 6.2 (Baseline 59) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 6.2 (Baseline 59)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 6.2 (Baseline 59)

Status: PUBLISHED as GitHub release `baseline-59` (2026-10-16). Release `1.0.0-beta.6.2`, Reborn `1.0.0-beta.6.2`, kernel `6.18.56-y2linux-1.0.0-beta.6.2`, update sequence 5700, Linux `8e07f47`, Reborn `f0f1091`, git tag `baseline-59` in both repositories. Built with `tools/production/release.py` (`--public`) in 125 s: container suite 740 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-6.2 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 2ee211b267169e502ef09ed82da71d76ef2402c1b58d12007ba8c057d2c74b4a |
| Y2ROOT | d6ad7e339f5fe2abaaf5530af9226beeb1365e23bc45c48c64ff85d1c1284284 |
| RECOVERY | eaf77c7fd8effa2dfeb28f4327719bf429ed08d8c494743dd1e65a1ff1a7922a |
| Y2DATA (no SSH key) | 290732bb65151486350fd3a3b55370421266c12b05295fdbd494965c3f4c207b |

## Since Beta 6.1 (Reborn)

Owner (2026-10-16): "do pull request 10 and add a clock in a nice way fitting for all skins"; "check that this is optimized and does not intruce do much drain or redraws"; "update all the other skins for the ui work we did today"; a skin "modelled after" the Rockbox theme bunnyPod, "cute / hello kitty style"; "yes publish".````````````````````

| Part | Detail |
| --- | --- |
| Clock (PR #10, samanz) | Status-bar time in a chosen zone (Settings → Display → Time Zone; built-in POSIX TZ rules, no zone database on the image; hidden until the clock is set). Reviewed: DST and unusual rules checked. |
| Clock in skins | Skins draw their own title bars, so the clock showed only in Reborn's own look. New skin value {clock} and condition has_clock; every shipped skin places it in its own style. |
| Cost | Clock text made once per minute and zone (host: 337 → 16 ns per call), picker zones once per minute (167 → 25 µs per frame). No new wakeups; one redraw per minute with the screen on, none with it off. |
| Today's screens in skins | Radio Now Playing (song/artist as announced, LIVE, full bar, logo or initials, no "1 of 1"), Station Info facts (station_facts), station logos in rows, a keyboard overlay layout under each skin's title bar, a favorite condition and heart icon, layout names for search/playlists/radio. Reborn's own look: 110 of 110 previews pixel-identical. |
| Bunny Bow | New skin: pastel pixel art (bunny with a red bow, cloud clock, sparkles, hearts, pill bars), all drawn by tools/assets/build_skins.py; inspired by bunnyPod (CC-BY-SA), none of its art or its font copied. Font Pixelify Sans (OFL 1.1; sources and hashes in Y2Reborn assets/fonts/pixelify, licence in legal-info via reborn.mk). |
| Skin generator | The clock/radio/keyboard/heart changes are finishing steps of build_skins.py, which reproduces all 14 generated skins byte for byte. |

Host evidence: 474 Reborn tests (new: every shipped skin loads without warnings with clock, keyboard layout and no queue position for a station; time zone picker and clock), strict Clippy, fmt; preview renders of all 16 skins; 767 Y2Linux host tests.

## Device checks owed (after the owner's over-the-air install)

Time Zone picker and the clock in Reborn's look and in skins; Bunny Bow on every main screen; radio Now Playing and Station Info in a skin; the keyboard in a skin; the Favorites heart; skin load time of Bunny Bow; plus the Beta 6.1 checks (AirPods sound after pause, skipping while a song starts).

## Known gaps

FM radio (next beta); no 12/24-hour switch (the zone decides); in-place decoder seek (≈1 s on Bluetooth); sleep ≈9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
