---
title: "Y2A-300 — M3 current state, 2026-09-10 - Innioasis Updater"
description: "Y2A-300 — M3 current state, 2026-09-10 <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2a-300.html"
---

# Y2A-300 — M3 current state, 2026-09-10 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2A-300 — M3 current state, 2026-09-10

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2A-300 — M3 current state, 2026-09-10 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

ACTIVE / NEAR COMPLETION. AUDIO-02 is deployed; native wired headphones are physically clean at S16 stereo44.1kHz. The period-notification fix `137b3f2` is built into `8f93e44` and physically tested (3.13s,130IRQs, advancing ALSA pointers, no reported underrun; owner: "perfect, no clicking!"). Do not deploy it again.

[Current result, architecture and evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-01-live-result.md). ALSA card `Y2Audio`, PCM0 `Y2 Headphone Playback`; correct CON3 path, upstream CS43131 and VGP2=1.8V. Tools/WAVs persist on SD via committed Buildroot content.

Remaining short core qualification:
  - Confirm current AUDIO-02 identity; the notification fix is already deployed/tested.
  - Quiet S16 stereo48kHz physical playback.
  - Explicit left/right separation.
  - Short stop/start/repeat, with owner listening and IRQ/PCM/dmesg checks for

distortion/pops/reset/underruns.

Do not reopen AFE/CON3/DAC/VGP2 discovery.32-bit I2S slots carry16-bit PCM; 24/32-bit and higher rates are unimplemented later enhancements. Speaker/amp identity, jack and precision clock validation remain explicitly separate gaps. After core qualification, audit the roadmap before M4. M4/M5/Y2PlayerNative are not started; #27 USB reconnect remains unresolved/deferred. No new feature, build, flash or device change during session close.

## Historical authorization and broader scope

## Active implementation authorization — 2026-09-10

Owner explicitly activates M3 against physical DEV-02 (`d76e57f`), with USB reconnect #27/#28 deferred to later qualification. Implement/build one integrated headphone-first ALSA/ASoC candidate; stop for manual BOOTIMG-only deployment. No source-only M3 closure. [Boundary audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23m3-activation-audit--2026-09-10&anchor=m3-activation-audit--2026-09-10). Earlier gated/deferred language below is historical and superseded by this entry.

## Platform-first gate — 2026-09-10

The owner now requires M2 core/Buildroot, complete M3 native audio, M4 full power, M5 connectivity, GPU/lima and final whole-platform qualification before Y2PlayerNative begins. This supersedes earlier wording that allowed central application work after a wired-player slice. DEV-02 qualifies the core resources but USB reconnect remains the immediate #27/#28 blocker. This checkpoint grants no new hardware-phase or flash authorization. [Live result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md).

# Y2A-300 — M3 native audio and analog routing proof

## Additional evidence — 2026-09-10

Retain the experimentally separated silence causes: CON1 can run DMA/IRQs with dead external pads; CON3 drives second-I2S, while VGP2-off can reset a digitally responsive DAC as I2S starts. This corroborates our HAL work. Their OCA72559 ID09, jack and audible wired results require verification on our older unit; 44.1-kHz clock accuracy remained open. Use v6.18 AFE helpers/upstream CS43131 support with corrected routing/error/lifetime design. Distinguish DMA faults from measured userspace scheduling underruns. M3 implementation follows genuine M2 completion; shared supplies belong in #23.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Donor update 2026-09-09: M3 remains gated. Retain donor DL1/second-I2S AFE and machine driver, upstream cs43130 support for CS43131, AW87559/OCA72559 tables, GPIO20/18/15 supply sequencing, GPIO8 amp enable and IRQ16 jack clues. Adapt v6.18 ASoC/lifetime/DMA/error paths and validate real rails, safe mutually exclusive headphone/speaker routing, clocks/rates and PCM. Do not restart audio reverse engineering from zero or begin application work. FM route is excluded on this older board. See [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md).

Canonical epic [#29](https://github.com/SchulzCode/Y2Linux/issues/29); [coverage audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

Deferred planning epic; no implementation-ready children added by this audit.

## Goal / why this epic is needed

Represent the blueprint's native-audio gate before substantial Y2PlayerNative audio development. Android bindings and HAL observations are reference evidence, not a working Linux ALSA/ASoC path.

## Dependencies / evidence

Core clocks/pinctrl/I2C/IRQ/DMA and sufficient measured memory under the core platform epic; supply ownership under #23/power epic; useful diagnostic capture. Use `docs/knowledge/audio-path.md` and its later second-I2S/DL1 stock references. Historical bus1 CS43131 at 0x30 and AW87559 at 0x58 identify research targets. Verify board/revision and exact driver applicability before choosing bindings.

## High-level coverage

MT6582 AFE/ASoC CPU DAI, correct I2S instance, DMA/FIFO/IRQ, PLL/MCLK/BCLK/LRCK and formats; codec I2C/reset/supplies; CS43131 upstream-driver applicability; machine/DAI route; separate amplifier/speaker path, headphone detection/ACCDET, mute/volume and pop-free sequencing. Capture firmware/calibration requirements if evidence identifies any; do not presume a codec binding supplies SoC support.

## Exit evidence / unlocks

A real ALSA PCM device plays known samples to the actual intended output. Record negotiated format/rate, channel correctness, safe level/routing, underruns, repeated start/stop/idle-resume and error behavior. Supported rates and bit depths are measured end-to-end, not inferred from a DAC specification. A tiny CLI/FFmpeg proof precedes player architecture. Gate D unlocks serious native audio work; speaker/high-resolution/Bluetooth may be separately declared follow-ups.

## Out-of-scope / stop

No player/decoder/DSP feature backlog or Android source port. Do not route audio through PipeWire merely for wired playback. Stop at uncertain analog wiring, unsafe gain/mute, clock/DMA mismatch or unverified supply/reset; no guessed live ioctls or playback experiments. FM and Bluetooth transport are separate gates.

## Execution and validation boundary

High-level planning epic only, not an implementation task or hardware permission. Expand only the next evidence-backed change when this phase is activated; preserve existing stable IDs and link existing issues instead of duplicating them. No speculative driver task list, build, flash or experiment is authorized by this epic.

Before closing the phase or proceeding through its exit gate, repeat the [standing roadmap/gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) using real hardware results. Separate owner reports, retained artifacts, source support and actual device validation. Unknown dependencies stop the relevant path; do not guess hardware or silently broaden scope. Milestone qualification uses the appropriate full verification boundary; small later fixes keep targeted validation and D08/package checks without routine provenance re-audits.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
