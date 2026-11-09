---
title: "Y2Linux 1.0 Beta 9.3.17: covers, file names, Bluetooth first connect - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.3.17: covers, file names, Bluetooth first connect Release 1.0.0-beta.9.3.17 , Y2Reborn 1.0.0-beta.9.3.17 , kernel 6.18.56-y2linux-1.0.0-beta.9.3.17 , u"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.3.17.html"
---

# Y2Linux 1.0 Beta 9.3.17: covers, file names, Bluetooth first connect - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.3.17: covers, file names, Bluetooth first connect

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.3.17: covers, file names, Bluetooth first connect

Release `1.0.0-beta.9.3.17`, Y2Reborn `1.0.0-beta.9.3.17`, kernel `6.18.56-y2linux-1.0.0-beta.9.3.17`, update sequence 15000, root `2026.08-platform-v1.248`. Published as GitHub release `baseline-225` (test build 225). Previous release: [Beta 9.3.16](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.16.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Covers are back on Now Playing and the Home screen for MP3 and AAC songs (Y2Reborn #102, Y2Linux #98), **files with dots, emoji or ';' in their names copy over USB (Y2Linux #88), Bluetooth headphones get the music on the first connect (Y2Reborn #103) and Cover Flow follows a folder cover that was deleted or replaced** (Y2Reborn #105). The fixes are written to hold for every format, file name and headset, not only for the ones in the reports.

## What changed
  - Covers on Now Playing: Beta 9.3.16 let a song's cover wait until a quarter of a second of the song was ready

to play, so that preparing the cover never starved the Bluetooth stream. With MP3, AAC (M4A), Opus and Ogg songs that amount was never reached, because these formats arrive in smaller pieces than FLAC, and the cover only came at the end of the song. Now the cover comes once enough music is ready or half a second after the song starts, whichever is first, for every format.
  - Copying over USB: names that the player refused or changed now copy as they are:
    - two or more dots in a row anywhere in the name ("I Still....m4a"),
    - emoji and other characters outside the basic set (Coldplay's 🌎 and 🪐 titles); such names on the card also

show whole on the computer now instead of cut off at the first emoji,
    - ';' ("Memphis; The Blues") is kept: it used to become '_', and sync tools such as MusicBee then copied the file

again on every sync,
    - long names in Chinese, Japanese or Korean are no longer cut short.

 Characters that memory cards cannot store (`\ / : * ? " < > |`) still become '_'; Windows never sends them.
  - Bluetooth on the first connect: when headphones connected, the player switched the music to them a moment

before their audio stream was fully set up; the switch was refused and the music stayed on the headphone jack until the headphones reconnected. The player now waits until the stream is ready, and if a switch still fails it tries again every 2 seconds, up to five times.
  - Cover Flow: a folder picture (cover.jpg and the like) that was deleted, added or replaced now shows in Cover

Flow too; before, Cover Flow kept the old picture while the album page showed the new one. All Cover Flow pictures are made once more after the update, as you scroll.

## How it was tested
  - Reports: the error reports named in the issues were read. On 9.3.16, MP3 libraries showed a cover for 0 of 1,

2 of 9, 3 of 9 and 4 of 60 songs played, a FLAC library for 4 of 4; before 9.3.16 MP3 libraries showed 25 of 25. The Bluetooth report shows the refused switch 0.66 s after the headphones connected, on every start.
  - New tests:
    - a cover test plays two 3-second songs in a row in each of MP3, M4A, Opus, Ogg and FLAC and requires each song's

cover within 1.5 s of its start (on 9.3.16's code the MP3 cover came at 2.96 s);
    - the USB test sends the names from the issue the way Windows does and reads them back as the computer would

(it fails with "Malformed object name" without the fix);
    - Bluetooth: a stream listed before it is set up is not used yet, and a failed switch is tried again;
    - Cover Flow: deleting and adding a folder cover makes a new thumbnail.

  - Before release: the platform's full check, Reborn's workspace tests and the tests of the release images.
  - On a player: test build 225 installed by update on the developer's player (back and confirmed 87 seconds

after the update started). A song with a folder cover showed it about 0.8 s after Play, the next gapless song's cover came too, and nothing ran empty. That player's card holds no MP3 with a cover and none of the issue's file names, so those two were tested on the computer.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to the version you had.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help), [Beta 9.3.15](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.15.md%23known-issues&anchor=known-issues) and [Beta 9.3.16](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.16.md%23known-issues&anchor=known-issues) still applies.
  - Names longer than 255 bytes (about 85 Chinese or Japanese characters) fit on the SD card but not on Internal

Storage.
  - Bluetooth headphones that offer only mono sound cannot play yet.
  - A soundbar that stutters while Wi-Fi is on (Y2Linux #99) and new SD songs that do not show (Y2Reborn #104) are

still being looked at; an error report helps.

## Technical appendix
  - Reborn `0978fb4` (`playback/decode.rs`): `Unsettled::due` settles a song (cover, media state, gapless preopen of

the next song) once ≥ 250 ms are queued or `SETTLE_WAIT` 500 ms after its first block. The decoder→sink channel holds 8 blocks; 8 MP3 (1152), AAC (1024) or Opus (960) blocks are 190–210 ms, so 9.3.16's cushion was unreachable (F74). Fixtures `cover-3s.*`, test `every_codec_gets_its_cover_early_in_the_song_and_after_a_gapless_boundary`.
  - Reborn `e9f72a0` (`outputs.rs`, `main_loop.rs`): `AutoOutput` treats a peer as ready when `playback_rate` succeeds

(stereo, rate known) and retries a failed switch after `AUTO_OUTPUT_RETRY` 2 s, `AUTO_OUTPUT_TRIES` 5 per connection (F76).
  - Reborn `0f09caa` (`artwork.rs`): the thumbnail cache name carries `Key::folder_revision` (folder cover candidates'

names, sizes, mtimes); prefix `thumb4-` (F77).
  - Linux `fc0888c5`: uMTP patch 0007 (only "." and ".." refused; surrogate pairs in both directions; ';' kept;

1024-byte name buffers), `tests/usb_mtp_protocol.c` name cases; patch 0006 `(void)ret` for gcc 16 (F75).
  - Linux `132cbec9` (built), Reborn `e14b17b` (built). Findings F74–F77 in the report ledger.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
