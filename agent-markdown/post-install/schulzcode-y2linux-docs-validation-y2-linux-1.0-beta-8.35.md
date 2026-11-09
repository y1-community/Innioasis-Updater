---
title: "Y2Linux 1.0 Beta 8.35 (Baseline 136) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.35 Baseline 136 Status: PUBLISHED as GitHub release baseline-136 2026-10-25, installed on the owner's player before publishing. Release 1.0.0-beta.8.35"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.35.html"
---

# Y2Linux 1.0 Beta 8.35 (Baseline 136) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.35 (Baseline 136)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.35 (Baseline 136)

Status: PUBLISHED as GitHub release `baseline-136` (2026-10-25), installed on the owner's player before publishing. Release `1.0.0-beta.8.35`, Reborn `1.0.0-beta.8.35`, kernel `6.18.56-y2linux-1.0.0-beta.8.35`, update sequence 9902, root `2026.08-platform-v1.178`, Linux `fc733e8`, Reborn `e0921a0`. Built with `tools/production/release.py` (106 s, resumed workspace, update based on `baseline-135`): container suite 881 OK; all seal checks PASS, no MediaTek firmware in any image. Reborn host tests: 662 passed, strict Clippy clean. Milestone audit BETA-8.35 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 060d80226afebf42e6a50c4cb74ce90413ab414808b6cb9bd0c1713b721d06ef |
| Y2ROOT | 85dd97301b7e3e2c52781983ad117268e45f711e3e2c9afe4dadfc86fdce04e5 |
| RECOVERY | 829e5c771f6619322a60576d7f9ec1240a92e5494d5e25249335622dcfae4cec |
| Y2DATA (no SSH key) | e2a6885fcfe407b637eaa2457ea16c6f18b4ced510005a0942daf96c92257f39 |

## Why

A user with FiiO FH7 IEMs (19 Ω, report 94debfc2, install 02f46e9f, Beta 8.34): "Not even the high gain setting can drive them properly … I can barely hear the song at 85." The report showed level High live and Master at −19.5 dB, volume 83 and a −6.9 dB headphone profile preamp, with no errors: 0 dBFS reached only ≈0.057 Vrms at the chip (ledger F45).

## Cause

Beta 8.5 to 8.34 held the DAC Master at −19.5 dB for every level so that nothing played louder than earlier builds. The loudest output was 0.106 / 0.149 / 0.183 Vrms (Low / Medium / High), against ≈0.71 on stock and 1.73 from the chip. The board probably also has ≈100 Ω in series with the jack (the chip's load measurement reads every load 102 Ω high), which costs a 19 Ω IEM about 16 dB. Not measured: the owner has no meter, so the levels below are chosen to work with or without that resistance. Assessment and numbers: [headphone drive plan](../planning/HEADPHONE-DRIVE-PLAN.md).

## What changed since Beta 8.34````````````

| Change | Detail | Evidence |
| --- | --- | --- |
| Master per level | Low −9 dB (≈0.35 Vrms at volume 100), Medium −6 dB (≈0.71, stock's loudest), High 0 dB (1.73). The C sink sets −24 dB until the amplifier is up, then the Master of the level it really runs at (rb_wired_masters) | Reborn 5a40103; core tests for the table |
| Volume in even dB steps | 10–100: 0.6 dB a step (1.2 dB a wheel click); 1–9: 3 dB a step to −81 dB; 0 silence (squared curve before) | volume_steps_are_even_in_db_and_reach_silence |
| Safe-volume warning | Safe level = the old loudest output (−14.7 dBV): safe volume 90 / 80 / 67. Wired volume up stops there and asks Raise the Volume?; the agreement lapses after 20 h above it (volume back to safe). rebornctl cannot go above it | UI test for the dialog; device check below |
| No louder after the update or a restart | A saved volume moves once to the same output (volume_scale); a start on the jack and a return from Bluetooth are capped at the safe volume. The normal restore now also gives the wired volume back after a Bluetooth absolute-volume session, as the recovery path did | migration test over all levels and volumes (never louder, within one step) |
| A level change keeps the loudness | A higher level lowers the volume at once; a lower level raises the number only for the new stream, after the old one is released | a_level_change_keeps_the_output_where_the_volume_reaches_it |

No kernel, platform, memory map, partition or packaging change.

## Device results (owner's player, build 136)``````````````

| Check | Result |
| --- | --- |
| Install by OTA staging | sequence 9902 Acknowledged; install ≈18 s |
| Volume migration | Low, volume 80 (old scale) → 76, volume_scale 1 |
| Low live | HP Output Level Live Low, Master 237 = −9.0 dB, reported hardware_mixer_gain_db −9.0 |
| Level changes while playing (owner, 6 changes Low/Medium/High) | each a clean stream restart (sink_reopened reason wired_settings), fade-in on a rise; High live with Master 255 = 0 dB |
| Warning | dialog shown at High's safe volume 67 (screenshot); Raise Volume logged loud_volume_allowed; volume up then passed 67 (71), loud_seconds counting |

## Open
  - Output not measured with a meter; the series resistance is still an inference.
  - Not tried on a device: the 20-hour lapse, the cap on a return from Bluetooth, a restart with a volume above the

safe level, distortion at High full scale on a low battery.
  - Owner feedback: at the same volume it is not louder (by design: the level change and the migration keep the

loudness); the extra range is above the safe volume after the warning.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
