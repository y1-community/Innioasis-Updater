---
title: "Y2Linux 1.0 Beta 8.38 (Baseline 146) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.38 Baseline 146 Status: PUBLISHED as GitHub release baseline-146 2026-10-25, installed on the owner's player before publishing. Release 1.0.0-beta.8.38"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.38.html"
---

# Y2Linux 1.0 Beta 8.38 (Baseline 146) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.38 (Baseline 146)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.38 (Baseline 146)

Status: PUBLISHED as GitHub release `baseline-146` (2026-10-25), installed on the owner's player before publishing. Release `1.0.0-beta.8.38`, Reborn `1.0.0-beta.8.38`, kernel `6.18.56-y2linux-1.0.0-beta.8.38`, update sequence 10310, root `2026.08-platform-v1.188`, Linux `4c79cdb`, Reborn `6c37d9f`. Built with `tools/production/release.py` (128 s, resumed workspace, update based on `baseline-144`): container suite 883 OK; all seal checks PASS, no MediaTek firmware in any image. Reborn host tests: 681 passed, strict Clippy clean. Label 145 (sequence 10300, the Bluetooth fix alone) was a device test build. Milestone audit BETA-8.38 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 40cb7974c9ca4e8d8e576bd7b8a6310933a030711255acf90d457c5ebef3b826 |
| Y2ROOT | edab74248bae8c2674c7680c5635b34f6d9df5f8bde3bc3134c0883ca8e3f733 |
| RECOVERY | badc21c055cb57e8b4fff6f01bbf3dc80d6ef65e22d292827a8c39b9d153565c |
| Y2DATA (no SSH key) | 2434a89f278bf2e7d11a29c0befbe2732da7a9690d0eb2ad33b21ca549f828d0 |

## What changed since Beta 8.37``

| Change | Detail | Evidence |
| --- | --- | --- |
| Bluetooth: sound after Pause → Play (ledger F43, install fae53a8f, AirPods Pro 2) | On Bluetooth, Pause releases the output and Play opens a new stream where the song was (about half a second). A BlueALSA stream drained and prepared again stayed silent in the headphones after every in-place resume (reports fef6e1e6 on 8.29, 73547e56 on 8.36), while every new stream — a skip, or a close and reopen 0.4 s apart — played. Wired pauses still hold in place | report timelines; not yet confirmed by ear with headphones that showed it |
| A smooth wave that moves with the music | The playing wave is one ribbon with shared joints and a one-pixel fading edge (anti-aliased without MSAA, no beading). Its height follows the loudness (typical music as before, loud up to about a third more, quiet calmer), bass swells it, highs ripple it. Measured in the audio thread before the volume (three bands, one-pole filters, meter.rs), timed by the output's delay (Bluetooth too). Home's now-playing card shows the same wave | meter tests (bands, loudness, delay, staleness); previews 14e/14f; on device smooth edges, ripple following the music, ≈1.7 ms CPU a frame |

No kernel, platform, memory map, partition or packaging change; session and settings unchanged.

## Open
  - F43: the reporter's confirmation with AirPods Pro 2.
  - Home redraws while music plays and it is on screen (as Now Playing does); nothing changes with the screen off.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
