---
title: "Y2Linux 1.0 Beta 9.2.3: album years, hidden Wi-Fi, clearer Cover Flow - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.3: album years, hidden Wi-Fi, clearer Cover Flow Release 1.0.0-beta.9.2.3 , Y2Reborn 1.0.0-beta.9.2.3 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.3 , upd"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.3.html"
---

# Y2Linux 1.0 Beta 9.2.3: album years, hidden Wi-Fi, clearer Cover Flow - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.3: album years, hidden Wi-Fi, clearer Cover Flow

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.3: album years, hidden Wi-Fi, clearer Cover Flow

Release `1.0.0-beta.9.2.3`, Y2Reborn `1.0.0-beta.9.2.3`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.3`, update sequence 11900, root `2026.08-platform-v1.217`. Published as GitHub release `baseline-194` (test build 194). Previous release: [Beta 9.2.2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.2.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.2.3 makes five requests from the GitHub issues the player's default, without new settings. Albums know their release year: an artist's albums go oldest first and show their year. You can join a Wi-Fi network that is hidden. Cover Flow shows where you are in its title bar and has bigger text below the covers. Every skin numbers the songs of an album. And the grey text is a little brighter, so it reads better with the screen turned down.

## What's new
  - Album years (Y2Reborn #66). The player now reads each song's year. An artist's albums are listed oldest

first (albums without a year come last), album rows say "Artist · 1979", and the album page and Cover Flow say "1979 · 12 songs · 48 min". With Album Order: Artist (Settings → Customize), each artist's albums are in year order too.
  - Hidden Wi-Fi networks (Y2Reborn #61). At the bottom of the Wi-Fi list, Other Network… asks for the

network's name, then its password (leave it empty for an open network). The player looks for that name directly. A wrong password opens the keyboard again with what you typed, as for other networks.
  - Cover Flow (Y2Reborn #70). "25 of 100" moved up into the title bar next to the screen's name, and the artist

and album details below the covers are bigger.
  - Track numbers in every skin (Y2Linux #75). The standard look already numbered an album's songs; skins showed

the album's cover on every song instead. Now every skin shows the number there.
  - Brighter grey text (Y2Reborn #59). Secondary text (the values on the right of Settings, hints, details) is a

step brighter, so it reads better at low brightness. The white text is still clearly the brightest.

## What you'll notice
  - After the update, the player reads your songs' tags once more in the background, to learn their years. You

can use the player meanwhile; years appear as it goes. On a very large library this takes a while once (at the same speed as a normal first scan). Nothing else changes in your library.
  - Album years on artist pages and in Cover Flow; Other Network… in the Wi-Fi list.

## How it was tested
  - Before release: the platform's full check on every change, Reborn's workspace tests and the tests of the

finished release images. New tests: the year from date tags and a library from before this release reading it once; an artist's albums oldest first with their year and Album Order by artist; Other Network… with both keyboards, an open hidden network and a too-short password, and the player probing a hidden network by name; Cover Flow's title; numbered album songs in a skin and every shipped skin.
  - Speed on large libraries: on the computer with 150 000 songs, the album lists take the same time with years

as before (albums by artist 28 ms, an artist page 2.5 ms, the album line 7.3 ms).
  - Skins: every skin drawn on the computer; album pages, Cover Flow and Settings checked by eye.
  - On the developer's player: installed over the air from Beta 9.2.2 and confirmed by the player itself

(Acknowledged); all four services and Reborn running, health OK (Bluetooth was switched off), the music player ready 37.5 s after the restart, kernel not tainted, Wi-Fi online. The first scan re-read all 323 songs' tags in 3.1 s; 311 of them now have a year (38 albums).

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.2.2 if you need to; the older version reads your library as before (it reads the tags once more itself).

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies.

## Technical appendix
  - Year:`Track.year` from the `date` tag (`year_of`: the first four digits, 1000–2999); additive column `year`,

`METADATA_REVISION` 5 (each row re-reads its tags once; quick scans walk again once because the volume's revision changed). An album's year is its earliest song's; the album totals carry it (`AlbumTotal`), the catalog sorts with `year_key` (unknown last). Host profile `profile_albums_150k` (ignored test).
  - Hidden Wi-Fi:`Purpose::WifiName`, `WifiPassword { hidden }`, `Effect::WifiConnect { hidden }`,

`wifi::Command::Connect { hidden }`; a hidden join sets `scan_ssid 1`. The Wi-Fi worker commands share `send_wifi`.
  - Cover Flow: the position joins the status bar title; skins have `{position}` (Classic's Cover Flow title uses

it).
  - Skins: row flag `numbered` and `{track_number}` in rows; `build_skins.py add_numbers`.
  - Theme:`MUTED` #A0A4AE → #B4B8C2 (contrast 8.1 → 10.1), `DIM` #848894 → #989CA8 (5.7 → 7.3).
  - Library migrations share `has_column`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
