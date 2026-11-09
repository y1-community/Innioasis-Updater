---
title: "Y2 CPU Final Fix03 physical qualification — prepared, not run - Innioasis Updater"
description: "Y2 CPU Final Fix03 physical qualification — prepared, not run <!-- knowledge-base-scope: historical-validation-receipt; baseline02-sync 2026-10-03 -- Historical exact-ima"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-fix03-physical-qualification.html"
---

# Y2 CPU Final Fix03 physical qualification — prepared, not run - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 CPU Final Fix03 physical qualification — prepared, not run

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 CPU Final Fix03 physical qualification — prepared, not run

Historical exact-image receipt. This report retains its named Fix image and dated result. It does not describe Baseline02 or negate the newer bounded UART01 C1/C2/C3 passes. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [latest CPU-idle hardware proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

Status: NOT_RUN. This page prepares the single owner-controlled acceptance run of the [Fix03 candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX03.md). Nothing here is a hardware result. Every row stays NOT_TESTED until a receipt from the installed Fix03 identity replaces it. The [Fix02 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md) remains the authoritative physical baseline until then.

## Owner action
  - Verify `SHA256SUMS` in `out/y2linux-cpu-final-fix03-candidate/`.
  - Install only BOOTIMG and ANDROID/Y2ROOT with

`MT6582_preserve_data_scatter.txt`, through the existing preserving workflow.
  - Start the temporary Wi-Fi observer over USB, as in Fix02. The session-local

wrapper is in `out/cpu-final-fix02-physical-qualification/20260929T152328Z/`: `export PATH=$PWD/$E/bin:$PATH`, `ssh y2 sh < $E/wifi-listener.sh`. Then run:
`python3 tools/development/qualify-cpu-fix03.py --run --host y2 --wifi-host y2-owner-wifi --allow-warm-reboot`

Owner inputs, all prompted: one USB unplug if charging is active (Wi-Fi then carries the run), one Power press for the Power-wake test, and the USB reconnect afterwards.

## What the harness checks

Awake checks run first, each with its own receipt:``````````````

| Step | Pass criterion |
| --- | --- |
| Identity | Installed build/Reborn/kernel/rootfs match the package manifest |
| Regression gate | Timers, highres/NO_HZ, 1-ms sleeps, QoS with Back (158), MMC runtime gating with verified data, PWRAP 1196/1300 MHz at 1.20/1.25 V |
| Coordinator parking | 3→2→1 parking in a silent screen-off window. The display wake restores 0-3, with hold_ms=60000 and pressure_restores=0 afterwards |
| SLIDLE radios-off | Run as a detached device job: SLIDLE entries advance, slow_reject_bus stays 0, restore failures 0 |
| USB loaded stress | 10 × 1 MiB up/down SHA-256 roundtrips, observed over Wi-Fi. irq_max_burst, irq_max_jiffy and irq_progress are recorded |
| SRAM journal | Awake self-test, plus warm-reboot retention over whichever host answers |

Only if every awake check passes:````

| Step | Pass criterion |
| --- | --- |
| Charger | Refusal only while charging is active, verified from failed_stage=DPM_PREPARED error=-16 |
| Staged PM | freezer/devices/platform/processors/core on the same boot, taint unchanged |
| Full RTC suspend | Same boot ID, RTC IRQ serviced, journal reaches EXIT |
| Power wake | One deliberate press on the same boot |
| Five RTC cycles | Each the same boot, then post-resume CPU/USB/MMC/Reborn/audio state |

If a backstop reset happens, the harness reads the previous boot's timed ring, names the last stage reached and the stalled call (for example `DEVICES_RESUMED` → `console_resume_all`), and records the decoded RGU cause (`/sys/firmware/y2_pm/reset_status`). That names the next single correction; it is not a pass.

## Not changed and not claimed

C3 stays default off. The screen-off frequency ceiling and the BSP 110/120 °C trips are unchanged owner decisions. No electrical power measurement is part of this run.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
