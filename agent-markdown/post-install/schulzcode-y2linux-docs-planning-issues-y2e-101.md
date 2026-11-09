---
title: "Y2E-101 — Inventory existing stock artifacts and establish evidence provenance - Innioasis Updater"
description: "Y2E-101 — Inventory existing stock artifacts and establish evidence provenance <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-101.html"
---

# Y2E-101 — Inventory existing stock artifacts and establish evidence provenance - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-101 — Inventory existing stock artifacts and establish evidence provenance

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-101 — Inventory existing stock artifacts and establish evidence provenance > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Canonical platform research task. Transferred from SchulzCode/Y2PlayerNative#1; the original URL redirects here and preserves history. This task belongs to the research/architecture workstream, not an implementation handoff. The research owner performs and reviews the evidence, then advances only satisfied prerequisites. No `state:luna-ready` label applies.

## Goal

Produce one auditable catalog of the existing stock/research artifacts so later tasks know which inputs they may trust.

## Why

The reference repository mixes vendor-package inputs, extracted stock binaries, modified firmware and historical captures. A package copy is not a per-device backup.

## Dependencies

None. This is the first research task.

## Evidence / Assumptions

Android reference: `/home/luca/Dokumente/Code/Y2Player`, inspected at `870f2b33e49129990bc0a98eeb34d58ed42542b6`. Ignored artifacts are not covered by that commit. Existing `OriginalFirmware/boot.img` SHA-256 is `8131020fafddb864d252b13f6bc7e83584487bd182d371d7e51f6244e2412f02`; recovery is `1c14b5316bfc0542b4b3b3c6c75208ff6da99e7302ef7c397aaa77e33cc6292c`. These are observed local hashes, not authenticity or restoration guarantees.

## Scope

Host-only artifact identity and provenance, historical capture integrity, and a short superseded/missing-source index.

## Out of Scope

No device access, full reverse engineering, archive-wide copying, firmware building, recovery execution or source port.

## Expected Files / Components

`docs/knowledge/evidence-index.md`, `docs/knowledge/artifact-manifest.tsv`, `.gitignore` entry for `/evidence-private/`; raw verification output under that ignored directory. Preserve the supplied untracked blueprint.

## Instructions
  - Record repository revision/status without altering the Android checkout. Add the private-evidence ignore rule before storing raw records.
  - Catalog all top-level regular files in `OriginalFirmware/` with byte size/hash and original path. Record package origin/date/revision as UNKNOWN if no source record exists. Classify bundled images as package inputs, never current-device dumps.
  - Verify the existing `checksums.txt` in the two snapshot directories `out/hardware-snapshots/2026-07-29_004316/` and `2026-07-29_004935/`. Record missing/extra members, including supplemental source media, without copying media. Inspect manifest outcome/error records, not just hashes.
  - Catalog the manifest/index files of `out/afe-runtime/2026-07-30_135519/`; the exact analyzed HAL and kernel ELF when available under `reverse/`; and manifests/checksums of `out/boot-adb/` and `out/firmware/` when available. Limit this to identifiable evidence inputs and manifests, not every build output. Mark absent paths explicitly.
  - Index `docs/Y2_HARDWARE_AND_DAC_ANALYSIS.md`, the audio phase-2/3/4 reports, `docs/BLUETOOTH_STACK_INVESTIGATION.md`, `docs/FM_RADIO_FEASIBILITY.md`, `RELEASE_2.5.md` and `docs/ADB_BOOT_IMAGE.md`. Record known conflicts: fixed versus dynamic audio route claims, old no-Bluetooth-runtime claim, FM chip/revision claims, missing PowerShell collector, stale README/input behavior. Do not settle hardware disputes in this task.
  - Reuse the exact-source metadata where present; distinguish raw capture, static inference, derived binary and generated firmware. Hash existing files without editing them.

## Acceptance Criteria
  -  Every top-level stock input has size, SHA-256, class, locator and origin/unknown field.
  -  Both snapshot verification outcomes are recorded, including failures and unmanifested supplemental files.
  -  Modified and stock inputs are unmistakably separated; no item is called a same-device recovery backup without evidence.
  -  Missing artifacts/tools and superseded reports are listed; errors are not represented as successful hardware observations.
  -  Raw/private evidence is ignored; only sanitized text is staged.

## Validation

From each snapshot directory run `sha256sum -c checksums.txt` and preserve the output/status. Use `stat -c '%s %n' <file>` and `sha256sum <file>` for manifest entries. If Windows path syntax prevents native manifest verification, record the failure and normalize only a disposable copy; preserve the original. Run `git check-ignore evidence-private/probe`, `git diff --check`, `git diff --cached --name-only`, and inspect staged text for private material.

## Expected Artifact

A small provenance catalog and two recorded snapshot integrity results, with an explicit list of inputs that remain untrusted.

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

Evidence review may unlock Y2E-105 research.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
