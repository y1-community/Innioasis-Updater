---
title: "Platform 1.0 independent final session results - Innioasis Updater"
description: "Platform 1.0 independent final session results 2026-10-04. Goals are reconstructed from retained admissions/reports/source, not claimed verbatim prompts: no orchestrator"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-platform-v1-final-session-results.html"
---

# Platform 1.0 independent final session results - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform 1.0 independent final session results

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform 1.0 independent final session results

2026-10-04. Goals are reconstructed from retained admissions/reports/source, not claimed verbatim prompts: no orchestrator directory exists. Git merge bases, full diffs, blob hashes and committed JSON receipts support this independent ledger. Original branches/worktrees are retained. Historical software counts below are owner receipts; fresh final counts are in [the baseline](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-BASELINE.md).

The package machine ledger `validation/session-ledger.json` lists every changed file, complete start/final hashes, all commits, diff/blob hashes, integration changes, tests and exact versus adapted bytes. All selected source paths survive. Outcome classifications describe source results; integrated physical qualification is NOT_RUN.

## 1. SESSION — Bluetooth

ORIGINAL GOAL: Bound idle/reconnect work and make discovery/codec observations reliable.

Y2Linux: `codex/platform-v1-bluetooth`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-bluetooth/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `5846a7a0a1336f581f075a1bba1ea6484439e760`; clean. 13 changed files / 1 commit.

Y2Reborn: `codex/platform-v1-bluetooth`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-bluetooth/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `de092094c27ad4ebba3cc0ba7003f29944de53ac`; clean. 3 changed files / 1 commit.

ACTUAL CHANGES: An event-driven bounded reconnect/intent worker replaces idle polling. Reborn waits for commands, bus activity and real deadlines. Paired, bonded, trusted, connected and services-resolved remain distinct; PCM epochs invalidate stale codec choices.

IMPORTANT FILES:

Y2Linux: `tests/native/bt-observe-json.c`, `tests/native/bt-reconnect-events.c`, `tests/test_platform_bluetooth.py`, `tools/connectivity/bt-observe.c`, `tools/connectivity/reconnect.c`, `tools/development/measure-bluetooth-idle.py`, `tools/platform/y2_platform/bluetooth.py`, `tools/platform/y2_platform/diagnostic_fields.py`

Y2Reborn: `crates/reborn-platform/src/bluetooth.rs`, `crates/reborn-platform/src/native.rs`

BUGS FIXED: Incorrect discovery JSON keys, stale owner/transport observations and unnecessary off-radio wakeups.

OPTIMIZATIONS: OPTIMIZED; HARDENED; BETTER_OBSERVABILITY; PARTIAL_REMAINS_OPEN. Off-radio thread polling and repeated snapshots are removed; reconnect budget stays bounded.

INVESTIGATED BUT LEFT UNCHANGED: Controller/CONSYS/BTIF ownership, conservative reconnect budget and BlueZ/BlueALSA transport. No invented codec activation or real-peer improvement.

SOFTWARE EVIDENCE: 12 Bluetooth host cases; native fake-bus event/restart/intent/JSON harness and Cortex-A7 QEMU; 238 historical Rust tests/fmt/Clippy/ARM. The final independent suite reruns the selected contracts.

PHYSICAL EVIDENCE: Baseline02 boot 27/taint 0 off/disconnected samples, no CONSYS/BTIF errors/IRQ increments. Changed worker was not installed; no available headset. Peer/audio/reconnect/coexistence/endurance remain unqualified.

MASTER INTEGRATION DECISION: Selected worker accepted; shared public diagnostics adapted. All useful owner source retained; no peer qualification accepted.

FINAL INTEGRATED STATE: Linux units `f463e65`; Reborn units `0fadf29`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 2. SESSION — Wi-Fi

ORIGINAL GOAL: Reduce readiness latency and duplicate policy/status work without changing fullmac ownership.

Y2Linux: `codex/platform-v1-wifi`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-wifi/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `78c3512400a3a907e93fe3d73bf2870dc5a35d14`; clean. 15 changed files / 5 commits.

Y2Reborn: `codex/platform-v1-wifi`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-wifi/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `2cdb9cce8df1b9a65a4f88f8cd39dd05f851093e`; clean. 1 changed files / 1 commit.

ACTUAL CHANGES: Boot/epoch/BSSID/address-bound readiness, bounded delayed STATUS, DNS scheduling and RSSI/inventory reuse. Separate real link loss from duplicate cleanup; fixed safe exported observations. Master combines supplicant and USB/signal wake in one select.

IMPORTANT FILES:

Y2Linux: `tests/test_diagnostic_export.py`, `tests/test_platform_contract.py`, `tests/test_platform_network_time.py`, `tests/test_radio_policy.py`, `tools/platform/y2_platform/diagnostic_fields.py`, `tools/platform/y2_platform/diagnostics.py`, `tools/platform/y2_platform/network.py`, `tools/platform/y2_platform/observe.py`, `tools/platform/y2_platform/radio_policy.py`, `tools/platform/y2_platform/service.py`

Y2Reborn: `crates/reborn-platform/src/wifi.rs`

BUGS FIXED: False disconnects from slow replies, reused stale Online/DNS evidence, duplicated disconnect accounting and repeated signal/inventory queries.

OPTIMIZATIONS: BUG_FIXED; OPTIMIZED; HARDENED; BETTER_OBSERVABILITY; PARTIAL_REMAINS_OPEN. Cache reuse is freshness-bound; no measured new-image throughput/power claim.

INVESTIGATED BUT LEFT UNCHANGED: Fullmac/supplicant/DHCP reconnect ownership and broken checksum-offload disable. FAST_PSP comparison was invalid because policy returned to CAM.

SOFTWARE EVIDENCE: 94 historical Linux affected cases/0 skips, 5 layout/6 privacy; 74 Rust platform plus fmt/Clippy/ARM. Delayed reply/epoch/route/privacy/request-count regressions are present.

PHYSICAL EVIDENCE: Baseline02 STATUS/SIGNAL_POLL 1.48–2.08 s; checksummed RX 43.941–44.922 / TX 46.376–46.942 Mb/s. TX iperf reset unresolved; changed-policy after/coexistence/AP loss/cold boot NOT_RUN.

MASTER INTEGRATION DECISION: Selected policy accepted; service wait and diagnostic/status union adapted. Independent radio responsibilities remain.

FINAL INTEGRATED STATE: Linux units `96ce4df`; Reborn units `5317b7c`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 3. SESSION — FFmpeg / metadata

ORIGINAL GOAL: Make metadata/artwork ingestion bounded, truthful and cheaper while preserving media formats.

Y2Linux: `codex/platform-v1-ffmpeg-metadata`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-ffmpeg-metadata/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `e709ecc7900690bfbbb765227092a9f3c81a99f8`; clean. 2 changed files / 2 commits.

Y2Reborn: `codex/platform-v1-ffmpeg-metadata`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-ffmpeg-metadata/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `c9ef7902e89443bfe26846dfe1f325de7d84598f`; clean. 37 changed files / 4 commits.

ACTUAL CHANGES: Demux-only inspection, source-bit-depth rules, date/genre and timing/I/O ABI fields, local custom AVIO/limits/cancellation, malformed tag/artwork fixtures and sidecar-only optimization. Extractor revision 2 is integrated into DB-owned schema 1 scanning. One bounded artwork wrapper includes checked JPEG reduction.

IMPORTANT FILES:

Y2Linux: evidence/admission documents; implementation resides in the paired repository.

Y2Reborn: `app/reborn/src/artwork.rs`, `app/reborn/src/playback.rs`, `crates/reborn-library/examples/media_bench.rs`, `crates/reborn-library/src/benchmark.rs`, `crates/reborn-library/src/lib.rs`, `crates/reborn-media/native/media.c`, `crates/reborn-media/src/lib.rs`, `crates/reborn-media/src/native.rs`, `tools/build/jpeg_fixture.c`, `tools/build/media_bench.py`, `tools/build/media_qemu.py`, `tools/build/media_sanitize.c`, `tools/build/metadata_fixtures.py`

BUGS FIXED: Unbounded/malformed metadata/artwork work, needless decoder/media opens, stale extractor reuse and duplicated parsing/scanner assumptions.

OPTIMIZATIONS: SIGNIFICANTLY_IMPROVED; HARDENED; OPTIMIZED; PARTIAL_REMAINS_OPEN. Host 10k initial scan median 7408→1084 ms is owner-subpass evidence, not integrated hardware speed.

INVESTIGATED BUT LEFT UNCHANGED: No new date/genre UI/database product features; same format policy, FFmpeg 9.0.2 pin and paired native membrane. Duplicate durable seen-marker scanner intentionally rejected.

SOFTWARE EVIDENCE: 252 historical Rust cases; 32 media / 30 library ARM-QEMU; 26 fixtures × 20 ASan/UBSan/LSan; 20-run host benchmarks. Committed compact receipts and fixtures match Git ledger.

PHYSICAL EVIDENCE: Storage-owned Baseline02 stock 1k scan: DATA 5526/393 ms and SD 5495/401 ms initial/incremental; 1000 indexed/reused each. No changed metadata full-app physical result.

MASTER INTEGRATION DECISION: Useful media/ABI/revision/limits accepted; duplicate scanner replaced by canonical DB TEMP/token protocol. Metadata and native library ship together.

FINAL INTEGRATED STATE: Linux units `0b78829`; Reborn units `5435572, 8365335`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 4. SESSION — High-resolution wired audio

ORIGINAL GOAL: Determine exact native precision and preserve low bits through software conversion.

Y2Linux: `codex/platform-v1-highres-audio`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-highres-audio/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `7163181805ff28846ab98c6a9bdd373dd980aad8`; clean. 19 changed files / 2 commits.

Y2Reborn: `codex/platform-v1-highres-audio`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-highres-audio/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `cd5d2430f7560b8077814f23cf45e88ae57bad55`; clean. 8 changed files / 1 commit.

ACTUAL CHANGES: Nearest ties-even final S24/S16 narrowing/saturation, independent-channel precision fixtures, kernel PCM contract and read-only ALSA constraint diagnostics. Source precision, FLTP DSP precision, final container/meaningful bits, I2S slot/payload and hardware admission stay distinct. Live f64 VolumeRamp is documented separately.

IMPORTANT FILES:

Y2Linux: `kernel/audio/mt6582-afe.c`, `tests/test_audio_capture.py`, `tests/test_audio_precision_contract.py`, `tests/test_platform_evidence.py`, `tools/connectivity/audio-contract.c`, `tools/host/audio_precision.py`, `tools/platform/y2_platform/diagnostic_fields.py`, `tools/platform/y2_platform/diagnostics.py`, `tools/platform/y2_platform/observe.py`, `tools/production/check_installed_arm.py`

Y2Reborn: `crates/reborn-audio/build.rs`, `crates/reborn-media/native/media.c`, `crates/reborn-media/src/native.rs`, `tools/build/fixtures.py`, `tools/build/precision-bench.c`

BUGS FIXED: Biased/truncating final narrowing and misleading precision reporting. S32 container no longer implies a true 32-bit native sink.

OPTIMIZATIONS: BUG_FIXED; HARDENED; BETTER_OBSERVABILITY; INVESTIGATED_NO_CHANGE_JUSTIFIED; PARTIAL_REMAINS_OPEN. This is software precision repair, not native highres enablement.

INVESTIGATED BUT LEFT UNCHANGED: Wider MT6582 fetch/interconnect programming lacks exact evidence. Native S16 stereo 44.1/48 and safe fallback retained; no guessed silicon ceiling or rates enabled.

SOFTWARE EVIDENCE: 241 historical Rust/fmt/Clippy/ARM; fresh kernel/config/DT/modules; 19 localized source/ABIchecks; 24 media + 8 ALSA QEMU. Unity-gain fixtures do not prove all gain/DSP states.

PHYSICAL EVIDENCE: Locked Baseline02 ALSA intersection admits only S16_LE stereo 44100/48000; S24/S32/88200/96000 refused. No serial low-bit/clock or analog proof.

MASTER INTEGRATION DECISION: Precision and telemetry accepted with shared ABI/diagnostics composition. Wider native formats/rates deliberately remain unavailable.

FINAL INTEGRATED STATE: Linux units `c95561f, 0b78829`; Reborn units `465b3d3, 5435572`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 5. SESSION — USB / desktop storage

ORIGINAL GOAL: Provide safe desktop file transfer with preserving layout and one filesystem owner.

Y2Linux: `codex/platform-v1-usb`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-usb/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `1115933c48e147e4cf4cffd60778716b27a270f5`; clean. 33 changed files / 6 commits.

Y2Reborn: `codex/platform-v1-usb`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-usb/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `51d477b2f30edfc90418d8d0c3fa5fad8de6f581`; clean. 7 changed files / 1 commit.

ACTUAL CHANGES: Configfs FunctionFS MTP and developer ECM/ACM, pinned GPL3+ responder, confined no-follow file access, durable refresh generations, typed Ready/Copying/Developer states, SD release transaction and MUSB PIO progress fix. Exact Linux 6.18 openat2/generatedARMsyscall headers fix fresh build compatibility.

IMPORTANT FILES:

Y2Linux: `buildroot/Config.in`, `buildroot/configs/y2_production_defconfig`, `buildroot/package/y2-mtp/0001-y2-safe-media-transfers.patch`, `buildroot/package/y2-mtp/Config.in`, `buildroot/package/y2-mtp/y2-mtp.hash`, `buildroot/package/y2-mtp/y2-mtp.mk`, `kernel/config/production.config`, `kernel/patches/0065-y2-musb-pio-progress.patch`, `kernel/patches/manifest.json`, `kernel/platform/usb.c`, `kernel/usb/fault.h`, `tests/test_cpu_fix03.py`, `tests/test_usb_product.py`, `tests/usb_mtp_fs.c`, `tests/usb_mtp_protocol.c`, `tools/platform/capabilities.json`, `tools/platform/y2_platform/cli.py`, `tools/platform/y2_platform/media.py`, `tools/platform/y2_platform/observe.py`, `tools/platform/y2_platform/service.py`, `tools/platform/y2_platform/usb.py`, `tools/production/build.py`, `tools/production/release.json`, `tools/production/tests.sh`, `tools/usb/mtp-safe.c`, `tools/usb/mtp-safe.h`, `tools/usb/qualify.py`, `tools/validation/dev_artifacts.py`

Y2Reborn: `app/reborn/src/bin/reborn-preview.rs`, `app/reborn/src/main.rs`, `crates/reborn-core/src/platform.rs`, `crates/reborn-platform/src/client.rs`, `crates/reborn-platform/src/storage.rs`, `crates/reborn-ui/src/pages.rs`, `crates/reborn-ui/src/tests.rs`

BUGS FIXED: Unsafe/ambiguous raw export design, supervisor ownership/recovery, stale transfer failure reporting, missing openat2 header and PIO progress. No raw MSC/RNDIS route shipped.

OPTIMIZATIONS: SIGNIFICANTLY_IMPROVED; HARDENED; BETTER_OBSERVABILITY; PARTIAL_REMAINS_OPEN. Desktop throughput remains unmeasured; implementation is meaningful without a false physical pass.

INVESTIGATED BUT LEFT UNCHANGED: No simultaneous live filesystem/raw block writers, system partition exposure, format/repartition, DMA redesign or assumed host matrix success.

SOFTWARE EVIDENCE: 411 historical production 406 pass / 5 native-covered skips; 240 Rust; 79 focused; fresh kernel/ARM/QEMU/ELF/package/source. Native confinement/protocol/fsync/delete/rename/hotplug and lease fixtures retained.

PHYSICAL EVIDENCE: Final USB subsystem candidate was uninstalled; lock-busy desktop campaign NOT_RUN. Older UART01 hashes are historical, not current desktop MTP acceptance.

MASTER INTEGRATION DECISION: Selected MTP/configfs/storage/refresh accepted with shared service/claim/sleep composition. Durable refresh cannot start scanner after sleep ACK.

FINAL INTEGRATED STATE: Linux units `c95561f, 96ce4df`; Reborn units `ccdb794, 30b6a95`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 6. SESSION — Full-system suspend

ORIGINAL GOAL: Check complete same-boot restore and explicit product quiescence; investigate RTC failure.

Y2Linux: `codex/platform-v1-suspend`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-suspend/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `2d2b543d3a597a9100a18d6352f63d3a5b19904b`; clean. 21 changed files / 10 commits.

Y2Reborn: `codex/platform-v1-suspend`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-suspend/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `c57a55f8d09af7e609ef3f76d4ba1e870493562c`; clean. 10 changed files / 3 commits.

ACTUAL CHANGES: Checked full-suspend Linux context/BIU/normalPCM/timer/CIRQ restore, shared failure quarantine, typed preparing/waking states and explicit Reborn prepare/restore ACK. All input queues reopen after wake. Codec failed-suspend rollback replays state and retained substep notes narrow future stalls. Master adds actual scanner/artwork/observation quiescence and deferred USB work.

IMPORTANT FILES:

Y2Linux: `buildroot/board/y2/production-overlay/usr/sbin/y2-suspend`, `kernel/patches/0030-cs43130-system-pm.patch`, `kernel/patches/manifest.json`, `kernel/platform/pm-journal.c`, `kernel/platform/spm-suspend-policy.h`, `kernel/platform/spm.c`, `tests/test_cpu_fix03.py`, `tests/test_platform_v1_suspend.py`, `tests/test_sleep_product.py`, `tests/test_suspend_audio.py`, `tests/test_suspend_policy.py`, `tools/development/qualify-platform-v1-suspend.py`, `tools/development/suspend_platform_device.py`, `tools/platform/y2_platform/cli.py`, `tools/platform/y2_platform/sleep.py`, `tools/platform/y2_platform/suspend_record.py`

Y2Reborn: `app/reborn/src/bin/reborn-preview.rs`, `app/reborn/src/main.rs`, `crates/reborn-control/src/lib.rs`, `crates/reborn-core/src/lib.rs`, `crates/reborn-core/src/platform.rs`, `crates/reborn-platform/src/client.rs`, `crates/reborn-platform/src/input.rs`, `crates/reborn-ui/src/lib.rs`, `crates/reborn-ui/src/pages.rs`, `crates/reborn-ui/src/tests.rs`

BUGS FIXED: Unverified restore success, failed preparation/charging misclassification, codec cache-only refusal rollback, wake-edge resleep and worker-start-after-ACK races.

OPTIMIZATIONS: HARDENED; BUG_FIXED; BETTER_OBSERVABILITY; PARTIAL_REMAINS_OPEN. No demonstrated fix of the previously observed full RTC stall.

INVESTIGATED BUT LEFT UNCHANGED: Proven runtime idle finisher/arm/restore unchanged. Ordinary full sleep still refuses unqualified hardware/charging; pm_test is not deep-resume proof.

SOFTWARE EVIDENCE: 244 historical Rust/fmt/Clippy/ARM; 129 sourcepasses/3 DTskips then 23 policy; 11 realcallbackfaulttests; freshARMkernel and headlessIPCnative/QEMU. Source changes were never installed.

PHYSICAL EVIDENCE: Baseline02 stagedfreezer/devices/platform/processors/core passes; charging refusal; awake RTC pass. One 12-second full RTC trial FAILED and watchdog recoveredboot 27→boot 88. RetainedDEVICES_RESUMING/wake 0 x 20/PCM596/reset 59325253; CS43131 resume enter 7407 lacks leave. Exact inner cause unknown; reboot hashes prove recovery only.

MASTER INTEGRATION DECISION: Checked restoration/codec/input/ACK source accepted with worker/source/USB adapters. RTC and Power physical acceptance remain separate open gates.

FINAL INTEGRATED STATE: Linux units `c95561f, 82499a0`; Reborn units `30b6a95`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 7. SESSION — Storage / filesystems

ORIGINAL GOAL: Bind media lifetime/card identity and expose truthful mode/integrity evidence.

Y2Linux: `codex/platform-v1-storage`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-storage/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `3a6b5f3e20b3e1ebaf709ff99035a7c067723d3b`; clean. 18 changed files / 2 commits.

Y2Reborn: `codex/platform-v1-storage`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-storage/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `f726ae40bfd965d7f09cb37b3e317bfb532db0f2`; clean. 6 changed files / 2 commits.

ACTUAL CHANGES: Fail-closed blockdev/diskseq live claims, persistentUUID+CID/geometry identity, FATUTF8/no-write filesystem preflight and runtimePM/tuning/fallback telemetry. Playback/queued-next/sidecars pin validated regularfile and parentFDs through decoder lifetime with no-follow walks and mount/card rechecks.

IMPORTANT FILES:

Y2Linux: `kernel/patches/0009-y2-msdc-readonly.patch`, `kernel/patches/manifest.json`, `tests/README.md`, `tests/test_filesystems.py`, `tests/test_platform_contract.py`, `tests/test_platform_storage_tools.py`, `tools/platform/y2_platform/bench.py`, `tools/platform/y2_platform/media.py`, `tools/platform/y2_platform/observe.py`, `tools/production/tests.sh`

Y2Reborn: `app/reborn/src/main.rs`, `app/reborn/src/playback.rs`, `crates/reborn-library/src/lib.rs`, `crates/reborn-media/native/media.c`, `crates/reborn-media/src/native.rs`, `crates/reborn-platform/src/storage.rs`

BUGS FIXED: ClonedUUID/reinsert stale-track admission, pathname-only decoder/sidecar opens, nested symlink escape and untruthful missinglifetime claims. Old queues refuse rather than silently bind another card.

OPTIMIZATIONS: HARDENED; BUG_FIXED; BETTER_OBSERVABILITY; PARTIAL_REMAINS_OPEN. Highest robust modes were measured, not automatically expanded.

INVESTIGATED BUT LEFT UNCHANGED: Partition/data schema/MMCclock/runtimePM/fallback remain. UUID-only legacyrows remainoffline; one rescan/newqueue selection is deliberate. No destructive guessed migration.

SOFTWARE EVIDENCE: 134 historicalsource/artifact +40 media/filesystem; fresh kernel/config/DT/ABI; all 33 audio FD/direct fixtures andJPEG/PNG/WebPpixelcomparison; special-file/symlink refusal and ARM/QEMU. Native Unicode/no-write/hash tests retained.

PHYSICAL EVIDENCE: Baseline02 eMMC 512 MiB ~98.72 MB/s; SD HS/SDR50/DDR50 ~23.23/44.45/43.28 MB/s; SDR104 4 GiB ~81.26 MB/s, zero recorded fault deltas. Same-card diskseq 2→3; stock 1kDATA/SDscratchscan/hashpass. Other-card/absent-boot/FAT/exFAT/endurance/new guard NOT_RUN.

MASTER INTEGRATION DECISION: Selected claim/filesystem/FD policy accepted with USB/metadata/DB/artwork adapters. Linux retains sole mount authority; cached artwork owns zero FDs.

FINAL INTEGRATED STATE: Linux units `c95561f, 02c314e`; Reborn units `b533ebb, 5435572, 8365335, 30b6a95`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 8. SESSION — Reborn performance

ORIGINAL GOAL: Measure and remove demonstrated render, interactive-loop and audio waste.

Y2Linux: `codex/platform-v1-reborn-performance`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-reborn-performance/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `949b78ce0f046398a3f630a4aa4ba4bcaf6f38bf`; clean. 2 changed files / 2 commits.

Y2Reborn: `codex/platform-v1-reborn-performance`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-reborn-performance/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `7ed4a406e812ca31b5f98a6cfb25e7a58f454f05`; clean. 31 changed files / 3 commits.

ACTUAL CHANGES: Visible-state rendering, descriptor waits, ordered adjacent-texture batching with 49,152 bytes of staging, opt-in bounded traces, asynchronous kernel/power/media observations on the existing watchdog, four-cover caching, and wired partial-write readiness pacing. Master adds source freshness, worker quiescence and canonical input timing.

IMPORTANT FILES:

Y2Linux: evidence/admission documents; implementation resides in the paired repository.

Y2Reborn: `app/reborn/src/artwork.rs`, `app/reborn/src/bin/reborn-bench.rs`, `app/reborn/src/main.rs`, `app/reborn/src/performance.rs`, `app/reborn/tests/architecture_guard.rs`, `crates/reborn-audio/src/native.rs`, `crates/reborn-graphics/native/graphics.c`, `crates/reborn-graphics/src/native.rs`, `crates/reborn-observability/src/lib.rs`, `crates/reborn-platform/src/allocation_counts.rs`, `crates/reborn-platform/src/bluetooth.rs`, `crates/reborn-platform/src/input.rs`, `crates/reborn-platform/src/kernel_events.rs`, `crates/reborn-platform/src/lib.rs`, `crates/reborn-platform/src/native.rs`, `crates/reborn-ui/src/lib.rs`, `tools/qualification/reborn-audio-write-profile.c`, `tools/qualification/reborn-audio-write-profile.rs`, `tools/qualification/reborn-performance-device.py`, `tools/qualification/reborn-performance-summary.py`

BUGS FIXED: Static redraw, repeated read-only work on the UI thread, unsuccessful cache insert eviction, and ALSA partial-capacity busy work.

OPTIMIZATIONS: SIGNIFICANTLY_IMPROVED; OPTIMIZED; PARTIAL_REMAINS_OPEN. Exact temporary 069415a binary: playing CPU 87.95→11.21% of one core; audio thread 82.63→5.11%; wheel KMS p95 59.93→17.52 ms, with zero measured XRUNs/errors.

INVESTIGATED BUT LEFT UNCHANGED: PCM formats, gain, buffers, lease and accepted-frame contracts remain. No extra renderer worker, electrical claim or perfect pixel identity. The weaker Bluetooth polling hunk is rejected. Initial cold layout/startup and two-sample Play/Pause regressions remain documented.

SOFTWARE EVIDENCE: Historical 243 Rust cases/fmt/strict Clippy/ARM; ten native scripted audio fault/null tests; audio-owner review binds exact pacing blob. Benchmark/capture fixtures and architecture guards are retained.

PHYSICAL EVIDENCE: Exact 069415a app SHA 7871ec67… on Baseline02 boot 88/taint 0. Supplemental 32-event Play/Pause replay improves p95. Static Home 14→0 frames/10 s; 1,000 synthetic steps; active SIGTERM 317.28 ms. Ten screen captures differ in 600/6,912,000 channels, maximum 5/255. Stock/data/policy restored. Synthetic timing excludes real mechanical IRQ/photon latency; no battery/endurance proof.

MASTER INTEGRATION DECISION: Useful performance, renderer and pacing accepted; stale BT polling omitted. Clock/source/cache/sleep contracts adapted. Exact pacing and renderer blobs retain owner bytes.

FINAL INTEGRATED STATE: Linux units `792f00a`; Reborn units `4ee462f, 7686c9b, 30b6a95`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 9. SESSION — GPU / display / graphics

ORIGINAL GOAL: Preserve the working GPU/runtime PM and reduce measured artwork cost.

Y2Linux: `codex/platform-v1-graphics`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-graphics/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `383234de0efbecf08db65b9f712211f2eec28eef`; clean. 7 changed files / 1 commit.

Y2Reborn: `codex/platform-v1-graphics`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-graphics/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `a2df691edfbb105a164e2f5f574b158ec5f81e6c`; clean. 2 changed files / 1 commit.

ACTUAL CHANGES: Checked JPEG profile/header/receive-based low-resolution decoding before 160×160 scaling. Bounded awake/off/wake/brightness and temporary native ARM measurements establish useful preservation evidence; master integrates one wrapper with FFmpeg limits.

IMPORTANT FILES:

Y2Linux: evidence/admission documents; implementation resides in the paired repository.

Y2Reborn: `crates/reborn-media/native/media.c`, `tests/artwork.py`

BUGS FIXED: Excess full-size JPEG decode cost and unchecked header-probe assumptions.

OPTIMIZATIONS: OPTIMIZED; INVESTIGATED_NO_CHANGE_JUSTIFIED; PARTIAL_REMAINS_OPEN. Temporary ARM JPEG median CPU 492.637→75.332 ms and RSS 29,920→9,320 KiB. This does not qualify the combined renderer.

INVESTIGATED BUT LEFT UNCHANGED: DRM/Lima/Mesa/GBM/EGL, scanout, clocks and runtime PM architecture remain. Static redraw is corrected by the performance owner. No optical, electrical or full-system-resume claim.

SOFTWARE EVIDENCE: Historical 68 Linux and 238 Rust cases, fmt/Clippy, ARM, ten artwork scenarios and QEMU. The receipt corrects SDK 9.0.2 and binds the tested membrane hash.

PHYSICAL EVIDENCE: Baseline02 boot 27/taint 0: static 25 frames/20.1377 s; screen-off zero frames/20.1909 s with GPU/KMS/MFG/scanout off. Five wake cycles and brightness 10/50/100 pass; 12 JPEG decodes per side. GPU job IRQ deltas and actual device FFmpeg runtime version were not independently captured.

MASTER INTEGRATION DECISION: JPEG improvement accepted through one bounded media decoder. GPU/scanout foundation preserved; new renderer batching belongs to performance with separate evidence.

FINAL INTEGRATED STATE: Linux units `792f00a`; Reborn units `5435572, 4ee462f`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 10. SESSION — SQLite / library database

ORIGINAL GOAL: Bound scan/catalog memory and avoid unnecessary persistent database writes.

Y2Linux: `codex/platform-v1-library-db`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-library-db/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `cdbdfe880609fcf8563991d5fe888fa055047857`; clean. 2 changed files / 1 commit.

Y2Reborn: `codex/platform-v1-library-db`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-library-db/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `c7a8786904825a0552ca26ee4bdc833eff822704`; clean. 11 changed files / 7 commits.

ACTUAL CHANGES: DB-owned TEMP scan_seen/scan_candidates, Begin/Probe/Batch/Finish tokens, conditional transactions, 512-row keyset pages and 250k total cap, no-op catalog preservation, WAL/durability and split-media fixtures. Master composes extractor revision 2/schema 1 migration and storage compatibility.

IMPORTANT FILES:

Y2Linux: evidence/admission documents; implementation resides in the paired repository.

Y2Reborn: `app/reborn/src/bin/reborn-bench.rs`, `app/reborn/src/main.rs`, `crates/reborn-library/src/benchmark.rs`, `crates/reborn-library/src/lib.rs`, `crates/reborn-library/src/platform_tests.rs`, `tools/build/library_db_baseline.py`, `tools/build/library_db_bench.py`

BUGS FIXED: Scan-wide maps, unchanged durable-row rewrites, unnecessary catalog reload, aborted-scan pruning, and stale source/revision reuse.

OPTIMIZATIONS: SIGNIFICANTLY_IMPROVED; OPTIMIZED; HARDENED; PARTIAL_REMAINS_OPEN. Native 50k catalog 8641.27→999.53 ms; unchanged scan 25471.03→3845.16 ms; RSS49.72→38.68 MiB. Ingest+5.7% and prune 85.50→155.21 ms tradeoffs remain.

INVESTIGATED BUT LEFT UNCHANGED: Schema 1, row IDs, foreign keys, WAL and FULL durability retained. 250k is an unqualified capacity ceiling. Target /proc/self/io was unavailable and normalized to null; no zero-NAND-write/wear claim.

SOFTWARE EVIDENCE: Historical 251 Rust cases/fmt/Clippy/ARM; seven-run host workloads through 50k; FULL/rollback/kill/reopen/identity/cancel tests. Integrated fixtures cover additive revision, UUID-only old queues and online/offline capacity.

PHYSICAL EVIDENCE: Six native 1k/10k/50k scratch runs on Baseline02 boot 27/taint 0 ; 50k split DATA/SD with DB on DATA. ext4 errors 0 and owned cleanup. Production app/DB not replaced; caches/OPPs uncontrolled; early after 1k/10k hashes not separately retained. Whole-app/endurance unqualified.

MASTER INTEGRATION DECISION: Canonical DB scanner accepted. FFmpeg second scanner rejected; its metadata acquisition/revision adapted. One catalog/scanner/DB worker remains.

FINAL INTEGRATED STATE: Linux units `792f00a`; Reborn units `8365335, 4ee462f, 30b6a95`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 11. SESSION — Input / wheel

ORIGINAL GOAL: Correct physical input timing, recovery and hold ownership with canonical actions.

Y2Linux: `codex/platform-v1-input`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-input/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `8b5803021ce8d7861278904f7afd8a06a381b0b3`; clean. 8 changed files / 4 commits.

Y2Reborn: `codex/platform-v1-input`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-input/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `e51a33525dc15eba144702a37eca694da9037b76`; clean. 4 changed files / 2 commits.

ACTUAL CHANGES: Stable physical parent identity, successfully selected evdev CLOCK_MONOTONIC provenance, kernel_mono_us, bounded 16 reads/device, backlog and press-age handling, typed Cancel for overflow/malformed keys, capture/analyzer. Master adds descriptor waits, full queue close/reopen and canonical Power routing.

IMPORTANT FILES:

Y2Linux: `tests/test_input_capture.py`, `tools/development/analyze-input.py`, `tools/development/input-capture.c`

Y2Reborn: `app/reborn/src/main.rs`, `crates/reborn-platform/src/input.rs`, `crates/reborn-ui/src/tests.rs`

BUGS FIXED: Wrong clock/backlog hold timing, stale held keys after malformed records, lost identity after rebind, wake-edge resleep and duplicate actions.

OPTIMIZATIONS: BUG_FIXED; HARDENED; BETTER_OBSERVABILITY; PARTIAL_REMAINS_OPEN. One WheelCadence owns duplicate filtering and acceleration. An isolated detent stays one semantic action.

INVESTIGATED BUT LEFT UNCHANGED: Wheel/PMIC kernel architecture retained. No invented counted-control/latency result. Old QuickSettings-on-Power expectation is replaced by shutdown confirmation; short paused Power requests guarded sleep, playing Power blanks.

SOFTWARE EVIDENCE: Historical 257 Rust cases including 37 input/40 UI, fmt/Clippy/ARM; strict C observer/analyzer. Integrated cases cover over-budget wake queues, malformed Cancel, timing/backlog and hold exclusivity.

PHYSICAL EVIDENCE: Locked Baseline02 boot 27/taint 0 observer 120.289 s captured ZERO events/IRQ deltas; owner readiness arrived after the window. The ARM userspace candidate never executed. Counted wheel/buttons/mechanical qualification NOT_RUN.

MASTER INTEGRATION DECISION: Input timing/cancellation accepted with performance/suspend adapters. kernel_mono_us is canonical; competing evdev_us field is absent.

FINAL INTEGRATED STATE: Linux units `6cd52a6`; Reborn units `7686c9b, 30b6a95`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

## 12. SESSION — Master / integration

ORIGINAL GOAL: Compose the selected subsystem handoffs into one coherent paired software candidate.

Y2Linux: `codex/platform-v1-integration`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Linux`; start/merge base `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; final `de9f26d6dc85a417e1f7f4febf5317cfbef04236`; clean. 120 changed files / 13 commits.

Y2Reborn: `codex/platform-v1-integration`; worktree `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Reborn`; start/merge base `b71b468860233faa0a42b8448ec5777fa952b8e3`; final `9cd12baeeb70b204e08299bd4c91c8c35604c304`; clean. 90 changed files / 14 commits.

ACTUAL CHANGES: Twelve Linux and thirteen Reborn units reconcile 34 concerns: shared wait, radio responsibilities, scanner/catalog, clock/cache/worker authority, storage/USB claims, precision/metadata ABI, diagnostics/privacy, sleep ACK barriers, wake input and source/version/dependency composition. One leased physical coordinator is prepared.

IMPORTANT FILES: Linux `service.py`, `observe.py`, `diagnostic_fields.py`, `usb.py`, `media.py`, production composition/configuration and qualification coordinator; Reborn `main.rs`, `background.rs`, `artwork.rs`, `playback.rs`, library/media/input/renderer contracts. The machine ledger lists all 210 changed paths across both repositories.

BUGS FIXED: Lost telemetry/bonded redaction, conflicting waits/scanners/JPEG/Power/timestamps, stale observations or USB refresh after ACK, pathname-only collection art, descriptor caches preventing eject, version identity and native audio/MTP package contracts.

OPTIMIZATIONS: HARDENED; BUG_FIXED; OPTIMIZED; BETTER_OBSERVABILITY; PARTIAL_REMAINS_OPEN. Independent software becomes one buildable source pair. Historical metrics do not prove new integrated hardware gains.

INVESTIGATED BUT LEFT UNCHANGED: CPU foundation, scanout release, native S16, battery safeguards, partitions/data and recovery preserved. Duplicate FFmpeg scanner, weaker BT polling, competing clock/cache/worker authority and unproven wider AFE enablement rejected.

SOFTWARE EVIDENCE: Master receipts:466 production cases/456 pass/ten native-covered skips; 324 Rust/fmt/Clippy; fresh kernel/ARM/QEMU; 384 ELFs/1411 edges, 106 packages, 449 source/license records. Fresh independent counts are in the baseline report.

PHYSICAL EVIDENCE: Master never contacted the device. Its compiled 4c72466/dd73dcc candidate (BOOT d2dec1… / ROOT cd3c07…) is physical NOT_RUN. Baseline02 RTC FAIL, firmware/codec permissions and source/collector limitations remain.

MASTER INTEGRATION DECISION: All eleven selected handoffs accepted with semantic adapters; owner branches/main/history untouched. Final verifier corrects stale current documents/identity, smoke/Power selection and the omitted telemetry regression contract, then builds afresh.

FINAL INTEGRATED STATE: Linux units `a99b56f..4c72466`; Reborn units `a243405..dd73dcc`. Selected source SOFTWARE_VALIDATED after independent qualification. INTEGRATED_PHYSICAL_NOT_RUN; inherited measurements remain attached to original image/binary. Above limitations remain open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
