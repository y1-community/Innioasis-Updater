---
title: "Suspend state probe — test plan (proposed, not yet run) - Innioasis Updater"
description: "Suspend state probe — test plan proposed, not yet run Goal: obtain the real PMIC/regulator/clock/GPIO state just before and just after sleep on DEEPSLEEP-FINAL-04 and com"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-suspend-state-probe-plan.html"
---

# Suspend state probe — test plan (proposed, not yet run) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Suspend state probe — test plan (proposed, not yet run)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Suspend state probe — test plan (proposed, not yet run)

Goal: obtain the real PMIC/regulator/clock/GPIO state just before and just after sleep on DEEPSLEEP-FINAL-04 and compare it with the awake baseline (archive 78) and the vendor suspend golden table (25 of 44 entries differ awake). This is evidence for ranking candidates; it is not a measurement of current and not a reading taken while the SoC sleeps.

## What the probe does (read-only)

`tools/development/power-session/suspend-probe.py` runs on the Y2 (stdlib Python, copied to tmpfs `/run/y2`). It reads the PMIC register dump (`/sys/kernel/debug/regmap/1000d000.pwrap/registers`, ~26 ms), regulator and clock summaries, GPIO, wakeup sources, SPM state, runtime-PM status. Captures: `pre-entry` (journal `suspend_syncing`, 0.1–0.7 s before freeze), `maintenance` (0.8 s after each maintenance wake), `post-resume` (first userspace instant after a BOOTTIME jump). A capture during which a suspend began is flagged `suspend_during_capture`. It never writes PM/PMIC/RTC/guard/wakeup state and holds no wakeup source. Captures go to `/data/logs/suspend-probe-<boot>-<time>/NNN-label.json` (small; ~60 KB each, max 24).

## Device changes if approved

Only: the probe file and log on tmpfs `/run/y2`, and its capture directory under `/data/logs`. No product, kernel, helper or policy change; the 04 image is untouched.

## Procedure
  - Owner: connect USB, device on the player, paused. Claude: archive first (`capture-return.py`), then `arm-suspend-probe.py` under the host lease.
  - Owner: screen dark, unplug, tell Claude the time, wait ~25 minutes untouched (>= 2 maintenance wakes; sleep starts ~40–60 s after darkness).
  - Owner: re-plug and tell Claude. Claude: archive first, then analyse: `tools/development/analyze-suspend-probe.py <captures> --baseline <archive 78 regs.txt>`.
  - Compare: rails on at pre-entry/maintenance/post-resume; LP_SEL bits; golden differences remaining; enabled clocks; SD/eMMC/connectivity/USB runtime-PM state.

## Stop conditions / safety

Probe self-limits (`--max-seconds` 3600, 24 captures) and stops on boot change. If a stall/reset occurs, do not restart; connect USB and archive (04 stall records apply). Do not read `/sys/power/wakeup_count` or `/proc/kmsg` over SSH.

## Interpretation limits

Registers read at pre-entry are the state before the freezer/SPM acts; the SPM/PCM may change PMIC state during sleep and restore it before post-resume. A difference between pre-entry and the golden table is therefore a candidate, not proof of a leak. A true during-sleep current needs an external measurement.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
