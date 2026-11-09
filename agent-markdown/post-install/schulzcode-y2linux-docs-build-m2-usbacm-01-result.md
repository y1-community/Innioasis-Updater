---
title: "M2-USBACM-01 — ready for owner enumeration test - Innioasis Updater"
description: "M2-USBACM-01 — ready for owner enumeration test <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-usbacm-01-result.html"
---

# M2-USBACM-01 — ready for owner enumeration test - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBACM-01 — ready for owner enumeration test

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBACM-01 — ready for owner enumeration test > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Subsequent [owner photograph](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md) shows successful unplugged-start PHY wake, then US:2 RC:-16 from a live PWRAP poll. No enumeration result. The original handoff below is retained as history; M2-USBACM-02 adds the missing failed-poll evidence.

2026-09-09, baseline `d9c2c98`, #23/#27 under active M2 #28. Offline validated; no physical device operation or enumeration result.

`/home/luca/Dokumente/Code/Y2Linux/out/m2-usbacm-01/BOOTIMG.img`

1,159,168 bytes; SHA-256: `d2d1f8cbbaa23ffcbdeddb317db7a8e62bc21deca9ebebc564c9b55a5590aedd`.

Screen/build M2-USBACM-01, Linux 6.18.0-y2-m2-usbacm1. [Hardware/software contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-enumeration.md), [host capture procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md).

## Combined attempt

This replaces the proposed extra USBGUARD-only test with one guarded attempt at controller/session ownership → upstream MUSB peripheral PIO → one g_serial CDC ACM → retained kernel/PID1 and live heartbeat logs. The CHRDET result already answered the immediate presence question. It did not establish that the PHY's connected-start state can be recovered; the candidate therefore starts unplugged.

The initial wake guard remains unchanged. Once it passes, the screen asks for attachment. Fresh supply/clock/PHY/DMA checks gate the exact LK/FM digital device-session sequence. FIFO readback gates connection. The original screen snapshot and signed failure stage remain available if any step refuses/fails. No PMIC writes, host VBUS sourcing, analog calibration writes or DMA transfer. This is an enumeration attempt, not a promise of hardware success.

## Validation
  - One clean pinned Linux 6.18/Clang 20.1.8 candidate build; no compiler warnings

or errors. 23 full-suite methods, **one additional linked-syscall mutation method, and eight observation methods** pass. This includes 30 QEMU ARM PID1 paths, production session/takeover guards, 49 existing wake scenarios, and host/ARM relay fault, partial-write, overflow and replay cases.
  - The complete real-artifact corruption suite rejects changed USB IRQ polarity,

host mode and PIO configuration as well as the existing D08/package faults. Linked MUSB/EP0/ACM/serial implementations and ARM mknod14/lseek19/ioctl54 are present, not ENOSYS; sleep162 still resolves to nanosleep_time32. No linked USB DMA engine, host setup or sibling MediaTek adapter. Resolved USB/selected dependency configuration and exact experimental DT node pass validation.
  - Linked access review retains the PHY6c/6d-only byte-store callback, DEVCTL

SESSION/HR suppression, error-dependent SOFTCONN gate, MAC interrupt widths/ W1C path, second eight-channel inactive-DMA sample, bounded worker and IRQ cutoff. Source hashes match the built diagnostic/relay sources. This is an offline software/access check; FIFO/IRQ/USB electrical behavior awaits hardware.
  - D08 still describes 24MiB+512KiB, CPU0 only. Kernel resident span, decompressor

workspace and initramfs remain within its unchanged limits; no RAM expansion. Initramfs gzip 9175 bytes. Complete LK read-tail and 16MiB BOOTIMG bounds pass. See [layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-01-layout.json) and [iteration record](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-01-iteration.json).
  - Output retains config/ELFs/build/test logs, focused disassembly, source snapshot,

input lock, hashes and host capture tooling. No duplicate successful build or repeated unchanged Linux/ROM/recovery provenance audit.

## Owner test — stop here
  - Use the established BOOTIMG-only procedure for this exact image. Start the

[host capture tool](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md) before the test boot.
  - Power on with USB unplugged. At `ATTACH USB CABLE NOW`, attach the data

cable to this Linux PC promptly and leave it connected.
  - Expected success: `US:6 RC:0`, increasing USB IRQs, `USB CONFIGURED`, a host

ttyACM port and a capture beginning `Y2LOG1 M2-USBACM-01`, followed by retained kernel/PID1 messages and increasing beats. A stage5/ready stage alone is not proof.
  - Keep the original 60 seconds from power-on limit and manual BOOTIMG

restoration boundary. USB disconnects at the 50s active-window deadline or first detach/error; do not reconnect during this initial experiment.
  - Return `out/m2-usbacm-01/capture-01/` and same-boot screen photos if practical,

near BEAT 10 and late in the window. If USB fails, photograph the complete screen including US/RC/IRQ/D, CHR/PW/CLK, LAST ERR and bottom raw/wake rows. Note cable timing and any freeze/reset; do not extend the test window.

Retained untested diagnostic fallback: [M2-USBGUARD-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbguard-01-result.md). Its connected-start test is optional follow-up evidence, not required before this unplugged-start attempt. The hardware-tested CHRDET image remains retained; its connected-start refusal is documented, not a successful connected wake.

#23/#27/#28 remain open. Physical enumeration, log continuity, late-open/no-reader and controller reconnect qualification are still outstanding. M1 stays complete; M2 exit criteria are unchanged, and M3/audio/Y2PlayerNative remain deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
