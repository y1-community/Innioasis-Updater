---
title: "M2-USBCLK-01 — ready for owner device test - Innioasis Updater"
description: "M2-USBCLK-01 — ready for owner device test <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-usbclk-01-result.html"
---

# M2-USBCLK-01 — ready for owner device test - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBCLK-01 — ready for owner device test

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBCLK-01 — ready for owner device test > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Returned [physical photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-hardware-result.md) now confirm CLOCK RC=0/VALID=15, increasing timer IRQ counts and BEAT 50 with no reported errors. Exact flashed hash and restoration remain unreported. The original pending-test handoff below is historical.

2026-09-09. Incremental #23/#27 prerequisite under active M2 #28. Offline validated; this candidate has not been flashed or hardware tested.

The preceding [M2-PWRAP-01 photographs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-hardware-result.md) confirm CID 0x2023, VUSB 0xc000, MemTotal 22208 kB and progress through BEAT 50. The timer -61 diagnostic is a source-identified parser mismatch. M1 stays complete; M2 and #22–#27 remain open.

## Candidate and change

`/home/luca/Dokumente/Code/Y2Linux/out/m2-usbclk-01/BOOTIMG.img`

1,093,632 bytes; SHA-256: `602080eb199f3a4be30082ee114dfeb97ef414e10d8ad4acf5d239f2096cd6ec`.

Kernel `6.18.0-y2-m2-usbclk1`, screen/build M2-USBCLK-01. [Reviewed contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-probe.md): after the first sleep, reuse the proven bounded PWRAP CID/VUSB read. On success with VUSB reported enabled, cache four ordinary clock register reads: PERI_PDN0_STA, CLK_CFG_2, UNIVPLL_CON0 and UNIVPLL_PWR_CON0. Each resource is claimed and released; a refusal stops further reads and preserves a partial validity mask. No new hardware write is added; no USB MAC, PHY, calibration or DMA register is accessed. USB enumeration/ttyACM is not expected in this candidate.

PID1 now matches the DT timer IRQ action token instead of the clock-event name. Clock fields replace the previous wrapper-detail rows; PWRAP RC/VALID and CID/VUSB remain visible. Screen fallback, D08, CPU0 and AP watchdog policy persist.

## Offline validation
  - One clean pinned Linux 6.18 / Clang 20.1.8 build, no compiler warnings/errors.

All 19 selected test methods pass: actual artifact/corruption and BOOTIMG checks, D08, overlays, framebuffer bounds, emitted watchdog/time32 checks, parser, 14 QEMU ARM PID1 scenarios, 20 PWRAP and 10 clock-probe scenarios.
  - Linked snapshot is PID1-only, 72 bytes, cached before hardware access. The clock

adapter at `0xc0015794` rejects all other addresses and has one mapped read; its store targets output RAM. PWRAP command/ACK bounds are preserved.
  - Resolved config differs from M2-PWRAP-01 only in LOCALVERSION. DT source is

unchanged; initrd-end follows the 4,840-byte gzip. No RAM/DMA/packaging policy change or repeated source/ROM/recovery audit was performed.
  - [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbclk-01-layout.json) and

[iteration](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbclk-01-iteration.json) retain dimensions and identity. BOOTIMG wrappers, complete LK read tail and the 16 MiB partition bound pass. Ignored output retains ELFs, source snapshot, lock, config, logs, focused linked disassembly and SHA256SUMS. Prior images are preserved.

## Owner test and evidence to return

Use the established BOOTIMG-only test/recovery procedure. Stop observation at 60 seconds from power-on; normal terminal stage is `STOP: RESTORE ANDROID` at BEAT 50. Stock preloader/LK, partition tables and calibration remain protected. No physical-device action was performed here.

Expected: guarded screen and heartbeat, briefly `READ PWRAP / USB CLOCKS`, then continuing heartbeat. Successful probe shows `PWRAP RC:0 VALID:3` and `CLOCK RC:0 VALID:15 READ ONLY`, plus raw CID/VUSB, PERI/MUX and PLL/PWR values. The raw clock values are unknown until this test. Timer IRQ CPU0 should become a decimal count that increases between photos. A probe refusal should remain visible while heartbeat continues. An MMIO hang can freeze at the pre-probe stage; preserve the existing manual recovery boundary.

Return:
  - Selected image SHA-256, and flashed/readback identity if the existing procedure

supplies it. The displayed version identifies the build, not the flashed hash.
  - Readable full-screen photos near BEAT 10 and BEAT 50/STOP, or the last

visible stage on failure. Include CLOCK RC/VALID, all PERI/MUX/PLL/PWR and CID/VUSB values, PWRAP RC/VALID, timer count, BEAT/FRAME, uptime, MemTotal, sleep/mount status and LAST ERR. Exact transcription is also sufficient.
  - Host elapsed time from power-on and between photos, whether the USB cable

remained attached, and any freeze/reset/display change.
  - Outcome of the usual BOOTIMG-only return to the known-good system, if performed.

Validity bits 0–3 correspond to PERI, MUX, PLL and PWR. Only values whose bits are set are evidence. `-19` refuses unmet prerequisites, `-16` is a resource conflict and `-12` is a mapping failure. Clock state does not measure frequency or establish the remaining PHY/VBUS/FIFO/IRQ/DMA ownership contract.

Retained previous candidate: `out/m2-pwrap-01/BOOTIMG.img`, SHA-256 `c51102c861d65d39f5af2425ed73e9c1ba21d8adaae1b016f450a58630946ac0`. The owner-proven stock/FM restoration and M1 fallback boundaries are unchanged. This handoff stops for the owner's physical test; M3 stays deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
