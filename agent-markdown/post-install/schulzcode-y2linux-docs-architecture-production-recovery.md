---
title: "Production v1 restoration - Innioasis Updater"
description: "Production v1 restoration <!-- knowledge-base-scope: historical-design-/-runbook -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-production-recovery.html"
---

# Production v1 restoration - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Production v1 restoration

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Production v1 restoration > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Keep the working SD and `out/y2linux-m3-audio-02/BOOTIMG.img` unchanged. Its 4816896-byte image SHA256 is b9dbf6b528e4afbee2a5ffb2fc65df7f6a076564e92960332e24cee3809b5842. Owner-proven BOOTIMG-only recovery remains valid; no new full-ROM restore test was performed. No bootloader, table or protected-data write belongs in recovery.

## Tool and stock source

SPFT: `/home/luca/Downloads/SP_Flash_Tool_v5.2032_Linux/flash_tool`, v5.2032.00 /5.2032.00.sn100, SHA256 d618e7d08ba5a4020038921a95336a3805a4b2cf17a374fd308cc5299ea7d9d8. Bundled DA `MTK_AllInOne_DA.bin`, SHA256 46cd175d7556e6e80b13f6a70827c6931a5dfa25a09c3cc50e75ba7ff9327618. Use the owner's established connection/power procedure; its precise button/timing sequence is not invented here. A normal SSH/ECM connection is not a DA session.

Original directory: `/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/`. Only recovery-source paths refer to that historical Android project; this firmware is built by and for SchulzCode/Y2Linux. All three overwritten partitions have verified factory restoration sources in manifest.json (size/hash rechecked for this package). They are not exact backups of installed personal Android state.

| Target | Factory source | Physical EMMC_USER start | Span |
| --- | --- | --- | --- |
| BOOTIMG | boot.img | 0x01d80000 | 0x01000000 |
| ANDROID | system.img (stock sparse ext4) | 0x05180000 | 0x33400000 |
| USRDATA | userdata.img (stock sparse ext4) | 0x40380000 | 0x32000000 |

Stock scatter SHA256: e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e. Verify original sources against manifest.restoration_sources and retain an independently accessible copy before writing. To restore personal Android data, retain a consistent full USRDATA readback before install. Factory userdata only restores factory state; NVRAM/calibration preservation is a separate requirement.

## Return immediately to SD development Linux

Load the original stock scatter in SPFT, Download Only. Deselect every row, then select BOOTIMG only and point it to the hashed AUDIO-02 image above. Do not use original scatter default selections. Flash by the owner's proven manual sequence. Read back EMMC_USER0x1d80000, length0x1000000; hash the first4816896 bytes against AUDIO-02. Insert the preserved working SD and boot: AUDIO-02 disables internal eMMC and resolves removable Y2ROOT. Internal Y2ROOT/Y2DATA are retained. This restores the development environment without restoring Android or wiping data.

## Restore stock Android factory userspace

With verified original FM sources available, load the original scatter, Download Only, deselect all, then select BOOTIMG→boot.img, ANDROID→system.img and USRDATA→userdata.img. These are the only three selected rows. This destroys Y2Linux root and Y2DATA; export persistent data first if needed. Restore a private preinstall USRDATA backup instead only after confirming that SPFT accepts its raw ext4 representation; do not improvise wrappers or offsets.

Never select PRELOADER, UBOOT/LK, MBR/EBRs, RECOVERY, NVRAM, PRO_INFO, PROTECT_F/S, SECCFG, SEC_RO, MISC, LOGO, EXPDB, CACHE, FAT or BMTPOOL. Do not select Format All, Firmware Upgrade or Write Memory. Abort any request to format, security mismatch, table mismatch or unexpected address/identity.

Read back the written ranges before Android boot; use raw prefix comparison for boot.img and compare material RAW/FILL chunks of stock sparse images against their physical expanded offsets. Stock DONT_CARE chunks have no prescribed hash; a factory sparse image's file SHA256 is not an eMMC readback hash. The corrected Y2Linux raw ext4 images avoid that ambiguity by defining every written byte. Recompare protected/table before/after captures. Then check actual Android UI, storage/audio/device-specific behavior; a green SPFT tick is insufficient.

Stock RECOVERY remains untouched, but its automatic Android filesystem repair, wipe and update functions are not a Y2Linux recovery mechanism. Use SPFT and known images rather than invoking Android wipe menus on the new filesystems.

## Missing/broken Y2ROOT or Y2DATA

The production rescue waits for the exact internal filesystem identities and geometry, validates layout/schema and executable availability, and logs errors over ACM while retaining PID1 if those checks fail. It never falls back to SD, formats storage or schedules automatic reboot. `panic=0` prevents timed panic reboots in the rescue; init sets `panic=10` only at the root handover (a failed handover restores 0), so the running system restarts 10 s after a kernel panic. The final switch_root/exec assumes the validated BusyBox init remains executable; post-handover crashes/hardware faults are not repaired by this rescue. No claim is made that USB observes a crash before gadget initialization.

Reflash only the failed allowlisted image using this release's matching profile, preserving USRDATA unless explicitly restoring/initializing data. Torn BOOTIMG may prevent rescue starting; stock loader + SPFT remains the recovery path.

Storage04 adds `y2.rescue=1` as an explicit production command-line entry and `y2-status storage|usb|audio|power` in both environments. The observer is optional instrumentation; platform drivers and display startup do not depend on it. The retained AUDIO-02 fallback is historical SD firmware, not a charging remedy: Y2Linux charging management and off-state power behavior remain unqualified.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
