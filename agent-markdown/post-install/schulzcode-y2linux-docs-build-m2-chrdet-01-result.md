---
title: "M2-CHRDET-01 — owner result received - Innioasis Updater"
description: "M2-CHRDET-01 — owner result received <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-chrdet-01-result.html"
---

# M2-CHRDET-01 — owner result received - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-CHRDET-01 — owner result received

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-CHRDET-01 — owner result received > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09 update: [returned photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) confirm successful CHRDET reads in both reported cable-at-startup conditions. Connected startup returns a guarded PHY refusal (6a=BE, W0), while no-USB photos show wake success. The next candidate is [M2-USBGUARD-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbguard-01-result.md), exposing the hidden raw guard inputs. The original offline validation and test instructions below are retained as the historical handoff; “not tested” no longer describes current status.

2026-09-09, #23/#27 prerequisite under active M2 #28, baseline 305f8f9. Offline validated; not flashed or hardware tested. The previous [same-boot PHY wake pair](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-hardware-result.md) confirms the guarded release and BEAT 10→49 with no reported errors and USB connected.

`/home/luca/Dokumente/Code/Y2Linux/out/m2-chrdet-01/BOOTIMG.img`

1,097,728 bytes; SHA-256: `e511fb89e45326673183f426a4bdd3b6ca708c25bf3e6ceecfc4a67478aa9660`.

Screen/build M2-CHRDET-01, Linux 6.18.0-y2-m2-chrdet1. [Exact access contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-probe.md).

Adds one PMIC CHR_CON0 read at 0x0000 through the proven bounded PWRAP transport, after CID/VUSB. Shows the raw value and bit5 charger-presence indication. This tests the independent PMIC indication while the connected cable still leaves MAC DEVCTL at 80. It cannot identify a USB host, cable data integrity or voltage. The guarded PHY 6a release remains unchanged. No added PMIC register, charger, analog/calibration, VBUS-force, clock, MAC-connection or DMA-control write.

## Validation
  - One clean pinned Linux 6.18 / Clang 20.1.8 build, no compiler warnings/errors.

All 18 selected test methods pass: 26 PWRAP fault/status scenarios, 10 clock, 37 USB-state, 48 PHY-wake, 22 QEMU ARM PID1 cases and affected artifact, BOOTIMG, D08, time32 syscall, framebuffer/text and watchdog checks. The new cases cover both status states and third-read completion/ack failures; invalid data is visibly unknown and PID1 continues through its bounded loop.
  - Linked snapshot c0015208 remains PID1-only/cached, exactly 260 bytes.

c0015830 supplies address zero; c0015840 calls the read helper after successful CID/VUSB. c0015844..54 sets validity only on success. The helper issues the read-only AP+9c command then acknowledges AP+a4 only after completion, with the two existing 1000-poll/10-us bounds. Existing PHY byte write c0015b90.
  - Resolved config differs only in LOCALVERSION; DT, D08, DMA and packaging policy

unchanged. [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-chrdet-01-layout.json) and [iteration record](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-chrdet-01-iteration.json) pass complete wrapper, LK read-tail, current-memory and 16 MiB partition bounds. Gzip 6020 bytes, resident kernel [0x80008000,0x8029f5b0), initramfs ends 0x84001784, decompressor workspace ends 0x803909f0.
  - Build-relevant source hashes match the validated layout. Output retains the

project snapshot, input lock, ELFs/config/logs, focused linked disassembly and artifact hashes. No duplicate build or unchanged source/ROM/recovery audit.

No device operation was executed. Stock preloader/LK, partition tables and persistent calibration remain protected. M1 stays complete; M2 remains open.

## Owner test

Use the established BOOTIMG-only procedure, with the **USB data cable attached to the Linux PC, maximum 60 seconds from power-on** and existing manual restoration boundary. Expected: continued heartbeat to BEAT 50/STOP, usually `PW:0 /7 CLK:0/15`, `CHR:xxxx D:0` or `D:1`, and the existing wake/trim rows. Both detection values are useful results, not errors. No ttyACM/enumeration is expected yet. `CHR:---- D:?` means the read is invalid; retain the exact PWRAP error/validity and last stage. A guarded PHY refusal remains useful evidence.

Return two readable full-screen photos from the same boot, near BEAT 10 and BEAT 50/STOP, saved in `out/m2-chrdet-01/`. Include the new CHR/PW/CLK row, all bottom four PHY rows, timer/uptime/MemTotal and LAST ERR. Report whether USB stayed connected, any freeze/reset, and restoration outcome if performed. If it stalls, return the last visible stage and approximate elapsed time; do not extend the existing observation window.

Retained prior candidate: `out/m2-phywake-01/BOOTIMG.img`, SHA-256 `d68c8fbc56721c7aa1fda5b3e321a9aff5876661aac857505864e28d8924793a`. Stop for this owner test. USB controller ownership/logging and M2 exit are not claimed; #23/#27/#28 stay open and M3 remains deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
