---
title: "M2-USBACM-01 — guarded first controller ownership and logging - Innioasis Updater"
description: "M2-USBACM-01 — guarded first controller ownership and logging <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate id"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-usb-enumeration.html"
---

# M2-USBACM-01 — guarded first controller ownership and logging - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBACM-01 — guarded first controller ownership and logging

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBACM-01 — guarded first controller ownership and logging > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

USBACM-03 now has successful physical kernel/PID1 logging evidence. [USBACM-04](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-04-result.md) extends the original first-detach stop below to one guarded reconnect; it is offline validated and untested on hardware. All other ownership/deadline boundaries remain. The original first-attachment contract is retained below as history.

## USBACM-04 lifecycle source contract

The pinned Linux v6.18 [musb_gadget.c](https://github.com/torvalds/linux/blob/v6.18/drivers/usb/musb/musb_gadget.c) requires `musb_g_disconnect` under the controller lock; it invokes the composite disconnect callback, clears speed/activity and returns B-peripheral/B-idle to B-idle with NOTATTACHED state. Its vbus_session gadget operation is disabled, so this adapter does not pretend a generic VBUS callback is available. [Core start/stop](https://github.com/torvalds/linux/blob/v6.18/drivers/usb/musb/musb_core.c) disable/re-enable interrupts using platform callbacks; stop samples/acknowledges pending status. Start does not assert SOFTCONN, so the adapter permits pullup only after successful re-entry and the unchanged FIFO-layout check. Existing write callbacks continue clearing SESSION/HR and implement MT6582 sampled W1C semantics. The upstream host-state alternatives are excluded by the existing peripheral-only configuration and runtime B-device guard; no OTG or DMA path is introduced.

On CHRDET loss, retain the owned controller and use the same saved-input `y2_session_end` contract already used by terminal teardown. On reattachment, require fresh supply/clocks, exact saved inputs, unchanged digital/mode/trim bytes and zero DMA controls before `y2_session_start`; do not replay the original inherited-controller takeover predicate against registers Linux now owns. One re-entry only, no deadline reset. These are source-supported implementation facts; physical detach/re-enumeration and heartbeat/replay require the combined owner test. An offline fixture cannot establish electrical behavior.

## Original first-attachment ownership contract

2026-09-09, baseline `d9c2c98`, #23/#27 under active M2 #28. The owner explicitly requested one combined enumeration/logging attempt to reduce physical cycles. [Scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23combined-usb-ownership-scope-review--baseline-d9c2c98&anchor=combined-usb-ownership-scope-review--baseline-d9c2c98). Offline implementation, not a successful hardware enumeration result.[Original candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-01-result.md); [sync-wait fix](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-03-result.md). The [first hardware photo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md) records a cable-wait PWRAP poll refusal before enumeration.

## Entry evidence and limits

[CHRDET photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) establish bit5 following the reported startup cable condition. Connected startup gives PHY6a=BE and a correct pre-write wake refusal; the complete connected-start PHY state remains unknown. Unplugged startup gives the reviewed passive handoff and successful 6a=04→00 release. The earlier [PHY-wake result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-hardware-result.md) remains the positive same-boot stability/calibration sample. None establishes enumeration.

This trial therefore boots unplugged, performs the existing guarded wake, and asks for USB attachment. It does not normalize BE or bypass the old guard. A late cable attachment is an explicitly untested hardware transition. A mismatch stops this candidate and preserves its screen; it does not authorize another write sequence. CHRDET is a charger-presence indication, not measured VBUS voltage.

## Controller contract and exact sources

Use the previously pinned Linux v6.18, public MediaTek `d53dd75c3ff77cac3f5be58fddfe660e94f94d64`, FM kernel and LK bytes identified by [USB source research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fusb-logging.md), [USB state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-probe.md), [clock](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-probe.md), [wake](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md) and [PWRAP](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-probe.md). No new ROM/source provenance claim is made. Additional bounded disassembly is retained in ignored `evidence-private/20260909-m2-enumeration/`; its extractor wraps the already retained symbol-delimited FM bytes in a temporary ELF for LLVM disassembly.````````````````````````````

| Operation | Evidence and implementation decision |
| --- | --- |
| MAC 0x11200000, PHY 0x11210800 | Previous FM/LK mapping and successful 21-register physical snapshot. Claim MAC 0x280 bytes and PHY 0x70 bytes separately; never treat PHY as MAC+0x800. |
| USB interrupt | FM mt_usb_init c04d7fdc/7fe0 assigns IRQ64; musb_probe c03a7dd8/7ddc passes flags8 to request_threaded_irq. DT uses SPI32 level-low through the already-working MT6582 sysirq/GIC hierarchy. FM mt_irq_set_polarity confirms the polarity bank and SPI indexing; Linux's MTK sysirq translates low to GIC high. No raw interrupt-controller writes added. |
| L1 interrupt routing | FM mt_usb_interrupt c04d8368/8388 reads MAC+a0/a4 and c04d843c masks7 for USB/TX/RX. Adapter enables only7; DMA and IDDIG sources remain masked. |
| Status acknowledgement | FM c04d851c..85a8 samples byte USB+a/enable+b, word TX+2/enable+6 and RX+4/enable+8, then writes sampled values back (RX acknowledgement at c04d85d8). Adapter supplies W1C callbacks to MUSB, including its initial interrupt flush; generic read-to-clear is unsuitable. |
| Core identity/indexing | Physical HWVERS=6503. FM musb_core_init c03a3ab4 selects INDEX0; c03a3acc reads ConfigData at1f and tests dynamic-FIFO bit2. Use upstream INDEXED_EP window0x10, require this capability before programming. |
| FIFO MMIO and widths | FM musb_write_fifo c03a521c..522c derives MAC+0x20+4*ep; its read/write functions use byte/halfword/word accesses. FM musb_gadget_enable c03acd88/c03acda8 programs byte TXFIFOSZ62/word TXFIFOADD64; c03ad00c/c03ad02c programs RX63/66. This matches upstream musb_core.c indexed dynamic FIFO programming. |
| FIFO capacity/layout | FM mt_usb_init c04d801c/8020 records 0x2000 bytes; vendor table uses 512-byte FIFOs. Candidate uses 1600 bytes: EP0 shared64, EP1 TX512 at64, RX512 at576, EP2 TX512 at1088. Single buffering. ram_bits=11 means 8192 in upstream's 1<<(ram_bits+2) bound. Read back sizes6 and address units8/72/136 before SOFTCONN. Both TX FIFOs allow512 because ACM allocates notification IN before bulk IN. |
| Peripheral session | LK 81e092f6..81e0930c and FM/vendor usb_phy_poweron agree: after the guarded wake and its800µs settle, clear PHY6c bit4, OR6c with2e, OR6d with3e. These force digital device/VBUS-valid inputs; they do not source external VBUS. Execute only after a fresh valid CHRDET1 sample and passive-state gate. Require masked readback6c=2e,6d=3e and DEVCTL B-device/VBUS-valid98 within1000×10µs; host/session request bits reject. |
| MAC device behavior | Use upstream MUSB core/EP0/gadget code and its standard FIFO, CSR, interrupt, POWER and address handling. Adapter clears FADDR on reset as the upstream MediaTek ISR does; this standard MAC operation is distinct from importing its unproven sibling PHY/toggle glue. Every DEVCTL write strips SESSION/HR, and any latched error suppresses SOFTCONN. No host callbacks or host stack. |

## Supply, clock, DMA and calibration ownership

The adapter owns a bounded retained-state experiment, not a completed SoC clock/regulator/PHY framework. It has a real integrated `usb_phy` object whose initialization refers to the guarded state and whose OTG callback attaches the gadget. It does not register a nop PHY or fabricate USB clocks. `USB_PHY=n` disables the global lookup/ULPI framework; upstream's inline usb_phy_init still calls this adapter's real callback. PM, USB_MUSB_MEDIATEK and GENERIC_PHY remain off; there is no clock/supply disable on probe exit.

Before any new controller write: the original complete power/clock/MAC snapshot, successful wake W1/V7F/FFF and original CHRDET0 must pass. After attachment, repeat bounded PWRAP CID/VUSB/CHRDET reads, clock gate/mux/PLL checks and the full 21-register snapshot. Require POWER20, B-device with no SESSION/HR/HOSTMODE, HWVERS6503, the reviewed digital PHY state with6a=00, and all eight DMA controls0. The seven saved PHY mode/trim bytes must exactly match the successful wake sample.

Only then mask L1 and core interrupt enables, clear POWER/DEVCTL, and resample all eight DMA controls before session/FIFO ownership. This takes over a controller already disconnected with inactive DMA; it does not stop active inherited DMA. Any nonzero channel refuses takeover. Upstream is built PIO-only and has no DMA controller callbacks or mask. Endpoint buffers reside in controller FIFO RAM; USB payload moves by CPU. Display DMA and the D08 RAM policy are unchanged.

The only added PHY writes are masked digital6c/6d operations. The three analog trim samples00/05/15 and four mode bytes1a/1d/22/63 are checked again after the session and recorded in the kernel ring. No analog calibration, PMIC register, rail enable, charging policy, clock gate/reference, host VBUS or controller-wide reset write is added. PWRAP continues only the already-reviewed AP read-command and valid-clear handshake; no PMIC write transaction.

Once active, check CHRDET/VUSB every250ms, with the existing bounded PWRAP transaction. Stop on error, first detach or 50s after the initial wake. Mask L1, drop SOFTCONN, notify PID1 to close its tty, unregister MUSB, then release only the digital6c/6d bits forced by this adapter, preserving other bits. Do not re-suspend or power-cycle the PHY. An IRQ burst above512 entries in one jiffy masks L1 and disables this IRQ, latching EOVERFLOW. No automatic retry/recovery.

## Gadget, PID1 and host contract

Built-in upstream g_serial defaults ACM on, OBEX off, one port. Standard 0525:a4a7 descriptors and one ttyGS0; no ADB, shell, filesystem export or network. CONFIGFS_FS and unused serial/OBEX function code are selected dependencies; no configfs mount and no additional function is instantiated.

PID1 retains its cached 260-byte baseline snapshot. USBACM-01 used a separate 36-byte live ABI: magic/result/stage/polls/CHRDET/DEVCTL/IRQ/events/configured. USBACM-02 bumps the magic to 0x59325532 and appends the 52-byte failed PWRAP poll snapshot (88 bytes total); zero snapshot magic means no failed poll. A dedicated spinlock protects the failure copy across worker/status reads; no user copy or hardware access occurs under that lock. The sample survives teardown. PID1 displays it without replacing the cached PHY/wake rows. Reads are PID1-only and copy cached RAM, without fresh MMIO. DEVCTL=0x100 is uncollected; CHRDET=0x10000 is invalid. Screen dashes distinguish unread values from zero. Stages:1 preflight,2 attach prompt,3 session,4 registration,5 ready,6 configured, 7 stopped. A latched signed error retains the failing stage and baseline rows.

The relay discovers `/sys/class/tty/ttyGS0/dev`, strictly parses major/minor and creates only volatile `/dev/ttyGS0` and read-only `/dev/kmsg` nodes. It uses ARM EABI mknod14, lseek19, ioctl54 and existing read/write/open/close; actual linked targets are checked against ENOSYS. Raw tty open is nonblocking/O_NOCTTY. There is no serial console dependency and no runtime UART write in PID1.

Only exact `LOG1\n` requests a stream. It emits `Y2LOG1 M2-USBACM-03` (01/02 in the earlier candidates), retained PID1 startup/mount/sleep/baseline rows and heartbeat/status/error rows, rewinds `/dev/kmsg` to the oldest available kernel-ring record, and continues both. Kernel records retain native level/sequence/timestamp; PID1 records identify the source and BEAT. The early kernel ring is128KiB; PID1 history8KiB, TX queue32KiB, record buffer8KiB. Full history keeps its early records and explicitly reports loss; queue overflow and kernel EPIPE overrun have GAP records. This is bounded, not a lossless panic/crash recorder. Each once-per-heartbeat service performs at most one32-byte command read,16 kmsg reads and8 partial writes; absent/slow readers and malformed input do not wait. Flush tty output before close.

[Host procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md) validates the CDC ACM USB parent, records descriptors/path/timestamps/raw bytes/hash and asserts DTR before LOG1. The automatic selector refuses ambiguity; tty numbering alone proves nothing. PTY fixtures are labeled as such and never count as physical enumeration.

## Qualification remaining

The first candidate combines the reviewed dependency chain, not its proof. Physical attachment, USB reset/control requests, ACM enumeration, log transfer, continued heartbeat and retained calibration require owner hardware evidence. Connected-start recovery and reconnect after a physical detach are deliberately unimplemented in this bounded first-attachment trial. The relay can reopen and replay a surviving tty, but that is not controller reconnect qualification. #27's late-open/non-reading/reconnect criteria remain intact and unfulfilled on hardware. #23, #27, #28 and every M2 exit gap stay open; M1 and later gates unchanged.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
