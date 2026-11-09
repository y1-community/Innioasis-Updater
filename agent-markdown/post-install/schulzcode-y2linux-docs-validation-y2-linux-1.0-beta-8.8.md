---
title: "Y2Linux 1.0 Beta 8.8 (Baseline 101) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.8 Baseline 101 Status: PUBLISHED as GitHub release baseline-101 2026-10-19. Release 1.0.0-beta.8.8 , Reborn 1.0.0-beta.8.8 , kernel 6.18.56-y2linux-1.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.8.html"
---

# Y2Linux 1.0 Beta 8.8 (Baseline 101) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.8 (Baseline 101)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.8 (Baseline 101)

Status: PUBLISHED as GitHub release `baseline-101` (2026-10-19). Release `1.0.0-beta.8.8`, Reborn `1.0.0-beta.8.8`, kernel `6.18.56-y2linux-1.0.0-beta.8.8`, update sequence 7000, Linux `be71b6d`, Reborn `b6b6fbc`. Built with `tools/production/release.py` (117 s): container suite 792 OK, host suite 819 OK, Reborn 543 tests and strict Clippy; all seal checks PASS, no MediaTek firmware in any image. Builds 99 and 100 (same version and sequence) were superseded before anyone installed them. Milestone audit BETA-8.8 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | e5c2aff008c84cbd2b4fb7f6ac74c2ad7a0299bf7e2df4f4537fec217e018fb5 |
| Y2ROOT | eb291915b184fb8daa5cf3d49afb8c2cb84eb19e6e3084f4c00441656e13f3db |
| RECOVERY | 04b8f9d7b822f70b86fbc2fe9d7d2c39a5ae44f71481afaaea57d9805ba997d4 |
| Y2DATA (no SSH key) | ab7835b13876f05eafb1a3b0695ad23e6473834e2a8e87c53eac51d0173226f3 |

## What changed``[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FERROR-REPORTS-PLAN.md)````````````````````````````````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FERROR-REPORTS.md)

| Part | Change |
| --- | --- |
| Error reports, saved (platform) | y2-platform report save --to internal\|sd [--topic] builds the scrubbed report of ERROR-REPORTS-PLAN and writes Error Reports/y2linux-report-<local time>.tar.gz on the MTP top level of that storage (Internal Storage = /media/internal/music). User-initiated: no opt-in, nothing queued; the install ID only when reports are on. Real directories on the mounted filesystem only (no links out), the file is named only when complete, the folder is synced for an SD card pulled right after. report status adds upload (false: no uploader yet) and the writable destinations. Reports now also hold BAT0/charging_state (#47). Linux 190d713, d06c606. |
| Report speed | ≈47 s → ≈10 s on the player. JSON lines scrubbed as one text (a private key's string value replaced in the text; lists/objects under private keys and Bluetooth peers still value by value; known values also in their JSON-escaped form), logs cut at line ends into 256 KB pieces for 4 worker processes, tokens a keyed hash (<ssid#3fa2c1>, per-report random key, never written), the live commands run during the scrub, send/save at nice 10. Linux be71b6d. |
| Boot ID | A /run/y2 storage record names the boot ID, which has an ext4 UUID's shape: it was masked in the logs as a serial. No longer (it is part of report.json by design). |
| Reborn | About & Updates → Error Reports → Save Report → storage → topic; the page shows the progress and where the file went. Without an uploader only Save Report and What Is Saved show; the switch, Send Report Now, the install ID and the one-time question stay hidden (nothing would be sent). Previews 33h–33k. Reborn 6cca742, b6b6fbc. |
| User guide | ERROR-REPORTS. |

## Device results (owner's player, test build 98 installed, new platform code run from `/tmp`)````````````

| Check | Result |
| --- | --- |
| Destinations | Internal Storage (ext4) and SD card (exFAT) both offered and written |
| First run | Found the Internal Storage path bug: /media/internal/Error Reports was outside MTP's Internal Storage (/media/internal/music); fixed in d06c606 |
| MTP | Both folders listed by the PC (KIO); a new file in an already listed SD folder appeared; an MTP copy matched the player's SHA-256 |
| Time | 47–48 s before; 27 s with the text path; 10.1–11.2 s (five reports) with 4 workers; parent and workers at nice 10 |
| Profile before | 71 of 77 s (profiled) in scrubbing: 354 000 text() calls, 2.8 M re.sub; each pattern scans 2–3.5 MB/s on the Y2 |
| Equivalence | 6 973 real JSON lines: text path vs value by value, 0 differences (tokens aside) |
| Privacy | The player's own 199 private values (Wi-Fi, Bluetooth names, Last.fm, SSH, serials, queue) searched in every report: none found |
| Size | ≈465 KB per report, 161–163 sections, nothing cut |
| Clean-up | Test reports, folders and /tmp/y2p removed |

The released build itself was not installed on the player before publishing; the owner installs it by OTA.

## Known gaps
  - No upload (R3 Worker, R4 uploader); automatic triggers are not wired to a periodic check yet, so nothing queues on

its own.
  - Not checked on the player: Save Report from the Reborn screens (host tests and previews only), a FAT32 card, a

full or read-only card on the player.
  - Unchanged from 8.7: battery current with a profile, output measurements, sleep drain (#42), GC9503V confirmation

(#45), charging on #47's player.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
