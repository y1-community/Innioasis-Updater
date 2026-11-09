---
title: "CONNECTIVITY-09 — permanent MT6582 E2 HCI page correction - Innioasis Updater"
description: "CONNECTIVITY-09 — permanent MT6582 E2 HCI page correction <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m5-connectivity-09-deployment.html"
---

# CONNECTIVITY-09 — permanent MT6582 E2 HCI page correction - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-09 — permanent MT6582 E2 HCI page correction

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-09 — permanent MT6582 E2 HCI page correction > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

**Owner-installed CONNECTIVITY-09 reaches standard hci0/BlueZ on normal boot, and normal BlueZ power-on/off succeeds.** No diagnostic module or runtime correction is needed; core errors/recoveries and kernel taint remain 0. [Physical -09 verification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity09%2FREADME.md). The HCI initialization defect was page 2 of Read Local Extended Features: page 1 advertises maximum 2, but page 2 returns status `0x30`. Linux's existing quirk and verified page limit 1 fix it without changing EDR/LE feature/command bits. [Physical result and limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity08%2FREADME.md).

This installed image makes the correction permanent, only for chip `6582`, HVR `8a01`, FVR `8a00`. The -08 RF calibration correction, patches, factory provider, DMA, M4 and memory/storage layout remain intact. Wi-Fi still fails after its Start command; no Wi-Fi fix or full radio qualification is claimed.

## Artifacts and validation

Directory: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m5-connectivity-09/`. Source: `f55fff48926c578fcfcd84ef8074d0693b3442e3`. Kernel: `6.18.0-y2linux-m5-connectivity-09`. Retain installed CONNECTIVITY-07 Y2ROOT and all Y2DATA.````````

| File | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 6150144 | 200346dff20ea1ffe769278bc8c52a19402d850a380c2054f6e93d1ef167de7a |
| fallback/BOOTIMG-previous.img | 6150144 | 5b8e333cdb9fff7bf314abf905ad11a7f26d23e8dab4fd4a4cf78a0bd58b0d78 |

[Validation receipts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m5-connectivity-09%2FREADME.md): 15 targeted connectivity tests, one clean build, emitted D08/DT/memory/BOOTIMG checks and BOOTIMG-only package validation. Normal-boot adapter registration and a standard runtime power-on/off are now physically verified on this -09 image.

## Owner installation and verified observation

The owner has completed this installation. The retained procedure below is for reproducibility; another installation is not required for this checkpoint.

The existing deployment contract reserves installation for the owner. Verify `sha256sum -c SHA256SUMS` in the package directory. Use the established SP Flash Tool setup, `MT6582_BOOTIMG_only_scatter.txt`, Download Only, and **BOOTIMG → BOOTIMG.img only**. Preserve ANDROID/Y2ROOT, USRDATA/Y2DATA, loaders, tables and protected partitions. No Format/Firmware Upgrade or assistant flash.

USB SSH verifies -09 with `uname -r`, the WMT 630-byte calibration success, `bluetoothctl list/show`, and one standard runtime-only power-on/off while retaining saved preferences. The BlueZ adapter appears without any diagnostic module or runtime patch. No factory/DMA/identification re-investigation occurs.

Fallback selects only BOOTIMG, using `fallback/BOOTIMG-previous.img` (-08). It keeps the RF fix but retains the unfixed HCI page-2 failure on a fresh boot; the temporary live HCI quirk does not survive reboot. Accepted M4 fallback artifacts remain documented in the original M5 handoff.

The verified -09 session is returned to both radios off, with saved preferences still 0 and the BlueZ adapter still visible. Pairing, A2DP, BLE/EDR data and coexistence remain unqualified. M5 stays open; GPU/Reborn remain out of scope.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
