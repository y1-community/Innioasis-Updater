---
title: "REBORN-BASELINE-01 — first implementation handoff - Innioasis Updater"
description: "REBORN-BASELINE-01 — first implementation handoff <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-baseline-01.html"
---

# REBORN-BASELINE-01 — first implementation handoff - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# REBORN-BASELINE-01 — first implementation handoff

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# REBORN-BASELINE-01 — first implementation handoff > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Ready for owner installation; physical acceptance is pending. No Reborn code has been installed on the Y2 by the assistant. GPU-02 is owner-confirmed and read-only SSH inspection confirms the current interfaces. This is a new native Linux application, with no Android runtime or ported Android architecture.

Built Reborn source: `77e673232a586e1f027538861bcbbec3466b36fd`. Built Y2Linux integration: `08b0e7d17c453037edf64f58a1798ff4457ca0ce`. Unchanged kernel source: `7e318afbffe640c6bf9da458f61ac2108f7d5bde`. Later handoff/qualification-tool commits do not change the embedded build identity.

Package: `/home/luca/Dokumente/Code/Y2Linux/out/REBORN-BASELINE-01`. [Package manifest](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/package-manifest.json), [architecture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fbaseline-01.md), [platform entry](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/platform-entry.txt), [BlueALSA API inspection](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/bluealsa-objectmanager.txt).

## 1–6. Toolchain, source structure and native boundary
  - Rust:`rustc 1.90.0 (1159e78c4 2025-09-14)`, pinned by

`rust-toolchain.toml`. Cargo lockfile and all 53 external dependency sources are committed. Production builds passed with networking disabled.
  - Target:`armv7-unknown-linux-gnueabihf`, Cortex-A7, hard-float glibc.

Linker is the actual Buildroot `host/bin/arm-linux-gcc`, GCC 13.3.0, Bootlin armv7-eabihf glibc stable-2024.05-1. The compiler-reported sysroot is `/home/luca/Dokumente/Code/Y2Linux/out/reborn-baseline-01-build/buildroot/host/arm-buildroot-linux-gnueabihf/sysroot`. [cross.sh](https://github.com/SchulzCode/Y2Reborn/blob/main/tools/build/cross.sh) selects CC/AR/linker/pkg-config from that SDK. Both binaries are ARM ELF32 PIE, hard-float, RELRO/NOW, nonexecutable stack.
  - Workspace: nine crates under `crates/`: `reborn-core`, `reborn-media`,

`reborn-library`, `reborn-audio`, `reborn-platform`, `reborn-graphics`, `reborn-ui`, `reborn-observability`, `reborn-control`. `app/reborn` builds `reborn` and `rebornctl`. Existing Git history and historical planning remain. No `Y2PlayerNative` repository existed at inspection.
  - Dependencies:[complete version/license inventory](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/architecture/dependencies.json).

Direct Rust dependencies are serde/serde_json, libc, rusqlite, dbus, font8x8, flate2/tar; cc/pkg-config are build-time only. Native production libraries: FFmpeg 9.0.1, SQLite 3.50.4, ALSA 1.2.13, Mesa 24.0.9, libdrm 2.4.124, D-Bus 1.14.10, BlueZ 5.79, BlueALSA 4.3.1, wpa_supplicant 2.12, libblkid from Buildroot. Buildroot is 2025.02.17. No async runtime, production bindgen, Python/Node/Java/Android runtime or FFmpeg executable.
  - Unsafe/FFI: only owned wrappers in `crates/reborn-{media,audio,graphics}/src/native.rs`

with their respective `native/{media,audio,graphics}.c`, plus the small `crates/reborn-platform/src/native.rs` POSIX/libblkid wrapper. Unsafe blocks document lifetime and ownership; decoder/graphics/PCM handles stay on their owning threads. Application/control/library/observability/UI logic forbids unsafe Rust. rusqlite/dbus provide upstream SQLite/D-Bus FFI.
  - FFmpeg: production 9.0.1, direct libavformat/libavcodec/libavutil/

libswresample and libswscale for artwork. Local-file protocols only; selected FLAC, MP3, AAC/M4A, Ogg Vorbis, Opus, WAV and PNG/JPEG artwork support.

## 7–15. Playback, services and persistence
  - Playback: main/UI alone owns typed AppModel. Fixed playback/audio/scanner/

DB/radio/diagnostic/control/logger/watchdog workers use bounded typed channels. Eight PCM blocks bound decoding ahead; generation IDs and cancellation discard stale data on stop, pause, seek and output change. Pause releases the sink; resume reopens/seeks. EOF drains; stalled/error sinks notify the model. Artwork loads lazily at 160×160 RGBA and uses a 64-file cache.
  - Audio:`AudioSink` abstraction; wired ALSA card discovered by ID `Y2Audio`,

using the physically proven 44.1 kHz stereo S16 path to CS43131. Bluetooth uses ALSA BlueALSA A2DP; ObjectManager/PCM1 selects the peer's stereo 44.1/48 kHz rate for both decoder and sink. Unsupported/missing PCMs fail explicitly. Period near 512/buffer near 4096, nonblocking writes, bounded recovery and software gain. Master/Headphone state is saved/restored. Active output holds the platform suspend activity lock. BT disconnect pauses playback.
  - Database: SQLite schema/user_version 1, WAL, foreign keys, NORMAL sync,

2-second busy timeout; one worker serializes access. `sources` stores stable ID/root/online. `tracks` stores source/path/filename/size/mtime, title/artist/ album/album_artist/track/disc, duration/codec/rate/channels/bitrate/artwork, scan marker/deleted. `(source_id,path)` is unique; artist/album indexes exist. Newer unsupported schemas fail safely. No UI-thread DB queries.
  - Scanner: source/path/size/mtime diff, batches of 64 DB writes; unchanged

entries reuse metadata. New/changed media uses FFmpeg; individual failures do not abort scanning. Missing records are marked deleted only after complete mounted-source traversal; offline source records remain. UUID-based SD identity, boot/insertion scans and explicit `scan incremental`. Depth 32/files 250,000 bounds; no symlink traversal. Reports discovered/reused/rescanned/failures/ throughput/elapsed. UI/queue cap is 20,000 tracks.
  - Graphics: discover Mediatek DRM and connected/preferred display mode;

linear XRGB8888 GBM, EGL ES2, GLES2 shader/text/art rendering on Mesa/Lima. Requires renderer `Mali400`. No framebuffer/X11/desktop fallback. Damage-driven submissions, 34-ms animation cap, static GPU idle, 1-Hz playing time display. Offscreen pixel test and bounded flips; one context recreation attempt on loss.
  - Input/UI: evdev discovery by proven device names, no fixed event numbers.

Key/wheel events become typed Actions. Main menu, artists/albums/tracks/folders, Now Playing, Bluetooth, Wi-Fi, diagnostics and settings work without touch. Power toggles display; first input wakes. Now Playing Select toggles, Left/ Right seeks 10 seconds, Up/Down changes track. Menu returns home; Back returns.
  - Wi-Fi: wpa_supplicant Unix control API, standard rfkill and existing Y2Linux

DHCP service. On/off, scan, saved/available networks, status/security/signal, connect/forget. WPA2 wheel entry: wheel selects character, Select/Right appends, Left deletes, Menu submits, Back cancels. Password text is masked, submitted only to supplicant, never duplicated in Reborn storage/logs.
  - Bluetooth: BlueZ system D-Bus Adapter1/Device1/ObjectManager and minimum

Agent1 DisplayYesNo. On/off, discovery, available/paired peers, pair/connect/ disconnect/forget/audio selection; bounded asynchronous operations preserve agent servicing. Select/Back confirms/rejects pairing. Legacy PIN-entry peers are explicitly rejected. BlueZ owns bonds; BlueALSA owns codec transport.
  - Persistence:`/data/reborn/library.db`, `state/session.json`, `cache/`,

`logs/`, `diagnostics/`; music defaults to `/data/music`, SD follows existing `/usr/sbin/y2-media` mount policy at `/media/sd`. No user music in Y2ROOT. Atomic fsync/rename state every 15 seconds plus pause/output/exit; queue, position, output/settings/section/source configuration restore paused. Service requires mounted Y2DATA/schema 1, mode-0700 directories; absent radios or SD do not prevent local/wired startup. Offline charging never reaches it.

## 16–25. Observability, automation and privacy
  - Logger: centralized nonblocking bounded queue (256), writer, recent-event

ring (512 × at most 4096 bytes), fixed subsystem tags, per-session correlation IDs, native FFmpeg/ALSA bridges. INFO default, runtime per-subsystem overrides, TRACE auto-expires after 300 seconds. Identical-event storms: ten/ten seconds. Logger errors degrade health while playback/ring continue. Worker heartbeats expose stalls; panic hook records context and exits 101. Supervisor permits five consecutive rapid failures, delays 2/4/6/8 seconds, then leaves SSH usable.
  - Format: JSONL with `timestamp_wall` (Unix ms), `timestamp_monotonic`

(session ms), `boot_id`, `reborn_session_id`, `sequence`, `level`, `subsystem`, `event`, `message`, `correlation_id`, `fields`. Device RTC is currently not synchronized; boot/session/monotonic fields are authoritative for correlation.
  - Rotation: current + previous-1 + previous-2, each at most 1 MiB: 3 MiB

main logs. Panic/startup/supervisor evidence replaces fixed files. Four diagnostic archives, each at most 2 MiB of uncompressed JSON; automatic bundle interval at least 300 seconds and serialized writer. Artwork budget 6.25 MiB.
  - Metrics: fixed names, no per-path/SSID/peer label growth:
````text reborn_uptime_seconds playback_tracks_started playback_tracks_completed playback_errors ffmpeg_packets_decoded ffmpeg_frames_decoded ffmpeg_decode_errors audio_buffer_frames audio_buffer_ms audio_xruns audio_recoveries decoder_stalls library_tracks library_scan_files_per_sec library_scan_errors database_query_latency_ms graphics_frames graphics_frame_time_ms graphics_missed_frames graphics_context_losses wifi_connects wifi_disconnects wifi_errors bluetooth_connects bluetooth_disconnects bluetooth_errors sd_insertions sd_removals logs_dropped log_write_errors ````
  - Health: runtime `ok`, `degraded`, `failed`, `unavailable`, required/optional

subsystem flags, fault summaries and worker deadlines. Required failures fail qualification; absent optional radios/SD warn. Health CLI exit status is 0 healthy, 1 degraded, 2 failed. Compiled-in support does not imply health.
  - Control:`/run/reborn/control.sock`, parent 0700/socket 0600, Unix only.

Versioned newline JSON, max eight clients, 8192-byte request/2-MiB response, 2-second request assembly and bounded operation waits. Rejects malformed, oversized, unknown-operation/unknown-field requests. No arbitrary exec, shell protocol, path writes or network listener.
  - CLI: all important output is JSON; `--json` is accepted:
````text status | health | metrics | snapshot | diagnose logs [--last N] [--since 60s] [--subsystem NAME] [--level LEVEL] [--follow] events [--last N] log-level [SUBSYSTEM LEVEL | reset] test list | test NAME scan incremental input monitor --seconds 10 play ID | pause | resume | stop | next | previous | seek MILLISECONDS volume 0..100 | output wired|MAC ``` Logs/events query the bounded ring; rotated historical files remain on Y2DATA. `snapshot` includes current model/service state, buffers, health, counters, resource summary, kernel fault excerpts and recent errors. Worker counters may advance during serialization; it is not a stop-the-world sample.`
  - Safe test inventory:`baseline`, `decoder`, `playback` (decode-only),

`database`, `library`, `storage`, `graphics`, `input`, `wifi-scan`, `wifi-connect --saved ID`, `bluetooth`, `bluetooth-scan --seconds 1..15`, `audio-wired`, `audio-bluetooth`. Baseline has no audible/radio state-changing tests. Explicit audio tests require paused playback and use one second of original -46 dBFS audio at further reduced gain. Scans restore radio/discovery state; no unknown-peer pairing or arbitrary-network connection. DB writes roll back; library checks sample at most 64 rows. Graphics does FBO readback.
  - Bundles: one `diagnostic.json` in a bounded `.tar.gz` under diagnostics,

including build/session/kernel/boot identity, snapshot/health/metrics/recent errors and up to 128 events, selected kernel fault excerpts, proc memory/ process information, CPU frequencies, DRM summary, ALSA cards, storage, radio/power and library summaries. Significant failures trigger rate-limited capture; no archive on every warning.
  - Redaction: recursive secret/PSK/password/link-key/LTK/IRK/bond/private-key/

calibration/protected-field filtering; private media metadata/paths/queues, pairing prompts and network identifiers are removed from bundles. Fixed allowlisted system sources only. No private-key reads, credential files, raw calibration/partitions or arbitrary personal files. Sanitizer, secret absence, disk-full, storm, ring/rotation/archive bounds have automated tests.

## 26–32. Qualification tool, results and exact artifacts
  - Astra host tool:[tools/qualification/reborn-baseline.py](https://github.com/SchulzCode/Y2Reborn/blob/main/tools/qualification/reborn-baseline.py).

Default host `root@10.42.0.1`, existing owner identity and mandatory approved known-hosts pin. It invokes JSON commands over SSH, never reads/copies/packages the private key and never installs. Timestamped results contain status, health, snapshots, metrics before/after, tests, selected JSONL, sanitized bundle, summary/report and checksums. Fail conditions include missing process/JSON, failed baseline/final health, software renderer, restart, unexpected requested build identity, new XRUN/playback/GPU errors; missing optional SD/network/peer warns. Radio scans/audio are explicit flags.
  - Automated results:50 Rust tests, 20 host daemon checks, **3 host

tooling tests, 8 installed ARM runtime/shell checks, 94 existing platform regressions** pass. Clippy all workspace/all targets passes with `-D warnings`. Full production image build passed inside `bwrap --unshare-net`. ARM runtime tests must be rerun with the installed binaries and production FFmpeg 9.0.1, with six format fixtures and embedded-art pixel check, SQLite/schema/rollback, library, metrics and sanitized diagnostic creation. Host scanner reused all six unchanged tracks, skipped malformed media and handled deletion. Raw ext4/tar byte comparisons, source IDs, fixtures, ext4 UUID/label/check, ELF ABI/hardening, root-only scatter, privacy exclusions and checksums pass. [Host summary](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/host-summary.json), [ARM results](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/arm-tests.json), [root checks](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/rootfs-checks.json). These are not physical acceptance.
  - Installed binary sizes:`reborn`1,829,852 bytes;

`rebornctl`441,260 bytes (stripped, native dynamic ELF).
  - Y2ROOT change: image remains 536,870,912 bytes (512 MiB);

ext4 allocated usage 89,853,952 bytes, increase **7,331,840 bytes (~6.99 MiB)** over GPU-02. No Y2DATA image/migration/format.
  - Y2ROOT:`/home/luca/Dokumente/Code/Y2Linux/out/REBORN-BASELINE-01/Y2ROOT.img`
````text c353152dea44a554486e024a4d8a8105fbbdfd1310db5749b28d7e5b8e5c8012 ````
  - Fallback: exact retained GPU-02 root, package `fallback/Y2ROOT.img`:
````text 1dec3b9c462587d804a022ef97e45222329065d263f53c2159ce00f728db145f ````
  - BOOTIMG:unchanged, no BOOTIMG payload selected or supplied in this

root-only package. Requires the owner-installed GPU-02 kernel already observed: `6.18.0-y2linux-gpu-02`; its retained BOOTIMG SHA256 is:
````text 2e5f7e785e80dfc646e57d0ccfadff683d54a2c5303671c819ea4e42863089a9 ````

## 33. Owner manual installation
  - Verify the package on the host:
` cd /home/luca/Dokumente/Code/Y2Linux/out/REBORN-BASELINE-01 sha256sum -c SHA256SUMS`
  - Use the established owner shutdown/USB/power-entry procedure and proven

SP Flash Tool v5.2032.00 with matching `MTK_AllInOne_DA.bin`.
  - Load `MT6582_reborn_root_only_scatter.txt` from this package. Choose

Download Only. Exactly ANDROID is selected, pointing to this package's `Y2ROOT.img`. BOOTIMG, USRDATA and every other row remain unchecked/NONE. Do not select Format/Firmware Upgrade or enter raw addresses.
  - Manually download the selected root and boot normal Linux. Y2DATA, saved Wi-Fi,

bonds, SSH identity, music and existing GPU-02 BOOTIMG remain in place.
  - Connect USB for the existing owner SSH workflow and report Reborn installed.

Expected marker: `/etc/y2linux/build-id` = `Y2LINUX-REBORN-BASELINE-01`; `rebornctl status --json` reports source `77e6732…` and version `0.1.0-baseline.01`.

For rollback, load the fallback directory's root-only scatter, select only ANDROID with its own `Y2ROOT.img`, Download Only. That restores GPU-02 userspace with the current GPU-02 BOOTIMG and preserves Y2DATA. Existing older two-image connectivity fallbacks are retained separately; this package never selects them.

## 34. Automated physical qualification after installation

First use SSH, without asking the owner to click through software tests:`rebornctl status --json rebornctl health --json rebornctl metrics --json rebornctl test baseline --json`

The host tool runs those and retains evidence, then performs selected safe tests:`cd /home/luca/Dokumente/Code/Y2Reborn python3 tools/qualification/reborn-baseline.py \ --known-hosts /home/luca/Dokumente/Code/Y2Linux/evidence-private/20260915-m5-entry/known_hosts \ --expected-build 77e673232a586e1f027538861bcbbec3466b36fd \ --output out/qualification`

After the first suite, an explicit targeted run may add `--radio-scans` and `--wired-audio`; audio must be paused. The latter produces the short quiet wired test signal. The former scans only and restores prior radio state. Do not change the pinned SSH identity to work around a mismatch; the default host known-hosts entry is stale, and the retained owner-approved pin worked during inspection.

Then collect a single 10-second input-monitor window while the owner exercises buttons/wheel; obtain one visible/audible confirmation. Use owner-selected Wi-Fi and Bluetooth peers, never arbitrary networks/devices. Run explicit saved-network connection and connected-peer audio tests; capture state/metrics around output switching, SD insertion/removal, display blank/wake, charger transitions and reboot restore. Real suspend remains a separate explicit test using the existing guarded GPU-02 procedure, with same-boot evidence; it is not part of baseline automation.

On failure collect snapshot, related logs, metrics, events, selected kernel excerpts and a sanitized bundle first. Identify the failing layer before a targeted correction; rerun affected checks and then baseline regression.

REBORN BASELINE 01 has not passed physical acceptance. Remaining gates are boot/visible Lima UI and controls, real internal/SD scans and hotplug, wired audio, BlueZ pairing/A2DP/output switching, WPA2/DHCP, screen-off/wake, reboot restore, same-session GPU-02 resume and normal-use stability. Device RAM/thread count/ startup timing/full-library throughput/XRUN/crash counts remain unmeasured for Reborn; the configured Rust topology is main plus ten workers. Do not substitute host/emulator measurements for these results.

Known implementation limits: basic ASCII glyph atlas, 20,000 loaded-track/queue cap, no legacy Bluetooth PIN-entry flow, stereo S16 at 44.1/48 kHz, no automatic deep-suspend policy. The requested advanced player features remain deferred. STOP for owner installation. Reborn 02 is not authorized.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
