---
title: "Y2E-115 — Inspect stock boot structure and config/device-tree availability offline - Innioasis Updater"
description: "Y2E-115 — Inspect stock boot structure and config/device-tree availability offline <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dat"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-115.html"
---

# Y2E-115 — Inspect stock boot structure and config/device-tree availability offline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-115 — Inspect stock boot structure and config/device-tree availability offline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-115 — Inspect stock boot structure and config/device-tree availability offline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Canonical platform research task. Transferred from SchulzCode/Y2PlayerNative#4; the original URL redirects here and preserves history. This task belongs to the research/architecture workstream, not an implementation handoff. The research owner performs and reviews the evidence, then advances only satisfied prerequisites. No `state:luna-ready` label applies.

## Goal

Document the exact local stock boot image's structure and what kernel/config/DT evidence is actually available.

## Why

Missing runtime DT/config exports do not establish that the image lacks those structures. The stock kernel may also use legacy board files or ATAGs.

## Dependencies
  - Y2E-101: [https://github.com/SchulzCode/Y2Linux/issues/1](https://github.com/SchulzCode/Y2Linux/issues/1) (evidence review required)
  - Y2E-110: [https://github.com/SchulzCode/Y2Linux/issues/3](https://github.com/SchulzCode/Y2Linux/issues/3) (evidence review required)

Y2E-101 and Y2E-110 reviewed, with an identified immutable package boot input. This can finish with clearly recorded negative extraction results; it cannot certify compatibility with the current device by itself.

## Evidence / Assumptions

Cataloged boot SHA-256: `8131020fafddb864d252b13f6bc7e83584487bd182d371d7e51f6244e2412f02`. Existing reference `tools/adb/build_adb_boot.py` describes Android v0 headers and a 512-byte MTK ROOTFS wrapper; it is a builder, not a safe general-purpose extraction command. `OriginalFirmware/kernel`, `ramdisk.img` and `reverse/ramdisk/` are candidate derivatives requiring lineage checks.

## Scope

Offline header/layout and available config/DT evidence only; reuse existing host inspection tools.

## Out of Scope

No builder entrypoint, repacking, adbd compilation, kernel builds, DTS edits, driver reconstruction, bootloader patching, device access or new reusable tooling.

## Expected Files / Components

`docs/knowledge/stock-boot-structure.md`; private extraction listings, offsets, hash records and any disposable derived files.

## Instructions
  - Verify original hashes. Inspect a disposable host copy with available read-only tools; record tool versions. Start with `file <boot-copy>` and `xxd -l 2048 <boot-copy>`. Read the existing parser source for layout reference without invoking its build flow.
  - Record magic/header interpretation, page alignment, kernel/ramdisk/second-stage sizes and offsets, load/tag addresses, command-line bytes and any trailing content. Verify all bounds against file length and the package's partition size. A blank header command line is not evidence that the bootloader supplies none.
  - Compare extracted component hashes against cataloged loose kernel/ramdisk files if an existing trusted extractor handles this format. Record MTK wrapper and compression boundaries before decompression. Use list-only cpio inspection or extraction that rejects absolute paths, parent traversal and escaping symlinks; never run extracted files or init scripts.
  - Inspect any already recovered kernel image/symbol records for version and CONFIG/DT signatures; use an existing extract-ikconfig tool if available and record its source/version and exact command. Missing tools are a reported blocker, not permission to install or build a new analysis system.
  - For candidate DTBs in the kernel/trailing data, require valid header, totalsize within source bounds and successful existing `dtc -I dtb -O dts` parsing into a private analysis artifact before calling one valid. Decompilation is evidence extraction, not authored DTS. If tooling or a candidate is absent, document the bounded search locations/method and UNKNOWN outcome. Do not infer no DTB from string search alone.
  - Inspect matched ramdisk init/fstab/default properties for mount, console, module and firmware-loader references. Record possible bootloader-provided ATAGs/board-file use as unresolved where unsupported. Stop after structure and availability; no board pinout reconstruction.

## Acceptance Criteria
  -  Header/component layout is bounds-checked with original/component hashes.
  -  Loose derivatives are linked to the exact image or explicitly unverified.
  -  Config and DT each have extracted-and-validated, not-found-in-stated-search, or unavailable-tool/access outcomes.
  -  Negative results do not become invented DTS facts; runtime and boot-header command lines remain distinct.
  -  Original inputs remain unchanged and no firmware artifact intended for booting is produced.

## Validation

Compare `sha256sum` of original inputs before/after; preserve exact extraction/listing commands. Use `gzip -t` only on an identified extracted gzip payload and `dtc` only for a bounded DTB candidate. Record missing tools explicitly. Verify artifact hashes and `git diff --check`. Do not run any build script as a validation shortcut.

## Expected Artifact

One offline boot-layout report with reproducible evidence locators and a precise list of missing stock-kernel evidence.

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

Evidence review may unlock Y2E-120 research.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
