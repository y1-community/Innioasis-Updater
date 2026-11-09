---
title: "Y2Player v2.3 for the Innioasis Y2 — Up Next queue, genre/year browsing, and album art in menus - Innioasis Updater"
description: "Y2Player v2.3 for the Innioasis Y2 — Up Next queue, genre/year browsing, and album art in menus Version 2.3 focuses on making the queue behave the way people expect, addi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2player-docs-y2player_v2_3_reddit_post.html"
---

# Y2Player v2.3 for the Innioasis Y2 — Up Next queue, genre/year browsing, and album art in menus - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=y2player-y2)

Post-install setup · Y2Player · Y2

# Y2Player v2.3 for the Innioasis Y2 — Up Next queue, genre/year browsing, and album art in menus

A Y2 custom Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=y2player-y2)[Install guide](../guide.html?model=Y2&software=y2player-y2)

# Y2Player v2.3 for the Innioasis Y2 — Up Next queue, genre/year browsing, and album art in menus

Version 2.3 focuses on making the queue behave the way people expect, adding more ways to browse a music library, and displaying album artwork throughout the menus without doing unbounded image work on the Y2's older hardware.

🎵 A Proper Up Next Queue

The queue is now split conceptually into two parts:
  - Up Next contains songs you deliberately add.
  - Continuation contains the rest of the album, playlist, or shuffled collection that was already playing.

Play Next places something directly after the current song. Add to Up Next appends it after the songs you already added. When those songs finish, Y2Player returns to the original album or collection.

Shuffle now exposes the real upcoming order instead of saying that the next song will be decided later. Manually added songs stay ahead of the shuffled continuation and retain their order. Turning Shuffle off restores the remaining collection order without discarding Up Next.

Duplicate songs are tracked as separate queue entries, so moving or removing one occurrence does not accidentally affect another copy.

🎛 Wheel-Friendly Queue Controls

Pressing Center on a queue entry opens a circular menu with Play Now, Play Next, Move, and Remove. Move uses the wheel to choose the new position directly.

The Queue Actions row provides:
  - Clear Up Next
  - Clear After Current
  - Stop & Clear

Queue management is now available directly from the queue instead of being buried behind several nested song menus.

📚 Albums, Collections, and Multi-Select

Holding Center on an album or another supported collection opens actions for the complete group:
  - Play Next
  - Add to Up Next
  - Add Shuffled

Track Options also has Select Multiple. Use Center to select or deselect songs in the current list, then hold Center to apply the same queue actions to the chosen set.

This means you can start an album or Shuffle All, build a short list of songs you want to hear first, and then let the original playback continue automatically.

🗂 Browse by Genre and Year

The Music menu now contains Genres and Years.

Inside either view you can browse all matching tracks, artists, or albums. The filter stays active as you move through an artist and into an album, rather than dropping you back into the complete library.

Repeated or semicolon-separated genre values become individual genres, while names such as `R&B/Soul` remain intact. Missing values are still available under Unknown Genre or Unknown Year.

Album sorting now supports title, artist, oldest release first, and newest release first. Year lists can be newest-first or oldest-first, and album rows display the release year when it is known. Albums with the same title but different album artists also remain separate.

🖼 Album Art in Menus

Song lists and the rows for albums, artists, genres, years, playlists, audiobooks, and the queue can now show album-art thumbnails on the left.

Embedded artwork is still preferred. The existing external `folder.jpg`, `folder.jpeg`, `folder.png`, `cover.jpg`, `cover.jpeg`, and `cover.png` files work here too.

The obvious concern was lag, so the implementation is deliberately conservative:
  - only artwork for rows currently visible on screen is requested;
  - thumbnails use the existing bounded artwork cache;
  - visible images are loaded in a controlled sequence;
  - offscreen and stale requests are cancelled or ignored;
  - damaged, oversized, missing, or unavailable images fail safely.

Album song lists keep their track numbers instead of replacing them with thumbnails.

📖 Audiobooks Stay in Audiobooks

Chapters under `AUDIOBOOKS` no longer appear among ordinary Songs, Albums, Artists, Genres, Years, Favorites, Recently Played, Folders, playlists, or Shuffle All.

They remain fully available in the dedicated Audiobooks section with resume progress and chapter ordering.

The circular menu while playing an audiobook is now limited to options that make sense there: Chapters, Queue, Sleep Timer, and Track Details.

🏷 Better Ogg/Opus Artist Metadata

Vorbis comments can contain several separate `ARTIST` values. FFmpeg presents those values to the app separated by semicolons, which Y2Player previously displayed as one giant artist name.

They are now split into individual artist entries. Duplicate values are removed, featured-artist parsing still works, and the complete credit remains available for display.

🧹 Maintenance

This update also removes unused model fields, counters, result wrappers, and duplicate state across the playback, queue, diagnostics, Bluetooth, display, backup, and library code. The goal is to keep the application smaller and easier to reason about without removing user-facing functionality.

The complete debug unit-test suite passes with the new queue, browsing, metadata, audiobook, and artwork behavior.

💿 Installation

The release provides the existing `system.img` update path and a complete `rom_y2.zip` package for the Innioasis Updater.

For the system-only method, use SP Flash Tool in Download Only mode with only the ANDROID partition selected.

The `rom_y2.zip` package is a full-device installation and erases user data. Create a Y2Player backup and copy anything important off the device before using it. Please verify the supplied checksums and read the complete installation guide before flashing.

🐞 Reporting Bugs

If you encounter a problem, enable verbose diagnostics first:

Settings → System → Diagnostics → Verbose Diagnostics

Reproduce the issue, then export the report:

Settings → System → Diagnostics → Export Diagnostics

Please attach the exported report when opening a GitHub issue. For queue problems, mention what originally started playback, which queue action you used, and whether Shuffle or Repeat was enabled. For artwork problems, mention whether the cover is embedded or external and include its filename if possible.

Thanks again to everyone testing Y2Player and taking the time to write detailed reports. The queue redesign, year and genre views, audiobook separation, repeated-artist handling, and menu artwork all came directly from that feedback.

These are Y2Player's own instructions, shown here word for word.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
