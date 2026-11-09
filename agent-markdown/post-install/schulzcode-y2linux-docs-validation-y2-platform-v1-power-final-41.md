---
title: "POWER-FINAL-41 — software restart keeps the display (SMI gates) - Innioasis Updater"
description: "POWER-FINAL-41 — software restart keeps the display SMI gates Status: SEALED, awaiting the owner flash 2026-10-16. Package out/y2linux-platform-v1-power-final-candidate-4"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-41.html"
---

# POWER-FINAL-41 — software restart keeps the display (SMI gates) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-41 — software restart keeps the display (SMI gates)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-41 — software restart keeps the display (SMI gates)

Status: SEALED, awaiting the owner flash (2026-10-16). Package `out/y2linux-platform-v1-power-final-candidate-41/` (fallback = 40), receipts `out/deep-sleep-final/build41-receipts/`. BOOTIMG `cda64be9b35e0861e266085031d62c4b7a8b61a66d7121b8fc7825118261d12a`, Y2ROOT `efe870d1d43b207ee1f539413b6459bddb660ee76535f042ef07cf23cfc9f47e`, RECOVERY `5712c4cd72100099fc7d342f4b484a83665d9d8d0eb53ae1096fd68abac45cdc`. Kernel `6.18.56-y2linux-platform-v1-power-final-41`, release `…candidate.41`, update sequence 4100. Container suite 718 OK, all seal checks PASS. Signed OTA (release key): `…-41-ota-release/`. Contains 40 (snapshots stay).

## Why

Root cause from [40](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-40.md): after a software restart the SMI common clock gate is still closed when LK starts (`MMSYS_CG_CON0` keeps Linux's shutdown state through the watchdog restart), so the first display fetch through larb0 never completes. The DSI handover now opens the SMI common/larb0 gates if they are closed, waits up to 10 ms for larb0 to drain and logs `handoff: SMI gates … left closed by a restart, opened; larb0 stat=… after … us`. A cold start does not log it.

## Device results
  - Cold start (archive `20261016/141`): healthy, no `SMI gates` line, larb0 idle.
  - Software restart (archive 142): still dark, but the cause is confirmed: `handoff: SMI gates 1 left closed by a

restart, opened; larb0 stat=00000001 after 10000 us`. With the clock back, SMI common reads like a cold start, yet the request LK issued while it was gated stays stuck in larb0. Opening at handover is too late; 42 reopens the gates before the restart.

## Owner steps
  - Flash 41 (BOOTIMG + ANDROID). Cold start: no `SMI gates` line expected.
  - With the owner's OK: one software restart. Expected: panel lit, `SMI gates 1 … opened`, larb0 stat 0.
  - Then `/data/updates/restart.json``{"mode": "reboot"}` and an install with no Power presses.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
