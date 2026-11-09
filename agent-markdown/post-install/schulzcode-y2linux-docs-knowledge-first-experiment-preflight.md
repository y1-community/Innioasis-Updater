---
title: "Y2B-240 authorized preflight — 2026-09-08 - Innioasis Updater"
description: "Y2B-240 authorized preflight — 2026-09-08 <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-first-experiment-preflight.html"
---

# Y2B-240 authorized preflight — 2026-09-08 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-240 authorized preflight — 2026-09-08

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-240 authorized preflight — 2026-09-08 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The owner explicitly authorized issue #19 as specified: one diagnostic BOOTIMG-only download, one normal boot observed for no more than 60 seconds, then FM BOOTIMG-only restoration and stock function checks. Authorization is recorded; no further flash permission is requested. The procedure and artifact remain unchanged. This is a preflight checkpoint, not an experiment result.

## Verified host inputs and settings
  - Fresh recovery verifier: all 24 FM files and SPFT executable/bundled DA pass.
  - All 37 candidate bundle entries pass SHA256SUMS verification.
  - Fresh real-artifact/D08/layout/wrapper/partition validation passes; all 11

tests pass, including emitted watchdog instructions and guarded diagnostics.
  - Candidate: `out/m1-risk-accepted-diagnostic/BOOTIMG.img`, 1,089,536 bytes,

SHA-256 `db7d8a5cf082b37f77c8732bd8e1ab742e4205f9383e421b051917f17364ab7e`.
  - FM fallback: 5,656,576 bytes, SHA-256

`5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6`.
  - Original FM scatter SHA-256:

`e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e`.
  - SPFT 5.2032.00 running executable was independently hashed through

`/proc/150273/exe` on the host: SHA-256 `d618e7d08ba5a4020038921a95336a3805a4b2cf17a374fd308cc5299ea7d9d8`.
  - Actual GUI DA is the original bundled `MTK_AllInOne_DA.bin`, SHA-256

`46cd175d7556e6e80b13f6a70827c6931a5dfa25a09c3cc50e75ba7ff9327618`.
  - Actual GUI shows original FM scatter, empty Authentication File,

Download Only, and BOOTIMG alone checked with the exact candidate. The final setup log at 22:41:37 Europe/Berlin confirms the same file/size.
  - All 20 normal partition entries in the retained BROM host setup log were

reviewed: only BOOTIMG enabled. PRELOADER, MBR, EBR1/2, PRO_INFO, NVRAM, PROTECT_F/S, SECCFG, UBOOT/LK, RECOVERY, SEC_RO, MISC, LOGO, EXPDB, ANDROID, CACHE, USRDATA and FAT are disabled. Scatter BMTPOOL is reserved and `is_download: false`; it is not a selected target.
  - GUI shows logical image interval `0x03180000..0x03289fff` inclusive.

This does not change the audited physical BOOTIMG partition interval `EMMC_USER [0x01d80000,0x02d80000)`. No raw-address write is proposed.
  - Existing setup reports USB high speed/auto-detect and DA checksum level 0.

These are recorded existing settings; no verification/security option was changed. Host SHA-256 validation is not a device readback verification.

An intermediate GUI view selected the older `out/m1-first-boot/BOOTIMG.img`. That mismatch was caught before Download and the subsequent GUI/log capture confirms the authorized diagnostic path. Initial saved selections included other ROM files; they are not the verified final selection. Setup-only desktop interaction was stopped when concurrent window/selection changes were detected.

## Execution remains pending

No Download control has been activated by this session. The retained tool snapshot contains setup activity, not a device flash result, and the GUI shows 0 Bytes / 0:00. Kernel diagnostics, PID1, heartbeats, resets/freeze, restoration and stock functional results are not observed / not performed.

After host verification, read-only `adb devices -l` returned an empty device list. Current target identity, cable/port, adequate charge, the owner's proven power/USB sequence and a ready physical screen observer still need recording. The desktop can be inspected, but there is no physical Y2 camera/UART feed; the Linux candidate has no ADB. An unanswered readiness question is not an observation channel or a power/recovery procedure.

Next step is physical coordination for the already-authorized experiment, followed by rechecking actual tool settings immediately before Download. Do not rebuild, substitute a candidate, retry, or expand to M2/full-ROM writes. Issue #19 remains open until trial and restoration evidence is recorded.

Private raw evidence: `evidence-private/20260908-y2b240-preflight/`; file hashes are retained in `capture-index.tsv`. Screenshots are desktop SPFT configuration evidence, not photographs of Linux output on the Y2.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
