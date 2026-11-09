---
title: "Reborn UI v1 navigation and focus map - Innioasis Updater"
description: "Reborn UI v1 navigation and focus map <!-- knowledge-base-scope: ui-design-/-scoped-candidate -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-ui-v1-navigation.html"
---

# Reborn UI v1 navigation and focus map - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn UI v1 navigation and focus map

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn UI v1 navigation and focus map > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

All rows traverse top-to-bottom in displayed order, skipping disabled actions. Visible windows contain five rows, or three below album/artist art. Counter shows position/total. Select opens/acts; Back restores parent filter/focus/scroll. Long Back returns Home unless closing a modal. Every interactive view has one focus. Boot and locked root-install preparation are noninteractive and have no focus.

Global Play/Pause, Previous/Next and Volume remain available through ordinary views, dialogs, pairing and password entry, subject to the existing input router. Volume never navigates. Screen-off navigation is ignored. Long Play opens Now Playing only outside a focus trap. Long Select means Context, or password submit. An unavailable context is a deliberate no-op, not an empty menu. No touch paths.``

| Screen | Parent / child destinations and focus order | Back | Context / special long action | Empty / unavailable |
| --- | --- | --- | --- | --- |
| Startup | Boot → Home after actual startup | None | None | Meaningful service failure; no fake progress |
| Home | Music → Now Playing → Queue → Connectivity → Settings | No-op | Long Play: Now Playing | Root navigation always available |
| Music | Home; Albums → Artists → Songs → Folders → Scan | Home | None | Scan is available; child lists explain empty state |
| Albums | Music or Artist; alphabetic album rows → Album | Restore parent | Jump to Letter | Scan Library action |
| Album | Albums/context; Play All → ordered tracks | Same album position | Play All: collection actions; track: track actions | Offline/missing collection explanation, Back |
| Artists | Music; artist rows → Artist | Music | Jump to Letter | Scan Library action |
| Artist | Artists/context; Play All → Albums by Artist → songs | Same artist position | Play All: artist actions; song: track actions | Unknown artist label; no fake art |
| Songs | Music; title-ordered tracks | Music or supplied parent | Track context + Jump to Letter for unfiltered Songs | Scan Library action |
| Folders | Music/folder; child folders then direct songs | Parent folder with same focus/scroll | Track actions for files | Scan; Back always reaches parent |
| Letter Index | Songs/Albums/Artists; represented letters, # for other initials | Restore original list position | Select jumps into originating list | Back row if no index |
| Now Playing | Home/long Play; Options → Queue → Audio Info | Restore invoking route | Track context | Open Music; sink/source recovery hint |
| Queue | Home/Now Playing; ordered occurrences | Restore invoking route | Play Now → Remove → Move Up → Move Down → Clear Future | Open Music |
| Track Information | Track context; Title → Artist → Album → File → Codec → Rate → Duration → Source | Focused track | Each fact opens Value Detail | Back / track unavailable |
| Track context | Focused track; Play → Play Next → Add to Queue → Album → Artist → Information → optional Letter Index | Close, restore track focus | Wheel trapped | Closes when its catalog indexes become invalid |
| Collection context | Album/Artist Play All; Play → Shuffle → Play Next → Add to Queue → optional Audio Info | Close | Wheel trapped | No playable tracks: no playback request |
| Queue context | Queue occurrence ID; Play Now → Remove → Move Up → Move Down → Clear Future | Close | Future moves only; Clear Future confirmation | Vanished occurrence closes menu |
| Connectivity | Home/Settings; Wi-Fi → Bluetooth → PC Transfer → Quick Settings | Parent | None | Explicit unavailable radio summaries |
| Quick Settings | Connectivity; Wi-Fi → Bluetooth → Output → Display → System Settings | Connectivity | None | Unavailable service facts/guarded effects |
| Wi-Fi | Connectivity/Quick Settings; Power → Scan → saved networks → other networks → Disconnect → Details → error detail | Invoking parent | Saved network: Connect → Forget → Disconnect → Details | Unsupported security disabled; unavailable adapter controls skipped |
| Wi-Fi Password | Unsaved secured network; circular characters → Delete → Connect → Cancel | Cancel and clear secret | Long Select submits valid passphrase | Invalid length never submits; typed content not drawn |
| Wi-Fi network context | Saved network | Close | Forget confirmation | Missing service failure remains visible |
| Bluetooth | Connectivity/Quick Settings; Power → Scan → Wired Output → devices → Codec/Audio Details → error detail | Invoking parent | Peer: Pair/Connect/Disconnect → Use for Audio → Forget → Details | Disabled radio controls; Wired Output and details remain reachable |
| Bluetooth pairing | Async request over current view; Confirm → Cancel; starts at Cancel | Reject and restore background | Globals remain available | Timed-out request disappears with service observation |
| Codec Preference | Bluetooth Audio; Preference → SBC → Auto → Stop Playback → Active Codec/PCM → Refresh | Bluetooth Audio | No codec inferred from preference | Auto/no eligible codec disabled; apply only stopped/connected |
| Settings | Home; Audio → Playback → Library → Connectivity → Storage → Display → Power → System | Home | None | Static hierarchy |
| Audio Settings | Settings/Quick output; Output → ReplayGain → Audio Info | Parent | Select cycles actual supported values | No fake gain/filter/EQ toggles |
| Playback Settings | Settings; Shuffle → Repeat → Gapless → Crossfade | Settings | Select cycles stored settings | Existing playback model only |
| Library Settings | Settings; Internal → SD → Scan → Rebuild → Scan Status | Settings | Rebuild opens distinct owner-maintenance scope | Scan status explains partial/failure and retained rows |
| Display | Settings/Quick; Screen Timeout | Parent | Select cycles 15/30/60/120/off | No unimplemented brightness/theme |
| Power | Settings; Battery/Source → Power Menu | Settings | Physical long Power also opens menu | No battery percentage |
| System | Settings/Quick; About → Update → Backup → Maintenance → Date/Time → Diagnostics | Parent | None | Static hierarchy |
| About | System; Reborn → Y2Linux → Kernel → Output → Build Information → Refresh | System | Select fact: full value | Missing observation explicitly unavailable |
| Build Information | About; release/build/output/compiled IDs/rootfs facts → Refresh | About | Select fact: full value | No guessed repository/package identity |
| Storage | Settings/Library/Diagnostics/USB; internal state/capacity/fs → SD state/capacity/fs if mounted → root state/capacity/fs → Refresh | Invoking parent | Facts open details | Missing SD collapses unused capacity rows; low space guidance |
| Power & Battery | Power/Diagnostics/Thermal; unavailable SOC explanation → actual supply/charging/voltage/source → low-battery policy → Refresh | Parent | Facts open details | Current/pack temperature explicitly unavailable |
| Date & Time | System; trust → sync source → timestamp only when valid → Refresh | System | Facts open details | Untrusted clock guidance |
| PC Transfer | Connectivity/Backup/Diagnostics; protocol → cable → readiness → address → authentication → activity availability → Wi-Fi exclusion → storage → Refresh | Parent | Facts open details | Disconnected/unavailable states retained |
| Software Update | System; release → state → Check → Stage → Install → available release → network → cancel → rollback → result → details → Refresh | System | Install/cancel/rollback confirmation | Actions depend on capabilities, journal and operation state |
| Update Details | Update/Diagnostics; journal/download/signature/result/scope/key/sequence/rollback facts and admitted actions → result → Refresh | Parent | Same confirmation rules | Absent key/progress remain unavailable |
| Install preparation | Confirmed root apply/restore | Temporarily blocked | Navigation/power/transport conflict suppression; wake/volume permitted | Failure unlocks route; platform owns restart |
| Backup & Export | System/maintenance; purpose → included → excluded → Create Export → Result → PC Transfer → Refresh | Parent | Safe platform export | No archive path until actual completion |
| Reset & Maintenance | System; Settings → Network → Bonds → Library → Cache → Full User Data | System | No destructive one-click effects | Requires authenticated USB stopped-service maintenance |
| Each reset scope | Maintenance/Library; owner requirement → exact scope → plan command → digest workflow → consequences → Backup → PC Transfer | Parent | Full user scope explains music removal separately | No false reset-success button |
| Diagnostics | System; Health → Result → Capabilities → CPU/Memory → Thermal/Power → Storage → Network → Bluetooth → Audio → USB → Update → Boot/Services → Checks | System | None | Observations remain explicitly unavailable |
| Platform Health | Diagnostics; overall → Refresh Health → observed subsystem checks → Refresh | Diagnostics | Select opens state/reason | Qualification pending is not failure |
| Capabilities | Diagnostics; observed capability rows → precision/codec/rate details → Refresh | Diagnostics | Select opens implemented/enabled/qualified summary | Unknown schema rejected upstream |
| CPU & Memory | Diagnostics; online/load/memory → frequency/governor → RSS/PSS → cache/slab → Refresh | Diagnostics | Select fact | No invented utilization/residency |
| Thermal & Power | Diagnostics; sensor explanation → die zones → cooling → Battery/Source → Refresh | Diagnostics | Select fact | Never labels die temperature as battery |
| Network Details | Wi-Fi/Diagnostics; readiness/reason/IP/route/DNS/signal/RX/TX → passive Network Check → Refresh | Parent | Select fact | No fabricated Online or credentials |
| Bluetooth Audio | Bluetooth/Diagnostics; peer → active codec → observed PCM format/rate/channels → preference → codec policy → adapter/trust/reconnect → Refresh | Parent | Codec preference child | No active codec without observation |
| Audio Information | Now Playing/Audio/Diagnostics; source → decode/process → RG/EQ/crossfade → selected output → observed sink → hw params → Refresh | Parent | Select fact | Inactive sink labeled last opened |
| Boot & Services | Diagnostics; boot IDs/clean state/stage/reset cause/taint → observed readiness → Refresh | Diagnostics | Select fact | Unknown reset cause remains unknown |
| Advanced Checks | Diagnostics; Result → Health → Network → Storage Benchmark → Library Benchmark → Refresh | Diagnostics | Benchmarks require confirmation | Busy/capability gates skip disabled controls |
| Operation Result | Update/Backup/Diagnostics/Checks; actual result/error → available export/checksum/benchmark metrics → Refresh | Parent | Select fact | Explicit no completed operation; no fake progress |
| Value Detail | Any fact; wrapped text → Back | Same fact and scroll position | No extra context | Bounded text with ellipsis; unavailable is readable |
| Power Menu | Long Power/Power Settings; Off → Restart → Cancel; starts at Cancel | Close | Off/Restart then confirmation | No recovery/partition controls |
| Confirmation | Invoking context; Cancel → Confirm; starts at Cancel | Close | Focus trapped, live admission rechecked | Invalidated Confirm disabled |
| Notice / volume indication | Noninteractive top overlay; no focus target | Underlying route | Expires with one final dirty redraw | Never replaces persistent error/result authority |
| Screen off / wake | Actual platform panel blank; retained route on wake | Navigation ignored while off | Playback/volume global under router; Power wakes | No persistent decorative lock view |

The physical focus test is automated over every normal screen and platform page, with empty/populated variants. Every enabled row is reached deterministically by wheel-only traversal and Back returns to a parent/root. Hardware input timing, legibility and physical focus visibility require owner qualification.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
