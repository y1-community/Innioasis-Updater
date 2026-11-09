---
title: "M2-USBACM-04 — one bounded disconnect/reconnect trial - Innioasis Updater"
description: "M2-USBACM-04 — one bounded disconnect/reconnect trial <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-usbacm-04-result.html"
---

# M2-USBACM-04 — one bounded disconnect/reconnect trial - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBACM-04 — one bounded disconnect/reconnect trial

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBACM-04 — one bounded disconnect/reconnect trial > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, baseline `7ee780a`. Offline validated; hardware test pending. The successful [USBACM-03 capture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-03-kernel-and-pid1-capture-confirmed&anchor=usbacm-03-kernel-and-pid1-capture-confirmed) is already pushed. #27 stays open until this robustness evidence is reviewed.

Candidate: `out/m2-usbacm-04/BOOTIMG.img`, 1,161,216 bytes. SHA-256: `ecdce008c34998dce03e1b5dd88b0c78c3015e5865b93d4ba609f6cbf134f365`. Heading/build M2-USBACM-04; Linux 6.18.0-y2-m2-usbacm4.

## Change and bounds

On first sampled CHRDET loss, disable the pullup and interrupt delivery, invoke upstream gadget disconnect/stop, and restore only the saved digital PHY session inputs. Keep the controller registered; PID1 closes its nonblocking tty, keeps its existing 8 KiB history, and continues displaying/logging beats at stage 8. The adapter suppresses delayed upstream pullup requests while unplugged.

One reconnect repeats fresh supply/clock checks, exact saved PHY6c/6d checks, passive B-device/no host request, unchanged seven mode/trim and five other digital PHY bytes, and all eight zero DMA controls. It reuses the guarded session sequence and upstream start, checks retained FIFOs, then allows the pullup. A second detach, failed guard, IRQ limit or original 50-second USB deadline ends the trial. Expected tty EIO/ENODEV/EPIPE during cable loss becomes a retained `LINK tty disconnected` event; other relay errors remain errors. Replay uses LOG1 and retained kernel/PID1 history, including explicit existing GAP markers.

No memory-policy, DMA ownership, DT hardware-node, rail, analog trim, boot packaging or unrelated USB feature change. The 60-second owner power-on limit, CPU0, watchdog stop, framebuffer fallback and BOOTIMG-only boundary remain. Connected-start recovery is still unsupported. [Scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23current-scope-review--one-bounded-usb-reconnect-baseline-7ee780a&anchor=current-scope-review--one-bounded-usb-reconnect-baseline-7ee780a).

## Validation

One clean build; no compiler warnings/errors. 16 targeted methods pass: 29 production reconnect lifecycle/guard scenarios, eight worker scenarios, 34 QEMU ARM PID1 scenarios, host/ARM bounded relay faults and replay, existing session/clock/PWRAP checks, real linked relay syscalls, corrupt-artifact tests, and D08/BOOTIMG bounds. Eight host capture/orchestration methods pass using PTY/mock devices only, covering pause timing, changed tty number, wrong path, missing reconnect, failed replay and refusal of an already-running candidate.

Resolved config differs from USBACM-03 only in LOCALVERSION. DT hardware nodes are unchanged; generated linux,initrd-end tracks the new gzip size. Initramfs gzip: 9510 bytes. Emitted ARM review retains ordered mask/pullup-clear, upstream disconnect/stop, byte-width PHY restoration, bounded re-entry guards, sampled W1C acknowledgement, start and pullup gate. No duplicate build or full source/ROM/SPFT audit. [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-04-layout.json), [iteration](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-04-iteration.json). Output retains sources, locked inputs, ELFs, disassembly, test logs and artifact hashes.

## One combined owner hardware test

Use the established procedure to flash only BOOTIMG, with the exact candidate above. The assistant has not flashed or written any physical device. Keep the known restoration path and restore Android within 60 seconds of power-on.

Start this on the real Linux host before booting the candidate:`sudo python3 tools/observation/usb_log_robustness.py --output out/m2-usbacm-04/robustness-01`

The privileged host invocation is necessary on the inspected host: `luca` cannot open the current root:uucp 0660 ACM tty, and noninteractive sudo requires a local password. Enter it only in the local terminal. It covers both tty enumerations without persistent host permission changes. An assistant with explicit tty access can run the same tool through host execution without sudo. A one-node ACL normally disappears on disconnect; do not assume it grants access after re-enumeration.
  - Boot unplugged, attach promptly at `ATTACH USB CABLE NOW`.
  - The tool verifies USB descriptors and the exact USBACM-04 manufacturer,

records the real port/tty, then leaves it unopened for 8 seconds.
  - It opens, asserts DTR, sends LOG1, reads 3 seconds, pauses userspace reads

6 seconds, then resumes for 3 seconds. The kernel may still buffer USB data during the pause; this tests a non-reading host application, not proof that every device queue filled. Offline relay fixtures cover actual EAGAIN.
  - At UNPLUG Y2 USB NOW, unplug once. Leave it unplugged 5 seconds;

observe the heartbeat continuing and reconnect once. No screen transcription is needed if retained stage-8 heartbeat records establish continuity.
  - The tool re-discovers the same physical USB port with a new device number;

tty numbering may change. It sends LOG1 again and captures up to 12 seconds. Its total budget is 42 seconds from first enumeration; the device's original deadline and owner's 60-second power-on limit take precedence.

Stop on a screen error, heartbeat stall, unexpected device identity, no reconnect or any safety concern. Retain the complete output directory even on failure. `robustness.json` records host phases; both capture subdirectories retain raw bytes, hashes, USB descriptors, timing and exit reasons. Exit 0 means capture is ready for review, not hardware qualification.

Review raw/chunk integrity and exact headers in both sessions; contiguous kernel sequence within each replay (replayed duplicates across sessions are expected); PID1 beat continuity, multiple stage-8/offline beats and subsequent configured beats without a restart/stall; bounded pause/unplug timing; and any GAP/ERR/LAST ERR. A disconnect may truncate the final transport line of the first capture; the second replay must recover the retained complete record. Unexplained omissions, malformed records or missing offline evidence do not pass. Report any overwritten history explicitly rather than claiming lossless delivery.

Only a successful evidence review closes #27. Then follow #22 → #23 → #24 → #25 → #26 → M2 boot/stability qualification and the standing closure audit. No later scope starts from this offline candidate. M1 complete; M2 active/exit blocked.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
