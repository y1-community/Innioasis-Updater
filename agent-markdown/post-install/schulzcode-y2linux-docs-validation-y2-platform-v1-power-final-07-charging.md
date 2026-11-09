---
title: "POWER-FINAL-07 — charging performance (vendor charging policy on the 06 base) - Innioasis Updater"
description: "POWER-FINAL-07 — charging performance vendor charging policy on the 06 base Status: implementation complete and offline-qualified; physical NOT RUN. The agent has not fla"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-07-charging.html"
---

# POWER-FINAL-07 — charging performance (vendor charging policy on the 06 base) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-07 — charging performance (vendor charging policy on the 06 base)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-07 — charging performance (vendor charging policy on the 06 base)

Status: implementation complete and offline-qualified; physical NOT_RUN. The agent has not flashed. Readiness: MORE_WORK_REQUIRED. High-current operation is implemented but not enabled and not qualified.

Identity: Linux `551baad703b31c4fadfd0db96478481c0f5067bc` (branch `codex/platform-v1-power-final-07`, from `codex/platform-v1-power-final-06` tip `bd7e54d`), Reborn `97ff8c357bab12319087740d7c97b5051e6588f5` (unchanged), kernel `6.18.0-y2linux-platform-v1-power-final-07`, root `2025.02.18-platform-v1.37`, release `1.0.0-platform-v1-power-final-candidate.7`, build `Y2LINUX-PLATFORM-V1-POWER-FINAL-07`. BOOTIMG `65a1daf484bb54cde14f6dd4906bd9b6b72872213a9409b2ea1fdc3fd38a3001`, Y2ROOT `83a61c1e73c5fa34acc7d6e9af707ac0fd54d20e1226da2ae278846ff6d19e66`. Fallback pair in `fallback/` is the sealed 06 (currently installed).

## SOURCE ANALYSIS

Vendor selector table (stock `CS_VTH`, `0xc07572f8`, 16 words, units of 0.01 mA, index = `CHR_CON4` field; identical order to BSP `CS_VTH_PMIC[]`): selector 0..15 = 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 650, 550, 450, 300, 200, 70 mA. The owner-supplied mapping matched entry for entry. Programming: `charging_set_current` (`0xc04cb934`) floors the request with `bmt_find_closest_level` and writes the index; Linux uses the same floor rule.

Stock source policy (`select_charging_curret`, `0xc03a1d88`; detection `charging_get_charger_type`, `0xc04cb2a8` stores only types 1, 3, 2, 5, 4): SDP 500 (PMIC 450), CDP 650, DCP 1100, nonstandard 1100, Apple 2.1 A 800, Apple 1.0 A 650 and 0.5 A 500 (consumed but never produced on this unit), unknown 70 mA. These differ from the reference `cust_charging.h` (AC 650, nonstandard 500), so they are product-specific.

Also verified from the stock/BSP code: BC1.1 flow (DCD, A1, A2, B2), pre-charge/CC at 3400 mV, CC/top-off at 4050 mV, recharge below 4110 mV, top-off timeout 10800 s, total 86400 s, charger watchdog service, `charger_hv_detect` thread, PMIC thermal trip ladder 50..120 C with 150 C critical, and `battery_meter_get_charging_current` (ISENSE-BATSNS over a sense-resistor constant). Differences kept on purpose: 4.175 V target with first-sample voltage termination instead of 4.2 V plus the 150 mA taper rule (POWER-02 overshot while waiting; no validated absolute current exists to run a taper rule).

## CURRENT LIMITS
  - SDP: stock 500 -> selector 12 (450 mA) once configured; 70 mA while unconfigured or before a data controller exists; 0 in reset/suspend; closest table step below any odd allowance. Never above 450 mA regardless of the owner ceiling.
  - CDP: 650 mA (stock).
  - DCP: stock 1100 mA, class ceiling 1100 mA, default result 650 mA (owner ceiling).
  - Apple (2.1 A signature): stock 800 mA, default result 650 mA.
  - Nonstandard: stock 1100 mA, class ceiling 70 mA (no defined capability, no validated VBUS-collapse check).
  - Unknown: 70 mA. Deep discharge (at or below 3.4 V): at most 450 mA.

## HIGHEST JUSTIFIED CURRENT
  - Requested (stock, DCP/nonstandard): 1100 mA.
  - Permitted by this build by default: 650 mA (hardware-exercised before). The owner ceiling can be raised, root-only, volatile, logged, to exactly 700/800/900/1000/1100 mA for qualification; 1200..1600 mA cannot be programmed.
  - Hardware-qualified: 70, 450 and 650 mA selectors (earlier images). Nothing above 650 mA has run.
  - Not yet qualified: 700..1100 mA, thermal derating on hardware, nonstandard-class charging, the charger-path current estimate.
  - Limiting evidence: no cell charge rating (no label, datasheet or manufacturer value; stock model 1300 mAh and the reference header's 1728 mAh are compiled constants; web sources only show other Innioasis models at 1250-1500 mAh),

no pack temperature sensor (stock reads a literal 25 C), no independent current measurement, and the PMIC die already reaches 43-47 C at 450 mA.

## PMIC / BATTERY

One table (`kernel/platform/charge-table.h`); the write boundary (`policy.h`), the sequencer (`charger-policy.h`) and the reporting helper (`power-math.h`) all use it. The CHR_CON4 write mask stays `0xf`; values 0..4 are refused by `y2_pmic_value_allowed`. Cell capacity and C-rate: not established; nothing in this build claims either.

## CC/CV BEHAVIOUR

Unchanged: hardware CV at selector 30 (4.175 V), independent 4.2 V sample guard, first-sample termination, recharge at 4.11 V after six 10 s confirmations. The `0x8` fault is the 4.2 V sample guard (POWER-02 waited above the target; fixed earlier). The single `0x80` fault was `y2_charge_protections()` finding `CHR_CON0` bit 0 (VCDT_HV_EN) clear (`0x62`) after about 38 min at 70 mA; the fail-closed inhibit worked, and what cleared the bit is not established. A current change always stops both engines, verifies, then re-programs and restarts through the hardware CSDAC ramp (no live current step). A high-current regression test covers CC -> hold -> full -> recharge at 1100 mA.

## THERMAL PROTECTION

PMIC-die ladder at the stock trip points: 60 C 450 mA, 70 C 200 mA, 80 C 70 mA, 90 C pause (`THERMAL_HOLD`, health OVERHEAT, no fault), 5 C hysteresis; 150 C stays the latched fault. The die is not the cell: this is a protective heuristic, not a pack temperature. Live trend on the 06 image (USB SDP, 450 mA): die 36.9 C at boot to 46.9 C after 28 min, still rising. The charger is linear; sustained high-current wall charging is expected to engage the ladder.

## USB COMPOSITE

Live read-only capture (`out/deep-sleep-final/evidence/20261010/91-power07-charging-readonly/`, 06 image): gadget `y2` bound to `musb-hdrc.4.auto`, functions `ecm.usb0` and `ffs.mtp`, UDC configured high-speed, MaxPower 500 mA / `bmAttributes 0x80`, `usb0` 10.42.0.1/24, MTP roots `/data/music` and `/media/sd`, `/media/sd` and `/data` mounted ext4. No USB gadget, MTP or storage code was changed in 07.
  - MTP, USB Ethernet, SSH, internal eMMC, microSD, simultaneous data + charging after the 07 flash: NOT_RUN (procedure: `tools/usb/qualify.py` while charging on a PC port, then a wall-charger session without reboot).

## PRODUCTION CLEANUP

Removed: three duplicate selector tables, the 70/450/650 allow-lists, `y2_source_charge_ua`/`y2_charge_selector`, and the mislabelled `selected_charge_ceiling_ua` observation key (now `programmed_charge_ua` and `owner_charge_ceiling_ua`). No debug sysfs, no polling added, no raw current interface; `charging_state` gained read-only fields. The owner ramp tool is a development helper and is not installed into the image. The broader production cleanup of the deep-sleep experiments remains scheduled after 06 qualification.

## TESTS
  - Locked-container production suite (`tools/production/tests.sh`): PASS, 598 cases (06: 581; +17 new), exit 0; 29 packaging-host and 27 native splash cases PASS.
  - New: `tests/test_charge_limits.py` (11 C and source-scan cases: table equals the stock array, write boundary, exhaustive decision invariants over source x allowance x voltage x thermal level x ceiling, thermal ladder hysteresis, source switching PC -> wall -> PC -> CDP -> Apple -> nonstandard without reboot, thermal pause/resume, 1100 mA CC/CV, ISENSE offset hygiene) and `tests/test_charge_qualify.py` (6, the ramp tool always restores 650 mA).

Mutation checks confirmed they fail when the nonstandard ceiling or the permitted-selector bound is broken.
  - Three old assertions encoded the three-selector policy (`test_power`, `test_power_policy`, `test_charger`'s 499.999 mA case) and were updated with comments; no failure was hidden.
  - Host broad run: same 48 environmental errors as the 06 baseline, none new (660 vs 643 tests).
  - Package validation, ELF closure (384 files / 1411 edges, no RPATHs), installed-ARM, release inventory, privacy (tree and root image): PASS. Kernel build: no warnings from the charger or policy objects; new strings present in the Image.
  - Reborn unchanged; see `validation/reborn-NOT-RERUN.md`.
  - Physical: NOT_RUN.

## COMMITS

`510b4e0` / `fd43f14` audit, `0b76407` charger policy and tests, `d254aab` tools/docs, `b47273b` release identity, `551baad` ISENSE offset hygiene (build commit), `b78e037` docs (after the build).

## OWNER ACTION

See `OWNER-HANDOFF.md`. Flash BOOTIMG + ANDROID only, tell me, I check identity and charger state read-only first.

## FINAL VERDICT

IMPLEMENTATION_READY_HIGH_CURRENT_QUALIFICATION_PENDING

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
