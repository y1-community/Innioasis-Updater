---
title: "Y2Linux 1.0 Beta 8.2 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.2: updates install in about 15 seconds. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates →"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-88.html"
---

# Y2Linux 1.0 Beta 8.2 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.2

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-88Y22026-10-18[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.2-first-install.zip[Y2Linux-1.0.0-beta.8.2-first-install.zip 55 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-88/Y2Linux-1.0.0-beta.8.2-first-install.zip)[macOSportable · 169 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-88/Y2Linux-1.0.0-beta.8.2-first-install-macos.zip)[Windowsportable · 252 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-88/Y2Linux-1.0.0-beta.8.2-first-install-windows.zip)[Linuxportable · 425 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-88/Y2Linux-1.0.0-beta.8.2-first-install-linux.zip)

Y2Linux 1.0 Beta 8.2: updates install in about 15 seconds. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## Faster updates
  - The installer now uses all four processor cores to unpack the new system, take the backup and check what it wrote. The download stays the same size (about 57 MB).
  - After an update has confirmed itself, its system part stays on the player. The next update uses it as the way back, instead of compressing the running system again first.
  - Measured on a real player: the installer took 53.5 s in Beta 8.1. The update to this release takes about 24 s, and later updates about 15 s. From Update Now to the running new version takes about a minute.
  - If the kept copy is not the running system (for example after flashing with a computer) or anything about it does not check out, the installer backs up the running system as before. The automatic way back after a failed update works as before.
  - The kept copy needs about 42 MB on the system data partition. If space runs short, it is the last thing an update removes.

Everything from Beta 8.1 is included.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.2-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md)

## Known issues (beta)
  - Battery life in sleep is not yet stock-like (about 8 mA vs stock 1.3 mA; some players draw more, [#42](https://github.com/SchulzCode/Y2Linux/issues/42)); the effect of Beta 8.1's panel power-down is being measured.
  - GC9503V players keep the old screen-off behaviour until a GC9503V owner has confirmed the new sequence ([#45](https://github.com/SchulzCode/Y2Linux/issues/45)).
  - The player cannot detect wired headphones yet; the jack plays whenever no Bluetooth headphones are connected.
  - The fast copy path has not yet been tested with the cable pulled mid-copy, across sleep, or with Windows Explorer.
  - Songs with several artists ("A;B") count as one artist; there is no Album Artist view yet.
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.8.2-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 6501). `rootfs.ext4.gz` is an ordinary gzip file made of independent 1 MiB pieces.
  - `Y2Linux-1.0.0-beta.8.2-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-88`.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek or Last.fm. Details: [Beta 8.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.2.md).

## Sources unchanged since an earlier release
  - `Y2Linux-sources-third-party-dce38ffdd9e0.tar` (attached to `baseline-52`), SHA-256 `dce38ffdd9e0a2b5adf687e95c2a67c22ca355e10c430f879630fbf0d5ea7c1a`
  - `Y2Linux-sources-toolchain-f7cda4c7d213.tar` (attached to `baseline-75`), SHA-256 `f7cda4c7d2134bed15dacc7afd7e1687621a57412d60e49c725efc3880bf1bc6`
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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-88&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
