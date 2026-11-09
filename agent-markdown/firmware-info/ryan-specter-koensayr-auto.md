---
title: "About Koensayr (Y1) - README.md - Innioasis Updater"
description: "A Y1 custom Software maintained by the community."
language: "en"
source: "https://innioasis.app/firmware-info/ryan-specter-koensayr-auto.html"
---

# About Koensayr (Y1) - README.md - Innioasis Updater

[← Firmware Downloads](../firmware.html)

Firmware README · Y1

# About Koensayr

A Y1 custom Software maintained by the community.

Also known as: README.md · ryan-specter/koensayr-auto · koensayr-auto · Koensayr · ryan-specter-koensayr-autoY1[Open the Koensayr guide](../guides/koensayr-y1.html)[Install with Updater CE](../firmware.html?model=Y1&software=koensayr-y1)[Why Koensayr?](../koensayr-benefits.html)Downloads from Firmware Archive1,110

# Koensayr

Innioasis Y1 firmware patcher & research toolkit (MT6572 / Android 4.2.2)

(The project name is a Star Wars deep cut: Koensayr Manufacturing made the Y-Wing starfighter; Y-Wing → Y1.)

## Overview
  - Music-player UX — Artist→Album navigation on the system music APK.
  - Bluetooth pairing — audio.conf / auto_pairing.conf / blacklist.conf / build.prop edits for car and headset pairing.
  - System config — enable ADB debugging, remove preinstalled bloatware.
  - Root — install `/system/xbin/su` (setuid, mode 06755) for `adb shell /system/xbin/su` escalation. Stock `/sbin/adbd` stays untouched.
  - AVRCP 1.3 metadata + control over Bluetooth — peer Controller sees full track metadata, ms-precision playhead, track / battery notifications, and bidirectional Repeat / Shuffle. Spec-compliant AVRCP 1.3 TG.
  - Investigation tooling — diagnostic scripts (`@btlog` tap, dual-capture, post-root probe, gdbserver attach). Not invoked by the patch flow — see [Diagnostics](#diagnostics).

Compatibility is defined by [`KNOWN_FIRMWARES`](#stock-firmware-manifest) in `apply.bash`; add a row to enrol a new build.

## Layout

The bash entry-point at the root dispatches into source trees under `src/`:
  - `apply.bash` — single entry point; flag-driven dispatch into the trees below
  - [`src/patches/`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/src/patches/) — byte/smali patchers (`patch_*.py`); see [`src/patches/README.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fsrc%2Fpatches%2FREADME.md) for the per-patcher table and [`docs/PATCHES.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FPATCHES.md) for byte-level detail
  - [`src/su/`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/src/su/) — minimal setuid-root `su` for `--root` (~1-2 KB direct-syscall ARM-EABI ELF, no libc). Build via `cd src/su && make`
  - [`src/Y1Bridge/`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/src/Y1Bridge/) — Android service app source for `Y1Bridge.apk` (consumed by `--avrcp`; hosts the Binder declaration MtkBt resolves to). Build via `cd src/Y1Bridge && ./gradlew --stop && ./gradlew assembleDebug`
  - [`src/btlog-dump/`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/src/btlog-dump/) — `@btlog` abstract-socket reader (diagnostic; same toolchain as `src/su/`). Build via `cd src/btlog-dump && make`
  - `tools/` — setup, diagnostic, and release helpers
  - `staging/` — default `--artifacts-dir`; drop `rom.zip` here

## Quick start

One-time setup (clones tooling, builds the prebuilt artifacts `--all` needs):`./tools/setup.sh # MTKClient + Python venvs ( cd src/su && make ) # setuid-su for --root ./tools/install-android-sdk.sh && source tools/android-sdk-env.sh ( cd src/Y1Bridge && ./gradlew --stop && ./gradlew assembleDebug ) # Y1Bridge.apk for --avrcp`

Then stage `rom.zip` (the official OTA — MD5-validated against [`KNOWN_FIRMWARES`](#stock-firmware-manifest)) and run:`cp /path/to/rom.zip staging/ ./apply.bash --all`

`--all` = `--adb --avrcp --bluetooth --music-apk --remove-apps --root`.

The bash extracts `system.img` from `rom.zip`, loop-mounts it, applies the patches in-place, unmounts, and flashes via MTKClient. Subdirectory build outputs and `tools/` contents are picked up automatically.

Anything under `staging/` other than its tracked README is `.gitignore`d. `git clean -dfx` will nuke staged firmware along with build artifacts — keep a backup of `rom.zip`, or pass `--artifacts-dir <path>` to stage elsewhere.

Override bundled tooling with `--mtkclient-dir <path>` / `--python-venv <path>` (or `MTKCLIENT_DIR` env).

### Flags````````````````````````````[``](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FPATCHES.md)[``](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md)````````````````````````````````````````````````````````

| Flag | Effect |
| --- | --- |
| --adb | Append persist.service.adb.enable=1 + persist.service.debuggable=1 to build.prop. |
| --avrcp | AVRCP 1.3 metadata pipeline: patches mtkbt, libextavrcp.so, libextavrcp_jni.so, MtkBt.odex, libaudio.a2dp.default.so, usr/keylayout/AVRCP.kl, plus Y1Bridge.apk install. Pre-requires gradlew assembleDebug in src/Y1Bridge/. Patch ID legend in docs/PATCHES.md; architecture in docs/ARCHITECTURE.md. |
| --bluetooth | Pairing-essential audio.conf / auto_pairing.conf / blacklist.conf / build.prop edits. Required for car pairing. |
| --music-apk | Patch Y1 music player APK (Artist→Album navigation; discrete PASSTHROUGH routing; media-key propagation; Y1Bridge smali injections). |
| --remove-apps | Remove bloatware (ApplicationGuide, BasicDreams, …). |
| --root | Install src/su/build/su at /system/xbin/su (mode 06755). Pre-requires make in src/su/. |
| --all | All of the above. Pre-requires the src/su/ + src/Y1Bridge/ builds. |
| --no-flash | Patch only; write system-*-devel.img without MTKClient flash (CI / repack). |
| --accept-any-firmware | Skip KNOWN_FIRMWARES MD5 checks; use --firmware-slug when unknown. Implies --skip-md5 on patchers. |
| --firmware-slug <id> | Output label when upstream rom.zip is not in the manifest (e.g. y1-stock-rom-2.8.2). |
| --skip-md5 | Bypass stock-binary MD5 gates in patch_*.py (diagnostic / CI). |

Run `./apply.bash --help` for full flag detail. Patchers can also be run standalone — see [`src/patches/README.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fsrc%2Fpatches%2FREADME.md).

## Diagnostics

Post-root tools for investigating AVRCP behaviour on hardware. None are invoked by the patch flow. Pre-req: `--root` flashed.
  - `@btlog` tap — `src/btlog-dump/` (no-libc ARM ELF) + `tools/dual-capture.sh` (push + run + capture btlog & logcat) + `tools/btlog-parse.py` (decode framing).
  - Post-root probe — `tools/probe-postroot.sh` + `tools/probe-postroot-device.sh`. Enumerates PIE base, debug nodes, btsnoop paths, `getprop` keys, ptrace policy, abstract sockets.
  - gdbserver attach to mtkbt — `tools/install-gdbserver.sh` + `tools/attach-mtkbt-gdb.sh`. Pulls a pinned static ARM gdbserver, attaches to the live PID, generates a breakpoint command file at the AVCTP-RX classifier + dispatcher arms.

Background on the failed alternatives these tools replace: [`docs/INVESTIGATION.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md).

## Status

`--all` produces a working device: Bluetooth pairing, A2DP audio, AVRCP 1.3 metadata + control, `--root`, `--music-apk` / `--remove-apps` / `--adb`. Every Mandatory and Optional ICS Table 7 (Target Features) row closes. Per-row scorecard: [`docs/BT-COMPLIANCE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FBT-COMPLIANCE.md). Architecture: [`docs/ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md).

## Stock firmware manifest

Known stock firmwares recognised by `KNOWN_FIRMWARES` in the bash. Add a row (same five-field schema) to enrol a new build.``````````````[](https://innioasis.app/firmware.html?model=Y1&software=original-y1)``````

| Version | system.img (raw, extracted) | boot.img (in zip; not consumed since v1.7.0) | rom.zip (input) | Music APK basename in app/ |
| --- | --- | --- | --- | --- |
| 3.0.2 | 473991dadeb1a8c4d25902dee9ee362b | 1f7920228a20c01ad274c61c94a8cf36 | 82657db82578a38c6f1877e02407127a | com.innioasis.y1_3.0.2.apk |
| 3.0.7 | 663baf9f… (Innioasis sparse→raw) or 017d62eb… (y1-community pre-expanded) | 83b946d1799b4f0281ba8e808ed7911b | aa9847088859176c76d8e203970e7032 | com.innioasis.y1_3.0.7.apk |

The MediaTek BT stack (`bin/mtkbt`, `lib/libextavrcp*.so`, `lib/libaudio.a2dp.default.so`, `app/MtkBt.odex`) is byte-identical between 3.0.2 and 3.0.7 — every native patch in `--avrcp` / `--bluetooth` applies unchanged. Only the music APK differs (resource-ID shifts + a few additions in `Y1Repository`), and `patch_y1_apk.py`'s smali anchors handle both builds.

Stock sizes: 3.0.2 `rom.zip` 259,502,414 bytes (raw `system.img` inside); 3.0.7 `rom.zip` from Innioasis may ship a sparse `system.img` (auto-de-sparsed via `simg2img`), while [y1-community/y1-stock-rom](https://innioasis.app/firmware.html?model=Y1&software=original-y1) releases use the same `rom.zip` MD5 but a pre-expanded raw `system.img`. Both raw `system.img`s are 681,574,400-byte ext4. `boot.img` 4,706,304 bytes on both.

## Requirements
  - Linux host, Bash 4+, `sudo`. The patcher uses `mount -o loop` and GNU `sed -i` syntax — both Linux-only. macOS users would need a Linux VM (Lima, OrbStack, UTM) or a remote Linux shell.
  - `git`, `unzip`, `md5sum`.
  - Python 3.8+ with `venv` module. Patcher byte-level scripts are stdlib-only; `patch_y1_apk.py` needs `androguard`, which `tools/setup.sh` installs into `tools/python-venv/`. Java 11+ also required for `--music-apk` (apktool's smali assembler; apktool itself is downloaded by `patch_y1_apk.py` on first invocation).
  - `tools/setup.sh` clones MTKClient (currently pinned to 2.1.4.1) into `tools/mtkclient/` and creates `tools/mtkclient/venv/` with its requirements. Override with `--mtkclient-dir <path>` or `MTKCLIENT_DIR` if you have it elsewhere.
  - `simg2img` — only if the matched `KNOWN_FIRMWARES` build bundles a sparse `system.img` (v3.0.2 is raw; v3.0.7 is sparse). Install: `dnf install android-tools` (Fedora / RHEL via EPEL), `apt install android-sdk-libsparse-utils` (Debian / Ubuntu), `pacman -S android-tools` (Arch).
  - For `--root` only: prebuilt `src/su/build/su` (`cd src/su && make`). Toolchain: `dnf install -y epel-release && dnf install -y gcc-arm-linux-gnu binutils-arm-linux-gnu make` (Rocky/Alma/RHEL/Fedora) or `gcc-arm-linux-gnueabi` on Debian/Ubuntu.
  - For `--avrcp` only: Android SDK + JDK 17+. `tools/install-android-sdk.sh` auto-installs into `tools/android-sdk/` (~1.5 GB, idempotent). Manual instructions: [`docs/ANDROID-SDK.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FANDROID-SDK.md).

## Automated releases (GitHub Actions)

Workflow [`.github/workflows/build-firmware-releases.yml`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/.github/workflows/build-firmware-releases.yml) builds an allowlisted set of [y1-stock-rom](https://innioasis.app/firmware.html?model=Y1&software=original-y1)`rom.zip` releases only:
  - Upstream tags 3.0.2 and Latest-3.0.7 (published as `{koensayr-version}-koensayr-3.0.2` / `{koensayr-version}-koensayr-3.0.7`)

For each input it downloads upstream `rom.zip`, verifies SHA256 (from the release asset) and MD5 against [`KNOWN_FIRMWARES`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/apply.bash), runs `./apply.bash --all --no-flash`, repacks `rom.zip`, and publishes a release on this repo.

Release tag pattern:`{koensayr-version}-koensayr-{firmware-version}` (e.g. `2.4.0-koensayr-3.0.7`) for Innioasis Updater compatibility. Release notes start with [`.github/workflows/workflow.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2F.github%2Fworkflows%2Fworkflow.md). Each release attaches `rom.zip` (patched) plus `build-manifest.json`.

Download from this repo’s release tag, not from [y1-community/y1-stock-rom](https://innioasis.app/firmware.html?model=Y1&software=original-y1) — upstream `rom.zip` is stock (~238–259 MB). Patched builds are larger (~295–329 MB) and have a different SHA256 (listed in the release notes / manifest).``````

| Release | Expected rom.zip size (approx.) | Patched SHA256 (May 2026 CI) |
| --- | --- | --- |
| *-koensayr-3.0.2 | 329,015,308 bytes (May 2026 CI) | 2371ac0970c0dbac318077373467859439aa0414caa15e29b90d8e879b8bbd80 |
| *-koensayr-3.0.7 | 309,073,126 bytes (May 2026 CI) | 2fa3fb7bf9ced11a21d0ce3bd0aec8a521dd3c6f22d9e0be8301b9ca3951dddb |

Triggers: weekly schedule, pushes to `main` that touch patcher/CI paths (always republish both firmware tags; existing releases are deleted and recreated), and manual `workflow_dispatch` (optional `force` / `source_repo` filter).

Confidence: Stock 3.0.2 / 3.0.7 OTAs are hardware-verified. See [`docs/SUPPORTED-FIRMWARE-CI.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FSUPPORTED-FIRMWARE-CI.md).

Local dry-run (no GitHub publish):`KOENSAYR_SKIP_PUBLISH=1 ./tools/ci/build-one.sh \ --source-repo y1-community/y1-stock-rom --source-tag 3.0.2 \ --release-tag 2.4.0-koensayr-3.0.2 \ --download-url "$(gh release view 3.0.2 --repo y1-community/y1-stock-rom --json assets -q '.assets[] | select(.name==\"rom.zip\") | .url')" \ --digest "$(gh release view 3.0.2 --repo y1-community/y1-stock-rom --json assets -q '.assets[] | select(.name==\"rom.zip\") | .digest' | sed 's/sha256://')" \ --slug y1-stock-rom-3.0.2`

## Documentation
  - [CHANGELOG.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2FCHANGELOG.md) — version history (Keep a Changelog format)
  - [docs/SUPPORTED-FIRMWARE-CI.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FSUPPORTED-FIRMWARE-CI.md) — CI upstream mapping and build expectations
  - [docs/ANDROID-SDK.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FANDROID-SDK.md) — Android SDK install instructions (only needed for `--avrcp` / Y1Bridge build)
  - [docs/ARCHITECTURE.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md) — AVRCP metadata proxy architecture: data-path diagram, trampoline chain, response-builder calling conventions, ELF segment-extension technique, code-cave inventory. Read this first if working on the metadata pipeline.
  - [docs/BT-COMPLIANCE.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FBT-COMPLIANCE.md) — current ICS Table 7 coverage scorecard (every Mandatory + every Optional row)
  - [docs/INVESTIGATION.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md) — chronological AVRCP investigation history, refuted hypotheses, trace log
  - [docs/PATCHES.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FPATCHES.md) — per-patch byte-level reference (offsets, before/after bytes, rationale)

## Deployment notes

The patched music-player APK must land in `/system/app/`, not via `adb install` / PackageManager — its stale META-INF only satisfies the parseable-signature requirement when filesystem-deployed at boot. `apply.bash --music-apk` handles this. Manual ADB push:`adb root && adb remount adb push com.innioasis.y1_<version>-patched.apk /system/app/com.innioasis.y1/com.innioasis.y1.apk adb shell chmod 644 /system/app/com.innioasis.y1/com.innioasis.y1.apk adb reboot`

## Verified against

Innioasis Y1 — MTK MT6572 ARM, Android 4.2.2. Hardware-verified against the v3.0.2 and v3.0.7 firmwares in [`KNOWN_FIRMWARES`](#stock-firmware-manifest); other builds need a manifest row added and may need patch-site offsets re-located if their stock MD5s diverge.

## Author

Sean Halpin ([github.com/SeanathanVT](https://github.com/SeanathanVT))

## License

GNU General Public License v3.0 (GPLv3) — see [LICENSE](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/LICENSE).

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
