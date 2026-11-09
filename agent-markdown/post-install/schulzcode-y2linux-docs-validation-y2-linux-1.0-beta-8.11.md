---
title: "Y2Linux 1.0 Beta 8.11 (Baseline 106) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.11 Baseline 106 Status: PUBLISHED as GitHub release baseline-106 2026-10-20. Release 1.0.0-beta.8.11 , Reborn 1.0.0-beta.8.11 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.11.html"
---

# Y2Linux 1.0 Beta 8.11 (Baseline 106) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.11 (Baseline 106)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.11 (Baseline 106)

Status: PUBLISHED as GitHub release `baseline-106` (2026-10-20). Release `1.0.0-beta.8.11`, Reborn `1.0.0-beta.8.11`, kernel `6.18.56-y2linux-1.0.0-beta.8.11`, update sequence 7500, Linux `9c7f079`, Reborn `727fd47`. Built with `tools/production/release.py` (133 s, resumed workspace, update based on `baseline-105`): container suite 827 OK, host suite 854 OK, Reborn workspace tests and Clippy clean; all seal checks PASS, no MediaTek firmware in any image. Not installed on a player before publishing (owner: "do fix 1 and 2 and publish as 8.11"). Milestone audit BETA-8.11 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 359be61e86baf6e2db67b2ae0a6958e414abf3ccce842beaa2d2f3cd33a8e44e |
| Y2ROOT | 03f0cefbdc31fc94946b498a7ed93b8fd557d71026e60abfa3c4fe703e6641c3 |
| RECOVERY | d86ccccdd125cced1d206d0c794337e0a64c1025993241e64dca51f4306e2faf |
| Y2DATA (no SSH key) | 0e381ca55fc30337a054c9dfd4d4f1d9724c0307190e68fb688867a2bfd73e71 |

## The report

A user wrote "My internal storage is still 700 mb after multiple restarts" with error report `y2linux-report-20261019-153610` (Beta 8.10):``````````````

| Evidence | Value |
| --- | --- |
| /run/y2/internal-media.json | Unavailable, filesystem_identity_not_y2media: p8 is still the stock FAT |
| /run/y2/internal-media-setup.json | Pending, reason battery_low |
| What they saw as storage | Y2DATA only: 789 MB, 729 MB free (the MTP drive "Firmware") |
| Every logged start | On battery, no charger: 3.54–3.59 V at 0.3 s; the charger came later (68 s, 105 s) |
| Power-on OCV / shown | BAT0 voltage_ocv 3.621 V (24.8 % on the stock curve) / 21 % |

Two faults:
  - Reborn dropped the reason. Every `Pending` said Restart to finish setting up, so the user restarted on

battery again and again, and each start refused the setup for the same reason.
  - The battery gate read the wrong voltage.`internal_media.automatic_blocked` compared `voltage_now` during the

boot load with 3.7 V. 3.7 V at rest is ≈39 % on the stock curve; with the boot sag (≈60–120 mV, ledger F30) a player needed roughly 45 % or more. The plan (STORAGE-SETUP) had said "battery ≥ 25 % or charging".

## What changed since Beta 8.10``````````````````````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FSTORAGE.md)

| Part | Change |
| --- | --- |
| Setup battery gate | On battery the setup now needs 25 % read from BAT0 voltage_ocv (PMIC power-on OCV, latched before the boot load; the same value the shown percentage starts from, stock oam_init) through the stock battery profile; voltage_now only when no OCV was latched; no profile → battery_unknown. Charging or USB input online still skips the check. Linux fee6b36. |
| Storage screen | InternalSetup::Pending carries SetupWait: battery_low/battery_unknown say Connect a charger and restart; an update's health boot keeps Restart to finish setting up. Preview 32-storage-setup-battery. Reborn f649609. |
| User guide | Storage: the setup waits below 25 % without a charger and what the screen says. |

The reporter's own player would still wait on battery (24.8 % at power-on); it now tells them to connect a charger.

## Device results

None: this build was not installed on a player before publishing. Host evidence: tests for the reporter's values (OCV 3.621 V → `battery_low`), an OCV above 25 % with `voltage_now` under load at 3.56 V → setup runs, missing OCV/voltage/profile → `battery_unknown`; Reborn parses the reasons and draws the new line (preview checked by eye).

## Known gaps
  - Owed on a player: the setup on battery above 25 % on a stock-FAT player, and the new storage line.
  - A `system.img` copied after the radio firmware is already installed is never removed (`radiofw.scan` returns at

`installed()` first); a second user asked whether the leftover copy may be deleted (it may).
  - Unchanged from 8.10: #47 confirmation, WAF rule and billing alert, sleep drain (#42), GC9503V confirmation (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
