---
title: "Y2Player V1.2 - Innioasis Updater"
description: "Changelog 1.2 Mostly things people asked for. The menu has been reorganised, so a few settings have moved. You might need to rescan your library, since i made some changes to the u"
language: "en"
source: "https://innioasis.app/release-notes/y2player-y2/releasev1.2.html"
---

# Y2Player V1.2 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

Firmware release notes · Y2Player · Y2

# Y2Player V1.2

A Y2 custom Software.ReleaseV1.2Y22026-07-26[schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=y2player-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

system.zip[system.zip 315 MB](https://github.com/SchulzCode/Y2Player/releases/download/ReleaseV1.2/system.zip)

# Changelog

## 1.2

Mostly things people asked for. The menu has been reorganised, so a few settings have moved. You might need to rescan your library, since i made some changes to the underlying database schema!

### New
  - Artists now open that artist's albums instead of jumping straight to every

track, so browsing goes Artists → album → songs. "All Songs" is still the first row, which is what pressing an artist used to do.
  - Light theme, under Settings → Display → Theme. The dark design is unchanged

and remains the default. On a transflective LCD like the Y2's, a light theme is also the more readable choice outdoors, because a pale background lets the backlight through instead of blocking it.
  - Left/right balance, under Sound Effects, for asymmetric hearing loss.

Centred by default. It attenuates the far channel rather than boosting the near one, so total loudness drops as you move off centre.
  - Wheel When Screen Off, under Controls, off by default. With it on, the click

wheel and its buttons keep working with the display asleep which also means they can be pressed in a pocket, which is why it is off unless you ask for it.

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

paused for audio, but only once per 64 files, which left roughly three seconds of uninterrupted work between pauses long enough to starve the playback buffer. It now yields every 8 files, for a share of what those files actually cost.
  - A Bluetooth headset reported as "not connected" on every screen except the

Bluetooth screen.
  - The DAC and output rows were hidden when the device's effect framework was

missing which is exactly the firmware whose behaviour those rows explain.
  - Two artists with an identically named album (a Greatest Hits each) opened

one merged track list. An album reached through an artist is now scoped to that artist. The global Albums list still merges shared names on purpose, so a compilation stays one album.
  - ALAC files in an `.m4a` were reported as AAC. They still cannot be played 

see below but they are now identified correctly and labelled, instead of failing silently when you press play.

### Why ALAC still does not play

Apple Lossless needs a decoder, and the Y2 runs Android 4.4. ALAC decoding was added to Android in version 12, eight years later. An app cannot supply the missing decoder: `MediaPlayer` and `MediaCodec` can only use codecs the operating system already has, so there is no setting or update to this app that would make an ALAC file play on this hardware.

What 1.2 does instead is stop pretending. The codec is now read out of the file itself rather than guessed from the container, so an ALAC track is labelled not playable in the list rather than appearing normal and then failing.

### For Now

If you have ALAC files, convert them to FLAC. Both are lossless, so the conversion is bit-exact for the audio you lose nothing but Apple's container and FLAC plays natively on the Y2:`ffmpeg -i input.m4a -c:a flac -compression_level 5 output.flac`

Supporting ALAC properly would mean bundling a decoder and building a second playback path to feed it, duplicating seeking, gapless and crossfade. That is a large amount of machinery for one format that converts losslessly in one command, so it is not planned.

### Also still true
  - Formats some firmware adds, such as WMA and APE, are deliberately left

unlabelled rather than guessed at, because they may well play on your device.

## Also useful
  - [Install guideStep-by-step install for Y2Player](../../guides/y2player-y2.html)
  - [Y2Player V2.5Release2.5 · 2026-09-04](../../release-notes/y2player-y2/release2.5.html)
  - [Y2Player V2.3ReleaseV2.3 · 2026-08-15](../../release-notes/y2player-y2/releasev2.3.html)
  - [Y2Player V2.2.2RealeaseV2.2.2 · 2026-08-10](../../release-notes/y2player-y2/realeasev2.2.2.html)
  - [Y2Player V2.2.1 ReleaseV2.2.1 · 2026-08-03](../../release-notes/y2player-y2/releasev2.2.1.html)
  - [Y2Player V2.2ReleaseV2.2 · 2026-08-01](../../release-notes/y2player-y2/releasev2.2.html)
  - [Y2Player V2.1ReleaseV2.1 · 2026-07-29](../../release-notes/y2player-y2/releasev2.1.html)
  - [Y2Player 2.0 Complete Media Engine RewriteReleaseV2.0 · 2026-07-27](../../release-notes/y2player-y2/releasev2.0.html)

Notes as published by the Y2Player project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=Y2Player&version=ReleaseV1.2&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
