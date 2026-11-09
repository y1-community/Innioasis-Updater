---
title: "Y2Linux 1.0 Beta 8.19 (Baseline 118) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.19 Baseline 118 Status: PUBLISHED as GitHub release baseline-118 2026-10-21. Release 1.0.0-beta.8.19 , Reborn 1.0.0-beta.8.19 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.19.html"
---

# Y2Linux 1.0 Beta 8.19 (Baseline 118) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.19 (Baseline 118)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.19 (Baseline 118)

Status: PUBLISHED as GitHub release `baseline-118` (2026-10-21). Release `1.0.0-beta.8.19`, Reborn `1.0.0-beta.8.19`, kernel `6.18.56-y2linux-1.0.0-beta.8.19`, update sequence 8302, root `2026.08-platform-v1.146`, Linux `6649c89`, Reborn `da5b777`. Built with `tools/production/release.py` (127 s, resumed workspace, update based on `baseline-114`): container suite 857 OK, host suite 884 OK, Reborn workspace tests (608), Clippy `-D warnings` and rustfmt clean, preview GLES comparison 165/165; all seal checks PASS, no MediaTek firmware in any image. **Installed on the owner's player before publishing** (this exact build, Acknowledged; test builds 115–117 before it). Beta 8.18 was built and installed for testing but never published: everything in it is part of 8.19. Milestone audit BETA-8.19 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 5ab70169b9718c3c4b751a976d32265156f91e46f26484e81600e718e4de1709 |
| Y2ROOT | a7ebe7fee93f06b2dcef3fcdc128f39306ebdc3a39d670c4ef3d25d92a180474 |
| RECOVERY | 71264c4ad14eafad8057cbb0fe1aedda2c44ac2d170d0223a0d337356bb6a803 |
| Y2DATA (no SSH key) | 0a6c1107e1c5ce619cf80d1488d91560b00acc3a5a63b068a50127dfe8f1bead |

## What changed since Beta 8.17````````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FAUDIOBOOKS.md)``````````````````````````````````

| Area | Change | Evidence |
| --- | --- | --- |
| Audiobooks (owner request, after Y2Player's feature) | Home → Audiobooks once the library holds a book (Customize → Home Menu switches it off). A book: an Audiobooks/Hörbücher folder (any case), any .m4b, or genre Audiobook/Hörbuch; CD/Disc/Part n folders fold into their book. List (in progress first, finished last), book page (Continue/Start Over, chapters, time left), hold menu (Continue, Start Over, Mark as Finished, Forget Progress), search results. Books leave every music list, the counts and Last.fm. User guide: Audiobooks | Reborn 11febec…da5b777; plan, code map and device test in Reborn docs/ui/REBORN-AUDIOBOOKS.md |
| Chapters | The files' own chapter marks (MP4/M4B chapter track or Nero chpl, MP3 ID3 CHAP, Ogg) through the new rb_media_chapters, read in the background; else one file is one chapter. Next/Previous move by chapter (Previous restarts after 5 s), Next on the last chapter keeps the place, a held seek steps 10/30/60 s | device: chapters from an M4B, Next/Previous, last chapter |
| Progress | state/books.json (apart from the session and the library database): part, place, finished, speed per book, found again after a rename; saved with every checkpoint; rewind 5/15/30 s by pause length; a finished book starts over | device: resume after a Reborn restart 5 s before the pause (a refresh of the last-listened time at shutdown skipped the rewind in build 117; fixed in da5b777) |
| Speed | 0.75×–2× per book through FFmpeg atempo (no pitch change); positions stay in source time | Y2Linux 01d8882 enables the filter (defconfig, verify-ffmpeg.py); device: atempo=1.50 in the chain, 6.4 s of book in 4 s |
| Sleep timer | 15/30/45/60 min (10 s fade) or End of Chapter/Song, for music too | device: paused at the next chapter's start |
| Long M4B books | A 10.5-h M4B scanned but played nothing and could not seek: FFmpeg's MP4 frame index (24 B/frame, one block) exceeded av_max_alloc(32 MiB). Now 128 MiB (≈36 h of AAC-LC at 44.1 kHz); large MP4s are scanned one at a time | host probe; device: plays, Reborn RSS 92 MB (155 MB at open), 741 MB available, a seek to 9 h 27 min in 2.8 s |
| M4B with a cover video track | refused before (any non-attached video); now in MP4 beside audio the video stream is discarded, never read | fixture test; device: plays |
| Sharper covers | Now Playing/Cover Flow artwork 180×180 (was 160, drawn at 176–180), thumbnails 128×128 straight from the picture, centre-crop instead of stretching, Lanczos with full-resolution chroma, half and quarter copies so no cover is shrunk by more than half on the GPU; thumbnail cache 4:2:0 (24 KB), 3 000 albums, least recently shown removed | Reborn 4895db4; GLES comparison; device screenshots |
| Customize | Settings → Customize: Wrap Around (Off / Menus, default / Everywhere; a fast spin stops at a long list's end), When Screen Off (Locked / Buttons, default / Wheel + Buttons), Home Menu and Album View (moved from Display) | Reborn 820fa50, ad4fdba |
| Headphones while paused | With Bluetooth headphones connected a pause keeps the player awake 15 min, so their play button can continue | HEADSET_PAUSE_AWAKE_SECS |

## Known gaps
  - Car head units without song/artist (owner's car): Reborn's player registers with BlueZ and its metadata matches

BlueZ 5.87's parser; the car's AVRCP traffic is being captured on the owner's player. Not fixed in 8.19.
  - A chapter jump or seek in a very long single-file book reopens the file (≈2–3 s); an in-file seek is a later change.
  - Held seek in a book and the sleep timer's fade were not checked by hand (button holds cannot be injected over SSH).
  - One OTA restart (build 115) took ≈4.5 min to reach the installer and then installed normally; three later installs

were normal (≈70 s). Cause unknown (before Linux runs).
  - After the update every thumbnail is rebuilt once (new cache format); Now Playing's cover appears after Play following

a restart (unchanged behaviour).
  - Unchanged: #42, #45, #47 confirmation, HLS radio, on-device SD repair, WAF rule and billing alert, USB DAC check.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
