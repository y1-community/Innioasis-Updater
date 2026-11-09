---
title: "Y2Linux 1.0 Beta 8.22 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.22: set the clock by hand, updates and wake fixes. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About &"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-121.html"
---

# Y2Linux 1.0 Beta 8.22 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.22

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-121Y22026-10-22[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.8.22-first-install.zip[Y2Linux-1.0.0-beta.8.22-first-install.zip 69 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-121/Y2Linux-1.0.0-beta.8.22-first-install.zip)[macOSportable · 183 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-121/Y2Linux-1.0.0-beta.8.22-first-install-macos.zip)[Windowsportable · 265 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-121/Y2Linux-1.0.0-beta.8.22-first-install-windows.zip)[Linuxportable · 438 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-121/Y2Linux-1.0.0-beta.8.22-first-install-linux.zip)

Y2Linux 1.0 Beta 8.22: set the clock by hand, updates and wake fixes. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new
  - Set the date and time by hand ([#53](https://github.com/SchulzCode/Y2Linux/issues/53)): Settings → Display → Date & Time. For players without Wi-Fi, whose clock otherwise starts at the release date after every restart. The time is kept across restarts; as soon as Wi-Fi brings the network time, that wins.

## What's fixed
  - Headphones silent or "Playback could not start" on some players ([#52](https://github.com/SchulzCode/Y2Linux/issues/52), [#54](https://github.com/SchulzCode/Y2Linux/issues/54)). The headphone DAC runs from a small crystal. On some players it needs longer to start, or stops when warm and pushed by quick skipping, and Y2Linux gave it about a second at every Play and changed its clock at every track. It now runs like on the stock firmware: the crystal starts when the player starts, keeps running while you use the player (it rests after two idle minutes) and is no longer switched at every track change. If your player had this problem, please update and send an error report after listening for a while.
  - "Downloading Update… Keep Wi-Fi on." forever. A download that was interrupted (for example by the battery running out) left the update page stuck, also after a restart. It now says "Update Didn't Finish – Nothing was changed on your player" with Check for Updates.
  - Headphones refused to start right after waking ("busy", then Bluetooth or an error): the player now lets music start as soon as the screen is back, and tries a busy output again for two seconds.
  - Bluetooth playback dead until a restart after headphones dropped out while switching codec. It now recovers when they reconnect.
  - Pair refused ("operation in progress") while the player was reconnecting to other headphones; it now waits its turn like Connect.
  - No sleep for the rest of the day after one harmless kernel warning (a player stayed awake for hours on a weak charger). A Wi-Fi shutdown race that caused such a warning is fixed too.
  - Updates that rolled back on some players (the new system did not start twice in a row, seen on two GC9503V players): the recovery now turns the screen off before restarting into the new system, like a normal restart. The first boots after an update now also leave a record of how far they got, so if it ever happens again an error report shows where.
  - Error reports: Wi-Fi failures keep their reason and the last failure, logs are no longer flooded by display messages (reports covered only the last minutes), quick track skips no longer list every queued song as unreadable.

Everything from Beta 8.21 is included.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.8.22-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
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
  - `Y2Linux-1.0.0-beta.8.22-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 8607).
  - `Y2Linux-1.0.0-beta.8.22-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-121`. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 8.22 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.22.md).

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-121&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
