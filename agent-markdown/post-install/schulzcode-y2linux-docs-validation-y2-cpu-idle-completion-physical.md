---
title: "Y2 CPU idle completion physical qualification - Innioasis Updater"
description: "Y2 CPU idle completion physical qualification <!-- knowledge-base-scope: exact-image-validation-receipt; baseline02-sync 2026-10-03 -- Baseline02 scope and current eviden"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-idle-completion-physical.html"
---

# Y2 CPU idle completion physical qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 CPU idle completion physical qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 CPU idle completion physical qualification

## Baseline02 scope and current evidence

[Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) is now the newest sealed candidate with automatic qualified CPU0 C3 startup. New-image/cold-boot hardware remains PHYSICAL_NOT_RUN. The [UART01 physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) proves bounded C1/C2/C3 on its exact installed pair. Default-off, UART blocker, pending-flash and harness preparation statements below retain their recorded image/session scope. They do not describe the new Baseline02 startup policy or reopen the solved UART01 architecture. This report's original exact-image evidence is preserved; full system suspend and battery measurements remain separate.

## UART01 installed hardware result — 2026-10-03

C1 WORKING; C2 WORKING; C3 WORKING_AND_REPEATEDLY_OBSERVED. The owner installed UART01; exact manifest/running identity matches Linux `e9e8d63f9c94232c2b6627881e0967583e202dac`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-cpu-c3-uart-01`, root `2025.02.18-platform-v1.20`, release `1.0.0-cpu-c3-uart-candidate.1`, build `Y2LINUX-CPU-C3-UART-01`. Boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b` and taint0 remain unchanged. Source HEADc8ae170 is a later harness fix; installed kernel/source archives and both sealed payload hashes are unchanged. No new images or flash are needed.
  - C1: all four enabled states enter/reside,400 requested1ms wakes return;

entry deltas+1573/+521/+1343/+271, rejections0.
  - C2: natural owned CPU0 parking, +6971 entries/+50.654676s in60.054881s,

84.35% residency, zero exact clock restore failures.
  - C3: first checked reset return then20 further budget1/RGU/SRAM cycles;

+3624 entries/+39.204662s in60.088344s under normal policy, 65.25% DORMANT residency. Final3647 entries/resumes/successes/UART ACKs, no UART timeout or clock/CIRQ/timer/context restore fault.
  - All five OPPs,18 hotplug transitions, eMMC/inserted-SD checksums, screen/

workload/playback wake and USB/independent Wi-Fi integrity pass; no new filesystem/IRQ fault. GPT6/GPT4/PPI29/CNTFRQ13MHz/highres/NO_HZ remain valid.

UART1 remains clocked: source-backed PIO sleep ownership/global SPM request/ ACK permits real DPIDLE without forcing its PERI gate. Two observer defects were corrected locally: fsynced evidence must precede a read-only stable MMC/ prerequisite window; admission counters also include safe pre/post-entry guard refusals. EXACTLY one real entry/return/ACK per bounded cycle is still required, with stronger SRAM reset marker and all original restore guards. Original raw FAIL receipts are retained alongside independent successful rechecks. 33 targeted harness/CPU/UART tests pass; no kernel rebuild is needed for these host qualification corrections. Fresh candidate build validation remains375 integrated/source109/native host/Reborn238/ARM/QEMU/config/DT/modules/ABI/ELF/ package checks as recorded in the historical handoff below.

C3 is enabled with normal budget-1 for the current boot. Original screen, Wi-Fi/BT, schedutil598–1300MHz and coordinator settings are restored; RGU is unarmed. Fresh boots retain image default-off/budget0. Persistent default-on, full system suspend, endurance, additional wake sources and electrical battery improvement are not qualified by this pass. No flash/push or owner-data wipe.

Authoritative raw/joined evidence: `out/cpu-c3-uart-physical/20261003T183259Z-uart01/`; `final-verdict.json`, `guarded-21-cycles.json`, `final-snapshot.json`, `qualification/result.json`, `final-c3/qualification/result.json` and numbered SSH command/UTC/source/boot/exit/output receipts. Detailed current qualification: [Y2-CPU-C3-UART-PHYSICAL.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

The following sealed handoff and candidate02 sections are historical; their NOT_RUN/never-entered/owner-flash statements do not describe the current device.

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

## C3 UART admission software correction — 2026-10-03

Candidate02's C1/C2 WORKING results remain valid; C3 has never entered. Exact MT6582 sources show UART1 is in the default blocker mask but PIO UART owners conditionally permit their clock and enable sleep before the global SPM request/ACK. This missing integration is now corrected with guarded ownership,100us ACK refusal, exact restore and diagnostics. No gate/FIFO/ data/baud/reset write, unrelated guard removal or C1/C2 redesign is added. The new source/candidate boundary remains SOFTWARE_READY_NEEDS_NEW_FLASH; no hardware ACK or DORMANT success is claimed. See [Y2-CPU-C3-UART.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART.md) and [Y2-CPU-C3-UART-PHYSICAL.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

## Candidate02 hardware qualification — 2026-10-03

**C1 WORKING; C2 WORKING; C3 BLOCKED BEFORE ENTRY BY UART1. Overall CPU idle qualification FAILS.** The owner flashed candidate02 and authorized these tests. The installed SPI0 correction is observed: SPI0 is quiet and released. UART1 still prevents dormant admission. No physical C3 call, context loss, forced gate, reboot, flashing or push occurred. This section supersedes candidate02 NOT_RUN and owner-flash instructions in the historical sections below.

Private raw evidence: `out/cpu-idle-completion-physical/20261003T144857Z-candidate02/`. SSH receipts retain host UTC, installed source identity, boot ID, command, stdout/stderr and exit status. `qualification/result.json` is the full harness result; `settled-preflight-result.json` isolates the remaining C3 blocker; `final-snapshot.json` and `final-verdict.json` record the restored device.

### Exact installed identity

All candidate manifest axes, running kernel and Reborn build match:``````````````

| Axis | Installed value |
| --- | --- |
| Kernel | 6.18.0-y2linux-cpu-idle-02 |
| Linux source | db0234e7519c559031da6f427869ab683ffe0f3c |
| Reborn source | b71b468860233faa0a42b8448ec5777fa952b8e3 |
| Rootfs | 2025.02.18-platform-v1.19 |
| Release / build | 1.0.0-cpu-idle-completion-candidate.2 / Y2LINUX-CPU-IDLE-COMPLETION-02 |
| Boot ID throughout | f155196b-64d4-45a4-88b3-27755a1a8926 |

Source checkout HEAD at admission was `76567e5`, a later documentation commit; it is not the installed kernel source. Reborn remains unchanged. Cmdline is `rdinit=/init earlycon console=ttyS0,921600n8 console=tty0 loglevel=3 panic=0 log_buf_len=1M user_debug=31`. Package `out/y2linux-cpu-idle-completion-02-candidate/` is unchanged. Fresh hashes:````

| Payload | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 7213056 | aa371ce343801c41b0908aa85f7c11d7ae6de91cbbe93420ce1f7d29a5b0caa2 |
| Y2ROOT.img | 536870912 | 54b799fbcd6c85ef4b61c4210e68e1ee19efa8e6079fd2c96bf238e16d728f15 |

### C1, natural parking and useful C2 residency

All four WFI states are enabled; entries and residency advance with no rejection. Wake observations are elapsed times for requested 1ms sleeps, not direct silicon exit-latency measurements. Each core completes 100 bounded sleeps.

| CPU | Additional WFI entries | Residency, us | Rejections | Median / p95 wake, ms |
| --- | --- | --- | --- | --- |
| 0 | 725 | 12170037 | 0 | 1.084885 / 1.104192 |
| 1 | 923 | 12210872 | 0 | 1.084423 / 1.116499 |
| 2 | 1695 | 11737138 | 0 | 1.085116 / 1.090577 |
| 3 | 669 | 12282932 | 0 | 1.085578 / 1.139421 |

Maximum sampled wake1.522331ms; MONOTONIC/RAW drift−410237ns in12.076045s. C1 needs no redesign. Three Linux hotplug cycles pass all18 transitions, CPU3→2→1 off and1→2→3 on, with exact secondary bits checked in both SPM power copies. Natural coordinator parking reaches CPU0/owner0xe after141.129531s. Ten-second observer sampling does not time every intermediate automatic step; the existing one-core policy and physical hotplug checks remain intact. Screen and real playback demand restore all four cores, with no ownership error.

With screen off, radios runtime-off and natural CPU0-only topology, SLIDLE adds 6,772 entries and50,669,913us in60.048084272s: 84.38% C2 residency. SLIDLE failures0, brokenN, exact clock restore failures0, bus rejections0; the final single-core blocker mask is0. CPU0 WFI also adds3.858558s in the metrics window. Pre/post clock, bus, timer, MMC, IRQ, CPU and coordinator snapshots are retained. APDMA bit11/BTIF bit20 legitimately block when Wi-Fi is active; MSDC bits12/13 appear during actual I/O. No blocker mask is weakened.

| Window | Seconds | CPU utilization | CPUs | CPU0 WFI, s | C2, s | IRQ/s | Context switches/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Screen on idle | 20.062027 | 3.66% | 0–3 | 19.416767 | 0 | 445.82 | 511.02 |
| Screen off before parking | 20.077351 | 2.89% | 0–3 | 19.567692 | 0 | 352.89 | 399.46 |
| Screen off, parked, C2 enabled | 60.048084 | 8.04% | 0 | 3.858558 | 50.669913 | 184.84 | 340.11 |

C2-window MONOTONIC/RAW drift−694347ns; ending temperatures39.865/40.4°C. CPU utilization is aggregated over online cores. There is no electrical measurement or battery-life claim. The earlier baseline enabled/disabled comparison remains separate evidence; it was not repeated in this run.

### C3: initial topology race, then exact settled preflight

The full harness initially rejects topology, secondary power and UART1 clocks: fsynced storage work has correctly restored four cores after the C2 window. This exposes a harness sequencing defect, not failed Linux hotplug. The device helper now waits again for normal CPU0-only parking, owner0xe, both physical secondary power copies clear and20s stability after sync/USB detach. It never forces topology or arms C3 while waiting. Durable progress saves are limited to once per60s to reduce observer I/O; timeout/boot change fail safely. New guard tests cover ownership, both power copies, timeout and reset. The supplementary physical run demonstrates the same settled topology rule; the edited complete harness was not rerun because UART1 still blocks entry.

The settled run uses only supported owners: screen off, no workload, radios runtime-off, USB role none,747.5MHz and natural parking. C3 stays disabled; budget1 and the10s RGU backstop are armed only to expose read-only preflight, then cleared. Results:

| Prerequisite | Settled physical result |
| --- | --- |
| CPU topology / secondary power / domains | CPU0 only, owner0xe; both power copies0x314c; secondary/domain masks0 |
| Frequency / screen / workload | 747500kHz; screen off; no disallowed lease |
| System / boot policy / SPM / broken state | All report ready; no broken latch |
| Local events / CIRQ / context availability | All report ready; actual deep restore unexercised |
| Runtime budget / qualification backstop / USB restore owner | All report ready in bounded preflight; cleared/restored afterward |
| INFRA / display / bus clocks | All blocker masks0 |
| PERI clocks | 0x00020000: UART1 bit17; clocks prerequisite fails |
| Runtime PCM | Exact MT6582 d53dd75c DPIDLE PCM,480words |
| Resume/context diagnostics | Vector0x80012000, expected0x804833c0, enable0x80000000; stash0x81433140, context_last0; actual programming not exercised |
| Architectural/GPT4 deadline | Future >2ms /26000ticks at13MHz rule present; dynamic admission/finisher not exercised |

Every exposed static prerequisite except clocks passes. `unmet=clocks,`. Installed handoff diagnostics show UART1 LCR/IER/LSR/DMA0, `reason=tx_not_drained retained=1`; UART2/3 LSR0x60 release, SPI0 COMMAND0/STATUS1=1 quiet/released. Rechecks advance without CCF failures.

Dormant attempts, entries, resumes, successes and residency all remain0. CIRQ entry/replay, GPT4 dormant handoff and local timer context save/restore are unexercised. Thus CPU0 context loss/return, GIC/MMU/VFP/cache/coherency restore, near-boundary deadline trials and20 repeated wake cycles are not qualified. C3 stays off. This is neither a C3 success nor proof of an exact hardware limit.

### Targeted UART1 evidence; no unsafe clock forcing

Two temporary diagnostic modules are built for the exact installed ARM kernel, with actual-function native guard/failure tests under UBSAN (8+11 cases pass). They use the fixed source-pinned MT6582 windows and normal balanced CCF borrow/ release, require UART1 already clocked, and skip live/unknown/aliased states. Both return EAGAIN after cleanup, so expected `insmod` exit1 leaves no resident module. No userspace MMIO or UART FIFO/data/baud/IRQ/DMA/GPIO/reset writes occur.

The read-only snapshot reports PERI reset0/0, UART sleep0, FCR_RD0, ACTIVE_EN0, IRQ/DMA0 and LSR0. It excludes a held PERI reset/enabled sleep-control explanation; these names/default-like values do not prove transmitter idle. A second bounded transaction follows the exact MT6582 BSP divisor-save sequence, temporarily selecting LCR.DLAB0x80, reading DLL1/DLH0, then restoring LCR0 and verifying it. It requires CPU0, all four cores, coordinator disabled and both radio power copies off. Its first invocation safely skips a still-active radio power domain; the settled invocation succeeds with gates unchanged. LSR remains0. The UART has a nonzero divisor; no source-backed proof justifies accepting LSR0 or gating this retained engine. The production guard is preserved.

Exact sources: [MT6582 UART definitions](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/mt6582/platform_uart.h), [platform UART](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/mt6582/platform_uart.c), [common UART save/baud code](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/uart.c). Pinned local vendor/retained Y2 provenance remains in the source record. Register inferences are restricted to exact MT6582 evidence; no adjacent-SoC transplant.

The main qualification and settled preflight ran at taint0. Diagnostic module loading then truthfully sets out-of-tree flag4096, which remains until a normal owner reboot; it is not hidden or cleared. Final evidence records that expected flag, no resident probes, no new critical kernel errors and the same boot.

### Independent regressions, software checks and final state

Both eMMC11230000.mmc and inserted SD11240000.mmc pass16 fsynced uncached128KiB SHA256 rounds per medium, split before/after the failed C3 preflight, not a dormant wake. Ext4 errors remain0 on rootmmcblk0p7, datammcblk0p5 and SDmmcblk1p1; MMC errors/mismatches0. Final clocks gated on both hosts; retained context advances (eMMC633/632 suspends/resumes, SD4149/4148). No live-media reset, CRC, timeout or DMA corruption observed. SD absent is not physically tested.

All five OPPs pass before and after preflight:598/747.5/1040MHz at1.15V, 1196MHz at1.20V and1300MHz at1.25V. PWRAP readiness/readback and thermal authority pass; no lowered ceiling. GPT6 free-running13MHz, GPT4 sole broadcast, PPI29, all four CNTFRQ13MHz, highres/NO_HZ and bounded timer continuity pass with per-core timer errors0. None of these observations proves dormant timer restoration.

Real Reborn/FFmpeg/ALSA silent playback adds352256 decoded frames, with errors, xruns and recoveries unchanged0; PlaybackNormal demand restores all cores. Screen restore passes through normal Reborn/DRM ownership. Three bidirectional 1MiB USB rounds match host/device SHA256; the pinned independent Wi-Fi observer responds on the same boot. Actual transport failover, radio throughput/endurance, manual button edges, full-system suspend and electrical battery benefit are unobserved. Independent phase results pass; overall CPU idle acceptance fails C3.

Fresh locked-host checks:90 CPU tests,8 slow-idle/suspend-policy tests and2 workload QoS tests pass; the dedicated harness/completion21 host cases also pass. The prior sealed kernel/root/config/DT/ABI/package validation stays valid: no production kernel or rootfs source change is made this turn. Changed tracked files are the device helper/tests and validation/release/roadmap records. No empty replacement image.

Final C3disable1, budget0, RGU disarmed; coordinatorY, schedutil598000–1300000, USB device, Wi-Fi on/Bluetooth off and original screen-off policy restored. Temporary observer/probe files and modules are absent; cleanup errors0. Playback is stopped. Its original paused selection was an already deleted historical qualification fixture, so it cannot be resumed through the normal owner API; the invalid preexisting selection is recorded, not silently replaced by music. Y2DATA and protected partitions remain intact. Issues#16/#27/#28/#29/#31/#32/ #33/#34 stay OPEN; no release milestone is closed.

Next boundary: resolve UART1 ownership with exact source/hardware evidence before another guarded C3 entry. There is no newly built image to flash, no request to reflash candidate02 and no safe supported live control that proves this retained UART can be gated. C1/C2 remain usable; C3 remains disabled.

## Candidate01 hardware qualification — 2026-10-03

C1 WORKING; C2 WORKING; C3 BLOCKED BEFORE PHYSICAL ENTRY. The owner installed the sealed images and authorized this hardware run. The automated overall qualification FAILS because C3 cannot pass its real clock prerequisites. Independent regressions completed; no reset, corruption or forced entry occurred. Earlier baseline results below are historical and do not substitute for this run.

Private evidence: `out/cpu-idle-completion-physical/20261003T130848Z-candidate/`. Admission, source/boot-tagged SSH command/stdout/stderr/exit receipts, durable qualification job and result, post-run state and summary are retained. Installed identity matches every candidate axis: Linux `3dfb5f5cc731ec5dac88a778290819c23dba6067`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-cpu-idle-01`, root `2025.02.18-platform-v1.18`, release `1.0.0-cpu-idle-completion-candidate.1`, build `Y2LINUX-CPU-IDLE-COMPLETION-01`. Boot `e0eb2f36-7c1f-4007-99e2-81d2eae047d4` stays unchanged; taint0 throughout.

### C1, parking and C2

All four WFI states are present and enabled. During the bounded qualification:

| CPU | Additional entries | Residency, us | Rejections | Median / p95 wake, ms |
| --- | --- | --- | --- | --- |
| 0 | 1271 | 11972491 | 0 | 1.083999 / 1.095614 |
| 1 | 1050 | 12207881 | 0 | 1.084691 / 1.110306 |
| 2 | 990 | 12337826 | 0 | 1.084306 / 1.093922 |
| 3 | 612 | 12244397 | 0 | 1.084306 / 1.091383 |

Maximum sampled1ms wake1.706998ms; MONOTONIC/RAW drift-9575ns in12.068182s. Three supported hotplug cycles pass all18 transitions and both physical power copies, CPU3→2→1 off and1→2→3 on. Automatic parking subsequently honors its pressure hold: first CPU3 parked at252s, CPU0/owner0xe at262s. Ten-second observer sampling does not individually time CPU2/CPU1; supported hotplug/source tests prove their exact physical bits and one-core policy. Screen wake and real PlaybackNormal demand restore all four cores without ownership errors.

Screen off and radios runtime-off make C2 naturally eligible. SLIDLE adds 7,040 entries and49,674,049us in60.047964546s (82.72%), with WFI4.061876s. SLIDLE failures0, bus rejections0, clock restore failures0, final blocker0 in this window. Active APDMA/BTIF are legitimate blockers when Wi-Fi returns; MMC request blockers appear during real I/O and disappear afterward.

| Window | Seconds | CPU utilization | CPUs | CPU0 WFI, s | CPU0 C2, s | IRQ/s | Context switches/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Screen on idle | 20.076549 | 3.58% | 0–3 | 18.649760 | 0 | 452.82 | 529.22 |
| Screen off before parking | 20.070139 | 3.41% | 0–3 | 19.450031 | 0 | 351.67 | 403.19 |
| Screen off, parked, C2 enabled | 60.047965 | 9.47% | 0 | 4.061876 | 49.674049 | 187.72 | 343.06 |

C2-window MONOTONIC/RAW drift218003ns. CPU utilization is aggregated over online cores; this is not an electrical comparison. Temperatures stay below the 75°C test guard (observed CPU about38–44.7°C). No measured battery-life claim.

### C3 preflight failure and exact remaining owners

Normal controls stop playback, turn radios runtime-off, detach USB through its role owner, cap747.5MHz, use automatic CPU0-only topology and arm the existing 10s RGU backstop with budget1. Preflight then reports:
  - Power copies0x314c/0x314c; secondary mask0, blocked domains0.
  - PERI blockers0x02020000 = UART1 bit17 + SPI0 bit25.
  - INFRA blockers0, DISP0/1 blockers0, bus0.
  - Every other exposed static prerequisite category passes; only clocks fails.
  - Runtime PCM480words, originMT6582_d53dd75c_dpidle; CIRQ ready and inactive.
  - Dynamic architectural/GPT4 deadline and actual context/vector programming

were not exercised: no actual dormant call was admitted.

Boot warnings identify both as retained active/unknown loader engines. CCF summary shows zero enable/prepare references and no consumer for both. Only UART0 at0x11002000 is Linux's serial owner; UART1's sampled window is0x11003000, SPI0's0x1100a000. Installed diagnostics do not expose the boot-time raw operands, so the exact UART busy field and observed SPI status value remain unknown. No userspace MMIO, register forcing, driver reset, guard bypass or fake counter.

SPM dormant attempts/entries/resumes/successes/residency remain0. CIRQ entries/ flushes and local timer context saves/restores remain0; no error in those counters is proof of dormant restoration. Near-boundary and20-cycle trials correctly do not run after failed preflight. C3 remains disabled, budget0, backstop disarmed. This is a software/clock ownership gap, not evidence of a hardware limit.

Source follow-up corrects the SPI predicate that treats the vendor's nonzero idle indication as busy, distinguishes UART timeout metadata from real DMA, retains error/unknown/aliased UART states, and adds boot-time read-only operands and reason names. See [the source record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md). A follow-up candidate must physically prove these decisions before any C3 success claim.

### Independent regressions and restored state

Both eMMC and inserted SD pass8 fsynced, uncached128KiB SHA256 rounds in each storage phase (16 per medium total). Ext4 errors remain0 for current root/data `mmcblk0p7`/`mmcblk0p5` and SD`mmcblk1p1`; driver errors/mismatches0. Runtime suspend/resume/retained-context counts advance and clocks gate afterward. SD absent is not observed. No mounted media reset or calibration access.

Both OPP sweeps reach598/747.5/1040MHz at1.15V,1196MHz at1.20V,1300MHz at1.25V, with original schedutil598000–1300000 policy restored. The second sweep follows C3 preflight, not dormant wake. GPT6 free-running13MHz, GPT4 sole broadcast, architectural PPI29/highres/NO_HZ and all four CNTFRQ readbacks remain intact; per-core timer errors0 and bounded continuity pass. Actual dormant timer handoff and CIRQ/GIC/MMU/VFP/cache restoration remain unobserved.

The real Reborn/FFmpeg/ALSA silent44.1kHz stereo test adds356,352 decoded frames, with decode/filter/playback errors0 and xruns0. Screen restore/all-core demand wake pass. Three1MiB USB bidirectional transfers match SHA256 on host/device; the separately pinned Wi-Fi observer responds on the same boot. Automatic USB→Wi-Fi fallback was not required during sparse polls; both may intentionally be unavailable while legitimate radio-off/USB detach controls run locally.

Finally screen off/Wi-Fi online/Bluetooth off/coordinator enabled/original DVFS and USB role are restored. Temporary test files and owned Wi-Fi listener are removed. The initial paused selection referred to an already deleted historical qualification fixture (track414), so it cannot safely be resumed; playback is left stopped. No new filesystem/IRQ fault, same boot, taint0. Full-system suspend is excluded because its historic resume failure remains a separate gate. No flash or push occurred.

## Historical installed baseline qualification

The previous installed baseline was qualified on 2026-10-03. Private raw evidence: `out/cpu-idle-completion-physical/20261003T074026Z/`. Every SSH receipt includes host UTC time, exact command, output, exit code, compiled source identities and boot identity. The automated candidate qualification is a separate run after owner flash; no candidate hardware result is claimed here.

Installed Linux `131ee4621cd583c955182f994adac5a594fb823f`, Reborn `7f9df397ab3809d52e2f1073ca93a305246e0c3a`, kernel `6.18.0-y2linux-baseline-01`, root `2025.02.18-platform-v1.17`, release `1.0.0-baseline-candidate.1`, boot `cee326c1-a5b0-447a-8eb0-dc3f39f7e2c2`, taint0. Runtime identity matches the sealed baseline BOOTIMG/Y2ROOT metadata, rather than being inferred from repository HEAD. The authorized USB SSH path was used, with a same-boot Wi-Fi observer verified before radio-off testing.

## C1: WORKING

Receipt `04-c1-all-cores`: all four CPUs online through the supported coordinator control, 100 one-millisecond sleeps pinned to each CPU, then a bounded 12-second idle window. Original coordinator policy was restored in finally.

| CPU | New WFI entries | New residency, us | New rejections | Median / p95 wake, ms |
| --- | --- | --- | --- | --- |
| 0 | 1123 | 12028655 | 0 | 1.071535 / 1.290226 |
| 1 | 916 | 12137106 | 0 | 1.082920 / 1.096997 |
| 2 | 649 | 12236436 | 0 | 1.087458 / 1.091458 |
| 3 | 1214 | 11744082 | 0 | 1.087227 / 1.095612 |

MONOTONIC versus MONOTONIC_RAW difference changed -39154 ns. Same boot, taint0, all cores returned. C1 architecture is frozen.

## C2: WORKING

Receipts `07`/`08` first establish legitimate APDMA/BTIF blockers with Wi-Fi on, and no such blockers with radios off. An initial 60-second observation did not produce C2 while the coordinator was honoring a four-minute pressure hold. That is a policy hold, not evidence of broken MMC clock gating.

Receipts `09`/`10` allow the existing policy to settle without bypassing its hysteresis. A radio restore/start-up burst escalated the hold to 480000 ms. Thirty-second observations show CPU3 parked at `settle-16` and CPU2/CPU1 parked by `settle-17`. Final owner mask0xe, CPU0 only, quiet139040 ms, sustained load129 millicores and high-frequency residency148 per mille. No manual offline was used to make this C2 window eligible.

During the 60.404075502-second CPU0-only, screen-off/radios-off window:
  - SLIDLE entries2657 ->9839: +7182.
  - SLIDLE residency18394631 ->69158372 us: +50763741 us, or50.763741 seconds,

approximately84.0% of wall time.
  - CPU0 WFI entries+1584, residency+3901404 us; DORMANT entries0.
  - SLIDLE failures0, clock restore failures0, brokenN, bus rejection0.
  - SLIDLE clock blockers0; both MMC controllers gated before and after.
  - CPU utilization8.5795%, IRQ168.250/s, context switches338.785/s.
  - MONOTONIC versus MONOTONIC_RAW difference changed -64809 ns.

The clock transaction restores the exact inherited bus configuration; no bit was removed from a blocker mask. The source change from Fix03 is present in the baseline and physically resolves the historical reset-default bus rejection. Preserve it rather than redesigning working C2 or storage.

## Storage after C2

Both eMMC and inserted SD were mounted and usable. In each of the two radio-off runs, eight fsynced, uncached SHA256 readback cycles per medium passed. Temporary random test files were removed. `mmcblk1p7`, `mmcblk1p5`, `mmcblk0p1` ext4 error counts remained0. Runtime suspend/resume and retained-context counters advanced on both controllers, with mismatches0/errors0 and both clocks gated afterward. Request refusal counts increased during real I/O, as required; DMA/controller/ FIFO/IRQ busy refusals remained0. No reset of mounted media was attempted. SD-absent operation is not observed: physical card removal requires the owner. The post-flash harness records whichever media are actually present.

## Hotplug, DVFS and timers

Receipt `11-hotplug-opps`: three complete supported hotplug cycles, offline CPU3 ->CPU2 ->CPU1 and restore CPU1 ->CPU2 ->CPU3, 18 transitions total. SPM power copies were captured at each step, proving physical secondary power-off rather than only scheduler exclusion. All CPUs then passed pinned one-millisecond sleeps (median about1.084 ms, maximum p95 about1.111 ms).

All five guarded OPPs were actually reached under bounded min=max policy: 598000,747500,1040000 kHz at1150000 uV;1196000 at1200000 uV;1300000 at1250000 uV. Voltage faultN, PWRAP request/readback error0. Original limits, schedutil and coordinator policy were restored. CPU temperature44–45.1 C, PMIC42.204–42.789 C. Same boot, ext4 counts0.

GPT6 free-running13 MHz, GPT4 broadcast, architectural physical timers/PPI29, high-resolution timers and NO_HZ are observed in initial raw state and bounded continuity receipts. No timer foundation was replaced.

## C3: SOFTWARE_READY_NEEDS_NEW_FLASH

The installed baseline has C3 registered but default disabled and never physically entered. It was not forced past current live prerequisites. Live preflight identifies frequency, powered radios, active/inherited display and peripheral clocks; the old unconditional DISP-power predicate additionally contradicts the exact MT6582 vendor clock-based condition. Screen-off currently blanks the backlight but keeps DRM scanout running.

Source fixes, candidate artifacts and the next qualification command are recorded in [the implementation record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md). This label is the software handoff category, not a claim of a successful DORMANT entry. Receipt12 additionally proves a USB0 clock ownership leak: normal role none changes MUSB active ->suspended, but PERI bit10 stays active; restoring device returns MUSB active on the same boot. No unsafe MMIO interface was used.

The new candidate must verify one bounded real CPU reset/resume, then at least 20 bounded cycles with unchanged boot identity, timer/IRQ/context continuity, restore counters, storage and interactive workload regressions. A failed first attempt quarantines C3; it is not automatically hammered again.

No electrical energy measurement was made. Residency is demonstrated; battery life improvement is not claimed. No flash or push occurred.

## Playback and demand wake

Receipt16 creates, scans and plays a temporary silent44.1-kHz stereo WAV through the actual Reborn/FFmpeg/ALSA pipeline. Eight seconds add352256 decoded frames; xruns, recoveries and playback errors add0. All cores online, a real PlaybackNormal lease active. Playback stopped and the fixture removed/rescanned. Receipt14 found no old retained fixtures and is explicitly not a playback pass.

Receipts17/18: normal Reborn screen-on/off transitions return on the same boot; three bidirectional1MiB USB SHA256 rounds pass with independent Wi-Fi SSH ready. These awake results do not qualify the candidate's new bus-clock gate yet.

## Controlled residency comparison

Receipt21 completes a device-side comparison without host polling during each window; initial screen/radio/C2 policy restored in finally, same boot, taint0. No C3 control was changed. Frequency residency and temperatures are retained alongside each raw before/after snapshot.

| Condition | Wall seconds | CPU utilization | Online CPUs | CPU0 WFI, s | CPU0 SLIDLE entries / seconds | IRQ/s | Context switches/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Screen on idle | 20.083 | 4.25% | 0–3 | 19.084 | 0 / 0 | 444.75 | 518.34 |
| Screen off before parking | 20.070 | 3.08% | 0–3 | 19.500 | 0 / 0 | 315.69 | 397.46 |
| Parked, C2 enabled | 30.062 | 9.39% | 0 | 1.942 | 3448 / 25.022727 | 168.42 | 337.24 |
| Parked, C2 disabled | 30.048 | 8.80% | 0 | 27.109 | 0 / 0 | 166.97 | 335.10 |
| Parked, C2 re-enabled | 30.048 | 9.23% | 0 | 1.964 | 3437 / 25.015727 | 167.96 | 338.02 |

SLIDLE occupies83.2% and83.3% of the enabled windows; disabling it shifts residency to WFI and re-enabling restores real deeper residency. CPU utilization is aggregated across the online cores, so the four-core and one-core percentages are not an energy comparison. The raw OPP time-in-state deltas show the unchanged schedutil policy, including short active high-frequency bursts. No new cpuidle rejection appears. MONOTONIC/RAW drift is between-74211 and-124163ns. CPU/PMIC temperatures are roughly39.9–45.1°C; conditions include external USB power and radio state changes. No battery-life or electrical-power claim follows.

Receipt22 final status/health/dmesg confirms the original installed identity, USB device role, schedutil598000–1300000kHz, C2 enabled, C3 disabled, same boot, taint0 and all three mounted ext4 error counts0. Normal Wi-Fi is online; the original screen is off and policy owns parking. Receipt23 stops only this pass's verified temporary Dropbear listener; ordinary USB SSH remains available.

The exact physical hotplug power mapping in receipt11 is CPU1=0x800, CPU2=0x400, CPU3=0x200 in both status copies. CPU3-off produces0x3d4e, then CPU2-off0x394e, then CPU1-off0x314e; restoration reverses these values. The kernel already used this descending MT6582 mapping. The new harness now checks these exact operands and has a regression fixture for a mismatched second status copy. An earlier unsealed package was rejected before handoff while that harness correction was incorporated; no device flash occurred.

Receipt25 runs the final candidate harness against this still-installed baseline. It rejects mismatched kernel, Linux, Reborn, rootfs, release and build identities before any device mutation; only two read-only SSH operations occur. Receipt26 reconfirms same boot/taint0, C2 enabled, C3 disabled, normal owner policies and mounted ext4 error counts0 at handoff.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
