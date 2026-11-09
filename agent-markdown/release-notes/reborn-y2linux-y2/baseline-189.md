---
title: "Y2Linux 1.0 Beta 9.1 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.1: tidying up after the rewrite. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates → Check f"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-189.html"
---

# Y2Linux 1.0 Beta 9.1 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.1

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-189Y22026-10-30[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.9.1-first-install.zip[Y2Linux-1.0.0-beta.9.1-first-install.zip 64 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-189/Y2Linux-1.0.0-beta.9.1-first-install.zip)[macOSportable · 178 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-189/Y2Linux-1.0.0-beta.9.1-first-install-macos.zip)[Windowsportable · 260 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-189/Y2Linux-1.0.0-beta.9.1-first-install-windows.zip)[Linuxportable · 433 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-189/Y2Linux-1.0.0-beta.9.1-first-install-linux.zip)

Y2Linux 1.0 Beta 9.1: tidying up after the rewrite. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new

Beta 9.1 looks and works like Beta 9.0. One small visible change: while an update downloads, the Settings list shows how far it is ("Downloading · 40%") instead of only "Downloading…".

The rest is housekeeping that the Rust rewrite in 9.0 made possible:
  - The player and the system now share one description of every message they exchange. Until now each side described the messages separately; if one renamed a field, the player would quietly show "unknown". Now both use the same definitions, so a mismatch stops the build instead of reaching your player. This covers the update page and download progress, the battery level and the shutdown notice, Wi-Fi status, the SD card and Internal Storage checks, the USB connection, error report progress, Internal Storage setup and the Wi-Fi/Bluetooth firmware.
  - The player's code is reorganised into smaller, named parts. The main program file went from 8,268 lines to under 1,000, the screen code from 4,493 to about 1,000, and the three longest functions (the main loop and the two audio threads, up to 2,000 lines each) are now short sequences of named steps. The moves were made by script and checked against the original text, so what the code does is unchanged; the same 748 automated tests pass before and after.
  - Small clean-ups in the system services: shared code where two copies existed, and fewer direct operating-system calls outside the one audited library (82 → 63).

Tested on the developer's player: installed over the air from 9.0 and confirmed; all services and Reborn running, Wi-Fi online, storage and health OK, no warnings in Reborn's log; Reborn's built-in decoder, playback, storage and baseline tests pass on the player; start to music player 37 s (as 9.0). Before release: 549 tests of the release images and the full host suites of both projects.

What changed and why, in plain words: [Beta 9.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.1.md). Everything from Beta 9.0 is included ([Beta 9.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md)).

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.9.1-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md) · Storage: [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FSTORAGE.md) · [Audiobooks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FAUDIOBOOKS.md) · Headphone settings: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FHEADPHONE-OUTPUT.md) · [Error reports](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FERROR-REPORTS.md)

## Known issues (beta)
  - Everything listed for Beta 9.0 still applies. Overnight sleep, a low-battery shutdown, an SD card repair or format and a reset have not been repeated on the developer's player since the rewrite. If anything behaves differently from 9.0, send an error report (Settings → Diagnostics); Settings → Diagnostics → Restore Previous System goes back to the version you had, with your data kept.
  - Battery life in sleep: about 2 mA overnight on the developer's player (estimated from the battery voltage); stock is about 1.3 mA.
  - Wi-Fi and Bluetooth on players with empty factory partitions (#62) use the chip's default calibration; please send a report if the range is poor.
  - Some players turned off by themselves during playback; the cause is not found yet. If yours does, start it again and send a report.
  - The speaker uses the same volume as the headphones; its loudest step is the stock speaker's. Start low the first time.
  - BBC radio stations stream only in HLS, which the player does not play yet. FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.9.1-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 11500).
  - `Y2Linux-1.0.0-beta.9.1-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-189`. The speaker amplifier driver is Chris Hendrickson's GPL-2.0 AW87559 driver. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Awinic, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 9.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.1.md).

## Sources unchanged since an earlier release
  - `Y2Linux-sources-third-party-a6aaa039273c.tar` (attached to `baseline-186`), SHA-256 `a6aaa039273c141a32e9c392305e2c3f75a4b48077ec78576b8f2c2a735551fd`
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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-189&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
