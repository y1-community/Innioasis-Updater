---
title: "Y2E-160 — Establish the MT6323 power and supply prerequisite map - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-160.html"
---

# Y2E-160 — Establish the MT6323 power and supply prerequisite map - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-160 — Establish the MT6323 power and supply prerequisite map

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## DEV-02 live hardware checkpoint — 2026-09-10

SATISFIED narrow research/bring-up scope on physical DEV-02; remaining production/full-platform concerns belong to #29–32.

[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) retains baseline, completed 256 MiB test, input/display/SD and USB failure evidence. No reboot, kernel build or BOOTIMG was prepared. This checkpoint supersedes stale untested/blocked statements below within its measured scope.

# Y2E-160 — Establish the MT6323 power and supply prerequisite map

## Offline integration checkpoint — 2026-09-10

One shared serialized PWRAP regmap now connects USB, upstream MT6323 MFD/regulators/power key and bounded backlight. CCF/pinctrl/EINT and I2C0/empty I2C1 are integrated. PMIC writes are filtered; battery ADC/charging policy remain disabled.

[M2-BASELINE-01: exact implementation, RAM decision, checks and owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md). The historical scope/sequence below is superseded where it conflicts with the owner’s combined integration instruction. All remaining acceptance criteria stay open.

## Additional evidence — 2026-09-10

The wrapper IRQ omission is a documented storm workaround, separate from PMIC EINT25. Final donor DT includes an MFD despite older minimal-PMIC prose. Next implement one serialized WACS2/regmap owner shared with USB, preserving sync-idle waits and refusal rules; derive real CCF/pin/rail contracts rather than trusting missing PLL probes or approximate rates. VGP2 brownout is a concrete shared audio-supply lead. Charging limits/telemetry still require our own validation.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

Donor update 2026-09-09: Donor PWRAP/MT6323, regulator and charger code materially accelerates provider design. Correct the variant and optional-IRQ/error handling, and use one serialized PWRAP/regmap owner shared with existing USB before enabling MFD/consumers. Do not replace the proven sync-idle wait or create competing wrapper claims. Separate calibrated ADC/status telemetry from the donor charger re-enable/current policy and unchecked writes. See [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md).

Canonical issue [#23](https://github.com/SchulzCode/Y2Linux/issues/23); [historical execution order](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md%23historical-foundation-research-queue&anchor=historical-foundation-research-queue).

## Current execution checkpoint — 2026-09-09

The owner explicitly requested one combined enumeration/logging candidate to reduce physical iteration. [Scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23combined-usb-ownership-scope-review--baseline-d9c2c98&anchor=combined-usb-ownership-scope-review--baseline-d9c2c98) keeps M1 complete, M2 active/exit blocked and later phases deferred. [CHRDET evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) establishes charger presence under the reported cable conditions; connected-start6a=BE still refuses wake. No new hardware result has been inferred.

Immediate next test: [M2-USBACM-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-01-result.md), 1,159,168 bytes, SHA-256 `d2d1f8cbbaa23ffcbdeddb317db7a8e62bc21deca9ebebc564c9b55a5590aedd`. [Reviewed combined contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-enumeration.md): boot unplugged, perform the proven guarded wake, attach at the screen prompt, check fresh supply/clock/PHY/DMA state, apply the FM/LK digital device-session sequence, then attempt upstream MUSB peripheral PIO, one standard g_serial ACM and bounded retained/live kernel + PID1 logging. No host VBUS supply, analog calibration, PMIC writes, active-DMA recovery, RAM expansion or other partition writes.

One clean build passes 23 full-suite methods, one additional linked-syscall mutation method and 8 observation methods, including 30 QEMU ARM PID1 scenarios and host/ARM relay faults. Exact DT/config, linked accesses, D08 and BOOTIMG pass. [Host capture tool](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md) is ready. No device operation was performed. Stop for the owner's BOOTIMG-only physical test within 60s. USBGUARD-01 remains an optional untested fallback, not a prerequisite test.

This advances offline implementation only. Physical enumeration, real log continuity, late-open/non-reading behavior and controller reconnect qualification remain outstanding. The first trial stops on first detach/error or 50s active window; reconnect and connected-start recovery are not implemented. #23/#27/#28 stay open, and every original hardware acceptance criterion remains intact. Original drafting-only restrictions below are superseded only for this specifically authorized/audited experiment, not a general production port.

## Type and goal

Research. Establish the minimum PMIC access and supply-ownership contract needed to research input, display/backlight and removable SD safely.

## Why it comes next

The stock inventory names `pmic_mt6323`, but battery service readings conflict. Rails and their control path are shared prerequisites; guessing them in each peripheral driver would multiply risk. Audio will later reuse this evidence.

## Dependencies

Execution follows Y2E-155's decision; expanded RAM is not a technical requirement. Use `power.md`, `y2-hardware.md`, retained platform metadata and the stock/FM kernel. Depend on the known M1 diagnostic baseline, not a new hardware test.

## Exact scope
  - Identify the bound PMIC/access transport and stock registration path, then

compare that specific path with pinned upstream v6.18 bindings/drivers.
  - Trace only named supply consumers for wheel/buttons, panel/backlight and SD;

record confirmed rails/enable owners versus unknown board routes. Locate potential GPIO/pinctrl/clock prerequisites without implementing controllers.
  - Explain duplicate battery fields from retained service evidence/code where

available; assess only standard, side-effect-reviewed power_supply metadata for units/source validity. Do not label voltage/state trustworthy by name alone.
  - Produce one dependency table and select the smallest future read-only identity

or telemetry implementation, or name the specific missing transport/rail proof.

## Explicit out-of-scope

Charging limits or regulator writes, complete regulator/charger/gauge port, calibration, battery cycling, suspend/cpufreq/cpuidle, shutdown/reboot changes, audio playback and Linux hardware operations.

## Expected files/components

`docs/knowledge/power.md`, relevant cross-references in `audio-path.md` and `open-unknowns.md`; evidence locators for vendor PMIC/PWRAP and matching upstream MFD, regmap, regulator and power_supply components. Do not assert sibling-SoC compatibility without register/transport evidence; no code edits.

## Acceptance criteria

Transport/driver identity and each scoped rail have CONFIRMED/INFERRED/UNKNOWN status with locators. Battery duplicate fields are explained or explicitly unresolved; no fabricated physical measurement. One future read-only probe has specified expected result, register/metadata safety and required prerequisites, or the document identifies a bounded blocker. Shared supply ownership is clear enough that later research will not propose disabling another consumer's rail.

## Validation

Reconcile stock bindings with FM call sites and exact upstream v6.18 support; verify units and distinguish framework output from hardware telemetry. Document all denials. Documentation/evidence consistency checks only in this issue.

## Stop conditions

Stop at any need for live PMIC/debug register reads of unknown side effects, rail/charge writes, uncertain units or ambiguous shared ownership. Preserve inherited power state and record the missing fact.

## Unlocks next

Safe input/display/SD research and a small later PMIC telemetry implementation; reusable supply prerequisites for audio without starting audio bring-up.

## Session and execution boundary

Planning only today. Executing this research issue later does not authorize a Linux build, DTS/driver change, flash, new boot, bus scan, raw MMIO access, security change or partition write. Use retained evidence and pinned v6.18 source first; allow only explicitly safe, bounded stock observations when available. Keep private device data in ignored evidence storage and cite source/hash/offset locators in knowledge documents. Preserve uncertainty; do not invent a compatible, register value or board wire. Do not create follow-on issues automatically.

Future localized implementation uses one clean build, affected tests and the D08/layout/BOOTIMG validator plus final size/hash. Material memory/architecture/ packaging changes or a new hardware subsystem require the broader relevant verification boundary, not a habitual full provenance/recovery re-audit. Stock preloader/LK, partition layout and calibration remain protected.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
