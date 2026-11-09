---
title: "CONNECTIVITY-02: correction of the first startup failure - Innioasis Updater"
description: "CONNECTIVITY-02: correction of the first startup failure <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identit"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity02-corrections.html"
---

# CONNECTIVITY-02: correction of the first startup failure - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-02: correction of the first startup failure

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-02: correction of the first startup failure > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

CONNECTIVITY-01 physically stopped with `stage=1 FS=0 result=-71`; MD shutdown succeeded. SSH inspection reconfirmed that state. The first candidate did not record the rejected message, so its exact rejection site remains unproven until the corrected image runs. No new factory-partition acquisition was needed.

## Targeted corrections
  - Normalize the MD filesystem request's optional trailing transport word before

passing counted arguments to the existing private service. The previous kernel rejected any bytes after the last argument. Stock `ccci_fsd` GetPackInfo (`0xd414`–`0xd4ac`) follows the argument count and four-byte alignment without requiring the final argument to exhaust the shared stream. Retained successful CCIF request lengths include 32-byte disk-info and 20-byte close transactions, consistent with a trailing word. This is protocol evidence, not calibration replay. Accept only zero or four trailing bytes, retain all bounds and the service's strict request/reply ABI, and never interpret the trailer as data.
  - Report failed message channel, size, slot, stage and completed transaction

count. A framing failure reports a recognized opcode and bounded argument count. Never print filenames, argument values, addresses belonging to devices, or calibration contents. Clear private buffers on failed calibration shutdown.
  - Include the signed regulatory database and its license in the production

initramfs. Built-in cfg80211 previously requested it before Y2ROOT mounted and got `ENOENT`. Use the exact hash-locked wireless-regdb 2026.05.30 archive already used by the installed Buildroot image; retain kernel signature enforcement.
  - Allow the existing BOOTIMG-only packager to use a data-preserving system-update

package as its verified base. Carry the existing Y2DATA identity by reference; never require or package a Y2DATA template for this update.

The FS framing correction is a bounded compatibility fix. The previous aggregate failure does not prove it was the only initialization problem. Physical calibration, controller identification, Wi-Fi and Bluetooth remain pending.

## Preserved components

Y2ROOT remains CONNECTIVITY-01 (`2025.02.17-connectivity.1`), including the factory provider, calibration daemon, wpa_supplicant, BlueZ and BlueALSA. User credentials, bonds, radio preferences and generated identities remain in Y2DATA. M4 power, charging, RTC, audio, memory reservations, DT and protected-partition write policy are unchanged. The early regulatory files start no radio in offline charging.

After the owner's BOOTIMG-only installation, inspect the new boot log, calibration completion/poweroff, regulatory loading and normal radio interfaces through SSH. If initialization succeeds, continue the existing M5 qualification procedure. Otherwise use the precise failure context for the next targeted correction. M5 stays open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
