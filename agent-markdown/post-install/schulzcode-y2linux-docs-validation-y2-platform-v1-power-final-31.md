---
title: "POWER-FINAL-31 — folder-first artwork and metadata formats - Innioasis Updater"
description: "POWER-FINAL-31 — folder-first artwork and metadata formats Status: SUPERSEDED, NEVER FLASHED ALONE 2026-10-14; contained in 32–34, installed as part of 33. Package out/y2"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-31.html"
---

# POWER-FINAL-31 — folder-first artwork and metadata formats - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-31 — folder-first artwork and metadata formats

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-31 — folder-first artwork and metadata formats

Status: SUPERSEDED, NEVER FLASHED ALONE (2026-10-14; contained in 32–34, installed as part of 33). Package `out/y2linux-platform-v1-power-final-candidate-31/` (fallback = 30), receipts `out/deep-sleep-final/build31-receipts/`. BOOTIMG `9aeeba7899f47b3d137f664f3ae0d20e6a25cde76e87f14ec3a837b0012bb384`, Y2ROOT `b275bf043f14979ffa6ffcf9a84f5882b9453c7da822879157c2de0078d6bf4f`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-31`, kernel `6.18.56-y2linux-platform-v1-power-final-31`, root `2026.08-platform-v1.61`, release `1.0.0-platform-v1-power-final-candidate.31`; Linux `ebd2a58`, Reborn `0892bf2`. Contains 27–30 (30 was never flashed; 31 supersedes it).

## What 31 changes (Reborn `0892bf2`)
  - Artwork: the album folder's cover first, the embedded picture only when the folder has none (thumbnails, Cover

Flow, Now Playing). Folder names by priority (any case, jpg/jpeg/png/webp): cover, folder, front, album, albumart, artwork; then Windows Media Player AlbumArt_{GUID}_Large / AlbumArtSmall; finally the only image in the folder. macOS `._*` never counts. Thumbnail cache renamed (`thumb2-`), old thumbnails removed once.
  - Library extensions `.m4b`, `.oga`, `.aifc` (already supported by the image's FFmpeg); `.mp4` deliberately excluded.
  - Vorbis/APE `ALBUM ARTIST` (with a space) read as album artist; `METADATA_REVISION` 4 re-reads every row's tags once.

Supported formats and the FFmpeg component list: scope audit "POWER-FINAL-31" in `docs/planning/roadmap-gap-audit.md`.

## Tests

Reborn workspace 379 (folder-over-embedded with a distinct cover, name priority / WMP / single-image fallback, extensions, legacy thumbnail removal), clippy `-D warnings`, fmt. Platform: validate PASS, ELF 354, installed ARM, privacy, inventory 108, container suite 711 OK. Packaging/inventory ran from a checkout of the build commit (a docs-only commit followed it).

## Owner checks after the flash
  - Album grid / Cover Flow show the folder image where both exist (first view rebuilds thumbnails).
  - The first library scan re-reads tags once (a few seconds); album artists tagged `ALBUM ARTIST` group correctly.
  - 30's checks: boot scan time, `noatime`, playback unchanged.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
