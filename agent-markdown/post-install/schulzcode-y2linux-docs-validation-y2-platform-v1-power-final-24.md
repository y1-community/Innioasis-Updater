---
title: "POWER-FINAL-24 — animation frame pacing (smooth Cover Flow) - Innioasis Updater"
description: "POWER-FINAL-24 — animation frame pacing smooth Cover Flow Status: INSTALLED; Cover Flow ≈27 fps was ≈10; tagged baseline-24 2026-10-13. Package out/y2linux-platform-v1-po"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-24.html"
---

# POWER-FINAL-24 — animation frame pacing (smooth Cover Flow) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-24 — animation frame pacing (smooth Cover Flow)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-24 — animation frame pacing (smooth Cover Flow)

Status: INSTALLED; Cover Flow ≈27 fps (was ≈10); tagged `baseline-24` (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-24/` (fallback = 23), receipts `out/deep-sleep-final/build24-receipts/`. BOOTIMG `653c7d85b7659f5dae6172f2d07dae8802a91ca3afc83c5adb8f97f176dbdda7`, Y2ROOT `21f21e4770b150c96b1947acc1ef29de8d05b0c4054afe31575a7bf90c99860b`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-24`, kernel `6.18.56-y2linux-platform-v1-power-final-24`, root `2026.08-platform-v1.54`, release `1.0.0-platform-v1-power-final-candidate.24`; Linux `d2b38e8`, Reborn `ced5199`. Platform as 22/23.

## 23 on the device (owner scrolling, 45-s live sample)

Cover Flow looks right but felt slow. Renderer metrics while scrolling: 3–17 ms per frame (`graphics_frame_time_ms`; CPU 1–2 ms, the rest waits for the page flip), yet only ≈10 frames per second (`graphics_frames` 568 → 1036 in 45 s). Reborn's main thread used 5.5 % CPU, the CPU stayed at 598–747 MHz. Cause: the main loop computed its wait before the animation marked the frame dirty, so between wheel events it slept its idle 250 ms (50 ms while playing); dirty frames were also capped at one per 34 ms.

Test library: 100 generated albums (300 silent 4-s FLACs, 8 cover styles, 8 genres) in `Cover Flow Test` on the SD card (generator in the session scratchpad). The owner's SD card also holds 11 macOS `._*.mp3` AppleDouble files that fail to parse, so every scan reports "incomplete" and keeps stale entries — a Reborn follow-up (skip `._*` and macOS system folders).

## What 24 changes

Reborn `main_loop_interval`: while `ui.animating()` (Cover Flow glide, cover flight) the loop waits for the next 16.7-ms frame start; presentation paces to the page flip. Idle (250 ms), playing (50 ms), dirty (34 ms) and screen-off (1 s) waits are unchanged. Test extended.

## Tests

Reborn clippy clean, workspace tests pass; container suite 693, exit 0; package checks PASS.

## Hardware result (owner scrolling, 40-s live sample + screen capture)````

|  | 23 | 24 |
| --- | --- | --- |
| frames per second while drawing | ≈10 | 27 median, 31 max |
| graphics_frame_time_ms | 3–17 ms | 3–18 ms |
| graphics_cpu_ms | 1–2 ms | 1–4 ms |
| Reborn main thread CPU | 5.5 % | 45 % |
| CPU clock | 598–747 MHz | 598–747 MHz (rarely 1.3 GHz) |

31 fps is half the panel's ≈63 Hz: a frame usually misses one page flip. GPU work is cheap; building a frame on the CPU (UI draw + loop work) takes ≈15 ms at the low clock. Next: an animation CPU workload lease (the platform's `workload` QoS, as artwork decoding already uses) and less per-frame work (e.g. `album_detail` filters every track each frame); measure `ui.draw` on the host first. Video for the community: `~/Videos/y2linux-cover-flow-24.mp4` (40 s, the capture itself reaches only ≈10–15 fps over USB, so it looks choppier than the panel). Seen in the video: "3 songs · 0 min" for sub-minute albums (show m:ss); the centre shows the placeholder during very fast first passes until thumbnails are cached (expected).

## What to check

Scroll Cover Flow again while the live sample runs: `graphics_frames` should rise ≈55–63 per second during the glide.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
