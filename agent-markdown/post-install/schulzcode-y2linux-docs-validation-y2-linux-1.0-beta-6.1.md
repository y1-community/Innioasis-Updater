---
title: "Y2Linux 1.0 Beta 6.1 (Baseline 58) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 6.1 Baseline 58 Status: PUBLISHED as GitHub release baseline-58 2026-10-16. Release 1.0.0-beta.6.1 , Reborn 1.0.0-beta.6.1 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-6.1.html"
---

# Y2Linux 1.0 Beta 6.1 (Baseline 58) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 6.1 (Baseline 58)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 6.1 (Baseline 58)

Status: PUBLISHED as GitHub release `baseline-58` (2026-10-16). Release `1.0.0-beta.6.1`, Reborn `1.0.0-beta.6.1`, kernel `6.18.56-y2linux-1.0.0-beta.6.1`, update sequence 5650, Linux `faf85ba`, Reborn `78e36db`, git tag `baseline-58` in both repositories. Built with `tools/production/release.py` (`--public`) in 124 s: container suite 740 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-6.1 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 1f9bdf14e1e9cdda3230a37cb2e7cc207d37b257d80d8f8165bbe9aced5b85d5 |
| Y2ROOT | ed5a1a230c112d29a28d026595f310b1507b89a4742f24e4d0f491f806e6605f |
| RECOVERY | 73574518c7e907be99085cab14ec97226d931d23bf5645616573425bb997590a |
| Y2DATA (no SSH key) | 7e4ef50f972f21781e263d9b787f9728656674f3823bcf32eb1025ceb4bbc6dd |

## Since Beta 6 (Reborn)

Owner (2026-10-15): "when i pause and resume now it works without buffering but no soudnd on resume"; "throws and error when i scroll left or right with could not complete that"; review of the day's changes for performance and duplicated code; and Y2Reborn issue #15 / PR #14 (samanz) "yes do both … review the pr before merging".``````````````

| Part | Detail |
| --- | --- |
| Bluetooth pause | Device log: pause in place used BlueALSA's snd_pcm_pause (device_pause: true); after resume the position advanced but the AirPods stayed silent. rb_sink_pause(s, on, device_pause): a bluealsa: PCM drains on pause (non-blocking) and is dropped/prepared on resume, as a start does; other PCMs keep the device pause. |
| Skipping while a song starts | with_model_action refused every action while a start was pending (≈1.1 s on Bluetooth): "Couldn't complete that". Next/Previous during a pending start now step the queue, hold output and restart once the pending start ends (seek_until); Play/Pause pauses, keeping the chosen song (an output or codec change still restores what worked). |
| SD card duplicates (#15) | Card source ids gained the CID; libraries from an earlier image kept the card under the bare uuid: id as well (owner's device: 2 rows; reporter: 5 830). A complete, identity-checked scan of the card marks rows under its bare id (offline, same root) deleted in the scan's finish transaction; ids with another CID are other cards and stay. |
| Playlist matching (#14) | samanz's PR merged after review: the path index takes songs on the player first and keeps a path once, so an entry finds the playable copy. Conflict with the review commit resolved; insert through one hash-map entry. |
| Review of Beta 6 | Failed station logos no longer redraw every frame; playlist facts cached per file and library; one atomic writer (hidden temporary) for favorites, logos and playlists; shared list helpers; flaky stream test serialised. Previews pixel-identical (0 of 327). |

Host evidence: 464 Reborn tests (new: pre-CID copy retired, duplicate library resolves to the online copy, failed logo never asked again, Windows-encoded station lists), strict Clippy, fmt; 767 Y2Linux host tests.

## Device checks owed (after the owner's over-the-air install)

Pause and Play on AirPods give sound again; Next/Previous right after starting a song skip without an error; Play/Pause during a start pauses on the chosen song; the library has no second copy of SD songs after the first scan.

## Known gaps

FM radio (next beta); in-place decoder seek (≈1 s on Bluetooth); sleep ≈9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
