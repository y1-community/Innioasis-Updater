---
title: "Bluetooth platform v1 contract - Innioasis Updater"
description: "Bluetooth platform v1 contract Superseded since Beta 9.3: one radio daemon owns Bluetooth, see radio-daemon.md radio-daemon.md. y2-bt-reconnect , bluetooth-power , the in"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-bluetooth-v1.html"
---

# Bluetooth platform v1 contract - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Bluetooth platform v1 contract

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Bluetooth platform v1 contract

Superseded since Beta 9.3: one radio daemon owns Bluetooth, see [radio-daemon.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fradio-daemon.md). `y2-bt-reconnect`, `bluetooth-power`, the intent file and the operation/PCM locks below no longer exist.

## Current Baseline02 source and qualification scope

CONSYS/HCI, BlueZ 5.87 and BlueALSA 5.0.0 remain radio/transport/encoder owners; Reborn retains decode/DSP and final conversion. Calibration, bonds and owner data stay private. `y2-bt-reconnect` remains the sole automatic connection owner. Requested preference, mutual availability, negotiated PCM and qualification remain separate; observation does not activate a radio or certify a peer.

The current owner-private integration profile builds and enables optional AAC/aptX/aptX-HD/LDAC endpoints through validated codec policy. SBC remains the baseline. Quality defaults are SBC high, LDAC standard and requested LDAC ABR; private SBC xq/xq+ controls are available. Compiled library, configured quality and requested ABR do not prove active negotiated output or adaptation. The public/SBC-only and earlier optional-disabled experiment profiles are separate configurations; neither is the current private Baseline02 default.

Private integration does not grant public redistribution or qualified Auto promotion. Earlier bounded owner-confirmed SBC peer playback remains its named receipt. The UART01 CPU-idle campaign uses a Wi-Fi observer with radios off for C3 entry; it does not qualify optional Bluetooth peer/CPU/coexistence/endurance. Baseline02's new-image/cold-boot tests are pending. Current source/API references: [codec inventory](https://github.com/schulzcode/y2linux/blob/HEAD/tools/production/codec_manifest.py), [quality controls](https://github.com/schulzcode/y2linux/blob/HEAD/tools/platform/y2_platform/codec_controls.py), [Bluetooth observation](https://github.com/schulzcode/y2linux/blob/HEAD/tools/platform/y2_platform/bluetooth.py), [service arguments](https://github.com/schulzcode/y2linux/blob/HEAD/buildroot/board/y2/production-overlay/usr/libexec/y2/connectivity), [feature inventory](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md) and [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md).

## Bluetooth optimization source contract — 2026-10-04

The [optimization receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BLUETOOTH-OPTIMIZATION.md) records the measured Baseline02 idle baseline and localized follow-up. The reconnect owner now consumes a GIO ObjectManager signal cache, watches explicit intent replacements, addresses the unique BlueZ owner, and uses one-shot retry and connection-stability deadlines. Its 5s status heartbeat performs no recurring D-Bus enumeration. Two attempts, 10s call timeout, 25s episode, 30s stable-link rearming and boot-bound inhibition/uncertain completion remain. A committed explicit connect/power-on intent rearms immediately; its 30s validity deadline is not a reconnect delay. Automatic candidates require a durable Bonded state as well as Paired/Trusted; a live audio peer is never displaced.

Reborn observes relevant BlueZ/BlueALSA signals, waits on D-Bus readiness and a bounded notified command queue, and retains a 30s reconciliation backstop plus operation/discovery/pairing deadlines. PCM lifetime invalidation and per-epoch codec capability caching remain; it still issues no automatic Device.Connect. BlueZ owner return restores agent registration. Status failure clears stale PCM/device observations; requested refresh preserves operation errors.

Native observation serializes numeric D-Bus dictionary keys as JSON strings (including discovery ManufacturerData) and retains 64-bit counters. Platform status exposes Pairable/Discoverable and Bonded independently. Encoder, codec quality, PCM buffering, kernel clocks/DMA/firmware and radio policy are unchanged. These are source/host/ARM software results, not headset/audio qualification or electrical battery evidence.

## Historical source contract and physical notes

The retained description below belongs to earlier profiles/source cuts. Optional-disabled, XQ-unsupported and preference-UI-deferred statements below are historical. Use the current source/feature inventory for active policy; retain the earlier ownership/lifecycle and evidence records for traceability.

# Bluetooth platform v1 contract

2026-09-28 source/physical scope: The candidate's private experiment profile compiles optional encoder libraries, but normal BlueALSA service starts with optional endpoints disabled and SBC as the baseline. The earlier source review's "no ARM proof/source integration" wording below applies to the pre-campaign configuration and is superseded by the [Hardware Final codec source work](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-RADIO-AUDIO.md). Fix01 physically proves a bounded isolated CONSYS retry, not headset audio or Auto qualification. [Current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md).

CONSYS/HCI, BlueZ 5.87 and BlueALSA 5.0.0 remain the control/transport/encoder owners. Reborn retains FFmpeg decode/DSP and one final conversion. Pairing trust, Rate/Format observation and transport generation invalidation were already fixed by later Reborn source; the older codec audit does not supersede those fixes.

`y2-bt-observe` makes bounded, read-only native GIO D-Bus queries. It never activates a radio or opens/selects a transport. It addresses unique daemon owners and checks owners again before publishing; owner replacement invalidates the sample. `y2-status bluetooth` normalizes adapter, paired/trusted/connected peer, manager runtime codecs, exact negotiated codec and PCM Format/Rate/Channels. S24_LE means 24 valid bits in a 32-bit container. Selected/requested preferences are separate from observation. Unsupported or incomplete PCM is degraded, never assumed S16.

BlueALSA GetCodecs reports a subset filtered by local enabled endpoints and remote capabilities. It is labelled mutually_usable; raw remote_advertised remains null. Neither live encoder bitrate nor radio packet loss is fabricated. PCM connection Sequence, object and owner are exposed; clients opening PCM must also consume ObjectManager removal and owner signals for per-open lifetime, as Reborn already does. A snapshot cannot prove no removal occurred between snapshots.

The image's codec inventory is generated from the configured, built BlueALSA source, with pinned source/configuration hashes. It fails packaging on an unexpected optional encoder. Build, runtime, remote/mutual, distribution and qualification states are separate. Current normal runtime starts conformant SBC high quality only; XQ remains unsupported. The owner-private experiment profile also compiles optional encoders, with their endpoints disabled at normal start. No optional peer codec is physically qualified for Fix01. Production Auto must not promote an unqualified codec.

Reborn exports /org/reborn/player and registers it with BlueZ Media1. A bounded eight-command queue accepts calls from the current BlueZ unique owner only. Play/Pause resolve idempotently against the current AppModel; Next/Previous and PlayPause use existing Actions. Playback status and bounded metadata are a projection of that model, not another player authority. PropertiesChanged reports actual model changes; requesting Pause does not claim playback has already paused. The registration is recreated when the BlueZ owner changes. No volume or gain policy is introduced. Physical AVRCP and peer interoperability remain PHYSICAL_GATE.

API basis: pinned BlueALSA 5.0.0 docs/org.bluealsa.PCM1.7.rst and src/bluealsa-dbus.c (GetCodecs filtering); pinned BlueZ 5.87 profiles/audio/media.c; [BlueZ Media API](https://github.com/bluez/bluez/blob/master/doc/org.bluez.Media.rst). Optional codec provenance/distribution and Auto/reconnect implementation are tracked separately in the completion ledger; an audit is not a release approval.

Automatic Device connection remains solely owned by y2-bt-reconnect. One episode allows at most two 10-second calls within a 25-second start window; successful connected observation for 30 seconds resets a later link-loss episode. Same-boot budget, explicit disconnect inhibition and unknown outstanding calls survive helper restart. A local/client timeout inhibits further automatic requests. A new explicit connect/power-on intent can re-arm; periodic polling cannot. Reborn and y2-radio hold a common Linux flock through each user operation. Pending intents inhibit recovery even if that client dies; only an observed successful explicit operation re-arms. No pairing is automatic. Runtime records are private, boot-bound and status rejects stale observations.

Linux lock interoperability is covered by an actual competing file-descriptor lock test and the pinned Rust implementation's [Unix flock semantics](https://doc.rust-lang.org/std/fs/struct.File.html#method.try_lock). This policy is HOST_VALIDATED; headset disappearance, daemon restart, intentional disconnect and reconnect after long absence remain owner qualification cases.

`rebornctl bluetooth codec Auto|SBC ADDRESS` implements explicit stopped-playback codec selection. Auto requires every inventory/runtime/mutual/distribution/physical gate. Two preferred candidates (LDAC, aptX-HD, aptX, AAC in that fixed order) and conformant SBC consume at most three attempts, with a 12-second attempt-start window and bounded D-Bus calls. This is a deterministic initial policy, not a measured quality ranking. All current Auto candidates are physically unqualified: the command reports the gate, never silently calls SBC qualified. Manual SBC is the qualification baseline. No automatic promotion/flapping or Device.Connect loop is added. SBC XQ, live bitrate and LE Audio remain unsupported.

A shared PCM lifetime lease excludes selection while a Reborn probe/handle exists, even when paused. Selection checks unique daemon owners, peer connection, PCM connection sequence/direction and supported stereo 44.1/48 rates. A pending record precedes mutation; ambiguous completion or app death blocks new PCM opens until BlueALSA owner replacement. Actual PCM remains separate from requested/selected codec. The control/API surface is implemented; preference UI is deferred.

Optional encoders in the private experiment profile are not normal-runtime endpoints or approved public product features. FDK-AAC's [NOTICE](https://raw.githubusercontent.com/mstorsjo/fdk-aac/master/NOTICE) grants no patent license; the [libfreeaptx LGPL source](https://github.com/regularhunter/libfreeaptx) is a better future linked-library candidate than mixing GPL-3 libopenaptx with FDK; [AOSP LDAC NOTICE](https://android.googlesource.com/platform/external/libldac/+/2efdd91222c4c5f929335f34cbc3b576343cf1d2/NOTICE) requests product certification. Public distribution approval is not evidenced. Their source integration and ARM/QEMU execution are described in the [later source receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-RADIO-AUDIO.md). Actual peer audio, CPU/coexistence, Auto promotion and public distribution approval remain BLOCKED_BY_EVIDENCE. SBC peer qualification is a separate physical gate; private source builds are not production authorization.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
