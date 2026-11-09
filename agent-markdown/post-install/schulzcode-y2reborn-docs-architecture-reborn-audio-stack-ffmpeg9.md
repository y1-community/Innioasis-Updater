---
title: "Reborn FFmpeg 9 audio stack - Innioasis Updater"
description: "Reborn FFmpeg 9 audio stack Current source/physical scope, 2026-09-28: FFmpeg 9.0.2 remains the sole decode/filter/resample path. The later live-volume contract live-volu"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-reborn-audio-stack-ffmpeg9.html"
---

# Reborn FFmpeg 9 audio stack - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn FFmpeg 9 audio stack

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn FFmpeg 9 audio stack

Current source/physical scope, 2026-09-28: FFmpeg 9.0.2 remains the sole decode/filter/resample path. The later [live-volume contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Flive-volume.md) adds a bounded integer sink-stage gain after that path; the older statement below that Rust has no integer volume stage is superseded. The [Fix01 physical run](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md) passed bounded S16 44.1 and 24/96 -> 48 silent fixtures with zero XRUN/decode/ filter errors. Analog quality, native S24/S32 and end-of-track crossfade remain unqualified by that run. The graph below describes FFmpeg processing before the current sink-stage user-volume ramp.

Reborn has one media path. `reborn-media` opens the local file with FFmpeg 9.0.2 `libavformat` and `libavcodec`, converts decoder output once to stereo `AV_SAMPLE_FMT_FLTP`, runs an optional `libavfilter` graph, and uses `libswresample` for the final sink rate and sample format. Rust owns only the opaque context, cancellation, bounded scheduling and diagnostics. The only additional integer PCM operation is the final bounded live user-volume ramp; Rust has no competing decoder, resampler or DSP graph.

Metadata/ingest source contract, 2026-10-04:`MediaFile` owns a separate demux-only context for library ingestion and embedded collection covers. Complete single-audio-stream headers supply tags/properties without PCM decoding or DSP setup; MP3/raw AAC and incomplete headers retain normal FFmpeg stream analysis. Detection budgets remain unchanged. Source precision/encoding, decoder format, FLTP and sink format are separate properties; lossy source precision is unknown. Incremental scans use bounded file stamps and an extractor revision, and do not reopen unchanged files. Header reads and artwork allocations/dimensions are bounded. See the [media pass receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-FFMPEG-METADATA.md) for measurements and physical qualification limits. The app and native membrane must be rebuilt and packaged together after this private ABI extension.

The cold startup path does not link the FFmpeg membrane into the `reborn` executable. Buildroot installs the one shared membrane at `/usr/lib/reborn/libreborn_media.so`; `reborn-media` resolves its `rb_*` API on the first media operation and keeps that handle resident for the process lifetime. This preserves one FFmpeg implementation while keeping the six large FFmpeg libraries out of the dynamic loader's pre-`main` work. The startup log records the pinned version immediately and obtains the actual component manifest when the membrane is opened.

The normal graph is:`demux -> decode -> stereo FLTP -> aformat -> ReplayGain/user volume -> optional equalizer -> alimiter -> final libswresample -> ALSA`

ReplayGain reads track and album gain/peak tags from container/stream metadata, with FFmpeg coded ReplayGain side data as a fallback when tags are absent. `Off`, `Track` and `Album` are distinct settings. Peak-aware headroom is applied before the FFmpeg volume filter and the limiter protects the integer sink. The source file is never changed. EQ bands are passed into `equalizer` and a graph is rebuilt when the playback settings change.

Gapless playback is the default queue behavior. The next decoder is opened before the current decoder reaches EOF, and the bounded PCM channel carries a boundary marker between the last valid sample of one track and the first valid sample of the next. Codec skip-sample side data is honored when FFmpeg exposes it; there is no fixed silence trim. Crossfade is independent. When enabled, the worker retains only the configured transition window, feeds both windows through FFmpeg `acrossfade` in canonical FLTP, then sends the single overlap window and continues with the unconsumed head of the next track.

Reborn can negotiate S32_LE when the sink permits it, but the **shipped Y2 enablement selects S16_LE** at 44.1/48-kHz output. Fix01 physically exercised bounded S16 44.1 playback and a 24/96 source converted to 48-kHz output; this does not qualify native wide/high-rate output or every 48-kHz transition. The separate audio-qualification configuration still names earlier narrow 44.1-kHz evidence; its static flag does not automatically update after a run. Reborn logs requested rate, selected ALSA format and each fallback reason. Bluetooth receives the processed PCM and differs at the BlueALSA sink boundary.

The production source matrix covers FLAC, MP3, AAC/ADTS, AAC/M4A, ALAC, Ogg Vorbis, Opus, WAV, AIFF, APE and WavPack, including PCM 16/24/32-bit integer and 32-bit float inputs. JPEG, PNG and WebP attached artwork remains in the same media membrane; `libswscale` is used only for image conversion.

`rebornctl audio --json` exposes the active source metadata, decoder and internal format, filter description, ReplayGain values, resampling decision, final format conversion, ALSA parameters, transition timing and fixed-cardinality audio metrics. A rate or channel change is reported as resampling; the intentional FLTP-to-packed-sink conversion is reported separately. Embedded and bounded local sidecar cover images use the same FFmpeg image decoders and libswscale path. `status --json` and `audio --json` report the runtime component manifest once the membrane has been loaded; they do not trigger a cold FFmpeg load on the UI thread. The decoder diagnostic loads it on its worker when an early manifest is required. Build verification rejects missing required components, any encoder or muxer, network protocols, the FFmpeg command-line tools, `libavdevice`, and unrelated codec families.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
