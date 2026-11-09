---
title: "Y2Linux 1.0 Beta 8.33 (Baseline 134) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.33 Baseline 134 Status: PUBLISHED as GitHub release baseline-134 2026-10-24, installed on the owner's player before publishing. Release 1.0.0-beta.8.33"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.33.html"
---

# Y2Linux 1.0 Beta 8.33 (Baseline 134) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.33 (Baseline 134)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.33 (Baseline 134)

Status: PUBLISHED as GitHub release `baseline-134` (2026-10-24), installed on the owner's player before publishing. Release `1.0.0-beta.8.33`, Reborn `1.0.0-beta.8.33`, kernel `6.18.56-y2linux-1.0.0-beta.8.33`, update sequence 9702, root `2026.08-platform-v1.176`, Linux `0caf312`, Reborn `eca7f49`. Built with `tools/production/release.py` (146 s, resumed workspace, update based on `baseline-130`): container suite 881 OK; Reborn workspace tests, `clippy -D warnings` and `fmt --check` clean; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.33 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

Beta 8.32 was never published: its test builds (labels 131, 132: the search overhaul) went to the owner's player only. Label 133 (sequence 9701) was the first queue build; 134 adds one fix found on the device. Everything since Beta 8.31 is in this release.````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 4e419a581c0560a794c25ef98e90d044657da728e6a9cfe7903f799d1b54bb24 |
| Y2ROOT | 5846674dd75ec56e4b0d6791d0cd7953631380bb13a5571ea7f3b707255c441f |
| RECOVERY | 2f790a4678e3569a11259de5b4cf8386af1fe9805266775e0f8ba59653c15895 |
| Y2DATA (no SSH key) | 4477940e8dd37d32c4fde30ff19ceb305d5907281e0925260ea2fda73d217377 |

## Why

The owner: the search "looks good but navigation wise it's a little tricky and also has some visual glitches"; then an assessment and redesign of the play queue. User requests behind the queue work: Y2Linux #60 (Up Next keeps played songs), Y2Reborn #31 (Play Next / Add to Queue for an album), #32 (move with the wheel, multi-select in the queue), #26 (multi-select). Also Y2Reborn #38 / Y2Linux #40 (one album listed under each artist of a joined tag).

## What changed since Beta 8.31``````````````````````````````````````````````

| Change | Detail | Evidence |
| --- | --- | --- |
| Search: one page | Search is a page with the keys over it. The first three results show above the keys as you type; Up from the top key row, a turn of the wheel or Search folds the keys away (180 ms, on a panel of their own) and the focus lands on the first result. Artists, Albums, Audiobooks and Songs under headings that are not stops, Play All above the songs. Select on the field brings the keys back; Cancel restores the search. Back from a result returns to the page as left. Audiobooks match word beginnings like music | Reborn 512a5f3, fdfa148; tests the_search_page_*, the_search_folds_*; device test on build 131/132 |
| Search glitches | The live result focus no longer covers the scroll rail; the count no longer crowds long text out of the field; typing no longer slides the screen; round artist covers keep the right corner colour while the focus glides (Moving::Corners, also in Artists); the field keeps one width | same |
| Queue model | Your queue plays first: Add to Queue goes after the songs you queued, before the rest of what plays (it went after up to 5 000 songs of All Songs); Play Next goes on top (newest first). The source keeps its order and name (Up Next: "Next from Night Drive") | Reborn 8f7de2c; reborn_core::queue tests (10) |
| No restart on queue edits | Play Next, Add to Queue, Remove, Move, Clear, Shuffle and Repeat used to reload the song (decoder restarted from the last reported position) only so the gapless pre-open learned the next song. Playback::set_upcoming now hands the running decoder the next 32 songs; it reopens the next song only when it changed | a_new_upcoming_list_changes_the_next_song_without_a_restart; device: decoder generation unchanged, position continuous |
| Next / Previous at the ends | Repeat All: Next on the last song starts over (it stopped), also gapless; your queued songs that played leave then. Previous on the first song restarts it (it stopped) | queue tests; device |
| Shuffle while playing | On: the rest of what plays shuffles (your queue stays); off: back to its own order, continuing after the song it is at. A queue restored from an 8.32 session (no order saved) restores the order Shuffle found | queue tests; device (the off case was the fix in 134, eca7f49) |
| Up Next | Opens on the song playing; HISTORY (last 50, kept across restarts) above, QUEUE and NEXT FROM below, headings with counts. Select plays (a history song plays now). Hold Select: Play Next, Move (the wheel carries it, into or out of your queue), Remove, Select Songs…, Add to Playlist…, Go to Album, Clear Queue / Clear Upcoming | up_next tests, UI tests; previews 17–17f; device |
| Select Songs | Up Next, Songs, album pages and search: tick songs, then Play Next, Add to Queue or Remove, Add to Playlist… | select_songs_chooses_rows_then_acts_on_them_together; device (remove two) |
| Queue a whole group | Albums (grid and Cover Flow), artists, genres, folders and the search's Play All: Play, Shuffle, Play Next, Add to Queue, Add to Playlist… in the hold menu; toasts confirm | albums_artists_genres_and_search_results_queue_as_a_whole; device (Cover Flow) |
| Now Playing | A NEXT line under the status icons; the menu's Up Next row names the next song | previews 14, device |
| Session schema 3 | Library songs saved by reference ({"ref":[source,path,id]}, filled from the library when it loads): a 313-song queue is 59 KB (≈190 B per song, was ≈820). Older sessions read as before. The platform's settings reset accepts schema 3 and keeps the queue as read | Linux 93d3652 (test_settings_reset_keeps_a_schema_3_queue_of_song_references, check_installed_arm.py); device restore after restart |
| Artists of joined tags (#38, #40) | "A;B" and "A feat. B" file a track under each name; an artist page lists an album once; "1 song" | Reborn 0d4e2fd |
| rebornctl action NAME | One UI action as a button gives it (context_menu = hold Select, home = hold Back, wheel_down/up), for device tests: injected key presses cannot hold, the button driver re-reports the real state after ≈30 ms | Reborn eae392b |

## Device results

| Check | Result |
| --- | --- |
| Install by OTA staging (owner's player) | builds 131, 132, 133, 134 each Acknowledged after a normal update restart |
| Search (131/132) | open, type, fold by Up/wheel/Search, headings skipped, fast spin 0 missed frames, field → keys rise, Cancel restore, artist → Back keeps focus, Play All, audiobooks, empty and no-match states |
| Add to Queue while playing (133) | decoder generation 1 before and after, position 247.7 → 248.3 → 250.0 s; the queued song played next, gapless |
| Up Next (133) | opens on the song playing, history above, Move into the queue (two detents), Select Songs + remove two ("2 songs removed"), all without a restart |
| Shuffle on / Repeat All / Previous (133) | Shuffle on reshuffled the rest, your song first, no restart; Next on the last song wrapped; Previous on the first restarted it |
| Groups and history (133) | album hold menu in Cover Flow → Play, source "Afterglow"; a history song played now |
| Schema 3 restore (134) | 313-song queue restored after the update restart, details from the library ("Waves — Glass Avenue"); 0 warnings, healthy |

## Open
  - Held buttons on the real hardware (hold Back to leave the keys, hold Select menus, Move feel on the wheel) were

driven through `rebornctl action`, not by hand.
  - Skins draw Up Next and Select Songs ticks through their list layouts; the "Moving" / "N Selected" titles are

Reborn's own look only.
  - Going back to a version older than 8.33 starts with an empty queue (schema 3 is refused; settings are kept).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
