---
title: "Y2E-110 — Reconcile stock scatter and runtime partition metadata - Innioasis Updater"
description: "Y2E-110 — Reconcile stock scatter and runtime partition metadata <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate iden"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-110.html"
---

# Y2E-110 — Reconcile stock scatter and runtime partition metadata - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-110 — Reconcile stock scatter and runtime partition metadata

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-110 — Reconcile stock scatter and runtime partition metadata > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Canonical platform research task. Transferred from SchulzCode/Y2PlayerNative#3; the original URL redirects here and preserves history. This task belongs to the research/architecture workstream, not an implementation handoff. The research owner performs and reviews the evidence, then advances only satisfied prerequisites. No `state:luna-ready` label applies.

## Goal

Produce a partition map that explicitly reconciles package address conventions with the current device's readable metadata.

## Why

The stock scatter distinguishes linear and physical addresses and eMMC regions. Guessing a block node or offset would invalidate backups and risk later writes.

## Dependencies
  - Y2E-101: [https://github.com/SchulzCode/Y2Linux/issues/1](https://github.com/SchulzCode/Y2Linux/issues/1) (evidence review required)
  - Y2E-105: [https://github.com/SchulzCode/Y2Linux/issues/2](https://github.com/SchulzCode/Y2Linux/issues/2) (evidence review required)

Y2E-101 and Y2E-105 reviewed; authorized non-root target unchanged. Unavailable runtime metadata must remain a blocker, not be replaced by package guesses.

## Evidence / Assumptions

`OriginalFirmware/MT6582_Android_scatter.txt` SHA-256: `e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e`. In this package BOOTIMG is linear `0x3180000`, physical `0x1d80000`, size `0x1000000`; PRELOADER is EMMC_BOOT_1. These values are reference observations, not approved read/write coordinates. `reverse/ramdisk/fstab` uses vendor /emmc@ aliases and protect partitions.

## Scope

Map metadata only, including calibration candidates and unresolved address translation.

## Out of Scope

No dd/cat of block-device contents, block ioctls, mounting, unmounting, filesystem repair, scatter editing, PMT repair, readback or flashing.

## Expected Files / Components

`docs/knowledge/partition-map.md`, `docs/knowledge/partition-map.tsv`; private raw metadata capture.

## Instructions
  - Read the exact cataloged scatter as text and reference ramdisk fstab/init mount lines. Include every scatter entry, even non-download, zero-size or sentinel entries.
  - With Y2E-105 capture rules, run separately: `cat /proc/partitions`, `cat /proc/dumchar_info`, `cat /proc/emmc`, `cat /proc/mounts`, `ls -l /dev/block`, `ls -l /dev/block/platform`, `ls -l /sys/class/block`, `ls -l /emmc@*`. Failure is valid evidence. Follow only the observed platform directories to inspect their by-name symlink listings; no recursive device opens.
  - For each observed mmc block/partition name, read only corresponding `/sys/class/block/<name>/dev`, `start`, `size`, and `uevent` if present. Record permissions and missing files. Treat sysfs block counts as 512-byte sectors; retain raw counts and annotate converted bytes, independently cross-checking another source. Do not equate these with physical-block-size values.
  - Table columns: region, scatter name, runtime alias/node and major:minor, linear offset, region-relative physical offset, runtime start/count with units, normalized byte range, package file/hash/type, download flag, mount/use, possible personalized data, confidence/evidence.
  - Explicitly discuss MBR/EBR layout versus runtime numbering, eMMC boot hardware regions versus EMMC_USER and SD, the scatter linear/physical offset difference, and FAT/BMTPOOL variable/sentinel semantics. Check normal fixed ranges for overlap and region bounds. Leave unresolved entries UNKNOWN.
  - List NVRAM, PRO_INFO, PROTECT_F, PROTECT_S, SECCFG, MISC and any newly observed calibration partitions as candidates for later assessment. Do not assume all contain calibration or that a package's SEC_RO replaces device-specific data.

## Acceptance Criteria
  -  Every scatter entry is accounted for; address domains and units remain distinct.
  -  Runtime mappings have direct evidence or explicit missing/conflicting evidence.
  -  Normal ranges are independently cross-checked; unresolved/sentinel entries are not assigned guessed readback ranges.
  -  Packaged images are distinguished from full partition lengths and personalized partitions with no supplied image.
  -  Report concludes whether precise backup coordinates can yet be approved; it contains no executable readback/flash recipe.

## Validation

Verify scatter checksum before/after. Cross-check at least BOOTIMG and RECOVERY against two independent available metadata sources; if impossible, record that validation as blocked. Show hex/decimal/sector arithmetic in the report. Verify raw capture checksums, `git diff --check`, and staged paths.

## Expected Artifact

A reconciled-or-explicitly-blocked partition table and a short list of mapping questions requiring review.

## Execution contract

Y2Linux is the canonical home for all platform research, evidence, recovery and Linux bring-up. Y2PlayerNative is reserved for the later Rust/C application. Preserve stable Y2E IDs. Do one task only; no application/kernel implementation, DTS changes, builds, flashing, reboot, boot-mode transitions, installs, adb root/su, remount, property/settings writes, radio toggles, log clearing, register access, guessed ioctls, bus probes, raw partition reads or writes. Read-only shell inspection is allowed only where explicitly listed.

Use the existing Git author/committer configuration and authenticated GitHub user. Verify with `git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT` before committing; stop if identity is missing or wrong. Never change identity or add model attribution.

Store raw files under ignored `evidence-private/<capture-id>/`; commit only reviewed/redacted reports and manifests. Use host UTC time; record device clock separately if available. For every observation record exact command/tool version, capture ID, source/build lineage, local exit status, remote exit status where obtainable, stdout/stderr, size, SHA-256, and outcome COLLECTED/EMPTY/DENIED/UNAVAILABLE/FAILED. Facts use CONFIRMED/INFERRED/UNKNOWN/DISPROVEN with evidence locator, date and task ID. Inspect error text: archived ADB commands returned host exit 0 with remote denial. Do not publish firmware, calibration, serial/MAC identifiers, credentials, pairing data or personal media.

## Stop Conditions

Stop the affected activity and report if identity is missing/wrong, inputs fail integrity checks, device identity differs unexpectedly, the target is ambiguous/offline/unauthorized, a command would mutate device state, or scope requires new tooling/privileges/architectural decisions. Record a bounded denial/missing resource and continue only other explicitly independent observations; never bypass it.

## Risk

Low: host documentation/offline analysis and explicitly bounded non-root observations only.

## Recovery

No device mutation is allowed. Missing access is evidence; it does not authorize a privilege or boot change.

## Completion Report

Report files changed, exact commands and tool versions, validation results, artifact manifest/hashes, provenance/limitations, unexpected findings, unresolved blockers and one suggested next step. Do not implement the suggestion. The research owner must review the evidence before advancing a dependent research task; closing this issue does not pass M0.

## Unlocks

Evidence review may unlock Y2E-115 research.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
