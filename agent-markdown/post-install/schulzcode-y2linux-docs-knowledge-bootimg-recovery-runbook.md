---
title: "Historical exact-backup runbook and current recovery route - Innioasis Updater"
description: "Historical exact-backup runbook and current recovery route <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate ident"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-bootimg-recovery-runbook.html"
---

# Historical exact-backup runbook and current recovery route - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Historical exact-backup runbook and current recovery route

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Historical exact-backup runbook and current recovery route > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current risk-accepted BOOTIMG-only experiment/restore procedure: [Y2B-240](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment.md). The exact-current-backup procedure below is optional historical work.

Current policy: [D11–D13 risk-accepted diagnostic](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md) supersedes the earlier absolute authentication/current-backup/full-handoff gates below. This document retains the historical assessment; watchdog, observation, verified recovery and BOOTIMG-only scope remain mandatory. No flash authorized.

2026-09-08, Y2E-145. Prepared procedure, not executed or ready for unattended use. Current BOOTIMG backup: NOT ACQUIRED. The owner-proven SP Flash Tool v5.2032 route is accepted. Exact historical DA/entry details and current acquisition/independent-retention requirements remain open. See [launch assessment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md) and [recovery baseline](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md).

## Pinned inputs and address semantics````````````

| Item | Exact value |
| --- | --- |
| Tool | /home/luca/Downloads/SP_Flash_Tool_v5.2032_Linux/flash_tool, v5.2032.00 / 5.2032.00.sn100 |
| Tool SHA-256 | d618e7d08ba5a4020038921a95336a3805a4b2cf17a374fd308cc5299ea7d9d8 |
| Bundled DA candidate | Same directory, MTK_AllInOne_DA.bin; SHA-256 46cd175d7556e6e80b13f6a70827c6931a5dfa25a09c3cc50e75ba7ff9327618 |
| Scatter | /home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/MT6582_Android_scatter.txt |
| Scatter SHA-256 | e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e |
| BOOTIMG readback region | EMMC_USER |
| Physical start | 0x01d80000 (30,932,992 bytes) |
| Length | 0x01000000 (16,777,216 bytes) |
| Exclusive end | 0x02d80000 (47,710,208 bytes) |
| Scatter logical address | 0x03180000; do not enter this as physical EMMC_USER readback start |
| Optional later installed-LK acquisition | UBOOT EMMC_USER start 0x01d20000, length 0x00060000; separate readback record, no write |

The 16 MiB extent is from both current dumchar metadata and the reconciled scatter. It is not a guessed mmcblk partition number: stock exposes BOOTIMG through dumchar and whole mmcblk0. PRELOADER's vendor span must not be reused as an eMMC boot-region read length.

## Readback prerequisites and acquisition
  - Confirm the exact DA and physical power/button/USB sequence of the successful owner operation. The bundled DA hash above is a candidate until selected and logged for the new procedure. Record target MT6582/eMMC identity, tool state, cable/port, power state and output location. A normal USB/ADB connection is not an SPFT readback session. No security bypass, auth-file substitution or DA patch is part of this procedure.
  - Establish trusted power and an operator-controlled transition to the proven connection state. Before changing mode, preserve the current Android identity/capture. If the connection sequence is unknown, stop. No trial reset/button combinations, automatic adb reboot or emergency-mode experiment is specified here.
  - In SPFT Readback, configure one explicit EMMC_USER record with the physical start and length above, saving to a fresh `bootimg-current-read1.bin`. Independently verify the displayed region/start/length and use no Download/Format/Memory Test command. Inspect MT6582/eMMC identification and abort on mismatch, authentication error, request to format, unexpected write, or undefined region/address semantics. Loading the DA changes volatile device state even though the requested storage operation is read-only; it is not passive ADB.
  - Complete readback using the established connection procedure and retain the entire operation log. Repeat the same immutable BOOTIMG range into `bootimg-current-read2.bin` and compare exact bytes. Neither file existed before this investigation. Do not generate empty placeholders and call them backups.
  - Require both files to be exactly 16,777,216 bytes with identical SHA-256 and byte contents. Independently parse the legacy Android header/page/MTK KERNEL+ROOTFS wrappers and their extents; all declared payloads must fit the 16 MiB image. Identify the active image prefix against known local images without treating prefix similarity as full-partition identity. Preserve the full trailing partition contents.
  - Retain the full readback, tool/DA/scatter hashes, region/range, target identity, UTC/operator/connection record and logs. Store and rehash another copy on independent storage accessible during recovery. Another directory or worktree on this disk is not independent retention. Current BOOTIMG is normally immutable during Android operation, but this does not establish consistency of mutable NVRAM/protect regions; use a separate reviewed acquisition plan for those required backups and recovery partition.

Host verification after real acquisition:`stat -c '%s' bootimg-current-read1.bin bootimg-current-read2.bin sha256sum bootimg-current-read1.bin bootimg-current-read2.bin cmp bootimg-current-read1.bin bootimg-current-read2.bin`

These commands check retained bytes only. They cannot prove the DA read the selected current device/range; operation and identity evidence must accompany them. No shell-level raw acquisition command is provided for the present denied ADB interfaces.

## BOOTIMG-only restoration after a separately authorized experiment
  - Verify the current-device backup and independent copy, tool, DA and original scatter against the recorded manifest. Resolve all acquisition/address checks before relying on restoration. Do not substitute the factory package boot.img for exact current state: it is an owner-proven fallback, not the acquired installed image.
  - Load the verified original scatter in SPFT. Select Download Only. Explicitly deselect every partition, then select BOOTIMG only and point it to the verified full 16 MiB current-device readback. Verify the resolved BOOTIMG partition and file length. If this tool/DA refuses the raw full-partition backup, stop and research its image acceptance; do not truncate, wrap, repartition or select another scene automatically.
  - Record/review the final target list before starting. PRELOADER, UBOOT/LK, MBR/EBRs, SECCFG, NVRAM, PROTECT, SEC_RO, RECOVERY, ANDROID, USRDATA and all other rows must remain unselected. No Format All, Firmware Upgrade, Write Memory, whole-disk restore, checksum bypass or preloader write. UI defaults and `CheckedItems=9,11` in a configuration file are not a reviewed target list.
  - After separate authorization, perform the owner's exact proven connection sequence with the tool waiting. Stop on timeout or unexpected identity/security/format prompts. Do not improvise modes or buttons. The intended write is exactly EMMC_USER [0x01d80000,0x02d80000); bounded erase behavior of the chosen tool/DA must be established before relying on preservation of neighboring regions.
  - Require successful operation logs and a fresh full BOOTIMG readback matching the original backup exactly. Start stock Android using the established method and verify owner-defined UI, storage, audio, radio/calibration and power behavior. A green tool check alone proves neither byte-exact restoration nor correct user state. Preserve before/after evidence.

The operation-specific timeout, DA/entry/power steps, full-image acceptance, transport erase behavior and post-restore checklist remain to be supplied/verified. This is a concrete blocked runbook, not a claim that an exact recovery execution has already been demonstrated. The original successful SPFT recovery remains strong evidence and does not need destructive re-proving. No restoration, readback, DA upload or candidate flash was performed in this session.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
