---
title: "POWER-FINAL-43 — hold SMI for LK's display until the display takes over - Innioasis Updater"
description: "POWER-FINAL-43 — hold SMI for LK's display until the display takes over Status: SEALED, awaiting the owner flash 2026-10-16. Package out/y2linux-platform-v1-power-final-c"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-43.html"
---

# POWER-FINAL-43 — hold SMI for LK's display until the display takes over - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-43 — hold SMI for LK's display until the display takes over

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-43 — hold SMI for LK's display until the display takes over

Status: SEALED, awaiting the owner flash (2026-10-16). Package `out/y2linux-platform-v1-power-final-candidate-43/` (fallback = 42), receipts `out/deep-sleep-final/build43-receipts/`. BOOTIMG `bf5739dece268ce2b76cef7a66993af4348bb0d81729f19c5f261b63ba881ddc`, Y2ROOT `d18c1f06b774027f6e3addb7479058a2df533c4c8357beb345fed2c5ab350641`, RECOVERY `54e7eab49e4ab4fb1d8302f80a5474d2974cd919fc935256a827dbed98c3b61d`. Kernel `6.18.56-y2linux-platform-v1-power-final-43`, release `…candidate.43`, update sequence 4300. Container suite 718 OK, all seal checks PASS. Signed OTA (release key): `…-43-ota-release/`.

## Why

42 (reopen the gates before the restart) did not help (archives `20261016/144`, and 145 with `dis_pdn` off): the gate is closed during the next boot, not left over. Lima shares SMI common and goes runtime idle 200 ms after its probe. Every lit cold start hands the display over ~0.10 s after Lima's probe; every dark restart (38–42, screen on or off) ~0.5 s after it (archives 135–145). Then the last reference drops, CCF closes SMI common under LK's running fetch and larb0 wedges. The owner observed the same with power-on from charging with USB plugged in, which also hands over late.``````

| Change | Detail |
| --- | --- |
| mm-clocks.c | Holds SMI common and larb0 from probe when LK left them running (holding SMI common/larb0 for the loader display …); y2_mm_release_loader_hold() drops the hold. |
| mutex (patch 0011) | Releases the hold in the first prepare, after enabling its own references. |
| 42's restart handler | Removed. 41's handover opener and the snapshots stay. |

## Device results — FIXED
  - Cold start (archive `20261016/146`): hold taken at 0.40 s (before Lima at 0.41 s) and handed to the display mutex

(enable counts 1/1 afterwards); display lit, taint 0.
  - Software restart (archive 147): display lit (owner: "it worked"). Handover at 0.89 s as on every restart boot,

but larb0 idle (`stat=0 greq=0`), no `SMI gates` line, vblank 17 → 219, taint 0. The dark panel after a software restart, open since candidate 11, is fixed.

## Owner steps
  - Flash 43 (BOOTIMG + ANDROID). Check: `holding SMI common/larb0` at boot, no `SMI gates` line, display lit.
  - With the owner's OK: one software restart; then power-off and power-on with USB plugged in.
  - If both stay lit: `/data/updates/restart.json` on and an install with no Power presses.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
