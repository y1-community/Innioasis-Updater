---
title: "Y2Linux 1.0 Beta 9.0: the system underneath, rebuilt - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.0: the system underneath, rebuilt Release 1.0.0-beta.9.0 , Y2Reborn 1.0.0-beta.9.0 , kernel 6.18.56-y2linux-1.0.0-beta.9.0 , update sequence 11400, roo"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.0.html"
---

# Y2Linux 1.0 Beta 9.0: the system underneath, rebuilt - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.0: the system underneath, rebuilt

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.0: the system underneath, rebuilt

Release `1.0.0-beta.9.0`, Y2Reborn `1.0.0-beta.9.0`, kernel `6.18.56-y2linux-1.0.0-beta.9.0`, update sequence 11400, root `2026.08-platform-v1.212`. Published as GitHub release `baseline-186` (test build 186). Previous release: [Beta 8.43](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.43.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.0 looks and works like Beta 8.43. Your music, playlists, settings, Wi-Fi networks and Bluetooth headphones stay as they are. What changed is the part of the system you never see: the services that look after the battery, sleep, Wi-Fi, Bluetooth, the SD card and Internal Storage, updates, USB file transfer, the clock and error reports. They were written in Python and are now written in Rust, the same language as the Reborn music player. The result:
  - 6–8 times less CPU spent by these services while the player is on but idle.
  - About 3½ times less memory (counted per process; the real share of RAM fell even more, see below).
  - Requests to the system are answered in a few thousandths of a second instead of half a second.
  - About 19 MB less on the system partition and a 6 MB smaller update download.
  - A slightly faster start.

On the way, a dozen small faults were found and fixed.

## What is "the platform"?

The Y2 runs two kinds of software:
  - Reborn is the music player you see: the menus, Now Playing, the library, the settings screens.
  - The platform works underneath it. Four small background services (called daemons) run all the time, and

one command-line tool (`y2-platform`) answers Reborn's questions. Between them they: - watch the battery and switch the player off safely when it runs flat; - put the player to sleep and wake it, and prove afterwards that it really slept and woke on the same start; - connect and supervise Wi-Fi, keep the clock right, and turn Bluetooth on and off; - check SD cards before they are used, mount them read-only between writes so a card pulled out stays clean, and repair or format a card when you ask; - set up Internal Storage on first start; - download, check and install updates, and undo them if the new version doesn't start properly; - show your music to a computer over USB (MTP); - collect and send error reports when you choose to.

Every time Reborn shows the battery percentage, the Wi-Fi state, the update page or the storage page, it asks the platform.

## Why rewrite it?

The platform was written in Python, which is quick to write and change, and which carried Y2Linux from the first beta to 8.43. But Python needs its interpreter on the player, and that has costs:
  - Every question costs half a second. Each `y2-platform` call started a new Python program. Even a simple

question like "is the player asleep?" took about 0.5 s and a burst of CPU. Reborn asks often (every few seconds while the screen is on), the Wi-Fi and clock events ask too, and every start and shutdown step wrote its journal through it.
  - CPU time is battery. While the player was on but idle, the platform used about 92 CPU seconds per hour.
  - Memory and space. The four Python services together took about 58 MB of RAM (counted per process). The

Python interpreter and its libraries took 22 MB on the system partition.
  - Two languages talking. Reborn (Rust) and the platform (Python) exchange messages. A misspelled field or

reason on one side was only found when something went wrong. One such mismatch once made the player say "wrong password" for a Wi-Fi network that hadn't accepted the connection for another reason.

With both sides in Rust, every answer the platform gives is now run through Reborn's own reading code before a build is accepted, so a mismatch is caught before it reaches a player. Moving Reborn onto the platform's shared message definitions, so that the compiler itself checks both sides, is the next step after this release.

## How we did it without breaking anything

A rewrite of this size is risky. It touches what happens when the battery runs out, how the player sleeps, and how updates install. We went step by step:
  - Write down what the old system does. Before any code was changed, every command and every file the

platform reads or writes was listed, and the old Python platform was recorded answering more than a thousand test situations (1,069, plus 5,729 ways of typing its commands): normal cases, odd ones and broken files. Each recording is a golden answer.
  - Translate first, change nothing. The Rust version was written to give exactly the same answers, byte for

byte, as the recordings. Only after it matched everywhere was Python removed from the player.
  - Then fix and tidy. Small faults found while translating were fixed one at a time. Each fix is listed below

and has its own test.
  - Then make it proper Rust ("typed records"). A translation from Python still thinks like Python: it handles

most of its data as loose bundles of text and numbers. In the last phase every file the system keeps became a clearly defined structure: the sleep receipt, the update journal, the SD-card record, the shutdown request and about fifty others. The computer now checks them instead of the code guessing what a field might hold.
  - Every step checked. Each change passed an automatic gate:
    - formatting and code checks;
    - a build for the player's ARM processor;
    - about 570 unit tests;
    - all golden answers;
    - Reborn's own reading of the platform's answers;
    - a check that the files on your data partition stay readable by the version before.

 That last check is what makes Restore Previous System safe: going back never finds a file it can't read.
  - On the real player. 22 test builds (165 to 186) were installed over the air on the developer's player,

each followed by a device check: health, daemons, Wi-Fi, USB, storage, sleep status and battery records. From test build 169, the first without Python, every update in the series was installed by the new code itself.

## What you'll notice

The same player, a little quicker and more frugal. Measured on the developer's player:

|  | Beta 8.43 (Python) | Beta 9.0 (Rust) |
| --- | --- | --- |
| CPU the system services use while on and idle | about 92 s per hour | about 12 s per hour |
| CPU Reborn uses with the screen off and idle | about 45 s per hour | about 14–16 s per hour |
| Memory of the system services (counted per process) | 58 MB | 17 MB |
| Their real share of RAM (shared parts counted once) | 35 MB | 5.5 MB |
| Answer to a simple question (sleep state, update state) | about 0.5 s | 6–8 thousandths of a second |
| System partition | 130 MB | 111 MB (no Python any more) |
| Update download (system part) | 56.4 MB | 50.6 MB |
| From pressing Power to the music player being ready | about 44 s | about 37 s |
| Shutdown steps after you choose Power Off | about 2.6 s | about 1.2 s |

What this means in daily use:
  - Less battery used while the player is on. Less CPU means the processor can rest more. How much battery

this saves depends on how you use the player. It matters most when the player sits on with the screen off (paused, or before it goes to sleep).
  - Menus that ask the system feel quicker. The battery, storage and update pages, the sleep request and the

Wi-Fi state no longer wait half a second for each answer.
  - Faster start and shutdown. Starting takes about 7 seconds less; shutting down runs its steps in half the

time.
  - More room. The system partition has 19 MB more free space, and updates download less.

Reborn got leaner too. With the screen off and nothing playing, Reborn now checks things every 5 seconds instead of every second, and its watchdog every 5 seconds instead of every second. Pressing a button, music starting, a headset connecting or a computer being plugged in still wakes it at once.

## Fixes in this release

Most of these were found while every line of the old system was read again for the rewrite.

Storage and USB
  - The SD card goes back to read-only right after a computer is unplugged. Y2Linux keeps a healthy SD card

read-only between writes, so pulling it out can't damage it. While a computer was connected over USB, the card's write permission was renewed every few seconds, and unplugging didn't close it. The card stayed writable for up to 30 seconds afterwards. Now the permission is closed when the cable is pulled.
  - A write permission that ran out could leave the card writable until the next card was inserted or removed.

The system now also checks for that regularly.
  - Copying over SFTP opened the old music folder. A text mismatch made SFTP (file access for advanced users)

always open the old `/data/music` folder instead of Internal Storage. Fixed.
  - The app no longer treats a read-only SD card as an error. A card with errors, which plays read-only until

you repair it, made the storage answer report a failure.

Updates
  - Two update checks at once. Starting a second check while one was still downloading made the update page

show a confusing failure, although the download went on. It now says *"An update check is already running. Try again in a moment."* and leaves the running one alone.
  - Restore Previous System on a low battery. If you chose to go back to the previous system with too little

battery, the request was refused, but the update page was left saying a restore was pending. The battery is now checked first, and nothing changes when it refuses.
  - Radio firmware that could not be installed now shows as failed instead of looking like success.

Battery, sleep and Wi-Fi
  - Automatic sleep while on the charger. The player can't sleep while a charger or computer is connected.

Reborn still asked every minute, and every try started a system process. Now it waits until the cable is unplugged; pressing Power still asks at once.
  - Battery percentage after a voltage reading. In one rare order of battery readings the old power service

stopped with an error and was restarted. That case now simply starts a fresh display value.
  - Wi-Fi briefly lost its name lookup (DNS) after renewing its address. When the router renewed the player's

address, the record of DNS servers was deleted, and for up to five minutes Wi-Fi could show no DNS. A renewal of the same address now keeps it.

Damaged files no longer crash things. The system keeps small records on the data partition: the last sleep, the update journal, the SD card, the reset plan. Such a record can be damaged by a sudden power loss or an unusual copy. The old system then sometimes stopped with an internal error. Now:
  - the status pages stay readable, and the affected item shows as unavailable;
  - in sleep, updates and reset, the player refuses the action with one clear reason (for example

`suspend_receipt_unreadable`) and starts a fresh record the next time.

A damaged record never decides that something is safe.

## What did not change
  - No new screens or settings, and nothing moved in the menus.
  - Your music, playlists, play queue, settings, Wi-Fi networks, Bluetooth pairings and Last.fm sign-in are kept.
  - The update installer (the small program that writes the new system) and the recovery screen are unchanged and

proven over many updates.
  - The kernel (Linux 6.18) and the drivers are unchanged, apart from the version number.

## Updating

Settings → About & Updates → Check for Updates → Update Now. The player restarts into the installer and back, as for every update, and confirms the new version once Reborn is running.

To go back: Settings → Diagnostics → Restore Previous System returns to the version you had before (8.43 or whatever you updated from). Your data stays; the new version was built so that the old one can still read everything.

## Known issues and what still needs your help

This is the largest change since the first beta, so please send an error report if anything behaves differently from 8.43.
  - Tested on one player so far. Beta 9.0 has run on the developer's player through 22 test builds, every one

installed over the air. Not yet repeated on that player since the last changes: - many sleep-and-wake cycles over a night; - a low-battery shutdown; - an SD card repair or format; - a reset.

 If one of these misbehaves, send an error report (Settings → Diagnostics) and, if needed, use Restore Previous System.
  - Battery life in sleep is unchanged by this release. It is about 2 mA overnight on the developer's player

(estimated from the battery voltage); stock is about 1.3 mA.
  - A system status request takes about a third of a second while charging. One of its readings has to wait

briefly while the charger is reporting. On battery it is quick. Reborn only asks for this every few seconds, and you won't notice it in the menus.
  - Everything listed under Known issues for Beta 8.43 still applies (in the [readme](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)).

## A few words explained
  - Python / Rust: programming languages. Python programs need an interpreter at run time. Rust programs are

translated in advance into machine code that runs directly.
  - Daemon / service: a small program that runs all the time in the background.
  - Golden answer: a recorded answer of the old system to a fixed situation. The new system had to give the

same one.
  - Typed record: a file whose layout is defined in the code, so the computer checks it instead of guessing.
  - Restore Previous System (rollback): going back to the system you had before the last update.
  - Over the air (OTA): installing an update downloaded over Wi-Fi.

## Technical appendix
  - Platform: one Rust binary `/usr/sbin/y2-platform` (4.2 MB) for the four daemons (power, connectivity,

service, ssh) and every command, `y2p-core` (shared rules) and `y2p-contract` (the types Reborn shares, checked against the goldens in both repositories). No Python interpreter or library in the image; the post-build step refuses one. Plans: [Rust port](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-PORT-PLAN.md), [refactor](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-REFACTOR-PLAN.md), [idiomatic Rust and typed records](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-IDIOMATIC-PLAN.md); what callers rely on: [platform contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fplatform%2FCONTRACT.md) (its "Typed records" section lists the changed refusal reasons and the record rules).
  - Verification per change:`tools/development/platform-gate.sh` covers:
    - formatting, clippy, the armv7 build and the host tests;
    - the golden suite (`tests/platform_goldens`) and the record-compat check of every /data file against the

previous release;
    - Reborn's contract test (`crates/reborn-platform/tests`).

 Reborn workspace: 738 tests. Device check per test build: `tools/development/platform-device-check.sh`.
  - Owner decisions on behaviour:
    - /data records stay readable by the release before (field names and types kept).
    - Status and health answers may change shape, with Reborn's parser changed in the same step.
    - On the critical path (sleep receipt and admission, reset, Reborn's sleep answer) a record that does not

read fails closed with one reason. There is no copying of Python's exception texts any more.

  - Measured on the developer's player:
    - test build 165 (Python, 2026-10-28) against Beta 9.0's test builds 169 and 185 (2026-10-30);
    - idle CPU from `/proc/<pid>/stat` over 300 s with the screen off;
    - memory from `smaps_rollup`;
    - start time from the boot journal's `application_ready` stage.

  - Known boundaries, kept as they are:
    - the native update core (C, `tools/update/core.c`): its journal is shown as the core writes it, with the fields

the platform reads typed;
    - Reborn's session file in a settings reset (only its settings are replaced);
    - power.json's battery reading as copied into the sleep receipt.

  - Checksums:`SHA256SUMS` in the GitHub release `baseline-186`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
