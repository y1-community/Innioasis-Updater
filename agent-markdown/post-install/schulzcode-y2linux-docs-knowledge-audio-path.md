---
title: "Audio and FM evidence - Innioasis Updater"
description: "Audio and FM evidence <!-- knowledge-base-scope: maintained-summary; baseline02-sync 2026-10-03 -- Current Baseline02 / UART01 scope 2026-10-04 wired precision pass ../va"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-audio-path.html"
---

# Audio and FM evidence - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Audio and FM evidence

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Audio and FM evidence

## Current Baseline02 / UART01 scope

2026-10-04 [wired precision pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-HIGHRES-AUDIO.md): exact BSP and stock HAL research leaves the MT6582 silicon maximum unresolved; S16 is the admitted path, not an immutable hardware ceiling. Stock fetch and connection width functions return ENOSYS. CS43131 independently accepts32-bit input. New source diagnostics and low-bit WAV/FLAC tests distinguish24 software packing from unproven wider DL1/I2S; full32 source precision is lost in FLTP. The complete path also includes live VolumeRamp after integer sink conversion: f64 gain then another integer quantization, advanced only by accepted frames. The low-bit fixtures use unity gain; the membrane benchmark excludes live gain and ALSA pacing. See the corrected diagram and software-proof scope in that report. Locked Baseline02 reads observe S16 44100/48000 constraints and idle runtime PM; fresh playback/CPU measurements remain NOT_RUN due to lock contention.

UART01 bounded real FFmpeg/ALSA fixture playback and demand wake pass with no recorded decode/filter/XRUN errors. Wired hardware output remains S16 stereo 44.1/48 kHz; native wider/high-rate output, perceptual fidelity and endurance remain separate. Baseline02 retains the paired current Reborn source and ARM checks.

[Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) carry exact identities, counters and limits.

## Historical source research and physical checkpoints

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Audio and FM evidence

Latest bounded physical result, 2026-09-27: Fix01 played silent S16 44.1 and 24/96 -> 48 fixtures with zero XRUN/decode/filter errors. This adds software/device operation evidence; it does not prove audible fidelity, real end-of-track crossfade, native wide/high-rate output, Bluetooth peer playback or endurance. The historical AUDIO-02 checkpoint below remains its own earlier test. [Fix01 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md%23playback-connectivity-and-recovery&anchor=playback-connectivity-and-recovery).

Current physical checkpoint: AUDIO-02 now produces owner-confirmed clean S16 stereo44.1kHz headphones. The notification fix is deployed and tested. [Current result and exact limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-01-live-result.md) supersede the historical untested/gated claims below.48kHz/LR/restart checks remain; M4/M5 and high-resolution implementation have not started.

2026-09-10 M3 ACTIVE: owner authorizes one integrated headphone-first ALSA candidate, with #27 reconnect explicitly deferred. [Implementation and source review](m3-audio-architecture.md); [deployment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m3-audio-01-deployment.md). Earlier gated wording below is historical. Physical M3 acceptance remains open.

2026-09-10: [porting history and failures](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md) corroborate external CON3/DL1 and distinguish digital DAC probe success from VGP2-powered analog operation. Their observed amplifier is OCA72559 ID09; our revision/rails/jack/clock accuracy remain untested. Capture M3 tests for DMA/IRQ continuity, supply brownout and scheduling underruns separately. M3 remains gated; the wired ALSA/Rust/C plan is unchanged.

## Donor integration input — 2026-09-09

M3 remains gated on M2. [Complete reuse audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md) and the immutable `donorSource/sound/soc/mediatek/mt6582/` now replace discovery from zero as the starting point. None of these donor claims is a new audio measurement on our Y2.``

| Contract | Donor implementation to preserve/review for v6.18 |
| --- | --- |
| AFE | 11220000, SPI104 level-low; DL1 base/current/end offsets40/44/48, IRQ control/status/clear/count at3a0/3a4/3a8/3ac. Uses shared MediaTek memif/IRQ framework and 32-bit DMA mask. |
| DAI | DL1 I05/I06→O00/O01; external second-I2S uses CON3 offset4c and FPGA_CFG1 bit4. 32-bit slots, 64 bit clocks per frame, rate table8–48kHz; this is a driver limit, not a proved hardware maximum. |
| Clock/PM | infra_audio, audintbus and audio CCF handles. Review runtime-resume failure unwinding, regmap errors and IRQ/substream lifetime against the v6.18 common AFE implementation. |
| CS43131 | Upstream cs43130 driver, I2C1:30, IRQ16, 22.5792MHz crystal; machine sets serial clock to rate×64. VGP2 plus GPIO20→18 and GPIO15 sequencing need electrical/supply validation. |
| Amp | I2C1:58, enable8; AW87559 ID5a / alternative OCA72559 ID09. Tables and enable delays retained in donor aw87559.c. Add mute/drop-enable on write failure and safe shutdown. |
| Routing | Headphones use HPOUTA/B; amplifier input takes both. Speaker DAPM event writes DAC PCM_PATH_CTL_2 mask7, mode5 versus stereo0. Independent switches do not enforce headphone/speaker exclusion; review jack integration, event return and pop-safe ordering. |
| FM | ASRC/gain2/32kHz route is donor reference only. Owner confirms the older physical Y2 lacks usable FM reception hardware. Do not enable this path or make reception an exit requirement for this board. |

The 6.12 machine driver uses card/DAI structures and shared static mutable state that must be adapted to 6.18, with proper DT reference/device lifetime and resource ownership. Real ALSA playback, rate/format/IRQ/DMA integrity and analog levels remain M3 tests before player features. Original historical evidence follows.

Date: 2026-09-08. Related task: Y2E-101; archived evidence reviewed, no active audio investigation in this session.

CONFIRMED in the integrity-verified `2026-07-29_004935` snapshot: `1-0030` binds `cs43131_dac`, `1-0058` binds `aw87559_pa`, `/proc/asound/cards` reports no soundcards. These observations identify a vendor-controlled system; `/dev/cs43131_dac` is not established as a PCM sink.

The exact archived stock primary HAL hashes to `5c5162f6a68f7db57febd050ee88cc886779dcce5948937149d6cd211eb0e6de`. Later `Y2_AUDIO_PATH_PHASE4_SECOND_I2S.md` and `out/afe-runtime/2026-07-30_135519/` supersede parts of earlier primary-I2S analysis and support a second-I2S/DL1 route. Treat the complete electrical/analog route, PMIC role, actual slot width, supported rates and analog performance as INFERRED/UNKNOWN until their specific evidence is reviewed. Android's observed 44.1-kHz PCM16 output does not set a Linux hardware maximum.

The current generated boot manifest records a CS43131 idle-resume kernel patch. Its installed presence is UNKNOWN. Avoid conflating that artifact with the exact original kernel analyzed offline.

FM feasibility reports record chip ID 0x6627 and tuning/routing experiments. A successful open/tune is not evidence of useful RF reception or a populated antenna path on this unit. Release notes distinguish hardware revisions, but the current unit's revision and original manufacturer evidence have not been established here.

Next passive proof: re-identify bound audio devices on the current build and reconcile exact HAL/kernel/firmware lineage. Later pin down reset/IRQ/supply/mute/clock ordering and headphone/speaker/PMIC topology before designing ASoC work. No raw node writes, guessed ioctls, live register dumps, bus scans, playback/rate changes or kernel patches are authorized by this document.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
