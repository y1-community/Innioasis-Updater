---
title: "Y2Linux 1.0 Beta 7.11 (Baseline 74) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7.11 Baseline 74 Status: PUBLISHED as GitHub release baseline-74 2026-10-17. Release 1.0.0-beta.7.11 , Reborn 1.0.0-beta.7.11 , kernel 6.18.56-y2linux-1."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-7.11.html"
---

# Y2Linux 1.0 Beta 7.11 (Baseline 74) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7.11 (Baseline 74)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 7.11 (Baseline 74)

Status: PUBLISHED as GitHub release `baseline-74` (2026-10-17). Release `1.0.0-beta.7.11`, Reborn `1.0.0-beta.7.11`, kernel `6.18.56-y2linux-1.0.0-beta.7.11`, update sequence 6352, Linux `9c3e4f1`, Reborn `814cd14`. Built with `tools/production/release.py` in 101 s on top of Baseline 73: container suite 766 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-7.11 and the USB-RX-DMA update in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md); design and full results in [USB-RX-DMA-MODE1-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FUSB-RX-DMA-MODE1-PLAN.md%23results-2026-10-17&anchor=results-2026-10-17).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | f90f42c3c72c967042ce41c8e4345ef52f12d1d6b3e845375d64a6d985155ed2 |
| Y2ROOT | 016ea5681360072d21fd5fc616242a2cd0c2dfa2c911b0dc46af99f6ea366f94 |
| RECOVERY | 6fdcd8c66c783553583c40f6e39dbd7e05fffd16b4b568df45d1f84382006a1a |
| Y2DATA (no SSH key) | 9dc3cba5b60daea0ea7107ca46f08193f19fcb009154f1bb864da991ca906aa4 |

## Since Beta 7.10````````````````

| Part | Change |
| --- | --- |
| Faster copies to the player | Multi-packet (mode 1) receive DMA for USB bulk OUT: one DMA program per request (64 KB for MTP) instead of a CPU read of every 512-byte packet. At the transfer's short or zero-length packet the CPU waits until two samples agree (RXCOUNT counts down while the engine unloads a packet), stops the channel and reads only that packet. On by default (rx_dma=2); echo 0 > /sys/devices/platform/11200000.usb/rx_dma returns to PIO, never to mode 0. The stock MediaTek kernel (REA) used mode 1 only for mass storage. (Linux 1f86b4f, b49afaa, 049df5c, 10ec3eb) |
| Test tool | tools/usb/mtpbench.c reads the closing zero-length packet of a download that fills its last read. (64af1b2) |

## Device result (owner's player, test builds of this release, every byte SHA-256 verified)

|  | Beta 7.10 (PIO) | Beta 7.11 |
| --- | --- | --- |
| Upload, Internal Storage 1 GiB | ≈10 MB/s | 29.6 MB/s |
| Upload, SD card 512 MiB | ≈9 MB/s | 23.3 MB/s |
| Upload over SSH (USB Ethernet) | 6–8 MB/s | 10–14 MB/s |
| Download | 37.7 MB/s | 37.5–37.9 MB/s |
| USB interrupts during an upload | ≈22 000/s, one core busy | ≈1 450/s, CPU ≈80 % idle |

Boundary sizes (0 B to 3 MB around every packet, 64 KB and 1 MiB edge) on both storages, 100 random sizes, `tools/usb/mtp-file-ops.c` 26/26 (switch on and default build), 1.5 GB soak, 300 MB over SSH, an upload aborted by the computer recovers like before, the off switch moves no byte by DMA. Dolphin copies confirmed by the owner. The first test build (sequence 6350) cut one upload after 9.6 MB (a single RXCOUNT sample mid-unload); fixed before 6351.

## Known gaps

Not yet run with this release: the cable pulled during a copy, sleep and wake with the faster path on, Windows Explorer. If copying to the player ever misbehaves, the developer switch above restores the Beta 7.10 behaviour.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
