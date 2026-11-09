---
title: "Current source and hardware boundaries - Innioasis Updater"
description: "Current source and hardware boundaries <!-- knowledge-base-scope: maintained-summary; baseline02-sync 2026-10-03 -- Current Baseline02 / UART01 scope UART01 closes bounde"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-platform-v1-hardware-gates.html"
---

# Current source and hardware boundaries - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Current source and hardware boundaries

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Current source and hardware boundaries

## Current Baseline02 / UART01 scope

UART01 closes bounded C1/C2/C3 architecture: timer/context/CIRQ/clock restore, natural parking, hotplug, five guarded OPPs and affected storage/playback/USB regressions pass. Baseline02 is sealed with automatic qualified CPU0 C3 policy; new-image cold boot is PHYSICAL_NOT_RUN. Retain all entry and fault guards. Full system suspend, native high-resolution audio, wider radio/USB/storage/endurance, electrical battery calibration and public distribution retain independent gates. Historical fixed-voltage/WFI-only recommendations below do not describe the current runtime architecture.

[Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) carry exact identities, counters and limits.

## Historical source research and physical checkpoints

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Platform v1 source and hardware boundaries

Latest physical boundary:[CPU Final Fix01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md) on 2026-09-27 physically verifies GPT6/GPT4/PPI29, highres/NO_HZ, real Reborn QoS, lower OPPs, hotplug and WFI. SLIDLE is blocked by MSDC0/1 runtime clocks, 1196/1300 fail PWRAP readiness, first devices-stage suspend loses recovery, and loaded USB loses the connection. The 2026-09-23 review below records the older Platform v1 source gate; its WFI-only/100-Hz and disabled-threshold wording does not describe this latest Fix01 image. See [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) for enabled provisional low-voltage policy and precise remaining gates.

2026-09-23 software review; no physical access. Exact primary-source URLs and hashes are in [the research inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/platform-v1-feasibility-sources.json). The retained [GPU-01 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md) contains narrow S16/44.1 playback and an adverse same-boot suspend result. Later source repairs do not supersede that physical failure without a new test.

## CPU, idle, memory and suspend

Keep 598/747.5/1040 MHz OPPs, the existing fixed voltage, WFI-only cpuidle, NO_HZ_IDLE/HZ=100, reserved regions and current thermal trip points. Collect frequency/idle residency, per-core load, interrupts/context switches, RSS/PSS, LOWMEM/HIGHMEM, page cache/slab, die temperatures and XRUNs for idle UI, screen off, FLAC16/44, 24/96 downsampling, EQ/crossfade, scan/artwork, Wi-Fi and SBC. No available measurement answers whether 598 MHz or fewer cores meet deadlines. The owner may compare supported governor/frequency policies after a baseline; do not infer a voltage change or copy one from a donor.

The pinned MediaTek [idle policy](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_idle.c) requires a single online CPU, clock exclusions, timer budget and early-suspend conditions. Its [SPM implementation](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_spm_sleep.c) has a distinct deep-idle PCM program, PMIC variants, UART handoff, interrupt/CIRQ handling and CPU context/timer restoration. Those are not established for the Y2 board by the existing full-suspend program. Deeper cpuidle is BLOCKED_BY_EVIDENCE / PHYSICAL_GATE; no speculative SPM code is added.

`y2-suspend` now refuses by default. The explicit `--owner-qualify` escape is only for the separately controlled resume experiment, never automatic UI idle. It retains the existing exclusive activity lock, radio-off checks and restoration. Reborn ALSA handles already hold a shared `/run/y2/activity.lock` for their whole lifetime; `y2-radio-hold COMMAND...` provides the same scoped lease for transfer work. Applications may use a shared nonblocking flock directly, close on exit, and treat an unavailable/exclusive lock as refusal. A lease is not proof of safe suspend; ordinary Platform v1 suspend stays disabled. Do not run the experiment with unsaved work, active update/maintenance or an unproven wake/recovery path.

## Internal audio and CS43131

Current AFE DMA consumes interleaved stereo S16, with direct hardware rates 44.1/48 kHz; the product allowlist remains S16/44.1. The I2S serializer uses 32-bit slots, which proves neither wider DMA fetch nor preserved source bits. The reviewed pinned vendor [AFE header](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/sound/mt6582/AudDrv_Afe.h) and associated source expose rate/channel/buffer configuration and independent I2S word length. They do not establish a Y2 DL1 high-definition fetch/alignment and interconnect path. Absence here is not proof the silicon cannot support it. Registers from newer MT8167/MT8173 hardware are not interchangeable evidence.

The pinned Linux 6.18 `sound/soc/codecs/cs43130.c` supports CS43131 clock families and wider formats, but that alone cannot qualify MT6582 fetch/clocking or board analog topology. Existing hardware volume/filter controls remain available. Load-measurement DT properties are absent and automatic impedance/gain policy remains disabled. S24/S32, preserved 24-bit and 88.2/96 kHz are unavailable, BLOCKED_BY_EVIDENCE / PHYSICAL_GATE, until the complete path is established.

`y2-audio-contract` queries combinations without committing hw_params or writing PCM. An occupied direct PCM may return Unavailable. Its `--device null` option is host/QEMU validation only. `tools/host/audio_precision.py OUTPUT` creates 24-bit WAV plus exact S24-in-32/S32 references and independent channel patterns; nonzero low bits reveal S16 truncation. It never plays them. After a future source-backed driver change, owner acceptance must compare DMA/sample words and logic captures, MCLK/BCLK/LRCLK at each supported rate, both channels, switching, XRUNs and analog pop/click behavior. Do not activate unsupported masks or rates to try these fixtures. Packed 24-bit file decoding already works; that is a different capability from high-resolution internal output.

## Reset evidence and watchdog

Previous boot ID/stage/orderly preparation and private bounded syslog tails are captured before this boot starts logging, once per boot. The status API exposes only metadata/hashes; `y2-platform boot-evidence` retrieves the private record. There is no claim that a panic reached persistent storage. Syslog rotation is bounded; no extra polling logger or reserved RAM was added. An unclean previous boot remains an observation, not a diagnosed watchdog/panic or electrical reset.

The existing Linux 6.18 MediaTek AP watchdog driver supports normal watchdog operations but does not populate a proven MT6582 reset-cause register. Its bootstatus zero is not an affirmative reset diagnosis. AP watchdog arming stays disabled; the charger watchdog is unrelated. Ramoops/pstore needs proven retained RAM placement across stock loaders; no reserved region is reclaimed or guessed.

Before an AP watchdog policy can ship, owner qualification must establish timeout clock, disable/magic-close behavior, actual reset and storage/loader recovery, then a durable bounded boot-attempt budget and rescue escalation. First test normal keepalive/disarm on a recoverable qualification image; only a separately approved session may stop keepalives. Do not make an untested watchdog the production recovery path or repeatedly reset after an unknown boot failure.

USB host/OTG remains unavailable until connector ID/role wiring, VBUS switch, source current and PHY behavior are established. No VBUS path is enabled.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
