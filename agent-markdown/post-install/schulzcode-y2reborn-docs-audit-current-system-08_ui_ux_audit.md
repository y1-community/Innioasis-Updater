---
title: "UI engineering, input and UX audit - Innioasis Updater"
description: "UI engineering, input and UX audit <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-08_ui_ux_audit.html"
---

# UI engineering, input and UX audit - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# UI engineering, input and UX audit

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# UI engineering, input and UX audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

No visual redesign was performed or proposed as a prerequisite for correctness. Engineering, interaction semantics and aesthetic preference are separate below.

## UI engineering: G04/G08/F21/F22/F23

Good boundary — IMPLEMENTED / HIGH.[Ui::draw](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-ui/src/lib.rs) consumes state and produces drawing quads. [Screens](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-ui/src/screens.rs), [components](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-ui/src/components.rs) and [theme](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-ui/src/theme.rs) own presentation. [Runtime](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs) owns service effects; the UI does not open ALSA, SQLite or radio hardware. The renderer receives shapes/textures, not playback policy. A visual redesign can mostly stay inside UI/theme/assets without touching decoder, DB or driver architecture. Preserve that separation.

That does not mean every model dependency is clean: screen-specific navigation is in AppModel, Ui::action mutates it, and Effects sometimes carry only a global list index when collection identity is needed. Fix that semantic interface (F08), not the whole reducer pattern. A pure reducer rewrite would not automatically repair it.

The production [native renderer](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-graphics/native/graphics.c) really uses GBM/EGL/GLES2/KMS. It requires a renderer containing Mali400; it does not silently claim hardware acceleration while accepting llvmpipe. Linear GBM buffers are registered as DRM FBs, page flips wait for completion, and the previous buffer is then released. Fonts/icons are static atlases; art is a reusable texture. No full-frame CPU readback/copy is on the ordinary presentation path. The splash uses an explicit KMS handoff. Historical GPU01 measurements and an older running Reborn radio inspection support real hardware acceleration, while the current polish image remains physically unqualified.

F22 — PARTIAL / MEDIUM confidence in full recovery. Native pageflip waits have a three-second deadline; failure can stall UI/input during that interval. Runtime drops/recreates the renderer once and waits for explicit wake for further recovery. This is reasonable containment, but correct old-CRTC/buffer ownership across splash handoff, pageflip timeout, screen-off, renderer recreation and system suspend needs physical stress tests. No new confirmed GPU use-after-free is claimed. Do not replace GBM/KMS to avoid performing those tests.

Dirty rendering and a ~34-ms render limit avoid a decorative continuous animation loop. Main still wakes every 15 ms; status/progress changes can request frames. Static-screen CPU/GPU-idle and screen-off playback need measurements of the app, not only the platform GPU checker. Glyphs/rounded rectangles generate many small draws and uniform lookups; this may be acceptable at 480×360. Batch only if target navigation measurements identify it as material.

F23 — WEAK / HIGH: visible list windows limit drawing, not data work. The UI constructs whole collection rows and main clones all loaded Track records per input action. A 20k library can make wheel input expensive. Four rendered rows do not prove virtualization. Use bounded views/IDs after measuring, not a generic virtual-DOM framework.

F21 — PARTIAL / HIGH: font atlases are 256×128 with a 16×8 cell layout (128 glyph slots). `glyph_index` accepts byte codepoints up to 255 while native texture coordinates use the 128-slot layout; higher Unicode becomes `?`. Accented/non-Latin metadata therefore lacks a correct complete glyph path; 128–255 can sample outside the intended atlas rows. This is an implementation limitation, not visual taste. The checked-in current DejaVu atlases are not the old font8x8 dependency still named in baseline docs/dependency metadata.

Layout tests check useful focus/label invariants, but do not cover the whole real glyph repertoire, long localized metadata or physical panel legibility. Preview rasterization is useful for layout and is not proof of native GLES clipping, timing or focus behavior under live events.

## Input architecture: G07/F20`kernel input device + evdev event -> device-specific map (no hardcoded eventN) -> InputManager: press/release/long/repeat/wheel acceleration -> ActionRouter: screen policy and semantic actions -> Ui/AppModel -> Effect -> runtime/service`

[input.rs](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/input.rs) owns Linux types and physical timing. Wheel direction cannot accidentally become Select solely because a navigation keycode overlaps: device identity is part of the mapping. Long-press suppression and global volume/playback policy have specific tests. This is appropriately sized, not gratuitously overengineered.

Current intended mapping:

| Physical input | Short/normal | Long/repeat | Screen off |
| --- | --- | --- | --- |
| Select | Select | Context menu | Ignored |
| Back | Back | Home | Ignored |
| Previous/Next | Track step | Seek | Track short presses retained; long-repeat behavior has inconsistency below |
| Play/Pause | Global toggle | Show Now Playing | Short toggle retained |
| Power | Sleep/wake | Power menu when screen on | Short Power is the wake action |
| Volume +/- | Global volume | Repeat | Retained without wake |
| Wheel | Navigation; volume on Now Playing | Central bounded acceleration | Ignored |

Long press is 650 ms; repeat begins at 400 ms then every 90 ms; wheel acceleration caps at six. These are policy choices, not inherently bugs. Qualification must verify feel, not just constants.

F20 concrete weaknesses:
  - `poll_at` calls `tick_at(now)` before reading queued releases and discards kernel event timestamps. If the UI loop stalls, a physically short press can be aged into a long press before its already-queued release is consumed. The three-second pageflip timeout and synchronous state/ALSA work make this a realistic integration scenario. Tests mostly drive `ingest`/`tick` directly and do not reproduce a delayed evdev backlog.
  - No SYN_DROPPED reconciliation or device-reopen strategy was found. Read errors are ignored; a lost release can leave stale pressed/router state until later heuristics or reset.
  - LongPress inserts into `long_pressed` before the screen-off early return. Subsequent Previous/Next Repeat checks that set but not `screen_on`, allowing seek repeats even though the initial screen-off long action was suppressed. This is inconsistent policy, not an accidental wheel/select mapping.

Targeted correction should preserve the semantic vocabulary and central timing ownership. Do not add a second key mapper in individual screens.

## UX/action correctness, separate from appearance

High-impact: album/artist/folder play actions can enqueue the whole library, collection add/play-next only one track, queue edits do not update the worker, and repeat-one is bypassed by automatic chaining. These are application semantics F03/F08, not a designer's preference. Ordinary volume and seek may reopen/fail the sink (F02), so a correct-looking input map does not establish reliable controls.

Other concrete F21 issues:
  - Back history stores Screen only; returning clears filter/focus/scroll. Navigating from a filtered album/artist into another screen and back loses the contextual route. Store enough route state to restore the user's place; no new navigation framework is needed.
  - Album identity is album title only, merging different artists' same-title albums; “Unknown” labels are not stable underlying identities.
  - `screens.rs` displays “Internal 128 GB” as a literal, despite this Y2's ~8-GB eMMC layout. This is leftover reference/mock content in a production screen, not merely optimistic styling.
  - The Settings SD availability check compares `source.id == "sd"`, whereas the real adapter uses `uuid:<...>`. A mounted SD can be described as absent in that setting.
  - Equalizer has an enable toggle but no ordinary way to configure its default-empty bands. The displayed On state can have no audible effect (F12).
  - Preopened next-track artwork can replace current artwork early (F24).

Positive UX engineering: destructive actions use confirmation/context actions; password entry hides content; disabled items are excluded from focus; focus metadata distinguishes currently playing from selected; actual display sleep is not an animated lock screen. Existing host tests cover these contracts. Keep those tests through any redesign.

Connectivity actions must distinguish Off, Starting, scanning, link-connected, IP-ready and failed states. Current scan progression is better than the older deployed error-footer behavior; association and actual audio still need qualification. Hiding all errors would not solve this.

## Visual/design concerns

No judgment that a different theme is required for release. Typography, density and artwork treatment are owner/design choices. Engineering prerequisites for later redesign are truthful state binding, durable collection/queue identities, tested focus/navigation, correct glyph support and bounded data work. The current theme/component/renderer boundary is already suitable for redesign once those interfaces are stable. Do not spend the next cycle changing colors while the normal play/volume/queue path remains incorrect.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
