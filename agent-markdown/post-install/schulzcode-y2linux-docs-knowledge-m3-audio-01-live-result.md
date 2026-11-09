---
title: "Native audio physical result — AUDIO-02 supersedes AUDIO-01 - Innioasis Updater"
description: "Native audio physical result — AUDIO-02 supersedes AUDIO-01 <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate iden"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m3-audio-01-live-result.html"
---

# Native audio physical result — AUDIO-02 supersedes AUDIO-01 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Native audio physical result — AUDIO-02 supersedes AUDIO-01

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Native audio physical result — AUDIO-02 supersedes AUDIO-01 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current result, 2026-09-10: clean native headphone output at S16 stereo 44.1 kHz. Owner reports "perfect, no clicking!" after manually flashing AUDIO-02. M3 is active / near completion, with focused 48 kHz, L/R and stop/restart/repeat checks remaining. The existing filename retains links to the original AUDIO-01 result.``````````

| Area | Current physical result / limit |
| --- | --- |
| Kernel | 6.18.0-y2linux-m3audio02, packaged commit 8f93e44; owner flash plus SSH release confirmed, whole BOOTIMG not read back |
| ALSA | Card Y2Audio, PCM0 Y2 Headphone Playback; hw:CARD=Y2Audio,DEV=0 |
| AFE / DMA / IRQ | DL1 continuously advances during the short run; ALSA hw_ptr crosses ring wraps; 130 IRQ events |
| External path | DL1 -> I05/I06 -> O00/O01 -> second-I2S CON3 -> upstream CS43131 -> headphones; own-unit clean audio proves this path functions |
| DAC power | CS43131 revisionA1; VGP2 regulator reports 1800 mV, GPIO20/18/15 supply chain active; no observed DAC reset |
| Test | Three-second faded -30dBFS WAV, Master 207=-24dB, period 1024/buffer 8192; elapsed3.13 seconds including setup/drain; exit0, no watchdog deadline or reported underrun |
| Cleanup | Headphone off, AFE stopped; no new audio kernel error; VCAMA/VRTC unsupported get_mode diagnostic warnings already present |
| Userspace | aplay/amixer/speaker-test, ALSA config/lib and test WAVs installed persistently on SD, verified in a fresh SSH session; no temporary-tool restore needed |
| Speaker / jack | SpeakerGPIO8 held low; amplifier identity/output and automatic jack reporting remain separate, unqualified subpaths |

## PCM support

| Format | Status |
| --- | --- |
| S16_LE stereo 44.1 kHz | PHYSICALLY CONFIRMED CLEAN for the short run |
| S16_LE stereo 48 kHz | Implemented; physical test pending |
| Native 24-bit PCM | Not implemented |
| Native 32-bit PCM | Not implemented |
| Higher sample rates | Not implemented |

I2S uses 32-bit slots (64BCLK/frame) containing 16-bit samples. DMA32 refers to address width, not sample depth. True 24/32-bit output needs AFE packing, DMA format, I2S, codec and ALSA constraint implementation/validation. It is a later enhancement, not tonight's work or an automatic M3 core gate. Future arbitrary ALSA applications, including Y2PlayerNative after the platform gates, can use CD-quality playback; higher-resolution sources currently need conversion.

## Period-notification defect: fixed, deployed and physically tested

AUDIO-01 `aa3c949` treated any nonzero `snd_pcm_hw_constraint_integer()` return as an error/early exit in `mt6582_open`. Upstream returns +1 when successfully adding the integer constraint. ASoC accepts nonnegative startup, but our early return skipped `afe->substream` assignment. DMA and IRQ hardware still ran and could repeatedly play already queued ring contents, producing audible sound with clicking while ALSA received no `snd_pcm_period_elapsed` notifications. Polling could update pointers but missed ring wraps and did not repair the notification contract. Audible sound alone therefore did not prove correct PCM.

Commit `137b3f2` changes the startup constraint checks to `ret < 0`; successful startup now attaches the substream for the existing IRQ notification path. No routing, clock, voltage or gain retuning accompanied this fix. Regression `tests/test_audio.py::AFE.test_startup_accepts_positive_constraint_success` invokes production startup for 0, +1 and negative errors, fails on old code and passes fixed code. Production trigger/IRQ/DMA and clock/DT tests also pass.

The fix was built into AUDIO-02 (`8f93e44`) and manually deployed by the owner. The recorded 3.13-second run, 130IRQs, advancing ALSA pointers and owner-confirmed clean sound validate it for this 44.1-kHz run. **Do not schedule its deployment again.** Longer stability and remaining rates are not inferred from that result.

## Evidence and next work
  - [AUDIO-02 exact test, logs and owner result](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-10-m3-audio-02-playback/)
  - [AUDIO-01 failure, test regression and raw logs](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-10-m3-audio-01-live/)
  - [Persistent SD installation](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-10-audio-tools-sd/)
  - [Architecture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-architecture.md) and [build/deployment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m3-audio-02-deployment.md)

Tomorrow verify the running release, then perform bounded quiet 48 kHz, explicit L/R separation and short stop/restart/repeat tests. Watch for distortion/pops, DAC reset, underruns and kernel errors; ask the owner about each listening result. Do not rediscover AFE/CON3/CS43131/VGP2 or repeat M2/reconnect work. On success, repeat the standing boundary audit before M3 core closure and M4 activation; retain speaker/jack/precision-clock/higher-resolution limitations separately.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
