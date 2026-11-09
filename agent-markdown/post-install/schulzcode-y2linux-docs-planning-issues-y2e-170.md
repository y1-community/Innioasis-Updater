---
title: "Y2E-170 — Specify a safe display handoff and backlight ownership boundary - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-170.html"
---

# Y2E-170 — Specify a safe display handoff and backlight ownership boundary - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-170 — Specify a safe display handoff and backlight ownership boundary

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## DEV-02 live hardware checkpoint — 2026-09-10

SATISFIED narrow research/bring-up scope on physical DEV-02; remaining production/full-platform concerns belong to #29–32.

[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) retains baseline, completed 256 MiB test, input/display/SD and USB failure evidence. No reboot, kernel build or BOOTIMG was prepared. This checkpoint supersedes stale untested/blocked statements below within its measured scope.

# Y2E-170 — Specify a safe display handoff and backlight ownership boundary

## Offline integration checkpoint — 2026-09-10

MT6582 DRM variants, 480x360 panel, corrected PHY rate/cold sequencing, reset and monotonic inherited-current backlight are integrated. Existing 6.18 pitch fix is retained; raw framebuffer writes are removed. Display failures must be classified with the live USB log.

[M2-BASELINE-01: exact implementation, RAM decision, checks and owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md). The historical scope/sequence below is superseded where it conflicts with the owner’s combined integration instruction. All remaining acceptance criteria stay open.

## Additional evidence — 2026-09-10

The later September 9 recovery journal retracts 368 lines and reports camera-verified 480×360, matching our working geometry. Cold DSI register access required PHY power; rate-after-prepare failed with EBUSY; GPIO112 mode1 routes MMSYS panel reset. These explain patches 0033–0037 but their module parameters/userspace devmem are not a complete driver. Linux 6.18 already restricts PITCH_MSB writes to AFBC-capable OVL variants. Adapt remaining formats/PHY/quiesce/panel/backlight dependencies into current drivers, preserving USB and distinguishing live-LK from cold startup.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Donor update 2026-09-09: Use donor OVL/RDMA/COLOR/DSI/mutex, GC9503V table and ganged backlight as implementation starting points after supply/clock/DMA prerequisites. Forward-port variants into v6.18; remove raw framebuffer/debug writes, reconcile 360/368-line and buffer-address contradictions, repair backlight error handling/current ceiling/nonmonotonic mapping and supply/reset/backlight relationships. Preserve canonical USB while taking over display. No donor modeset is considered tested on our Y2. See [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md).

Canonical issue [#25](https://github.com/SchulzCode/Y2Linux/issues/25); [historical execution order](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md%23historical-foundation-research-queue&anchor=historical-foundation-research-queue).

## Type and goal

Research. Decide the smallest safe transition from the temporary D13/D14 framebuffer diagnostic to a standard Linux display interface, with explicit backlight and inherited-scanout ownership.

## Why it comes next

The actual 480x360 RGB565 path is now observed working. That is a useful display baseline but not a native panel/DRM/backlight driver. Power evidence and the input contract enable a coherent local interface without replacing the player yet.

## Dependencies

Execution follows Y2E-165; actual input implementation is not a hard dependency. Use Y2E-160 supply ownership, D13/D14, the FM-remapped panel/LK evidence and latest hardware result. Requires no RAM expansion; high framebuffer remains excluded.

## Exact scope
  - Trace only final normal LK scanout/backlight state into Linux, matching the

FM panel candidate and existing OVL/DSI guard evidence to board confidence.
  - Assess whether a simple-framebuffer/simpledrm handoff is defensible in pinned

v6.18 with this inherited pipeline and excluded aperture. Treat that as an interim interface only, not proof of panel initialization or full DRM support.
  - Identify the exact clock/supply/backlight owners that a future driver could

inadvertently gate, plus the diagnostic writer exclusivity requirement.
  - Choose one smallest handoff step, or document the specific controller support

prerequisite if takeover cannot preserve the observable recovery screen. Backlight control remains unchanged until its path and safe limits are known.

## Explicit out-of-scope

DRM/panel/DSI driver implementation, complete display-stack reverse engineering, panel reset/init writes, brightness experiments, suspend, rotation, acceleration, framebuffer reallocation and replacement of high-RAM exclusions.

## Expected files/components

`docs/knowledge/display-input.md`, `on-screen-diagnostics.md`, `power.md`, `open-unknowns.md`; prospective bindings/components in simple-framebuffer, simpledrm, MediaTek DRM, panel and backlight areas named only where evidenced. No DTS/config/diagnostic writer changes in this research issue.

## Acceptance criteria

Record exact aperture, dimensions, format, stride, scratch exclusions, ownership and candidate panel confidence. State GO/NO-GO for one standard-interface handoff, required clock/power support and how to avoid two active framebuffer writers. Specify a later visible pass/fail test with the old candidate retained. Do not equate ST7701-family naming with a verified board panel init sequence.

## Validation

Cross-check LK/FM evidence with v6.18 format/binding and driver ownership behavior; review mapping/cache policy, scanout DMA range and unused-clock/supply handling. A future new display subsystem gets its appropriate broader validation review; no build, panel command or boot occurs here.

## Stop conditions

Unknown panel reset sequence, unsafe gating, scanout ownership conflict, required RAM reclamation or loss of the only observation path stops takeover design. Keep D13/D14 intact and identify the smallest missing prerequisite.

## Unlocks next

One standard display-interface implementation, followed later by proper panel/ backlight work once specified; an explicit display-DMA exclusion for SD planning.

## Session and execution boundary

Planning only today. Executing this research issue later does not authorize a Linux build, DTS/driver change, flash, new boot, bus scan, raw MMIO access, security change or partition write. Use retained evidence and pinned v6.18 source first; allow only explicitly safe, bounded stock observations when available. Keep private device data in ignored evidence storage and cite source/hash/offset locators in knowledge documents. Preserve uncertainty; do not invent a compatible, register value or board wire. Do not create follow-on issues automatically.

Future localized implementation uses one clean build, affected tests and the D08/layout/BOOTIMG validator plus final size/hash. Material memory/architecture/ packaging changes or a new hardware subsystem require the broader relevant verification boundary, not a habitual full provenance/recovery re-audit. Stock preloader/LK, partition layout and calibration remain protected.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
