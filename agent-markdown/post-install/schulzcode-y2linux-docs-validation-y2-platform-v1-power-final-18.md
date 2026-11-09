---
title: "POWER-FINAL-18 — stock PMIC suspend fields - Innioasis Updater"
description: "POWER-FINAL-18 — stock PMIC suspend fields Status: INSTALLED, FIRST BOOT HEALTHY; tagged baseline-18 2026-10-13. Package out/y2linux-platform-v1-power-final-candidate-18/"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-18.html"
---

# POWER-FINAL-18 — stock PMIC suspend fields - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-18 — stock PMIC suspend fields

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-18 — stock PMIC suspend fields

Status: INSTALLED, FIRST BOOT HEALTHY; tagged `baseline-18` (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-18/` (fallback = 17 = `baseline-17`), receipts `out/deep-sleep-final/build18-receipts/`. BOOTIMG `5d4052282f37f224c4328ffdd1a2e167c0213596f2ba90c147a9574219042ace`, Y2ROOT `718528695cdd681fe093fc895c1c4c0285ab0c5c4a616246d1548ea36b32c612`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-18`, kernel `6.18.56-y2linux-platform-v1-power-final-18`, root `2026.08-platform-v1.48`, release `1.0.0-platform-v1-power-final-candidate.18`; Linux `d2fff53` on `main` (later: test-only commits), Reborn unchanged (`217e28d`). Flash BOOTIMG + ANDROID only with `MT6582_preserve_data_scatter.txt`, Download Only. Scope audit: "POWER-FINAL-18 PMIC suspend-field scope audit" in the [roadmap gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## Why

17 showed that the SoC side of sleep is now stock-identical (REA on the stock kernel, [ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstock-suspend-re-ledger.md) F14) while INFRA still never powers down and the night drain was ≈8.6 mA on 16. All 15 PMIC rows that still differed from the stock suspend golden were mapped to stock field names (F15). The prime suspect is the PMIC's audio 26 MHz clock-square request, `rg_clksq_en_aud`: stock clears it when no analog audio is in use and in its audio suspend hook; Linux never wrote it, so the bootloader's 1 stayed set all the time (F16).

## What 18 changes``````````````````

| Group (pmic_sleep bit) | Stock suspend value applied inside the SPM enter callback, exact restore before any device resumes |
| --- | --- |
| 1 audio clocks | 0x102[0] rg_clksq_en_aud 1 → 0; 0x70c[4] rg_adacck_en 1 → 0 |
| 2 unused PMIC clocks | 0x108[6] rg_drv_2m_ck_pdn, 0x108[10] rg_rtc_mclk_pdn, 0x108[12] rg_efuse_ck_pdn, 0x10e[5] rg_auxadc_ctl_ck_pdn 0 → 1 |
| 4 VREF18 | 0x776[15] rg_vref18_enb, 0x778[15] rg_vref18_enb_md 0 → 1 |

The PMIC write policy admits exactly these bits. A field already at stock is not written; a failed write undoes everything already written and sleep continues unchanged. The PMIC golden capture now runs after the VPROC and PMIC steps, so `pmic_golden` shows what really enters sleep (the four VPROC rows no longer appear as differences). State: `/sys/module/pwrap/parameters/pmic_sleep_state` (`groups entries restores failures last_error last_changed pending`), also in every sleep-diagnostics row. Owner switch:`{"pmic_sleep": 0}` (or 1/2/4 subsets) in `/data/system/platform/power-features.json`.

Also: power-journal rows keep `suspend.reason` and `suspend.error` (17 lost why two requests were refused).

Not in 18:
  - VEMC3V3 (eMMC supply) off. Overlay 0029 keeps the root eMMC powered and in transfer state across suspend

without re-initialisation, because the storage firewall blocks the commands a re-init needs. Removing its supply would break the next root access. It needs a different eMMC suspend model first (CMD5 sleep and re-init through the firewall), which is separate storage work with data risk.
  - 0x108[9] headset-detect clock: Linux already gates it; stock keeps it running.
  - AUXADC hardware-mode/reset bits, VSYS/VPA sleep, depop VCM.

## Tests

Unit: `test_pmic_sleep` (apply reaches stock on 17's real entry values, bit-exact restore, per group, no write when already stock, failed write and failed readback undone, every write passes the production PMIC policy, VEMC enable closed), wiring order and switch, journal reason.

Locked-container production suite: 685 cases, exit 0 (17: 682). Two existing harnesses that compile the real `y2_spm_enter()` needed stubs for the new step (they now also check it is balanced on every abort and runs inside the VPROC window). Package validation, ELF closure, installed ARM, privacy and inventory PASS.

## Hardware results

**First boot (2026-10-13, boot `69ef8c26`, archive `out/deep-sleep-final/evidence/20261013/113-power18-first-check/`, captured at 27 s uptime; state re-read at 55 s):** kernel `-power-final-18`, taint 0, `application_ready` 44.3 s; `pmic_sleep=7`, `pmic_sleep_state groups=0x7 entries=0 failures=0`; `md1_gate=1 md1_sta=0x3ffffff`, `dcm_result=0`, `golden_apply=0xf`, `dis_pdn=1`; Wi-Fi (`wlan0`), Bluetooth (`hci0`), USB/SSH up, charging. Known lines only (eMMC erase, splash `Errno 22`). The first SSH attempt timed out during boot. Sleep test (1 h) next.

1-hour sleep (2026-10-13, archive `out/deep-sleep-final/evidence/20261013/114-power18-hour-sleep/`): unplugged sleep 12:20:56 → Power 13:23:47 (63 min), 3 entries / 3 resumes / 0 aborts, two 1800-s maintenance wakes, wake `0x20`; USB worked after the replug.
  - PMIC step:`pmic_sleep_state entries=3 restores=3 failures=0 last_changed=0x3f pending=0x0` — all six fields

applied and restored on every cycle. PMIC golden differences 15 → 7 (left: 0x04e/0x120 AUXADC modes, 0x108[9] accdet (Linux gates more than stock), 0x256 VSYS sleep, 0x310 VPA, 0x508 VEMC3V3, 0x70c[9] depop VCM). SoC golden 10/34.
  - INFRA still retained:`last_lost=0x0`, `pdn0 0x2fcffff` on all 3 restores. The PMIC audio clock request was not

the (only) INFRA blocker.
  - Wake: SPM return 95.13 s → DSI modeset 95.66 s (≈0.5 s, as 17).
  - USB: `dma_unmask_rearms=8`, `dma_unmask_lost=3` (real losses, re-armed, USB fine).
  - Audio after the wake: no playback logged before the capture (owner check pending). The Bluetooth

`SelectCodec ... no_eligible_codec` warning after reconnect also appears on 16/17 (SBC-only gate), not new.
  - No drain figure: the sleep started 18 s after unplugging from the charger (4.06 V charging → 4.02 V), relaxation

dominates an hour.

## What to check after the flash
  - Display, audio (headphones and Bluetooth), Wi-Fi, USB, charging as on 17.
  - `cat /sys/module/pwrap/parameters/pmic_sleep` = 7.
  - After a sleep: `pmic_sleep_state``entries` = sleeps, `restores` = entries, `failures=0`, `last_changed=0x3f`

(six fields); audio still plays after the wake; `pmic_golden` differences down (VEMC row and the unadopted rows remain); `y2_infra/state last_lost` (non-zero = INFRA finally powers down).
  - Overnight drain against 16's ≈8.6 mA (and 17's night if measured).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
