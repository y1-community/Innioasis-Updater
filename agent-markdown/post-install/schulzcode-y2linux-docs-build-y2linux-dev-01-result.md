---
title: "Y2LINUX-DEV-01 integrated development candidate - Innioasis Updater"
description: "Y2LINUX-DEV-01 integrated development candidate <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-dev-01-result.html"
---

# Y2LINUX-DEV-01 integrated development candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-DEV-01 integrated development candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-DEV-01 integrated development candidate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Built and offline validated; stop at owner manual deployment. Latest physical result remains `2efcdc1` / M2-BASELINE-03 capture-02: Linux and USB healthy through 180 seconds, all 606 kernel records, black physical display after successful DRM, 55 balanced button pairs and eight wheel IRQs with eight I2C -110 results. The owner confirms earlier working wheel rotation; its exact canonical artifact was not established. No wheel protocol rediscovery or new hardware success claim.

Deliverables are in `out/y2linux-dev-01/`:``````

| File | Bytes | SHA-256 |
| --- | --- | --- |
| BOOTIMG.img | 4675584 | 59f2d5980cdcfe0f7da3f6ec76f7c653528dddc481173660f3b99f615bded9ff |
| rootfs.ext4 | 536870912 | ecf7f9a448e708f9a1c023443ab4d4a9a22d9ab4e8e812b3319b58770dbd2ed3 |
| rootfs.tar | 19025920 | e2eaeac8d0f954e60d24b83367f9946ef0f28656831d720b9e0e9b2fb0819648 |

The directory also contains kernel.config, buildroot.config, y2.dtb, Image, zImage, zImage-dtb, exact DRM module, rescue initramfs, observer/pattern binaries, layout.json, source-manifest.json, result.json, validation/build logs, SHA256SUMS and DEPLOYMENT.md. [Owner deployment commands](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-dev-01-deployment.md).

## Display and wheel

The 480x360 MT6582 variant already selected XRGB8888 encoding `4 << 12` at BASELINE-03; v6.18 also already had the generic OVL pitch/address alias fix. Neither was falsely claimed as a newly discovered fix. The new post-layer-commit log records the actual fourcc, framebuffer dimensions/pitch/GEM DMA/allocation, expected versus live OVL address, EN/SRC/ROI/control/pitch/size/offset/layer RDMA. The fb0 tool paints white/red/green/blue plus a checkerboard, then compares an expected pixel checksum with a volatile readback of the visible framebuffer. It never maps arbitrary physical memory.

Donor-supported corrections avoid soft-resetting an enabled OVL, clear stale LK mutex membership after DSI parking and retain a deasserted, live LK panel instead of unconditionally resetting/replaying DCS. The cold/reset path retains the full GC9503V sleep-out/display-on initialization. The path stays OVL0 → RDMA0 → COLOR0 → DSI0; BLS is not added as a DDP component. Geometry remains 480x360.

Four bounded post-modeset samples hold a DRM vblank reference and record vblank and DSI interrupt counts, OVL/RDMA/COLOR/DSI state, route and mutex registers, GPIO112 mux/direction/output/input and D-PHY state. Backlight readback separately reports enable, PWM and current-step state. These changes address credible post-modeset failure paths; the black-screen cause and actual visible success remain pending physical observations, not inferred from successful probing.

The APT32F address 0x51, register-zero write plus repeated-start nine-byte read, header/class/direction contract and one transfer per interrupt are preserved. The exact old working canonical build was unavailable; comparison uses retained history and the donor contract without rejecting the owner's earlier success. DEV-01 stops clearing inherited I2C pulls, keeps the evidence-backed live CCF parent/divider (not the donor dummy rate), and resets MT6582 controller/APDMA before unmapping/freeing buffers on timeout/NACK. Error logs retain START, interrupt status/mask, timing/control, FIFO/debug/IO, transfer lengths and DMA ownership. No retry loop is added. Those values distinguish a stuck/no-start controller, NACK, unfinished DMA and completion-IRQ problems; they cannot prove an electrical wire transition without a physical bus capture.

## Development foundation

[RAM reconciliation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdevelopment-memory.md) implements the evidenced 992 MiB bank, 40 MiB loader reservation, 16 KiB boot data and both uncertain high ownership alternatives. About 951 MiB remains before kernel allocations. HIGHMEM is enabled with PAGE_OFFSET c0000000 / PHYS_OFFSET 80000000. Actual MemTotal, highmem operation and allocator tests await hardware.

[Buildroot 2025.02.17](https://buildroot.org/downloads/) is pinned by archive SHA-256 in `buildroot/inputs.lock.json`, with the Bootlin ARMv7 EABIHF glibc stable 2024.05-1 toolchain and Buildroot's package hashes. This is a compiled rootfs, not just a defconfig. BusyBox init/devtmpfs, iproute2, procps, util-linux/lsblk, i2c-tools, ethtool, strace, e2fsprogs, dosfstools, kmod and memtester are present. No Debian, desktop, Y2PlayerNative or audio/radio stack.

The filesystem is ext4 LABEL Y2ROOT, UUID 79324c69-6e75-4801-8000-000000000001. Buildroot reproducible mode, fixed timestamps, filesystem UUID/hash seed and deterministic rescue packaging are configured. A second full reproducibility build was intentionally not performed.

BOOTIMG contains BusyBox/glibc rescue PID1 and the independent observer. It waits 20 seconds, searches labels only under the removable 11240000.mmc controller, refuses duplicates/wrong filesystems, validates init before switching root, and stays in rescue with ACM on missing/broken media. Internal eMMC is disabled. The removable SD controller supports one-bit block I/O at up to 13 MHz without new rail/voltage changes.

MUSB stays PIO/peripheral, with 2144 bytes of FIFO for ECM+ACM in the existing 8 KiB RAM. Software time/reconnect limits are removed; real power-state faults remain terminal. ECM uses 10.42.0.1/24, and services handle late USB attachment. The observer restarts logging once across switch_root without requiring another host LOG1. A reconnect still supports a fresh host capture/handshake.

Dropbear is key-only, with the exact explicitly supplied ED25519 public key (fingerprint `SHA256:IS9HhrmQKRtlEEbrcJjZa0XQHVwnRXRUzQQ61/7XAb8`). Root's password hash is unusable but the account remains eligible for public-key authentication. No host private key was inspected or packaged. Device host keys are generated on the SD at runtime. SSH and its entropy/startup behavior need the physical run.

## Validation and reproduction

One clean kernel tree and one Buildroot tree were used. Compiler corrections and rootfs finalization reused those trees; no duplicate kernel qualification build, full upstream-tree hash, ROM/recovery audit or hardware write was performed. The final kernel/module build has no compiler warnings/errors or modpost failures. The host kmod build emitted an upstream const-qualification warning with this host compiler; it completed and produced the checked module indexes.

Passed: actual ELF/link/syscall/config checks; zero-fuzz hash-verified source overlays; exact DT and full large-RAM relocation/staging/reservation arithmetic; independent rescue cpio and BOOTIMG parsing; matching single-module ABI/bytes; changed subsystem tests (wheel framing/error bounds, rescue root selection and bad-media cases, relay handoff/errors, 100 USB reconnect cycles and existing power/PHY/clock/MMC command firewalls); host capture PTY/identity tests; ARM observer selftest and QEMU execution of actual BusyBox script parsing/Dropbear. The D08 DT fixture was run against the retained BASELINE-03 DT; DEV has its own actual-DT mutation tests. No old-D08 acceptance was substituted for the new map.

`e2fsck -f -n` passes all five phases. Independent ext4 reads match tar contents for the key, shadow policy, observer, pattern and DRM module. ARM hard-float/glibc, required tools, module indexes, ownership and startup service bits are checked. `rootfs-validation.json` and test/build logs retain details. Unified-diff patch context includes intentional space+tab/blank prefixes; whitespace checks apply to non-patch files and the added source lines independently.

For a future fresh output directory, the checked-in orchestrator performs the same build phases (network only for missing Buildroot downloads):`python3 tools/build/development.py --output out/y2linux-dev-01-rebuild \ --public-key /home/luca/.ssh/y2linux_ed25519.pub`

It reuses the existing locked kernel environment, bootstraps it only if missing, verifies the pinned Buildroot archive, builds kernel and userspace once, packages, tests and retains hashes. It refuses to overwrite an existing kernel build. The orchestrator itself was syntax-checked; this candidate used the same phase commands during development, without running a second clean build to test it.

No milestone closes here. After manual deployment, collect all platform state, observe the real pattern and wheel, test allocator memory once, and check SD root, ACM reconnect, ECM and SSH together. Remaining failures belong in an integrated DEV-02 iteration. [Boundary audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23y2linux-dev-01-manual-deployment-boundary-audit--2026-09-10&anchor=y2linux-dev-01-manual-deployment-boundary-audit--2026-09-10).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
