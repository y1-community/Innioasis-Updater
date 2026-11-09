---
title: "POWER-FINAL-25 — Cover Flow at the panel's rate, short album lengths, macOS card metadata - Innioasis Updater"
description: "POWER-FINAL-25 — Cover Flow at the panel's rate, short album lengths, macOS card metadata Status: INSTALLED 2026-10-13; first check archive 119, superseded by 26. Package"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-25.html"
---

# POWER-FINAL-25 — Cover Flow at the panel's rate, short album lengths, macOS card metadata - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-25 — Cover Flow at the panel's rate, short album lengths, macOS card metadata

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-25 — Cover Flow at the panel's rate, short album lengths, macOS card metadata

Status: INSTALLED (2026-10-13; first check archive 119, superseded by 26). Package `out/y2linux-platform-v1-power-final-candidate-25/` (fallback = 24 = `baseline-24`), receipts `out/deep-sleep-final/build25-receipts/`. BOOTIMG `44a9c3cfcffb28538bb748d7a5923a7574c87b77223ffc0b360b662d38563cf7`, Y2ROOT `6f629a895e41ae9c75ccadada4a22e39752a39011b31bb84c02ea33f9eba8f67`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-25`, kernel `6.18.56-y2linux-platform-v1-power-final-25`, root `2026.08-platform-v1.55`, release `1.0.0-platform-v1-power-final-candidate.25`; Linux `f7eb741`, Reborn `ed6a8cb`. Platform as 24.

## Why 24 ran at 27 fps

24 shortened the loop's wait while animating, but the render gate still required 34 ms between frame starts (`render_time.elapsed() >= 34 ms`). Presentation is synchronous (`eglSwapBuffers` → `drmModePageFlip` → wait for the flip event), so a frame started ≥34 ms after the previous one lands on the 2nd or 3rd vblank of the ≈63-Hz panel: 21–31 fps, measured 27 median / 31 max.

## What 25 changes (Reborn `ed6a8cb`)
  - `frame_gap(gliding)`: 12 ms start-to-start while `Ui::gliding()` (Cover Flow glide, cover flight), so the vblank paces

frames; 34 ms otherwise. Spinners, fades and the power ring keep the calm budget (no 60-fps spinner during a scan).
  - The Interactive CPU lease (kernel floor 747.5 MHz, 250 ms) is renewed while gliding, not only per wheel event.
  - Album detail line ("9 songs · 38 min") cached per album and library. Host profile at 3000 tracks: `ui.draw`

0.033 ms/frame, two thirds of it that all-track scan.
  - Albums shorter than a minute show m:ss ("1 song · 0:42") instead of "0 min".
  - Scanner skips AppleDouble `._*` files (in `supported`) and `.Spotlight-V100`, `.fseventsd`, `.Trashes`,

`.TemporaryItems` folders; scans of a Mac-written card complete and prune again.

## Tests

Reborn: `cargo fmt`, `cargo clippy --workspace --all-targets -D warnings`, `cargo test --workspace` all pass; new tests for the frame gap, `gliding`, the sub-minute length/cache, and a card with a `._` file and an unreadable `.Spotlight-V100` (fails without the fix). Renderer unchanged (no GLES comparison needed). Platform: `validate.py` PASS, ELF closure 354 files PASS, installed ARM PASS, privacy clean, release inventory 108 packages, container suite 693 OK.

## Owner checks after the flash
  - Cover Flow smoothness: 40-s `metrics` sampler (frames/s from `graphics_frames` deltas) while scrolling; expect

well above 31 fps, ≈60 when frames fit one vblank. `graphics_frame_time_ms` shows frames that miss.
  - A rescan of the owner's card reports complete (no "11 traversal failures"); stale entries disappear.
  - Still owed from 24: start-up colour flash, Genres after the tag re-read; then the sleep tests (archive 119+).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
