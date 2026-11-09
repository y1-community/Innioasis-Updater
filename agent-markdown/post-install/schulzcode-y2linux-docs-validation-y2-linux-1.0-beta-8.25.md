---
title: "Y2Linux 1.0 Beta 8.25 (Baseline 124) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.25 Baseline 124 Status: PUBLISHED as GitHub release baseline-124 2026-10-23. Release 1.0.0-beta.8.25 , Reborn 1.0.0-beta.8.25 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.25.html"
---

# Y2Linux 1.0 Beta 8.25 (Baseline 124) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.25 (Baseline 124)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.25 (Baseline 124)

Status: PUBLISHED as GitHub release `baseline-124` (2026-10-23). Release `1.0.0-beta.8.25`, Reborn `1.0.0-beta.8.25`, kernel `6.18.56-y2linux-1.0.0-beta.8.25`, update sequence 8901, root `2026.08-platform-v1.165`, Linux `f7f23d4`, Reborn `40386bc`. Built with `tools/production/release.py` (111 s, resumed workspace, update based on `baseline-123`): container suite 867 OK, host suite 894 OK, all seal checks PASS, no MediaTek firmware in any image. Installed on the owner's player before publishing. Milestone audit BETA-8.25 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

Three builds of label 124: the first stopped at the production tests (the codec sleep harness in `tests/test_suspend_audio.py` did not know `y2_codec_up`, fixed in `85aac4e`); the second (sequence 8900) ran on the owner's player and made static in the headphones at screen wake (the stock start powered the headphone amplifier outside its DAPM sequence); the third (sequence 8901, `0a67d9a`) keeps the amplifier down during the start and is the published one. One host-suite run in between had one failure that a rerun did not repeat (894 OK); the failing test was not captured.````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | ca3788de6015e809622be2589d63379c44a6cf17ca889cc4a3689bde63a1282e |
| Y2ROOT | 675b2606ddb215a78f4eac4611a1c0380c60f0ef6b5ae8463171a02455240d92 |
| RECOVERY | 9504c3108d026a097d78eac30ddf1a0d7f879404b46774203aaf1c8537f15517 |
| Y2DATA (no SSH key) | 78633c969c8ddf738545dd49201f46487961d0a0b6a1a5bd60672ac17e91c66a |

## Why 8.24 was not enough (#52, #54)````````````````````````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FISSUE-52-54-CRYSTAL-HANDOFF.md)

| Evidence | What it shows |
| --- | --- |
| #52 report y2linux-report-20261022-230113 (install 2813306c, clean SP Flash install of 8.24; stock ROM before it played fine) | first song 146 s after boot, at 44.1 kHz (no PLL): XTAL not ready 146230 ms after power-up, status1=48 (XTAL_ERR, no ready flag), silent. After a restart, nothing played: ready=0 errors=1, so the error was already there 20 ms after power-up |
| #54 report 768b0d04 (install 0400eb78, 8.24) | the same: XTAL not ready 60800 ms, status1=48, errors=1, silent |
| Owner's player, 8.24 | ready_ms=30 errors=0 |
| Both 8.24 reports | cycles=0: 8.24's power cycle only ran for a crystal that had been ready or used before; the first song after a failed power-up got none |
| Stock RE (out/rea/fm-kernel.elf) | same VGP2 voltage (1800 mV), rail order and delays, crystal bias and clock select; stock cs43131_hw_init starts the crystal with the whole chip powered (PWDN_CTL=0), we powered only the clock parts (0xF0). Full analysis: handoff |

So the PLL theory of 8.24 was wrong: on these two players the crystal fails at power-up, and two units failing the same way while stock plays points to a difference in our start, not a bad crystal.

## What changed since Beta 8.24``````````````````````````

| Area | Change | Evidence |
| --- | --- | --- |
| Crystal start as stock (#52, #54) | Every DAC power-up starts the crystal with the chip powered as stock hw_init (PWDN_CTL=0) except the headphone amplifier (0x10: powered outside its DAPM sequence it was audible as static), waits up to 100 ms for the ready flag, then hands the other blocks back to DAPM (f0 idle) | Linux 55adb1e, 0a67d9a (overlay 0030), register model in tests/test_codec_clock.py |
| Retry | No ready flag or an error flag: rails off 500 ms and another start, three tries per power-up; the crystal is used after the last try anyway, as stock | same; mutation-checked (1 try, no stream cycle, clocks-only start all fail the test) |
| First song after a failed power-up | One more cold start before that stream (the 8.24 gap); the counter resets only on a real power-up, so a stream can never cycle without end (worst case 3 + 3 starts) | same |
| Tests for the reporters | module switches y2_xtal_full_power (default Y; N = 8.24's clocks-only start), y2_xtal_start_hp (default N; Y = exact stock start, amplifier included) and y2_xtal_quiet_start (no bias write and status read before the start); echo cycle > y2_hp/xtal runs one cold start; y2_hp/xtal adds tries= start_ms= stream_cycles= full_power= start_hp= quiet= | same |

## Device results (owner's player)````````````

| Check | Result |
| --- | --- |
| OTA 8800 → 8900 (second build) | back after ≈50 s, Acknowledged; ready_ms=30 tries=1; 10 × cycle: 10/10 first try at 30 ms; 5 × with y2_xtal_full_power=0: 5/5; play + 10 quick Next: PCM running, no crystal/ASoC/-110 line |
| Listening, build 8900 | static in the headphones when waking the player after 3 min with the screen off (the DAC had powered down and started again with the amplifier on) |
| OTA 8900 → 8901 (published build) | back after ≈60 s, Acknowledged; ready_ms=40 tries=1 start_hp=0; 10 × cycle: 10/10 first try at 30 ms; PWDN_CTL=f0 after the start |
| Listening, build 8901 | no static at the wake after 3 min screen off; playback normal |

## Result from the reporters (2026-10-23)

Both issues were closed by their reporters on 8.25:
  - #54 (install 0400eb78, report 5f909e65, first 8.25 boot): `y2_hp/xtal` shows `ready=1 ready_ms=30 tries=1 errors=0

cycles=0 cold_start=0 stream_cycles=0 full_power=1 start_hp=0`. The crystal, which on 8.22 and 8.24 flagged XTAL_ERR at every power-up on this unit, came up at the first try with the chip-powered start, exactly like the owner's player. 23 tracks started, `playback_errors=0`, one deep sleep, no codec warning in the boot. Reporter: "It works perfectly now!"
  - #52 (install 2813306c): "It works, and I couldn't break it." (songs, restart, screen off); no 8.25 report uploaded.

So the cause was the clocks-only start (`PWDN_CTL=0xF0`): the retries and the first-stream cold start were not needed on either unit, and neither switch comparison was run. Stays open only as a cosmetic item below.

## Open
  - #52/#54: none. The switches `y2_xtal_full_power`, `y2_xtal_start_hp`, `y2_xtal_quiet_start` stay as diagnostics; the

trim plan of the 8.24 handoff entry (remove non-stock crystal code) may now proceed.
  - Cosmetic: a manual `cycle` logs "codec power-cycled after a crystal error" and counts in `cycles=`; read `cycles=`

together with the reporter's test runs.
  - The amplifier-off start (`0x10`) was sufficient for both reporters; `y2_xtal_start_hp=1` (exact stock `0x00`) is not

needed and is not click-free.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
