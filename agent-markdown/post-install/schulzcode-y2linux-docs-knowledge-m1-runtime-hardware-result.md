---
title: "M1 — Continued native PID1 execution on the physical Y2 - Innioasis Updater"
description: "M1 — Continued native PID1 execution on the physical Y2 <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m1-runtime-hardware-result.html"
---

# M1 — Continued native PID1 execution on the physical Y2 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M1 — Continued native PID1 execution on the physical Y2

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M1 — Continued native PID1 execution on the physical Y2 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Recorded 2026-09-08 from the owner's explicit report of today's real Y2B-245 diagnostic hardware test. This is owner-observed hardware evidence, not a host fixture, synthetic preview or a device observation made during this documentation session.

## Confirmed in the owner report
  - Linux version displayed: `6.18.0-y2-m1`.
  - Native initramfs PID1 running.
  - BEAT increases; sleep works; uptime increases.
  - `/proc` and `/sys` mounted.
  - Framebuffer diagnostics work; watchdog reports stopped.
  - CPU0 online; static D08 RAM visible.

**M1's core objective is achieved: Linux 6.18, initramfs and native PID1 are running on the physical Y2, with observed periodic execution.** The earlier sleep -38 report remains historical evidence of a separate failed iteration, not the current result. This observation is consistent with the time32 fix in Y2B-250 #21; the owner calls the successful test Y2B-245. Do not silently relabel the flash or assert an exact binary identity from the version string.

## Scope and diagnostic oddities kept separate

The report does not supply the flashed BOOTIMG hash, numeric counters, full screen text/photo, FRAME progression, timer IRQ count/rate, precise MemTotal, elapsed duration, terminal 50-beat STOP stage, reset history or this trial's restore outcome. These are unreported, not failed checks. No new oddity beyond the historical ENOSYS failure is invented; any other diagnostic discrepancy needs its exact screen field/value before diagnosis.

The retained Y2B-250 offline candidate is 1,093,632 bytes, SHA-256 `074c3e6946e6e8ac61bc1df0da4fa53807071dd50ae3db4def97563c9207afce`. That is a candidate identity, **not an independently verified identity of today's flashed bytes**. The previous linked-ELF proof of the time32 fix remains in [y2b250-result.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2b250-result.md).

Working sleep/uptime establishes timer-backed progress as observed, not timing accuracy or a stress/stability certification. D08 visibility establishes this map boots, not safety of the rest of the 1 GiB or all inherited DMA. The watchdog status concerns the reviewed AP_RGU check, not all potential reset sources. Inherited RGB565 display output is not native panel/DRM/backlight support. Physical UART remains unverified and is not required to acknowledge this result.

## Session boundary and next work

Only evidence and planning were updated today. No device access, implementation, Linux build, BOOTIMG creation or flash was performed in this session. No M2 execution has begun. [The five historical foundation research issues](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md%23historical-foundation-research-queue&anchor=historical-foundation-research-queue) prepare later implementation one evidence boundary at a time; the native player, audio, networking and persistent rootfs remain outside this wave.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
