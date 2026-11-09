---
title: "First-device launch gates after the M1 offline wave - Innioasis Updater"
description: "First-device launch gates after the M1 offline wave <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-first-boot-launch-gates.html"
---

# First-device launch gates after the M1 offline wave - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# First-device launch gates after the M1 offline wave

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# First-device launch gates after the M1 offline wave > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current: [risk-accepted diagnostic GO](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Frisk-diagnostic-result.md), pending separate flash authorization. The earlier candidate/assessment below is retained as history.

Current policy: [D11–D13 risk-accepted diagnostic](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md) supersedes the earlier absolute authentication/current-backup/full-handoff gates below. This document retains the historical assessment; watchdog, observation, verified recovery and BOOTIMG-only scope remain mandatory. No flash authorized.

Historical verdict: [Y2E-145 launch assessment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md) — NO-GO. Ordinary USB/ADB does not establish early observation; installed authentication and current BOOTIMG backup are unproved. New package analysis finds a nominal 10-second watchdog interval on normal initialization, without an established normal-handoff disable. The current no-watchdog candidate is not approved for the proposed 60-second run.

2026-09-08; Y2B-235. Offline artifact acceptance is complete only when its reproducibility report passes; hardware launch is still blocked. The initial Y2B-235 review used retained package disassembly and audited upstream sources, with no ADB, device mode change, raw readback, DA execution, flash or boot. The later U10a update below additionally uses explicitly safe read-only stock ADB from Y2E-140. Known-good owner recovery remains strong evidence. No research was delegated.

## U07b — Installed LK and authentication

The FM `lk.bin` analysis is package evidence, not installed bytes. Re-reading retained `20260908-ram-map/lk.thumb.txt` establishes concrete branch conditions at `0x81e207d0`: the word at a runtime structure's +0x10 selects the software-secure path when equal to 1 (`0x81e207e8..0x81e207ec`); otherwise a policy helper at `0x81e20210` is called with argument 1. A zero return branches to `0x81e209e0` and the “Don't check” path. Other paths include BOOTIMG verification at `0x81e2081a..0x81e20820`, as well as unlock-only and SEC_RO checks. Static recovered register annotations are not treated as live values across branches.

Unresolved proof: installed LK/preloader identity and the selected normal boot's actual policy/configuration state. Package branch existence, stock-ROM flash success and an Android SHA-1 image ID cannot supply that proof. Next bounded acquisition must establish installed loader hashes and appropriately exposed stock security state/logs, with an approved backup/readback method if ordinary non-root exports cannot. No fuse/security setting changes, bypass, or unsigned-image trial is proposed as a discovery shortcut.

## U07c — DMA, entry mode and secure state

Retained FM instructions at `0x81e05334` set the eMMC DMA stop control and poll the active bit until clear (`0x81e0535e..0x81e05362`). The selected normal storage paths call this helper. Final `0x81e00458` still contains only its LED/GIC cleanup calls, with cache/MMU cleanup elsewhere. This strengthens the storage-specific argument but does not establish display, modem, connectivity or secure-world bus-master quiescence/containment for the installed loader.

D08 excludes LK/heap uncertainty, display scratch/high framebuffer, modem and connectivity storage. The actual artifact exposes no peripheral DMA driver, but these facts cannot stop inherited DMA. The D09 no-hyp build also requires the traced SVC entry contract to match the installed loader. The first artifact has no watchdog driver: inherited watchdog enable/timeout must be accounted for in launch timing, not assumed disabled. Next proof is a bounded final-handoff state analysis for the installed normal path and safe existing stock observations; no arbitrary register sweep or experimental boot. Full RAM expansion/physical rank discovery remains deferred.

## U10a — Observable console

[Y2E-140 / D10](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md) supersedes the original UART3 default-string inference: fresh installed console-core/sysfs evidence selects ttyMT0 → mtk-uart.0 → UART0 at 0x11002000. FM kernel settings and console functions were independently remapped and confirm that indices are not swapped. Package LK selects UART0 when the preloader boot-argument logging fields satisfy its conditional branch; otherwise UART3. Both package paths configure 921600 8N1. Exact installed loader identity, selected handoff routing and live baud remain unproved.

The revised, fully revalidated offline DT uses UART0, IRQ51 and the same 26 MHz clock; the only Linux alias remains `serial0` / `ttyS0`. stdout-path has no baud suffix/current-speed, so upstream earlycon preserves inherited baud until normal `console=ttyS0,921600n8` setup. No pinmux or peripheral feature was added. A pre-earlycon hang can still be silent.

Unresolved proof: confirmed board TX/GND, measured pad voltage/receiver compatibility, stock LK plus kernel serial capture and inherited routing. Native SoC UART pins are documented in a 1.8 V domain, which is not a measurement at a Y2 test point. The host [receive-only capture tool/runbook](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fstock-console-capture.md) is tested with PTYs only. Readable stock `/proc/last_kmsg` is a previous late kernel log, not serial proof or a Linux fallback. No serial adapter was present. A bootloader UART-over-USB accessory route is the smallest remaining alternative lead if native pads cannot be established, but detection/wiring/voltage/persistence are not yet proved. Y2E-140 remains open.

## Backup/recovery and power

Owner-confirmed SP Flash Tool restore with the FM ROM is accepted; local tool v5.2032.00 is corroborated and the package/scatter hashes are already recorded in [recovery.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md). Remaining prerequisites are concrete: same-device boot/recovery and personalized NVRAM/calibration/protect/security backups with verified independent retention; exact tool/DA/mode/connection/target semantics; trusted power and a consistent acquisition state. Retained research files are not these backups. Loading a DA or changing boot mode is a separate operation, not passive ADB inventory. No destructive recovery rehearsal is required.

## Conditional first experiment — specification for later review, not executable authorization
  - Close the four gate groups above and retain their evidence. Verify exact artifact hashes and the D08 report. Confirm a stock console capture works before changing BOOTIMG. Record the operator's proven SPFT tool/DA/connection steps and a BOOTIMG-only restore path using the verified same-device backup.
  - After a separately authorized bounded procedure, use that proven transport in Download Only mode with only BOOTIMG selected. Target the established eMMC-user BOOTIMG interval `[0x01d80000,0x02d80000)`; write the exact validated file starting at its beginning, including its zero read tail. Require bounded readback/hash verification where the approved transport supports it. Do not modify preloader, LK, partition tables, recovery, Android/system/userdata or personalized regions. No Format All, repartition or rootfs installation.
  - Capture one normal stock-LK launch into the candidate, timestamped from before power-on. Expected evidence is Linux 6.18 banner, controlled cmdline, CPU0, D08 memory, PID1 `Y2DIAG READY` and at least three five-second heartbeats. Confirm proc/iomem/meminfo and interrupt diagnostics; described RAM is 24.5 MiB, not predicted MemTotal. No input or persistent writes are needed.
  - Planned observation window: at most 60 seconds, subject to the confirmed watchdog/power procedure. On silence, panic, reset loop or unexpected memory/CPU state, stop, retain the log and return to research; do not repeat with expanded RAM or changed loaders. Restore only the backed-up BOOTIMG through the known-good bounded route, then verify stock boot and owner-defined functional/calibration checks.

Exact DA/entry/readback and console-wiring steps remain intentionally unresolved until evidence supplies them. This is therefore a conditional target experiment, not a ready-to-run flashing recipe. No verified nonpersistent `fastboot boot` route is available to substitute. M0 and the hardware completion of M1 remain open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
