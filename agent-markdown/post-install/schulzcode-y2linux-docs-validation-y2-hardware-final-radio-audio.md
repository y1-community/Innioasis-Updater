---
title: "Hardware Final radio and audio source work - Innioasis Updater"
description: "Hardware Final radio and audio source work <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-hardware-final-radio-audio.html"
---

# Hardware Final radio and audio source work - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Hardware Final radio and audio source work

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Hardware Final radio and audio source work > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-27. This supplement records source/host/ARM work; the coordinated campaign owns physical receipts and the final capability table. Temporary userspace probes do not replace the installed Hardware 02 kernel or authorize an intermediate firmware image.

## Current source, rather than the historical codec proposal

The September 22 Reborn codec audit describes BlueALSA 4.3.1 and missing trust, format and Auto policy. Current source already uses BlueALSA 5.0.0, BlueZ 5.87, libsbc 2.2, bounded Pairable/Bonded/Trusted/Connect operations, typed PCM Rate/Format/Channels, AVRCP registration and gated stopped-playback selection. [Current contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fplatform-bluetooth-v1.md) takes precedence. The checksum-offload advertisement repair is already in Hardware 02; PHY-001's checked DNS/TCP physical pass must not be presented as a new correction here.

## Owner-private optional encoder profile

`BR2_PACKAGE_Y2_CODEC_EXPERIMENTS` deliberately selects FDK-AAC 2.0.3, libfreeaptx 0.2.2 and LDAC encoder/ABR 2.0.2.3. BlueALSA enables AAC, aptX, aptX HD and LDAC together at compile time. The profile rejects libopenaptx, whose different licensing is unnecessary for this integration. Exact source URLs, archive hashes, commits, license-file hashes and distribution limits are in [codec-sources.json](https://github.com/schulzcode/y2linux/blob/HEAD/tools/production/codec-sources.json) and the Buildroot package recipes/hash files.

Source gates were checked against primary upstream material:
  - [FDK-AAC NOTICE](https://raw.githubusercontent.com/mstorsjo/fdk-aac/v2.0.3/NOTICE)

permits source/binary redistribution under its conditions, requires the notice and corresponding source, and grants no patent license. Public product patent/distribution approval remains unestablished.
  - [libfreeaptx 0.2.2 source](https://github.com/regularhunter/libfreeaptx/tree/0.2.2)

uses LGPL-2.1-or-later and implements ordinary aptX/aptX HD. Build a shared library and retain source/license material. No Adaptive, Lossless or product trademark clearance is claimed.
  - [LDAC complete release](https://innioasis.app/release_notes.html?author=EHfive&project=ldacBT&version=v2.0.2.3)

contains Linux CMake integration and the pinned Sony encoder/ABR source. The ordinary GitHub source tarball omits its submodule and cannot build it. Apache-2.0 source licenses and [AOSP NOTICE](https://android.googlesource.com/platform/external/libldac/+/2efdd91222c4c5f929335f34cbc3b576343cf1d2/NOTICE) are preserved; the latter requires product certification. Certification and public product distribution approval remain unestablished.
  - [BlueALSA 5.0.0 configuration](https://github.com/arkq/bluez-alsa/blob/v5.0.0/configure.ac)

has explicit FDK-AAC, libfreeaptx and LDAC configure paths. Codec libraries encode A2DP on the CPU; FFmpeg file decoding is unchanged.

These are owner-private qualification builds, not public release approval. Normal boot and supervised restart explicitly disable every compiled optional endpoint. This is necessary because upstream AAC is enabled by default when compiled; `--codec=SBC` alone does not turn AAC off. Mandatory SBC remains available. The generated inventory records compilation, private-experiment availability, default runtime state, public distribution gate and physical gate separately. Every `platform_qualified` flag remains false, so Auto cannot promote an unqualified codec. No manual preference is represented as the negotiated codec.

Validation completed during source work:
  - Exact archives and all listed license hashes verified; Buildroot Kconfig

selects the intended libraries and profile. Recipe modernization is idempotent.
  - FDK-AAC, libfreeaptx, LDAC encoder/ABR and BlueALSA 5.0.0 compile with the

retained ARMv7 hard-float compiler. The daemon links all four optional codec libraries; ELF has no RPATH/RUNPATH. ARM QEMU `bluealsad --help` executes and lists SBC/AAC/aptX/aptX-HD/LDAC source support.
  - Manifest rejection tests cover unexpected encoders, an incomplete experiment

profile, wrong aptX library, and unchanged Auto/public-distribution gates. Normal-service arguments disable every optional endpoint on both launch paths.
  - Full final-source Buildroot/package/installed-root validation is a separate

campaign requirement; the temporary component build cannot certify it.

Private working artifacts are under `out/hardware-final-codec-research/`. `target-codec-bundle.tar.gz` contains a temporary daemon, the four new shared libraries, generated manifest and SHA256SUMS. It replaces no root file, kernel, partition or calibration. The retained build logs include resolved initial CMake 4 policy and isolated-sysroot/libtool-path setup failures. Production's pinned CMake 3.31 path does not require the host CMake 4 compatibility option.

## Physical qualification without a flash

First retain Hardware 02 SBC PCM/audio evidence. Stop/release the application PCM before selection, hold the existing Bluetooth-operation lease, and suspend only the connectivity supervisor while substituting a temporary BlueALSA daemon; keep calibration, HCI, BlueZ and Wi-Fi alive. A cleanup trap must terminate the temporary daemon and resume the supervisor so its normal SBC-only daemon is restored. Never run two BlueALSA daemons under the same D-Bus name.

For AAC use the bundle library directory through `LD_LIBRARY_PATH`, `-p a2dp-source --codec=+AAC --codec=-aptX --codec=-aptX-HD --codec=-LDAC`. Retain mandatory SBC. AirPods Pro 2 are the available owner peer; observe actual GetCodecs and negotiated PCM before claiming AAC. Use `bluealsactl codec -c2 -r44100 PCM_PATH AAC` only with the PCM released and peer support observed. Do not use `--force` or raw codec blobs. Confirm sound/volume, CPU/temperature, XRUNs, disconnects, screen-off and coexistence before promotion. First use AAC's 220 kbps CBR default without afterburner; performance evidence may justify a later controlled option comparison.

aptX/HD and LDAC remain physically pending when no suitable peer is available. For each later supported peer, enable one optional endpoint plus SBC; test standard SBC first, then the requested codec, observing the result after every reconnect. LDAC modes are 303/606/909 kbps at 44.1-family or 330/660/990 at 48-family; standard quality is the initial controlled comparison. ABR capability is not a measured live bitrate. Keep highest quality out of Auto until sustained Wi-Fi-off/idle/scan/transfer audio and CPU evidence exists. A temporary daemon restart may cause an audible interruption; no seamless-switch claim is made.

## Internal wired audio and CS43131

The actual path is interleaved stereo S16 userspace -> ALSA managed DMA -> DL1 base/current/end -> AFE_DAC_CON1 rate and mono field -> I05/I06 -> O00/O01 -> second I2S_CON3 -> CS43131. Current rate codes are 9/10 for 44.1/48 kHz and period IRQ accounting is in frames. 32-bit serial slots do not change the 16-bit DMA fetch contract.

The donor `memif_data` explicitly has `hd_reg = -1`. The retained exact [MT6582 vendor AFE header](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/sound/mt6582/AudDrv_Afe.h) separates I2S word length from DL1 channel/rate fields; its rate enum ends at 48 kHz. Neither establishes high-definition DL1 alignment, wider interconnect transport or 88.2/96-kHz clock programming. This is insufficient evidence, not proof that the silicon is incapable. S24/S32, preserved 24-bit and 88.2/96 kHz remain BLOCKED_BY_HARDWARE_EVIDENCE. Do not add format masks or copy register layouts from newer MediaTek parts. Closure requires exact MT6582 fetch/packing and rate-field documentation or proven stock programming, followed by DMA low-bit fixtures and I2S MCLK/BCLK/LRCLK/word captures on this board.

The upstream CS43130/CS43131 driver already exposes hardware master volume, filter speed, phase compensation, high-pass and de-emphasis controls. Their presence is not additional board qualification. The Y2 DT deliberately uses ready-status polling and has no EINT16 or load-measurement properties. Upstream load work depends on measurement completion and may change headphone voltage; therefore impedance-driven gain remains disabled. Closure requires board interrupt/jack/load-path verification and controlled known-load measurements. 48-kHz S16 already has driver support and needs sustained Reborn playback, 44.1/48 transitions, screen-off and owner pop/click checks before product promotion.

## Wi-Fi observer and counters

PHY-020's timeout evidence must retain both the failure and the real network state. Platform Wi-Fi status now includes the exact `wpa_cli status` command failure and monotonic duration; the existing timeout is unchanged. A control query timeout cannot itself prove a disconnection.

Reborn previously counted every transition from COMPLETED to ERROR as `wifi_disconnects` and the next successful sample as `wifi_connects`. A transient STATUS timeout therefore manufactured an apparent link cycle. The counter tracker now preserves the last known association across missing/unknown observations and scans; explicit DISCONNECTED/INACTIVE/INTERFACE_DISABLED/OFF states count a disconnect. Current UI/error/readiness observations remain truthful rather than retaining a stale Online claim. Sequence tests cover repeated timeout recovery, scans/rekey, real disconnect/reconnect and radio off. Actual supplicant events/lease epochs remain separate evidence; a missed event cannot be reconstructed from sampled state.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
