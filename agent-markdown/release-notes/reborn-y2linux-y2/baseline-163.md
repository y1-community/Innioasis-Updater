---
title: "Y2Linux 1.0 Beta 8.42 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.42: sleep, large SD cards, and fixes from your error reports. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Setting"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-163.html"
---

# Y2Linux 1.0 Beta 8.42 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.42

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-163Y22026-10-28[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.42-first-install.zip[Y2Linux-1.0.0-beta.8.42-first-install.zip 69 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-163/Y2Linux-1.0.0-beta.8.42-first-install.zip)[macOSportable · 183 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-163/Y2Linux-1.0.0-beta.8.42-first-install-macos.zip)[Windowsportable · 266 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-163/Y2Linux-1.0.0-beta.8.42-first-install-windows.zip)[Linuxportable · 439 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-163/Y2Linux-1.0.0-beta.8.42-first-install-linux.zip)

Y2Linux 1.0 Beta 8.42: sleep, large SD cards, and fixes from your error reports. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new
  - Power puts the player to sleep without the screen lighting up again. The screen goes dark at once, as on the stock firmware. A second press while it gets ready wakes it straight back to where you were, and a sleep the player has to refuse (for example while charging) keeps the screen dark instead of turning it back on.
  - Wi-Fi and Bluetooth on newer players (#62): some Y2s from 2026 (without FM radio) came with two empty factory partitions, and the radios never started. They now start with the chip's built-in defaults, as on the stock firmware.
  - Large SD cards play at once. A card with tens of thousands of songs (over about 72 000 on a 1 TB card) was kept read-only and offered for a Repair that changed nothing. The card is now checked in the background while your music plays; only a card that really has errors asks for Repair.
  - Faster restarts with a big library: after a restart the player no longer reads every unchanged folder again. If you edit tags on a computer, use Settings → Scan for Music afterwards.
  - Bluetooth headphones after a sleep: pressing Play in the seconds before your headphones reconnect no longer plays on the speaker (or the empty jack). The player waits for them and plays there.
  - Wi-Fi: no more "wrong password" when the password is right, and the player reconnects to your saved network by itself after a sleep or start, without tapping it.
  - Updates (#63): an update that hung on "Installing Update" now restarts and finishes by itself, and the first start after an update no longer falls back to the rescue screen.
  - Restart and Power Off can no longer hang with the screen dark (one player drained a full battery that way); if anything stalls, the player completes the restart or turns off by itself.
  - Battery: the percentage stays right after a restart or update (it could show 13 % instead of 95 %), and the player now sleeps at low battery instead of staying awake and draining faster.
  - Holding Power right after waking shows the power-off ring instead of cutting the power.
  - The screen at start: a screen that stayed dark from power-on (seen once on an ST7701S player) is restarted by itself.
  - Error reports now show more about why a player turned off, so the remaining cases can be found.

Everything from Beta 8.41 (internal speaker, headphone detection, haptic feedback) is included. Thanks for all the reports!

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.42-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
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
  - `Y2Linux-1.0.0-beta.8.42-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 10900).
  - `Y2Linux-1.0.0-beta.8.42-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-163`. The speaker amplifier driver is Chris Hendrickson's GPL-2.0 AW87559 driver. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Awinic, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 8.42 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.42.md).

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-163&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
