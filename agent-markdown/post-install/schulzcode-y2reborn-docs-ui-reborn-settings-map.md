---
title: "Reborn settings map - Innioasis Updater"
description: "Reborn settings map <!-- knowledge-base-scope: source-contract -- Source-contract scope. Where every setting lives since 1.0 Beta 9.2.10 and the rules for adding one. Cod"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-settings-map.html"
---

# Reborn settings map - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn settings map

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn settings map > **Source-contract scope.** Where every setting lives (since 1.0 Beta 9.2.10) and the rules for adding > one. Code: `crates/reborn-ui/src/pages.rs` (`settings`, `system_menu`, `library`, Sound, Display), > `crates/reborn-ui/src/customize.rs` (Customize's pages, pickers and hints). 

## Before you add a setting

First find the right place, then add the setting. A new setting never goes "somewhere for now". Ask:
  - Is it needed at all? Prefer a good default to a setting (the project keeps Reborn free of feature

creep; requests that only some people want belong to plugins later).
  - Which question does it answer? Pick the place below whose question it answers. If two seem to fit,

take the one a listener would open first when looking for it.
  - Does the page still fit one screen? At most six rows on a page (the root holds eight). If a page

would get a seventh, group related rows into a sub-page of their own with a name that says what is inside, rather than letting the page scroll.
  - Name it by what it does, show its value. The row's label says what changes ("Buttons While Screen

Off", not "When Screen Off"); its value on the right says what it is now ("Play Buttons", not "On").
  - Use the matching control. On/off: a switch. Two named choices: Select steps them, the value shows

which. Three or more: a picker page with a check mark on the current choice. A level or a time: a picker or a card with a slider.
  - Give it a hint. Customize's settings carry one line at the bottom saying what the setting in focus

does (`customize::hint`); pickers say what each choice means.
  - Update this map and the previews (`app/reborn/src/bin/reborn-preview.rs`) in the same change.

A session is saved with its screen: a new page is a sub-page (an existing screen plus a navigation filter, as `Screen::Customize` with "browsing") unless older versions can read a new `Screen` value, so that Restore Previous System does not throw the session away.

## The places

| Place | The question it answers |
| --- | --- |
| Bluetooth | Which headphones or speakers play? |
| Wi-Fi | Which network is the player on? |
| Sound | How does the music sound, and where does it go? |
| Display | How bright is the screen, and when does it turn off? |
| Skin | How does Reborn look? |
| Customize | How does Reborn behave: Home, the lists, the wheel and the buttons? |
| Library | Where is my music, and where does my listening go? |
| System | The player itself: updates, the clock, reports, resets, about. |

## The tree`Settings ├ Bluetooth devices, Search for Devices ├ Wi-Fi networks, Other Network… ├ Sound Equalizer › · Normalize Volume · Balance › · Playback › · Output card › │ ├ Playback Gapless Playback · Crossfade › │ └ Output Headphone Jack / Bluetooth devices · Speaker · Headphone Level › · DAC Filter › ├ Display Brightness card · Screen Off After › ├ Skin the skins ├ Customize Home Menu › · Browsing › · Wheel & Buttons › │ ├ Home Menu the places on Home and their order │ ├ Browsing Cover Flow · Sort Albums · Artist's Albums › · Artists List │ │ · Lists Wrap Around › │ └ Wheel & Buttons Wheel on Now Playing · Wheel Click · Haptics › · Buttons While Screen Off › ├ Library Scan for Music · Storage › · Last.fm › └ System Software Update › · Time Zone › · Date & Time › · Error Reports › · Reset & Maintenance › · About › (About › Version, tapped seven times: the service menu — codecs, Battery, Sleep, Diagnostics)`

Software Update ends with Update Notifications (a toggle, off by default, Y2Reborn #97): when it is on, Reborn looks at the platform every two minutes while Wi-Fi is up, and when the platform's daily check has found a newer version the status bar says "Software update available" once for that version (not on Software Update itself, which shows it). The toggle is under every Software Update page that has a choice, not while a check or install runs.

Library's hint line names the audio the last scan left out because Reborn cannot play its type ("43 files can't be played here (WMA, DSD), so they aren't in your library.", Y2Reborn #104); without such files there is no line.

Shuffle and Repeat are on Now Playing's menu, the sleep timer on Now Playing too: things you change while listening stay where you listen.

## The Quick Menu (hold Power)

Since 1.0 Beta 9.3.15 (Y2Linux #85), holding Power on any screen opens the Quick Menu; releasing keeps it open, Back or a short press of Power closes it. It holds what people change on the go, without walking into Settings, and nothing else:`┌ Quick Menu ─────────────────────────── Battery 72 % ┐ a centred panel; it grows in over the │ [ Wi-Fi network ] [ Bluetooth device ] │ dimmed screen, the tiles one after another │ [ ☀ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━○────── 60 % ] │ │ [ ☾ Sleep Timer ] [ ↻ Restart ] [ ⏻ Power Off ] │ └────────────────────────────────────────────────────┘`

The wheel goes Wi-Fi → Bluetooth → Brightness → Sleep Timer → Restart → Power Off; the menu opens on Brightness. Wi-Fi and Bluetooth: Select switches them, the tile fills with the accent while on. Brightness: Select, turn the wheel, Select (the Display card's adjustment). Holding Select on Wi-Fi, Bluetooth or Brightness opens Settings' Wi-Fi, Bluetooth or Display page instead, to choose a network or a device (Y2Reborn #101); the menu closes and Back returns to the screen it was opened on. Sleep Timer opens the timer's picker. Restart and Power Off act at once and wait while the platform works (an update). Keep holding Power with the menu open: after 3 s a ring fills around the Power Off tile ("Hold to Turn Off") and turns the player off 1.2 s later, as a hold always did; the hardware resets the player after 10 s. Over the keyboard, a pairing question or a message the full-screen ring starts at once. Skins get the same panel in their palette. Each control is also where it always was in Settings; anything added here must be a quick control that already has its place in the tree (six tiles fill the panel). Code: `crates/reborn-ui/src/quick_menu.rs` (rows, actions), `views_quick.rs` (the panel).

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
