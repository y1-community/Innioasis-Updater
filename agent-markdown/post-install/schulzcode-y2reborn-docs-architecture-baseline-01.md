---
title: "Reborn Baseline 01 architecture and operator contract - Innioasis Updater"
description: "Reborn Baseline 01 architecture and operator contract <!-- knowledge-base-scope: historical-design-/-runbook -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-baseline-01.html"
---

# Reborn Baseline 01 architecture and operator contract - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Baseline 01 architecture and operator contract

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Baseline 01 architecture and operator contract > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Historical Baseline 01 architecture. Later fixes and platform integration are recorded in [correctness closure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FLUNA-CORRECTNESS-CLOSURE-01.md) and [Platform v1 integration](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FPLATFORM-V1-INTEGRATION.md); those records supersede the initial dependency versions and pending-work statements.

Reborn is a native Linux application. Platform entry: Y2Linux `16b2fb8`, retained GPU-01 graphics/audio evidence, then owner-confirmed and pinned-SSH-observed GPU-02 (`6.18.0-y2linux-gpu-02`, root `Y2LINUX-GPU-02`). The read-only capture is [platform-entry.txt](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/platform-entry.txt). No Reborn binary has been installed by the assistant. GPU-02 deep suspend, Wi-Fi association and Bluetooth peer/audio qualification remain physical gates.

## Workspace and dependencies

| Crate | Owned responsibility |
| --- | --- |
| reborn-core | Typed AppModel, actions/events/commands, queue, generation, settings, atomic checkpoints |
| reborn-media | Unique FFmpeg decoder, FLTP DSP/filter graph, final libswresample conversion, metadata and embedded artwork |
| reborn-audio | AudioSink, ALSA PCM/mixer, wired/BlueALSA selection and recovery |
| reborn-library | SQLite schema v1, DB worker, incremental scanner, source availability |
| reborn-platform | Evdev mapping, mount identity, rfkill/wpa control, BlueZ Agent1, power_supply/backlight |
| reborn-graphics | DRM/GBM/EGL/GLES2 ownership, shaders, glyph/art textures, page flips, offscreen test |
| reborn-ui | Wheel/button navigation, screens, list/group views, masked WPA2 entry, pairing prompt |
| reborn-observability | JSONL, ring, levels, metrics, health, heartbeats, panic record, sanitized bundles |
| reborn-control | Typed JSON protocol, bounded Unix socket server and client |
| app/reborn | UI authority, worker orchestration, playback and diagnostics workers; reborn/rebornctl binaries |

Rust 1.90.0; target armv7-unknown-linux-gnueabihf, Cortex-A7. Production linker is Buildroot's `host/bin/arm-linux-gcc` (GCC 13.3.0), sysroot queried from that compiler. `tools/build/cross.sh` sets target CC/AR/linker and pkg-config sysroot; it invokes locked, offline Cargo. All 53 external locked packages, including inactive host/Windows support crates, are vendored. The [full version/license inventory](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/architecture/dependencies.json) records every package. Direct Rust dependencies: serde/serde_json, libc, rusqlite, dbus, font8x8, flate2/tar; cc/pkg-config are build dependencies. No async runtime or bindgen.

Production FFmpeg 9.0.1, SQLite 3.50.4, Mesa 24.0.9, libdrm 2.4.124 come from Buildroot 2025.02.17. The media contract and selected component families are documented in [the FFmpeg 9 audio-stack design](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Freborn-audio-stack-ffmpeg9.md): local music demuxers/decoders, FLTP libavfilter processing, libswresample, JPEG/PNG/WebP artwork and no FFmpeg executable, encoder or network protocol. Original synthesized fixtures carry CC0 provenance and hashes. Native libraries retain their Buildroot license/source receipts; Rust vendors retain upstream licenses. The graphics lifetime code is adapted from Y2Linux's MIT gpu-check.

The player ELF has no direct `libav*``DT_NEEDED` entries. Buildroot packages the single `libreborn_media.so` membrane under `/usr/lib/reborn`, which is loaded on first media use. Reborn starts after `S02y2-data`; radio and network workers retry independently while their providers start later. The GPU context is opened before the library scan, but KMS ownership remains with the early splash until Reborn presents its first complete frame. Startup phase events cover model restore, graphics, storage, library workers, core services, radio workers and runtime readiness.

## Threading, playback, storage and UI

The UI thread alone owns the application state. Fixed workers: playback, audio, scanner, database, Wi-Fi, Bluetooth, diagnostics, control, logger, watchdog. Channels are bounded: playback 4, audio commands 8, PCM 8 blocks, playback events 64, database 32, scanner requests 1/results 2, radio requests 8/results 2, diagnostics 2, control requests 8, logger 256. Cancellation/generation atomics and observability locks are coordination only, not shared application authority. FFmpeg contexts use one decoder thread. ALSA writes are nonblocking, with at most 20 ms waits; stale generations are discarded on stop, pause, seek and output switch. Pause releases the sink; resume decodes from the last measured position. Wired playback prefers S32_LE at the source-native qualified rate, while the current qualification profile deliberately selects the physically proven 44.1 kHz stereo S16 mode. Bluetooth consumes the same processed PCM stream and adapts at its final BlueALSA sink boundary; discovery uses the 4.3.1 ObjectManager API. A missing or unsupported PCM fails before output changes. Eight 2048-frame blocks bound decoder buffering to about 372 ms plus the sink. The native resampler staging buffer is bounded separately. EOF drains pending PCM; a stalled sink reports an error rather than blocking the UI.

Wired ALSA is discovered by card identity Y2Audio, not card number. The sink negotiates the qualified stereo format/rate from the platform profile, logs any explicit fallback, and rejects an unqualified combination. It saves/restores Master/Headphone mixer state, uses the proven -24 dB hardware level and keeps software volume inside the FFmpeg filter graph. BlueALSA uses validated peer addresses with PROFILE=a2dp; BlueZ and BlueALSA own transport/codecs/keys. Opening an audio sink holds the platform's shared `/run/y2/activity.lock`; closing it releases the suspend lease. This prevents the existing explicit suspend helper from interrupting playback. Screen blanking does not suspend.

Internal music defaults to `/data/music`; Reborn refuses normal startup without mounted Y2DATA schema 1. SD mounting uses the existing bounded `y2-media` helper and its unique ext4/vfat/SD-controller selection. Mount entries and libblkid UUID identify sources. Removal pauses affected playback, marks source entries offline, and retains their database records. Reinsertion triggers an incremental scan. No block-number assumptions, formatting, Y2ROOT music writes, or protected reads.

SQLite user_version 1, foreign keys, WAL, NORMAL synchronization and 2-second busy timeout. `sources` stores identity/root/online. `tracks` stores all requested file and metadata fields, a unique (source_id,path), scan marker and deletion flag. A single DB worker owns the connection. Scanner batches 64 writes in transactions; (size,mtime) reuse skips FFmpeg. Missing files are marked deleted only after a complete mounted-source traversal. Traversal errors retain records; bad media is skipped. Symlinks are not traversed; depth <=32 and <=250,000 files per scan. UI lists/queues currently cap at 20,000 tracks; a paged DB query API is available.

Artwork is extracted only when opening a selected track, reduced to 160x160 RGBA, and cached under a track/size/mtime identity. At most 64 cache files (6.25 MiB). The GPU texture is reused; no frame-time artwork decode. Missing/invalid artwork gets the built-in Reborn tile. The UI uses a public-domain bitmap glyph atlas; non-ASCII glyphs currently display `?`. This is a known baseline limitation.

DRM driver identity selects Mediatek KMS; connected connector/preferred mode is queried. Linear XRGB8888 GBM scanout, EGL ES2 config, GLES textured rectangles, alpha blending, font/art textures and page flips follow the physically proven Lima path. A non-Mali400 renderer is rejected. Static screens stop submissions; damage is capped at ~29.4 FPS (34 ms). Now Playing updates once per elapsed second. Page flips have a 3-second deadline. Context failure captures evidence and makes one recreation attempt; hardware resume correctness remains to be qualified.

Evdev nodes are discovered by the four proven device names; node numbers are never fixed. Standard Linux KEY_UP/DOWN/LEFT/RIGHT/ENTER/BACK/MENU, media/volume/ Power and REL_WHEEL map to Actions; release events do not activate UI actions. All main screens work from buttons/wheel. Now Playing: Select toggles, Left/Right seek 10 seconds, Up/Down previous/next. Menu returns home, Back returns one level. WPA2 entry: wheel chooses a character, Select/Right appends, Left deletes, Menu submits, Back cancels. Text is masked. Saved networks connect with Select and forget with Left. Bluetooth device pages offer Pair/Connect/Disconnect/Forget/ Use for audio. Pair confirmation uses Select/Back; legacy PIN-entry peers are explicitly rejected by the baseline DisplayYesNo agent.

Wi-Fi uses native Unix datagram wpa_supplicant control plus standard rfkill; DHCP remains with the existing Y2Linux connectivity service. No wpa_cli backend. Passwords are sent only to wpa_supplicant, never stored in Reborn DB/state or logged. BlueZ uses system D-Bus ObjectManager, Adapter1, Device1, AgentManager1/ Agent1. Pair/connect requests are asynchronous on the agent connection with bounded pending operations and deadlines. BlueALSA ObjectManager/PCM1 exposes available PCM/rate/codec state. No bluetoothctl application backend. The live GPU-02 service accepted the read-only ObjectManager query; no peer was connected.

`power_supply` and backlight are discovered under sysfs. Idle screen timeout is 60 seconds by default, adjustable 30..600. Screen-off leaves playback running; input wakes without accidentally activating the underlying selection. Reborn does not initiate deep suspend, reboot, charging changes or radio-pair tests from baseline qualification. Offline charging remains in the platform initramfs.

## FFI boundary and persistence

Application, UI, control, library and observability logic forbid unsafe Rust. Reviewed owned native wrappers are `reborn-media/src/native.rs` + `native/media.c`, `reborn-audio/src/native.rs` + `native/audio.c`, `reborn-graphics/src/native.rs` + `native/graphics.c`, and the small `reborn-platform/src/native.rs` POSIX/libblkid wrapper. Every Rust unsafe block documents lifetime/ownership. Native contexts are !Send and thread-confined; only the separately allocated C11 atomic cancel handle is Send+Sync through Arc. Packet/frame/codec/resampler pointers never leave reborn-media. rusqlite and dbus supply their own narrow maintained FFI.

Mutable layout, mode 0700 directories and 0600 state/log/bundle files:`/data/reborn/library.db (+ WAL/SHM) /data/reborn/state/session.json /data/reborn/cache/*.rgba /data/reborn/logs/{reborn-current,reborn-previous-1,reborn-previous-2}.jsonl /data/reborn/logs/{panic-last.json,startup-last.jsonl,supervisor-last.json} /data/reborn/diagnostics/reborn-diagnostic-*.tar.gz /run/reborn/control.sock`

State includes queue, position, source configuration, output, settings and screen. Atomic temporary-file/fsync/rename/parent-fsync checkpoints occur every 15 seconds, on pause/output changes and orderly exit. Restore always starts paused/stopped. The database preserves offline sources. Radio secrets/preferences remain with the existing platform service stores under Y2DATA.

## Observability and control

JSONL fields: timestamp_wall (Unix ms, device RTC may be unset), timestamp_monotonic (session ms), boot_id, reborn_session_id, sequence, level, subsystem, event, message, correlation_id, fields. Stable subsystem tags are listed in `reborn-observability::SUBSYSTEMS`. Correlation IDs are monotonically allocated per session and follow playback/scan/radio operations. Native errors retain readable FFmpeg/ALSA codes; D-Bus errors retain interface/method/error name. FFmpeg and ALSA callbacks enter the same logger. Repeated identical messages are limited to ten per ten seconds; dropped counts are metrics. No per-write INFO.

Default INFO; runtime ERROR/WARN/INFO/DEBUG/TRACE per subsystem. Overrides reset on restart; TRACE expires after 300 seconds. Ring: 512 events, <=4096 bytes each. Logger queue: 256 events; overflow drops logging, never blocks playback. Rotation: three files, 1 MiB each (3 MiB total). Disk-full/write failures degrade logging health and leave the recent-event ring available. Panic evidence replaces one small file. Diagnostic archives: <=2 MiB uncompressed data, four retained, and at most one automatic bundle per 300 seconds. Cache/log/bundle limits are independent.

Metrics registry uses a fixed low-cardinality inventory (see source/dependencies handoff); counters cover playback, decode, audio XRUN/recovery, graphics, scanner, Wi-Fi/Bluetooth, SD and logger errors; gauges cover buffer frames/ms, query/frame latency, scan throughput, track count and uptime. No per-track/path/peer labels. Health states: ok/degraded/failed/unavailable, with required/optional classification, recent faults and runtime heartbeats. Unavailable optional radios/SD do not fail the baseline; required graphics/audio/database/storage/input can fail it. Watchdog checks UI/audio/playback/scanner/DB deadlines without restarting workers. Panic hook retains version/thread/location/message/event IDs/state summary and exits 101 for supervision. SIGINT/SIGTERM checkpoint and close graphics/audio.

Protocol: versioned newline-terminated JSON on a local Unix socket; no TCP listener. Parent 0700/socket 0600, owner/root access. Eight clients maximum; requests <=8192 bytes, responses <=2 MiB, request assembly 2 seconds, bounded response deadlines. Unknown operations/fields, malformed JSON and oversized requests are rejected. No exec command, arbitrary file write or free-form backend command exists.

`rebornctl` always emits JSON (`--json` accepted):
  - status, health (0 healthy / 1 degraded / 2 failed), metrics, snapshot
  - logs [--since 60s] [--subsystem audio] [--level warn] [--last 100] [--follow]
  - events [--last 100]; log-level [SUBSYSTEM LEVEL | reset]
  - diagnose; test list; scan incremental; input monitor --seconds 1..30
  - play ID; pause; resume; stop; next; previous; seek MILLISECONDS; volume 0..100
  - output wired|MAC (Bluetooth must already be connected with A2DP/BlueALSA)

Logs/events queries use the bounded live ring, not an unbounded file read. `logs --follow` polls that live stream. Previous rotated files are available for owner SSH inspection. Snapshot combines the UI-owned model with worker state, metrics/health/resources/recent faults. Individual counters may progress during serialization; it is not a stop-the-world sample.

Safe tests: baseline, decoder, playback (decode-only), database, library, storage, graphics, input, wifi-scan, wifi-connect --saved ID, bluetooth, bluetooth-scan --seconds 1..15, audio-wired, audio-bluetooth. Audio tests are explicit and reject active playback; they output one second of generated -46 dBFS audio at reduced test gain. Default baseline does not play sound, change radio state, pair, reboot, suspend or modify personal files. Scan tests restore prior power/discovery state; connection to a saved network requires that explicit command. Database writes are rolled back; quick_check and a <=64-track consistency sample are used.

Bundles contain build/session/kernel/boot identity, status/health/metrics, up to 128 recent events, selected recent kernel GPU/audio/storage fault excerpts, proc memory/process summaries, ALSA cards, storage/mount identity, renderer, radio state, power supplies and DB/scanner summaries. A recursive sanitizer removes secret/PSK/link-key/IRK/calibration/private-key fields, pairing prompts, media paths and private title/artist/album/queue data. Fixed allowlisted sources only: no credentials, protected partition bytes, factory inputs or arbitrary user files. The host qualification tool never reads a private SSH key; OpenSSH uses the existing owner identity and required pinned known-hosts file.

## Validation boundary

Host tests cover state/generation/queue/source loss, sink failure/stop/switch, SQLite migration/future-schema/ref-counted identity/offline retention/SQL injection, scanner incremental reuse/deletion/malformed files, six decoder formats/truncation/ cancellation, log rotation/ring/size/redaction/disk-full/storm/metrics/heartbeat, control validation/JSON/socket permissions/slow clients, UI/navigation and state restore. An isolated ARM run will exercise the actual FFmpeg 9.0.1/SQLite ELF binaries and JSON control tests; it does not emulate physical Lima/audio/radios.

Remaining physical gates: visible GPU rendering and physical input, real wired and Bluetooth audio/XRUN/coexistence, pairing/reconnect/output switching, WPA2/DHCP, real SD hotplug, screen-off/wake, reboot restore and GPU-02 same-boot deep resume. Only physical evidence can produce REBORN BASELINE 01 PASSED.

API references used during implementation: [FFmpeg send/receive](https://ffmpeg.org/doxygen/7.1/group<strong>lavc</strong>encdec.html), [wpa_supplicant control](https://w1.fi/wpa_supplicant/devel/ctrl_iface_page.html), [BlueZ Agent1](https://bluez.readthedocs.io/en/latest/agent-api/). The pinned Buildroot and installed native headers determine the compiled ABI.

## Historical Android reference

Preserved from the September 8, 2026 planning assessment. The Android reference was `/home/luca/Dokumente/Code/Y2Player` at `870f2b33e49129990bc0a98eeb34d58ed42542b6`, clean when inspected. Ignored firmware and captures are not authenticated by that source revision. Paths in this section refer to that repository; these are behavioral references, not Reborn capabilities.

The Android player is an API-19 HOME launcher with a custom drawn, wheel-oriented 480 × 360 interface. Its `AppContainer.kt`, `core/state/`, `queue/`, `input/`, `library/`, `playback/` and tests capture useful behavior and ownership boundaries.

Useful references include explicit queue ordering and shuffle passes; seek, previous and repeat rules; gapless/crossfade cancellation; ReplayGain fallback and peak handling; volume transition safety; route-loss pause; storage removal and USB export coordination; incremental metadata scanning; lazy bounded artwork; audiobook progress; playlists; backup/import; search; screen-off controls; listening history; and themes. At that revision, `RELEASE_2.5.md` documented search, hardware-dependent FM, alphabet navigation and expanded timers, while the README still described 2.3 and denied search and the old input map denied acceleration. Resolve behavior against the dated source/tests and release record.

`docs/ARCHITECTURE.md` and `docs/PLAYBACK_ENGINE.md` described one audio owner thread, bounded/coalescing commands, two decoder handles for transitions, explicit decoded/submitted/played accounting, cancellation and persistent PCM buffers. The inspected FFmpeg engine used a fixed 44,100-Hz `PcmFormat`; C decoding and metadata crossed JNI, DSP stayed float until PCM16 AudioTrack output, and SQLite indexed the library. Native persistence and tests are designed separately.

The original native blueprint proposed a Rust state/action/reducer/effect core, a C decoder/DSP ABI, independent output sinks and standard Linux adapters. JNI, Android services, wake locks, AudioTrack, vendor HAL interfaces and permission workarounds remain historical context. Its Last.fm, modern Bluetooth, LVGL/DRM and direct-ALSA targets were proposals, not inherited capabilities; the current Reborn implementation uses its documented FFmpeg/ALSA/DRM/GLES architecture. Platform hardware evidence and the original Y2E research specifications are maintained in [Y2Linux's evidence baseline](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2FM0-evidence-and-recovery.md).

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
