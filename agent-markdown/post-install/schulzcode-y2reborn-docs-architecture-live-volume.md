---
title: "Live user volume - Innioasis Updater"
description: "Live user volume <!-- knowledge-base-scope: source-contract -- Source-contract scope. This page describes software ownership and interface behavior. See current state ../"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-live-volume.html"
---

# Live user volume - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Live user volume

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Live user volume > **Source-contract scope.** This page describes software ownership and > interface behavior. See [current state](../CURRENT_REBORN_STATE.md) for the exact latest image > and physical limits; implemented or enabled does not mean qualified. 

Volume keys and `rebornctl volume` update an atomic sink-worker target. They do not invalidate the playback generation, seek, rebuild the FFmpeg filter graph, or reopen ALSA. This addresses the owner-observed SBC pause and “starting audio” state on every volume adjustment.

Playback decodes at neutral user gain while retaining FFmpeg ReplayGain, headroom, EQ and the clipping limiter. The sink applies the existing squared volume curve after those stages, so buffered and crossfaded PCM responds to a new volume without recovering amplitude from already-muted samples. This changes limiter interaction: limiting operates before user attenuation, including at low listening volume. The live `audio_user_volume` metric reports the user target; FFmpeg's gain metadata describes its own graph and excludes this final gain.

Changes ramp over five milliseconds with one gain per stereo frame. A partial or zero-frame ALSA write advances the envelope only by accepted frames; retries use original PCM, avoiding repeated attenuation. Writes process at most 512 frames per iteration. The downstream ALSA/BlueALSA/headset buffering still adds its normal latency, so this is not a zero-latency remote-volume claim.

Unity gain passes bytes unchanged. S16, sign-extended S24 in 32-bit containers, and S32 are supported. Gain is rounded and bounded in the negotiated integer format; no additional output precision is claimed. Volume zero is exact silence.

Tests exercise the real decoder with queued PCM and a partially accepting fake Bluetooth sink, starting muted then raising/muting/raising volume. They prove one sink open, one start event, unchanged generation and exact frame count. Separate waveform tests cover stereo ramp continuity, zero/partial acceptance, retargeting, signed packing, unity low-bit preservation and exact mute. Physical volume-key/listening confirmation remains required for a new binary.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
