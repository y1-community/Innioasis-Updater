---
title: "Reborn UI v1 - Innioasis Updater"
description: "Reborn UI v1 Software design/candidate scope. The real Fix01 run exercised wheel key events, semantic Interactive/Artwork/Playback/Scan leases and bounded playback, but i"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-ui-v1.html"
---

# Reborn UI v1 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn UI v1

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn UI v1

Software design/candidate scope. The real Fix01 run exercised wheel key events, semantic Interactive/Artwork/Playback/Scan leases and bounded playback, but it was not a visual-legibility, analog-listening or full UI endurance review. See [current Reborn state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FCURRENT_REBORN_STATE.md) and the [physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md).

Owner-review software candidate for the 480×360 Y2 and frozen Y2Linux Platform v1. This is a native GLES application with a wheel and physical buttons. It has no touch, mouse, swipe, drag, hover, gesture unlock or on-screen transport buttons. Physical and endurance qualification remain outstanding. Do not flash as part of this implementation task.

## Visual authority and review

The complete owner-supplied Reborn Y2 Simple UI Asset Pack was read before implementation: README, tokens, docs, components, SVGs and all eight native-size references. The supplied ZIP was not present in the workspace; its complete extracted directory was available. Historical Android/Y2Player screenshots were not used as design authority. Reference compositions were adapted for one linear wheel path, real observations and readable five-row lists.

The visual system is authoritative in `crates/reborn-ui/src/theme.rs`:````````````````````````

| Role | Value |
| --- | --- |
| Background / raised | #090B0D / #0F1215 |
| Panel / alternate | #15191D / #1B2025 |
| Divider / track | #2B3036 / #3B4148 |
| Text / secondary / muted | #F2F0EB / #A7A9AC / #74787E |
| Accent / focus / focus fill | #E7C98B / #FFE2A4 / #201C16 |
| Type | Hero 26, title 20, section 18, row 15, body 14, secondary 12 px |
| Geometry | 16 px margins, 28 px status, 36 px footer, 46 px rows on 48 px pitch |
| Focus | One 2 px warm outline with restrained dark-gold fill; no continuous glow |
| Artwork | 164 px Now Playing; 78 px collection detail; 26 px mini-player |

Selected settings use explicit values such as On/Off and preference labels. Playing tracks use a separate triangle and queue-state text. Disabled rows use muted type and never receive wheel focus. Gold is reserved for focus and playback progress. Cards are not stacked inside cards. No expensive blur or page animation.

One licensed, proportional DejaVu Sans 2.37 atlas replaces the old ASCII and separate display-font paths. Its official public source, exact TTF hash and full license are in `assets/fonts/`. Latin extensions, Greek and Cyrillic are supported; unsupported CJK/emoji use a bounded replacement glyph. Shaping and bidirectional layout are not implemented. Text is sanitized, measured by advance widths and ellipsized without crossing neighboring controls or sampling outside the atlas. Value details wrap at readable size with a bounded final-line ellipsis. There is no constantly moving marquee.

The Simple pack SVG sources and their hashes are preserved in `assets/icons/`. A build-time rasterizer makes the 192×160 icon atlas. Python, SVG parsing and TTF rasterization are not runtime UI dependencies. The reference album art is only in `docs/ui/fixtures/` and the preview executable. The production ELF/package checks explicitly reject the sample artist/device/artwork markers.

## Architecture and components

`AppModel → UI → semantic Action → typed Effect → runtime worker/service → observed result → state`remains the application boundary.`reborn-platform::input` is the only physical key mapper. The UI never opens ALSA, writes SQLite, calls raw BlueZ, operates wpa_supplicant, changes sysfs policy or writes OTA blocks.````````````````````

| Module | Responsibility |
| --- | --- |
| reborn-core | Navigation/history, queue occurrence identity, preferences, transient platform observation bundle |
| reborn-ui/theme | Single palette, type, spacing and focus authority |
| reborn-ui/components | Canvas, status/title, focus/value rows, artwork, progress, mini-player, modal and notice |
| reborn-ui/catalog | Cached ordered row identities, collection grouping and folder hierarchy |
| reborn-ui/screens | Native screen composition, boot, Now Playing, lists, detail and password views |
| reborn-ui/platform | Human-readable projection of versioned observations and capability-gated actions |
| reborn-ui/lib | Semantic navigation, context/dialog behavior and effect selection |
| reborn-platform/dashboard | Bounded asynchronous fixed-argv Platform v1 client, schema and deadline checks |
| reborn/artwork | Four-entry, route/source/mount-aware collection artwork cache and worker |
| reborn/main | Existing playback, library, radio and platform service coordination |

Platform telemetry has a separate observer queue from operations so staging or benchmarks do not block status refresh. Response size is capped at 1 MiB, command arguments are fixed and deadlines are bounded. Health's nonzero degraded/failure exit remains an observation, not a lost response. Automatic observation refresh runs only in platform views or while an operation is active, at ten-second intervals. Missing/failed refresh clears usable capability observations.

Navigation/filter/focus/scroll are retained in a bounded history. Dialogs retain background position and trap wheel focus. Disabled actions are skipped. Confirm rechecks live update/benchmark admission; stale capability state cannot admit an operation. Root apply/restore temporarily traps navigation and power/playback requests while the platform prepares restart. Volume and wake remain available.

Queue contexts resolve `QueueEntryId`, not track ID or an old row number, so reordered duplicate occurrences stay distinct. An async library replacement closes stale index-based track contexts. Returning from a normal detail visit restores the same collection position.

## Music-first behavior

Home offers Music, Now Playing, Queue, Connectivity and Settings. Music offers Albums, Artists, Songs, Folders and Scan. Favorites are omitted because the current model has no durable favorites. Songs are title ordered; albums and artists use readable lists. Long Select offers a letter index on Songs/Albums/Artists, alongside track actions where relevant. `#` groups non-ASCII initials, symbols and numbers; locale-aware collation is not claimed. Existing wheel acceleration remains active.

Album/artist detail uses representative real embedded or sidecar art, collection count/duration and a vertically linear list. Play All has collection context Play/Shuffle/Play Next/Add to Queue; a focused song's actions affect that song. Artist albums are a separate child list. Folders preserve parent/child routes and Back position. Missing metadata uses filename/Unknown fallbacks. Partial scans show validated stored rows while keeping the incomplete/error status; no failed scan is represented as completed and the scanner's non-pruning safety remains.

Now Playing prioritizes art, two-line title, artist, album, elapsed/remaining and actual playback state. Its wheel path is Options → Queue → Audio Info. Play/Pause, Previous/Next and Volume remain hardware actions. Source-unavailable and sink-error states supply compact recovery guidance. The main screen carries no invented source-as-output format claim. Browsing has a non-focusable mini-player.

Queue shows ordered entries, Now Playing/Up Next/Played, duration and repeat/shuffle state. Context offers Play Now, Remove, Move Up/Down and confirmed Clear Future. Moving is supported only within future entries; current-track removal is disabled. There are no drag handles. Existing queue construction and transactional playback reconfiguration retain their safety model; this UI does not replace the engine.

## Physical controls

| Input | Behavior |
| --- | --- |
| Wheel clockwise/counterclockwise | Next/previous enabled item; existing acceleration; value/character selection when editing |
| Select | Open, accept, toggle or add the selected password character |
| Long Select / Context | Context menu; submit Wi-Fi password in text entry |
| Back | Close overlay/cancel entry, otherwise restore parent route/focus/scroll |
| Long Back | Home; first closes a modal if one is open |
| Play/Pause | Global playback toggle, including screen off and dialogs |
| Long Play/Pause | Now Playing when screen on and no modal/entry/pairing trap |
| Previous/Next | Global previous/next track |
| Long Previous/Next | Existing semantic seek, ±30 seconds per emitted action |
| Volume buttons | Always global volume, including screen off; never menu navigation |
| Power short | Existing platform panel sleep/wake |
| Power long | Power menu when supported by the existing screen-on input policy |

The existing router owns long-press timing, event cancellation, repeats and screen-off policy. Off-screen wheel/select/Back/Home/context do not move focus. No decorative lock screen runs while the panel should be off; wake returns to the retained route. OTA apply/restore is the explicit operation-conflict exception to normal global transport behavior. There is no new key mapper.

## Platform bindings and honest unavailable states

| UI | Authority and presentation |
| --- | --- |
| Wi-Fi | Existing radio worker plus fresh Platform v1 readiness: Off, Starting, Scanning, Associating, Authenticated, AcquiringIP, Online, Failed. Authentication never implies Online. Saved networks merge with scan results. Open/WPA-PSK supported; unsupported WEP/enterprise/SAE-only networks disabled. Connect/disconnect/forget/rescan use existing effects. Compact errors never expose D-Bus/credentials. |
| Wi-Fi password | One circular character/action path; Delete/Connect/Cancel and long-Select submit. Masked count, no typed password on screen. WPA passphrase remains 8–63 ASCII characters; owner USB provisioning remains available. |
| Bluetooth | Observed adapter/peer/paired/connection state. Pair/connect/disconnect/forget and output selection; named peer/passkey confirmation defaults to Cancel. AVRCP reaches the same semantic playback actions. |
| Codec | Preference persisted separately from active transport. SBC baseline available only for stopped, connected audio peer. Auto disabled when the capability list has no qualified eligible codecs. Active codec/PCM/rate/channels come from actual BlueALSA observations. No optional codec controls. |
| Audio Info | Source codec/rate/precision; decoded and internal processing format; ReplayGain/EQ/crossfade; selected output; observed sink format/rate/channels. Inactive sink information explicitly means last opened sink. |
| PC Transfer | USB cable/UDC and authenticated USB-only SFTP readiness, configured address, storage link. Transfer counters/progress are explicitly unavailable where not observed. No private key material or Wi-Fi transfer listener. |
| Storage | Actual mounted state, available/total space, filesystem and low/critical-space messages. Missing SD has one clear state, not fabricated capacities. |
| Power | Charging/source/voltage and platform low-battery policy; no SOC, runtime, battery temperature or current estimate. Unreliable capacity never enters the UI power view. |
| Clock | Shows timestamp only when Platform v1 establishes clock readiness; otherwise untrusted state and synchronization guidance. |
| Update | Real journal/download/verification/readiness; check/stage/confirmed root install and cancel/rollback where admitted. No fake percent or automatic BOOTIMG update. Last result and advanced sequence/signing details are separate. Key ID remains Unavailable when the status API does not expose it. |
| Backup | Platform consistent settings/player/database export, completion path and SHA-256; retrieve through USB SFTP. Excludes SSH private keys, network passwords, Bluetooth bonds and calibration. |
| Maintenance | Distinct settings/network/bonds/library/cache/full-user scopes. Current API requires stopped services and an expiring exact plan digest, so these are explicit owner USB-maintenance instructions, not pretend in-app reset buttons. Full reset explains music deletion. |
| About | User-friendly Reborn/platform release first; compiled source and rootfs/build identities under Build Information. UI package identity does not replace frozen platform/kernel provenance. |

Diagnostics is Settings → System → Diagnostics: Platform Health, Latest Operation, Capabilities, CPU/Memory, Thermal/Power, Storage, Network, Bluetooth, Audio, USB, Update, Boot/Services and Advanced Checks. Facts open a readable detail view. Health preserves OK/DEGRADED/FAILED/UNAVAILABLE; qualification pending is not silently converted into failure. Capabilities keep implemented/enabled/qualified separate. CPU policies/load, total/available/RSS/PSS/cache/slab, die temperatures, cooling, route/DNS/IP/RX/TX, peer trust/reconnect and PCM are observed facts.

Safe advanced actions use platform tools: health refresh, passive network readiness check, confirmed 16 MiB/64-operation storage scratch test, and confirmed 1,000-track library scratch benchmark. They never use music files. No power/suspend/USB VBUS experiments, OTA fault injection or unqualified audio-mode actions are exposed.

Normal UI omits USB Host/UAC, deeper cpuidle, deep suspend, wired S24/S32/preserved 24-bit or 88.2/96 kHz, AAC/aptX/aptX HD/LDAC, advanced DAC gain/filter policy and automatic BOOTIMG OTA. Existing capability records may describe these as unavailable, disabled or qualification pending in Diagnostics; their appearance is not enablement. Brightness, useless EQ switches, Airplane Mode, DND and fake favorites are omitted.

## Rendering, memory and persistence

Dirty GLES rendering remains. Idle menus do not redraw for playback position; Now Playing updates on displayed seconds. Notices request one final redraw on expiry. No continuous animation or blur. Five visible rows (three under collection art) are formatted from cached identities; wheel steps do not clone the complete catalog or regenerate every row. Catalog replacement/route changes rebuild indexes; collection/queue operations may still scale with the collection intentionally.

The shared font texture is 4 MiB; each decoded art texture is 100 KiB. Collection art caches at most four images (400 KiB), uses one bounded worker/channel, rejects stale source/mount results and reuses the current playback art only when identity matches. Actual target RSS/PSS, frame timing and audio coexistence remain physical qualification tasks; host/QEMU figures are not Cortex-A7 performance claims.

Persisted data remains meaningful preferences/session/queue: output, volume, ReplayGain, playback options, timeout and codec preference. Navigation, display sleep, live source readiness, generation, transient errors/scanning, negotiated codec and platform diagnostics are not serialized. Existing settings are migrated with a safe SBC preference default; this does not assert negotiated SBC.

## Validation and handoff

See `REBORN-UI-V1-REPORT.md` for exact revisions, receipts, artifact hashes and limitations, `REBORN-UI-V1-NAVIGATION.md` for every route and focus path, and `REBORN-UI-V1-QUALIFICATION.md` for owner testing. `previews/v1/` contains 69 native screens and a contact sheet from the production draw path using isolated fixtures. The first and second visual passes were corrected for density, Unicode bounds, contrast, full confirmation text, storage wording and status truthfulness.

Build tools: `tools/build/cross.sh`, `tools/build/package_ui_v1.py`, existing isolated `qemu-check.py`, and `ui_benchmarks.py`. The new packager checks committed production inputs while preserving unrelated owner files. It overlays only app ELFs/licenses/provenance and version metadata on the exact hash-verified Platform v1 root, verifies readback/ELF dependencies/filesystem, and selects ANDROID only. No platform implementation source or hardware policy was changed for the UI.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
