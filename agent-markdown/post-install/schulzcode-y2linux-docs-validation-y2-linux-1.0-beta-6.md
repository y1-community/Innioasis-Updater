---
title: "Y2Linux 1.0 Beta 6 (Baseline 57) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 6 Baseline 57 Status: PUBLISHED as GitHub release baseline-57 2026-10-15. Release 1.0.0-beta.6 , Reborn 1.0.0-beta.6 , kernel 6.18.56-y2linux-1.0.0-beta."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-6.html"
---

# Y2Linux 1.0 Beta 6 (Baseline 57) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 6 (Baseline 57)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 6 (Baseline 57)

Status: PUBLISHED as GitHub release `baseline-57` (2026-10-15). Release `1.0.0-beta.6`, Reborn `1.0.0-beta.6`, kernel `6.18.56-y2linux-1.0.0-beta.6`, update sequence 5600, Linux `45d3696`, Reborn `544d3c9`, git tag `baseline-57` in both repositories. Built with `tools/production/release.py` (`--public`) in 120 s: container suite 740 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-6 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | ed0db4a0eddd18c292e8efc661722c5ff0006c6c39acb9ce298db877b33cb575 |
| Y2ROOT | 48d3da384daf2fa2518cf095122bfeffe56471a1fa541997bb7344b70d2ab051 |
| RECOVERY | 1a804133a99adb80d12fa033a1260093bbb27a20c89716f162738d8c077837d5 |
| Y2DATA (no SSH key) | d8a39666c1d1cf2da9ceb7197175196ae7791d6372d1f036199cf33a974aa31b |

## Since Beta 5.1 (Reborn)``

| Part | Detail |
| --- | --- |
| Playlists | Owner: a playlist feature like Y2Player's, its own section, add/remove on the device, optimized, fixing Y2Player's issues. The .m3u/.m3u8 file is the playlist (no database copy): found anywhere on Internal Storage and the SD card (not Radio/hidden/system folders), read in UTF-8, UTF-8/16 with BOM or Windows-1252 and written back in kind, comments/tags/missing entries kept, atomic writes, each edit checked against a fresh read. Entries by place (duplicates, one removed at a time). Paths from computers (Windows, macOS, Linux, file://) matched in memory by their ending. Section with mosaics, Favorites with a heart, Move with the wheel, picker, rename/duplicate/delete, Save Queue as Playlist. 20 000 entries: 19 ms first open on the host, 0.3 µs per frame. |
| Pause in place | Owner: "pausing and playing again … will always buffer". Beta 5.1 log: pause closed the BlueALSA PCM, play reopened file, seek and PCM (≈1.3–1.4 s). Now the pipeline holds (device paused via snd_pcm_pause, else drop/prepare; decoder waits with its heartbeat), resume instant; released after 3 min, before sleep, by any stop/start. Wired and Bluetooth. Stations still stop (live). |
| Seeking | Owner: "scrolling right and left also gives an error" (hold Previous/Next: a restart per 90-ms step → "audio reconfiguration is still pending"). Steps now move the position while the sound holds; one restart 350 ms after the last step. |

Host evidence: 460 Reborn tests (playlist files, encodings, path styles, edits vs computer edits, worker, UI flows; a held pause writes nothing and never reopens the device), strict Clippy, fmt; previews 80–87. Image check: the new pause and playlist code is in the built Reborn.

## Device checks owed (after the owner's over-the-air install)

Pause/play continues at once (Bluetooth and wired; the `alsa paused` log line says whether the device paused itself); holding Previous/Next scrubs without errors; Playlists: a computer's playlist opens and matches, New Playlist, Add to Playlist, Move, Remove, Favorites heart, rename/delete; files stay readable on the computer afterwards.

## Known gaps

FM radio (next beta); HLS stations; sleep ≈9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection; a seek still restarts playback (≈1 s on Bluetooth).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
