---
title: "Y2Linux 1.0 Beta 7.4 (Baseline 65) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7.4 Baseline 65 Status: PUBLISHED as GitHub release baseline-65 2026-10-16. Release 1.0.0-beta.7.4 , Reborn 1.0.0-beta.7.4 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-7.4.html"
---

# Y2Linux 1.0 Beta 7.4 (Baseline 65) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7.4 (Baseline 65)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 7.4 (Baseline 65)

Status: PUBLISHED as GitHub release `baseline-65` (2026-10-16). Release `1.0.0-beta.7.4`, Reborn `1.0.0-beta.7.4`, kernel `6.18.56-y2linux-1.0.0-beta.7.4`, update sequence 6000, Linux `d909231`, Reborn `8c0f8c4`, git tag `baseline-65` in both repositories. Built with `tools/production/release.py` in 118 s: container suite 743 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-7.4 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 7766e213605c06e9902e30670fb232f08a70924731dd5ecd6dbc75981544c1c1 |
| Y2ROOT | 3abdc117d1099bb16ec61d9ae9435053ef52cfa5513d0323914973efdcc13f9c |
| RECOVERY | d42cb1e09a79514aacad7634a043642575735c26226609496f205592eee17d95 |
| Y2DATA (no SSH key) | ce839d23683de3fa64da3817ee7624b0d69267c878109e06d494788d8c4e534f |

## Since Beta 7.3 (Reborn `6e9b58c`)``

| Part | Cause / change |
| --- | --- |
| Messages | Owner: the message sat too high (over the status bar; the clock peeked out beside it). Three placements were rendered (below the bar, at the bottom, in the bar); the owner chose in the bar: a 26-px pill (was 34) with an icon for its subject (USB, note, Bluetooth, Wi-Fi, download, heart; a red warning for problems); the bar's title and status cluster give way while it shows, the back arrow stays. It covers no content. |
| Warmth | Owner felt the player warmer on 7.2/7.3. Device (charging, after an OTA install, during measurements): CPU 43.6 °C, PMIC 41.6–44.0 °C, comparable to Beta 6.3 while charging (archive 156: 31.7–50.4 °C); idle at 598 MHz. The one new load: the playing wave held the Interactive CPU lease (≥ 747 MHz) all the time Now Playing was visible. Now only motion a button started takes the lease (Ui::responding); the wave keeps 60 fps pacing at the lowest clock (≈3 ms CPU per frame). |

Host evidence: 487 Reborn tests (new: the wave alone takes no CPU boost; the status-bar symbol gives way under a message), strict Clippy, fmt; previews of the three placements.

## Device checks owed
  - Now Playing while playing on battery: frame rate stays ≈64 fps; CPU clock at 598 MHz (`cpufreq` time_in_state), CPU

and PMIC temperature over ten minutes.
  - Messages: computer connect, songs added, a play error appear in the status bar; the bar comes back after them.
  - Still open: the Songs list scroll sample (7.2), the 7.1 and 7 checks.

## Known gaps

As Beta 7.3.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
