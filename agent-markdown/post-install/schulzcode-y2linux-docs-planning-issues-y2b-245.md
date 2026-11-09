---
title: "Y2B-245 — Useful on-screen Linux diagnostic environment - Innioasis Updater"
description: "Y2B-245 — Useful on-screen Linux diagnostic environment <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-245.html"
---

# Y2B-245 — Useful on-screen Linux diagnostic environment - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-245 — Useful on-screen Linux diagnostic environment

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-245 — Useful on-screen Linux diagnostic environment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2B-240 #19: the owner observed solid green, proving the implemented PID1 diagnostic stage. No heartbeat/checkerboard result is claimed. M1's Linux plus initramfs PID1 boot objective is achieved; continued execution and richer diagnostic output remain to be demonstrated.

Implement offline only. Keep D08 RAM, CPU0, DT hardware, loader packaging, watchdog entry and D13 hardware guard unchanged. No deployment in this issue.

## Intended change (D14)
  - Tiny 5x7 bitmap font doubled to 10x14 pixels in 12x16 cells: 40 columns,

22 rows, inside the proven 480x360 RGB565 aperture. Kernel owns two status rows; PID1 supplies 20 bounded text rows. No display-controller writes.
  - A root/PID1-only character endpoint `/dev/y2diag` at local experimental

char major 120, minor 0 accepts only a fixed, versioned text-frame packet. No mmap, raw address, arbitrary pixel or register access. It permits reporting failed proc/sysfs mounts without depending on those mounts to paint.
  - Fresh framebuffer/watchdog guards before every frame; kernel status reports

only successful guard observations. Invalid guard state stops pixel writes.
  - PID1 first presents status, then gathers bounded read-only runtime values

with visible progress markers. Show version, PID1, CPU/board identity with DT-described versus runtime values distinguished, CPUs online, MemTotal and D08-described RAM, uptime, timer IRQ count, heartbeat and mount/error status.
  - No PID1 console dumps or hot-path printk. UART hardware/console support stays

compiled for optional early output. Screen refresh must not await UART drain.
  - One-second checked sleeps, changing counter/indicator; bounded 50-iteration

diagnostic run followed by a clear STOP/RESTORE screen. Host 60-second limit still governs any later authorized experiment. No automatic reset or flash.

## Acceptance
  -  Font, frame validation and pixel bounds tested against malformed frames.
  -  Runtime formatting/parsing and failure paths tested; no silent truncation

or timer/read success inferred from an unchecked return code.
  -  Actual ARM PID1 screen loop exercised with a host syscall fixture, including

failed mounts/read/sleep and a console-write trap; distinguish from hardware.
  -  All existing D08/artifact/packaging/watchdog tests pass without weakened limits.
  -  Two fresh locked builds match; reviewed source/artifact hashes retained.
  -  BOOTIMG retained separately from Y2B-240; exact hash and expected screen

sequence documented. No flash performed; no automatic M2 work.

Completed offline: source `d83fccfcc03f86f2085ed1279aa3dce352fcf8fe`; two clean builds match and all 14 tests pass. Candidate: `out/m1-y2b245-diagnostics/BOOTIMG.img`, 1,091,584 bytes, SHA-256 `f2c048405c7aafc5c368d51b85a9eeb9d9f42ee3b1a6abe308701e5b551c52a0`. [Result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fbuild%2Fy2b245-result.md). No flash performed; this issue does not authorize a new hardware trial.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
