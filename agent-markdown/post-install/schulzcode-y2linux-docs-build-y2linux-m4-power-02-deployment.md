---
title: "M4-POWER-02 integrated physical qualification - Innioasis Updater"
description: "M4-POWER-02 integrated physical qualification <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m4-power-02-deployment.html"
---

# M4-POWER-02 integrated physical qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M4-POWER-02 integrated physical qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M4-POWER-02 integrated physical qualification > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Source `83d475ef71a3dd84f6e3cc483a7637b13520e4f7` builds one integrated production hardware candidate. [Exact build receipt and hashes](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-power-02%2FREADME.md). M4 remains ACTIVE/PARTIAL. No new hardware pass is implied by compilation.

Latest result, 2026-09-15: [fresh authenticated inspection and full image-length readback](../hardware-evidence/2026-09-15-m5-entry/README.md) match this BOOTIMG. PC charging subsequently stops at 4.200073 V with latched voltage fault `0x8` and remains off after the reading falls. This is separate from the earlier OVP failure. SPM entries/resumes remain zero on the inspected boot; M4 is not ready to close or serve as a qualified M5 entry. No new deployment is requested.

Subsequent owner result, 2026-09-14: wall charging showed animation without recovery, requiring stock recharge. After Linux reinstall, [read-only SSH evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-14-m4-power02-charge-fault%2FREADME.md) confirms POWER-02 starts 450-mA charging from a recognized PC source, then stops after about one second with latched OVP fault 0x10. Charging qualification has failed; the exact detector and earlier wall-session cause remain unresolved. The sequence below is the original candidate handoff, not a successful result or a new request to repeat flashing. The prior 70-mA gain baseline also failed.

2026-09-15 runtime workaround:[two physical USB reconnects now pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-15-usb-reconnect%2FREADME.md) with the MUSB child's runtime-PM policy held at `on`. The matching change is installed in `/etc/init.d/S20y2-usb` and scoped to POWER-02; it does not require flashing. This is a workaround, not a kernel fix. Added idle consumption is unmeasured. The short DCP wall test had no fault, but the prior charging failure and full M4 acceptance remain unresolved. A bounded persistent recorder now preserves diagnostics when a restart is necessary.

## Deploy only BOOTIMG

Package: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m4-power-02/`. Use its `MT6582_BOOTIMG_only_scatter.txt` in the established SP Flash Tool. Select Download Only, BOOTIMG only, and the package's `BOOTIMG.img`. Keep PRELOADER, LK/UBOOT, all partition tables, recovery, root/data and NVRAM unchecked. Never select Format or Firmware Upgrade. The user's authorization covers this integrated M4 pass; no bootloader modification is needed.

After a successful flash, disconnect USB and leave the Y2 off. Connect a normal wall charger without pressing Power. Record the actual screen text and whether the screen blanks automatically. Expected: a charging activity display for eight seconds, then darkness; a brief Power press shows status again. A fresh two-second Power hold and release requests normal boot only once voltage has been at least 3.4 V for three samples. Do not hold for the hardware emergency reset interval. Charging may continue offline indefinitely through normal termination/hold/recharge, without automatically starting Buildroot.

At low battery, remain in offline charging. No SSH/ECM is expected there. Minute-spaced kernel records preserve voltage, source, programmed limit, watchdog service, PMIC temperature, raw BATON/ISENSE and charge state for later retrieval after deliberate normal boot. No development process controls charging.

The prior kernel is preserved at `fallback/BOOTIMG-previous.img`. It restores M4-CHARGE-01 and its known limitations, including inhibition below 3.4 V. It must not be represented as an empty-battery recovery path.

## One coherent physical session

The agent uses `tools/development/qualify-m4-power.sh` for explicit normal-API inventory, root/data sentinels, bounded OPP testing, audio, suspend and power phases. Both host shell and the actual production ARM BusyBox syntax check pass. It is a qualification helper, never a charger/watchdog or production PM owner.
  - Demonstrate wall-source offline entry, timed blanking and brief status input.

Then perform deliberate normal Power-on with the source still connected. Retrieve boot metadata and the retained offline charge history. Establish sustained gain before heavy load or repeated power-transition tests.
  - Test PC and power-bank source classification/charging, including off-state

insertion without normal userspace. Check the PC offline ACM-only descriptor and absence of ECM/SSH. Wall/bank charging must not require enumeration.
  - In normal userspace retain boot ID, RTC, root/data sentinels, complete power,

thermal, clock, regulator and device inventory. Use normal interfaces only. Check fresh thermal acquisition against actual response before any load test.
  - Qualify each 598/747.5/1040-MHz OPP repeatedly at the retained 1.15 V, bounded

load and cooling constraints; verify WFI usage. Do not call fixed-voltage frequency scaling voltage DVFS.
  - Verify charger-active suspend inhibition while screen-off charging continues.

After charging is safely inhibited or disconnected, test s2idle fallback, then SPM deep suspend with Power and RTC wake. Require an unchanged boot ID, actual `cpu_resume` counter advancement and no PCM debug fault. Record real duration and voltage behavior; no calibrated standby current is available.
  - After resume test display/backlight, Power, volume, navigation/wheel, optional

external SD, root/data sentinels, ALSA/CS43131 and the proven 44.1-kHz playback. No mounted-filesystem fsck, raw storage changes or emergency reset cycles. Wider M3 48-kHz/channel/repeat tests and #27 remain separate unless blocking.
  - Set RTC through its standard API using the recorded host UTC time, preserving

any unrelated alarm and all RTC spare/boot words. Check reboot persistence, suspend alarm, deep wake, and hardware-off persistence where supported.
  - Qualify ordinary reboot and actual BBPU hardware poweroff with the cable

removed, subsequent ordinary Power boot, then poweroff while connected returning to offline charging. Offline unplug must turn off; reinsertion must return offline. A black screen alone is not proof of power removal.
  - Retain the final-current termination and recharge evidence, including the

unattended-by-userspace offline path. Low-voltage source entry must show actual recovery; crossing 3.4 V must never automatically boot the full OS.

Every physical result goes into the [current M4 acceptance matrix](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-end-user-power.md). Unrun, failed or unobservable cases remain open. Neither simulated charger completion nor a host suspend-sequence test closes a hardware gate. M5 is not started during this session.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
