---
title: "Current unknowns and historical architecture decisions - Innioasis Updater"
description: "Current unknowns and historical architecture decisions <!-- knowledge-base-scope: maintained-summary; baseline02-sync 2026-10-03 -- Current Baseline02 / UART01 scope Reso"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-open-unknowns.html"
---

# Current unknowns and historical architecture decisions - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Current unknowns and historical architecture decisions

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Current unknowns and historical architecture decisions

## Current Baseline02 / UART01 scope

Resolved CPU blockers: MMC runtime clock ownership, useful automatic parking, all five guarded OPPs, C2 entry/restore and UART1/global-ACK C3 admission. UART01 proves real repeated C3 CPU reset/return. Current open CPU boundary is Baseline02 new-image and automatic cold-boot qualification. Full system suspend/Power+RTC resume, injected CIRQ pending-edge coverage, wider endurance/charging thermal envelope and electrical battery measurements remain separate. Native 24-bit/high-rate audio, optional Bluetooth peers/codecs, exhaustive storage ceiling/host/recovery/distribution questions also remain open; the old M0/M1 discovery list below is history.

[Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) carry exact identities, counters and limits.

## Historical source research and physical checkpoints

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Unknowns and architecture decisions

Current unresolved CPU/transport group, 2026-09-27: exact PWRAP readiness operand; MMC runtime clock gating without storage/card regression; a sustained, useful system-idle interval; first kernel suspend boundary and SRAM journal retention; loaded USB fault/recovery. C3/full RTC/Power wake and high-voltage transitions remain NOT_TESTED. GPT6/GPT4/PPI29, highres/NO_HZ and all real Reborn workload classes pass narrowly. These latest facts are in the [current platform state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) and [Fix01 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md). The much older M0/M1 unknown list below is a dated discovery record.

Historical checkpoint — 2026-09-10: M1 complete; M2 core/Buildroot physically qualified for progression; M3 AUDIO-02 has clean44.1kHz headphones and a deployed/tested notification fix. USB reconnect #27 remains unresolved. M4/M5/Y2PlayerNative are not started. Earlier unknowns below are historical wherever the current hardware reports supersede them.

2026-09-10: [additional reverse-engineering audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md) narrows U10b/U11: SMP release, input protocol, display failures and audio supply requirements now have concrete external experiments to validate/forward-port. U07c's loader/DMA ownership and U09's trustworthy power telemetry remain open. External hardware successes do not change our capability classifications; M1 complete, M2 active, M3/application and M5 implementation deferred.

Current hardware result: [owner-observed M1 runtime success](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md) confirms Linux 6.18, native PID1, increasing BEAT/uptime, working sleep, proc/sysfs mounts, CPU0, D08 RAM visibility, framebuffer diagnostics and stopped-watchdog status. M1 core achieved. Exact flashed hash and unreported diagnostic fields remain unverified. Earlier dated statements below are historical.

Y2B-240 hardware result: the owner reports solid green, which the implemented state machine reaches through initramfs `/init` running as PID1. M1's Linux 6.18 plus PID1 boot objective is achieved. No heartbeat/checkerboard success is claimed. [Y2B-245 / D14](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fon-screen-diagnostics.md) is the offline follow-up for readable runtime diagnostics.

2026-09-08 hardware update: [Y2B-240 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment-result.md) records owner-observed green PID1 evidence and successful BOOTIMG-only Android recovery using the owner-selected boot-adb image. Timed heartbeats, cutoff and exact FM restoration were not verified. Historical pre-launch unknowns below must be read with this narrower new evidence.

Current first-experiment policy is [D11–D13](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md): unsigned acceptance, missing current BOOTIMG backup and incomplete DMA/secure-state proofs are accepted experimental risks, not absolute launch blockers. They remain factual unknowns. Guarded inherited video replaces physical UART as the proposed first-test observation; successful board output is not yet observed.

Date: 2026-09-08. [Y2E-130](https://github.com/SchulzCode/Y2Linux/issues/7) fixes the offline memory policy after Y2E-125. M0 remains open. The owner subsequently authorized direct M1 offline implementation; its [validated result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md) does not clear hardware gates.

## Resolved or materially improved``````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md)

| ID | New evidence / decision |
| --- | --- |
| U01/U02 recovery selection | Owner confirms successful SPFT flashing of this exact Y2 with the FM ROM. It is the owner-proven fallback; 24 current files and scatter are hashed. Exact current installed hashes and historical-byte identity remain distinct unknowns. |
| U03 tool identity | Local executable identifies v5.2032.00 / 5.2032.00.sn100; archive matches executable; recent-file history names the FM scatter. Previously used build strongly corroborated; DA/settings not proved. |
| U06 recovery viability | Successful owner-observed same-device recovery/flash accepted as strong evidence. Do not re-prove from scratch or require deliberate damage. Exact emergency entry/runbook details remain incomplete. |
| U07 address/boot-data discrepancy | Package LK overrides header addresses: kernel 0x80008000, tags 0x80000100, ramdisk 0x84000000, machine ID 6582. ATAG construction and final entry traced. No RAM-alias explanation is required. |
| U07a / U08 memory fixups | FM symbols independently remapped. D08 fixes a 24.5 MiB static DT map, disables ATAG import, and specifies exact permitted load/decompression/DTB/initramfs intervals and artifact rejection rules. Full policy. This resolves offline memory architecture, not DMA-safe launch. |
| U08/U11 boot fundamentals | Upstream v6.18 includes mt6582.dtsi, ARMv7/GIC/sysirq/GPT/UART foundation, GENERIC_DT fallback and appended-DTB/ATAG conversion. No new legacy board-file port is presently justified. This is not proof of a complete working Y2 port. |

## Remaining unknowns[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md)

| ID | Bounded missing evidence | Blocks / current action |
| --- | --- | --- |
| U01 | Current PCB/build and installed loader/image lineage | Pin the actual experiment target. Do not infer exact installed bytes from fingerprint or package name. |
| U02 | Original download authenticity and current bytes versus historical flashed bytes | Record provenance accurately; does not negate the owner's successful same-device fallback. |
| U03 | Exact historical DA, flash mode/targets and reviewed acquisition/connection semantics | Future backup/runbook. Bundled DA hash is a candidate, not an established historical selection. |
| U04 | PRELOADER hardware-region configuration, EBR span and BMTPOOL semantics | Special-region acquisition. Ordinary boot/recovery metadata is reconciled; no guessed raw ranges. |
| U05 | Consistent per-device boot/recovery/calibration/protect backups and independent copies | Optional exact-state preservation for this experiment; FM fallback accepted under D11. No factory-data substitution or unapproved filesystem freeze/unmount. |
| U06 | Detailed independent-of-Android entry sequence and recorded post-restore checks | Future operator procedure; reuse owner-proven recovery, no broad viability re-test. |
| U07c | Live inherited DMA/secure state; loader heap extent, display scratch lifetime, physical ranks and secure/shared aliases remain incompletely observed | Accepted first-experiment risk (D11). Reduced static memory avoids identified storage but is not bus-master containment. Trace the selected normal loader path and obtain bounded stock evidence; no arbitrary MMIO probes. Full rank topology/high-memory reclamation is deferred. |
| U07b | Installed loader identity and hardware-selected authentication policy | Y2E-145 finds package ROM_INFO +0xe8=0x22 still consults bit 1 of 0x10206060; not unconditional disable. Current ADB exposes neither installed bytes nor a reliable policy result. Assessment. |
| U08 | Expanded allocator RAM, exact working set and stability beyond the reported run | Core board execution, working sleep and increasing BEAT/uptime are owner-observed. D08 RAM is visible; exact MemTotal, stress/timing accuracy and expanded RAM remain unverified. Y2E-155 plans one safe expansion decision; no RAM change is authorized today. |
| U09 | Conflicting battery readings / trusted power and consistency prerequisites | Future acquisition/restore/boot procedure; passive evidence only. |
| U10a | Physically usable console, routing, voltage/pins, baud and stock output | Y2E-140 confirms installed ttyMT0/UART0 controller selection and corrects/revalidates the artifact. Board TX/GND, pad voltage, live baud and stock LK+kernel serial capture remain open; host PTY tests and ADB last_kmsg are not that proof. Evidence. |
| U10b | Panel/input, audio supplies/reset/clocks/analog path, radios/firmware/calibration | Later subsystem work, one bounded proof at a time. |
| U11 | Y2-compatible clocks/pinctrl/MMC, SMP release and full peripheral support | Later persistent rootfs/platform work. Source names/sibling compatibles do not prove support. |

## Decisions
  - D01: Y2Linux owns platform evidence, recovery, kernel/DT research and implementation issues; Y2PlayerNative is the later native Rust + C application. Initial issues were transferred, preserving stable IDs/history.
  - D02: Research precedes small specified implementation checkpoints. For M1 the owner explicitly authorized the same lead to implement directly, with no delegation. No task in this wave is `state:luna-ready`.
  - D03: Failed generated-distribution checks quarantine those claims; independently verified historical evidence and safe observations remain useful. Missing/denied evidence is not silently promoted to success.
  - D04: Closed Y2E-101/105/110/115/120 represent completed bounded investigations, not M0 passage. Y2E-125 updates their conclusions without duplicating their backlog.
  - D05: Candidate boot strategy: retain preloader/LK; legacy 2 KiB BOOTIMG with KERNEL(zImage + appended Y2 DTB), ROOTFS(small initramfs), CPU0 and observable console. No persistent eMMC rootfs or Linux-initiated eMMC writes; any later BOOTIMG-only deployment separately requires passed launch gates and explicit authorization. DT/ATAG policy is now fixed by D08.
  - D06: Accept owner-observed successful SPFT recovery and the corroborated v5.2032 installation. Focus remaining recovery work on exact procedure/backups, not proving viability again. Preserve preloader/calibration and prohibit destructive formatting.
  - D07: Treat the supplied Debian/replacement-BOOTIMG description as a consistent engineering lead, not implementation evidence. Kernel target is upstream 6.18 LTS. Do not repurpose everything after BOOTIMG; recovery/security/table partitions intervene.
  - D08:[Initial RAM policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md): 24 MiB low RAM and 512 KiB initramfs bank; all other DRAM omitted, first 16 KiB retained. Appended DTB with no ATAG import; controlled DT bootargs and exact inner initrd length. Fixed caps and symbol-based relocation/overread checks permit bounded offline implementation. Failure to fit returns for review; no automatic memory expansion. U07c remains a launch gate.

Next implementation boundary can be a tiny offline artifact/layout task under D08, after its concrete issue is specified. No implementation issue was created in Y2E-130. Next research is a bounded prerequisite for a hardware launch: inherited DMA/secure-state assurance or physical console evidence, with installed-loader and recovery prerequisites preserved. Do not bundle all peripherals into a speculative backlog.
  - D09:[Kconfig compatibility and console policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fkernel-policy.md). One reviewed prompt-visibility patch makes the existing D08 `ARM_VIRT_EXT=n` requirement selectable on v6.18; upstream default and all memory limits stay unchanged. Static `PHYS_OFFSET=0x80000000` is checked. The original UART3 candidate is superseded by D10; physical readiness remains U10a.

## M1 offline boundary

Y2B-201 through Y2B-235 deliver a reproducible, strictly validated offline candidate. [Launch-gate review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-boot-launch-gates.md) records the rechecked FM security branches, storage DMA stop, final cleanup and UART selection, plus the smallest missing live/backup proofs. U07b/U07c/U10a and recovery/power remain open; M0 is not passed and M1 has no hardware-boot result. No device interaction occurred during this wave.

## Y2E-140 observation boundary
  - D10:[Installed observation evidence and controller correction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md): UART0 at 0x11002000, IRQ51, sole serial0/ttyS0 alias; D08 and kernel features unchanged. Two complete clean builds pass and match. Expected native logic is 1.8 V; 921600 8N1 is the firmware-supported receive candidate, not a measured board rate.
  - U10a remains open for board-specific TX/GND/level and actual stock LK/kernel capture. No safe physical connection was established. Bounded alternative: trace the FM preloader's existing UART-over-USB accessory selection/electrical requirements if native TX access is unavailable; do not guess a cable or change the PHY live.
  - This later research used passive stock ADB, including a previous kernel RAM-console tail. It made no device state change or experimental boot. After U10a passes, resolve installed loader/authentication U07b, with U07c and backup/recovery/power gates preserved.

## Y2E-145 GO / NO-GO boundary

NO-GO for the requested 60-second first BOOTIMG-only experiment. Ordinary USB/ADB does not provide the proved early observation channel; current BOOTIMG backup/independent retention and installed authentication remain missing. Normal package LK arms a nominal 10-second watchdog interval with IRQ/dual-mode behavior; identified disable calls are Download/Fastboot, not normal BOOTIMG handoff. Treat it as inherited until disproved. Current candidate has no watchdog servicing, so a reviewed minimal timing/watchdog policy may be needed after installed-lineage proof. No feature or D08 change was made to guess past this gate.

[Complete decision/evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md), [blocked BOOTIMG backup/restore procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fbootimg-recovery-runbook.md). Y2E-140 (#16) and Y2E-145 (#17) stay open. No first-boot execution issue was created because GO was not reached.
  - D11: Owner accepts the three specified launch uncertainties for one BOOTIMG-only test; recovery files, watchdog and useful observation remain required.
  - D12: Stop AP_RGU at zImage entry, read back and branch past linker padding before decompression.
  - D13: Guarded inherited RGB565 pixel diagnostics only; no display register writes or D08 allocator expansion.

## Current core result and next planning boundary

[M1 runtime result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md) supersedes historical claims above that no Linux hardware execution or heartbeat has been observed. The sleep ENOSYS failure is historical; increasing BEAT and working sleep are now reported. Physical UART, exact image lineage and broader DMA/power/peripheral questions remain separate. Exactly five research issues are queued in [the historical execution order](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md%23historical-foundation-research-queue&anchor=historical-foundation-research-queue); no implementation or M2 execution occurred today.

## USB log-channel planning, 2026-09-09

[USB logging research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fusb-logging.md) selects peripheral-only MUSB/PIO plus g_serial CDC ACM and nonblocking kernel/PID1 replay. The upper-layer contract is specified; exact MT6582 PHY/clock/VUSB/FIFO and handoff support blocks hardware implementation readiness. No reliable smaller host-readable alternative is established; this does not negate working visual M1 diagnostics. One additional owner-requested logging issue is drafted; no implementation/build/flash occurred.

## Whole-roadmap coverage audit, 2026-09-09

[Classified coverage matrix and standing rule](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md) explicitly tracks shared clocks/resets/pinctrl/GPIO/I2C, SMP, production watchdog/reset, native audio/analog routing, thermal and PM, radio firmware/calibration/FM, rootfs and update/security lifecycle. Deferred epics #28–#32 cover these gaps without claiming implementation readiness or changing D08. M1 core remains achieved; M0 residual questions and full stability qualification remain separate.

## M2 activation / USB prerequisite update — 2026-09-09

M2 #28 is active under the owner's incremental implementation instruction; M1 core remains complete. USB #27 has priority over optional RAM expansion. FM/LK now establish the specific PWRAP read protocol and VUSB register needed for a [bounded inherited-state probe](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-probe.md), owned by #23. This is offline contract evidence, not a new PMIC/USB hardware result. #23's other consumer rails and trustworthy telemetry remain unknown; #27 still needs its complete clock/PHY/VBUS/FIFO/IRQ/DMA contract. D08 remains authoritative.

## Returned M2-PWRAP-01 photographs — 2026-09-09

[Physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-hardware-result.md) now confirms one successful inherited PWRAP CID/VUSB snapshot: RC 0, VALID 3, CID 0x2023, VUSB 0xc000, and continued heartbeat through BEAT 50. MemTotal is 22208 kB. This supersedes the preceding checkpoint's absence of PMIC hardware evidence; it does not qualify general PMIC control, supply voltage, repeated boots or USB logging. Timer -61 is traced to the IRQ action-name parser, with hardware confirmation of its correction pending. The next [clock snapshot](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-probe.md) reads four corroborated clock registers without enabling clocks or accessing USB MAC/PHY/DMA. Other unknowns and milestone classifications are unchanged.

## Clock hardware result and next USB prerequisite — 2026-09-09

[M2-USBCLK-01 photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-hardware-result.md) confirm all four clock reads, enabled USB0/mux/PLL reference, corrected increasing timer IRQ counts and BEAT 50 without errors. This resolves the narrow inherited-clock observation, not the clock provider/USB controller contract. [Read-only USB state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-probe.md) is the next prerequisite; no MAC/PHY/DMA hardware result exists yet. M2 remains open with unchanged input/display/media/rootfs and qualification gaps.

## USB state result / bounded PHY wake — 2026-09-09

[Returned USB-state photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-hardware-result.md) confirm all 21 MAC/digital-PHY/DMA reads, disconnected B-device state, eight zero DMA controls, PHY force_suspendm=1/value=0 and BEAT 50 without errors. This is one cached snapshot, not DMA ownership or a USB enumeration result. The next [guarded PHY wake](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md) checks remaining mode controls and conditionally clears only the suspend-force bit. Calibration/analog controls, clocks, VBUS forcing, controller connection and DMA remain unchanged. The candidate must stop for owner testing; full USB/clock-provider/PHY/VBUS/FIFO/IRQ/ DMA contract, host logging and M2 exit remain unqualified.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
