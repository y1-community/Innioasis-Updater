---
title: "POWER-FINAL-23 — Reborn Cover Flow and Genres - Innioasis Updater"
description: "POWER-FINAL-23 — Reborn Cover Flow and Genres Status: INSTALLED; Cover Flow looks right but ran at ≈10 fps → 24 2026-10-13. Package out/y2linux-platform-v1-power-final-ca"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-23.html"
---

# POWER-FINAL-23 — Reborn Cover Flow and Genres - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-23 — Reborn Cover Flow and Genres

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-23 — Reborn Cover Flow and Genres

Status: INSTALLED; Cover Flow looks right but ran at ≈10 fps → 24 (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-23/` (fallback = 22), receipts `out/deep-sleep-final/build23-receipts/`. BOOTIMG `9ea7a94377b0f63977a8732569c357a837112b69f321f8f501424b2a72a475cb`, Y2ROOT `8fff0f839836ca5583ac9bdd76eb71d82840a45a0df347ecf6e75468fae0d297`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-23`, kernel `6.18.56-y2linux-platform-v1-power-final-23`, root `2026.08-platform-v1.53`, release `1.0.0-platform-v1-power-final-candidate.23`; Linux `7f5445d`, Reborn `83c9127` (new). The platform is 22 unchanged. Flash BOOTIMG + ANDROID only with `MT6582_preserve_data_scatter.txt`, Download Only. Scope audit: "POWER-FINAL-23 Reborn Cover Flow and Genres scope audit" in the [roadmap gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## Owner request and decisions

Cover Flow for albums, highly optimised (smooth scrolling, an animation opening the album), and Genre in the main list. Decisions: Albums opens Cover Flow, Settings → Display → Album view switches back to the Grid; Genre → Albums (headed by All Songs) → Songs.

## What changes (Reborn `58670c8`, `116f673`, `83c9127`)
  - Genres: the library stores the genre tag (additive column; `METADATA_REVISION` 3, so an existing library

re-reads every song's tags once during the next scan, no rebuild). Home and Music get Genres (the home menu now has seven rows; spacing follows the count). A genre opens its albums in the chosen album view, headed by **All Songs; untagged songs are listed as No Genre**.
  - Cover Flow: each cover is a square turned about its vertical axis and pushed back, projected (focal length

300 px) into a perspective-correct quadrilateral, with a mirrored reflection fading into the background; title, artist, length and "n of N" below. The row glides to the focus with time-based easing (≈0.4 s to rest, smooth at any frame rate and under fast wheel spins). Select flies the centre cover into the album page while its list rises in (300 ms); Back flies it home. Once the row rests, the centre cover is decoded at 160 px by the artwork worker (the side covers use the 96-px thumbnails).
  - Renderer:`Quad.warp` (four corners, per-corner tints), sampled with `texture2DProj` so the projective divide

happens in the texture unit at full precision. A first version divided in the fragment shader; on the host it shifted glyph sampling (Mali-400 fragment shaders are fp16), caught by the GLES comparison and fixed.
  - Setting: Settings → Display → Album view (Cover Flow / Grid).

## Tests

Reborn: rustfmt, clippy `-D warnings`, 370 workspace tests (new: genre storage and pre-genre migration, Genres navigation, seven-row home fit, Cover Flow geometry and easing, view switch, flight and full-resolution cover request). Host GLES: ordinary screens render bit-identically to 22's renderer; all 77 preview screens match the reference rasteriser. Y2Linux: container suite 693, exit 0; package validation, ELF, installed ARM, privacy, inventory PASS.

## What to check on the device
  - After the first boot the library re-reads tags once (a scan); then Home shows Genres with a count.
  - Albums: Cover Flow; spin the wheel slowly and fast — the glide should stay smooth; the centre cover sharpens a

moment after stopping. Select → the cover flies into the album page; Back → it flies home.
  - Genres → a genre → All Songs and its albums; No Genre lists untagged songs.
  - Settings → Display → Album view → Grid restores the old grid.
  - Frame times: `graphics_frame_time_ms` in Reborn's metrics while scrolling (target ≤ 16.7 ms).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
