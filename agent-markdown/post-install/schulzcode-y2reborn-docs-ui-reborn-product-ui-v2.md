---
title: "Reborn Product UI v2 - Innioasis Updater"
description: "Reborn Product UI v2 <!-- knowledge-base-scope: source-contract -- Source-contract scope. This page describes the Product UI v2 source Reborn 0.2.0. See current state ../"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-product-ui-v2.html"
---

# Reborn Product UI v2 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Product UI v2

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Product UI v2 > **Source-contract scope.** This page describes the Product UI v2 source > (Reborn 0.2.0). See [current state](../CURRENT_REBORN_STATE.md) for what is > installed and physically observed; built does not mean qualified. 

Reborn is a dedicated music player for the Innioasis Y2 (480×360, scroll wheel and buttons, no touch). Product UI v2 keeps the existing visual language (dark background, warm gold accent, one licensed sans atlas, one icon atlas) and removes everything a listener does not need. The navigation tree is in [REBORN-PRODUCT-NAVIGATION-V2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-NAVIGATION-V2.md); the platform boundary is in [platform-api-boundary](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fplatform-api-boundary.md); the audit and pruning ledger is in [REBORN-PRODUCT-PASS-V2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Freview%2FREBORN-PRODUCT-PASS-V2.md).

## Principles
  - Every normal screen answers "would a person using a music player use

this?". If not, it is removed, merged, moved to Diagnostics or hidden.
  - Normal screens never show Linux, driver, service, transport, schema or

signing vocabulary. A test fails the build if they do (`normal_screens_never_show_engineering_terms_or_generic_unavailable`).
  - There is no generic "Unavailable". A state names itself: Wi-Fi Is Off,

No SD card, Connecting…, Connect to Wi-Fi to Check for Updates, Updates Are Installed with a Computer, Song Not Found.
  - A problem state has a short heading, one explanation and one useful

action. Raw errors appear only in Diagnostics.
  - Exactly one focus on every interactive screen. Static fact pages

(Battery, Storage, Song Info) have no focus because nothing on them acts.

## Layout system``

| Region | Geometry | Content |
| --- | --- | --- |
| Status bar | 0–28 px | Playing glyph (gold) · Wi-Fi and Bluetooth glyphs (bright when connected) · battery % and icon, + while charging, red when low |
| Title | y 40, 20 px | Screen name; long lists show a muted position counter |
| Content | 76–316 px | Five 46 px rows on a 48 px pitch, or hero + facts + rows |
| Footer | 324–360 px | Mini player (art, title, artist, state) or one status line (radio progress/problem) |

  - Rows: 15 px label, 12 px secondary, optional 12 px duration. Focus is a

gold outline with a warm fill; the playing track has a small gold play glyph. Long lists draw a thin scroll rail.
  - Hero: 20 px heading (up to two lines) and 14 px body (up to three

lines) for off, empty, progress and error states.
  - Facts: two columns, 14 px label left and value right, 34 px pitch.
  - Sheets (Quick Settings, options, pickers, confirmations): centred,

sized to content, up to six 40 px rows; destructive confirmations start on Cancel and name their action (Power Off, Forget, Rebuild).
  - Toasts: one line above the footer for 1.8 s.

Minimum functional text is 12 px; normal list text is 15 px. Accent gold is used for focus, the playing glyph, progress and active shuffle/repeat only.

## Screens

Home — Music, Now Playing (current title), Queue (song count), Settings.

Music — Albums, Artists, Songs, Folders. Album and Artist pages show art, name and secondary line above Play All, then tracks; album rows omit the artist when it equals the album artist. Folders' roots are Internal Storage and SD Card. Empty lists explain themselves (No Music Yet, *Finding Your Music…*, Library Scan Didn't Finish, Can't Read Your Music) and offer Scan for Music where useful.

Now Playing — 176 px art, title (up to three lines), artist, album, state (Playing, Paused, SD card removed, No audio output with one hint), progress with elapsed/remaining, and a volume bar. The wheel changes volume by a fixed 2 per detent; Select opens Now Playing options: Show Queue, Shuffle, Repeat, Go to Album, Go to Artist, Song Info. The footer shows the output and shuffle/repeat state.

Queue — ordered occurrences, the current one marked. Hold Select: Play Now, Remove from Queue, Move Up, Move Down, Clear Upcoming (confirmed).

Song Info — Title, Artist, Album, Length, Format (`FLAC · 96 kHz`), File, Location (Internal Storage / SD Card).

Settings — Wi-Fi, Bluetooth, PC Transfer, Audio, Playback, Library, Display, System, each with a one-line summary.
  - Wi-Fi: Wi-Fi toggle, joined network first (Connected, Connecting…,

Getting network address…, Connected · No internet, *Couldn't connect*), saved and nearby networks with signal words, Search Again. Off: Wi-Fi Is Off + Turn On Wi-Fi. Problems in the footer: wrong password, no address, no name lookup, network not found.
  - Bluetooth: toggle, devices (Playing audio · AAC, Connected,

Paired, Not paired), Search for Devices. A connected device opens Disconnect, Use for Audio, Codec (only with a real choice), Forget Device.
  - PC Transfer: Connect to a Computer, Preparing PC Transfer…, *PC

Transfer Ready*, PC Transfer Disconnected, free space and *Scan for New Music*.
  - Audio: Output (picker: Headphone jack and connected Bluetooth

devices), ReplayGain (Off/Track/Album).
  - Playback: Shuffle, Repeat (Off/All/One), Gapless Playback, Crossfade

(Off/3/6/10 s).
  - Library: Internal Storage and SD Card song counts, *Scan for New

Music*, Rebuild Library (confirmed; re-reads every file, never empties the library).
  - Display: Brightness (20–100 %, shown only when the backlight has

levels), Screen Timeout (15 s – 5 min, Never).
  - System: Battery, Storage, Software Update, About, Reset &

Maintenance, Diagnostics, Restart, Power Off.

Battery — charge % when the platform publishes a valid estimate and the charging state; Low Battery / Battery Critically Low heroes. Transitions to Low and Critical are announced once by a toast.

Storage — Internal Storage and SD Card as 3.2 GB free of 6.4 GB, *No SD card* or SD card error · Reinsert the card; Storage Running Low / Storage Almost Full heroes.

Software Update — Software Update (check), Checking for Updates…, Up to Date, Update Available (download), Downloading Update…, *Ready to Install* (Restart to Install / Cancel Update, confirmed), *Installing Update…*, and named failures (Connect to Wi-Fi to Check for Updates, Updates Are Installed with a Computer, Not Enough Space for the Update, Update Couldn't Be Verified, Update Didn't Finish). No keys, sequences, manifests or journals.

About — Reborn 0.2.0, System Y2Linux 1.0.0, Device Innioasis Y2, Licenses.

Reset & Maintenance — Reset Reborn Settings, Forget Wi-Fi Networks, Remove Bluetooth Pairings, Rebuild Music Library, Clear Cache. Each is a real operation behind a confirmation that states its consequence. A full user-data wipe is not offered on the device.

Quick Settings (hold Power) — Wi-Fi and Bluetooth toggle in place, Output, Brightness, Restart, Power Off.

Diagnostics (Settings → System → Diagnostics) — see the [navigation map](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-NAVIGATION-V2.md%23diagnostics-tree&anchor=diagnostics-tree).

## Boot and shutdown

The early splash (Y2Linux `tools/graphics/reborn-splash.c`) shows the Reborn wordmark, one thin white bar and a short status line on the product background. Its pixels are generated from Reborn's own boot screens (`reborn_ui::boot_screen`) and a cross-repository test proves the splash and Reborn's hand-off frame are identical. The bar fills to coarse real startup milestones and never shows a number. The splash keeps the display until Reborn's first complete UI frame is ready (Reborn itself starts last, after the platform services and enabled radios are up); that frame is presented under the full boot screen, which is revealed over ten frames (~340 ms) with input held until it is done. See [boot progress and hand-off](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fboot-handoff.md).

On a platform shutdown or restart intent Reborn dissolves the UI into the same screen (Saving), saves the session and closes audio and the library database, shows Shutting down (or Restarting, Battery empty) while the bar drains and the screen dims, presents a black frame, turns the backlight off and then acknowledges (23 frames at ~34 ms ≈ 0.8 s of visuals plus the save time). The platform turns the backlight off before it stops a Reborn that did not acknowledge, and again before init powers down, so a crashed or hung Reborn cannot leave a lit panel.

## Wheel

One physical detent is one step everywhere. Only long library lists (Albums, Artists, Songs, Folders, Album, Artist with at least 40 rows) honour the input layer's acceleration, which needs a sustained rotation of four or more detents and resets on a 220 ms pause or reversal. Settings, Queue, sheets and password entry move one row, item or value per detent; Now Playing changes volume by a fixed step. See [the pass report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Freview%2FREBORN-PRODUCT-PASS-V2.md%237-wheel&anchor=7-wheel).

## Previews

The 480×360 previews of every state were in `previews/v2/` (replaced by the [v3 previews](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/ui/previews/v3/) in Reborn 0.3.0), rendered from the production UI code by `reborn-preview` and `tools/preview/render_previews.py`.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
