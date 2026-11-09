---
title: "Y2Linux 1.0 Beta 8.21 (Baseline 120) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.21 Baseline 120 Status: PUBLISHED as GitHub release baseline-120 2026-10-22. Release 1.0.0-beta.8.21 , Reborn 1.0.0-beta.8.21 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.21.html"
---

# Y2Linux 1.0 Beta 8.21 (Baseline 120) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.21 (Baseline 120)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.21 (Baseline 120)

Status: PUBLISHED as GitHub release `baseline-120` (2026-10-22). Release `1.0.0-beta.8.21`, Reborn `1.0.0-beta.8.21`, kernel `6.18.56-y2linux-1.0.0-beta.8.21`, update sequence 8500, root `2026.08-platform-v1.148`, Linux `2e914d6`, Reborn `cdc6b43`. Built with `tools/production/release.py` (134 s, resumed workspace, update based on `baseline-119`): container suite 857 OK, host suite 884 OK; all seal checks PASS, no MediaTek firmware in any image. Installed on the owner's player before publishing (this exact build, OTA stage 9 s, install 17.5 s, Acknowledged). Milestone audit BETA-8.21 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | bec8a80610d6fa535864e22f63641bd6621db871b24f809f5550ca84c5287f9b |
| Y2ROOT | ad85d99c707be7552fd0678c6cae5853e29266c842b957e4f322d611abcd890b |
| RECOVERY | 469702ca78ef6e3f52c10ce866af1b1a2430e8bb4313f53ac2293ffefe88c870 |
| Y2DATA (no SSH key) | 1e8531024bfa42da01985b34be3cbf98a7f00a24b4432716adc4fce5cee9a3a8 |

## Why 8.20 was not enough````````````````````````

| Evidence | What it shows |
| --- | --- |
| #52 reports y2linux-report-20261021-221744 and -20261022-022000 (install 2813306c, 8.20) | 8.20 fails at 15 µA as well (XTAL not ready … crystal=02, boosted=1). After a 3-h rest it played; repeated Next then found a sticky XTAL_ERR (status1=49), the driver stopped and restarted the crystal, and the restarts timed out (1 of 6 recovered by a rail cycle) |
| #54 report y2linux-report-20261022-061935 (install 0400eb78, 8.20) | a second player: headphones never play (16 opens, every one XTAL_ERR at 12.5 and 15 µA, rail cycles no help), yet the same player plays on the stock firmware / Y2Player. "One marginal unit, no software lever" (8.20 report) was wrong |
| Stock kernel (REA/llvm-objdump on out/rea/fm-kernel.elf) | cs43131_hw_init: PWDN_CTL=00 (everything on, crystal included), msleep(20), SYS_CLK_CTL_1=04 (crystal, 22.5792 MHz), …, INT_MASK_1=9f (XTAL_RDY and XTAL_ERR masked), msleep(12). It never waits for XTAL_RDY and never reads XTAL_ERR. cs43131_on (stream start) only lifts PDN_HP/PDN_ASP; cs43131_off sets them again; the crystal keeps running until the codec loses power |
| Our overlay 0030 (8.17–8.20) | started the crystal only at hw_params, stopped it before every retry (tries of 100 and 300 ms, then 500 ms after a rail cycle: at most ≈0.5 s of continuous running), stopped it after a failed open and after any sticky XTAL_ERR, and the codec's rails dropped 100 ms after a close. A crystal that needs longer than that never got going; on stock it simply runs |

## What changed since Beta 8.20````````````````

| Area | Change | Evidence |
| --- | --- | --- |
| Crystal start (#52, #54) | As stock: the crystal starts when the codec powers up (runtime resume, after the cache replay), stops only with the rails (runtime suspend). A stream waits for XTAL_RDY until the crystal has run 1 s in total and then uses it anyway, logging XTAL not ready N ms after power-up, used as stock does with the live clock registers. Ready/error flags seen later are counted and logged, never acted on. No automatic 15 µA boost (stock leaves the 12.5 µA reset value; 8.20 showed it does not help), no rail cycle. A PLL that never locks (48 kHz family) still fails that open and leaves the codec on RCO, with the crystal running for the retry | Linux 9ba00b9 (overlay 0030, tests/test_codec_clock.py register model incl. a 5-s crystal, tests/test_suspend_audio.py) |
| Codec idle | runtime autosuspend 5 s instead of upstream's 100 ms, so track changes and short gaps keep the running crystal | same |
| y2_hp/xtal | running= ready= unconfirmed= errors= boosted=; ready is the last power-up's result; boost (tests) sets 15 µA from the next power-up | same |

## Device results (owner's player, build 120)

Driven over SSH (`rebornctl`), host harness: each step checks Reborn playing, position moving, ALSA `hw_ptr` moving, no new `XTAL`/`ASoC error`/`PLL_READY` kernel line, plus `y2_hp/xtal` and the codec's runtime state.````````````````

| Run | Steps | Result |
| --- | --- | --- |
| Stock bias | cold start from a suspended codec (44.1 kHz MP3), 30 Next/Previous 0.3 s apart, 20 Next 0.6 s apart, pause 3 s, pause 12 s (Reborn keeps the PCM open), 48 kHz FLAC (PLL), 96 kHz FLAC, back to 44.1 kHz, stop 8 s (codec suspended, running=0), 48 kHz from the powered-down codec, 44.1 kHz again, long pause (Reborn closed the sink after 68 s, codec off) and resume, 3 × 12 Next/Previous 0.25 s apart | all PASS, every power-up ready=1, unconfirmed=0 errors=0, no crystal kernel line |
| boost (15 µA) | stop 8 s, power-up at 15 µA (CRYSTAL_SET=02, SYS_CLK_CTL_1=04 as stock), 15 Next 0.4 s apart | PASS; only kernel line the expected XTAL bias 15 uA from the next codec power-up |

Harness misses that were not product faults: the expected boost notice counted as a new kernel line, and Next landing on 4-s test tracks (position restarts between two samples). The owner's player stays at 15 µA until its next restart.

## Open
  - The slow-crystal path (`unconfirmed`, crystal used without its flag) cannot be reproduced on the owner's player

(its crystal is ready within the first poll); confirmation is owed by the #52 and #54 reporters (`y2_hp/xtal` in a report: `unconfirmed` > 0 with audio playing means the stock path carried it). If such a player plays silence with a moving position, the crystal really does not run in time and a longer pre-start (e.g. keeping the codec powered while the screen is on, as stock) is the next lever.
  - #53 (clock shows the build time without Wi-Fi): diagnosed (no network time, RTC not retained), not changed in 8.21;

awaiting the owner's choice (manual time, last known time, or hiding the clock until it is known).
  - Unchanged from 8.20: car AVRCP metadata, in-file seek for long books, #42, #45, #47 confirmation.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
