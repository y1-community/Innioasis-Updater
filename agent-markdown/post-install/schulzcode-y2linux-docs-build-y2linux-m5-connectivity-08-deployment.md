---
title: "CONNECTIVITY-08 — targeted RF calibration protocol correction - Innioasis Updater"
description: "CONNECTIVITY-08 — targeted RF calibration protocol correction <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate id"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m5-connectivity-08-deployment.html"
---

# CONNECTIVITY-08 — targeted RF calibration protocol correction - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-08 — targeted RF calibration protocol correction

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-08 — targeted RF calibration protocol correction > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The candidate fixes the verified host rejection of this MT6582 E2 controller's 630-byte RF calibration event. Full STP negotiation, both patch downloads and both resets already succeed. The new kernel preserves strict length, CRC, status and operation checks and scopes the extended reply to HVR `8a01` / FVR `8a00`. M4, firmware sequence, factory handling, DMA and memory layout are unchanged. [Physical diagnosis](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-protocol%2FREADME.md).

## Ready artifacts

Package: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m5-connectivity-08/`. Source: `8b18ca35956bf3287b7d8a15fdb8d4dcddda3d49`. Kernel: `6.18.0-y2linux-m5-connectivity-08`. Retain installed CONNECTIVITY-07 Y2ROOT and all existing Y2DATA.````````

| File | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 6150144 | 5b8e333cdb9fff7bf314abf905ad11a7f26d23e8dab4fd4a4cf78a0bd58b0d78 |
| fallback/BOOTIMG-previous.img | 6150144 | eaf2360d3e29b77d860689c4f9b97f6729143e0cebcd8bef4e001b72cee39ea0 |

[Targeted validation receipts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m5-connectivity-08%2FREADME.md) record the clean build, 14 passing connectivity tests, emitted artifact checks, original-failure regression and BOOTIMG-only package validation. The emitted-DT test runs against the completed candidate; unchanged source/ROM provenance is not repeated.

## Owner installation

The standing deployment contract remains manual owner installation. Verify `sha256sum -c SHA256SUMS` from the package directory. In the established SP Flash Tool setup, load `MT6582_BOOTIMG_only_scatter.txt`, use Download Only, and select BOOTIMG → BOOTIMG.img only. Preserve ANDROID/Y2ROOT, USRDATA/Y2DATA, loaders, tables and protected partitions; do not use Format/Firmware Upgrade. Start normal Linux deliberately using the accepted M4 power procedure and reconnect USB SSH. This session has performed no assistant flash.

For the responsive -07 Linux fallback, select the same single BOOTIMG row but use `fallback/BOOTIMG-previous.img`. Its radio startup still fails at the RF result. It is compatible with the retained -07 root. Accepted M4 fallback artifacts remain documented in the original M5 deployment handoff.

## Continue the live session

After `uname -r` confirms -08, inspect only the new startup stages and interfaces:`cat /sys/devices/platform/18070000.connectivity/status dmesg | grep -E 'WMT|STP|connectivity|Bluetooth|wlan' bluetoothctl list iw dev`

Expected progression is full STP verified, patch 1/reset, patch 2/reset, `WMT RF calibration succeeded: event=630 bytes`, then coex/co-clock and function startup. If necessary, use the existing runtime-only radio controls and standard BlueZ/cfg80211 tools, preserving saved radio preferences. A sysfs hci0 object alone is insufficient: require a BlueZ adapter or an `iw dev` wlan0 interface. Capture any subsequent opcode/stage failure before changing another component.

Do not redo factory acquisition, DMA/IRQ or controller identification research. A normal boot necessarily executes its existing initialization, but this is not a new diagnostic workstream. M5 remains open; pairing/audio/network/coexistence qualification and any future milestone audit are separate later gates. GPU/Reborn remain out of scope.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
