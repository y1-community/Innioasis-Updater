---
title: "Y2Linux 1.0 Beta 7 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7: a calmer, consistent player. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates → Check for"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-61.html"
---

# Y2Linux 1.0 Beta 7 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-61Y22026-10-16[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.7-first-install.zip[Y2Linux-1.0.0-beta.7-first-install.zip 55 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-61/Y2Linux-1.0.0-beta.7-first-install.zip)[macOSportable · 169 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-61/Y2Linux-1.0.0-beta.7-first-install-macos.zip)[Windowsportable · 251 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-61/Y2Linux-1.0.0-beta.7-first-install-windows.zip)[Linuxportable · 425 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-61/Y2Linux-1.0.0-beta.7-first-install-linux.zip)

Y2Linux 1.0 Beta 7: a calmer, consistent player. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Download Update → Restart and Install.

## New: the UI v4 design
  - A calmer Home: Now Playing, Music, Playlists, Radio, Search and Settings. Music holds Artists, Albums, Songs, Genres and Folders with how much each has. Want a list on Home again? Settings → Display → Home Menu.
  - One look everywhere: the same highlight in every list, menu and setting, one kind of button, one kind of message screen, and one accent colour for everything you can switch or select. The album cover's colour now belongs to Now Playing.
  - Less clutter: no instruction lines under lists and keyboards (hold Select on anything for its options), no "NOW PLAYING" label, no codec and bitrate in radio lists, simpler Bluetooth and Wi-Fi lists, colour previews in the theme picker, and a tidier Storage and About page.

## Fixed
  - The CPU's overheat protection switched itself off after the first sleep and stayed off until the next restart. It now comes back after every sleep.
  - Pressing Power to sleep sometimes turned the screen back on after a few seconds, because a routine battery update arrived while the player was getting ready to sleep. The player now simply tries again.

Everything from Beta 6.3 (sleep while paused) and earlier betas is included. Skins keep their own look.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.7-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package onto the Firmware drive. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md)

## Known issues (beta)
  - The new design and both fixes were built and checked on the computer; this is their first release on the player.
  - The 12- or 24-hour clock follows the time zone; there is no switch yet.
  - Jumping to a new place in a song still takes about a second on Bluetooth.
  - FM radio is planned for the next beta.
  - Battery life in sleep is not yet stock-like (about 8 mA vs stock 1.3 mA). The player cannot detect wired headphones yet.

## Files
  - `Y2Linux-1.0.0-beta.7-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 5800).
  - `Y2Linux-1.0.0-beta.7-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party sources and Linux source linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-61`.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis or MediaTek. Details: [Beta 7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.md).

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-61&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
