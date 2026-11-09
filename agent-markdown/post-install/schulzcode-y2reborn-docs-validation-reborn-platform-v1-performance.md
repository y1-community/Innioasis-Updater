---
title: "Reborn Platform 1.0 performance and responsiveness - Innioasis Updater"
description: "Reborn Platform 1.0 performance and responsiveness 2026-10-04. Source and validation are isolated on codex/platform-v1-reborn-performance . Product UI v2 is preserved. No"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-platform-v1-performance.html"
---

# Reborn Platform 1.0 performance and responsiveness - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Platform 1.0 performance and responsiveness

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Platform 1.0 performance and responsiveness

2026-10-04. Source and validation are isolated on `codex/platform-v1-reborn-performance`. Product UI v2 is preserved. No flash, push, production package change or main-worktree edit is performed by this pass.

The measured bottlenecks are fixed: wired partial-write churn, repeated kernel-log reads, periodic hardware observation on the UI thread, per-quad GL submission, redundant radio redraws and frame-budget drift. Playing CPU falls from 87.95% to 11.21% of one core. The four-cover cache also keeps valid entries when another cover is corrupt or missing.

## Evidence and baseline

Installed platform: Y2LINUX-BASELINE-02, Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, installed Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`. The real panel is 480x360; Mali400, GLES2 Mesa 24.0.9, EGL 1.4.

The device rebooted during an independent suspend qualification before the final matched comparison. Both final executables are therefore rerun on boot88b85fa3; earlier boot27e6d684 receipts remain historical. This pass performs no suspend trial.

Baseline executable: installed Reborn source b71b4688 plus opt-in profiling/benchmark instrumentation, with original rendering and loop behavior. Candidate source: `069415a4207c00f0a32a3a2ac00602ddea29a895`. Exact ARM executable and benchmark SHA-256 values are retained in [summary.json](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/summary.json); raw binaries, traces, captures and build logs remain in ignored `out/performance/`.

Before boot `88b85fa3-2282-4d93-b0b8-818a105ddd0a`; after boot `88b85fa3-2282-4d93-b0b8-818a105ddd0a`. Each run restores the installed service and original data and ends on its starting boot with taint 0. Physical operations hold `/tmp/y2-platform-v1-device.lock`. Temporary executables use a private bind-mounted copy of app data; SQL uses fresh private scratch.

The live input fixture uses the original three-track library and one private 40-second PCM queue entry. The separate product benchmark uses 10,000 tracks, 50 artists and 1,000 ordinary albums, plus stress collections containing all 10,000 tracks. Live input latency is not represented as a 10k-library end-to-end measurement.

Controls use synthetic records through the real supported evdev handles and actual kernel monotonic timestamps. They exclude mechanical, GPIO/wheel IRQ and debounce timing. Select/Back timestamps belong to routed release events; driver-generated releases can precede the fixture release write, so the analyzer joins the nearest fixture record and checks the routed action. KMS completion is not light reaching the panel. Handler-complete timing includes effects/I/O and is an upper bound on AppState mutation. No analog audible-response timing is claimed.

One matched run per executable, 32 frames per screen, 16 collection navigation repetitions, 17 Now Playing entries, 1,000 fast wheel steps and four process starts are retained. Small-sample p95 values are descriptive rather than confidence bounds. Production governor/guards remain in use; no benchmark CPU-frequency or radio override is applied.

Exploratory receipts with per-event evdev reopen overhead or an unavailable/rejected restored queue are excluded from control/playback acceptance. The final persistent-handle fixture verifies successful playback and zero dropped trace samples.

## Input and navigation

All values below are milliseconds, p95. AppState -> frame completion is retained separately in the JSON. Single-sample routes are marked by their count.

| Action | Samples before/after | Event -> handler before/after | Event -> KMS before/after |
| --- | --- | --- | --- |
| Ordinary wheel | 55/55 | 14.87 / 0.36 | 59.93 / 17.52 |
| Fast 1000-wheel sequence | 1000/1000 | 29.06 / 10.60 | 27.99 / 26.35 |
| Home -> Library | 1/1 | 10.45 / 0.34 | 22.80 / 12.98 |
| Library -> Albums | 16/16 | 12.53 / 0.23 | 31.48 / 17.24 |
| Albums -> Album | 16/16 | 15.33 / 0.26 | 34.21 / 17.09 |
| Album -> Albums | 16/16 | 14.65 / 0.37 | 60.01 / 17.21 |
| Albums -> Library | 16/16 | 21.24 / 0.26 | 67.57 / 17.18 |
| Library -> Artists | 16/16 | 46.01 / 0.32 | 60.95 / 23.45 |
| Artists -> Artist | 16/16 | 26.63 / 0.27 | 33.18 / 18.05 |
| Artist -> Artists | 16/16 | 15.22 / 0.25 | 53.81 / 25.63 |
| Artists -> Library | 16/16 | 15.76 / 0.32 | 62.07 / 16.62 |
| Library -> Tracks | 1/1 | 12.52 / 0.21 | 29.58 / 4.17 |
| Home -> Now Playing | 17/17 | 31.44 / 0.30 | 77.61 / 17.15 |
| Now Playing -> Home | 17/17 | 15.26 / 0.25 | 65.54 / 18.15 |
| Home -> Queue | 1/1 | 10.16 / 0.24 | 28.65 / 12.56 |
| Queue -> Home | 1/1 | 7.38 / 0.17 | 23.40 / 3.57 |
| Home -> Settings | 1/1 | 10.40 / 0.23 | 28.56 / 17.96 |
| Play/Pause | 2/2 | 17.50 / 19.69 | 21.75 / 42.47 |
| Volume up while playing | 16/16 | 25.27 / 15.11 | 50.28 / 33.13 |
| Volume down while playing | 16/16 | 26.73 / 10.94 | 51.76 / 24.91 |
| Screen wake | 1/1 | 42.44 / 39.27 | 57.31 / 53.84 |

The two Play/Pause events above are insufficient to establish a regression. A separate matched replay on the same boot varies frame phase, waits for native playback, and records 16 resume and 16 pause events per executable. Both executables use the same private queue and original Now Playing screen; SQL/GPU/idle fixtures are skipped. [The supplemental receipt](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/play-pause.json) retains all samples and zero trace drops/XRUNs/playback errors.

| Repeated control | Samples per side | Handler p95 before/after | KMS p95 before/after |
| --- | --- | --- | --- |
| Resume | 16 | 24.68 / 15.63 | 43.98 / 22.55 |
| Pause | 16 | 39.84 / 17.22 | 64.70 / 38.50 |

The fast sequence routes all 1,000 single steps in both runs, with zero selection mismatches or non-single steps. Direction alternates to exercise one-detent semantics without triggering intentional acceleration; acceleration/duplicate suppression code is unchanged and its existing tests pass. 801 / 641 steps are superseded before an individual frame. KMS latency for that sequence describes only unsuperseded frames and must not hide the handler tail; all-action p99/max values remain in the JSON.

Volume updates reach the live sink gain control before handler completion; persistence remains synchronous and measured. Playback state and ALSA parameters are retained in the final receipt. Audible timing, peer Bluetooth audio and physical long-press ergonomics require separate observation.

## Frame and rendering cost

32 complete frames per screen on real KMS. Values are p95 ms. Submission ends before swap/KMS waiting; CPU is thread CPU time across submission and presentation.

| Screen | Layout before/after | GL submit before/after | Render CPU before/after | Present before/after |
| --- | --- | --- | --- | --- |
| home | 0.19 / 0.20 | 7.97 / 1.26 | 9.77 / 1.84 | 12.32 / 14.62 |
| music | 0.13 / 0.15 | 4.06 / 1.20 | 5.22 / 1.82 | 13.19 / 14.38 |
| artists | 0.12 / 0.15 | 5.12 / 1.13 | 6.57 / 1.65 | 12.15 / 14.54 |
| albums | 0.18 / 0.28 | 7.49 / 1.20 | 9.94 / 1.76 | 12.02 / 14.66 |
| tracks | 0.19 / 0.25 | 6.14 / 1.33 | 7.58 / 1.96 | 11.78 / 14.49 |
| artist | 0.25 / 0.22 | 7.05 / 1.95 | 6.91 / 2.68 | 12.08 / 13.86 |
| album | 0.22 / 0.21 | 6.42 / 1.60 | 8.20 / 2.24 | 12.22 / 14.22 |
| now_playing | 0.12 / 0.18 | 3.89 / 2.07 | 5.09 / 2.82 | 11.90 / 13.92 |
| queue | 0.23 / 0.26 | 7.73 / 1.39 | 9.85 / 2.07 | 11.53 / 14.42 |
| settings | 0.21 / 0.24 | 4.88 / 1.23 | 6.36 / 1.86 | 12.43 / 14.41 |

Present waiting can increase when CPU submission finishes earlier. The change reduces CPU work; it does not claim a faster panel refresh or bypass vblank. The live complete-frame p50 is 15.97 -> 11.12 ms, p95 18.79 -> 17.26 ms.

Home keeps all 147 quads and reduces draw calls from 147 to 9. Batching preserves adjacent texture order and uses exactly 49,152 bytes of fixed staging storage.

Cold catalog cost is retained separately from warm layout. First Albums layout is 26.66 -> 29.80 ms; first Tracks 15.77 -> 20.61 ms. Catalog algorithms are unchanged; these single cold samples are not optimization claims.

| Stress destination | Tracks | Select -> complete layout p95 | Render CPU p95 |
| --- | --- | --- | --- |
| artist | 10000 | 7.09 | 1.51 |
| album | 10000 | 34.36 | 2.79 |

Both stress fixtures verify Select and Back. They measure UI/renderer work on the device, not evdev-to-photon latency. No before/after claim is made for these newly added stress cases.

The single-album 10k-track extreme still spends 34.36 ms in Select plus complete layout. This pass retains that measured limit rather than introducing an unmeasured collection-cache rewrite; normal 10k-library album fixtures contain ten tracks per album.

Ten complete RGBA screen captures differ in 600 of 6912000 channels (0.0087%). Maximum difference is 5/255; 47 channels differ by more than one step. The changed pixels are small antialiased edges; this is bounded near-equivalence rather than bit-identical rendering. Layout, assets, text, colors and draw order are preserved. These captures use the benchmark UI without live cover content. Capture/readback is qualification-only and outside timed frame samples; normal rendering uses neither readback nor glFinish.

## Artwork and allocations

JPEG/PNG/WebP and the fourth cover each decode to 160x160 RGBA (102,400 bytes). Four valid entries bound cache payload to 409,600 bytes, plus transient reply/decoder storage. GPU textures keep their existing lifetime. The sequence deliberately changes covers and uploads each changed route; unchanged selections are suppressed and cannot repeatedly decode/upload on static frames.

| Artwork measure | Before | After |
| --- | --- | --- |
| First four decodes, range ms | 6.64–30.05 | 6.09–9.25 |
| JPEG after corrupt/missing requests | 6.24 ms; cache miss | 0.10 ms; cache hit |
| Maximum upload ms | 0.68 | 0.64 |

Malformed and missing covers return no pixels and cause no upload. The final fixture asserts all eight expected warm hits, preservation of the four valid entries after failed covers, and suppression of all 14 unchanged route repeats.

| Calling-thread Rust allocation window | Mean calls | Mean allocated bytes |
| --- | --- | --- |
| 1000_scrolled_frame_layouts | 65.08 | 58903.26 |
| 1000_wheel_actions | 4.00 | 74.00 |

Per-screen cold and warm layout counts remain in the JSON. Counts include allocations/reallocations on the calling Rust thread, exclude C/GL allocations and describe cumulative bytes rather than retained heap. Only reborn-bench installs the counting allocator. Normal Reborn retains its existing allocator. Warm layout cost is small enough that draw-list/glyph/string pooling is rejected; eliminating needless idle frames is more useful.

## Startup

Elapsed from Rust run entry unless marked external exec. Four warm application starts per executable; nearest-rank p50/p95 are ms. These are not new cold-boot trials.

| Boundary | Before p50 / p95 | After p50 / p95 |
| --- | --- | --- |
| graphics_ready | 134.00 / 138.00 | 132.00 / 134.00 |
| storage_ready | 146.00 / 150.00 | 144.00 / 146.00 |
| database_ready | 152.00 / 156.00 | 150.00 / 151.00 |
| library_workers_ready | 152.00 / 156.00 | 150.00 / 152.00 |
| core_services_ready | 160.00 / 164.00 | 158.00 / 159.00 |
| audio_ready | 160.00 / 165.00 | 158.00 / 160.00 |
| radio_workers_ready | 161.00 / 166.00 | 159.00 / 161.00 |
| runtime_ready | 166.00 / 172.00 | 164.00 / 165.00 |
| ready | 189.00 / 210.00 | 176.00 / 185.00 |
| library_ready | 247.00 / 255.00 | 271.00 / 303.00 |
| interactive | 759.00 / 779.00 | 493.00 / 499.00 |
| exec_to_first_KMS_completion | 213.14 / 228.74 | 197.43 / 210.28 |

The previously retained Baseline02 boot27e6d684 log reports first application frame at 446 ms from run entry and application-ready at 41.343 s after kernel boot. That observation is preserved separately; no improved cold-boot claim is made. The boot cover uses the same Product v2 frame count and handoff. Correcting start-to-start frame pacing removes the accidental extra delay before first interactivity.

Platform/radio workers start asynchronously. Selected screens do not require an initial platform-client snapshot; the first successful snapshot now logs platform_ready when actually requested. No startup connection-time comparison is invented, and the UI does not wait for that lazy API operation.

## CPU, idle and blocking I/O

CPU percentages are of one core; context switches include scheduling/I/O and are not exact timer wake counts. Paused states use 10-second windows; playing uses five seconds. The optional one-second audio syscall profile runs afterward, outside these measurements.

| State | Frames before/after | CPU % before/after | Switches/s before/after |
| --- | --- | --- | --- |
| home_static_paused | 14.0 / 0.0 | 4.96 / 1.88 | 133.44 / 47.23 |
| now_playing_paused | 14.0 / 0.0 | 5.35 / 2.67 | 133.65 / 48.90 |
| playing | 12.0 / 5.0 | 87.95 / 11.21 | 350.42 / 296.50 |
| settings_menu_idle | 14.0 / 0.0 | 5.76 / 2.47 | 133.86 / 48.11 |
| screen_off_paused | 0.0 / 0.0 | 4.25 / 2.87 | 89.27 / 49.11 |

C1 entries progress in these windows; C2/C3 counts are zero under the existing connected-USB/radio guards. Qualified CPU0 C3 policy remains Enabled, budget -1, disable 0 in the restoration receipt. This pass reduces application wakeups without modifying those guards or claiming electrical battery savings/full suspend.

The repeated 2,048-record kernel-log pattern takes 95–105 ms in the retained on-device read reproduction, matching periodic input stalls. The watchdog now keeps a persistent nonblocking cursor and bounded 32-error history, reading new records rather than replaying the ring. Its filtering, truncation, overrun handling and retained history have a targeted test.

Power-supply reads take 10–20 ms; native filesystem safeprobes about 5 ms per volume. [Read reproductions](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/power-sysfs-profile.json), [block probe timings](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/blkid-profile.json), and [kernel-read timings](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/kmsg-profile.json) support those boundaries. Periodic reads now use the existing watchdog and one bounded request/result slot; the UI applies replies, discards stale music-directory media results, and retains source-change/scanner/playback ownership. Shutdown-intent polling and prepare/ack paths remain on their existing control path.

The actual background observation sample p95 is 26.00 ms; this work is outside the UI event/render path. Normal worker-result service is bounded by the 50-ms main wait, while real input interrupts that wait immediately.

SQLite/library I/O already runs on its database/scanner workers. The matched baseline 10k page query p95 is 1.79 ms, artist 1.83 ms, album 1.08 ms; full library worker load is 189.86 ms. Database reopen/checkpoint timing is retained in the JSON. No schema, WAL, batching or query rewrite is introduced. The standalone uncached folder-enumeration fixture is heavier and lacks normal mounted source roots; it does not certify deep-folder navigation.

The original playing audio thread consumes 82.63% of one core; the final thread consumes 5.11%. The untimed pre-fix one-second profile records 5,959 ioctls and 4,469 clock reads. [The write-size probes](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/audio-write-profile.json) isolate the cause using the actual VolumeRamp source and normal S16/48k, 512-period, 4096-buffer wired sink: gain work allows a few new frames to become available, so repeated short writes never return EAGAIN and the loop keeps recomputing a 512-frame gain window. The probe sees over 10,600 writes/s, almost all below 64 frames, and approximately 999 ms CPU per second. A capacity wait reduces it to 131 writes and approximately 30 ms CPU; these are writer-probe results, distinct from the whole-application table above.

The final wired sink returns each accepted prefix immediately and waits on the next call, after control polling. It performs at most one configured 20-ms readiness wait per call, including ready->EAGAIN races; timeout/interruption consume no PCM, recovery and discard reset pacing, and fatal wait errors propagate. Bluetooth short-write pacing, formats, byte strides, buffers, gain/ramp and transport leases are preserved. The configured wait bound does not include unrelated scheduling time or pre-existing XRUN recovery.

Scripted fault coverage checks partial->timeout->EINTR->ready/EAGAIN->full plus wait XRUN/fatal propagation and unchanged Bluetooth positive-short behavior. Real ALSA-null tests check readiness, exact S16/S24/S32 frame counts, native recovery and discard; they do not simulate a physical hardware XRUN. Final real-device controls check resume, seek, wired, pause, resume, stop, resume, with active-playback SIGTERM exit in 317.28 ms. No hard kill is required. Exact metrics before the optional syscall observer and after controls are retained; deliberate native XRUN/peer Bluetooth/analog quality testing remains separate.

## Implemented and rejected changes
  - Adjacent same-texture quad batching in original order, with one fixed 48-KiB staging array; no new texture pool or renderer thread.
  - Dirty-only redraws for changed Wi-Fi/Bluetooth presentation and facts; authoritative radio state still updates on every event.
  - Input readiness wait on existing handles, 34-ms frame budget from frame start, 50-ms asynchronous service bound, existing 15-ms held-button cadence.
  - Powered-off Bluetooth D-Bus wait 100 ms; active/pending/scan keeps 20 ms. Signals wake immediately; off-worker power-on dispatch can take up to 100 ms. Peer behavior/power-on latency is not hardware-qualified here.
  - Incremental kernel diagnostics and off-path periodic power/storage reads on the existing watchdog; bounded channels and UI-owned transitions.
  - Wired partial-write capacity pacing, measured against real gain/native writer churn; at most one 20-ms wait per call and unchanged accepted-frame accounting.
  - Valid-cover eviction only when inserting a new valid cover; bounded cache size unchanged.
  - Opt-in bounded 8,192-sample trace, renderer CPU/submission/present/upload metrics, startup markers and repeatable product fixtures. Trace allocations/I/O are disabled in normal runs; enabled traces write once on exit.

Rejected: visual redesign; desktop frame assumptions; text/glyph/string pooling; larger cover cache; permanent screenshot synchronization; GPU/vblank/CPU-policy tuning; DB schema/query/persistence rewrites; speculative startup dependency removal. Targeted measurements favor these smaller changes. Large-queue persistence, analog audible latency, cold boot after installation, peer radios, full suspend and electrical power are separate remaining qualifications.

## Validation, files and handoff
  - cargo fmt --all -- --check: PASS.
  - cargo clippy --workspace --all-targets --locked -- -D warnings: PASS.
  - cargo test --workspace --locked: 243 passed, zero failed/ignored.
  - ARM Cortex-A7/NEON release workspace build with the installed Baseline02 Buildroot SDK: PASS; no image build/flash.
  - Host 1k/10k/20k navigation, large-collection Select/Back, allocation and cover-cache/dedup fixtures: PASS; host timings are not hardware claims.
  - Four tooling tests, 20 host-daemon checks, Python compilation, diff whitespace check: PASS.
  - Standalone ARM native/gain write probes compile; native C passes `-Wall -Wextra -Werror`, standalone Rust passes formatting. Scripted wait/race faults and real ALSA-null frame contracts are distinct from the physical no-XRUN playback proof.
  - Hardware: all requested screens, 10k SQL/UI/GPU fixture, wheel/control/playback/idle scenarios, four application starts, ten screen readbacks and graceful service/data restoration. Exact errors/counters/limitations remain in the JSON.

Local source commits are `b8c05db` (rendering/interactive loop) and `069415a4207c00f0a32a3a2ac00602ddea29a895` (wired pacing). The report/evidence and paired Linux closing audit are separate local commits; branch history records their final IDs. Linux admission is `f3de513`. Existing configured Luca author/committer and GitHub identity are preserved; no identity setting or model attribution is added.

Files changed in Reborn:
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

Y2Linux changes only its standing admission/closing gap audit and roadmap: `docs/planning/roadmap-gap-audit.md` and `docs/planning/platform-v1-roadmap.md`. Its source, memory map, packages, installed image and policy are unchanged by this pass.

## Platform 1.0 verdict

PASS for the measured Product v2 application responsiveness and wired-playing CPU scenarios. Preserve the explicit limits above; this is a scoped application performance result rather than full-platform, analog/power/endurance or release acceptance. Existing epics remain open. The next boundary is integration of the independent platform branches, including source-epoch/prepare handling, followed by the relevant combined qualification; no deployment/push is authorized by this report.

During integration, preserve the storage owner's fresh FD/source admission when applying cached observations and invalidate inflight observations across source epochs/suspend prepare. Reconcile the local Bluetooth timeout change with its owner's event worker; that superseded hunk should give way to the event worker, with combined idle/control behavior remeasured. The independent full-resume failure remains a release gate.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
