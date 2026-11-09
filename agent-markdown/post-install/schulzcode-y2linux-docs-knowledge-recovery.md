---
title: "Recovery baseline - Innioasis Updater"
description: "Recovery baseline <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-recovery.html"
---

# Recovery baseline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Recovery baseline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Recovery baseline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-08 hardware update: [Y2B-240 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment-result.md) records owner-observed green PID1 evidence and successful BOOTIMG-only Android recovery using the owner-selected boot-adb image. Timed heartbeats, cutoff and exact FM restoration were not verified. Historical pre-launch unknowns below must be read with this narrower new evidence.

For the risk-accepted first experiment, verified owner-proven FM boot.img restoration is sufficient; an exact current BOOTIMG backup is optional. See [D11 recovery tradeoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md%23recovery-tradeoff&anchor=recovery-tradeoff). All 24 ROM files and SPFT/DA were rehashed in Y2E-150; neither loader was changed. Later full-ROM recovery would require separate authorization and may lose current software/userdata.

Date: 2026-09-08. [Y2E-125](https://github.com/SchulzCode/Y2Linux/issues/6) updates [Y2E-120](https://github.com/SchulzCode/Y2Linux/issues/5). Known-good owner-observed SP Flash Tool recovery/flash exists. M0 remains open because device-specific backups and experiment prerequisites are incomplete. This is an evidence assessment, not an executable flashing procedure.

## Owner-confirmed history: accepted evidence

The owner reports personally successfully flashing this Y2 with SP Flash Tool obtained from [spflashtool.com](https://spflashtool.com/) and the ROM at `/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/`.

Classification: CONFIRMED owner observation, strong evidence of a working tool/package/device combination. This supersedes the earlier assessment that no compatible tested combination or same-device restore evidence existed. We do not need to establish SP Flash Tool's recovery viability from scratch or deliberately repeat a restore to accept this history. The website is the owner's stated download source; its current headline version is not evidence of the previously used version or manufacturer provenance.

The successful operation's date, precise target selection/mode, DA choice, USB entry sequence and recorded post-flash checks are not supplied. Current local hashes identify bytes inspected today, not a retroactively verified historical checksum. This distinction does not diminish the reported successful recovery, but prevents inventing a fully reproducible runbook.

## Exact local tool identification

Found `/home/luca/Downloads/SP_Flash_Tool_v5.2032_Linux/` and its ZIP. Offline ELF inspection resolves `ToolInfo::ToolName()` and `ToolInfo::VersionNum()`: format strings and constants identify MediaTek SP Flash Tool v5.2032.00, detailed version 5.2032.00.sn100, build string `2020/08/11 13:36`. The version is derived from executable code, not merely the folder name. The flasher was not executed.

Its `history.ini` points both `lastDir` and `scatterHistory` to the owner's exact FM scatter. The installed executable matches the archived executable byte for byte. Together these make this build the strongly corroborated previously used local tool, although no operation log proves the exact executable/DA/settings of the successful write.``````

| Artifact | Bytes | SHA-256 |
| --- | --- | --- |
| flash_tool | 11,392,491 | d618e7d08ba5a4020038921a95336a3805a4b2cf17a374fd308cc5299ea7d9d8 |
| SP_Flash_Tool_v5.2032_Linux.zip | 73,238,268 | 83e0367b2f357eacaca8e6dabedba0c09c06236f95a9fa458573b4ad52f024cc |
| Bundled MTK_AllInOne_DA.bin | 16,107,176 | 46cd175d7556e6e80b13f6a70827c6931a5dfa25a09c3cc50e75ba7ff9327618 |

The DA is a hashed bundled candidate, not a confirmed selection during the successful operation. Launcher, libraries and history are additionally hashed in [handoff-artifacts.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/handoff-artifacts.tsv); private `spft-version-disassembly.txt` records the offline version proof. Historical Y1/MT6572 tool-package observations remain in prior history/manifests but are no longer the preferred recovery evidence. Do not use that Y1 scatter on this Y2.

## Exact owner-ROM identity

All 24 top-level regular ROM files were hashed without modification; see [handoff-artifacts.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/handoff-artifacts.tsv). There is no claim that these are full per-device partition backups.````````````

| Input | SHA-256 |
| --- | --- |
| MT6582_Android_scatter.txt (7,666 bytes) | e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e |
| boot.img (5,656,576 bytes) | 5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6 |
| recovery.img (6,041,600 bytes) | 319ae8113b7741c13a0ab6254575c9a0e70336c4290fca49dd33abb4f85f29b0 |
| system.img | 5a7a92f3a95374f31abe8b3ddbd68c5c2ce5677547db3d1cbc21653d24c76989 |
| lk.bin | bb1a93b4c1f02eab09ebad1314a8fdc25d94d3ca99771fc14e21cb18a289964a |
| preloader_eastaeon82_wet_kk.bin | 1df1b62498754aab0c7ddc80a79d310a92fcf81f29b515730c562aaeeb6a884a |

Scatter and LK match OriginalFirmware; preloader/kernel/boot/recovery/system differ. Keep package lineages separate. The FM set is now the owner-proven same-device fallback, replacing the former equal-ranking of untested candidates. Exact current installed build/PCB details still need recording for a precise future operation, not for re-proving the owner's history.

## Remaining safeguards and evidence gaps

| Requirement | Updated assessment |
| --- | --- |
| Working recovery/flash method | Established by owner observation, corroborated by local tool/scatter history. |
| Identifiable compatible package | Owner-proven FM package; current local files/scatter fully hashed. |
| Exact historical tool build | v5.2032.00 / 5.2032.00.sn100 strongly corroborated; operation log absent. |
| Exact DA/mode/targets/connection procedure | Incomplete historical details; record before a future operation. |
| Recovery independent of functioning Android | SPFT history is strong evidence of the MediaTek recovery route; exact emergency entry conditions with damaged BOOTIMG are not separately recorded. No intentional damage test is needed. |
| Same-device boot/recovery and personalized backups | Not established by this research; factory/package images do not substitute. |
| Independent backup copies | Not established. Private research captures on this host are not independent partition backups. |
| Power/capture consistency | Battery reporting conflict and mutable protect/NVRAM consistency strategy remain unresolved. |
| Linux boot experiment | Still gated by memory/observation/installed-loader evidence and backups. |

Preserve NVRAM, calibration, protect/security data and individual radio identity. Preserve preloader/LK and partition tables during ordinary bring-up. No Format All, destructive formatting, automatic repartitioning or preloader write is authorized. A successful historical flash does not make those operations safe or recreate lost personalization. No generic factory file may be treated as a calibration backup.

A later acquisition proposal must pin exact tool/DA, connection behavior, region/offset/length semantics, consistency state, expected output bytes, hashes and abort conditions. A readback feature does not make loading a DA or switching device mode a passive operation. Current non-root block permissions provide no already-approved raw-read route. Retain and verify a second independent backup copy before experimentation.

A future bounded restore runbook should record the owner's proven sequence, exact package/tool selection, target list, USB/host/power prerequisites, timeouts and functional/calibration checks. Exclude preloader/LK, tables, calibration and formatting from ordinary restoration. Execute no restoration in this research session. Existing successful owner recovery satisfies the known-method evidence; a new full-flash rehearsal is not imposed merely to reconfirm it.

## Current M0 gate and next boundary
  -  Stock-family artifacts and owner-confirmed FM fallback hashed; failed generated distributions kept separate.
  -  Non-root baseline and ordinary partition layout reconciled.
  -  Package boot structure and actual LK load/ATAG contract analyzed.
  -  Successful same-device SP Flash Tool recovery/flash accepted and local build corroborated.
  -  Current-device image lineage and exact future recovery procedure/DA recorded sufficiently for the bounded operation.
  -  Same-device boot/recovery/personalized backups verified with independent retention.
  -  Power/capture consistency and safe acquisition procedure established.
  -  Safe initial RAM exclusions, observation channel and installed-loader launch policy resolved.

The next main research proof is the [boot memory envelope](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fboot-chain.md), not another broad investigation of whether SPFT works. Recovery work should fill the concrete remaining backup/runbook gaps using the known-good history. M0 remains open; no Linux boot artifact or implementation issue is ready.

## Y2E-130 boundary

The [fixed initial RAM policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md) permits bounded offline artifact work; it does not pass M0 or change recovery authorization. Owner-confirmed SP Flash Tool recovery remains accepted. Per-device backups/independent retention, exact procedure and trusted power remain incomplete; inherited DMA/secure state, installed-loader/security and observation-channel checks still precede a hardware experiment. No device operation or boot artifact was produced during this research.

## M1 offline boundary

A [validated offline BOOTIMG candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md) now exists under the owner's later implementation authorization. This changes neither the accepted SPFT recovery history nor the open backup/DA/entry/power requirements. M0 remains open. [The conditional experiment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-boot-launch-gates.md) specifies a later BOOTIMG-only target and restore concept; it cannot be executed until the missing operator/backup/console/security evidence is supplied and the bounded operation is separately authorized. No new flash, readback, DA execution, ADB or device operation occurred. Earlier no-artifact statements describe their dated research phase.

## Y2E-145 current-device recovery assessment

Fresh shell uid/group and device-node permissions confirm that mmcblk0, bootimg and uboot are not readable through current ADB access; no raw acquisition was performed. Current BOOTIMG backup and independent copy: absent. Live dumchar still identifies EMMC_USER [0x01d80000,0x02d80000), 16 MiB. Tool/DA hashes were reverified; configured SPFT log directory is absent, and available-scene flags/unchecked historical settings cannot prove the old DA/mode/targets. Owner success remains accepted.

[Prepared BOOTIMG-only acquisition/restore runbook](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fbootimg-recovery-runbook.md) fixes physical addresses, exact bytes, input hashes, repeat-read verification, independent retention and BOOTIMG-only Download Only selection. Exact DA/connection/power and bounded transport/image acceptance remain open; it was not executed. [Launch decision](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md): NO-GO, also due to observation/authentication and the newly identified normal-path watchdog risk. No preloader/LK/table/calibration or other partition operation occurred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
