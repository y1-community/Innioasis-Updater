---
title: "POWER-FINAL-39 — display mutex reset for the software restart; smoother update screen - Innioasis Updater"
description: "POWER-FINAL-39 — display mutex reset for the software restart; smoother update screen Status: SEALED, awaiting the owner 2026-10-15. Package out/y2linux-platform-v1-power"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-39.html"
---

# POWER-FINAL-39 — display mutex reset for the software restart; smoother update screen - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-39 — display mutex reset for the software restart; smoother update screen

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-39 — display mutex reset for the software restart; smoother update screen

Status: SEALED, awaiting the owner (2026-10-15). Package `out/y2linux-platform-v1-power-final-candidate-39/` (fallback = 38), receipts `out/deep-sleep-final/build39-receipts/`. BOOTIMG `e3ba4a51f4b0009db518739348fd97b6b061307647a4f4b1e0e46e0f53ead3ee`, Y2ROOT `304057726d8e0fd02a73feaf4f173b33a53c33f5a0e495ecc8e736d5f1e55803`, RECOVERY `dca8076362830f8c4683e5276f8128d57c3bb04c080c58bb752103ac8d31ac65`. Kernel `6.18.56-y2linux-platform-v1-power-final-39`, release `1.0.0-platform-v1-power-final-candidate.39`, update sequence 3900. Container suite 718 OK, all seal checks PASS. Signed OTA (release key): `…-39-ota-release/`.

## Why

38's stock restart sequence (external reset) did not fix the dark panel after `y2-platform shutdown reboot` (archive `20261015/135`, boot_reason 4, vblank stuck at 1). Snapshot diff against the cold start just before (archive 134): DSI and MIPI TX equal; the overlay FIFO full (`OVL_RDMA0_CTRL``0x03ff0001` vs `0x00080001`), OVL flow/RDMA debug stuck, the mutex block with a timeout flag (`INTSTA``0x10000101` vs `0x10000001`) and a pending commit (`REG_COMMIT` 8 vs 0), and Linux logging `could not acquire mutex 0` 33 s after boot: its first frame is never committed. On a cold start the same full FIFO clears with Linux's first frame (0.6 s).``````

| Change | Detail |
| --- | --- |
| Mutex handover | First mutex prepare per boot pulses MUTEX_RST for all six mutexes and clears INTSTA (vendor register map), logging Y2SCAN mutex reset: intsta … commit …. |
| Recovery screen | Double-buffered with page flips at vblank (owner: flicker); activity as dots after the step name instead of a moving mark in the bar (owner: looked like a second bar). |

## Device results
  - Flashed 2026-10-15 (archive `20261015/136`): cold start healthy; the handover reset logged

`intsta 10000001->10000000 commit 00000000->00000000`.
  - Software restart, screen on: still dark (archive 137). The mutex was clean at handover, so the stale mutex

seen on 38 is a consequence. New decisive difference: **SMI larb0 status (`0x14010000`) 1 = busy after the restart, 0 after a cold start**; overlay FIFO full, RDMA not done, DSI idle follow from it.
  - Software restart with the screen off (CRTC disabled, nothing fetching): still dark, larb0 busy again

(archive 138). So it is not a reset during a memory fetch. The display power domain was not powered down at screen-off (`dis_offs=0`), so "domain off before restart" is untested.
  - Restart boots reach the display handover about 0.4 s later than cold boots, and DVFS admits 1.3 GHz at once

(`result=0`, cold: deferred). Not yet linked to larb0.
  - Next diagnostic: snapshot at the moment of handover (before Linux parks LK's pipeline) on a cold and a restart

boot, to see whether larb0 is already busy when Linux takes over.

## Owner steps
  - Flash 39 (BOOTIMG + ANDROID; the kernel changed). The agent checks the `mutex reset` line on the cold boot.
  - With the owner's OK: one software restart. Panel lit → `restart.json` on and an install without Power presses

(39's OTA package or a reinstall). Panel dark → hold Power; diff the snapshots again.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
