---
title: "Y2Linux 1.0 Beta 8.37 (Baseline 144) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.37 Baseline 144 Status: PUBLISHED as GitHub release baseline-144 2026-10-25, installed on the owner's player before publishing. Release 1.0.0-beta.8.37"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.37.html"
---

# Y2Linux 1.0 Beta 8.37 (Baseline 144) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.37 (Baseline 144)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.37 (Baseline 144)

Status: PUBLISHED as GitHub release `baseline-144` (2026-10-25), installed on the owner's player before publishing. Release `1.0.0-beta.8.37`, Reborn `1.0.0-beta.8.37`, kernel `6.18.56-y2linux-1.0.0-beta.8.37`, update sequence 10200, root `2026.08-platform-v1.186`, Linux `69f9f4c`, Reborn `69232c2`. Built with `tools/production/release.py` (130 s, resumed workspace, update based on `baseline-138`): container suite 883 OK; all seal checks PASS, no MediaTek firmware in any image. Reborn host tests: 679 passed, strict Clippy clean. Labels 139–143 were device test builds of this release (sequences 10150–10190), not published. Milestone audit BETA-8.37 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 55cc8b30ff2a0bc520ab99bf1425791d10598c91d5a1607643c940fd1460d581 |
| Y2ROOT | bd6507a6499a88047657af23ec131a528bf130c9a5d79d9cdbce290583744098 |
| RECOVERY | 42dfb6f71e37539ac924de37ce4e98c80bc6574eac13c3fc57adee8dbac33ed7 |
| Y2DATA (no SSH key) | d288083c17df2e7e067dcb586022db4767a023dc7cd9d941d2018d0fa6aae6ce |

## What changed since Beta 8.36``````

| Change | Detail | Evidence |
| --- | --- | --- |
| Sleep timer lengths (Y2Reborn #29) | Now Playing's Sleep Timer opens a picker: Off, End of Song (Chapter), 5–45 min, 1 h, 1 h 15, 1 h 30, 2 h, 2 h 30, 3 h; opens on the timer set (else 30 min), marks it with its time left, Select starts, Back cancels. Times read in hours ("Sleeps in 2 h"); Now Playing redraws them as the minutes change, also while paused. Skins get {sleep}, "if": "sleep" and the moon icon; every shipped skin shows "Headphone Jack · Sleeps in 23 min" | tests; on device 2 h → "1 h 59 min" while paused, Classic line |
| Search (Y2Reborn #44) | Back goes up one level (results → typing → out); a new search starts empty (a result opened and Back keeps it); playlists are found by name; each section shows its first four with See All N, which opens that section alone (Back returns); Play All keeps every song found | tests; on device: "a" 25 rows with See All 82 Songs, Back ×3 → Home, two SD playlists found and opened |
| Playlist page | the focused song stays on screen (it went off the bottom from the fourth song in every playlist) | test fails on the old code at the 4th song; on device |
| One way of scrolling (owner request) | headers stay — album, playlist and audiobook headers, Display's brightness card, the search field — and only the list under them scrolls, a row a step with the list glide; settings pages keep their rows until the focus reaches an edge | tests (focus always in view, one row a step); owner checked on device |

No kernel, platform, memory map, partition or packaging change; session and settings unchanged.

## Open
  - Haptic feedback (Y2Reborn #28) still needs a driver for the vibration motor.
  - The artist page keeps its own sideways row of albums.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
