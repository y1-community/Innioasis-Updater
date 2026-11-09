---
title: "Changelog - Innioasis Updater"
description: "Changelog Unreleased - Added .m4b audiobook indexing and AAC/ALAC playback through the existing FFmpeg MOV/MP4 path. 2.5 — FM radio and unified search - Added FM Radio su"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2player-changelog.html"
---

# Changelog - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=y2player-y2)

Post-install setup · Y2Player · Y2

# Changelog

A Y2 custom Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=y2player-y2)[Install guide](../guide.html?model=Y2&software=y2player-y2)

# Changelog

## Unreleased
  - Added `.m4b` audiobook indexing and AAC/ALAC playback through the existing FFmpeg MOV/MP4 path.

## 2.5 — FM radio and unified search
  - Added FM Radio support for the built-in MediaTek MT6627 tuner.
  - Combined the complete Search-enabled Y2Player line with FM controls and the latest playback, wake-lock, timer, equalizer, wrapping, shuffle, and artwork fixes.
  - Added the production `ACCESS_MTK_MMHW` permission required to open `/dev/fm`.

## 2.3 — Up Next queue, library browsing, and menu artwork
  - Rebuilt the playback queue around explicit Up Next and continuation sections, preserving the source collection after manually added songs finish.
  - Made Shuffle expose the actual upcoming order while keeping deliberate Up Next entries ordered and restoring the remaining collection order when Shuffle is disabled.
  - Added wheel-friendly circular actions for playing, promoting, moving, and removing individual queue occurrences.
  - Added focused Clear Up Next, Clear After Current, and confirmed Stop & Clear queue actions.
  - Added batch Play Next, Add to Up Next, and Add Shuffled actions for complete collections and manually selected groups of tracks.
  - Added Genres and Years library views with filtered track, artist, and album navigation.
  - Added independent sorting for tracks, albums, and year lists, including oldest-first and newest-first album chronology.
  - Kept same-named albums from different album artists separate and displayed release years on album rows where available.
  - Added bounded album-art thumbnails to visible menu rows while retaining track numbers in album song lists.
  - Excluded audiobook chapters from music collections, playlists, counts, and Shuffle All while preserving the dedicated Audiobooks experience.
  - Reduced audiobook Now Playing actions to Chapters, Queue, Sleep Timer, and Track Details.
  - Parsed repeated Vorbis `ARTIST` values into individual artists while preserving the complete display credit.
  - Removed unused state and result fields across device, diagnostics, playback, queue, backup, playlist, Bluetooth, and display code.

## 2.2.1 — playback stability, controls, and Now Playing refinements
  - Fixed brief volume peaks during volume-mode changes, playback resume, pause, lock, and screen wake.
  - Fixed locked-screen In-App volume changes being overwritten when the display turned back on.
  - Added reliable press-and-hold volume adjustment and guarded firmware ownership of the Y2's physical volume keys.
  - Kept paused, resumable playback sessions loaded when the interface disconnects or the screen turns off.
  - Preserved shuffle traversal progress when Shuffle is changed so unplayed queue items cannot become stranded.
  - Made Left and Right control Previous and Next everywhere; held directions seek and Center handles menu navigation.
  - Removed the duplicate Now Playing main-menu row and made a short Center press on Now Playing keep the display active without toggling playback.
  - Added wheel acceleration for long collections and an optional Wrap Lists control.
  - Added active-state indicators, including a filled heart for favorited tracks.
  - Replaced the Now Playing button hints with Shuffle, Repeat, transition, and queue status.
  - Added an animated circular playback-options menu opened by holding Center on Now Playing.
  - Split additional metadata into separate genre and technical-information lines and added delayed scrolling for selected long text.
  - Kept the album line visible when an album has the same name as its artist.
  - Improved multi-disc audiobook ordering and normalized artist identity across capitalization and surrounding whitespace.
  - Hardened library reset, playback-history handling, output-gain sequencing, and firmware-image verification.

## 2.2 — interface redesign, audiobooks, and library browsing
  - Added Audiobooks as a main-menu destination. Books are grouped by folder, and disc or part folders collapse into the book above them.
  - Added audiobook resume that returns to the saved position inside a chapter instead of restarting it, with a short rewind and an end-of-chapter guard.
  - Persisted audiobook position on the existing progress tick. Previously only chapter start, pause, and release wrote a position, so a force-quit mid-chapter lost the place.
  - Added a per-book chapter list, Start from Beginning, and a confirmed Clear Progress, backed by the schema-14 audiobook_progress table.
  - Fixed a defect where every library scan rebuilt LibraryState from scratch and erased all saved audiobook positions.
  - Added 47 stroke-only vector row icons drawn from one shared Path and RectF, with no per-frame allocation and no bitmap assets.
  - Rebuilt the main menu, Music section, and Settings tree around the four rows the 480 x 360 display shows at once.
  - Moved Bluetooth from Audio to the Settings root.
  - Reordered every menu by how often each entry is opened, placing reference screens such as About and Diagnostics last and destructive rows below the actions beside them.
  - Added confirmation prompts to all six irreversible actions. Delete Playlist, Clear History, and Clear Queue previously ran on a single press.
  - Moved Reset Library out of Diagnostics and onto Settings, System, Reset, where it now asks for confirmation before deleting the index.
  - Added Listening History under Settings, Library. The session count is read when the screen is opened rather than reported as zero until the row is pressed.
  - Corrected the Reset Library description, which stated that playlists and favourites were rebuilt from the card when they are deleted.
  - Fixed albums breaking apart when browsed by artist. Album membership now uses the album-artist tag, so a feature credit on one track no longer hides that track.
  - Added featured artists as their own entries using a parser that splits only on explicit feature words and never on &, comma, or plus.
  - Added a Shuffle row to album track lists, matching Songs, Favorites, Recently Played, artists, and playlists.
  - Removed every non-essential comment across the repository and verified by lexing that the code stream and all string literals were unchanged.
  - Added a screen catalogue derived from Screen sealed subclasses that fails when a new screen is added without navigation coverage.

## 2.1 — scanner and media-engine improvements
  - Added the collation-correct `(volume_id, relative_path COLLATE NOCASE)` covering index, reducing the measured large-library fallback lookup from 258.160 seconds to 4.124 seconds.
  - Increased scanner and unchanged-file database batches to 400, reducing fingerprint queries and transactions from 144 to 23 in the 9,178-file benchmark.
  - Reduced an unchanged 9,178-file scan from 42.106 seconds to 19.070 seconds while retaining one-file metadata work for add, modify, rename, and delete cases.
  - Reduced metadata probing to a 32 KiB probe and 100 ms analysis limit after validating 76 fixtures and 1,394 metadata assertions on physical hardware.
  - Added scan progress feedback and a dedicated partial wake lock held only for active library work.
  - Completed metadata propagation for comments and track/disc totals; improved ReplayGain, ADTS AAC, FLAC bit-depth, malformed-file, and partial-playback handling.
  - Kept artwork payloads out of scan-time indexing and moved compressed artwork extraction to the bounded on-demand loader and shared cache.
  - Added portable Windows, macOS, and Linux absolute-path relocation for imported playlists.
  - Refactored decoded audio, ReplayGain, balance, fades, and crossfades to float32 with one final PCM16 conversion at the API-19 AudioTrack boundary.
  - Fixed decoder abort ordering, exact short-FLAC seek fallback, bounded invalid-packet recovery, gapless/crossfade wake-lock continuity, and duplicate playback notification work.
  - Added a deterministic media corpus, physical-device regression runner, resource checks, native phase profiling, and a secure non-root ADB boot-image pipeline.
  - Added guarded and independently verified primary-audio HAL DAC-frequency-hook groundwork without changing the advertised 44.1 kHz PCM16 playback output.

## 2.0 — unified FFmpeg engine
  - Replaced playback and format diagnostics with one FFmpeg 8.1.2 engine for MP3, AAC/M4A, ALAC/M4A, FLAC, WAV/PCM, and Ogg Vorbis.
  - Added a reproducible NDK r25c/API-19/armeabi-v7a build that statically consolidates the allowlisted FFmpeg runtime into one `liby2audio.so`.
  - Installed that runtime at `/system/lib/liby2audio.so` in generated firmware, with byte-for-byte APK/image verification and stock Android 4.4 file metadata.
  - Added persistent AudioTrack PCM output, native seek/abort handling, playback-head position accounting, PCM gapless promotion, and PCM crossfade mixing.
  - Added album, track, and shuffle-aware ReplayGain using embedded gain/peak metadata with peak-based clipping prevention.
  - Unified library metadata under FFmpeg: tags, technical fields, ReplayGain, and lazy embedded artwork now use the same backend as playback, including Opus on Android 4.4.
  - Hardened metadata scans with local-file/demuxer allowlists, a wall-clock deadline, no decoder opening, scan-time artwork-payload skipping, lazy artwork size limits, and real probe-I/O diagnostics.
  - Fixed Shuffle All to begin at the first entry of a complete library permutation and generate a fresh permutation after every full pass.
  - Simplified Home to Music, Shuffle All, Audio, and Settings. Audio groups Playback and Sound, while Bluetooth sits under Settings alongside focused Interface and Library submenus; detailed track, queue, and output actions moved out of contextual landing screens.
  - Added explicit application wake-lock ownership and retained queue, focus, Bluetooth, media-control, storage, persistence, sleep-timer, and effects policies.
  - Removed playback and diagnostic framework-decoder paths and invalidated their stale unsupported-file verdicts.
  - Direct DAC now reports the audited stock-HAL limitation and falls back to standard AudioTrack without speculative device access.

## 1.2

Mostly things people asked for. The menu has been reorganised, so a few settings have moved.

### New
  - Artists now open that artist's albums instead of jumping straight to every

track, so browsing goes Artists → album → songs. "All Songs" is still the first row, which is what pressing an artist used to do.
  - Light theme, under Settings → Display → Theme. The dark design is unchanged

and remains the default. On a transflective LCD like the Y2's, a light theme is also the more readable choice outdoors, because a pale background lets the backlight through instead of blocking it.
  - Left/right balance, under Sound Effects, for asymmetric hearing loss.

Centred by default. It attenuates the far channel rather than boosting the near one, so total loudness drops as you move off centre.
  - Wheel When Screen Off, under Controls, off by default. With it on, the click

wheel and its buttons keep working with the display asleep — which also means they can be pressed in a pocket, which is why it is off unless you ask for it.

### Changed
  - Settings is reordered by how often each entry is actually opened. Bluetooth

is first, because connecting a headset is a recurring task rather than a setting. Sound Effects is now a top-level entry rather than living inside Playback, so the equalizer and balance are three presses away instead of four. Sort Order sits next to Storage, since both concern the library.
  - Haptics and System UI Sounds moved off Display onto a new Controls screen,

together with the setting above. They are feedback for input, not display settings.
  - Playback's settings are grouped by what they do: what plays next, transitions,

seeking, volume, then interruptions.
  - Sound Effects lists the things you can change before the things you can only

read.
  - Track info states whether the file carries a track number.

### Fixed
  - Choppy playback during a library scan should be much rarer. The scan already

paused for audio, but only once per 64 files, which left roughly three seconds of uninterrupted work between pauses — long enough to starve the playback buffer. It now yields every 8 files, for a share of what those files actually cost.
  - A Bluetooth headset reported as "not connected" on every screen except the

Bluetooth screen.
  - The DAC and output rows were hidden when the device's effect framework was

missing — which is exactly the firmware whose behaviour those rows explain.
  - Two artists with an identically named album (a Greatest Hits each) opened

one merged track list. An album reached through an artist is now scoped to that artist. The global Albums list still merges shared names on purpose, so a compilation stays one album.
  - ALAC files in an `.m4a` were reported as AAC. In the 1.2 framework engine they could not be played —

see below — but they are now identified correctly and labelled, instead of failing silently when you press play.

### Why ALAC did not play in 1.2

Apple Lossless needs a decoder, and the Y2 runs Android 4.4. ALAC decoding was added to Android in version 12, eight years later. An app cannot supply the missing decoder: the framework decoder and `MediaCodec` could only use codecs the operating system already has, so there is no setting or update to this app that would make an ALAC file play on this hardware.

What 1.2 does instead is stop pretending. The codec is now read out of the file itself rather than guessed from the container, so an ALAC track is labelled not playable in the list rather than appearing normal and then failing.

If you have ALAC files, convert them to FLAC. Both are lossless, so the conversion is bit-exact for the audio — you lose nothing but Apple's container — and FLAC plays natively on the Y2:`ffmpeg -i input.m4a -c:a flac -compression_level 5 output.flac`

Supporting ALAC properly would mean bundling a decoder and building a second playback path to feed it, duplicating seeking, gapless and crossfade. That is a large amount of machinery for one format that converts losslessly in one command, so it is not planned.

### Also still true
  - Formats some firmware adds, such as WMA and APE, are deliberately left

unlabelled rather than guessed at, because they may well play on your device.

## 1.1

A maintenance release. Everything here comes from bug reports and device logs from 1.0 users.

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
  - ALAC could not be played by the 1.1 framework backend. Converting to FLAC was the lossless workaround at that time.
  - Formats some firmware adds, such as WMA and APE, are deliberately left unlabelled rather than guessed at, since they may well play on your device.

## 1.0

First released version.

These are Y2Player's own instructions, shown here word for word.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
