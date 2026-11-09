---
title: "M2-INPUT-01 — GPIO navigation through evdev and USB logs - Innioasis Updater"
description: "M2-INPUT-01 — GPIO navigation through evdev and USB logs <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identit"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-input-01-result.html"
---

# M2-INPUT-01 — GPIO navigation through evdev and USB logs - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-INPUT-01 — GPIO navigation through evdev and USB logs

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-INPUT-01 — GPIO navigation through evdev and USB logs > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, baseline `8ebc800`. Offline validated; physical input test pending. The [donor audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md) and [scope review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23donor-adoption-and-gpio-input-scope--baseline-8ebc800&anchor=donor-adoption-and-gpio-input-scope--baseline-8ebc800) supersede the old rigid foundation queue. M1 complete, M2 active/exit blocked.

Candidate: `out/m2-input-01/BOOTIMG.img`, 1,204,224 bytes. SHA-256: `05c6f33d7fadb75c9bc5d8cc4a23aed1a5dcc79cf6b4fe735ce9006906290d37`. Build/header M2-INPUT-01; Linux 6.18.0-y2-m2-input1.

## Implemented slice

Donor GPIO register layout and navigation wiring feed a small standalone, input-only GPIO provider under the existing diagnostic overlay. It claims `10005000+1000` and exposes only GPIO6/7/9/10/54 via DT reserved ranges. Reads DIR/DIN and logs inherited mux/level on request; refuses output-configured pins. No GPIO, mux, pull, EINT, clock, rail or DMA write is added. It does not claim general MT6582 pinctrl/EINT support. Chris Hendrickson's original source/commit and GPL licensing are retained in the adapted source and donor manifest.

Upstream v6.18 `gpio-keys-polled` polls at 20 ms and provides ordinary evdev events for left/back/right/playpause/enter. These mappings are donor claims awaiting verification on this older board. No wheel rotation, volume or power key is implemented by this candidate.

PID1 searches event0–7 by the exact device name, rejects ambiguity, reads the sysfs major/minor and verifies the opened device with EVIOCGNAME. It records the five initial key states with EVIOCGKEY, then drains up to 64 events per heartbeat without blocking. `INPUT KEY sequence code value` and `INPUT SYN sequence sec usec` go into the existing retained/live LOG1 relay; SYN_DROPPED, malformed reads and device errors produce `INPUT ERROR` and stop input collection. Missing input does not prevent heartbeat/USB. The build row shows event count or input error; all USB/supply failure fields remain available. Holding a key before the open is reported as INITIAL state, not invented as a new press.

Canonical USB controller/session/clock/PWRAP source is byte-unchanged from USBACM-04, which preserves the initial attachment path and adds the still unqualified bounded reconnect. USBACM-03 remains the physically proven fallback; USBACM-04's original robustness image/tool remain retained. This input test does not qualify reconnect. D08/CPU0, early watchdog stop, guarded framebuffer, stock loaders, BOOTIMG packaging and the original 60-second power-on limit remain.

## Validation

One clean kernel build, no compiler warnings/errors. Configuration review caught that the MediaTek architecture already selects the pinctrl core; the fragment now explicitly reflects it. No MT6582 pinctrl implementation is enabled. Resolved additions are input/evdev/polled keyboard, GPIOLIB/OF_GPIO and the 8250-selected serial GPIO helper; there are no modem/radio/MMC/I2C/EINT/CMA or memory-policy additions. GPIO userspace write interfaces remain disabled.

The first complete package failed the ARM evdev test, which caught array-size versus event-size mistakes in batch validation/counting. Retained rejected output: `out/m2-input-01-rejected-evdev/` (do not flash). The unchanged kernel build was retained; corrected PID1, DT and package were rebuilt. The final candidate passes 29 build-suite tests and 12 observation tests, including 16 ARM input scenarios, all 169 GPIO bank/direction cases plus out-of-range refusal, 34 ARM PID1 scenarios, existing USB/relay lifecycle/fault regressions and corrupt-artifact/layout tests. No duplicate successful kernel build.

Emitted ARM review shows bounded GPIO offsets, input-direction refusal and ordered MMIO loads only; no GPIO MMIO stores. Expected GPIO/polled-key/evdev symbols are linked, and mknod/read/ioctl/close use the existing real syscall implementations. Initramfs gzip: 10,760 bytes. Full current D08 reservation, decompressor/DT/initramfs and LK read-tail/16 MiB BOOTIMG checks pass. [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-input-01-layout.json), [iteration/source and artifact hashes](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-input-01-iteration.json). Output retains all 75 implementation/tool/test source files, config diff, ELFs, disassembly and test logs. No unchanged ROM/recovery/source-tree re-audit.

## Owner hardware test

The assistant has not flashed or written any physical device. Flash **only BOOTIMG** using the existing manual SP Flash Tool procedure and the exact image hash above. Preserve the known restoration path and restore Android within 60 seconds from power-on. No Y2 was attached during host visibility checks.

Start the existing host capture tool before booting the candidate:`sudo python3 tools/observation/usb_log_capture.py \ --build M2-INPUT-01 --output out/m2-input-01/capture-01`

Use host execution with tty access; `sudo` is needed only if the local account lacks it, as in the earlier inspected host. The tool discovers the actual ACM tty through USB/sysfs identity; it does not assume ttyACM0. The explicit build selects `Y2LOG1 M2-INPUT-01`; old USBACM-03/04 capture remains supported.
  - Boot unplugged; attach at `ATTACH USB CABLE NOW` and keep USB attached.
  - After logging starts, press/release Prev, Menu, Next, Play, Select, in

that order, one at a time. Hold each roughly half a second, with a short gap. Repeat once if time permits; avoid long power-key holds in this input trial.
  - Retain the entire capture directory, including on error. If enumeration

fails, retain the full diagnostic screen showing build, US/RC and INPUT RC.

Expected codes: 105, 158, 106, 164, 28. Each press should yield value1 and release value0 with SYN records; verify physical labels rather than assume the mapping. Review the GPIO request/mux messages, `INPUT OPEN` and INITIAL states, event sequence/timestamps, sustained PID1 beats and kernel warnings/deferred probes. Any `INPUT ERROR`, `GAP`, unexplained missing transition, stuck key, heartbeat stall, USB error or unsafe state fails the relevant test. End capture and restore within the existing limit. A capture exit0 only verifies collection; hardware success requires reviewing its contents. #24/#27/#28 remain open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
