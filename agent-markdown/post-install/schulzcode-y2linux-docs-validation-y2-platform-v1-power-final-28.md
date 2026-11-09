---
title: "POWER-FINAL-28 — stock battery percentage and top-off - Innioasis Updater"
description: "POWER-FINAL-28 — stock battery percentage and top-off Status: SEALED, AWAITING THE OWNER FLASH 2026-10-14. Package out/y2linux-platform-v1-power-final-candidate-28/ fallb"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-28.html"
---

# POWER-FINAL-28 — stock battery percentage and top-off - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-28 — stock battery percentage and top-off

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-28 — stock battery percentage and top-off

Status: SEALED, AWAITING THE OWNER FLASH (2026-10-14). Package `out/y2linux-platform-v1-power-final-candidate-28/` (fallback = 27), receipts `out/deep-sleep-final/build28-receipts/`. BOOTIMG `eb413fdc22ac656ed85067efd62d86da01e1c24057b9c8cdede53ffd0b779c94`, Y2ROOT `7537ba4311b347355e5a6df1edfca2a793eb02fef1f4f7bf671ccefa0a01afdf`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-28`, kernel `6.18.56-y2linux-platform-v1-power-final-28`, root `2026.08-platform-v1.58`, release `1.0.0-platform-v1-power-final-candidate.28`; Linux `36b8500` (changes `257fe3b`), Reborn `1c9edd4` (unchanged). Contains 27 (stock panel power-down, idle VGP2, VSYS sleep state).

## Why

Owner: on the charger 100 %, after a restart about 80 %; wanted 100 % when really full, then 99, 98, 97 … Stock analysis with REA: ledger F28–F33 (`docs/knowledge/stock-suspend-re-ledger.md`). Measured on 27 (boot `5919b4fe`): the first sample after boot read 4.002 V under load (87 %) while the PMIC's power-on OCV was 4.062 V; the charger stopped at the first 4.175 V sample, so the pack rested ≈4.09 V (95 % on the stock curve), and on the charger it ran from the battery down to 4.00 V (87 %) while the display said 100; nothing survived a restart.

## What 28 changes``````````````````````````````````

| Area | Stock (REA) | 28 |
| --- | --- | --- |
| Top-off | Hardware CV until (ISENSE − BATSNS + offset) × 1000 / 68 ≤ 150 mA for 6 × 10 s, or 3 h (BAT_TopOffModeAction, battery_meter_get_charging_current). | First 4.175 V sample at the normal current → 70 mA finish stage; Full at 4.175 V again or when the net sense drop ≤ 10.2 mV for 6 samples ≥10 s apart. 4.175 V target, hardware CV selector 30, 4.2 V guard and all timers/protections unchanged. charging_state shows finish, taper_samples, full_rest_uv, recharge_uv. |
| Recharge | Below 4.110 V. | Below min(4.110 V, last Full rest − 30 mV), floor 4.00 V. |
| Boot voltage | get_hw_ocv: PMIC 0x724 latched at power-on. | BAT0 voltage_ocv, read once at probe; used for the first estimate unless a charger moved it by 31+ points. |
| Display | UI SOC separate from SOC; 99 cap while charging; +1 per 10 s to 100 at Full and gauge reset; 100 through recharges; down-only on battery; saved in an RTC spare register, reused within 40 points. | Same rules in battery.py; 100 = the curve value at the Full rest voltage (anchor_percent); saved in /data/system/platform/battery-ui.json. power.json battery adds estimate_percent, anchor_percent, full_latched. |

## Tests

New/updated: `test_charger` (finish stage, stock taper rule and its 10-s spacing, recharge level and its loop guard, unknown current = 26 behaviour, boot OCV conversion of the live 0xc813 → 4062 mV), `test_battery_soc` (99 cap, Full count-up, 100 held on the charger, 100 → 99 → 98 → 97 single steps after unplug, restart restores 100 instead of the 87 % boot sag, 40-point and charger-moved-OCV refusals, persistence wiring). Kernel warnings unchanged (47, vendor Wi-Fi). Platform: `validate.py` PASS, ELF closure 354 PASS, installed ARM PASS, privacy clean, inventory 108 packages, container suite 707 OK.

## Owner checks after the flash
  - First boot: `cat /sys/class/power_supply/BAT0/voltage_ocv` (power-on OCV) and the shown percentage.
  - One full charge on the PC with SSH (archive before/after): `charging_state` must go `finish=1` at 4.175 V with

`charge_limit_ua=70000`, then Full; note `full_rest_uv` (expected clearly above 26's 4.09 V) and `recharge_uv`. No fault (`fault=0x0`), especially not 0x8.
  - On the charger after Full: display 100; then unplug and watch 100 → 99 → 98.
  - Restart (hold Power): the percentage stays where it was (not ≈80 %).
  - Still open from 27: one short sleep to read the VSYS/pmic_sleep counters.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
