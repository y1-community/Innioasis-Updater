---
title: "POWER-FINAL-14 — 13 plus persistent sleep and USB diagnostics - Innioasis Updater"
description: "POWER-FINAL-14 — 13 plus persistent sleep and USB diagnostics Status: IMPLEMENTATION READY PHYSICAL NOT RUN sealed, awaiting the owner flash. Package out/y2linux-platform"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-14.html"
---

# POWER-FINAL-14 — 13 plus persistent sleep and USB diagnostics - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-14 — 13 plus persistent sleep and USB diagnostics

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-14 — 13 plus persistent sleep and USB diagnostics

Status: IMPLEMENTATION_READY_PHYSICAL_NOT_RUN (sealed, awaiting the owner flash). Package `out/y2linux-platform-v1-power-final-candidate-14/` (fallback = sealed 13), symbols `…-14-symbols/`, receipts `out/deep-sleep-final/build14-receipts/`, branch `power-final-14`. Identity: Linux `9d06ac4deb158183f56f845086aaa307ce836177`; Reborn `63ac4a75286944ac0c57a2f15bb3b841923dd0f3` (code identical to `71ddb0d`). BOOTIMG `273dc927fbdb5778089ad76179ae92f8a32cb7625a83b39cc0850b572d7d3e5a`, Y2ROOT `78203697a71be7669c9e6f88dedc3a6daa80cd8ff6876d35779e86bb6ba314b9`. Fallback = sealed 13.

## Change
  - `sleep_diagnostics.py` (new): bounded private `/data/system/platform/sleep-diagnostics.jsonl` (2 × 2 MiB, 64 KiB per

row, fsync). Rows at `kernel_suspend`, `kernel_resumed` (with `golden`), `restoring_radios`, `complete_result_*` and `product_failure`. A row holds `vproc_sleep`/`vproc_sleep_state`, `lp_sel`, `phy_savecurrent`, wheel `sleep`, `y2_infra/state`, SPM `state`, the USB/network snapshot and a filtered `/dev/kmsg` tail (USB, gadget, sleep path; at most 80 lines). There is also a row on a UDC state change and one 30 s later, at most one row per 10 s.
  - `power_journal.py`: every row gains `usb_net` (UDC state, configfs UDC, `usb0` operstate/carrier/IPv4 from

`/proc/net/fib_trie`, interface counters, y2-usb status summary, OUT-path counters, `umtprd`/`dropbear` running). Shared bounded append helper; per-second USB watch on the existing power sample.
  - `suspend_record.py`: calls the diagnostics on the stages above; refusals write nothing.
  - Identity bump; scope audit: POWER-FINAL-14 entry in `docs/planning/roadmap-gap-audit.md`.
  - Read-only sysfs/procfs. A failure is counted, never raised, and never blocks sleep. SSH stays bound to `usb0`.

## Evidence behind the change

Archive 104: 13 slept 12,104 s (7 suspends, 6 maintenance wakes, Power wake, `complete_result_0`). After the wake, USB enumerated but passed 0 bytes. The hold-Power restart then lost every 13 counter, and the syslog kept only boot start-up. The same USB failure recurred at 20:56 (0 bytes, MTP dead too).

## Tests

Locked-container production suite: 8 suites OK, 664 cases, 10 host-dependency skips (13: 651; plus 12 `test_sleep_diagnostics` cases and the `package.py --stock` case). The run ended at the same final step as 13's; its exit code was not captured. Packaging-host tests: 32 PASS. Splash: 27 PASS. Package validation, ELF closure (385 files / 1,416 dependency edges), installed-ARM (39 modules), inventory (106 packages) and privacy (1,442 root files, no private state) PASS. Host regression comparison against `main`: the same 38 host-environment failures, and 524 tests against 512.

## Not verified

Everything physical: that the rows are written on the device at each stage, their size and timing on eMMC, and the `/dev/kmsg` filter on real messages. Defect B is not fixed; 14 only makes it observable.

## Verdict

IMPLEMENTATION_READY_PHYSICAL_NOT_RUN

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
