---
title: "Production Storage / Installation v1 — issue 33 - Innioasis Updater"
description: "Production Storage / Installation v1 — issue 33 <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-production-storage-v1.html"
---

# Production Storage / Installation v1 — issue 33 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Production Storage / Installation v1 — issue 33

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Production Storage / Installation v1 — issue 33 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

ACTIVE, wider qualification pending. **Storage06 internal boot and owner SSH are physically confirmed.** The former Storage03 pending-flash body is superseded by the local Storage06 source and hardware evidence.

The stock logical disk needs a 23552-sector native offset and exposes 15203328 logical sectors. Source `bea30cd5883f524a252d8b94d7e914d9d2f7cbdb` restores that translation for ordinary block reads/writes without changing the stock tables or protected-region firewall. The owner manually deployed Storage06 and then the corrected owner-key Y2DATA initialization. Authenticated SSH confirms Linux 6.18.0-y2linux-storage06, four CPUs, 954376 KiB MemTotal, internal ext4 p5 root/p7 data, no SD block device and working USB ECM/ACM. Full BOOTIMG readback and stock MBR/EBR hashes match. Existing owner key/identity are retained.

[Storage06 result and exact artifacts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fbuild%2Fy2linux-production-v1-r6-deployment.md) · [Hardware evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage06-owner%2FREADME.md) · [Addressing proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fknowledge%2Fstorage06-addressing-correction.md).

The owner explicitly authorized M4 progression and confirmed preserving this Storage06 layout. Y2LINUX-M4-01 is now built from `f2d2ac641ee67cd94cd2c57c9f5201b6e78841fc`, awaiting manual BOOTIMG-only deployment. It reuses current root/data and includes the working Storage06 BOOTIMG fallback. It introduces normal power/thermal/cpufreq/idle/suspend/RTC/ reset APIs with bounded charging inhibition. No M4 hardware success is claimed. [M4 deployment and qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fbuild%2Fy2linux-m4-01-deployment.md) · [M4 epic](https://github.com/SchulzCode/Y2Linux/issues/30).
  -  Internal Y2ROOT/Y2DATA mount and Buildroot switch_root with SD absent.
  -  Owner-key SSH, four CPUs and expected measured RAM.
  -  Stock table hashes and complete Storage06 BOOTIMG readback.
  -  Bounded scratch-write/repeat/persistence and preserving reinstall qualification.
  -  Wider protected-region/readback, rescue-negative and recovery qualification.
  -  Suspend/resume root/data integrity, display/input/audio regression tests.
  -  Controlled reboot, actual hardware-off and subsequent normal power-on under M4.

Two synthetic ext4 buddy-cache inode warnings remain recorded; the image checks report clean and the system boots. Do not turn that into an unperformed stress, power-fail or full filesystem acceptance claim. M3's narrow residual checks remain #29; USB cable reconnect #27 is deferred and does not block M4 unless it directly prevents suspend qualification. Radios and Y2PlayerNative stay deferred. The owner alone performs BOOTIMG flashing; root/data, loaders, partition tables, NVRAM/calibration and unrelated partitions are preserved in this M4 update.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
