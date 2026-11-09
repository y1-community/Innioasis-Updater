---
title: "Y2Linux 1.0 Beta 8.16 (Baseline 113) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.16 Baseline 113 Status: PUBLISHED as GitHub release baseline-113 2026-10-20. Release 1.0.0-beta.8.16 , Reborn 1.0.0-beta.8.16 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.16.html"
---

# Y2Linux 1.0 Beta 8.16 (Baseline 113) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.16 (Baseline 113)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.16 (Baseline 113)

Status: PUBLISHED as GitHub release `baseline-113` (2026-10-20). Release `1.0.0-beta.8.16`, Reborn `1.0.0-beta.8.16`, kernel `6.18.56-y2linux-1.0.0-beta.8.16`, update sequence 8000, Linux `342a130`, Reborn `eea9312`. Built with `tools/production/release.py` (131 s, resumed workspace, update based on `baseline-112`): container suite 842 OK, Reborn workspace tests, Clippy `-D warnings` and rustfmt clean; all seal checks PASS, no MediaTek firmware in any image. Not installed on a player before publishing; the owner updates by OTA, and the reporting user (28 600 songs) tests the scan. Milestone audit BETA-8.16 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 5c0b45d965ac230ddaaa779c1246eb2e23974a4c79588ad90fc266dab56a6cd4 |
| Y2ROOT | 6897c56c9f94121f1ffa5fff5564c96a7e38ce38f1d1455788e6eec4db6285aa |
| RECOVERY | 8b61768be6aad8cb509019d953de47a17f12c1690ee4221b687a6ba5e4f9fcda |
| Y2DATA (no SSH key) | a63d638c389c866bc15d6515acc668c0a8b7285ac5262b47fe27e54e8332857c |

## The report

User with 28 600 songs on a 512 GB card (install 03df8d42, report 9765e1e7, Beta 8.14): "Couldn't complete that" for any song from All Songs, and a first scan of "10 to 15 minutes".````````````

| Finding | Evidence |
| --- | --- |
| Every play from All Songs refused | 17 × invalid queue bounds: MAX_QUEUE 20 000 < 28 600. A saved queue is ≈ 500 bytes per song in a session capped at 8 MiB, so more than ≈ 16 700 songs never saved either |
| Scan time | Full scan 757.8 s (12 890 files read, 15 710 reused): database 504.7 s, FFmpeg open 190 s, probe 30.5 s, 3.6 GB read. The scan right after, nothing changed: 759.2 s, of which database 749.2 s — and that scan runs at every start |
| Cause of the database time | The scan probe's INSERT … SELECT … WHERE t.id IS NOT NULL over scan_candidates ⟕ tracks is planned as SEARCH t USING INDEX (source_id=?) then SCAN c: every track of the source per 64-file batch (1.7 s per batch on the player, 447 batches) |

## What changed since Beta 8.15``````````

| Part | Change |
| --- | --- |
| Queue | MAX_QUEUE 5 000 (≈ 2.5 MB session). A larger collection plays as a window around the chosen song (a tenth before it); Shuffle takes a random 5 000 of the whole collection; positions are chosen before any song is copied; a saved queue over the limit is trimmed around the current song instead of rejected (Reborn 122607f) |
| Scan probe | Matching track ids come from the indexed lookup itself and are inserted into scan_seen by id. Host benchmark at 28 600 tracks: 54.7 → 0.08 ms per 64-file batch (Reborn 5c7e768) |
| Tag reading | New and changed files are read on up to 3 worker threads (cores online under the LibraryScan lease, one left for UI and playback), nice 10, results applied in file order; panics stay isolated per file. Host: 3.3× faster for 600 files (Reborn 4922cab) |

## Expected on the reporting player (not measured yet)

A rescan with no changes: seconds of database work plus walking the folders, instead of 12.7 min. A first scan of a new 28 600-song library: the 8.4 min of database time gone, and the tag reading spread over three cores (the SD card's read speed now sets part of the pace).

## Known gaps
  - Not run on a player before publishing; the scan timing on the reporting player is the check.
  - A shuffle of everything plays 5 000 songs, then stops until Shuffle is pressed again.
  - Unchanged: codec choice while connecting not checked on a player, A7 glyph timing, USB DAC hardware check, video not

for 1.0, Strawberry itself not run, slow crystal, sleep with a parked CPU, #47, WAF rule and billing alert, #42, #45.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
