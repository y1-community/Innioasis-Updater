---
title: "Y2Player V2.2.2 - Innioasis Updater"
description: "2.2.2 backup, artwork, and playback reliability - Added a versioned Backup & Restore screen for settings, favorites, Y2Player-created playlists, audiobook progress, recent plays, t"
language: "en"
source: "https://innioasis.app/release-notes/y2player-y2/realeasev2.2.2.html"
---

# Y2Player V2.2.2 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

Firmware release notes · Y2Player · Y2

# Y2Player V2.2.2

A Y2 custom Software.RealeaseV2.2.2Y22026-08-10[schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=y2player-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

rom_y2.zip[rom_y2.zip 283 MB](https://github.com/SchulzCode/Y2Player/releases/download/RealeaseV2.2.2/rom_y2.zip)

system.zip[system.zip 215 MB](https://github.com/SchulzCode/Y2Player/releases/download/RealeaseV2.2.2/system.zip)

## 2.2.2 backup, artwork, and playback reliability
  - Added a versioned Backup & Restore screen for settings, favorites, Y2Player-created playlists, audiobook progress, recent plays, the saved queue and session, and listening history.
  - Made backups portable across library rescans and storage mount aliases, checksum-verified them before import, and made failed restores roll back cleanly.
  - Added external Now Playing artwork from `folder.jpg`, `folder.jpeg`, `folder.png`, `cover.jpg`, `cover.jpeg`, and `cover.png`, while continuing to prefer embedded artwork.
  - Fixed album navigation for comma-separated and featured artist credits so an album stays intact and opens with every track from any credited artist.
  - Added live playback progress to the menu banner and allowed long title, artist, and album lines on Now Playing to scroll independently.
  - Fixed Wrap Lists behavior in settings menus and made every brightness preset survive Android's percentage conversion without changing value.
  - Matched the low-battery warning sound to the active playback volume and kept it silent when playback volume is muted.
  - Fixed end-of-track output draining that could prevent ordinary queue advancement, while preserving repeat, shuffle, gapless, and crossfade behavior.
  - Hardened preloading, seeking, pausing, and track transitions so stale callbacks cannot publish the wrong playback state and a track change is reported only after output becomes audible.
  - Hardened held volume-button handling and In-App/System volume-mode handoffs with bounded repeat behavior and playback-thread acknowledgement before raising the system stream.
  - Added a confirmed Clear Diagnostic Log action and made internal logging, card mirroring, rotation, crash flushing, and fresh diagnostic exports more resilient.

## Also useful
  - [Install guideStep-by-step install for Y2Player](../../guides/y2player-y2.html)
  - [Y2Player V2.5Release2.5 · 2026-09-04](../../release-notes/y2player-y2/release2.5.html)
  - [Y2Player V2.3ReleaseV2.3 · 2026-08-15](../../release-notes/y2player-y2/releasev2.3.html)
  - [Y2Player V2.2.1 ReleaseV2.2.1 · 2026-08-03](../../release-notes/y2player-y2/releasev2.2.1.html)
  - [Y2Player V2.2ReleaseV2.2 · 2026-08-01](../../release-notes/y2player-y2/releasev2.2.html)
  - [Y2Player V2.1ReleaseV2.1 · 2026-07-29](../../release-notes/y2player-y2/releasev2.1.html)
  - [Y2Player 2.0 Complete Media Engine RewriteReleaseV2.0 · 2026-07-27](../../release-notes/y2player-y2/releasev2.0.html)
  - [Y2Player V1.2ReleaseV1.2 · 2026-07-26](../../release-notes/y2player-y2/releasev1.2.html)

Notes as published by the Y2Player project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=Y2Player&version=RealeaseV2.2.2&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
