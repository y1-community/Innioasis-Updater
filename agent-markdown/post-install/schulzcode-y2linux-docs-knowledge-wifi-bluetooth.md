---
title: "Wi-Fi, Bluetooth and firmware evidence - Innioasis Updater"
description: "Wi-Fi, Bluetooth and firmware evidence <!-- knowledge-base-scope: maintained-summary; baseline02-sync 2026-10-03 -- Wi-Fi optimization branch — 2026-10-04 Lock-protected"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-wifi-bluetooth.html"
---

# Wi-Fi, Bluetooth and firmware evidence - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Wi-Fi, Bluetooth and firmware evidence

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Wi-Fi, Bluetooth and firmware evidence

## Wi-Fi optimization branch — 2026-10-04

Lock-protected SSH now observes installed Baseline02 (compiled Linux `8584ccd`, Reborn `b71b468`, root v1.21, taint 0), superseding awaiting-installation wording for identity alone. The isolated Wi-Fi pass fixes measured observer deadlines, new-lease DNS scheduling, redundant RSSI/list/policy work and association-bound Online proof, plus useful redacted Wi-Fi diagnostic enums/counters. Baseline platform readiness took 27.99–32.24 s despite IP in 2.68–5.88 s; four 8 MiB HTTP transfers passed hashes at RX 43.94–44.92 / TX 46.38–46.94 Mb/s. Physical after measurements could not obtain the shared lock; source checks pass but whole-platform acceptance remains PARTIAL. The checksum repair, firmware/register semantics, conservative CAM automatic default and Bluetooth implementation remain unchanged. Exact results and remaining physical gates belong to the [Wi-Fi optimization report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-WIFI-OPTIMIZATION.md). Source tests do not close cold-boot, coexistence, electrical-power, endurance or full-suspend acceptance. Earlier physical failures below retain their scope.

## Current Baseline02 / UART01 scope

UART01 uses an independent Wi-Fi observer and bounded transport integrity alongside USB checks. Radios are off for guarded C3 entry windows. This does not qualify Bluetooth peer playback, optional Auto/ABR/codecs, radio endurance or full-system-suspend restoration. Baseline02 preserves matched firmware/provisioning and the current private experiment software; qualification and public distribution remain separate.

[Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) carry exact identities, counters and limits.

## Historical source research and physical checkpoints

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Wi-Fi, Bluetooth and firmware evidence

Latest bounded physical result, 2026-09-27: Fix01 independently verified four small Wi-Fi hash roundtrips totaling 1 MiB in each direction. An isolated CONSYS retry after a mandatory WMT timeout restored firmware, RF calibration, WLAN and HCI. Full suspend restoration and peer Bluetooth audio were NOT_TESTED; the final health check still reported supplicant_unavailable despite association, route and working TCP. Earlier radio discovery notes below retain their original scope. [Fix01 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md%23playback-connectivity-and-recovery&anchor=playback-connectivity-and-recovery).

2026-09-15:[fresh M5 entry audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity-entry.md) supersedes the deferred research wording below. Own retained BTIF/DMA/IRQ and CONSYS_MT6582 metadata, exact stock firmware hashes/header order and private read-only NVRAM/PROTECT copies are now recorded. Actual controller stepping, calibration record mapping and radio addresses remain unresolved. Current POWER-02 charging fails; M4 acceptance and the integrated M5 deployment remain blocked. No native Wi-Fi/HCI or connectivity qualification is claimed.

2026-09-10: [additional research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md) supplies native cold-start/A2DP records with complete modem calibration followed by MD1 off. It also records failed EDR remedies and a Basic Rate workaround. Validate our own revision and calibration; never adopt another player's fixture. M5 remains deferred, and FM reception is excluded for the owner's older board.

Date: 2026-09-08. Related tasks: Y2E-101/105/115. No radio scan, enable, pair, connect or firmware-loading action was performed.

CONFIRMED current metadata: `/system/etc/firmware` lists several WIFI_RAM_CODE variants, WMT_SOC.cfg, MT6572/82 patch blobs and an mt6627 directory. `/system/lib/modules/wlan.ko` is a symlink naming wlan_consys_mt6582.ko; target availability/loading is not established by that listing. `/proc/modules` is empty. Firmware presence does not prove which blob is selected, which transport is used, or whether a radio is populated and operational.

CONFIRMED static ramdisk evidence: WMT/connection loader declarations and STP-related node setup; a ttyMT2 connectivity comment. These identify a vendor ecosystem, not a standard Linux HCI transport contract or safe diagnostic UART. Current `ro.hardware=mt6582` is observed; reconcile it with older Bluetooth HAL-selection inferences instead of copying them.

The early `BLUETOOTH_STACK_INVESTIGATION.md` describes BlueAngel artifacts and originally lacked runtime evidence. Later archived route observations have different scope. Neither justifies promising BlueZ/PipeWire compatibility or specific negotiated codecs on native Linux.

UNKNOWN: exact controller revision, bus/transport, power/reset/clock sequence, required firmware/module hashes and order, calibration storage/ownership, MAC persistence and standard-kernel driver applicability. Keep addresses, bonds and network credentials private. Next proof is a bounded driver/firmware identity inventory with no radio state changes.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
