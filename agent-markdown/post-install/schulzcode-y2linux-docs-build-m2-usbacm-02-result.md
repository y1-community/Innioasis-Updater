---
title: "M2-USBACM-02 — retain the failed PMIC poll - Innioasis Updater"
description: "M2-USBACM-02 — retain the failed PMIC poll <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-usbacm-02-result.html"
---

# M2-USBACM-02 — retain the failed PMIC poll - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBACM-02 — retain the failed PMIC poll

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBACM-02 — retain the failed PMIC poll > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Subsequent [owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-02-result&anchor=usbacm-02-result) shows the prompt followed by poll-5 sync-only refusal before cable attachment. The original validated handoff below is historical; USBACM-03 addresses the single-sample sync check.

2026-09-09, baseline `c066d62`, active M2 / #23 / #27 / #28. Offline validated; this replacement has not been hardware tested.

`/home/luca/Dokumente/Code/Y2Linux/out/m2-usbacm-02/BOOTIMG.img`

1,159,168 bytes; SHA-256: `4ff741513ef842fca28e6fd8cd08829c9c8c9d2e3e160da70552e06166460e20`.

Heading/build M2-USBACM-02, Linux 6.18.0-y2-m2-usbacm2.

## Why this image

The [USBACM-01 photo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md) shows successful unplugged-start PHY wake, then US:2 RC:-16 and invalid live CHRDET. This identifies a live PWRAP poll refusal before controller registration. The original candidate discards the failed WACS state, preventing diagnosis of the exact idle condition.

This image retains that snapshot through teardown and displays POLL/PW/V, WACS before/after, and G gate fields. The cached wake/PHY rows remain visible; CPU-online and mount rows are replaced only when this failure occurs. The misleading USBGUARD heading is corrected. The local live ABI is versioned and expanded to 88 bytes; the 260-byte baseline snapshot is unchanged.

The underlying busy condition is not yet fixed. There is no change to the PWRAP protocol, hardware guards/writes, USB poll/stop limits, D08 map, CPU0, packaging or recovery procedure. This candidate obtains the missing evidence while retaining the original guarded enumeration attempt if the polls succeed.

## Validation
  - One clean pinned build, no compiler warnings/errors. 15 targeted methods

and four host-capture methods pass: five production worker/status scenarios, 33 QEMU ARM PID1 paths, renderer bounds, PWRAP busy/stale/timeout and completion faults, existing wake/session/relay checks, linked relay-syscall mutations, real-artifact corruptions and BOOTIMG/D08 checks.
  - Kernel config differs from USBACM-01 only in LOCALVERSION. No added subsystem

or memory configuration. Initramfs gzip is 9379 bytes; complete LK read-tail, decompressor/initramfs bounds and 16 MiB BOOTIMG partition checks pass.
  - Linked worker review shows the 52-byte failed snapshot copied into retained

RAM before the latched error/teardown. Status dispatch checks the new magic and 88-byte size; cached baseline remains 260 bytes. The linked PMIC read transaction and read/write/delay callbacks are byte-identical to USBACM-01. The larger probe function is not byte-identical; no identity claim is made for it. Source protocol and its fault tests remain unchanged.
  - Source/artifact hashes, logs, config, ELFs, focused disassembly, source snapshot

and input lock retained in the output directory. [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-02-layout.json) and [iteration record](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-02-iteration.json). No repeated unchanged ROM/recovery provenance audit or duplicate successful build.

## Owner test
  - Use the established BOOTIMG-only procedure for the exact image above.

Start the updated [host capture tool](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md) before the boot: `python3 tools/observation/usb_log_capture.py --output out/m2-usbacm-02/capture-01`.
  - Power on with USB unplugged. Attach promptly only if `ATTACH USB CABLE NOW`

appears, then leave the cable connected for the bounded attempt.
  - If USB STOP appears, photograph the whole screen including **US/RC, POLL/PW/V,

WACS, G and bottom PHY rows**. WACS gives full hexadecimal before/after words; G reports MUX, WRAP, channel and init low bytes, and full arbitration. If POLL/WACS/G are absent, retain the whole screen to locate another failure.
  - If enumeration proceeds, retain the capture directory. Expected LOG1 header

is now `Y2LOG1 M2-USBACM-02`; use the updated host tool with this image.
  - Keep the existing 60 seconds from power-on limit and manual Android

BOOTIMG restoration. The USB active deadline remains 50 seconds; no reconnect or connected-start recovery is added. Record cable timing and any freeze/reset.

USB logging and M2 exit remain blocked. M1 stays complete; #23/#27/#28 stay open. M3/audio/application work is still deferred. Original USBACM-01 image and owner photo are retained; no physical operation was performed to prepare this update.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
