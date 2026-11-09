---
title: "Physical Y2 wired precision completion - Innioasis Updater"
description: "Physical Y2 wired precision completion Completion follows the newest integrated Baseline-final source, 2444e0f65811e688250a8cd069a57dd780b2d6d3 . The physical Baseline01"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-y2-wired-precision-completion.html"
---

# Physical Y2 wired precision completion - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Physical Y2 wired precision completion

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Physical Y2 wired precision completion

Completion follows the newest integrated Baseline-final source, `2444e0f65811e688250a8cd069a57dd780b2d6d3`. The physical Baseline01 runs Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304` with FFmpeg 9.0.2. The media/audio/volume implementations used for these observations are shared with the selected source. No product DSP or radio implementation changed.

**Correction: hardware24/32 feasibility is not established; impossibility is not proven.** The earlier HARDWARE_PROVEN_UNSUPPORTED verdict is withdrawn. The MT6582 specification documents two16-bit DL1 monitor fields and no wider fetch selector was found. A monitor's width does not conclusively define all internal data-path modes. Installed playback is verified S16; I2S and the CS43131 accept wider words, but a complete wider source transport is unproven. The canonical evidence, register contract, live results, CPU measurements and hardware source identities are in the paired Y2Linux repository: `docs/validation/Y2-HIGHRES-AUDIO-COMPLETION.md`.

The existing architecture decodes PCM24 into S32/Q31, converts to FLTP for DSP, then converts to the negotiated sink. Neutral S24_LE software output preserved every signed low-bit fixture value on the actual Cortex-A7. S32_LE output of that source preserved 24 bits left-aligned with eight zero padding bits. Binary32 DSP cannot preserve arbitrary signed PCM32 values at ordinary amplitudes; those software containers are not a true 32-bit precision claim.

Six installed-Reborn playback cases (16/24/32 source at 44.1/48 kHz) selected S16_LE, stereo, period 512 and buffer 4096 frames. Each 256-byte kernel DMA snapshot matched the native final conversion probe byte-for-byte at settled unity live gain. Samples differing only below bit 16 collapsed. No xruns, recoveries, playback, decode or filter errors occurred in these bounded runs. There was no external I2S or analog measurement.

## Native conversion probe

`tools/build/precision-probe.c` includes the actual native media implementation, as does the existing CPU benchmark. It dumps decode/float-DSP/final integer bytes without opening an audio sink. Its neutral graph retains the limiter. It does not include PlaybackWorker's live VolumeRamp or kernel transport; those were checked separately by comparison with the observed DMA ring.

Build with the production SDK and matching FFmpeg libraries:`task_sdk="$Y2_BUILDROOT_OUTPUT/host" task_sysroot=$("$task_sdk/bin/arm-linux-gcc" -print-sysroot) export PKG_CONFIG_SYSROOT_DIR="$task_sysroot" export PKG_CONFIG_LIBDIR="$task_sysroot/usr/lib/pkgconfig:$task_sysroot/usr/share/pkgconfig" "$task_sdk/bin/arm-linux-gcc" -O2 -Wall -Wextra -Werror \ -mtune=cortex-a7 -mfpu=neon-vfpv4 -mfloat-abi=hard \ tools/build/precision-probe.c -o /tmp/y2-precision-probe \ $("$task_sdk/bin/pkg-config" --cflags --libs libavformat libavcodec libavfilter libswresample libswscale libavutil) \ -lm -lpthread /tmp/y2-precision-probe source.wav 48000 3 /tmp/source-s24le.raw`

Format IDs: 1 = S16_LE, 2 = S32_LE/Q31, 3 = ALSA S24_LE (24 valid bits in the low three bytes of a four-byte container, padding byte zero). Successful output explicitly reports `physical_output:false`. The ARM probe built with strict warnings, ran on the Y2, and its S24 result also matched under QEMU Cortex-A7. Workspace fmt, strict Clippy, 324 tests and the production ARM build passed.

The ordinary stereo FLTP→S16 path on the installed FFmpeg uses `swri_oldapi_conv_fltp_to_s16_2ch_neon`: Q31 conversion followed by high-half packing, rather than nearest rounding at the S16 grid. This differs from the rounded packed-float converter and the explicit ties-even integer narrowing used by crossfade/S24 packing. No dither is selected. Settled unity VolumeRamp copies bytes; non-unity gain still performs a second integer quantization. These details are recorded rather than presented as a single idealized conversion. They do not explain away the independently documented DL1 ceiling.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
