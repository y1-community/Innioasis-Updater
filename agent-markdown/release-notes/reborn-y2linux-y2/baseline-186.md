---
title: "Y2Linux 1.0 Beta 9.0 - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.0: the system underneath, rebuilt. Linux 6.18 and the native Reborn music player for the Innioasis Y2. Already running Y2Linux Settings → About & Updates → Check"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-186.html"
---

# Y2Linux 1.0 Beta 9.0 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.0

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-186Y22026-10-30[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

Y2Linux-1.0.0-beta.9.0-first-install.zip[Y2Linux-1.0.0-beta.9.0-first-install.zip 64 MB](https://github.com/SchulzCode/Y2Linux/releases/download/baseline-186/Y2Linux-1.0.0-beta.9.0-first-install.zip)[macOSportable · 178 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-186/Y2Linux-1.0.0-beta.9.0-first-install-macos.zip)[Windowsportable · 260 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-186/Y2Linux-1.0.0-beta.9.0-first-install-windows.zip)[Linuxportable · 433 MB](https://github.com/y1-community/y2linux-mirror/releases/download/baseline-186/Y2Linux-1.0.0-beta.9.0-first-install-linux.zip)

Y2Linux 1.0 Beta 9.0: the system underneath, rebuilt. Linux 6.18 and the native Reborn music player for the Innioasis Y2.

## Already running Y2Linux

Settings → About & Updates → Check for Updates → Update Now.

## What's new

Beta 9.0 looks and works like Beta 8.43. Your music, playlists, play queue, settings, Wi-Fi networks, Bluetooth pairings and Last.fm sign-in all stay. What changed is everything underneath the music player. This is the biggest change to Y2Linux since the first beta.

### The part you never see: "the platform"

The Y2 runs two kinds of software. Reborn is the music player you see: the menus, Now Playing, the library and the settings screens. Underneath it, the platform works all the time: four small background services and one command tool. Between them they:
  - watch the battery and switch the player off safely before it runs flat;
  - put the player to sleep and wake it, and check afterwards that it really slept and woke on the same start;
  - connect and supervise Wi-Fi, keep the clock right, and turn Bluetooth on and off;
  - check SD cards before they are used, keep a healthy card read-only between writes so pulling it out can't damage it, and repair or format a card when you ask;
  - set up Internal Storage on the first start;
  - download, verify and install updates, and undo an update that doesn't start properly;
  - show your music to a computer over USB;
  - collect and send error reports when you choose to.

Every time Reborn shows the battery, the Wi-Fi state, the storage page or the update page, it asks the platform.

### From Python to Rust

Until 8.43 the platform was written in Python, which needs its own interpreter on the player. That had costs you could feel:
  - Every question took about half a second. Each request started a new Python program, even "is the player asleep?". Reborn asks every few seconds while the screen is on, and so do the Wi-Fi and clock events and every start and shutdown step.
  - CPU time is battery. While the player was on but idle, the platform alone used about 92 CPU seconds every hour.
  - Memory and space. The Python services took about 58 MB of RAM, and Python itself 22 MB on the system partition.
  - Two languages talking to each other. A misspelled field on one side was only noticed when something went wrong. Once this made the player say "wrong password" for a Wi-Fi network that had failed for another reason.

In Beta 9.0 the whole platform is Rust, the language Reborn is written in. It's one program of 4.2 MB, with no Python left on the player. Every answer the platform gives is now run through Reborn's own reading code before a build is accepted, so a mismatch is caught before it reaches a player (letting the compiler check both sides directly is the next step).

### The numbers

Measured on the developer's player:

|  | Beta 8.43 (Python) | Beta 9.0 (Rust) |  |
| --- | --- | --- | --- |
| CPU the system services use while the player is on and idle | ≈ 92 s per hour | ≈ 12 s per hour | about 7× less |
| CPU Reborn uses with the screen off and nothing playing | ≈ 45 s per hour | ≈ 14–16 s per hour | about 3× less |
| Memory of the system services (counted per process) | 58 MB | 17 MB | about 3½× less |
| Their real share of RAM (shared parts counted once) | 35 MB | 5.5 MB | about 6× less |
| Answer to a simple question (sleep, update, battery state) | ≈ 0.5 s | 6–8 ms | about 70× faster |
| System partition | 130 MB | 111 MB | 19 MB more free space |
| Update download (system part) | 56.4 MB | 50.6 MB | 6 MB smaller |
| Press Power → music player ready | ≈ 44 s | ≈ 37 s | about 7 s faster |
| Shutdown steps after Power Off | ≈ 2.6 s | ≈ 1.2 s | twice as fast |

What this means for you:
  - Less battery used while the player is on. It matters most when the player sits on with the screen off: paused, or waiting to go to sleep.
  - Snappier system pages. The battery, storage, update and Wi-Fi information no longer waits half a second per question.
  - A quicker start and shutdown, more room on the system partition, and smaller updates.

Battery life in sleep is unchanged by this release (see Known issues).

### Reborn got leaner too
  - Quieter when dark. With the screen off and nothing playing, Reborn now checks things every 5 seconds instead of every second, and reads the battery and storage every 10 seconds instead of every 2. A button press, music starting, a headset connecting or a computer being plugged in still wakes it at once.
  - No more sleep attempts on the charger. The player can't sleep while a charger or computer is connected, but Reborn used to ask every minute anyway, and each try started a system process. Now it waits until the cable is unplugged; pressing Power still asks at once.

### How we made sure nothing broke

A rewrite like this touches the scariest parts of the system: running out of battery, sleep, and installing updates. So it went in careful steps:
  - Recorded the old system first. Every command and every file the platform uses was listed. The old Python platform was then recorded answering 1,069 test situations: normal ones, odd ones and damaged files. It was also recorded handling 5,729 ways of typing its commands.
  - Translated without changing anything. The Rust version had to give exactly the same answers, byte for byte, before Python was removed.
  - Fixed what we found, one fault at a time, each with its own test (list below).
  - Turned it into proper Rust. Every file the system keeps is now a clearly defined structure: the sleep record, the update journal, the SD card record, the shutdown request and about fifty more. The computer checks them instead of the code guessing what a field holds.
  - Checked every step automatically:
    - about 570 platform tests and 738 Reborn tests;
    - all recorded answers;
    - Reborn reading every platform answer;
    - a check that everything on your data partition stays readable by the previous version.

 That last check is what keeps Restore Previous System safe.
  - 22 test builds on a real player, every one installed over the air and checked on the device.

### Fixes in this release

Storage and USB
  - The SD card goes back to read-only right after you unplug a computer. While a computer was connected, the card's write permission was renewed every few seconds and never closed on unplug, so it stayed writable for up to 30 seconds.
  - A write permission that ran out could leave the card writable until the next card was inserted or removed. The system now checks for that regularly.
  - SFTP (file access for advanced users) opened the old music folder instead of Internal Storage.
  - A card with errors (which plays read-only until repaired) was reported as a failure.

Updates
  - Two update checks at once showed a confusing failure. Now: "An update check is already running. Try again in a moment."
  - Restore Previous System on a low battery was refused but left the update page saying a restore was pending. The battery is now checked first.
  - Radio firmware that could not be installed now shows as failed instead of looking like success.

Battery, sleep and Wi-Fi
  - DNS after an address renewal. When the router renewed the player's address, Wi-Fi could show no DNS for up to five minutes. The DNS servers are now kept.
  - Battery percentage. In one rare order of battery readings the power service stopped with an error and had to be restarted.

Damaged files no longer cause internal errors. A sudden power loss can damage one of the small records the system keeps. Now:
  - the status pages stay readable, and the affected item shows as unavailable;
  - sleep, updates and reset refuse with one clear reason and start a fresh record next time.

A damaged record never decides that something is safe.

### What did not change
  - No new screens or settings, and nothing moved in the menus.
  - The update installer and the recovery screen, both proven over many updates.
  - The kernel (Linux 6.18) and drivers, apart from the version number.

The full story, written for players' owners, with a glossary and a technical appendix: [Beta 9.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md). Everything from Beta 8.43 is included.

## Install (from stock)

You need SP Flash Tool v5.2032, a USB cable, `Y2Linux-1.0.0-beta.9.0-first-install.zip` below and the Innioasis Y2 firmware package v3.2.0 from Innioasis (only this version works; it is also your way back to stock).
  - Unpack both.
  - SP Flash Tool → Download Only → load `MT6582_Android_scatter.txt`from the Y2Linux zip. Exactly BOOTIMG, RECOVERY, ANDROID and USRDATA are ticked.
  - Click Download and connect the switched-off Y2; wait for the green tick.
  - Unplug and press Power: the player sets up its Internal Storage (a few seconds), then Y2Linux and Reborn start, music works.
  - Connect the Y2 to the computer and copy (don't move) `system.img` from the Innioasis package into the Firmware folder on Internal Storage. The player takes the Wi-Fi/Bluetooth firmware from it and turns the radios on.

Full guide: [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) · How updates work: [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FRECOVERY-AND-UPDATES.md) · Storage: [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FSTORAGE.md) · [Audiobooks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FAUDIOBOOKS.md) · Headphone settings: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FHEADPHONE-OUTPUT.md) · [Error reports](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FERROR-REPORTS.md)

## Known issues (beta)
  - A big change underneath: Beta 9.0 has run through 22 test builds on the developer's player, but not yet on many players. Overnight sleep, a low-battery shutdown, an SD card repair or format and a reset have not been repeated since the last changes. If anything behaves differently from 8.43, send an error report (Settings → Diagnostics); Settings → Diagnostics → Restore Previous System goes back to the version you had, with your data kept.
  - Battery life in sleep: about 2 mA overnight on the developer's player (estimated from the battery voltage); stock is about 1.3 mA. This release doesn't change it.
  - Wi-Fi and Bluetooth on players with empty factory partitions (#62) use the chip's default calibration; please send a report if the range is poor.
  - Some players turned off by themselves during playback; the cause is not found yet. If yours does, start it again and send a report.
  - While a large SD card is being checked (up to a few minutes), you can't copy music to it over USB yet.
  - The speaker uses the same volume as the headphones; its loudest step is the stock speaker's. Start low the first time.
  - Going back to a version older than 8.33 starts with an empty queue (your settings are kept).
  - Some car radios don't show the song and artist yet; we are looking into it.
  - In a very long single-file book, jumping to another chapter takes 2–3 seconds.
  - With very large libraries (100 000+ songs) a list can still take up to about a second the first time right after the player starts, and the first scan of such a card takes several minutes.
  - BBC radio stations stream only in HLS, which the player does not play yet (planned for a later beta).
  - FM radio is in the works for a later beta.

## Files
  - `Y2Linux-1.0.0-beta.9.0-first-install.zip`: images, scatter files and checksums for SP Flash Tool. The data image has no SSH key (developers: `tools/production/first_owner.py`).
  - `manifest.json`, `manifest.sig`, `rootfs.ext4.gz`, `bootimg.img.gz`, `recovery.img.gz`: the signed over-the-air update (Ed25519 key `platform-v1-release-20261015`, sequence 11400).
  - `Y2Linux-1.0.0-beta.9.0-sources-buildroot-legal-info.tar` (licences, manifests, this project's packages) and the third-party, toolchain and Linux sources linked below: corresponding sources. Our own code: Y2Linux and Y2Reborn at tag `baseline-186`. The speaker amplifier driver is Chris Hendrickson's GPL-2.0 AW87559 driver. The headphone profiles are AutoEq results (MIT, Jaakko Pasanen); their licence ships with them.
  - `SHA256SUMS` for the attached files.

Beta software: use at your own risk. Not affiliated with Innioasis, MediaTek, Awinic, Last.fm, AutoEq, Strawberry or Google. Noto Sans CJK is licensed under the SIL Open Font License 1.1. Details: [Beta 9.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md).

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
  - [Y2Linux 1.0 Beta 9.3.7baseline-215 · 2026-11-03](../../release-notes/reborn-y2linux-y2/baseline-215.html)

Notes as published by the Reborn (Y2Linux) project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-186&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
