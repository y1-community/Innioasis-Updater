---
title: "POWER-FINAL-30 — storage and decode performance pass - Innioasis Updater"
description: "POWER-FINAL-30 — storage and decode performance pass Status: SUPERSEDED, NEVER FLASHED ALONE 2026-10-14; contained in 31–34, installed as part of 33. Package out/y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-30.html"
---

# POWER-FINAL-30 — storage and decode performance pass - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-30 — storage and decode performance pass

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-30 — storage and decode performance pass

Status: SUPERSEDED, NEVER FLASHED ALONE (2026-10-14; contained in 31–34, installed as part of 33). Package `out/y2linux-platform-v1-power-final-candidate-30/` (fallback = 29), receipts `out/deep-sleep-final/build30-receipts/`. BOOTIMG `7d95f85517e8744fc4c19c904e422decaade4cf9d7cd19004b186e4cb4c302b9`, Y2ROOT `65467e6ab707cca8078a315ed31ed8f845cf11566151b37ac4910836fe2b82c2`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-30`, kernel `6.18.56-y2linux-platform-v1-power-final-30`, root `2026.08-platform-v1.60`, release `1.0.0-platform-v1-power-final-candidate.30`; Linux `6aa52e3`, Reborn `f08cf93`. Contains 27–29.

## Measured on 29 (boot `cac3e209`)
  - Library database (317 tracks, 393 KB): query 2.7 ms, open+checks ≈56 ms, initial catalog ≈70 ms; warm rescan ≈200 ms.
  - `session.json` durable save 7.9 ms (1.0 ms without fsync), on user actions only.
  - Start-up scan 6975 ms, all of it cold SD directory reads: `find /media/sd -type d` 7955 ms cold / 38 ms warm for 118

directories; one cold listing = ~200 unmerged 512-byte reads (~50 ms). The card itself: 85 MB/s sequential.
  - Pre-mount `fsck.exfat -n`: 315 ms cold.
  - FFmpeg pipeline (stage benchmark, % of one core at 1.2–1.3 GHz): MP3 320k decode 1.3 / pipeline 2.5; CD FLAC 0.9 /

2.1; 24/96 FLAC 2.1 / 4.6; AAC 0.9 / 2.0; `alimiter` ≈ half of each pipeline.

## What 30 changes
  - Kernel: plugged directory readahead for exFAT (`0068`), FAT (`0069`) and the ext4 batch reader (`0070`): a cold

directory cluster is one request instead of one per 512-byte sector. Read path only.
  - `noatime` for SD cards of every format and the internal Y2Media partition (no access-time writes during playback).
  - Reborn `f08cf93`: the limiter runs only when the DSP graph can raise a peak (active EQ or positive net gain); the

default pipeline costs about half as much CPU and loud masters are no longer limited above −0.18 dBFS.

## Tests

`test_exfat_readahead` (three plugged loops, noatime), `test_platform_storage_tools`/`test_internal_media` (mount options), Reborn `limiter_only_when_the_graph_can_raise_a_peak` (+ workspace tests, clippy, fmt). Kernel warnings unchanged (47). validate PASS, ELF 354, installed ARM, privacy, inventory, container suite 711 OK.

## Owner checks after the flash
  - Normal boot; the start-up scan in Reborn's log (`scan_completed elapsed_ms`) should drop from ≈7000 ms to well

under 1000 ms; cold `find /media/sd -type d` likewise.
  - Playback sounds unchanged (default settings: no limiter stage; EQ on: limiter present).
  - `mount | grep -E "media/(sd|internal)"` shows `noatime`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
