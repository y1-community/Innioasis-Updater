---
title: "Y2Linux 1.0 Beta 1 - Innioasis Updater"
description: "The first public beta of Y2Linux and the Reborn music player for the Innioasis Y2. Linux 6.18 and a native music player replace the stock Android system; the bootloaders, calibrati"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-50.html"
---

# Y2Linux 1.0 Beta 1 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 1

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-50Y22026-10-14[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.1-first-install.zip[Y2Linux-1.0.0-beta.1-first-install.zip 54 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-50/Y2Linux-1.0.0-beta.1-first-install.zip)[macOSportable · 169 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-50/Y2Linux-1.0.0-beta.1-first-install-macos.zip)[Windowsportable · 251 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-50/Y2Linux-1.0.0-beta.1-first-install-windows.zip)[Linuxportable · 424 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-50/Y2Linux-1.0.0-beta.1-first-install-linux.zip)

The first public beta of Y2Linux and the Reborn music player for the Innioasis Y2. Linux 6.18 and a native music player replace the stock Android system; the bootloaders, calibration and factory partitions stay untouched. Ready-made images, one SP Flash Tool pass, then updates over Wi-Fi.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.1-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package onto the Firmware drive. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work and why RECOVERY is flashed once: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md)

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Download Update → Restart and Install.

## Highlights
  - Reborn: Cover Flow and album grid, Genres, 15 themes, A–Z sorting that ignores case, accents and "The", click-wheel UI on the GPU.
  - Wired playback; Bluetooth with automatic codec choice: SBC, AAC (fdk-aac-free) and LDAC.
  - Over-the-air updates: daily check, download with progress and speed, one-minute install with backup, readback and automatic rollback; the player restarts by itself.
  - Deep sleep with stock-parity power settings; stock battery percentage and top-off charging; MTP for internal storage and SD card.
  - No proprietary MediaTek firmware in any image: each player uses its owner's copy, kept across updates.

## Known issues (beta)
  - Battery life in sleep is not yet stock-like (about 8.3 mA vs stock 1.3 mA).
  - Rarely a slow display start after a restart (the picture starts anyway since 47); if the panel stays dark, hold Power for 10 s.
  - USB after a wake from deep sleep not yet confirmed over many wakes; Bluetooth headphones not always reconnected after a wake; AAC with AirPods not yet confirmed.
  - Tested on one hardware revision and one player. A kernel that hangs before its rescue system can only be fixed with SP Flash Tool.

## Files
  - `Y2Linux-1.0.0-beta.1-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 5000).
  - `…-sources-buildroot-legal-info.tar`, `…-sources-linux-6.18.56.tar.xz`: corresponding sources and licences. Our own code: Y2Linux and Y2Reborn at tag `baseline-50`.
  - `SHA256SUMS` for all of the above.

Thanks to @samanz for the headphone-level work and the Reborn improvements in this beta.

Beta software: use at your own risk. Not affiliated with Innioasis or MediaTek. Details: [Beta 1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-1.md).

## Also useful
  - [Install guideStep-by-step install for Reborn (Y2Linux)](../../guides/reborn-y2linux-y2.html)
  - [Y2Linux 1.0 Beta 9.3.19baseline-228 · 2026-11-08](../../release-notes/reborn-y2linux-y2/baseline-228.html)
  - [Y2Linux 1.0 Beta 9.3.18baseline-227 · 2026-11-08](../../release-notes/reborn-y2linux-y2/baseline-227.html)
  - [Y2Linux 1.0 Beta 9.3.17baseline-225 · 2026-11-08](../../release-notes/reborn-y2linux-y2/baseline-225.html)
  - [Y2Linux 1.0 Beta 9.3.16baseline-224 · 2026-11-06](../../release-notes/reborn-y2linux-y2/baseline-224.html)
  - [Y2Linux 1.0 Beta 9.3.15baseline-223 · 2026-11-05](../../release-notes/reborn-y2linux-y2/baseline-223.html)
  - [Y2Linux 1.0 Beta 9.3.13baseline-221 · 2026-11-05](../../release-notes/reborn-y2linux-y2/baseline-221.html)
  - [Y2Linux 1.0 Beta 9.3.12baseline-220 · 2026-11-04](../../release-notes/reborn-y2linux-y2/baseline-220.html)
  - [Y2Linux 1.0 Beta 9.3.7baseline-215 · 2026-11-03](../../release-notes/reborn-y2linux-y2/baseline-215.html)

Notes as published by the Reborn (Y2Linux) project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-50&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
