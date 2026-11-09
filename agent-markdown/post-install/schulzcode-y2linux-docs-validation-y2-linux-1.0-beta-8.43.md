---
title: "Y2Linux 1.0 Beta 8.43 (Baseline 164) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.43 Baseline 164 Status: PUBLISHED as GitHub release baseline-164 2026-10-28 at the owner's word"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.43.html"
---

# Y2Linux 1.0 Beta 8.43 (Baseline 164) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.43 (Baseline 164)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.43 (Baseline 164)

Status: PUBLISHED as GitHub release `baseline-164` (2026-10-28) at the owner's word ("publish and answer the issues"), after test build 164 on the owner's player (the published images). Release `1.0.0-beta.8.43`, Reborn `1.0.0-beta.8.43`, kernel `6.18.56-y2linux-1.0.0-beta.8.43`, update sequence 11000, root `2026.08-platform-v1.206`, Linux `f5529b7`, Reborn `a08ca5d` (fixes `2eada03`). Built with `tools/production/release.py` (resumed workspace, update based on `baseline-163`): container suite 926 OK, host suite 953 OK (one load-sensitive report test passes alone), Reborn 729 tests, clippy and rustfmt clean; all seal checks PASS, no MediaTek firmware in any image. Reborn only: the platform changes the version. Milestone audit BETA-8.43 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | ea43cb5e7f040044f612f33233af4deac64a142d35137b6772bab4004e5614ea |
| Y2ROOT | 457b9786081525472c220f7c1057f1837e51fb2e564063a265b8aec3740786b3 |
| RECOVERY | d32f676e75a2dc648d2e6422759e8690d127ab39e110451c5684ffae1fdd7fb8 |
| Y2DATA (no SSH key) | 7be89b3edf0e5bd668b146a39b2aa6d38f15df52017007d6673971517c456065 |

## What changed since Beta 8.42 (Y2Reborn issues)``````````````

| Issue | Change | Evidence |
| --- | --- | --- |
| #51 | Cancel on the search keys always leaves Search (with or without text) to the screen it was opened from; a held Back while typing leaves too, also when its press already folded the keys into Results (the router remembers the Back press); the dead keyboard Leave path is gone | routed tests app/reborn/tests/search_keys_route.rs |
| #45, #46 | reborn_core::albums::unify_album_artists on the library thread: within one storage, folder and album title, songs without Album Artist take the album's single Album Artist (case and spaces ignored); compilations and two-artist albums stay; Last.fm keeps the song's own tag | 4 unit tests (Discovery, compilation), UI test |
| #52, #55 | Settings::home_hidden: Customize › Home Menu hides Music, Playlists, Radio, Search; Now Playing and Settings stay; hidden Playlists/Search at the end of Music | owner's player: Radio hidden and shown again |
| #60, #25 | QueueOrigin: the Go to Album row of Now Playing's menu becomes Go to Playlist/Folder/Search/Genre/Songs; no row added; old sessions keep Go to Album | owner's player: fallback for an old queue; UI tests |
| #57 | skin remap recolours gradient (warp) corners, so Cover Flow's shelf fades into the skin's background | skin test with a white background |
| #56 | AlbumOrder Title / Artist, Customize › Album Order (new row); the letter follows | owner's player: row present |
| #30 | a fast wheel steps letter by letter in Songs, Artists, Albums, Folders while the letter shows (700 ms linger) | UI tests |
| #62 | "Headphones unplugged. Playback paused." when an unplug pauses | owner's player: toast and pause in place |
| #28 | haptic tick on a computer connecting and on held seek steps (at most every 300 ms); no wheel ticks | unit tests |

## Open
  - By hand on a player: letter-scroll feel, USB and seek ticks, leaving Search, the shelf in Bunny Bow/Cassette/Mini

Blue, Go to Playlist after starting a playlist.
  - Everything open after Beta 8.42 (its report's Open section).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
