---
title: "Y2Linux 1.0 Beta 5 (Baseline 55) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 5 Baseline 55 Status: PUBLISHED as GitHub release baseline-55 2026-10-15. Release 1.0.0-beta.5 , Reborn 1.0.0-beta.5 , kernel 6.18.56-y2linux-1.0.0-beta."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-5.html"
---

# Y2Linux 1.0 Beta 5 (Baseline 55) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 5 (Baseline 55)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 5 (Baseline 55)

Status: PUBLISHED as GitHub release `baseline-55` (2026-10-15). Release `1.0.0-beta.5`, Reborn `1.0.0-beta.5`, kernel `6.18.56-y2linux-1.0.0-beta.5`, update sequence 5450, Linux `5dd995f`, Reborn `84df9ae`, git tag `baseline-55` in both repositories. Built with `tools/production/release.py` (`--public`) in 134 s: container suite 740 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-5 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 0f478d3b85edbd97341acf35bde7440e9c35089349e08d635fe135bf1160fa14 |
| Y2ROOT | 15d870b8f29d8628c21865ac815587a0feb2504a5d4795a2ee85c018aa69a0f8 |
| RECOVERY | 57b34de882669ba7163c524896421843f564a636a3c4a26895ae3fe08f8a582e |
| Y2DATA (no SSH key) | 2865ccf8af3632a855371b4270edf657c1b6ba33fb87f17950694ecb57b9c52a |

## Since Beta 4.1: keyboard, search and a UI pass (Reborn only)

Owner request (2026-10-15): station search with the one-row letter wheel is "a miserable experience"; a full-screen keyboard for every text entry, driven by the buttons, not the wheel, keeping a way back. Owner decisions: Back = row up, hold Back = leave; QWERTY. Then: "do a ui pass that everything is correct and looks good".````

| Part | Detail |
| --- | --- |
| Keyboard | reborn_ui::keyboard: four QWERTY rows; pages abc/ABC (Shift once, twice = lock), 123, #+= (all printable ASCII), àé (searches); show/hide key for passwords; Done reads Join or Search; rows wrap. Used for the Wi-Fi password, radio station search (reopens with the last search) and library search. |
| Buttons | ActionRouter::set_keyboard: Back/Play-Pause/Previous/Next = up/down/left/right on press, held Previous/Next repeat every 180 ms, hold Back = cancel, the wheel is inert; Select types, hold Select = Done. No track skipping while it is open; volume, Power and headphone buttons unchanged. |
| Library search | Home → Search: artists, albums and songs whose words begin with every typed word, folded like A to Z order; live count while typing; results list (Edit Search, artists, albums, songs). |
| UI pass | All 95 preview states checked in Reborn's look and skins: one capitalization rule (Title Case titles/rows/buttons/menus, sentence case descriptions and values; 83 labels), one name for "Scan for Music", notices in the status bar instead of over the focused row or cover, opaque turn-off hold, "Wi-Fi Password" keyboard title. |
| Assets | Icons Shift, ShiftOn, Backspace, Eye, EyeOff added; font atlases unchanged (regeneration reproduced them). |

Host evidence: 437 Reborn tests (keyboard layout/movement/pages/limits; router keyboard mode including held buttons and a keyboard closed while a button is held; search matching; Wi-Fi, radio and library flows), strict Clippy, fmt; preview renders.

## Device checks owed (after the owner's over-the-air install)

Type a Wi-Fi password and join; radio search; library search; held Previous/Next repeat speed; hold Back cancels; playback keeps running while typing; screens look as in the previews. Still owed from Beta 4.1: station stop/pause, Wi-Fi after screen-off, update check after deep sleep.

## Known gaps

FM radio (next beta); HLS stations; sleep ≈9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection; full install from stock run on one player only.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
