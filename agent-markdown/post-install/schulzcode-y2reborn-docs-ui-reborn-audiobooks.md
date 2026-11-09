---
title: "Reborn Audiobooks (plan, Beta 8.19+) - Innioasis Updater"
description: "Reborn Audiobooks plan, Beta 8.19+ Owner request 2026-10-21: audiobooks as a full feature, a Home entry that can be switched on and off, chapters, remembering where the l"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-audiobooks.html"
---

# Reborn Audiobooks (plan, Beta 8.19+) - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Audiobooks (plan, Beta 8.19+)

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Audiobooks (plan, Beta 8.19+)

Owner request (2026-10-21): audiobooks as a full feature, a Home entry that can be switched on and off, chapters, remembering where the listener stopped, built on Reborn's FFmpeg layer. Y2Player had the feature; it was assessed, not copied.

## Owner decisions
  - What is a book: a folder named `Audiobooks` / `Hörbücher` (any case, anywhere in the path;

Y2Player's `AUDIOBOOKS` rule), every `.m4b`, and files tagged genre `Audiobook` / `Hörbuch`.
  - Playback speed 0.75–2.0×, per book, in this feature (Y2Linux FFmpeg gains `atempo`).
  - Sleep timer (15/30/45/60 min, end of chapter, fade-out) in this feature; it works for music too.
  - Home entry shown automatically once the library holds a book; switched off and on in

Customize > Home Menu.

## What Y2Player had (assessment)

Kept: path identity (book = folder, `Disc/CD/Part N` folders fold into it, author folders stay), natural chapter order (disc, folder, track only if every file has one, filename), one progress row per book, saves on start/pause/change/tick, nothing saved in the first 10 s or last 5 s of a file, 5 s rewind on resume, books kept out of every music view, Book Options (Chapters, Start from Beginning, Clear Progress), books always in order.

Fixed here: embedded chapters were never read (an M4B was one long item); Next on the last chapter deleted the progress; starting a book turned shuffle and repeat off globally for good; renaming a folder lost the progress; search named books "CD1"; the rewind applied only from the book list; no finished state, no speed, no book-level time left, no settings.

## Constraints found in Reborn
  - `AVFormatContext->chapters` is never read; FFmpeg's mov (QuickTime chapter track, Nero `chpl`),

mp3 (ID3 `CHAP`) and ogg (`CHAPTERxx`) demuxers produce them.
  - No `atempo` in the device FFmpeg; speed touches `RbDspConfig` (352-byte layout asserts), the

position maths (`playback.rs` position, UI extrapolation, crossfade windows, scrobble time).
  - Every seek, resume and output change runs a full `load()` (sink reopen, open + probe).
  - Open budget 32 MiB and `av_max_alloc(32 MiB)`: a single-file M4B over roughly 9 h of AAC-LC may

not open (the mov sample index is one allocation). Non-attached video streams are refused.
  - One global `position_ms`; full `Track`s go into the 8 MiB session — chapters stay out of `Track`.
  - Settings root holds 9 rows, the Music page 5; `components::time` has no hours.

## Phase 0 results (2026-10-21, host FFmpeg 9.0.2 = device version)

Fixtures made with the host `ffmpeg` (sine audio, ffmetadata chapters), run through Reborn's media layer (`crates/reborn-media/examples/book_probe.rs`: inspect, open, read, seek to 90 %):````````

| File | Result before | Action |
| --- | --- | --- |
| 3-min M4B, 4 chapters (QuickTime chapter track) | ok; FFmpeg chapters incl. umlauts | read them (phase 1) |
| 3-min MP3, ID3 CHAP | ok; chapters | same |
| Folder book Audiobooks/Author/Book/CD n/0n.mp3 | ok | grouping (phase 1) |
| M4B with the cover as an MPEG-4 video track | refused (any non-attached video) | admit_streams: in MP4/M4B beside audio the video stream is discarded, never read |
| 10.5-h M4B, AAC-LC 44.1 kHz 32 kb/s (1.63 M frames) | scanned, but no audio and no seek: the mov index (24 B/frame, one allocation) exceeds av_max_alloc(32 MiB) and FFmpeg drops it silently | cap 128 MiB (≈36 h at 44.1 kHz AAC-LC); large MP4s scanned one at a time |

Cost of the 10.5-h book with the larger cap: peak RSS 186 MB vs 49 MB for a short book (open 49 ms, seek to 90 % in 1 ms). The player has ≈822 MB available; Reborn's RSS is ≈33 MB.

## Phases
  - Risks with real files: fixtures for an M4B with chapters, a >10 h M4B, an M4B with an image

track, an MP3 folder book, an MP3 with `CHAP`; scan + open within the budgets; chapters seen.
  - Library: `book` identity computed from path/extension/genre (no schema or revision bump);

grouping and order; author from album artist/artist; `rb_media_chapters` + a chapter cache table keyed by file identity; books removed from Songs/Albums/Artists/Genres/Folders, Cover Flow, counts, Recently added, Shuffle, Last.fm.
  - Progress: additive `book_progress` table (book key, file, position, chapter, finished,

updated); found again by file name + size after a rename; saved every 15 s, on pause, chapter change, switching away and shutdown; rewind 5 s (pause < 10 min), 15 s (< 1 day), 30 s (longer); finished instead of deleted.
  - Playback rules: no shuffle/repeat/crossfade for books (music settings untouched); Next/Previous

= chapter (Previous restarts after 5 s); last chapter never deletes; held seek steps 10 s → 30 s → 60 s; in-file seek without reopening; AVRCP title = chapter, album = book.
  - Menus: Home > Audiobooks (continue first, cover, author, "Chapter 3 of 12 · 45 %",

Finished), book page (Resume, Start Over, Chapters, Mark as Finished, total/left), Now Playing for books (chapter title and progress, book time left, `h:mm:ss`), hold menu Chapters / Speed / Sleep.
  - Speed: `atempo` in Y2Linux FFmpeg and its verify lists, `RbDspConfig.speed`, scaled times.
  - Sleep timer.
  - Finish: tests, previews, skins, docs, device test with real books, beta.

## Status (2026-10-21)

Phases 0–6 are implemented on main (`11febec` library, `faa87fc` progress and playback, `56f79ac` menus, `6aeec66` speed, `b2951f5` sleep timer, `f61c7c3` skins); Y2Linux `01d8882` builds FFmpeg with `atempo`. Code map:
  - `reborn_core::books`: detection (`is_book`), grouping and order (`books`, `order`, `natural`),

chapters (`ChapterMark`, `Span`, `spans`), the playing book (`Listening`: chapter at, next, previous, progress), the shelf (`Shelf`, `Progress`, `rewind_ms`), speeds (`SPEEDS`, `next_speed`).
  - `AppModel.book` (session), `LibraryState.shelf` / `.chapters` (kept out of action rollback),

`AppModel.sleep_timer` (memory only); effects `PlayBook`, `SetBookFinished`, `ForgetBook`, `LoadChapters`, `SetAudiobooksOnHome`, `SetBookSpeed`, `SetSleepTimer`.
  - App: `app/reborn/src/books.rs` (shelf file `state/books.json`, chapter reader thread, start,

chapter steps, finish, rewind), `sleep_timer.rs`; hooks in `main.rs` (checkpoint saves the place, queue replacement saves first, Next/Previous, track end, crossfade 0 and speed in `load()`, book seek steps, rewind in `toggle()`); `playback.rs` scales played frames by the job's tempo.
  - UI: `views_books.rs` (list rows, book page, `BookNow` for Now Playing and skins), Home entry,

Home Menu toggle, hold menus, search results, `components::time` with hours.
  - Media: `rb_media_chapters`, `admit_streams`, `av_max_alloc` 128 MiB, `RbDspConfig.speed`

(360 bytes) with `atempo` after `aformat`, `heavy_mp4` scan serialisation.

Host evidence: workspace tests (608), clippy, previews `b1`–`b6` in Reborn's look and two skins, GLES comparison 165/165.

## Device test (2026-10-21, owner's player, builds 117 and 118 = 1.0.0-beta.8.19, seq 8301/8302)

Test books in `Internal Storage/Audiobooks/Reborn Test Books/` (the Phase 0 fixtures: 3-min M4B with 4 chapters, the same as MP3 with ID3 CHAP, an M4B with a cover video track and Nero chapters, a 10.5-h M4B, a 6-file `Frank Test/The Folder Book/CD 1|2` book). Buttons by evdev injection, screens by `y2-screen-stream`.
  - Scan: all 10 files, the 10.5-h book with its length; Home shows Audiobooks; the list shows all

five books with author and length, in progress first, finished last.
  - A book's page reads the M4B's chapters in the background (0:45 / 1:05 / 0:40 …).
  - Chapter 3 plays from 1:50; Next → chapter 4 (150 s); Previous early → 110 s; Previous after 6 s

restarts the chapter; Next in the last chapter keeps the place.
  - Speed 1.5×: the chain carries `atempo=1.50`, the position moved 6.4 s in 4 s; kept per book.
  - A book played to its end is Finished and starts over; its speed is kept.
  - 10.5-h M4B: plays; Reborn RSS 92 MB (peak 155 MB at open), 741 MB still available; a seek to

9 h 27 min (`rebornctl seek`) took 2.8 s including a full reopen.
  - Sleep timer End of Chapter paused at the next chapter's start; Now Playing said "Sleeps after

chapter".
  - Resume after a Reborn restart: build 117 skipped the rewind (the shutdown checkpoint refreshed

the last-listened time); fixed in `da5b777`, build 118 continued 5 s before the pause.
  - The cover-track M4B plays.

Not testable by injection: held seek (the button driver reports the key released ~18 ms after an injected press). Not done: in-file seek without a reopen (a chapter jump in a very long single file costs ≈2–3 s); heard by ear: speed quality, the sleep fade.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
