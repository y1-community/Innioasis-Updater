---
title: "Audio, FFmpeg, precision and playback audit - Innioasis Updater"
description: "Audio, FFmpeg, precision and playback audit <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-05_audio_audit.html"
---

# Audio, FFmpeg, precision and playback audit - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Audio, FFmpeg, precision and playback audit

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Audio, FFmpeg, precision and playback audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## Bottom line

The shared FFmpeg architecture is the right foundation. Current wired production output is S16_LE, stereo, 44.1 kHz. High-resolution source decoding exists; a genuine 24/32-bit wired output path does not. Ordinary playback controls, queue mutation, native allocation lifetime and crossfade delivery have release-relevant defects. Two-file FLAC gapless has meaningful host evidence, but sample-accurate general playback is not established.

Evidence is anchored in [media.c](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-media/native/media.c), [media Rust wrapper](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-media/src/native.rs), [playback worker](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/playback.rs), [runtime](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs), [ALSA C boundary](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-audio/native/audio.c), [ALSA Rust boundary](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-audio/src/native.rs), [AFE](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/audio/mt6582-afe.c), [card](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/audio/y2-cs43131.c), and the [qualification profile](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/etc/y2linux/audio-qualified.json).

## 1. Actual FFmpeg version and compiled surface

VERIFIED generated-build inspection / HIGH: the retained complete Buildroot output contains FFmpeg 9.0.1 source/version/configuration and these target library versions:

| Library | Version |
| --- | --- |
| libavcodec | 63.1.101 |
| libavformat | 63.1.101 |
| libavutil | 61.1.101 |
| libavfilter | 12.1.101 |
| libswresample | 7.1.101 |
| libswscale | 10.1.101 |

`tools/production/verify-ffmpeg.py --buildroot-output out/y2linux-reborn-audio-final/buildroot` passed. This inspects generated component headers and target ELF dependency boundaries, not just the desired defconfig. The latest package's media membrane was also present in read-only image inspection; this audit did not execute that ARM image on Y2.

Exact enabled generated component lists in the inspected build:
  - Demuxers: `aac aiff ape flac mov mp3 ogg wav wv`.
  - Audio decoders: `aac alac ape flac mp3 mp3float opus vorbis wavpack pcm_f32be pcm_f32le pcm_s16be pcm_s16le pcm_s24be pcm_s24le pcm_s32be pcm_s32le`.
  - Image decoders: `mjpeg png webp`, plus required `vp8` implementation dependency. `webp_anim` is allowed by the verifier but was not enabled in the inspected generated header.
  - Parsers: `aac flac mpegaudio opus vorbis`.
  - Selected filters: `acrossfade afade aformat alimiter amix aresample asetnsamples atrim equalizer volume`; `abuffer` and `abuffersink` are available endpoints.
  - Protocols: `file` only. Encoders: none. Muxers: none.
  - Programs, network, avdevice and hardware/video acceleration families: disabled. No target ffmpeg/ffprobe/ffplay CLI.

The six-library dynamic membrane is lazily loaded from `/usr/lib/reborn/libreborn_media.so`; its handle deliberately stays resident for process lifetime. This is not a duplicate decoder implementation. Startup's pinned version text must not be confused with the runtime manifest obtained after loading the membrane.

Assessment: sensibly minimal, not materially bloated or codec-starved.`swscale` and VP8 have real artwork purposes. Some selected filters are not currently on the normal path, but removing a few is not a success-determining optimization. The real format gap is the scanner whitelist, not this codec configuration.

| User format | Decoder/container exists | Ordinary library discovery | Physical current-Reborn qualification |
| --- | --- | --- | --- |
| FLAC; MP3; AAC/ADTS; M4A AAC/ALAC; Ogg Vorbis/Opus; WAV | Yes | Yes for listed extensions | Not established for the whole matrix |
| AIFF; APE; WavPack | Yes; host fixtures decode | No: extensions excluded | Not established |
| PCM 16/24/32 integer, float32 | Selected LE/BE variants above | Via supported discovered containers | Does not prove corresponding hardware output precision |
| JPEG/PNG/WebP covers | Yes, embedded and selected sidecars | Artwork service | Host pixel-size/content sanity, not malformed-image endurance |

## 2. Wired hardware trace`Reborn file decoder + processing -> bounded interleaved stereo bytes -> ALSA hw:CARD=Y2Audio,DEV=0 (not a plug/default software-conversion PCM) -> ASoC DL1 frontend -> MT6582 AFE DMA/IRQ -> I2S backend, CPU clock provider, normal polarity -> 64 BCLK/frame / 32-bit slots carrying current 16-bit samples -> mainline cs43130 driver supporting CS43131, board PM fixes -> DAPM HPOUTA/HPOUTB -> Headphone`

AFE `mt6582_params` explicitly rejects formats other than S16_LE and channels other than two. Both DAI descriptors expose only S16_LE and 44.1/48 kHz. A larger internal rate-code lookup is not the advertised/implemented hardware matrix. `mt6582_i2s_prepare` selects 32-bit slots, not 32-bit source precision. The card's codec DAI clock is rate×64 and its external MCLK selection is 22.5792 MHz. No general high-rate/word-width/MCLK-family switching implementation is established.

The codec has upstream format support broader than this board AFE. That cannot make the frontend accept S32. Board GPIO rails and DAPM output are real; a separately controlled external headphone-amplifier stage was not established from inspected source/evidence. Do not invent one in the system diagram. Physical schematic/measurements would be needed to extend that conclusion.

ALSA planning prefers S32, but wired profile checks allow only S16/44100. Runtime initially requests the source rate and falls back to 44100 if not qualified. Both inspected source and the latest image's JSON agree. The JSON parser uses substring-based section searches, not full schema validation: a small privileged configuration today, but too fragile as the future authoritative qualification format. Keep the fail-closed qualification concept; eventually parse exact card/rate/format/channel tuples.

The sink configures a 512-frame period, 4096-frame buffer, and nonblocking writes; recovery handles underrun/suspend error returns. A shared activity lock prevents deep suspend while the sink owns audio. Hardware Master volume is set to -24 dB and headphone output enabled; prior mixer values are restored on close. Software volume/RG occur before ALSA. There is no demonstrated click-free gain ramp for repeated sink teardown/reopen.

Physical evidence:[GPU01 audio capture](https://github.com/SchulzCode/Y2Linux/blob/main/docs/hardware-evidence/2026-09-18-gpu01/audio.txt) and owner observations record clean two-channel S16/44100 tones without observed XRUNs/clicks, using aplay with period 1024/buffer 8192. This is valuable hardware baseline evidence, not qualification of current Reborn's different buffering, seek/volume transitions, mixed-rate queue, decoder or long-session behavior.

## 3. Exact current precision trace: F10``````````````````

| Stage | 16-bit / 44.1-kHz FLAC | 24-bit / 96-kHz FLAC |
| --- | --- | --- |
| libavcodec decoded samples | s16, source rate | s32 representation of 24-bit content, 96 kHz |
| Canonical conversion | libswresample → stereo fltp, 44.1 kHz | libswresample → stereo fltp, 96 kHz |
| Graph input | aformat constrained FLTP | Same, at 96 kHz |
| Gain | optional volume, default float precision; squared user-volume law + RG/headroom | Same |
| EQ | configured nonzero bands through FFmpeg equalizer; auto precision negotiates FLTP in the observed graph; no user band editor | Same |
| Limiter internal format | packed double (dbl) negotiated by alimiter | Same |
| Graph output | forced FLTP, stereo | forced FLTP, stereo |
| Final rate/format conversion, normal non-crossfade job | packed S16, 44.1 kHz | packed S16, resampled to 44.1 kHz |
| Rust PCM bytes / real sink | interleaved S16 stereo | interleaved S16 stereo |
| ALSA / ASoC AFE | S16_LE/44100 | S16_LE/44100 |
| I2S | 32-bit slots, 64 BCLK/frame, 16-bit payload | Same |
| CS43131 interface | codec hw_params from the S16 stream | Same |

Source evidence: `make_filter_graph`, `rb_media_open`, `source_to_canonical`, `rb_media_read`; AFE params/DAI descriptors and card params. The actual pinned FFmpeg `libavfilter/af_alimiter.c` declares `FILTER_SINGLE_SAMPLEFMT(AV_SAMPLE_FMT_DBL)`. Therefore “one FLTP graph” describes the endpoints/canonical format, not every internal filter format. FFmpeg inserts conversions around the limiter. `af_volume.c` defaults to float precision. The diagnostic `internal_sample_fmt=fltp` does not enumerate these internal negotiations.

An additional cached-host negotiation probe confirmed this for both FLAC specimens: source/decoder `s16` and `s32` respectively, canonical `fltp`, final `s16`, and auto-inserted FLTP→DBL→FLTP around the limiter at the source rate. A second run with volume 35 and a +3-dB/1-kHz EQ band confirmed FLTP leaving `equalizer` before the limiter. These are actual host graph logs, not merely comments; they still do not substitute for target ALSA/electrical evidence. See the command in [executed checks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F15_EXECUTED_CHECKS.md).

Crossfade additionally requests S32 working PCM even for an S16 sink: FLTP graph → S32 packed → FLTP crossfade → S32 packed → sink conversion to S16. These are all FFmpeg operations, not competing Rust DSP, but they are additional allocations/conversions. `rb_media_convert` creates a swresample context per conversion call. A future clean transition path should avoid avoidable integer round trips without introducing another DSP authority.

Float32 can represent 24-bit integer input values at unity scaling, but gain/filter calculations round, and full 32-bit integer precision is not preserved through this canonical representation. Regardless, the final S16 reduction conclusively prevents a preserved 24-bit wired output claim. No explicit dither policy is configured. This is not a bit-perfect bypass: the limiter is always present, even when RG/EQ are off and volume is 100.

| Capability | Architecture/code | Host tests | ALSA accepted on Y2 | Electrically/heard qualified |
| --- | --- | --- | --- | --- |
| Decode 24/96 source | IMPLEMENTED | Fixture decoded | Not an output claim | Current end-to-end path UNKNOWN |
| S16/44.1 wired | IMPLEMENTED | Format/planning logic | Historical aplay evidence | Historical tones/owner observation |
| S16/48 wired | Driver advertises it | Fake sink/decoder tests | Current direct-device acceptance UNKNOWN | Unqualified; profile excludes it |
| S32 wired | MISSING in AFE | Conversion buffers tested only | Driver rejects it | Not qualified |
| Native 88.2/96-kHz wired | MISSING in exposed AFE path | Source decode/resampling only | Not established/supported by current DAI | Not qualified |

Do not “fix” high-resolution output by editing the qualification JSON. It requires scoped driver/clock/format work and subsequent physical qualification; no such work is authorized here.

## 4. Native lifetime and sink lifecycle: F01/F02

F01 — WEAK / HIGH, source defect supported by host measurement.`source_to_canonical` allocates `AVFrame *canonical` around line 539. On positive conversion output it calls `av_buffersrc_add_frame`, then returns without `av_frame_free`. FFmpeg's pinned `buffersrc.c` allocates a destination and `av_frame_move_ref`s the caller frame; it does not free the caller's frame shell. Error branches also need ownership review. Contrast `rb_media_crossfade`, which frees its moved-from input frames correctly.

A read-only execution probe using the cached host membrane decoded and closed 250 identical one-second tracks per phase. Process maximum RSS was 60,744 → 67,272 → 73,904 → 80,256 KiB after 250/500/750/1000 closed contexts. This supports accumulating allocations; it is not an exact heap attribution or target leak-rate estimate. No ASan/LSan/Valgrind run or ARM endurance measurement was performed. Fix ownership and verify with an allocator-aware test before new audio features.

F02 — WEAK / HIGH.`Runtime::load` calls `AlsaSink::plan`; `rb_alsa_plan` opens the actual hardware PCM. Only subsequently does `load_with_gapless` call `stop`. The existing audio worker may still own the exclusive device. Volume, seek, skip and DSP toggles therefore have an ordering failure even though worker generation cancellation is otherwise sensible. The desired owner is one sink lifecycle that can negotiate/reconfigure after releasing or deliberately retaining its own handle. Do not solve this by switching to a hidden software mixer and losing format authority.

## 5. ReplayGain, EQ and gain staging: F12

Track Gain, Album Gain, Track Peak and Album Peak are read from container/stream metadata with uppercase/lowercase forms. Mode and volume persist. Track/Album choose distinct tag pairs; Album does not implement an explicit fallback policy to track tags. Values use `strtod`; absent/zero are conflated by helper fallback, and finite/range validation is incomplete. Invalid tags must be a bounded fallback, not graph failure or unexpected gain.

Gain is combined as RG + user-volume dB + peak-derived headroom, applied before optional EQ. User volume is a squared amplitude mapping; zero maps to -120 dB, not an explicit all-zero mute. For the present S16 sink that largely quantizes away, but it is not an exact future S32 mute contract.

Confirmed limiter mismatch: code specifies `alimiter=limit=0.98:latency=1` without `level=0`. FFmpeg's limiter defaults `auto_level=1`, multiplying output by 1/0.98 (~+0.175 dB). Thus the nominal 0.98 ceiling is normalized back toward full scale, and a diagnostic gain/headroom value does not completely describe output level. This is not proof of audible hard clipping on every track; it is proof that the intended headroom cannot be inferred from the option name. Test known RG amplitudes, peaks, full-scale transients, EQ boosts and silence end-to-end.

The limiter precedes final sample-rate conversion. A pre-resampling sample ceiling also does not establish post-resampling/true-peak headroom; no explicit post-conversion peak/dither policy is proven. Inspect output samples for adversarial high-frequency/full-scale material before claiming clipping prevention across all sources.

EQ processing itself is IMPLEMENTED and host-tested with a supplied band. User configuration is MISSING: default `eq_bands` is empty, and UI/control effects only toggle enable. With the ordinary settings path, “Equalizer On” can mean no EQ at all. No band editor/preset selection was found. Decide whether to expose a real minimal EQ or label/withhold the control; do not build an elaborate DSP framework.

ReplayGain tests check extracted tags and changed PCM; they do not establish exact level/headroom, malformed-tag safety, album transition consistency or physical loudness. Classification: PARTIAL / HIGH, not absent.

## 6. Gapless and seek: F11

There is real transition machinery: skip-sample side data, no heuristic silence trimming, next-decoder opening, a bounded PCM channel and an ordered boundary marker without a sink reopen. The same-rate two-FLAC ramp test checks total frames (8192) and boundary slope, not merely successful return. This is worth preserving.

It is not complete proof:
  - Next decoder opening is not next-PCM predecoding. Opening/artwork for following tracks can block the decode producer while the short output queue drains; the media interrupt deadline is up to ten seconds.
  - Source skip/padding relies on FFmpeg-provided side data and the manual-skip setting; no broad lossy encoder-delay/edit-list fixture matrix establishes correctness.
  - Filters and resamplers are per track; flushes, latency compensation, mixed rates and sample rounding need waveform/count assertions.
  - A job retains the initial sink rate for its copied queue; it does not negotiate native output rate per subsequent track.
  - Boundary position reporting resets relative to the next track while ALSA still has buffered frames. Block position is based on decoded-frame PTS and not advanced for each partial block read. This is not sample-accurate output-clock tracking.

Seek is demonstrably approximate. `rb_media_seek` seeks the demuxer, resets processing, and sets `position` to the requested time. `decode_more` checks timestamps to update the label but sends pre-target decoded samples into processing rather than trimming to the exact target. The existing seek test checks the reported position, not the waveform.

An additional cached-host probe decoded `tone.flac` at matching 48 kHz: unseeked output was 48,000 frames; seeking to 500 ms yielded 24,448, not 24,000, while the first block reported 500 ms. At 44.1-kHz output it yielded 22,461 rather than 22,050. This is meaningful evidence of the label/audio discrepancy. A preliminary seek on the very short FLAC ramp returned an error; it was not counted as a passed test. Full commands/limits are in [executed checks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F15_EXECUTED_CHECKS.md).

Conclusion: VERIFIED limited same-rate FLAC continuity; PARTIAL general gapless; WEAK sample-accurate seek. Existing playback fixtures all passed in this audit, serially and in parallel. Earlier reported failures were not reproduced, and no specific failing historical log was identified; there is no basis to invent their cause or dismiss them as unrelated UI work.

## 7. Crossfade: F04

FFmpeg `acrossfade` does the actual mix; per-track volume/RG/EQ is applied before mixing. Both windows are at the job rate, so differing source rates are resampled into that rate first. Cancellation generations guard transfer, but the in-memory graph operation is not an independently bounded real-time stage. This is an implemented transition, not production-grade delivery.

The code supplies `nb_samples` and `overlap=1` but no curve options. Pinned FFmpeg `af_afade.c` defaults both crossfade curves to TRI (linear slopes), not an explicitly designed equal-power curve. This is a legitimate simple choice, but perceptual level continuity and RG interaction have not been characterized. It is not a reason to add a custom mixer.

The full overlap is emitted as one Pcm block. `AlsaSink::write` rejects slices larger than 524,288 bytes. At 44.1 kHz stereo S16, that permits only 131,072 frames (~2.972 s); at S32 it permits half as many. UI choices are 5/10/15 seconds, all beyond the S16 bound when both tracks supply the full overlap. Five seconds alone is 882,000 bytes after S16 conversion. The fake sink in the 50-ms unit test accepts arbitrary block sizes, masking the integration defect.

The tail window uses front-draining vectors, repeatedly shifting retained PCM; long transitions create memory-copy cost. At the allowed 30 seconds, one stereo S32 window is ~10.1 MiB, and head/tail/mix/conversion allocations coexist. These are significant but not automatically out-of-memory on Y2; the concrete sink-size failure is more urgent.

On crossfade error, the fallback sends the old suffix but does not restore the already-consumed next-track overlap; only the unconsumed head remainder is retained. A failed mix can therefore lose the beginning of the next track. Post-overlap position and actual gain-curve/loudness continuity also need explicit tests. Correct chunked delivery and fallback semantics before presenting crossfade as a normal feature.

## 8. Bluetooth and physical qualification

Bluetooth uses the same decoder/processing worker and `AudioSink` boundary, then BlueALSA's ALSA PCM and SBC encoder. No separate unprocessed Rust/BlueZ audio path was found. Its rate comes from the exact peer's A2DP-source/sink PCM; this selection has useful mocked D-Bus tests. Wireless latency, disconnect and reconnect add separate failure modes and cannot be inferred from wired success. See [connectivity](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F06_CONNECTIVITY_AUDIT.md).

Before release, qualify current-image wired start/stop/pause/resume/seek/volume/skip, screen-off playback, corrupt media, SD removal, output switch, DAC power transitions, underrun recovery and long-session memory behavior. For any future precision claim, capture ALSA hw_params plus I2S word/slot/clock evidence and an independently known low-bit waveform; hearing a 24/96 file after downsampling is not high-resolution qualification.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
