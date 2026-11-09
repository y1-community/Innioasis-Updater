---
title: "D14 — Self-observable initramfs diagnostics - Innioasis Updater"
description: "D14 — Self-observable initramfs diagnostics <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-on-screen-diagnostics.html"
---

# D14 — Self-observable initramfs diagnostics - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# D14 — Self-observable initramfs diagnostics

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# D14 — Self-observable initramfs diagnostics > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current hardware result: [owner-observed M1 runtime success](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md) confirms Linux 6.18, native PID1, increasing BEAT/uptime, working sleep, proc/sysfs mounts, CPU0, D08 RAM visibility, framebuffer diagnostics and stopped-watchdog status. M1 core achieved. Exact flashed hash and unreported diagnostic fields remain unverified. Earlier dated statements below are historical.

Y2B-245 [#20](https://github.com/SchulzCode/Y2Linux/issues/20), offline successor to the owner-observed solid-green PID1 stage of Y2B-240. Green is evidence of Linux 6.18 executing initramfs `/init` as PID1 and reaching the framebuffer stage. No white-half heartbeat or checkerboard result was reported. The M1 Linux-plus-PID1 boot objective is achieved; timing/stability remain unverified.

## Narrow text interface

Keep the exact D13 read-only watchdog/OVL/DSI snapshot and guard predicate. Only the already-proven visible RGB565 aperture `[0xbfb00000,0xbfb54600)` is written, with the same 16-bit writes, WC mapping and final write barrier. Neither DT hardware/memory nor entry watchdog instructions change.

The kernel exposes one character device, major 120 minor 0, named y2diag. Major 120 is in upstream v6.18 `Documentation/admin-guide/devices.txt`'s 120–127 local/experimental character range. Registration fails on collision; it does not take over an existing device. The immutable initramfs contains root-owned `/dev/y2diag`, mode 0600. There is no mmap/read/ioctl or raw-address operation. Writes additionally require task PID1, exact 804-byte packet length, magic `0x59325431` and 800 printable ASCII bytes. A mutex protects staging. The packet has no framebuffer address, dimensions or hardware settings.

Using a character endpoint instead of procfs for text permits PID1 to display proc/sysfs mount failures. Failure to register/open this endpoint necessarily leaves the last kernel/loader screen; it cannot display its own missing-output error. Likewise guard refusal leaves the previous frame unchanged. A counter that stops changing is evidence to record, never proof the last status remains current. No unsafe alternate mapping/display initialization is attempted.

## Screen and progress

Original 5x7 glyphs doubled in both axes occupy 12x16 cells: 40 columns, 22 rows. The remaining bottom eight scanlines are black. Kernel-only rows show the diagnostic title and watchdog-stopped/framebuffer-guard status, refreshed only after a successful live guard check. PID1 supplies the remaining 20 rows. Lowercase is rendered as uppercase. White text on black plus green status avoids dependence on distinguishing RGB versus BGR for colored text.

PID1 presents its first frame before mounting proc/sysfs, records both mount return codes, and starts the visible loop before optional data collection. After each successful one-second sleep, its beat count and marker change. Screen updates precede each bounded read, so an unexpected stall has a visible last operation. Release comes from `uname`, independent of proc/sysfs mounts and the deliberately disabled PROC_SYSCTL configuration. Runtime fields include release, CPU part, CPUs online, MemTotal, uptime/idle and CPU0 `mtk-clkevt` IRQ count. SoC compatibility and D08 RAM are read from live DT properties and explicitly labelled DT-described; they are not newly detected physical silicon/RAM capacity. Described memory is 24 MiB plus 512 KiB, not a claim of all 1 GiB being usable.

Each file has at most eight read attempts and a 4096-byte cap; descriptors are nonblocking and always closed after successful open. Missing fields, oversize data, open/read/close errors and exhausted interrupted-read retries are explicit negative errno values. `~` marks a truncated display row. Last error is sticky; successful later operations do not erase it. Previous frame write result is labelled previous because the current result is known only after that frame is submitted. Successful packet writes return 804.

The MTK GPT clockevent name comes from audited v6.18 `drivers/clocksource/timer-mediatek.c` and the timer-of IRQ registration path; missing or changed proc interrupt formatting yields an explicit error. Uptime, IRQ count and a checked sleep counter are separate displayed values; their changing values must be observed before claiming timing works.

After 50 successful one-second sleeps, display STOP / RESTORE ANDROID and pause indefinitely. A sleep error displays STOP / SLEEP ERROR then pauses. There is no retry/reboot/poweroff, new persistent write or automatic next test. Rendering, reads and startup add overhead: this is not an exact 50-second wall-clock duration. The 60-second external limit from power-on still governs any later authorized experiment and may precede the final screen.

## UART independence and first-trial interpretation

Y2B-240 wrote proc/sysfs dumps to `/dev/console` after green and before entering its heartbeat loop. Its blocking write loop and the active UART console could delay or stall progress in that interval. The green-only owner report cannot distinguish this from missed transitions, sleep/timer trouble or a later hang. This is a possible explanation, not a diagnosed UART fault.

Y2B-245 neither opens the console nor writes to it during normal PID1 execution; the screen-write handler performs no printk. The QEMU ARM syscall fixture traps any normal PID1 console write and tests successful and failing collection loops. UART support and existing early console configuration remain unchanged for optional early kernel output; generic kernel logging is not redirected into a new display console. Hardware behavior of the new text candidate is untested.

Host preview and syscall fixtures are synthetic, never device screenshots or evidence of Linux hardware success. D08, emitted watchdog code, image wrappers, partition bounds and full clean-build reproducibility remain mandatory.

## Proposed first M2 subsystem, after a successful diagnostic trial

Research USB device-mode diagnostics for a host serial link (CDC ACM) as the next platform boundary: it could export full logs without physical UART pads. Upstream [gadget serial documentation](https://docs.kernel.org/usb/gadget_serial.html) describes the host serial function, not MT6582 platform readiness. This first requires MT6582 controller/PHY, clocks, interrupts and DMA ownership to be researched and specified. Android ADB working does not prove upstream Linux USB support or authorize reusing inherited USB state. No USB code, networking, mass storage, Debian or M2 hardware experiment is part of Y2B-245.

Build runner: verified cache overlays are reused without rewriting their inode. New overlays are patched in private temporary files and atomically published only after hash verification. This removes the shared-overlay rewrite race caught by the config validator during an unpublished development build.

## Real hardware follow-up

Y2B-245 reached the real text renderer and PID1 with both mounts successful, then stopped at sleep -38 with BEAT 0. [Exact report and time32 ABI diagnosis](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2b245-hardware-result.md). Y2B-250 changes only kernel time32 syscall availability; the D14 renderer and PID1 state machine remain unchanged. Continued heartbeat execution still needs testing.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
