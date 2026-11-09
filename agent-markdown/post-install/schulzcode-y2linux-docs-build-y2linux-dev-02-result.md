---
title: "Y2LINUX-DEV-02 — root handoff ABI and wheel transaction corrections - Innioasis Updater"
description: "Y2LINUX-DEV-02 — root handoff ABI and wheel transaction corrections <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candid"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-dev-02-result.html"
---

# Y2LINUX-DEV-02 — root handoff ABI and wheel transaction corrections - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-DEV-02 — root handoff ABI and wheel transaction corrections

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-DEV-02 — root handoff ABI and wheel transaction corrections > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Built and physically booted; live core qualification retained, USB reconnect fails.[DEV-02 live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md). Four CPUs, expanded RAM/short memory test, Buildroot Y2ROOT, input, visible display and initial SSH/ECM/ACM work. The owner restart confirms persistent userspace fixes. The original offline/deployment checkpoint follows as history. [Deployment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-dev-02-deployment.md). The existing DEV-01 SD filesystem stays in place; no second Buildroot compilation or SD rewrite is required.````````

| Artifact | Bytes | SHA-256 |
| --- | --- | --- |
| BOOTIMG.img | 4683776 | 3afbc15950e75d0477036709aabf32ceb2101ff090a6625ba5e9f7d5e840df05 |
| y2.dtb | 7774 | 57d774abaf2d410bbfbd5ec8956f7f3c4a35bf3120611fadb474cd51c12947e7 |
| initramfs.cpio.gz | 1562123 | ddd2f516124f2dbb11165e47467f7c56145d9da9343406794e84d0085a6f83a4 |
| display.ko | 158300 | 545e29be86e0148445d70a5e508fedcdcc21126ca3d236000029bd1aaea86174 |

Exact configs, ELF-derived layout, source manifest, unchanged rootfs images, module update tar, logs, result.json and SHA256SUMS are in `out/y2linux-dev-02/`. The new kernel identifies itself as 6.18.0-y2linux-dev02. LOG1/rootfs/USB serial retain the DEV-01 userspace identity for compatibility with the installed SD.

## Evidence and corrections

[DEV-01 capture and owner photograph](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-development-hardware-result.md) confirm visible console, four CPUs, MemTotal954668KiB including HighTotal228352KiB, advancing display vblank, matching GEM/OVL addresses and a successfully mounted SD Y2ROOT. PID1 dies by SIGILL immediately after the switch-root message. The exact faulting PC was not recorded, so no single cause is asserted as proved.

DEV-01 had `ARM_THUMB=n`, although the toolchain's ARMv7 glibc advertises Thumb-2 code. The actual v6.18 `arch/arm/mm/Kconfig` says disabling this support can break signal handling when userspace switches ISA, including illegal-instruction aborts. `KUSER_HELPERS=n` similarly removes fixed-address ABI helpers; the actual packaged glibc contains a reference to 0xffff0fa0. Enable both supported userspace contracts. This removes known configuration incompatibilities without replacing glibc, selecting Debian, reducing RAM or changing the working display route.

`CONFIG_DEBUG_USER=y` with `user_debug=31` records future user faults instead of leaving only the final PID1 exit signal. A small glibc child preflight is run while rescue PID1 and its observer remain alive. It deliberately installs a Thumb signal handler from ARM code and returns through the kernel, checks kuser version, barrier and TLS helpers, creates/joins a glibc thread, executes VFP arithmetic, reads the monotonic clock and checks one MiB of allocator memory. A five-second alarm bounds it; failure leaves rescue selected. It does not prove every later init path or turn the photograph into a known fault-PC trace.

`CONFIG_FB_DEVICE=y` restores the normal framebuffer userspace device missing from DEV-01. Its color tool had logged ENOENT despite visible fbcon. Existing 480x360 timings, panel takeover, OVL format/address handling, PHY and mutex programming are preserved. Actual pattern visibility/readback awaits DEV-02.

The wheel's controller diagnostics show op1 (write), transactions2, DMA finished one-byte TX, no I2C completion and ten timeouts. Source review finds v6.18's WRRD combination gated solely on `auto_restart`, whereas MT6582's selected mt6577-compatible controller has `auto_restart=0`. It consequently requests two writes with only the first message configured and waits indefinitely for completion until the normal timeout. DEV-02 allows the already implemented WRRD path for exactly `mediatek,mt6582-i2c` when two messages are write then read to the same address. This sets direction change and 1/9-byte transfer lengths in one hardware operation. APT32F register-zero/frame contract, clocks, pulls, DMA channel, IRQ handling and timeout policy remain; no retries are added. Hardware confirmation remains required.

## Validation and compatibility

One clean new kernel build, without warnings/errors; existing pinned Buildroot binaries reused. Exact kernel/DRM module, DT, decompressor relocation, BOOTIMG staging/overread and rescue archive checks pass. The physical bank and reservations are unchanged; actual kernel span is10626240bytes and exact initrd length1562123.

Tests exercise the real patched I2C dispatch with non-auto-restart MT6582, the existing modern path, nonmatching messages, invalid buffers and a single bounded failed operation with balanced clocks. New config tests reject the actual old DEV-01 ABI settings and independently disabled Thumb/helpers/fb-device/debug support. A simulated SIGILL in the probe child leaves the rescue gate disabled. Existing shared provider/PHY/relay/USB tests and DEV DT/layout/archive mutations pass; the historical D08-specific baseline DT fixture is explicitly skipped by the generic test script, with DEV actual-DT checks taking its place.

QEMU runs the actual ARM probe successfully, plus startup shell parsing and Dropbear help. QEMU emulates the userspace kernel ABI; these results do not prove real-Y2 signal handling. The linked kernel config and actual hardware preflight provide the complementary checks. Read-only e2fsck and independent ext4/tar checks of the unchanged rootfs/key/tools pass.

The new DRM module is loaded from rescue. SD userspace/observer binaries are unchanged and skip module loading when DRM already exists. The old SD module index therefore does not prevent this boot, but must be refreshed before later module reloads. A root-owned, version-specific `sd-module-update.tar` is prepared for installation on verified removable Y2ROOT over SSH after successful startup. The module payload has no loader, partition, calibration or private-key contents.

The [boundary audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23dev-02-root-handoff--wheel-correction-audit--2026-09-10&anchor=dev-02-root-handoff--wheel-correction-audit--2026-09-10) keeps M2 active and incomplete. No device writes were executed by the assistant. Next is one owner flash and integrated physical acceptance, not separate images for the panic, wheel and framebuffer node.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
