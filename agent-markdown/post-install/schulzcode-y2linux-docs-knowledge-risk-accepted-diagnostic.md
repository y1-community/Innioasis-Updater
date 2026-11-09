---
title: "D11 — Risk-accepted first diagnostic boot policy - Innioasis Updater"
description: "D11 — Risk-accepted first diagnostic boot policy <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-risk-accepted-diagnostic.html"
---

# D11 — Risk-accepted first diagnostic boot policy - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# D11 — Risk-accepted first diagnostic boot policy

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# D11 — Risk-accepted first diagnostic boot policy > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-08; Y2E-150 [#18](https://github.com/SchulzCode/Y2Linux/issues/18). The owner's latest instruction supersedes the absolute authentication, exact installed BOOTIMG backup, and complete inherited DMA/secure-state gates in the previous Y2E-145 assessment. These remain uncertainties, now accepted for one bounded experiment. No hardware flash is authorized by this decision.

Unchanged requirements: BOOTIMG only, stock preloader/LK untouched, no formatting, repartitioning, system/userdata/rootfs changes; verified owner-proven FM/SPFT fallback; watchdog handling and useful observation. D08 allocator memory and all artifact caps remain exact. A separate GO issue and owner flash authorization are required. No automatic RAM expansion or security-state changes are allowed.

## D12 — Entry watchdog stop

Upstream v6.18 `mt6582.dtsi` supplies AP_RGU 0x10007000 and compatibles `mediatek,mt6582-wdt`, `mediatek,mt6589-wdt`. In `drivers/watchdog/mtk_wdt.c`, `mtk_wdt_init` recognizes an enabled watchdog and reloads its timeout; it does not stop it. Registration can arrange core servicing, but normal driver probe cannot cover the interval before decompression/initcalls or promise arrival before the inherited deadline. Merely enabling that driver is insufficient.

Use the same keyed MODE read/clear-ENABLE/write as upstream `mtk_wdt_stop` and FM LK disable helper 0x81e10ddc. Insert the board-specific operation immediately after masking interrupts in compressed/head.S, before stack, relocation and inflation. Only scratch r0/r1 are used; saved r7/r8/r9 and loader artifacts are preserved. Key 0x22000000, clear bit 0, DSB and readback. If still enabled, do not continue. An explicit branch into the text continuation skips linker padding; the emitted branch target is validated in addition to the stop instructions. No length, reset-request, security, PMIC or display register writes. The diagnostic kernel rechecks MODE disabled before exposing a visible stage.

This stops the identified AP watchdog, not every possible watchdog. A hang before entry, loader authentication rejection, inaccessible RGU or an already pending reset can still fail/reset. No guaranteed reset delay is claimed. Once stopped, a later kernel hang can remain frozen until the owner uses the proven power/recovery sequence. No automatic repeated boot/reset is requested.

## D13 — Guarded inherited video diagnostic

Exact FM LK input SHA-256: `bb1a93b4c1f02eab09ebad1314a8fdc25d94d3ca99771fc14e21cb18a289964a`. FM kernel was remapped using its own recovered symbols, not old kernel offsets. Private evidence: `20260908-risk-diagnostic/`.
  - FM panel parameter functions at 0xc04a2314 / 0xc04a25f8 describe 480x360 DSI;

mode at parameter +0x130 is 1 (sync-pulse video). LK corresponding parameter setup at 0x81e1ee00..0x81e1ee94 agrees; the embedded panel name includes `st7701_hvga_dsi_vdo_boe`. This does not prove an installed panel revision.
  - Stock ADB fb0 metadata: 480x1080 virtual, 32 bpp, stride 1920. This is Android

triple-buffer metadata, not LK's pixel layout.
  - LK display init 0x81e0a470 computes page span

align16(480)*align16(360)*2 = 353280 (0x56400). Layer 2 starts at framebuffer base, layer 3 console at base + page. Both use format enum 1 / RGB565 and 960-byte rows. Layer 2 is 480x360 at (0,0). Scratch base minus 4 MiB is not a diagnostic buffer. The framebuffer reservation is [0xbfb00000,0xc0000000).
  - Drawing uses base or base + 3*0x56400 = 0xbfc02c00, through

0x81e0a7fc / 0x81e0a854. Normal BOOTIMG continuation calls 0x81e0a9c4 at 0x81e18464. That routine waits for update; if the next draw offset is zero, copies the last logo from page 3 to base and switches layer 2 to base. Otherwise base was already selected. Thus normal final scanout converges on 0xbfb00000, not Android's active framebuffer index.
  - LCD_ConfigOVL 0x81e0db00 calls 0x81e13730, then layer config 0x81e12a84.

Layer-2 case 0x81e12e38..0x81e12f14 programs CON at 0x14007070, size +0x78, offset +0x7c, address +0x80 and pitch +0x84. Format is bits 15:12 = 1; memory source bits 29:28 = 0. The backing struct initializes source/alpha/key disabled for layer 2. Exact binary corroborates vendor definitions; do not confuse virtual f400xxxx with physical 1400xxxx.
  - Continuous video requires no per-frame CPU start operation. DSI registers

at 0x1400c000 START, +0x10 COM_CTRL, +0x14 MODE_CTRL identify running, enabled, non-reset sync-pulse video (frame/mixed/sleep modes excluded). Normal final platform cleanup does not stop this engine. Its LED cleanup 0x81e115c4 turns off LEDs 0,1,2, not backlight 6. Backlight-off caller 0x81e182a6 is a conditional charging-mode reboot, not normal boot.
  - Linux's minimal config has no display/PM/clock-gating driver to turn this

inherited path off. Persistence for the actual board is an experiment to observe, not a claimed successful hardware capture.

Implementation policy: only on `innioasis,y2`, read a bounded whitelist of AP_RGU/OVL/DSI configuration registers. Require watchdog disabled, expected running video and enabled layer 2, exact base/size/pitch/offset/RGB565 memory source, alpha/key disabled. Refuse all pixel writes on mismatch; UART reports failure. No fallback addresses or runtime register programming. Map only [0xbfb00000,0xbfb54600) = 345600 visible bytes using ioremap_wc; this is an explicit nonallocatable diagnostic aperture inside the existing excluded high framebuffer, not a new DT RAM bank. Write 16-bit pixels with ordered I/O and a completion barrier. Never touch the high scratch/other pages or low D08 RAM outside ordinary allocations. Read-only OVL/DSI mappings never receive writes.

A built-in board diagnostic marks kernel initcall progress with black/white stripes. PID1 writes a one-byte command to its dedicated root-only proc endpoint for solid green after a two-second stripe hold, then ten five-second heartbeat transitions with a white half alternating on green. After ten intervals it displays a terminal checkerboard and emits no further heartbeat. No display reinitialization, page flip, clock/pinmux/panel/LED/backlight programming or framebuffer device stack. Procfs is mounted nosuid/nodev/noexec but writable for this volatile PID1-only endpoint; sysfs remains read-only. UART0 remains additional output. Greyscale and green avoid red/blue ordering ambiguity. Tearing and bootloader console overlay are acceptable; stale logo, stripes alone or static green are not full success.

References: audited local upstream v6.18 sources; pinned manufacturer [watchdog driver](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/wdt/mt6582/mtk_wdt.c), [OVL implementation](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/dispsys/mt6582/ddp_ovl.c), [display register definitions](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/dispsys/mt6582/ddp_reg.h), [DSI register definitions](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/video/mt6582/dsi_reg.h).

## Recovery tradeoff

Fallback is owner-proven FM boot.img, not a current-device backup. Restoring it replaces any installed custom kernel, ramdisk, init/adbd configuration and boot-specific changes. Compatibility with the currently installed Android system is not guaranteed; full FM restoration might be needed. Such a later whole-ROM operation requires separate authorization and can replace system and lose userdata depending on targets/mode. It is not part of this BOOTIMG-only experiment. A generic ROM cannot recreate unique NVRAM/calibration. Preloader, LK, partition tables and personalized partitions remain prohibited targets.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
