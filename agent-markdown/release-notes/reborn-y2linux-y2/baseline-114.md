---
title: "Y2Linux 1.0 Beta 8.17 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.17: fixes from your reports. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates → Check for U"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-114.html"
---

# Y2Linux 1.0 Beta 8.17 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.17

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-114Y22026-10-21[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.17-first-install.zip[Y2Linux-1.0.0-beta.8.17-first-install.zip 69 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-114/Y2Linux-1.0.0-beta.8.17-first-install.zip)[macOSportable · 183 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-114/Y2Linux-1.0.0-beta.8.17-first-install-macos.zip)[Windowsportable · 265 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-114/Y2Linux-1.0.0-beta.8.17-first-install-windows.zip)[Linuxportable · 438 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-114/Y2Linux-1.0.0-beta.8.17-first-install-linux.zip)

Y2Linux 1.0 Beta 8.17: fixes from your reports. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new
  - Headphones keep working after a pause (#51). After pausing, locking the screen and pressing Next, the headphones could go silent with "Playback could not start: ALSA -110" until a restart. The headphone chip's clock now keeps running between songs, as on the original firmware, and if it ever fails to start the chip is powered off and on once before giving up.
  - SD cards that a computer reads are no longer refused as "needs repair". A card that was pulled out or switched off while in use often carries small leftovers (a stale free-space count, a renamed label, a few unused clusters) that Windows ignores; the player now accepts those too and only refuses real damage. A card that is just slow to check says so instead of "needs repair", and songs on a refused card no longer ask you to reinsert it.
  - Bluetooth headphones that drop out no longer block every button. If the connection was lost at the wrong moment, every button could say "Couldn't complete that" until a restart. The player now notices, pauses and switches back to the headphone jack.
  - Bluetooth search and Connect work on the first press. Search no longer fails the first few times, and Connect waits for (and cancels) an automatic reconnect to other headphones that are switched off, instead of saying an operation is in progress. Paired devices don't need a new search: pick them and press Connect.
  - Steadier sound on weak Bluetooth speakers. With SBC (most soundbars and receivers), the player now lowers the bitrate step by step when the link struggles and raises it again when it recovers.
  - Smaller fixes: a failed update check is retried within the hour instead of the next day; your own radio stations recognise playlists served as plain text, and the reason a station fails is logged; a Bluetooth pause no longer logs a fault; error reports carry more evidence for Wi-Fi not finding your network after a wake, rare dark screens after a wake, and SD card checks.

Thanks to everyone who sent reports, opened #51, or posted on Reddit — every item above comes from them.

Everything from Beta 8.16 is included.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.17-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
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
  - BBC radio stations stream only in HLS, which the player does not play yet (planned for a later beta); stations that offer a plain MP3 or AAC stream play.
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.8.17-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 8100).
  - `Y2Linux-1.0.0-beta.8.17-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-114`. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 8.17 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.17.md).

## Sources unchanged since an earlier release
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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-114&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
