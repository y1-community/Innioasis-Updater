---
title: "Y2Linux 1.0 Beta 7.5 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7.5: a status bar you can read, skins in their own place. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → Ab"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-66.html"
---

# Y2Linux 1.0 Beta 7.5 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7.5

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-66Y22026-10-16[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.7.5-first-install.zip[Y2Linux-1.0.0-beta.7.5-first-install.zip 55 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-66/Y2Linux-1.0.0-beta.7.5-first-install.zip)[macOSportable · 169 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-66/Y2Linux-1.0.0-beta.7.5-first-install-macos.zip)[Windowsportable · 252 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-66/Y2Linux-1.0.0-beta.7.5-first-install-windows.zip)[Linuxportable · 425 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-66/Y2Linux-1.0.0-beta.7.5-first-install-linux.zip)

Y2Linux 1.0 Beta 7.5: a status bar you can read, skins in their own place. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## Changed
  - A larger status bar. The screen's name now sits beside the back arrow in normal capitals ("About & Updates" instead of tracked small caps), and the clock, battery percentage, Wi-Fi, Bluetooth and USB symbols and the battery are bigger.
  - Home has a header: "Reborn" and the version where other screens show their name.
  - Messages are larger too ("Connected to a computer", new songs, problems).
  - Skins have their own place: Settings → Skin (it was Settings → Display → Theme). Settings still fits on one screen, and Display no longer scrolls.
  - Skins folder: copy skins into a folder named `Skins` on Internal Storage or the SD card. A `Themes` folder you already have keeps working.
  - About & Updates no longer has the Music Library entry that only opened Storage; the song count is now beside Scan for Music in Storage.

Skins keep their own status bars. Everything from Beta 7.4 (messages in the status bar, the cooler Now Playing) and earlier is included.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.7.5-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package onto the Firmware drive. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md)

## Known issues (beta)
  - The new status bar was built and checked on the computer; this is its first release on the player.
  - Now Playing redraws continuously while music plays and the screen is on (for the wave), at the lowest processor speed.
  - The 12- or 24-hour clock follows the time zone; there is no switch yet.
  - FM radio is planned for the next beta.
  - Battery life in sleep is not yet stock-like (about 8 mA vs stock 1.3 mA). The player cannot detect wired headphones yet.

## Files
  - `Y2Linux-1.0.0-beta.7.5-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 6050).
  - `Y2Linux-1.0.0-beta.7.5-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party sources and Linux source linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-66`.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis or MediaTek. Details: [Beta 7.5 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.5.md).

## Sources unchanged since an earlier release
  - `Y2Linux-sources-third-party-dce38ffdd9e0.tar` (attached to `baseline-52`), SHA-256 `dce38ffdd9e0a2b5adf687e95c2a67c22ca355e10c430f879630fbf0d5ea7c1a`
  - `linux-6.18.56.tar.xz` (attached to `baseline-52`), SHA-256 `4633bbda2ab95eaf2a7af4041236451d6759c72e6946265531af4b3aacefbf89`

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-66&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
