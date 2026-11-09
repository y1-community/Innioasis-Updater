---
title: "Y2Linux 1.0 Beta 8.26 (Baseline 125) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.26 Baseline 125 Status: PUBLISHED as GitHub release baseline-125 2026-10-23. Release 1.0.0-beta.8.26 , Reborn 1.0.0-beta.8.26 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.26.html"
---

# Y2Linux 1.0 Beta 8.26 (Baseline 125) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.26 (Baseline 125)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.26 (Baseline 125)

Status: PUBLISHED as GitHub release `baseline-125` (2026-10-23). Release `1.0.0-beta.8.26`, Reborn `1.0.0-beta.8.26`, kernel `6.18.56-y2linux-1.0.0-beta.8.26`, update sequence 9000, root `2026.08-platform-v1.166`, Linux `518c641`, Reborn `404edb3`. Built with `tools/production/release.py` (137 s, resumed workspace, update based on `baseline-124`): container suite 871 OK, host suite 898 OK (one load-flaky report-queue test that passes alone, seen before this change too); all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.26 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 8a2d66f1f79da5fc839cb3322f55edb787ae9e2fe95c1f497172179d0df8a979 |
| Y2ROOT | f909056154fdc98e1fe85c94b0eb2b46fa248054e389aa6db2eb4f580e18880c |
| RECOVERY | ef4e369d037beb42b879760e44e86c41a63425c1d67f46fc00b2d700d671d474 |
| Y2DATA (no SSH key) | 6bd005bcf45a796a389ad8a767e6d186599d4e81f6f4059c6db790e5d7108d75 |

## What changed since Beta 8.25

The twelve uploaded reports pending on 2026-10-23 (8.16–8.25, ten players) were reviewed against Beta 8.25; findings F35–F41 in the review ledger (`UserReports/REVIEWED.md`), with new evidence for F12 and F13. No Reborn code changed.````````````````````````````````````````````

| Finding | Change | Evidence |
| --- | --- | --- |
| F36: after a real drain to 5 % a player turned off 15–22 s after every start, also on a charger at 3.72–4.03 V, five times in 13 h (97f11bb1, 8.16) | Three parts. A start on a charger no longer restores a saved percentage lower than the live estimate (a charger only adds charge; the charging screen can run for an hour first). The PMIC's power-on OCV is used only when the first sample comes within 2 min of the kernel start (after the charging screen it predates the charge). The 5 % shutdown applies on battery only: on a charger the shown value cannot fall, and the 3.4 V floor still turns a player off whose charger cannot carry the load. With the report's values the starts now show 80 % and 39 % and stay up; on battery a saved 5 % at 3.63 V still shuts down | Linux 1e51811; tests/test_battery_soc.py |
| F37: turning Wi-Fi on after the player slept with Wi-Fi off showed STARTING, then OFF or "interface disabled" 3 s later, a scan was refused, a second tap worked (72f7e3ee, a19646dd, 3 times) | Every sleep switched Wi-Fi off with rfkill block wlan, which also sets the default for every Wi-Fi rfkill made later; the wake restored it only when Wi-Fi was on. Reborn switches Wi-Fi on per device, so the cfg80211 rfkill made when the card starts came up blocked. y2-radio now switches each Wi-Fi rfkill by itself and never changes the default | Linux 7698bb1; tests/test_suspend_policy.py |
| F39: an update restart left no shutdown_pending/shutdown_complete and once hung until the player was forced off (471831b6, 8.20 → 8.24); c14a3860 reported a clean 8.21 → 8.22 update as an unclean restart. 2 of 55 update restarts in all reports | Cause unproven. The shutdown's journal writes get 3 s (were 1 s: a Python start and an fsync on a busy shutdown), and every shutdown step goes to pstore's message buffer (RAM, it cannot stall the shutdown), which the next boot's retained capture or the recovery keeps | Linux 1e51811; tests/test_platform_power_contract.py |
| F38: on a nonstandard charger (dumb adapter, charge-only cable) the player stayed awake and drained while "Charging" (cb904ffb, e7604e73) | Such sources get 450 mA, what a PC port already gets here, instead of 70 mA (below the awake load; stock asks 1100 mA). Sleep stays refused while charging: the charger needs the awake watchdog service, as on stock. Not yet qualified on a nonstandard charger | Linux 1e51811; tests/test_charge_limits.py, tests/test_power_policy.py |
| F35: WARN sme.c:1200 cfg80211_roamed at a driver re-association (ba0e41a6) | The roam event hands cfg80211 the BSS entry, as the connect path has since 8.13 (F1) | Linux 7698bb1 |
| F13: the saved network "not found" for up to an hour, also with Bluetooth off and the network listed at −66 dBm (cb904ffb); empty scans after wakes on 8.25 (29ed4ccb) | Evidence: a "not found" with the saved network listed records the entry's age in the scan table, its security flags and the saved network's key management (never a name or address) | Linux 7698bb1; tests/test_wifi_failure_evidence.py |
| F12: SD cards refused on 8.25 for a finding nobody could read (29ed4ccb) | Evidence: a refused card records what its unclassified fsck.fat lines said: lines with a path are only counted, quoted text and numbers are blanked | Linux 44e23e0; tests/test_platform_storage_tools.py |
| F41: songs called "Ready" or "1.0" replaced Reborn's shutdown answer and the release inside build IDs in reports | Library names without a letter, and a short list of state words, are no longer replaced; network, device and account names keep the strict rule | Linux 44e23e0; tests/test_error_reports.py |

Not changed: F40 (two ALSA underruns in one report, no kernel trace) stays a watch item.

## Device results (owner's player)````````````````````````````````````````

| Check | Result |
| --- | --- |
| F37 reproduced on 8.25 first | Wi-Fi off as Reborn does it, the sleep's y2-radio wifi off-runtime, Wi-Fi on as Reborn does it: the new phy4 rfkill came up soft=1, wpa_state=INTERFACE_DISABLED (the reports' symptom) |
| OTA 8901 → 9000 | staged in 9 s, back on 8.26 after ≈75 s, Acknowledged on health boot 1 |
| F37 on 8.26 | same sequence: y2-wifi alone blocked by the sleep step, the next phy1soft=0, COMPLETED; the normal wake path (off-runtime, on-runtime with Wi-Fi on) also COMPLETED |
| F39 trail | software restart: the next boot's retained capture holds every step (shutdown execute reboot user … journal_pending ok … sync ok … journal_complete ok, init_reboot ok); the two stage writes took 0.47 s and 0.55 s on an idle player (old limit 1 s); history shutdown_complete, orderly |
| F36 restore path | saved display set to 5 % (thresholds disabled by a temporary override, so a wrong result could not loop): the start on the PC port showed the live 96 %; overrides removed, back to 99 %, thresholds on. The low-battery case itself (live estimate within 40 points of 5 %) needs a drained battery and is covered by the host test with the report's values |
| F38 | PC port still source=1 limit=450000; no nonstandard charger available |
| F41 | a saved report keeps Y2LINUX-1.0.0-BETA-8.26 / -8.25 in every build ID and "outcome":"Ready"; no music tokens on this library |
| Health and playback | taint 0, no kernel warnings, Wi-Fi Online; wired playback at 44.1 kHz with pause/resume (hw pointer ≈44 100 frames/s), crystal tries=1 ready_ms=40 errors=0, 0 playback errors, 0 underruns |

## Open
  - F36 on a real drained battery and F38 on a real nonstandard charger: not reproduced on a player.
  - F39's cause: the next stalled update restart should leave its step trail.
  - F13's cause: the next "not found" report shows whether the listed entry was stale or rejected.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
