---
title: "Y2Linux 1.0 Beta 9.2.13: one song from search, quick audiobook resume, letter scrolling you can reach - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.13: one song from search, quick audiobook resume, letter scrolling you can reach Release 1.0.0-beta.9.2.13 , Y2Reborn 1.0.0-beta.9.2.13 , kernel 6.18"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.13.html"
---

# Y2Linux 1.0 Beta 9.2.13: one song from search, quick audiobook resume, letter scrolling you can reach - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.13: one song from search, quick audiobook resume, letter scrolling you can reach

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.13: one song from search, quick audiobook resume, letter scrolling you can reach

Release `1.0.0-beta.9.2.13`, Y2Reborn `1.0.0-beta.9.2.13`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.13`, update sequence 12900, root `2026.08-platform-v1.227`. Published as GitHub release `baseline-204` (test build 204). Previous release: [Beta 9.2.12](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.12.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Picking a song in the search results now plays just that song; Play All is there for all of them (Y2Reborn #79). Long MP3 and AAC files (audiobooks, long recordings) took seconds to continue after the player had been asleep, and longer the further in you were; they now continue at once (Y2Reborn #80). Letter-by-letter fast scrolling, which Beta 9.2.2 made so hard to start that a hard spin never reached it, starts again at a real spin while a quick turn still moves row by row (Y2Linux #64). And error reports now say why a Bluetooth device disconnected, to find out why some players lose their headphones often.

## What changed
  - One song from search (Y2Reborn #79): selecting a song among the search results played it together with

every other song found, so Play All did nothing a single pick did not. Now a picked song plays alone, on the results page and on See All; Play All plays every song found. Now Playing still offers Go to Search.
  - Quick resume of long MP3 and AAC files (Y2Reborn #80): these formats carry no table of where each minute

starts, so to continue at, say, 3 hours the player read the file from the beginning up to that point, every time it woke from sleep. Now it remembers the places it already passed and starts reading just before the spot. On a computer, continuing at 90 % of a 3-hour file went from 0.1 s to under a millisecond; on the Y2 that is several seconds saved. It remembers the last four long files until the player restarts; the first resume after a restart still reads from the beginning once. M4A, M4B and Opus files were never affected.
  - Letter scrolling (Y2Linux #64): 9.2.2 started the letter jumps only at the wheel's very fastest speed (ten

steps under 45 ms apart), which two users could not reach however hard they spun. They now start at a real spin (six steps under 70 ms apart). A quick, steady turn still moves row by row, as 9.2.2 made it.
  - Bluetooth disconnects in error reports: each disconnect is now logged with whose side ended it: the link was

lost (out of range, radio), the headphones ended it (switched off, battery, case), or the player ended it. If your headphones drop often, send an error report right after it happens.

## How it was tested
  - Before release: the platform's full check, Reborn's workspace tests (774) and the tests of the finished release

images. New tests, each failing without its change: a picked search song plays alone and See All plays one, not nine; a second opening of a 10-minute AAC file lands on its target although the file's middle was blanked after the first (only possible from the remembered places); a 2-step turn moves rows and a 3-step spin shows the letter; every Bluetooth disconnect reason is named and its device read.
  - On the developer's player (from Beta 9.2.11 by update): staged in 8.6 s, installed and back in about 50 s

(install steps 16 s), acknowledged on the first start. Reborn 9.2.13 ran; the new Bluetooth record caught a real disconnect of the saved headphones right after the start (BlueZ named no reason for that one: "Unspecified").
  - Still to check on a player: how long a resume takes after sleep, and whether the new letter speed feels right.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.2.12.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies.

## Technical appendix
  - Reborn `76edbe8`: `play_effect` gives a search song a one-member `PlayCollection` (source "Search “…”" kept).
  - Reborn `9d2c2ae`: without `AVFMT_FLAG_FAST_SEEK`, FFmpeg 9.0.2's `mp3_seek` returns -1 and ADTS AAC has no

`read_seek`, so `seek_frame_generic` reads from `data_offset`; resume reopens the decoder (`playback/decode.rs`). `native/seek_index.c` keeps a sparse copy of a closing decoder's generic index (4 files, ≤2048 points ≥5 s apart, spans ≥120 s) keyed by device/inode/size/mtime and adds it before the next decoder's first seek. Host, 3-h files at 90 %: AAC 109 → 0 ms, MP3 64 → 0 ms, exact positions.
  - Reborn `56405af`: the Bluetooth worker watches BlueZ 5.87 `Device1.Disconnected(reason, message)` and logs

`peer_disconnected` {address, reason timeout|remote|local|unknown, bluez_reason, message}.
  - Reborn `141a9ff`: `LETTER_SCROLL_STEPS` 4 → 3 (`WheelCadence`: 3 = six detents, smoothed ≤70 ms).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
