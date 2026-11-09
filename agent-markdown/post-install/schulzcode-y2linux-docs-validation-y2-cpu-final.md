---
title: "Y2 CPU Final - Innioasis Updater"
description: "Y2 CPU Final <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final.html"
---

# Y2 CPU Final - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 CPU Final

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 CPU Final > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

CPU Final implementation candidate, 2026-09-27. No device access, flash or push. This supersedes the Hardware Final software gaps for dormant/CIRQ/deadline ownership; it does not supersede historical hardware failures with invented passes. Physical qualification is independent of implementation and runtime admission. The preserving package is `out/y2linux-cpu-final-candidate/`; its manifest and validation receipts identify the exact built source pair.

## Clock and timer ownership

GPT6 is the sole free-running 13 MHz architectural counter foundation. GPT2 is the calibration reference and retained 32-bit fallback clocksource/sched_clock. `arch_sys_counter` is the normal monotonic clocksource; its upstream rollover, clocksource watchdog and suspend timekeeping machinery remain intact. RTC supplies wall-clock/long-duration wake; the DT does not claim the counter ticks in suspend.

Each CPU uses physical CNTP on PPI29, `arch_sys_timer`, with upstream per-CPU IRQ, CPUHP registration/teardown and oneshot registration. Every online CPU now sets and checks its CNTFRQ against 13 MHz and checks counter advancement with a bounded loop. Failed startup rolls back upstream timer registration/CPUHP; GPT survives. Early GPT6 rate/readback validation still occurs before architectural discovery.

GPT4 is the normal Linux broadcast clockevent, registered by the existing GPT owner on the existing shared GPT interrupt. GPT1 is stopped and its IRQ disabled when GPT4 is selected; failed preparation or `y2.local_timer=off` keeps GPT1 and legacy dummy per-CPU broadcast. GPT6 never becomes a deadline timer. GPT4 and GPT6 cannot be separately claimed by another platform driver.

HIGH_RES_TIMERS and NO_HZ_IDLE use upstream oneshot/highres/nohz transitions, not an extra periodic platform timer. The real per-CPU event has a higher rating than the dummy event. Runtime telemetry reads actual highres/nohz flags per CPU and actual selected event names; configuration alone is not reported as activation. `CPUIDLE_FLAG_TIMER_STOP` hands the next deadline to Linux tick broadcast before DORMANT and returns ownership after wake. Linux owns conversion, earliest-deadline selection, broadcast IRQ delivery and overdue event handling; the port does not manually overwrite CNTP deadlines or create a second GPT4 owner.

## CPU frequency and voltage

The stock bin0 table is 598/747.5/1040 MHz at 1.15 V, 1196 MHz at 1.20 V and 1300 MHz at 1.25 V. The retained loader's unique complete devinfo tag must match stock table0 selection. Unknown/malformed/other bins remain capped at 1040 MHz; there is no arbitrary overclock or assumed alternate-bin voltage table.

CCF sequences the CPU through MAINPLL/2, programs ARMPLL/dividers, waits for readback and returns the mux. PWRAP is the sole VPROC owner: MT6323 register 0x220, selectors 72/80/88, SPM command slots and normal-PCM handshake. Voltage increase precedes clock increase; decrease follows verified clock decrease. Stock 40 us settling/readback, bounded SPM acknowledgement, failed mux rollback and divided MAINPLL fallback remain. Unknown/unsafe voltage readback contains the CPU at the lowest clock; high OPPs are refused after a fault until reboot.

Automatic admission runs when both policy and SPM exist. It verifies the stock 1.15 V baseline and slot readback before releasing the stock-bin 1300 MHz ceiling. Failure leaves conservative OPPs; no owner must select MHz. `y2.dvfs=off` suppresses high-bin admission and retains the stock 1.15 V lower table. Existing optional owner ceiling is diagnostic only, never an application API. Thermal cooling is an independent FREQ_QOS_MAX ceiling, authoritative over minimum workload leases.

## Scheduler and workloads

schedutil remains the default with all four cores available. No automatic rapid hot-unplug policy is installed. Deep idle and Linux scheduler utilization precede optional owner hotplug; CPU0 remains non-offlineable. CPU1–3 retain the source-backed MTCMOS, cache/coherency exit, secondary entry and upstream IRQ/timer CPUHP lifecycle. Retained Hardware02 receipts already prove checked 1–4-core cycles; this candidate adds CNTFRQ/counter checks to each online transition without requalifying hardware.

Per-open QoS supports Idle, PlaybackNormal, PlaybackHeavy, Interactive, ArtworkDecode, LibraryScan, NetworkTransfer and Maintenance. Normal playback has no synthetic frequency floor. Heavy/interactive/artwork/scan ask for bounded minimum capacity, with latency limits where needed. Maximum remains unconstrained by a workload descriptor so supported stock bins and thermal caps remain usable. Leases expire within 30 seconds, close on process death and never set per-core MHz.

Interactive hints are 250 ms, coalesced within 50 ms and separate from playback renewals. A racing expired worker checks the renewed monotonic deadline before clearing QoS, including jiffies wrap. Screen-off immediately closes the interaction descriptor. Artwork decoding uses a scoped CpuWorkloadLease; acquire/renew/release expose classes only. No scaling_setspeed, raw OPP, voltage or SPM API is exported.

## Idle, dormant and context

C1 WFI retains context. C2 SLIDLE is enabled for automatic selection with exact stock single-CPU/peripheral/MSDC preflight, bus DCM readback/restore and WFI fallback. The shared CCF lock owns the entire bus transition. Unknown inherited state, active clocks or failed restore never forces a new power state.

C3 DORMANT is implemented and initially disabled as an experimental state. It uses the exact stock-matched 480-word non-MT6333 runtime PCM, event offsets 0/9/28/68, not the 597-word suspend program. Its conditions are CPU0 only, CPU1–3 physically off in both power-status copies, low source-backed OPP, no active radio/modem/media domains, stock PERI/INFRA clock masks plus MSDC/AFE, no clock-owner contention, CIRQ available and next deadline at least 2 ms away. Requiring media domains off is deliberately stricter than stock clock masks; retained critical display clocks can therefore prevent entry. It never offlines cores to force eligibility. The implementation is present even when this preflight rejects current four-core use.

Linux cpu_suspend/cpu_resume owns ARMv7 banked execution/MMU/CP15 context; cpu_pm owns VFP/NEON, private GIC, timer control and configured debug/PMU state; cpu_cluster_pm owns shared GIC. The added timer notifier preserves CNTP compare, control and CNTFRQ (upstream only saves CNTKCTL). The platform owns MCU_BIU and CA7_CACHE_CONFIG bit4, suppressing L2 reset invalidation for DORMANT and restoring it on both reset-resume and WFI abort. Cortex-A7 integrated coherency uses upstream v7_exit_coherency_flush(all), CLREX/DSB/WFI and SMP/cache re-entry on abort. No ARM64 sequence or independent SCU register mapping is imported. Flushing all levels is conservative with retained L2; residency values are provisional, not measured.

Failure descends C3 -> C2 -> C1; MMIO/timeout faults disable the affected deep path. Linux cpuidle counts usage/time/rejection for the actual returned state. Additional SPM entry/resume/abort/failure counts, last stage/error and clock blocker masks explain preflight failure. Dormant is opt-in through existing cpuidle state disable attributes; the separate atomic dormant-abort count includes deadline rejections. No app-level performance mode or MHz picker is required.

## CIRQ and wake

A dedicated latch owner maps MT6582 0x10204000, inputs0–154 = GIC64–218. It reads live GIC enable/config and sysirq polarity, acknowledges only stale latches and keeps parent-pending enabled events. It clones before masking SPIs, enables edge-only CIRQ, leaves only source-backed SPM149 unmasked, then enters CPU PM. After GIC restoration it unmasks latches, reads status, writes GIC pending-set, masks/disables CIRQ and restores exact original GIC masks. Reserved tail bits are excluded. This uses stock explicit flush; the newer hardware FLUSH bit is not used. No second IRQ domain or guessed interrupt polarity is introduced.

Power and RTC use existing MT6323 IRQ/wake hierarchy, Power-key wake configuration and corrected RTC alarm programming/clear. Both route through EINT in the SPM wake mask. Runtime idle additionally enables source-backed GPT/AFE/USB-PDN/CIRQ wake. SPM raw wake reason and RTC alarm/interrupt observation remain available. Power and RTC same-boot wake are implemented but have no new physical success receipt.

## System suspend and device restoration

The helper freezes through Linux system suspend after taking the platform activity lease, powering radios down, checking complete function/power release and syncing storage. Linux owns device/ALSA/DRM suspend, secondary CPU shutdown and syscore timer ordering. SPM owns wake mask, PCM, retained infrastructure/DDRPHY and CPU0 shutdown. CIRQ brackets CPU/cluster PM; MCU_BIU, GIC, local timer and clocks restore before device resume. Normal PCM is explicitly reinstalled on every return, including aborted entry, rather than assuming a firmware loop is enough.

The captured processor-stage receipt already restored CPUs3/2/1. Its failure was USB overflow and a mandatory-STP WMT boot timeout, not proof of failed CPU restore. MUSB now disconnects through its gadget owner, refuses live DMA, acknowledges sampled stale USB/TX/RX/DMA W1C status, saves quiescent endpoints and clears stale conditions before restored interrupt enables. ECM/ACM re-enumerate on system resume. The IRQ burst window resets with this lifecycle; the terminal fault guard remains. Runtime restoration preserves pending transfer events; stale acknowledgements are limited to successful system quiescence and its saved context. Failed DMA quiesce also preserves pending completion status. The exact runtime top-level IRQ gate returns after endpoint restoration; system resume enables its gate through the platform hook. A terminal fault stays masked.

CONSYS retries one failed boot only after complete power/DMA/clock/rail isolation, matching the retained timeout followed by a successful second start. No DMA buffer is reset/freed to make a retry appear safe. HCI/WLAN consumers see success only after firmware boot; a second failure propagates. Existing y2-bt-reconnect remains the only automatic Bluetooth reconnect owner. Power intent keeps it inhibited during controller startup. The helper records quiesce/kernel/restore/result stages and propagates radio errors. GPU01 clock/genpd/runtime/display corrections and native ALSA/CS43131 volume/PM ordering are preserved, not replaced by CPU policy.

This completes these software restoration paths and contains their observed fault classes. A successful full same-boot suspend/resume of this exact candidate is not claimed; deep suspend remains on the explicit qualification interface by default.

## Diagnostics and recovery

`y2-platform status cpu` reports policies/requested and actual readback, voltage, stock-bin ceiling/fault, online cores, workload leases, timer/highres/nohz state, idle usage/residency/latency/rejection, CIRQ, SPM result/wake/stages/restore timing, clock blockers and conservative switches. Negative voltage readback means error, not a synthetic voltage. `y2-platform status` retains radio/USB/audio/thermal fields.

`y2.cpu_safe=1` is the single conservative baseline: legacy GPT timer, 598 MHz ceiling at stock voltage, WFI only, system suspend disabled. Existing `y2.local_timer=off` is retained; `y2.cpuidle=off`, `y2.deep_idle=off`, `y2.dvfs=off`, `y2.suspend_safe=1` isolate features. Invalid values fail conservative. These switches never change loader, memory reservations, Y2DATA or protected data.

## Source and software validation

[Source/register map](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-SOURCES.md) records applicability and retained binary evidence. Curated CPU Final tests execute the actual CIRQ MMIO clone/replay, runtime PCM/UART bounds, stale USB status/live-DMA refusal, isolated radio retry and renewed-expiry worker, alongside existing transition rollback/voltage ordering, QoS/parser, hotplug sequencer, slow idle and suspend-helper tests. Host synthetic register results and ARM cross-builds are distinct from hardware qualification. Final current-source kernel/config/DT, Buildroot/Reborn ARM, modules/ABI, production and Reborn tests, fmt/strict Clippy, QEMU, ELF/package/data/fallback receipts belong to the candidate validation directory. Unrelated user documentation/assets stay outside its source checkout. No stale root image is accepted as a new build.

## Final candidate receipt

Built runtime pair: Linux `ff586dfff2b5e7abd28af339c055375307308f1f`, Reborn `afcf9ffa1bc45073e97520d592c0284ce73fefcf`. Linux release is `6.18.0-y2linux-cpu-final`; root is `2025.02.18-platform-v1.6`, `1.0.0-cpu-final-candidate.1`. The kernel/modules and all target Buildroot/Reborn binaries were built in a fresh output, with no reused root or target binaries. The later `3f86af2` changes only the DT validator/rejection tests: exact CIRQ and MCU cache context mappings, no changed compiled runtime code. The isolated cache symlink and host bc PATH failures were corrected; failed attempts and final passes remain in the logs. No hardware result is inferred from their software resolution.

| Final check | Result |
| --- | --- |
| Fresh kernel/config, modules, DT, rescue/BOOTIMG, memory/partition bounds | PASS; reservations unchanged |
| Fresh Buildroot, paired Reborn ARM, ABI, FFmpeg/ALSA | PASS |
| Locked production regressions | 208 run, 205 passed, 3 explicit native dependency skips |
| Native dependency coverage | 12 passed, no skips; covers all 3 locked prerequisites |
| Reborn workspace, fmt, strict Clippy | 189 passed; format/Clippy pass |
| ARM/QEMU application and installed platform modules | PASS; 8 app checks, 23 Python modules, 1k database/scan fixture |
| ARM ELF/interpreter/dependency closure | 382 files, 1396 dependency edges, no build RPATH |
| CPU C/MMIO fault injection, recovery/options, stock auto-admission, ARM W=1 | PASS; no new CPU warnings |
| Pinned source inventory and legal/source collection | 105 packages; hashes verified, retained recipe metadata limits recorded |
| Package, preserving scatter, root filesystem/data contract, exact fallback | PASS; BOOTIMG/Y2ROOT only |

The package is `out/y2linux-cpu-final-candidate/`. Its `validation/summary.json`, `manifest.json`, source bundles and top-level checksums are authoritative.
  - `BOOTIMG.img`: 7178240 bytes, SHA-256 `ab9a1621ffd3e650ac65be0e26a4f76f104bc5c5be77a496d1d699dd1790221f`.
  - `Y2ROOT.img`: 536870912 bytes, SHA-256 `68134c6c9712d4d88770694000a30d6f3f13d0f480a7a53bf5c2ba4883c7691b`.

Hardware02 stays the retained physical baseline; CPU Final qualifications are independent and false. Dormant is implemented/experimental/default off with the source-backed single-CPU and domain/clock constraints above. Deep suspend retains the explicit existing qualification entry point. No new four-core dormant, full same-boot suspend, Power/RTC wake or device-resume hardware pass is claimed. Y2DATA/protected regions, Git identity/account and unrelated worktree edits are preserved; no device access, flash, push or external epic closure occurred.

## Physical CPU Final result — 2026-09-27

The owner-flashed exact pair above was verified on real Y2. See [Y2 CPU Final physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-PHYSICAL-QUALIFICATION.md) for per-feature PASS/FAIL/PARTIAL/NOT_TESTED, private receipts, measurements and one prioritized fix batch. These observations supersede any implied runtime success from the software implementation description; source implementation and physical qualification remain separate.

GPT6/GPT4/PPI29 admission rejects at boot; actual legacy GPT/dummy local events have highres0/nohz0. Lower598/747.5/1040MHz scaling, bounded hotplug, schedutil, kernel QoS/thermal priority and WFI work. PMIC216=0 blocks voltage/high-bin admission;1196/1300MHz and voltage sequencing remain unqualified. Actual Reborn formatted workload writes split parser requests and getEINVAL. SLIDLE is enabled but always blocked; dormant remains disabled with its timer prerequisite failed.

Freezer and battery devices/platform/processors/core pm_test return on the same boot, secondary CPUs recover and quiescent MUSB context resumes without storm. A mandatory-STP CONSYS timeout is followed by a successful isolated retry. The first full RTC suspend loses USB/Wi-Fi recovery and never returns before owner restart; no controlled Power wake or full device restoration PASS. Original boot18248d38-f426-4090-add7-a99a7a3a067d; recovered boot 2aff9ecf-dac0-4479-913e-46dc343964d0. Filesystems remain rw/error0, original media and installed pair preserved. No implementation source change/rebuild/flash was made during the sweep. CPU Final is not accepted as the normal CPU platform; automatic deep suspend and C3 must retain their existing qualification/default-off controls. The successful fallback runtime is distinguished from failed new paths.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
