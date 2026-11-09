---
title: "Y2Linux 1.0 Beta 7.9 (Baseline 72) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7.9 Baseline 72 Status: PUBLISHED as GitHub release baseline-72 2026-10-17. Release 1.0.0-beta.7.9 , Reborn 1.0.0-beta.7.9 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-7.9.html"
---

# Y2Linux 1.0 Beta 7.9 (Baseline 72) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7.9 (Baseline 72)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 7.9 (Baseline 72)

Status: PUBLISHED as GitHub release `baseline-72` (2026-10-17). Release `1.0.0-beta.7.9`, Reborn `1.0.0-beta.7.9`, kernel `6.18.56-y2linux-1.0.0-beta.7.9`, update sequence 6250, Linux `2ac6abd`, Reborn `926ef45`, git tag `baseline-72` in both repositories. Built with `tools/production/release.py` in 125 s on top of Baseline 71: container suite 765 OK, all seal checks PASS, no MediaTek firmware in any image; the new boot script, MTP responder, start screen and platform files were checked inside the root image. Milestone audits STORAGE-SETUP and BETA-7.9 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md); plan: [INTERNAL-STORAGE-SETUP-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FINTERNAL-STORAGE-SETUP-PLAN.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 6b8b3309d38a041128f656de167fa1cb5a0e3203915fff7de08afd72310cd064 |
| Y2ROOT | 53a4409082dc7ba075ebc6a82b2a166da39397ce7b127f8259ae0bad8a31efd2 |
| RECOVERY | 06956f9db29fdfd6967078b563705ab9ccc75410c5b92c04760198d718bda2f5 |
| Y2DATA (no SSH key) | bcff5304238143181b84b75e7c71844188c7832001cf3f9e193327988b46c187 |

## Since Beta 7.8``````````````

| Part | Change |
| --- | --- |
| Internal Storage for every player | At start the stock FAT storage (p8) becomes Y2MEDIA (5.4 GiB ext4) by itself: nothing to keep → at once; user files ≤ 400 MB → kept (Y2DATA with SHA-256, then Old Player Files); a larger library → nothing changes, Old Storage read-only over USB, Reborn asks once, Settings → Storage → Set Up Internal Storage erases it and restarts. Every phase recorded on Y2DATA and resumable; never on an update's health boot or a low/unknown battery. mkfs.ext4 names every setting (identical to the first Y2MEDIA, host-checked with the real tool). Start screen: Setting up storage, Keeping your old files, Preparing Internal Storage, Moving your old files. (Linux 5d2801c, Reborn 93be94f) |
| Radio firmware (issue #39) | With Internal Storage the copy goes into its Firmware folder (any size fits, removed afterwards); the separate Firmware drive remains only without it. A copy refused for space says Not Enough Space for That File (zip file or SD card). The responder already refused such copies before writing (nothing left behind). |
| SD cards (issue #44) | A FAT card pulled out while mounted is mounted again (dirty bit and its boot-sector copy are the only findings allowed); a damaged card says Needs repair · Check it on a computer instead of No SD card. (Linux 3110f3a, Reborn b023daf) |

Host evidence: 792 Y2Linux host tests (setup cases, resume at every phase, refusals, leftover rules, real `mkfs.ext4` layout, real `fsck.fat` admission, Old Storage/Firmware views, splash phases; safety rules mutation-checked), 514 Reborn tests, strict Clippy, previews.

## Device test (owner's player)

Prepared 2026-10-16: Internal Storage (138 skin files, 2.6 MB) backed up to the computer and the SD card (hashes identical); p8 recreated as the stock FAT (serial `3F93-07E6`) with the 512 files of the 2026-10-10 stock backup, every hash identical (evidence `20261016/internal-storage-backup-before-stock-test`). Owed after the OTA install: restart once after the update is confirmed → case 2 (21 MB): start screen stages, *Internal Storage is ready · Kept 512 files in Old Player Files*, Y2MEDIA identical to before (features, UUID, label, geometry), kept files hash-identical to the backup; then the skins copied back.

## Known gaps

As Beta 7.8. Case 3 (large library) and a power cut during the setup are host-tested only.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
