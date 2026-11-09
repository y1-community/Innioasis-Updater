---
title: "Y2Linux 1.0 Beta 8.27 (Baseline 126) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.27 Baseline 126 Status: PUBLISHED as GitHub release baseline-126 2026-10-23, installed on the owner's player first. Release 1.0.0-beta.8.27 , Reborn 1."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.27.html"
---

# Y2Linux 1.0 Beta 8.27 (Baseline 126) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.27 (Baseline 126)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.27 (Baseline 126)

Status: PUBLISHED as GitHub release `baseline-126` (2026-10-23), installed on the owner's player first. Release `1.0.0-beta.8.27`, Reborn `1.0.0-beta.8.27`, kernel `6.18.56-y2linux-1.0.0-beta.8.27`, update sequence 9100, root `2026.08-platform-v1.167`, Linux `65e1c47`, Reborn `4947352`. Built with `tools/production/release.py` (134 s, resumed workspace, update based on `baseline-125`): container suite 878 OK, host suite OK; Reborn workspace tests, clippy and fmt clean; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.27 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | fdb2f8da58f4da93d723bd467ba1e46eb9b64975e28ef38d41dfa3fba80beed6 |
| Y2ROOT | 29cb8d2f30e7f3b5d5283412861bcf9ff43835b87d98bd3a0fff1404f9173e52 |
| RECOVERY | 28efbe111ca0c1a6b2dfe07d3556b57f54af12152d5bfe7757ffc86b884714c0 |
| Y2DATA (no SSH key) | 0d3ce17b35cc5fd1cf6949c6684848892a63f89f8289a9bcb9328e932f6e8238 |

## Why

A user on 8.25 (report 29ed4ccb, install 09cabe08, F12 in the review ledger): every SD card showed *Needs Repair · Check on a Computer* after it had been taken out to add audiobooks on a Mac; Disk Utility's First Aid did not help. The player refused any card whose read-only check found a line it did not know, so nothing played. The log showed the card pulled out while mounted, refused when it came back. The owner chose: all three phases, the repair only with the owner's confirmation.

## What changed since Beta 8.26````````````````````````````````````````

| Phase | Change | Evidence |
| --- | --- | --- |
| 0: what interrupted writes leave | Host reproduction (mkfs.fat/mcopy images with the states an interrupted copy leaves, fsck.fat 4.2 as on the player): a chain shorter than the file, a free first cluster, a lost chain with an orphaned long name, FAT copies that differ, two files sharing clusters. All five were refused as other; fsck.fat -a cleans all five. Two are invisible to Linux and Windows and are now admitted: FATs differ but appear to be intact (Linux reads the first FAT) and an orphaned long-name part | Linux 7668944; tests/test_platform_storage_tools.py (the captured lines) |
| 1: a damaged card plays | A FAT32/exFAT card whose check finds errors, or whose check does not finish, is mounted read-only instead of refused: the library scans it and it plays; nothing is written, so the damage cannot spread. Settings → Storage: Has errors · Playing only (Not checked · Playing only after an unfinished check); a notice when such a card comes in. Over USB the card is read-only. ext4 cards with damage stay refused (even a read-only ext4 mount replays its journal) | Linux 7668944; Reborn c1e60d6 |
| 2: Repair SD Card | Settings → Storage → Repair SD Card, confirmed (red: damaged files may be shortened or removed). Only on the card the player marked (read-only with errors, or refused), on a charger or above 30 %, with the player kept awake; playback from the card stops first. The card's tables (boot sectors, FATs; exFAT up to its cluster heap; ≤ 256 MiB, newest only) are copied to /data/system/platform/sd-repair/ for support, then fsck.fat -a -w / fsck.exfat -p / e2fsck -p, then the normal check: a clean card mounts writable again. The answer says how many files were shortened; sd-repair-last.json (no names) goes into reports | Linux 7668944; Reborn c1e60d6 |
| 3: prevention | A healthy card is protected: mounted read-only and writable only inside named windows with an end time — a computer connected over USB (renewed while the host has the player enumerated), a playlist change on the card (Reborn's playlist worker), a report saved to the card, the radio firmware import removing its system.img. The media tick (3 s) makes it read-only again when no window is left, which flushes it and clears its dirty bit. Reborn's audit found no other writes to the card (scanning, playback, covers, database, positions all stay on Y2DATA). Owner switch for the old writable mount: /data/system/platform/sd-always-writable | Linux 7668944; Reborn c1e60d6 |

## Device results (owner's player, exFAT card)``````````````````````````````

| Check | Result |
| --- | --- |
| OTA 9000 → 9100 | Acknowledged on health boot 1, taint 0 |
| Protected card, computer connected | claim read_only: protected, card rw while the host has the player enumerated (usb window renewed every 10 s); status Ready, writable: true, space Normal |
| Windows | a reborn window opens next to usb and ends again without closing the card; an unknown holder is refused; Save Report → SD Card wrote its file inside a report window |
| Cable pulled (17:12:09) | card ro at 17:12:13; fsck.exfat -n on the read-only card: clean (dirty mark cleared by the remount) |
| Unplugged | two songs started from the read-only card; product sleep 17:13:02–17:15:55 with the card read-only, woke normally |
| Cable back (17:15:57) | card rw at once; a cable bounce went read-only and back within 4 s |
| fsck.fat on the player | three damaged images from the host reproduction: the same lines as on the host, fsck.fat -a -w cleans each (check afterwards exit 0) |

## Open
  - Read-only fallback and Repair on a really damaged card were run on the host (fixtures with real `fsck.fat`

output, and `fsck.fat -a` on damaged images) but not on a damaged card in a player.
  - The reporter's `other` line itself is still unknown (8.26 records its shape).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
