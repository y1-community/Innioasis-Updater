---
title: "Y2Linux 1.0 Beta 8.12 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.12: crash loop, silent audio and sleep fixes. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Upda"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-108.html"
---

# Y2Linux 1.0 Beta 8.12 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.12

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-108Y22026-10-20[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.12-first-install.zip[Y2Linux-1.0.0-beta.8.12-first-install.zip 55 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-108/Y2Linux-1.0.0-beta.8.12-first-install.zip)[macOSportable · 170 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-108/Y2Linux-1.0.0-beta.8.12-first-install-macos.zip)[Windowsportable · 252 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-108/Y2Linux-1.0.0-beta.8.12-first-install-windows.zip)[Linuxportable · 425 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-108/Y2Linux-1.0.0-beta.8.12-first-install-linux.zip)

Y2Linux 1.0 Beta 8.12: crash loop, silent audio and sleep fixes. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

Stuck in a loop with a garbled screen, or updates that undo themselves ([#49](https://github.com/SchulzCode/Y2Linux/issues/49))? Take the SD card out, hold Power for 10 s and turn the player on again, install this update, then put the card back.

## What's new
  - No more crash loop from a playlist on the SD card ([#49](https://github.com/SchulzCode/Y2Linux/issues/49)). A playlist (`.m3u`/`.m3u8`) with a character such as `’`, `º` or `é` at one particular place in a line made Reborn crash a few seconds after every start. The screen was left garbled, and an update couldn't confirm itself, so it was undone. Such playlists now open normally (Windows-1252 files too), and entries that aren't on the player say so.
  - One odd file can no longer stop the player. A crash while reading a single playlist, cover picture or song now skips that file instead of stopping Reborn.
  - A clear screen if Reborn can't start. After five failed starts the player shows Couldn't Start instead of a garbled screen. Inserting or removing the SD card tries again; on battery it switches off after 10 minutes instead of draining.
  - No more silence after changing the equalizer ([#48](https://github.com/SchulzCode/Y2Linux/issues/48)). Each equalizer change restarts the headphone DAC. If its clock crystal was slow to start, the song kept "playing" in silence until the next track. The crystal now gets a second, longer try; if it still fails, the player starts the song again instead of playing nothing.
  - Sleep works again after a refused attempt. If the system refused sleep at the very first step (which could happen right after the player parked an idle processor core), the player then stayed awake for hours on battery. That first step no longer fails, and a refusal like that is retried after two minutes.
  - A dark screen after an update restart is less likely: a start-up race could leave the display unable to show anything until the previous version was restored.
  - More useful error reports. A crash loop sends one report instead of many, triggers that fire together share one report, and the reports finally include the kernel's `/proc` and debug files and the DAC registers, which had been left out by mistake.
  - A `system.img` copied into Firmware after the radio firmware is already installed is now checked and removed.

Everything from Beta 8.11 is included.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.12-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md) · Storage: [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FSTORAGE.md) · Headphone settings: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FHEADPHONE-OUTPUT.md) · [Error reports](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FERROR-REPORTS.md)

## Known issues (beta)
  - The highest volume is still lower than stock's, even at High; demanding headphones may want more.
  - A headphone profile still uses some extra processor time while it plays; its effect on battery life has not been measured yet.
  - The restart fix of Beta 8.4 is not yet confirmed over many restarts. If the screen ever stays dark, hold Power for 10 s and start again.
  - Battery life in sleep is not yet stock-like (about 8 mA vs stock 1.3 mA; some players draw more, [#42](https://github.com/SchulzCode/Y2Linux/issues/42)).
  - GC9503V players keep the old screen-off behaviour until a GC9503V owner has confirmed the new sequence ([#45](https://github.com/SchulzCode/Y2Linux/issues/45)).
  - The charging fix (#47) is not yet confirmed on an affected player; if yours still doesn't charge, please send a report (Send Report Now, or Save Report and attach it).
  - The player cannot detect wired headphones yet; the jack plays whenever no Bluetooth headphones are connected.
  - The fast copy path has not yet been tested with the cable pulled mid-copy, across sleep, or with Windows Explorer.
  - Songs with several artists ("A;B") count as one artist; there is no Album Artist view yet.
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.8.12-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 7601).
  - `Y2Linux-1.0.0-beta.8.12-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-108`. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Last.fm or AutoEq. Details: [Beta 8.12 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.12.md).

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-108&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
