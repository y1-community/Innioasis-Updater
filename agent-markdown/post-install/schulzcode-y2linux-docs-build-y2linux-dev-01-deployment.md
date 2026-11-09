---
title: "Y2LINUX-DEV-01 — owner manual deployment - Innioasis Updater"
description: "Y2LINUX-DEV-01 — owner manual deployment <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-dev-01-deployment.html"
---

# Y2LINUX-DEV-01 — owner manual deployment - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-DEV-01 — owner manual deployment

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-DEV-01 — owner manual deployment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Candidate files: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-dev-01/`. Linux 6.18, Buildroot 2025.02.17, rescue BOOTIMG and 512 MiB ext4 root filesystem. This candidate has passed offline validation; it has not been physically booted. Display visibility, wheel recovery, large RAM, SD root, ECM and SSH remain unproved.

## 1. Verify the files`cd /home/luca/Dokumente/Code/Y2Linux/out/y2linux-dev-01 sha256sum -c SHA256SUMS`

The rootfs contains only the explicitly supplied host public key in root's `authorized_keys`. Fingerprint: `SHA256:IS9HhrmQKRtlEEbrcJjZa0XQHVwnRXRUzQQ61/7XAb8`. Password authentication is disabled. Device host keys are generated on first Dropbear start and persist on the SD. No host private key was accessed or packaged.

## 2. Identify the removable card before any write

On the host, run this before insertion and again after insertion:`lsblk -e 7 -p -o NAME,SIZE,MODEL,TRAN,RM,TYPE,FSTYPE,LABEL,UUID,MOUNTPOINTS ls -l /dev/disk/by-id/`

Match the newly appeared reader/card by size, model and physical insertion. Check its parent disk is the removable card, not the system disk or Y2 internal storage. Some USB readers report RM=0; resolve any ambiguity before writing. Use an existing confirmed partition on that card, at least 512 MiB. This image is an ext4 filesystem image, not a partition-table/disk image. If the card needs partitioning, provide this listing first so commands can name the verified card. Do not guess `/dev/sdX` or `/dev/mmcblkX`.

The following commands are for the owner only. Replace the placeholder with the verified persistent partition path, including its real `-partN` suffix:`ROOTPART=/dev/disk/by-id/REPLACE_WITH_VERIFIED_REMOVABLE_PARTITION case "$ROOTPART" in *REPLACE*) echo 'Set the verified removable partition first'; exit 1;; esac test -b "$ROOTPART" || exit 1 lsblk -s -p -o NAME,SIZE,MODEL,TRAN,RM,TYPE,FSTYPE,LABEL,UUID,MOUNTPOINTS "$ROOTPART" sudo blockdev --getsize64 "$ROOTPART"`

Confirm that output yourself. Unmount that partition and any other mounted partitions of this same card using their verified paths. The next operation replaces all contents of ROOTPART; it must be at least 536870912 bytes:`sudo umount "$ROOTPART" # skip if already unmounted sudo dd if=rootfs.ext4 of="$ROOTPART" bs=4M conv=fsync status=progress sudo e2fsck -f -n "$ROOTPART" sudo blkid -p "$ROOTPART" sync`

Expected: ext4, `LABEL="Y2ROOT"`, `UUID="79324c69-6e75-4801-8000-000000000001"`. Initially the filesystem remains 512 MiB even on a larger partition. Expansion is optional after first boot. Eject the reader cleanly, then put the card into the Y2. Do not unpack rootfs.tar onto the host root; it is a companion archive, not the SD-writing operation.

## 3. Flash BOOTIMG only

Use the already established SP Flash Tool / existing correct Y2 scatter workflow. Choose Download Only, select BOOTIMG only, and point it at this directory's `BOOTIMG.img`. The assistant does not run the flasher or write any device. Never select Format/Firmware Upgrade or write PRELOADER, LK, partition tables, NVRAM/calibration, other Android partitions or internal eMMC filesystems.

Keep the known recovery/stock BOOTIMG available through the existing procedure. This does not require a new ROM/donor/recovery audit.

## 4. Boot, observe and connect

Boot USB unplugged, retaining the inherited USB power-state guard; attach USB after ten seconds or later. There is no former 295-second software shutdown or one-reconnect limit. A real USB power/ownership fault still stops that driver.

Start capture on the host before attaching:`cd /home/luca/Dokumente/Code/Y2Linux python3 tools/observation/usb_log_capture.py --build Y2LINUX-DEV-01 \ --seconds 240 --output out/y2linux-dev-01/capture-01`

The verified composite USB identity is `0525:a4aa`; ACM is its serial function. The root transition can emit a second DEV-01 header and replay the kernel ring. Retain the raw stream: replayed sequence numbers are not missing-record evidence. If you disconnect USB, the capture closes cleanly; run it again with a new output directory after reconnect. Linux should stay running throughout.

The screen test is white, red, green and blue columns above a checkerboard, at 480x360. Record whether that pattern or fbcon is actually visible; independently record whether the backlight is lit. DRM/fb0 registration is not display success. Press all navigation, volume and Power buttons and turn the wheel both ways.

Rescue waits 20 seconds, accepts only one ext4 Y2ROOT on removable controller `11240000.mmc`, validates the root and switches to Buildroot init. Missing, ambiguous or unusable roots stay in rescue with ACM and no reboot loop.

Identify the newly appeared ECM interface on the host:`ip -br link lsusb -d 0525:a4aa`

Use the actual newly appeared USB Ethernet interface; replace the placeholder:`Y2IF=REPLACE_WITH_VERIFIED_USB_ETHERNET_INTERFACE case "$Y2IF" in *REPLACE*) echo 'Set the actual Y2 Ethernet interface first'; exit 1;; esac sudo ip address replace 10.42.0.2/24 dev "$Y2IF" sudo ip link set "$Y2IF" up ping -c 3 10.42.0.1 ssh root@10.42.0.1`

The matching key must be available to your host SSH agent. If selecting an agent-held identity explicitly, OpenSSH accepts `-o IdentityFile=/home/luca/.ssh/y2linux_ed25519.pub` (public path only). No password login or default route is configured. If a host network already uses 10.42.0.0/24, resolve the route conflict before connecting.

Once you tell the assistant deployment is complete, it can collect ACM and SSH in the same session. A manual equivalent is:`ssh root@10.42.0.1 /usr/sbin/y2-collect > out/y2linux-dev-01/runtime-01.txt ssh root@10.42.0.1 /usr/sbin/y2-memory-check > out/y2linux-dev-01/memory-01.txt 2>&1`

This collects dmesg, CPU/memory/interrupts, DRM/framebuffer, clocks, input, I2C, MMC, network and mounts; the second command tests allocator-owned memory once. After one disconnect/reconnect, verify both a fresh ACM capture and SSH again. Record visible output and wheel motion along with those files. Hardware failures remain open and should be fixed together in DEV-02, not closed on probe success.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
