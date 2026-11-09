---
title: "Y2Linux 1.0 Beta 9.3.7 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.3.7: Bluetooth rebuilt for reliability. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → System → Software"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-215.html"
---

# Y2Linux 1.0 Beta 9.3.7 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.3.7

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-215Y22026-11-03[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.9.3.7-first-install.zip[Y2Linux-1.0.0-beta.9.3.7-first-install.zip 64 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-215/Y2Linux-1.0.0-beta.9.3.7-first-install.zip)[macOSportable · 178 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-215/Y2Linux-1.0.0-beta.9.3.7-first-install-macos.zip)[Windowsportable · 261 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-215/Y2Linux-1.0.0-beta.9.3.7-first-install-windows.zip)[Linuxportable · 434 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-215/Y2Linux-1.0.0-beta.9.3.7-first-install-linux.zip)

Y2Linux 1.0 Beta 9.3.7: Bluetooth rebuilt for reliability. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → System → Software Update → Update Now (on Beta 9.2.8 and older: Settings → About & Updates → Check for Updates → Update Now).

## What changed

Bluetooth used to be handled by five separate pieces that coordinated through lock files; when two acted at once, headphones stayed half connected or reconnects stalled. One radio program now owns Bluetooth and the radio it shares with Wi-Fi. The player says what it wants, and the radio program gets there and repairs itself. Every codec, rate and quality setting from 9.2.16 is kept.
  - Headphones come back after sleep, also when they reconnect by themselves: AirPods Pro were ready 2.5–5 s after a wake (before: often 15–20 s).
  - Bluetooth repairs itself (cancel a stuck step, restart the radio, BlueALSA, BlueZ). If everything fails it says so: switching Bluetooth off and on in Settings now restarts all of Bluetooth.
  - Connect Automatically per device (Y2Reborn #78): Settings → Bluetooth → a paired device.
  - Codec and quality changes apply without restarting the player (the headphones are back in about 7–9 s).
  - Your library is no longer emptied when a Bluetooth output fails (Y2Reborn #92).
  - Headphones that are switched off are no longer paged forever; pausing keeps the connection instead of stopping the stream; Wi-Fi uses its power saving while Bluetooth plays; after sleep Wi-Fi waits for your headphones; each pair of headphones starts at the rate it managed last time.

Before release: the platform's full check, Reborn's workspace tests, the 552 tests of the release images, and a fake Bluetooth stack with six failure scenarios. On the developer's player with AirPods Pro: 19 sleep/wake cycles without a failed connection. Only AirPods Pro were tried, and there is no overnight run on this exact build yet: if your headphones behave worse than in 9.2.16, please send an error report.

What changed and why, in plain words: [Beta 9.3.7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.7.md). Versions 9.3 to 9.3.6 were unpublished test builds; everything from Beta 9.2.16 is included ([Beta 9.2.16 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.16.md)).

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.9.3.7-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md) · Storage: [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FSTORAGE.md) · [Audiobooks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FAUDIOBOOKS.md) · Headphone settings: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FHEADPHONE-OUTPUT.md) · [Error reports](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FERROR-REPORTS.md) · Skins: [skin guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fskins.md)

## Known issues (beta)
  - Bluetooth after a long pause: with AirPods Pro, a pause longer than about 20 seconds drops the connection once; they reconnect within seconds, but pressing play during those 20 seconds can stay silent until they are back. Being investigated.
  - Everything listed for Beta 9.0 still applies. If anything behaves differently from 9.2.16, send an error report (Settings → System → Error Reports); Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to the version you had, with your data kept.
  - Battery life in sleep: about 2 mA overnight on the developer's player (estimated from the battery voltage); stock is about 1.3 mA.
  - Some players turned off by themselves during playback; the cause is not found yet. If yours does, start it again and send a report.
  - The speaker uses the same volume as the headphones; its loudest step is the stock speaker's. Start low the first time.
  - How loud the wheel click should be is a first guess; tell us if it is too loud or too soft.
  - BBC radio stations stream only in HLS, which the player does not play yet. FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.9.3.7-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 14000).
  - `Y2Linux-1.0.0-beta.9.3.7-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-215`. The speaker amplifier driver is Chris Hendrickson's GPL-2.0 AW87559 driver. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Awinic, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 9.3.7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.7.md).

## Sources unchanged since an earlier release
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

Notes as published by the Reborn (Y2Linux) project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-215&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
