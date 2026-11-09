---
title: "Over-the-air updates through the Y2 recovery image (OTA-35) - Innioasis Updater"
description: "Over-the-air updates through the Y2 recovery image OTA-35 <!-- knowledge-base-scope: source-contract -- Source-contract scope. This page describes software ownership and"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-ota-v2.html"
---

# Over-the-air updates through the Y2 recovery image (OTA-35) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Over-the-air updates through the Y2 recovery image (OTA-35)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Over-the-air updates through the Y2 recovery image (OTA-35) > **Source-contract scope.** This page describes software ownership and interface behavior. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result; implemented > does not mean qualified. Supersedes the root-only [signed update contract v1](platform-update-v1.md). 

A player on Wi-Fi checks for a new release, downloads it and installs the whole system: kernel, device tree, modules and rescue (BOOTIMG), the root file system with Reborn (Y2ROOT) and, when it changed, the installer itself (RECOVERY). Y2DATA (settings, library, music) is kept. Scope audit: [OTA-35](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23ota-35-full-over-the-air-updates-through-a-y2-recovery-image-scope-audit--2026-10-15&anchor=ota-35-full-over-the-air-updates-through-a-y2-recovery-image-scope-audit--2026-10-15).

## Why a recovery image

LK loads one boot image. BOOTIMG holds the kernel and the rescue, so a kernel cannot safely replace its own image: a torn write leaves nothing that boots. The stock LK (installed bytes identical to the analysed FM `lk.bin`, `bb1a93b4…`) boots the RECOVERY partition instead when the MISC partition starts with the Android bootloader command `boot-recovery`; it checks this before charging mode and has no key combo.

Two boot images that guard each other:``

| Running kernel | May write | Never writes |
| --- | --- | --- |
| from BOOTIMG (normal system, rescue) | RECOVERY, MISC message, ANDROID, USRDATA, FAT | BOOTIMG |
| from RECOVERY (y2.recovery=1) | BOOTIMG, MISC message, ANDROID, USRDATA, FAT | RECOVERY |

The kernel enforces this ([storage-policy.h](https://github.com/schulzcode/y2linux/blob/HEAD/kernel/platform/storage-policy.h)); the image is named by its own DTB (`bootargs … y2.recovery=1`), because LK's command line never reaches our kernel. The MISC window is the first 4 KiB only; LK's `ENV_v1` block at MISC+128 KiB stays read-only. Everything else (loaders, tables, NVRAM, protected and security partitions) stays read-only.

## Images

`RECOVERY.img` is built with every candidate: the same zImage and initramfs as BOOTIMG, the recovery DTB, the ramdisk wrapper label `RECOVERY` (LK checks it) and the boot-image name `Y2Recovery-1` (our updater checks it before it ever asks LK for recovery). The initramfs contains both paths; only a kernel started with `y2.recovery=1` runs [recovery.sh](https://github.com/schulzcode/y2linux/blob/HEAD/initramfs/production/recovery.sh), and only that kernel can write BOOTIMG. First installation: [one SP Flash Tool row](https://innioasis.app/guides/reborn-y2linux-y2.html).

## Release package and channel

`tools/update/package.py package --image Y2ROOT.img --bootimg BOOTIMG.img [--recovery RECOVERY.img]` creates `manifest.json` (schema 2), its detached Ed25519 `manifest.sig` and single-member gzip payloads `rootfs.ext4.gz`, `bootimg.img.gz` and optionally `recovery.img.gz`. The manifest binds product, board, layout/data/database schemas, `recovery_api` 1, release version, monotonic `sequence` (candidate × 100), minimum compatible sequence, kernel, root and Reborn versions, both source commits, key ID, rollback/downgrade policy, short release notes, and size, SHA-256 and raw SHA-256 of every payload. Nothing in it is acted on before the signature is verified.

Root layout (OTA-50, Beta 8.2): `rootfs.ext4.gz` is still one ordinary gzip member, made of independent 1 MiB raw-deflate segments (each ended with a full flush, the last with the final block: the `pigz -i` layout). The manifest adds `segment_bytes` (1048576), `segments` (encoded length of each segment) and `raw_crc32`. Any gzip reader, including the core of Beta 8.1 and earlier, decodes it as one stream; the current core decodes the segments on four threads. An index that is present but does not fit (count, lengths, sum, segment size) refuses the package. `package.py` decodes every segment on its own before it signs.

The channel is shipped in `/etc/y2linux/update-channel.json`: GitHub Releases of SchulzCode/Y2Linux, `releases/latest/download/manifest.json`. `/data/updates/channel.json` may override `manifest_url`. HTTPS redirects are followed only to the listed hosts (`github.com`, `objects.githubusercontent.com`, `release-assets.githubusercontent.com`); authenticity comes from the signature, not from TLS. The installed release's own sequence and the accepted high-water mark on Y2DATA refuse replays and downgrades; a development key may downgrade only with a signed manifest flag.

## Flow
  - Check (Reborn: Settings → About & Updates, or automatically once a day when Wi-Fi is online): only

the manifest and signature are fetched; `/data/updates/download.json` says `Checked` with version, size and notes. A failed background check leaves the page as it was. Never installs by itself.
  - Download: payloads go to a private staging directory on Y2DATA (space for the payloads plus a

root backup estimate and 96 MiB reserve), each is hashed against the signed manifest, then the native core decompresses and verifies every payload (ext4 identity of the root, MTK boot layout and name of both boot images) and queues the package. Space (OTA-46): a package left by a cancelled or failed update is deleted first; the current rollback copies count as free, because the recovery deletes them right before it writes the new ones; if the download still does not fit, disposable data goes one entry at a time until it does — everything in `/data/logs` except `system.log`, `recovery-last.log` and `recovery-display.txt`, the rotated `*.previous.jsonl` platform journals and finished qualification runs. Music (on its own partition), settings, the library and the rollback copies are never touched. Last of all goes the kept package (`current/`, see step 5): without it the next install backs up the live root, which is only slower. If that is not enough, the download is refused with `needed_bytes` in `download.json` and Reborn says how much system space the update needs. The same cleanup makes room for the manifest itself, so a check works on a nearly full volume. Cancel deletes the package. Progress (OTA-48): the download writes `/run/y2/update-progress.json` (RAM, four times a second: phase `download`/`verify`/`done`/`failed`, bytes, speed over the last four seconds, seconds left); the one decoding check (the queue's) writes `/run/y2/update-check-progress` (`<percent> check`). Reborn reads both directly, because the download task answers only when it is finished. Download and check run at nice 10. The journal on Y2DATA records only the start and the result.
  - Install (`Restart to Install`): needs the charger or ≥ 50 % battery. The core writes a newer

RECOVERY image from the package first (BOOTIMG is untouched by that), reads it back, checks that RECOVERY holds a Y2 recovery image, then writes `boot-recovery` / `recovery\n--y2-update\n` to MISC. The player restarts into the recovery (default since OTA-46; restarts are lit since 43). Owner override `/data/updates/restart.json``{"mode": "poweroff"}`: it turns off and Power starts the recovery.
  - Recovery: verifies the package again, backs up the current root (compressed extent) and the

whole 16 MiB BOOTIMG span to Y2DATA, decodes and checks the new BOOTIMG in memory, writes the root, reads it back from the medium, writes BOOTIMG with `O_DIRECT`, reads it back, records `PendingHealth` and only then clears MISC. It shows progress on screen and restarts into the new system (with the override: turns off; Power starts it). Low battery without a charger: it waits up to ten minutes for one, else always turns off with the request still set. Root backup (OTA-50): when the queue found a kept package of the running release (step 5; journal `kept_manifest_sha256`), the recovery checks it again (signature, the queued manifest hash, segment index and `raw_crc32`, extent equal to the live root's, SHA-256 of the payload) and renames its `rootfs.ext4.gz` to `previous.ext4.gz` (record `source: package`). Otherwise the live root is compressed into the same segmented layout. The root keeps no state of its own (host keys, Bluetooth, settings and journals live on Y2DATA), so the signed image of the running release is a complete way back. Decoding, backup compression and readback CRC run on four threads while the main thread does the I/O; the write still compares each 128 KiB chunk with the medium and skips equal ones. Owner's player: installer 53.5 s (Beta 8.1) → 23.6 s with the live backup → 14.9 s with the kept package (verify 3.2, backup 1.8, system 5.3, check 3.9, boot 0.8 s; the 3.2 s included the kept check, hashed in parallel with verify since 8.3). The readback is bound by the eMMC (512 MiB ≈ 3.7 s). Each run records its phases in milliseconds in the journal (`timings`). Time left (Beta 8.3): a plan of the run's phases with modelled durations (30 ms per encoded MiB hashed, 21 per MiB of live-root backup, 10 written, 7.5 read back; kept root 0.3 s, boot backup 1.7 s, BOOTIMG 0.8 s), rescaled by the finished phases' real speed, the current phase by its own byte rate. Progress lines are `"<percent> <step> <seconds left>"` (readers before 8.3 use the first two fields); the bar is time-weighted and never moves back.
  - Health: the platform acknowledges the new system when Reborn presents frames, answers and the core

checks pass (unchanged 180-second worker). The acknowledgement moves the installed package to `/data/updates/current/` (manifest, signature and root payload; the boot payloads are deleted) when its manifest is the one the journal installed. The next queue keeps it only if it is the running release: authentic and compatible (replay and minimum checks do not apply), its sequence equals the running compat sequence and both source commits equal `/etc/y2linux/versions.json`; otherwise it is deleted. Backups stay for an owner rollback (`rollback_allowed`).

## Failure handling``````

| Situation | Result |
| --- | --- |
| Power lost during backup or install | MISC still requests recovery; the next power-on restores both images (RolledBack) or, if backup had not finished, nothing was written. |
| Readback mismatch | Both images restored from the verified backups. |
| Backup corrupt when needed | RescueRequired: no automatic retry; the recovery screen asks for a computer. |
| Health not confirmed (deadline) | Rollback queued and MISC set at once; the next power-on restores. |
| New system never confirms (powered off early) | The BOOTIMG rescue counts boots; after two unconfirmed boots it requests recovery and powers off. |
| LK booted BOOTIMG although an install was requested | Nothing was written yet: the update is marked failed, MISC cleared, the intact system starts. |
| Request keeps getting lost | After three requests the rescue stays in RAM (RescueRequired). |
| No Y2 recovery image in RECOVERY | MISC is never written; the update is refused. |

Accepted risk: a new kernel that hangs before its initramfs runs cannot be caught (LK has no try-once boot). OTA BOOTIMGs are therefore byte-identical to candidates first flashed and checked with a computer. SP Flash Tool remains the outside recovery path.

## Commands`y2-platform update check|stage # channel default; --url / --package for owner tests y2-platform update status y2-platform update apply # battery gate, recovery image, MISC request, restart y2-platform update cancel # cancel a queued update and delete its package y2-platform update rollback # restore the previous system through recovery y2-platform update probe-recovery # owner test of recovery entry, no install y2-platform update recovery-status # MISC request and RECOVERY identity, read-only y2-platform update auto-check # what the daily check runs`

Native core: `check`, `check-manifest`, `queue`, `prepare`, `probe`, `misc`, `status`, `ack`, `cancel`, `rollback` (normal system); `boot-needed`, `boot-check` (BOOTIMG rescue); `recovery` (recovery image). Host tests drive the real core against files with real signatures, injected interruptions and readback faults ([test_platform_update.py](https://github.com/schulzcode/y2linux/blob/HEAD/tests/test_platform_update.py)); they are not power-loss evidence. Physical qualification: recovery entry, install, interruption, rollback.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
