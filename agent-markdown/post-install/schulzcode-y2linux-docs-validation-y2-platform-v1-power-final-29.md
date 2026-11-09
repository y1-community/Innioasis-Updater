---
title: "POWER-FINAL-29 — finish-stage and discharge-estimate corrections - Innioasis Updater"
description: "POWER-FINAL-29 — finish-stage and discharge-estimate corrections Status: INSTALLED, FULL CHARGE QUALIFIED 2026-10-14, archive 127, boot cac3e209 . Package out/y2linux-pla"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-29.html"
---

# POWER-FINAL-29 — finish-stage and discharge-estimate corrections - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-29 — finish-stage and discharge-estimate corrections

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-29 — finish-stage and discharge-estimate corrections

Status: INSTALLED, FULL CHARGE QUALIFIED (2026-10-14, archive 127, boot `cac3e209`). Package `out/y2linux-platform-v1-power-final-candidate-29/` (fallback = 28), receipts `out/deep-sleep-final/build29-receipts/`. BOOTIMG `3f82ae593a936067730cd735c780cf42d483457ab8f2591590748448cc6efc07`, Y2ROOT `5d9f298bb8432a0bcf13acb1ae2498e9d95252764f4f461003d9a0bc2b717f52`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-29`, kernel `6.18.56-y2linux-platform-v1-power-final-29`, root `2026.08-platform-v1.59`, release `1.0.0-platform-v1-power-final-candidate.29`; Linux `f9ce653` (changes `f2c9e0b`), Reborn `1c9edd4`. Contains 27 and 28.

## 28 on the device (archive `20261014/126`)

Boot `8f43c71e` started at 89 % from the power-on OCV (27's loaded-sample method: ≈81 %); the restart (`129e5611`) restored the saved 85 %. One short sleep: pmic_sleep 1/1, `last_changed` 0x3ff, `vsys_refusals` 0 (27's VSYS step works). A second request was refused by the known `wake_event_in_progress` race. Charge (`charge-log.jsonl`): 450 mA CC for 15 min to 4.175 V, finish stage entered without fault, then 70 mA: the pack fell back to 4.09 V and stayed flat (ISENSE est. ≈90 mA, screen off, idle, awake on USB). The 3-h top-off budget would have ended it as a timeout fault. On battery the display drifted 89 → 85 in 3.5 min toward the loaded-voltage SOC.

## What 29 changes
  - Finish stage steps 450/650 → 200 → 70 mA at successive 4.175 V samples; at 70 mA it completes on 4.175 V, the stock

taper rule, or a plateau (no 5 mV rise in 10 min). Full still needs the ≥4.07 V rest. The 3-h top-off budget completes a finishing cycle (stock `BAT_TopOffModeAction`); 24-h and precharge timeouts stay faults. `charging_state` shows `finish` as the current cap, `plateau_uv`, `topoff_done`.
  - On battery with samples ≤60 s apart, the estimate follows stock `oam_run` (model current (OCV(SOC) − V)/R(V)

integrated against 1300 mAh); after longer gaps (suspend) the rested voltage is used as before.

## Tests

`test_charger` (steps, plateau from the archive-126 trace, rise restarts the window, top-off budget completes only a finishing cycle), `test_battery_soc` (archive-126 drift: stays ≥88 instead of 85; sustained load still discharges; suspend gap uses the rested voltage). Kernel warnings unchanged (47). validate PASS, ELF 354, installed ARM, privacy, inventory 108, container suite 708 OK.

## Owner checks after the flash
  - A full charge on the PC with SSH: `finish` 200000 → 70000 → Full, `full_rest_uv`, no fault.
  - After Full: 100 on the charger; unplug: 100 → 99 → 98 without a quick sag while using it.
  - Restart: the percentage stays.

## On the device (archive `20261014/127`, `charge-log.jsonl`)

Boot restored the saved 94 % (power-on OCV 4.094 V). Charge with SSH, no fault at any point: 450 mA → 4.175 V → 200 mA (28 min, sense drop ≈46 mV, voltage rising) → 4.175 V → 70 mA → voltage flat 4.13–4.15 V → plateau completion after 10 min (`status=3`) → rest ≥4.07 V for 60 s → Full (`status=4`). The owner unplugged once 1 s after the first plateau hold (cycle reset by design), the replugged cycle completed at 3676 s: `full_rest_uv`4128442 (26/27: ≈4.09 V), `recharge_uv` 4098442, display 100, `anchor_percent` 97.68, `full_latched` true. Owner observation: while charging the display stayed at 97–98 until Full (stock 99 cap / estimate), then 100.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
