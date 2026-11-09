---
title: "M2-CHRDET-01 — PMIC charger-presence observation - Innioasis Updater"
description: "M2-CHRDET-01 — PMIC charger-presence observation <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-chrdet-probe.html"
---

# M2-CHRDET-01 — PMIC charger-presence observation - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-CHRDET-01 — PMIC charger-presence observation

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-CHRDET-01 — PMIC charger-presence observation > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Result received: [CHRDET follows reported startup cable state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md). The connected-start PHY guard refuses before writing; the next step exposes its original inputs in [M2-USBGUARD-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-guard-diagnostic.md). The contract below describes the tested candidate.

2026-09-09, localized #23/#27 prerequisite after the [same-boot PHY wake result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-hardware-result.md). USB is attached but DEVCTL remains 80. Read the independent PMIC indication before considering the stock internal VBUS-force sequence. No electrical cable/connector assumption.

## Exact source and access contract

The retained FM upmu_get_rgs_chrdet at c04b8c38 calls pmic_read_interface at c04b8c68 with address 0x0000, mask 1, shift 5. The pinned MT6582 upmu_hw.h independently identifies CHR_CON0=0x0000, RGS_CHRDET mask 1/shift 5. This is the ordinary status accessor, not interrupt status or an acknowledge. Focused disassembly is retained privately as fm-chrdet-accessors.txt; reuse the existing FM provenance and pinned source d53dd75c3ff77cac3f5be58fddfe660e94f94d64. FM charging_get_charger_det_status at c04cb0b0 calls this same accessor twice, corroborating ordinary repeatable status reads (fm-chrdet-charging.txt). The vendor usb_cable_connected also checks role and charger type; CHRDET alone does not distinguish a data host, charger, usable data wires or USB readiness.

Extend the established PWRAP whitelist with exactly this one 16-bit PMIC read, after successful CID/VUSB transactions and the MT6323 CID guard. Its AP WACS2 read command is 0x00000000 at AP+9c; bit31 remains clear. Use the existing bounded completion/idle waits, acknowledge only this completed response and never retry, clear stale responses or issue a PMIC write. Failure stops further clock/USB probing. Preserve partial validity: CID=1, VUSB=2, CHR_CON0=4; full=7.

Snapshot grows four bytes to 260, shared by kernel and native PID1. Display `CHR:<raw four hex digits> D:<bit5>` when valid, otherwise `CHR:---- D:?`. Both CHRDET 0 and 1 are successful observations; do not turn a low status bit into a transport error. The rest of the PHY wake probe is unchanged, including its one guarded 6a write and calibration checks. No new hardware write beyond the PWRAP read request/ack, no charger policy, interrupt enable, clock, VBUS-force, MAC connection, DMA or calibration change. Everything remains cached once/boot.

## Validation and hardware boundary

This is a localized extension of the hardware-proven read transport, not a new subsystem or memory/DMA/packaging policy. One clean build, affected PWRAP/clock/ state/wake/PID1 tests, linked transaction review, standard artifact checks and D08/current-memory/BOOTIMG size/hash validation. No duplicate build or unchanged source/ROM/recovery audit. Test both detection states and third-transaction timeout, lost-init, invalid-FSM and acknowledge-to-idle failures.

Stop at BOOTIMG for the owner test with the USB data cable attached to the PC. Return same-boot readable photos near BEAT 10 and 50/STOP showing CHR/PW/CLK, USB and all four PHY rows, uptime/IRQ and LAST ERR. Retain the established maximum 60 seconds from power-on and BOOTIMG-only recovery boundaries. Enumeration/ttyACM is not expected; #23/#27 and M2 remain open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
