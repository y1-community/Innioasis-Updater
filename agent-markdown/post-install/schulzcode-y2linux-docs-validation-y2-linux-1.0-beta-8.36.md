---
title: "Y2Linux 1.0 Beta 8.36 (Baseline 138) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.36 Baseline 138 Status: PUBLISHED as GitHub release baseline-138 2026-10-25, installed on the owner's player before publishing. Release 1.0.0-beta.8.36"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.36.html"
---

# Y2Linux 1.0 Beta 8.36 (Baseline 138) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.36 (Baseline 138)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.36 (Baseline 138)

Status: PUBLISHED as GitHub release `baseline-138` (2026-10-25), installed on the owner's player before publishing. Release `1.0.0-beta.8.36`, Reborn `1.0.0-beta.8.36`, kernel `6.18.56-y2linux-1.0.0-beta.8.36`, update sequence 10050, root `2026.08-platform-v1.180`, Linux `8d22ba1`, Reborn `92b9c9a`. Built with `tools/production/release.py` (128 s, resumed workspace, update based on `baseline-136`): container suite 883 OK; all seal checks PASS, no MediaTek firmware in any image. Reborn host tests: 673 passed, strict Clippy clean; Y2Linux host tests 910 OK. Label 137 (sequence 10002, the issue fixes alone) was built and installed on the owner's player but not published. Milestone audit BETA-8.36 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 82961141f371562d8a39aac1fc5dca402de9a3cf28352aea07fa1c569a87e373 |
| Y2ROOT | eb73fcc25da1f9161f358c01371a7103e058be05d5b2b93a1bf828d2e06589e8 |
| RECOVERY | 172f8016d4e7bf10094b89af87c41d682099bd5f66b6452711f57325e8a416f3 |
| Y2DATA (no SSH key) | eec00240c244bffbe4afdeaa24b8b47e90bd08ddb775c3e84fbc60940684a3d9 |

## Why

An assessment of every open GitHub issue (Y2Linux and Y2Reborn) on 2026-10-25: the bugs found in the code, then the owner's request to add the asked-for features without bloating menus, "consistent for the whole UI", with labels that mean what they say. A Reddit user's fresh install showed Couldn't Start and the only log was lost when the player went back to stock.

## Bugs fixed````````````

| Issue | Cause | Fix | Evidence |
| --- | --- | --- | --- |
| Y2Reborn #43: songs without an album show another song's cover in lists | the thumbnail key of a song without an album was its folder (or "" + artist), so such songs shared one cover | the key is the song itself (components::art_key) | test; on device three album-less songs of one folder and artist each showed their own cover |
| Y2Linux #60: in a skin, the playing mark sits two rows above the song playing | skins compared Up Next's row index with the queue position; since 8.33 Up Next has headings and history | compared by the queue entry (Ui::entry_key) | skin test (failed before: row 1 instead of 3); Classic on device |
| Y2Reborn #32: Up Next jumps to the top after Play Next or when a song ends | the focus kept its index; a heading landing there sent it to the first selectable row | the focus follows its song (keep_up_next_focus); otherwise the nearest selectable row | test; the reporter's three steps on device |
| Y2Linux #40: "Jazz;R&B" is one genre, "A;B" shown on album pages | genres were not split; song rows printed the raw tag | split_genres, joined_names ("A, B") | tests; on device |
| Couldn't Start left no log a user can reach | Reborn's startup log stays on Y2DATA | the screen saves an error report onto Internal Storage (or the SD card) once a boot; USB file transfer runs without Reborn | tests/test_reborn_supervise.py 7/7; on device the report was saved, seen and copied over MTP |

## One menu order and Customize (owner request)``

| Change | Detail |
| --- | --- |
| One order | Every song and collection menu: Play, Shuffle · Play Next, Add to Queue · Move, Remove from … · Add to Favorites, Add to Playlist… · Go to Album, Go to Artist · Select Songs…. Rows that would change nothing are left out (test every_menu_lists_its_shared_actions_in_one_order) |
| Up Next | Add to Queue for a song or chosen songs (end of your queue, Y2Reborn #26/#32), Go to Artist; the song playing holds Save Up Next as Playlist… (from Now Playing, now 8 rows), Clear Queue, Clear Up Next |
| Playlists | Play and Shuffle in a playlist's hold menu |
| Customize | Home Menu, Cover Flow On/Off (albums and audiobooks, Y2Reborn #36/#37), Artists All / Album Artists (Y2Linux #41), Now Playing Wheel Volume / Seek (Y2Reborn #34; steps as holding Previous/Next, stations keep volume), Wrap Around, When Screen Off |
| Albums from a genre | show that genre's songs, "Jazz · 2 of 3 songs", last row Show All 3 Songs (Y2Linux #50) |
| Values fit | a menu value uses the room its label leaves: the Up Next row names the whole next song (Y2Linux #60), in skins too |

Spec: Y2Reborn `docs/ui/REBORN-PRODUCT-UI-V4.md` (last section). No kernel, platform API, memory map, partition or packaging change; the settings gain two fields with defaults (session schema unchanged).

## Device results (owner's player, builds 137 and 138)``

| Check | Result |
| --- | --- |
| Install by OTA staging | 10002 and 10050 Acknowledged, healthy, library unchanged |
| Covers (#43), genres and commas (#40) | test folder: own covers, "Y2Jazz" and "Y2Soul" split, "Y2 Test A, Y2 Test B" |
| Up Next focus (#32) | Play Next with an empty and a non-empty queue, a song ending: the focus stays on the song |
| Playing mark (#60) | Classic skin: on the song playing, also after Play Next |
| Couldn't Start report | five forced failures: screen shown, report Error Reports/y2linux-report-… with the failure line, listed and copied over MTP (identical) |
| Customize | six rows; Cover Flow On and Wrap Off kept from the owner's settings |
| Album Artists | 53 artists, a compilation once, its page named after it |
| Genre album | "Y2Jazz · 2 of 3 songs", Show All opens the three |
| Wheel seek | paused: five detents +5.0 s, two back −2.0 s; volume unchanged |
| Menus | Now Playing names a 60-character next title whole; Up Next song and playing menus as specified; Add to Queue toast |
| Audiobooks | Cover Flow over the owner's six books |

## Open
  - Haptic feedback (Y2Reborn #28) needs a Linux driver for the vibration motor (PMIC VIBR) first.
  - The Up Next preview does not scroll (it uses the row's room instead; a moving line would keep the screen drawing).
  - Bluetooth (AVRCP) and Last.fm still get a joined artist tag as tagged.
  - Songs deleted while queued stay in Up Next until the queue changes.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
