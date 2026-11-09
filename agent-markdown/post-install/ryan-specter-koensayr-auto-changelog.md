---
title: "Changelog - Innioasis Updater"
description: "Changelog All notable changes to this project will be documented in this file. Format: Keep a Changelog https://keepachangelog.com/en/1.1.0/. Versioning: SemVer https://s"
language: "en"
source: "https://innioasis.app/post-install/ryan-specter-koensayr-auto-changelog.html"
---

# Changelog - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=koensayr-y1)

Post-install setup · Koensayr · Y1

# Changelog

A Y1 custom Software maintained by the community.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=koensayr-y1)[Install guide](../guide.html?model=Y1&software=koensayr-y1)

# Changelog

All notable changes to this project will be documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/spec/v2.0.0.html). For full prose detail on any entry, see `git log`.

## [2.4.0] - 2026-05-22

### Fixed
  - Broader head-unit coverage for live metadata. Continuous notifications across track, play-state, position, and repeat/shuffle edges; head units detect each new track even when titles repeat; clean subscription state on every fresh connection.
  - Metadata + play / pause indicators now work on the broad class of head units and speakers that strictly require their AVRCP transaction IDs be echoed back. Previously, those head units silently rejected every response Y1 sent and fell back to key-press-only mode — metadata panes stayed blank and play-state indicators drifted out of sync.
  - Head units that gate metadata on AVRCP browse capability now enter full metadata mode. Restored the public-browse-group SDP attribute that some head units use as a "this peer supports full AVRCP" discriminator.
  - Metadata no longer freezes on head units that close the audio stream between tracks. The AVRCP control channel now survives audio open/close cycles, so the metadata view stays in sync without re-handshaking after every skip.
  - Head-unit play / pause glyphs flip reliably after a head-unit-initiated PAUSE. The music-player Activity was seeding a PLAYING announcement immediately after its own startup-reset PAUSE, racing out to the AVRCP wire as PAUSED → PLAYING; head units saw the trailing PLAYING and refused to flip.
  - Discrete PAUSE on head units with separate Play and Pause buttons pauses idempotently instead of toggling.
  - Spurious paused-state blips during track changes no longer interrupt head-unit playback indicators.

### Changed
  - Lower-latency metadata responses under sustained head-unit polling. Track-info exchange between the music app and the Bluetooth stack now uses shared memory (single-digit-ms reads vs ~25 ms before) with no torn reads at track edges.

### Added
  - `apply.bash --debug` build emits per-emit wire-side markers (`Y1T :` logcat tag) for diagnosing head-unit-specific AVRCP issues. Pair `tools/avrcp-wire-trace.py` with `tools/btlog-parse.py --avrcp` on a simultaneously-captured `btlog.bin` for the matching mtkbt-internal view.

## [2.3.0] - 2026-05-16

### Added
  - Stock firmware v3.0.7 support. `KNOWN_FIRMWARES` enrols the new build; `patch_y1_apk.py` accepts both 3.0.2 and 3.0.7 stock music APKs. MediaTek BT stack binaries (`mtkbt`, `libextavrcp*.so`, `libaudio.a2dp.default.so`, `MtkBt.odex`) are byte-identical between the two builds — `--avrcp` and `--bluetooth` patches apply unchanged. The music APK differs (resource-ID shifts, additional methods in `Y1Repository`); every smali anchor in `patch_y1_apk.py` (literal-text + the `AlbumsActivity.initView` regex) handles both builds.

## [2.2.0] - 2026-05-16

### Changed
  - AVRCP 1.3 §5.4.2 strict subscription gating in the trampoline chain — one CHANGED per CT registration; CT re-registers to receive the next. Matches reference-TG observed cadence on spec-compliant Controllers.
  - `mtkbt` outbound-frame drop bypass — every T9 / T5 CHANGED emit reaches the wire under sustained traffic (stock dropped silently under A2DP saturation).
  - TRACK_CHANGED `Identifier` carries the per-track audio ID so strict 1.4+ Controllers invalidate their `GetElementAttributes` cache on every track edge instead of serving stale metadata.
  - Faster perceived metadata refresh — TRACK_CHANGED pre-emits at `setDataSource` and at `playerPrepared` tail (was: `OnPreparedListener`, ~100-500 ms later). PLAYBACK_STATUS_CHANGED fresh-track edge fires ~260 ms earlier.
  - `GetCapabilities(EventsSupported)` advertises the 1.4+ event IDs (0x09-0x0c) alongside the 1.3 set — INTERIM-acked with zero payload. Strict Controllers gate metadata-pane render on these even from a 1.3-declared TG.
  - `--bluetooth``ro.bluetooth.class` accurately advertises the Y1 as Audio/Video Major / Portable Audio Minor with Audio + Information service bits.
  - `T_charset` rejects `InformDisplayableCharacterSet` with AV/C `NOT_IMPLEMENTED` (spec-permissible per AVRCP 1.3 §5.2.7, Optional) — avoids a multi-second pre-subscription stall some Controllers exhibit.

### Added
  - `GetElementAttributes` synthesises a `PlayingTime` via a synchronous `MediaMetadataRetriever` fallback for responses that arrive before `prepareAsync` completes — Controllers no longer see "0:00 duration" on track transitions.
  - `--debug` build path (`KOENSAYR_DEBUG=1`): native `__android_log_print` injection in `libextavrcp_jni.so` plus smali-side instrumentation in the metadata pipeline. Release builds are byte-identical without the env var.
  - `tools/btlog-hci-extract.py` decodes `mtkbt`'s `btlog.bin` as AVRCP frames for offline trace inspection.

### Fixed
  - `TrackInfoWriter.onSeek()` no longer treats the music app's post-`prepareAsync` "resume from saved progress" seek as a user seek (was: spurious wire-side `setSeekStatus`). Real user seeks (drag the seek bar) propagate unchanged.
  - TRACK_CHANGED no longer re-emits on the music app's same-track `prepareAsync` cycles (now dedup'd on audio ID).

## [2.1.0] - 2026-05-13

AVRCP 1.3 metadata + control pipeline over Bluetooth. A peer Controller now sees full track metadata, live play status, and play-state changes from the Y1, and can drive Repeat / Shuffle from its own UI. Reference docs: [`docs/BT-COMPLIANCE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FBT-COMPLIANCE.md), [`docs/ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md), [`docs/PATCHES.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FPATCHES.md). Investigation history: [`docs/INVESTIGATION.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md).

### Added
  - AVRCP 1.3 metadata (Title / Artist / Album / Genre / TrackNumber / TotalNumberOfTracks / PlayingTime), with UTF-8 codepoint-safe text truncation.
  - Live play status with millisecond-precision playhead, track-edge anchoring, end-of-track freeze + reset.
  - Track-change notifications, including TRACK_REACHED_END (on natural end-of-track) and TRACK_REACHED_START.
  - Battery-status notifications with bucketed change-on-edge semantics.
  - Seek-bar propagation — the music app's in-UI seek lands on the CT's playhead immediately.
  - Bidirectional Repeat / Shuffle. CT and Y1 UI stay in sync without navigating away and back.
  - Discrete PASSTHROUGH routing (PLAY / PAUSE / STOP / NEXT / PREVIOUS) for CTs that don't tolerate toggle behaviour, plus PLAY-while-playing → pause-toggle for non-spec CTs.
  - A2DP stream survives pauses — AudioFlinger silence-timeout no longer tears down the AVDTP source.
  - Per-subscription notification gating (AVRCP 1.3 §5.4.2) — one INTERIM + one CHANGED per registration, matching spec-compliant TG semantics.
  - `Y1Bridge` Android service satisfies MtkBt's `bindService(MediaPlaybackService)` and answers synchronous queries from the music-app-owned state file.
  - Spec-compliant `GetElementAttributes` response shape — TG emits exactly the requested attribute IDs in the requested order; unsupported IDs emit with length 0.

### Changed
  - GitHub repository renamed `y1-mods` → `koensayr`.
  - `--all` now includes `--avrcp`. The AVRCP 1.3 pipeline is spec-mature; the prebuild requirement (`./gradlew assembleDebug` in `src/Y1Bridge/`) mirrors `--root`'s `make` in `src/su/`.
  - `tools/release.sh --push` now pushes the current branch instead of hardcoded `main`. Bails with a clear error if invoked from a detached HEAD.

### Removed
  - Legacy SDP-only byte-patch attempts (regressed PASSTHROUGH without delivering metadata).
  - Legacy adbd byte-patch attempts (superseded by `src/su/`).

## [2.0.0] - 2026-05-04

Foundational rebrand + diagnostic tooling release. The `--avrcp` flag is documented as known-broken pending the user-space proxy work that becomes the [Unreleased] pipeline.

### Added
  - `src/btlog-dump/` — minimal ARM ELF that taps mtkbt's `@btlog` socket; pulls AVRCP / AVCTP / L2CAP traces invisible to `logcat`.
  - `tools/dual-capture.sh` + `tools/btlog-parse.py` — captures and decodes the btlog stream alongside `logcat`.
  - `tools/probe-postroot.sh` — one-shot device probe enumerating mtkbt internals, btsnoop paths, ptrace policy, abstract sockets.
  - `tools/release.sh` — release helper (version bump, CHANGELOG rewrite, tag).
  - `tools/install-android-sdk.sh` — auto-installs Android SDK for the `Y1Bridge` build.
  - `LICENSE` — canonical GPLv3 text (project has claimed GPLv3 since v1.0.8).

### Changed
  - Project rebrand `Innioasis Y1 Firmware Fixes` → `Koensayr`. GitHub repo name stays for discoverability.
  - Orchestration script renamed `innioasis-y1-fixes.bash` → `apply.bash`.
  - `--all` redefined as `--adb` + `--bluetooth` + `--music-apk` + `--remove-apps` + `--root`. `--avrcp` excluded.
  - `--avrcp` documented as known-broken on the byte-patch path; runs only on explicit opt-in with a startup warning.
  - `--bluetooth` no longer sets `persist.bluetooth.avrcpversion` (mtkbt can't deliver the claimed version). Pairing-essential edits remain.
  - `--artifacts-dir` is optional; defaults to `./staging/` inside the repo. `cp rom.zip staging/` is enough.
  - Project is now unambiguously Linux-only. macOS support removed (uses `mount -o loop` and GNU `sed -i`).
  - README, sub-READMEs, and `apply.bash --help` rewritten end to end for the new state.

### Fixed
  - Defensive hardening across `apply.bash` and helper scripts: pre-checks for `python3` / `sudo` / git config, exit-code checks on `simg2img` / `cp` / `mount` / `umount` / MTKClient flash, cleanup trap unmounts on EXIT, `--help` no longer triggers side effects in tools that previously ran setup work on it.
  - `--remove-apps` now actually removes apps (glob expansion was suppressed by quoting for the project's entire history).
  - Patcher `OUTPUT_MD5` mismatch now exits non-zero (was silently exit 0).
  - `tools/install-android-sdk.sh` license accept no longer fails silently under `set -o pipefail` (SIGPIPE on `yes`); partial-state downloads recover cleanly across re-runs.
  - `tools/setup.sh` partial-state bug — incomplete venvs are detected via a marker file and retried rather than appearing complete.

## [1.10.0] - 2026-05-03

### Added
  - `tools/setup.sh` — clones MTKClient at a pinned ref, builds the patcher's Python venv. Idempotent.
  - `--mtkclient-dir` / `--python-venv` flags + `MTKCLIENT_DIR` env var to override the in-tree tooling.

### Changed
  - Bash no longer assumes `/opt/mtkclient-2.1.4.1` paths. Resolution order: flag → env var → `tools/` default.

### Fixed
  - `src/Y1MediaBridge/` missing `local.properties` ignore + missing Gradle wrapper that prevented `./gradlew assembleDebug` from running.

## [1.9.1] - 2026-05-03

### Fixed
  - Switch `Y1MediaBridge` build target from `assembleRelease` to `assembleDebug` (avoids `lintVitalReportRelease` requiring a configured SDK path; both targets produce structurally identical APKs here).

## [1.9.0] - 2026-05-03

### Changed
  - `--avrcp` builds `Y1MediaBridge.apk` from in-tree source via Gradle. Previously expected a pre-staged APK.
  - `rom.zip` is the only required staged artifact.

## [1.8.x] - 2026-05-03

### Changed
  - Monorepo layout: `su/` → `src/su/`; byte/smali patchers → `src/patches/`; `Y1MediaBridge` imported as `src/Y1MediaBridge/`.
  - `apply.bash``show_help` and in-source comments trimmed to single-screen output. Authoritative detail moved to README + docs.

### Added
  - `CHANGELOG.md` (this file).
  - `docs/PATCHES.md` — per-patch byte-level reference.

## [1.8.0] - 2026-05-03

### Added
  - `--root` flag (current form): installs a minimal setuid-root `/system/xbin/su`. Stock `/sbin/adbd` stays untouched. `adb shell /system/xbin/su` gives root.
  - `src/su/` — ~900-byte direct-syscall ARM-EABI ELF, no libc, no manager APK.

## [1.7.0] - 2026-05-03

### Removed
  - Previous `--root` flag (boot.img `adbd` byte-patch). Hardware testing produced "device offline" — patched adbd brought up the USB endpoint but never completed the ADB handshake.

## [1.6.0] - 2026-05-03

### Changed
  - Accept the official OTA `rom.zip` as the primary firmware input. Bash MD5-validates against `KNOWN_FIRMWARES`, then extracts what each flag needs.

## [1.5.0] - 2026-05-03

### Changed
  - Stock-firmware MD5 validation against a `KNOWN_FIRMWARES` manifest (version, system.img, boot.img, rom.zip, music-APK basename). Replaces the previous hardcoded version constant.

## [1.4.x] - 2026-05-03

### Changed
  - `--avrcp` and `--music-apk` extract stock binaries from the mounted `system.img`, patch in place, and write back. Only `rom.zip` (and the `Y1MediaBridge.apk` build output) need staging.
  - Sparse-`system.img` auto-detection via `simg2img`.

## [1.3.x] - 2026-05-03

### Changed
  - Initial boot.img-based `--root` (later superseded by the setuid-su approach in 1.8.0). Direct cpio mutation in pure Python; no shell-side `dd` / `mkbootimg`.

## [1.2.x] - 2026-04-26 → 2026-05-01

### Added
  - Initial byte-patcher trio: `patch_mtkbt.py`, `patch_mtkbt_odex.py`, `patch_libextavrcp_jni.py`. Legacy SDP-shape byte-patch attempt (later determined inadequate and removed in 2.0.0).

## [1.1.x] - 2026-04-26

### Added
  - `--root` flag (ramdisk-based; broke at 1.2.0, reintroduced differently at 1.3.0, broken again, finally reworked at 1.8.0).

## [1.0.x] - 2026-04-23 → 2026-04-25

### Added
  - Initial release: Artist→Album navigation patch on the music app, Bluetooth pairing config (audio.conf / auto_pairing.conf / blacklist.conf / build.prop), preinstalled-bloatware removal, system patch dispatch via `apply.bash` flags.

These are Koensayr's own instructions, shown here word for word.

Published by the [ryan-specter/koensayr-auto](https://innioasis.app/firmware.html?model=Y1&software=koensayr-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=ryan-specter%2Fkoensayr-auto&software=koensayr-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aryan-specter)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
