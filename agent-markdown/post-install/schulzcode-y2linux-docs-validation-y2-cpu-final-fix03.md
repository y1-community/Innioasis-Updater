---
title: "CPU Final Fix 03 implementation and candidate receipt - Innioasis Updater"
description: "CPU Final Fix 03 implementation and candidate receipt <!-- knowledge-base-scope: historical-validation-receipt; baseline02-sync 2026-10-03 -- Historical exact-image recei"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-fix03.html"
---

# CPU Final Fix 03 implementation and candidate receipt - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CPU Final Fix 03 implementation and candidate receipt

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CPU Final Fix 03 implementation and candidate receipt

Historical exact-image receipt. This report retains its named Fix image and dated result. It does not describe Baseline02 or negate the newer bounded UART01 C1/C2/C3 passes. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [latest CPU-idle hardware proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

Owner-authorized correction batch for the real-device failures recorded by the [Fix02 physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md) (2026-09-29). This pass changes software and produces one preserving candidate. It does not access or flash a Y2, and it restarts no architecture. Every Fix02 physical pass is kept as a regression requirement: timers, highres/NO_HZ, hotplug, QoS, thermal authority, WFI, MMC runtime gating, automatic parking, 1196/1300-MHz DVFS, SRAM self-test/retention, staged PM and charger refusal. Software tests are not physical passes. Sources are in the [Fix03 ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX03-SOURCES.md). The next run is prepared in [Fix03 physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX03-PHYSICAL-QUALIFICATION.md). Admission is recorded in the [Fix03 implementation boundary](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23cpu-final-fix03-implementation-boundary--2026-10-01&anchor=cpu-final-fix03-implementation-boundary--2026-10-01).

Starting Linux `19ab970` (Fix02 physical report commit); starting Reborn `77cf83e09a18f82a867040e72d35b6e70b26fa85` (unchanged, no Reborn change needed).

## 1. Full-suspend resume completion: diagnostics first

Evidence. The retained record from the Fix02 RTC attempt shows the Y2 resume stamp (`0x59325253`), SPM wake `0x20`, the resume vector, and every device resume/complete pair through `faux`. The last stage was `DEVICES_RESUMING` with error 0. `Y2_PM_EXIT` was never written, and the RGU backstop reset the board about 30 s after wake.

What was missing. The unmarked window was `dpm_resume_end` → `console_resume_all` (which ends in a synchronous `pr_flush(1000, true)`) → `platform_resume_end` → `suspend_finish` (thaw, `filesystems_thaw`, `PM_POST_SUSPEND` notifiers, `pm_restore_console`). No mark pinged the backstop there, and the ring had no time.

Change. Seven stages are appended, so old records still decode: `DEVICES_RESUMED`, `CONSOLE_RESUMED`, `PLATFORM_ENDED`, `TASKS_THAWED`, `FILESYSTEMS_THAWED`, `POST_SUSPEND_NOTIFIED`, `CONSOLE_RESTORED`. Each one marks the record and pings the backstop. Device callbacks ping it too, so only one call that makes no progress for the full period resets the board, not a long but progressing phase. Ring entries now carry `local_clock()` milliseconds. Every stage mark is also a ring entry (phase 254), interleaved with the callback trail, so the last line names the last boundary reached. Names keep a 16-byte tail. A Fix02-layout ring is reported as `fix02_layout` and not decoded. The SRAM window (0x0010dc00..0x0010e0ff), slots, stamp and 24-entry ring size are unchanged.

Reset cause. The watchdog probe reads MT6582 RGU `WDT_STATUS` (+0x0c) before its first `WDT_MODE` write. `/sys/firmware/y2_pm/reset_status` decodes it (`watchdog_timeout`, `software_reset`, `watchdog_irq`, `debug_reset`, `spm_watchdog`). `boot.json`, the previous-boot evidence and the status snapshot record that cause instead of `not_observed`. A zero value is reported as `rgu_status_none_reported`, never as proof of a power-on reset; whether the loader preserves the register is a physical question.

Not changed. One hypothesis: the console flush after resume may stall if UART or fbcon state was lost in SPM sleep. It is not established. With `loglevel=3` the suspend backlog is small, which weakens it. Per the handoff, the next RTC attempt names the stalled call, and only that call is corrected.

## 2. SLIDLE: the bus-DCM baseline

Root cause.`TOPCKGEN+4` is `DCM_CFG` (AXI bus DCM). The MT6582 BSP never initializes it (`DCM_ENABLE_DCM_CFG` is undefined, "use default value"), and `bus_dcm_disable` clears only bit 7 after `bus_dcm_enable` writes 0x8f. The stock idle baseline is therefore 0x00 before the first slow or deep idle, and 0x0f afterwards. The Y2 predicate demanded exactly 0x0f. The board reads 0x00, so with radios off and a zero clock mask every attempt failed `slow_reject_bus` (0 → 20809). This is the same class of mismatch as Fix01's PWRAP 0x1ff/0x7f.

Correction.`y2_bus_dcm_baseline()` accepts {0x00, 0x0f}. Anything else, including DCM already enabled by another owner, is still refused. `y2_ccf_slow_idle`, `y2_ccf_deep_idle_begin` and the read-only `dormant_preflight` all use it. The verified 0x8f write and the exact restore of the inherited value are unchanged. Clock blockers (APDMA/BTIF with radios on) remain legitimate refusals.

## 3. Loaded USB upload: a false storm

Root cause. The storm guard counted every interrupt per jiffy (HZ=100) and stopped at 512. With Inventra mode-0 RX DMA, a 512-byte packet costs one endpoint interrupt and one DMA interrupt, so the guard caps throughput at about 12 MB/s. In both Fix02 faults the ISR, DMA-interrupt and DMA-programming deltas match that per-packet pattern with no excess. Boot 1: 1155 interrupts for 611 programs, against a bound of 1222. A stuck source would have added ≥513 extra interrupts. The two snapshots show different, ordinary mid-transfer phases (RX pending, DMA channel 5 pending). Fix02 had also recorded a legitimate peak of 426 per jiffy. The handoff's re-arm hypothesis is not supported, and the Inventra/MT6582 RX and DMA paths stay unchanged.

Correction.`y2_usb_irq_storm()` counts only interrupts that occur without new accepted DMA programming (counted in the existing `channel_program` wrapper). It also keeps a hard ceiling of 4096 per jiffy, above the HS bulk maximum of about 2080. Both remain terminal with the existing snapshot and teardown. Status adds `irq_max_jiffy`, `irq_jiffy_limit` and `irq_progress`. PIO (`y2.usb_dma=off`) is guarded as before, since it has no DMA progress.

## 4. Policy defects``````````````

| Defect | Correction |
| --- | --- |
| A wake's start-up/render burst on the single parked CPU crossed the 1-s saturation threshold about 0.6 s before the display restore, so the hold doubled (Fix02: burst_ms=780 already before the wake) | A display, workload or input restore within 2 s of a pressure restore undoes that one escalation (wake_reclassified). The reset attribution is kept as observed. Sustained load without a wake still escalates |
| media.inventory() keyed SD presence on kernfs inode/ctime; drop_caches remounted /media/sd twice | The key is now dev_t, the disk sequence number and CID. Reclaim no longer looks like a change, and a re-enumerated identical card still does |
| admission_error=1 meant success (the positive return of freq_qos_update_request) | Successful admission reports 0 |

## Harness

`tools/development/qualify-cpu-fix03.py` corrects the six Fix02 harness defects: Back (158) drives QoS input; parking and radios-off SLIDLE are separate verdicts; the warm reboot falls back to Wi-Fi; per-process percent is of one core; charger refusal is read from `failed_stage=DPM_PREPARED error=-16`; and a launch step runs once on one probed host, with the `rtc-alarm` output captured to a receipt. It adds the display-wake hold check, a detached radios-off SLIDLE job, five RTC cycles, and the naming of the stalled resume call from the timed ring.

## Tests added

`tests/test_cpu_fix03.py` exercises the real functions on host models. It covers the bus baseline for slow and deep idle, including exact restore, refusal of 0x8f and the shared preflight predicate. For USB it replays the Fix02 counts and checks a stuck source, the hard ceiling and the driver wiring. It covers wake reclassification and its boundaries, SD identity across kernfs reclaim and re-enumeration, the order of every resume-window mark, the timed ring decode with stage entries, backstop pings on callbacks, RGU decode, the probe read order and the `boot.json` cause, the DVFS label, and the harness helpers and plan. Fix02/Final fixtures were updated to the new ring contract and guard state.

## Final software receipt

| Identity | Commit/version |
| --- | --- |
| Starting Linux / Reborn | 19ab970b4aeda5bece021058f6fd3068f0b942f1 / 77cf83e09a18f82a867040e72d35b6e70b26fa85 |
| Built Linux runtime | 76a5d41df683a1680b1127393deb0101aafe7697 |
| Built Reborn | 77cf83e09a18f82a867040e72d35b6e70b26fa85 (unchanged since Fix02) |
| Kernel / root | 6.18.0-y2linux-cpu-final-fix03 / 2025.02.18-platform-v1.9 |
| Release / build | 1.0.0-cpu-final-fix03-candidate.1 / Y2LINUX-CPU-FINAL-FIX03 |

A first build from `6dfbfe7` failed the container regression suite. One older fixture (`test_hardware_ceiling` DMA observer) did not define the new progress counter. The fixture was corrected in `76a5d41` (test-only), and the candidate was rebuilt, repackaged and revalidated from that commit. The superseded outputs are kept privately with a `superseded-…-6dfbfe7` prefix. A later documentation commit seals this receipt and changes no built kernel or userspace (recorded in the candidate's `sources/campaign-docs-commit.txt`). The Git identity, its configuration and the authenticated account are unchanged. There is no model attribution and no push.````

| Fresh check (isolated worktrees at the built commits) | Result |
| --- | --- |
| Kernel/config/modules, production DT, BOOTIMG/memory bounds (artifact validation) | PASS; BOOTIMG 7198720 bytes |
| Targeted ARM W=1 of every changed object (pm-journal, clocks, spm, system-idle, usb, cpu-dvfs, mtk_wdt, PM suspend) | PASS, no warnings (kernel sources identical in 6dfbfe7 and 76a5d41) |
| Production/platform/CPU regressions (incl. test_cpu_fix03) | 266 tests: 263 PASS, 3 explicit native-dependency skips |
| Native dependency tests on the packaging host | 12 PASS, no skips |
| Reborn workspace | 193 PASS; cargo fmt and strict Clippy all-targets -D warnings PASS |
| Buildroot ARM, Reborn ARM and QEMU | PASS |
| Installed ARM (Python modules, SQLite/OpenSSL, Reborn, ALSA) | PASS, 26 modules |
| ELF dependency closure | 382 ARM ELF files / 1396 edges PASS; no build RPATH |
| FFmpeg/ALSA | fresh FFmpeg feature contract and ALSA constraints PASS |
| Locked source/release inventory, legal-info | 105 packages hash-verified; legal-info collected with existing recipe-metadata limits |
| Recovery options and automatic-admission fault containment | PASS, including the positive QoS return reported as 0 |
| Preserving package / fallback | PASS clean ext4 and on-image identity, BOOTIMG/Y2ROOT only, no Y2DATA payload, exact Hardware02 fallback |
| Qualification harness offline | plan-only default, --wifi-host required, evaluation helpers PASS |
| Documentation links/catalog | 0 problems |

Candidate: /home/luca/Dokumente/Code/Y2Linux/out/y2linux-cpu-final-fix03-candidate/

| Payload | SHA256 |
| --- | --- |
| BOOTIMG.img | c55b26407e46a436f2bfffe216feecfd18ced6b7bd404ed8ab6eaa013ba9cce6 |
| Y2ROOT.img | 04cafd4bddab65a01e0a35c056ee9a22a6b00ffa059cd863a95095af635d7257 |
| fallback/BOOTIMG.img | b2a2c3bcb7cc7783828882e447e8b867453cb5b65846ce63577076b1ca4afeea |
| fallback/Y2ROOT.img | 63dbd0a198cd86e847c10ed163fd14b2cbe269595fa1988c99ac8393160bb547 |

The fallback is the accepted Hardware02 pair (Linux 76bc8229, Reborn 95747e0a, kernel 6.18.0-y2linux-hardware-02, root 2025.02.18-platform-v1.4), identical to the Fix01 and Fix02 fallbacks. The package has no preloader/LK/NVRAM/PROTECT/calibration/factory/data payload. No device access, flash or push occurred.

Owner next action: see [Fix03 physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX03-PHYSICAL-QUALIFICATION.md).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
