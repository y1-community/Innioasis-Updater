---
title: "Y2Linux 1.0 Beta 8.31 (Baseline 130) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.31 Baseline 130 Status: PUBLISHED as GitHub release baseline-130 2026-10-24, installed on the owner's player before publishing. Release 1.0.0-beta.8.31"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.31.html"
---

# Y2Linux 1.0 Beta 8.31 (Baseline 130) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.31 (Baseline 130)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.31 (Baseline 130)

Status: PUBLISHED as GitHub release `baseline-130` (2026-10-24), installed on the owner's player before publishing. Release `1.0.0-beta.8.31`, Reborn `1.0.0-beta.8.31`, kernel `6.18.56-y2linux-1.0.0-beta.8.31`, update sequence 9500, root `2026.08-platform-v1.172`, Linux `b0b8ae6`, Reborn `b07cb9d`. Built with `tools/production/release.py` (147 s, resumed workspace, update based on `baseline-129`): container suite 880 OK; Reborn workspace tests, `clippy -D warnings` and `fmt --check` clean; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.31 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 2c65908857a4b245577c7832c05aa9bab1dc9b7fab4178dc824b9c96f3f817f4 |
| Y2ROOT | 20d0fa8fbe2a367dbf5915b5e4a657a8462aa63a91d7988e9e894e251c9a6814 |
| RECOVERY | a3c185404771bba65a3803312179e88157df6833281fa2971eca4e360584ad7d |
| Y2DATA (no SSH key) | 5fd7c202065699212376ddc63627068f67aac610fbb3f5f6541e6b9baaca26a3 |

## Why

A user request: "Sometimes I go a bit deaf in my left ear, so I adjust the left side by -1 to compensate."

## What changed since Beta 8.30``````````

| Change | Detail | Evidence |
| --- | --- | --- |
| Settings → Sound → Balance | Left +10 dB … Center … Right +10 dB in 1 dB steps (settings.balance, -10..=10, negative = left louder, clamped on load). The louder side is reached by lowering the other side's samples at the live sink gain (VolumeRamp::balance), never by raising one, so it cannot clip; jack and Bluetooth alike, live while playing (an atomic like the volume, no reopen). The list opens on the current value | Reborn b12a1ee; balance_lowers_only_the_other_side (-1 dB: 10 000 → 8913 on the right), balance_opens_on_the_current_side_and_sets_it |
| Sound page layout | Six rows no longer fit: once the focus reaches Balance the first row scrolls away, as on Display, so the Output card stays on screen | previews 27, 29d, 29e |

## Device results``````

| Check | Result |
| --- | --- |
| Install by OTA staging (owner's player) | sequence 9500 Acknowledged after a normal update restart |
| Settings → Sound → Balance, driven with button events over SSH | Sound page and Balance list as in the previews; Left +1 dB selected → session.json"balance":-1; playback 4 s with it on: playing, 0 xruns, 0 playback errors; set back to Center ("balance":0) |
| Listening check of the shift | not done by ear in this session |

## Open
  - The left/right shift was checked in host tests (sample values) and on the device as a setting, not by ear.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
