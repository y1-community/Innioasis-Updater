---
title: "Y2Player v2.3 — Up Next Queue, Library Browsing, and Menu Artwork - Innioasis Updater"
description: "Y2Player v2.3 — Up Next Queue, Library Browsing, and Menu Artwork Version 2.3 focuses on making the playback queue predictable, expanding the ways a library can be browse"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2player-docs-y2player_v2_3_release_post.html"
---

# Y2Player v2.3 — Up Next Queue, Library Browsing, and Menu Artwork - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=y2player-y2)

Post-install setup · Y2Player · Y2

# Y2Player v2.3 — Up Next Queue, Library Browsing, and Menu Artwork

A Y2 custom Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=y2player-y2)[Install guide](../guide.html?model=Y2&software=y2player-y2)

# Y2Player v2.3 — Up Next Queue, Library Browsing, and Menu Artwork

Version 2.3 focuses on making the playback queue predictable, expanding the ways a library can be browsed, and bringing album artwork into the menu system without turning scrolling into unbounded image work.

It also separates audiobooks more cleanly from music, improves repeated Vorbis metadata handling, and removes unused internal state across the application.

## A Queue That Shows What Will Actually Play

The playback queue has been rebuilt around two explicit sections:
  - Up Next contains tracks deliberately added by the user.
  - Continuation contains the remaining tracks from the album, playlist, library collection, or shuffled collection that started playback.

Play Next puts a track or selected collection directly after the current track. Add to Up Next appends tracks in the order they were added. When Up Next is empty, playback returns to the original continuation instead of abandoning the album or collection that was already playing.

Shuffle now exposes the actual upcoming playback order in the queue. Manually added tracks remain ahead of the shuffled continuation and keep their deliberate order. Turning Shuffle off restores the remaining source collection to its original order without losing Up Next.

Repeat All repeats the source collection rather than repeatedly injecting manually added Up Next entries. Duplicate tracks also receive distinct queue-entry identities, so moving or removing one occurrence does not affect another copy of the same song.

## Queue Controls Designed for the Click Wheel

The queue screen now places Queue Actions at the top and then shows the current and upcoming songs in playback order.

Pressing Center on a queue entry opens a circular action menu containing the actions that apply to that occurrence:
  - Play Now
  - Play Next
  - Move
  - Remove

Move opens the queue itself as a wheel-controlled position selector. Reordering stays inside the relevant Up Next or continuation section, so an ordinary move cannot accidentally change the meaning of the queue.

Queue Actions provides focused cleanup commands:
  - Clear Up Next removes only manually added songs.
  - Clear After Current keeps the current song and removes everything after it.
  - Stop & Clear stops playback and removes the complete queue after confirmation.

The navigation has also been flattened. Queue management no longer requires opening several nested menus from an individual song, and holding Center on a queue row remains a quick Play Now shortcut.

## Add Albums, Collections, or Several Selected Songs

Queue actions are no longer limited to one track at a time.

Holding Center on an album or another supported collection opens batch actions for the complete collection:
  - Play Next
  - Add to Up Next
  - Add Shuffled

Track Options also includes Select Multiple. Center toggles individual songs in the current list, and holding Center opens the same batch queue actions for the selected set.

This makes it possible to start an album or Shuffle All, choose several songs to hear first, and then return automatically to the original playback sequence.

## Browse Music by Genre and Year

The Music menu now includes Genres and Years.

Opening a genre or year provides separate destinations for all matching tracks, artists, and albums. The selected filter is retained while navigating through an artist and into one of their albums, so a year or genre view does not unexpectedly expand back into the entire library.

Genre values separated by repeated Vorbis comments or semicolons are treated as separate genres. Duplicate values are collapsed case-insensitively, while names containing characters such as the slash in `R&B/Soul` remain intact. Tracks without a genre or year remain available under Unknown Genre and Unknown Year.

Album identity now includes the album artist. Two artists can therefore each have an album called Greatest Hits without their tracks being merged into one global album entry.

## More Sorting Choices

Sort Order under Settings → Library is now divided into three groups:
  - Tracks retains the existing track-order choices.
  - Albums can be ordered by title, artist, oldest release first, or newest release first.
  - Year Lists can show newest or oldest years first.

Album rows display their release year where it is available. Unknown years stay at the end in both directions, and the chronological order of songs inside an album is not changed by a library-level sorting preference.

The new album and year sorting preferences are included in Backup & Restore. Older backups receive stable defaults when imported.

## Album Artwork in Menus

Album artwork is now displayed on the left side of song lists and on representative rows for albums, artists, genres, years, playlists, and audiobooks. Queue entries and filtered library views use the same artwork path.

The existing artwork rules still apply: embedded artwork is preferred, followed by supported external cover files such as `folder.jpg`, `folder.jpeg`, `folder.png`, `cover.jpg`, `cover.jpeg`, and `cover.png`.

The Y2 has limited CPU and memory, so list artwork is deliberately bounded:
  - only rows currently visible on screen are scheduled;
  - images are decoded at thumbnail size through the shared artwork cache;
  - visible requests are processed in a controlled sequence;
  - requests are cancelled when rows move offscreen, the screen changes, or the view is hidden;
  - stale results are rejected if the library or source file changed;
  - missing, unavailable, blank, oversized, or damaged artwork is ignored safely.

Album track lists continue showing track numbers instead of thumbnails, preserving the most useful information for ordered album playback.

## Better Audiobook Separation

Files stored under `AUDIOBOOKS` remain fully available through the dedicated Audiobooks section, including chapters, resume progress, and queue continuation.

They are no longer mixed into the music-facing Songs, Albums, Artists, Genres, Years, Favorites, Recently Played, Folders, playlists, track counts, or Shuffle All views. This keeps audiobook chapters from appearing as ordinary songs while preserving their dedicated playback behavior.

The circular menu for an audiobook chapter is also more focused. It contains Chapters, Queue, Sleep Timer, and Track Details instead of music-only actions such as Shuffle, Repeat, Favorite, and Add to Playlist.

## Repeated Vorbis Artist Values

Ogg Vorbis and Opus files can store several `ARTIST` comments. FFmpeg exposes repeated values as one semicolon-separated string, which Y2Player previously treated as a single artist name.

Repeated values are now parsed into individual artist entries. Feature-credit parsing still applies, duplicate names are removed case-insensitively, and the complete original credit remains available for display and playback metadata.

## Internal Cleanup and Validation

Version 2.3 also removes unused fields, counters, wrappers, and duplicate state from the device, display, diagnostics, playback, queue, backup, and playlist code. Media-key classification is shared between the hardware gate and broadcast receiver, and several result objects that carried values no caller used have been simplified.

These changes are maintenance rather than feature removal. The updated code and new visible-row artwork planner are covered by the complete debug unit-test suite.

## Installation

The release provides the existing system-only update path as well as a complete `rom_y2.zip` package for the Innioasis Updater.

For the system-only method, use SP Flash Tool in Download Only mode with only the ANDROID partition selected, pointing to the supplied `system.img`. Do not select or format any other partition.

The `rom_y2.zip` package performs a full-device installation and erases user data. Create a Y2Player backup and copy important media, exports, and other files off the device before using the full-ROM method.

Verify the supplied checksums and read the complete installation guide in the repository before flashing either package.

## Reporting Bugs

If you encounter a problem, enable verbose diagnostics first:

Settings → System → Diagnostics → Verbose Diagnostics

Reproduce the problem, then export the report:

Settings → System → Diagnostics → Export Diagnostics

Please attach the exported report to a GitHub issue. For queue problems, include the collection that started playback, the queue action used, and whether Shuffle or Repeat was enabled. For artwork problems, mention whether the cover is embedded or external and include the external filename where applicable.

Thank you to everyone who reported the queue, metadata, audiobook, browsing, and menu-artwork issues that shaped this release.

These are Y2Player's own instructions, shown here word for word.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
