---
title: "Power, charging, suspend and safety audit - Innioasis Updater"
description: "Power, charging, suspend and safety audit <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-07_power_platform_audit.html"
---

# Power, charging, suspend and safety audit - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Power, charging, suspend and safety audit

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Power, charging, suspend and safety audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## Safety boundary

Unattended charging and current integrated suspend safety are UNKNOWN. This is not a claim that the device has been proven unsafe; it is a refusal to infer electrical/cell safety from a policy simulator, a voltage reading or an older owner acceptance. Do not change charging thresholds, rail voltages or memory reservations on the basis of this audit.

Sources: [charger policy](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/charger-policy.h), [charger driver](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/mt6323-charger.c), [source policy](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/source-policy.h), [USB PHY](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/phy-mt6582.c), [thermal](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/thermal.c), [SPM](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/spm.c), [DT](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/dts/innioasis-y2.dts), [offline charging](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/offline-charge.c), [suspend helper](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/sbin/y2-suspend).

## Charging/source ownership: F16

Good mechanisms are real: one PMIC/regmap ownership path; explicit register masks; protection/readback validation before enable; bounded I/O retries; fault latching; stop charger engines before disabling watchdog; actual forced watchdog strobes rather than cached regmap writes; source detection owned by the USB PHY rather than two competing BC1.1 drivers. Software tests inject register failures and check ordering. VERIFIED software mechanism / HIGH, not qualified charging safety.

Current policy inventory:

| Concern | Actual code policy | Evidence limit |
| --- | --- | --- |
| Charge target / software safety ceiling | 4.175 V / 4.200 V | ADC/calibration/cell-voltage accuracy and transient behavior need independent measurement. |
| Recharge | 4.110 V with time-qualified observations | Does not by itself validate cell state of charge or real recharge cycling. |
| Precharge/deep recovery | Threshold 3.4 V; current ceiling now 450 mA | Newer than the retained 70-mA experiment and older POWER-03 acceptance. |
| Timing | 3-hour precharge, 24-hour total, 3-hour top-off/CV budgets | Boottime accounting is useful; repeated reboot/source cycles and real pack behavior need review. |
| SDP source | Configured 500-mA allocation maps to 450-mA charging selector; smaller allocation to 70 mA; absent allocation inhibits | Battery charging current is not total USB input current under system load. |
| CDP/DCP/recognized higher-current source | Capped at 650 mA in current conservative policy | Detection and actual source/cable current limits require physical tests. |
| Unknown/nonstandard source | Conservative 70 mA | May not cover device load; that is not proof of successful charging. |
| Protection | Inherited/validated OVP/protection fields; source/input and battery OVP distinguished | Register acceptance is not fault-injection/electrical OVP qualification. |
| Watchdog | Approximately one-second worker, late-pet guard and hardware timeout | Host scheduler-stall tests cannot fully represent load/suspend/power faults. |
| Temperature | PMIC die and inherited protection checks; software die threshold 150°C | Not measured battery-cell temperature. |

The driver explicitly reports that pack temperature, current and SOC are unavailable. `isense`/battery ADC observations are not a calibrated `current_now` measurement. Do not use configured charge current as measured battery or USB current, and do not show invented battery percentages.

Completion is not absent: policy stops at target and uses multiple spaced engine-off observations to qualify HOLD/FULL, with a recharge hold interval. But this is a voltage/time policy, not a validated taper-current/coulomb-count/SOC algorithm. The label FULL must be interpreted within that limitation. Safety needs the actual cell specification, pack protection behavior, thermistor availability and measured voltage/current/temperature over the relevant cycle.

### Physical evidence must be version-specific

[70-mA baseline result](https://github.com/SchulzCode/Y2Linux/blob/main/docs/hardware-evidence/2026-09-14-m4-70ma-baseline/result.json) explicitly reports failure of useful sustained charge gain: same-boot endpoints fell ~39.990 mV over ~1015.808 s; subsequent observation was after charging had already been inhibited. It explicitly does not claim calibrated current/energy. This is valuable adverse evidence, not a passed charge test.

`out/m4-owner-acceptance.md` records owner acceptance of POWER-03/source `16875c4...`, not a newly measured charging/thermal/SPM series. Later commit `3dc0a8b` changes deep-recovery current policy to 450 mA. Neither the older 70-mA observation nor the earlier generic acceptance qualifies that new behavior. A current policy-to-image-to-measurement receipt is needed before broader public or unattended use.

## Low battery, offline charging and connected poweroff

Offline charging runs in initramfs before normal root/data/services, limits active subsystems, uses a power-button intent gate and avoids waking the full app merely because USB was attached. Its boot voltage guard uses a conservative 3.4-V threshold; it is not identical to every lower kernel policy constant. This is purposeful separation between minimal charging and normal-operation admission.

Normal Reborn [power adapter](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/power.rs) reads supplies, blanks the backlight and invokes platform shutdown. It does not implement low-battery warning/escalation/checkpoint-and-poweroff. No complete application/platform userspace graceful low-battery shutdown policy was found in the inspected normal path. MISSING / HIGH, distinct from the implemented boot/offline guard or hardware's eventual protection cutoff.

Power-off while connected, unplugging during offline charging, deeply discharged recovery, PMIC power-key long hold, brownout during DB/state writes and cable reinsertion need physical scenario testing. A successful `poweroff` syscall or a boot voltage threshold does not prove the device remains off or preserves data under every charger condition.

## Runtime power and deep suspend: F17

The MFG generic power domain, G3D gate and Lima ownership are cleanly separated. GPU01 records runtime-idle domain/clocks powering down after contexts close. With a live context/scanout, userspace and display ownership differ. Reborn screen-off releases renderer resources and blanks the display, while playback can continue; this should not be conflated with system suspend.

`y2-suspend` takes an exclusive activity lease, temporarily quiesces radios, checks shared connectivity state and attempts memory suspend with restoration logic. Audio and radio shared leases inhibit it. This is a sensible first policy for a player; do not bypass those checks to make a suspend test pass.

Physical [GPU01 suspend evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md) records a failed real attempt and a staged CPU3 shutdown timeout. Status changed at bit 9 while code waited for bit 13; CPU restart was correctly refused after the ambiguous transition. A later source correction addresses the observed mismatch, but the retained record leaves same-boot suspend/resume qualification open. PARTIAL / HIGH. “M4 accepted” cannot erase a subsequently observed integrated failure.

Required evidence for offered deep sleep: bounded CPU-off/on before full entry; same boot ID after Power/RTC wake; balanced PMIC IRQ/clock state; eMMC persistence; display/Lima reopen; audio and radio service restoration; repeated cycles and suspend refusal during active playback. Do not describe suspend-during-playback as seamless if the intended policy is to refuse it. Both successful refusal and subsequent idle suspend are meaningful tests.

## RTC, thermal, CPU frequency and memory

RTC uses the MT6323/mt6397 subsystem with error/epoch fixes and HCTOSYS; an alarm wake source is declared. Wall-clock persistence and alarm wake are different claims. Same-boot alarm resume is not proven by merely creating `/dev/rtc0` or reading a plausible time.

Thermal code reads calibration via nvmem/efuse and rejects invalid data, rather than fabricating temperatures. It preserves inherited protection ownership. DT's CPU passive/critical points are 110/120°C and PMIC critical 150°C, based on the current board evidence. These are die policies, not safe battery-surface limits. No sustained worst-case playback+scan+radio+charge thermal qualification was found. Do not reinterpret old suspect sensor readings as calibrated pack temperature.

CPU OPPs are 598, 747.5 and 1040 MHz, all at 1.15 V. The normal boot helper selects schedutil; the kernel fallback governor is conservative. This is frequency scaling at fixed voltage, not demonstrated dynamic voltage scaling. GPU has a fixed stock-derived frequency policy, not a new DVFS ladder. Keep the unqualified voltage dimension closed.

Memory reservations and DMA addressing are consequential hardware contracts. DT keeps the historical loader gap and connectivity reserved range, HIGHMEM is enabled, and no speculative GPU carveout/CMA pool was added. A 1-GiB marketing description is not a reason to reclaim reserved bytes. This audit changes none of them.

## Current / target / gap

CURRENT: substantial source-aware power implementation, containment, offline charging, historical normal-operation/owner evidence, and a known integrated suspend regression history.

TARGET: a narrow, documented operational envelope with validated charging/source/temperature behavior, graceful low-battery handling, and proven suspend policy for the features actually offered.

GAP: current hardware evidence, pack safety information and selected missing normal-runtime behavior. This is not solved by adding more nominal tests or increasing charge current until the voltage rises. Before a hardware/memory/power milestone change, follow the standing roadmap/gap audit and obtain the owner's explicit scope decision.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
