---
title: "POWER-FINAL-15 — 14 with every component on its newest release - Innioasis Updater"
description: "POWER-FINAL-15 — 14 with every component on its newest release Status: IMPLEMENTATION READY PHYSICAL NOT RUN sealed, awaiting the owner flash. Package out/y2linux-platfor"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-15.html"
---

# POWER-FINAL-15 — 14 with every component on its newest release - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-15 — 14 with every component on its newest release

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-15 — 14 with every component on its newest release

Status: IMPLEMENTATION_READY_PHYSICAL_NOT_RUN (sealed, awaiting the owner flash). Package `out/y2linux-platform-v1-power-final-candidate-15/` (fallback = sealed 14), symbols `…-15-symbols/`, receipts `out/deep-sleep-final/build15-receipts/`, branch `power-final-15` (Y2Reborn branch `power-final-15`). Identity: Linux `be1aac2123abbe68778aa52c8ae206c55cdf8a6e` (a later test-only commit follows); Reborn `f68e088d7de9591e13ff1925590ceb419d340625`. BOOTIMG `86dc957a6a74da5107d9e889bf48686acb904d3bab6510f6a83e461ed450844d`, Y2ROOT `0b14b79445f160b4e07430386b5ca1b576bb7b04d793ef8ce3c09a8156d620ae`. Fallback = sealed 14.

## Versions

| Component | 13/14 | 15 |
| --- | --- | --- |
| Linux | 6.18.0 | 6.18.56 (stays on 6.18, as the owner asked) |
| Buildroot | 2025.02.18 (line ended) | 2026.08 (newest release) |
| Cross toolchain | Bootlin 2024.05-1 | Bootlin 2026.08-1 (GCC 15.3.0, glibc 2.44, binutils 2.45.1) |
| Kernel build sandbox | Alpine 3.22.1, LLVM 20.1.8 | Alpine 3.24.2, LLVM 22.1.3 (newest in Alpine), GCC 15.2, qemu 11.0.3 |
| Rust | 1.90.0 | 1.99.0 |
| Image packages |  | Mesa 26.2.4, OpenSSL 4.0.3, Python 3.15.0, OpenSSH 10.6p1, GLib 2.90.1, D-Bus 1.16.2, util-linux 2.42.4, iproute2 7.2.0, busybox 1.38.0, SQLite 3.54.0, e2fsprogs 1.47.4, kmod 34.2, libdrm 2.4.134, ncurses 6.6, readline 8.3, expat 2.9.0, exfatprogs 1.4.3, fdk-aac 3.0.0, iperf3 3.22, iw 6.17, ethtool 7.1, json-c 0.19, libnl 3.12.0, libffi 3.8.0, libxcrypt 4.5.2, pcre2 10.49, procps-ng 4.0.7, strace 7.2, evtest 1.36, memtester 4.7.1, CA certificates 20260816 |
| Already newest |  | FFmpeg 9.0.2, BlueZ 5.87, SBC 2.2, bluez-alsa 5.0.0, ALSA 1.2.16.x, curl 8.22.0, Dropbear 2026.94, wpa_supplicant 2.12, zlib 1.3.2, libsodium 1.0.22, wireless-regdb 2026.09.03 |
| Host build tools |  | meson 1.12.1; Python build packages to newest PyPI (pypa-build 1.6.1, setuptools 84.0.0, wheel 0.48.0, flit-core 4.1.0, …) |
| Left at Buildroot's choice |  | host-only tools that never ship: pkgconf 2.3.0 (3.0.8 exists), automake 1.16.5, libtool 2.5.4, patchelf 0.13 (deliberately pinned by Buildroot) |
| Not changed |  | Reborn's vendored Rust crates (separate step) |

Every source archive is pinned by SHA-256; where upstream publishes a checksum it was compared (Linux, Buildroot, Bootlin, OpenSSL, GLib, util-linux, iproute2, iperf3, Rust manifest, PyPI, Debian CA certificates, Alpine).

## Changes needed by the new versions
  - Kernel: 49 overlays apply with fuzz 0 on 6.18.56 (12 re-based without conflict). i2c-mt65xx: upstream combines

every write-then-read, which covers MT6582. mtk_dsi: our probe order already satisfies upstream's fix. Four overlays are upstream now and were removed (ext4 0032–0034, fs freeze 0066). SPM driver ported to the 6.18.y `struct syscore` API. The GC9503V panel sets `prepare_prev_first` because 6.18.y reverted the DSI host's request.
  - Buildroot: defconfig options that 2026.08 removed (e2fsck and flock are always built; Mesa folded KMSRO into

Lima). Python 3.15: Buildroot's patches 0002/0005 re-based. util-linux/Mesa patches that are upstream or irrelevant were dropped. OpenSSL 4.0 has no `c_rehash`, so the CA hook uses `openssl rehash`. libldac states the CMake 4 policy floor. The post-build and packaging steps find the OpenSSH/Mesa/libdrm build folders instead of naming old versions. The validator accepts Mesa's single `libgallium` (Lima + KMSRO, no software rasterizer). `build.py` reads the kernel version from the source.
  - Reborn: Rust 1.99 Clippy fixes (`as_chunks`, `try_update`, pointer cast for the signal handler, zip counter).

## Tests

Locked-container production suite: 8 suites, 664 cases, 10 host-dependency skips, exit 0 (two earlier runs stopped at tests that encoded 6.18.0 behaviour; adjusted in the test-only commit). Packaging-host 32 and splash 27 PASS. Package validation PASS; ELF closure 354 files / 1,135 dependency edges (fewer than 14 because Mesa now ships one library instead of per-driver copies); installed-ARM PASS (Python 3.15 imports all 39 platform modules under qemu, SQLite 3.54.0, OpenSSL 4.0.3); inventory 108 packages; privacy 1,491 root files, no private state. Reborn: 362 tests, fmt and strict Clippy on Rust 1.99. Host regression comparison against `main`: same 38 environment failures.

## Not verified

Everything physical, in particular the display (DSI order, Mesa 26/Lima), audio, Bluetooth (BlueZ/BlueALSA on the new GLib/D-Bus), Wi-Fi (wpa_supplicant with OpenSSL 4.0), SSH/SFTP (OpenSSH 10.6 sftp-server), MTP, sleep.

## Verdict

IMPLEMENTATION_READY_PHYSICAL_NOT_RUN

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
