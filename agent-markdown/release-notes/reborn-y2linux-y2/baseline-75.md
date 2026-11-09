---
title: "Y2Linux 1.0 Beta 8.0 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.0: fixes from the 1.0 review. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates → Check for"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-75.html"
---

# Y2Linux 1.0 Beta 8.0 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.0

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-75Y22026-10-18[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.0-first-install.zip[Y2Linux-1.0.0-beta.8.0-first-install.zip 55 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-75/Y2Linux-1.0.0-beta.8.0-first-install.zip)[macOSportable · 169 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-75/Y2Linux-1.0.0-beta.8.0-first-install-macos.zip)[Windowsportable · 252 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-75/Y2Linux-1.0.0-beta.8.0-first-install-windows.zip)[Linuxportable · 425 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-75/Y2Linux-1.0.0-beta.8.0-first-install-linux.zip)

Y2Linux 1.0 Beta 8.0: fixes from the 1.0 review. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## Fixed
  - Updates no longer undo themselves when one song is broken. A single file the player could not read (a truncated download, a mislabelled `.mp3`) made every library scan count as interrupted; the update's health check then restored the previous version about three minutes after installing. Such files are now simply counted (Settings → Library: N can't be read) and the update check asks Reborn whether it is healthy.
  - Songs deleted from a computer leave the library again, even when a broken file sits on the same storage.
  - Large or slow SD cards mount. A card whose check took more than about seven seconds was never mounted, and the checks piled up in the background. The check now runs on its own, as long as it needs.
  - Settings survive going back a version. If an update is rolled back, the older Reborn keeps every setting it understands instead of starting from defaults (the refused file is kept).
  - A stuck installer turns off after ten minutes on battery instead of keeping the screen on until the battery is empty.
  - USB copies: a rare fallback in the fast receive path now stops the DMA engine before the processor takes over, so it can never lose part of a packet unnoticed.
  - Internal Storage no longer repeats a refused background write at every start.

Installed over the air on a real player and checked there with a deliberately broken song on Internal Storage: the update confirmed itself and the library kept working.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.0-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

The zip now carries the current install guide as `install.md`. Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md)

## Known issues (beta)
  - Battery life in sleep is not yet stock-like (about 8 mA vs stock 1.3 mA; some players draw more, [#42](https://github.com/SchulzCode/Y2Linux/issues/42)).
  - The player cannot detect wired headphones yet; the jack plays whenever no Bluetooth headphones are connected.
  - The fast copy path has not yet been tested with the cable pulled mid-copy, across sleep, or with Windows Explorer (developers: `echo 0 > /sys/devices/platform/11200000.usb/rx_dma` switches back).
  - Songs with several artists ("A;B") count as one artist; there is no Album Artist view yet ([#40](https://github.com/SchulzCode/Y2Linux/issues/40), [#41](https://github.com/SchulzCode/Y2Linux/issues/41)).
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.8.0-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 6400).
  - `Y2Linux-1.0.0-beta.8.0-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages), `Y2Linux-sources-toolchain-…tar` (new: glibc and GCC runtime sources of the Bootlin toolchain), and the third-party sources and Linux source linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-75`.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek or Last.fm. Details: [Beta 8.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.0.md).

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-75&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
