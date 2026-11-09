---
title: "Platform 1.0 input ownership - Innioasis Updater"
description: "Platform 1.0 input ownership Source contract, 2026-10-04. Physical acceptance belongs to the paired Linux docs/validation/Y2-PLATFORM-V1-INPUT.md ; this page claims no in"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-platform-v1-input.html"
---

# Platform 1.0 input ownership - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Platform 1.0 input ownership

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Platform 1.0 input ownership

Source contract, 2026-10-04. Physical acceptance belongs to the paired Linux `docs/validation/Y2-PLATFORM-V1-INPUT.md`; this page claims no installation.

The APT32F data-ready IRQ at EINT55 causes exactly one bounded register-zero repeated-start nine-byte I2C0/0x51 read. Valid AA/55 class-3 frames map codes 1/2 to KEY_UP/PAGEUP and 3/4 to KEY_DOWN/PAGEDOWN. Each is a synthetic down, SYN_REPORT, up, SYN_REPORT pulse. The driver owns frame validation, not detent filtering or acceleration; no firmware commands or polling are added.

Navigation uses gpio-keys-polled at 20 ms with the Linux driver's debounce; MT6582 keypad hardware debounces the two volume keys and its driver reports state changes; MT6323 PMIC owns Power IRQ/wake. Reborn never guesses at button bounce in the UI. It rejects repeated down while already held and treats an unmatched release/repeat as cancellation.

`InputManager` opens named evdev devices with CLOCK_MONOTONIC, reads at most 16 x 1,024 bytes per device per poll, preserves cross-device timestamp order, and converts records into `NormalizedInput`. Wheel releases and EV_KEY value-2 wheel events do not count. WheelCadence alone owns the unchanged 8 ms same- direction filter and EWMA cadence: four sustained detents permit two steps at <=110 ms; six permit three at <=70 ms; ten permit four at <=45 ms. A reversal, backward timestamp or >=220 ms pause resets. A missing trusted clock uses single steps instead of filtering several queued events by receipt time.

Button holds use physical kernel times when available. A queued real hold emits LongPress before Release even if no timer tick occurred during the hold; a queued short press remains short. 650 ms owns long press, 400 ms begins repeat, and repeat cadence is 90 ms. Kernel value-2 records cannot create a second repeat authority. Late ticks emit at most one repeat and long seek starts once, then repeats after 90 ms. Volume acts on down/repeat; navigation and transport short actions act on release. Long releases are consumed.

`ActionRouter` alone owns semantic actions and screen policy. Select/Back begun dark remain suppressed through wake. Dark wheel events never navigate. Transport and volume remain global; dark Previous/Next holds seek and consume the short track action. Play/Pause holds cannot open an invisible screen. Power begun dark belongs to wake, including an external display wake before release; it cannot immediately sleep or open Quick Settings. Power begun lit short-sleeps, while a long hold opens Quick Settings exclusively. Call `begin_batch` before routing a polled batch; wheel suggestions decoded before a screen transition stay precise for that batch. The app clears cadence on screen transitions as well.

The main thread polls directly; there is no evdev-reader thread or semantic channel. No wheel coalescing is introduced because one suggestion describes one detent and fine-control contexts intentionally ignore its magnitude. Every accepted detent therefore remains one action, including in small lists, Queue, dialogs, value editing and Now Playing volume. Only Product v2 catalog lists of >=40 rows honor suggested acceleration. UI code never reads evdev codes. UI changes AppModel and returns Effect; runtime executes audio/platform work. Dirty frames are normalized, drawn and presented through DRM/GBM/EGL.

On SYN_DROPPED the manager cancels held state and cadence, ignores through the next SYN_REPORT and consumes orphan releases. Device EOF/read errors also cancel; rescans retry at most once a second, including failed initial opens or previously absent devices. Identity uses the stable hardware parent, not the changing inputN/eventN allocation. EINTR is transient. A read-budget hit delays hold timers until the queued release can be consumed.

Full suspend remains platform-owned. `InputManager::reset()` closes old evdev queues, clears cadence/hold/drop state, reopens named devices and returns typed Cancel events; route those and reset ActionRouter at the platform boundary. A successful platform wake must deliver the existing typed ScreenWake action from the platform's actual wake result. Do not infer a second sleep request from an orphan post-resume Power release. Ordinary display sleep keeps evdev open for transport/volume/Power and preserves a confirmed held Power gesture.

`rebornctl input monitor --seconds 30` enables bounded diagnostics only for the requested 1..30-second window: up to 2,048 raw records, wheel accepted/rejected counts, cadence, read-limit hits/reopens/rescans and up to 512 normalized events, actions, state/focus/volume and next successful presentation-return timestamp. Timestamps are absolute CLOCK_MONOTONIC microseconds. The raw collection flags truncation. Frame returns follow DRM page-flip completion during steady scanout; first modeset return and photon latency are separate limits. No permanent raw logging or normal UI diagnostics are added. Monitor state is discarded on completion. Volume updates the existing atomic audio target and marks the session dirty; the existing 15-second checkpoint/shutdown saves it, avoiding per-step storage flushes. A crash can lose the last uncheckpointed volume.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
