---
title: "CONNECTIVITY-04: verify the real CONN EMI remap before startup - Innioasis Updater"
description: "CONNECTIVITY-04: verify the real CONN EMI remap before startup <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate i"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity04-corrections.html"
---

# CONNECTIVITY-04: verify the real CONN EMI remap before startup - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-04: verify the real CONN EMI remap before startup

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-04: verify the real CONN EMI remap before startup > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

CONNECTIVITY-03 now passes the native MD completion gate on this Y2: `stage=2 FS=841 restore=1 open=0 result=0 poweroff=0`, at uptime 48.502808 s. The owner reports a crash shortly afterward. Photos show faults on idle CPUs in timer/RCU interrupt processing; SSH stops responding. Both the kernel and Y2ROOT identify CONNECTIVITY-03, and the installed calibration helper matches the corrected binary. This is progress through MD calibration, not successful WMT/RF initialization or usable Wi-Fi/Bluetooth.

## Concrete register error

`y2_ccf_radio_remap(0)` used INFRACFG_AO + `0x1310`, physical `0x10002310`. The retained stock FM kernel's `mtk_wcn_consys_hw_init` at `0xc0564fa4` constructs virtual `0xf0001000` and accesses offset `0x310`: physical `0x10001310`. The donor's corrected header agrees; older donor comments still describe the wrong offset. The native implementation followed that stale offset, leaving the actual CONN-to-AP DRAM translation unchanged.

Correct the access to INFRACFG_AO + `0x310`. Replace the complete 13-bit address/enable field with `0x1bdf`, preserving other bits, and check readback. A rejected write returns `-EIO` before CONN power-on/reset release. The target remains the existing excluded `0xbdf00000` region. MD's four remap registers at `0x300`–`0x30c`, memory reservations and M4 ownership remain unchanged. Two bounded startup messages identify remap verification and BTIF entry.

The crash timing and multi-CPU faults are consistent with incorrect remote memory translation. After owner installation, the corrected candidate remains responsive through 813 seconds, including a bounded radio recovery, with the same boot ID and no captured crash signature. WMT startup still times out; see the [physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-16-m5-connectivity04%2FREADME.md). The lost CONNECTIVITY-03 stream does not identify every failing access.

## Validation and deployment scope

The regression executes the production remap function against modeled MMIO. It checks the stock register address, replacement of stale mappings, preserved adjacent/high fields, ignored-write failure, and unchanged MD mappings. It rejects the previous source. No device calibration is used in this test.

Build CONNECTIVITY-04 as a production BOOTIMG-only update retaining the installed CONNECTIVITY-03 Y2ROOT and Y2DATA. No firmware changes, factory writes, new memory ranges, or power-platform redesign. After manual installation, capture the same startup through remap, CONN/BTIF/WMT and interface readiness, then continue M5 qualification if startup succeeds. M5 remains open.

The previous CONNECTIVITY-03 BOOTIMG reproduces the crash and is not a working recovery choice. Known bootable rollback pairs remain CONNECTIVITY-02 with CONNECTIVITY-01 Y2ROOT, or accepted POWER-03 with its previous root; both require the corresponding root image and preserve Y2DATA.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
