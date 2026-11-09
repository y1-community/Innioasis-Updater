---
title: "M2-PHYWAKE-01 — build and owner test handoff - Innioasis Updater"
description: "M2-PHYWAKE-01 — build and owner test handoff <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-phywake-01-result.html"
---

# M2-PHYWAKE-01 — build and owner test handoff - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-PHYWAKE-01 — build and owner test handoff

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-PHYWAKE-01 — build and owner test handoff > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, active M2 #28, USB prerequisite #27/#23. Superseded test status: the owner has now supplied a successful [same-boot physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-hardware-result.md). The original pre-test handoff below is retained as history. Previous [USB-state photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-hardware-result.md) confirm reads and BEAT 50 without errors; they identify PHY suspendm forced low.

## Candidate

`/home/luca/Dokumente/Code/Y2Linux/out/m2-phywake-01/BOOTIMG.img`

1,097,728 bytes; SHA-256: `d68c8fbc56721c7aa1fda5b3e321a9aff5876661aac857505864e28d8924793a`.

Screen/build M2-PHYWAKE-01, Linux 6.18.0-y2-m2-phywake1. [Exact contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md).

This candidate adds one conditional volatile PHY write: 0x1121086a, 04→00 to release force_suspendm. It first requires the known supply/clock state, disconnected B-device MAC, observed HWVERS, zero DMA controls and reviewed PHY mode controls. A fresh 6a check precedes the write. It then waits 800 us and records PHY state, calibration-related bytes and MAC POWER/DEVCTL.

No analog trim/calibration, PMIC/clock, VBUS-force, MAC-connection, interrupt or DMA-control write is added. It does not run the full vendor PHY recovery sequence. USB enumeration/ttyACM is not expected. A successful force-bit release alone does not establish a ready PHY, physical VBUS or complete controller contract.

## Validation
  - One clean pinned Linux 6.18 / Clang 20.1.8 build, no compiler warnings/errors.

All 21 top-level test methods and four host-PTY observation methods pass. Included production scenarios: 48 PHY wake, 37 USB state, 20 PWRAP, 10 clock, plus 20 QEMU ARM PID1 cases. Refusal, read failures, stale force state, changed trims, unexpected connection/host state and continued heartbeat are covered; fixture outcomes are not physical evidence.
  - Emitted cached snapshot is PID1-only and 256 bytes. Release/settle are inlined:

fresh read c0015b40, comparison with 04 c0015b4c, sole new MMIO byte write c0015b64, followed by the correct 800-us const_udelay argument. Seven mode reads precede the write; twelve bounded readbacks follow. No retry/rollback.
  - Resolved config differs only in LOCALVERSION; DT source is unchanged. D08,

CPU0, watchdog instructions, framebuffer guard and linked time32 syscall pass. No memory/DMA/packaging policy change; no duplicate build or unchanged full source/ROM/recovery re-audit.
  - [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-phywake-01-layout.json) and

[iteration](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-phywake-01-iteration.json) retain dimensions/identity. Gzip is 5901 bytes, resident kernel [0x80008000,0x8029f5b0), initramfs ends 0x8400170d, decompressor workspace ends 0x80390790. Complete BOOTIMG wrappers, LK read tail, D08 and 16 MiB partition bounds pass.

Output retains source snapshot, lock, ELFs, config, logs, disassembly and hashes. No physical Y2 command or flash was executed. Stock preloader/LK, partition tables and persistent calibration remain protected.

## Owner test and exact evidence

Use the established BOOTIMG-only procedure, maximum 60 seconds from power-on. Expected: first heartbeat, briefly `CHECK PHY / RELEASE SUSPEND`, then continuing progress to BEAT 50 / `STOP: RESTORE ANDROID`. A bus hang may freeze at the pre-probe stage; use the existing bounded manual recovery procedure.

Successful release shows:
  - `USB RC:0 VALID:001FFFFF`, `PW:0 /3 CLK:0/15`.
  - `WAKE:0 W:1 V:7F/FFF`, followed by post-read MAC `P:` and `D:` values.
  - `6A:04>00` and seven post-read PHY68..6e bytes, packed as two hex digits each.
  - `CTL:` pre-read PHY1a/1d/22/63 values.
  - `TRIM:` pre/post pairs for PHY00/05/15; each pair should match.
  - Increasing heartbeat/timer counts and `LAST ERR: NONE`.

A refusal can show `WAKE:-19 W:0`; this is useful evidence of an unmet guard, not permission to force a value. -16 is a stale-force/resource refusal, -12 a mapping failure, -5 a readback/trim/mode mismatch. W states whether the sole write occurred. V is before/after validity: 7F means all seven control reads; FFF means PHY68..6e, trims00/05/15 and POWER/DEVCTL all read back. Zero fields without validity are not evidence. All observations are cached once per boot.

Return readable full-screen photos near BEAT 10 and BEAT 50/STOP, or the exact last stage on failure. Include all bottom four rows, USB/PW/CLK status, timer/uptime/MemTotal, mount/sleep status and LAST ERR. Also report selected image hash (flashed/readback identity if available), host elapsed time, whether the USB data cable stayed attached to the Linux PC, any reset/freeze and the usual BOOTIMG-only restoration outcome if performed.

Retained previous candidate: `out/m2-usbstate-01/BOOTIMG.img`, SHA-256 `8c1f701b61a1adb70b1377071e6cb885cda989a422fd75d626cd5c7da5bdb5e7`. Owner-proven stock/FM restoration and M1 fallback boundaries are unchanged. Stop here for the physical test. #23/#27/#28 stay open; M3 remains deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
