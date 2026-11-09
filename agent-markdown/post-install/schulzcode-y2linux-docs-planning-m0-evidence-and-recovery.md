---
title: "M0 — Evidence & Recovery Baseline - Innioasis Updater"
description: "M0 — Evidence & Recovery Baseline <!-- knowledge-base-scope: decision-log-/-historical-roadmap -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-m0-evidence-and-recovery.html"
---

# M0 — Evidence & Recovery Baseline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M0 — Evidence & Recovery Baseline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M0 — Evidence & Recovery Baseline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current audit (2026-09-09): M1 core is achieved under the owner-accepted bounded risk policy, and same-device SPFT/BOOTIMG recovery evidence exists. M0 remains open for unresolved personalized backup/lineage/consistency facts; older absolute launch-blocker language below is historical. See [roadmap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md) and [D11](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md). Recovery/production continuity is tracked by Y2R-600 #32, without another blanket SPFT rehearsal.

Updated 2026-09-08. Canonical milestone: [Y2Linux M0](https://github.com/SchulzCode/Y2Linux/milestone/1). Gate: NOT PASSED.

## Ownership and history

Y2Linux owns all reverse engineering, stock firmware/kernel analysis, hardware evidence, recovery, Linux 6.18 research, kernel/device-tree work and platform bring-up. Y2PlayerNative owns the later native Rust/C application and its application architecture. The local Android reference remains `/home/luca/Dokumente/Code/Y2Player/`.

The first five issues were transferred from Y2PlayerNative without duplication. Original issue URLs redirect to Y2Linux and GitHub preserves the transfer history. The old native-repository M0 milestone was closed as superseded, not passed. The supplied blueprint remains a historical architecture reference; the current repository/role instruction supersedes its assignment of research tasks to an implementation role.

Research owner: investigation, read-only captures, reverse engineering, evidence interpretation, knowledge documents, architecture and precise implementation specifications. Implementation owner: only the bounded intended change after those questions are answered. No current research task is implementation-ready.

## First evidence boundary and results[](https://github.com/SchulzCode/Y2Linux/issues/1)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fevidence-index.md)[](https://github.com/SchulzCode/Y2Linux/issues/2)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstock-system-baseline.md)[](https://github.com/SchulzCode/Y2Linux/issues/3)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fpartition-map.md)[](https://github.com/SchulzCode/Y2Linux/issues/4)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fboot-chain.md)[](https://github.com/SchulzCode/Y2Linux/issues/5)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md)

| Stable ID | Research outcome | Prerequisite review |
| --- | --- | --- |
| Y2E-101 | Provenance audit: 24 original-package files hashed, both 93-file snapshots verify, generated-package failures quarantined | Independent passive device inspection allowed; no recovery certification |
| Y2E-105 | Current non-root baseline: one authorized target, remote error markers, denied/missing exports explicit | Partition metadata allowed; exact installed image still unknown |
| Y2E-110 | 21-entry partition reconciliation, eight exported starts/counts cross-check, special vendor spans unresolved | Exact packaged boot can be inspected offline; no raw device acquisition |
| Y2E-115 | Boot structure: stock component lineage verified, no DT/config markers in bounded search, load-address discrepancy documented | Recovery capability assessment allowed; Linux artifact construction blocked |
| Y2E-120 | Recovery gap packet: package/tool candidates, access/personalization/retention gaps and three next proofs | First research boundary reviewed; M0 remains open |

The issue specifications in `issues/` retain the original bounded goals with corrected canonical ownership/research role. Results above and the linked knowledge documents are authoritative for subsequent decisions. Denied/missing/failed observations can complete an investigation without satisfying the underlying hardware/recovery requirement.

## Second evidence boundary: Y2E-125

[Y2E-125](https://github.com/SchulzCode/Y2Linux/issues/6) accepts owner-observed successful SP Flash Tool recovery using the FM ROM, hashes all 24 package inputs, and corroborates local tool v5.2032.00. Offline preloader/LK analysis resolves the header/runtime discrepancy and confirms kernel entry, ATAGs, ramdisk relocation and command-line source. The exact v6.18 audit supports a candidate appended-DTB/initramfs strategy with unchanged loaders. See [boot-chain.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fboot-chain.md), [recovery.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md) and [linux-6.18-support.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flinux-6.18-support.md).

That memory proof was the next boundary and is now addressed by Y2E-130 below. Installed-loader/security state, observable console and device-specific backups still gate an experiment.

## Third evidence boundary: Y2E-130

[Y2E-130](https://github.com/SchulzCode/Y2Linux/issues/7) independently remaps FM symbols, explains the high reservation pattern and fixes D08: static DT memory `[0x80000000,0x81800000)` plus `[0x84000000,0x84080000)`, no ATAG import. The [initial RAM policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md) specifies permitted intervals, limits and exact decompressor/LK validation formulas. Small offline implementation can now be specified without delegating memory architecture. No implementation issue was created here.

U07c explicitly retains the unproved inherited DMA/secure-state requirement before launch. The reduced map excludes identified storage; it is not a DMA firewall or tested boot. M0 stays open.

## Coverage contract

| Area | Evidence now available | Remaining evidence before relevant implementation |
| --- | --- | --- |
| Identity/access | Fresh non-root system/build/USB state, errors and permissions | Physical revision, installed image provenance |
| Boot/storage | Package components/map and traced package preloader/LK ATAG handoff | D08 actual artifact validation, inherited DMA/secure state, installed-loader policy, special-region semantics and acquisition method |
| Audio/FM | Verified archived bindings and exact HAL/kernel derivatives; later route reports indexed | Current lineage, physical routing, reset/supplies/clocks/mute, reception/revision |
| Display/input | Archived controller and evdev capability identities; application behavior | Panel/interface/timings, wiring/reset/wake and current raw-code relationships |
| Power | PMIC historical identity, conflicting current battery service output | Trusted readings/calibration, charging/suspend/wake behavior |
| Wi-Fi/Bluetooth/firmware | Current filename/module metadata, stock loader declarations and vendor analysis | Controller/transport, loaded firmware hashes, calibration/power and upstream applicability |
| Recovery | Owner-observed successful same-device SPFT/FM restore; exact ROM and local v5.2032.00 tool hashed | Same-device backups/independent copies, exact DA/settings/entry sequence and power prerequisites |

## Execution and gates

Use CONFIRMED/INFERRED/UNKNOWN/DISPROVEN with date, task and raw locator. Preserve host UTC, remote status, command/tool version, bytes and hashes. ADB host 0 does not imply remote success. Private artifacts remain ignored and are never staged. Do not automatically execute historical scripts or vendor debug reads.

The first batch used no device writes, reboot, boot-mode change, radio toggle, raw block-device access, downloaded-agent execution, kernel/DTS change or application implementation. Read-only metadata does not make all possible device reads harmless: each later command needs a known interface and bounded scope.

M0 PASS requires a trustworthy device/build/partition/boot baseline, sufficient subsystem evidence and explicit critical unknowns, verified same-device boot/recovery/personalized-data backups with independent retention, and a documented known-good recovery path with appropriate checks. The owner's successful same-device SPFT recovery now supplies the actual tested-method evidence; do not demand another full-flash rehearsal merely to reconfirm it. Exact procedure/DA/entry details and backups remain incomplete. Preloader/LK/table/calibration writes and formatting stay outside ordinary restoration. Any later device operation still needs a concrete bounded procedure and authorization.

The memory/ATAG policy is fixed; next research must address a bounded launch prerequisite such as inherited DMA/secure state or physical console. Fill the specific acquisition/runbook gaps using the known-good recovery history; pursue console/power evidence only within safe bounded scopes. No speculative implementation backlog or M1 tasks were created. Only after research fixes a concrete intended change should an implementation issue be written.

## Later owner authorization: M1 offline wave

The owner changed the M1 execution model to direct implementation by the lead, without delegation. [M1 offline checkpoints](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md) are now implemented and validated against D08. This supersedes earlier implementation-role and no-artifact restrictions for offline work only. M0 hardware/recovery gates remain unsatisfied; actual artifact bounds are now resolved, while installed-loader/security, inherited-state, console, backups and power remain required before device launch.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
