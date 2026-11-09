---
title: "M2-USBACM-03 — wait for PMIC synchronization before commands - Innioasis Updater"
description: "M2-USBACM-03 — wait for PMIC synchronization before commands <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate ide"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-usbacm-03-result.html"
---

# M2-USBACM-03 — wait for PMIC synchronization before commands - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBACM-03 — wait for PMIC synchronization before commands

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBACM-03 — wait for PMIC synchronization before commands > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

[Owner capture-03](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-03-kernel-and-pid1-capture-confirmed&anchor=usbacm-03-kernel-and-pid1-capture-confirmed) now confirms 11754 bytes of kernel/PID1 logs, kernel sequence 0–77 and beats 1–43, with no captured relay gaps/errors. Normal 45-second capture exit: 0. Basic logging works; broader qualification and M2 exit remain outstanding.

Earlier [host journal evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-03-host-enumeration-confirmed&anchor=usbacm-03-host-enumeration-confirmed) confirms 0525:a4a7 enumeration and ttyACM0. The first capture was sandboxed; the second reached the tty but lacked host permissions. Those historical access failures are superseded by the successful owner capture-03 above.

2026-09-09, baseline `c066d62` plus the retained USBACM-02 source snapshot. Offline validated and hardware logging confirmed by capture-03.

`/home/luca/Dokumente/Code/Y2Linux/out/m2-usbacm-03/BOOTIMG.img`

1,159,168 bytes; SHA-256: `20c7f01ad97832def704523897fb5ec08cbfacd560558bbd3989b4f4426f734a`.

Heading/build M2-USBACM-03, Linux 6.18.0-y2-m2-usbacm3.

## Fix and evidence

The owner reports USBACM-02 displayed the attach prompt, then failed before attachment. Its [photo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-02-result&anchor=usbacm-02-result) records poll 5 and WACS2 `00200001`: initialized, no request, idle FSM, only sync-idle absent. A single synchronization sample caused immediate -16 refusal.

This candidate waits up to 1000 ten-microsecond intervals for sync-idle at probe entry and immediately before each PMIC command. It still requires the complete original ready predicate before issuing a command. Missing init, an active request or any nonzero FSM stops immediately; persistent sync activity returns -110. There is no command retry, stale-response acknowledgement or reset. The [source contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-probe.md) documents the exact scope.

The existing failed-poll snapshot/display remains available. USB ownership, poll interval/deadlines, D08/CPU0, local snapshot sizes and packaging/recovery boundaries are unchanged. The software fix addresses the observed premature refusal; capture-03 now confirms synchronization and enumeration succeeded in one physical run; repeatability and reconnect remain unqualified.

## Validation
  - One clean pinned build, no compiler warnings/errors. 15 targeted methods

and four host-capture methods pass. The protocol regression includes the original 26 scenarios plus 36 new cases across probe entry and all three pre-command checks: immediate/delayed readiness, 999/1000/1001-delay boundaries, lost init, new request, stale completion and invalid FSM. Exact command/ack counts prove no transaction is issued on a failed gate.
  - Five worker/status scenarios and 33 QEMU ARM PID1 paths pass, along with

existing wake/session/relay checks, linked relay-syscall mutations, real-artifact corruptions and BOOTIMG/D08 checks. No duplicate successful build or unchanged source/ROM/recovery provenance audit.
  - Emitted ARM review shows the new wait inlined into probe/read paths, bounded

RDATA reads/delays, init/request/FSM checks before CMD and VLDCLR only after this probe's completed read. No new MMIO callback or register is introduced.
  - Resolved config changes only LOCALVERSION from USBACM-02. Initramfs gzip is

9372 bytes. Decompressor/initramfs bounds, LK complete read-tail and the 16 MiB BOOTIMG partition checks pass. [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-03-layout.json) and [iteration](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-03-iteration.json); output retains source snapshot, input lock, artifact hashes, ELFs, config, logs and focused disassembly.

## Original owner test (completed by capture-03)

Use the established BOOTIMG-only procedure with the exact image above. Start the updated capture tool before booting:`python3 tools/observation/usb_log_capture.py --output out/m2-usbacm-03/capture-01`

Power on unplugged; attach promptly at `ATTACH USB CABLE NOW`, then leave the cable attached. If an error appears, retain a complete photo including US/RC, POLL/PW/V, WACS, G and bottom PHY rows, and state whether attachment happened. If enumeration succeeds, return the capture directory; the expected header is now `Y2LOG1 M2-USBACM-03`. Use the updated capture tool with this image.

Keep the original 60 seconds from power-on limit and manual Android BOOTIMG restoration. The USB active deadline remains 50 seconds; no reconnect or connected-start recovery is added. [Full capture procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fusb-log-capture.md).

M1 remains complete, M2 active with blocked exit; #23/#27/#28 stay open and M3/application work deferred. No physical operation was performed to prepare this candidate. Prior images and both owner photographs remain retained.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
