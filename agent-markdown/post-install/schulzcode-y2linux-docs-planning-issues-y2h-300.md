---
title: "Y2H-300 — M2 core platform foundations and boot stability - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2h-300.html"
---

# Y2H-300 — M2 core platform foundations and boot stability - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2H-300 — M2 core platform foundations and boot stability

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## Current session checkpoint — 2026-09-10

M2 core/Buildroot is physically qualified for progression; #22–26 are closed. Initial ACM/Ethernet/SSH and restart recovery work. #27 cable reconnect remains unresolved/deferred under this open epic; do not reopen solved core research.

[September 10 session audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23current-session-close-audit--2026-09-10&anchor=current-session-close-audit--2026-09-10). Earlier phase ordering below is historical where superseded.

## DEV-02 live hardware checkpoint — 2026-09-10

OPEN: physical USB reconnect failed; core/Buildroot otherwise substantially qualified.

[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) retains baseline, completed 256 MiB test, input/display/SD and USB failure evidence. No reboot, kernel build or BOOTIMG was prepared. This checkpoint supersedes stale untested/blocked statements below within its measured scope.

## Y2LINUX-DEV-01 manual-deployment boundary audit — 2026-09-10

Offline implementation and the combined candidate are now built and validated: [DEV-01 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-dev-01-result.md), [memory reconciliation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdevelopment-memory.md). Rechecked every hardware coverage row against the retained BASELINE-03 capture and owner observations. No newer physical capture exists, so **no physical classification or milestone exit is promoted**. M1 COMPLETE; M2 ACTIVE/exit incomplete; audio/application, radio, product PM/security and later milestones retain their gaps and owners.

The owner-specified ED25519 public key is packaged; no host private key was accessed. Kernel/module, large-memory DT, rescue archive, actual pinned Buildroot, ext4/tar content and key policy pass offline validation. Rootfs/ECM/SSH now have built implementations; their physical state remains untested. SD writes and BOOTIMG flashing remain owner-only. Next action is one manual deployment and combined visible-display, wheel, RAM, SD, persistent USB/network/SSH collection. No unchanged ROM/recovery provenance or duplicate clean build was repeated.

## Y2LINUX-DEV-01 integration scope audit — 2026-09-10

Fresh-session local baseline 2efcdc1, clean main; current open issues #16, #22–32 agree with the local BASELINE-03 checkpoint. Reviewed all coverage rows, retained capture-02 (102314 bytes, all 606 kernel records, 180 seconds), source and artifact metadata. No new hardware success is claimed. Owner confirms an earlier wheel-working integrated baseline; its exact artifact identity is not established in the retained canonical captures. Treat current eight -110 reads as an integration regression and preserve register-zero repeated-start framing.

The owner now explicitly authorizes one integrated development candidate: post-modeset display fixes/diagnostics at 480x360; wheel transport correction; large RAM with explicit reservations and HIGHMEM; pinned ARMv7 hard-float glibc Buildroot; removable-SD ext4 LABEL=Y2ROOT; rescue initramfs; persistent ACM+ECM; key-only Dropbear. This supersedes D08 as the final target, identity-only SD and temporary USB disconnect deadlines. Internal eMMC remains protected; no assistant flash, SD write, loader/partition/calibration/Android write is authorized.

Every physical coverage classification below remains unchanged. Display remains PARTIAL with failed visible output despite successful DRM initialization. Wheel remains PARTIAL with working historical owner observation and current transport regression. RAM, removable SD and USB are PARTIAL; Buildroot/rootfs/SSH are PLANNED pending implementation/build and then physical qualification. SMP and buttons retain their narrow successes. All power/thermal, audio, radio, recovery, production security, time/entropy and application gaps retain their existing owners and limitations. M1 COMPLETE; M2 ACTIVE/exit incomplete; M3/application and later product phases are not activated. Existing #22–28 own this work; #30 retains sustained-workload/power qualification and #32 production policy.

Proceed offline together, preserving attribution/identity and unchanged donor, ROM and recovery provenance. One clean kernel tree, one pinned Buildroot build, changed-subsystem tests and full new memory/layout/BOOTIMG/rootfs validation. Record exact artifact hashes and remaining physical tests. Stop for owner manual SD identification/write and BOOTIMG-only deployment. Permanent USB observation is a development capability, not sustained power/thermal qualification. Re-audit before milestone closure using the subsequently collected real hardware results.

# Y2H-300 — M2 core platform foundations and boot stability

## Offline integration checkpoint — 2026-09-10

The coherent Linux 6.18 core baseline is built and offline validated. One manual owner flash replaces tiny controller candidates. M1 COMPLETE, M2 ACTIVE; no hardware classification or exit criterion is promoted by compilation.

[M2-BASELINE-01: exact implementation, RAM decision, checks and owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md). The historical scope/sequence below is superseded where it conflicts with the owner’s combined integration instruction. All remaining acceptance criteria stay open.

## Current strategy — M2-BASELINE-01

The owner's 2026-09-10 instruction supersedes the historical tiny-candidate sequence below. Build one coherent Linux 6.18 core baseline, including the existing USBACM-04 and navigation code, with safe controller probe failures visible together in the full live log. No separate prerequisite flash of those two candidates. [Scope and five-minute test audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23m2-baseline-01-integration-authorization--2026-09-10&anchor=m2-baseline-01-integration-authorization--2026-09-10). M1 complete; M2 active. Hardware classifications and closure requirements remain.

## Additional evidence — 2026-09-10

M1 remains complete; M2 active with all exit criteria intact. Additional experiment history makes SMP release, wheel, PMIC and display validation/adaptation tasks rather than discovery from zero. Keep M2-INPUT-01/USBACM-04 pending owner tests, then corrected shared CCF/PWRAP/EINT/I2C/DMA and useful RAM reconciliation, followed by display and storage/rootfs. Linux 6.18 already covers the old OVL pitch/address and PMIC single-key fixes. No kernel/config/image changed, no new physical result, no new issues and no M3/application or radio activation.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Canonical epic [#28](https://github.com/SchulzCode/Y2Linux/issues/28); [coverage audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

ACTIVE, entry PARTIAL (2026-09-09 owner authorization). See the [activation audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23m2-activation-audit--2026-09-09&anchor=m2-activation-audit--2026-09-09). USB #27 and the smallest #23 prerequisite come first. Exit remains blocked; no optional-feature waiver is claimed.

## Current execution checkpoint — 2026-09-09

The owner explicitly requested one combined enumeration/logging candidate to reduce physical iteration. [Scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23combined-usb-ownership-scope-review--baseline-d9c2c98&anchor=combined-usb-ownership-scope-review--baseline-d9c2c98) keeps M1 complete, M2 active/exit blocked and later phases deferred. [CHRDET evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) establishes charger presence under the reported cable conditions; connected-start6a=BE still refuses wake. No new hardware result has been inferred.

Immediate next test: [M2-USBACM-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-01-result.md), 1,159,168 bytes, SHA-256 `d2d1f8cbbaa23ffcbdeddb317db7a8e62bc21deca9ebebc564c9b55a5590aedd`. [Reviewed combined contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-enumeration.md): boot unplugged, perform the proven guarded wake, attach at the screen prompt, check fresh supply/clock/PHY/DMA state, apply the FM/LK digital device-session sequence, then attempt upstream MUSB peripheral PIO, one standard g_serial ACM and bounded retained/live kernel + PID1 logging. No host VBUS supply, analog calibration, PMIC writes, active-DMA recovery, RAM expansion or other partition writes.

One clean build passes 23 full-suite methods, one additional linked-syscall mutation method and 8 observation methods, including 30 QEMU ARM PID1 scenarios and host/ARM relay faults. Exact DT/config, linked accesses, D08 and BOOTIMG pass. [Host capture tool](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md) is ready. No device operation was performed. Stop for the owner's BOOTIMG-only physical test within 60s. USBGUARD-01 remains an optional untested fallback, not a prerequisite test.

This advances offline implementation only. Physical enumeration, real log continuity, late-open/non-reading behavior and controller reconnect qualification remain outstanding. The first trial stops on first detach/error or 50s active window; reconnect and connected-start recovery are not implemented. #23/#27/#28 stay open, and every original hardware acceptance criterion remains intact. Original drafting-only restrictions below are superseded only for this specifically authorized/audited experiment, not a general production port.

## Goal / why this epic is needed

Keep the core-hardware exit gate represented beyond the existing five research issues: a repeatably bootable, observable device with usable memory, display, input and storage. M1's physical Linux/PID1 success is achieved; exact-hash boot repeatability, timing accuracy and long-run stability are not yet qualified.

## Existing work and dependencies

Track, do not duplicate: RAM #22, shared power #23, controls #24, display #25, read-only SD #26, blocked USB logging #27 and optional physical UART #16. Depend on M1 evidence and the relevant recovery policy, not a new M0 recovery rehearsal. Share supply/thermal prerequisites with the power epic.

## High-level coverage
  - Boot identity/result capture, bounded repeated boots, timer/IRQ accuracy,

working-set/stress evidence, reset/reboot and kernel regression policy.
  - Static RAM expansion/exclusions, optional researched SMP release/coherency,

complete needed clocks/resets, pinctrl/GPIO/IRQ domains and I2C access.
  - Production watchdog ownership, early-to-driver handoff, timeout/reset behavior;

stopped AP watchdog remains the experiment policy until separately replaced.
  - Standard display/panel/backlight and evdev wheel/buttons/power key; determine

whether stock touch-named nodes imply a physical touch interface on this board.
  - USB controller/PHY/device-mode debug; do not hide missing lower-layer drivers

behind generic compatibles. Preserve the diagnostic path during takeover.
  - Removable SD first, later eMMC controller/DMA and filesystem integrity. Define

a recoverable development rootfs and storage access boundaries with the production epic; no automatic reuse of everything after BOOTIMG.

## Exit evidence / unlocks

Reviewable actual-hardware reports demonstrate boot repeatability, adequate measured memory, observable failures, viable display/input, media access and a recoverable rootfs plan/implementation appropriate to the phase. No claim that all 1 GiB, SMP or every peripheral is mandatory for the first wired-player slice. List any waived optional feature explicitly. Unlocks Gate C device-UI experiments and the native audio proof, not Android retirement.

## Out-of-scope / stop

Audio playback, radios, complete product PM and application logic are owned by later epics. Stop a subsystem at missing clock/pin/rail/DMA contracts or loss of recovery/observation; decompose that single prerequisite when authorized.

## Execution and validation boundary

The owner has activated incremental M2 research and implementation. This epic alone grants no physical-device permission. Expand only the next evidence-backed change when this phase is activated; preserve existing stable IDs and link existing issues instead of duplicating them. No speculative driver task list, build, flash or experiment is authorized by this epic.

Before closing the phase or proceeding through its exit gate, repeat the [standing roadmap/gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) using real hardware results. Separate owner reports, retained artifacts, source support and actual device validation. Unknown dependencies stop the relevant path; do not guess hardware or silently broaden scope. Milestone qualification uses the appropriate full verification boundary; small later fixes keep targeted validation and D08/package checks without routine provenance re-audits.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
