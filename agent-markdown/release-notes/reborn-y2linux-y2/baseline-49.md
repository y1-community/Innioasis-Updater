---
title: "Y2Linux Baseline 49 - Innioasis Updater"
description: "Y2Linux Baseline 49 — ready-made images for a first install, and the update for players that already run Y2Linux. Already running Y2Linux 46 or later Settings → About & Updates → C"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-49.html"
---

# Y2Linux Baseline 49 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux Baseline 49

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-49Y22026-10-14[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-49-first-install.zip[Y2Linux-49-first-install.zip 54 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-49/Y2Linux-49-first-install.zip)[macOSportable · 169 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-49/Y2Linux-49-first-install-macos.zip)[Windowsportable · 251 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-49/Y2Linux-49-first-install-windows.zip)[Linuxportable · 424 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-49/Y2Linux-49-first-install-linux.zip)

Y2Linux Baseline 49 — ready-made images for a first install, and the update for players that already run Y2Linux.

## Already running Y2Linux (46 or later)

Settings → About & Updates → Check for Updates → Download Update → Restart and Install. Your Wi-Fi and Bluetooth firmware is kept automatically.

## New install (from stock)

You need SP Flash Tool v5.2032, a USB cable, this release's `Y2Linux-49-first-install.zip` and the Innioasis Y2 firmware package v3.2.0 from Innioasis.
  - Unpack the Y2Linux zip and the Innioasis package.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download, connect the switched-off Y2; wait for the green tick.
  - Unplug, press Power: Y2Linux and Reborn start.
  - Connect the Y2 to the computer again and copy `system.img` from the Innioasis package to the Firmware drive. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · why RECOVERY is flashed: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md)

## What's new
  - No proprietary MediaTek firmware in any image. Each player uses its owner's copy (kept across updates). The system images of releases 46–48 were removed because they contained it.
  - One-time flash package with the Y2 recovery image; afterwards everything updates over Wi-Fi.
  - Bluetooth codecs: SBC, AAC (fdk-aac-free, AAC-LC) and LDAC.
  - Headphone load measurement and two CS43131 driver fixes (thanks @samanz, #38); covers that load reliably, A–Z sorting that ignores case, accents and "The", genre titles on the album grid (thanks @samanz, Y2Reborn #6–#8).

## Files
  - `Y2Linux-49-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 4900).
  - `Y2Linux-49-sources-*`: corresponding sources (Buildroot legal-info with package sources, patches and licences; the Linux 6.18.56 archive). Our own code is this repository and Y2Reborn at tag `baseline-49`.
  - `SHA256SUMS` for all of the above.

Kernel `6.18.56-y2linux-platform-v1-power-final-49`. Developer preview; use at your own risk. Not affiliated with Innioasis or MediaTek.

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-49&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
