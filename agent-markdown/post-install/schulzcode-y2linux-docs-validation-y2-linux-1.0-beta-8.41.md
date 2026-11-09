---
title: "Y2Linux 1.0 Beta 8.41 (Baseline 159) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.41 Baseline 159 Status: PUBLISHED as GitHub release baseline-159 2026-10-27 at the owner's word"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.41.html"
---

# Y2Linux 1.0 Beta 8.41 (Baseline 159) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.41 (Baseline 159)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.41 (Baseline 159)

Status: PUBLISHED as GitHub release `baseline-159` (2026-10-27) at the owner's word ("do the build and publish it"), after test builds 155–158 on the owner's player. Release `1.0.0-beta.8.41`, Reborn `1.0.0-beta.8.41`, kernel `6.18.56-y2linux-1.0.0-beta.8.41`, update sequence 10700, root `2026.08-platform-v1.201`, Linux `af69742`, Reborn `1358702`. Built with `tools/production/release.py` (resumed workspace, update based on `baseline-154`): container suite 895 OK, host suite 922 OK (one load-sensitive report test passes alone), Reborn 698 tests, clippy and rustfmt clean; all seal checks PASS, no MediaTek firmware in any image. Entry audits HAPTICS (#28) and SPEAKER, milestone audit BETA-8.41 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md); research and stock evidence in [SPEAKER-HAPTICS-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FSPEAKER-HAPTICS-PLAN.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 6a65f32b54418553b152e2bc19b009fbad9d0dde60a24fa6cd98a7586067e44e |
| Y2ROOT | 44d8f8ca61c34825bd8fe32235e1a30bec3f666f57d69d0ad7ebff509291f733 |
| RECOVERY | dead59f0ace4846fb847c4ecdf1b20d434ad3efeb647e65024ec2714f2e7c094 |
| Y2DATA (no SSH key) | a14d7fb87d31a707d93c0f3a0ec1c730c9a4b73eade0ad913651d90e671e2848 |

## What changed since Beta 8.40``````````````

| Change | Detail | Evidence |
| --- | --- | --- |
| Haptic feedback (#28) | The vibration motor is regulator-haptic on the MT6323 VIBR LDO, as the stock vibrator (REA: vibr_power_set VOSEL 5 = 2.8 V, dct_pmic_VIBR_enable 0x542 bit 15). PWRAP policy admits only the enable, the stock thermal shutdown (set once at boot, never cleared) and 1.8–2.8 V. Reborn: Customize > Haptics Off (default) / Light (2.0 V) / Strong (2.8 V, stock); one 60 ms tick per button press as stock's key vibration (framework-res config_virtualKeyVibePattern = 60 ms); no wheel ticks (30 ms per-step ticks felt buzzy) | test builds 155/158 on the owner's player; tests/test_haptics.py, PWRAP/PMIC tests |
| Internal speaker | The OCA72559/AW87559 amplifier (I2C1 0x58, GPIO8) with the stock register tables (donor driver, identical to stock aw87559_on/off), behind the CS43131 as the card's "PA". The codec writes the stock speaker route at HP power-up (PCM path 0x05, channel 2 on the left slot, full scale 1.73 Vrms). Outputs are exclusive; no switch under a running stream; no speaker while the detector reads a plug | owner's player: OCA72559 (ID 0x09) answers, route registers as stock mid-stream, speaker audible; tests/test_speaker.py |
| Headphone detection | The CS43131 detector (stock 0xCA) is read every 200 ms while the codec is powered (screen on: Reborn's DAC hold; or playback), as stock detects only then too. No codec IRQ: EINT16 would take the sticky bits the #52/#54 crystal start polls. A plug turns a playing speaker off at once; an unplug needs two reads. Reported on the card's "Headphone" jack | owner's player: jack 1 → 0 → 1 on real plugs, "speaker off" on each plug while playing |
| Reborn output | The Headphone Jack output plays on the speaker while the jack is empty (Output > Speaker, on by default as stock); mono (L+R)/2; Master −3 dB (stock's top speaker step). Headphones in move a playing speaker to them; headphones out pause | on-device path test below |

## On the player

Owner's player (ST7701S panel), test builds 155 → 158 by staged OTA, each Acknowledged, taint 0.
  - 155: motor input `regulator-haptic`, VIBR brought from 1.2 to 1.8 V at registration (admitted), VIBR_THR=1. Owner:

Light and Strong work but 30 ms wheel ticks felt "buzzy and mushy"; stock key-press feel chosen.
  - 156: OCA72559 found; manual tone on the Speaker pin audible; detector 1 → 0 on unplug. The audio I2C bus probed as

bus 0 on that boot, so Reborn's fixed `1-0030` path never saw the jack (fixed in 157: either bus, as the DAC hold).
  - 157: owner heard the speaker; headphones in while it played left Now Playing at "Starting": the jack change called

`load()` outside a model action, so the new output's start was never polled (fixed in 158).
  - 158: `rebornctl jack in|out` feeds a change where the kernel's report enters. Path test with the headphones out:

| # | Path | Result |
| --- | --- | --- |
| 1 | Play, jack empty | speaker, PCM running |
| 2 | Headphones in while the speaker plays | headphones, PCM running (was "Starting") |
| 3 | Headphones out while they play | paused in place, no sound |
| 4 | Play again | speaker |
| 5 | Paused on the speaker, headphones in, Play | headphones |
| 6 | Paused on headphones, headphones out, Play | speaker |
| 7–9 | Again in, same report twice, out while playing | headphones, unchanged, paused |

## Open
  - Overnight drain with 8.41 (speaker and haptics idle) not measured; the jack poll runs only while the codec is

powered and never marks it busy.
  - The speaker shares the wired volume; a separate speaker volume and a speaker high-pass were not added.
  - Real plug while the speaker plays was checked on 157's kernel side; on 158 only through `rebornctl jack`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
