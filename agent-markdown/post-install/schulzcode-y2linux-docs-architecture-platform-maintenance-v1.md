---
title: "Owner reset and state export - Innioasis Updater"
description: "Owner reset and state export <!-- knowledge-base-scope: source-contract -- Source-contract scope. This page describes software ownership and interface behavior. See curre"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-maintenance-v1.html"
---

# Owner reset and state export - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Owner reset and state export

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Owner reset and state export > **Source-contract scope.** This page describes software ownership and > interface behavior. See [current state](../CURRENT_PLATFORM_STATE.md) for the exact latest image > and physical limits; implemented or enabled does not mean qualified. 

Software contract; target filesystem/flush/reboot qualification remains PHYSICAL_GATE. No maintenance command has been run on Y2 during this pass. Commands operate only on identity-checked Y2DATA. They never format it or touch protected partitions, NVRAM, firmware calibration or factory records.

`y2-platform export-state` creates a private mode-0600 archive under `/data/exports`. It includes the atomic Reborn session (settings/queue/position) and Bluetooth preferred peer, excluding bonds and all private keys. Add `--include-database` for a consistent SQLite online backup/quick_check; the source is opened read-only and checked against replacement. Add `--include-network` only when deliberately exporting private WPA credentials. The manifest records that privacy choice, source identity, sizes and hashes. Each file and the SQLite snapshot is coherent; no cross-file transaction is claimed. Download the archive over authenticated USB SFTP and verify its reported SHA256. Incomplete archives have a `.partial` name, never a successful export receipt. No automatic import or untrusted archive extraction is provided.

Reset scopes are separate:````````````````

| Scope | Exact behavior |
| --- | --- |
| settings | Use defaults emitted by the installed Reborn binary; replace only model.settings in session schema 2. Preserve queue, position, library and music. Backup original session first. |
| network | Quarantine saved network directory; boot creates disabled/default network configuration. |
| bluetooth-bonds | Quarantine BlueZ adapter state and preferred peer. Bind-mount root remains intact; no copied-back bond material. |
| library | Quarantine database + WAL/SHM/journal as one recoverable operation; Reborn rebuilds its database. Music stays. |
| caches | Quarantine known platform/Reborn cache directories. |
| full-user | Explicit logical reset of known Reborn/music/network/settings/apps/legacy-player/cache/log and Bluetooth user state. Requires a second --erase-user-music flag. |

Full logical reset preserves owner SSH access, entropy, platform boot/update/ rollback records, existing exports and reset quarantine, factory/calibration, and unknown data directories. It is not secure erasure of every old byte or an indiscriminate Y2DATA wipe. Existing exports can preserve sensitive owner state and must be handled separately before handing the device to another owner.

`y2-platform reset plan --scope settings` first reports consumers that must be stopped. It never stops hardware or deletes files automatically. Stop the listed init services with a bounded owner command (for example `timeout 10 /etc/init.d/S90reborn stop`) and run plan again. If a process remains in kernel I/O, execution refuses rather than proceeding. The plan returns exact paths, identities, preserved state and a five-minute confirmation digest.`y2-platform reset plan --scope settings y2-platform reset execute --confirm DIGEST # Full user reset requires both the matching full-user plan and: y2-platform reset execute --confirm DIGEST --erase-user-music`

Execution rechecks process owners, update state, boot/mount generation and every target inode before mutation. A durable maintenance marker prevents Reborn, connectivity, BlueZ and readiness startup while an operation is incomplete. Each rename into `/data/reset-quarantine/ID` is fsynced and recorded. After interruption, stop any listed consumers and use `reset resume --confirm DIGEST` (and the full reset flag if applicable). Resume across a new boot requires the same validated data UUID, original inode identities and private journal. Conflicting new files are never overwritten. Keep the marker and inspect the exact source/quarantine paths if conflicts prevent resume; do not force a reset through uncertainty. On success the marker is removed; the owner reboots through the platform command so ordinary initialization recreates missing defaults and service bind mounts.

Quarantine makes reset recoverable but does not free its occupied space. Explicit `reset purge --id ID --confirm DIGEST` deletes only that completed reset's numeric payload entries, at most 256 entries/eight seconds per call. Repeat while it says `MoreRemaining`. It pins directories, rejects submounts, and unlinks symlinks without following them. The small manifest is retained. No cache cleaner ever purges this user-state recovery area or removes music automatically.

Tests exercise live WAL backup, credential exclusion, exact settings-only reset, process/mount/confirmation gates, interrupted multi-file reset across boot, full-reset preservation and symlink-safe bounded purge. Host tests are separate from physical eMMC power-loss behavior. All current services still run with owner/root privilege; this utility narrows paths and state transitions, not the trusted owner's administrative authority.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
