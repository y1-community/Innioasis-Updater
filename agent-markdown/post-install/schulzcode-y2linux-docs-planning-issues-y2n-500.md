---
title: "Y2N-500 — M5 connectivity, firmware and conditional FM coverage - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2n-500.html"
---

# Y2N-500 — M5 connectivity, firmware and conditional FM coverage - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2N-500 — M5 connectivity, firmware and conditional FM coverage

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## Current session checkpoint — 2026-09-10

M5 NOT STARTED. Wi-Fi/Bluetooth, own firmware/calibration, BlueZ and reconnect/coexistence remain later. USB Ethernet is not radio qualification.

[September 10 session audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23current-session-close-audit--2026-09-10&anchor=current-session-close-audit--2026-09-10). Earlier phase ordering below is historical where superseded.

## Platform-first gate — 2026-09-10

The owner now requires M2 core/Buildroot, complete M3 native audio, M4 full power, M5 connectivity, GPU/lima and final whole-platform qualification before Y2PlayerNative begins. This supersedes earlier wording that allowed central application work after a wired-player slice. DEV-02 qualifies the core resources but USB reconnect remains the immediate #27/#28 blocker. This checkpoint grants no new hardware-phase or flash authorization. [Live result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md).

# Y2N-500 — M5 connectivity, firmware and conditional FM coverage

## Additional evidence — 2026-09-10

Retained cold-boot logs show full firmware/filesystem calibration (592 records) followed by MD1 off, then Classic discovery/A2DP; power-only and stopping at boot-ready failed. This explains prerequisites outside donorSource but does not justify using another player's private calibration or raw-MMIO bootstrap architecture. EDR credit stalls survived calibration/reset, address-init and PA-settle experiments; Basic Rate is a controller-scoped quirk, not a global ban, and remains a workaround. Interrupted calibration/radio restart reboot remains unexplained. Validate own cold/warm behavior in M5; no usable FM reception target on our older board.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Donor update 2026-09-09: The donor WMT/STP/BTIF, cfg80211 fullmac and FM source is retained as later-phase reference. Connectivity remains deferred unless a small M2 dependency requires it. The owner confirms this physical older Y2 has no usable FM reception hardware: reception is not an implementation or exit promise for this board. Preserve firmware/calibration and shared power/memory ownership gates; no global Bluetooth workaround or whole vendor dump enters M2. See [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md).

Canonical epic [#31](https://github.com/SchulzCode/Y2Linux/issues/31); [coverage audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

Deferred planning epic; no implementation-ready children added by this audit.

## Goal / why this epic is needed

Keep native Wi-Fi/Bluetooth and revision-dependent FM foundations represented without treating stock firmware filenames as proof of usable upstream drivers. FM application work remains the blueprint's later M16 boundary.

## Dependencies / evidence

`docs/knowledge/wifi-bluetooth.md`, `audio-path.md`, stock ramdisk WMT/STP and firmware inventories; shared power/reset/clock/transport and reserved-memory contracts from the core/power epics. Bluetooth audio also needs native audio. Do not require successful Wi-Fi/BT/FM before the initial wired player slice.

## High-level coverage

Identify exact controller/revision, SDIO/UART/other transport, STP/WMT role, reset/IRQ/clock/supplies and native driver feasibility. Pin actually selected firmware, initialization order, calibration/NVRAM/MAC ownership and redistribution provenance. A vendor 3.4 kernel module is not a v6.18 driver. Preserve credentials, bonds and unique addresses privately; package no unreviewed firmware blobs.

Wi-Fi scope eventually includes standard interface, regulatory/antenna/region constraints, WPA capability, reconnect, DHCP/DNS and trusted time. Bluetooth includes HCI/BlueZ feasibility, pairing/reconnect, A2DP/AVRCP and measured codec negotiation, shared radio coexistence and power behavior.

Explicit FM branch: distinguish chip ID/open/tune from actual RF reception, antenna population, board revision and native transport/audio routing. Record supported or unsupported/deferred per revision; never promise FM universally.

## Exit evidence / unlocks

For each supported radio: hardware/firmware/driver provenance plus captured native functional and reconnect/power results. FM remains conditional on useful reception evidence. Gate F unlocks network/BT application services; FM support unlocks later FM-specific planning. Missing/unpopulated functionality is recorded explicitly rather than hidden behind a generic connected status.

## Out-of-scope / stop

No network UI, scrobbling, proprietary stack port, bus probing, firmware execution or calibration writes today. Stop at unproved transport, firmware provenance, missing native driver, unsafe power/coexistence or unverified radio hardware. No detailed radio backlog is created before the first bounded identity proof.

## Execution and validation boundary

High-level planning epic only, not an implementation task or hardware permission. Expand only the next evidence-backed change when this phase is activated; preserve existing stable IDs and link existing issues instead of duplicating them. No speculative driver task list, build, flash or experiment is authorized by this epic.

Before closing the phase or proceeding through its exit gate, repeat the [standing roadmap/gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) using real hardware results. Separate owner reports, retained artifacts, source support and actual device validation. Unknown dependencies stop the relevant path; do not guess hardware or silently broaden scope. Milestone qualification uses the appropriate full verification boundary; small later fixes keep targeted validation and D08/package checks without routine provenance re-audits.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
