---
title: "Y2 + Reborn Platform 1.0 live integration status - Innioasis Updater"
description: "Y2 + Reborn Platform 1.0 live integration status Installed baseline physical follow-up — 2026-10-04 The exact-image physical receipt ../validation/Y2-PLATFORM-V1-BASELINE"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-platform-v1-integration-status.html"
---

# Y2 + Reborn Platform 1.0 live integration status - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 + Reborn Platform 1.0 live integration status

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 + Reborn Platform 1.0 live integration status

## Installed baseline physical follow-up — 2026-10-04

The [exact-image physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BASELINE-PHYSICAL.md) records PARTIAL / INTERRUPTED qualification, bounded smoke/C1/hotplug/OPPs/C2 and DATA/SD successes, no qualified C3 entry, owner-reported USB reconnect trouble and recovered-boot DRM WARNING / C3 safely Skipped. Firmware/software seal below is unchanged; it is not full hardware acceptance. Owner-prioritized audio testing finishes before exclusive USB diagnosis. No main/public promotion.

## Independent final baseline — 2026-10-04

Current software handoff: Y2LINUX-PLATFORM-V1-BASELINE-01 — READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION. Compiled Linux `98daf3f0220f4a1580bb4893094ee9f0e02362a5` / Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304`; kernel `6.18.0-y2linux-platform-v1-baseline-01`, root `2025.02.18-platform-v1.24`. Canonical owner candidate: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-baseline-candidate`. Fresh 475 production cases / 465 passed / ten dependency skips, all ten independently passed; 324 Reborn tests, fmt/strict Clippy/fresh kernel/ARM/QEMU/package/source/privacy PASS. SOFTWARE_VALIDATED / INTEGRATED_PHYSICAL_NOT_RUN; PUBLIC_DISTRIBUTION_NOT_READY. UART01 CPU hardware is inherited; Baseline02 RTC FAIL remains unresolved. Policy-enabled C3, native S16, battery safeguards, DATA/layout and recovery stay.

See [baseline](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-BASELINE.md), [twelve sessions](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-FINAL-SESSION-RESULTS.md), [independent integration review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INDEPENDENT-VERIFICATION.md) and [one smoke-gated physical campaign](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-PHYSICAL-QUALIFICATION.md). This current section supersedes candidate/build/acceptance wording in the dated master planning and execution record below. Older NOT_CREATED/NOT_BUILT/accepted-none and in-progress text describes its observation time, never the current baseline. No main merge, push, flash or physical/public milestone promotion occurred.

## Historical master planning and execution record (retained)

Observation started 2026-10-04T16:46:18.335648+00:00 (Europe/Berlin: UTC+02 on this date).

Verdict: READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION. This is a timestamped evidence review; live trees can change immediately afterward. Never infer completion or hardware qualification from Git activity. See [plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INTEGRATION-PLAN.md) and [master](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-MASTER.md).

Immutable local snapshot: `/home/luca/Dokumente/Code/Y2Linux/out/platform-v1-integration-analysis/20261004T164618.335648Z/inventory.json`, paired tracked diffs, copied changed handoff documents, graph/ref inventory, candidate manifest copies and file fingerprints. Raw receipts stay ignored/private; no image/source-tree/ROM rehash. Refresh with `python3 tools/development/observe-platform-v1.py` and review changes before updating this report. The observer changes no owner refs/index/files and never marks work accepted/finished. A snapshot or manifest marked unstable must be read again.

## Source and device axes````````````````````````````

| Axis | Identity / scope |
| --- | --- |
| Linux integration foundation | b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c (main at entry) |
| Reborn integration foundation | b71b468860233faa0a42b8448ec5777fa952b8e3 (canonical checkout cpu-idle-completion; one scanout-release commit ahead of main) |
| Reborn main | 7f9df397ab3809d52e2f1073ca93a305246e0c3a; do not omit b71b468 when integrating |
| Latest installed identity in owner receipts | Baseline02, compiled Linux 8584ccd8 / Reborn b71b4688, root v1.21. Earlier subsystem boot 27e6d684-3794-4490-95db-a489027cd4f4; single RTC full-sleep trial watchdog-recovered to 88b85fa3-2282-4d93-b0b8-818a105ddd0a, taint 0. Master did not access device. |
| Protected CPU physical receipt | UART01 Linux e9e8d63f9c94232c2b6627881e0967583e202dac / Reborn b71b4688, boot fd955840-35d9-47db-83e0-ff47d6bb2d2b. C1 working; C2 84.3473%; C3 65.2450%, 3,647 checked returns, zero restore failures. |
| Baseline02 full sleep / automatic C3 / final integration | RTC full trial FAIL: no same-boot complete resume; retained DEVICES_RESUMING/wake 0x20/PCM 596/reset 0x59325253. Matching direct scratch hashes and ext4 counters after reboot prove recovery only. Automatic cold-boot/C3 gate remains open. Source units are integrated; fresh final image build and qualification remain. |

## Eleven finished source handoffs

Both branch names are `codex/platform-v1-<subsystem>` in their respective repositories. Full worktree paths and all fields follow the compact table. New commits are counted from the protected foundation; Reborn b71b468 is shared foundation, not eleven independent new changes.````````````````````````````````````````````

| Subsystem | Linux HEAD / dirty | Reborn HEAD / dirty | Lifecycle | Master source disposition | Order |
| --- | --- | --- | --- | --- | --- |
| bluetooth | 5846a7a0a133 / clean | de092094c27a / clean | Finished software handoff; physical gates open | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 5 |
| ffmpeg-metadata | e709ecc79006 / clean | c9ef7902e894 / clean | Finished software handoff; physical scan/playback NOT_RUN | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 6 → 7 → 8 |
| graphics | 383234de0efb / clean | a2df691edfbb / clean | Finished paired handoff; bounded native-ARM/awake/off/wake evidence, overall PARTIAL | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 8 |
| highres-audio | 7163181805ff / clean | cd5d2430f756 / clean | Finished software handoff; native wider hardware admission open | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 6 |
| input | 8b5803021ce8 / clean | e51a33525dc1 / clean | Finished paired source handoff at owner closure; physical MORE_WORK_REQUIRED | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 9 → 10 |
| library-db | cdbdfe880609 / clean | c7a878690482 / clean | Finished paired handoff; native 1k/10k/50k scratch evidence, wider qualification open | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 7 |
| reborn-performance | 949b78ce0f04 / clean | 7ed4a406e812 / clean | Finished clean paired handoff; scoped exact069415a device performance PASS | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 8 → 10 |
| storage | 3a6b5f3e20b3 / clean | f726ae40bfd9 / clean | Finished paired handoff; target acceptance partial | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 1 → 2 |
| suspend | 2d2b543d3a59 / clean | c57a55f8d09a / clean | Finished paired source handoff; Baseline02 full RTC FAIL, new code NOT_RUN | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 1 (kernel review) → 10 (product) |
| usb | 1115933c48e1 / clean | 51d477b2f30e / clean | Finished software/image/final harness handoff; physical NOT_RUN | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 1 → 3 → 4 → 10 |
| wifi | 78c3512400a3 / clean | 2cdb9cce8df1 / clean | Finished source handoff; Platform 1.0 physical acceptance PARTIAL | ACCEPT_WITH_INTEGRATION_ADJUSTMENT (selected source); physical gates separate | 4 |

## bluetooth

Linux branch: `codex/platform-v1-bluetooth`. Reborn branch: `codex/platform-v1-bluetooth`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-bluetooth/Y2Linux`. HEAD `5846a7a0a1336f581f075a1bba1ea6484439e760`; CLEAN; observation stable.

Commits since protected foundation:
  - `5846a7a0a1336f581f075a1bba1ea6484439e760` — Use Bluetooth events for bounded reconnect and repair discovery diagnostics

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/architecture/platform-bluetooth-v1.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-BLUETOOTH-OPTIMIZATION.md`
  - `docs/validation/evidence/platform-v1-bluetooth-optimization.json`
  - `tests/native/bt-observe-json.c`
  - `tests/native/bt-reconnect-events.c`
  - `tests/test_platform_bluetooth.py`
  - `tools/connectivity/bt-observe.c`
  - `tools/connectivity/reconnect.c`
  - `tools/development/measure-bluetooth-idle.py`
  - `tools/platform/y2_platform/bluetooth.py`
  - `tools/platform/y2_platform/diagnostic_fields.py`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-bluetooth/Y2Reborn`. HEAD `de092094c27ad4ebba3cc0ba7003f29944de53ac`; CLEAN; observation stable.

Commits since protected foundation:
  - `de092094c27ad4ebba3cc0ba7003f29944de53ac` — Reduce Bluetooth idle polling and restore daemon observation safely

Files changed (committed plus staged/unstaged/untracked at observation):
  - `crates/reborn-platform/src/bluetooth.rs`
  - `crates/reborn-platform/src/native.rs`
  - `docs/architecture/bluetooth-codecs.md`

Lifecycle: Finished software handoff; physical gates open. Platform 1.0 verdict: ACCEPT_WITH_INTEGRATION_ADJUSTMENT (source); NEEDS_MORE_WORK (qualification).

Interfaces changed: Event-driven bounded command queue; Paired/Bonded/Trusted remain distinct; negotiated_codec/PCM generation preserved; fixed discovery JSON keys.

Tests reported/receipts reviewed: Owner report: 12 Bluetooth tests; connectivity 14 pass/1 artifact skip; 7 radio and 11 platform; 238 Reborn/workspace fmt/clippy; ARM and native fake-bus Cortex-A7 QEMU pass.

Physical evidence: Baseline02 boot 27e6d684…: off/disconnected controller samples, zero CONSYS/BTIF idle IRQ increments/errors/recoveries. Changed binaries NOT_INSTALLED; no headset available; no after CPU/audio/reconnect/endurance acceptance.

Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: Foundation; shared radio ownership; diagnostic union C08; Wi-Fi coexistence and real codec peer later.

Integration risk: Medium: observer/reconnect ownership + diagnostic union. Merge order: 5.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-bluetooth/Y2Linux/docs/validation/Y2-PLATFORM-V1-BLUETOOTH-OPTIMIZATION.md`. Final paired report is reviewed. Source requires semantic composition; no new claim/mount/playback guard was installed.

## ffmpeg-metadata

Linux branch: `codex/platform-v1-ffmpeg-metadata`. Reborn branch: `codex/platform-v1-ffmpeg-metadata`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-ffmpeg-metadata/Y2Linux`. HEAD `e709ecc7900690bfbbb765227092a9f3c81a99f8`; CLEAN; observation stable.

Commits since protected foundation:
  - `e709ecc7900690bfbbb765227092a9f3c81a99f8` — Reconcile bounded physical stock media scan evidence
  - `0d692f29301e7f752c00a880129b97faf03980ed` — Audit Platform 1.0 media pass software boundaries

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-ffmpeg-metadata/Y2Reborn`. HEAD `c9ef7902e89443bfe26846dfe1f325de7d84598f`; CLEAN; observation stable.

Commits since protected foundation:
  - `c9ef7902e89443bfe26846dfe1f325de7d84598f` — Add physical stock media scanner baseline receipts
  - `bf1c50ad2475ccfeccd2ebcaad79d6cfbfca6a0c` — Record Platform 1.0 media metadata and ingest validation
  - `43a695cbb550e20a6a7e8afd2c078a50d5d45d90` — Skip media opens for sidecar-only collection artwork
  - `a22107c53fc841f7f7e6e7767822ebec720bea99` — Harden FFmpeg metadata and bound incremental library ingestion

Files changed (committed plus staged/unstaged/untracked at observation):
  - `app/reborn/src/artwork.rs`
  - `app/reborn/src/playback.rs`
  - `assets/fixtures/README.md`
  - `assets/fixtures/metadata/art-jpg.flac`
  - `assets/fixtures/metadata/art-png.flac`
  - `assets/fixtures/metadata/art-webp.flac`
  - `assets/fixtures/metadata/corrupt-art.flac`
  - `assets/fixtures/metadata/duplicate.flac`
  - `assets/fixtures/metadata/empty.flac`
  - `assets/fixtures/metadata/huge-art-dimensions.flac`
  - `assets/fixtures/metadata/huge-art-metadata.flac`
  - `assets/fixtures/metadata/huge.png`
  - `assets/fixtures/metadata/id3.mp3`
  - `assets/fixtures/metadata/invalid-utf8.flac`
  - `assets/fixtures/metadata/large.jpg`
  - `assets/fixtures/metadata/long.flac`
  - `assets/fixtures/metadata/manifest.json`
  - `assets/fixtures/metadata/tags.aiff`
  - `assets/fixtures/metadata/tags.ape`
  - `assets/fixtures/metadata/tags.flac`
  - `assets/fixtures/metadata/tags.wav`
  - `crates/reborn-library/examples/media_bench.rs`
  - `crates/reborn-library/src/benchmark.rs`
  - `crates/reborn-library/src/lib.rs`
  - `crates/reborn-media/native/media.c`
  - `crates/reborn-media/src/lib.rs`
  - `crates/reborn-media/src/native.rs`
  - `docs/DOCUMENTATION_CATALOG.md`
  - `docs/README.md`
  - `docs/architecture/reborn-audio-stack-ffmpeg9.md`
  - `docs/validation/REBORN-PLATFORM-V1-FFMPEG-METADATA.md`
  - `docs/validation/evidence/platform-v1-ffmpeg-metadata.json`
  - `tools/build/jpeg_fixture.c`
  - `tools/build/media_bench.py`
  - `tools/build/media_qemu.py`
  - `tools/build/media_sanitize.c`
  - `tools/build/metadata_fixtures.py`

Lifecycle: Finished software handoff; physical scan/playback NOT_RUN. Platform 1.0 verdict: NEEDS_REBASE_OR_RECONCILIATION (C02/C03/C09/C24). Owner's PLATFORM_V1_READY_WITH_LIMITATION refers to this software subpass only.

Interfaces changed: Demux-only MediaFile metadata; paired RbMetadata C/Rust date/genre/timing/I/O fields and limits init; bounded local custom AVIO; metadata reuse/scanner changes; JPEG reduction.

Tests reported/receipts reviewed: Final tracked report/compact JSON: fmt/strict clippy/252 workspace tests, fresh Baseline02 ARM build and 32 media + 30 library QEMU tests, six daemon/control checks, six-library FFmpeg 9.0.2 ABI/runtime manifest, 26-fixture × 20 native ASan/UBSan/LSan ownership stress, documentation/syntax/whitespace pass. Earlier local failure remains historical. Host alternating 10k scans median 7,408→1,084 ms initial / 191→130 ms unchanged; process peak 66,488→53,720 KiB. Cortex-A7 user-mode QEMU 1k 17,058→692 ms is emulator cost, not Y2 speed.

Physical evidence: Later c9ef7902 compact receipt faithfully preserves storage-owned Baseline02 1k stock scanner evidence: DATA 5,526 ms initial / 393 ms incremental, SD 5,495 / 401 ms, all 1,000 indexed/reused with no failures or controller faults. Raw receipt hashes/source identity are retained; this is baseline evidence, not a changed metadata after-result. No fresh physical qualification of the final source pair is established.

Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: Highres narrowing/precision C09; DB-owned scan contracts C02; graphics artwork C03; playback/artwork worker instrumentation.

Integration risk: High: duplicated scanner and JPEG decoder C02/C03, storage suffix-free artwork C26, production 9.0.2 environment C22. Merge order: 6 → 7 → 8.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-ffmpeg-metadata/Y2Reborn/docs/validation/REBORN-PLATFORM-V1-FFMPEG-METADATA.md`. Native membrane/Rust ABI must be built and packaged together. Extracted date/genre do not create new DB/UI features.

## graphics

Linux branch: `codex/platform-v1-graphics`. Reborn branch: `codex/platform-v1-graphics`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-graphics/Y2Linux`. HEAD `383234de0efbecf08db65b9f712211f2eec28eef`; CLEAN; observation stable.

Commits since protected foundation:
  - `383234de0efbecf08db65b9f712211f2eec28eef` — Record Platform 1.0 graphics power evidence and remaining gates

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/knowledge/gpu-platform.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-GRAPHICS.md`
  - `docs/validation/evidence/platform-v1-graphics/peer-baseline.json`
  - `docs/validation/evidence/platform-v1-graphics/physical.json`
  - `docs/validation/evidence/platform-v1-graphics/software.json`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-graphics/Y2Reborn`. HEAD `a2df691edfbb105a164e2f5f574b158ec5f81e6c`; CLEAN; observation stable.

Commits since protected foundation:
  - `a2df691edfbb105a164e2f5f574b158ec5f81e6c` — Reduce JPEG artwork decode size before texture scaling

Files changed (committed plus staged/unstaged/untracked at observation):
  - `crates/reborn-media/native/media.c`
  - `tests/artwork.py`

Lifecycle: Finished paired handoff; bounded native-ARM/awake/off/wake evidence, overall PARTIAL. Platform 1.0 verdict: NEEDS_REBASE_OR_RECONCILIATION for artwork; keep current GPU/scanout baseline.

Interfaces changed: Reduced JPEG header/decode helper; unchanged 160×160 RGBA/GL texture path; external max-pixels/thread bounds. No GPU/display/kernel ownership change.

Tests reported/receipts reviewed: Final frozen report/JSON: 68 Linux; 238 Reborn + fmt/strict clippy; ARM; 10 artwork scenarios; changed ARM membrane QEMU. Earlier GPU-02/host-cache failures explicitly superseded by final Baseline02-environment run. SDK 9.0.2 correction and tested ARM membrane SHA 5d448d9a… close C22 wording discrepancy.

Physical evidence: Durable physical.json: locked Baseline02 boot 27e6d684…/taint0. Static 25 frames/20.1377s with 4148 ms GPU runtime active; off zero frames/20.1909s, zero GPU active, KMS/MFG/scanout clocks off. Five wake cycles, brightness 10/50/100 readbacks and pre/post offscreen graphics tests pass. Temporary ARM JPEG helper reverse-order CPU median 492.637→75.332 ms, RSS29920→9320 KiB, 12 decodes each; exact changed membrane hash recorded. GPU job IRQ deltas NOT_CAPTURED after regex error; no optical/electrical/full-suspend proof. Original app/Home/paused/off/brightness restored, scratch removed, same boot/taint. Static redraw gap belongs to performance; this does not qualify its new shaders/batches.

Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: FFmpeg artwork selection C03; performance timing/capture; full-suspend and protected scanout-release foundation.

Integration risk: Medium/high: JPEG lowres duplicated with FFmpeg C03. Merge order: 8.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-graphics/Y2Linux/docs/validation/Y2-PLATFORM-V1-GRAPHICS.md`, clean paired 383234de/a2df691e closing receipt; overall PARTIAL with explicit remaining gates.

## highres-audio

Linux branch: `codex/platform-v1-highres-audio`. Reborn branch: `codex/platform-v1-highres-audio`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-highres-audio/Y2Linux`. HEAD `7163181805ff28846ab98c6a9bdd373dd980aad8`; CLEAN; observation stable.

Commits since protected foundation:
  - `7163181805ff28846ab98c6a9bdd373dd980aad8` — docs: include live sink gain in PCM precision audit
  - `d9595d6f9c64ef846243903ca4dd30a14c302e80` — audio: expose truthful PCM contract and record MT6582 precision evidence

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/CURRENT_PLATFORM_STATE.md`
  - `docs/knowledge/audio-path.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-HIGHRES-AUDIO.md`
  - `docs/validation/evidence/highres-audio/software-validation.json`
  - `docs/validation/evidence/highres-audio/sources.json`
  - `docs/validation/evidence/highres-audio/stock-cs43131-init.asm`
  - `docs/validation/evidence/highres-audio/stock-width-stubs.asm`
  - `kernel/audio/mt6582-afe.c`
  - `tests/test_audio_capture.py`
  - `tests/test_audio_precision_contract.py`
  - `tests/test_platform_evidence.py`
  - `tools/connectivity/audio-contract.c`
  - `tools/host/audio_precision.py`
  - `tools/platform/y2_platform/diagnostic_fields.py`
  - `tools/platform/y2_platform/diagnostics.py`
  - `tools/platform/y2_platform/observe.py`
  - `tools/production/check_installed_arm.py`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-highres-audio/Y2Reborn`. HEAD `cd5d2430f7560b8077814f23cf45e88ae57bad55`; CLEAN; observation stable.

Commits since protected foundation:
  - `cd5d2430f7560b8077814f23cf45e88ae57bad55` — audio: round final PCM narrowing and verify low-bit precision

Files changed (committed plus staged/unstaged/untracked at observation):
  - `assets/fixtures/manifest.json`
  - `assets/fixtures/precision-24-44100.flac`
  - `assets/fixtures/precision-24-48000.flac`
  - `crates/reborn-audio/build.rs`
  - `crates/reborn-media/native/media.c`
  - `crates/reborn-media/src/native.rs`
  - `tools/build/fixtures.py`
  - `tools/build/precision-bench.c`

Lifecycle: Finished software handoff; native wider hardware admission open. Platform 1.0 verdict: ACCEPT_WITH_INTEGRATION_ADJUSTMENT (source); NEEDS_MORE_WORK (native highres qualification).

Documentation-only closing correction 71631818 retains d9595d6 implementation / cd5d2430. The live post-conversion f64 VolumeRamp and second integer rounding are now explicit; fixtures prove unity-volume software precision and the membrane benchmark excludes live gain/ALSA/whole-app cost. No new build/device evidence follows.

Interfaces changed: Kernel pcm_contract JSON and audio.pcm_contract diagnostics; configured/running/meaningful bits distinct; final S24/S16 nearest ties-even saturation; full32 FLTP loss explicitly tested.

Tests reported/receipts reviewed: Pinned report/software-validation.json: fresh ARM kernel/config/Image/modules; 6 audio/clock/capture/DT + 19 localized source/ABI/layout checks; 241 Reborn fmt/strict clippy/tests + ARM; Cortex-A7 QEMU 24 media + 8 ALSA; 7 module ABIs. Final receipts explicitly supersede draft fixture/link/constraint failures. No new release package.

Physical evidence: Locked Baseline02 ALSA constraint intersection/idle AFE/PM reads. Admitted native S16_LE stereo 44.1/48 kHz; no demonstrated wider MT6582 fetch/interconnect contract or external serial bit/rate capture.

Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: FFmpeg FFI/metadata and DSP integration C09; safe diagnostic union C08; no speculative format-mask expansion.

Integration risk: Medium/high: FFI + honest hardware precision contract. Merge order: 6.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-highres-audio/Y2Linux/docs/validation/Y2-PLATFORM-V1-HIGHRES-AUDIO.md`. Final paired report is reviewed. Source requires semantic composition; no new claim/mount/playback guard was installed.

## input

Linux branch: `codex/platform-v1-input`. Reborn branch: `codex/platform-v1-input`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-input/Y2Linux`. HEAD `8b5803021ce8d7861278904f7afd8a06a381b0b3`; CLEAN; observation stable.

Commits since protected foundation:
  - `8b5803021ce8d7861278904f7afd8a06a381b0b3` — Close input source pass with physical acceptance limits
  - `95ed5090f9d4b863767a53ea346b34722544c003` — Record locked idle observation and refresh input candidate evidence
  - `44f8d9b79eddd13ac9b08def9c912e624d7eef39` — Record input candidate validation and retained physical event evidence
  - `99087bac96728d1b61ee92828d8d56608f5cc27d` — Add bounded physical input capture and admit Platform v1 input pass

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-INPUT.md`
  - `docs/validation/evidence/platform-v1-input-live.json`
  - `docs/validation/evidence/platform-v1-input-retained.json`
  - `tests/test_input_capture.py`
  - `tools/development/analyze-input.py`
  - `tools/development/input-capture.c`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-input/Y2Reborn`. HEAD `e51a33525dc15eba144702a37eca694da9037b76`; CLEAN; observation stable.

Commits since protected foundation:
  - `e51a33525dc15eba144702a37eca694da9037b76` — Cancel held input after malformed key records
  - `a701e0b866293c7e2bdfab95545081a8e363c074` — Fix physical input timing, wake ownership and evdev recovery

Files changed (committed plus staged/unstaged/untracked at observation):
  - `app/reborn/src/main.rs`
  - `crates/reborn-platform/src/input.rs`
  - `crates/reborn-ui/src/tests.rs`
  - `docs/architecture/platform-v1-input.md`

Lifecycle: Finished paired source handoff at owner closure; physical MORE_WORK_REQUIRED. Platform 1.0 verdict: NEEDS_REBASE_OR_RECONCILIATION (C04/C14); NEEDS_MORE_WORK (physical). Final 8b58030 report retains missing counted tests; no pending input reservation or candidate execution.

Interfaces changed: Stable physical parent identity across inputN rebind; monotonic evdev timestamps; bounded 16 reads/device; ordering/backlog/press ages; kernel_mono_us capture; suspend separately changes PowerShort/PowerHold and resume suppression, while performance adds competing evdev_us/wait.

Tests reported/receipts reviewed: Refreshed report: 257 Reborn workspace tests (37 input / 40 UI), fmt/strict clippy and ARM workspace pass; Linux input/analyzer tests and host/ARM observer -Werror. e51a335 additionally cancels stale held state on malformed key values. Line-buffered observer/graceful stop recorded by 95ed509. Physical cardinality/latency remains unmeasured.

Physical evidence: Current durable platform-v1-input-live.json: locked Baseline02 boot27e6d684…/taint0, 120.289-second raw observer captured ZERO events because owner readiness arrived after the window. Four named control IRQ deltas zero; CPUs0–3 online, C2/C3 no entries, topology guard remains. /run helper removed, installed app/hash/boot/taint unchanged; no candidate executed. This is untouched observation, not counted acceptance. Retained DEV02/GPU01 event captures stay historical; owner-ready next counted pass still pending.

Candidate produced: Refreshed ARM userspace only: `/home/luca/Dokumente/Code/worktrees/platform-v1-input/Y2Linux/out/platform-v1-input-candidate/`, Y2-INPUT-V1-CANDIDATE-01; Linux95ed509 / Reborn e51a335. Reborn SHA783291dc4b41257038d122875543fddf662e0d859e1c29c3fce0ccdaed4fbc64; no BOOTIMG/Y2ROOT, not installed/executed. Earlier a701e candidate identity remains archived as superseded source/artifact observation; see registry.

Dependencies: Suspend resumed hooks and wake-edge routing C04; performance input/state/frame correlation; display/screen owner.

Integration risk: High: competing physical stream/Power router changes C04. Merge order: 9 → 10.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-input/Y2Linux/docs/validation/Y2-PLATFORM-V1-INPUT.md`. Final paired report is reviewed. Source requires semantic composition; no new claim/mount/playback guard was installed.

## library-db

Linux branch: `codex/platform-v1-library-db`. Reborn branch: `codex/platform-v1-library-db`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-library-db/Y2Linux`. HEAD `cdbdfe880609fcf8563991d5fe888fa055047857`; CLEAN; observation stable.

Commits since protected foundation:
  - `cdbdfe880609fcf8563991d5fe888fa055047857` — docs: reconcile bounded library database performance evidence

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-library-db/Y2Reborn`. HEAD `c7a8786904825a0552ca26ee4bdc833eff822704`; CLEAN; observation stable.

Commits since protected foundation:
  - `c7a8786904825a0552ca26ee4bdc833eff822704` — docs: qualify library database performance through 50k tracks
  - `c161404630616b909183f66d187c1f06e89a9aac` — test: support bounded split-media library fixtures
  - `d6c92b151a9b1ac95e241ae0cb5fa64d8901ab64` — perf: preserve the catalog after unchanged library scans
  - `25d4ea4dad0162aa3b7614a5c7d16c3313523f70` — test: assert library foreign keys and durability policy
  - `eca41fc51b56ed5d00bf796188f2231048fc778c` — test: preserve UUID-less CID source compatibility
  - `b0b114e00e6c0c9fcf50f1401bf535d32543beb1` — perf: bound library scans and avoid unchanged database writes
  - `91520053d796545312044138f0435f56fdedc507` — test: add reproducible large-library database workloads

Files changed (committed plus staged/unstaged/untracked at observation):
  - `app/reborn/src/bin/reborn-bench.rs`
  - `app/reborn/src/main.rs`
  - `crates/reborn-library/src/benchmark.rs`
  - `crates/reborn-library/src/lib.rs`
  - `crates/reborn-library/src/platform_tests.rs`
  - `docs/README.md`
  - `docs/validation/REBORN-PLATFORM-V1-LIBRARY-DB.md`
  - `docs/validation/evidence/reborn-platform-v1-library-db-host.json`
  - `docs/validation/evidence/reborn-platform-v1-library-db-y2.json`
  - `tools/build/library_db_baseline.py`
  - `tools/build/library_db_bench.py`

Lifecycle: Finished paired handoff; native 1k/10k/50k scratch evidence, wider qualification open. Platform 1.0 verdict: NEEDS_REBASE_OR_RECONCILIATION (C02/C19/C24).

Interfaces changed: DB-owned Catalog/Begin/Probe/Batch/Finish; TEMP scan_seen/scan_candidates; 512-row pages/250k total cap; bounded fingerprint batches; unchanged durable-write suppression/source-prune transactions; new ScanMetrics.removed and no-op catalog preservation d6c92b1; split-media benchmark c161404.

Tests reported/receipts reviewed: Final source-frozen handoff: 251 workspace tests, fmt/strict clippy, pinned ARM build; host seven-run workloads through50k and FULL/rollback/kill/reopen/identity/cancel tests. Host seven no-op50k scans process writebytes1534.879MiB→0.008MiB including observability; host memory168.17→112.78MB. Target `/proc/self/io` unavailable; prior zero sentinel normalized to null, never a NAND wear or zero-write claim.

Physical evidence: Reviewed durable Y2 JSON/report: six native 1k/10k/50k scratch runs, Baseline02 boot27e6d684…/taint0/mount generation preserved. 50k split25k DATA+25k SD, DB onDATA; median full catalog8641.27→999.53ms, unchanged25471.03→3845.16ms, mixed25731.81→3873.91ms, process peak49.72→38.68MiB and DB21.617→20.457MiB. Initial ingest17.53→18.53s (+5.7%) and prune85.50→155.21ms are recorded regressions/tradeoffs. Final ext4 errors0, scratch/binaries cleaned, normal lock release. Exact before/after50k hashes retained; earlier after1k/10k digest not separately retained. Uncontrolled caches/OPPs; no installed app/production DB replacement, rendered latency/coldboot/concurrent playback/endurance/electrical proof.

Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: FFmpeg demux-only acquisition C02 and additive metadata_revision reuse/migration C24; app catalog/event loop C05; USB generation-triggered scan, storage source lifetime and old-queue admission C19/C26.

Integration risk: High: two incompatible incremental scanners C02. Merge order: 7.

Draft handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-library-db/Y2Reborn/docs/validation/REBORN-PLATFORM-V1-LIBRARY-DB.md`, frozen closing cdbdfe8/c7a8786 with host and native-Y2 durable JSON. Whole-platform source/physical integration remains separate.

## reborn-performance

Linux branch: `codex/platform-v1-reborn-performance`. Reborn branch: `codex/platform-v1-reborn-performance`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-reborn-performance/Y2Linux`. HEAD `949b78ce0f046398a3f630a4aa4ba4bcaf6f38bf`; CLEAN; observation stable.

Commits since protected foundation:
  - `949b78ce0f046398a3f630a4aa4ba4bcaf6f38bf` — docs: close scoped Reborn performance qualification on Baseline02
  - `f3de5137a47096106752d86d774858c146aec95a` — docs: admit measured Reborn performance pass on Baseline02

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-reborn-performance/Y2Reborn`. HEAD `7ed4a406e812ca31b5f98a6cfb25e7a58f454f05`; CLEAN; observation stable.

Commits since protected foundation:
  - `7ed4a406e812ca31b5f98a6cfb25e7a58f454f05` — docs: record measured Reborn performance and control qualification
  - `069415a4207c00f0a32a3a2ac00602ddea29a895` — perf: pace wired PCM writes after partial capacity
  - `b8c05db871fe0d59c3134cf8f2420945d8967b3b` — perf: reduce Reborn rendering and interactive-loop work

Files changed (committed plus staged/unstaged/untracked at observation):
  - `app/reborn/src/artwork.rs`
  - `app/reborn/src/bin/reborn-bench.rs`
  - `app/reborn/src/main.rs`
  - `app/reborn/src/performance.rs`
  - `app/reborn/tests/architecture_guard.rs`
  - `crates/reborn-audio/src/native.rs`
  - `crates/reborn-graphics/native/graphics.c`
  - `crates/reborn-graphics/src/native.rs`
  - `crates/reborn-observability/src/lib.rs`
  - `crates/reborn-platform/src/allocation_counts.rs`
  - `crates/reborn-platform/src/bluetooth.rs`
  - `crates/reborn-platform/src/input.rs`
  - `crates/reborn-platform/src/kernel_events.rs`
  - `crates/reborn-platform/src/lib.rs`
  - `crates/reborn-platform/src/native.rs`
  - `crates/reborn-ui/src/lib.rs`
  - `docs/CURRENT_REBORN_STATE.md`
  - `docs/DOCUMENTATION_CATALOG.md`
  - `docs/README.md`
  - `docs/validation/REBORN-PLATFORM-V1-PERFORMANCE.md`
  - `docs/validation/evidence/reborn-platform-v1-performance/audio-write-profile.json`
  - `docs/validation/evidence/reborn-platform-v1-performance/blkid-profile.json`
  - `docs/validation/evidence/reborn-platform-v1-performance/kmsg-profile.json`
  - `docs/validation/evidence/reborn-platform-v1-performance/play-pause.json`
  - `docs/validation/evidence/reborn-platform-v1-performance/power-sysfs-profile.json`
  - `docs/validation/evidence/reborn-platform-v1-performance/restoration.json`
  - `docs/validation/evidence/reborn-platform-v1-performance/summary.json`
  - `tools/qualification/reborn-audio-write-profile.c`
  - `tools/qualification/reborn-audio-write-profile.rs`
  - `tools/qualification/reborn-performance-device.py`
  - `tools/qualification/reborn-performance-summary.py`

Lifecycle: Finished clean paired handoff; scoped exact069415a device performance PASS. Platform 1.0 verdict: ACCEPT_WITH_INTEGRATION_ADJUSTMENT (source); wider qualification open.

Interfaces changed: Wired-only partial PCM capacity pacing069415a with one20ms readiness wait per call and unchanged accepted-frame/gain/byte/format/buffer/lease contract (C29); opt-in bounded trace/per-thread CPU/render submit/present/draw counts; native adjacent-texture batching/shaders; input descriptor wait with competing evdev_us; visible-state redraw; kernel log off the UI path; capacity-one asynchronous power/media observation via existing watchdog C25. Weaker old Bluetooth wait hunk rejected (C15).

Tests reported/receipts reviewed: Current final-source report so far gives 243 workspace tests, fmt/strict workspace-all-target clippy, pinned fresh exact069415a ARM build, four qualification-tool tests, 20 daemon tests and 1k/10k/20k fixture checks. Ten audio tests include scripted timeout/EINTR/ready-EAGAIN/XRUN/fatal states and real-null S16/S24/S32 readiness/discard; audio owner PASS_SOURCE_REVIEW binds exact069415a/fileSHA78a1f816/Gitblob0580a345. Final primary physical receipt reviewed; final clean paired handoff7ed4a406/949b78ce reviewed.

Physical evidence: Final report and durable summary/receipt now bind exact069415a ARM app SHA7871ec67f6678c7f522b1b84da0f1e53ab1646e89bc6abb6b7eafe10c02286c7 (benchmark2bbe524b) to matched instrumented baseline app2342b483 (benchmark18ec9399), both Baseline02 boot88b85fa3-2282-4d93-b0b8-818a105ddd0a/taint0 after the independent failed suspend reboot. Whole-app playing CPU87.95→11.21% of one core; audio-thread82.63→5.11%, measured audio_xruns/playback/FFmpeg errors0. Wheel KMS p9559.93→17.52ms, Now Playing77.61→17.15;1000 single steps/no mismatches, synthetic evdev only. Static Home4.96→1.88%/14→0frames over10s; four warm interactive starts759→493ms. Ten benchmark screens differ in600/6,912,000channels (0.0087%), max5/255; live covers not in those pixels, antialias/interpolation near-equivalence rather than bit identity. Retained cold layout/startup regressions and all latency tails remain in the report. Actual controls resume/seek/wired reopen/pause/resume/stop/resume PASS, active SIGTERM317.28ms/no hard kill. Stock b71/paused/off/three tracks/data restored, C3Enabled/-1/disable0, schedutil598–1300, same boot/taint0/ext4 counters0 and normal lock release. Raw compact summary/restoration/probe/receipt copied immutably to13:58 snapshot performance-final-069415a. Play/Pause only2samples KMS21.75→42.47ms remains an honest regression; a separate phase-varied16resume/16pause replay on each exact binary improves KMS p9543.98→22.55/64.70→38.50ms and handler24.68→15.63/39.84→17.22ms, all32samples/side/trace dropped0/xruns0/playback and FFmpeg errors0. Legacy bounded logger drops15/13 are retained and distinct from zero trace drops. Primary two-sample result remains intact. Supplemental play-pause.json is archived in14:10 snapshot. Stock restoration/boot88/taint0/no hard kill and normal session2232 release are recorded; closing7ed4a406/949b78ce clean and reviewed. No master device access, no analog/real IRQ/headset/coldboot/electrical/endurance qualification. Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: Graphics renderer C05; FFmpeg artwork worker/cache C27; DB catalog and main-loop patches; optional trace privacy/overhead; ALSA pacing C29 exact-source audio-owner review and final-binary measured pass retained; integrated behavior must be rerun.

Integration risk: High: native render C21, audio pacing C29, app/control/catalog, input timing C14, asynchronous source observations versus suspend quiescence C25; final source-bound pass retained; supplemental control pass and clean documentation freeze reviewed. Merge order: 8 → 10.

Final handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-reborn-performance/Y2Reborn/docs/validation/REBORN-PLATFORM-V1-PERFORMANCE.md`. Final primary comparison/capture/restoration reviewed; supplemental control pass and clean paired closing7ed4a406/949b78ce reviewed.

## storage

Linux branch: `codex/platform-v1-storage`. Reborn branch: `codex/platform-v1-storage`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-storage/Y2Linux`. HEAD `3a6b5f3e20b3e1ebaf709ff99035a7c067723d3b`; CLEAN; observation stable.

Commits since protected foundation:
  - `3a6b5f3e20b3e1ebaf709ff99035a7c067723d3b` — docs: record Platform 1.0 storage evidence and remaining gates
  - `2a603c13193552c6e07e028fa10cb87b9848bb16` — storage: harden media admission and instrument integrity workloads

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/DOCUMENTATION_CATALOG.md`
  - `docs/architecture/platform-storage-v1.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-STORAGE.md`
  - `docs/validation/Y2-SD-SDR104-DIAG.md`
  - `docs/validation/Y2-STORAGE-CEILING.md`
  - `docs/validation/evidence/platform-v1-storage-20261004.json`
  - `kernel/patches/0009-y2-msdc-readonly.patch`
  - `kernel/patches/manifest.json`
  - `tests/README.md`
  - `tests/test_filesystems.py`
  - `tests/test_platform_contract.py`
  - `tests/test_platform_storage_tools.py`
  - `tools/platform/y2_platform/bench.py`
  - `tools/platform/y2_platform/media.py`
  - `tools/platform/y2_platform/observe.py`
  - `tools/production/tests.sh`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-storage/Y2Reborn`. HEAD `f726ae40bfd965d7f09cb37b3e317bfb532db0f2`; CLEAN; observation stable.

Commits since protected foundation:
  - `f726ae40bfd965d7f09cb37b3e317bfb532db0f2` — storage: pin validated media files for current and queued playback
  - `ee1c25a60a2e0d63a6a83dbd442b5486543ec46e` — storage: bind removable sources to stable card instances

Files changed (committed plus staged/unstaged/untracked at observation):
  - `app/reborn/src/main.rs`
  - `app/reborn/src/playback.rs`
  - `crates/reborn-library/src/lib.rs`
  - `crates/reborn-media/native/media.c`
  - `crates/reborn-media/src/native.rs`
  - `crates/reborn-platform/src/storage.rs`

Lifecycle: Finished paired handoff at 3a6b5f3 / f726ae40; qualification partial. Platform 1.0 verdict: NEEDS_REBASE_OR_RECONCILIATION (C07/C19); qualification partial.

Interfaces changed: source_instance block:dev_t:diskseq lifetime; fail closed when absent; CID/geometry-qualified persistent Reborn SD IDs, FAT utf8=1 and read-only mount-preflight gate; passive runtime-PM/tuning/fallback diagnostics. Playback admission and decoder/sidecar file/parent descriptor lifetime are committed at Reborn f726ae40; source reviewed below (C26), not yet integrated or physically qualified.

Tests reported/receipts reviewed: Current closing report: 134 source/artifact + 40 final media/filesystem cases with no skips; fresh Image/zImage/modules/config/DT/ABI and warning-free MSDC object; three native no-write filesystem/Unicode/hash tests; Reborn platform 74 + library 28 in the earlier implementation receipt, targeted fmt/clippy and full pinned ARM release/QEMU; ARM Python scratch/hash/large-offset ABI. Source admission fixes not installed. Latest playback pin tests: app 38 / platform 77 / library 28 / media 22, strict lint and pinned ARM; all 33 valid audio fixtures have identical direct-versus-FD metadata/first PCM/position, plus JPEG/PNG/WebP pixels and malformed/short/FIFO/socket refusal. Final Linux 3a6b5f3 report/audit is clean and source-bound. Final ARM ELF/dependency/no-RPATH checks and Cortex-A7 QEMU direct-versus-FD JPEG/PNG/WebP pixels pass.

Physical evidence: New draft sanitized receipt identifies Baseline02 boot 27e6d684… / taint 0. Bounded direct reads: eMMC 512 MiB ~98.72 MB/s; SD HS/SDR50/DDR50 1 GiB ~23.23/44.45/43.28 MB/s; SDR104 type-B 4 GiB ~81.26 MB/s, recorded controller deltas zero. Same-card diskseq 2→3 and 2-file reinsert scan/reuse with 0 failures. Advisory cache-drop filesystem results are not guaranteed cold reads. Completed stock 1k corpus on each volume: DATA 1.731/3.078 MB/s write-fsync/read-SHA, 5,526/393 ms initial/incremental scan; SD 1.532/3.034 MB/s, 5,495/401 ms; all 1,000 indexed/reused per volume, zero failures/fault deltas. Owned scratch/harness cleaned and normal release restores mounted HS200/SDR104, same boot/taint 0. No second-card replacement/absent boot/physical FAT-exFAT/endurance/new-image qualification; frozen guard remains uninstalled.

Candidate produced: no sealed BOOTIMG/Y2ROOT release pair. The retained offline artifact /home/luca/Dokumente/Code/worktrees/platform-v1-storage/Y2Linux/out/storage-kernel/BOOTIMG.img is 7,149,568 bytes, reported SHA256 c13df78b3eefad83b2c54e9efc95fb5331f37ab29ec1e3743876fe8aa52edeca, uninstalled and not the master RC. Final f726ae40 ARM app SHA ee02fa2407427eb9552e7d4ac86e44661460c92002591c03829201eb941217c2 / matching media membrane 4301bb096b371ad085ce14c7f631e5ce7a92b80c61d7ab08efab7e0959860b17 have ELF/QEMU evidence only; no new root image or physical source acceptance.

Dependencies: USB root pins/eject C07; Reborn source identity and DB prune/reuse C19/C24; playback/queued-next/custom AVIO source binding C26; preserve MMC runtime gating for C2/C3.

Integration risk: High: persistent source-ID upgrade C19, resolved owner source guard C26 still needing combined-media regression and USB/scanner lifetime/claim C07; no automatic faster-mode admission from bounded measurements. Merge order: 1 → 2.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-storage/Y2Linux/docs/validation/Y2-PLATFORM-V1-STORAGE.md`. Final paired report is reviewed. Source requires semantic composition; no new claim/mount/playback guard was installed.

## suspend

Linux branch: `codex/platform-v1-suspend`. Reborn branch: `codex/platform-v1-suspend`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-suspend/Y2Linux`. HEAD `2d2b543d3a597a9100a18d6352f63d3a5b19904b`; CLEAN; observation stable.

Commits since protected foundation:
  - `2d2b543d3a597a9100a18d6352f63d3a5b19904b` — Record failed RTC return at codec resume and preserve qualification evidence
  - `a69bd50a75a8c21f34bb01df50c2a8caab596b2c` — Restore codec state after suspend refusal and retain full-resume substeps
  - `564710f54105f01e105e67dd66fac10160da5e33` — Record complete evdev resume reset validation
  - `5ed5e089c632354209dbf2132acb99373adc80bf` — Record retained suspend qualification lease checks
  - `7e10bdc94b3c0848ddccb6c8737a245b038fe15f` — Retain the shared device lease throughout suspend qualification
  - `c7086e8c4a695bdf7710beaf7dc720498316cf7e` — Record ARM sleep handshake and suspend file inventory
  - `e5b805e6e4a690865ea2759efc8f7feef7774cfa` — Record suspend source validation and exact implementation commits
  - `50cc21856a637fe15a3ad07f89b71379192826a6` — Support a verified temporary Wi-Fi suspend observer
  - `c73cd8385fb5f3a4df81b04e215c5989f0c841ab` — Keep charging and failed preparation as explicit sleep refusals
  - `69fa2c7a21a4b5b548736e61492b38d4d35686e6` — Check full-suspend restoration and require explicit Reborn sleep acknowledgement

Files changed (committed plus staged/unstaged/untracked at observation):
  - `buildroot/board/y2/production-overlay/usr/sbin/y2-suspend`
  - `docs/DOCUMENTATION_CATALOG.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-SUSPEND.md`
  - `docs/validation/evidence/platform-v1-suspend-2026-10-04.json`
  - `kernel/patches/0030-cs43130-system-pm.patch`
  - `kernel/patches/manifest.json`
  - `kernel/platform/pm-journal.c`
  - `kernel/platform/spm-suspend-policy.h`
  - `kernel/platform/spm.c`
  - `tests/test_cpu_fix03.py`
  - `tests/test_platform_v1_suspend.py`
  - `tests/test_sleep_product.py`
  - `tests/test_suspend_audio.py`
  - `tests/test_suspend_policy.py`
  - `tools/development/qualify-platform-v1-suspend.py`
  - `tools/development/suspend_platform_device.py`
  - `tools/platform/y2_platform/cli.py`
  - `tools/platform/y2_platform/sleep.py`
  - `tools/platform/y2_platform/suspend_record.py`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-suspend/Y2Reborn`. HEAD `c57a55f8d09af7e609ef3f76d4ba1e870493562c`; CLEAN; observation stable.

Commits since protected foundation:
  - `c57a55f8d09af7e609ef3f76d4ba1e870493562c` — Reopen evdev queues after whole-system resume
  - `f69c3c4cffcd38817bb5d0c62acaa9737205eb10` — Clear wake input before fallible display restoration
  - `4544b1a897e71397fef8bacad5df4d1258ed1333` — Prepare and restore Reborn through typed whole-system sleep states

Files changed (committed plus staged/unstaged/untracked at observation):
  - `app/reborn/src/bin/reborn-preview.rs`
  - `app/reborn/src/main.rs`
  - `crates/reborn-control/src/lib.rs`
  - `crates/reborn-core/src/lib.rs`
  - `crates/reborn-core/src/platform.rs`
  - `crates/reborn-platform/src/client.rs`
  - `crates/reborn-platform/src/input.rs`
  - `crates/reborn-ui/src/lib.rs`
  - `crates/reborn-ui/src/pages.rs`
  - `crates/reborn-ui/src/tests.rs`

Lifecycle: Finished paired source handoff; Baseline02 full RTC FAIL, new code NOT_RUN. Platform 1.0 verdict: NEEDS_REBASE_OR_RECONCILIATION; full sleep hardware open.

Interfaces changed: sleep preparing/waking states, legacy restoring compatibility; sleep_prepare/sleep_restore control acknowledgement; PowerShort/PowerHold; wake-edge suppression; full PCM/reset/same-boot proof; suspend_restore_failures; committed codec PM retained substep notes and suspend-refusal cache replay (C28).

Tests reported/receipts reviewed: Latest report: pinned production ARM Image/zImage/modules; 132 source cases = 129 pass / 3 emitted-DTB skips; later 23 policy tests. Final codec source a69bd50 + report2d2b543: 11 focused callback fault tests PASS; earlier 12 audio/policy pass / 1 DTB skip; fresh ARM Image/zImage/modules PASS. Real callbacks exercise rail/reset/regcache refusal/recovery and silent ordinary runtime tracing. New full source is not installed. Reborn fmt/strict clippy/244 tests + ARM; native and Cortex-A7 QEMU headless prepare/refusal/restore/repeat IPC pass. New image not installed. Earlier ambiguous 132-pass wording superseded; protected idle tests repeat after integration.

Physical evidence: Reviewed owner raw receipts on installed Baseline02: freezer and battery devices/platform/processors/core staged passes, clean charging devices refusal -EBUSY, awake one-shot RTC pass. Single 12-s RTC full trial FAILS: old boot 27e6d684 watchdog-recovers to 88b85fa3, taint0; retained valid sequence175 DEVICES_RESUMING/wake0x20/fullPCM596/reset59325253/ringcycle138/backstop30 with no complete/EXIT. The ring includes enter7407 for 1-0030 (DTS CS43131 codec) without matching leave through7422; MMC callbacks leave0. This narrows investigation, not a proven codec root cause. Master corrected the owner’s initial all-callbacks-returned inference. Both 64-KiB aligned O_DIRECT scratch hashes match after reboot and root/data/SD ext4 counters0: recovery only. Owner reports normal cleanup/release, no second deep trial. New-source full RTC/Power restoration, mixed5/10 cycles/endurance NOT_RUN. pm_test cannot qualify full sleep.

Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: Input pipeline C04; graphics scanout foundation; USB copy/refusal, radio/storage restoration; shared SPM restore/broken gate C13.

Integration risk: High: protected shared SPM + input/Power + Reborn RPC. Merge order: 1 (kernel review) → 10 (product).

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-suspend/Y2Linux/docs/validation/Y2-PLATFORM-V1-SUSPEND.md`. Final clean report/source pair reviewed; exact inner codec stall remains unknown until a coherent owner-installed future image. Ordinary product full-sleep gate remains refused. Master must compose shared contracts and preserve both the failure and software-only fix limits.

## usb

Linux branch: `codex/platform-v1-usb`. Reborn branch: `codex/platform-v1-usb`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-usb/Y2Linux`. HEAD `1115933c48e147e4cf4cffd60778716b27a270f5`; CLEAN; observation stable.

Commits since protected foundation:
  - `1115933c48e147e4cf4cffd60778716b27a270f5` — Seal USB candidate handoff and qualify transfer diagnostics
  - `d9ea222de458ce79fdfda940542ccd93e1ec6d93` — Record USB software qualification and guarded owner transfer matrix
  - `08019df44c8a7fbc249fc49a5a41f7ac906429ba` — Build MTP against pinned openat2 and generated ARM syscall ABI
  - `6fcd1b2e135d9f4b05097b4dfa2f7c9dca82789d` — Preserve transfer failure causes and freeze latest hardware evidence
  - `5cb5be0c1f06f9a853f0cce6b4aef914bf9e23e5` — Validate configfs-only gadget and recover supervisor ownership
  - `418723dece8c2294ad221c9e7a542af33ad8aef0` — Add safe desktop MTP transfer with ECM and media refresh

Files changed (committed plus staged/unstaged/untracked at observation):
  - `buildroot/Config.in`
  - `buildroot/configs/y2_production_defconfig`
  - `buildroot/package/y2-mtp/0001-y2-safe-media-transfers.patch`
  - `buildroot/package/y2-mtp/Config.in`
  - `buildroot/package/y2-mtp/y2-mtp.hash`
  - `buildroot/package/y2-mtp/y2-mtp.mk`
  - `docs/architecture/platform-usb-v1.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-USB.md`
  - `docs/validation/evidence/platform-v1-usb.json`
  - `kernel/config/production.config`
  - `kernel/patches/0065-y2-musb-pio-progress.patch`
  - `kernel/patches/manifest.json`
  - `kernel/platform/usb.c`
  - `kernel/usb/fault.h`
  - `tests/test_cpu_fix03.py`
  - `tests/test_usb_product.py`
  - `tests/usb_mtp_fs.c`
  - `tests/usb_mtp_protocol.c`
  - `tools/platform/capabilities.json`
  - `tools/platform/y2_platform/cli.py`
  - `tools/platform/y2_platform/media.py`
  - `tools/platform/y2_platform/observe.py`
  - `tools/platform/y2_platform/service.py`
  - `tools/platform/y2_platform/usb.py`
  - `tools/production/build.py`
  - `tools/production/release.json`
  - `tools/production/tests.sh`
  - `tools/usb/mtp-safe.c`
  - `tools/usb/mtp-safe.h`
  - `tools/usb/qualify.py`
  - `tools/validation/dev_artifacts.py`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-usb/Y2Reborn`. HEAD `51d477b2f30edfc90418d8d0c3fa5fad8de6f581`; CLEAN; observation stable.

Commits since protected foundation:
  - `51d477b2f30edfc90418d8d0c3fa5fad8de6f581` — Integrate USB file transfer states and incremental library refresh

Files changed (committed plus staged/unstaged/untracked at observation):
  - `app/reborn/src/bin/reborn-preview.rs`
  - `app/reborn/src/main.rs`
  - `crates/reborn-core/src/platform.rs`
  - `crates/reborn-platform/src/client.rs`
  - `crates/reborn-platform/src/storage.rs`
  - `crates/reborn-ui/src/pages.rs`
  - `crates/reborn-ui/src/tests.rs`

Lifecycle: Finished software/image/final harness handoff; physical NOT_RUN. Platform 1.0 verdict: NEEDS_REBASE_OR_RECONCILIATION (C01/C07/C17/C19); NEEDS_MORE_WORK (qualification). Closing 1115933 records later harness PID/start-time-safe CPU/RSS/HWM metrics and sixth harness guard; the sealed image remains compiled 08019df/51d477b.

Interfaces changed: FunctionFS MTP + developer ECM/ACM selection; Linux-only filesystem owner; org.y2linux.usb-transfer/v1 at system.usb.file_transfer; durable refresh_generation and active; typed Copying/Developer; SD release transaction.

Tests reported/receipts reviewed: Fresh source-bound build-freeze/exit-code/build-check receipts: ARM kernel/Buildroot/Reborn/config/DT/modules/ABI pass; 411 production cases (406 pass, five minimal-host skips separately covered by 27 native filesystem/GIO + three ALSA), 79 focused + five final harness, 240 Reborn/fmt/clippy, Cortex-A7 QEMU/installed ARM/ELF/inventory/legal-info/preserving package pass. Earlier missing openat2-header exit-2 failure retained; owner 08019df supplies exact pinned/generated kernel headers and superseding successful receipts (C23). Legal collection is not public-distribution clearance.

Physical evidence: Lock-busy batch NOT_RUN; no current desktop enumeration/speed/throughput or changed-image acceptance. Earlier installed-UART01 wording corrected by 6fcd1b2 using the retained locked Baseline02 receipt. Original UART01 bounded checksums stay historical; no new C3 qualification.

Candidate produced: sealed `out/y2linux-platform-v1-usb-candidate/`, compiled Linux `08019df44c8a7fbc249fc49a5a41f7ac906429ba` / Reborn `51d477b2f30edfc90418d8d0c3fa5fad8de6f581`; manifest image hashes indexed below. Later d9ea222 changes report/harness only. Subsystem release metadata v1.22/USB is not the master RC identity; physical acceptance NOT_RUN.

Dependencies: Storage diskseq/root identity C07; shared Wi-Fi event wait C01; one DB/scanner and Reborn generation consumer C05; final packaging/legal/source closure.

Integration risk: High: package/gadget/media lifetime + wait loop. Merge order: 1 → 3 → 4 → 10.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-usb/Y2Linux/docs/validation/Y2-PLATFORM-V1-USB.md`; exact-image desktop acceptance remains MORE_WORK_REQUIRED. Latest Linux fix supersedes the earlier CDC module design with configfs-only ownership.

## wifi

Linux branch: `codex/platform-v1-wifi`. Reborn branch: `codex/platform-v1-wifi`.

Y2Linux worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-wifi/Y2Linux`. HEAD `78c3512400a3a907e93fe3d73bf2870dc5a35d14`; CLEAN; observation stable.

Commits since protected foundation:
  - `78c3512400a3a907e93fe3d73bf2870dc5a35d14` — Record Wi-Fi optimization baseline, fixes and remaining physical gates
  - `7056977dc534a655f0ca8d1a4c1f4353e8131d27` — Preserve reviewed Wi-Fi observations in redacted diagnostics
  - `2bd345a3eb2b35c30c3103dacd43cb9ed903fae7` — Reuse a fresh RSSI observation across DNS readiness checks
  - `61eecee1961c9243077388d196bd8113db626b5a` — Separate real Wi-Fi link losses from duplicate cleanup notifications
  - `d408b28ac7513470a66d2b49a9ebbf3347e79d6a` — Fix Wi-Fi readiness delays and bound redundant status and policy work

Files changed (committed plus staged/unstaged/untracked at observation):
  - `docs/knowledge/wifi-bluetooth.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-WIFI-OPTIMIZATION.md`
  - `docs/validation/evidence/platform-v1-wifi-optimization.json`
  - `tests/test_diagnostic_export.py`
  - `tests/test_platform_contract.py`
  - `tests/test_platform_network_time.py`
  - `tests/test_radio_policy.py`
  - `tools/platform/y2_platform/diagnostic_fields.py`
  - `tools/platform/y2_platform/diagnostics.py`
  - `tools/platform/y2_platform/network.py`
  - `tools/platform/y2_platform/observe.py`
  - `tools/platform/y2_platform/radio_policy.py`
  - `tools/platform/y2_platform/service.py`

Y2Reborn worktree: `/home/luca/Dokumente/Code/worktrees/platform-v1-wifi/Y2Reborn`. HEAD `2cdb9cce8df1b9a65a4f88f8cd39dd05f851093e`; CLEAN; observation stable.

Commits since protected foundation:
  - `2cdb9cce8df1b9a65a4f88f8cd39dd05f851093e` — Reduce redundant Wi-Fi inventory queries and bind readiness to the live link

Files changed (committed plus staged/unstaged/untracked at observation):
  - `crates/reborn-platform/src/wifi.rs`

Lifecycle: Finished source handoff; Platform 1.0 physical acceptance PARTIAL. Platform 1.0 verdict: ACCEPT_WITH_INTEGRATION_ADJUSTMENT (C01/C08); NEEDS_MORE_WORK (qualification).

Interfaces changed: Current boot/epoch/BSSID/IP DNS and Online proof; 3 s observation bound; 30 s RSSI/inventory caches; DnsProbeSchedule; status_query_failures and signal_observation; wpa_supplicant remains reconnect owner.

Tests reported/receipts reviewed: Final report/evidence: 94 affected Linux / 0 skips + 5 layout + 6 diagnostic export checks; 74 Reborn platform tests, fmt/strict clippy and ARM platform-crate build. Delayed fake replies, inventory request counts, epochs/route races, status failures and privacy covered. Earlier draft/cache/epoch failures superseded by final tests; no global image pass inferred.

Physical evidence: Locked installed Baseline02 before: 1.48–2.08 s STATUS/SIGNAL_POLL; IP/DNS/platform-ready latency, checksummed HTTP RX 43.941–44.922 / TX 46.376–46.942 Mb/s. TX iperf control reset stays unresolved. FAST_PSP sample reverted to CAM, INVALID for power comparison. Changed-policy after runs NOT_RUN due lock; headset/coexistence/local-playback/AP loss/cold-boot remain open. Zero C2/C3 in four-core/USB windows is not a Wi-Fi-only conclusion.

Candidate produced: no new sealed subsystem release manifest discovered for this pair. ARM objects/helpers/benchmark outputs are not boot/root images. Re-scan before final handoff.

Dependencies: USB service wait C01; preserved checksum-offload disable; Bluetooth coexistence; full suspend restoration.

Integration risk: High: USB/Wi-Fi service wait replacement C01. Merge order: 4.

Handoff: `/home/luca/Dokumente/Code/worktrees/platform-v1-wifi/Y2Linux/docs/validation/Y2-PLATFORM-V1-WIFI-OPTIMIZATION.md`. Final paired report is reviewed. Source requires semantic composition; no new claim/mount/playback guard was installed.

## Cross-branch overlaps

Temporary-copy probes at the first reviewed source cut found text conflicts in Linux service.py (USB/Wi-Fi), Reborn library lib.rs (FFmpeg/DB), media.c artwork (FFmpeg/graphics), and input.rs (input/suspend). Changes remained local to scratch copies. Counts belong to that exact cut and can change; file hashes are in `out/platform-v1-integration-analysis/merge-probes-20261004.json`. C01–C29 in the [plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INTEGRATION-PLAN.md%23conflict-decisions-required-before-integration&anchor=conflict-decisions-required-before-integration) give semantic ownership and required regressions.

A later source-only pairwise review of the stable 13:32 cut checks 64 overlapping owner pairs and finds 16 pairs with text conflict regions. Its exact heads/file hashes and per-pair counts are in `20261004T133242.502821Z/pairwise-merge-review/receipt.json` under the analysis folder. This additionally confirms diagnostic allowlist/enum insertion, explicit production-test list, collection-art cache, FFmpeg/storage playback/native-image and performance/USB main-loop conflicts. Scratch output is not an implementation or proof of semantic compatibility; clean text overlaps still need C01–C29.``````````````````````````````````````````````````````````````````

| Repository / overlapping file | Owners | Classification / decision |
| --- | --- | --- |
| Y2Linux: docs/DOCUMENTATION_CATALOG.md | storage, suspend | Independent documentation additions; retain both links (C12) |
| Y2Linux: docs/planning/platform-v1-roadmap.md | bluetooth, ffmpeg-metadata, graphics, highres-audio, input, library-db, reborn-performance, storage, suspend, usb, wifi | Repeated insertions; likely text conflict and stale identity risk (C12/C20) |
| Y2Linux: docs/planning/roadmap-gap-audit.md | bluetooth, ffmpeg-metadata, graphics, highres-audio, input, library-db, reborn-performance, storage, suspend, usb, wifi | Repeated insertions; likely text conflict and stale identity risk (C12/C20) |
| Y2Linux: kernel/patches/manifest.json | storage, suspend, usb | Independent patch entries, new codec PM overlay and final digest/composition review (C10/C28) |
| Y2Linux: tests/test_cpu_fix03.py | suspend, usb | Independent test additions; preserve USB and suspend assertions (C13/C16) |
| Y2Linux: tests/test_platform_contract.py | storage, wifi | Independent test additions; storage and Wi-Fi fixture union (C06/C07) |
| Y2Linux: tools/platform/y2_platform/cli.py | suspend, usb | Independent command additions; shared parser/error behavior (C11) |
| Y2Linux: tools/platform/y2_platform/diagnostic_fields.py | bluetooth, highres-audio, wifi | Independent Bluetooth/audio/Wi-Fi fields; projection gap partially resolved by 7056977 (C08/C18) |
| Y2Linux: tools/platform/y2_platform/diagnostics.py | highres-audio, wifi | Independent audio/Wi-Fi public enums; preserve redaction and fix remaining C18 gap |
| Y2Linux: tools/platform/y2_platform/media.py | storage, usb | Lifetime/eject dependency; semantic review (C07/C19) |
| Y2Linux: tools/platform/y2_platform/observe.py | highres-audio, storage, usb, wifi | Independent sections; shared schema/diagnostic union (C06/C18) |
| Y2Linux: tools/platform/y2_platform/service.py | usb, wifi | Confirmed text/semantic wait conflict (C01) |
| Y2Linux: tools/production/tests.sh | storage, usb | Independent additions; union explicit test lists (C10) |
| Y2Reborn: app/reborn/src/artwork.rs | ffmpeg-metadata, reborn-performance | FFmpeg sidecar freshness versus performance successful-insert eviction/metrics; one bounded cache/worker (C27) |
| Y2Reborn: app/reborn/src/bin/reborn-bench.rs | library-db, reborn-performance | Independent workload instrumentation; shared metrics types (C02/C05) |
| Y2Reborn: app/reborn/src/bin/reborn-preview.rs | suspend, usb | Independent fixtures; enum/constructor union (C11) |
| Y2Reborn: app/reborn/src/main.rs | input, library-db, reborn-performance, storage, suspend, usb | Shared catalog/control/frame loop, asynchronous observations and source-bound playback; semantic union (C05/C14/C17/C25/C26) |
| Y2Reborn: app/reborn/src/playback.rs | ffmpeg-metadata, storage | Source/root lifetime pins versus media/art cache changes; review every decoder/queued-next open and paired ABI/cancellation (C09/C26) |
| Y2Reborn: crates/reborn-core/src/platform.rs | suspend, usb | Additive USB/sleep enums; exhaustive match union (C11) |
| Y2Reborn: crates/reborn-library/src/benchmark.rs | ffmpeg-metadata, library-db | Shared scanner/metrics; interface reconciliation (C02) |
| Y2Reborn: crates/reborn-library/src/lib.rs | ffmpeg-metadata, library-db, storage | Confirmed scan conflict/duplication FFmpeg+DB; storage+DB duplicate CID helper; C02/C19 |
| Y2Reborn: crates/reborn-media/native/media.c | ffmpeg-metadata, graphics, highres-audio, storage | Shared artwork decoder, precision and suffix-free pinned-file detection; semantic composition (C03/C09/C26) |
| Y2Reborn: crates/reborn-media/src/native.rs | ffmpeg-metadata, highres-audio, storage | Paired native ABI/limits + precision tests; semantic union (C09) |
| Y2Reborn: crates/reborn-platform/src/bluetooth.rs | bluetooth, reborn-performance | Duplicated optimization; reject stale performance hunk (C15) |
| Y2Reborn: crates/reborn-platform/src/client.rs | suspend, usb | Independent typed USB/sleep parsing; enum/schema review (C11) |
| Y2Reborn: crates/reborn-platform/src/input.rs | input, reborn-performance, suspend | Confirmed text conflict; timing/Power/handle disagreement (C04/C14) |
| Y2Reborn: crates/reborn-platform/src/native.rs | bluetooth, reborn-performance | Independent native wait helpers; retain both symbols (C15) |
| Y2Reborn: crates/reborn-platform/src/storage.rs | storage, usb | Independent additions; source/lifetime/eject semantics (C07/C19) |
| Y2Reborn: crates/reborn-ui/src/lib.rs | reborn-performance, suspend | Visible-state/frame and Power effects; semantic union (C05/C11) |
| Y2Reborn: crates/reborn-ui/src/pages.rs | suspend, usb | Mostly independent USB/sleep presentation; enum/UX review (C11) |
| Y2Reborn: crates/reborn-ui/src/tests.rs | input, suspend, usb | Power contracts disagree; reconcile expected behavior (C04/C11) |
| Y2Reborn: docs/DOCUMENTATION_CATALOG.md | ffmpeg-metadata, reborn-performance | Harmless independent report registrations; retain both and verify catalog/link consistency |
| Y2Reborn: docs/README.md | ffmpeg-metadata, library-db, reborn-performance | Harmless independent report links; retain both and verify catalog/link consistency |

## Candidate registry

Manifest-recorded image hashes and source identities below are retained provenance, not recomputed hashes or final-RC acceptance. No subsystem candidate supersedes the protected foundation without a reviewed decision. Historical candidate purpose comes from its name/build identity and original manifest/report. Exact physical verdicts remain in those dated receipts. All prior evidence is retained; none is deleted.``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| Candidate path under Y2Linux/out (unless absolute) | Linux / Reborn source | BOOTIMG / Y2ROOT recorded SHA256 | Purpose / physical state / supersession |
| --- | --- | --- | --- |
| cpu-idle-completion-physical/20261003T130848Z-candidate | not recorded / not recorded | not recorded / not recorded | Unsealed candidate directory; no manifest source/image identity or physical acceptance inferred. |
| cpu-idle-completion-physical/20261003T144857Z-candidate02 | not recorded / not recorded | not recorded / not recorded | Unsealed candidate directory; no manifest source/image identity or physical acceptance inferred. |
| platform-v1-candidate-before-license-fix | 6128dd010c3c41e64a73219a38178488537c50a0 / 6c8aa128550ec80addd08ef3145e9d5a846ddf2e | f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622 / 183ddfc2d9986d20c5703241fef1563e3dbd82a57ecd64742cb67827b5b6cafa | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| platform-v1-candidate-license-checkpoint | 62e1eb8ef50c465d07747d62b5060441b18684d3 / 6c8aa128550ec80addd08ef3145e9d5a846ddf2e | f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622 / 6f89e6e7324724798fc22fe55a0f0d3764bc2e2ea1f11a1bde38d29bb5400f85 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-baseline-02-candidate | 8584ccd85f052f351fe51650b2348c83ca894ed4 / b71b468860233faa0a42b8448ec5777fa952b8e3 | 5d8a2999368a04b23b898d2106b465eb6b028c2314da1a39c66c6b26dc8c41a3 / 3148bea2b6d78be34afcbb9cd933502f14416e81c8053324ff6c9ea151ee3892 | Sealed software foundation; installed identity observed, cold-boot/C3 qualification open; not superseded by active drafts. |
| y2linux-baseline-candidate | 131ee4621cd583c955182f994adac5a594fb823f / 7f9df397ab3809d52e2f1073ca93a305246e0c3a | fd5fab1eb67375ed29a8d8cbfabf070c1be18c3e43143821b4763fa358e71603 / 390e41c05e520baa36759d0cdb95c185231b536b480d32e12deb260eaeaf3623 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-community-beta-feature-completion-candidate | 02eb7359cff1d1e6eec725d496078338d1e7d601 / 72e94b2d8eb13dcb7e2677bff2846edec3ddf81a | 060145e3931e1d23f0b9805c0f12417d47f1589cf4489010705876a1ade7b098 / 2039d61e30bd02d0f3fd8006808e7dbc95bbaabce7f1834fa12d57bcccd81995 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-cpu-c3-uart-candidate | e9e8d63f9c94232c2b6627881e0967583e202dac / b71b468860233faa0a42b8448ec5777fa952b8e3 | a35e7ccb11dfcc642089e422d48a274ab2c700dbba15d00b21cce7b463e4006a / d3a8282a9f5d1b0046283bce1b595eb5797b62c2bff90a62260e80bbfafb5d98 | Protected UART01 bounded CPU evidence/rollback pair; superseded as latest software image by Baseline02, physical evidence retained. |
| y2linux-cpu-final-candidate | ff586dfff2b5e7abd28af339c055375307308f1f / afcf9ffa1bc45073e97520d592c0284ce73fefcf | ab9a1621ffd3e650ac65be0e26a4f76f104bc5c5be77a496d1d699dd1790221f / 68134c6c9712d4d88770694000a30d6f3f13d0f480a7a53bf5c2ba4883c7691b | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-cpu-final-fix01-candidate | 0de6e951b438bf0f2d701e23e476d2b2405ba3c6 / 36db1869c6bab1ad2d00b7d8e7807ea6ef5b3803 | 82b38fd31549f6a2aa84c10c11e4cc42015a225fddc7ded7d40feb3145a0ab25 / 26aa01ce84cc012e08309269a464e609e4d9dc1a9a837528eecbbe9e99a1d1f5 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-cpu-final-fix02-candidate | 1a1a6693dcd82f62daecd4c1491ef512823a86c5 / 77cf83e09a18f82a867040e72d35b6e70b26fa85 | a621e270038356056ec21cb332a6592a18373e075e4df8a1f32beaca3b8fdd5e / 5010d839766f52ebce9934f07ee6e4189c3318eacc460021f156a92b9ea27835 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-cpu-final-fix03-candidate | 76a5d41df683a1680b1127393deb0101aafe7697 / 77cf83e09a18f82a867040e72d35b6e70b26fa85 | c55b26407e46a436f2bfffe216feecfd18ced6b7bd404ed8ab6eaa013ba9cce6 / 04cafd4bddab65a01e0a35c056ee9a22a6b00ffa059cd863a95095af635d7257 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-cpu-idle-completion-02-candidate | db0234e7519c559031da6f427869ab683ffe0f3c / b71b468860233faa0a42b8448ec5777fa952b8e3 | aa371ce343801c41b0908aa85f7c11d7ae6de91cbbe93420ce1f7d29a5b0caa2 / 54b799fbcd6c85ef4b61c4210e68e1ee19efa8e6079fd2c96bf238e16d728f15 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-cpu-idle-completion-candidate | 3dfb5f5cc731ec5dac88a778290819c23dba6067 / b71b468860233faa0a42b8448ec5777fa952b8e3 | 3303cad8d0b73a78653f58d80ede2d1583ed7ef89a48f781f8aaf1669240092d / 816b9a271633c96fd937fa71ef1ac1f93e74436fbd8e97c9d0491470cc4babbb | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-hardware-02-candidate | 76bc8229580ec8d101008c5bad47419f2c110eae / 95747e0a36c7b27beb44b8cdd54feda1813f2f3a | b2a2c3bcb7cc7783828882e447e8b867453cb5b65846ce63577076b1ca4afeea / 63dbd0a198cd86e847c10ed163fd14b2cbe269595fa1988c99ac8393160bb547 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-hardware-final-candidate | 067003f8988042a832181e935128ea93e26070a7 / 5b5d23b89952d88faf3155cf680ccce918f1b099 | fc43a5a46fafd070c49785b0d16c12c85a64120338090e68e475e68069fa864a / 047185abd2e1a3f423fe7e15358009d9c10a43731155a9d63de1948c187d221e | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-platform-v1-candidate | d04b95aaff713edf943042d97a4c6134ca19fc24 / 6c8aa128550ec80addd08ef3145e9d5a846ddf2e | f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622 / 970330d24f6a0bddb0cb685d37232b298566c5cd7025a45990566f03c3f66fa3 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-platform-v1-physical-01-candidate | 198fa7cfd54a93826b54e3c0c4fab4d32e84acec / feb530fae2cdf785c764d619e8df22798c8e524c | f3309fd98e204da9013636c67a3cff9ab359cf92eae6f320d8c536853115a151 / e21ee81570a1beef7ea007bb992abcebfb78992686c66124aa3b0f357fcb2840 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-platform-v1-telemetry-01-candidate | not recorded / not recorded | not recorded / not recorded | Historical manifest/checkpoint; not a final Platform 1.0 RC; physical state not established here. |
| y2linux-reborn-boot-order-candidate | 68f1480720b53fc6da7f3ed34fb4cf0f45682e38 / 0de7af3a90692aeecc4d13b12c5520075e9b4f40 | 33a6ecd6b30a3c5a9655a4ced136f4cccc1dcb957cc6dccebffb4ba0c89a19ad / 8e008a42577242513d03f82e1035c48c04c3cd6a2302cfeea57bdd0d7d156c53 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-reborn-boot-polish-candidate | 9ac2c0b7018ce707ec15f8845daf58ce38ec18a0 / eb64b8b21058eacb1ef183f7570cca8100cbbb46 | 4e665b3c67e8d9674181e173c83623372c0986b83584d3137e2392aed310d1c0 / 25862b1e0078bb064d3d840caa0f7571234e69181d39f30d9e36771c375079f1 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-reborn-product-ui-v2-candidate | 5cfe04cb2fe9e1177df99f3113b7a17ee7d442f5 / bd8436dd2afcdbe4a45b9140aa98e4d20307482b | 8a974cb5dc672dd0f2a6589a3b8da08a7225879ee7c60e929ed398bbd293e7bf / a5c2914ed688ff1bc5eecad276a071d084995b47c1ad8c2b1de21182e79f474c | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-reborn-ui-v1-candidate | not recorded / not recorded | not recorded / not recorded | Historical manifest/checkpoint; not a final Platform 1.0 RC; physical state not established here. |
| y2linux-reborn-ui-v1-candidate-initial | not recorded / not recorded | not recorded / not recorded | Historical manifest/checkpoint; not a final Platform 1.0 RC; physical state not established here. |
| y2linux-sd-sdr104-diag03-candidate | c5f0eecf51901f51f16f80a3291a7a8630cc75ba / b92d312cc2dc4b74f57a1a9a7b1407e34707137a | 94b9976dd3fed82122197acd1f8de1fa116b346f0f1a1db0330b529261798689 / b163d0d1f9301c6067c1e46577942ca5dd3f88bac6c93b1a581425879310f1a7 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-sd-sdr104-diag04-candidate | dcbd7d1b8ad502e574e5a4f7b927d62b45ac81dd / b92d312cc2dc4b74f57a1a9a7b1407e34707137a | 139e1d05fb7d5bdada4a499eb2fbfebf21467317fd01a2ee1189763284aecd19 / a88aa8395dc9dcd53e2700a4cc60bcb4ac81940d95d4fc7871c218222e629384 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-storage-ceiling-02-candidate | 4db6d6dee8e8b21d85f4f7dfa8e6b7aac82d5e56 / b92d312cc2dc4b74f57a1a9a7b1407e34707137a | 5c17f744a0569feb16f6954531024ae7dcafee10bf14cbdb2eb18ba5d083fd36 / dc611011ce6f129cf18a61a28f9435e2504ade1d416f0b78d6db26764fd20a59 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| y2linux-storage-ceiling-candidate | 540ae029b13940d4b2dfe21902bed71b89cb117a / b92d312cc2dc4b74f57a1a9a7b1407e34707137a | 4332d4f284e9ee76b4d76985480c184ebaacd7c674a3656925ff290ef3cd501c / 72eab34a39255a1b7f2eba0fe0a6abd891a0b089f8fb847cf42ad8eec033ba72 | Historical subsystem/diagnostic/checkpoint candidate; superseded as latest software foundation by Baseline02. Original image-specific physical state remains separate. |
| /home/luca/Dokumente/Code/worktrees/platform-v1-input/Y2Linux/out/platform-v1-input-candidate | 95ed5090f9d4b863767a53ea346b34722544c003 / e51a33525dc15eba144702a37eca694da9037b76 | No BOOTIMG/Y2ROOT. reborn 783291dc4b41257038d122875543fddf662e0d859e1c29c3fce0ccdaed4fbc64; rebornctl 1bad84301dd2ff2574fa4e8b8e0cca4623a87a8c5218e056aa367cc3f6eea28a; input-capture cef15c48a2655d13512c41ee1c05b4504f8b18aae0e6f388a88ec5a50313499d | Refreshed ARM input userspace, Y2-INPUT-V1-CANDIDATE-01; latest e51a335 code and 95ed509 tooling. Not installed/executed; physical PENDING. Earlier a701e/d0330570 manifest retained in prior dated inventories; current path replacement does not transfer its evidence. Not a final release/fallback. |
| /home/luca/Dokumente/Code/worktrees/platform-v1-usb/Y2Linux/out/y2linux-platform-v1-usb-candidate | 08019df44c8a7fbc249fc49a5a41f7ac906429ba / 51d477b2f30edfc90418d8d0c3fa5fad8de6f581 | b1b9dc1ec000159cb9d9c75327ab6d60aa32f29ffe476ab8450f7850e76fc9c4 / cf0a4eccbd30cb556bb28d3ca7d145a8a75e968e24b1fbaf70d31b3dcaed9c52 | USB MTP + ECM subsystem candidate; software/package pass, physical NOT_RUN. Compiled 08019df/51d477b; later d9ea222 report/harness separate. Not the final RC; supersedes its failed build attempt only. |

The master candidate `out/y2linux-platform-v1-integration-candidate/` is NOT_BUILT; no BOOTIMG/Y2ROOT hash exists for it. Candidate manifests, fallback pairs and subsystem evidence are not combined by relabeling files.

## Every registered worktree and historical reference

Historical clean/detached build snapshots are inactive retained artifacts by observed purpose, not newly discovered live engineering sessions. Completion is not inferred from their commits. Missing/prunable registrations remain untouched. Status belongs to this observation; no worktree pruning/cleaning occurred.``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| Repository | Worktree path | Registered HEAD | Branch / lifecycle | Dirty state |
| --- | --- | --- | --- | --- |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux | b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c | refs/heads/main; canonical checkout | dirty |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/baseline-02-worktrees/Y2Linux | 8584ccd85f052f351fe51650b2348c83ca894ed4 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/baseline-worktrees/Y2Linux | 131ee4621cd583c955182f994adac5a594fb823f | refs/heads/baseline-integration; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/boot-order-worktrees/Y2Linux | 68f1480720b53fc6da7f3ed34fb4cf0f45682e38 | refs/heads/boot-order-polish; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/boot-polish-worktrees/Y2Linux | 9ac2c0b7018ce707ec15f8845daf58ce38ec18a0 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/cpu-c3-uart-worktrees/Y2Linux | e9e8d63f9c94232c2b6627881e0967583e202dac | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix01-worktrees/Y2Linux | 0de6e951b438bf0f2d701e23e476d2b2405ba3c6 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix02-worktrees/Y2Linux | 1a1a6693dcd82f62daecd4c1491ef512823a86c5 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix03-worktrees/Y2Linux | 76a5d41df683a1680b1127393deb0101aafe7697 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-worktrees/Y2Linux | ff586dfff2b5e7abd28af339c055375307308f1f | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/cpu-idle-completion-worktrees/Y2Linux | db0234e7519c559031da6f427869ab683ffe0f3c | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/feature-completion-worktrees/Y2Linux | 02eb7359cff1d1e6eec725d496078338d1e7d601 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/hardware-final-worktrees/Y2Linux | 067003f8988042a832181e935128ea93e26070a7 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/hardware02-worktrees/Y2Linux | 76bc8229580ec8d101008c5bad47419f2c110eae | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/platform-v1-physical-worktrees/Y2Linux | 198fa7cfd54a93826b54e3c0c4fab4d32e84acec | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/reborn-product-ui-v2-final-worktrees/Y2Linux | 5cfe04cb2fe9e1177df99f3113b7a17ee7d442f5 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/reborn-product-ui-v2-worktrees/Y2Linux | 5cfe04cb2fe9e1177df99f3113b7a17ee7d442f5 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/sd-diag03-worktrees/Y2Linux | c5f0eecf51901f51f16f80a3291a7a8630cc75ba | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/sd-diag04-worktrees/Y2Linux | dcbd7d1b8ad502e574e5a4f7b927d62b45ac81dd | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /home/luca/Dokumente/Code/Y2Linux/out/storage-ceiling-worktrees/Y2Linux | 4db6d6dee8e8b21d85f4f7dfa8e6b7aac82d5e56 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Linux | /tmp/y2linux-boot-handoff | 5d2bb63781120e3c656e834f470a15d6146bf235 | refs/heads/docs/stock-boot-handoff; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-gap-audit | ebeed72745df66d23861e0ecbc40cbc05715f189 | refs/heads/docs/platform-gap-audit; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-launch-gates | 83f9a24f375a825d8a48982b57e0306f7c1f8003 | refs/heads/research/launch-gates; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-m0-research | 5a167944aabc7b2093b04547068f869f1bc8efc9 | refs/heads/docs/m0-evidence-baseline; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-m1 | 5ab850f46e334f60c153091befe3ac0a39511cab | refs/heads/build/m1-offline; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-next-five | a5ea039896b907d18da6341c80d2011a955c76c1 | refs/heads/docs/m1-hardware-platform-next-five; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-platform-v1-pass/Y2Linux | 6e444d392b5bcf630f018b26b936c511c40e9f26 | refs/heads/platform-v1-completion; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-ram-map | a4c7f5bb7382d054b2f104b23d4876549b9696ae | refs/heads/docs/initial-ram-map; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-risk-diagnostic | b90ffb9af53558cddef4c081ce0f8144d42765ab | refs/heads/research/risk-accepted-diagnostic; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-usb-logging | 00b4afa957a05c9169db4d19b91968593237c097 | refs/heads/docs/y2e180-usb-logging; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-y2b245 | 0a580b146533095ec35d93524f178f0a77e2a3f9 | refs/heads/build/y2b-245; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-y2b250 | 61b70c4b9233f7cb4465686382b791ce315a3555 | refs/heads/fix/y2b250-time32-nanosleep; missing/prunable historical registration | absent |
| Y2Linux | /tmp/y2linux-y2e140 | b4fcc12fc86d025dfa626c671db0eb611bf97943 | refs/heads/research/y2e-140-observation; missing/prunable historical registration | absent |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 | refs/heads/cpu-idle-completion; canonical checkout | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/baseline-02-worktrees/Y2Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/baseline-worktrees/Y2Reborn | 7f9df397ab3809d52e2f1073ca93a305246e0c3a | refs/heads/baseline-integration; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/boot-order-worktrees/Y2Reborn | 0de7af3a90692aeecc4d13b12c5520075e9b4f40 | refs/heads/boot-order-polish; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/boot-polish-worktrees/Y2Reborn | eb64b8b21058eacb1ef183f7570cca8100cbbb46 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/cpu-c3-uart-worktrees/Y2Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix01-worktrees/Y2Reborn | 36db1869c6bab1ad2d00b7d8e7807ea6ef5b3803 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix02-worktrees/Y2Reborn | 77cf83e09a18f82a867040e72d35b6e70b26fa85 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix03-worktrees/Y2Reborn | 77cf83e09a18f82a867040e72d35b6e70b26fa85 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-worktrees/Y2Reborn | afcf9ffa1bc45073e97520d592c0284ce73fefcf | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/cpu-idle-completion-worktrees/Y2Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/feature-completion-worktrees/Y2Reborn | 72e94b2d8eb13dcb7e2677bff2846edec3ddf81a | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/hardware-final-worktrees/Y2Reborn | 5b5d23b89952d88faf3155cf680ccce918f1b099 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/hardware02-worktrees/Y2Reborn | 95747e0a36c7b27beb44b8cdd54feda1813f2f3a | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/platform-v1-physical-worktrees/Y2Reborn | feb530fae2cdf785c764d619e8df22798c8e524c | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/reborn-product-ui-v2-final-worktrees/Y2Reborn | bd8436dd2afcdbe4a45b9140aa98e4d20307482b | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/reborn-product-ui-v2-worktrees/Y2Reborn | 94e79d82cebedf8d6ca1cdc8f8e2ff8d317e2358 | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/sd-diag03-worktrees/Y2Reborn | b92d312cc2dc4b74f57a1a9a7b1407e34707137a | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/sd-diag04-worktrees/Y2Reborn | b92d312cc2dc4b74f57a1a9a7b1407e34707137a | detached; inactive retained build/history snapshot; no live completion inferred | clean |
| Y2Reborn | /home/luca/Dokumente/Code/Y2Linux/out/storage-ceiling-worktrees/Y2Reborn | b92d312cc2dc4b74f57a1a9a7b1407e34707137a | detached; inactive retained build/history snapshot; no live completion inferred | clean |

## All local and cached remote refs

No fetch or push was performed. Upstream tracking values reflect locally cached refs. Unreferenced frozen detached build HEADs appear in the worktree table. Full local graph is archived alongside inventory; implementation admission uses commits since the foundation, not generic ahead-of-main counts.

### Y2Linux`baseline-integration 131ee4621cd583c955182f994adac5a594fb823f boot-order-polish 68f1480720b53fc6da7f3ed34fb4cf0f45682e38 build/m1-offline 5ab850f46e334f60c153091befe3ac0a39511cab origin/build/m1-offline build/y2b-245 0a580b146533095ec35d93524f178f0a77e2a3f9 codex/platform-v1-bluetooth 5846a7a0a1336f581f075a1bba1ea6484439e760 codex/platform-v1-ffmpeg-metadata e709ecc7900690bfbbb765227092a9f3c81a99f8 codex/platform-v1-graphics 383234de0efbecf08db65b9f712211f2eec28eef codex/platform-v1-highres-audio 7163181805ff28846ab98c6a9bdd373dd980aad8 codex/platform-v1-input 8b5803021ce8d7861278904f7afd8a06a381b0b3 codex/platform-v1-integration 4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2 codex/platform-v1-library-db cdbdfe880609fcf8563991d5fe888fa055047857 codex/platform-v1-reborn-performance 949b78ce0f046398a3f630a4aa4ba4bcaf6f38bf codex/platform-v1-storage 3a6b5f3e20b3e1ebaf709ff99035a7c067723d3b codex/platform-v1-suspend 2d2b543d3a597a9100a18d6352f63d3a5b19904b codex/platform-v1-usb 1115933c48e147e4cf4cffd60778716b27a270f5 codex/platform-v1-wifi 78c3512400a3a907e93fe3d73bf2870dc5a35d14 cpu-idle-completion b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c origin/cpu-idle-completion [ahead 1] docs/initial-ram-map a4c7f5bb7382d054b2f104b23d4876549b9696ae docs/m0-evidence-baseline 5a167944aabc7b2093b04547068f869f1bc8efc9 docs/m1-hardware-platform-next-five a5ea039896b907d18da6341c80d2011a955c76c1 docs/platform-gap-audit ebeed72745df66d23861e0ecbc40cbc05715f189 docs/stock-boot-handoff 5d2bb63781120e3c656e834f470a15d6146bf235 docs/y2e180-usb-logging 00b4afa957a05c9169db4d19b91968593237c097 fix/y2b250-time32-nanosleep 61b70c4b9233f7cb4465686382b791ce315a3555 hardware-final a605c884aed7705a93293299628ef95d5f0219f8 origin/hardware-final main b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c origin/main platform-v1-completion 6e444d392b5bcf630f018b26b936c511c40e9f26 research/launch-gates 83f9a24f375a825d8a48982b57e0306f7c1f8003 research/risk-accepted-diagnostic b90ffb9af53558cddef4c081ce0f8144d42765ab research/y2e-140-observation b4fcc12fc86d025dfa626c671db0eb611bf97943 origin b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c origin/build/m1-offline 5ab850f46e334f60c153091befe3ac0a39511cab origin/cpu-idle-completion acb5bb3e8fb3a0cdc07a6d31fc64b6e83118ccbc origin/hardware-final a605c884aed7705a93293299628ef95d5f0219f8 origin/main b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`

### Y2Reborn`baseline-integration 7f9df397ab3809d52e2f1073ca93a305246e0c3a boot-order-polish 0de7af3a90692aeecc4d13b12c5520075e9b4f40 codex/platform-v1-bluetooth de092094c27ad4ebba3cc0ba7003f29944de53ac codex/platform-v1-ffmpeg-metadata c9ef7902e89443bfe26846dfe1f325de7d84598f codex/platform-v1-graphics a2df691edfbb105a164e2f5f574b158ec5f81e6c codex/platform-v1-highres-audio cd5d2430f7560b8077814f23cf45e88ae57bad55 codex/platform-v1-input e51a33525dc15eba144702a37eca694da9037b76 codex/platform-v1-integration dd73dcc3243045cd33e319dda2f76918ed37ea31 codex/platform-v1-library-db c7a8786904825a0552ca26ee4bdc833eff822704 codex/platform-v1-reborn-performance 7ed4a406e812ca31b5f98a6cfb25e7a58f454f05 codex/platform-v1-storage f726ae40bfd965d7f09cb37b3e317bfb532db0f2 codex/platform-v1-suspend c57a55f8d09af7e609ef3f76d4ba1e870493562c codex/platform-v1-usb 51d477b2f30edfc90418d8d0c3fa5fad8de6f581 codex/platform-v1-wifi 2cdb9cce8df1b9a65a4f88f8cd39dd05f851093e cpu-idle-completion b71b468860233faa0a42b8448ec5777fa952b8e3 hardware-final b5d1f4f985ffcbb14da013e7d56c098285496b46 origin/hardware-final main 7f9df397ab3809d52e2f1073ca93a305246e0c3a origin/main platform-v1-completion 8675020660e97df0bec09ea7a4f3fad5d671a88a origin 7f9df397ab3809d52e2f1073ca93a305246e0c3a origin/hardware-final b5d1f4f985ffcbb14da013e7d56c098285496b46 origin/main 7f9df397ab3809d52e2f1073ca93a305246e0c3a`

## Supplementary layout discovery

A bounded directory audit also found storage's `/home/luca/Dokumente/Code/worktrees/platform-v1-storage/Y2Player`symlink to canonical `/home/luca/Dokumente/Code/Y2Player`, not a twelfth independent worktree. No source changes or new local commits were observed there; it is supplementary stock-product reference, not an integration target. Other unrelated neighboring repositories were not inspected. Read-only auxiliary refs/graph/registrations are archived in the snapshot.````````````````````````````````````````````````````````````````````````````````````````````````

| Supplementary checkout/registration | HEAD | Branch / state |
| --- | --- | --- |
| /home/luca/Dokumente/Code/Y2Player | 870f2b33e49129990bc0a98eeb34d58ed42542b6 | refs/heads/main; clean; no commits beyond local main |
| /home/luca/Dokumente/Code/Y2Player/.git/worktrees/issue44/C:/Users/Luca/Documents/Y2Player/build/worktrees/issue44 | 1fdbe4acbf76bf096e8109f6918f494312cee5cb | refs/heads/fix/issue-44-alphabet-scrub; absent/prunable historical registration |
| /home/luca/Dokumente/Code/Y2Player/.git/worktrees/issue76/C:/Users/Luca/Documents/Y2Player/build/worktrees/issue76 | a05f5b028796fb0c216867f1d0b03e3f58c36b4d | refs/heads/fix/issue-76-artist-albums; absent/prunable historical registration |
| /home/luca/Dokumente/Code/Y2Player/.git/worktrees/issue82/C:/Users/Luca/Documents/Y2Player/build/worktrees/issue82 | 0d0831f127aec7919b421ff08f01cdd0a3ed84b6 | refs/heads/fix/issue-82-dismiss-transient-alert; absent/prunable historical registration |
| /home/luca/Dokumente/Code/Y2Player/.git/worktrees/issue83/C:/Users/Luca/Documents/Y2Player/build/worktrees/issue83 | 8ebaca7674772d68d59c99f5aa23c89a04138ff6 | refs/heads/fix/issue-83-remove-transition-footer; absent/prunable historical registration |
| /home/luca/Dokumente/Code/Y2Player/.git/worktrees/issue84/C:/Users/Luca/Documents/Y2Player/build/worktrees/issue84 | bd656a93e761d4104afc92db6b8b692f8ea0d743 | refs/heads/fix/issue-84-usb-haptic; absent/prunable historical registration |
| /tmp/y2-fm-branch | 80d130a4876342a4f547026e5c1779eedf37196e | detached; absent/prunable historical registration |
| /tmp/y2-fm-integration | 4db3851855b4753fb34dace43ef309c8d66dd828 | refs/heads/fm-radio-v3.2; absent/prunable historical registration |
| /tmp/y2player-device-update | f4e788fca2865e9c3e5124e035e55600d9cdca20 | detached; absent/prunable historical registration |
| /tmp/y2player-device-update-94 | af9fce5881b17655c2ec06e2232b1e53e088c7cc | detached; absent/prunable historical registration |
| /tmp/y2player-eq-ux | 1ee38afda71586622eb9a86282a9bd180796c15e | refs/heads/fix/94-equalizer-selection-ux; absent/prunable historical registration |
| /tmp/y2player-search | 4b257a435a44647f0993980dfe6154575341d757 | refs/heads/feature/54-device-search; absent/prunable historical registration |
| /tmp/y2player-search-followup | b04bc570768b592be6b095562c7575a7c5a0e65d | refs/heads/fix/54-search-keyboard-layout; absent/prunable historical registration |
| /tmp/y2player-search-input | 3659119148acc14ed6c9f548722d83707125eb3e | refs/heads/fix/54-search-empty-input; absent/prunable historical registration |
| /tmp/y2player-search-opt | 723d4cd972d033f52a99ef5a36526fe9fdfc6484 | refs/heads/perf/54-search-index; absent/prunable historical registration |
| /tmp/y2player-wrap-all | a74c02f4c0be066baef599449240f71c66e94666 | refs/heads/fix/67-wrap-all-screens; absent/prunable historical registration |

Auxiliary cached refs (no fetch/push):`backup-session-2026-08-02 6fff51cb2410de4faeb4a97f502db4d183c4db84 feature/54-device-search 4b257a435a44647f0993980dfe6154575341d757 fix/54-search-empty-input 3659119148acc14ed6c9f548722d83707125eb3e fix/54-search-keyboard-layout b04bc570768b592be6b095562c7575a7c5a0e65d fix/67-wrap-all-screens a74c02f4c0be066baef599449240f71c66e94666 fix/94-equalizer-selection-ux 1ee38afda71586622eb9a86282a9bd180796c15e fix/issue-44-alphabet-scrub 1fdbe4acbf76bf096e8109f6918f494312cee5cb fix/issue-72-custom-sleep-timer a648c10f5c6efa5e0f5eccdb3c6f962e2cfa2925 fix/issue-74-screen-off-audio 86ddd515272994b5c019f73a7b2f0475ab05af95 fix/issue-76-artist-albums a05f5b028796fb0c216867f1d0b03e3f58c36b4d fix/issue-79-queue-input de0e651495e4e028066c5462bfb179b6d69146e9 fix/issue-81-sleep-timer-expiry 7094f5ec5a0deeec1bfdf34deb2bcf01f7e40b83 fix/issue-82-dismiss-transient-alert 0d0831f127aec7919b421ff08f01cdd0a3ed84b6 fix/issue-83-remove-transition-footer 8ebaca7674772d68d59c99f5aa23c89a04138ff6 fix/issue-84-usb-haptic bd656a93e761d4104afc92db6b8b692f8ea0d743 fix/issue-86-artwork efdbda99a6cbfee5e652bce11bb109bd6e24cef9 fix/issue-93-shuffle-order ecdd6d0ace6760e56467ff04e873f6a71d849aeb fix/issue-98-wake-seek 0fd0c74d63b80413a67bb9ee0c72dca348b1028b fm-radio 80d130a4876342a4f547026e5c1779eedf37196e fm-radio-v3.2 4db3851855b4753fb34dace43ef309c8d66dd828 integrate/completed-issues bb36db708b7474b502aac20b51b9fcfb10ae7b0b main 870f2b33e49129990bc0a98eeb34d58ed42542b6 perf/54-search-index 723d4cd972d033f52a99ef5a36526fe9fdfc6484 origin 870f2b33e49129990bc0a98eeb34d58ed42542b6 origin/fix/54-search-empty-input 3659119148acc14ed6c9f548722d83707125eb3e origin/fix/issue-44-alphabet-scrub 39447a0c026b30afee483b6e3b9de2cbb01086b9 origin/fix/issue-76-artist-albums a05f5b028796fb0c216867f1d0b03e3f58c36b4d origin/fix/issue-79-queue-input de0e651495e4e028066c5462bfb179b6d69146e9 origin/fix/issue-81-sleep-timer-expiry 7094f5ec5a0deeec1bfdf34deb2bcf01f7e40b83 origin/fix/issue-82-dismiss-transient-alert 0d0831f127aec7919b421ff08f01cdd0a3ed84b6 origin/fix/issue-83-remove-transition-footer 8ebaca7674772d68d59c99f5aa23c89a04138ff6 origin/fix/issue-84-usb-haptic bd656a93e761d4104afc92db6b8b692f8ea0d743 origin/fix/issue-86-artwork efdbda99a6cbfee5e652bce11bb109bd6e24cef9 origin/fm-radio 80d130a4876342a4f547026e5c1779eedf37196e origin/integrate/completed-issues bb36db708b7474b502aac20b51b9fcfb10ae7b0b origin/main 870f2b33e49129990bc0a98eeb34d58ed42542b6 RealeaseV2.2.2 ae3945fbbcc0518e3b6c3e9857de438b29d6a469 Release c27b504774d7989f00c39797494bfa65e236a3f8 Release2.5 a4f3c6ea1ee22d23e52cdf891272b7e0c4412315 ReleaseV1.1 4811574eb4df2d57602f2599809ba0cb61ac0e3b ReleaseV1.2 4563d91398ec2ab2cbc74be6aa6f911ac61ef45f ReleaseV2.0 bb098e2a74529fd2de4869dbd2965ea434df9e41 ReleaseV2.1 8680efe68f8c5184c459150dacdc89d75157f39b ReleaseV2.2 ddd8dc84f063b79c0bd14a8725209d79b0498e26 ReleaseV2.2.1 b8268259552c28cae249eeec4bdac3f39609834e ReleaseV2.3 263552d114b66601ab0cd8223f4d5779750b9b6b`

## Refresh/validation limits

Registered worktrees: Linux 44, Reborn 31; live subsystem pairs 11. Snapshot stability is per worktree, not an atomic multi-repository transaction. The first prototype inventory had a leading-space status parsing defect and misclassified the historical physical-worktrees directory; corrected observer snapshots from 11:02:21 UTC onward govern the tables above.

Master validation so far: read-only inventory, actual diffs/reports/log files, temporary-copy merge probes, pure combined diagnostic projection, offline existing qualification plans and document/diff checks. No subsystem tests, build, device experiment, flash, merge, rebase, main commit or push was performed.

## Master integration execution — source composition complete

Isolated paired branches `codex/platform-v1-integration` are under `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/`. Owner admission remains the frozen14:24 final source roster;15:40 observer confirms all22 owner heads unchanged, clean and stable. Total registered Linux/Reborn worktrees is77 including these two master trees. No owner worktree/ref/index was changed.

All chosen subsystem source units are composed with targeted software checks. Reborn324 workspace tests, strict workspace/all-target Clippy and fmt check PASS; Linux40 focused suspend/diagnostics/precision and earlier unit tests PASS. Exact pinned9.0.2 ARM/QEMU, fresh production/kernel/DT/modules/ABI, package/privacy and source/notices gates remain. Current image is NOT_BUILT; subsystem candidates remain separate retained artifacts. Source admission is distinct from product acceptance: full RTC failure, hardware-limited highres and unrun peer/desktop/ input/endurance lanes remain open.

Rejected/superseded source fragments: performance's stale Bluetooth timer hunk; FFmpeg's competing durable presence/wall-marker scanner in favor of DB-owner TEMP/token protocol; duplicate JPEG decoders in favor of graphics checked lowres inside FFmpeg's unified bounded wrapper; old input timestamp/Power definitions and pathname-only art access. All original handoffs and measured regressions are preserved. Warm art retains four pixel entries plus immutable claims and zero cached file descriptors, preserving SD eject. See master execution ledger and C01–C30 decisions for the exact composition and new conflict regressions.

## Source composition cutoff — 2026-10-04

All eleven paired source handoffs are finished, clean and unchanged at the 15:40 read-only refresh. Each useful implementation is now ACCEPT_WITH_INTEGRATION_ADJUSTMENT in the master branches; this supersedes the initial reconciliation requests in the historical review below. Graphics GPU/runtime-PM and protected CPU foundations are deliberately preserved. Physical/product acceptance remains PARTIAL or NEEDS_MORE_WORK as recorded per owner. No integrated image exists at this cutoff. See the master execution ledger for every integration commit and rejected duplicate/stale hunk.

Current master source checkpoints: Linux `e4a615dc9d02b70a3ceb71558162fce0cc70614d` and Reborn `dd73dcc3243045cd33e319dda2f76918ed37ea31`. All selected source is integrated; fresh production composition is running. Initial reconciliation dispositions in dated owner sections record the discovery review; the compact source disposition above reflects completed semantic integration. No Platform 1.0 candidate is sealed yet.

## Final integrated candidate — 2026-10-04

## Current integration result — 2026-10-04

READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION. All eleven source handoffs are finished, all selected source is integrated, and no sessions remain active. The paired integration branches contain one source/image-bound owner-local candidate. Integrated physical/endurance qualification is NOT_RUN and public distribution remains blocked. The repeated boundary audit and roadmap precede this readiness change; no main merge, push, flash or owner-tree/ref/index change.

Compiled Linux `4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2` / Reborn `dd73dcc3243045cd33e319dda2f76918ed37ea31`. Candidate: `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Linux/out/y2linux-platform-v1-integration-candidate`. BOOTIMG `d2dec1a517a596861adb69b4c9aaab51e68d5caf46712a99dbd8607e9d8fbb06`; Y2ROOT `cd3c077fd6c4882c82b7c67c42266f5f0ddc04828ddc2af111434740153bd1dc`. Exact next owner action: SPFT Download Only with the candidate's MT6582_preserve_data_scatter.txt, select BOOTIMG.img and Y2ROOT.img only; leave USRDATA and all other partitions unselected. Retain the separate matching UART01 fallback. Then review exact source/boot/taint and use one A–J campaign.

All selected source dispositions are ACCEPT_WITH_INTEGRATION_ADJUSTMENT. All11sessions are finished source handoffs; none is promoted to integrated hardware qualification. Full source/data/contract/commit/validation evidence is retained above. Historical source/candidate states are superseded for current software readiness by the final seal, never for their actual hardware scope.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
