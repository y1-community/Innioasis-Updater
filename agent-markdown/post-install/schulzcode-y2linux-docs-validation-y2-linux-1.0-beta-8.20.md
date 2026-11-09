---
title: "Y2Linux 1.0 Beta 8.20 (Baseline 119) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.20 Baseline 119 Status: PUBLISHED as GitHub release baseline-119 2026-10-22. Release 1.0.0-beta.8.20 , Reborn 1.0.0-beta.8.20 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.20.html"
---

# Y2Linux 1.0 Beta 8.20 (Baseline 119) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.20 (Baseline 119)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.20 (Baseline 119)

Status: PUBLISHED as GitHub release `baseline-119` (2026-10-22). Release `1.0.0-beta.8.20`, Reborn `1.0.0-beta.8.20`, kernel `6.18.56-y2linux-1.0.0-beta.8.20`, update sequence 8400, root `2026.08-platform-v1.147`, Linux `0f0b4ed`, Reborn `cdae78e`. Built with `tools/production/release.py` (134 s, resumed workspace, update based on `baseline-118`): container suite 857 OK, host suite 884 OK, Reborn app tests; all seal checks PASS, no MediaTek firmware in any image. Installed on the owner's player before publishing (this exact build, OTA stage + apply in 62 s, Acknowledged). Milestone audit BETA-8.20 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 69cdc2581e7ce5f09b92ec9fb861f4eb66db3e22212c77b3cbc585039e7072e7 |
| Y2ROOT | 4d11d7e6ad07b104a26e338c2cd40e0fe920c100916083caaf07e70d0e0c21d0 |
| RECOVERY | d5954c6397dbb904e693c8d6d2919cfd5c11c5fc184df7e7d8c7b0787570e91e |
| Y2DATA (no SSH key) | 8c8ee8087c08e46f12681271f7613f35e0f3a0d121fad8bdc01d16e8a204c611 |

## What changed since Beta 8.19````````````````````````````

| Area | Change | Evidence |
| --- | --- | --- |
| #52: "Playback could not start: audio open deadline exceeded", every Play until a restart and after it | Reports y2linux-report-20261021-210225/-211858 (install 2813306c = the #48/#51 player, 8.19): every failed open is cs43130 XTAL not ready … status1=08 — the CS43131 itself flags XTAL_ERR ("crystal not running") — at the stock bias (crystal=04, 12.5 µA, the reset value stock also leaves); once the crystal started and later stopped while running (status1=49). 1 of 9 rail cycles recovered. Of 22 installs that sent reports only this one ever logged a crystal error (#48 on 8.11, #51 on 8.16, #52 on 8.19); its codec revision (A1), LK and eMMC type match unaffected players: a marginal crystal circuit on that unit. A crystal that fails to start, or stops while running, now gets the chip's strongest bias, 15 µA (CRYSTAL_SET = 2), written with the crystal down and kept in the register cache for the rest of the boot; players whose crystal starts keep the stock 12.5 µA. y2_hp/xtal shows boosted= and takes boost (tests) | Linux d63c4f6 (overlay 0030, tests/test_codec_clock.py: stock bias on a good start, 15 µA after a stop or a failed try, written only with the crystal down) |
| Reborn gave up too early | Reborn's open deadline (2 s) expired during its own second open (the kernel's tries + rail cycle take ≈1.4–1.9 s per open), so an open that later succeeded was still reported as failed and stopped. Now 5 s | Reborn 34a07b6 |
| Reports | y2_hp/xtal (running, failures, recoveries, boosted) is collected | Linux d63c4f6 |
| SD card / macOS (reporter: macOS 15.8.1, SanDisk 128 GB exFAT) | not involved: the reports' library has no ._/.DS_Store/Spotlight entries, every scan 0 failures/0 unreadable. Pulling the card only let the codec power off for minutes before the next (lucky) cold start | reports |

## Device results (owner's player, build 119)

Driven over SSH (`rebornctl`, evdev injection, screen captures). Each step checks: Reborn playing, position moving, ALSA `hw_ptr` moving, no new `XTAL`/`ASoC error` kernel line, the chip's live `INT_STATUS_1` without XTAL_ERR and `PWDN_CTL` with the crystal on.``````````

| Run | Steps | Result |
| --- | --- | --- |
| Stock bias (12.5 µA) | cold start after the codec powered down, 48 kHz FLAC (PLL path, clk1=01), 96 kHz FLAC (plays at 48 kHz), back to 44.1 kHz, 15 track changes 0.3 s apart, 20 changes 0.5 s apart, 30 Next/Previous presses, 5 Next, Play/Pause, pause 3 s/20 s, resume after the codec powered down (60–95 s), 48 kHz from a powered-down codec, 10.5-h M4B + seek to 9 h, MP3 chapter book, screen off/on while playing | all PASS, failures=0, no crystal kernel line |
| Forced 15 µA (echo boost) | the same steps | all PASS, CRYSTAL_SET=02 on the chip, only kernel line XTAL bias raised to 15 uA |
| #52 path by hand | playing, Music → Albums, ≈240 Cover Flow detents back and forth, open an album, Play | PASS: playback never stopped, the album played and moved on |

Harness misses that were not product faults: tracks on SD cards not inserted ("media source offline"), 4-s tracks during position checks, and the wheel's input node number changing after a restart (event2 → event3).

## Open
  - The fix cannot be reproduced on the owner's player (its crystal never fails); confirmation is owed by the #52

reporter (`y2_hp/xtal` in the next report: `boosted=1` and no failures means fixed). If 15 µA is not enough, the part is likely defective (no further software lever: the CS43131 needs its crystal; no external MCLK on this board).
  - Unchanged from 8.19: car AVRCP metadata, in-file seek for long books, #42, #45, #47 confirmation.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
