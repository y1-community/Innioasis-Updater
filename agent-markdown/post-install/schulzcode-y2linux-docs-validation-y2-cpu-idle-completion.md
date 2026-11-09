---
title: "Y2 CPU idle completion - Innioasis Updater"
description: "Y2 CPU idle completion <!-- knowledge-base-scope: exact-image-validation-receipt; baseline02-sync 2026-10-03 -- Baseline02 scope and current evidence Baseline02 Y2-BASELI"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-idle-completion.html"
---

# Y2 CPU idle completion - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 CPU idle completion

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 CPU idle completion

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

## Candidate02 installed hardware result — 2026-10-03

The owner-installed candidate02 is now physically tested. **C1 WORKING, C2 WORKING; C3 BLOCKED BEFORE ENTRY BY UART1. Overall acceptance FAILS C3.** This supersedes candidate02 NOT_RUN/SOFTWARE_READY_NEEDS_NEW_FLASH and its installation instruction below; the sealed images have already been flashed. No exact hardware limit is established and no dormant success is claimed.

Installed Linux`db0234e7519c559031da6f427869ab683ffe0f3c`, Reborn`b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel`6.18.0-y2linux-cpu-idle-02`, root`2025.02.18-platform-v1.19`, release `1.0.0-cpu-idle-completion-candidate.2`; unchanged boot `f155196b-64d4-45a4-88b3-27755a1a8926`. Every installed manifest axis matches. The [physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md) contains full counters, individual prerequisites, sources, limitations and restored state. Raw evidence: `out/cpu-idle-completion-physical/20261003T144857Z-candidate02/`.
  - Four-core WFI entries+725/+923/+1695/+669, residency advances, rejections0.
  - Natural CPU0/owner0xe parking; C2+6772 entries/+50.669913s in60.048084s

(84.38%), clock restore failures0.
  - Three hotplug cycles/18 physically checked transitions; all five OPPs before/

after preflight, timer continuity, both media integrity, screen/playback and USB/independent Wi-Fi observation pass.
  - Installed SPI0 STATUS1=1 now correctly releases the gate. Settled C3 preflight

has only PERI UART1 bit17/0x20000 unmet; CPU0, both physical secondary power copies, domains,747.5MHz and all other exposed static predicates pass.
  - Actual dormant calls/entries/resumes/residency0. GPT4 dormant deadline,

CIRQ/GIC/context/MMU/VFP/cache/coherency return and20 wake cycles unexercised.

The full harness first caught a second issue: synced storage demand restores cores after its C2 window, so C3 must wait for normal parking again. The device helper now requires CPU0/owner0xe/both secondary power copies clear for20s after sync/USB detach, before budget/backstop/preflight. It uses sparse durable progress writes and rejects timeout/boot change without arming entry. Two new behavioral tests cover ownership, both physical copies and safe failures; the existing first-failed-cycle quarantine test remains. Fresh locked-host CPU90, slow-idle/suspend-policy8 and workload QoS2 cases pass; dedicated host harness/completion21 cases pass. The supplementary physical settled run validates the topology requirement, while the edited full harness is not repeated against the known UART1 blocker.

Exact-kernel, nonresident diagnostic probes establish UART1 reset0/0, sleep/FCR_RD/ACTIVE_EN/IRQ/DMA/LSR0 and DLL1/DLH0; the temporary divisor bank selection restores LCR exactly. Their native guard/failure19 cases and ARM builds pass. These observations do not justify treating LSR0 as drained or forcing its clock off. No production clock guard/reset changes follow. Normal CCF references balance, no resident probe remains; the final expected diagnostic out-of-tree taint4096 is recorded. Main qualification/settled preflight were taint0; no C3 trial occurs under diagnostic scope.

Only the host/device qualification helper, its tests and evidence/roadmap/release records change this turn. Kernel/rootfs binaries and sealed package are unchanged; fresh payload recheck matches the hashes below. No new candidate, flash or push. Normal controls restore, C3 off/budget0/backstop disarmed, ext4/MMC errors0. Playback stays stopped because the original paused selection referenced an already deleted historical fixture. Full-system suspend and electrical battery benefit remain unqualified. Next boundary is exact safe UART1 ownership closure before any bounded dormant trial; there is no new owner flash action this turn.

## Candidate02 sealed software handoff — 2026-10-03

Hardware tests are complete on installed candidate01: **C1 WORKING, C2 WORKING, C3 blocked before entry by UART1/SPI0**. No C3 entry/resume/restoration success is claimed. Same boot`e0eb2f36-7c1f-4007-99e2-81d2eae047d4`, taint0, mounted media errors0; final receipt restores screen/radio/USB/DVFS/coordinator state. The failed clock preflight led to the guarded source fixes below and one coherent follow-up. Candidate02 C3 category: SOFTWARE_READY_NEEDS_NEW_FLASH. This means ready for controlled qualification; whether its guards clear both retained engines remains unobserved. It is not proof of a hardware limit or C3 acceptance.

Latest candidate: `out/y2linux-cpu-idle-completion-02-candidate/`. The installed candidate01 at`out/y2linux-cpu-idle-completion-candidate/` remains unchanged. Built source Linux`db0234e7519c559031da6f427869ab683ffe0f3c`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. Kernel`6.18.0-y2linux-cpu-idle-02`, root`2025.02.18-platform-v1.19`, release`1.0.0-cpu-idle-completion-candidate.2`. All current integrated code is included; later source HEAD changes are receipts.````

| New payload | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 7213056 | aa371ce343801c41b0908aa85f7c11d7ae6de91cbbe93420ce1f7d29a5b0caa2 |
| Y2ROOT.img | 536870912 | 54b799fbcd6c85ef4b61c4210e68e1ee19efa8e6079fd2c96bf238e16d728f15 |

Fresh kernel/config/DT/modules/ARM ABI and Buildroot/Reborn ARM pass. The fresh full build preceded the final late-handoff review; all affected components and local ARM packages were rebuilt from frozen db0234e afterward, with a new root image and matching identities. No reused userspace/root image. Production366 cases:361 pass in the locked host, five explicit native prerequisite skips; all five are covered by30 native packaging/evidence cases with no skips. CPU/idle source owner/fault suite100 pass; Reborn238 pass/0ignored, fmt/clippy pass. ARM/QEMU,31 platform imports, null-ALSA constraints/1000-track benchmark, 383 ARM ELF files/1403 dependency edges, inventory/legal-info, preserving/root/ package composition/privacy/source/checksum validation pass. Unchanged pinned third-party inputs are retained; software checks do not establish C3 hardware. Receipts:`out/cpu-idle-completion-02-validation/` and package`validation/`. The unsealed inventory initially rejected newly attached harness files; it was refreshed before successful source sealing and final validation. No rejected staging package was handed off or flashed.

Only BOOTIMG+ANDROID/Y2ROOT are new payloads. Y2DATA remains in place; no preloader/LK/NVRAM/PROTECT/calibration/factory/table payload. Exact Hardware02 fallback is retained. New source files in this follow-up: clocks.c/clocks.h, idle-clock-policy.h/system-idle.c, production config/release metadata, observe.py and test_cpu_idle_completion.py, plus the linked validation/release/ roadmap records. Preexisting six owner documentation edits remain separate. Local source commits:`143fab1` (SPI/UART decisions/diagnostics/physical record), `db0234e` (late handoff/clear-on-read protection/CCF fault tests). Reborn is unchanged from the integrated b71b4688 DRM ownership fix.

Exact next owner action: install only this candidate02's BOOTIMG and ANDROID/Y2ROOT using its preserving scatter, keep USRDATA/Y2DATA unselected, then report installation. The agent will run the bundled guarded SSH harness once: all prerequisite checks, one bounded entry, then19 further cycles only on success, failure quarantine and independent regressions. The package's `CPU-IDLE-OWNER-HANDOFF.md` also provides the one-command option. No flash/push was performed. Full-system suspend and electrical battery benefit stay separate.

## Candidate01 hardware result and candidate02 follow-up — 2026-10-03

The installed candidate01 is now physically tested, Linux3dfb5f5/Rebornb71b4688, boot `e0eb2f36-7c1f-4007-99e2-81d2eae047d4`. **C1 and C2 WORKING; C3 blocked before entry by UART1/SPI0 clocks. Overall qualification FAIL.** C2 adds7,040 entries/49.674049s in60.047965s (82.72%); restore/storage errors0. Hotplug, parking, all five OPPs, screen/workload wake, real playback and USB/Wi-Fi pass. Detailed [physical record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md) supersedes the old "not run" handoff statement below. No actual dormant entry or battery measurement.

The clock owners retained two unsupported loader engines, with no Linux consumer/CCF reference. Candidate01 exposes neither raw handoff decision. We cannot infer UART's exact field or prove that software fixes below release both clocks until another owner flash. No supported installed control owns those engines, so no safe runtime clock forcing is available or attempted.

Source-backed candidate02 changes are limited to the existing unused-clock owner, diagnostics and regression tests:
  - SPI CMD+0x18/STATUS1+0x20: the pinned MT6582 vendor `spi_is_busy` helper says

STATUS1 bit0=1 is idle. Candidate01 wrongly rejected all nonzero status and accepted0. Accept exactly1 only with no ACT/RESUME/reset/pause/DMA operands; keep unknown status/active engines. STATUS0+0x1c is clear-on-read and is never sampled. The corroborating helper is commented in these BSPs; this is source interpretation, not an observed Y2 status value or completed physical fix.
  - UART DMA_EN+0x4c: exact MT6582 defines RX/TX DMA bits0/1 and timeout-counter

auto-reset metadata bit2. Metadata alone no longer falsely implies DMA. IRQ-enabled, DLAB/alternate bank, RX data, incomplete TX, line/FIFO errors and unknown DMA/status bits remain blocked. No UART interrupt/FIFO/DMA reset/write.
  - Sample known operands only while their inherited clock is enabled, retain

the boot/latest idle recheck in a read-only `clocks/unused_handoff` diagnostic with reason names, and surface it in `y2-platform status cpu`. DLAB/alternate banks are retained without reading aliased IER/LSR fields; live IRQ/DMA owners are not disturbed by clear-on-read LSR, and already gated engines are not read.
  - Partial NAND/PWM clock handoff retains its gate rather than returning a

probe-aborting error for the entire shared CCF provider. Real allocation/ mapping errors still fail provider registration.

The unused-clock owner also rechecks retained UART1–3/SPI0 through the existing CPU0-only, screen-off, lease-free deferrable worker, only with both radios physically off. It borrows/releases through CCF, keeps IRQ/DMA/unknown engines, never reads gated or aliased windows, avoids live UART clear-on-read LSR, and quarantines a failed gate readback. A transient loader operation no longer pins its clock forever. No new timer, coordinator-policy/hysteresis change or reset. Native fault tests cover real refs, still-busy engines, unavailable domains, unclocked skips, allocation/borrow and gate-readback failures.

Masks, C1/C2 algorithms, MMC high-speed/runtime PM, timer broadcast, PCM, CIRQ/context/coherency, coordinator hysteresis, guarded OPPs and ABI remain unchanged. New tests exercise genuine busy/unknown/metadata/idle states, aliased banks, clear-on-read avoidance and partial provider handoff. Candidate02 uses kernel`6.18.0-y2linux-cpu-idle-02`, root`2025.02.18-platform-v1.19`, release `1.0.0-cpu-idle-completion-candidate.2`, build`Y2LINUX-CPU-IDLE-COMPLETION-02`. Fresh build/qualification and exact candidate hashes are recorded at sealing.

Primary source references (pinned MT6582; no adjacent-SoC transplant): [UART platform definitions](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/mt6582/platform_uart.h), [UART platform lifecycle](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/mt6582/platform_uart.c), [SPI d53 source](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/spi/mt6582/spi.c), [SPI 3be93a68 cross-check](https://android.googlesource.com/kernel/mediatek/+/3be93a68c209393cfe24a842e2d5896a17ea37dc/drivers/misc/mediatek/spi/mt6582/spi.c), [krillin MT6582 cross-check](https://github.com/ubports/kernel_krillin/blob/874057f3c28735d606385361fb9a4cd4545ceba6/mediatek/platform/mt6582/kernel/drivers/spi/spi.c). Private source downloads and hashes remain under `out/cpu-idle-completion-research/`.

## Historical candidate01 software handoff

Owner-authorized CPU completion pass,2026-10-03. Entry baseline Linux `131ee4621cd583c955182f994adac5a594fb823f` / Reborn `7f9df397ab3809d52e2f1073ca93a305246e0c3a` is verified against the installed kernel/root/release and sealed package. Entry boot `cee326c1-a5b0-447a-8eb0-dc3f39f7e2c2`, taint0. No flash or push is permitted. Preexisting owner documentation changes are preserved separately from this pass.

## Physically established foundation

[Raw qualification and results](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md): C1 WORKING on all four CPUs. C2 WORKING after natural parking:7182 additional entries, 50.763741s residency in60.404076s, exact clock restore failures0, eMMC/SD integrity and timer continuity. Freeze both algorithms and the proven MMC transport/PM patch; do not import the reverted later storage experiment. Three hotplug cycles prove both physical power-status copies; all five guarded OPPs and real wired playback pass. Historical full-system suspend failure remains a separate gate.

## Source changes and ownership

| Defect/prerequisite | Resulting source behavior | Evidence/guard |
| --- | --- | --- |
| Screen off left DRM scanout active | Reborn's existing DRM master synchronously disables its CRTC, retaining its current GBM/EGL buffer; wake restores the same owned mode before lighting the screen | Pending flip bounded; failed disable/wake rolls back screen model; first-frame/LK handoff covered; no synthetic suspend |
| Permanent shared display clock holds | MT6582 mutex now owns SMI_COMMON/SMI_LARB0/MUTEX in a balanced bulk lifecycle alongside its32k clock | Lima retains an independent SMI_COMMON reference; other SoCs unchanged; loader clocks protected until real owner handoff |
| Inherited unused MM clocks | Stopped CRTC/mutex owner retires BLS enables (Linux's Y2 route bypasses BLS), then acquires/releases only demonstrably quiet unsupported clocks through CCF | GREQ/DMA/CMDQ/engine checks, coupled operands snapshotted before any gate; unpowered windows never read; live/unknown engines retained, never reset |
| Inactive PERI/INFRA clocks | Expose exact MT6582 NFI/NLI,PWM,UART1–3,SPI0,L2C_SRAM/TRNG/CPUM gates to normal CCF unused-clock ownership | UART0 console/thermal/AUXADC/EFUSE retained; active UART/DMA/NAND/PWM/SPI state stays blocked; NAND register access requires both stock clocks enabled |
| Stopped audio clocks retained loader gates | Real AFE runtime owner can release AUDIO/AUDINTBUS/INFRA_AUDIO at reference zero | Initial unused sweep remains protected; existing AFE DMA/PCM lifecycle preserved |
| USB0 gate leaked despite suspended MUSB | USB glue claims a real CCF bus clock only after safe initialization; generic MUSB runtime PM saves endpoints, checks detached/session/FIFO/all8DMA/IRQ idle, gates, then restores clock before any MAC context access | Physical receipt12 proves current leak; ordinary role none/device; inherited gate protects failed probe; parent rate remains honestly unknown; no USB PLL/PHY retune |
| Wrong unconditional DISP-power rejection | C3 admits powered DISP only when the complete exact stock DISP0/1 masks are quiet | PERI/INFRA masks remain intact; MD/CONN/MFG/ISP/VDEC and physical secondary power bits remain strict |
| C3 runtime control | Default C3 remains off; positive dormant_budget permits that many actual cpu_suspend calls; -1 is deliberately qualified normal policy | Qualification budget requires owner-armed existing RGU10–30s; journal captures exact stage; bounded first failure cannot be repeatedly hammered |
| Opaque admission/context | Read-only preflight exposes every static prerequisite and real topology/OPP/clock/domain/PCM/vector/stash operand; status cpu decodes C2 and C3 owners | Dynamic deadline checked at actual admission and finisher; unknown/missing counters are not success |
| Timer handoff | Linux remains sole GPT4 broadcast programmer; require13MHz one-shot, IRQ armed, not pending, compare in future, at least26000ticks | 64-bit ticks*1000/13 conversion, past/wrapped/near/repeating/incorrect-clock rejection; no second clockevent owner |
| Local timer context | Per-CPU save-valid state rejects incorrect CNTFRQ; restore disables CNTP, restores13MHz and saved64-bit compare/control before Linux reprograms the local event and verifies writable state | Unentered CPU_PM_ENTER_FAILED does not restore an uninitialized buffer; restore faults quarantine C3 |
| CIRQ correctness | Exact155 interrupts64–218, five banks/tail0x07ffffff; clone mask/sensitivity/polarity readback before GIC masking; replay pending after Linux GIC restore; verify masks and disable | Exact MT6582 offsets and enable/edge-only ordering; no newer-SoC FLUSH layout; clone/restore faults quarantine C3 |
| CPU/cache/context | Linux cpu_suspend/cpu_resume owns registers, CP15/MMU/idmap/VFP/GIC; validate its actual CPU0 stash/physical buffer, resume vector and PCM storage; retain/restore CA7_CACHE_CONFIG bit4 and MCU_BIU with readback | A7 integrated coherency, existing stock-backed Linux hotplug; no A9 SCU transplant or arbitrary power writes |
| Runtime PCM/restore | Keep independently stock-matched480-word DPIDLE program, retained INFRA/DDRPHY; verify arm operands and restore normal28-word program after entry/abort | No invented instructions or system-suspend PCM substitution; real reset return and fully successful restore counted separately |
| Workload guard | IRQ-safe aggregate of existing successful non-Idle leases protects deep entry | Expiry/renewal/failure/release ownership tested; no mutex taken inside idle; original QoS/thermal/parking policy preserved |

C1/C2 registration and fallback, coordinator30-second quiet policy, one-at-a-time CPU3→2→1 parking and1→2→3 owned restore, hysteresis/pressure hold, schedutil, thermal authority and598/747.5/1040/1196/1300MHz remain intact. The C3 entry frequency rule is exactly598000 or747500kHz, including rejection of unknown0; it does not reduce active performance. No root/data reset, partition/memory layout change, /dev/mem, userspace MMIO, firmware invention or clock-bit masking.

## Exact source ledger and confidence

The retained Y2 PCM, CIRQ/context/SPM disassembly and prior source ledger are reused rather than repeatedly recapturing unchanged ROM/recovery provenance. [CPU Final source ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-SOURCES.md) names retained function/offset and independent binary matching. Additional narrow downloads and SHA256 receipts are in `out/cpu-idle-completion-research/manifest.json`.
  - [Google MT6582 d53dd75c BSP](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/): `mt_idle.c` full clock masks/minimum26000ticks, `mt_spm_sleep.c` runtime DPIDLE480 words (distinct from SODI/system PCM), `mt_dormant.c` and `cpu_dormant.S` CA7/BIU/L2 context, `mt_cirq.c` exact bank map and clone/replay. Direct exact-SoC evidence, independently retained-Y2 matched.
  - [Google MT6582 3be93a68 BSP](https://android.googlesource.com/kernel/mediatek/+/3be93a68c209393cfe24a842e2d5896a17ea37dc/arch/arm/mach-mt6582/): independent version cross-check; no adjacent-SoC assumptions imported.
  - [MT6582 clock manager](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_clkmgr.c): named PERI/INFRA/DISP gates and `cg_bootup_pdn`0xb0e0/0x2fef7fd. The bring-up shutdown routine is evidence that these are clock gates used while the CPU executes; applying it to unconsumed Linux idle/test clocks is an explicit inference, not evidence of arbitrary L2 power control. CA7 SRAM-retention configuration is separate and unchanged.
  - [MT6582 USB PHY](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/usb20/mt6582/usb20_phy.c): `usb_enable_clock` owns MT_CG_PERI_USB0 through balanced clock-manager operations; physical supported-role receipt corroborates the missing Linux owner.
  - [MT6582 display register/engine sources](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/dispsys/mt6582/): `ddp_cmdq.c`, `ddp_cmdq_debug.c`, `ddp_reg.h`, `ddp_bls.c`, `dpi_reg.h`, WDMA/RSZ/TDSHP sources. WROT ROT_EN+0x7c is explicitly named by debug code; reset status+0x14 alone is insufficient. RDMA idle monitor+0x408 mask0x7ff00=0x100 is used before clock disable. CMDQ has seven thread enables; DPI EN/status offsets0/0x40, LARB GREQ0x450, BLS bits0/16. These are exact MT6582 operands; unsupported activity always retains clocks.
  - [BQ/ubports MT6582 NAND](https://github.com/ubports/kernel_krillin/blob/874057f3c28735d606385361fb9a4cd4545ceba6/mediatek/platform/mt6582/kernel/drivers/nand/mtk_nand.c): `nand_enable_clock`/`nand_disable_clock` owns both NFI and NLI; MT6582-path `mt6575_nand.h` defines MASTERSTA+0x210, CON+8, STA+0x60, FIFO+0x64. Legacy filename does not change actual SoC relevance.
  - [MT6582 PWM](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/pwm/mt6582/mt_pwm_hal.c) and [SPI](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/spi/mt6582/spi.c): exact activity operands. SPI's real CMD/STATUS1 offsets0x18/0x20; any unknown nonzero state is busy.
  - [Cortex-A7 TRM](https://documentation-service.arm.com/static/5f042da1dbdee951c1cd8c11): dormant/reset/coherency/cache constraints, with Linux's own A7 implementation supplying the port. [Linux v6.18 ARM suspend](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/arch/arm/kernel/suspend.c?h=v6.18), `sleep.S` and `proc-v7.S` are the locked local code; generic save block is36+12bytes, actual stash/physical-idmap and reset-return ownership are used directly.

## Automated next physical qualification

Run the single host harness after owner flash. Default displays a plan without contacting hardware. `--run` verifies exact manifest and running Reborn identity, then launches one durable private device job. A mutation is launched exactly once even if SSH disappears; only read-only observations retry over independently pinned Wi-Fi. Sparse observers preserve idle windows. If both transports are intentionally off, the device job continues and restores supported USB role and radios in finally. An RGU reset is a failed trial, captured from retained stage, not a successful same-boot wake; there is no automatic reflash/retry.

The harness covers GPT6/GPT4/PPI29/highres/NO_HZ receipts and per-core1ms wake, three physical hotplug cycles, all five bounded OPPs, screen-on/off metrics, natural quiet/ownership parking, C2 useful residency/restore, fsynced uncached SHA256 on eMMC and whichever SD is actually inserted, all C3 prerequisites, too-close deadlines, one checked C3 timer-wake followed by19 only after success, context/timer/CIRQ/GPT wake checks, screen/workload wake, real silent playback, USB bidirectional1MiB SHA256 transfers with independent Wi-Fi observation, filesystem/kernel IRQ faults and thermal state. It restores owner policies; `--enable-qualified-runtime` leaves C3 enabled through ordinary cpuidle policy only after20 successful bounded trials and an additional runtime-residency window.

It does not automatically remove SD or create a radio peer, and does not claim physical external input-edge latch qualification from a synthetic key injection. All such unobserved scenarios stay explicit. No electrical battery improvement is claimed. Full-system suspend is excluded from this CPU-only runner because its historical resume defect is a separate owner scope and hardware gate.

## Software qualification and package

Final clean source pair 3dfb5f5cc731ec5dac88a778290819c23dba6067 / b71b468860233faa0a42b8448ec5777fa952b8e3 produces kernel `6.18.0-y2linux-cpu-idle-01`, root `2025.02.18-platform-v1.18`, release `1.0.0-cpu-idle-completion-candidate.1` and build `Y2LINUX-CPU-IDLE-COMPLETION-01`. Kernel/config/DT/module/ rescue/ARM ABI validation, fresh Buildroot/Reborn ARM, FFmpeg verification, QEMU, installed ARM tools, ELF/dependencies, complete regression suite and preserving-package validation pass. No baseline userspace binaries were reused.

Production runner: 364 cases:359 pass in the locked host and five explicit native prerequisite skips. All five skipped assertions pass in the packaging-host follow-up (25 cases, no skips), yielding364 covered production cases. Reborn workspace 238 pass,0 ignored, clippy/fmt pass; source owner/fault suite98 pass. Installed ARM imports31 platform modules, SQLite3.53.4/OpenSSL3.5.8, null-device audio constraints12 combinations, real 1000-track ARM library benchmark and eight Reborn control/QEMU checks pass. ELF verification covers383 ARM files and1403 dependency edges without build RPATHs. QEMU and null-device checks are software evidence, not Y2 hardware tests.

Actual receipts/logs: `out/cpu-idle-completion-validation/` and the sealed package's `validation/`. Pinned source hashes/dependency inventory, notices and exact committed source archives are included. Buildroot legal-info succeeds; its existing local-package/external-toolchain notice omissions are retained explicitly in the receipt, with paired source/licenses and pinned inventory. Owner-local distribution scope is unchanged; no public distribution is asserted.

Final preserving package: `out/y2linux-cpu-idle-completion-candidate/`. Only BOOTIMG and ANDROID/Y2ROOT are supplied as new flash payloads; Y2DATA is preserved in place. The exact Hardware02 fallback is retained. Full ext4/root content, module/identity/dependency, scatter/preservation/composition/privacy and complete checksum inventory checks pass. No flash or push occurred.````

| Payload | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 7208960 | 3303cad8d0b73a78653f58d80ede2d1583ed7ef89a48f781f8aaf1669240092d |
| Y2ROOT.img | 536870912 | 816b9a271633c96fd937fa71ef1ac1f93e74436fbd8e97c9d0491470cc4babbb |

C3 physical category: SOFTWARE_READY_NEEDS_NEW_FLASH. Current installed DORMANT entry/success/residency remain0; no actual CPU0 power-off/resume has been observed. Source-ready software does not promote the candidate's physical acceptance. The baseline C1/C2 results stay attached to their real identities.

Fresh ARM linking caught a64-bit diagnostic division using an unavailable userspace runtime symbol; the kernel variant now uses div_u64 while native fixtures retain identical13MHz arithmetic. This was corrected before a complete build or candidate was packaged. Baseline receipt18 adds three bidirectional 1MiB USB SHA256 passes with an independently reachable Wi-Fi observer.

Final source fault review adds fail-closed partial-DPI handoff (no unclocked partner register read), counted/quarantined CIRQ enable-readback failure, and all-five-OPP qualification again after C3 before restoring schedutil for the actual playback test. Native dropped-clone/enable writes and partial coupled clock fixtures pass. These refinements precede final packaging/qualification.

The final hardware harness distinguishes stable dormant_wake_result/stage from subsequent admission refusals: a spent positive budget may legitimately refuse more idle attempts without erasing the observed wake. Native tests explicitly cover successful reset return followed by budget refusal, and restoration faults. DT validation now admits only exact USB0 ID44 on the USB consumer, preserving existing profile ceilings for every other consumer and requiring the four exact MT6582 mutex/shared-clock specifiers. Invalid IDs/providers remain rejected.

The bounded dormant journal appends restoration stages for PCM, CPU/cache/GIC, CIRQ and clocks without changing existing stage IDs, retained record layout or memory ownership. Normal unlimited idle does not pay qualification journal/ watchdog overhead. The host harness checks the physically demonstrated descending MT6582 secondary power bits0x800/0x400/0x200; the kernel mapping was already correct.

## Completion handoff record
  - Installed baseline. Kernel6.18.0-y2linux-baseline-01; Linux

131ee4621cd583c955182f994adac5a594fb823f; Reborn 7f9df397ab3809d52e2f1073ca93a305246e0c3a; boot cee326c1-a5b0-447a-8eb0-dc3f39f7e2c2. Rootv1.17/releasebaseline.1 match the sealed baseline package. Both Git status/HEAD/log80 snapshots precede changes.
  - C1. Stock WFI and existing Linux cpuidle fallback preserved. All four

cores registered/enabled;3902 new entries and48.146279 aggregate core-seconds, rejections0. Per-core results and wake percentiles are in the physical record.
  - C2. Initial live mask0x100800: APDMA bit11 and BTIF bit20 owned by active

connectivity, legitimate with Wi-Fi running. Initial MMC references are real I/O and drain normally; no new MMC ownership leak exists in this baseline. Radio runtime-off removes these blockers; natural pressure-hold expiry gives CPU0 eligibility. Existing Fix03 exact0/0x0f bus DCM save/0x8f/restore remains. No blocker mask was removed.7182 new entries/50.763741s, restore failures0; enabled/disabled/re-enabled comparison proves meaningful residency.
  - Core parking. Existing sustained-load/high-frequency/30-second quiet

policy, pressure hysteresis, leases/screen/input demand and owner mask retained. Natural CPU3→2→1 parking reaches CPU0/owner0xe; owner-only1→2→3 restoration and actual PlaybackNormal demand restore all cores. Three hotplug cycles verify CPU1/2/3 physical bits0x800/0x400/0x200 in both copies.
  - C3 software. Every preflight predicate is exposed: system_running,

boot_policy, spm, local_events, cirq, topology, frequency, screen_off, workload, runtime_budget, qualification_backstop, linux_context, timer_context, usb_restore, broken, clocks, display_clocks and bus; secondary_power and domains are decoded separately. The actual entry also checks CPU0 identity, future deadline/GPT4 arm, serialization, resume-vector readback, runtime PCM and finisher's actual Linux context buffer. Baseline failures were topology/frequency/domains/clocks; display/shared/audio/USB0 and inherited PERI/INFRA owners are corrected by their real lifecycles. Powered DISP is permitted only by exact stock clock quiescence; other domains and physical secondary-off masks remain strict. Active unknown devices remain blockers. Runtime480-word DPIDLE PCM is retained, not SODI or597-word system suspend; normal28-word PCM restored/read back. Exact CIRQ155 interrupt mapping/clone/enable/replay/disable is verified. Linux GPT4 owns the13MHz one-shot deadline,≥26000ticks, checked at admission and finisher. OPP is exactly598000/747500; active1300000 remains available. cpu_suspend/cpu_resume supplies MMU/CP15/general/VFP/GIC context; A7 coherency/L2-retention/MCU_BIU/local timer state are saved and checked. Restore faults quarantine C3; bounded qualification uses retained stages and10-second RGU backstop, with no unlimited-runtime journal overhead.
  - C3 physical state: SOFTWARE_READY_NEEDS_NEW_FLASH. No hardware limit

is inferred. No C3 entry is claimed from a software test. Default remains off; the one-shot/20-cycle harness uses normal experimental runtime controls.
  - Timer regression. GPT6/GPT4/PPI29/13MHz/highres/NO_HZ baseline evidence,

pinned per-core1ms wake and MONOTONIC/RAW continuity pass. Native deadline boundaries,64-bit conversion, timer compare/control/CNTFRQ faults, aborted context and fallback pass. Actual post-dormant continuity awaits owner flash.
  - DVFS regression. All five OPPs598/747.5/1040/1196/1300MHz physically

reached;1.15/1.15/1.15/1.20/1.25V readbacks pass, faultN/PWRAPerrors0. Schedutil/QoS/thermal/voltage order/ceiling preserved. Harness repeats all five before and after C3.
  - Storage regression. eMMC plus inserted SD each pass eight fsynced,

uncached checksums per radio-off run; request/DMA/FIFO/controller drain, retained-context/runtime resume/gate and media access pass; mismatch/error0, mounted ext4 errors0. Candidate retains reviewed high-speed MMC transport. SD-absent is unobserved; no live media reset/removal was synthesized.
  - Tests. Fresh qualification numbers and artifact receipts above; CPU,

timer, idle, clock, coordinator, hotplug, suspend-related, MMC/USB, thermal/DVFS and existing tests pass. All native prerequisites completed. Candidate package/root/preservation/fallback checks pass. The new host harness was also run against the actual old baseline: receipt25 refuses all mismatched identities before mutation, without starting C3 or radios.
  - Research. Exact pinned MT6582 Google/independent BSPs, retained Y2

source/disassembly/PCM, Linuxv6.18 and Cortex-A7 TRM. Full primary URLs, function/register relevance, confidence and explicit inference are in the source ledger above and CPU-FINAL-SOURCES. Narrow downloads retain SHA256.
  - Files changed. Exact lists follow. Preexisting owner edits in six

documentation files remain unstaged; they are not included as this pass's modifications or in the built source archive.
  - Local commits. Linux implementation/fault/harness commits below;

Rebornb71b468 adds owned DRM screen sleep/wake. A following documentation receipt commit records the final seal; it changes no compiled source. Git identity and authenticated GitHub account remain unchanged; no push.
  - Candidate path.`/home/luca/Dokumente/Code/Y2Linux/out/y2linux-cpu-idle-completion-candidate/`.
  - BOOTIMG SHA256.`3303cad8d0b73a78653f58d80ede2d1583ed7ef89a48f781f8aaf1669240092d`.
  - Y2ROOT SHA256.`816b9a271633c96fd937fa71ef1ac1f93e74436fbd8e97c9d0491470cc4babbb`.
  - Exact next owner action. Install BOOTIMG+ANDROID through the included

preserving scatter/Download Only, retaining Y2DATA and all protected partitions. Boot with existing USB SSH and stopped playback, then run the single command below. It records one first entry and stops C3 on failure; only successful repeated qualification enables ordinary runtime C3.
`cd /home/luca/Dokumente/Code/Y2Linux python3 tools/development/qualify-cpu-idle-completion.py \ --run --enable-qualified-runtime \ --package out/y2linux-cpu-idle-completion-candidate \ --ssh-config out/cpu-final-fix02-physical-qualification/20260929T152328Z/ssh-config \ --host y2 --wifi-host y2-owner-wifi`

The package's CPU-IDLE-OWNER-HANDOFF.md contains the same owner action and fallback. Electrical battery life, SD absence and physical external-peer/input edge behavior are not claimed. Full-system suspend's separate failure and unrelated release acceptance gates remain open.

### Changed Linux files`docs/planning/platform-v1-roadmap.md docs/planning/roadmap-gap-audit.md docs/release/Y2-COMMUNITY-BETA-FEATURE-AUDIT.md docs/release/Y2-COMMUNITY-BETA-FEATURES.json docs/release/Y2-COMMUNITY-BETA-PLAN.md docs/validation/Y2-CPU-IDLE-COMPLETION-PHYSICAL.md docs/validation/Y2-CPU-IDLE-COMPLETION.md kernel/config/production.config kernel/dts/innioasis-y2.dts kernel/patches/0011-mt6582-mutex.patch kernel/patches/0058-y2-musb-sleep-lifecycle.patch kernel/patches/manifest.json kernel/platform/cirq.c kernel/platform/cirq.h kernel/platform/clocks.c kernel/platform/clocks.h kernel/platform/idle-clock-policy.h kernel/platform/idle-completion-policy.h kernel/platform/idle.c kernel/platform/local-timer.c kernel/platform/local-timer.h kernel/platform/mm-clocks.c kernel/platform/pm-journal.c kernel/platform/pm-journal.h kernel/platform/spm-idle-policy.h kernel/platform/spm.c kernel/platform/spm.h kernel/platform/system-idle.h kernel/platform/usb-pm.h kernel/platform/usb.c kernel/platform/workload.c tests/test_cpu_final.py tests/test_cpu_fix02.py tests/test_cpu_fix03.py tests/test_cpu_idle_completion.py tests/test_cpu_idle_harness.py tests/test_workload_qos.py tools/development/cpu_idle_completion_device.py tools/development/qualify-cpu-idle-completion.py tools/platform/y2_platform/diagnostic_fields.py tools/platform/y2_platform/observe.py tools/production/release.json tools/production/tests.sh tools/validation/dev_dtb.py`

### Changed Reborn files`app/reborn/src/main.rs crates/reborn-graphics/native/graphics.c crates/reborn-graphics/src/native.rs`

### Built source commits`be38f81 Complete guarded CPU idle clock ownership, context checks and qualification harness 49249dc Use kernel ARM division and keep failed idle qualification disabled 8ba3a91 Guard partial display handoff and failed CIRQ enable before dormant qualification 60f05b6 Restore the RGU qualification control using its decoded armed value c82d4e9 Preserve actual dormant wake results and journal checked restore stages 3dfb5f5 Check exact descending MT6582 CPU power bits in physical harness b71b468 Release owned DRM scanout during screen sleep and restore it on wake`

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
