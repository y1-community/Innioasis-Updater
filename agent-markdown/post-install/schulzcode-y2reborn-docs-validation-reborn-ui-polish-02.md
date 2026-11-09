---
title: "REBORN-UI-POLISH-02 — physical-device legibility validation - Innioasis Updater"
description: "REBORN-UI-POLISH-02 — physical-device legibility validation <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-ui-polish-02.html"
---

# REBORN-UI-POLISH-02 — physical-device legibility validation - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# REBORN-UI-POLISH-02 — physical-device legibility validation

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# REBORN-UI-POLISH-02 — physical-device legibility validation > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Status: host-validated candidate; manual Y2 installation and physical viewing remain intentionally pending.

This is a presentation-layer polish pass on the reset UI. `AppModel`, typed `Action`/`Effect` flow, platform services, playback, storage, radios, power, and the native GLES renderer remain in place. Y2Linux source was not changed.

## Native-size review

All previews are deterministic Quad renders at exactly 480×360. They were reviewed at 1:1 pixel size after rasterization; the supplied reference PNGs were used as composition targets, never as shipped UI backgrounds.

Preview directory:

`/home/luca/Dokumente/Code/Y2Reborn/out/reborn-ui-polish-02/previews/`````````````````

| Screen | Preview |
| --- | --- |
| Now Playing | now-playing.png |
| Library | library.png |
| Artist | artist.png |
| Queue | queue.png |
| Settings | settings.png |
| Quick Settings | quick-settings.png |
| Lock / minimal player | lock.png |
| Boot | boot.png |

The preview generator is `app/reborn/src/bin/reborn-preview.rs`; the host rasterizer is `tools/preview/render_previews.py`.

## Physical-size tokens

The pack palette remains the source of truth. `TEXT_MUTED` is lifted from the pack's `#747A83` to `#858B93` for functional readability at normal handheld distance; operational secondary information uses the unchanged brighter secondary tier. No screen contains required information below 12 px.

| Token | Polish value |
| --- | --- |
| Hero / track title | 26 px |
| Screen title | 22 px |
| Section title | 18 px |
| Primary row | 16 px |
| Body | 14 px |
| Secondary / compact functional | 12 px |
| Decorative label only | 10 px |
| Normal interactive row | 54 px |
| Status bar | 32 px |
| Mini-player strip | y=306, 54 px |
| Now Playing artwork | 168×168 px |
| List artwork | 48×48 px |
| Album grid | 2×2 visible, 72 px artwork |
| Focus outline | 2 px warm gold |

Functional text advance was tightened from the reset pass to reduce tracking on the physical panel. Integer coordinates are retained throughout the screen composition. DejaVu Sans and DejaVu Serif are the packaged, licensed atlas fonts (`assets/fonts/DejaVu*.LICENSE`) used by the existing native renderer.

## State and focus policy

`Canvas::active_panel` is used for current/selected state: a quiet surface, gold icon/text, and a small accent marker. `Canvas::focus_panel` is reserved for the one item that Select would activate. `Quad.focus_target` is validation metadata ignored by native rendering; UI tests count it to enforce the one-focus invariant.

Playing/current state is separate from focus. Disabled items remain muted and are not focusable. Modal composition clears the underlying focus markers before emitting its single modal target.

## Screen-by-screen report

### Now Playing
  - Primary: 168 px artwork, 26 px title, 18 px artist, visible progress and

12 px elapsed/remaining time.
  - Secondary: 14 px album and a single readable `codec · sample rate` line;

channel count was removed from the normal view.
  - Smallest functional font: 12 px.
  - One focused target: the volume panel, matching the screen's wheel semantics.
  - No mini-player; the lower strip is volume, output, and gain status.
  - Runtime titles and metadata use ellipsis when necessary; no continuous

marquee is used.
  - Playback glyphs are state indicators, not touch buttons.

### Library
  - The six-card grid was replaced with four cards in a 2×2 wheel window.
  - Album title is 14 px and artist is 12 px; the library rail is 14 px body

text with 22 px icons.
  - One focused album card; the active `Albums` category uses only the active

marker and does not look focused.
  - Four list rows are visible on non-album library pages.
  - Mini-player is reserved at the bottom and never overlaps content.
  - Runtime album/artist names may truncate; static category labels do not.

### Artist
  - Artist name is 26 px with real track/album counts; fabricated genre copy was

removed.
  - Two readable top tracks and two real album entries are shown; the wheel can

scroll the underlying collection instead of shrinking the content.
  - One focused action/track target; album artwork is informational on this view.
  - Mini-player is present with a fixed 54 px reservation.

### Queue
  - Current track is separated from `Up Next` with a gold current marker.
  - Four 48 px queue entries are shown with 16 px titles, 12 px artist/status

lines, 12 px durations, and 36 px artwork.
  - Exactly one upcoming row is focused; current/playing is not a focus outline.
  - Permanent right-side menu/drag handles were removed. Queue operations remain

available through the physical Menu/context action, including explicit Move Up/Move Down actions.
  - No mini-player is shown because Queue already owns the current-track area.

### Settings
  - The pack's left-category/right-value composition is retained.
  - Categories use 14 px text; setting labels use 16 px; values use 12 px.
  - Three 54 px rows are visible at once; scrolling is intentional.
  - Exactly one right-pane row is focused. The selected left category is active

only, with a marker and gold icon.
  - Static names were shortened to `Equalizer` and `Audio Info`; no controlled

label is ellipsized.
  - Mini-player is present and occupies the explicit bottom strip.

### Quick Settings
  - Two large focused connectivity cards remain the first page.
  - Real lower status panels are `Paired Devices`, `Saved Networks`, `Output`,

and `Screen Timeout`; the unsupported `Network & Sync` placeholder was removed.
  - Card titles are 18 px and states are 12 px natural-language values such as

`None`, `1 saved`, `Off`, or `Wired`.
  - One focused card; lower status panels are not presented as fake touch

controls. Mini-player is present.

### Lock / minimal player
  - Artwork is 128 px to make room for a readable sequence: 18 px title, 14 px

artist, 12 px album, progress, 12 px times, transport indicators, and output/volume status.
  - The view is a non-navigable minimal playback state, so it has no navigation

focus target; physical playback/volume controls remain global.
  - It has no mini-player and no permanent footer branding. Actual display sleep

still powers the panel off rather than continuously rendering this view.

### Boot
  - Reborn/Y2 identity and the pack's artwork-led composition remain unchanged.
  - The progress bar is now explicitly indeterminate (`STARTING REBORN`) rather

than implying a fabricated percentage.
  - Branding remains here because it is a boot/loading context, not an

operational footer.

## Truncation and animation

Static labels are authored to fit their controlled bounds. Runtime track, artist, album, Bluetooth, Wi-Fi, and SSID strings use a single ellipsis policy; there is no always-running marquee and no decorative animation loop. A future focused-item marquee, if needed on-device, must remain delayed and singular.

## Physical input contract retained

The existing input boundary remains:

`evdev device/keycode → InputManager → NormalizedInput → ActionRouter → Action → Ui/AppModel → Effect → service`

The audited physical mappings are:````````````````````````````````````

| Physical control | Linux source | Normalized event | Semantic action |
| --- | --- | --- | --- |
| Select | Y2 navigation buttons, EV_KEY 28 | press/release; long at 650 ms | Select / ContextMenu |
| Back | Y2 navigation buttons, EV_KEY 158 | press/release; long | Back / Home |
| Previous | navigation 105 or keypad 165 | press/release/repeat; long | Previous / SeekBackward |
| Next | navigation 106 or keypad 163 | press/release/repeat; long | Next / SeekForward |
| Play/Pause | navigation 164 or keypad 57 | press/release; long | PlayPause / ShowNowPlaying |
| Power | mtk-pmic-keys, EV_KEY 116 | press/release; long | ScreenSleep / ScreenWake / PowerMenu |
| Volume − | any supported device, EV_KEY 114 | press/repeat | VolumeDown |
| Volume + | any supported device, EV_KEY 115 | press/repeat | VolumeUp |
| Wheel clockwise | click wheel EV_REL 8 or key 108/109 | WheelClockwise | list down, or volume up in Now Playing |
| Wheel counter-clockwise | click wheel EV_REL 8 or key 103/104 | WheelCounterClockwise | list up, or volume down in Now Playing |

Long-press threshold is 650 ms; repeat starts at 400 ms and repeats every 90 ms. Wheel acceleration is centralized and caps at six steps. Long press suppresses the matching short release. Only Power produces ScreenWake while the display is off; volume and selected playback controls continue without waking, while wheel/navigation/select/back are ignored.

## Validation performed for this pass
  - `cargo fmt --all -- --check`
  - `cargo test -p reborn-ui` — 10 passed, including one-focus, static-label,

wheel, context-menu, destructive-confirmation, and password-hiding tests.
  - `cargo check --workspace`
  - deterministic preview generation and native 480×360 rasterization
  - Y2Linux working tree remained unchanged; no platform patch was required

ARM release, offline Buildroot/rootfs packaging, hashes, and manual installation coordinates are recorded after the committed source is built.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
