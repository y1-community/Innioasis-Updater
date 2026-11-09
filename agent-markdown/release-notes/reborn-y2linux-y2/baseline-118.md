---
title: "Y2Linux 1.0 Beta 8.19 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.19: audiobooks, sharper covers and Customize. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Upda"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-118.html"
---

# Y2Linux 1.0 Beta 8.19 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.19

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-118Y22026-10-21[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.19-first-install.zip[Y2Linux-1.0.0-beta.8.19-first-install.zip 69 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-118/Y2Linux-1.0.0-beta.8.19-first-install.zip)[macOSportable · 183 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-118/Y2Linux-1.0.0-beta.8.19-first-install-macos.zip)[Windowsportable · 265 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-118/Y2Linux-1.0.0-beta.8.19-first-install-windows.zip)[Linuxportable · 438 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-118/Y2Linux-1.0.0-beta.8.19-first-install-linux.zip)

Y2Linux 1.0 Beta 8.19: audiobooks, sharper covers and Customize. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new
  - Audiobooks. Put books in a folder named `Audiobooks` (or `Hörbücher`), use `.m4b` files, or tag them with the genre Audiobook, and Home → Audiobooks appears. Books you are listening to come first, with Chapter 3 of 12 · 45 %; a book's page shows its chapters and how long it still runs. Books never show up among your songs, albums or artists, and they are not scrobbled.
    - Chapters: the chapter marks inside M4B and MP3 files, otherwise one file per chapter. Next and Previous move by chapter; holding them winds through the book in big steps.
    - Your place is kept for every book, also across restarts and updates and after renaming a folder; when you continue, the book goes back a few seconds (more after a long pause). A finished book starts over.
    - Speed: 0.75× to 2× per book, without changing the voice's pitch (hold Select on Now Playing → Speed).
    - Very long single-file books play (they used to stay silent beyond about 9 hours), and M4B files that carry their cover as a video track are no longer refused.
    - Guide: [Audiobooks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FAUDIOBOOKS.md).

  - Sleep timer, for music and books: hold Select on Now Playing → Sleep Timer → 15, 30, 45 or 60 minutes (it fades out) or the end of the chapter or song.
  - Sharper covers. Covers are shown at the size they are drawn, scaled with a better filter, and small covers in lists are made from the full picture. Wide or tall covers are cropped to their centre instead of stretched. The cover cache holds 3 000 albums (it is rebuilt once after the update). For your own files: square covers of 300–600 px look best.
  - Settings → Customize (new):
    - Wrap Around: menus continue at the other end (Menus, the default), also long lists (Everywhere), or not at all (Off). A fast spin through a long list stops at its end first.
    - When Screen Off: what the wheel and its buttons do in the dark: Locked (safe in a pocket), Buttons (Play/Pause, Previous/Next; as before), or Wheel + Buttons (also the wheel as volume and the centre as Play/Pause). Power, the volume keys and headphone buttons always work.
    - Home Menu and Album View moved here from Display.

  - Bluetooth headphones while paused: the player stays awake for 15 minutes, so your headphones' own play button can continue.

Everything from Beta 8.17 is included (8.18 was a test build only).

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.19-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md) · Storage: [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FSTORAGE.md) · [Audiobooks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FAUDIOBOOKS.md) · Headphone settings: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FHEADPHONE-OUTPUT.md) · [Error reports](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FERROR-REPORTS.md)

## Known issues (beta)
  - Some car radios don't show the song and artist yet; we are looking into it.
  - In a very long single-file book, jumping to another chapter takes 2–3 seconds.
  - The highest volume is still lower than stock's, even at High; demanding headphones may want more.
  - The restart fix of Beta 8.4 is not yet confirmed over many restarts. If the screen ever stays dark, hold Power for 10 s and start again.
  - Battery life in sleep is not yet stock-like (about 8 mA vs stock 1.3 mA; some players draw more, [#42](https://github.com/SchulzCode/Y2Linux/issues/42)).
  - GC9503V players keep the old screen-off behaviour until a GC9503V owner has confirmed the new sequence ([#45](https://github.com/SchulzCode/Y2Linux/issues/45)).
  - The charging fix (#47) is not yet confirmed on an affected player; if yours still doesn't charge, please send a report.
  - The player cannot detect wired headphones yet; the jack plays whenever no Bluetooth headphones are connected.
  - BBC radio stations stream only in HLS, which the player does not play yet (planned for a later beta).
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.8.19-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 8302).
  - `Y2Linux-1.0.0-beta.8.19-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-118`. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 8.19 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.19.md).

## Sources unchanged since an earlier release
  - `Y2Linux-sources-third-party-b24c80bffef1.tar` (attached to `baseline-114`), SHA-256 `b24c80bffef118ebe6f08843ae51e8516dd9be04decc1e76e5063c4eb7a2b2ca`
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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-118&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
