---
title: "Y2Linux 1.0 Beta 8.42 (Baseline 163) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.42 Baseline 163 Status: PUBLISHED as GitHub release baseline-163 2026-10-28 at the owner's word"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.42.html"
---

# Y2Linux 1.0 Beta 8.42 (Baseline 163) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.42 (Baseline 163)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.42 (Baseline 163)

Status: PUBLISHED as GitHub release `baseline-163` (2026-10-28) at the owner's word ("do a build now and publish"), after test builds 160–162 on the owner's player. Release `1.0.0-beta.8.42`, Reborn `1.0.0-beta.8.42`, kernel `6.18.56-y2linux-1.0.0-beta.8.42`, update sequence 10900, root `2026.08-platform-v1.205`, Linux `7e5b151`, Reborn `25b8e06`. Built with `tools/production/release.py` (resumed workspace, update based on `baseline-159`): container suite 926 OK, host suite 953 OK, Reborn 707 tests, clippy and rustfmt clean; all seal checks PASS, no MediaTek firmware in any image. Review of 40 error reports and findings F50–F57 in `UserReports/REVIEWED.md` (private); milestone audit BETA-8.42 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 2d6464653e3db295e2cf10df0835b744d097ce0fb791f1e4c209c00ca207f36a |
| Y2ROOT | d7fa4af0c57ea48d3f10d9ca14f2a681a9fabbf02f1d71b86ace8f4c99dd86af |
| RECOVERY | a58a71d7e411c7b3b7676ee8c59e26f3256f2490f2839236ceb446f2de0d4925 |
| Y2DATA (no SSH key) | d8d4047caccc93795a2779a4890b593574f91a015db760b10fb2ef81276821f8 |

## What changed since Beta 8.41````````````````````````````````````````````

| Change | Detail | Evidence |
| --- | --- | --- |
| Sleep without relighting (F47/F48) | UART0 RX pad to GPIO in sleep as stock mtk_uart_suspend (d3b49f2); a refused sleep stays dark (2200bad); Reborn blanks at once on Power and no longer opens the Sleep page (57b47b2, 9ee61f0) | report 66e5feea; build 161 on the owner's player: 17.3 h asleep at ≈2 mA (voltage estimate), no kernel refusal |
| Large SD cards (F49) | admission check 20 s, an unfinished FAT32/exFAT check mounts read-only checking and media verify checks it in the background (84e5366) | report d32f8f3c (71 400 songs, 59 s check); host tests; slow-card device check owed |
| Reborn quick scan | automatic scans skip unchanged folders while exFAT/ext4 free space is unchanged (c2ef3af) | report d32f8f3c (62–70 s per restart); device timing owed |
| Wi-Fi/Bluetooth with empty PROTECT_F/S (#62) | a never-formatted factory partition (every byte zero) gives no MD records instead of stopping the radios; stock mounts them with check only and its modem uses defaults; anything else unreadable still fails closed (9ee3f04) | issue #62 report (8.40, non-FM 2026 player); host end-to-end test with zeroed and one-byte images; radio start owed on that player |
| Shutdown (F39, F50) | SoC watchdog armed for the whole shutdown (BAT0/watchdog_powers_off: a power-off reset ends off or in charging mode), pmsg begin/result per step, radio stop after sync one radio at a time, Wi-Fi IRQ not claimed when it cannot be cleared, a last power-off handler that never returns (no "Attempted to kill init" hang) | 5 hung restarts and 3 panic hangs in reports; build 162: a user restart wrote the full trail in 2.7 s |
| Updates (F34, F23, #63) | recovery watchdog from the first step; init waits for both partitions and probes the root again before rescuing | reports 5497435a, 37bb7ede; host tests |
| Bluetooth after a loss (F51) | Play with nothing in the jack waits up to 20 s for the headphones just lost (120 s after the loss or the wake), then plays there (Reborn 3a4860b) | 13 jack/speaker starts on one install; unit test |
| Wi-Fi (F52, F53) | only real credential reasons say "wrong password"; WRONG_KEY latches on the second; a saved network DISCONNECTED 30 s while visible is selected again; an INTERFACE_DISABLED interface is added again; wifi-journal.jsonl | 11 manual joins in 4 days on one install; host tests |
| Battery (F54, F55) | a warm restart keeps the saved percent (stock dod_init); sleep refused for the battery only at filtered 3.4 V or 5 % | reports 98499743 (95 % → 13 %), 189640af (refused at 37 %) |
| Power held after a wake (F57) | EVIOCGKEY after resume: a held Power starts the hold (Reborn 13f03d0) | reports a9d78ab5, 496f54ad |
| Dark screen at start (F17) | no DCS reads while DSI reads are doubled, DSI restart (≤ 2) when an enable shows no frames, splash CRTC cycle, Reborn EACCES on a screen-off before its first mode | report 3e55b45e (ST7701S); build 162 streams normally (vblank 16), no restart fired |
| Diagnostics (F56) | /sys/firmware/y2_pmic/power_status into previous-boot-evidence.jsonpmic (long-press reset record and setting, UVLO selector); a kept pstore panic is not re-sent | build 162: long-press reset enabled, 11 s, no record |
| Kernel size | CONFIG_LOG_BUF_SHIFT 19: the 1 MiB log comes from log_buf_len=1M; the Image was 5.4 KiB over the 12 MiB D08 cap, now 1.6 MiB under | build 162: log buffer data + meta data: 1048576 + 3276800 |

## On the player

Owner's player (ST7701S panel): 161 ran 22 h (overnight sleep above); 162 installed by staged OTA, Acknowledged on health boot 1; `y2-platform shutdown reboot --reason user` wrote `watchdog ok`, every step `ok`, `init_reboot ok`, and came back normally. Build 163 differs from 162 by the #62 provider change and the sequence; it was not installed before publishing.

## Open
  - Device checks per fix: warm restart on battery (`start: warm/saved`), sleep below 3.6 V, Bluetooth Play after a

sleep, Wi-Fi heal and interface re-add, Power held after a wake, watchdog power-off, a large slow SD card, quick-scan timing, #62 radio start on the reporter's player.
  - F56 (player dead during playback) cause open; F13/F40 watch.
  - Owner decisions: sleep floor, PMIC long-press reset policy (stock disables it), watchdog in normal use, `panic=10`

in the running system, Wi-Fi heal thresholds, panel re-init when LK reports `lcm=0`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
