---
title: "Y2Linux 1.0 Beta 8.33 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.33: a new search and a new play queue. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates → C"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-134.html"
---

# Y2Linux 1.0 Beta 8.33 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.33

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-134Y22026-10-24[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.33-first-install.zip[Y2Linux-1.0.0-beta.8.33-first-install.zip 69 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-134/Y2Linux-1.0.0-beta.8.33-first-install.zip)[macOSportable · 183 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-134/Y2Linux-1.0.0-beta.8.33-first-install-macos.zip)[Windowsportable · 265 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-134/Y2Linux-1.0.0-beta.8.33-first-install-windows.zip)[Linuxportable · 438 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-134/Y2Linux-1.0.0-beta.8.33-first-install-linux.zip)

Y2Linux 1.0 Beta 8.33: a new search and a new play queue. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new
  - Search is one page. The first results show above the keys while you type. Press up from the top row of keys, turn the wheel or press Search and the keys fold away: everything found is listed under Artists, Albums, Audiobooks and Songs, with Play All for the songs. Select the search field to type again.
  - Your queue plays first.Add to Queue now puts songs right after the ones you queued, before the rest of the album or list (it used to add them at the very end). Play Next puts them on top.
  - No more hiccups. Adding, removing or moving songs, Shuffle and Repeat no longer restart the song that is playing.
  - Up Next is new. It opens on the song playing; scroll up for the last 50 songs you heard, and below come your queue and the rest of what plays, each under its own heading. Hold Select on a song for Play Next, Move (turn the wheel to carry it anywhere, Select to put it down), Remove, Add to Playlist and more.
  - Select Songs. In Up Next, Songs, an album or a search, hold Select → Select Songs…, tick several songs and act on them together: Play Next, Add to Queue or Remove, Add to Playlist.
  - Whole albums, artists, genres and folders (and a search's songs): hold Select on them for Play, Shuffle, Play Next, Add to Queue and Add to Playlist.
  - Shuffle now shuffles what is playing right away, and turning it off goes back to the album's order. With Repeat All, Next on the last song starts over; Previous on the first song starts it again instead of stopping.
  - Now Playing shows which song comes next.
  - Songs tagged with several artists ("A;B", "A feat. B") are listed under each of them, and an album shows up once.

Thanks to everyone who asked for these (#60, Y2Reborn #26, #31, #32, #38)!

Everything from Beta 8.31 is included.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.33-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md) · Storage: [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FSTORAGE.md) · [Audiobooks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FAUDIOBOOKS.md) · Headphone settings: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FHEADPHONE-OUTPUT.md) · [Error reports](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FERROR-REPORTS.md)

## Known issues (beta)
  - Going back to an older version than 8.33 starts with an empty queue (your settings are kept).
  - The Bluetooth volume takeover was tested without real headphones; if your headphones' volume behaves oddly, please send a report.
  - Some car radios don't show the song and artist yet; we are looking into it.
  - In a very long single-file book, jumping to another chapter takes 2–3 seconds.
  - The highest volume is still lower than stock's, even at High; demanding headphones may want more.
  - The restart fix of Beta 8.4 is not yet confirmed over many restarts. If the screen ever stays dark, hold Power for 10 s and start again.
  - Battery life in sleep is not yet stock-like (about 8 mA vs stock 1.3 mA on the developer's player).
  - The charging fixes (#47, Beta 8.29) are not yet confirmed on an affected player; if yours still doesn't charge, please send a report.
  - The player cannot detect wired headphones yet; the jack plays whenever no Bluetooth headphones are connected.
  - BBC radio stations stream only in HLS, which the player does not play yet (planned for a later beta).
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.8.33-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 9702).
  - `Y2Linux-1.0.0-beta.8.33-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-134`. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 8.33 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.33.md).

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-134&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
