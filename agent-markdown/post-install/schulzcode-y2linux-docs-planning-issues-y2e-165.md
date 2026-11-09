---
title: "Y2E-165 — Resolve the wheel and select-button event path - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-165.html"
---

# Y2E-165 — Resolve the wheel and select-button event path - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-165 — Resolve the wheel and select-button event path

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## DEV-02 live hardware checkpoint — 2026-09-10

SATISFIED narrow research/bring-up scope on physical DEV-02; remaining production/full-platform concerns belong to #29–32.

[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) retains baseline, completed 256 MiB test, input/display/SD and USB failure evidence. No reboot, kernel build or BOOTIMG was prepared. This checkpoint supersedes stale untested/blocked statements below within its measured scope.

# Y2E-165 — Resolve the wheel and select-button event path

## Offline integration checkpoint — 2026-09-10

Navigation, APT32F repeated-start wheel, keypad and PMIC power key are integrated with multi-device evdev/USB capture. Separate navigation-only flashing is superseded; all physical mappings and IRQ behavior await this combined boot.

[M2-BASELINE-01: exact implementation, RAM decision, checks and owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md). The historical scope/sequence below is superseded where it conflicts with the owner’s combined integration instruction. All remaining acceptance criteria stay open.

## Additional evidence — 2026-09-10

Keep the offline-validated M2-INPUT-01 as the navigation candidate; no returned hardware result was found. The history supports separate GPIO buttons and I2C0:0x51 rotation. Register-zero/repeated-start reads avoid the wandering pointer; final donor emits key taps, not the relative events claimed in prose, and omits AA header validation. Linux 6.18 already fixes the PMIC missing-home-key long-press pointer. Next prerequisites are reviewed pin/EINT maps, clocked and DMA-owned I2C, then wheel/keypad/PMIC-key validation on our older unit.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Canonical issue [#24](https://github.com/SchulzCode/Y2Linux/issues/24); [historical execution order](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md%23historical-foundation-research-queue&anchor=historical-foundation-research-queue).

## Type and goal

Research. Specify the minimal path for clockwise/counterclockwise wheel movement and the select button to become Linux evdev events.

## Why it comes next

Local controls are the next useful interaction primitive once diagnostics work. Power/transport evidence should precede controller access. Existing `mtk-kpd`, `mtk-tpd` and APT32F/UPDATE names do not prove which hardware produces the wheel.

## Dependencies

Execute after Y2E-160; use its supply/transport findings and report unresolved prerequisites instead of assuming them. Read `display-input.md`, the retained input capability inventory and Android behavior reference. No RAM expansion or full display driver is required for this research.

## Exact scope
  - Map only wheel CW/CCW and select press/release through retained stock input

capabilities, keylayout and the exact corresponding FM handler/call sites.
  - If safe stock access and owner actions are available in the later session,

capture bounded passive evdev/getevent output for those actions. No synthetic input, device grab, firmware update or arbitrary vendor ioctl. Otherwise state the missing event observation and preserve the offline findings.
  - Resolve transport, IRQ, pinmux/reset/supply prerequisites only for this path;

distinguish an MCU protocol from GPIO/keypad behavior using evidence.
  - Specify event codes, direction, release/repeat semantics and the smallest

upstream-compatible driver/DT addition, with raw trace fixtures where available.

## Explicit out-of-scope

Implementing input, all-button coverage, power-key hold/off, wake/suspend, Bluetooth/AVRCP, app navigation/acceleration policy, MCU firmware and bus probing.

## Expected files/components

`docs/knowledge/display-input.md`, a focused `docs/knowledge/input-path.md`, `open-unknowns.md`; reviewed prospective Linux input/evdev component and DT nodes. Android keylayout/handler references are evidence, not copied application code.

## Acceptance criteria

CW, CCW and select each have a source/event mapping, or explicitly named missing observation. No Android KEYCODE is substituted for an unproven evdev code. The selected path has register/protocol, supply, IRQ and pinmux provenance adequate for one implementation, or a single bounded prerequisite is reported. Draft the future on-screen event-counter test and stop criteria; no driver is authored.

## Validation

Cross-check sample press/release/detent ordering against stock handler behavior; check proposed v6.18 input API/binding support from pinned source. Count exact observed actions without claiming unmeasured debounce or acceleration behavior.

## Stop conditions

Ambiguous wheel source, unknown MCU protocol or required privileged/bus-changing access stops implementation specification. Do not guess GPIOs, scan addresses or flash peripheral firmware to discover functionality.

## Unlocks next

A tiny evdev input implementation and local navigation of future diagnostics. Display research follows in the queue without requiring that driver to be built.

## Session and execution boundary

Planning only today. Executing this research issue later does not authorize a Linux build, DTS/driver change, flash, new boot, bus scan, raw MMIO access, security change or partition write. Use retained evidence and pinned v6.18 source first; allow only explicitly safe, bounded stock observations when available. Keep private device data in ignored evidence storage and cite source/hash/offset locators in knowledge documents. Preserve uncertainty; do not invent a compatible, register value or board wire. Do not create follow-on issues automatically.

Future localized implementation uses one clean build, affected tests and the D08/layout/BOOTIMG validator plus final size/hash. Material memory/architecture/ packaging changes or a new hardware subsystem require the broader relevant verification boundary, not a habitual full provenance/recovery re-audit. Stock preloader/LK, partition layout and calibration remain protected.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
