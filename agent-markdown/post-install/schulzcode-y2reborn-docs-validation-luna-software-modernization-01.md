---
title: "LUNA Software Modernization 01 - Innioasis Updater"
description: "LUNA Software Modernization 01 <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-luna-software-modernization-01.html"
---

# LUNA Software Modernization 01 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# LUNA Software Modernization 01

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# LUNA Software Modernization 01 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Date: 2026-09-22 Scope: software stabilization, userspace modernization, reproducible ARMv7 candidate build Hardware scope: unchanged; no flash, boot-mode change, charging experiment, suspend experiment, bond change, credential change, protected-partition access, or Y2DATA replacement

## Starting state and audit basis

The full current-system audit (`docs/audit/current-system/00...15`) and the complete Bluetooth codec audit (`docs/architecture/bluetooth-codecs.md` plus `docs/audit/bluetooth-codecs/2026-09-22-evidence-and-tests.md`) were read before source changes.

Starting Y2Linux HEAD: `be7e64c5dd5c6bdfe39c35e8fbd70e6b4b2c4717` Starting Y2Reborn HEAD: `011884b7ef13187171225f252c213afeeb6da851` Starting Y2Linux worktree: no tracked modifications. Starting Y2Reborn worktree: reference-only untracked audit inputs under `docs/architecture/bluetooth-codecs.md` and `docs/audit/`; preserved throughout.

The standing roadmap boundary was not crossed: this session changed software inputs and validation only. Linux 6.18, the kernel configuration, DT memory reservations, PMIC/charger policy, AFE/I2S architecture, graphics ownership, eMMC layout, protected storage, preloader/LK/NVRAM/PROTECT, calibration, and factory material remained outside the change set.

## Focused commits

Y2Reborn:``````````````````

| Commit | Finding/package | Files or boundary | Tests/evidence | Limitation |
| --- | --- | --- | --- | --- |
| f9856bb | F01 media lifetime; seek trimming | crates/reborn-media/native/media.c and media wrapper | media decode/seek/cancel/fixture tests; workspace tests | allocator-aware target long-run remains unqualified |
| 86f9152 | F02 sink ownership; transition cancellation | playback and ALSA ownership boundary | playback sink failure, output switch and transition tests | no physical exclusive PCM run |
| e215df1 | F03/F08 queue authority | queue entry identity, collection intent, repeat and worker schedule | duplicate/queue-boundary/playback tests | no large-library target measurement |
| db1623b | F05/F06/F07 persistence and database commit semantics | library worker acknowledgement, scan finalization, bounded schema checkpoint, corrupt DB quarantine | library commit, ENOSPC/error, schema and quarantine tests | physical power-loss and full-card qualification remains open |
| 09465bf | F20/F21/F24/F25/F26 software truth | input loss/reopen timing, bounded glyph fallback, route/storage/artwork/metric state | platform, UI, observability and storage tests | broad font coverage and physical storage removal remain open |
| 42dc1f5 | BlueALSA 5 PCM negotiation and trust seam | typed negotiated PCM observation, final sink conversion, v5 Rate/Format, explicit Pair→Trusted | Bluetooth platform/audio tests; ARM BlueALSA integration build | no autonomous codec policy, AVRCP, or physical A2DP claim |

Y2Linux:``````````````````````

| Commit | Finding/package | Files or boundary | Tests/evidence | Limitation |
| --- | --- | --- | --- | --- |
| a6f3124 | reproducible dependency inputs | Buildroot lock, package versions/hashes, modernization transform, FFmpeg 9.0.2 | locked source/hash checks; clean Buildroot build | Buildroot remains on the 2025.02 LTS line |
| b74e2d1 | obsolete ALSA patch removal | modernization transform | fresh ALSA 1.2.16.1/1.2.16 ARM build | no hardware AFE change |
| cd5bca3 | BlueALSA 5 shared linking | generated v5 patch removes upstream -static link flag only | fresh bluealsad ARM link and rootfs inspection | patch remains local because v5 source still carries that flag |
| b94a671 | FFmpeg 9.0.2 receipt | exact SONAME verifier | fresh generated libav* verification | no general encoder/network/video stack enabled |
| 8e5b53b | build provenance correction | tools/production/build.py derives Y2_BUILD_ID from rootfs version | clean rebuild embeds PREMIUM-03; package validator passes | path-dependent old generated output was quarantined, never reused |

## F01–F32 audit status````````

| Finding | Status | Evidence and remaining limit |
| --- | --- | --- |
| F01 | FIXED | AVFrame ownership and adjacent error paths corrected; media workspace tests pass. |
| F02 | FIXED | Sink planning/reconfiguration is serialized with worker ownership; failure/rollback tests pass. |
| F03 | FIXED | Stable QueueEntryId and live future schedule preserve duplicate entries and mutations. |
| F04 | FIXED | FFmpeg crossfade output is chunked to the sink bound and preserves fallback audio; offered durations are tested. |
| F05 | FIXED | Batch and finalization acknowledgements gate scan success and pruning. |
| F06 | FIXED | Dirty, bounded, schema-versioned checkpoints and restore diagnostics replace periodic whole-session writes. |
| F07 | FIXED | Corrupt DB is quarantined before clean recreation; source media is retained. |
| F08 | FIXED | Album/artist/folder playback carries collection intent through the queue authority. |
| F09 | FIXED | AIFF, APE and WavPack discovery is aligned with target FFmpeg demuxers/decoders. |
| F10 | BLOCKED_BY_HARDWARE_SCOPE | Native wired S32/high-rate playback was explicitly excluded; no AFE/I2S/codec hardware policy changed. |
| F11 | PARTIALLY_FIXED | Coarse seek trimming, decoder/filter/resampler reset and transition timing were corrected; the full MP3/AAC/Opus/mixed-rate sample-boundary matrix remains. |
| F12 | PARTIALLY_FIXED | ReplayGain malformed/zero/non-finite/unreasonable values and limiter headroom policy are hardened; the empty EQ path remains deferred/disabled until it has useful configuration. |
| F13 | FIXED | Buildroot, FFmpeg and package inputs are pinned by URL/hash/source epoch; paired HEADs and rootfs identity are embedded and checked. |
| F14 | BLOCKED_BY_ARCHITECTURE_DECISION | Legacy Y2PlayerNative application fields still require a coordinated manifest/validator/consumer contract decision; changing one producer alone would make old fallback manifests invalid. |
| F15 | DEFERRED | Optional codec and owner-firmware/asset redistribution requires an explicit legal and distribution decision; no new optional codec was added. |
| F16 | BLOCKED_BY_HARDWARE_SCOPE | Charging/current/thermal and low-battery policy were not changed or experimented with. |
| F17 | BLOCKED_BY_HARDWARE_SCOPE | Suspend/resume and GPU recovery remain physical qualification work. |
| F18 | PARTIALLY_FIXED | Native Wi-Fi userspace remains bounded and current; association/IP/DNS/coexistence is not physically qualified here. |
| F19 | PARTIALLY_FIXED | BlueZ/BlueALSA/SBC software stack, v5 adapters, format truth and trust seam are updated; pairing, A2DP stability, reconnect and AVRCP remain physical/feature qualification. |
| F20 | FIXED | Queued release ordering, timestamp aging, SYN_DROPPED, reopen and screen-off repeat behavior have targeted tests. |
| F21 | PARTIALLY_FIXED | Storage/SD identity, route state and bounded Unicode fallback are corrected; broad glyph coverage remains limited. |
| F22 | BLOCKED_BY_HARDWARE_SCOPE | Renderer recovery and suspend/pageflip lifetime were not tested on the device. |
| F23 | DEFERRED | Large-library query-backed scaling was outside this stabilization pass. |
| F24 | PARTIALLY_FIXED | Stable entry-aware artwork state and cache handling were corrected; full sidecar invalidation qualification remains. |
| F25 | FIXED | Packet/status/scan completion semantics no longer overstate success or double-count cumulative values. |
| F26 | PARTIALLY_FIXED | Software error propagation and reporting were improved; hot removal/full filesystem behavior still needs target qualification. |
| F27 | PARTIALLY_FIXED | Fresh Rust, production, ARM, FFmpeg, rootfs, ELF and package evidence exists; broad historical host discovery still has environment/profile failures documented below. |
| F28 | DEFERRED | Current target CPU/RAM/wakeup budgets were not invented or claimed without measurements. |
| F29 | BLOCKED_BY_HARDWARE_SCOPE | Board contracts, reservations, sequencing and thermal assumptions were preserved; no new hardware boundary was crossed. |
| F30 | DEFERRED | Legacy/reference cleanup was not mixed into the stabilization changes. |
| F31 | PARTIALLY_FIXED | A checked preserving BOOTIMG+ANDROID system-update profile and exact fallback are packaged; independent manual installation/recovery remains unperformed. |
| F32 | ALREADY_RESOLVED | Existing bounded private diagnostics, redaction, key-only SSH and malformed-input boundaries remain intact. |

## Dependency inventory and decisions

Versions were checked against official release/tag/download sources and the fresh Buildroot output. `UPGRADED` means the final shipped input changed in this pass; `HELD` means the current version was retained deliberately.````````

| Dependency | Old | Newest stable considered | Final | Decision and reason |
| --- | --- | --- | --- | --- |
| Buildroot | 2025.02.17 | 2026.08 | 2025.02.18 | UPGRADED to the latest 2025.02 LTS bugfix; 2026.08 held for broad Buildroot/hardware qualification scope. |
| Linux | 6.18 Y2 tree | current supported stable/LTS line | 6.18.0-y2linux-gpu-02 | HELD; vendor board contracts and physical qualification dominate freshness. |
| Rust toolchain | 1.90.0 pinned | 1.98.1 | 1.90.0 | HELD; ARMv7/Buildroot cross-build is clean and replacing the ABI/toolchain is outside this pass. |
| GCC/binutils/glibc | Bootlin armv7-eabihf glibc 2024.05-1 | Bootlin 2026.08-1: GCC 15.3, binutils 2.45.1, glibc 2.44 | Bootlin 2024.05-1 | HELD; whole ABI/toolchain replacement requires separate qualification. |
| FFmpeg | 9.0.1 | 9.0.2 | 9.0.2 | UPGRADED; official stable security/bugfix release, exact audio-only component set and hash verified. |
| BlueZ | 5.79 | 5.87 | 5.87 | UPGRADED; current stable, local obsolete patches removed after source review. |
| BlueALSA | 4.3.1 | 5.0.0 | 5.0.0 | UPGRADED; v5 API/source was inspected and Reborn uses bluealsad, Rate, and Format deliberately. |
| libsbc | 2.0 | 2.2 | 2.2 | UPGRADED; mandatory SBC remains the only enabled A2DP codec. |
| ALSA lib/utils | 1.2.13 | 1.2.16.1 / 1.2.16 | 1.2.16.1 / 1.2.16 | UPGRADED; obsolete no-MMU/rawmidi patches removed for the MMU Cortex-A7 target. |
| SQLite | 3.50.4 | 3.53.4 | 3.53.4 | UPGRADED; single writer and schema contract retained. |
| OpenSSL | 3.5.7 | 3.5.8 | 3.5.8 | UPGRADED through the selected Buildroot LTS bugfix. |
| expat | 2.8.3 | 2.8.4 | 2.8.4 | UPGRADED through the selected Buildroot LTS bugfix. |
| Dropbear | 2026.93 | 2026.94 | 2026.94 | UPGRADED; persistent key-only SSH contract retained. |
| BusyBox | 1.37.0 | 1.37.0 stable (1.38.0 not stable) | 1.37.0 | HELD/CURRENT; no unstable release adopted. |
| D-Bus | 1.14.10 | 1.16.2 | 1.14.10 | HELD; 1.16 is a Meson/package migration with wider service qualification impact. |
| wpa_supplicant | 2.12 | 2.12 | 2.12 | CURRENT; no newer stable suitable input in the selected Buildroot line. |
| Mesa | 24.0.9 | 26.1.8 | 24.0.9 | HELD; Lima/Mali400 renderer and KMS/GBM/EGL/GLES2 need a separate physical graphics qualification. |
| libdrm | 2.4.124 | 2.4.134 | 2.4.124 | HELD with Mesa for the same renderer/UAPI qualification boundary. |
| e2fsprogs | 1.47.2 | 1.47.2 | 1.47.2 | CURRENT. |
| dosfstools | 4.2 | 4.2 | 4.2 | CURRENT. |
| util-linux | 2.40.4 | 2.40.x | 2.40.4 | HELD; no reason to widen the storage qualification surface for an incremental update. |
| zlib | 1.3.2 | 1.3.2 | 1.3.2 | CURRENT; actual provider is Buildroot libzlib. |
| libpng | 1.6.58 | 1.6.58 | 1.6.58 | CURRENT. |
| libjpeg-turbo | 2.1.5 | newer upstream | 2.1.5 | HELD; no image-stack migration was required for the current FFmpeg/artwork membrane. |
| libwebp | 1.5.0 | 1.5.0 | 1.5.0 | CURRENT. |
| libffi | 3.4.6 | newer upstream | 3.4.6 | HELD; unrelated ABI migration. |
| direct Rust crates | serde 1.0.228, serde_json 1.0.145, libc 0.2.177, cc 1.2.41, pkg-config 0.3.32, rusqlite 0.37.0, dbus 0.9.9, flate2 1.1.5, tar 0.4.44 | current pinned stable releases evaluated | unchanged exact pins | CURRENT; no unconstrained lockfile churn, workspace checks pass. |

Official source references used: [Buildroot downloads](https://buildroot.org/downloads/), [FFmpeg downloads](https://ffmpeg.org/download.html), [BlueZ releases](https://www.kernel.org/pub/linux/bluetooth/), [BlueALSA 5.0.0](https://innioasis.app/release_notes.html?author=arkq&project=bluez-alsa&version=v5.0.0), [BlueALSA migration notes](https://github.com/arkq/bluez-alsa/wiki/Migrating-from-release-4.3.1-or-earlier), [SQLite changes](https://sqlite.org/changes.html), [ALSA downloads](https://www.alsa-project.org/wiki/Download), [D-Bus releases](https://dbus.freedesktop.org/releases/dbus/), [Dropbear releases](https://matt.ucc.asn.au/dropbear/releases.html), [Bootlin ARMv7 toolchains](https://toolchains.bootlin.com/releases_armv7-eabihf.html), and [Rust release announcements](https://blog.rust-lang.org/releases/).

## Bluetooth modernization record

The codec-audit assumptions that remain valid are the one FFmpeg decode/DSP path, one final sink conversion, BlueALSA/BlueZ/HCI ownership, SBC as the compatible fallback, one reconnect owner, no optional-codec auto-enable, and the distinction between requested, negotiated, and physically qualified behavior.

The changed assumptions are version-specific BlueALSA details: v5 ships `bluealsad`/`bluealsactl`, uses `Rate` rather than the audited v4 `Sampling` property, exposes the negotiated PCM `Format` with v5 semantics, and required a small shared-link patch because the source build flags still injected `-static`. BlueZ is 5.87; its current source absorbed the obsolete local patches. No 4.3.1 D-Bus property names were carried forward silently.

The fresh rootfs compiles and installs BlueALSA 5.0.0 with SBC only. AAC, aptX, aptX HD, LDAC, LHDC, LC3plus, FastStream and other optional codecs are disabled. Reborn now decodes the observed BlueALSA format into a typed sink contract: S16, S24 in a 4-byte container, and S32 are represented explicitly; unsupported/packed formats fail closed. The final FFmpeg conversion is selected from the negotiated PCM object, never inferred from the codec label.

The safe foundation is observation, not an autonomous negotiation engine: typed Bluetooth PCM observation and current codec display exist, but no reconnect loop, background codec probing, per-packet policy, adaptive LDAC contract, or per-device codec profile was invented. AVRCP application integration was not added. Pairing only establishes BlueZ `Trusted` after explicit user confirmation; `y2-bt-reconnect` remains the sole connection retry owner. No physical A2DP, reconnect, RF coexistence, AVRCP or optional-codec qualification is claimed.

## Validation and evidence tiers

Fresh source identities for the candidate are Y2Linux `8e5b53bc9fb934e1f668b9e7e9e34f0fc5e4130e` and Y2Reborn `42dc1f562d00439e8edcbb52fc070be28a69378e`. The later work-log-only Y2Reborn commit does not change the shipped source.``````````

| Check | Result | Evidence tier / limitation |
| --- | --- | --- |
| cargo fmt --all -- --check | PASS | source, fresh current workspace |
| cargo check --workspace --locked | PASS | source, locked dependencies |
| cargo test --workspace --locked | PASS | app 6, control 1, audio 2, control library 5, core 7, library 8, media 15, observability 13, platform 24, UI 10; no device claim |
| Y2Linux tools/production/tests.sh in locked build environment | PASS | production/storage/connectivity/power/GPU/ABI suites; no flash |
| Targeted Y2Linux Python tests | PASS | connectivity/power/Wi-Fi/GPU and production/format/storage/handover tests; two documented skips |
| Fresh ARMv7 Buildroot | PASS | clean output directory, Buildroot 2025.02.18, current Y2Linux HEAD, owner firmware supplied only as a local build input |
| FFmpeg component verifier | PASS | FFmpeg 9.0.2, expected audio decoders/demuxers/filters, exact generated SONAMEs |
| Rootfs/ELF/package validation | PASS | ARM hard-float ELF checks, rootfs ownership/contracts, BlueZ/BlueALSA/SBC inventory, preserving manifest and rootfs checks |
| Candidate hash check | PASS | SHA256SUMS verifies every packaged file |
| Broad historical host discovery | LIMITED | 123-test locked sweep had one failure and 42 errors from environment/profile mismatches (QEMU/fixture/config assumptions); the focused production suite passed and failures were not suppressed |
| Physical Y2 qualification | NOT RUN | explicitly outside this session |

## Candidate and update boundary

Candidate package: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-reborn-software-modernization-01/` Fresh build receipt: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-reborn-software-modernization-01-build/` Fallback is retained inside the candidate under `fallback/`; the candidate contains no `Y2DATA.img`.````````````````

| File | SHA-256 |
| --- | --- |
| BOOTIMG.img | e6625ba5a7b3a94e91fa70a41a1b4ea64ae7a68e3228f0213173ee7c2afdf8bd |
| Y2ROOT.img | 59548c18d010016e1434f2abe6b972e0d5ebc9ba580e5a08f1e2dde3ef62e524 |
| manifest.json | 2b577f114ba39f6b9aa4145374116af4548b5305d6f85b084a6fc14b56c3779c |
| SHA256SUMS | d49fc51403c7ce3f2700b21bd429096a788fa36582c3dc9cfb6033b902e0169f |

The manifest is `system-update`, selects only `BOOTIMG` and `ANDROID`, retains layout/data schema 1, and records `build_git_commit == rootfs_build_git_commit == 8e5b53b...`. Kernel source/config architecture stayed at Linux 6.18; `BOOTIMG.img` was regenerated as the normal fresh candidate container, without kernel policy or hardware changes.

Safe manual update procedure, when separately approved: verify `SHA256SUMS` and `manifest.json` offline; retain a copy of the candidate and its `fallback/`; use only the included `MT6582_preserve_data_scatter.txt`; in the existing owner-approved SP Flash Tool workflow select `BOOTIMG` and `ANDROID` only; leave `USRDATA`/`Y2DATA`, preloader, LK, NVRAM, PROTECT, calibration and factory regions unselected; verify readback with the included readback plan and hashes before booting. Do not use the first-install scatter or data image for this candidate. This session performed none of those physical steps.

## Remaining blockers

The remaining work is chiefly the coordinated F14 manifest contract, distribution/legal closure for private firmware/assets and optional codecs, physical wired-audio and Bluetooth qualification, graphics/Lima recovery and suspend qualification, target long-run memory/XRUN/input/storage tests, and the broad-test environment/profile cleanup. No kernel/BOOTIMG policy change, charging change, suspend change, memory reservation change, eMMC translation change, or protected-partition operation is part of this candidate.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
