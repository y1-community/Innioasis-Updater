---
title: "Release V1.1 - Innioasis Updater"
description: "Changelog 1.1 Fixed - Albums copied from a Mac appeared twice. macOS writes a hidden . Track.flac companion beside every file it copies to the player. These were indexed as tracks,"
language: "en"
source: "https://innioasis.app/release-notes/y2player-y2/releasev1.1.html"
---

# Release V1.1 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

Firmware release notes · Y2Player · Y2

# Release V1.1

A Y2 custom Software.ReleaseV1.1Y22026-07-25[schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=y2player-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

system.zip[system.zip 315 MB](https://github.com/SchulzCode/Y2Player/releases/download/ReleaseV1.1/system.zip)

# Changelog

## 1.1

### Fixed
  - Albums copied from a Mac appeared twice. macOS writes a hidden `._Track.flac` companion beside every file it copies to the player. These were indexed as tracks, so you got a second copy of the album with no metadata that skipped silently when played — and could not be deleted, because both the desktop and the player hide dot-files. Hidden files are now skipped. One rescan removes the leftovers.
  - Albums listed out of order when only some files carried a track number, for example 5, 1, 2, 6, 3, 4. Track numbers are now trusted only when every track on the album has one; otherwise the filenames decide the order. Browsing a folder follows album order too, instead of sorting by title.
  - "Library needs attention" could not be cleared. A single unreadable or zero-byte file on the card made every rescan report a problem, permanently. The same fault also stopped deleted files from disappearing from the library, and stopped the last-scan time from updating. The alert now names its cause, and a scan you cancel yourself raises nothing.
  - Bluetooth stem controls needed playback to be started on the player first. Media-button ownership is now re-taken whenever a headset connects. The first press after connecting is also no longer swallowed.
  - Triple press to skip back did not start playback when nothing was playing.
  - A connected Bluetooth headset was reported as "not connected" on every screen except the Bluetooth screen.
  - Pressing the track that is already playing restarted it and rebuilt the queue from whatever list you were looking at, losing your position and your album or queue order. It now just opens Now Playing.
  - ALAC files in an `.m4a` were reported as AAC. The codec is now read from the container itself, so the format shown is the real one.
  - The on-device log only ever showed the last 12 lines. It now shows considerably more, and reads them from the end of the file instead of loading the whole thing.

### New
  - Tracks in a format this device cannot decode are labelled "not playable" before you press play. A file that fails to play once is remembered, and the note is withdrawn if it ever does play or if you replace the file.
  - Technical metadata is now read directly for MP3, M4A, AAC, OGG, Opus and AMR as well, alongside the existing WAV, FLAC, AIFF, WavPack and DSD support.
  - Battery percentage is always shown, not only while charging or when low.
  - Track info states whether the file carries a track number.

### Performance
  - Playback stutters far less while the library is scanning. Scanning now yields briefly to audio and runs at background priority.
  - Less repeated work during playback: audio route, DAC status and progress updates no longer rebuild themselves on every tick.

### Known limitations
  - ALAC still cannot be played. Android 4.4 has no ALAC decoder and one cannot be added from an app. Converting to FLAC is lossless and plays natively — `ffmpeg -i input.m4a -c:a flac output.flac`.
  - Formats some firmware adds, such as WMA and APE, are deliberately left unlabelled rather than guessed at, since they may well play on your device.

## 1.1

## Also useful
  - [Install guideStep-by-step install for Y2Player](../../guides/y2player-y2.html)
  - [Y2Player V2.5Release2.5 · 2026-09-04](../../release-notes/y2player-y2/release2.5.html)
  - [Y2Player V2.3ReleaseV2.3 · 2026-08-15](../../release-notes/y2player-y2/releasev2.3.html)
  - [Y2Player V2.2.2RealeaseV2.2.2 · 2026-08-10](../../release-notes/y2player-y2/realeasev2.2.2.html)
  - [Y2Player V2.2.1 ReleaseV2.2.1 · 2026-08-03](../../release-notes/y2player-y2/releasev2.2.1.html)
  - [Y2Player V2.2ReleaseV2.2 · 2026-08-01](../../release-notes/y2player-y2/releasev2.2.html)
  - [Y2Player V2.1ReleaseV2.1 · 2026-07-29](../../release-notes/y2player-y2/releasev2.1.html)
  - [Y2Player 2.0 Complete Media Engine RewriteReleaseV2.0 · 2026-07-27](../../release-notes/y2player-y2/releasev2.0.html)
  - [Y2Player V1.2ReleaseV1.2 · 2026-07-26](../../release-notes/y2player-y2/releasev1.2.html)

Notes as published by the Y2Player project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=Y2Player&version=ReleaseV1.1&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
