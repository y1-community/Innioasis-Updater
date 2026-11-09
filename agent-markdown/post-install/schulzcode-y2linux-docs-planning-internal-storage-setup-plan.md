---
title: "Internal Storage for every player — plan (2026-10-16) - Innioasis Updater"
description: "Internal Storage for every player — plan 2026-10-16 Status 2026-10-17: IMPLEMENTED and released as Beta 7.9 Linux 5d2801c, Reborn 93be94f; device run on the owner's playe"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-internal-storage-setup-plan.html"
---

# Internal Storage for every player — plan (2026-10-16) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Internal Storage for every player — plan (2026-10-16)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Internal Storage for every player — plan (2026-10-16)

**Status (2026-10-17): IMPLEMENTED and released as Beta 7.9 (Linux 5d2801c, Reborn 93be94f); device run on the owner's player owed** (p8 restored to the stock FAT from the 2026-10-10 backup, evidence 20261016/ internal-storage-backup-before-stock-test). Deviations from the plan: start-screen progress in words (the boot screen never shows numbers: Keeping your old files, Preparing Internal Storage, Moving your old files); after *Set Up Now* the player restarts; the MTP responder needed two lines to pin Old Storage at its start; the Firmware drive's copies were already refused before writing when too large (only the message was missing). Ships with Beta 7.9 together with the fixes for issues #44 (done on `main`) and #39. Owner decisions 2026-10-16: automatic setup with three cases; about 400 MB as the "keep automatically" limit; kept files in `Old Player Files`; progress on the start screen while files are copied; every player gets exactly the same storage layout.

## Why

The 5.46 GiB partition p8 (the stock player's own storage) only becomes Internal Storage after `y2-platform internal-media provision` over SSH. Public images carry no SSH key, so community players never get it: they have the SD card and nothing else for music, and the radio firmware's Firmware drive sits on the small Y2DATA (800 MiB, ≈585–770 MB free). An unpacked 860 MB `system.img` can never fit there (issue #39); the 518 MB file from the Innioasis zip only just fits.

## Result: one layout on every player``````````````

| Partition | Name (label) | UUID | Size | Use |
| --- | --- | --- | --- | --- |
| p5 | Y2ROOT | 79324c69-6e75-4801-8000-000000000101 | 820 MiB | system (from the flashed image) |
| p7 | Y2DATA | 79324c69-6e75-4801-8000-000000000102 | 800 MiB | settings, logs, library database (from the flashed image) |
| p8 | Y2MEDIA | 79324c69-6e75-4801-8000-000000000103 | 5.46 GiB | Internal Storage, /media/internal/music |

Y2MEDIA is created with every ext4 setting named, so a later e2fsprogs cannot change it: `mkfs.ext4 -F -q -L Y2MEDIA -U …0103 -m 0 -J size=64 -b 4096 -I 256 -i 16384 -O none,has_journal,ext_attr,resize_inode,dir_index,orphan_file, filetype,extent,64bit,flex_bg,metadata_csum_seed,sparse_super,large_file,huge_file,dir_nlink,extra_isize,metadata_csum -E lazy_itable_init=1,lazy_journal_init=1`. Checked on the host (e2fsprogs 1.47.4) against the owner's p8 (made 2026-10-10 by `provision`): identical features, 358 336 inodes, 1 432 576 blocks, no reserved blocks. The owner's player already has this result; the setup never touches a valid Y2MEDIA.

## What the user sees
  - Flash with SP Flash Tool as today (same four rows; no new image, no partition-table change).
  - First start: the start screen shows Setting up storage for a few seconds; while kept files are copied the bar

moves with the progress (up to a couple of minutes for 400 MB). Then Reborn starts.
  - Over USB: Internal Storage (5.4 GB), SD Card if inserted. While the radio firmware is missing, Internal

Storage contains a folder Firmware with a README: copy `system.img` there (any size fits). The separate Firmware drive only appears on players without Internal Storage (case 3).
  - Reborn: Wi-Fi and Bluetooth are ready, the Firmware folder is removed; music goes to Internal Storage or SD.

Players already on Y2Linux: the same check at the first start after an update was confirmed (never during the update's 180 s health boot); Settings → Storage shows Restart to finish setting up Internal Storage until then.

## The three cases (decided before anything is written)

The platform mounts the stock FAT read-only (after the #44 read-only check) and lists it:

| Case | Old storage holds | What happens |
| --- | --- | --- |
| 1 | nothing, or only stock leftovers | set up at once, no question |
| 2 | user files ≤ 400 MB, and Y2DATA keeps ≥ 150 MB free after a copy | files copied to Y2DATA (hash-checked), set up, files moved to Internal Storage → Old Player Files (hash-checked); the library finds old music at once |
| 3 | more, or the old storage cannot be read | nothing is changed; Reborn asks once (Set Up Now erases / Later); over USB the old files are shown read-only as Old Storage to copy off; Settings → Storage keeps Set Up Internal Storage |

Stock leftovers (never kept): empty folders; `.android_secure`, `Android/data/com.android.providers.media/albumthumbs` (thumbnail cache), `.thumbnails` folders, `.nomedia`; computer clutter (`System Volume Information`, `.Spotlight-V100`, `.Trashes`, `.fseventsd`, `.DS_Store`, `._*`). Everything else counts as the user's, including `LOST.DIR`, `Themes` and app folders. Reference: the owner's stock p8 before conversion (backup 20261010/93) held 541 files, 31 MB — case 2.

Preconditions for any automatic run: p8 at the exact geometry (start 3742720, 11 460 608 sectors, internal controller) with a vfat filesystem; battery ≥ 25 % or charging; no update waiting for its health check; USB file transfer not yet running (the setup runs in `S02y2-media`, before USB and Reborn).

## Safety: every step can be interrupted

A record on Y2DATA (`/data/system/internal-media-setup.json`, survives formatting p8) names the partition (geometry, old FAT serial) and the phase. Each boot resumes from it:````````

| Phase | Power lost here → next start |
| --- | --- |
| staging (case 2: copying to Y2DATA) | old FAT unchanged; copying resumes (verified copies are kept, partial .part files redone) |
| formatting | p8 may be unreadable; the record (same geometry + serial, all copies verified) is the only thing that allows formatting again |
| migrating (onto Y2MEDIA) | resumes with hashes; copies on Y2DATA are removed only after every file verified on Y2MEDIA |
| done | record removed; status says how many files were kept |

Without a matching record, an unreadable p8 is never formatted automatically (reported only). Copies use the existing `copy_verified` (temporary name, fsync, SHA-256 of source and target, atomic rename). `/data/music` (old unprovisioned library) is migrated as `provision` does today.

## Changes

Y2Linux``````````````````````````````````````

| File | Change |
| --- | --- |
| tools/platform/y2_platform/internal_media.py | read-only inspection + case decision; setup() state machine with the Y2DATA record and resume; pinned mkfs.ext4; kept files to music/Old Player Files; read-only Old Storage mount for case 3 |
| etc/init.d/S02y2-media | internal-media setup --automatic before mount; skipped on update health boots and low battery |
| cli.py | internal-media setup [--automatic \| --confirm-serial X]; status shows case, file count, size, phase |
| observe.py | storage status carries the setup state for Reborn (counts only, never file names) |
| radiofw.py | Firmware folder on Internal Storage when it exists (already accepted by candidates()), separate drive otherwise; failed copy (mtp-events errno 28 or a stalled invalid file) deleted at once, state Failed/no_space; README names the zip's file and the SD alternative |
| usb.py | no Firmware drive when Internal Storage exists; Old Storage (read-only) in case 3 |
| reborn-splash phase table | phase Setting up storage with progress steps |
| tests | case decision on stock-like trees; resume at every phase (fixtures); pinned features with real mkfs.ext4; real mkfs.fat stock image; firmware ENOSPC cleanup |
| docs | INSTALL (SSH provisioning section removed, new first start), knowledge/internal-storage, readme, audit, report |

Y2Reborn````

| Part | Change |
| --- | --- |
| core / platform client | setup state (not needed · restart pending · ask (files, size) · running · done (kept) · failed); task InternalStorageSetup → y2-platform internal-media setup --confirm-serial <serial from status> |
| UI | one-time question (case 3); Settings → Storage row Set Up Internal Storage (refused while connected to a computer: Unplug from the computer first); message Internal Storage is ready · Kept N files in Old Player Files; Firmware not enough space message; boot label Setting up storage |
| tests / previews | question, row, messages, start screen |

## Testing
  - Host: everything above, mutation-checked; the owner's 2026-10-10 stock backup as the case-2 fixture.
  - Device, end to end on the owner's player (needs the owner's go, it writes p8):
    - copy Internal Storage music to the SD card with hashes (124 GB free there);
    - recreate the stock FAT on p8 (`mkfs.fat`, serial `3F93-07E6`) and restore the 541 files from the backup — the exact

pre-conversion state;
    - install Beta 7.9 over the air, restart after it is confirmed → case 2 runs: check Y2MEDIA (features, UUID, label,

geometry identical to today), `Old Player Files` hash-identical to the backup, start screen, timing;
    - optional: case 3 with > 400 MB on the stock FAT (question, Old Storage read-only, Set Up Now);
    - copy the music back from the SD card.

  - Optional second player: the #39/#44 reporter offered to test.

## Open

Device run 2 needs the owner's authorisation for writes to p8 over SSH (earlier SSH writes were stopped by the permission check; the owner can allow them or run the commands). Release Beta 7.9 (label 72, sequence > 6200) only on the owner's word.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
