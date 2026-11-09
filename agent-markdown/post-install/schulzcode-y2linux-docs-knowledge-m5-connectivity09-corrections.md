---
title: "CONNECTIVITY-09: MT6582 E2 local extended feature page limit - Innioasis Updater"
description: "CONNECTIVITY-09: MT6582 E2 local extended feature page limit <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate ide"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity09-corrections.html"
---

# CONNECTIVITY-09: MT6582 E2 local extended feature page limit - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-09: MT6582 E2 local extended feature page limit

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-09: MT6582 E2 local extended feature page limit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

CONNECTIVITY-08 physically clears the RF-result EPROTO. The next exact failure is HCI Read Local Extended Features (`0x1004`) page 2: this controller's page-1 reply advertises maximum 2, but page 2 returns status `0x30`. Linux maps that status to `-38` and aborts initialization before BlueZ exposes the adapter. [Own hardware trace and successful runtime test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity08%2FREADME.md).

After successful vendor setup/reset, apply Linux's existing `HCI_QUIRK_BROKEN_LOCAL_EXT_FEATURES_PAGE_2` only to chip `6582`, HVR `8a01`, FVR `8a00`, and cap `max_page` at the verified page 1. Setting the quirk alone does not lower a false value cached by an earlier failed initialization. The normal nonpersistent setup callback repeats the correction after function power loss. No HCI feature or supported-command bitmap is edited. EDR, LE, status checking, WMT framing/patch/calibration, factory, DMA and M4 stay intact.

The targeted regression combines the actual native quirk helper with the pinned Linux extended-feature reply handler and page iterator. It reproduces unfixed page-2 `-ENOSYS`, verifies fresh and previously failed HCI state, retains all feature/command bytes and unrelated quirks, preserves negative status, and leaves other controller triples untouched.

The live -08 diagnostic first reached standard hci0/BlueZ and accepted runtime power-on. The owner-installed -09 production BOOTIMG now verifies the same result on normal boot, without any diagnostic module or runtime correction. Standard BlueZ power-on/off succeeds with zero core errors/recoveries and kernel taint 0. [Physical -09 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity09%2FREADME.md). CONNECTIVITY-07 Y2ROOT/Y2DATA and the -08 BOOTIMG fallback are retained. No Wi-Fi fix or full pairing/audio/coexistence qualification is implied; M5 remains open. Do not repeat settled identification/factory/DMA work.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
