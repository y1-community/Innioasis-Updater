---
title: "Current non-root system baseline - Innioasis Updater"
description: "Current non-root system baseline <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-stock-system-baseline.html"
---

# Current non-root system baseline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Current non-root system baseline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Current non-root system baseline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Date: 2026-09-08. Task: [Y2E-105](https://github.com/SchulzCode/Y2Linux/issues/2). Capture: `20260908-stock`. One authorized USB target was selected explicitly for all remote commands; its serial and full properties remain private. No device state was intentionally changed.

## Method and status

Host ADB: 1.0.41, platform-tools `37.0.1-15733141`, `/opt/android-sdk/platform-tools/adb`. Initial sandbox USB/ADB access was denied; the host-side permission retry succeeded. This is distinct from device-side access denial. Commands were captured separately with a 15-second host timeout. The first status-marker attempt failed because the device lacks `printf`; its diagnostic output was retained. The compatible form was `<read command>; y2_rc=$?; echo __Y2_REMOTE_EXIT__=$y2_rc`. Both host status and remote marker are retained. Device clock is recorded separately; host UTC anchors the session.``````````````````````````````````

| Evidence | Result | Scope |
| --- | --- | --- |
| id | CONFIRMED uid 2000 shell, SELinux context u:r:init_shell:s0 | Non-root only; no privilege changes attempted. |
| /proc/version | CONFIRMED Linux 3.4.67, GCC 4.7, SMP PREEMPT, build timestamp June 1 2026 | Version string alone does not exclude a patched kernel. |
| /proc/cpuinfo | CONFIRMED MT6582, Cortex-A7 part 0xc07, ARMv7, NEON/VFPv4 | Revision string 0000 is not a physical PCB-revision identification. |
| Selected properties | Android 4.4.2/API 19, model/board/device Y2, ro.hardware=mt6582 | Current runtime evidence supersedes assumptions about hardware property resolution. |
| Build identity | Y2/Y2/Y2:4.4.2/KOT49H/1786599642:user/test-keys, display Y2-v1.0.0 | Device is not certified stock. Exact installed boot/system image hashes and installation lineage remain UNKNOWN. |
| Security/USB properties | secure=1, debuggable=0, adb.secure=1; mass_storage,adb | Consistent with secure non-root ADB; does not uniquely identify an image. |
| /proc/meminfo, interrupts, iomem, CPU topology | COLLECTED | Evidence available for later memory/IRQ analysis; do not treat an incomplete reservation map as boot-ready. |
| /proc/modules | EMPTY successful observation | No loadable modules listed at capture; built-ins remain possible. |
| /proc/cmdline, dmesg | DENIED, remote 1 while ADB host 0 | No root/su workaround. |
| uname -a | UNAVAILABLE, remote 127 while ADB host 0 | Use the separately captured proc version. |
| config.gz and exported DT paths | UNAVAILABLE, remote 1 | No exported tree/config; embedded config/DT remains an offline question. |
| Module/firmware directory metadata | PARTIAL; aggregate remote 1 | /system paths list entries while /vendor/lib/modules and /vendor/firmware are absent. Do not discard the successful portion. |
| dumpsys battery | COLLECTED but internally conflicting | Repeated status/present/level fields disagree (100/50 and true/false). Do not infer battery health or adequate recovery power from this service alone. |

Firmware names include `WIFI_RAM_CODE_MT6582`, other Wi-Fi variants, `WMT_SOC.cfg`, MT6572/82 patch blobs and an `mt6627` directory. `/system/lib/modules/wlan.ko` points to `wlan_consys_mt6582.ko`; the listing alone does not establish that the target exists or is loaded. No firmware was executed and no radio state was toggled.

Mount evidence shows read-only `/system`, writable `/data`, `/cache`, `/protect_f` and `/protect_s`, plus mounted internal and removable-card media. USB composition does not prove storage is safely quiesced for a raw snapshot. Protect/calibration candidates are mutable mounted filesystems at this point.

## Review decision

The access baseline is complete, including denials and missing exports. The target is a non-root stock-family Android system; exact installed provenance remains unknown. This is sufficient for Y2E-110 to read partition metadata only. It is insufficient for raw partition acquisition, any recovery write or Linux boot. Battery service inconsistency is recorded as a separate observation for later passive power investigation.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
