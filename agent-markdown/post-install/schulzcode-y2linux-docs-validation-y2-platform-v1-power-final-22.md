---
title: "POWER-FINAL-22 — dark DSI hand-over (no colour flash between logo and splash) - Innioasis Updater"
description: "POWER-FINAL-22 — dark DSI hand-over no colour flash between logo and splash Status: SEALED, AWAITING THE OWNER FLASH 2026-10-13. Package out/y2linux-platform-v1-power-fin"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-22.html"
---

# POWER-FINAL-22 — dark DSI hand-over (no colour flash between logo and splash) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-22 — dark DSI hand-over (no colour flash between logo and splash)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-22 — dark DSI hand-over (no colour flash between logo and splash)

Status: SEALED, AWAITING THE OWNER FLASH (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-22/` (fallback = 21), receipts `out/deep-sleep-final/build22-receipts/`. BOOTIMG `f73ba54c706d1d15612d8bfea7d1273b93a45293190da5a476f9f76fa8fb402b`, Y2ROOT `d7d21d71a397acb7d7e95d0f240c798e35da6d7068030844dc867854542e6a0d`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-22`, kernel `6.18.56-y2linux-platform-v1-power-final-22`, root `2026.08-platform-v1.52`, release `1.0.0-platform-v1-power-final-candidate.22`; Linux `430ff11` on `main`, Reborn unchanged (`217e28d`). Flash BOOTIMG + ANDROID only with `MT6582_preserve_data_scatter.txt`, Download Only. Sleep code identical to 20/21.

## 21 result (owner, 2026-10-13)

The white/colour screen after the shutdown animation is gone. The colour flash between the bootloader logo and the splash remained.

## Cause (21 boot `a0c4d60e`, archive 118)

`mtk-dsi: handoff: clocks on; park video` at 0.489 s stops LK's video stream; Linux's first DSI modeset (from the fbdev client) streams at 0.532 s; the splash's first frame appears at 0.642 s. The lit panel had no stream for ≈40 ms. 21's splash-side darkening ran after the modeset and could not cover it.

## What 22 changes

Overlay `0017-mt6582-dsi.patch` (`mtk_dsi.c`, in `display.ko` loaded from the initramfs at ≈0.47 s): before "park video" the hand-over switches the panel's backlight (the DT `backlight` phandle of the panel node) off, only if it was lit; 50 ms after the first Linux `atomic_enable` it relights; a 3-s fallback relights if no enable comes, and a devm release relights on unbind or probe failure. Expected: logo → short dark → black → splash. 21's changes stay.

## Tests

`test_display_quiet_power` (+ the hand-over order), `test_overlay_hashes`; locked-container production suite 693 cases, exit 0; package validation, ELF, installed ARM, privacy, inventory PASS.

## What to check after the flash

Power on several times: no colour flash between logo and splash; `dmesg | grep handoff` shows `backlight off until the first Linux frame` then `backlight restored`. Shutdown stays dark. Then the sleep tests.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
