---
title: "Stock CPU DVFS evidence and current admission - Innioasis Updater"
description: "Stock CPU DVFS evidence and current admission <!-- knowledge-base-scope: maintained-summary; baseline02-sync 2026-10-03 -- Current Baseline02 / UART01 scope UART01 before"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-hardware-final-dvfs.html"
---

# Stock CPU DVFS evidence and current admission - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Stock CPU DVFS evidence and current admission

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Stock CPU DVFS evidence and current admission

## Current Baseline02 / UART01 scope

UART01 before/after C3 readback passes all five guarded OPPs: 598/747.5/1040 MHz at 1.15 V, 1196 at 1.20 V and 1300 at 1.25 V. The earlier PWRAP admission failure is resolved. Current source retains the source-backed software VOSEL bank 0x21e, ordering, silicon/PWRAP checks and thermal authority; the older 0x220 stock analysis below is historical. Worst-case endurance/charging comfort and natural thermal-trip qualification remain open.

[Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) carry exact identities, counters and limits.

## Historical source research and physical checkpoints

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Hardware Final: stock CPU DVFS admission and qualification

Latest physical correction boundary, 2026-09-27: Fix01 recognizes the actual software VOSEL bank `0x21e`, selector/NI feedback `0x48` at 1.15 V. 1196/1300 MHz still fail admission at `pwrap_readiness` (-95); the three raw predicate operands were not available. No voltage-changing transition was physically exercised. The old `0x220` bank and admission design below document the stock-kernel path, not the current loader's selected software bank. [Current source/physical comparison](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md%23opps-dvfs-and-thermal-authority&anchor=opps-dvfs-and-thermal-authority).

2026-09-27. This is the pre-implementation scope audit for the owner's combined Hardware Final campaign. The campaign authorizes source-backed stock DVFS; neither the earlier planning epic nor this audit qualifies a new operating point. Default maximum remains 1040 MHz. No intermediate image is planned.

The retained physical Hardware 02 predecessor census identifies this unit's `devinfo[3] & 3 = 2`, `devinfo[15] >> 28 & 7 = 0` (Hardware Ceiling receipts 32–34). Exact stock `PTP_get_ptp_level` at `0xc0045e90` maps those fields to table 0. Runtime admission must independently parse the bounded, reserved LK ATAG area and require those same fields; no private fuse array is exported. The known baseline is 598/747.5/1040 MHz at 1.15 V. Physical timer, hotplug and suspend results remain separate gates.

The retained stock kernel's `mt_cpufreq_pdrv_probe` at `0xc0036378` and `mt_cpufreq_volt_set` at `0xc00361f8` establish the table-0 levels:

| Frequency | VPROC target | MT6323 selector | PWRAP slot |
| --- | --- | --- | --- |
| 598 / 747.5 / 1040 MHz | 1.15 V | 72 | 2 |
| 1196 MHz | 1.20 V | 80 | 1 |
| 1300 MHz | 1.25 V | 88 | 0 |

The sole PWRAP owner programs slots at `0xe4 + 8 * slot` with PMIC address `0x220`; each data value is `700 mV + selector * 6.25 mV`. This is not an unrestricted regmap VPROC write permission. The sole SPM owner requests the slot through `SPM_AP_DVFS_CON_SET` (`0x604`, bits 2:0), waits 5 microseconds and polls bit 31 with the stock bounded 100-by-5-microsecond acknowledgement budget. The exact stock `spm_dvfs_ctrl_volt` at `0xc0032cb4` matches that sequence. The pinned BSP's `mt_cpufreq_set` requires a further 40-microsecond voltage settle before raising frequency, and 30 microseconds after PLL programming. Higher rates use the existing MAINPLL/2 transition, with PCWs `0x800b8000` and `0x800c8000`. No FHCTL takeover, calibration or overclock is admitted.

Implementation admission requires a root-only runtime qualification control, an initial cpufreq QoS ceiling of 1040 MHz, exact own-bin validation, inherited SPM/PWRAP ownership checks, selected VPROC bank validation, slot/readback checks and a latched fault on uncertain transitions. Raise voltage before frequency; lower only after the lower frequency is verified. On an ambiguous PLL rollback, retain the higher voltage and refuse high OPPs. Preserve the existing sleep slots at 1.15 V and suspend operating point at 598 MHz. Generic WACS VPROC writes, 1.05-V operating OPPs and unmeasured undervolting remain prohibited.

The CPU nodes retain their shared OPP table but no longer attach cpufreq-dt to the generic MT6323 regulator. That regulator cannot independently request voltage through WACS: it remains always-on with the stock 1.15–1.25-V envelope. The CPU clock operation owns voltage sequencing through the existing wrapper and SPM owners. This also prevents two competing transition sequences. The Y2-only cpufreq-dt probe guard preserves the PMIC-readiness dependency before initial governor startup. A missing PWRAP owner defers the probe; it does not leave a prematurely started policy without voltage access.

Runtime controls are root-only under `/sys/module/cpu_dvfs/parameters/`: `qualification_max_khz` accepts 1040000, 1196000 or 1300000; `bin_supported` and `voltage_fault` report admission and the latched failure. Return to the 1040-MHz ceiling and verify a baseline running frequency before admitting a new maximum; qualification requires the active selector to be 72. Every high admission verifies slots and exercises a baseline 1.15-V SPM request first. The command requests a ceiling, not a current frequency. Use cpufreq's normal governor/userspace controls for bounded workloads, then read the actual rate. A latched transition fault refuses all high requests until a clean reboot.

Source and host fault tests cannot establish actual rail voltage, stable CPU operation, thermal margin or power benefit. The final candidate must first qualify 1196 MHz, then 1300 MHz, with the owner's existing 60°C test stop bound, readback/error checks and CPU/FFmpeg/SQLite/scan/radio/USB/GPU mixed workloads. Restore the 1040-MHz qualification ceiling after each bounded test. Final promotion depends on real measurements; these OPPs are physical-pending.

Targeted validation uses the production C functions in host fault fixtures: all 25 OPP transitions, raising/lowering failures, failed PLL rollback, invalid and truncated bin data, wrapper slot corruption, PMIC read failures, wrong bank/arbitration, SPM ownership, missing ACK and its exact timeout bound. The shared PLL test covers the five source frequencies and retained fallback. All four ARM objects compile in the locked production environment. The current production DT validates with a retained baseline initrd-size input; that is a DT-only check, not certification of a new image or stale final binary.

Private source extracts remain in `out/hardware-final-power-source/` and the retained `out/platform-v1-hardware-ceiling/stock-reference/`; the original kernel provenance is unchanged. The standing campaign roadmap audit is owned by the coordinating agent; this document records the precise voltage scope admission before implementation, without closing a milestone.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
