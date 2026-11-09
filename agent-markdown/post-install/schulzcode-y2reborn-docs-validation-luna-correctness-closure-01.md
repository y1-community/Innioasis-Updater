---
title: "Luna correctness closure 01 - Innioasis Updater"
description: "Luna correctness closure 01 <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-luna-correctness-closure-01.html"
---

# Luna correctness closure 01 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Luna correctness closure 01

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Luna correctness closure 01 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Started: 2026-09-22. Final candidate evidence updated: 2026-09-23. This is a software-only closure record for the finite findings in the latest independent review. No physical Y2 was accessed, paired, configured, flashed, or tested. This record distinguishes host/source evidence from physical qualification.

## Starting state and boundary``````````````

| Repository | Starting HEAD | Starting worktree |
| --- | --- | --- |
| Y2Linux | 8e5b53bc9fb934e1f668b9e7e9e34f0fc5e4130e | clean; main ahead 29 |
| Y2Reborn | 8a1443daa25419834c800a7f9d707e66f80e0f90 | main ahead 37; pre-existing untracked docs/audit/, docs/review/, and docs/architecture/bluetooth-codecs.md preserved |

Y2Linux roadmap boundary audit: commit `8c485b6`. It records the retained GPU-01, CONNECTIVITY-10, and M4 evidence limits, current open platform issues, and that this work neither closes a platform milestone nor authorizes hardware activity. The architecture and hardware exclusions in the request remain in force. No candidate exists yet.

## R1 — render and persistence intent

Status: FIXED
  - Finding and symptom: Runtime used one `dirty` boolean for frame redraw

and session persistence. A render could suppress a position checkpoint; a save could suppress the redraw requested by a setting or service notice.
  - Current source confirmation:`Runtime` previously cleared the same flag

after `model.checkpoint()` and after drawing; its 15-second save condition also depended on that flag.
  - Implementation: Split runtime dirtiness into `render` and `persistence`

state. Draw success clears only `render`; checkpoint success clears only `persistence`; checkpoint failure retains persistence intent. Position and queue-boundary changes request persistence, which is serviced at the existing 15-second cadence. Setting, playback, Bluetooth-loss and source changes keep their required redraw/save behavior. Removed a redundant second Bluetooth-loss checkpoint.
  - Files changed:`app/reborn/src/main.rs`.
  - Tests added: Seven runtime dirty-state tests for stopped screen-timeout

save/redraw, render-before-save, save-before-render, Bluetooth-loss notice, position cadence after rendering, unchanged state, and failed checkpoint retry intent.
  - Tests run:`cargo fmt --all -- --check`; `cargo test -p reborn --bin reborn

--locked runtime_dirty_tests` — 7 passed.
  - Result: Separate runtime intents; targeted host tests pass.
  - Commit:`f081a78` (`Separate render and persistence dirty state`).
  - Remaining limitation: This is software/runtime-state evidence. The

current candidate's physical UI and persistence behavior remain `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + fresh targeted host test.

## R2 — signed 24-bit PCM in a 32-bit container

Status: FIXED
  - Finding and symptom: Rust represented `S24_LE` as four bytes, but the C

media membrane mapped format code 3 to S16. Nonzero S32-to-S24 output was consequently corrupted; the previous zero-only test could not expose it.
  - Current source confirmation: The Rust format model already specified

24 valid bits and 32 physical bits. The ALSA C mapping selected `SND_PCM_FORMAT_S24_LE`, while FFmpeg conversion and decoder output treated code 3 as S16. ALSA documents `S24_LE` as signed 24-bit LE using the low three bytes in a 32-bit word; `S24_3LE` is a separate packed three-byte format. See the [ALSA PCM format reference](https://www.alsa-project.org/alsa-doc/alsa-lib/group___p_c_m.html) and [PCM transfer semantics](https://www.alsa-project.org/alsa-doc/alsa-lib/pcm.html).
  - Implementation: Preserve the existing model's four-byte sample/eight-

byte stereo-frame sizing and document the low-three-byte LE contract. FFmpeg converts through S32 Q31; native packing takes the signed top 24 bits, writes them into bytes 0–2, and zeros the padding byte. S24 input ignores padding, sign-extends the low 24 bits into Q31, and S24-to-S24 normalizes padding. Decoder and crossfade paths use the same packing boundary. ALSA code 3 maps to `SND_PCM_FORMAT_S24_LE`; unknown codes are rejected, and runtime format reporting checks ALSA valid/physical widths. Receipt text says `s24le-in-32` rather than claiming FFmpeg has a packed S24 sample format.
  - Files changed:`crates/reborn-core/src/lib.rs`,

`crates/reborn-media/native/media.c`, `crates/reborn-media/src/native.rs`, `crates/reborn-audio/native/audio.c`, `crates/reborn-audio/src/native.rs`.
  - Tests added: Exact S32-to-S24 bytes for zero, ±1-LSB, half-scale, maximum

positive and minimum negative values in distinct stereo channels; S24-to-S32 sign extension with ignored padding; actual decoded FLTP-to-S24 output compared sample-for-sample with S32 top bits and frame counts; S24 crossfade; ALSA valid/physical-width mapping; unsupported-format rejection; and core byte/valid-bit sizing.
  - Tests run:`cargo fmt --all -- --check`; `cargo test --locked -p

reborn-core -p reborn-media -p reborn-audio` — 32 passed, 0 failed.
  - Result: Nonzero and extreme sample packing, conversion, stereo order,

frame accounting, ALSA mapping, and fail-closed behavior pass on the host.
  - Commit:`f90f9fb` (`Fix signed 24-bit PCM container conversion`).
  - Remaining limitation: No optional Bluetooth codec was enabled. No Y2

sample playback or high-resolution wired behavior is claimed; `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + host native-library tests + local ALSA

format-width query + official ALSA documentation.

## R3 — transactional sink reconfiguration

Status: FIXED
  - Finding and symptom: Reconfiguration released the old sink, but planning

or opening the replacement could fail after callers had already changed output, queue, playback position, or DSP settings. The open command was fire-and-forget, and the release's two-second timeout began only after a blocking command-channel send.
  - Current source confirmation:`Runtime::load()` previously planned after

release but mutated `Buffering` state and submitted the replacement without waiting for the sink actor's factory result. `Playback::stop_and_wait()` used blocking `send()` before calling `recv_timeout(2s)`.
  - Implementation: Reconfiguration now runs release acknowledgement,

sink planning, and nonblocking worker-open enqueue. The sink actor has a direct one-slot open-result reply which the runtime polls while the UI loop continues. Decoder start and model persistence occur only after the open acknowledgement; a failed or timed-out open invalidates its generation and queues release. A sink-open guard refuses a second open until the prior release is acknowledged. The two-second release deadline covers retrying a full command queue and waiting for the release reply. Runtime action snapshots restore output, settings, queue, selection, and position on failure; after release starts, active playback is reported as `Error`, stale generations are invalidated, and the restored state is checkpointed. Planning/open failure never commits candidate output or settings. New audio actions are held briefly while one open result is pending.
  - Files changed:`app/reborn/src/main.rs`, `app/reborn/src/playback.rs`.
  - Tests added: Runtime tests inject plan failure after releasing a live fake

sink, verify no replacement start, and verify single sink ownership on a successful replacement. Model recovery tests cover output, queue selection, seek position, volume, ReplayGain, and EQ rollback, plus pre-release failure. Playback tests inject sink-open failure, a deliberately stalled open actor, a full command queue, a disconnected receiver, and a full event queue that stalls the actor; they assert the runtime-facing open call returns before the actor, no `TrackStarted` occurs on failure, bounded release, and recovery once the stalled queue drains. Existing output-switch coverage also verifies that the sink actor rejects a second open without release acknowledgement.
  - Tests run:`cargo fmt --all -- --check`; `cargo check -p reborn --locked`;

fresh-target `cargo test -p reborn --bin reborn --locked` — 27 passed, 0 failed after the nonblocking-open correction. The full workspace run exposed scheduler sensitivity in a 100-ms wall-clock assertion; it was replaced with a held-worker barrier that directly proves the caller returns before open completes, and the full workspace run then passed.
  - Result: Release/plan/start/commit/fail ordering is explicit and the

failure-boundary tests pass. The prior logical state is preserved where safe; failed active transitions cannot report `Playing` without a sink.
  - Commit:`72f9995` (`Make sink reconfiguration transactional`),

`9b72382` (`Keep sink-open waits off the runtime loop`), and `dde3c53` (`Make async sink test scheduler independent`).
  - Remaining limitation: Sink release acknowledgement and ALSA planning

remain synchronous on the runtime thread; release stays bounded at two seconds, including command-queue backpressure. The worker-open acknowledgement is polled without blocking the UI loop. Actual BlueALSA and wired-device timing remains `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + fake sink/worker host tests. No physical

sink was opened.

## R4 — scan identity and pruning safety

Status: FIXED
  - Finding and symptom: A changed file whose FFmpeg metadata open failed was

counted as a failure but left the per-source `complete` flag true. Finish could therefore prune the previous valid row. SD scan safety also used only `root.is_dir()`, which remains true when `/media/sd` is an empty unmounted directory or a different filesystem has reused that path.
  - Current source confirmation:`scan_sources()` continued after

`Decoder::open()` errors without clearing `complete`, and Finish pruned all rows whose `seen` token did not match. The old SD completion guard checked only directory existence.
  - Implementation: Decoder-open, metadata, traversal, and directory-entry

read failures now make the source incomplete; any such incomplete scan skips pruning. SD `Source` snapshots carry the observed mount ID in addition to the UUID-backed source ID. The scanner verifies the same mount ID at traversal boundaries and again in the database writer immediately before Finish. Traversal uses an open directory descriptor through `/proc/self/fd`, so a replaced path cannot redirect the in-flight walk to a different filesystem. Missing UUID or mount identity fails closed. Finish reports whether pruning actually occurred; batch, finish, and storage-full errors propagate without marking the scan complete.
  - Files changed:`crates/reborn-core/src/lib.rs`,

`crates/reborn-library/src/lib.rs`, `crates/reborn-platform/src/storage.rs`, `app/reborn/src/main.rs`, `app/reborn/src/bin/reborn-preview.rs`.
  - Tests added: Changed-file FFmpeg open failure retains the old row; an SD

path that is unmounted or reused with a new mount ID is rejected; mid-scan identity loss and a database-writer identity recheck disable pruning; a safe complete scan still prunes. SQLite trigger fault injection covers batch failure, finish failure, and a simulated `SQLITE_FULL`/ENOSPC message; all preserve prior rows. Mountinfo parsing preserves mount IDs and escaped paths.
  - Tests run:`cargo fmt --all -- --check`; `cargo check --workspace --locked`;

`cargo test -p reborn-library -p reborn-platform -p reborn-core --locked` — 49 passed, 0 failed.
  - Result: A scan is prune-safe only after traversal, file metadata, stable

source identity, batch persistence, and finish persistence all succeed.
  - Commit:`6e8ea74` (`Prevent unsafe library scan pruning`).
  - Remaining limitation: Unclassified decoder-open failures are treated as

unsafe even if a file is permanently corrupt; row removal waits for a later identity-consistent successful scan. `/proc/self/mountinfo` and a usable filesystem UUID are required for SD pruning. Physical media removal and card replacement remain `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + SQLite/file fault injection + host

mountinfo parser tests. No SD card or physical Y2 was accessed.

## R5 — database recovery classification

Status: FIXED
  - Finding and symptom: Startup treated nearly every SQLite open/setup error

as corruption, moved the live database first, then moved `-wal` and `-shm` independently. A future schema, lock, read-only filesystem, or full disk could detach a valid database; a sidecar rename failure could leave a split database set.
  - Current source confirmation:`Database::spawn()` previously quarantined

any non-future-schema open error, while `open()` returned untyped strings and enabled WAL before checking the schema version.
  - Implementation: SQLite failures are classified by primary/extended error

code and operation stage into corruption, future schema, busy/locked, read-only, full disk, permission, I/O, WAL/SHM, migration, or setup failures. The schema version is read before changing journal mode. Only SQLite `CORRUPT`/`NOTADB` or a failed `quick_check(10)` reaches quarantine; all operational and newer-schema cases preserve the source DB and fail startup. Corruption recovery moves the DB and existing sidecars into one evidence directory. Rename failures roll back in reverse order. An `INCOMPLETE` marker lets the next startup restore a set left mid-transaction by process interruption before attempting SQLite open.
  - Files changed:`crates/reborn-library/src/lib.rs`.
  - Tests added: Bad-header and damaged-page databases quarantine and rebuild;

future schema remains intact; locked, read-only, disk-full, permission, generic I/O, WAL/SHM, and migration failures retain their distinct class. Sidecar-set success, injected WAL/SHM rename failures with full rollback, and interrupted-quarantine recovery are exercised at the filesystem boundary.
  - Tests run:`cargo fmt --all`; `cargo test -p reborn-library --locked` —

23 passed, 0 failed. Workspace/package check follows with the host gate.
  - Result: Only genuine corruption is quarantined; newer and operational

failures preserve the existing DB, and sidecar handling has rollback plus a startup recovery path.
  - Commit:`d61e6fe` (`Classify database recovery failures safely`).
  - Remaining limitation: The startup integrity probe reads the SQLite

database and busy handling may wait up to two seconds. Host fixtures verify classification and recovery; target filesystem behavior remains `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + SQLite fault injection + temporary

filesystem tests. No Y2 storage was accessed.

## R6 — crossfade input-window recovery

Status: FIXED
  - Finding and symptom:`read_window()` consumed several next-track decoder

blocks into a local vector. If a later decoder read failed, `?` returned the error and dropped that local prefix even though the decoder had advanced.
  - Current source confirmation: The previous helper returned

`Result<Option<Pcm>, String>` and did not return accumulated PCM on error.
  - Implementation: Window failures now carry both the error and any PCM

already consumed. The transition recovery drains the old-track suffix first, then queues the consumed next-track prefix before the authoritative boundary; subsequent decoder reads continue after that prefix. The existing `send_stream()` chunking remains the sink write boundary.
  - Files changed:`app/reborn/src/playback.rs`.
  - Tests added: Injected failure before input, after the first block, after

multiple blocks, and one frame short of 5-, 10-, and 15-second windows, with sample-by-sample continuity checks. A recovery-order test verifies the old suffix precedes the new prefix, and a large partial-prefix case verifies every sink chunk stays at or below 524,288 bytes without losing samples.
  - Tests run:`cargo fmt --all`; `cargo test -p reborn --bin reborn --locked

playback::tests` — 13 passed, 0 failed.
  - Result: Every consumed input frame has an owner after a later read error;

the old suffix and next prefix remain ordered and sink writes stay bounded.
  - Commit:`48ddaaa` (`Preserve crossfade input after read errors`).
  - Memory inspection:`TailWindow`, the next-track window and the mixed PCM

can coexist, at up to three stereo S32 windows (`3 × seconds × rate × 8` bytes). The eight-slot PCM channel plus one worker and one producer chunk add at most about 5 MiB at the 524,288-byte sink-write cap. Static live-PCM estimates are about 10.0/15.1/20.1 MiB for 5/10/15 seconds at 44.1 kHz and 16.0/27.0/38.0 MiB at 96 kHz; decoder/filter allocations are additional. This is a source-based bound estimate, not target RSS measurement. The fix does not add another whole-window copy beyond the retained inputs and mix result, and chunking remains bounded.
  - Remaining limitation: Fault injection exercises the real window assembly

and stream chunker with deterministic PCM; measured target peak memory and physical 5/10/15-second playback remain `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + runtime helper fault injection + host

playback tests. No physical output was used.

## R7 — filtered single-track context actions

Status: FIXED
  - Finding and symptom: In a filtered view, context-menu Play could start the

selected track plus the rest of the filtered collection, while Play Next and Add to Queue enqueued every filter match.
  - Current source confirmation: The context handler routed Play through the

collection-aware `play_effect()` and special-cased filtered queue actions to `PlayNextCollection`/`AddToQueueCollection`.
  - Implementation: Context rows are resolved against the focused source row.

A `track:*` row exposes single-track actions; Play emits `Play(index)`, and Play Next/Add emit their single-index effects regardless of active album, artist, or folder filter. Explicit Album collection rows still emit collection effects. Album/artist collection context actions retain their collection semantics.
  - Files changed:`crates/reborn-ui/src/lib.rs`,

`crates/reborn-ui/src/screens.rs`.
  - Tests added: Album screen, artist screen, and folder-filtered tracks each

select the second matching track and verify Play, Play Next, and Add affect only that track. Explicit album Play, Play Next, and Add continue to target both album members.
  - Tests run:`cargo fmt --all`; `cargo test -p reborn-ui --locked` — 12

passed, 0 failed.
  - Result: Context action intent stays on the selected queue candidate while

explicit collection actions remain collection-wide.
  - Commit:`ae4ce7b` (`Keep filtered track actions singular`).
  - Remaining limitation: Verification is at the UI Action/Effect boundary;

actual queue mutation and physical button interaction remain `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + host UI action tests.

## R8 — cancel actions after input loss

Status: FIXED
  - Finding and symptom:`SYN_DROPPED` and descriptor loss synthesized

`Release`, which the action router treated as Select, Next/Previous, Play/Pause, or Power activation.
  - Current source confirmation:`InputManager::release_stale_inputs()`

emitted `NormalizedInput::Release` on loss, and the router mapped confirmed releases directly to actions. It also accepted unmatched release/repeat events.
  - Implementation: Added an explicit `Cancel` normalized event. State loss

cancels held controls and clears timing/long/repeat state; unmatched release and repeat records cancel rather than activate. For `SYN_DROPPED`, the input manager discards all events through that device's next `SYN_REPORT`. It does not attempt an unsafe key-state ioctl through the existing abstraction and remains fail-safe until a new press is observed. Device paths are reopened by matching the canonical sysfs device identity and name, and missing devices are rediscovered on subsequent polls.
  - Files changed:`crates/reborn-core/src/lib.rs`,

`crates/reborn-platform/src/input.rs`.
  - Tests added: Held Select, Next, and Power followed by `SYN_DROPPED`; stale

events through `SYN_REPORT`; unmatched release/repeat after reconnect; device disappearance before release; cancellation of long/repeat router state; and event-node replacement with the same physical identity versus a reused node with a different identity.
  - Tests run:`cargo fmt --all -- --check`; `cargo test -p reborn-platform

--locked` — 28 passed, 0 failed.
  - Result: Input loss cannot synthesize an activation-sensitive command;

current key state remains unknown and therefore canceled until a fresh press.
  - Commit:`d592203` (`Cancel activation after input state loss`).
  - Remaining limitation: No current key-state ioctl resynchronization is

attempted; loss of state requires a release then a new press before that key can activate. `SYN_DROPPED` behavior follows the [Linux kernel evdev event protocol]([https://docs.kernel.org/input/event-codes.html](https://docs.kernel.org/input/event-codes.html)). Hardware button behavior remains `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + deterministic event-stream tests +

official Linux kernel documentation. No input device was opened on the Y2.

## R9A — artwork occurrence and presentation order

Status: FIXED
  - Finding and symptom: Artwork used a separate event queue from playback

boundaries and only carried `TrackId`. The same track queued twice could receive art before the second occurrence became current, then reject and lose that art permanently.
  - Current source confirmation: The decoder sent artwork directly through

the UI event queue while audio boundaries crossed the sink stream; the UI matched only generation and track ID.
  - Implementation: Artwork now travels through the bounded audio stream

after its authoritative boundary and uses the same playback event sender. Events carry `QueueEntryId`; the UI accepts art only for the current queue occurrence and clears presentation state at a boundary.
  - Files changed:`app/reborn/src/playback.rs`, `app/reborn/src/main.rs`.
  - Tests added: Duplicate `TrackId` occurrences reject next-entry art before

the boundary and accept it after; the playback event channel preserves boundary-before-art order.
  - Tests run: `cargo test -p reborn --bin reborn --locked

artwork_presentation_tests`;`cargo test -p reborn --bin reborn --locked boundary_event_precedes_its_queue_entry_artwork` — both passed.
  - Result: Queue occurrence, not only track identity, controls artwork

presentation timing.
  - Commit:`ed645c8` (`Bind artwork to queue entry boundaries`).
  - Remaining limitation: Renderer/art decoding behavior has host evidence;

display presentation remains `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + targeted host runtime/event tests.

## R9B — Bluetooth transport epoch and open contract

Status: PARTIAL
  - Finding and symptom: Transport identity was only a hash of the PCM object

path. An object reused after daemon restart or renegotiation could leave a stale typed sink plan active; the `bluealsa:` ALSA `plug` endpoint can also hide conversion from the application.
  - Current source confirmation:`pcm_generation()` depended only on the

path. `AlsaSink::open_spec()` previously did not compare the actual opened rate, format, channels, or device with the plan.
  - Implementation: Transport epochs now change on a daemon owner event,

object removal/recreation (including same path), or any observed contract property change (Device, Transport, Mode, Codec, Format, Rate, Channels). Epoch IDs are process-wide so a Bluetooth worker restart cannot reuse a previous worker's values. The required D-Bus matches are registered with the bus; if a required match cannot be installed, Bluetooth PCM observations are withheld. `SinkSpec` records the object/device/transport/mode/codec and epoch, validates the selected peer and negotiated format/rate/channels, and open checks the actual ALSA application-side parameters against the plan. Runtime reloads an active sink for a newly observed epoch and stops truthfully if its selected PCM disappears.
  - Files changed:`crates/reborn-platform/src/bluetooth.rs`,

`crates/reborn-audio/src/lib.rs`, `crates/reborn-audio/src/native.rs`, `app/reborn/src/main.rs`.
  - Tests added: Fake private D-Bus property change and same-path

remove/recreate; epoch invalidation for owner changes and each contract property; non-reuse across a worker restart; SinkSpec stale generation, wrong peer and changed-property rejection; runtime changed/unavailable epoch behavior.
  - Tests run:`cargo test -p reborn-audio --locked` — 5 passed;

`cargo test -p reborn-platform --locked bluetooth::tests` — 7 passed; `cargo test -p reborn --bin reborn --locked bluetooth_epoch_tests` — 1 passed; `cargo check -p reborn --locked` passed.
  - Result: Stale object-path-only identity is removed and the application-side

ALSA plan/open contract is checked; loss or change invalidates the active sink.
  - Commit:`246dc41` (`Invalidate stale Bluetooth transport plans`).
  - Remaining limitation:`bluealsa:` is an ALSA `plug` wrapper, so the app

can verify the ALSA-facing contract but cannot prove the underlying BlueALSA PCM is bit-precise without a private/raw interface. The software deliberately makes no bit-precision claim. SBC remains the active codec; physical transport qualification is `PHYSICAL_QUALIFICATION_PENDING`.
  - Evidence tier: source inspection + targeted host Rust tests + private

fake-D-Bus lifecycle/property test. No BlueALSA service or Y2 was accessed.

## R10 — build, version, and manifest truth

Status: FIXED
  - Finding and symptom: Reborn's product label and ARM checker still

reported FFmpeg 9.0.1 / SONAMEs `.101` despite the pinned target being 9.0.2 / `.102`. Y2Linux's current package producer and validator still described `Y2PlayerNative`, `implemented=false`, and `/usr/bin/y2player`, although the rootfs installs Reborn.
  - Current source confirmation:`reborn-media` hard-coded 9.0.1;

`tools/build/qemu-check.py` asserted 9.0.1 and `.101`; the package producer emitted and validator required the obsolete application fields. FFmpeg source acquisition required the archive to be pre-seeded.
  - Implementation: Added a single Reborn `FFMPEG_VERSION` source used by

runtime reporting, QEMU verification, fixtures, and Y2Linux's pinned source acquisition. The locked build runner now binds the paired Reborn source and forwards the production artifact directory and paired source path, plus the hash-validated owner-firmware input required by the production post-build step. The ARM checker now checks the final loaded runtime and `.102` SONAMEs. The production application receipt names Reborn's actual binaries, shared media library and `/data/reborn` state; rootfs and manifest validation verify those files and reject `/usr/bin/y2player`. Boot-only/system-update receipts preserve or update the installed application identity correctly. When a legacy base lacks a Reborn version field, its retained version is resolved from the exact recorded Reborn source commit; packaging refuses a retained rootfs whose application identity cannot be established. Local review documents remain untracked and are excluded from candidate clean-source checks. FFmpeg acquisition now downloads the official pinned archive to a temporary file, verifies the existing exact SHA256, then atomically installs it. The test harness documents production, retained profile/source-boundary, and host prerequisite classes without deleting historical tests.
  - Files changed: Reborn `FFMPEG_VERSION`,

`assets/fixtures/manifest.json`, `crates/reborn-media/src/native.rs`, `docs/architecture/dependencies.json`, `docs/architecture/reborn-audio-stack-ffmpeg9.md`, `tools/build/fixtures.py`, and `tools/build/qemu-check.py`; Y2Linux `buildroot/package/reborn/reborn.mk`, `tests/README.md`, `tests/test_reborn_receipts.py`, `tools/build/run.py`, and `tools/production/{application.py,boot_update.py,build.py,ffmpeg9.py,package.py,system_update.py,tests.sh,validate.py}`.
  - Tests added: Workspace-version and Reborn application receipt checks;

exact retained source-commit version resolution; rejection of unverifiable identity and the stale legacy receipt; verified archive acquisition and checksum-failure cleanup; Reborn root-image path/legacy-binary checks; locked source-mount resolution.
  - Tests run:`cargo fmt --all -- --check`,

`cargo check --workspace --locked`, and fresh-target `cargo test --workspace --locked` — 143 passed, 0 failed. Y2Linux's locked `tools/production/tests.sh` passed 67 + 38 tests, QEMU shell syntax, ARM ABI and ALSA utility checks. The final ARM QEMU runtime checker passed all 8 software checks and reported FFmpeg 9.0.2; generated-component/ELF verification passed with the exact `.102` library versions, selected components, no encoders/muxers/network protocols/CLI and correct media membrane linkage. Direct ARM ELF inspection confirms hard-float Reborn, ALSA/SQLite, BlueZ/BlueALSA/libsbc and FFmpeg linkage without non-empty RPATH/RUNPATH. Package `validate.py` passed rootfs, ELF, ownership, manifest, fallback and preserve-data checks; all 24 `SHA256SUMS` entries verify.
  - Result: Version and product receipts match the built rootfs. The locked

production test run also exposed and closed a source-path assumption: the FFmpeg receipt loader now honors the runner's `/tmp/Y2Reborn` mount through `Y2_REBORN_SOURCE`. The preserving update selects only BOOTIMG and ANDROID and carries no Y2DATA image. All software/package gates pass.
  - Commits: Reborn `20eb29b` (`Align FFmpeg and Reborn build receipts`);

Y2Linux `609212a` (`Make Reborn build and package receipts truthful`) and `df1bccf` (`Honor locked Reborn source mount in receipts`). Final Y2Linux candidate/audit HEAD is recorded below.
  - Remaining limitation: Historical baseline documents and fixture

provenance continue to name FFmpeg 9.0.1 where that is the version actually tested/generated. Runtime build-configuration strings retain toolchain provenance paths, but inspected target ELFs are ARM EABI hard-float, use no host libraries, and contain no non-empty host search path. Physical qualification remains pending.
  - Evidence tier: fresh host workspace tests + fresh ARMv7 production

package build + QEMU runtime and component/ELF checks + rootfs/package/hash verification. No physical evidence is claimed.

## Final candidate identity and gates

Candidate package: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-reborn-correctness-closure-01/`. The packaged software sources are Y2Linux `5f6b4468fb43605ca1da679420823afa72cea73f` and Y2Reborn `dde3c537cec66b3b2f70a032584cb054bdb3037e`. Y2Reborn's final validation-document commit follows package creation and changes no compiled code; the manifest's `reborn_source_commit` therefore names the exact compiled code commit. The package identity is kernel `6.18.0-y2linux-gpu-02`, Buildroot `2025.02.18`, Reborn `0.1.0` (release `0.1.0-premium.3`), FFmpeg `9.0.2`, BlueZ `5.87`, BlueALSA `5.0.0`, and libsbc `2.2`.````````````````

| Artifact | SHA-256 |
| --- | --- |
| BOOTIMG.img | 34482a2d65c303ac7099f2ea31e1f8104a4d57792767b62081b83c8761abfe1e |
| Y2ROOT.img | ac03708e57489033438627055f8b0b170511fbd38674bc84fdb4674e70faf774 |
| manifest.json | d5b8ec6bf4a2173266f784ece134e48f70c664e129db9be55a440ba624926134 |
| SHA256SUMS | 031728b5a5da7d4abe312ee98647504941d0a199bfa6e6414ebbfe3a31016cbf |

The final review gate found no additional source of truth, no new synchronous UI wait (sink-open waits are polled; the existing release boundary is bounded to two seconds), no weakened fail-closed path, no broadened hardware scope, and no protected-storage, power, or kernel-policy changes. User-visible changes are limited to truthful error/buffering states, single-track intent in filtered contexts, and cancellation after input loss. R9B remains the one software limitation: ALSA `plug` hides the underlying BlueALSA PCM contract, so the application validates only its ALSA-facing negotiated contract and makes no bit-precision claim. All physical Y2 checks remain pending.

## Owner-run physical qualification checklist — not performed
  - Verify the recorded package hashes against every included file.
  - Preserve a tested fallback and confirm its BOOTIMG/Y2ROOT pair.
  - Use `MT6582_preserve_data_scatter.txt` from this package.
  - Select only `BOOTIMG` and `ANDROID`; never select Y2DATA/USRDATA, preloader,

LK, NVRAM, PROTECT, calibration, or factory regions.
  - Boot this exact candidate and confirm the installed build/source markers.

Then qualify, in order: boot/rescue; UI; buttons/wheel; wired playback; pause/resume; volume; seek; next/previous; duplicate queue entries/live edits; ReplayGain; gapless; 5/10/15-second crossfade; screen-off playback; SD insert/remove; Wi-Fi scan; WPA association; DHCP; DNS; reconnect; Bluetooth fresh pairing; trust; SBC playback; Bluetooth reconnect; Wi-Fi + SBC coexistence; and long-playback RSS/XRUN behavior. Charging, suspend and power qualification remain separately scoped and require their own safety procedure.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
