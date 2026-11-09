---
title: "Charging current policy (POWER-FINAL-07) - Innioasis Updater"
description: "Charging current policy POWER-FINAL-07 <!-- knowledge-base-scope: current-production-policy -- 2026-10-10. Source-complete and offline-tested; not physically qualified ab"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-charging-current-policy.html"
---

# Charging current policy (POWER-FINAL-07) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Charging current policy (POWER-FINAL-07)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Charging current policy (POWER-FINAL-07) 2026-10-10. Source-complete and offline-tested; **not physically qualified above the 450/650 mA selectors**. Supersedes the 70/450/650 mA statements in [the M4 charging record](m4-charging.md), which stays as history. 

## What was verified from the vendor code``````````````````````````````````````````````````

| Item | Evidence |
| --- | --- |
| Selector table | Stock CS_VTH at 0xc07572f8: 16 words, units of 0.01 mA, index = CHR_CON4 field. Read from fm-decompressed.bin: 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 650, 550, 450, 300, 200, 70 mA. Identical order to BSP CS_VTH_PMIC[] (charging_hw_pmic.c). The owner-supplied mapping was checked entry by entry against this array and is identical. |
| Programming | charging_set_current (0xc04cb934) applies bmt_find_closest_level (closest entry that does not exceed the request) and writes the index with upmu_set_rg_cs_vth. Linux uses the same floor rule. |
| Source types | Stock detection charging_get_charger_type (0xc04cb2a8) stores only 1 STANDARD_HOST, 3 NONSTANDARD, 2 CHARGING_HOST, 5 APPLE_2_1A, 4 STANDARD_CHARGER. The BSP flow is DCD, A1 (Apple vs nonstandard) or A2/B2 (SDP, CDP, DCP). Types 6 and 7 (Apple 1.0/0.5 A) are consumed by select_charging_curret but never produced on this unit. |
| Per-source request | select_charging_curret (0xc03a1d88): type 1 = 500 mA (PMIC floors to 450), 2 and 6 = 650, 3 and 4 = 1100, 5 = 800, 7 = 500, else 70 mA. These differ from the reference cust_charging.h (AC 650, nonstandard 500), so they are product-specific values. |
| Lifecycle | Pre-charge to CC at 3400 mV, CC to top-off at 4050 mV, recharge below 4110 mV, top-off timeout 10800 s, total 86400 s, software termination after six samples at or below 150 mA (BAT_*Action, 0xc03a205c..0xc03a2328). Linux keeps these except termination and recharge: it stops on the first sample at 4.175 V (no validated absolute current for the stock taper rule; POWER-02 overshot while waiting). From POWER-FINAL-12 a hold that ends an active cycle is Full when it rests at or above 4.07 V for six spaced samples (the pack relaxes to about 4.09-4.10 V; with the stock 4.11 V rule it restarted every ~70 s and never reported Full); below 4.07 V charging resumes; after Full a maintenance cycle starts only below 4.00 V. |
| HV detect | Stock charger_hv_detect_sw_thread_handler sets the 7 V HV threshold, reads the HV status and services the watchdog every 2 s. Linux requires CHR_CON0 bit 0 (VCDT_HV_EN) set, with the 7 V input OVP; the single historical 0x80 fault was this check failing (CHR_CON0 read 0x62). What cleared the bit is not established. |
| PMIC thermal | Stock mtk_ts_pmic.c: trip ladder 50..120 C, critical 150 C. No battery NTC is read (force_get_tbat returns 25 C). |

## The three different limits````

| Limit | Value | Source |
| --- | --- | --- |
| Hardware selector range | 1600 mA | CS_VTH |
| Highest stock request | 1100 mA (DCP, nonstandard) | select_charging_curret |
| Verified cell charge rating | unknown | no label, datasheet or manufacturer value in evidence |

Selectors 0 to 4 (1200 to 1600 mA) are in the table but are rejected by the PMIC write boundary (`kernel/platform/policy.h`) and by the sequencer, because no stock source requests them.

## Policy

One table (`charge-table.h`), one decision function (`charge-limits.h: y2_charge_decide`), one programming path. The result is the minimum of:
  - Stock request for the detected source (`source-policy.h`). SDP follows the USB allowance (500 mA configured,

100 mA unconfigured, 0 in reset/suspend, 70 mA before a data controller exists).
  - Class ceiling: SDP 500, CDP 650, DCP 1100, Apple 800, nonstandard 70, unknown 70 mA. Nonstandard stays at the

previously validated 70 mA: BC1.2 defines no capability for it and there is no validated VBUS-collapse check.
  - Deep discharge: 450 mA at or below 3.4 V.
  - Thermal cap from the PMIC die (60 C: 450 mA, 70 C: 200 mA, 80 C: 70 mA, 90 C: pause; 5 C hysteresis; the 150 C

latched fault is unchanged). The die is not the cell and the linear charger dissipates `(Vchr - Vbat) * I`, so this is a protective heuristic, not a pack temperature.
  - Owner ceiling (`BAT0/constant_charge_current_max`): default 650 mA, accepts only exact permitted table

steps, root-only, volatile (reverts at boot), logged when raised above 650 mA. It is a ceiling; the policy still picks the selector. A PC port is capped at 450 mA whatever the ceiling.

The result is floored to a table step, so it can never exceed any input.

## Why the default stays at 650 mA

The stock firmware requests 1100 mA on this exact product, which is real evidence about the original pack. It is not a cell rating: the stock sense-resistor constant (68 mohm) disagrees with the hardware, the stock model capacity (1300 mAh) is a compiled constant, and there is no pack temperature sensor. The PMIC die already reaches 43 to 46 C at 450 mA while the system runs. Until a cell charge rating, or independent source-side current and pack temperature measurements, exist, the 1100 mA path is implemented, tested and reachable only by an explicit owner ceiling.

## Thermal reality of a linear charger

The MT6323 charger is linear: the die dissipates `(Vbus - I * 0.2 ohm - Vbat) * I`. With an assumed 5.0 V source (VBUS is not measured; a real source sags with cable drop) and a 3.78 V cell this is about 0.51 W at 450 mA, 0.71 W at 650 mA, 0.85 W at 800 mA and 1.0 W at 1100 mA, and more on a lower cell voltage (about 1.4 W at 1100 mA and 3.5 V). Live evidence (`out/deep-sleep-final/evidence/20261010/91-power07-charging-readonly/`, 06 image, USB SDP, 450 mA selector, system running): the PMIC die rose from 36.9 C at boot to 46.9 C after 28 minutes of charging and was still rising. The 60 C step of the derating ladder is therefore expected to engage during sustained high-current wall charging, which makes the higher selectors thermally self-limiting by design. Whether the real limit is the die or the cell is not known without a pack sensor; that is why the ladder uses the stock PMIC trip points and why the ramp tool stops at 55 C.

## Measurement

`charging_state` reports three separate quantities: the stock request (`stock_request_ua`), the programmed selector (`charge_limit_ua`, `selector`) and `sense_current_est_ua`.

The estimate is `(ISENSE - BATSNS - offset) / 200 mohm`. Evidence: 16 constant-current samples at the 450 mA selector average 98.3 mV across 3.70 to 4.17 V, 2 samples at 650 mA (DCP) average 139.6 mV, and the zero-current offset is about 2 mV, giving 0.21 ohm. The BSP header uses `CUST_R_SENSE 200` for the internal linear charger (68 only for an external FAN5405/BQ24158), which fits; the stock Y2 binary compiles 68, which does not. The estimate reads about 6 percent above the selector label. It is the charger path only: not USB input current, not net battery current (the system also draws from the battery), and unvalidated without an external meter. It is deliberately not exposed as `current_now`.

## Not done

No VCDT (VBUS) ADC channel is read, so a collapsing source is not detected. No pack-temperature or current calibration exists. Termination is voltage-limited rather than the stock current-taper rule. No high-current mode was exercised on hardware.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
