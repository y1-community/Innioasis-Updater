---
title: "Y2B-240 — One risk-accepted BOOTIMG-only diagnostic experiment - Innioasis Updater"
description: "Y2B-240 — One risk-accepted BOOTIMG-only diagnostic experiment <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-240.html"
---

# Y2B-240 — One risk-accepted BOOTIMG-only diagnostic experiment - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-240 — One risk-accepted BOOTIMG-only diagnostic experiment

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-240 — One risk-accepted BOOTIMG-only diagnostic experiment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

**Experiment concluded on 2026-09-08: owner-observed green PID1 stage, successful BOOTIMG-only Android recovery. Timed heartbeats and 60-second cutoff were not verified; actual restore image differed from the planned FM fallback. See the recorded result; no further experiment is authorized.** The experiment uses [D11–D13](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md), not the superseded Y2E-145 hard gates. Candidate BOOTIMG SHA-256: `db7d8a5cf082b37f77c8732bd8e1ab742e4205f9383e421b051917f17364ab7e`, 1,089,536 bytes. Build source `1234f857810f979bae821649c3202c2a9f132e0a`. Two clean builds match; all 11 tests pass. [Offline result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fbuild%2Frisk-diagnostic-result.md).

## Inputs and recovery already on this host
  - Candidate: `/home/luca/Dokumente/Code/Y2Linux/out/m1-risk-accepted-diagnostic/BOOTIMG.img`.
  - Fallback: `/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/boot.img`,

5,656,576 bytes, SHA-256 `5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6`.
  - Original scatter in that FM directory: `MT6582_Android_scatter.txt`, SHA-256

`e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e`.
  - Owner-proven tool: `/home/luca/Downloads/SP_Flash_Tool_v5.2032_Linux/`,

executable `flash_tool` version 5.2032.00, SHA-256 `d618e7d08ba5a4020038921a95336a3805a4b2cf17a374fd308cc5299ea7d9d8`.
  - Bundled `MTK_AllInOne_DA.bin`, SHA-256

`46cd175d7556e6e80b13f6a70827c6931a5dfa25a09c3cc50e75ba7ff9327618`. The exact historical DA selection is unrecorded. Use the owner's working setup and retain the actual selected DA hash for this operation; no patched DA, substitute auth file or security-state adjustment.
  - Local fallback boot/scatter convenience copies are also retained alongside

the candidate under `recovery/`; they are not independent backup storage.

Before execution rerun `python3 tools/observation/verify_recovery.py` and verify bundle `SHA256SUMS`. Any mismatch stops the procedure. Current installed BOOTIMG is not backed up; the owner accepts returning to FM boot state. The owner's successful same-device SPFT restore supplies the recovery evidence; no destructive rehearsal is needed.

## Exact bounded operation after authorization
  - Record the authorization, candidate hash, target Y2 identity, date, tool/DA,

selected USB cable/port and the owner's proven power/connection sequence. Ensure the owner can observe the screen and perform that recovery sequence. No UART adapter is required for this experiment. Start with adequate charge using the owner's ordinary indication; contradictory ADB battery records are not an independent battery measurement.
  - Open the owner's working SPFT v5.2032 setup. Load the **original verified FM

scatter, choose Download Only, deselect every row**, select only BOOTIMG, and set that row's file to the exact candidate above. Keep all other locations/selection flags untouched and unselected. Review/record the final target list before starting; do not rely on saved checkbox indices.
  - Allowed target: BOOTIMG, EMMC_USER [0x01d80000,0x02d80000) (16 MiB).

Let the verified scatter/tool resolve its addressing; do not substitute the logical 0x03180000 as a raw physical offset. No Write Memory, Readback-based write, Format All, Firmware Upgrade or automatic partition-table change. PRELOADER, UBOOT/LK, MBR/EBRs, NVRAM, PROTECT, SECCFG, SEC_RO, RECOVERY, ANDROID/system, USRDATA and every other partition stay unselected.
  - Perform one Download Only operation with the owner's proven attachment/power

sequence. Retain the operation log. Abort on identity mismatch, authentication rejection, checksum failure, format/upgrade request, unexpected selected target or transport error. Do not disable verification or improvise a mode. A green SPFT result is transport evidence, not proof of Linux execution. Readback verification is useful if the supported workflow provides it, but is not a new absolute exact-backup gate under D11.
  - Perform one normal stock-LK boot, recording start time and visible

transitions. Observe for at most 60 wall-clock seconds from power-on. No ADB connection is expected from Linux: it has no USB gadget/adbd. There are no shell commands or peripheral tests to run on the candidate.
  - Desired sequence: normal LK logo → black/white vertical stripes (kernel

initcall) → solid green (PID1, after about two seconds) → white half moving left/right on green every five seconds → checkerboard after ten heartbeat intervals. Kernel/loader startup and console output add latency: these are not exact times from power-on. The 60-second host cutoff takes precedence. Stage timing depends on actual timer operation. UART0, if later connected safely, additionally emits `Y2DIAG` progress and error lines.
  - Success evidence is the ordered PID1/heartbeat sequence, with at least three

timed changes. The terminal checker is stronger completion evidence. A stock logo, kernel stripes alone, static green, USB disconnect, backlight alone or reset alone is not successful first-boot evidence. On silence, unexpected colors/sequence, freeze or reset, stop at the cutoff and record exactly the last observation. No retry, RAM expansion or loader modification.
  - End the trial using the owner's known power/recovery sequence. Restore

BOOTIMG only through the same verified scatter and Download Only selection, this time pointing the BOOTIMG row to the exact fallback FM `boot.img`. Record the selected rows, fallback hash and successful operation. Boot stock Android and check the owner's normal UI/storage/audio behavior. If FM boot alone cannot restore stock operation, stop: full-ROM recovery is a separate decision/authorization, never an automatic escalation of this test.

## Failure behavior and accepted uncertainty

The entry code disables AP_RGU and does not rearm it. Once this works, a later hang may remain frozen; there is no guaranteed automatic reset, automatic rollback, Linux power-button handler or safe programmed power-off. PID1 stops its visual sequence after ten intervals and sleeps indefinitely. Manual termination/recovery is part of the experiment. Before kernel entry or if the watchdog write cannot take effect, the inherited nominal 10-second IRQ/dual-mode interval, rejection/halt or repeated stock-loader reset may occur; no exact reset timing is promised. Do not allow unattended repeated attempts.

Accepted risks include unsigned-image rejection, mismatch between installed and analyzed loaders, absence of exact installed boot state, incomplete DMA/secure/shared-state knowledge, and unmeasured watchdog/display behavior. The visual guard fails closed on incompatible register state, so that failure can still be silent without UART. A working guarded pixel path is supported by firmware/source evidence, not yet demonstrated on this board under Linux. Restoring FM boot loses current custom kernel/ramdisk changes; separately required full-ROM restoration could lose current system/userdata. Generic ROM files do not recreate unique calibration. None of these tradeoffs authorizes writes to loaders, partition tables or calibration regions in this experiment.

Close this issue only after the authorized operation, observations and stock restoration results are retained and interpreted. M1 hardware completion is not implied by offline GO.

Depends on completed Y2E-150 #18 / D08 / offline M1. The old Y2E-145 #17 absolute gates are superseded by D11; physical UART work in #16 remains deferred.

Execution acceptance:
  -  Separate explicit owner authorization recorded (2026-09-08).
  -  Tool/DA/scatter/candidate/fallback hashes and BOOTIMG-only target list recorded; actual owner-selected restore image is separately hashed in the result.
  -  One launch observed for at most 60 seconds; actual stages/timing/failure recorded.
  -  BOOTIMG-only stock restore performed and result recorded, or any restore failure escalated without automatically changing scope.
  -  Evidence interpreted and next smallest diagnostic step proposed; no implementation or new trial started.

Status: experiment concluded with partial diagnostic evidence and documented deviations. Android works after owner-operated BOOTIMG-only restoration. M1 heartbeat validation remains unproven.

Result: [first-experiment-result.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fknowledge%2Ffirst-experiment-result.md) Unchecked original acceptance items represent unverified procedure details, not authorization to repeat the trial.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
