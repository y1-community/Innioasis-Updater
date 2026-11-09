---
title: "POWER-FINAL-47 — DSI register read lag: keep DCM off for DSI/DPI - Innioasis Updater"
description: "POWER-FINAL-47 — DSI register read lag: keep DCM off for DSI/DPI Status: PUBLISHED as GitHub release baseline-47 ; its fix confirmed on 48 archive 20261016/151 . Package"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-47.html"
---

# POWER-FINAL-47 — DSI register read lag: keep DCM off for DSI/DPI - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-47 — DSI register read lag: keep DCM off for DSI/DPI

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-47 — DSI register read lag: keep DCM off for DSI/DPI

Status: PUBLISHED as GitHub release `baseline-47`; its fix confirmed on 48 (archive `20261016/151`). Package `out/y2linux-platform-v1-power-final-candidate-47/` (fallback = 46, which the player runs), receipts `out/deep-sleep-final/build47-receipts/`. BOOTIMG `97f2ef876bc78b140933204f504142830786f6ec9b4f65a2b5b08b632cf9e280`, Y2ROOT `efb3f4e66f85ed8f200f4b292d1e1a2894bf462e04641748e27aff5a1df40bce`, RECOVERY `4293cfcafa4d041bdfb89c6af5c9e3dbc57d24949a4b2ee9d3f25ac9deb2ce35`. Kernel `6.18.56-y2linux-platform-v1-power-final-47`, update sequence 4700, Linux `ba7a003`, Reborn `850687d`. Container suite 718 OK, all seal checks PASS. Signed with the release key: `…-47-ota-release/`.

## Why

46's recovery log (archive `20261016/150`) narrows the lag to a 42 ms window: LK's DSI registers read correctly at the hand-over (`ps=000305a0 vact=00000168`), every read lags at Linux's first modeset, and power-cycling DSI clocks and PHY three times does not clear it. In that window the display mutex's first prepare applies MMSYS DCM, group 1 (DSI engine/digital, DPI) included. Stock (`out/rea/fm-kernel.elf`) calls `dcm_enable` only from `mt_dcm_init` and the sysfs store — once at boot, with its display streaming — and toggles only bus DCM around idle. All three lagged boots (143, 43's recovery, 150) are after POWER-FINAL-16 introduced the DCM; the older dark restarts read correctly.``````````

| Change | Detail |
| --- | --- |
| dcm-policy.h | DIS DCM group 1 stays off (0x1400012c/0x14000130 = 0xf; the clear register is not written). Group 0 and SMI DCM unchanged. No power cost: the DSI streams whenever the screen is on; DIS is powered down when it is off. |
| DSI evidence (patch 0017) | Hand-over and read-back lines print dcm1= (0xf expected from 47 on). |
| update probe-recovery | Follows the restart setting: restart into the recovery screen and back, nothing installed. |

## Owner steps
  - Install 47 over Wi-Fi from the release (Settings → About & Updates).
  - With the owner's OK: several `y2-platform update probe-recovery` runs (each restarts into the recovery screen

and back); the agent archives each recovery log. Pass: every recovery screen lit, no `read-back` line.

## Device results (on 48, archive `20261016/151`)
  - 48's own install (over Wi-Fi from the release): recovery screen lit (vblank 16 → 219, no read lag, 53 s),

`Acknowledged`. DCM group 1 reads `0x1400012c = 0000000f` in the recovery and the running system.
  - Five restart-entered recovery probes (owner-approved): all five recovery screens produced frames (vblank 16–17

at 1.2 s, OVL irq `0x10`, RDMA irq `0x27`, no vblank/flip timeouts), all five returned on their own in 20–35 s, every return boot lit. Logs `probe1..5-recovery.log` and `probe1..5-return-dmesg.txt` in the archive.
  - The read lag itself is not DCM: probes 4 and 5 still read the DSI one register late with `dcm1=0000000f`

(44's three power cycles again did not clear it). But unlike every lagged boot before (143, 150: OVL irq 0, RDMA `0x24`, vblank 1), the pipeline ran. So far the evidence says DSI DCM turned the lag into a dark screen; the lag's own cause is unknown (2 of 5 restart entries). 44's power-cycle retry is useless and costs ~75 ms when it fires.
  - Visual confirmation of each probe screen by the owner: pending.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
