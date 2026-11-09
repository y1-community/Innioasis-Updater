---
title: "Y2Linux 1.0 Beta 8.10 (Baseline 105) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.10 Baseline 105 Status: PUBLISHED as GitHub release baseline-105 2026-10-19. Release 1.0.0-beta.8.10 , Reborn 1.0.0-beta.8.10 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.10.html"
---

# Y2Linux 1.0 Beta 8.10 (Baseline 105) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.10 (Baseline 105)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.10 (Baseline 105)

Status: PUBLISHED as GitHub release `baseline-105` (2026-10-19). Release `1.0.0-beta.8.10`, Reborn `1.0.0-beta.8.10`, kernel `6.18.56-y2linux-1.0.0-beta.8.10`, update sequence 7400, Linux `9df5ccf`, Reborn `cfac12b`. Built with `tools/production/release.py` (106 s, resumed workspace, update based on `baseline-101`): container suite 826 OK, host suite 853 OK, Reborn 545 tests and strict Clippy, Worker 14 `node --test`; all seal checks PASS, no MediaTek firmware in any image, the error report upload key included. Test builds 103 and 104 (same version, sequences 7200 and 7300) were installed on the owner's player only; 8.9 (label 102) was never published, its change is in this release. Milestone audit BETA-8.10 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 5f4630f75e2bc91ad5f44435d5ac4f0dbcaa7b46a9b5c585707ed78020628ed3 |
| Y2ROOT | 3e8a0edf5e19dc959427753e96cd72de0d756c1355f296461be90c46b1b8bfc8 |
| RECOVERY | a5e3bd94566785b3a5ad110b12432f235ebc5d169e6ee5ddfd59f0cdac1b0a27 |
| Y2DATA (no SSH key) | b8cd84944ac4dab2762a5be9c631ea880043acb34c64f0a8c73c55196b78becf |

## What changed since Beta 8.8````````````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FERROR-REPORTS.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Ftools%2Freports%2FREADME.md)

| Part | Change |
| --- | --- |
| Charging (#47) | The start sequence refused any inherited charge voltage other than 4.175/4.2 V; the reporter's player held 4.1875 V (selector 31, probably left by stock firmware) and never charged on any charger (fault 0x80, -EIO, nothing in check_*). Now whatever CV, input OVP and battery OVP earlier software left is replaced by the stock values (4.175 V, 7 V, 4.3 V on) and read back; only a battery over-voltage the detector reports refuses. Refused inherited values are recorded in check_*. All 32 CV, 16 input OVP and the battery OVP states tested. Linux 4dc193e, 2ebca90. |
| Error reports over Wi-Fi | Opt-in uploads (the one-time question, Settings switch, Send Report Now, install ID) to a Cloudflare Worker + private R2 bucket (180-day expiry), pulled by tools/reports/fetch.py. Only on Wi-Fi, TLS clock, no update, ≥ 15 % or charging; certificate checked, no redirects; retries up to 3 days. Receiver budget in a Durable Object: 100 reports / 40 MiB a day for all, 10 per install, 30 per network, 2 MiB each: R2 stays in its free tier. ERROR-REPORTS, receiver, plan R3/R4. |
| Report screens | No topic for Save Report (8.9) or Send Report Now; live progress like the update download (Collect · Clean · Send/Save, percent, KB, time left). |
| Triggers | No report for: Wi-Fi joining a network (the failure record is rewritten on every connection), a sleep a wake event cancelled (-EBUSY), a pulled SD card's I/O errors, the boot-time DSI read lag when the screen lit anyway. |

## Device results (owner's player)

| Check | Result |
| --- | --- |
| Install | Test builds 103, 104 and this build 105 by stage + apply: each Acknowledged (7200, 7300, 7400), ≈45 s |
| Upload | Send Report Now on 104: built and in R2 in ≈12 s (523 KB, 166 sections); an automatic report (display, see below) and a waiting one went out by themselves after the router's stale DNS answer expired |
| Privacy | Leak search on the player for received reports: 0 of 203 private values |
| Receiver | Wrong key 403, broken body 400, GET 405, other paths 404; synthetic upload stored, duplicate 200, fetched byte-equal, deleted; R2 token read-only (DELETE 403) |
| Charging on 105 | PC port: constant current, no fault, CV 4.175 V |
| Finding | After a restart through the recovery the boot log shows "DSI register reads still lag" (the driver copes, the screen lights): the 8.4 restart fix covers normal restarts only |

Not checked on a player: the #47 fix itself (the owner's player holds CV 30, so it never hit the check), charging from a wall charger on this build, the progress page by eye, the one-time question on a player that never answered.

## Known gaps
  - #47: confirmation from the reporter owed.
  - Cloudflare WAF rate-limit rule and R2 billing alert (owner, dashboard): see the receiver README.
  - Unchanged from 8.8: battery current with a profile, output measurements, sleep drain (#42), GC9503V confirmation

(#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
