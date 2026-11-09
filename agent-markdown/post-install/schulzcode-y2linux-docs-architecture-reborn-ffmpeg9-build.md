---
title: "Reborn FFmpeg 9.0.2 production build - Innioasis Updater"
description: "Reborn FFmpeg 9.0.2 production build <!-- knowledge-base-scope: source-contract -- Source-contract scope. This page describes software ownership and interface behavior. S"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-reborn-ffmpeg9-build.html"
---

# Reborn FFmpeg 9.0.2 production build - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Reborn FFmpeg 9.0.2 production build

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Reborn FFmpeg 9.0.2 production build > **Source-contract scope.** This page describes software ownership and > interface behavior. See [current state](../CURRENT_PLATFORM_STATE.md) for the exact latest image > and physical limits; implemented or enabled does not mean qualified. 

Y2Linux pins the Reborn media build to FFmpeg 9.0.2. Buildroot supplies `libavformat`, `libavcodec`, `libavutil`, `libavfilter`, `libswresample` and `libswscale`; the FFmpeg command line tools, `libavdevice`, network protocols, capture devices, hardware autodetection, post-processing and unrelated video families are disabled. Encoders and muxers are empty because Reborn only reads and processes local media. `libswscale` remains for JPEG, PNG and WebP artwork conversion.

The component lists live in [`y2_production_defconfig`](https://github.com/schulzcode/y2linux/blob/HEAD/buildroot/configs/y2_production_defconfig). `tools/production/verify-ffmpeg.py` checks the generated FFmpeg `config_components.h`, generated `config.h`, target library SONAMEs, and CLI and `libavdevice` absence after Buildroot finishes. The ARM runtime manifest is checked by `Y2Reborn/tools/build/qemu-check.py`; it records the actual FFmpeg and library versions rather than trusting the Buildroot defconfig.

FFmpeg's WebP decoder requires its VP8 decoder, so `vp8` is the sole intentional video-codec dependency. VP9 and other video codecs remain disabled.

The ALSA qualification profile intentionally prefers `S32_LE` but currently allows only the owner-confirmed `S16_LE`, stereo, 44.1 kHz wired combination. The MT6582 driver and CS43131 path have not been physically qualified for S32_LE or higher rates in the retained evidence. Reborn therefore logs and performs an explicit fallback to the qualified combination instead of advertising an untested format.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
