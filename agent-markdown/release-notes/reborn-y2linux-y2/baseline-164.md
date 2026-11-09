---
title: "Y2Linux 1.0 Beta 8.43 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.43: your requests for Reborn. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates → Check for"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-164.html"
---

# Y2Linux 1.0 Beta 8.43 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.43

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-164Y22026-10-28[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.43-first-install.zip[Y2Linux-1.0.0-beta.8.43-first-install.zip 69 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-164/Y2Linux-1.0.0-beta.8.43-first-install.zip)[macOSportable · 183 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-164/Y2Linux-1.0.0-beta.8.43-first-install-macos.zip)[Windowsportable · 266 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-164/Y2Linux-1.0.0-beta.8.43-first-install-windows.zip)[Linuxportable · 439 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-164/Y2Linux-1.0.0-beta.8.43-first-install-linux.zip)

Y2Linux 1.0 Beta 8.43: your requests for Reborn. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new
  - Choose what's on Home (#52, #55): Settings → Customize → Home Menu now has a switch for Music, Playlists, Radio and Search too (Now Playing and Settings always stay). A hidden Playlists or Search is still at the end of Music.
  - Go back to where the music came from (#60, #25): Now Playing's menu (hold the center button) has Go to Playlist, Go to Folder, Go to Search, Go to Genre or Go to Songs, depending on where you started the music, and opens it with the playing song selected.
  - Leaving Search is easy again (#51): Cancel always leaves Search, also with text in the box, and holding Back while typing does too. Both go back to where you opened Search.
  - No more duplicate albums (#45, #46): an album where only some songs have the Album Artist tag is listed once.
  - Albums by artist (#56): Settings → Customize → Album Order: Title or Artist (then title). Cover Flow follows it.
  - Faster scrolling in long lists (#30): spin the wheel fast in Songs, Artists, Albums or Folders and it jumps letter by letter; the letter stays for a moment after you stop, so you can turn back without losing it.
  - Cover Flow in light skins (#57): the shelf under the covers now fades into the skin's background instead of black.
  - Headphones unplugged (#62): the player now says "Headphones unplugged. Playback paused."
  - More haptic feedback (#28): a tick when a computer connects and while you hold Previous/Next to seek (with Haptics on in Customize).

Everything from Beta 8.42 (sleep, large SD cards, report fixes, Wi-Fi and Bluetooth on players with empty factory partitions) is included. Thanks for all the requests!

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.43-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md) · Storage: [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FSTORAGE.md) · [Audiobooks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FAUDIOBOOKS.md) · Headphone settings: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FHEADPHONE-OUTPUT.md) · [Error reports](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FERROR-REPORTS.md)

## Known issues (beta)
  - Wi-Fi and Bluetooth on players with empty factory partitions (#62) use the chip's default calibration; please send a report if the range is poor.
  - Some players turned off by themselves during playback; the cause is not found yet. If yours does, start it again and send a report.
  - While a large SD card is being checked (up to a few minutes), you can't copy music to it over USB yet.
  - The speaker uses the same volume as the headphones; its loudest step is the stock speaker's. Start low the first time.
  - Going back to a version older than 8.33 starts with an empty queue (your settings are kept).
  - Some car radios don't show the song and artist yet; we are looking into it.
  - In a very long single-file book, jumping to another chapter takes 2–3 seconds.
  - With very large libraries (100 000+ songs) a list can still take up to about a second the first time right after the player starts, and the first scan of such a card takes several minutes.
  - Battery life in sleep: about 2 mA overnight on the developer's player (estimated from the battery voltage); stock is about 1.3 mA.
  - BBC radio stations stream only in HLS, which the player does not play yet (planned for a later beta).
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.8.43-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 11000).
  - `Y2Linux-1.0.0-beta.8.43-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-164`. The speaker amplifier driver is Chris Hendrickson's GPL-2.0 AW87559 driver. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Awinic, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 8.43 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.43.md).

## Sources unchanged since an earlier release
  - `Y2Linux-sources-third-party-b24c80bffef1.tar` (attached to `baseline-120`), SHA-256 `b24c80bffef118ebe6f08843ae51e8516dd9be04decc1e76e5063c4eb7a2b2ca`
  - `Y2Linux-sources-toolchain-f7cda4c7d213.tar` (attached to `baseline-120`), SHA-256 `f7cda4c7d2134bed15dacc7afd7e1687621a57412d60e49c725efc3880bf1bc6`
  - `linux-6.18.56.tar.xz` (attached to `baseline-120`), SHA-256 `4633bbda2ab95eaf2a7af4041236451d6759c72e6946265531af4b3aacefbf89`

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-164&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
