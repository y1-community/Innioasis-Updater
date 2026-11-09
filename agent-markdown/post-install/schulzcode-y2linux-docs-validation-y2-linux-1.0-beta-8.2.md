---
title: "Y2Linux 1.0 Beta 8.2 (Baseline 88) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.2 Baseline 88 Status: PUBLISHED as GitHub release baseline-88 2026-10-18, after the device check on the owner's player. Release 1.0.0-beta.8.2 , Reborn"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.2.html"
---

# Y2Linux 1.0 Beta 8.2 (Baseline 88) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.2 (Baseline 88)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.2 (Baseline 88)

Status: PUBLISHED as GitHub release `baseline-88` (2026-10-18), after the device check on the owner's player. Release `1.0.0-beta.8.2`, Reborn `1.0.0-beta.8.2` (identity only), kernel `6.18.56-y2linux-1.0.0-beta.8.2`, update sequence 6501, Linux `1d463f6`, Reborn `5aad5f1`. Built with `tools/production/release.py`: container suite 774 OK, host suite 801 OK, update suite (`tests.test_platform_update`) 34 OK, also under ThreadSanitizer and AddressSanitizer/UBSan; all seal checks PASS, no MediaTek firmware in any image. Baseline 87 (sequence
  - was the first test build of this release, never published. Milestone audit BETA-8.2 in

[roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 27dc7112de60bdd606694b93a23d78b97ef2f974c2abec0aa93b2bb33bbdd869 |
| Y2ROOT | b0bd1b88cbfc691bdd71a417cabe2744e050f65fa46d0c839cd3055c6f4a6e7e |
| RECOVERY | 184411f4097a5c75468aed0dc8bbecb7492bf81f9fd58b7ddb2ed543dea2cd22 |
| Y2DATA (no SSH key) | 34da6864bb12b562b3959db8b8576b1bf68c4caf38a6b88c2bc06482512633f8 |

## Faster updates (OTA-50)

The owner asked whether the update could be faster. The Beta 8.1 installer log showed where the time went: verify 1.9 s, backup 30.8 s, system 12.9 s, check 4.8 s, boot 1.1 s (53.5 s, plus a 4 s pause). Measured on the player: reading the 512 MiB root takes 3.7 s, zlib level 1 compression of it 20.4 s and inflating it 10.7 s on one core. The recovery has four cores online and used one.``````````````````````

| Part | Change (Linux f9c1eae) |
| --- | --- |
| Root payload layout | rootfs.ext4.gz is one gzip member of independent 1 MiB raw-deflate segments (pigz -i layout); the signed manifest adds segment_bytes, segments and raw_crc32. Any gzip reader still decodes it as one stream (Beta 8.1's own core queued it unchanged). At level 9 it is 41.8 MB (Beta 8.1's single stream: 41.6 MB). package.py decodes every segment on its own before signing. |
| Four cores | The recovery decodes the root, compresses the live-root backup and checksums the readback on four threads while the main thread does the I/O. Writes still compare each 128 KiB chunk with the medium and skip equal ones. A segment index that does not fit refuses the package. |
| Kept package | After the health ack the installed package stays in /data/updates/current/ (manifest, signature, root payload; boot payloads deleted). The next queue keeps it only if it is the running release (signature, sequence = running compat sequence, both source commits = versions.json); the recovery checks it again (queued manifest hash, extent, SHA-256) and moves its root payload into place as the rollback copy. Anything else falls back to the four-core backup of the live root. The root keeps no state of its own, so the signed image of the running release is a complete way back. |
| Space | The kept package (about 42 MB) is the last thing the download cleanup removes; without it the next install is only slower. /data/updates holds about 87 MB between updates (before: about 56 MB). |
| Restart | The Update installed screen restarts after 1 s instead of 4 s. |
| Found on the way | restore() kept a pointer to the journal's own failure text across a journal update and read it after it was freed (found with ThreadSanitizer). Fixed by copying it. |

Docs: [platform OTA v2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fplatform-ota-v2.md), [Recovery and updates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FRECOVERY-AND-UPDATES.md).

## Device result (owner's player, 2026-10-18)

| Install | verify | backup | system | check | boot | Installer |
| --- | --- | --- | --- | --- | --- | --- |
| Beta 8.1 (before) | 1.9 s | 30.8 s | 12.9 s | 4.8 s | 1.1 s | 53.5 s |
| 8.1 → 6500 (live root, four cores) | 1.8 s | 12.5 s | 4.5 s | 3.9 s | 0.8 s | 23.6 s |
| 6500 → 6501 (kept package) | 3.2 s | 1.8 s | 5.3 s | 3.9 s | 0.8 s | 14.9 s |

  - Both installs acknowledged by the platform on their own; apply to the running new system: 66 s.
  - 6501's backup record says `source: package` with 6500's root payload; after the ack `current/` holds 6501.
  - The queue's decoding check (before the restart) took 7.6 s instead of 15.8 s.
  - The readback (check) is bound by the eMMC: 512 MiB ≈ 3.7 s.

## After publishing: rollback from a kept package, and the 3.2 s verify (2026-10-18)

Owner rollback on the player (`y2-platform update rollback` on 6501, whose rollback copy was 6500's kept package, `source: package`): command at 15:41:35, player back on 6500 and healthy at 15:42:44 (69 s). Recovery log: `restore` 1.85 s → `check` 9.27 s → `restore` (BOOTIMG) 13.22 s → `restored` 14.01 s, i.e. both backups checked and the root written in 7.4 s (four-core decode, 128 KiB compare), readback 3.9 s, BOOTIMG 0.8 s. Journal `RolledBack`, `accepted.json``current_sequence` 6500 (high-water mark stays 6501), Reborn `healthy`, panel power-down armed. 6501's package stays in `current/` and is dropped by the next queue (not the running release). Logs: `out/ota50-rollback-88/{before,after}` (local).

Why verify took 3.2 s: not the verify. In `backup()` the kept-package check (signature, SHA-256 of the 41.8 MB root, rename) ran before `step=backup` was logged, so its time counted under verify, and *backup 1.8 s* was the BOOTIMG backup alone. Measured on the player: cold read of the kept root 0.31 s, SHA-256 0.93 s, one after the other. Fixed after the release (Linux `9c7dae7`, not yet in a release): the backup step is logged where it starts, the kept root is hashed on its own core while verify hashes the new package (its three payloads now in parallel too), and every install and restore phase records its milliseconds in the journal (`timings`).

## Known gaps
  - The parallel hashing of `9c7dae7` is host-tested only (34 tests, ThreadSanitizer, AddressSanitizer/UBSan).
  - Unchanged from 8.1: the sleep drain with the panel powered down is not measured yet (#42); the GC9503V

panel path awaits a GC9503V owner (#45).
  - `tests.test_platform_update` is not part of the container release gate (as before); it ran on the host.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
