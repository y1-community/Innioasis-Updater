---
title: "POWER-FINAL-42 — reopen the SMI gates before a software restart - Innioasis Updater"
description: "POWER-FINAL-42 — reopen the SMI gates before a software restart Status: SEALED, awaiting the owner flash 2026-10-16. Package out/y2linux-platform-v1-power-final-candidate"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-42.html"
---

# POWER-FINAL-42 — reopen the SMI gates before a software restart - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-42 — reopen the SMI gates before a software restart

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-42 — reopen the SMI gates before a software restart

Status: SEALED, awaiting the owner flash (2026-10-16). Package `out/y2linux-platform-v1-power-final-candidate-42/` (fallback = 41), receipts `out/deep-sleep-final/build42-receipts/`. BOOTIMG `6eb3209b2f8b56a0c1f810d9379769928a3f7f9f63bbdc118bcda3e888527ff3`, Y2ROOT `25252bba7ee8c4ccdab44cb721fb70f1678c52c75402272a8952ae3447ad918b`, RECOVERY `5a5725dc73e20bbb228814bfb95a184cd4ae2b0be45ca1a478ed8906ff9443e7`. Kernel `6.18.56-y2linux-platform-v1-power-final-42`, release `…candidate.42`, update sequence 4200. Container suite 718 OK, all seal checks PASS. Signed OTA (release key): `…-42-ota-release/`.

## Why

41 confirmed that a software restart leaves the SMI common gate closed (archive `20261016/142`), but opening it at the next handover is too late: LK's request issued while the clock was off stays stuck in larb0. 42 adds a restart handler (priority 255, before the watchdog handler, after all drivers have shut down) in `mm-clocks.c` that reopens SMI common and larb0 (`MMSYS_CG_CLR0` = 3) when the DIS domain is powered, so LK starts from the cold-start state. 41's handover opener and the snapshots stay.

## Device results
  - First boot after the flash dark with larb0 idle (archive `20261016/143`, stale state after the stuck 41 restart and

the flash); the next cold start was healthy.
  - Restart still dark (archive 144), also with `dis_pdn` off (145): `SMI gates 1 left closed` at handover again.

The gate is closed during the next boot (Lima runtime idle), not left over. Fix: [43](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-43.md).

## Owner steps
  - Flash 42 (BOOTIMG + ANDROID).
  - With the owner's OK: one software restart. Expected: panel lit, larb0 idle at handover, no`SMI gates` line.
  - Then `/data/updates/restart.json``{"mode": "reboot"}` and an install with no Power presses.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
