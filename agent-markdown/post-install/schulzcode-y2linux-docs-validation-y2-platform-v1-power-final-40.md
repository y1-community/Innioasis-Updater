---
title: "POWER-FINAL-40 — handover snapshot for the restart display defect - Innioasis Updater"
description: "POWER-FINAL-40 — handover snapshot for the restart display defect Status: SEALED, awaiting the owner flash 2026-10-15. Package out/y2linux-platform-v1-power-final-candida"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-40.html"
---

# POWER-FINAL-40 — handover snapshot for the restart display defect - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-40 — handover snapshot for the restart display defect

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-40 — handover snapshot for the restart display defect

Status: SEALED, awaiting the owner flash (2026-10-15). Package `out/y2linux-platform-v1-power-final-candidate-40/` (fallback = 39), receipts `out/deep-sleep-final/build40-receipts/`. BOOTIMG `bc44a93d183ea980a4755eef95f0b935dbd491a86084eda1d87c93870d68d503`, Y2ROOT `37198d908a7e3fc99265e227f596993dfd2e2ed9b543cfd64e42d900cfd6392d`, RECOVERY `ad06315e34500c6a33d90f8d6e81867d5c03409a12cdec57c2d6fac8de16d1f6`. Kernel `6.18.56-y2linux-platform-v1-power-final-40`, release `…candidate.40`, update sequence 4000. Container suite 718 OK, all seal checks PASS. Diagnostic only; contains 39.

## Why

After a software restart SMI larb0 reads busy (39, archives 137/138), also when the display was stopped before the restart. Unknown: is larb0 already busy when Linux takes over LK's pipeline, or does our handover wedge it?``````````

| Change | Detail |
| --- | --- |
| Handover snapshots | /sys/kernel/debug/y2_display_snapshot slots 2 (handover, DSI probe before Linux touches LK's live pipeline) and 3 (parked), first probe of the boot only; larb0 0x400–0x4fc added. |
| Log | handoff: snapshot … and handoff: parked … with larb0 stat/greq, OVL status, OVL RDMA0, RDMA irq. |

## Device results — root cause found

Cold start (archive `20261016/139`) and one software restart (archive 140, panel dark). At **handover, before Linux touches anything** (slot 2), the restart differs from the cold start in exactly the way that explains the defect:``

| Register | Cold | Restart |
| --- | --- | --- |
| MMSYS_CG_CON0 (0x14000100) | 0 | 1 — SMI common clock gated |
| SMI common config (0x14011200/228/230/234/300/404) | configured | 0 (gated block reads zero) |
| larb0 status / GREQ (0x14010000 / 0x450) | 0 / 0 | 1 / 1 — request pending |
| OVL status | 0x1e | 0x1f (still running) |

Linux gates SMI common when the display and GPU release it at shutdown; the watchdog restart keeps `MMSYS_CG_CON0`; LK assumes the cold default, shows its logo, and its first fetch through larb0 never completes. Every later symptom (full OVL FIFO, no RDMA frame, no vblank, mutex timeout) follows. 38's external reset and 39's mutex reset could not help. Fix: [POWER-FINAL-41](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-41.md).

## Owner steps
  - Flash 40 (BOOTIMG + ANDROID). Cold start: the agent saves the snapshots.
  - With the owner's OK: one software restart; the panel will likely stay dark. The agent saves the snapshots, then

the owner holds Power 10 s. Diff cold/warm at `handover` and `parked`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
