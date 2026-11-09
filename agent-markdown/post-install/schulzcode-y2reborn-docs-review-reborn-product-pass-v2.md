---
title: "Reborn Product Pass v2 — audit, decisions and ledger - Innioasis Updater"
description: "Reborn Product Pass v2 — audit, decisions and ledger <!-- knowledge-base-scope: scoped-validation-record -- Scoped record, 2026-10-01. Software pass on the CPU Final Fix0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-review-reborn-product-pass-v2.html"
---

# Reborn Product Pass v2 — audit, decisions and ledger - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Product Pass v2 — audit, decisions and ledger

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Product Pass v2 — audit, decisions and ledger > **Scoped record, 2026-10-01.** Software pass on the CPU Final Fix03 base > (Linux `76a5d41`/`aef3ab8`, Reborn `77cf83e`). Built and validated, not > flashed or physically qualified. Exact candidate identity and hashes are > in the [Y2Linux receipt](https://github.com/SchulzCode/Y2Linux/blob/main/docs/validation/Y2-REBORN-PRODUCT-UI-V2.md). 

Design: [Product UI v2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V2.md) · [navigation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-NAVIGATION-V2.md) · [platform boundary](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fplatform-api-boundary.md) · previews (v2, since replaced by the [v3 previews](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/ui/previews/v3/)).

## 1. Product simplification

| Measure | Before (UI v1) | After (v2) |
| --- | --- | --- |
| Root items | 5 (Music, Now Playing, Queue, Connectivity, Settings) | 4 (Music, Now Playing, Queue, Settings) |
| Normal routes (screens + platform pages) | about 45 (v1 map: 55 rows incl. diagnostics) | 27 |
| Diagnostics routes | 13 + Capabilities/Result | 1 root + 13 sections |
| Settings rows across all settings pages | 38 (incl. Connectivity, Quick Settings, Power) | 28 + 6 in the Quick Settings sheet |
| Routes printing platform commands | 6 reset-scope pages | 0 |
| Focusable "fact" rows on normal pages | Every About/Storage/Power/USB/Update fact | 0 (static facts) |

## 2. UI pruning ledger``

| Old screen / item | Classification | Action | Reason |
| --- | --- | --- | --- |
| Home → Connectivity | REDUNDANT | remove | Wi-Fi, Bluetooth, PC Transfer now in Settings |
| Connectivity screen | REDUNDANT | remove | Duplicated Settings/Quick Settings |
| Quick Settings screen | REDUNDANT | merge | Became the hold-Power sheet with power options |
| Power Menu modal | REDUNDANT | merge | Into Quick Settings (Restart, Power Off) |
| Settings → Power (Battery & Source, Power Menu) | REDUNDANT | merge | Battery → System; power actions → System/Quick Settings |
| Settings → Storage | USEFUL_END_USER | move | To System → Storage |
| SettingsWifi / SettingsBluetooth duplicate routes | REDUNDANT | remove | One Wi-Fi and one Bluetooth screen |
| Music → Scan Library | USEFUL_END_USER | move | Library settings, PC Transfer, empty-library action |
| Audio → Audio Info | DIAGNOSTIC_ONLY | diagnostics | Diagnostics → Audio |
| Now Playing → Audio Info button | DIAGNOSTIC_ONLY | diagnostics | Same |
| Now Playing → Options/Queue/Audio Info buttons | REDUNDANT | merge | Wheel = volume, Select = options sheet |
| Track Information: Source codec/rate/Source ID | ESSENTIAL (format) / DEVELOPMENT_ONLY (source id) | keep / remove | Format and Location kept in words |
| Library → Scan Status row | USEFUL | merge | Into the Scan row's secondary text |
| Library → Rebuild (opened owner-maintenance page) | NOT_IMPLEMENTED | keep, implemented | Real full re-read |
| Display → Brightness | NOT_IMPLEMENTED | keep, implemented | Real backlight levels when supported |
| System → Date & Time | DIAGNOSTIC_ONLY | diagnostics | Clock trust is in Boot & Services; update copy covers the user consequence |
| System → Backup & Export | ADVANCED_USER | diagnostics | Diagnostics → Export Player Data |
| About: Kernel, Current output, Build Information | DIAGNOSTIC_ONLY | diagnostics | Build Information section |
| Build Information: commits, build ID, rootfs | DIAGNOSTIC_ONLY | diagnostics | Same |
| Software Update: scope, network readiness, signing key, sequence, rollback, download state | DIAGNOSTIC_ONLY | diagnostics | Update section |
| Software Update: Restore Previous Root | ADVANCED_USER | diagnostics | Restore Previous System |
| Update Details page | DIAGNOSTIC_ONLY | diagnostics | Update section |
| PC Transfer: protocol, SFTP, address, authentication, Wi-Fi exclusion, DMA counters | DIAGNOSTIC_ONLY | diagnostics | USB section |
| PC Transfer: cable/readiness/free space | ESSENTIAL | keep | Product states |
| Power & Battery: SOC source/confidence, calibration, voltage, current, pack temperature, supplies, policy | DIAGNOSTIC_ONLY | diagnostics | Battery section |
| Storage: filesystem, controller clocks, transport recovery, system root | DIAGNOSTIC_ONLY | diagnostics | Storage section |
| Network Details (IP, route, DNS, RX/TX) | DIAGNOSTIC_ONLY | diagnostics | Network section |
| Bluetooth Codec & Audio Details | DIAGNOSTIC_ONLY | diagnostics | Bluetooth section |
| Codec Preference page (SBC, Auto disabled, Stop Playback) | STALE / UNSUPPORTED | hide | Codec row only with ≥2 enabled, peer-supported codecs |
| Bluetooth → Use Wired Output | REDUNDANT | merge | Output picker |
| Wi-Fi → Disconnect, Network Details, Connection Problem rows | REDUNDANT | merge | Network options; footer problem line |
| Reset scopes ×6 printing y2-platform reset plan | NOT_IMPLEMENTED | remove / implemented | Five real operations; full wipe not offered |
| Platform Health, Capabilities, CPU & Memory, Thermal & Power, Boot & Services, Advanced Checks, Latest Operation | DIAGNOSTIC_ONLY | diagnostics | Diagnostics root |
| Benchmarks (storage, library) | DEVELOPMENT_ONLY | diagnostics | Confirmed, Diagnostics only |
| Status bar "Reborn"/"Wired" text | REDUNDANT | remove | Playing glyph; output shown on Now Playing |
| Footer hints ("Back Parent • Hold Back Home") | REDUNDANT | remove | Mini player or one status line |
| Splash "REBORN \| Y2", "LISTEN DEEPER", loading bar, "INITIALIZING MUSIC EXPERIENCE", photo scene | STALE | remove | Mark + breathing rule |

## 3. Unavailable cleanup

Before: 67 "unavailable / not available / not exposed" occurrences in UI and application sources, including generic value rendering of every missing platform field as Unavailable on normal pages. After: no user-visible normal-page string uses that pattern (enforced by `normal_screens_never_show_engineering_terms_or_generic_unavailable` and `empty_library_states_name_the_problem_without_generic_unavailable`). Internal error strings remain in the application but are mapped by `friendly_error` (Wi-Fi is starting. Try again in a moment.). Diagnostics states a missing field as Not reported, which is accurate there.

## 4. Boot
  - Old: stock preloader/LK logo → kernel → initramfs splash with a

photographic scene, taglines and a bouncing bar → a different Reborn boot screen (Reborn / MUSIC LIVES ON / Starting music services) → UI.
  - New: preloader and LK unchanged → the initramfs splash shows the Reborn

mark on `#090B0D` with a breathing gold rule → Reborn takes the display with the pixel-identical frame → 6-frame dissolve into the UI.
  - Stage ownership: LK logo (stock, untouched) → `reborn-splash` from the

initramfs after the unchanged charger and voltage gate (`KD_GRAPHICS` keeps fbcon hidden) → Reborn via the existing READY/RELEASED/PRESENTED handoff.
  - Timing: no wait was added. The splash pulse costs one 40×2 px fill

per 50 ms poll that already existed; the dissolve starts only after the first UI frame is ready and lasts ~200 ms. The Y2 was not run, so splash visibility, process start, first frame and ready times were not measured on hardware; Reborn's `startup.phase` events and the splash `events.jsonl` record them on the next boot.
  - Flashes: the background is the same `#090B0D` in the splash, Reborn's

first frame and the UI; fbcon stays in `KD_GRAPHICS`. The LK→kernel transition is owned by stock firmware and was not changed.

## 5. Shutdown
  - Old: Reborn saved state and exited after its acknowledgement. Its DRM

device closed with the backlight on, so the kernel's fbdev emulation restored its own buffer (stale, console or white) until power was cut.
  - New: UI fades (7 frames) → Reborn mark (Battery empty on

low-battery shutdown) while audio, session and database close → mark fades → black frame → backlight off (`bl_power`) → acknowledgement → exit. The DRM device stays open until the process exits. Visuals take ~0.9 s.
  - Platform: the coordinator turns every backlight off after stopping or

killing Reborn and before `busybox poweroff/reboot`, so a crashed or hung Reborn still ends dark. The platform deadline (10 s for user requests) and its continuation without an acknowledgement are unchanged.

## 7. Wheel
  - Root cause (software, from source): `InputManager::poll_at` gave every

record of a 15 ms read batch the same `Instant::now()` and accelerated from the second same-direction event within 180 ms (`previous_steps + 1`). Two real detents read in one batch, or one bounced data-ready edge re-reading the latched APT32F frame (the driver emits a press/release pair per IRQ), moved 1 + 2 rows; brisk rotation reached 3–6 rows per detent. The physical bounce rate was not captured on hardware.
  - Path: APT32F I²C frame → `apt32f-wheel` KEY_UP/PAGEUP/DOWN/PAGEDOWN

press+release → evdev → `InputManager` (cadence, dedupe) → `NormalizedInput::Wheel*` → `ActionRouter` (screen-off drop) → `Action::Wheel*` → `Ui::wheel` (context policy).
  - Dedupe: kernel timestamps (`EVIOCSCLOCKID` → monotonic); same direction

under 8 ms is one detent; releases and autorepeat are never detents.
  - Acceleration: 1 step until four detents of one rotation; then 2 (≤110 ms

smoothed interval), 3 (≤70 ms after 6), 4 (≤45 ms after 10). Reset after 220 ms, on reversal, device loss or a backwards clock.
  - Contexts: long library lists use the suggestion; everything else one

step; Now Playing volume ±2.

## 9. Information removed from normal screens

Kernel version, boot ID, kernel taint, Reborn/Y2Linux commits, build ID, rootfs version, platform build; CPU frequency/governor/idle states, load, memory, die temperatures, cooling; SOC source/confidence/calibration, supply voltage, current, pack temperature, low-battery policy; filesystem, UUID, controller clocks, transport errors; IP, route, DNS, signal dBm, RX/TX; SFTP/SSH, USB address, authentication, DMA counters; BlueZ/BlueALSA, PCM format/rate/channels, codec policy, trust, reconnect state; ALSA format, rate, hw_params, decoder/DSP formats; update scope, journal, signing key ID, sequence, rollback; capability implemented/enabled/qualified flags; reset plan commands; benchmark controls.

## 10. Feature UX summary

Music, Queue, Wi-Fi, Bluetooth, codec, USB, battery, storage, update and reset behave as described in [Product UI v2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V2.md%23screens&anchor=screens). The codec preference row is hidden on the current platform policy (SBC only at runtime); it appears automatically when an enabled optional codec is usable with the connected peer.

## 11. Performance
  - Rendering stays dirty-flag driven at ≤30 fps, visible rows only. The boot

dissolve renders 6 extra frames once; the shutdown 27 frames once.
  - Platform polling: one worker instead of two; a `y2-platform` process runs

only while a platform-backed screen is visible (every 15 s, 4 s on PC Transfer) or after an explicit operation, never with the display off. The previous design refreshed every 10 s on platform pages via a second worker.
  - Screen-off cadence is unchanged (50 ms loop); no new wake sources.

Battery remains a 2 s file read of the platform power record.

## 16. Remaining product limitations
  - Battery percentage is the platform's provisional voltage estimate; there

is no measured current or calibrated capacity.
  - Software updates need an owner-configured update channel; without one the

device says updates are installed with a computer.
  - PC Transfer is authenticated SFTP over USB; it is not a USB mass-storage

drive, and loaded USB transfer failed the last physical CPU qualification.
  - Optional Bluetooth codecs remain disabled by platform policy, so SBC is

the only codec offered.
  - No sleep/suspend: screen-off keeps the system running.
  - Brightness and the shutdown backlight sequence are implemented against the

standard backlight class and were not physically observed.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
