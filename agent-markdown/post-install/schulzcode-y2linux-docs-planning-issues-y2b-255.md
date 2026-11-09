---
title: "Y2B-255 — Add bounded USB CDC ACM kernel and PID1 logging - Innioasis Updater"
description: "<!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-255.html"
---

# Y2B-255 — Add bounded USB CDC ACM kernel and PID1 logging - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-255 — Add bounded USB CDC ACM kernel and PID1 logging

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2) > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## Current session checkpoint — 2026-09-10

Initial ACM/Ethernet/SSH work, including return after owner startup/restart. USB cable disconnect/reconnect still fails without restart. This issue remains OPEN and deferred to later platform qualification, not an M3 blocker.

[September 10 session audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23current-session-close-audit--2026-09-10&anchor=current-session-close-audit--2026-09-10). Earlier phase ordering below is historical where superseded.

## DEV-02 live hardware checkpoint — 2026-09-10

OPEN: physical USB reconnect failed; core/Buildroot otherwise substantially qualified.

[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) retains baseline, completed 256 MiB test, input/display/SD and USB failure evidence. No reboot, kernel build or BOOTIMG was prepared. This checkpoint supersedes stale untested/blocked statements below within its measured scope.

# Y2B-255 — Add bounded USB CDC ACM kernel and PID1 logging

## Offline integration checkpoint — 2026-09-10

The proven ACM path and offline one-reconnect lifecycle are integrated into the combined baseline; shared PMIC/clock ownership and early USB startup replace competing mappings. New provider integration and reconnect remain unqualified on hardware.

[M2-BASELINE-01: exact implementation, RAM decision, checks and owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md). The historical scope/sequence below is superseded where it conflicts with the owner’s combined integration instruction. All remaining acceptance criteria stay open.

## Additional evidence — 2026-09-10

USBACM-03 remains our confirmed 11,754-byte kernel/PID1 capture. USBACM-04 and M2-INPUT-01 remain pending hardware results. The external project confirms ACM+ECM feasibility and documents the mc IRQ name and getty HUPCL/DTR pitfall, but supplies no equivalent bounded reconnect qualification. Our reader already clears HUPCL during capture. Preserve canonical guarded PIO MUSB/PHY and existing robustness tests; no donor PHY replacement, ECM expansion or new USB hardware claim.

[Research matrix and source limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). M1 complete; M2 active/exit incomplete. External results do not promote our hardware status. Existing acceptance criteria and historical checkpoints follow.

## Current execution checkpoint — 2026-09-09

The owner explicitly requested one combined enumeration/logging candidate to reduce physical iteration. [Scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23combined-usb-ownership-scope-review--baseline-d9c2c98&anchor=combined-usb-ownership-scope-review--baseline-d9c2c98) keeps M1 complete, M2 active/exit blocked and later phases deferred. [CHRDET evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) establishes charger presence under the reported cable conditions; connected-start6a=BE still refuses wake. No new hardware result has been inferred.

Immediate next test: [M2-USBACM-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-01-result.md), 1,159,168 bytes, SHA-256 `d2d1f8cbbaa23ffcbdeddb317db7a8e62bc21deca9ebebc564c9b55a5590aedd`. [Reviewed combined contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-enumeration.md): boot unplugged, perform the proven guarded wake, attach at the screen prompt, check fresh supply/clock/PHY/DMA state, apply the FM/LK digital device-session sequence, then attempt upstream MUSB peripheral PIO, one standard g_serial ACM and bounded retained/live kernel + PID1 logging. No host VBUS supply, analog calibration, PMIC writes, active-DMA recovery, RAM expansion or other partition writes.

One clean build passes 23 full-suite methods, one additional linked-syscall mutation method and 8 observation methods, including 30 QEMU ARM PID1 scenarios and host/ARM relay faults. Exact DT/config, linked accesses, D08 and BOOTIMG pass. [Host capture tool](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md) is ready. No device operation was performed. Stop for the owner's BOOTIMG-only physical test within 60s. USBGUARD-01 remains an optional untested fallback, not a prerequisite test.

This advances offline implementation only. Physical enumeration, real log continuity, late-open/non-reading behavior and controller reconnect qualification remain outstanding. The first trial stops on first detach/error or 50s active window; reconnect and connected-start recovery are not implemented. #23/#27/#28 stay open, and every original hardware acceptance criterion remains intact. Original drafting-only restrictions below are superseded only for this specifically authorized/audited experiment, not a general production port.

## Status, type and goal

Draft implementation contract; BLOCKED on the MT6582 USB controller gate below. Not implementation-ready for hardware, and not `state:luna-ready`. The upper-layer logging design is specified; no implementer is asked to choose PHY registers or invent a DT compatible. This issue does not absorb an unresearched controller port.

One goal: over the existing Y2 USB data port, retrieve retained kernel messages and continuing PID1 logs on a Linux PC, independent of screen reading or physical UART. Exactly one CDC ACM port; no interactive shell.

[Research, source evidence and detailed contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fknowledge%2Fusb-logging.md).

## Why now / dependencies

M1 hardware execution and periodic PID1 diagnostics are owner-observed (#20/#21). Host log access would shorten every later RAM, input, display and storage cycle. Y2E-160 #23's PMIC/supply research is a prerequisite source for VUSB, not a claim that USB power is already understood. Physical UART #16, full RAM expansion #22, input/display/SD implementation are not prerequisites. D08 remains the default. No reordering/execution of the five queued foundation issues is authorized here.

Hard gate before any runtime implementation: record an exact, reviewed MT6582 USB device-controller contract in `docs/knowledge/usb-logging.md`:
  - Controller MMIO span, SPI/polarity, interrupt handling and sufficient FIFO/

endpoint layout for EP0 + ACM bulk IN/OUT + notification IN.
  - Actual clock-provider/gate/48 MHz mapping, USB2 PHY register/initialization/

calibration contract and VUSB supply/ownership after normal LK handoff.
  - Peripheral/VBUS detection and safe disconnect/reconnect; no host VBUS sourcing.
  - Quiescence of inherited USB DMA before PIO, without touching display DMA.
  - Exact v6.18 glue/PHY compatibility or a reviewed completed prerequisite change.

Stock `musb-hdrc.0` IRQ 64 and public MT6582 SPI32 evidence support the route. They do not prove that existing `mediatek,mtk-musb` glue plus a sibling PHY works. Upstream glue needs three clocks and a generic PHY; current Y2 DT provides neither. Do not unblock until this gate is resolved. If it needs a controller/clock/PHY implementation, stop and return the single smallest prerequisite for owner review; do not create further issues or expand this issue automatically.

## Exact implementation scope after the gate
  - Reuse proven MUSB in peripheral-only PIO mode with built-in `g_serial`,

defaults ACM on / OBEX off / one port. Kernel intent: `USB_SUPPORT=y`, `USB_GADGET=y`, `USB_MUSB_HDRC=y`, `USB_MUSB_GADGET=y`, `MUSB_PIO_ONLY=y`, `USB_G_SERIAL=y`; host `USB=n`, DMA/OTG/dual-role off. `USB_MUSB_MEDIATEK` and `NOP_USB_XCEIV` apply only if the exact glue is verified; selected GENERIC_PHY/USB_ROLE_SWITCH and the real provider must be accounted for. `U_SERIAL_CONSOLE=n`; no `console=ttyGS0` dependency. Existing PRINTK/TTY/ proc/sysfs/time32 stay enabled. g_serial selects LIBCOMPOSITE/CONFIGFS_FS and serial functions; no configfs mount or setup daemon is needed.
  - DT: only the reviewed USB/PHY/clock/supply nodes, `dr_mode="peripheral"`.

Extend the exact DT validator whitelist, not D08 bounds. No guessed addresses, dummy PHY, fake fixed clocks, unrelated clock gating or full-SoC DTS import.
  - Existing native PID1: bounded raw nonblocking `/dev/ttyGS0` relay. Discover

its dynamic device number from sysfs; read kernel ring through `/dev/kmsg` (1:11, read-only). Keep an 8 KiB PID1 startup/status ring, 32 KiB TX queue, 8 KiB kernel-record buffer. Service at most 16 records / 16 KiB each heartbeat pass. Preserve partial writes and report drops/gaps; boot/heartbeat never waits for a host. New syscall numbers require actual linked-kernel checks.
  - Host sends only `LOG1\n` to begin/restart replay of retained kernel and PID1

startup records, then live records/status. Bounded 16-byte parser; no shell, arbitrary command execution or writable filesystem/log API. Include kernel release, build identifier, source/sequence and explicit overflow markers.
  - Host script selects an explicit verified USB tty path, commonly `/dev/ttyACM0`

but never inferred from numbering alone. Raw 115200 8N1/no flow control, ACM DTR asserted, sends LOG1, records bytes/timestamps/USB identity and exit reason. Use upstream standard g_serial descriptors, not stock Android VID/PID. Read `/sys/class/tty` USB parent identity; no privileged global host-rule changes.

## Files/components

Prospective edits only: `kernel/config/first-boot.config`, `kernel/dts/innioasis-y2-first-boot.dts`, `tools/validation/dtb.py`, `initramfs/init.c` and a small bounded relay helper; `tools/observation/usb-log-capture.py`, `tests/test_usb_logging.py` and affected PID1/syscall/artifact tests; `docs/build/usb-log-capture.md`, `docs/knowledge/usb-logging.md`. Reuse upstream MUSB/gadget code where the gate establishes compatibility. A broad USB/PHY/clock/PMIC driver port is a prerequisite, not hidden scope here.

## Explicit out-of-scope

Implementation/build/flash during this drafting session; automatic hardware trials; ADB/adbd, networking, RNDIS/ECM, mass storage, Debian, storage access, app work, USB host/OTG switching, charging-policy changes, accessory UART muxing, preloader/ LK/security/partition changes, RAM expansion, full display driver, persistent ramoops reservations and guaranteed pre-enumeration crash/panic capture.

## Acceptance criteria
  -  Hardware prerequisite contract is reviewed and complete; no guessed driver,

compatible, clock, PHY/power or DMA handoff assumption remains.
  -  Resolved config is peripheral/PIO/one-ACM, with expected dependencies and

real syscall implementations; only approved DT nodes are added.
  -  Linux host enumerates the selected Y2 as CDC ACM and opens its tty without

custom kernel drivers; capture identifies actual USB path/descriptors.
  -  One LOG1 capture includes retained early kernel-ring messages, PID1

startup/mount/sleep status and at least ten increasing heartbeat records. These are actual kernel logs, not only rendered-screen summaries.
  -  Late host open, non-reading host and one authorized disconnect/reconnect

do not stall PID1; reconnection can replay and reports any overwritten logs.
  -  Positive hardware results name candidate SHA-256, host tool/version, raw

log/hash and timing. Offline fixture success is not enumeration success.
  -  D08, CPU0, watchdog and guarded framebuffer fallback remain intact;

BOOTIMG bounds pass and loader/partition/calibration state is untouched.

Do not close as hardware-success based only on source review or fixture tests. The issue may remain blocked while upper-layer intent is fully specified.

## Validation

No implementation or device tests in this session. Later targeted host/ARM fixtures must cover partial/EAGAIN/EINTR/ENODEV/EPIPE writes, ring wrap/overrun, late LOG1, malformed/overlength input, partial lines, no-reader/reconnect and continued heartbeat. Check actual linked syscall targets, dynamic tty discovery and bounded memory/CPU budgets. Replay pre-enumeration kernel records if still retained; report gaps instead of silently promising lossless delivery.

Initial USB is a new hardware subsystem: review controller/PHY/clock/power and DMA safety, binding/config resolution, affected regressions and complete D08/layout/BOOTIMG validation under the broader verification boundary. Trust unchanged pinned source/toolchain/recovery provenance. Subsequent relay-only changes use one clean build, targeted tests and final D08/package size/hash, without routine historical full-suite or two-build repetition.

Any later device validation requires a separately authorized BOOTIMG-only trial, retained known-good fallback and bounded observation window. No flash is implicitly authorized by implementing or closing an offline checkpoint.

## Stop conditions and alternative

Stop at the controller gate, unexpected PHY/PMIC/clock/reset dependencies, inherited-DMA uncertainty beyond the approved experiment, IRQ storm, VBUS-source risk, framebuffer/heartbeat regression, parser bounds failure or D08 overflow. Do not enlarge RAM or port an entire subsystem to make this issue fit.

No simpler reliable host-readable alternative is established: ADB, USB Ethernet and vendor bulk all require the same missing UDC/PHY; UART-over-USB requires an unverified electrical accessory, and ramoops lacks a proven retained range and reader. Preserve the working screen temporarily; do not call it USB logging.

## Unlocks

Host-retained boot/runtime logs for faster single-change RAM/input/display/storage bring-up. It does not observe preloader/LK or hangs before USB/PID1 initialization, and it does not start another platform milestone or Y2PlayerNative work.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
