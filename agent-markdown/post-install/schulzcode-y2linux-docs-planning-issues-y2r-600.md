---
title: "Y2R-600 — M6 recoverable production userspace, updates and security - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2r-600.html"
---

# Y2R-600 — M6 recoverable production userspace, updates and security - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2R-600 — M6 recoverable production userspace, updates and security

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## Platform-first gate — 2026-09-10

The owner now requires M2 core/Buildroot, complete M3 native audio, M4 full power, M5 connectivity, GPU/lima and final whole-platform qualification before Y2PlayerNative begins. This supersedes earlier wording that allowed central application work after a wired-player slice. DEV-02 qualifies the core resources but USB reconnect remains the immediate #27/#28 blocker. This checkpoint grants no new hardware-phase or flash authorization. [Live result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md).

# Y2R-600 — M6 recoverable production userspace, updates and security

## Additional evidence — 2026-09-10

Retain the deterministic rootfs-placement failure: vendor/DA/Linux address spaces differed, leaving an old superblock while overwriting the filesystem body. Separate continuous DA verification reads from region-relative writes; never reuse Tempo's partition offsets or automatic installer. Their frozen-rootfs backup cleanup deadlocked, reinforcing independent cleanup/offline consistency. LK recovery-key/software-entry claims are source evidence, not our installed-loader proof or write authorization. Existing rootfs/application/recovery choices remain authoritative; production implementation stays deferred.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Canonical epic [#32](https://github.com/SchulzCode/Y2Linux/issues/32); [coverage audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

Deferred planning epic; no implementation-ready children added by this audit.

## Goal / why this epic is needed

Connect the diagnostic initramfs to an appliance userspace and eventual safe Android retirement. Current BOOTIMG recovery is not a production update system. Track the platform part of later M18–M20; native application tasks stay in its repo.

## Dependencies / evidence

M0 residual backup/lineage knowledge and owner-proven recovery; core storage, power, logging and native-audio gates. Do not re-prove SPFT viability from scratch. Use `partition-map.md`, `recovery.md`, `first-experiment-result.md` and M1 runtime limits. Production distribution choice follows measured footprint/support.

## High-level coverage

Recoverable development rootfs then production image selection (no premature Debian/Buildroot/Yocto commitment), ARMv7 userspace/toolchain/ABI contract, bounded boot services and non-root app permissions/udev or narrow privileged service. Read-only/mutable partition policy, filesystem/power-loss behavior, storage capacity, service supervision and data migration/backup; no speculative A/B layout.

Complete same-device personalized backup/independent retention and recovery consistency where needed; preserve stock loaders/calibration and known-good fallback. Track signed payloads/integrity, interruption-safe install, rollback and key management/threat model. Update signatures alone do not establish a hardware verified-boot chain behind unchanged LK. Do not bypass security state.

Pin maintained 6.18.y selection/update process, reproducible release manifests, firmware/source/license provenance and notices; retain audit traceability. Define production debug exposure, secret-redacted exports, entropy/identity, RTC versus network-time policy and certificate needs. Shutdown/recovery, service restart and update-failure tests precede release qualification and Android removal.

## Exit evidence / unlocks

A measured minimal image boots reliably, supervises the non-root player against standard Linux interfaces, preserves user/calibration data and can recover/roll back tested interrupted updates under an approved storage model. Security and support limitations are explicit. Provides M6 platform contracts for M7+ and the later M18–M20 release gates; core app development need not wait for full OTA.

## Out-of-scope / stop

No repartitioning, formatting, rootfs install, signing key generation, firmware redistribution decision or updater implementation today. Stop on uncertain write ranges/rollback semantics, inadequate backup/power, provenance or privilege gaps. Do not make a whole-ROM restore the automatic fallback for a BOOTIMG-only trial.

## Execution and validation boundary

High-level planning epic only, not an implementation task or hardware permission. Expand only the next evidence-backed change when this phase is activated; preserve existing stable IDs and link existing issues instead of duplicating them. No speculative driver task list, build, flash or experiment is authorized by this epic.

Before closing the phase or proceeding through its exit gate, repeat the [standing roadmap/gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) using real hardware results. Separate owner reports, retained artifacts, source support and actual device validation. Unknown dependencies stop the relevant path; do not guess hardware or silently broaden scope. Milestone qualification uses the appropriate full verification boundary; small later fixes keep targeted validation and D08/package checks without routine provenance re-audits.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
