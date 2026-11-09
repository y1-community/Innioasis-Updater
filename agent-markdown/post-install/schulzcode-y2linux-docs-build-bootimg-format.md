---
title: "Legacy BOOTIMG package contract - Innioasis Updater"
description: "Legacy BOOTIMG package contract <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-bootimg-format.html"
---

# Legacy BOOTIMG package contract - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Legacy BOOTIMG package contract

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Legacy BOOTIMG package contract > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Y2B-230 packages only the validated payload. Offline inspection of the owner-proven FM `boot.img` confirmed `ANDROID!`, 2048-byte page size, header fields `kernel_addr=0x10008000`, `ramdisk_addr=0x11000000`, `second_addr=0x10f00000`, `tags_addr=0x10000100`, zero second/DT sizes, empty header cmdline, and SHA-1 over each wrapped kernel/ramdisk section followed by its little-endian size, then zero second size. These are legacy header fields; FM LK's actual load/entry addresses remain D08's `0x80008000` and `0x84000000`.

Each MTK wrapper is 512 bytes: little-endian magic `0x58881688`, inner byte length, 32-byte NUL-padded KERNEL or ROOTFS name, then 472 bytes of `0xff`. New header name is deterministic `Y2Linux-M1`; trailing ID bytes and unused header bytes are zero. Neither the old Android SHA-1 ID nor SHA-256 manifest constitutes an image signature or proves installed LK acceptance.

Output is Android header page + page-padded wrapped kernel + page-padded wrapped initramfs + two explicit zero pages. This covers the entire additional LK read traced in Y2E-125/D08 instead of relying on stale partition tail contents. The resulting file must equal `2048 + align_up(K,2048) + align_up(W,2048) + 4096` and be no larger than the 16 MiB BOOTIMG partition. All page padding is zero. The parser checks every field, payload byte, SHA-1 ID, wrapper and padding extent independently before output is written. No flasher or partition-access code exists in this build path.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
