---
title: "Luna stabilization review — source findings - Innioasis Updater"
description: "Luna stabilization review — source findings Historical review scope, 2026-09-22. This review found specific software defects at the revisions it inspected. See the later"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-review-luna_stabilization_review.html"
---

# Luna stabilization review — source findings - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Luna stabilization review — source findings

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Luna stabilization review — source findings

Historical review scope, 2026-09-22. This review found specific software defects at the revisions it inspected. See the [later correctness closure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FLUNA-CORRECTNESS-CLOSURE-01.md) and [current application state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FCURRENT_REBORN_STATE.md) before interpreting remaining-work or release statements as current.

2026-09-22. Companion to [CURRENT_PROJECT_STATE.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Freview%2FCURRENT_PROJECT_STATE.md), which contains the complete project overview, dependency assessment and test-failure classification. No implementation changes, builds, device access or flashing were performed by this review.

Scope: Reborn `011884b7…` → `8a1443d…`; Linux `be7e64c…` → `8e5b53b…`. Source findings below distinguish a reproducible sample defect from source-traced control/error paths; they are not claimed physical reproductions.

## R1 — High: save intent and redraw state share one flag (new)

[Runtime](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs), lines 119–130, 313–314, 638–686, 1623–1673.

`checkpoint()` now clears `self.dirty`. `effect()` sets it before dispatch, so a successful setting checkpoint can clear the redraw requested by that same action. For example, changing screen timeout while stopped saves successfully but leaves no dirty frame to render until another event. Bluetooth-loss handling also checkpoints before setting its new notice.

Conversely, the regular renderer clears this same flag, and the new 15-second checkpoint condition requires it. A durable position change already rendered may not be saved at the next checkpoint; unrelated screen-off/status activity can keep triggering full saves. This is not a coherent persistence-dirty mechanism. Existing schema/size tests do not execute Runtime's save/render cadence.

F06 STILL_BROKEN; F21 PARTIAL. Separate durable-state intent from rendering intent before qualification; no framework rewrite is needed.

## R2 — High: S24 type contract produces S16 bytes (new, reproduced)

[C conversion](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-media/native/media.c), lines 200–218 and 766; [Rust conversion](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-media/src/native.rs), lines 309–327 and 850–875; [ALSA mapping](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-audio/native/audio.c), lines 102–108.

Rust format 3 has four bytes per sample and 24 valid bits. ALSA maps it to `SND_PCM_FORMAT_S24_LE`. C maps only 2 to S32 and every other value to S16, although validators now admit 3. This affects final conversion and decoder output opened directly as S24.

Read-only probe of the existing cached native library:`rb_media_convert(input, 1 frame, 48000 Hz, input_format=2, output_format=3, output, capacity_frames=1) input S32 stereo: [1073741824, -1073741824] expected S24 containers: [4194304, -4194304] returned frames: 1 actual bytes: 00 40 00 c0 00 00 00 00 actual i32 containers: [-1073725440, 0]`

The probe loaded `target/debug/build/reborn-media-ef9aa12355fbbdcd/out/libreborn_media.so`; its build timestamp follows the changed C source. No new library was compiled. The zero-only S24 test passes because zero hides both packing and written-length errors.

Wider Bluetooth readiness is PARTIAL. This does not corrupt current SBC, which uses S16. S32 maps correctly; do not describe all wider output as forced S16. Correct right-justified signed-24 packing, valid-bit semantics and nonzero/extreme/channel tests before enabling an S24 codec path.

## R3 — High: sink ordering repaired, failed reconfiguration not transactional

[Runtime load/switch/effects](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs), especially 98–117, 133–225 and 283–310; [worker stop](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/playback.rs), 1267–1278.

The old worker drops its sink before acknowledging Stop; Runtime waits before probing. The original exclusive ALSA-open ordering is therefore fixed on the successful path.

But callers first mutate model output/settings/queue/position. Once Stop succeeds, a plan error returns before generation invalidation and Buffering transition. `fail()` logs/notices without restoring the prior setting/output or changing the old Playing state to an accurate stopped/error state. The old sink is already gone. The worker's later open can fail too; no complete restoration transaction exists.

The nominal two-second stop bound starts after blocking `.send()`. The actor can also block emitting events into the UI-drained bounded event queue. A non-draining UI therefore falls outside the claimed bound. Existing fake-sink playback tests do not exercise Runtime's exclusive-device probe/reopen or this queue saturation boundary.

F02 PARTIAL. Preserve the actor; define release/plan/open/commit/failure outcomes and end-to-end cancellation deadlines.

## R4 — High: incomplete source reads can still prune valid library entries

[Scanner/database](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-library/src/lib.rs), lines 213–214, 391–437 and 442–475; [source construction](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/storage.rs), `sources`.

Batch and Finish replies propagate SQL failures. A failed transaction exits before later pruning, and a failed Finish cannot report successful scan completion. These are genuine improvements.

Two remaining traces violate the wider F05 contract:
  - An indexed file changes, then FFmpeg open fails due to transient I/O or bad/truncated content. The scanner increments failures and skips it, without clearing `complete` or marking its existing row seen. Finish marks the previously valid row deleted.
  - SD root is `/media/sd`. After unmount, that directory still exists. A scan snapshot can enumerate the empty surviving mountpoint and pass `root.is_dir()`, then mark the old SD rows deleted. Root existence does not establish mounted source identity or generation.

F05 PARTIAL. Protect retained rows using completion/source identity evidence. Existing library tests cover ordinary transactions, offline records and corrupt headers, not these scan failure boundaries or injected batch/finalization failure.

## R5 — High: corrupt-DB recovery treats operational failures as corruption (new risk)

[Database startup](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-library/src/lib.rs), lines 164–203.

Apart from a string-matched future-schema error, any `open()`/setup failure with an existing pathname triggers DB, WAL and SHM renames followed by recreation. Busy/read-only/full/I/O conditions are not equivalent to a corrupt database. A successfully quarantined healthy database is retained as a backup, but the application can start against a fresh database and lose its active state/ID relationship.

The three renames have no multi-file recovery protocol; failure midway leaves split locations. A version-compatible DB can also open despite damage found only by later queries. The one garbage-header test establishes neither operational-error handling nor general corruption recovery.

F07 PARTIAL. Require a classified recovery reason and a recoverable DB/WAL operation; distinguish retryable startup failure, quarantine and deliberate rebuild.

## R6 — Medium/high: crossfade prefix still lost on input-window error

[Playback](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/playback.rs), `read_window` at 279–310; transition at 671–857.

`read_window` accumulates decoded blocks, then uses `?` for the next read. If a later read errors, its local accumulated bytes are discarded while the next decoder has advanced. The caller's error fallback flushes only the old tail and then continues that advanced decoder. Thus beginning-of-next-track loss remains on this boundary.

The separate mix-error fallback now correctly emits old suffix plus consumed next prefix. Chunking in `send_stream` removes the sink block-size rejection: stereo S32 5/10/15-s windows at 44.1 kHz fit into 4/7/11 chunks respectively. This arithmetic is not duration/timing qualification. Whole-window tail/head/mix/filter/copy allocations still scale with duration. Existing playback tests use 50-ms crossfade and do not inject either error boundary.

Boundary markers are emitted after the overlap (or restored next prefix), so exact next-track position/metadata presentation also needs an explicit contract and observation.

F04 PARTIAL. Retain/replay successfully consumed input on every recoverable failure and measure the advertised windows.

## R7 — Medium: filtered single-track context actions enqueue a collection (new)

[UI context dispatch](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-ui/src/lib.rs), lines 1080–1117.

The menu identifies a selected `track_index`, but Play Next/Add to Queue ignores it whenever `navigation.filter` is nonempty. Long-pressing one track within an album, artist or folder consequently inserts every filtered member. The dedicated collection menu already has its own action; a filter is not evidence that this was a collection-wide request.

Queue-entry IDs otherwise repair duplicate-track boundary selection. Runtime rebuilds the worker snapshot on successful active mutations; a copied execution snapshot is not intrinsically a second authority. However, track/ID parallel vectors, restart-on-edit and incomplete rollback retain fragility. Shuffle toggles do not reshuffle an existing future queue; repeat-one/all restart at the wrap boundary. Album-artist/title grouping improves, while empty metadata and compilation ordering still need explicit semantics.

F03/F08 PARTIAL. Test actual context requests and live queue playback, not just the model's duplicate-ID helper.

## R8 — Medium: input loss becomes ordinary user actions (new)

[Input manager/router](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/input.rs), lines 137–203 and 377–393.

`SYN_DROPPED` and descriptor-loss recovery synthesize `Release` for pressed controls. Release is an activation event in ActionRouter: Select activates, Next/Previous skip and Power toggles the display. Losing input state can therefore cause an unintended action. The new test checks that release is emitted rather than checking that activation is cancelled.

Polling releases before aging is useful but not a complete backlog fix: only a bounded read is consumed, kernel event timestamps are discarded, and SYN_DROPPED does not discard through SYN_REPORT/reconcile actual key state. Device reopen also reuses the old path rather than rediscovering a replacement node.

F20 PARTIAL. Cancellation/resynchronization must differ from confirmed button release.

## R9 — Medium: artwork event ordering and transport identity are not authoritative

[Artwork producer/boundaries](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/playback.rs), lines 390–446, 848–857 and 1043 onward; [artwork consumer](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs), 1185–1199.

The decoder enqueues an audio Boundary, then directly sends Artwork on a different channel. The sink may still be playing queued old-track PCM; Artwork reaches Runtime first, fails its current-track check and is discarded permanently. Equal library IDs for duplicated queue entries can instead pass the check early. Cache-hit rewrite avoidance is correct, but track ID is not queue-entry ID and producer order across channels does not establish presentation order. F24 PARTIAL.

[Bluetooth observation](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/bluetooth.rs), 116–120 and 160–192; [ALSA sink planning](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-audio/src/native.rs), `plan_bluetooth`.

Rate/Format/Channels and device/transport/mode selection match BlueALSA 5's shipped PCM1 documentation. But `transport_generation` is solely a hash of object path, so restart/reconnect/property changes at that path retain the same value; it is not asserted at actual open/write. The installed `usr/share/alsa/alsa.conf.d/20-bluealsa.conf` defines `pcm.bluealsa` as `type plug` over a BlueALSA slave. Cached negotiation can therefore be converted silently rather than rejected. Typed negotiation is a foundation, not complete transport authority.

## R10 — Medium: receipt/test claims overstate the qualified boundary
  - [Static FFmpeg label](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-media/src/native.rs), line 274, still says 9.0.1. [ARM QEMU checker](https://github.com/SchulzCode/Y2Reborn/blob/main/tools/build/qemu-check.py), lines 21–22, requires 9.0.1 and `.1.101`; actual target is 9.0.2 / `.1.102`. Generated-config validation does not execute that runtime assertion. This is a current verification regression/obsolete assertion, distinct from the 43 historical-sweep results.
  - [Package metadata](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/package.py) still describes `Y2PlayerNative` as unimplemented; [validator](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/validate.py) enforces the obsolete application fields. Aligned Git/build IDs do not close F14.
  - [FFmpeg adapter](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/ffmpeg9.py), lines 16–20, requires a cached source archive before normal Buildroot acquisition. A fresh output build with supplied caches is not a demonstrated fresh-machine/repeatable-input build.
  - The retained final workspace run at 17:45:26 UTC reports 91 passes. Independent cached reruns passed 45 tests. The retained broad sweep at 17:42:09 UTC really returned 1 failure/42 errors; the primary document accounts for all 43 by inspected root cause. Neither count closes missing failure-boundary tests.

The historical failing invocation was unrestricted `unittest discover -s tests -p "test_*.py"` inside the locked build shell, with `PYTHONPATH=/project` and `Y2_ARTIFACT_TEST_ROOT=/build`. Representative source anchors are Linux [artifact tests](https://github.com/SchulzCode/Y2Linux/blob/main/tests/test_artifacts.py), [baseline policy tests](https://github.com/SchulzCode/Y2Linux/blob/main/tests/test_baseline.py), [PID1 fixture](https://github.com/SchulzCode/Y2Linux/blob/main/tests/fixtures/pid1_syscalls.c), [evdev fixture](https://github.com/SchulzCode/Y2Linux/blob/main/tests/fixtures/evdev.c) and [relay fixture](https://github.com/SchulzCode/Y2Linux/blob/main/tests/fixtures/relay.c). The production runner's host include setup is in [tests.sh](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/tests.sh).

## Improvements independently supported
  - F01: frame-shell ownership repaired on success/error/zero-output paths; packet/frame/decoder cleanup and seek resets inspected. Endurance qualification remains open.
  - F09: actual file-extension discovery now reaches AIFF/APE/WavPack decoders present in the ARM configuration.
  - F11/F12: seek-prefix trimming, finite/ranged ReplayGain parsing and `alimiter level=0` fix concrete problems; broader audio claims remain partial.
  - Build integration: actual selected versions/hashes, BlueALSA daemon rename/shared link, PCM property adaptation and FFmpeg SONAME-vs-file-version distinction are sound. Removed BlueZ/SQLite/ALSA patches were checked against replacement source and target scope.
  - Architecture: no new competing decode, database, rendering or Bluetooth retry service was introduced. The correct next step is targeted correctness closure and qualification, not a subsystem rewrite.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
