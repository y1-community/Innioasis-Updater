---
title: "Host-readable USB logging — minimal path and controller gate - Innioasis Updater"
description: "Host-readable USB logging — minimal path and controller gate <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate ide"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-usb-logging.html"
---

# Host-readable USB logging — minimal path and controller gate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Host-readable USB logging — minimal path and controller gate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Host-readable USB logging — minimal path and controller gate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current next test: [USBACM-04 bounded robustness handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-04-result.md). USBACM-03 basic logging is confirmed and pushed; late-open/non-reading host, offline heartbeat and controller reconnect/replay remain hardware-unqualified. The one-reconnect implementation and host orchestration pass offline checks. #27 stays open until the combined physical result is reviewed.

Current physical result: [USBACM-03 capture-03](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-03-kernel-and-pid1-capture-confirmed&anchor=usbacm-03-kernel-and-pid1-capture-confirmed) confirms retained early kernel messages and increasing PID1 heartbeats over CDC ACM. The initial transport blocker is resolved; broader logging remains PARTIAL pending repeatability/reader/reconnect/stability qualification. Earlier research/checkpoints below retain their original evidence limits.

2026-09-09. [Y2B-255 #27](https://github.com/SchulzCode/Y2Linux/issues/27). Originally research/planning only; subsequent authorized execution is recorded below. Baseline: audited upstream v6.18 `7d0a66e4bb9081d75c82ec4957c50034cb0ea449`.

## Current execution checkpoint — combined first enumeration attempt

The owner requested a combined candidate instead of another register-only test. [M2-USBACM-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-enumeration.md) now implements the bounded retained-state adapter, exact FM/LK device-session sequence, upstream peripheral PIO MUSB and one ACM log relay. [Offline validated handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-01-result.md). Boot unplugged, attach at the prompt, attempt host capture in the same test. It refuses active inherited DMA rather than attempting an unreviewed DMA stop. This supersedes the original implementation stop for this specifically audited first-attachment experiment; it does not complete the general controller port or establish reconnect behavior. No physical enumeration result exists yet. USBGUARD-01 remains an optional untested fallback. #27 and M2 stay open with all hardware/late-open/non-reading/reconnect acceptance criteria intact.

## Original decision and gate

Prefer **one CDC ACM function using built-in g_serial, peripheral-only MUSB, PIO transfers, and a nonblocking PID1 log relay**. Host Linux would expose `/dev/ttyACM<N>` (often ttyACM0); Y2 exposes ttyGS0. This uses the existing data cable without ADB, network, mass storage, configfs orchestration or a shell. The [kernel gadget-serial documentation](https://docs.kernel.org/usb/gadget_serial.html) establishes this host/device interface, not MT6582 board readiness.

Not yet a config-only implementation-ready Y2 port. The gadget/logging contract can be fixed now; the controller/PHY/clock contract cannot honestly be filled with guessed sibling compatibles. Stop implementation at that gate. No reliable smaller host-readable channel is currently established on this Y2.

## M2 execution update — 2026-09-09

The owner has activated M2 and prioritized this path. Focused FM/LK comparison now distinguishes controller `0x11200000` from PHY `0x11210800`; it also confirms FM's VUSB request and the AP PWRAP read transaction. Exact locators and the [selected PWRAP/VUSB prerequisite](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-probe.md) are retained separately. A bounded candidate will read inherited PMIC identity and VUSB enable status on the existing screen. It does not enable this logging implementation. #23 and #27 remain open; no physical USB enumeration or rail state has been observed.

Remaining USB contract includes clock-provider integration, PHY recovery and analog trim differences, peripheral/VBUS behavior, FIFO/interrupt semantics and inherited DMA quiescence. In particular, FM `usb_phy_recover` includes devinfo conditionals and slew measurement; LK's selected trim branch is not mechanically interchangeable with the generic vendor source. This probe performs none of those analog/clock operations. A successful PWRAP read would resolve one supply observation prerequisite, not the complete hard gate.

## Evidence reviewed````````````````````````````````

| Evidence | Finding / limit |
| --- | --- |
| Retained 20260908-stock/interrupts.stdout:4 | IRQ 64 identifies musb-hdrc.0; retained Android mass_storage,adb composition and owner ADB connection prove this connector has a stock USB device path. They do not initialize USB for Linux. |
| Vendor mt_irq.h:51 | MT6582 USB0 is GIC_PRIVATE_SIGNALS + 32, consistent with the stock IRQ 64. SPI 32 is a candidate; final polarity/routing needs FM confirmation. |
| Vendor mt_reg_base.h:202; retained FM LK USB references | Vendor virtual USB_BASE 0xf1200000 and FM LK physical 0x11200000 references support the USB2 controller address. Do not reuse the vendor virtual address as DT reg. The PHY register window/offset convention needs separate reconciliation. |
| Vendor mt_devs.c:163 and usb20.c:786 | MUSB peripheral mode exists; vendor declares 16 endpoints and eight DMA channels; platform init supplies an 8 KiB FIFO layout and shared IRQ handling. These are vendor source facts, not a verified upstream FIFO configuration on this board. |
| Vendor usb20.c:808 | Non-FPGA init requests MT6323 VUSB at 3.3 V. This is an internal supply, not permission to drive 5 V out of the USB connector. Exact FM/installed supply/handoff ownership is not yet pinned. |
| Retained vendor usb20_phy.c:166,178,448 | PHY clock path manipulates UNIVPLL_CON0 bit 26 (48 MHz per comment) and MT_CG_PERI_USB0. Recovery performs USB/UART mux and PHY analog changes/delays; it is not a no-op transceiver. Actual FM sequence/calibration and inherited state remain unresolved. |
| v6.18 drivers/usb/musb/mediatek.c | Generic mediatek,mtk-musb match requires main, mcu, univpll clocks and a generic PHY. It programs a fixed eight-endpoint FIFO scheme and calls PHY init/power/mode functions. Do not infer MT6582 support from the generic match. |
| v6.18 Documentation/devicetree/bindings/usb/mediatek,musb.yaml | Enumerates mt8516, mt2701, mt7623; no mt6582. Requires reg/interrupts/phys/clocks. Current Y2 DT and upstream mt6582.dtsi supply none of the USB controller/PHY/clock-provider nodes. |
| v6.18 drivers/phy/mediatek/ and retained clock audit | No established MT6582 USB PHY match or complete Y2 clock/power provider. MT2701 T-PHY is not evidence of identical older USB2 PHY layout. |

The five newly fetched vendor files are pinned to [MediaTek source commit d53dd75](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/). Hashes and exact URLs are retained in `usb-logging-sources.json`; downloaded source bytes remain in ignored `evidence-private/20260909-usb-logging/`. Vendor code is reference evidence only. Previously retained FM bytes/symbols are the next specific comparison input, not interchangeable with that public source tree.

## Smallest lower-layer prerequisite

One exact MT6582 peripheral-only controller contract must resolve: MMIO span, SPI/polarity, endpoint/FIFO limits and IRQ acknowledge semantics; clock gates / 48 MHz source; PHY register layout, initialization/calibration and VUSB supply; normal BOOTIMG handoff state, cable/VBUS detection, and inherited DMA stop. Compare only the relevant FM `mt_usb_init`, `mt_usb_enable`, PHY/clock helpers and normal LK USB cleanup against the sources above. No whole-ROM re-audit. Use Y2E-160 #23 for shared PMIC/rail facts, extending its research to VUSB when needed. This is the blocking proof, not physical UART, input, display takeover, SD or full-RAM expansion. Do not implement a full PMIC/clock framework in this logging issue just to avoid acknowledging the prerequisite.

PIO removes newly requested USB DMA transfers, not inherited DMA activity. A reviewed controller stop/reset sequence must quiesce inherited channels before PIO ownership; no dummy PHY, arbitrary fixed clocks, guessed full-speed-only workaround, charger writes, host mode or unconditional VBUS drive is accepted.

## Fixed upper-layer implementation contract (after the gate)
  - Built-in `USB_SUPPORT=y`, `USB_GADGET=y`, `USB_MUSB_HDRC=y`,

`USB_MUSB_GADGET=y`, `MUSB_PIO_ONLY=y`, `USB_G_SERIAL=y`; `TTY`, `PRINTK`, `PROC_FS`, `SYSFS`, `COMPAT_32BIT_TIME` remain enabled. `USB=n` (host stack), MUSB host/dual-role and `USB_INVENTRA_DMA=n`. No DMA engine for USB.
  - Existing MediaTek glue, only if confirmed compatible, needs

`USB_MUSB_MEDIATEK=y`, `NOP_USB_XCEIV=y` and its selected GENERIC_PHY and USB_ROLE_SWITCH. The real PHY/clock configuration is a blocking prerequisite, not a missing option to guess. Any required MT6582 glue must be specified first.
  - g_serial defaults to `use_acm=1`, `use_obex=0`, `n_ports=1`. Preserve its

standard upstream gadget descriptors/IDs for this unchanged protocol; no stock Android VID/PID impersonation. `USB_G_SERIAL` selects USB_U_SERIAL, F_ACM, F_SERIAL, F_OBEX and LIBCOMPOSITE; LIBCOMPOSITE selects CONFIGFS_FS even though no configfs mount/setup or OBEX function is used. Account for resolved size.
  - Leave `U_SERIAL_CONSOLE=n`; do not add `console=ttyGS0`. Kernel log retrieval

uses `/dev/kmsg` with existing PRINTK. Keep the screen and UART0 as optional outputs; logging/boot must never await a host terminal or UART drain.
  - Future DT changes are restricted to the reviewed USB node, `dr_mode=peripheral`,

PHY and exact clock/supply references. Extend `tools/validation/dtb.py`'s explicit node/property whitelist for those reviewed nodes only. D08 memory, load addresses, framebuffer exclusions, CPU0 and watchdog remain unchanged.

## Log relay and host capture

Use the existing freestanding PID1; no BusyBox, systemd, adbd or login service. Discover ttyGS0 major/minor from `/sys/class/tty/ttyGS0/dev`, create its node in writable /dev; do not hardcode a dynamically assigned major. `/dev/kmsg` is read-only char 1:11. Open both nonblocking, raw serial mode, no echo/flow control; handle ENODEV, EAGAIN, EPIPE, partial writes and EINTR without blocking the heartbeat. Preserve the fixed time32 sleep ABI and check every new syscall against the actual linked kernel table.

A bounded `LOG1\n` request from the host starts/restarts a snapshot: firmware build identifier, current PID1 state, retained `/dev/kmsg` records from the oldest available sequence, then live kernel records and one PID1 status record per heartbeat. Emit `KMSG_GAP` on ring overrun/EPIPE; sequence numbers distinguish replayed records. PID1 retains its own bounded 8 KiB startup/status ring, with explicit drop count. Use a maximum 32 KiB TX queue, maximum 8 KiB kmsg record buffer, 16 records / 16 KiB processed per heartbeat pass, and bounded 16-byte request parser. Finish partially transmitted records before advancing; report truncation/oversized records explicitly. Never allocate without a cap or replace kernel logs with screen-only summaries. New LOG1 resets replay deliberately. No command execution, filesystem access requests or writable kernel-log endpoint.

A host script takes an explicit selected tty path and output directory, verifies USB parent descriptors, sets raw 115200 8N1 with no flow control, opens with DTR asserted for ACM, sends LOG1 and captures raw bytes plus host monotonic timestamps/metadata for a bounded duration. Baud is an ACM line-coding convention, not a physical UART requirement. Resolve identity via sysfs; ttyACM0 numbering alone is not device identity. Do not stop ModemManager or alter global host rules automatically. Host non-reader, late open and reconnect must not stall PID1.

Ring replay retrieves kernel messages emitted before USB enumeration only while still retained in RAM. It cannot capture preloader/LK, decompressor or a fatal hang before usable USB/PID1, and does not guarantee panic/crash delivery. Keep that limitation explicit; no new persistent reservation is implied.

## Alternatives assessed

ADB requires a working USB UDC plus an extra userspace/protocol stack. USB network or vendor bulk also require the same missing controller/PHY support and add complexity; neither bypasses the gate. Electrical UART-over-USB needs an unproved accessory, not an ordinary cable. Stock last_kmsg/ramoops retrieval has no proven cross-boot layout/retention/reader contract and would change D08. Current screen output is a functioning temporary aid but does not meet the requested host-log channel. Therefore no smaller reliable host-readable fallback is claimed.

## Returned M2-PWRAP-01 hardware evidence

[Owner photographs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-hardware-result.md) confirm RC=0/VALID=3, CID=0x2023, VUSB=0xc000 and continued execution through BEAT 50. This resolves the narrow inherited AP read-transport/VUSB-enable observation for this boot. It is one cached snapshot, not repeated sampling, voltage measurement or battery telemetry. Earlier pending/unknown statements describe the original handoff. Next: [read-only USB clock handoff snapshot](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-probe.md), with the source-identified timer IRQ-name parser correction. USB ownership remains blocked.

## Clock hardware result and next USB prerequisite — 2026-09-09

Latest: [M2-USBCLK-01 photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-hardware-result.md) confirm inherited VUSB and USB clock enables, corrected timer reporting and BEAT 50 without errors. [M2-USBSTATE-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbstate-01-result.md) is the next read-only MAC, digital PHY and DMA-control observation. USB initialization/logging remains blocked; earlier pending-clock statements describe historical checkpoints.

## USB state result / bounded PHY wake — 2026-09-09

[Returned USB-state photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-hardware-result.md) confirm all 21 MAC/digital-PHY/DMA reads, disconnected B-device state, eight zero DMA controls, PHY force_suspendm=1/value=0 and BEAT 50 without errors. This is one cached snapshot, not DMA ownership or a USB enumeration result. The next [guarded PHY wake](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md) checks remaining mode controls and conditionally clears only the suspend-force bit. Calibration/analog controls, clocks, VBUS forcing, controller connection and DMA remain unchanged. The candidate must stop for owner testing; full USB/clock-provider/PHY/VBUS/FIFO/IRQ/ DMA contract, host logging and M2 exit remain unqualified.

[The confirmed same-boot PHY wake result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-hardware-result.md) now records 6a 04→00, unchanged sampled trims, BEAT 10→49 and no reported errors with USB attached. DEVCTL remains 80; release alone does not establish PHY readiness or physical VBUS. The next localized prerequisite is [PMIC CHRDET observation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-probe.md), not guessed VBUS forcing.

## CHRDET result / connected-start refusal — 2026-09-09

[Returned CHRDET photographs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) show PMIC bit5=1 with USB connected at startup and 0 without it. Connected startup instead refuses the PHY wake guard before writing: 6a=BE, W0, V00/000. Original MAC, remaining PHY, DMA and IRQ-enable data are hidden by the old wake presentation; its unread zeros are not evidence of reset registers or a completed 6a write. [M2-USBGUARD-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-guard-diagnostic.md) exposes the original snapshot and validity with unchanged hardware behavior. Capture that startup condition before choosing an FM/LK-derived recovery/session step. USB ownership, MUSB/gadget, CDC ACM and live host logs remain blocked; charger detection alone is insufficient.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
