---
title: "Boot progress and display hand-off - Innioasis Updater"
description: "Boot progress and display hand-off <!-- knowledge-base-scope: source-contract -- Source contract, software-validated only. Not flashed. The first boot of a build containi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-boot-handoff.html"
---

# Boot progress and display hand-off - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Boot progress and display hand-off

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Boot progress and display hand-off > **Source contract, software-validated only.** Not flashed. The first boot of > a build containing it is the only way to measure splash-visible, first-frame > and fade times on the device. 

## Ownership and boot order

The early splash (Y2Linux `tools/graphics/reborn-splash.c`, started from the initramfs) owns the display from early boot until Reborn has rendered its first complete UI frame. Reborn starts last (`S90reborn`), after the platform services, the system bus and, when the user has them enabled, the radios are up (`/usr/libexec/y2/boot-gate`, bounded to 45 s, never a fixed delay). So the first frame is a complete system: Wi-Fi, Bluetooth, audio and the library workers exist when the user first sees and can touch the UI. The sequence is:
  - The splash shows the Reborn wordmark, one thin white bar and a short status

line. The bar fills left to right to coarse positions of real milestones.
  - Reborn finishes starting, then renders the real Home frame with the full boot

screen over it (`reborn_ui::boot_transition`, remaining = 1). The bar is already full and the status is "Starting Reborn" (milestone `ready`).
  - Reborn sends `READY 1`. The splash completes bar and status if they are not

already there, drops DRM master and replies `RELEASED 1`. There is no timer.
  - Reborn takes master, waits for the frame's page-flip completion, and sends `PRESENTED 1`; the splash

destroys its buffer and exits. The first presented frame is pixel-identical to the splash's last frame.
  - Reborn reveals the UI over `BOOT_FADE_FRAMES` (10) frames, ≈0.34 s: the bar

and status line fade out first, then the wordmark lifts a few pixels and dissolves with the cover on an ease-in-out curve. Input is ignored until the UI is fully visible. `application_ready` is announced after the first frame is presented, not before.

`drmModeSetCrtc` returning zero is insufficient: physical deep-sleep validation found a boot where it returned after a kernel vblank timeout. The native path therefore requests and waits for a page-flip event even on its first frame. Missing completion or a rejected flip fails readiness, retains scanout buffers until teardown, and reports failed graphics health. Context creation alone is reported as waiting for presentation. The native regression executes the actual implementation with missing/failed/completed events and fails on the old code.

Repeated presentation failure allows one automatic renderer recreation, then waits for an explicit screen wake. A completed frame restores that budget. This prevents the observed repeated context creation/logging during a display fault; it does not repair the underlying kernel or hardware fault. A splash handoff retry must complete a fresh READY/RELEASED handshake even if the splash could not reclaim DRM master after the previous client timed out.

## Why the logo used to stay up

Reborn handed off as soon as its renderer existed (`graphics_ready`) and presented `boot_frame()`, a static copy of the logo. It then ran the rest of startup on its render thread (media sources, database and scanner, audio, Wi-Fi and Bluetooth workers, control server, diagnostics, platform client, artwork, AVRCP) and only drew again when that loop began. The splash was gone, so nothing animated and the logo stayed for the whole remainder of startup; the dissolve started only afterwards, and `application_ready` was announced for the logo frame. Reborn also used to start before the radios and the system bus existed (`S05reborn`), so its first frames were an incomplete system.

## Milestones

Producers write a milestone name to `/run/reborn-splash/phase`: the initramfs through `y2_stage` (its existing stage names), `rcS` before each service that matters (`rc_*`), `boot-gate` for each real wait, and Reborn through `startup_phase` (`reborn_platform::contract::boot_milestone`). The table lives in `reborn_ui::BOOT_PHASES`; `reborn-preview` exports it with the rendered text to `docs/ui/previews/v3/boot-layout.json`, and Y2Linux `tools/graphics/make-splash-mark.py` generates `reborn-splash-mark.h` from it.````````````````````````````````````````````````

| Milestones | Status line |
| --- | --- |
| start, root_data_mounted, switch_root, rc_data | Starting system |
| storage_discovery … fsck_complete | Preparing storage |
| rc_time | Setting the clock |
| rc_power | Starting power |
| rc_bluetooth | Starting Bluetooth |
| rc_connectivity … conn_activated | Starting connectivity (factory records, calibration, radio activation) |
| conn_wifi_wait, conn_wifi | Starting Wi-Fi (only when enabled) |
| conn_bluetooth_wait, conn_bluetooth | Starting Bluetooth (only when enabled) |
| system_ready, model_restored | Starting Reborn |
| graphics_ready, storage_ready | Loading music library |
| library_workers_ready, core_services_ready | Starting audio |
| audio_ready | Starting connectivity (Reborn's radio workers) |
| radio_workers_ready … ready | Starting Reborn |

The positions are ordinal weights, not time or work estimates, and are never shown as numbers. The bar only moves forward: earlier or unknown names are ignored, a missing milestone (a disabled radio) leaves the bar where it is until a later one arrives, and nothing advances on a timer. The splash redraws only while the bar is gliding to a new position (33 ms ticks) and is otherwise asleep in `poll`. `rcS` also writes every script's start and end uptime to `/run/y2/boot-trace.jsonl` for profiling.

The initramfs `rescue` stage and a failed hand-off show "Could not start / Restart the player" without a bar. The failure timeout counts from the last milestone (60 s), so a slow but progressing boot is never called a failure. A late `READY` still works.

## Early-boot waits that were removed
  - The initramfs credits the device's stored random seed as soon as Y2DATA is

mounted. Before, the kernel needed ~6 s to gather entropy on this CPU and the first process that waited for randomness (the platform helper's temporary file names) blocked until then, about 3 s with nothing booting.
  - `y2-platform` records no longer use `tempfile`, so they never wait for the

random pool.
  - Storage discovery polls every 50 ms instead of once a second.

## Shutdown

Reborn dissolves the UI into the same screen with a full bar and Saving, saves (audio, session, database), then shows Shutting down (or Restarting, Battery empty) while the bar drains right to left and the screen dims. It presents a black frame, waits one refresh, turns the backlight off and acknowledges. It does not invent progress: the two labels are the two real phases. If Reborn never acknowledges (hang, crash, deadline), the platform turns the backlight off before stopping Reborn, so restoring the fbdev buffer cannot show on a lit panel.

## Checks
  - `cargo test -p reborn-ui` (phase table, bar geometry, no accent colour, fade

and shutdown schedules) and `cargo test -p reborn --test boot_handoff_guard` (first frame is the real UI under the cover, readiness after presentation).
  - Y2Linux `tests/test_reborn_splash.py` (milestone mapping, no regression,

missing/failed milestones, pixel identity with Reborn, hand-off timing, idle without wake-ups) and `tests/test_platform_power_contract.py`.
  - Previews: `docs/ui/previews/boot/contact-sheet.png`, made by Y2Linux

`tools/graphics/boot-previews.py`.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
