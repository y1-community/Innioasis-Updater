---
title: "Reborn application audit - Innioasis Updater"
description: "Reborn application audit <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-04_reborn_audit.html"
---

# Reborn application audit - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn application audit

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn application audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## Architecture judgment

The existing architecture is worth retaining. Core/UI/runtime forbid unsafe Rust; native contexts are behind purpose-specific C boundaries with Rust lifetime wrappers. The database has one owner, rendering is on one thread, and audio decoding is not performed in draw functions. Typed `Action`, `Effect` and service events are more useful here than introducing a new state-management framework. IMPLEMENTED / HIGH, with several meaningful host tests.

It is not a perfectly pure reducer system. [Ui::action](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-ui/src/lib.rs) mutates navigation/AppModel and returns effects; [Runtime::effect](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs) performs model transitions as well as dispatch. That is acceptable if ownership remains explicit. The actual problem is where state has two operational authorities, most notably the playback queue (F03), or where an effect does device work synchronously before the worker relinquishes ownership (F02). Fix these contracts before stylistic decomposition.

## Repository and module quality

The non-vendored application is approximately 16k source lines. The largest modules include `main.rs` (~1.5k), `playback.rs` (~1.5k), UI screens (~1.6k), UI interaction (~1.4k), and native media (~1.2k). Size alone does not justify a refactor. Files deserving focused ownership review are:````````````

| Module | Concrete reason |
| --- | --- |
| app/reborn/src/main.rs | Owns presentation dispatch, playback planning, queue mutation, persistence cadence, source detection, radio projections and control requests. Several operations can block the UI loop. |
| app/reborn/src/playback.rs | Decoder preparation, transition-window buffering, artwork caching, PCM transport, sink lifecycle and state reporting are interleaved. Queue/artwork/transition contracts are not explicit enough. |
| crates/reborn-media/native/media.c | Highest-risk lifetime/precision seam; frame ownership defect and implicit filter conversions. |
| crates/reborn-library/src/lib.rs | Sound single-writer design, but dense worker dispatch makes error acknowledgement and scan commit semantics difficult to audit. |
| crates/reborn-ui/src/lib.rs + screens.rs | Interaction/draw separation is useful, but both derive collection identity independently and can disagree with runtime playback. |

There is no reason to replace bounded channels with a general async runtime, introduce a message broker, or split this player into many processes. Narrow extraction of a lifecycle/queue contract after tests would be justified; a repository-wide architecture rewrite would not.

## Playback and queue state: F02/F03/F08

WEAK / HIGH. The [runtime](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs), `load` at approximately line 107, plans ALSA before `Playback::load_with_gapless` stops the existing job. Normal seek/volume/RG/EQ paths call `load`. The underlying planner opens the actual PCM. An exclusive hardware PCM may reject this with EBUSY; no physical reproduction is claimed. Even when it succeeds, controls reconstruct decoding and discard queued audio. See [audio details](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F05_AUDIO_AUDIT.md).

`load` copies upcoming `Track`s; the decode worker makes its own track vector. Play Next/Add/Remove/Move/Clear subsequently change AppModel and checkpoint but do not revise that vector. Generation cancellation is good at invalidating jobs; it does not solve mutations inside a still-current generation. A removed track can still be played; a requested next track can be absent from the worker's list.

Further deterministic semantic defects:
  - `AppModel::apply(TrackBoundary)` uses the first `.position(track.id == id)` then requires that position be after the current index. A repeated library track in the queue does not have a unique queue-entry identity, so a later occurrence can fail to advance the visible current index.
  - Repeat-one is handled in `Runtime::finish_track`, but a gapless worker emits final TrackEnded only after traversing its preloaded queue. It does not repeat the chosen track at each boundary.
  - `Ui::play_first_filtered`/`play_track` reduce a collection to a global track index and discard the filter when navigating. `Runtime::play_index` builds the entire loaded library queue. “Play Album” therefore does not mean play only that album. Collection Add/Play Next selects only the first matching track.
  - Shuffle toggling changes a setting, not an already-running queue; repeatable seeding gives the same order for the same starting selection. Reproducibility is not inherently wrong, but the UX and live-queue behavior need a declared contract.
  - Clicking a queue entry resolves it back into the library rather than using an unambiguous queue-entry command. Offline/stale rows and duplicates require explicit handling.

TARGET: one authoritative ordered queue with stable entry IDs; the worker receives a versioned schedule and reports entry boundaries. GAP: runtime edits are not reconciled with the worker, and collection context is not carried into play effects. This is a small set of contracts, not a mandate for event sourcing.

## Library/scanner/database: G06/F05/F07/F09/F23

Good: [library code](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-library/src/lib.rs) has a single SQLite connection worker, channel bound 32, two-second busy timeout, WAL/NORMAL, foreign keys, transactional batches of 64 and source+path uniqueness. UPSERT preserves a track ID across metadata rescans. Source identity uses SD filesystem UUID via the platform adapter, not a fixed `/dev/mmcblkN` index. Offline records can be retained and restored. Tests exercise source-offline and reinsert behavior. Keep this structure.

F05 — scan completion is not a commit guarantee (WEAK / HIGH).`DbCommand::Batch` and `Finish` have no result reply. The worker logs their errors and continues. The scanner enqueues a later `Test` as a FIFO barrier; this establishes ordering, not success of previous writes. A transient failed batch followed by a successful `Finish` can mark old rows deleted because their `seen` epoch was never updated. A later `quick_check`/rolled-back write test can pass despite the earlier loss. Persistent ENOSPC may also make the final test fail; the exact bug is loss of transaction-result causality, not that every full disk falsely passes.

`complete &= source.root.is_dir()` cannot establish that the same mounted filesystem survived the scan. File decode errors are counted and skipped, but do not necessarily make traversal incomplete. A transient read/storage failure can thus be interpreted as removed content. The target is per-scan write acknowledgement and pruning conditional on complete traversal and successful persistence, with the source's mount identity checked.

F07 — corruption recovery MISSING / HIGH. Database-open/schema errors fail startup; the supervisor can restart the same failure. There is no quarantine/restore/rebuild workflow for a corrupt DB. `Effect::RebuildLibrary` invokes the normal incremental scanner; it neither recreates a corrupt database nor forces reparsing of unchanged metadata. “Rebuild” is therefore not a repair operation. Future schema versions are correctly rejected, but only schema creation/version 1 migration currently exists.

F09 — format surface PARTIAL / HIGH.`supported()` accepts flac/mp3/aac/m4a/ogg/opus/wav only. AIFF/APE/WavPack are decoded by FFmpeg tests but are absent from ordinary discovery. This is not a missing decoder. Add the right classification to user-facing support lists before claiming complete format support.

F23 — 10k/20k scale UNKNOWN, >20k UI PARTIAL / HIGH. SQLite's basic schema is reasonable for these sizes. However, runtime requests one `limit:20000` page; no browsing pagination follows. The scanner materializes up to 250k existing tracks per source into a map. UI actions clone the loaded library, then build/filter/sort collection rows in memory. Queue setup copies Track metadata again. Rendering a four-row viewport is not data virtualization. No retained physical benchmark proves acceptable navigation/RAM at 20k. The target is bounded query-backed views and lightweight track/queue references where measurements justify them—not sharding SQLite.

Incremental scans avoid most repeated decoding via size/mtime, but still upsert reused metadata and `seen` each boot. The DB worker executes `count(*)` after commands for a metric. Scanner metadata opens the full decoder/filter setup. These are meaningful CPU/write candidates for measurement. No content-hash rename tracking is present; a rename creates a new path identity, a reasonable alpha limitation if queues handle disappearance correctly.

Albums are grouped by album title in `Ui::catalog_rows`, while the DB index includes album artist. Same-titled albums by different artists collapse in the UI. Empty names shown as “Unknown” are then compared with the literal underlying field, another identity/display-label mismatch. Keep identity separate from labels.

## Persistence and sudden power loss: G09/F06

`AppModel::checkpoint` serializes queue/current index/position/output/settings and runtime state; library track rows and navigation are skipped. `restore` checks queue count/index, limits input to 8 MiB, clamps several settings and intentionally restores playback paused. Volume, RG mode, EQ configuration, crossfade, gapless, shuffle/repeat, screen timeout and output persist; Wi-Fi/BlueZ persistence is owned by their platform services. The library persists separately in SQLite.

The [atomic write primitive](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-core/src/lib.rs), `atomic_write`, uses mode 0600, writes/syncs a temporary file, renames and syncs the parent. VERIFIED host/source / HIGH, and worth retaining. This is not electrical power-cut qualification of eMMC caches/filesystem behavior.

F06 — WEAK / HIGH: main's unconditional 15-second checkpoint rewrites the full queue even when idle, with additional synchronous writes for controls. At 1 MiB per saved state this is about 5.6 GiB/day of logical data before filesystem/device write amplification; this is a conditional calculation, not measured NAND wear. Twenty thousand metadata-rich queue records can exceed restore's 8-MiB cap; checkpoint has no matching cap. `restore(...).unwrap_or_default()` silently replaces malformed/oversized/incompatible state with defaults and gives no explanation to the user. There is no explicit versioned state envelope/migration or retained last-good copy.

TARGET: preserve the atomic primitive, serialize only durable state, save only meaningful changes with a bounded position cadence, enforce matching write/read bounds, and expose recovery. GAP: cadence, size and evolution are not coherent. Do not increase sync frequency to compensate for this; test power loss and define the acceptable resume-position loss window.

## Artwork and metadata: F24

FFmpeg handles ID3/Vorbis/FLAC/MP4 metadata, with bounded strings exposed to Rust. Embedded JPEG/PNG/WebP and selected local sidecars use the same media boundary; images become one 160×160 RGBA texture (102,400 bytes). The disk cache is capped around 64 entries (~6.25 MiB payload). Source image pixel/allocation/file limits exist. These are sensible embedded constraints.

Weaknesses in [publish_artwork](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/playback.rs): a cache hit is atomically rewritten/fsynced; external-cover changes are not in the track-ID/size/mtime cache key; preopening the next decoder publishes its artwork under the current generation before the track boundary. The event has no track-entry identity, so next-track art may replace current-track art early. Failed artwork leaves no per-track negative-cache strategy. The 16-Mpixel ceiling permits appreciable temporary decode memory; the 32-MiB `av_max_alloc` limit is per allocation, not a total process cap. Bound total memory by measurement with malformed/large artwork, not by the small final texture alone.

## Error handling and lifecycle review

Searching `unwrap`/`expect` mostly finds tests, build scripts and fixed-length slices guarded by input sizes. It would be misleading to characterize this as widespread panic-driven runtime code. Native errors generally become Results/events. There are nevertheless consequential silent/error-ordering paths: DB write replies absent; restore defaults without a warning; ignored mount/unmount results; cache errors discarded; radio/control sends sometimes ignored; source state mutated before a failed effect is rolled back.

Channels are bounded (decode 4, sink 8, PCM 8, playback events 64). Position updates may be dropped; terminal events use a blocking send. This is a sensible basic tradeoff, but a stalled UI or shutdown that stops draining events can stall producers. Playback shutdown has a two-second sink acknowledgement, not joined completion of every worker. Do not claim race/deadlock freedom from current fake-sink tests. Test rapid commands, full channels, blocked media reads, service death and shutdown together.

## Resources/performance/battery: F01/F23/F28

Ordinary PCM blocks are 2048 stereo frames; eight queued blocks are about 372 ms at 44.1 kHz, plus ALSA's ~93-ms configured buffer. That is bounded and modest. Crossfade is a separate large-window case, and the AVFrame leak defeats long-duration bounds. See [audio](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F05_AUDIO_AUDIT.md).

There are dedicated workers for decode, audio, database, scanner, Wi-Fi, Bluetooth, control, logging, diagnostics and monitoring. This is not inherently excessive on four Cortex-A7 cores, but thread stacks and idle wakeups need measurement. Main sleeps 15 ms; Bluetooth D-Bus processing uses a 20-ms interval; other workers use bounded polling/timeouts. Static dirty rendering avoids a continuous animation loop, but recurring status events can still make it dirty. Do not assume “no animation” means no CPU wakeups.

The codec contexts explicitly request one decode thread, but filter graphs do not explicitly constrain their `nb_threads`; FFmpeg's automatically selected filter execution resources must be included in a target thread/memory inventory. Do not assume the Rust worker count is the whole process thread count.

No reliable current-product Y2 measurements were found for idle RAM/CPU, UI navigation at 20k tracks, 16/44.1 playback, 24/96 decoding/downsampling, EQ, scanning, artwork or SBC encode cost. The earlier GPU check's CPU/RSS is not Reborn performance. Measure those workloads after correctness fixes before introducing batching/caches/threads as speculative optimizations.

## Observability: G10/F25

[Observer](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-observability/src/lib.rs) and [control server](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-control/src/lib.rs) are useful, not gratuitous infrastructure: bounded event ring, bounded asynchronous log queue, rotation, fixed metric names, rate-limited bounded diagnostic bundles, health states and correlation IDs. Keep the local enumerated `rebornctl` interface. It can materially shorten physical-device debugging.

The limits do not make every value trustworthy. `ffmpeg_packets_decoded` is increased by the decoder's cumulative packet counter on each block, overcounting. Metadata captured at open cannot report later corruption/skip totals accurately without refresh. Health “OK”/scan completion cannot overrule the DB acknowledgement defect. Logs and snapshots have different privacy policies; media/network labels may remain visible in local control output. Correct semantics, not more metrics, is the next step. Persistent logging is bounded, while session checkpoint/cache rewrite behavior is the more obvious flash-wear concern.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
