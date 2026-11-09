---
title: "Y2Player V2.2 - Innioasis Updater"
description: "Y2Player v2.2 - Interface Redesign, Audiobooks, and Library Browsing Version 2.1 focused on the library scanner and media engine. Version 2.2 is all about the user experience. The"
language: "en"
source: "https://innioasis.app/release-notes/y2player-y2/releasev2.2.html"
---

# Y2Player V2.2 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

Firmware release notes · Y2Player · Y2

# Y2Player V2.2

A Y2 custom Software.ReleaseV2.2Y22026-08-01[schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=y2player-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

system.zip[system.zip 215 MB](https://github.com/SchulzCode/Y2Player/releases/download/ReleaseV2.2/system.zip)

# Y2Player v2.2 - Interface Redesign, Audiobooks, and Library Browsing

Version 2.1 focused on the library scanner and media engine. Version 2.2 is all about the user experience. The biggest additions are proper audiobook support and a redesigned menu system, alongside improvements to artist and album browsing, confirmation prompts for destructive actions, and a cleanup of comments throughout the codebase.

## Row Icons

Menus now use a much larger and more consistent icon set, with 47 icons in total.

These aren't image assets. Every icon is drawn using strokes on a single shared `Path` and `RectF`, both of which are reused for every menu row. Nothing is decoded, cached, or allocated while scrolling, so the new icons come at essentially no runtime cost.

## Audiobooks

Audiobooks are now a dedicated section on the main menu instead of something you have to reach through the folder browser.

Any audio files stored inside a folder named `AUDIOBOOKS` are automatically grouped into books. Common folder names such as `Disc 1`, `CD2`, or `Part 3` are collapsed into the parent book, so multi-disc audiobooks appear as a single entry.

Each audiobook now has its own menu with:
  - Chapters
  - Start from Beginning
  - Clear Progress

When clearing progress, the player tells you exactly which chapter's position will be forgotten and asks for confirmation before doing so.

## Menu Ordering

Almost every menu has been reorganized with one simple goal: the options you use most often are now at the top, while reference and maintenance screens are moved toward the bottom.
  - Settings now opens with Bluetooth, followed by Audio, Interface, Library, and System.
  - Music starts with Shuffle All and Songs, followed by Albums, Artists, Playlists, and finally Folders.
  - System now ends with About, with Diagnostics and Reset placed just above it.
  - Now Playing opens with Shuffle, Repeat, and Queue so the playback controls are immediately visible.
  - Track Options now begin with Play Next and Add to Queue instead of Browse Track and Track Details.

Destructive actions have also been moved beneath the actions they're related to. For example:
  - Clear Progress is below Start from Beginning.
  - Remove is below Play Now.
  - Reset sits just above About.

Several menu labels were also shortened to fit the Y2's 480-pixel display more comfortably.
  - Previous Restarts Track → Previous Button
  - Hold Seek Step → Seek Step When Held
  - Import/Export M3U Playlists → Import/Export Playlists
  - Sound Effects (toggle) → Audio Effects

The Favorite menu item now keeps a fixed title, with its enabled state shown in the subtitle. This matches how Shuffle, Repeat, and Theme already behave and prevents the label from constantly changing length.

## Confirmation for Irreversible Actions

Y2Player has six actions that cannot be undone:
  - Forget Bluetooth Device
  - Clear Audiobook Progress
  - Clear Queue
  - Reset Library
  - Clear Listening History
  - Delete Playlist

Previously, Delete Playlist, Clear History, and Clear Queue executed immediately with a single button press.

All six actions now use the same confirmation screen. The confirmation clearly states what will happen, and Cancel is selected by default so the destructive option is never under the cursor when the dialog opens.

A static validation also ensures these six operations can only be triggered through their confirmation screens, preventing future changes from accidentally introducing a one-click destructive action.

## Artist and Album Browsing

Artist and album browsing has been completely reworked to properly support featured artists.

Previously, albums were grouped using the raw `artist` tag, even though the `albumArtist` tag was already scanned, stored in the database, and available. It simply wasn't being used.

For example, if one song on an album was tagged as `Daft Punk feat. Pharrell Williams`, the player would:
  - create a separate artist entry named `Daft Punk feat. Pharrell Williams`;
  - show only twelve tracks instead of thirteen under Daft Punk;
  - completely hide the featured track when opening the album through the artist view.

Albums are now grouped using the `albumArtist` tag first, which is exactly what it was designed for. Albums and compilations remain intact without relying on fragile string parsing.

Featured artists are then added separately using a conservative parser. It only splits on explicit feature markers:
  - `feat.`
  - `feat`
  - `ft.`
  - `ft`
  - `featuring`
  - bracketed `with`

Each marker is matched as a complete word. It intentionally ignores characters like `&`, `,`, and `+` because they appear in legitimate artist names such as Simon & Garfunkel, Earth, Wind & Fire, and Florence + the Machine. A plain `with` is also ignored to avoid incorrectly splitting names like Sleeping with Sirens.

Since the Y2 has no built-in tag editor, preserving existing metadata is much safer than trying to aggressively interpret it.

The end result is:
  - featured artists now appear in their own artist entries;
  - selecting that artist shows the albums they appear on, with the album's primary artist displayed underneath;
  - opening the album shows only the tracks they contributed to.

The full artist credit is still shown on the Now Playing screen, notifications, and in exported M3U playlists.

`Various Artists` is no longer treated as a standalone artist. Only performers that actually appear on individual tracks receive their own artist entry.

## Collection Shuffle

Version 2.1 introduced per-collection Shuffle actions for Songs, Favorites, Recently Played, artists, and playlists.

Albums now support this as well, with a Shuffle option automatically added as the first row whenever an album contains more than one track. Single-track albums do not display the option since shuffling would have no effect.

## Additional Metadata

A new Additional Metadata option has also been added to Settings.

When enabled, Y2Player displays extra information throughout the interface where available, providing more detailed information about your music library without affecting the default, cleaner layout for users who prefer it.

## Navigation

Pressing and holding the Play/Pause button from anywhere within the menus now jumps directly back to the Now Playing screen.

## Scrobble

Y2Player can now export your listening history, making it easy to keep a record of the tracks you've played.

## Also useful
  - [Install guideStep-by-step install for Y2Player](../../guides/y2player-y2.html)
  - [Y2Player V2.5Release2.5 · 2026-09-04](../../release-notes/y2player-y2/release2.5.html)
  - [Y2Player V2.3ReleaseV2.3 · 2026-08-15](../../release-notes/y2player-y2/releasev2.3.html)
  - [Y2Player V2.2.2RealeaseV2.2.2 · 2026-08-10](../../release-notes/y2player-y2/realeasev2.2.2.html)
  - [Y2Player V2.2.1 ReleaseV2.2.1 · 2026-08-03](../../release-notes/y2player-y2/releasev2.2.1.html)
  - [Y2Player V2.1ReleaseV2.1 · 2026-07-29](../../release-notes/y2player-y2/releasev2.1.html)
  - [Y2Player 2.0 Complete Media Engine RewriteReleaseV2.0 · 2026-07-27](../../release-notes/y2player-y2/releasev2.0.html)
  - [Y2Player V1.2ReleaseV1.2 · 2026-07-26](../../release-notes/y2player-y2/releasev1.2.html)

Notes as published by the Y2Player project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=Y2Player&version=ReleaseV2.2&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
