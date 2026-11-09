---
title: "Y2E-120 — Assess recovery capability and propose the next safe acquisition boundary - Innioasis Updater"
description: "Y2E-120 — Assess recovery capability and propose the next safe acquisition boundary <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The da"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-120.html"
---

# Y2E-120 — Assess recovery capability and propose the next safe acquisition boundary - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-120 — Assess recovery capability and propose the next safe acquisition boundary

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-120 — Assess recovery capability and propose the next safe acquisition boundary > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Canonical platform research task. Transferred from SchulzCode/Y2PlayerNative#5; the original URL redirects here and preserves history. This task belongs to the research/architecture workstream, not an implementation handoff. The research owner performs and reviews the evidence, then advances only satisfied prerequisites. No `state:luna-ready` label applies.

## Goal

Produce a reviewable recovery capability/gap packet that determines the next small evidence wave.

## Why

A stock firmware package and a successful firmware build do not prove the unit can recover from a failed kernel experiment.

## Dependencies
  - Y2E-101: [https://github.com/SchulzCode/Y2Linux/issues/1](https://github.com/SchulzCode/Y2Linux/issues/1) (evidence review required)
  - Y2E-105: [https://github.com/SchulzCode/Y2Linux/issues/2](https://github.com/SchulzCode/Y2Linux/issues/2) (evidence review required)
  - Y2E-110: [https://github.com/SchulzCode/Y2Linux/issues/3](https://github.com/SchulzCode/Y2Linux/issues/3) (evidence review required)
  - Y2E-115: [https://github.com/SchulzCode/Y2Linux/issues/4](https://github.com/SchulzCode/Y2Linux/issues/4) (evidence review required)

Y2E-101, Y2E-105, Y2E-110 and Y2E-115 reviewed. Unresolved findings carry forward as explicit blockers, never implicit permission.

## Evidence / Assumptions

Historical starting point: the package has boot/recovery/system/LK/preloader/scatter files, but NVRAM and several protect/config entries have no supplied image. At Y2E-120 intake, same-device restoration and tool compatibility were unknown. Superseded by [Y2E-125](https://github.com/SchulzCode/Y2Linux/issues/6): the owner confirms successful SPFT flashing of this Y2 with the FM ROM; local v5.2032.00 and scatter history corroborate it. See [current recovery knowledge](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md). The original task specification below is retained as history, not a requirement to re-prove recovery from scratch.

## Scope

Host-only recovery capability audit and a proposed acquisition sequence, with explicit preconditions for future operator work.

## Out of Scope

No new issues beyond this packet, tool installation, tool-device connection, preloader/BROM transitions, download-agent upload, rooting/exploits, flashing, raw reads, recovery rehearsal, partition formatting or M1 planning.

## Expected Files / Components

`docs/recovery/capability-and-gaps.md`, `docs/recovery/m0-gate-checklist.md`.

## Instructions
  - Build a matrix for vendor package, current-device boot/recovery, calibration/NVRAM/protect data, independent backup copy, compatible scatter/DA/tool/host, USB normal/recovery/preloader/BROM reachability, restore runbook and actual restore proof. Give each proven/unproven/blocked state an artifact locator.
  - Inspect existing local flashing tool metadata/version files, manifests and historical restore records only. Missing tooling or records are UNKNOWN. Do not run a flasher or introduce a guessed SP Flash Tool/mtkclient version, DA or command. Vendor-package availability does not prove board compatibility.
  - Identify which exact per-device objects need backup and whether current non-root access can acquire them. Use the reviewed map; do not print executable raw read commands until all ranges/regions are verified. Distinguish partition image bytes from full partition contents and stable boot data from mutable calibration data.
  - Specify backup verification requirements: source device/region/offset/length, exact command/tool and status, host bytes/hash, repeat-read or independent verification where appropriate, a second independently retained copy, and treatment of mutable data consistency. Factory defaults do not replace personalized NVRAM.
  - Draft preconditions for a later bounded operator recovery procedure: healthy device/power/cable, exact restore inputs and expected hashes, correct host/tool/DA, explicit allowed targets, expected enumeration/timeouts, abort conditions, readback and normal boot/peripheral/calibration checks. Unknown fields remain visibly UNRESOLVED. Protect preloader/LK/partition tables/calibration from ordinary writes; never select format or whole-device download.
  - Explain how recovery independent of working Android must eventually be demonstrated without deliberately corrupting the unit. A stock restore rehearsal needs backups and separate explicit authorization before execution; it does not require M0 to have already passed.
  - Return at most three prioritized next proofs and a passive-subsystem coverage gap table for audio/FM, panel/input, power, Wi-Fi/Bluetooth/firmware and storage/USB. Each next proof states what evidence would make it ready. Do not create those issues or solve those subsystems.
  - Set the gate to NOT PASSED unless actual same-device proof satisfies every M0 criterion; this first batch has no restore authorization and is expected to leave the gate closed.

## Acceptance Criteria
  -  Package availability, per-device backups and demonstrated restoration are separate states.
  -  Exact blockers for safe readback and later restoration are visible, including tool/DA/region and device revision uncertainty.
  -  Verification includes backup completeness/consistency, independent retention and restore readback, not hashes alone.
  -  A bounded future procedure is concrete where evidenced and explicitly incomplete where unknown; no invented commands fill gaps.
  -  At most three next proofs and a subsystem evidence-gap table are returned for architectural review.
  -  Experimental kernel work remains blocked; no claim of M0 PASS from documentation alone.

## Validation

Trace every asserted capability to a source from the four predecessor reports; check that each required recovery object has a state and each proposed operation has prerequisites/stop conditions. Recheck cited local hashes with `sha256sum <file>` where needed, then `git diff --check` and inspect staged text. No device validation is part of this task.

## Expected Artifact

A recovery decision packet and explicitly unresolved M0 gate checklist ready for review.

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

Architectural review of the first evidence boundary only. No automatic M1 or flash authorization.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
