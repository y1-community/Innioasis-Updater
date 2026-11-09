---
title: "Y2Linux 1.0 Beta 8.12 (Baseline 108) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.12 Baseline 108 Status: PUBLISHED as GitHub release baseline-108 2026-10-20. Release 1.0.0-beta.8.12 , Reborn 1.0.0-beta.8.12 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.12.html"
---

# Y2Linux 1.0 Beta 8.12 (Baseline 108) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.12 (Baseline 108)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.12 (Baseline 108)

Status: PUBLISHED as GitHub release `baseline-108` (2026-10-20). Release `1.0.0-beta.8.12`, Reborn `1.0.0-beta.8.12`, kernel `6.18.56-y2linux-1.0.0-beta.8.12`, update sequence 7601, Linux `570ed90`, Reborn `90f3da6`. Built with `tools/production/release.py` (103 s, resumed workspace, update based on `baseline-106`): container suite 840 OK, host suite 867 OK, Reborn workspace tests and Clippy clean; all seal checks PASS, no MediaTek firmware in any image. Test build 107 (sequence 7600, identical except the codec-register path in reports) was installed on the maintainer's player and checked (below). Owner: "fix it all and build a point release … then install on my player and check … publish it". Milestone audit BETA-8.12 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 5b7d4d46b4b4771a33301c3c08c05b91b73c569ba186c0c64adee1b924606c27 |
| Y2ROOT | c5b733074b232d0c1b5e09bf76e918b96e97d7dbaf8c26c056ed36e501bd4b37 |
| RECOVERY | 50336208457eef75d223694c6511a160038c03e925f61463f6a9c21703b137b6 |
| Y2DATA (no SSH key) | 2ed9cbbaea53d8b092a088313be2ec1cf2abb7c2395db42105be6af4c15e7375 |

## The reports

Issues [#48](https://github.com/SchulzCode/Y2Linux/issues/48) and [#49](https://github.com/SchulzCode/Y2Linux/issues/49) and 16 uploaded error reports from five players (Beta 8.10/8.11, 2026-10-19/20):````````````````````````

| Finding | Players | Evidence |
| --- | --- | --- |
| Reborn crash loop at every start | a8125bf1 (#49), c077cc2e, c9daa105 | panic-last.json: playlists.rs:223 "end byte index 8 is not a char boundary" inside º / ’; only after scans that include the SD card; restart_budget_exhausted; RolledBack on two players; the unclean restarts are the users holding Power afterwards |
| Silence after EQ changes | 2813306c (#48) | cs43130 Error waiting for XTAL_READY interrupt: -110 6 ms before the 5th stream open in a burst of EQ changes; progress kept moving |
| Sleep refused for 4.4 h on battery | c43e8711 | PM ring SUSPEND_REQUEST → FILESYSTEM_SYNCED → EXIT -1, Y2SPM: CPU3 power-off 9 ms after PM: suspend entry; quarantine kept, 237 refusals |
| Dark display after a restart from the recovery | c077cc2e (GC9503V) | "SMI common gated" with CG_CON0=00000000, no "holding SMI common/larb0" line, larb0 wedged, vblank timeouts, 180 s health restore |
| Report gaps | all | no /proc or debugfs file in any report; three reports in 10 s for one event; a crash loop re-fired reborn_crash |

## What changed since Beta 8.11``````````````````````````````````````````````````````````````````````````

| Part | Change |
| --- | --- |
| M3U parsing | #EXTINF: / file:// prefix tests and %XX decoding no longer slice user text by byte; tests at every split point in UTF-8 and Windows-1252. Reborn 3ff346a. |
| Crash isolation | reborn_observability::isolated(): inside it the panic hook records panic-last.json ("isolated": true) and returns instead of exit(101); used per playlist file and job, per cover decode and per scanned song (then unreadable). Reborn bc2762d. |
| Audio open | A refused output open is tried once more after 250 ms. Reborn 2db37cf. |
| CS43131 clock | Crystal retry (100 ms, off, 5 ms, 300 ms); mclk_int_src recorded after the switch; a failure returns to RCO and fails hw_params; clock requests tracked per DAI (a hw_free after a failed hw_params or a repeated hw_params no longer drifts clk_req). Overlay 0030, Linux 4d77820, tests/test_codec_clock.py. |
| Suspend prepare | system-idle PM notifier at priority 1 (before cpu_hotplug_pm_callback), so parked CPUs come back before hotplug is disabled; a failed restore only warns. Linux c885c12. |
| Sleep guard | A failure that ended before TASKS_FROZEN is kernel_prepare_refused, retried after 120 s; anything later keeps the Defect A/B quarantine. Linux c93fcb7. |
| Loader display hold | The SMI hold is checked with the clock provider runtime-active (pm_runtime_resume_and_get). Linux d491201. |
| Error reports | One report per check (triggers), reborn_crash keyed on version+location+message, seq_files read through (all /proc and debugfs files were missing), codec regmap on *-0030 (bus 0 or 1 by probe order), serial= on the command line scrubbed. Linux 02ebd61, 81cd4e3. |
| Crash loop screen | reborn-supervise: light off after each failed start, reborn-splash --failed (Couldn't Start) after five, new budget on an SD card change, power-off on battery after 10 min (never during PendingHealth). Linux f056579. |
| Radio firmware | A complete Firmware/system.img copied after installation is verified and removed. Linux dccce63. |

## Device results (test build 107, maintainer's player, ST7701S)````````````````````````

| Check | Result |
| --- | --- |
| OTA 8.11 → 8.12 (stage + apply) with two crash-trigger playlists (’ at bytes 6..9, º at 7..9, é at 6..8, %’; UTF-8 and Windows-1252) on the SD card | Acknowledged; no panic, no supervisor exit; scans with both sources ran twice |
| Playlists screen | Both lists shown (6 songs each); the 1252 file decodes; the real song resolves, the others say Not on the player; same Reborn process |
| Loader display hold | "holding SMI common/larb0 for the loader display" at 0.37 s |
| 25 stream reopens (next/previous every 1.2 s) | No XTAL error, no open retry needed, stream RUNNING, SYS_CLK_CTL_1 = 0x04 (crystal, 22.5792 MHz) |
| Error report (Save Report, 8.7 s, 392 KB) | /proc/*, clk_summary, regulator_summary, wakeup_sources, suspend_stats present; leak check 0 of 44 private values; codec registers missing (path 0-0030 vs 1-0030 on this player → fixed in 108) |

## Known gaps
  - Build 108 itself was not installed on a player (the auto-mode classifier refused the install); its only difference

from 107 is the codec-register glob in `report.py` (host tests) and the sequence.
  - Owed on a player: a slow crystal (not reproducible here), sleep with a parked CPU (the player was on USB, which

refuses sleep), the Couldn't Start screen, restarts from the recovery on a GC9503V player.
  - The Couldn't Start screen keeps its old text (no SD card hint); that needs new splash artwork.
  - EQ changes still reopen the stream (a live filter change is a larger Reborn change).
  - Unchanged from 8.11: #47 confirmation, WAF rule and billing alert, sleep drain (#42), GC9503V confirmation (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
