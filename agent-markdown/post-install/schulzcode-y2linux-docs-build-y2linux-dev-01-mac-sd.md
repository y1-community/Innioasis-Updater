---
title: "DEV-01 SD preparation from the owner's Mac - Innioasis Updater"
description: "DEV-01 SD preparation from the owner's Mac <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-dev-01-mac-sd.html"
---

# DEV-01 SD preparation from the owner's Mac - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# DEV-01 SD preparation from the owner's Mac

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# DEV-01 SD preparation from the owner's Mac > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The owner has a USB-C card reader usable on the Mac, not the Linux host. The already flashed BOOTIMG can remain while the prepared ext4 filesystem is transferred and installed. No storage target has yet been identified on the Mac; no disk write is authorized by a guessed disk number.

The losslessly compressed `out/y2linux-dev-01/rootfs.ext4.gz` is 8,337,371 bytes. Its SHA-256 is `67399d568fa50c459aeac033f9b22f828f228f156ddccdfd956047845a502a48`. Decompression was checked against the existing ext4 SHA-256 `ecf7f9a448e708f9a1c023443ab4d4a9a22d9ab4e8e812b3319b58770dbd2ed3`. This is a transport copy of DEV-01, not a new rootfs build or kernel candidate. The original candidate SHA256SUMS remains unchanged.

A temporary host HTTP server serves only the gzip and checksum files from `out/y2linux-dev-01/mac-transfer`, bound to `192.168.123.204:8765`. This address is the Linux host's currently observed LAN address. The Mac must be on the same reachable LAN; no public upload or SSH key access is involved. Stop the server after transfer is confirmed; its lifetime is this working session.

On the Mac:`mkdir -p ~/Downloads/Y2Linux-DEV-01 cd ~/Downloads/Y2Linux-DEV-01 curl -fLO http://192.168.123.204:8765/rootfs.ext4.gz curl -fLO http://192.168.123.204:8765/rootfs.ext4.gz.sha256 shasum -a 256 -c rootfs.ext4.gz.sha256`

Expect `rootfs.ext4.gz: OK`. Existing files with those names are replaced by curl; these commands write only the download directory, never the card.

Run the following read-only command before and after connecting the card reader:`diskutil list`

Send the listing and identify any contents that need preserving. Confirm the new external physical device, capacity and partition before constructing its exact unmount/write/verification commands. Do not select a Mac internal disk, APFS container or guessed `/dev/diskN`. The supplied image is an ext4 filesystem, not a partition-table image; the owner will write an identified suitable partition.

[Apple disk identification guide](https://support.apple.com/en-mide/guide/disk-utility/dskutl1005/mac) explains checking internal/external location and capacity in Disk Utility. [Apple command-line reference](https://www.apple.com/server/docs/Command_Line_v10.4_2nd_Ed.pdf) documents the read-only `diskutil list` command. No Mac write command has been executed or disk identifier assumed.

## Owner-identified target — 2026-09-10

The owner supplies a Mac `diskutil list` and explicitly allows erasing the 128 GB SanDisk card. Its current identifier is disk10, external/physical, 127.9 GB, FDisk partition scheme, one DOS_FAT_32 UNTITLED partition disk10s1. Internal disk0 and all APFS/simulator disks are excluded. The existing partition is large enough for the 512 MiB image; no partition-table rewrite is needed. The on-disk MBR type may continue to say FAT32; Linux root discovery uses the actual ext4 superblock label, not that partition-type description.

Owner commands below assume the gzip is directly in Downloads and the card has stayed connected with the same disk identifier. Re-identify after reconnect. The subshell stops on failure without closing the interactive Terminal.`( set -eu cd "$HOME/Downloads" printf '%s\n' '67399d568fa50c459aeac033f9b22f828f228f156ddccdfd956047845a502a48 rootfs.ext4.gz' | shasum -a 256 -c - gzip -dc rootfs.ext4.gz > rootfs.ext4 printf '%s\n' 'ecf7f9a448e708f9a1c023443ab4d4a9a22d9ab4e8e812b3319b58770dbd2ed3 rootfs.ext4' | shasum -a 256 -c - diskutil info /dev/disk10 diskutil unmountDisk /dev/disk10 sudo dd if=rootfs.ext4 of=/dev/rdisk10s1 bs=4m sync sudo dd if=/dev/rdisk10s1 of=rootfs.sd-readback.ext4 bs=4m count=128 printf '%s\n' 'ecf7f9a448e708f9a1c023443ab4d4a9a22d9ab4e8e812b3319b58770dbd2ed3 rootfs.sd-readback.ext4' | shasum -a 256 -c - diskutil eject /dev/disk10 )`

Expect three checksum OK messages, including the SD readback, and successful ejection. No host storage write was executed by the assistant. If macOS prompts about an unreadable filesystem, choose Ignore, not Initialize; ext4 is intended for the Y2. After ejection, power the Y2 off, insert the card, boot USB unplugged, wait about30seconds, then attach USB and collect rootfs/network state. Root starts at512MiB filesystem size; online expansion can follow a successful SD boot. The earlier MMC command timeouts remain a qualification concern, not proof that this prepared root will fail or succeed. Report any command error before retrying.

[Apple's dd source manual](https://github.com/apple-oss-distributions/file_cmds/blob/main/dd/dd.1) defines the block-size/count and source/destination behavior used for the exact 512MiB write and independent readback.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
