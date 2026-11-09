---
title: "Y2Linux 1.0 Beta 7.5 (Baseline 66) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7.5 Baseline 66 Status: PUBLISHED as GitHub release baseline-66 2026-10-16. Release 1.0.0-beta.7.5 , Reborn 1.0.0-beta.7.5 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-7.5.html"
---

# Y2Linux 1.0 Beta 7.5 (Baseline 66) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7.5 (Baseline 66)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 7.5 (Baseline 66)

Status: PUBLISHED as GitHub release `baseline-66` (2026-10-16). Release `1.0.0-beta.7.5`, Reborn `1.0.0-beta.7.5`, kernel `6.18.56-y2linux-1.0.0-beta.7.5`, update sequence 6050, Linux `2ec56d2`, Reborn `0291d69`, git tag `baseline-66` in both repositories. Built with `tools/production/release.py` in 121 s: container suite 743 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-7.5 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 7d2dae955fc923abdb5c30df7ae75d727c18086e8867327eb6c48321542420cd |
| Y2ROOT | e840b2e1c747f99eef092bcf7e16ac05b280a73e8588a6d1a108694bcf6b9803 |
| RECOVERY | dcdf446b93f446203a7fa974c441905ce1cb4ef94e546c009c366ee7402ff0f4 |
| Y2DATA (no SSH key) | 6e896290c619cd3ecde58decf9f68842de9421cba169e2c6fcdd417ad5a4d361 |

## Since Beta 7.4 (Reborn `d5db247`)````

| Part | Cause / change |
| --- | --- |
| Status bar | Owner: "everything is very small and we still have some space". Four layouts were rendered; the owner chose C: the screen's name beside the back arrow in Title Case (SemiBold 15, white) instead of centred tracked caps; clock SemiBold 15, percentage SemiBold 13; icons 18 px with Wi-Fi and Bluetooth at 22 px (they looked smaller than the USB plug at one size); battery 25 × 13; back arrow 22 px. Skins keep their compact cluster. |
| Home header | "Reborn" and the short version where other screens show their name (owner asked for a header). |
| Messages | The status-bar pill is 30 px (was 26) with SemiBold 15 text and an 18 px icon. |
| Skin | Owner: Theme should become "Skin" and leave Display. Settings → Skin is a seventh Settings row (44-px rows, no scrolling; new palette icon); Display keeps Brightness and four rows and no longer scrolls. Skins are read from Skins folders and still from Themes. |
| About & Updates | The Music Library row only opened Storage (owner: "double"); removed. The song count is Scan for Music's secondary text in Storage. |

Host evidence: 487 Reborn tests (Skin row in Settings, not in Display; Title Case titles), strict Clippy, fmt; all 115 previews compared by eye; Classic, Big Type and Winamp skins rendered (their own bars unchanged; the native Cover Flow, equalizer and update screens inside skins take the new bar).

## Device checks owed
  - The new status bar, Home header and messages on the panel: legibility, nothing clipped with Wi-Fi, Bluetooth, USB and

charging all shown.
  - Settings → Skin opens the picker; a skin copied into `Skins` appears.
  - Still open from 7.4: Now Playing on battery (598 MHz, temperatures, fps), the Songs list scroll sample, 7.1 and 7 checks.

## Known gaps

As Beta 7.4.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
