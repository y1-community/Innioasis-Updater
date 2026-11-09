---
title: "Y2E-155 — Specify one safe static RAM expansion step - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-155.html"
---

# Y2E-155 — Specify one safe static RAM expansion step - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-155 — Specify one safe static RAM expansion step

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## DEV-02 live hardware checkpoint — 2026-09-10

SATISFIED narrow research/bring-up scope on physical DEV-02; remaining production/full-platform concerns belong to #29–32.

[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) retains baseline, completed 256 MiB test, input/display/SD and USB failure evidence. No reboot, kernel build or BOOTIMG was prepared. This checkpoint supersedes stale untested/blocked statements below within its measured scope.

# Y2E-155 — Specify one safe static RAM expansion step

## Offline integration checkpoint — 2026-09-10

D08 retained after large-bank/LK/DMA/HIGHMEM reconciliation. The unresolved live ownership boundary outside D08 prevents defensible expansion; no arbitrary increment or donor 992MiB mapping. Actual combined kernel/layout fits D08.

[M2-BASELINE-01: exact implementation, RAM decision, checks and owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md). The historical scope/sequence below is superseded where it conflicts with the owner’s combined integration instruction. All remaining acceptance criteria stay open.

## Additional evidence — 2026-09-10

The additional history corroborates the large stock bank but does not establish LK heap lifetime or complete DMA ownership. A traced stock modem load overwrote their supposedly excluded HYP trace/stub region. Keep D08; #22 still needs a justified useful static expansion with explicit loader/high exclusions and Linux 6.18 lowmem/HIGHMEM validation. No new safe RAM interval or hardware result is claimed.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Donor update 2026-09-09: The donor DT corroborates our stock main 992 MiB bank. The owner explicitly supersedes tiny arbitrary increments: target a useful large static expansion toward evidenced RAM after reconciling LK heap/lifetime, all inherited DMA, high carveouts and v6.18 lowmem/HIGHMEM. Donor consys@bdf00000 is a chosen reservation, unlike our inferred stock bfa00000 allocation. D08 remains unchanged in the first GPIO-input candidate. Full memory/layout and allocator-owned-page hardware validation still gate expansion. See [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md).

Canonical issue [#22](https://github.com/SchulzCode/Y2Linux/issues/22); [historical execution order](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md%23historical-foundation-research-queue&anchor=historical-foundation-research-queue).

## Type and goal

Research. Produce an evidence-backed decision for one additional allocator RAM interval beyond D08, or a precise NO-GO identifying the one missing proof. Do not implement the expansion.

## Why it comes next

Physical Linux/PID1 and periodic diagnostics now work, but D08 describes only 24.5 MiB. Extra working space will help later drivers/userspace. Stock reporting of nearly 1 GiB is not permission to reclaim loader, DMA or display storage.

## Dependencies

Y2E-130 #7, Y2B-250 #21 and the latest owner-reported diagnostic success. Read `initial-ram-map.md`, `boot-chain.md` and the retained FM/LK analyses. This is first in the five-issue execution order.

## Exact scope
  - Trace only normal-handoff LK live allocation/heap/stack limits relevant to the

smallest useful candidate bank; remap symbols against the pinned FM inputs.
  - Reconcile that bank with retained stock iomem, ramdisk copy, low boot data,

modem/connectivity, display scratch and secure/DMA exclusions. RAM omission alone is not DMA containment. Do not reopen unrelated boot-chain research.
  - Specify one exact half-open added interval, expected extra described bytes,

non-LPAE mapping implications and retained exclusions. No full-1-GiB target.
  - Draft the explicit successor to D08 needed for that one experiment, including

all affected validator assumptions. D08 remains authoritative until reviewed; preserve current load addresses and caps unless a separately justified change is unavoidable. Record a bounded allocation/check/release test design using allocator-owned pages only, never a raw physical-memory sweep.

## Explicit out-of-scope

DTS/kernel/test implementation, memory stress on the device, SMP/HIGHMEM/CMA, reclaiming high framebuffer/modem storage, source/provenance re-audit and builds.

## Expected files/components

`docs/knowledge/initial-ram-map.md`, `docs/knowledge/open-unknowns.md`, a proposed `docs/knowledge/ram-expansion.md`; reviewed future impact list for `kernel/dts/innioasis-y2-first-boot.dts`, `tools/validation/d08.py`, DT/artifact validators and memory regression fixtures. No edits to those code components.

## Acceptance criteria

One candidate interval has source/runtime provenance and an overlap/lifetime matrix, or NO-GO has one named missing datum and safe acquisition plan. Explicitly separate observed RAM from inferred reusable RAM. Specify exact future DT and validator changes plus expected described-RAM delta, rollback candidate and observable pass/fail checks. No unbounded heap-end assumption is accepted.

## Validation

Cross-check interval arithmetic against the retained artifact layout and stock map; independently review loader-live versus post-handoff lifetimes. Document that a memory-policy change will require full relevant memory/layout regression and reproducibility review before any separately authorized trial. No build today.

## Stop conditions

Stop expansion design at unexplained overlap, heap/secure/DMA ownership ambiguity, non-LPAE limit or missing evidence. Keep D08 and record NO-GO rather than guessing.

## Unlocks next

A tiny explicitly reviewed static-memory implementation, independent of peripherals; the next queued power research can proceed even if expansion remains NO-GO.

## Session and execution boundary

Planning only today. Executing this research issue later does not authorize a Linux build, DTS/driver change, flash, new boot, bus scan, raw MMIO access, security change or partition write. Use retained evidence and pinned v6.18 source first; allow only explicitly safe, bounded stock observations when available. Keep private device data in ignored evidence storage and cite source/hash/offset locators in knowledge documents. Preserve uncertainty; do not invent a compatible, register value or board wire. Do not create follow-on issues automatically.

Future localized implementation uses one clean build, affected tests and the D08/layout/BOOTIMG validator plus final size/hash. Material memory/architecture/ packaging changes or a new hardware subsystem require the broader relevant verification boundary, not a habitual full provenance/recovery re-audit. Stock preloader/LK, partition layout and calibration remain protected.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
