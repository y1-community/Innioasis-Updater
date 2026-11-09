---
title: "Y2Linux development hardware results - Innioasis Updater"
description: "Y2Linux development hardware results <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-y2linux-development-hardware-result.html"
---

# Y2Linux development hardware results - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux development hardware results

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux development hardware results > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## DEV-02 live Buildroot qualification — 2026-09-10

[Complete evidence-backed report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md): four CPUs, MemTotal954660KiB, completed256MiB short RAM pass, writable removable Y2ROOT, all buttons/wheel, visible DRM pattern and initial SSH/ECM/ACM are measured. USB reconnect fails before enumeration; only the owner's subsequent restart restores access. M2's remaining concrete blocker is #27/#28 USB re-entry. Runtime/module/cursor and host configuration fixes are retained and reproducible. No assistant reboot or new BOOTIMG was performed.

## DEV-01 SD mounts, then PID1 SIGILL — 2026-09-10

After the Mac SD-writing instructions, the owner's photograph shows ext4 recovery, UUID79324c69-6e75-4801-8000-000000000001 on mmcblk0p1, a successful read/write remount and `Y2ROOT: verified /dev/mmcblk0p1; switching to Buildroot` at23.490923s. At23.723691s the kernel panics: `Attempted to kill init! exitcode=0x00000004`. That is SIGILL; no fault PC/instruction was printed. This confirms removable-SD filesystem access and root selection, not successful Buildroot PID1/SSH. The visible display still works. It supersedes the earlier no-root-media observation; the earlier MMC timeouts do not establish inability to read this written card.

DEV-01 disabled ARM_THUMB despite Thumb-2 toolchain code and disabled kuser helpers despite glibc containing a reference to the fixed helper page. Kernel ARM Kconfig explicitly documents possible SIGILL for either incompatibility. Those are supported corrections, not proof of the photographed fault's exact instruction. DEV-02 also enables user fault diagnostics, adds a child ABI probe before handoff, enables FB_DEVICE for the missing fb0 node, and corrects the I2C controller WRRD dispatch behind the continuing wheel timeout. See [DEV-02 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-dev-02-result.md). No new physical success or milestone completion is inferred from the new build.

## DEV-01 rescue capture-02 — 2026-09-10

After the owner enabled host ACM access, a 45-second capture succeeded: `out/y2linux-dev-01/capture-02/raw.bin`, 196354 bytes, SHA-256 `32085a995f111f9e1dd8acf1e18ff2d8ea3389b586e9ef211e74ab8c279bfe69`. All 704 kernel records 0–703 are present. The LOG1 header and USB descriptor identify DEV-01. The history replay includes earlier boot snapshots; capture success does not mean every snapshot was freshly taken during these 45 seconds.
  - CPUs online 0–3; MemTotal 954668 KiB (about 932 MiB), HighTotal 228352 KiB.

Large RAM/HIGHMEM is visible; allocator stress is still untested.
  - XRGB8888, 480x360, pitch1920, GEM allocation692224 bytes. GEM DMA and live

OVL both `84900000`, match1; layer control `000040ff` selects format4. Vblank advances18 →86 →154 →221; mutex module mask488, SOF1. GPIO112 mux1, direction/output/input1; enabled backlight with inherited PWM/current. These support the owner's visible-console observation without identifying which combined correction caused it.
  - The color tool reports `framebuffer query: No such file or directory` at8.496s.

No successful test-pattern/memory-readback result exists; investigate fb0 node availability in the next integrated correction while preserving visible fbcon.
  - Ten wheel I2C reads still time out: controller START1/status0/irq_seen0,

parent273MHz/div16/bus100kHz, op1, DMA enable0/flags1. The regression remains in the transaction path; retain exact diagnostics for the next combined fix.
  - Rescue declares no usable Y2ROOT at22.106s. The SD rootfs is not installed.

MMC command timeouts are present; SD filesystem boot is not qualified. USB composite enumeration and ACM log transfer work. ECM traffic, SSH, reconnect and allocator memory tests remain unqualified.

The owner can attach the card reader only to a Mac. A verified 8.3 MB gzip of the existing ext4 image is ready for LAN transfer. [Mac preparation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-dev-01-mac-sd.md) starts with a read-only disk listing, before any exact owner write commands. No new candidate build, storage write, private-key access or milestone closure.

## DEV-01: owner sees the Linux console — 2026-09-10

At source checkpoint `a34a360`, the owner reports manually flashing the new BOOTIMG and seeing the Linux console. The SD rootfs has not been prepared. This is positive physical visible-output evidence, superseding BASELINE-03's black-screen observation for this boot. Exact flashed bytes and the color test pattern are not independently verified; no claim identifies which combined source correction caused the improvement.

Read-only host discovery independently identifies USB `0525:a4aa`, serial `Y2LINUX-DEV-01`, manufacturer `Linux 6.18.0-y2linux-dev01 with musb-hdrc`, speed 480 Mbit/s and an ACM interface on `/dev/ttyACM0`. Identity is retained in `out/y2linux-dev-01/usb-identity-owner-console.json`. This proves composite enumeration, not Ethernet traffic, successful log streaming or reconnect.

ACM capture-01 could not open the serial device (host EACCES); sudo capture-02 could not start because a host password is required. No runtime log capture was obtained. The host currently lists only its internal NVMe and zram, with no removable SD attached. No disk or device storage was written.

Expected current userspace is rescue, pending logs; SD root, Buildroot init, SSH, RAM size/stability, wheel and button operation on DEV-01 remain unverified. M2 stays active and incomplete. Next steps: attach the removable card to a host reader and identify it before owner writing, enable host ACM access, retain the running boot logs, then test Y2ROOT and networking together. No kernel rebuild or second BOOTIMG flash is needed merely to install the prepared SD rootfs.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
