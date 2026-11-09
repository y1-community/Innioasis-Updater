---
title: "Reborn Product UI v3 - Innioasis Updater"
description: "Reborn Product UI v3 Reborn 0.3.0, 2026-10-10 candidate 11 adds the screens listed under System . A visual and navigation redesign of Product UI v2 for the 480×360 panel."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-product-ui-v3.html"
---

# Reborn Product UI v3 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Product UI v3

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Product UI v3

Reborn 0.3.0, 2026-10-10 (candidate 11 adds the screens listed under System). A visual and navigation redesign of Product UI v2 for the 480×360 panel. Source-complete, unit-tested and previewed on the host; not yet observed on hardware (see Not verified). The state machine, the library, audio, platform and boot-handoff code are unchanged except where this document says otherwise.

## Why

The owner found v2 "not intuitive" and full of options that are not for listeners (a Power menu, Quick Settings, Queue/options screens, codec and update internals). v3 keeps the player simple: Home → library → Now Playing, one calm Settings tree and nothing technical in the way.

## Design language

Near-black canvas; white type in three tiers (all small text ≥ 4.5:1); one accent colour taken from the cover that is playing (a calm cool white when the cover is dull); translucent "glass" for raised areas; selection is never colour only (a pill, ring or weight change as well). Type is Open Sans (SIL OFL 1.1), rendered once per size, so every glyph is drawn 1:1 on the pixel grid. No runtime font loader. Details: `assets/fonts/README.md`.

## Screens
  - Home — Now Playing, Artists, Albums, Songs, Folders, Settings with

counts; the playing cover with progress, or Recently added when idle.
  - Library — artist list with round avatars, artist page (albums), 4×2 album

grid with a lifted, ringed selection, album page (Play / Shuffle, tracks), songs with covers, folders (Internal Storage / SD Card, then contents), Up next. Fast wheel rotation in long lists shows a large current letter.
  - Now Playing — cover, title, artist, a quality tag, **icons for the options

that are on** (shuffle, repeat all/one, gapless, equalizer, normalise), the progress bar, transport and the output device. There is no volume text anywhere: the volume line is a bare 4 px line at the right edge for about a second. Select opens a short sheet (Up next, Shuffle, Repeat, Go to album/artist).
  - Settings — Bluetooth, Wi-Fi, Sound (equalizer presets, normalise volume,

gapless, crossfade, output), Display (brightness, screen-off delay), Storage, About & Updates (update status, version, reset).
  - System — the player raises these itself: Connected to a computer

(Internal Storage and SD cards with free space, then a sweeping ring and "Don't unplug until it finishes" while copying; Back dismisses it, it returns on a new connection), a Battery low dialog (once per level), the Bluetooth pairing card ("Pairing with … Keep the headphones close.") and a Couldn't connect dialog with Try again, the update download (since Baseline 48: step, percentage, gliding bar, MB, speed and time left from the platform's live progress; Connecting… with a sweeping segment before the first report), a scanning ring, and SD card removed / N new songs added toasts. Rings sweep where no progress figure exists; no percentage is ever invented. Crossfade has its own option icon on Now Playing. The Power button: a short press turns the screen off or on; a hold fills a ring ("Hold to turn off"), release cancels. There is no menu. (Since Beta 9.3.15 the hold opens the Quick Menu first, see [the settings map](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-SETTINGS-MAP.md%23the-quick-menu-hold-power&anchor=the-quick-menu-hold-power).)

Removed from the normal UI: Diagnostics, maintenance/rebuild, codec and LDAC tuning, update internals, Quick Settings, the Power menu, song info and jump to letter. The service menu (all of those, plus battery, sleep and restart) opens after seven taps on Version in About & Updates.

## Startup and shutdown

Startup keeps the v2 structure — wordmark, one thin bar, one status line — in a new style: lowercase "reborn" (Light 44 px, tracked) over a faint glow, a 124 px hairline bar with a leading dot, tracked-caps status text. The early splash (Y2Linux `tools/graphics/reborn-splash.c`) draws the same pixels from `previews/v3/boot-layout.json`; the hand-off frame is pixel-identical (tested). The failure screen reads *Couldn't start — Hold Power for 10 seconds, then turn it on again.*

Shutdown (`boot::shutdown_plan`): the UI recedes into the wordmark with Saving your place, the save runs, the bar drains through Closing and Shutting down (or Restarting), bar and label vanish, the wordmark dims to a single point of light, black. With a nearly empty battery a shorter farewell shows a red battery and *Battery empty. Your place is saved. Charge to continue.* Timings are in frames at the UI's 34 ms cadence and are estimates until observed on hardware.

## Renderer and memory

The renderer's fragment program is unchanged (texture × tint). New textures: three 1024-wide glyph pages and one 512-wide shape/icon page, stored as one byte per texel and sampled as luminance-alpha, and a 1024×512 RGBA thumbnail atlas (50 cells of 96×96 with a replicated gutter). Quads now carry a texture and a source rectangle; rounded shapes are built from non-overlapping pieces so translucent colours blend once. A frame is a few hundred quads in about 40 batches. Video memory for UI textures grows from about 4.4 MB to about 9 MB; the audit in the Y2Linux roadmap records the scope.

## Covers

Thumbnails are produced by a background worker (never on the UI thread), from the same pinned, freshness-checked cover loader as before, and cached in `/data/reborn/cache` as `thumb-<id>-<mtime>-<size>.t96` (96×96 RGBA, at most 1500 files, emptied by Clear cache). Until a cover is ready the row shows a calm placeholder. The accent is computed from the 160×160 now-playing cover.

Since Beta 8.18 (sharper covers). Covers are cropped to their centre (never stretched) and scaled with Lanczos (bicubic when a small picture has to grow) with full-resolution chroma. The now-playing and Cover Flow artwork is 180×180, the largest size drawn (Home's card); thumbnails are 128×128, decoded straight from the picture. Every picture goes to the GPU with box-filtered half and quarter copies (`reborn_graphics::level_block`), and each quad samples the smallest copy at least as large as it is drawn (`level_source`), so GL's bilinear filter never shrinks a cover by more than half: no grainy list covers without mipmaps. The thumbnail atlas is 2048×1024 (70 cells of 196×130, about 8 MB). The disk cache is `thumb3-<id>-<mtime>-<size>.t128`: 4:2:0 YCbCr, 24 KB per album, at most 3000 files (about 72 MB); when full, the 300 least recently shown are removed (a shown file's time is refreshed at most once a day). Older `thumb-`/`thumb2-` files are removed once. Recommended covers for users: square, at least 180×180 (300–600 px JPEG is plenty).

## Host verification of the GL path

`tools/preview/gles_compare.py` renders every preview quad list through the production GL code (`graphics.c`, via `gl_setup`) on a host GLES2 context (Mesa, EGL surfaceless) and compares each frame with the Python rasteriser: all 62 frames match (mean difference < 1.5/255). It validates the luminance-alpha textures, tinting, UV mapping, thumbnails and artwork; it cannot show behaviour on the Mali-400.

## Not verified

On-device rendering (GLES2 luminance-alpha textures on the Mali-400), frame times, thumbnail load times and cache behaviour on a real library, the Power hold feel, and the shutdown timing. The previews are rendered by `tools/preview/render_previews.py`, which mirrors the renderer; they are not screenshots of the device.

## Charging screen

While the player is off and charging, Y2Linux's rescue charger (`offline-charge.c`) shows a ring with a bolt, Charging / Charged / Charging paused and Hold Power to turn on. Its static images are rendered here (`charge.rs`, exported as `previews/v3/charge-layout.json`); only the sweeping segment is drawn by the charger. It shows no percentage and no time to full: the battery estimate is provisional and time-to-full is not computed.

## Open product questions

Where the output device belongs (bottom-left today), a search screen, playlists (Reborn has none) and the wording of Saving your place.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
