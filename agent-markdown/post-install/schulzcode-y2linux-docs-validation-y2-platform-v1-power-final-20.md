---
title: "POWER-FINAL-20 — reclaim the never-initialised UART1 clock - Innioasis Updater"
description: "POWER-FINAL-20 — reclaim the never-initialised UART1 clock Status: INSTALLED, FIRST BOOT CHECKED 2026-10-13. Package out/y2linux-platform-v1-power-final-candidate-20/ fal"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-20.html"
---

# POWER-FINAL-20 — reclaim the never-initialised UART1 clock - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-20 — reclaim the never-initialised UART1 clock

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-20 — reclaim the never-initialised UART1 clock

Status: INSTALLED, FIRST BOOT CHECKED (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-20/` (fallback = 19), receipts `out/deep-sleep-final/build20-receipts/`. BOOTIMG `1ffdb4a2d024cf2d1c8554c518b859b2e7fe8a56186aefea4f8cbb35e4e93c55`, Y2ROOT `98ffdca9c2595f245c0ad94b25c9e89c99796f2234324fbd22c994c046859548`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-20`, kernel `6.18.56-y2linux-platform-v1-power-final-20`, root `2026.08-platform-v1.50`, release `1.0.0-platform-v1-power-final-candidate.20`; Linux `c853915` on `main`, Reborn unchanged (`217e28d`). Flash BOOTIMG + ANDROID only with `MT6582_preserve_data_scatter.txt`, Download Only. Scope audit: "POWER-FINAL-20 UART1 clock reclaim scope audit" in the [roadmap gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## Why

After 19 every INFRA clock gate matches stock at sleep entry and INFRA still stays powered (archive 116). The last peripheral gate that differs is PERI_PDN0 bit 17, UART1: stock gates it in every scenario checklist (idle, deep idle, suspend). UART1 has no Linux owner. 19's boot handoff showed `UART1 lcr=0 ier=0 lsr=0x0 dma=0 reason=tx_not_drained retained=1`: an all-zero, never-initialised UART was taken for an undrained transmitter, so its clock stayed on from the bootloader for the whole uptime (UART2/3 read the idle 0x60 and were gated).

## What 20 changes
  - `y2_unused_uart_never_initialised()` (`idle-clock-policy.h`): an all-zero LCR/IER/DMA/LSR set is not busy; the CCF

unused-clock handoff reclaims UART1 at boot like UART2/3. Any non-zero field keeps the previous rule. `clocks.unused_handoff` reports `reason=never_initialised retained=0`.
  - Every UART1 register read in the kernel was already conditional on its clock being on.
  - Expected side effect: the deep-idle UART owner check no longer sees an unknown UART1.

## Tests

Locked-container production suite: 689 cases, exit 0 (the new assertions extend `test_cpu_idle_completion`). Package validation, ELF, installed ARM, privacy and inventory PASS.

## Hardware results

First boot after the flash (boot `53bad0d8`), USB networking did not work. The gadget enumerated and configured (stage 6, `usb0` up with 10.42.0.1), the Y2 received 36 packets but sent none (`usb0 tx_packets=0`, DMA completions 10/10, no unmask loss); the host saw bulk-OUT transmit timeouts (`NETDEV WATCHDOG`, 83 TX errors, ARP for 10.42.0.1 FAILED). Wi-Fi ping answered. The owner turned the player off and on (clean shutdown) and replugged; the next boot `6fd4d362` worked at once. A milder version occurred on 18's first check (first SSH timed out, 1 of 2 pings answered), so it is not attributed to 20's change; cause open (first connection after a flash). Evidence: archive `out/deep-sleep-final/evidence/20261013/117-power20-first-check/` (rows of boot `53bad0d8` in `sleep-diagnostics.jsonl`).

Working boot `6fd4d362` (archive 117): kernel `-power-final-20`, taint 0, `application_ready` 40.4 s; `clocks.unused_handoff`: `UART1 ... reason=never_initialised retained=0`; `uart1_gate_now=1`; awake PERI_PDN0 `0x2eed3fd` (bit 17 set); `uart_sleep_owner_ready=1` (the deep-idle UART owner check no longer refuses); all 16–19 features armed; Wi-Fi, Bluetooth, USB (archive taken over it), charging.

## What to check after the flash
  - Boot, display, audio, radios, USB; `cat /sys/module/clocks/parameters/unused_handoff` shows UART1

`reason=never_initialised retained=0`; PERI_PDN0 bit 17 set (`golden` row `PERI_PDN0_STA` now matching).
  - A ~35-min sleep: golden SoC differences down by one; `y2_infra/state last_lost`.
  - The overnight drain against 16's ≈8.6 mA (first night for 17–20 together).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
