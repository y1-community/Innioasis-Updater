---
title: "Y2 C3 UART candidate physical record - Innioasis Updater"
description: "Y2 C3 UART candidate physical record <!-- knowledge-base-scope: exact-image-validation-receipt; baseline02-sync 2026-10-03 -- Baseline02 scope and current evidence Baseli"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-c3-uart-physical.html"
---

# Y2 C3 UART candidate physical record - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 C3 UART candidate physical record

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 C3 UART candidate physical record

## Baseline02 scope and current evidence

[Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) is now the newest sealed candidate with automatic qualified CPU0 C3 startup. New-image/cold-boot hardware remains PHYSICAL_NOT_RUN. The [UART01 physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) proves bounded C1/C2/C3 on its exact installed pair. Default-off, UART blocker, pending-flash and harness preparation statements below retain their recorded image/session scope. They do not describe the new Baseline02 startup policy or reopen the solved UART01 architecture. This report's original exact-image evidence is preserved; full system suspend and battery measurements remain separate.

## UART01 physical qualification — 2026-10-03

PASS. C1 WORKING; C2 WORKING; C3 WORKING_AND_REPEATEDLY_OBSERVED. This supersedes all prior NOT_RUN/never-entered/software-awaiting-flash statements for this installed pair. No new build or owner flash is needed. C3 is intentionally enabled through normal runtime policy for this boot; fresh image boots remain default disabled/budget0. No persistent default-on policy or full-system suspend qualification was performed.

### Exact installed and source identity````````````````

| Axis | Verified installed value |
| --- | --- |
| Build | Y2LINUX-CPU-C3-UART-01 |
| Kernel | 6.18.0-y2linux-cpu-c3-uart-01 |
| Linux | e9e8d63f9c94232c2b6627881e0967583e202dac |
| Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 |
| Rootfs / release | 2025.02.18-platform-v1.20 / 1.0.0-cpu-c3-uart-candidate.1 |
| Boot throughout all jobs and final SSH | fd955840-35d9-47db-83e0-ff47d6bb2d2b |
| Taint | 0 |

Manifest, uname, versions and running Reborn agree. Checkout55db6d3 at physical admission and later harness commitc8ae170 are not the installed kernel source. Kernel/DT/context/clock/PCM/OPP implementation is unchanged after owner install. Sealed package `out/y2linux-cpu-c3-uart-candidate/` freshly rehashed unchanged:````

| Payload | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 7208960 | a35e7ccb11dfcc642089e422d48a274ab2c700dbba15d00b21cce7b463e4006a |
| Y2ROOT.img | 536870912 | d3a8282a9f5d1b0046283bce1b595eb5797b62c2bff90a62260e80bbfafb5d98 |

No flash, push, protected-partition/data wipe, arbitrary userspace MMIO or forced UART gate was performed. Six preexisting owner documentation edits are preserved separately.

### Preserved C1/C2, topology and performance

All four enabled WFI states advance;400 requested1ms sleeps return on their bound cores. These elapsed sleeps include scheduling and are not direct silicon exit-latency measurements.

| CPU | Entry delta | Residency delta, us | Rejections | Median / maximum requested1ms sleep, ms |
| --- | --- | --- | --- | --- |
| 0 | 1573 | 11919284 | 0 | 1.085065 / 1.174603 |
| 1 | 521 | 12104878 | 0 | 1.085143 / 2.729740 |
| 2 | 1343 | 12348263 | 0 | 1.084604 / 1.110065 |
| 3 | 271 | 12302521 | 0 | 1.084604 / 1.130142 |

C1 MONOTONIC/RAW drift−121412ns over12.067737s. Eighteen normal hotplug transitions check CPU3→2→1 off and1→2→3 on, including both exact physical SPM power copies. Natural coordinator parking reaches CPU0/owned mask0xe; no manual secondary power writes or forced parking are used for C3. Each C3 admission verifies owned topology, both copies showing secondary bits0 and all static prerequisites. Screen and real playback demand restore all cores.

C2 adds 6971 entries and50,654,676us in60.054880715s: 84.35% residency. Slow-clock restore failures0, idle failures0. Legitimate MSDC/APDMA/radio/I2C and other guards remain. Before/after clock/bus/MMC/timer/CPU/IRQ snapshots are retained. No C1/C2 redesign or blocker masking was needed.

All five OPPs pass before and after C3 with voltage readback: 598/747.5/1040MHz at1.15V,1196MHz at1.20V,1300MHz at1.25V. Schedutil, thermal authority, PWRAP, boost/QoS and original active ceiling are preserved.

### UART contract physically proved

All exposed static C3 prerequisites pass when CPU0 alone, CPUs1–3 physically off, screen/radios off, USB detached, no workload, <=747.5MHz, real owned clocks/media idle, CIRQ/GPT4/context/480-word PCM available and budget/backstop armed. UART1 hardware clock remains present (PERI bit17); its conditional PIO sleep adoption is ready. UART0 console sleep enable is1, DMA0. UART1 normal bank LCR/IER/DMA are0; temporary UART_SLEEP_EN changes0→1→0 with exact checked restore. Hardware UART1 PERI gate remains0 before and after, with zero UART restore failures. No FIFO/data/baud/gate/reset/pinmux write is used.

Actual SPM request sets POWER_ON_VAL1 0x15820→0x15821, hardware R13 changes 0x8040000→0x8140000 on the first entry (bit20 ACK); wake cleanup restores 0x15820. All3647 final UART attempts receive ACK, successes3647, timeouts0, request restore failures0, live request/ACK0 after wake. This is the exact stock global pair, not a UART1-specific ACK. The source-backed conditional owner contract, rather than permanently dropping bit17, resolves the prior admission error. The conditional follow-up for a failed UART handshake is not needed: no physical UART handshake failed.

### First real entry and twenty further guarded cycles

The first25ms observation window produces exactly one CPU context entry, reset resume and success: 8,065us driver /9,363us cpuidle residency. GPT wake reason0x10, PCM debug0, same boot, taint0. SRAM contains UART_REQUEST→UART_ACK→DORMANT_CONTEXT→DORMANT_FINISH→DORMANT_RETURN→restores→ DORMANT_COMPLETE with reset-vector assembly stamp 0x59325253. CPU resume is genuine: the MMU-off reset vector records that stamp and branches into normal Linux `cpu_resume_arm`; it is not an unchanged-WFI counter.

Twenty additional independent budget1/RGU10s cycles complete successfully, with25/50/100/200ms observation windows. EXACTLY one actual entry, resume, success and UART request/ACK per cycle; positive residency and every checked restore. Guarded driver residency totals211,010us; cpuidle totals238,313us. All21 retained traces have the reset stamp, checked return and restore stages. No failed CPU context entry, missed timer, watchdog reset or corruption occurs.

GPT4 finisher deadlines range 3,471,384..18,392,615ns, all safely above2ms. Compare-minus-count conversion exactly matches13MHz within integer rounding; IRQ bit3 armed, source clock0, future compare and no pending handoff IRQ. Architectural timer state restores21/21 then3647/3647 overall, failures0, all four CNTFRQ13000000/per-core errors0. GPT6 free-run/highres/NO_HZ and sole GPT4 broadcast remain ready. Twenty requested1ms wake windows add no C3 entry; this observes near-deadline fallback, not proof that a specific guard executed instead of the governor choosing a shallower state. Unit tests cover the exact 2ms/26000-tick rules.

CIRQ64–218 clones and flushes3647/3647, clone/restore failures0, inactive on return. Pending banks are0 in bounded snapshots; do not infer an experimentally injected edge-replay result from zero pending bits. Linux cpu_pm/cluster_pm, GIC/VFP and cpu_suspend/cpu_resume own generic context; retained cache/BIU checks and functional same-boot storage/render/playback/hotplug pass. No custom duplicate MMU/VFP/GIC restore or later-SoC CIRQ layout is introduced. Runtime PCM remains exact MT6582 d53dd75c DPIDLE 480 words / IM length479; normal restore returns to28 words. Infrastructure/DDRPHY/L2 stay retained.

### Meaningful normal-policy idle

After21 guarded successes, budget-1 enables ordinary scheduler-selected C3 for60.088343522s. It adds **3624 successful DORMANT entries and39,204,662us: 65.25% cpuidle residency**. Another two entries occur after the sampled window before USB restoration. Final **3647 entries=resumes=successes=UART requests= ACKs=CIRQ clones/flushes=timer context saves/restores**, driver residency 39,100,882us. UART/PCM/clock/timer/CIRQ/context failures0 and same boot.

| Window | Seconds | CPU utilization | Online CPUs | CPU0 C1, s | C2, s | C3, s | IRQ/s | Context switches/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Screen on idle | 20.065239 | 3.63% | 0–3 | see raw metrics | 0 | 0 | 447.69 | 528.48 |
| Screen off before parking | 20.069114 | 3.63% | 0–3 | see raw metrics | 0 | 0 | 361.55 | 412.57 |
| Parked C2 enabled | 60.054881 | 8.35% | 0 | see raw metrics | 50.654676 | 0 | 185.05 | 337.86 |
| Parked C3 enabled | 60.088344 | 10.28% | 0 | 3.865243 | 9.572727 | 39.204662 | 163.36 | 332.04 |

C3 window ends at37.526/37.500°C,598MHz before/747.5MHz after; MONOTONIC/RAW drift−410481ns. Bounded-window drift magnitude≤2727ns. These are separate physical windows, not a controlled electrical comparison: C3 has useful residency and lower sampled IRQ rate but slightly higher CPU utilization. No battery-duration or electrical power improvement is claimed.

### Storage and wake regressions

Both eMMC `/data` and inserted SD `/media/sd` pass eight fsynced/readback checksum rounds each after C2 and after C3. Controllers runtime-gate with request/DMA/FIFO/controller/IRQ ownership checks; saved state mismatch0, errors0 and all ext4 error counters0. No live root/data reset or raw media write. SD-absent C3 testing is not claimed; no physical removal was requested. Screen wake restores all four cores. Indexed silent playback exercises actual FFmpeg/ALSA and PlaybackNormal QoS, with clean decoding and unchanged error/ xrun counters. All five OPPs pass again. USB bidirectional1MiB integrity passes three rounds with an independent pinned Wi-Fi observer; Wi-Fi runtime restores and same-boot observation succeeds. Final dmesg has no new filesystem/MMC/IRQ/ BUG/Oops error. Cleanup errors0; temporary owned key-only observer removed.

### Observer defects and preserved raw evidence

The original packaged harness stopped before UART entry because it fsynced its durable arm receipt after checking clocks: legitimate MSDC0 bit12 then blocked C3. Correct the harness to save FIRST, then check real MMC gates and all prerequisites over a read-only stable window, with C3 disabled. Initial admission also waits rather than sampling a transient storage clock once. No MMC guard or runtime-PM owner is weakened.

SPM `dormant_attempts` counts admission calls BEFORE budget/static guards. The first real success included two consumed-budget refusals, and cycle17 included two earlier safe refusals before the last successful return. The original checker wrongly required exactly one admission, then wrongly required the last call to be budget-refused. Correct interpretation accounts every extra admission as an abort while requiring exactly one ACTUAL context entry/return/ success/ACK and all original restore guards plus checked sleep flag and SRAM reset stamp. Original FAIL receipts remain untouched; independent rechecks prove their genuine successful entries. Closing generic admission attempts 18455/aborts14808 reflect dynamic topology/clock/budget guards, not failed hardware entries. Counts can grow while owner transports/cores are restored.

No physical failure was retried. C3 was disabled/budget0 after each observer stop. One first success plus17 individually rechecked cycles were resumed through a hash-checked same-boot contiguous receipt; only the remaining3 were run. Normal policy was enabled only after the21 checks. New boots/source or missing/failed UART/context/restore evidence reject continuation before mutation. The sealed packaged harness remains historical; use current `tools/development/qualify-cpu-idle-completion.py` and neighboring device helper for subsequent qualification. c8ae170 contains these localized fixes;33 fresh harness/CPU/UART tests pass. Existing375/source109/native host/Reborn238/ARM/ QEMU/config/DT/modules/ABI/ELF/package validation remains valid because the installed kernel/production binaries are unchanged.

Raw evidence: `out/cpu-c3-uart-physical/20261003T183259Z-uart01/`. `final-verdict.json` joins all physical assertions; `guarded-21-cycles.json` retains every original row and corrected independent verdict; original `qualification/`, `corrected-c3/`, `repeat-c3/`, `repeat-c3-settled/` and final `final-c3/` receipts retain command/UTC/source/boot/exit/stdout/stderr and harness SHA256. `verified-18-entry-receipt.json` is explicitly derived and lists original receipt SHA256; final SSH status/health/dmesg/timers/IRQs are under `closing/` and `final-snapshot.json`.

### Research, changed files and owner action

Exact MT6582/Y2 research and pinned source/register/PCM origins are in [Y2-CPU-C3-UART.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART.md). This installed test required only `tools/development/cpu_idle_completion_device.py`, `tools/development/qualify-cpu-idle-completion.py` and `tests/test_cpu_idle_harness.py` fixes plus current validation/release/roadmap receipts. No Reborn or kernel implementation change after install.

Next owner action: none for this installed hardware qualification. Use the player normally. C3 remains runtime-enabled/budget-1 on this boot; original screen/radio/schedutil598–1300MHz/coordinator settings are restored and RGU is disarmed. Normal guards still exclude active USB/radios/workloads/high OPP or multi-core topology. Fresh boots remain default-off/budget0: persistent boot policy is a separate release decision. Full-system suspend, additional wake-source coverage, longer endurance and electrical battery measurement remain distinct work; the remaining UART1 C3 blocker is closed.

The following software handoff is historical, prior to this owner install.

## UART01 sealed software handoff — 2026-10-03

C3 SOFTWARE_READY_NEEDS_NEW_FLASH. New candidate physical NOT_RUN. Owner flash is the remaining boundary. C3 has never been entered on the connected candidate02; neither hardware failure nor hardware impossibility is established. C1/C2 physical working results are preserved.

Candidate: `out/y2linux-cpu-c3-uart-candidate/`. Build `Y2LINUX-CPU-C3-UART-01`, kernel `6.18.0-y2linux-cpu-c3-uart-01`, root `2025.02.18-platform-v1.20`, release `1.0.0-cpu-c3-uart-candidate.1`. Frozen Linux `e9e8d63f9c94232c2b6627881e0967583e202dac`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. Source commits `7ef608a` and `e9e8d63` implement the contract and required kernel errno include; subsequent docs are receipts, not a different installed/build source.````

| Payload | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 7208960 | a35e7ccb11dfcc642089e422d48a274ab2c700dbba15d00b21cce7b463e4006a |
| Y2ROOT.img | 536870912 | d3a8282a9f5d1b0046283bce1b595eb5797b62c2bff90a62260e80bbfafb5d98 |

Fresh kernel/Buildroot/Reborn ARM and config/DT/modules/ABI checks pass. Production suite375 cases: five minimal-host dependency skips are covered by native filesystem/GIO/ALSA tests and ARM compilation/query. Extended source contracts109, native packaging/filesystem/GIO27, ALSA evidence3 and Reborn238 cases pass; formatting/Clippy, Cortex-A7 QEMU, installed ARM helpers and ELF checks pass. Preserving package, source seal (445 source/license files) and sealed-image validation pass. Collector limitations remain recorded; this is an owner-local package, not public distribution approval.

Receipts: `out/cpu-c3-uart-validation/`; all integrated exit codes0. Manifest SHA256 `a43eb82521df9d94ec26b5b1cd46bd0234ff0807ffdcab7fedaf951deb04d48a`; checksum inventory SHA256 `c3041b0a848b2ce8a0a991238cee3433a43b33bf9e0654cd92e4c0bc9c945c49`. Source archives match the frozen pair. Only BOOTIMG/ANDROID payloads and accepted candidate02 fallback BOOTIMG/ROOT are packaged; no Y2DATA, preloader/LK/NVRAM/PROTECT/calibration/table payload.

Owner action: use `MT6582_preserve_data_scatter.txt`, Download Only, selecting BOOTIMG.img and ANDROID/Y2ROOT.img. Preserve existing Y2DATA. Boot normally, then confirm installation; the prepared SSH harness will verify identity and preserved regressions, attempt one25ms RGU/SRAM/budget1 timer wake, and allow20 further cycles only after real UART ACK and all same-boot restore checks pass. The packaged `CPU-C3-UART-OWNER-HANDOFF.md` gives the exact invocation. C3 stays default disabled/budget0 until the guarded physical test. No flash or push was performed; six preexisting owner doc edits remain unstaged.

Final read-only SSH receipt: `out/cpu-c3-uart-physical/20261003T164546Z/read-only-close.json`. Installed identity remains Linuxdb0234e/Rebornb71b4688, kernelidle-02/rootv1.19, boot `f155196b-64d4-45a4-88b3-27755a1a8926`, C3 disabled/budget0/entries0, expected prior probe taint4096. It contains no new UART handshake or deep wake.

2026-10-03: new C3 UART candidate NOT_RUN; C3 SOFTWARE_READY_NEEDS_NEW_FLASH. No hardware ACK or dormant entry is claimed.

Installed candidate02 remains physically C1/C2 WORKING. C3 has never been entered. Its settled blocker is hardware UART1 PERI bit17 at0x11003000, not the Linux UART0 console. Existing physical evidence remains authoritative in [Y2-CPU-IDLE-COMPLETION-PHYSICAL.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md). Fresh targeted read-only admission is under `out/cpu-c3-uart-physical/20261003T164546Z/`: Linuxdb0234e/Rebornb71b4688, kernelcpu-idle-02/rootv1.19, boot `f155196b-64d4-45a4-88b3-27755a1a8926`, C3 disabled/budget0, prior probe taint4096. No runtime controls, register writes or C3 attempts were made.

[The source contract and implementation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART.md) explain why an eligible active UART clock can defer to the stock global request/ACK rather than being forced off. The next result must capture the real ACK and return, not merely an improved preflight. Owner flashing is required to install those changes. A fresh normal boot removes the earlier probe taint; the harness requires taint0 and exact package identity before guarded tests.

Run the packaged host harness after owner confirmation. It checks preserved regressions, arms one bounded25ms timer wake with budget1/RGU/retained stages, then20 further checked cycles only after success. Require unchanged boot, new attempts/entries/resumes/successes and UART ACK, positive residency and all timer/CIRQ/context/clock/media restores. Missing ACK must record UART_BUSY, request cleanup and no dormant entry. Any failed trial disables C3 and stops repetition. Store new raw SSH evidence under `out/cpu-c3-uart-physical/`.

Do not overwrite the candidate02 counters or promote C3 physical/release status until those observations exist. Full-system suspend and electrical battery measurement are outside this narrow pass.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
