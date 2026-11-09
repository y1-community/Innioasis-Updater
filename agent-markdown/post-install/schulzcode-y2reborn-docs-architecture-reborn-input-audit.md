---
title: "Reborn physical input audit - Innioasis Updater"
description: "Reborn physical input audit <!-- knowledge-base-scope: historical-design-/-runbook -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-reborn-input-audit.html"
---

# Reborn physical input audit - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn physical input audit

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn physical input audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

The Y2 UI consumes semantic actions only. Raw Linux input records stop at `reborn-platform::input::InputManager`.````````````````````````````````````````````````````````````````````````````````

| Physical control | Linux source / event | Normalized event | Semantic action |
| --- | --- | --- | --- |
| Click wheel clockwise | APT32F click-wheel, EV_KEY KEY_DOWN/KEY_PAGEDOWN, or EV_REL REL_WHEEL > 0 | WheelClockwise(steps) | WheelClockwise(steps) in lists; volume up in Now Playing |
| Click wheel counter-clockwise | APT32F click-wheel, EV_KEY KEY_UP/KEY_PAGEUP, or EV_REL REL_WHEEL < 0 | WheelCounterClockwise(steps) | WheelCounterClockwise(steps) in lists; volume down in Now Playing |
| Center / Select | Y2 navigation buttons, EV_KEY 28 | Press/Release(Select) | Select on release; long release becomes ContextMenu |
| Back | Y2 navigation buttons, EV_KEY 158 | Press/Release(Back) | Back; long press goes Home |
| Previous | Y2 navigation buttons, EV_KEY 105, or any device EV_KEY 165 | Press/Release(Previous) | Previous track; long press seeks backward |
| Next | Y2 navigation buttons, EV_KEY 106, or any device EV_KEY 163 | Press/Release(Next) | Next track; long press seeks forward |
| Play / Pause | Y2 navigation buttons, EV_KEY 164, or any device EV_KEY 57 | Press/Release(PlayPause) | Toggle playback; long press opens Now Playing |
| Power | mtk-pmic-keys, EV_KEY 116 | Press/Release(Power) | Short press sleeps/wakes display; long press opens power menu |
| Volume down | Any accepted input device, EV_KEY 114 | Press/Repeat(VolumeDown) | Volume down; never navigation |
| Volume up | Any accepted input device, EV_KEY 115 | Press/Repeat(VolumeUp) | Volume up; never navigation |

## Keyboard mode (since 1.0.0-beta.5)

While the full-screen keyboard is open (`ActionRouter::set_keyboard(true)`, set by the main loop before each event), Back, Play/Pause, Previous and Next produce `NavigateUp`, `NavigateDown`, `NavigateLeft` and `NavigateRight` on press; their releases produce nothing. Held Previous/Next repeat every other repeat tick (180 ms). A long Back press produces `Home` (cancel). Wheel rotation produces nothing. Select keeps `Select` on release and `ContextMenu` (Done) on a long press. A button pressed as an arrow keeps its hold and release in keyboard mode even if the keyboard closed meanwhile.

## Timing owned by the input boundary
  - Long press: 650 ms.
  - Repeat begins: 400 ms.
  - Repeat cadence: 90 ms.
  - Wheel acceleration: up to six semantic steps for same-direction events

within 180 ms.

Long press is emitted once and recorded by `ActionRouter`; the matching release is consumed, so a long press cannot also trigger its short action.

## Screen-off policy

`ActionRouter::route` receives the authoritative screen-on flag. While the screen is off, wheel/navigation/select/back actions produce no semantic action. Volume and playback controls remain global and do not wake the display. Only a Power release while the screen is off produces `ScreenWake`.

Playback buttons and volume are routed above the current screen, so ordinary navigation and Back cannot stop playback. The UI only returns typed `Effect` values; service calls remain in `app/reborn`.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
