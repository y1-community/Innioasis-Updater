---
title: "POWER-FINAL-27 — stock sleep-parity gaps C, A, B - Innioasis Updater"
description: "POWER-FINAL-27 — stock sleep-parity gaps C, A, B Status: SEALED, AWAITING THE OWNER FLASH 2026-10-14. Package out/y2linux-platform-v1-power-final-candidate-27/ fallback ="
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-27.html"
---

# POWER-FINAL-27 — stock sleep-parity gaps C, A, B - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-27 — stock sleep-parity gaps C, A, B

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-27 — stock sleep-parity gaps C, A, B

Status: SEALED, AWAITING THE OWNER FLASH (2026-10-14). Package `out/y2linux-platform-v1-power-final-candidate-27/` (fallback = 26), receipts `out/deep-sleep-final/build27-receipts/`. BOOTIMG `c9017de1d19924c404f0776b9bacd0e09df9bca1c82802fc7f260e058c57902c`, Y2ROOT `c70dc92bb86a883ef83a0af22bbda52f6cd19577710f15a8532d576fa73f737a`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-27`, kernel `6.18.56-y2linux-platform-v1-power-final-27`, root `2026.08-platform-v1.57`, release `1.0.0-platform-v1-power-final-candidate.27`; Linux `2c3e2bd` (changes `f1d77a0`, identity/audit `df15aab`, include fix `2c3e2bd`), Reborn `1c9edd4` (unchanged).

## Why

26's night (archive `20261014/124`): 10.3 h, 21/21 clean sleeps, whole-night ≈8.3 mA, but the voltage slope fell from −10.6 to −1.2 mV/h through the night (post-charge relaxation), so the late-night drain is only bounded to ≈2–8 mA. The read-only stock comparison (ledger F18–F27, `docs/knowledge/stock-suspend-re-ledger.md`) found four real differences; 27 implements the three without storage risk.

## What 27 changes``````````````````````````````````

| Gap | Change | Switch (/data/system/platform/power-features.json) | Kernel default |
| --- | --- | --- | --- |
| C panel | Screen-off sends the stock GC9503V lcm_suspend table (vendor pre-sequence, display off, sleep-in, 25 analog writes) and leaves reset high 50 ms (panel.c). Any DCS failure falls back to 26's display-off, sleep-in, reset-low. Screen-on unchanged: reset pulse + full init. | panel_stock_suspend (/sys/module/panel/parameters/stock_suspend) | N (26) |
| A VGP2 | DTS regulator-always-on removed from VGP2 (CS43131 VA/VP/VCP, its only user in stock). The audio card holds one reference unless the switch is set; then the codec's runtime PM turns VGP2 off with VD/VL while idle (GPIOs first, VGP2 last, as stock cs43131_power_down_hw). DTB validator requires the new contract. | vgp2_idle_off (/sys/module/y2_cs43131/parameters/vgp2_idle_off) | N (hold, 26) |
| B VSYS | pmic_sleep group 8: stock PMIC_INIT VSYS fields (slew rates, TRANSTD 3, VOSEL_TRANS_EN, VSLEEP_EN, QI_VSYS_VSLEEP 2, VOSEL_CTRL 1 last) inside the SPM enter, restored exactly (mode bit first) before any resume. Only while VSYS is in software mode with VOSEL = VOSEL_ON = VOSEL_SLEEP = readback (live 0x40, 2.2 V), else refused and counted (vsys_refusals). VSYS selectors stay unwritable: the voltage never changes. | pmic_sleep (15 = with VSYS, 7 = 26) | 0 |

`power_features` arms all three at `application_ready`; the sleep diagnostics rows record `panel_stock_suspend`, `vgp2_idle_off` and `pmic_sleep_state` (now with `vsys_refusals`).

Not changed: gap D (VEMC3V3, eMMC power-off needs a new storage suspend model).

## Tests

Host: `test_power_final_27` (stock panel table byte-exact against the decoded image, reset-high/fallback order, VGP2 hold balance, DTS/validator contract, switches), `test_pmic_sleep` (VSYS group reaches stock, mode bit last/first, refuses any selector mismatch, selectors unwritable), `test_vproc_sleep`/`test_pmic_lowpower` updated for the admitted VSYS mode bits. Build: kernel warnings unchanged (47, all in the vendor Wi-Fi driver). Platform: `validate.py` PASS, ELF closure 354 PASS, installed ARM PASS (40 modules), privacy clean, inventory 108 packages, container suite 701 OK (693 + 8).

## Owner checks after the flash
  - Boot, screen on/off several times (panel wakes every time; `dmesg | grep -i "panel\|gc9503"` has no

`stock power-down cmd … failed`), and a screen-off longer than a minute.
  - Play music after the DAC has been idle (first play after a pause; listen for pops), with and without headphones in.
  - `cat /run/y2/power-features.json`: `panel_stock_suspend`, `vgp2_idle_off` = Y, `pmic_sleep` = 15;

`cat /sys/kernel/debug/regulator/regulator_summary`: `vgp2-audio` use 0 while idle.
  - One short sleep, then `pmic_sleep_state` (`entries` up, `vsys_refusals=0`, `last_changed` includes the VSYS bits

0x3c0) and the PMIC capture (0x256 row now matches).
  - Overnight: start ≥4 h after charging, ≥12 h; compare the late-night voltage slope with 26's (archive 124).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
