---
title: "Audiobooks - Innioasis Updater"
description: "Audiobooks Since Y2Linux 1.0 Beta 8.19 the Reborn player has a place of its own for audiobooks: it remembers where you stopped in every book, moves by chapter, plays at t"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-audiobooks.html"
---

# Audiobooks - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Audiobooks

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Audiobooks

Since Y2Linux 1.0 Beta 8.19 the Reborn player has a place of its own for audiobooks: it remembers where you stopped in every book, moves by chapter, plays at the speed you like and can stop by itself when you fall asleep. Books never mix with your music.

## Where to put books

Copy books to Internal Storage or the SD card, in any of these ways:
  - A folder named `Audiobooks` or `Hörbücher` (any capitals, anywhere), with one folder per

book inside. An author folder in between is fine: `Audiobooks/Michael Ende/Momo/01.mp3`, `02.mp3`, … Folders called `CD 1`, `Disc 2`, `Part 3` (or `Teil 3`) inside a book belong to that book.
  - Any `.m4b` file, wherever it is: one file is one book. Several `.m4b` files make one book

only when they share the same album tag (`Book Part 1.m4b`, `Book Part 2.m4b`).
  - Files tagged with the genre `Audiobook` or `Hörbuch`.

A book's name comes from its album tag, else its folder (or file); the author from its album artist or artist tag, else an author folder. Parts play in disc order, then folder order, then by track number (when every file has one), then by file name, where `2` comes before `10`.

Books are not songs: they stay out of Songs, Albums, Artists, Genres, Folders, Cover Flow, search's music results, Shuffle and the counts, and they are never scrobbled to Last.fm.

## Listening

Home → Audiobooks appears once your library holds a book (switch it off and on under Settings → Customize → Home Menu). Books you are listening to come first, the last one you listened to at the top, with Chapter 3 of 12 · 45 %; new books follow A to Z, finished books come last.

Open a book to see its chapters, how far you are and how long it still runs:

| Button | What it does |
| --- | --- |
| Continue (Play for a new book) | Goes on where you stopped, a little before. |
| Start Over | From the first chapter. |
| A chapter | Plays from the start of that chapter. |

Hold Select on a book for Continue, Start Over, Mark as Finished (or Not Finished) and Forget Progress.

Chapters are the book's own chapter marks when its files have them (M4B, MP3 and Ogg files usually do), otherwise each file is a chapter. While a book plays:
  - Next / Previous go to the next or previous chapter. Previous more than 5 seconds into a

chapter goes back to that chapter's start. Next in the last chapter does nothing: your place is never lost.
  - Holding Next / Previous winds through the book: 10 seconds a step at first, then half a

minute, then a minute.
  - Now Playing shows the chapter, the book and its author, the chapter's progress and how much of

the book is left. Bluetooth headphones and car radios see the chapter as the title.
  - Shuffle, Repeat and Crossfade never apply to books; your music settings stay as they are.

## Where you stopped

Reborn keeps your place in every book (every few seconds while it plays, when you pause, change chapter, switch to music and when the player turns off), also across restarts, updates and a library rebuild. When you continue, it goes back a little so you can find your way in again: 5 seconds after a short pause, 15 seconds after more than ten minutes, 30 seconds after a day. Renaming or moving a book's folder keeps its place.

A book that has played to its end is Finished and starts over next time.

## Speed

Hold Select on Now Playing and press Speed: 0.75×, 1×, 1.1×, 1.25×, 1.5×, 1.75×, 2×, round again. The voice keeps its pitch. Every book keeps its own speed; music always plays at normal speed.

## Sleep timer

Hold Select on Now Playing and press Sleep Timer: 15, 30, 45 or 60 minutes, End of Chapter (End of Song for music), or Off. A timed sleep fades out over its last ten seconds and pauses; End of Chapter pauses where the next chapter begins, so you continue right there. Now Playing shows Sleeps in 23 min. Restarting the player ends the timer. It works for music too.

## Good to know
  - Very long single-file books play and seek normally (tested with a 10.5-hour M4B; books up to

about 36 hours of AAC at 44.1 kHz). Opening such a book takes a moment more memory than a song.
  - An M4B that carries its cover as a video track plays (the video part is ignored).
  - A paused book with Bluetooth headphones connected keeps the player awake for 15 minutes, so the

headphones' own play button can continue it.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
