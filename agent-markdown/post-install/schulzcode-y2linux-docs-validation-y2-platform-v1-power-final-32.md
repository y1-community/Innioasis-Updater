---
title: "POWER-FINAL-32 — deep idle during screen-off playback - Innioasis Updater"
description: "POWER-FINAL-32 — deep idle during screen-off playback Status: SUPERSEDED, NEVER FLASHED ALONE; PLAYBACK TEST OWED 2026-10-14; contained in 33–34, installed as part of 33."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-32.html"
---

# POWER-FINAL-32 — deep idle during screen-off playback - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-32 — deep idle during screen-off playback

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-32 — deep idle during screen-off playback

Status: SUPERSEDED, NEVER FLASHED ALONE; PLAYBACK TEST OWED (2026-10-14; contained in 33–34, installed as part of 33). Package `out/y2linux-platform-v1-power-final-candidate-32/` (fallback = 31), receipts `out/deep-sleep-final/build32-receipts/`. BOOTIMG `5f1766ca727ffee2824aab2f2bfee5f09d06bbe68dcc27146887338bc591a131`, Y2ROOT `f9ca5bbc5c7400e9d7d45708efcf70d8f58c9afe79ebfe4ded8724763d558938`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-32`, kernel `6.18.56-y2linux-platform-v1-power-final-32`, root `2026.08-platform-v1.62`, release `1.0.0-platform-v1-power-final-candidate.32`; Linux `4ded0fe`, Reborn `0892bf2`. Contains 27–31.

## Why

Awake idle on 29 (ledger F34–F38): only WFI is ever used awake. Screen-off playback never deep-idled because Y2's deep-idle clock rule also required the INFRA audio clock (bit 5) off; stock dpidle does not (INFRA mask `0xa080`, AUDIO group unchecked, AUDINTBUS moved to 26 MHz around the WFI, which Y2 already mirrors). Enabled-but-idle Bluetooth blocks every deep idle (BTIF/AP_DMA clocks, CONN domain); that is a separate, larger change (STP PSM).

## What 32 changes

`clocks.c`: `deep_idle_audio` (kernel default N = 31) drops bit 5 from the INFRA deep-idle mask; `deep_audio_entries` counts deep-idle clock handovers made with the AFE clock on. `power_features` arms the switch; sleep rows record it.

## Tests

`test_cpu_fix03` (audio clock blocks when off, admitted and counted when on, stock-mask INFRA clocks still block), `test_cpu_c3_uart`/`test_cpu_fix02` (shared mask helper), `test_power_final_27` (switch armed/overridable). Kernel warnings unchanged (47). validate PASS, ELF 354, installed ARM, privacy, inventory, container suite 713 OK.

## Owner test

Wired headphones, Bluetooth off, screen off, ≈30 min playback. Before/after: SPM `dormant_entries` / `dormant_residency_us`, cpuidle SLIDLE/DORMANT usage/time, `deep_audio_entries`, Reborn `audio_xruns`, listening for clicks. Disable with `{"deep_idle_audio": false}` in `/data/system/platform/power-features.json`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
