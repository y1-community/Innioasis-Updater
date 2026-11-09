---
title: "Platform implementation pass — 2026-10-02 - Innioasis Updater"
description: "Platform implementation pass — 2026-10-02 <!-- knowledge-base-scope: historical-implementation-receipt; baseline02-sync 2026-10-03 -- Dated implementation receipt. The ca"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-implementation-platform.html"
---

# Platform implementation pass — 2026-10-02 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform implementation pass — 2026-10-02

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform implementation pass — 2026-10-02

Dated implementation receipt. The campaign identities, test counts and pending actions below belong to the recorded source cut. The newest sealed integrated candidate is [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md). [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) now proves bounded C1/C2/C3. Baseline02 new-image/automatic cold boot and unrelated release gates remain open.

Source baseline `9ac2c0b7018ce707ec15f8845daf58ce38ec18a0`; retained Fix02 qualification and Fix03 instrumentation are the starting authority. The current read-only observation (`out/feature-completion/device-readonly.txt`) identifies installed candidate4 `dcbd7d1` / Reborn `b92d312`, boot `159f7c81-ab89-4440-bc89-df827dd8bc34`, taint 0. This supersedes the planning snapshot's latest-installed candidate3; it is not a load/resume qualification. No device writes, flash, unsafe clocks, voltage guesses or protected images.

## 1. Full suspend / same-boot product restoration

Starting state: Fix02 entered SPM, returned through the reset vector and completed the device callback ring, then hit the owner-armed 30-second backstop before `pm_suspend` exit. Fix03 already brackets `dpm_resume_end`, console resume, platform end, thaw, filesystem thaw, post-suspend notifiers and console restore. Its prepared physical run remains unexecuted. Current4 has no valid current/previous PM record or callback ring; it cannot identify the stalled call.

Source findings:`cpu_suspend` has Linux architectural context, CPU/cluster PM entry/exit, exact BIU restore, normal PCM restore, CIRQ replay and syscore timer restoration. IRQ/noirq/device/complete stages retain their existing breadcrumbs. There is no new evidence justifying a replacement suspend architecture or a speculative console/timer/GIC fix. Charger refusal, CONSYS isolated retry, USB stale-status guards, SRAM layout and abort unwind are unchanged.

Implemented:
  - `tools/platform/y2_platform/sleep.py`, `suspend_record.py`, and CLI/observation

integration expose `org.y2linux.sleep/v1` through `y2-platform sleep request|status`and`power.sleep`. States are idle, requested, refused, sleeping, restoring, restored and restore_failed. The existing owner helper's receipt gains this product object without importing SPM into Reborn.
  - Product requests return a durable, explicit `physical_qualification_required`

refusal while full resume remains unqualified. The existing explicit `--owner-qualify` helper remains the only entry path. No editable boolean can silently authorize ordinary full suspend.
  - Restoration success now requires a valid kernel `EXIT` with error 0, the same

request/current boot ID and a responding Reborn control socket. An app probe alone no longer declares resume complete. Reboot during an incomplete attempt reports restore_failed; a failed device prepare is a refusal.
  - Wake attribution uses deltas of the actual serviced `mt6397-rtc` and

`mtk-pmic-keys` child IRQs, on the same boot after a successful kernel exit. Shared SPM EINT bit 5 alone stays unknown; simultaneous sources say multiple. `sleeping` is durable pre-entry intent, not a claim of measured SPM residency.
  - Current4 exposed undefined cold SRAM as fictitious ring cycle/last/backstop

values. `pm-journal.c` now emits zero metadata for an absent ring, and accepts only the exact `0x59325253` resume-vector stamp. No retained memory layout or journaling architecture change.

Tests: nine product-state tests cover typed refusal, lock collision, complete same-boot success, reset, absent/failed kernel exit, Reborn failure, prepare refusal, IRQ attribution, malformed old receipts and symlink rejection. Existing Fix01/02/03 and helper regressions pass (63 tests). Journal regression uses the exact meaningless words observed on candidate4. A new kernel object build is recorded below.

Remaining: actual post-SPM stalled-call evidence and correction, Power/RTC same-boot return and complete storage/USB/radio/DRM/GPU/AFE/DAC/Reborn physical restoration. The existing detailed Fix03 journal is the necessary instrumentation; no new blind-interval recorder was added. **PARTIAL / hardware proof blocks full resume closure.** No separate licensing issue.

## 2. C2 SLIDLE and conditional C3 DORMANT

Starting/source state: Fix03 accepts the exact observed TOPCKGEN+4 baseline 0 or 0x0f, writes verified 0x8f during idle, and restores the exact inherited value. The real busy-clock mask, one-CPU topology and CCF ownership remain. GPT6/GPT4/PPI29, CNTFRQ13MHz, highres/NO_HZ, parking, OPP/QoS guards and WFI remain intact. Runtime C3 retains its exact MT6582 PCM, CIRQ, physical-secondary power check, <=747.5MHz gate, media/radio domains, CPU/cache context and future GPT4 deadline handoff.

Current4 observation: online CPU0, local events and CIRQ ready, but C3 preflight reported1300MHz, domain blockers0xa and live clocks; APDMA and BTIF remain legitimate C2 blockers while radios are active. Neither counter is proof of entry. This installed image reports the global eligibility option `deep_idle_enabled=1`, while C3 retains `CPUIDLE_FLAG_OFF`: its cpuidle state is still disabled by default. The option readback alone does not enable C3.

Implementation: no predicate weakening, forced parking/frequency, guessed register write or rewrite. Tests preserve both accepted bus baselines, exact restore, busy-clock refusal, runtime PCM/CIRQ/deadline and fallback paths.

Remaining: naturally sustained radios-off C2 entry/residency/exact restore; C3 physical prerequisites and actual reset-return including timer/context. Use the same integrated harness after owner flash; `y2.cpuidle=off`, `y2.deep_idle=off` and `y2.cpu_safe=1` remain. BLOCKED_BY_HARDWARE_PROOF. No separate licensing issue.

## 3. Fastest robust storage

Starting state: current4 contains stock input Schmitt/RDSEL/TDSEL, selectable mutual card drive types, exact32-tap dual-edge command/data tuning and diagnostics. Current4 read-only status observed HS200 and SDR104 at199999771Hz, width8/4, 1.8V, no logged errors/fallbacks in that narrow sample. This is not sustained integrity evidence; prior candidate3's200MHz CRC failures/100MHz bounded read pass remain relevant, not a hardware impossibility verdict.

Root causes fixed:
  - Widest-eye selection used the diagnostic budget of eight windows. A32-tap

map can have16 islands, so a valid wider ninth island could be missed. Search covers the full geometry while diagnostic output remains bounded.
  - Failed data tuning restored IOCON/PAD_TUNE but left a changed PATCH_BIT0 latch

clock. Failure now restores that register exactly too.
  - Linux6.18 `mmc_retune` clears `need_retune` and returns an execute-tuning

error; it does not renegotiate card timing. The existing callback lowered capabilities without correcting the still-active old `ios.timing`. Runtime failures now queue the existing claimed worker to reconcile the lower level; payload requests in the rejected timing fail before DMA while the worker acquires the host. Initialization keeps the core's normal retry. If core recovery won the race, there is no redundant reset/double fallback; a reset failure continues down the ladder. No failed write is replayed by this worker.
  - `Y2_MSDC_LAB` defaulted to1 and the separate clock-cap control remained writable

even without it. Default is now0: public `y2_lab` is absent and clock cap is read-only. Explicit internal lab builds may define1; all passive diagnostics, high modes, card intersection and safe fallback remain.

Files:`kernel/patches/0009-y2-msdc-readonly.patch` and its verified manifest hash, `kernel/platform/storage-tuning.h`, SD/storage/recovery tests and `tests/test_storage_runtime_tuning.py`.

Tests:42 targeted storage tests pass (one artifact-dependent case skipped on host); five existing hardware-ceiling tests also pass. Two new tests execute the actual runtime callback, mode reconciliation and request guard for discovery, runtime failure, recovery race, reset failure, high-mode payload rejection and successful retune. Pure tests reproduce the ninth-window defect and exact failed latch-clock restoration.

Remaining: HS200/DDR52/HS52 and SD SDR104/SDR50/DDR50/HS sustained safe-file read/write/fsync/hashes, hotplug, runtime PM, same-boot suspend and fallback. The intended ceilings remain HS200200MHz and robust SDR104200MHz if the actual board/card supports it;100MHz SDR50/lower SDR104 remain candidates, not silently selected as universal policy. PARTIAL / hardware proof required. No separate licensing issue.

## 4. USB half of USB / power

Starting/root cause: Fix02's513-per10ms guard treated legitimate endpoint + Inventra mode0 DMA packet events as a storm. The existing Fix03 progress-aware repair counts only interrupts without newly accepted DMA programming and retains an independent4096-per-jiffy hard ceiling. Current4 uses Inventra DMA and its read-only observation shows378 DMA interrupts,380 programs, no DMA/bus errors, max burst26 and max jiffy27; this is light activity only.

Source review: existing bus-abort teardown retires BUS_ABORT as well as BUSY, channel allocation/program/abort counters distinguish failures, EP1 RX ownership and RX-pending handling remain upstream/stock backed. System suspend disconnects through the gadget owner and refuses a live DMA enable; runtime resume preserves valid completions. Terminal faults retain snapshots and orderly teardown; PIO and `y2.usb_dma=off` remain. NCM is not enabled to bypass ECM.

Implementation: no new hardware/source defect was proven beyond the already implemented Fix03 repair. Existing targeted tests execute legitimate packet progress, stuck source, hard storm ceiling, accepted/failed DMA programming, bus-abort cleanup, stale/live DMA suspend refusal and100 reconnect cycles. They are included in the targeted lane run below.

Remaining: repeated up/down hashes and throughput with a Wi-Fi observer, actual disconnect/reconnect and host sleep, then PIO regression. **PARTIAL / BLOCKED_BY_HARDWARE_PROOF.** Battery/charging is handled by the main campaign.

## Source ledger and integrated qualification inputs
  - [Linux6.18 MMC host](https://github.com/torvalds/linux/blob/v6.18/drivers/mmc/core/host.c),

`mmc_retune`: runtime error does not renegotiate; `doing_retune` identifies the runtime path. Local locked `.cache/sources/linux-6.18` is the exact build base.
  - [Fix03 source ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX03-SOURCES.md): exact MT6582

bus-DCM values, USB per-packet physical arithmetic and post-resume call order.
  - [SD source/hardware ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-SD-SDR104-DIAG.md): actual32-tap

geometry, absent RXDLYSEL, stock input pads, card driver and clock divider.
  - The integrated harness should read the existing PM ring/previous ring after a

reset, invoke existing awake/staged/Fix03 checks only after matching installed identity, and compare boot IDs/child wake IRQ deltas/product state. Idle and storage diagnostics are passive; public lab mutations are absent. Sustained storage tests use verified filesystem scratch files, never unknown raw writes.

Do not mark F033/F034/F028/F030/F038/F043–F047/F127 physically qualified from these source fixes or synthetic tests. Distribution and implementation remain independent of physical evidence.

## Validation receipt and local commits

The final targeted lane run executed146 tests successfully (one existing artifact-dependent test skipped on the host). Log: `out/feature-completion/platform-targeted-tests.log`. Fresh ARM builds of `drivers/mmc/host/mtk-sd.o` and `drivers/y2/pm-journal.o` with `W=1` passed without warnings in `out/feature-completion-platform-build`; explicit lab1 and default lab0 variants also passed. Logs: `platform-object-build.log` and `platform-lab-build.log` under `out/feature-completion/`. These are targeted source checks; the root campaign owns the fresh complete integration build.

Focused local commits: `56e020c` (runtime tuning/window/restore/lab safety), `4ecba3a` (cold-SRAM evidence), `a4d0d8a` (typed sleep product/receipt). Shared CLI/status and production-suite integration are committed by the campaign owner together with the other platform APIs.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
