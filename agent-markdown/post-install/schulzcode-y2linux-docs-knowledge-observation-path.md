---
title: "Y2 first-boot observation path - Innioasis Updater"
description: "Y2 first-boot observation path <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-observation-path.html"
---

# Y2 first-boot observation path - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 first-boot observation path

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 first-boot observation path > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current visual runtime success is recorded in [M1 hardware evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md). [USB host logging research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fusb-logging.md) now selects CDC ACM plus a nonblocking PID1 relay, gated on MT6582 controller/PHY/clocks. No USB implementation or device observation occurred in this session.

The owner authorized a temporary alternative in Y2E-150: [D13 guarded inherited-framebuffer diagnostics](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md). UART0 remains compiled as an additional path. Physical UART/stock serial capture below remains unproved, but is no longer required for this risk-accepted visual experiment. Display persistence and visible stages still require the first board trial.

2026-09-08, [Y2E-140 / #16](https://github.com/SchulzCode/Y2Linux/issues/16). Software controller corrected to UART0; physical observation gate remains open. This investigation used offline FM artifacts, pinned source, public PCB imagery and bounded read-only ADB on the already running Android device. No reboot, port/register probing, wiring, accessory-mode change, image installation or experimental boot occurred.

## Installed evidence takes precedence over the package default string````````````````````````````````````

| Evidence | Observation | Meaning / limit |
| --- | --- | --- |
| Fresh /proc/consoles | ttyMT0, enabled/preferred console, device 204:209; also ram-1 | Installed kernel's active serial console is index 0. This is not UART output received on a wire. |
| /sys/class/tty/console/active | ttyMT0 | Independent console-core corroboration. |
| /sys/class/tty/ttyMT0[/device] links | devices/platform/mtk-uart.0/tty/ttyMT0 / mtk-uart.0 | Platform device 0, not an alias for port 3. |
| Fresh /proc/iomem | 11002000-110020ff : mtk-uart.0; ports 1–3 follow at 11003000, 11004000, 11005000 | Installed resource mapping identifies hardware UART0. Resource size is stock driver's declared 0x100; upstream DT uses its researched 0x400 register window. |
| /proc/version | 3.4.67, build June 1 2026 | Stock-family kernel, not a hash of installed boot/loader bytes. Existing modified Android lineage remains possible. |
| /proc/cmdline, dmesg | Permission denied; remote RC 1 | No live baud/options or early LK transcript recovered from these interfaces. |
| /proc/last_kmsg | Readable previous kernel RAM-console tail, uptime about 1304–1316 s, shutdown/reset messages | Real retained stock kernel log, not current boot's early log, not a UART capture, not proof of LK visibility. |

Raw output and UTC command manifests are under private `20260908-observation/stock-verified/` and `stock-mapping/`. Each command has a separately recorded remote `echo` status marker; Android's old ADB host return code alone is not sufficient. Preliminary top-level captures used an unavailable `printf` marker and are retained only as superseded attempts; their remote status must not be inferred. No serial-device file or arbitrary register was opened on Android. Public integrity locators are in [capture-index.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/capture-index.tsv).

## FM kernel mapping independently remapped

This uses the exact FM decompressed kernel and its recovered symbols from Y2E-130, not offsets from the earlier non-FM kernel. The input hashes remain in [handoff-artifacts.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/handoff-artifacts.tsv); `fm-uart-functions.txt` records instruction bytes, virtual addresses and resolved literals.
  - `get_uart_default_settings` at `0xc04a736c` returns `0xc0a01518 + index * 28`. The four entries' base words at offset 0x0c are `0xf1002000`, `0xf1003000`, `0xf1004000`, `0xf1005000`.
  - `mtk_uart_console_init` at `0xc0970294` uses the UART array at `0xc0b8c8f8`, stride 0x1dc. It preserves the index and converts the virtual peripheral address to the corresponding `0x1100...` physical base. Index 0 is hardware UART0.
  - `mtk_uart_console_setup` at `0xc0970138` directly selects that indexed structure. Defaults are 115200, `n`, eight bits; supplied command-line options are parsed before `uart_set_options`.
  - `mtk_uart_console_setting_switch` at `0xc04a9f3c` changes index-0 TX/RX modes to non-DMA and enables deep-idle handling. It does not exchange UART indices or MMIO bases.

The matching vendor implementation independently explains this behavior: [common UART source](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/uart.c), [MT6582 port source](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/mt6582/platform_uart.c), and [register definitions](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/include/mach/mt_reg_base.h). Vendor macros are one-based: `UART1_BASE` means `0xf1002000`, hardware UART0. The kernel source's command-line adjustment prefers a non-null bootloader console over a conflicting non-null kernel console. Source resemblance supports interpretation; it does not establish installed binary identity.

## Preloader/LK branch and baud

The FM package preloader is 120,384 bytes, SHA-256 `1df1b62498754aab0c7ddc80a79d310a92fcf81f29b515730c562aaeeb6a884a`. The package LK disassembly remains `20260908-ram-map/lk.thumb.txt`.

LK's helper at `0x81e00de8` dereferences its boot-argument pointer: when byte +0x14 is nonzero and word +0x0c equals `0x11002000`, it returns 1; otherwise 4. These fields are consistent with the preloader logging-enable/port contract. At `0x81e00fc8`, LK configures GPIO arguments `0x8000006d` and `0x8000006c` in mode 1, then selects UART0 on the return-1 branch at `0x81e01032`, otherwise UART3 at `0x81e00fee`. Both join at `0x81e01006` and use line-control value 3 (8N1), baud `0xe1000` = 921600, and a 26 MHz reference. Helper `0x81e00e1c` also changes the Android `ttyMT` digit to zero on that selected branch. GPIO numbers 109/108 are software arguments, not identified Y2 PCB pads, and do not establish which physical mux reaches the connector.

Conclusion: UART0 is the normal installed-kernel observation candidate. The live result is consistent with LK's conditional UART0 branch, so using the package's default UART3 string as the current candidate was wrong. The precise installed preloader/LK branch and log-enable values are still unobserved; do not promote this consistency to proof that the installed LK is byte-identical or that UART0's native pads carry output. The current Android kernel's exact baud remains unmeasured. 921600 8N1, no flow control is the firmware-supported initial receive setting; 115200 is a documented kernel fallback only, not a second automatic trial. Decode actual stock output before fixing a launch runbook.

## Physical evidence and electrical boundary

No board-specific TX, RX or GND test point is confirmed. A [firsthand Y2 teardown](https://www.reddit.com/r/innioasis/comments/1urrqn3/y2_internal_photos_so_far_pre_review/) supplies a [retained board photo](https://i.redd.it/y6r85h46r7ch1.jpg), showing covered components and unlabelled pad groups near connectors. Its board markings/revision have not been tied to this device. No readable UART labels or demonstrated net continuity identify a connection. Locations inferred from a round pad's appearance are not a pinout. No local owner board photo, schematic or prior serial transcript was found in the project evidence; no USB-UART ttyUSB/ttyACM adapter or by-id directory was present at host inventory time.

MediaTek's manufacturer-authored [MT6582 Technical Brief](https://device.report/m/09c50b26c755173dbd88dbf3a4f8720f16810b54ffb56fb78197abf968657287.pdf), detailed-pin Table 2-4, printed page 24, assigns native UART0 TX/RX to DVDD18_IO3, and UART3 to DVDD18_IO1. Thus 1.8 V is the expected native SoC logic domain. This is a public mirror of a 2013 manufacturer document, not a Y2 schematic or board-pad voltage measurement. Its extracted table was inspected; the PDF binary download and image rendering were unavailable, so no local PDF hash or visual package-coordinate verification is claimed. Do not assume a board test point is untranslated native I/O or that an adapter's VCC jumper sets its RX threshold. Do not connect a 3.3/5 V transmitter, RS-232 interface, adapter VCC, or any voltage source to an unverified pad.

The smallest missing physical evidence is a board-revision-specific, credible mapping of UART0 TX and GND, plus a safely established signal level and receiver compatibility. Obtain existing manufacturer/service/owner pinout evidence and then a documented high-impedance measurement on the identified net; do not discover it by blindly touching powered pads. No RX connection is needed for this experiment.

## Selected setup and stock proof procedure

Use a receive-only external UART capture after the physical boundary above is satisfied. The [host runbook](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fstock-console-capture.md) specifies TX-to-RX plus verified common ground only, a confirmed 1.8 V-capable receiver, initially 921600 8N1, and bounded raw/timestamped capture. Adapter TX, VCC, DTR and RTS remain physically disconnected. Host configuration/open/close can change modem-control lines even with a read-only file descriptor; physical separation is essential.

The standard-library tool records raw bytes, chunk receipt times, settings, setup record and hashes. PTY fixtures test byte preservation, no echo/data transmission, empty capture rejection, bounded truncation and disconnect retention. Those tests do not validate electrical thresholds, adapter clock accuracy, board routing or stock boot visibility. Gate acceptance requires actual identifiable stock LK and kernel output in order, obtained before changing BOOTIMG. Ideally retain two ordinary stock starts to demonstrate repeatability, starting capture before owner-operated power-on; no automated reboot or power action is provided here. Silence or garbled output leaves the gate open.

## Smallest alternatives considered[](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/usb20/mt6582/usb20_phy.c)````[](https://github.com/torvalds/linux/blob/v6.18/Documentation/admin-guide/ramoops.rst)

| Channel | Actual evidence | Remaining prerequisite / decision |
| --- | --- | --- |
| Bootloader UART over USB accessory route | FM preloader contains UART-mode and Prolific/FTDI cable-detection strings (retained offsets/hashes); the vendor USB PHY source contains CONFIG_MTK_UART_USB_SWITCH, PHY reconfiguration and UART0 register +0x90 routing. | Smallest alternative to research next if native TX is inaccessible, because inherited UART0 could in principle serve the current kernel without adding USB gadget support. Need trace the exact FM accessory-detection condition, real connector wiring/voltage/accessory specification, LK inheritance and persistence through early/normal console setup. Strings and a conditional sibling-source implementation do not prove selection. Do not connect guessed resistor cables, apply signals to USB pins or switch PHY modes. |
| ADB + existing /proc/last_kmsg | Successfully retrieved a stock previous-kernel tail this session. | Useful stock diagnostics only. Current native artifact has no Android/adbd/USB stack and will not export this file over ADB. It is not a first-Linux observation channel. |
| Reserved-RAM log / ramoops | Upstream v6.18 ramoops documentation requires reserved persistent RAM and a subsequent reader. Stock RAM-console export demonstrates one existing reader. | No proved common format, physical retained interval, reset/loader preservation, or safe offline extraction route. Needs a separately reviewed reservation/logging design and retention proof; a late panic logger also misses pre-initialization hangs. Not implemented or silently added to D08. |
| USB gadget serial, display/LED, network | No first-artifact support or complete Y2 bring-up proof. | Adds unresearched peripherals and cannot substitute for early LK/kernel evidence in this wave. |

No reliable physical alternative is established yet. Continue the UART evidence boundary rather than interpreting host tests, prior RAM logs or a speculative USB mux as permission to launch.

## D10 — Revise only the diagnostic controller

Replace UART3 with UART0 `0x11002000`, GIC SPI 51, 26 MHz, following the installed mapping and audited upstream MT6582 node. It remains the sole Linux serial alias `serial0` / `ttyS0`. Keep stdout-path without baud suffix, preserving inherited earlycon baud; keep normal `console=ttyS0,921600n8` pending wire confirmation. No new pinctrl, GPIO setup, DMA, peripheral, memory change or kernel feature is introduced.

The DTS, strict DT validator and actual-artifact negative tests now enforce UART0/IRQ51. Both new clean builds passed the complete offline pipeline; 11 outputs are byte-identical. Kernel, initramfs, config, sizes and every D08 interval are unchanged; only DTB/appended-payload/BOOTIMG hashes change. [Current artifact result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md) supersedes the old UART3 candidate. This correction does not establish that the inherited pad mux or early baud is correct.

Y2E-140 stays open: physical routing/level, actual serial stock LK+kernel capture and installed handoff continuity are not proved. After those are established, resolve U07b installed loader/authentication; U07c inherited DMA/secure/watchdog state and backup/recovery/power prerequisites remain mandatory. No candidate was flashed or booted.

## USB-only follow-up in Y2E-145

The owner confirms only the normal USB/ADB connection is available. Exact FM preloader disassembly now traces the Prolific/FTDI lead to electrical PHY line-state detection, followed conditionally by UART-mode register writes; it is not a serial service carried by Android ADB. Detector 0x0021065c tests 0xc0/0x80 at 0x11200620; caller 0x0020b584 branches to UART switch 0x0020b024 only on detection. Normal USB takes the other branch. [Full evidence and limitations](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md). Cable pinout/level, selected installed routing and serial capture remain unproved, so no wiring or USB-mode manipulation is proposed. Y2E-140 remains open; current USB/ADB is insufficient for GO.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
