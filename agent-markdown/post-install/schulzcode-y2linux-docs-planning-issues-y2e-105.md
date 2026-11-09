---
title: "Y2E-105 — Capture the current non-root ADB system and access baseline - Innioasis Updater"
description: "Y2E-105 — Capture the current non-root ADB system and access baseline <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-105.html"
---

# Y2E-105 — Capture the current non-root ADB system and access baseline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-105 — Capture the current non-root ADB system and access baseline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-105 — Capture the current non-root ADB system and access baseline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Canonical platform research task. Transferred from SchulzCode/Y2PlayerNative#2; the original URL redirects here and preserves history. This task belongs to the research/architecture workstream, not an implementation handoff. The research owner performs and reviews the evidence, then advances only satisfied prerequisites. No `state:luna-ready` label applies.

## Goal

Capture the current device's identity, stock-family system evidence and access limitations in one bounded non-root session.

## Why

Historical captures came from a secure-ADB boot image and cannot establish today's installed boot/system state.

## Dependencies
  - Y2E-101: [https://github.com/SchulzCode/Y2Linux/issues/1](https://github.com/SchulzCode/Y2Linux/issues/1) (evidence review required)

Y2E-101 evidence reviewed. Its private-evidence convention and artifact catalog must exist. One already connected, authorized target is required; if absent, report the blocked capture without changing device configuration.

## Evidence / Assumptions

Archived records identify MT6582/ARMv7 and Linux 3.4.67, but current build/revision and modifications are UNKNOWN. Older captures show denied dmesg/cmdline with host exit 0, absent config.gz/DT exports, and missing uname. Do not assume BusyBox, root, modern toybox or working Android command exit propagation.

## Scope

One passive host/system inventory, with no interactive subsystem tests.

## Out of Scope

No partition contents, deep sysfs walks, radio changes, input generation, playback changes, permission workarounds or collector framework.

## Expected Files / Components

`docs/knowledge/stock-system-baseline.md`; ignored per-command output and capture manifest under `evidence-private/<capture-id>/`.

## Instructions
  - Record host `date -u`, `uname -a`, `adb version`, `command -v adb`, `lsusb` if available, and `adb devices -l`. Use the chosen private serial explicitly for every later command. Stop for zero/multiple ambiguous/unauthorized/offline targets.
  - Capture each remote command separately with a host `timeout 15s adb -s "$Y2_SERIAL" shell '<command>'`. Record the remote exit with a shell-status marker if supported; keep local status separately. Capture `id`, `date`, `getprop`, `uname -a`, `cat /proc/version`, `cat /proc/cpuinfo`, `cat /proc/meminfo`, `cat /proc/cmdline`, `cat /proc/interrupts`, `cat /proc/iomem`, `cat /proc/modules`, `getenforce`, `dmesg`, `cat /proc/mounts`, and `dumpsys battery`. Missing/denied commands are recorded once, not retried with privileges.
  - List metadata only: `ls -ld /proc/config.gz /proc/device-tree /sys/firmware/devicetree/base`, `ls -l /system/lib/modules /vendor/lib/modules /system/etc/firmware /vendor/firmware`. Record CPU possible/present/online from their explicit files if readable. Do not recursively read firmware or sysfs.
  - Record USB properties from getprop and shell uid/groups/SELinux. Compare the selected build identity to cataloged stock/modified provenance. A matching fingerprint alone does not establish stock boot or stock HAL. Use owner-provided installation history if available, otherwise UNKNOWN; do not flash to make the unit stock.
  - Produce a compact access matrix and present-day versus historical differences. Preserve full raw getprop privately; publish only relevant redacted values.

## Acceptance Criteria
  -  One target and current session are traceable privately; host/kernel/build/privilege facts have raw evidence.
  -  Every requested command has collected/empty/denied/unavailable/failed outcome, including error text and independent status handling.
  -  Device time is not silently used as trustworthy UTC; no inaccessible resource is inferred absent.
  -  Installed boot/system lineage is explicitly confirmed or unknown, never inferred from a fingerprint alone.
  -  Capture hashes validate and the sanitized report identifies prerequisites still blocking readback.

## Validation

Re-read outputs for `Permission denied`, `Operation not permitted`, `not found`, timeout and empty data even when ADB returns 0. Verify the raw capture manifest with `sha256sum -c SHA256SUMS` from its directory; verify `git check-ignore evidence-private/probe` and `git diff --check`. No repeat capture is required solely to make a denial disappear.

## Expected Artifact

One timestamped passive capture, checksums and a system/access report suitable for partition-map planning.

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

Evidence review may unlock Y2E-110 research.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
