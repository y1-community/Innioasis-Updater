---
title: "Reborn Product UI v2 navigation and focus map - Innioasis Updater"
description: "Reborn Product UI v2 navigation and focus map <!-- knowledge-base-scope: source-contract -- Source-contract scope. Routes of the Product UI v2 source. See current state ."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-product-navigation-v2.html"
---

# Reborn Product UI v2 navigation and focus map - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Product UI v2 navigation and focus map

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Product UI v2 navigation and focus map > **Source-contract scope.** Routes of the Product UI v2 source. See > [current state](../CURRENT_REBORN_STATE.md) for the installed build. 

## Global controls

| Control | Short press | Hold |
| --- | --- | --- |
| Wheel | Move one row / item / value (Now Playing: volume ±2) | — |
| Select | Open / act | Context options of the focused item; in password entry: connect |
| Back | Parent screen (restores focus and scroll) | Home |
| Play/Pause | Play / pause anywhere | Now Playing |
| Previous / Next | Previous / next track | Seek −/+ 30 s, repeating |
| Volume − / + | Volume (works with the screen off) | Repeats |
| Power | Screen off / on | Quick Settings |

With the screen off only transport, volume and Power act. Sheets trap focus; Back closes them and restores the screen underneath. During an update install or a shutdown only wake and volume act.

## Normal navigation tree`Home ├── Music │ ├── Albums ─ Album ─ (Play All, tracks) │ ├── Artists ─ Artist ─ (Play All, Albums by this Artist → Albums, songs) │ ├── Songs ─ (Jump to Letter) │ └── Folders ─ Internal Storage / SD Card ─ folders ─ songs ├── Now Playing ─ options: Show Queue, Shuffle, Repeat, Go to Album, Go to Artist, Song Info ├── Queue ─ options: Play Now, Remove, Move Up, Move Down, Clear Upcoming └── Settings (since 9.2.10 see REBORN-SETTINGS-MAP.md: the places, the tree and the rules for adding a setting) ├── Wi-Fi ─ network options: Connect/Disconnect, Forget Network; password entry ├── Bluetooth ─ device options: Pair/Connect/Disconnect, Use for Audio, Codec, Forget Device ├── PC Transfer ├── Audio ─ Output picker, ReplayGain ├── Playback ─ Shuffle, Repeat, Gapless Playback, Crossfade ├── Library ─ Internal Storage, SD Card, Scan for New Music, Rebuild Library ├── Display ─ Brightness, Screen Timeout └── System ├── Battery ├── Storage ├── Software Update ├── About ─ Licenses ├── Reset & Maintenance ├── Diagnostics (technical subtree, below) ├── Restart (confirmed) └── Power Off (confirmed) Hold Power: Quick Settings ─ Wi-Fi, Bluetooth, Output, Brightness, Restart, Power Off`

## Route table[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V2.md%23screens&anchor=screens)

| Screen | Parent | Focus order | Context (hold Select) | Empty / loading / error |
| --- | --- | --- | --- | --- |
| Home | — (Back no-op) | Music → Now Playing → Queue → Settings | — | — |
| Music | Home | Albums → Artists → Songs → Folders | — | — |
| Albums / Artists | Music (or Artist) | Alphabetical rows | Jump to Letter | No Music Yet / Finding Your Music… / Scan Didn't Finish / Can't Read Your Music + Scan for Music |
| Album | Albums, Now Playing, song options | Play All → tracks (disc, track order) | Play All: Play, Shuffle, Play Next, Add to Queue; track: song options | As above |
| Artist | Artists, options | Play All → Albums by this Artist → songs | As Album | As above |
| Songs | Music | Title order | Play, Play Next, Add to Queue, Go to Album, Go to Artist, Song Info, Jump to Letter | As above |
| Folders | Music / parent folder | Folders, then songs | Song options | As above |
| Jump to Letter | Albums/Artists/Songs | Letters present | — | — |
| Now Playing | Any (Back restores) | Volume bar (wheel) | Select or hold: Now Playing options | Nothing Playing + Open Music |
| Queue | Home, Now Playing options | Occurrences | Queue options | Queue Is Empty + Open Music |
| Song Info | Song options | Static facts | — | Song Not Found |
| Settings | Home | Wi-Fi → … → System | — | — |
| Wi-Fi | Settings, Software Update | Toggle → networks → Search Again | Saved network: Connect/Disconnect, Forget | Is Off + Turn On; Is Starting…; problems in footer |
| Password entry | Wi-Fi (secured network) | One character per detent; Delete, Connect, Cancel | Hold Select connects | Fewer than 8 characters: toast |
| Bluetooth | Settings | Toggle → devices → Search for Devices | Device options (Select on a connected device) | Is Off + Turn On; Is Starting…; no devices hint in footer |
| Pairing | Over any screen | Pair → Cancel | — | Disappears when the request ends |
| PC Transfer | Settings | Scan for New Music | — | Connect to a Computer / Preparing… / Ready / Disconnected |
| Audio | Settings | Output → ReplayGain | — | — |
| Output picker | Audio, Quick Settings | Headphone jack → Bluetooth devices | — | Only usable devices listed |
| Playback | Settings | Shuffle → Repeat → Gapless → Crossfade | — | — |
| Library | Settings | Internal → SD → Scan → Rebuild | — | Scan/Rebuild disabled while scanning |
| Display | Settings | Brightness (if supported) → Screen Timeout | — | — |
| System | Settings | Battery → … → Power Off | — | — |
| Battery | System | Static | — | Low / Critically Low heroes |
| Storage | System, Library | Static | — | Checking… / Running Low / Almost Full / Storage Problem; SD error |
| Software Update | System | Hero action(s) | — | See UI |
| About | System | Licenses | — | — |
| Reset & Maintenance | System | Five operations | — | Each confirmed, starting on Cancel |
| Value detail | About, Diagnostics facts | Back | — | — |

Back always returns to the parent with its focus and scroll restored (tested for every reachable route). Long Back returns Home.

## Diagnostics tree

Settings → System → Diagnostics:`Diagnostics ├── Health (Run Checks) ├── Battery SOC, source, confidence, calibration, low-battery policy, voltage, current, pack temperature, supplies ├── Storage state, space, free/total, filesystem, UUID, device, mount generation, controllers and error counters ├── Network readiness, reason, IP, route, DNS, signal, RX/TX, power save ├── Bluetooth adapter, audio service, peers, active codec, PCM format/rate/channels, transport generation, codec policy, reconnect ├── Audio source codec/rate/bits, decoded and DSP format, ReplayGain, crossfade, sink, PCM format/rate/channels, enabled formats/rates, hw_params ├── CPU & Power cores, load, memory, clocksource, highres, NO_HZ, frequency/governor, idle states, die temperatures, Reborn PSS ├── USB cable, transfer service, address, SFTP, DMA path and counters ├── Update journal, download, offered release, failures, signing key ID, sequence, rollback, scope ├── Boot & Services boot IDs, clean shutdown, last stage, reset cause, taint, clock, readiness ├── Build Information Reborn build, Y2Linux release, build ID, kernel, rootfs, source commits ├── Capabilities implemented / enabled / qualified / experimental per capability ├── Network Check · Storage Benchmark · Library Benchmark (confirmed) · Export Player Data ├── Restore Previous System (confirmed; only when a verified previous root exists) └── Latest Result`

Every fact opens its full value. Each section has Refresh (one platform observation) and Health has Run Checks.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
