---
title: "Y2Linux 1.0 Beta 9.2.15: Settings scrolls smoothly with a large library - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.15: Settings scrolls smoothly with a large library Release 1.0.0-beta.9.2.15 , Y2Reborn 1.0.0-beta.9.2.15 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.15"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.15.html"
---

# Y2Linux 1.0 Beta 9.2.15: Settings scrolls smoothly with a large library - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.15: Settings scrolls smoothly with a large library

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.15: Settings scrolls smoothly with a large library

Release `1.0.0-beta.9.2.15`, Y2Reborn `1.0.0-beta.9.2.15`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.15`, update sequence 13100, root `2026.08-platform-v1.229`. Published as GitHub release `baseline-206` (test build 206). Previous release: [Beta 9.2.14](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.14.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

A user with 72 000 songs found that scrolling in Settings lagged since the Settings redesign of Beta 9.2.10, while every other menu was fast (Y2Reborn #85). They found the cause themselves and sent the fix (Y2Reborn #86): the Settings page and Settings → Library, which both show how many songs you have, counted the whole library again for every picture the player drew. They now use the count the player already keeps, as all other pages do. Every other screen was checked the same way with 72 000 songs: none of them does this.

## What changed
  - Settings is fast with a large library (Y2Reborn #85, fix by mrtngamper in #86). While the player lays out a

screen it lends the song list to the layout for a moment; these two pages read the song count from the place the list had just left, found it empty, and so the saved count was thrown away and made again from all songs on every frame. With 72 000 songs that took about 20 ms per frame on a computer, many times longer on the Y2.

## How it was tested
  - Before release: the platform's full check, Reborn's workspace tests (776) and the tests of the finished release

images. The new test fails without the change: Settings and Settings → Library show the song count of the list they are given. A timing of every screen with 72 000 songs, one frame each while scrolling, found Settings and Settings → Library at about 19.5 ms per frame without the fix and every screen under 0.5 ms with it (on a computer).
  - On the developer's player (from Beta 9.2.14 by update): staged, installed and acknowledged on the first start

about 95 s after Apply; Reborn drew its first frame 23.7 s after the start. The developer's library is small, so the speed itself was measured on a computer, not on the player.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.2.14.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies.

## Technical appendix
  - Cause: `main_loop.rs` render and `Ui::model_action``mem::take``model.library.tracks` while `normalize` and

actions run; `pages::settings` and `pages::library` read `m.library.tracks` for `Ui::library_counts`, whose single-slot cache is keyed by `library_stamp` (pointer, length). The empty borrow and the real list alternated, so each draw recounted every track into the artist, album and genre sets.
  - Reborn `97e46a8` (PR #86, squashed): both pages count the `tracks` they are given; test

`settings_count_the_songs_they_are_given`. `224f4f9` restores a test name the PR changed by accident.
  - Audit: the other borrow, `Runtime::with_model_action`, puts the library back before the action runs; no other

reborn-ui code reads `m.library.tracks`; `AppModel::rehydrate_queue` runs only when the library is published.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
