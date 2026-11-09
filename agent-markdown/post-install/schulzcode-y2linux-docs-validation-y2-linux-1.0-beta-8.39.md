---
title: "Y2Linux 1.0 Beta 8.39 (Baseline 153) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.39 Baseline 153 Status: PUBLISHED as GitHub release baseline-153 2026-10-26, installed on the owner's player before publishing. Release 1.0.0-beta.8.39"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.39.html"
---

# Y2Linux 1.0 Beta 8.39 (Baseline 153) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.39 (Baseline 153)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.39 (Baseline 153)

Status: PUBLISHED as GitHub release `baseline-153` (2026-10-26), installed on the owner's player before publishing. Release `1.0.0-beta.8.39`, Reborn `1.0.0-beta.8.39`, kernel `6.18.56-y2linux-1.0.0-beta.8.39`, update sequence 10470, root `2026.08-platform-v1.195`, Linux `1c599c5`, Reborn `7cf527d`. Built with `tools/production/release.py` (142 s, resumed workspace, update based on `baseline-146`): container suite 883 OK; all seal checks PASS, no MediaTek firmware in any image. Reborn host tests: 691 passed, strict Clippy clean. Labels 147–152 (sequences 10410–10460) were device test builds. Milestone audit BETA-8.39 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | ea434c43b78d46db1fa3ae7251c153c6befd777d11572327e507d375328730d2 |
| Y2ROOT | b467c78ef69e41bc6b75ecbf03b9cb0c218d62f2c229a85e324d4ba29319ff8e |
| RECOVERY | d658a09e67e14ff4c13e2ebb2026b3d641a31e443b8930efa15fa0bca35767e1 |
| Y2DATA (no SSH key) | c8fe7d3f819081d21980212973e05a665c1500f5dc0ccc7672eb36fbe34a6bed |

## What changed since Beta 8.38

From a user report (Reddit, 2026-10-26): 512 GB SD card, 33 000 MP3s on the way to about 120 000, browses by folder because the folders are tidier than the tags.````

| Change | Detail | Evidence |
| --- | --- | --- |
| Folders as a file manager shows them | A folder lists its folders, then its songs, both by name (case and accents folded, numbers as numbers: "2 - Intro" before "10 - Outro"). Songs show their file name, not the title tag, and are no longer in library order (artist, album), which put a loose "Skydivin' - Darren Styles.mp3" among that artist's songs and a compilation without an album artist in artist order. Picking a song plays that folder's songs in the order shown (it played the whole subtree in library order); Play on a folder plays its folders first, then its songs, all the way down. Storages are titled SD Card and Internal Storage | UI tests (order, labels, queue, group order); previews 13, 13b; on device: Clubland 01, 02, 03 by file name, Next after 02 plays 03 from a 40-song queue |
| Shuffle Off, Songs, Albums | Settings → Playback and Now Playing step through them. Shuffle Albums plays whole albums in random order, each in disc/track/file order; an album is its folder (CD 1 / Disc 2 folders fold into it) and its album tag. Picked with it on, that song's album plays first from that song on; turned on while playing, the album playing goes on. Shuffle Albums is also in the menus of folders, artists, genres, playlists and an artist's Play. Skins get shuffle_albums; older sessions read shuffle as Songs | core tests (whole albums, order, lead song, disc folders, on/off); on device on a 5 000-song queue: 135–278 ms |
| Sort for playlists | Playlist Order, Album, Artist, Title or File Name, in a playlist's menus (and on holding its Play or Shuffle); the page shows and plays in that order, the file keeps its own; kept per playlist; Move only in Playlist Order | UI tests; on device: Sort steps in the open menu, Move hides, the list re-sorts, kept across a restart |
| A 120 000-song library | Measured on the player with 120 829 songs (9 518 albums, 11 760 folders, exFAT card), see below. A folder index per library (each folder's songs, folders and song count), album totals for Cover Flow's album line, Songs/Albums/Artists/Genres kept per library, a menu's song count counted once, cheaper queue building; while the screen is off the long lists, the search index and the playlists' songs are made ahead | device performance traces before/after (below) |
| Playlists without a walk of the card | The library scan keeps the playlist files it meets; Playlists reads those (and each storage's Playlists folder) instead of walking every folder on every visit (94 s on that card), and keeps them across restarts. A playlist copied from a computer shows after the scan that follows the copy, as songs do | worker tests; on device: Playlists in about 1 s, also during the startup scan |

No kernel, platform, memory map, partition or packaging change. Settings gain `shuffle_albums` and `playlist_sort` (older sessions read as before); metrics gain `ui_action_ms` and `ui_layout_ms`.

## 120 000 songs on the player

Synthetic library on the owner's SD card (1-s MP3s at 128 kbps with ID3 tags, compilations without album artist, loose files, CD folders, 4 % untagged; plus 500 full-length 4-min MP3s), timed with Reborn's performance trace.``

| Measure | Result |
| --- | --- |
| First full scan, 120 000 new files | 370 s (325 files/s) |
| Rescan, nothing changed | 88–104 s: walking the card (find alone: 94 s, 70 s of it in the kernel) |
| 500 full-length MP3s | 3.9 ms and 33 KB read each |
| Start with the library | first frame 7.4 s, library ready 13–14 s; Reborn ≈130 MB of 928 MB, database 102 MB |
| Scrolling Songs, Artists, Cover Flow, a folder | 54–73 fps, no frame over 33 ms |
| Opening a folder | 250–380 ms → under 1 ms |
| A whole card's hold menu | 2.2 s a frame → 30 ms |
| Play / Shuffle / Shuffle Albums on the whole card | 4.5–6.6 s, once a playback error → about 0.2 s (1.7 s the first time after a start) |
| Cover Flow spinning | 15 → 71 fps |
| First Songs / Artists / Albums / Genres / Search / Playlists after the screen was off | 0.4–2.6 s → 20–50 ms |
| Playlists | about 90 s every visit → about 1 s |

## Open
  - Lists are made ahead only while the screen is off: browsing right after a start can still take up to about a

second on a list's first opening with 120 000 songs, and a few seconds while the startup scan runs.
  - The test songs were 1 s long; playback was not listened to by ear. Holds were sent with `rebornctl action`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
