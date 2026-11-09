---
title: "Stock console capture runbook - Innioasis Updater"
description: "Stock console capture runbook <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-stock-console-capture.html"
---

# Stock console capture runbook - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Stock console capture runbook

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Stock console capture runbook > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

[Y2E-140 research and unresolved physical gate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md) is authoritative. This procedure is prepared, not performed on Y2 serial hardware. Current installed software selects UART0; 921600 8N1 is the firmware-supported starting setting, and native SoC logic is expected to be 1.8 V. Exposed board pads, pad voltage, adapter and actual stock serial baud are not yet verified.

## Before any connection
  - Establish the exact board revision and a credible UART0 TX/GND net mapping. Record evidence references, orientation and pad identifiers. Package BGA coordinates and LK GPIO numbers are not exposed-pad labels. No blind pin probing or guessed USB accessory cable.
  - Establish the identified TX net's logic level without driving it, using a suitable high-impedance instrument and known ground. Confirm receiver absolute maximum ratings and guaranteed RX high/low thresholds for that measured level at 921600 baud. A VCC selection label alone is insufficient. Record adapter make/model/revision, driver, stable USB identity, datasheet, wiring and measurement evidence.
  - With a reviewed power/ground procedure, connect Y2 TX → adapter RX and verified Y2 GND → adapter GND only. Leave adapter TX, VCC, DTR and RTS disconnected, and do not power Y2 from the adapter. Do not use RS-232 voltage levels. Opening/configuring even a read-only tty may assert modem-control lines; the physical two-wire setup prevents these lines from reaching Y2.
  - Close other serial clients. Ensure the exact adapter is not being claimed by a modem manager or another process. Use existing host permissions and a stable `/dev/serial/by-id/...` path; this tool makes no permission/group/service changes. It never scans or opens other ports.

Write a plain-text setup record containing the points above, current Android build/boot context, capture operator/date and intended stock power-on action. The tool retains a copy and hash; it does not certify those statements. Keep device identifiers and raw logs in `evidence-private/`, not public Git.

## Bounded capture

Once the prerequisites are actually satisfied, substitute the verified device path and setup file:`python3 tools/observation/capture.py \ --device /dev/serial/by-id/VERIFIED_ADAPTER \ --setup evidence-private/stock-uart-setup.txt \ --output evidence-private/stock-uart-start-01 \ --baud 921600 --seconds 60`

The output directory must not already exist. Wait for `capture.json` to say `capturing`, then perform the separately reviewed owner-operated ordinary stock start. This program does not reboot, change boot mode, connect ADB, power the device, send serial bytes, send BREAK or alter board registers. It sets host raw 8N1, disables echo and software/hardware flow control, requests exclusive access, preserves queued bytes rather than flushing, and restores host tty attributes on exit. Duration is bounded to 600 seconds, storage to 64 MiB; defaults are 60 seconds/16 MiB. Ctrl-C retains an interrupted record. USB disconnect, empty capture or hitting the byte bound returns failure. Device/driver inability to retain requested settings also fails.

Outputs:
  - `raw.bin`: exact received bytes, never interpreted as terminal escape sequences by the tool.
  - `chunks.jsonl`: offsets, lengths and monotonic host receipt times; these are not on-wire per-byte timestamps.
  - `capture.json`: UTC capture boundaries, platform/Python, selected and resolved tty, baud/settings, byte count, SHA-256, completion/error, tool/setup hashes. `hardware_proof` remains false; receiving any bytes cannot certify a Y2 boot.
  - `setup.txt`: retained operator setup/connection evidence.

Review logs as escaped text or hex before displaying them in a terminal. Preserve raw bytes first. Hashes establish retention integrity, not a noise-free wire or source authenticity. There is no auto-baud sweep: only after safely identified wiring and evidence of a different rate should another explicit receive setting be selected. 115200 is supported for the known stock-driver fallback, not automatically tried and not accepted as the installed rate without decoding proof.

## Stock acceptance

A completed host capture is only the first check. Record identifiable, ordered LK initialization/BOOTIMG handoff and stock Linux 3.4.67 startup, with sensible text/timestamps and the expected stock boot identity. Record any stage-specific baud change; a capture of only late kernel output does not demonstrate the pre-kernel path. Keep host start preceding device power-on and document gaps, disconnections or undecodable intervals. Seek a second consistent ordinary stock capture using the same setup. Do not change BOOTIMG to test the observation channel.

This session recovered `/proc/last_kmsg` through ADB, but only a previous stock shutdown tail. That does not satisfy the serial/LK acceptance above. Until a real capture passes, Y2E-140 remains open. If pads are inaccessible, the next bounded alternative investigation is the existing bootloader UART-over-USB accessory path, with no guessed cable or live mux change.

Before any Linux launch, compare the proven controller, inherited routing and stage baud against the current UART0/IRQ51 artifact. Its earlycon preserves inherited baud and its normal console requests 921600n8. Any mismatch requires another reviewed correction and full offline validation; DEBUG_LL/decompressor output is not enabled. An early hang can still be silent.

## Host-only verification`python3 -m unittest discover -s tests/observation -v`

The PTY suite checks exact binary/control-byte capture without echo, no-data failure, truncation bounds, and disconnect preservation. These tests ran on host Python 3.14.7; Linux serial hardware and electrical behavior were not tested. The same four tests also pass on Python 3.12.14 in the locked, isolated build environment. Kernel artifact tests remain the complete separate `tools/build/build.sh` pipeline.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
