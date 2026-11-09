---
title: "Reborn UI reset architecture - Innioasis Updater"
description: "Reborn UI reset architecture <!-- knowledge-base-scope: historical-design-/-runbook -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-reborn-premium-overhaul.html"
---

# Reborn UI reset architecture - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn UI reset architecture

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn UI reset architecture > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

This document records the product and architecture target for the Reborn overhaul. It is grounded in the current native Rust code, the captured Y2 input evidence, and the supplied Reborn UI Implementation Pack. It is not derived from any older player UI.

## Audit result

The visual references share a small, readable premium language:
  - near-black/navy background and slightly raised blue-black surfaces;
  - warm white primary text, cool grey secondary text, and restrained gold for

focus, progress, active state, and the primary action;
  - album art as the main visual anchor, with thin dividers and compact rounded

cards rather than dense diagnostic panels;
  - one unmistakable focus target, stable list scrolling, and minimal status

indicators;
  - a compact 480x360 layout with no touch affordances.

The superseded Reborn presentation layer had a flat text list, developer labels, a global notice string, and screen-local selection. This reset retires that presentation layer while keeping the working runtime, service, and audio systems underneath it.

## Hardware input contract

The current Y2Linux evidence identifies these devices by name. Event numbers are intentionally not part of the contract.````````````````````````````````````````

| Physical control | Linux source | Captured event | Reborn semantic action |
| --- | --- | --- | --- |
| Center / Select | Y2 navigation buttons | EV_KEY 28 press/release | Select; hold = ContextMenu |
| Back | Y2 navigation buttons | EV_KEY 158 press/release | Back; hold = Home |
| Previous | Y2 navigation buttons | EV_KEY 105 press/release | PreviousTrack; hold = SeekBackward |
| Next | Y2 navigation buttons | EV_KEY 106 press/release | NextTrack; hold = SeekForward |
| Play/Pause | Y2 navigation buttons | EV_KEY 164 press/release | PlayPause; hold = ShowNowPlaying |
| Power | mtk-pmic-keys | EV_KEY 116 press/release | screen wake/sleep; hold = PowerMenu |
| Volume - | PMIC/keypad source | EV_KEY 114 press/release/repeat | VolumeDown |
| Volume + | PMIC/keypad source | EV_KEY 115 press/release/repeat | VolumeUp |
| Wheel clockwise | mt6582-keypad | EV_KEY 108 detent | WheelClockwise |
| Wheel counter-clockwise | mt6582-keypad | EV_KEY 103 detent | WheelCounterClockwise |
| Alternate wheel | APT32F click-wheel | EV_REL 8 if emitted | WheelClockwise/CounterClockwise |

The 2026-09-18 capture contained no events from the APT32F node, while the keypad node emitted Up/Down detents. The implementation therefore supports the APT32F axis without depending on it and uses the proven keypad detent path. The direction names follow the captured keypad semantics (`Down` is the forward/clockwise direction); physical acceptance remains an owner test.

The mapping is kept behind the platform input boundary and is validated by the input tests; screen code never sees Linux event codes or device names.

## Target interaction model

Short and long-press decisions are centralized in `InputManager`:
  - long press threshold: 650 ms;
  - repeat begins at 400 ms;
  - repeat period: 90 ms for volume and navigation holds;
  - long press is emitted once and suppresses the matching short press;
  - wheel detents are independent from center/select and never activate focus.

When the screen is on, wheel rotation navigates lists except on Now Playing, where it adjusts volume. Volume keys always adjust volume. Previous/Next are global transport controls; in a list they do not become focus navigation.

When the screen is off, only Power wakes it. Volume, Play/Pause, Previous, and Next may continue to operate without waking the display. Navigation, Select, Back, ContextMenu, and wheel input are ignored without changing focus or route.

Power short toggles sleep/wake. Power long opens a confirmation-backed power menu while awake. Back short pops the explicit stack; Back long returns home; Back never stops playback. Destructive actions use a safe-default confirmation overlay.

## Product information architecture

The root is deliberately consumer-facing:
  - Music — Artists, Albums, Tracks, Folders, Scan Library.
  - Now Playing.
  - Queue — current item, Up Next, remove/reorder/clear.
  - Connectivity — Bluetooth and Wi-Fi.
  - Settings — Audio, Playback, Library, Bluetooth, Wi-Fi, Display, Power,

System.

Diagnostics remains available under System and through `rebornctl`; raw BlueZ paths, ALSA controls, FFmpeg filters, SQL errors, and errno values are not product copy.

## Rust ownership model

`AppModel` is the only owner of product state and is confined to the Reborn UI thread. Background workers own their platform/decoder handles and communicate with bounded channels. They never mutate AppModel or UI fields.

The UI module performs navigation and returns typed `Effect` values. The main application loop interprets effects through service boundaries. Service results become typed core events and are applied before the next render.

The chosen pattern is a small Elm-style update/effect loop, not a framework or a single giant reducer:`normalized input / service event -> semantic Action/Event -> UI/application update -> AppModel + typed Effect -> service command -> typed result event -> AppModel -> render(state)`

Navigation state is explicit and transient. Persisted state remains a narrow session/settings document: queue, current track, position, output, volume, ReplayGain/EQ/crossfade, timeout, and library source preferences. Renderer cache, focus animation, radio notices, and open dialogs are not serialized.

## Design tokens for 480x360

The renderer uses central tokens rather than screen-local literals:`background #090B0D raised surface #101317 surface #15191E surface hover #1B2026 surface border #2A3037 primary text #F2F1ED secondary text #AAAEB5 muted text #747A83 accent gold #E6B965 bright gold #FFD17B dim gold #7D6337 focus glow #F5C973 focus fill #211B12 success #74B68B danger #D46B65 track #444A51 screen margin 16 px status bar 30 px row 44 px now-playing art 168 px list art 42 px focus border 2 px warm gold corner radii 6 / 10 / 14 px`

Static screens render once after state change. Time/progress and temporary overlays are the only regular redraw sources; screen sleep stops normal render and animation work while playback continues.

## Validation target

Host tests cover input timing/mapping, screen-off gating, navigation invariants, queue/context-menu transitions, and serialization boundaries. Existing audio, library, radio, graphics, daemon, and ARM qualification paths remain in scope. The resulting root-only package is stopped for manual installation; no flash or protected partition write is performed by this work.

## Before/after application boundary

Before, `app/reborn` received a raw `(device, Action)` tuple, treated the action as a screen callback, and toggled the display for every input while it was off. The UI also kept its own selection while the runtime kept a second track list.

After, ownership is deliberately one-way:`Linux evdev record -> InputManager (device identity, debounce, long press, repeat, acceleration) -> NormalizedInput -> ActionRouter (screen-off policy and long/short suppression) -> semantic Action -> Ui::action (navigation + typed Effect) -> Runtime::effect (service boundary) -> bounded worker/service channel -> typed Event / authoritative AppModel -> render(AppModel, view-only service snapshots)`

`AppModel` is owned by the UI/application thread. Playback, scanner, Wi-Fi, Bluetooth, and graphics workers own their handles and communicate through bounded channels. No worker writes `AppModel`; no view calls FFmpeg, ALSA, BlueZ, wpa_supplicant, or power APIs.

The chosen pattern is intentionally a small Elm-style update/effect loop rather than a Redux dependency or a single giant reducer. The navigation module is the product update boundary, `AppModel::apply` handles asynchronous domain events, and `Runtime::effect` is the one service orchestration boundary. This keeps ownership obvious without creating a framework-sized abstraction.

## Physical-control matrix

| Control | Short press/release | Long press | Repeat / screen off |
| --- | --- | --- | --- |
| Power | sleep when on; wake when off | Power menu when on | no wake side effect from other keys |
| Select | open focused row | context menu | long suppresses short |
| Back | pop one parent route | Home | ignored while screen is off |
| Play/Pause | toggle playback | Now Playing | short works screen-off; no wake |
| Previous | previous track | seek backward | seek repeat after long; short works screen-off |
| Next | next track | seek forward | seek repeat after long; short works screen-off |
| Volume + / - | volume step | — | repeat; never navigation; never wakes |
| Wheel | focus one or accelerated list step | — | list focus, or volume on Now Playing; never Select |

The `InputManager` timing constants are centralized: 650 ms long press, 400 ms repeat start, 90 ms repeat period, and a 180 ms sustained-wheel window with a six-step cap. The application tests assert that long press suppresses short press, wheel cannot become Select, and only Power wakes the screen.

## Screen and modal model

The current screen is the single `AppModel::screen` value. The navigation stack stores parent routes only; it does not duplicate the current screen. Focus, scroll, active modal, modal focus, and context target are explicit in `NavigationState`. Modals are `ContextMenu`, `PowerMenu`, or a typed confirmation action. Confirmations default to Cancel for power, reboot, library rebuild, forget, and queue-clear operations.

The product route graph is:`Home ├─ Music ─ Artists ─ Artist ─ tracks │ ├ Albums ─ Album ─ tracks │ ├ Tracks │ └ Folders ─ Tracks ├─ Now Playing ├─ Queue ├─ Connectivity ─ Bluetooth / Wi-Fi └─ Settings ├ Audio ├ Playback ├ Library ├ Bluetooth ├ Wi-Fi ├ Display ├ Power └ System ─ Diagnostics`

Now Playing is reachable from Home, the mini-player, and a long Play/Pause. The wheel is volume there; transport keys remain global. Queue clear removes upcoming items but never silently stops the current track.

## Implemented consumer settings

The UI exposes only behavior wired to the current Rust services:
  - Audio: Wired or a connected Bluetooth output, ReplayGain Off/Track/Album,

Equalizer on/off, and a secondary Audio Information view.
  - Playback: shuffle queue ordering, repeat Off/Track/All, actual gapless

enable/disable, and crossfade Off/5/10/15 seconds.
  - Library: internal/SD source status, scan, and confirmation-backed rebuild.
  - Bluetooth: power, scan, connect/disconnect, use for audio, negotiated codec

when BlueALSA reports it, and confirmation-backed forget.
  - Wi-Fi: power, scan, saved-network connect/forget, network connect, and a

physical-control character picker whose password is masked and never logged.
  - Display: 15 s/30 s/1 min/2 min/Never timeout.
  - System: About, diagnostics, reboot, and confirmation-backed power off.

Developer concepts remain in `rebornctl`, health, metrics, logs, and detailed diagnostics. They are not primary navigation or context-menu actions.

## Loading, empty, and error behavior

Library, queue, radio, and audio-information views have explicit empty copy. Radio scan failures and service failures are translated to short recovery copy in the UI; raw errno, FFmpeg errors, SQL details, BlueZ paths, and Wi-Fi passwords stay in observability logs. Bluetooth loss pauses playback and returns the authoritative output to Wired, so the status bar cannot continue to present a disconnected Bluetooth route as active.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
