---
title: "Y2Linux + Reborn Community Beta 1 — feature-completion plan - Innioasis Updater"
description: "Y2Linux + Reborn Community Beta 1 — feature-completion plan Baseline01 physical gate interrupted / USB diagnosis pending — 2026-10-04 Exact installed Baseline01 Linux 98d"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-community-beta-plan.html"
---

# Y2Linux + Reborn Community Beta 1 — feature-completion plan - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux + Reborn Community Beta 1 — feature-completion plan

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux + Reborn Community Beta 1 — feature-completion plan

## Baseline01 physical gate interrupted / USB diagnosis pending — 2026-10-04

Exact installed Baseline01 Linux `98daf3f` / Reborn `9cd12bae`, kernel baseline-01 and root v1.24 passes original machine/owner smoke on boot `ef2c8f2f…`, taint 0. All-four-core C1, 18 hotplug transitions, five OPP/voltage readbacks and natural parking/C2 pass; C2 has 4,857 entries and 85.4572% residency in 60.05534 seconds, zero restore faults. Eight scratch hash rounds each on DATA/SD after C2 pass. The owner restarted after an overlong deliberate USB-off C3 topology wait; C3 has no recorded armed/entered cycle and remains unqualified, not a proven C3 crash. Recovered boot `9d4d0245…` logs a DRM WARNING; automatic C3 correctly reports Skipped. Earlier post-flash USB disconnects remain independently open. Host ECM static-IP/autoconnect matching is corrected and saved; the host harness now keeps USB attached during parking and bounds its offline window to 180 s. Thirty affected host tests pass; installed firmware/images are unchanged. The owner prioritizes the separate wired-audio session holding the shared lock; USB diagnosis waits for its completion. No further CPU/transfer/suspend stress. Full Power and RTC wake remain separately NOT_RUN, historical Baseline02 RTC FAIL stays open, and endurance/electrical/distribution gates remain unqualified. See [the physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BASELINE-PHYSICAL.md). All 233 feature identities are retained; sealed package metadata remains its seal-time record. No main merge, push, flash or public/physical promotion.

## Independent final baseline — 2026-10-04

Current software handoff: Y2LINUX-PLATFORM-V1-BASELINE-01 — READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION. Compiled Linux `98daf3f0220f4a1580bb4893094ee9f0e02362a5` / Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304`; kernel `6.18.0-y2linux-platform-v1-baseline-01`, root `2025.02.18-platform-v1.24`. Canonical owner candidate: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-baseline-candidate`. Fresh 475 production cases / 465 passed / ten dependency skips, all ten independently passed; 324 Reborn tests, fmt/strict Clippy/fresh kernel/ARM/QEMU/package/source/privacy PASS. SOFTWARE_VALIDATED / INTEGRATED_PHYSICAL_NOT_RUN; PUBLIC_DISTRIBUTION_NOT_READY. UART01 CPU hardware is inherited; Baseline02 RTC FAIL remains unresolved. Policy-enabled C3, native S16, battery safeguards, DATA/layout and recovery stay.

See [baseline](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-BASELINE.md), [twelve sessions](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-FINAL-SESSION-RESULTS.md), [independent integration review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INDEPENDENT-VERIFICATION.md) and [one smoke-gated physical campaign](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-PHYSICAL-QUALIFICATION.md). This current section supersedes candidate/build/acceptance wording in the dated master planning and execution record below. Older NOT_CREATED/NOT_BUILT/accepted-none and in-progress text describes its observation time, never the current baseline. No main merge, push, flash or physical/public milestone promotion occurred.

## Historical feature/planning snapshots (retained)

## Current baseline and next boundary — 2026-10-03

FEATURE COMPLETION IN PROGRESS. Baseline02 is the latest sealed integrated, owner-local candidate: Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`, release `1.0.0-baseline-candidate.2`. Fresh software/package validation passes; new-image and automatic cold-boot hardware qualification are NOT_RUN. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [the current feature inventory](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md).

The preceding UART01 image proves C1/C2/C3 physically working, including natural parking, 21 guarded actual C3 reset-and-return trials and 3,624 normal-policy C3 entries at 65.2450% residency. The UART1 ownership/global SPM sleep ACK issue is resolved. C2 has 6,971 entries at 84.3473% residency and zero clock restore failures. Timers/hotplug/all five guarded OPPs and bounded storage/playback/USB regressions pass. [Authoritative hardware report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

Baseline02 adds the owner-selected automatic qualified CPU0 C3 startup policy, with static admission/readback/rollback and unchanged dynamic guards. The next CPU action is owner-preserving installation and the included exact-image SSH harness: cold-boot policy proof, C1/C2/timer/hotplug/storage/OPP regression, one guarded C3 trial plus 20 cycles, normal runtime and wake/I/O checks. Preserve Y2DATA and protected partitions; only BOOTIMG and ANDROID/Y2ROOT are payloads. No C1/C2 redesign or repeat of the solved UART blocker is planned.

## Remaining release work

The 233-feature target remains. Carry forward bounded successes and test affected paths on the integrated candidate. Full same-boot system suspend/Power+RTC wake, wider thermal/charging/endurance conditions, measured electrical battery benefit, native meaningful 24-bit/high-rate wired output, optional Bluetooth peer/codec acceptance and distribution/source/signing/first-owner release decisions remain separate gates. Runtime C3 is not full system sleep or a measured battery result.

Prior day-by-day schedules and candidate labels below are dated planning history. They do not turn closed C1/C2/C3 implementation into new work, authorize another flash or change the current feature inventory. Review remaining scope at the [standing milestone boundary](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) before activating or closing a new milestone; no GitHub issue is closed here.

## Historical plans and CPU candidate boundaries

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Y2Linux + Reborn Community Beta 1 — feature-completion plan

## CPU idle candidate02 hardware boundary — 2026-10-03

The owner-installed candidate02 is physically tested at Linuxdb0234e/Rebornb71b4688, kernelidle-02/rootv1.19, unchanged boot`f155196b-64d4-45a4-88b3-27755a1a8926`. C1 and C2 WORKING; C3 remains blocked before entry by UART1. C2 spends 50.669913s of60.048084s in SLIDLE (6772 entries,84.38%), restore failures0. Normal parking/demand restore, timers/hotplug/all five OPPs, both media integrity, screen/playback and USB/independent Wi-Fi observation pass. SPI0 releases; an actual settled CPU0/747.5MHz preflight isolates UART1 PERI0x20000 alone.

CPU idle completion remains unaccepted: no dormant call, actual context return, CIRQ/GPT4 wake or20-cycle result. Bounded exact-kernel UART observations do not prove safe gating of LSR0/nonzero-divisor UART1, nor any hardware impossibility. Keep C3 disabled and close its exact clock-owner dependency before another guarded trial. The harness now rechecks natural parking after synced storage; targeted100 locked CPU/idle/suspend/workload tests pass. No new kernel/root image or owner flash is required for this harness/evidence change. Historical02 NOT_RUN/owner-flash instructions below are superseded.

Main qualification taint0; removed diagnostic probes leave expected flag4096, recorded in the final restored same boot. Full-system suspend, electrical battery benefit, SD-absent and radio endurance stay separate/unqualified. No external issue/milestone closure, production activation, protected-partition write, flash or push. See [current physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md) and [source record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md).

## CPU idle candidate02 software boundary — 2026-10-03

Installed01 C1/C2/parking regressions pass; C3 UART1/SPI0 preflight fails with zero actual dormant entries. Follow-up02 is sealed at Linuxdb0234e/Rebornb71b4688, with100 CPU owner/fault cases,366 production cases/native prerequisites,238 Reborn cases, fresh ARM kernel/root, QEMU/dependencies and preserving-package checks passing. Candidate02 is NOT_RUN physically, C3 SOFTWARE_READY_NEEDS_NEW_FLASH; raw UART/SPI decisions and actual deep wake still require the owner flash. No full-suspend/battery-energy/unrelated release promotion, no flash/push. See [exact source/hashes/handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md).

## CPU idle candidate01 hardware result — 2026-10-03

Owner-installed Linux3dfb5f5/Rebornb71b4688 is now tested on unchanged boot `e0eb2f36-7c1f-4007-99e2-81d2eae047d4`, taint0. C1 and C2 are WORKING; C2 adds7,040 entries/49.674049s in60.047965s (82.72%), restores/media errors0. Natural parking, three hotplug cycles, all five OPPs before/after preflight, screen/workload wake, real playback and USB/independent Wi-Fi integrity pass. Overall CPU idle qualification FAILS: C3 preflight retains UART1/SPI0, PERI0x02020000, and no physical dormant call occurs. Other reported static prerequisites pass. C3 remains off; dynamic deadline/context/CIRQ wake unobserved.

Exact MT6582 source follow-up corrects SPI idle polarity/UART DMA metadata, retains unknown/live/aliased engines and adds read-only handoff operands. Candidate02 requires a fresh preserving build and owner flash; no claim that it already releases both clocks. Electrical battery benefit and full-system suspend remain unqualified. No flash/push, protected-data write, external issue closure or unrelated release promotion. See [physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md) and [source follow-up](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md).

## CPU idle software handoff — 2026-10-03

One fresh preserving CPU idle candidate is sealed and software validated at Linux3dfb5f5/Rebornb71b4688. Kernel/config/DT/modules/ABI, Buildroot/Reborn ARM, production364 cases with native prerequisites completed, Reborn238 cases, QEMU/ELF/dependencies and package validation pass. C1/C2 are physically WORKING on the verified installed baseline; C2 shows useful84% residency and a controlled enabled/disabled comparison. C3 is SOFTWARE_READY_NEEDS_NEW_FLASH, with no actual dormant entry claimed. Candidate hardware acceptance remains NOT_RUN; the single automated SSH qualification follows owner-only flash. No flash/push, Y2DATA or protected-partition write, milestone closure or unrelated release-gate promotion. Exact hashes, source ledger, changes and owner command: [completion record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md).

CPU idle update,2026-10-03: installed baseline C1 and C2 are now physically working (C2+7182 entries/+50.763741s of60.404076s, restores/storage errors0). C3 source and one coherent candidate target the owner-flash boundary; no actual dormant success is claimed. This supersedes historical C2 wording below, while full suspend and unrelated release gates remain open. See [CPU idle completion](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md) and [physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md).

## Sealed feature-completion integration — 2026-10-02

READY FOR HARDWARE DECISION RUN. The [implementation pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-IMPLEMENTATION-PASS.md) records the ten-workstream results, fresh build/tests, exact hashes and single owner handoff.233features and their release requirements remain. Native wired24/high-rate programming and full-resume closure remain unresolved; physical qualification and public distribution are separate open gates. No flash or push. Older snapshots below are historical.

## Active implementation campaign — 2026-10-02

The owner now explicitly authorizes implementation, fresh validation and one owner-local BOOTIMG/Y2ROOT integration candidate, preserving Y2DATA. The original planning-only authorization statement below describes the earlier document, not the current session. No flash/push or public release is authorized.

Use [the implementation pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-IMPLEMENTATION-PASS.md) for current results and the unchanged233-feature JSON for remaining obligations. Latest live identity is candidate4, taint0; the earlier unflashed statement is superseded by read-only observation. Ten independent lanes are being completed together. Native wired24/high-rate fetch/clock evidence, same-boot full resume, actual C2/C3, robust storage/USB and codec peer/distribution acceptance remain hard gates; working fallbacks do not waive them. Current verdict remains **FEATURE COMPLETION IN PROGRESS** pending fresh integrated validation and owner physical decisions.

Updated 2026-10-02 following the owner's explicit release-target correction. This replaces the earlier minimum-subset planning philosophy. Authority is documentation/planning only: no implementation, build, flash, physical test, push, publication or milestone activation is performed or authorized by this document. The [master audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md) and [233-feature JSON inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/release/Y2-COMMUNITY-BETA-FEATURES.json) preserve factual state, failures, fallbacks and evidence.

## What feature-complete beta means

All intended major product capabilities are present, with polished end-user operation, even if some have bounded experimental labels, bugs or named peer/card compatibility limits. Community testing should find bugs, compatibility, UX and endurance issues across the intended product, rather than discover that its main capabilities were intentionally omitted.

Required vision: high-quality wired playback and meaningful native24-bit where the AFE path supports it; native88.2/96 where supported; viable Classic SBC/XQ/AAC/aptX/HD/LDAC and ABR; intelligent CPU power management including C2 and evaluated C3; actual deep sleep and same-boot Power/RTC wake; admitted598/747.5/1040/1196/1300MHz; fastest robust eMMC/SD modes; reliable high-performance USB; useful battery/charging; polished Reborn; safe preserving update/recovery.

A feature may remain out only for a demonstrated hardware limit, legal/distribution restriction, or genuinely nonessential experiment outside the intended major product. Difficulty, missing qualification, reverse engineering, a lower-mode fallback or the seven-day deadline are not exclusion reasons. Safety remains a gate: no corruption, unsafe power behavior, unexplained repeated reboot or unworkable recovery is accepted under an “experimental” label.

## Exact current baseline and verdict

Reclassification source: Linux `e2dd583` (full hash in the audit/JSON), Reborn `b92d312cc2dc4b74f57a1a9a7b1407e34707137a`. Newest sealed candidate4 was built from Linux `dcbd7d1` / code `3920a54`; its [receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-SD-SDR104-DIAG.md%23candidate-4-receipt&anchor=candidate-4-receipt) reports304 production/platform tests and ARM/ELF/inventory/legal-info checks PASS. Candidate4 is unflashed and physically unqualified. Candidate3 remains latest reported installed/physically characterized; Fix02 remains latest broad physical qualification. No new hardware observation was made in this reclassification.

Candidate3 reported200MHz SD CRC failures across sampling/drive sweeps, with SDR104 timing capped100MHz passing2GiB at~42MB/s. Candidate4 adds stock input-pad and card-driver controls; its pending hardware result matters. Neither prior failure proves200MHz impossible after the remaining correct settings, nor the short100MHz pass proves production integrity.

Verdict: FEATURE COMPLETION IN PROGRESS. Native wider/higher-rate hardware output is not implemented; Classic optional endpoints remain disabled; C2 correction lacks closure; C3 has no entry proof; full suspend returns from SPM but fails before completed userspace resume. Existing lower paths work, but do not complete the target. Distribution and first-owner installation also remain unresolved.

## Independent planning axes

Every feature retains implementation state and evidence independently from:

| Product target | Release meaning |
| --- | --- |
| CORE_RELEASE_FEATURE | Required functional/safety/integration foundation |
| FEATURE_COMPLETE_TARGET | Intended product capability; difficult or disabled does not mean optional |
| CONDITIONAL_ON_HARDWARE | Required hardware investigation, then implementation/qualification if supported |
| ACCEPTABLE_BETA_LIMITATION | Explicit permitted limitation, with required safe alternative where applicable |
| UNSUPPORTED_HARDWARE | No supported target hardware/platform path; scope the evidence precisely |
| EXPERIMENTAL_POST_BETA | Genuinely nonessential extension outside the specified major product |

`release_required`, `hardware_conditional`, `public_distribution_state`, `current_limitation`, `next_action` and A–G completion groups are explicit in JSON. Meaningful24-bit is FEATURE_COMPLETE_TARGET with a hardware condition;88.2/96 and C3 are CONDITIONAL_ON_HARDWARE. Codec distribution approval is independent of technical viability. 91 former C/D rows move into required/conditional scope; all233 rows receive the new axes. Counts and exact changed IDs are in JSON. No maturity promotion is implied; only F233 gains SOFTWARE_VALIDATED from the new sealed receipt.

## Three engineering passes

These are coherent work batches with reviewed interfaces, not20 separate candidate releases. Source work and targeted software checks can overlap; hardware access is serialized and requires its separate owner boundary. One shared-device reality and available engineering time limit parallelism. Hardware evidence needed to implement safely cannot be postponed until after all code is written.

### Pass 1 — Platform feature completion

Goal: complete power/sleep/storage/USB/battery platform behavior, maintaining existing electrical and data safeguards.
  - Close C2 actual entry/residency/restore; evaluate C3 preflight/topology/≤747.5MHz entry, runtime PCM, CIRQ, GPT4 deadline and CPU context. Preserve full active OPP range with bin/thermal guards.
  - Localize the existing full-resume stall using Fix03 breadcrumbs; complete same-boot Power and RTC wake plus storage/USB/radio/display/audio restoration. Define platform sleep intent/status and active-playback/charging policy for Reborn.
  - Finish current SD ceiling investigation and qualify HS200/DDR52/HS52 plus SD SDR104/SDR50/DDR50/HS. Select the fastest robust supported mode per board/card; retain automatic containment and known lower fallbacks. Do not arbitrarily cap all users to50MHz.
  - Close existing loaded USB DMA failure with progress-aware guard/focused repair; verify PIO fallback, throughput, repeated integrity, reconnect and supported host sleep/wake.
  - Complete useful SOC/charging/warnings/shutdown/reserve. Investigate actual MT6323/Y2 current/coulomb/NTC support; implement only a proven calibrated measurement path. Root/data integrity and thermal safety are non-negotiable.

Exit: platform source complete for supported scope; unresolved hardware questions have exact evidence or remain explicit blockers. Existing bounded1196/1300MHz qualification is retained; mixed workload/endurance/comfort is the gap, not admission optionality. C2+parking equivalence to C3 requires measured drain/latency and an explicit owner product decision, not assumed equivalence.

### Pass 2 — Audio / Bluetooth feature completion

Goal: native high-quality output and the full viable Classic codec product.
  - Resolve exact MT6582 fetch/packing/interconnect/rate-clock evidence before adding ALSA masks. Implement meaningful24-bit via the proven S24/S32/24-in32 path; implement88.2/96 if supported. Keep decode precision, DSP precision, ALSA format, AFE fetch, I2S slots, payload and DAC precision distinct.
  - Preserve native44.1/48; integrate real sink capability negotiation/conversion, truthful source/output information and robust format/rate transitions. Wider containers are not proof of preserved bits.
  - Complete SBC XQ, AAC, aptX, aptX HD, LDAC quality/ABR integration. Existing encoders/BlueALSA/private builds are a foundation, not required new codec implementations.
  - Complete peer capabilities, mutual availability, user preferences, qualified Auto, actual negotiated reporting, bounded fallback/reconnect and CPU/load/thermal behavior. Measure Wi-Fi coexistence at admitted quality modes.
  - Resolve public distribution review independently. Do not fake approval flags or interpret a disabled endpoint as permission to bundle its binary. Retain FEATURE_COMPLETE_TARGET if lawfully public inclusion remains blocked.

Exit: supported wired modes and codec behaviors integrated with software proof; exact physical cases prepared, compatible peers available and distribution decisions recorded. Missing peer/capture equipment is an acceptance/resource blocker, not a hardware-unsupported verdict. Linkage alone does not close audible or ABR behavior.

### Pass 3 — Reborn / release polish

Goal: expose completed features as a coherent product, with understandable installation, use and recovery.
  - Integrate the deliberate Power sleep/wake flow, active-playback screen-off distinction, audio format/codec/quality/Auto controls and truthful status through the platform API. Expose existing EQ cleanly; no DSP architecture rewrite.
  - Finish current Productv2 navigation, one-detent/one-step with intentional acceleration, focus/Back/long-name/empty/error behavior, boot handoff and final shutdown frame. Any engineering-prototype route becomes pre-release work. Existing generic-Unavailable pruning is retained, not redone.
  - Keep technical diagnostics separate; provide a redacted bug bundle with clear export/retrieval, distinct from private state backup. No scattered Y2-specific access; inspect any new boundary exceptions.
  - Complete first-owner provisioning, supported identity/layout checks, personal keys and firmware delivery, protected partition exclusions, license/source/package checks and tester instructions.
  - Qualify safe preserving beta1→beta2 update and recovery. Fully automatic OTA can remain an explicit limitation if the manual preserving workflow is rehearsed; do not require an A/B architecture project.

Exit: no dead engineering routes in supported workflows; release candidate interfaces/code/package scope fixed; named exceptions are hardware/distribution/nonessential only. No publishing or flashing is authorized by this plan.

### Candidate and dependency strategy

Reuse existing candidate4 and retained hardware evidence for targeted investigation where separately authorized. Do not create one public candidate per CPU/codec/UI subsystem. A bounded diagnostic iteration is justified if needed for safe hardware proof; count and identify it, and never call it an integrated RC.

After three passes, seal one integrated RC with exact Linux/Reborn sources, kernel/root/codec/firmware identities and enabled-feature manifest. Run broad RC software/image/source/notices checks once. Then perform integrated physical qualification and endurance. A reproduced safety/core blocker may require one focused RC correction with affected regression; a mandatory new correction means the original one-week date may slip.`flowchart LR H[Exact hardware evidence and distribution review] --> P1[Pass 1: platform completion] H --> P2[Pass 2: audio and Bluetooth] P1 --> P3[Pass 3: Reborn and release integration] P2 --> P3 P3 --> RC[One integrated RC] RC --> Q[Physical qualification and endurance] Q --> R[Feature-complete beta decision] H --> R`

P1 and P2 can overlap source investigation and independent components, but audio/codec power and sleep restoration depend on the finalized platform behavior. P3 UI preparation can overlap; final integration waits for actual typed contracts. Distribution/provisioning/documentation starts Day1, not Day7.

## Aggressive one-week roadmap

Seven days is an attempt at maximum realistic completion, not an evidence-backed promise. It assumes prompt hardware/peer access and enough implementation capacity for overlapping work; one engineer plus one device cannot execute every lane simultaneously. Exact AFE hardware evidence and the unknown resume stall are the largest schedule uncertainties. Do not shorten necessary safety observations to meet the date.

| Day | Batched work and overlap | Required decision / dependency |
| --- | --- | --- |
| 1 | Freeze real target; reconcile candidate4 ceiling evidence when available; investigate C3/suspend/AFE fields/current-sense path; begin firmware/codec distribution and onboarding work; prepare Reborn integration contracts | Name exact missing registers/stock programming, capture access, compatible peers and firmware delivery. Hardware impossibility needs proof; unknown stays open |
| 2 | Pass1: localize/fix full-resume stall, C2/C3 prerequisites, storage pads/tuning, DMA/reconnect and power gaps. Parallel audio evidence and release tooling preparation | Successful same-boot diagnostic return or exact outstanding stall; storage ceiling direction; no removal of safety predicates to obtain entry |
| 3 | Pass2 wired: implement proven native24-bit and88.2/96 path, conversion/negotiation and low-bit software fixtures. Complete remaining platform interfaces | If exact DL1/interconnect/clock proof remains absent, record unresolved fields and likely delay. S16 fallback does not close this feature |
| 4 | Pass2 BT: endpoint/policy/quality/ABR integration; peer and coexistence bring-up, CPU measurement where authorized; P1 regression; P3 typed UI integration | Each codec separately records built/enabled/mutual/negotiated/audible/load/distribution status. A missing peer or legal decision remains a named gate |
| 5 | Pass3: Power/audio/codec controls, wheel/boot/shutdown, diagnostic export, install/update/recovery; finish targeted software gates and seal one integrated RC if required implementation/hardware decisions are resolved | Feature freeze, exact delivered capability manifest and supported limits. Do not seal an allegedly feature-complete RC over known mandatory omissions |
| 6 | Integrated physical qualification: mode/bit/clock/peer checks, Power/RTC wake/restoration, fast storage and USB hashes, charge/load and full tester journey; start overnight endurance | Stop on corruption, unsafe thermal/power, repeated reboot or core playback failure. Correct defects only; affected results reset |
| 7 | Finish endurance/cycles, preserving-update/recovery rehearsal, second-person instructions, source/notices/private-state checks; final release decision | Publish only same tested bytes if gates close. Otherwise issue a precise remaining-blocker schedule and delay; never silently move main features post-beta |

Preparatory targeted hardware evidence during passes must have separate authorization; this documentation task runs none. Day6–7 can accommodate an8h wired window and shorter codec/sleep windows only if most implementation and peer bring-up are already complete. Charging reserve/hold and low-power evidence can need additional elapsed time. If the feature freeze slips, the integrated/endurance window moves with it.

## Exact delay triggers and missing proof

| Required feature | Current blocker / missing proof | Decision if not closed within one week |
| --- | --- | --- |
| Meaningful native24-bit | Exact MT6582 DL1 fetch/packing/interconnect, bit capture and DAC acceptance | Delay unconditional feature-complete release while unknown. Exclude only after demonstrated hardware limit, recorded honestly |
| 88.2/96 | Exact rate/clock programming and measured native clocks/sample count | Same hardware-proof decision; decoded high-rate files are not completion |
| C2/C3 | C2 post-fix entry; C3 topology/domains/clocks/CIRQ/GPT4/context/actual return | Close C2; C3 remains conditional pending real evidence or explicit measured equivalent-product tradeoff. Time shortage alone cannot defer it |
| Full deep sleep | Post-resume console/platform/thaw/notifier stall; no complete Power/RTC same-boot product return | Delay beta. Screen-off/Power Off are fallbacks, not full sleep |
| Classic codecs/ABR | Endpoints off, no optional peer/audible/CPU/coexistence proof, unresolved public rights | Delay technical completion; legal-only omission may be separately documented/accepted, with target retained |
| Storage ceiling | Candidate4 untested, no sustained high-mode write/sleep proof | Qualify highest robust lower mode after proper ceiling investigation; do not insist200MHz if genuine board/card limit is demonstrated |
| DMA USB | Fix03 source repair not physically closed; prior0/10 loaded uploads | Complete/qualify DMA or prove concrete hardware/driver limit and accepted bounded PIO product behavior; no silent performance scope cut |
| Battery measurement | Unproven sense/coulomb/NTC topology/calibration | Resolve support; useful labeled SOC/charging may satisfy approved hardware limitation, but warnings/shutdown/charging safety cannot be omitted |
| Distribution/install | Firmware permission/delivery, codec review, personal keys, current first-install workflow | Block public release until lawful deliverable and understandable recovery exist; private experimentation is not public clearance |

## Top 10 implementation tasks

These are proposed work, not changes made by this audit. “Implement” includes completing/admitting existing guarded code; do not rewrite what is already present.
  - Repair full resume completion: use Fix03 stage journal to identify the failed return-to-userspace call, then close Power/RTC same-boot wake.
  - Complete intelligent idle: close C2, evaluate/admit C3's runtime PCM/CIRQ/GPT4/context path without weakening predicates; retain full guarded OPP range.
  - Stabilize fastest storage modes: finish candidate4 pad/card-driver/tuning work and robust production ceiling selection, with fallbacks and integrity.
  - Close USB/power gaps: resolve residual DMA/reconnect issues, charging/shutdown state restoration, safe low-voltage reserve and truthful conditional measurements.
  - Implement native meaningful24-bit output: exact proven AFE fetch/interconnect/ALSA/I2S contract, low-bit preservation and sink reporting.
  - Implement native88.2/96 where supported: exact clock/rate programming and stable format/rate transitions.
  - Complete Classic codec product paths: SBC XQ/AAC/aptX/HD/LDAC endpoints, quality/ABR, peer intersection, preference/Auto and actual reporting.
  - Integrate Reborn product behavior: deliberate sleep/playback policy, codec/audio/EQ controls, wheel/boot/shutdown/empty states and clean typed boundary.
  - Finish tester operations: redacted diagnostics, transfer help, first-owner keys/data/firmware, preserving update and recovery workflow.
  - Complete release composition: rights decisions, exact source/notices, capability manifest, protected exclusions, credential/private-state rejection and reproducible packaging.

## Top 10 physical qualification tasks

No test below is run or authorized by this documentation update. Preserve existing bounded passes and repeat affected/integrated paths, not unchanged ROM provenance.
  - Power and RTC full sleep/wake: staged gates then actual same-boot return, wake reason, every restored subsystem, no watchdog reset; at least10 mixed cycles and longer sleep residence. Numeric drain claims require measurement.
  - C2/C3 and admitted CPU OPPs: real entries/residency, deadline/IRQ/context checks, park/restore, mixed workload and charging comfort at1196/1300 under existing guards; no forced overheating.
  - Native audio precision/rates: low-bit fixtures and I2S capture, native44.1/48/88.2/96 where admitted, format/rate switching, channel/sign/packing/pop and audible fidelity.
  - Every viable Classic codec: actual peer negotiation and audible output, SBC XQ and LDAC modes, user/Auto/fallback/reconnect; ABR adaptation observed, not inferred from linkage.
  - Coexistence and codec load: Wi-Fi off/idle/scan/transfer with each admitted codec quality, CPU/thermal/underrun data, screen-off and sleep-restoration behavior; publish named peer limits.
  - Fast storage integrity: selected eMMC/SD highest-robust modes plus fallbacks, multi-offset reads/writes/fsync/hashes, representative cards/filesystems, hotplug/replacement, runtime PM/sleep and boots; zero data corruption.
  - USB integrity/performance/recovery: DMA then PIO fallback,10×1MiB each direction before a mixed≥256MiB corpus,10 cable sessions, supported host sleep/wake; hashes and sustained throughput recorded, no terminal fault.
  - Battery/charging/shutdown: ordinary PC/wall sources, load/idle/hold/recharge, honest SOC, warning/reserve, app/DB persistence, actual off and clean next boot; measured current/temp only when real.
  - Polished full tester journey: current wheel/button/Power semantics, every normal route, boot/shutdown video, realistic1k–10k library/formats, diagnostic retrieval, initial install and preserving beta2/recovery rehearsal.
  - Integrated endurance:8h mixed wired/high-resolution playlist,at least20min audible operation per admitted codec family,30min per admitted LDAC quality mode and a2h highest-load/ABR segment (overlap compatible segments),≥2h actual sleep/residence/wake campaign; combine bounded scans/transfers where safe. Extend beyond the week for unexplained growth/dropout/heat or inadequate codec coverage; collectors alone are not tests.

Retain exact images/source/boot IDs, negotiated modes, before/after counters, audible observations and bounded resource trends. A failed codec/mode cannot be marked qualified because another passed. Limited compatibility and community endurance discovery are acceptable only after the minimum safe functioning product is shown. Physical regression of an unchanged foundation can ride on integrated tests; no isolated233-test hardware campaign is required.

## Release/distribution and permitted limitations

The pinned [codec ledger](https://github.com/schulzcode/y2linux/blob/HEAD/tools/production/codec-sources.json) records unresolved FDK rights review, freeaptx source/product review and LDAC NOTICE/certification review. This is evidence of unestablished public approval, not a new definitive legal judgment. Track AAC/aptX/HD/LDAC as FEATURE_COMPLETE_TARGET plus DISTRIBUTION_BLOCKED_OR_REVIEW_REQUIRED. Endpoint disablement does not remove bundled binaries. Firmware likewise needs established permission or a tested lawful owner-local path; calibration stays device-local. Do not remove technical targets simply to make legal packaging easier.

Manual preserving update is acceptable after a real rehearsal and clear recovery. Estimated SOC is acceptable if useful and visibly honest while conditional measurement questions are resolved. Named peer/card/revision limits and lower fallbacks remain. Fully automatic BOOTIMG/A-B OTA, extra Favorites/search/playlist screens, NCM if ECM suffices, network/video/FM product expansion and advanced DAC features outside the proven path are genuinely nonessential to this defined release.

Do not create fake work for LE Audio without ISO support, Adaptive/Lossless without a supported implementation path, SD HS400, unsupported host VBUS power or imagined DAC functions. Lack of proof for native24/96, C3, battery current or host wiring is conditional, not proof of absence.

## Required beta documentation and final decision

Prepare supported-device/host/card/peer matrix; actual feature manifest and known bugs; first install/backup/personalization; controls and distinct sleep/screen-off/off behavior; source-versus-output precision and codec/quality/Auto; transfer; battery/charging; preserving updates/recovery; diagnostic export/privacy; exact hashes/source/notices and any hardware/distribution exclusions. Begin drafts during implementation; finalize against actual tested behavior. This planning task does not write those end-user manuals.

At release, answer separately: are major features implemented, are hardware conditions resolved, are safety/physical gates passed, is composition publicly deliverable, and is ordinary use polished? If any required major capability remains simply unfinished, verdict is FEATURE COMPLETION IN PROGRESS and beta moves. READY FOR INTEGRATED RC requires implementation closure and explicit hardware/distribution decisions; READY FOR FEATURE-COMPLETE BETA additionally requires integrated physical/endurance/recovery acceptance.

## Release-completion groups — every open item

These replace the earlier A–E meaning and may overlap. Every one of233 rows carries an explicit assignment in the [master matrix](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md%233-complete-feature-matrix&anchor=3-complete-feature-matrix) and JSON `release_completion_index`; the full ID index is at the end of the audit. Existing mature foundations are marked for carry-forward regression, not falsely reopened as unimplemented.

| Group | Meaning | Principal work |
| --- | --- | --- |
| A | MUST IMPLEMENT BEFORE FEATURE-COMPLETE BETA | Resume/product sleep, conditional nativeHD, codec enablement/integration, EQ/product polish, current gaps in provisioning/export |
| B | MUST PHYSICALLY QUALIFY BEFORE FEATURE-COMPLETE BETA | Supported complete product, including high modes/codecs/sleep; retained bounded passes carried forward |
| C | REQUIRED IF HARDWARE SUPPORTS IT | Native24-bit/rates, C3, SDR104 ceiling, real battery measurements and host board path; exact questions/proof in audit/JSON |
| D | RELEASE / DISTRIBUTION BLOCKER | Firmware/codecs, source/notices, keys, compatibility, installation, safe update/recovery and exact public package |
| E | ACCEPTABLE BETA LIMITATION | Manual update, truthful bounded measurement/compatibility/logging limits; never a catch-all for unfinished major features |
| F | GENUINELY POST-BETA / EXPERIMENTAL | Nonessential extras and engineering interfaces outside specified product vision |
| G | UNSUPPORTED / DO NOT PURSUE | Unsupported current controller/codec paths; SD HS400 is explicitly invalid in the F050 subfeature record |

Release verdict: FEATURE COMPLETION IN PROGRESS. This is the intended full-product plan, with a seven-day attempt and explicit delay criteria. Safe fallback behavior is retained throughout; it does not erase feature obligations.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
