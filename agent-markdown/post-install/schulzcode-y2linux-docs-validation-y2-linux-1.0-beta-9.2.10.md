---
title: "Y2Linux 1.0 Beta 9.2.10: tidier Settings, menus that scroll properly - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.10: tidier Settings, menus that scroll properly Release 1.0.0-beta.9.2.10 , Y2Reborn 1.0.0-beta.9.2.10 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.10 , u"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.10.html"
---

# Y2Linux 1.0 Beta 9.2.10: tidier Settings, menus that scroll properly - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.10: tidier Settings, menus that scroll properly

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.10: tidier Settings, menus that scroll properly

Release `1.0.0-beta.9.2.10`, Y2Reborn `1.0.0-beta.9.2.10`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.10`, update sequence 12600, root `2026.08-platform-v1.224`. Published as GitHub release `baseline-201` (test build 201). It includes the unpublished test build 200 (Beta 9.2.9). Previous release: [Beta 9.2.8](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.8.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Settings is reorganised so that each place answers one question, every page fits on one screen, and every setting says what it does. Menus now scroll the same way everywhere, like the song and artist lists. The Music page no longer loses its last rows, and Cover Flow no longer shows an album's year twice.

## What's new
  - Settings in eight places. Bluetooth, Wi-Fi, Sound, Display, Skin, Customize, Library and System, all on

one screen: - Customize opens three short pages instead of nine loose settings: Home Menu, Browsing (Cover Flow, Sort Albums, Artists List, Lists Wrap Around) and Wheel & Buttons (Wheel on Now Playing, Wheel Click, Haptics, Buttons While Screen Off). - Sound keeps Equalizer, Normalize Volume, Balance and Output; Gapless Playback and Crossfade moved to Sound → Playback. - Display is Brightness and Screen Off After. - Library holds Scan for Music, Storage and Last.fm. - System (was About & Updates) holds Software Update, Time Zone, Date & Time (they were under Display), Error Reports, Reset & Maintenance and About.
  - Clearer settings. Names say what they change and the value says what is set ("Sort Albums: By Title",

"Buttons While Screen Off: Play Buttons"). On/off settings are switches. Settings with three choices open a short list with a check mark on the current one and a line explaining each choice. Customize's pages say at the bottom what the setting in focus does.
  - Menus scroll like lists (Y2Reborn #74). The settings pages used to show their rows inside a box that stayed

put while the rows slid inside it. Now the rows sit on the screen and scroll like Artists or Songs, down to the bottom edge, with a thin scroll bar on the right when there is more. This covers Wi-Fi and Bluetooth too.
  - The Music page scrolls (Y2Reborn #74). With Playlists and Search moved off Home, Music has seven lists;

the last ones stayed below the screen and the highlight disappeared there. Now they scroll into view.
  - Cover Flow names the artist alone (Y2Reborn #73). The artist line under the cover read "Artist · 2023"

above "2023 · 1 song · 3 min"; the year now appears once.

## What you'll notice
  - Your settings stay as they were; only their places changed. Where to find things:
    - Check for updates: Settings → System → Software Update.
    - Error reports: Settings → System → Error Reports.
    - Time zone and clock: Settings → System.
    - Wheel Click and Haptics: Settings → Customize → Wheel & Buttons.
    - Cover Flow: Settings → Customize → Browsing.
    - Last.fm and Scan for Music: Settings → Library.

  - The hidden service menu now opens by tapping Version in Settings → System → About.

## How it was tested
  - Before release: the platform's full check, Reborn's workspace tests and the tests of the finished release

images. New tests: the eight places on one screen; Customize's pages; the choice lists opening on the current choice, explaining each choice and going back to their page; the hint line; Music reaching its seventh list on the screen; a long settings list scrolling to its last row; Cover Flow showing the year once.
  - Every page drawn on the computer in the standard look and in the Classic skin and checked by eye.
  - On the developer's player: installed over the air from Beta 9.2.9 and confirmed by the player itself

(Acknowledged); the platform and Reborn running, health OK, kernel not tainted, and the saved session (queue, settings) carried over.

## Updating

Settings → About & Updates → Check for Updates → Update Now (from this version on: Settings → System → Software Update). Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.2.8; your session stays readable for it.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. The Output page does not scroll yet when there are many Bluetooth devices. Some routers refuse the player for minutes (Y2Linux #83); 9.2.8's reports will tell why.

## Technical appendix
  - Settings tree:`pages::settings`, `system_menu` (`Screen::Update`, filter "" ; Software Update is filter

`software`), `library` (`Screen::SettingsLibrary`), Sound, Display, `SettingsPlayback`; `customize.rs`: Customize's pages (filters `browsing`, `wheel`), pickers (`choose:<setting>`, rows `set:<setting>:<i>`), the hint line; `pages::sub_page` routes them. No new `Screen` values: a session saved on a new page reads in older versions. The map and the rule for adding settings: Y2Reborn `docs/ui/REBORN-SETTINGS-MAP.md`.
  - Scrolling: settings rows (`group`, the root, Wi-Fi/Bluetooth, Storage) without the card, to the hint or

the screen's edge, `group_window` + `Moving::List` + `scroll_rail`; Music `MUSIC_ROWS` 5 with `list_window`; Sound's one-row shift glides (`Moving::Scroll`).
  - Cover Flow:`catalog::album_artist` (no year) under the cover.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
