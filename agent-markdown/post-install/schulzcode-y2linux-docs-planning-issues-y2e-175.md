---
title: "Y2E-175 — Specify a read-only removable-SD controller proof - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-175.html"
---

# Y2E-175 — Specify a read-only removable-SD controller proof - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-175 — Specify a read-only removable-SD controller proof

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## DEV-02 live hardware checkpoint — 2026-09-10

SATISFIED narrow research/bring-up scope on physical DEV-02; remaining production/full-platform concerns belong to #29–32.

[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) retains baseline, completed 256 MiB test, input/display/SD and USB failure evidence. No reboot, kernel build or BOOTIMG was prepared. This checkpoint supersedes stale untested/blocked statements below within its measured scope.

# Y2E-175 — Specify a read-only removable-SD controller proof

## Offline integration checkpoint — 2026-09-10

Both MSDC controllers are enabled only for identification/metadata, at <=400kHz with inherited rails. No MMC block driver, filesystem mount/write, erase or eMMC CMD6. Safe eMMC init refusal after identity is expected; no rootfs installation.

[M2-BASELINE-01: exact implementation, RAM decision, checks and owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md). The historical scope/sequence below is superseded where it conflicts with the owner’s combined integration instruction. All remaining acceptance criteria stay open.

## Additional evidence — 2026-09-10

External records report working eMMC/SD and later asynchronous MMC discovery; use this to validate/adapt MSDC rather than rediscover it. No specific reproducible controller CRC/timing failure was found. Correct pinctrl/error handling, derive clocks/rails/pins, own DMA and retain read-only removable SD first. The rootfs corruption investigation instead identifies mismatched deployment address spaces; it is not an MMC tuning fix or permission to adopt their partition layout.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Donor update 2026-09-09: Donor board DT and mtk-sd patch accelerate MSDC work but do not establish safe controller compatibility. Preserve v6.18 improvements, correct optional pinctrl handling (including probe defer), identify real clocks/rails/card pins and quiesce/own DMA. Read-only removable SD remains the first storage validation, then development rootfs and appropriate read-only eMMC understanding. Never adopt donor root=p8 or write unrelated partitions. See [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md).

Canonical issue [#26](https://github.com/SchulzCode/Y2Linux/issues/26); [historical execution order](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md%23historical-foundation-research-queue&anchor=historical-foundation-research-queue).

## Type and goal

Research. Define one evidence-backed removable-SD identification/read test that leaves internal eMMC completely outside Linux driver ownership.

## Why it comes next

Storage will eventually carry music and a rootfs, but removable SD is the smaller first experiment surface. The retained map distinguishes mmcblk1 from eMMC; upstream mt6582.dtsi has no MMC node and no exact compatible is established. Display-DMA, power and memory constraints must precede a new bus master.

## Dependencies

Execute after Y2E-170's display ownership/DMA decision and use Y2E-160 supplies, Y2E-155 memory decision (D08 remains default), partition-map.md and the audited v6.18 MMC support gap. A RAM/display/input implementation is not required to complete this research; missing dependencies must be explicit in the proposal.

## Exact scope
  - Map the removable slot to one stock MSDC controller, MMIO/IRQ, pins, clock,

power/card-detect and bus width using retained registration/code/metadata. Do not infer controller numbering from mmcblk order alone.
  - Compare only its initialization and read-transfer essentials with pinned

v6.18 `mtk-sd.c`; state the exact match/gaps instead of choosing a sibling compatible by name. Identify minimal clock/pinctrl/PMIC prerequisites.
  - Choose evidenced PIO or bounded DMA semantics for one future CID/CSD/capacity

and known-block read proof, with timeouts, DMA ownership and error reporting.
  - Specify enforceable no-write/no-mount behavior, explicit internal-eMMC disable,

and a separately owner-approved disposable test card/known reference block. Host/card preparation and raw reads are not performed by this issue.

## Explicit out-of-scope

MMC/clock/pinctrl implementation, raw block acquisition, eMMC enable or writes, boot0/boot1, partition changes, filesystem mount/repair, Debian/rootfs, hotplug, high-speed tuning, SDIO/radios and card preparation.

## Expected files/components

New `docs/knowledge/storage-path.md`, `partition-map.md`, `power.md`, `linux-6.18-support.md`, `open-unknowns.md`; exact prospective MMC host, clock, pinctrl/regulator and DT dependencies. Do not edit runtime code.

## Acceptance criteria

One controller-to-slot mapping and minimal read-mode contract has evidence for every required address/IRQ/clock/supply/pin. Identify unsupported upstream pieces and select just the first implementation prerequisite if a host driver is too large. Include the no-write enforcement mechanism, selected-card identity guard, read/hash comparison, timeout and visible error criteria for a later trial. If these cannot be specified, report the single smallest blocker, not a guessed DTS or an umbrella complete-storage implementation.

## Validation

Reconcile FM/LK read/stop sequences and slot metadata; review proposed DMA ranges against the retained RAM/display exclusions, and read-mode behavior against upstream source. No new device operation or complete ROM re-audit is needed.

## Stop conditions

Stop on uncertain eMMC/SD identity, unproved compatible/clock/pins, unavoidable write/erase/tuning operation, unbounded DMA or inability to enforce no writes. Do not enable internal eMMC as a fallback to a missing removable-card path.

## Unlocks next

One small host prerequisite or read-only SD implementation; later file access, eMMC and persistent rootfs remain separate evidence/authorization boundaries.

## Session and execution boundary

Planning only today. Executing this research issue later does not authorize a Linux build, DTS/driver change, flash, new boot, bus scan, raw MMIO access, security change or partition write. Use retained evidence and pinned v6.18 source first; allow only explicitly safe, bounded stock observations when available. Keep private device data in ignored evidence storage and cite source/hash/offset locators in knowledge documents. Preserve uncertainty; do not invent a compatible, register value or board wire. Do not create follow-on issues automatically.

Future localized implementation uses one clean build, affected tests and the D08/layout/BOOTIMG validator plus final size/hash. Material memory/architecture/ packaging changes or a new hardware subsystem require the broader relevant verification boundary, not a habitual full provenance/recovery re-audit. Stock preloader/LK, partition layout and calibration remain protected.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
