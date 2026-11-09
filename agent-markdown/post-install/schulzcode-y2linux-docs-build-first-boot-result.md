---
title: "M1 offline first-boot result - Innioasis Updater"
description: "M1 offline first-boot result <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-first-boot-result.html"
---

# M1 offline first-boot result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M1 offline first-boot result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M1 offline first-boot result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current: [risk-accepted diagnostic GO](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Frisk-diagnostic-result.md), pending separate flash authorization. The earlier candidate/assessment below is retained as history.

2026-09-08, revised by [Y2E-140 / D10](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md) to UART0/IRQ51 after installed-stock evidence. The previous UART3 candidate is superseded; its [layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m1-uart3-superseded-layout.json) and [hash inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m1-uart3-superseded-reproducibility.json) remain historical evidence. Offline candidate built and validated; no experimental device boot or flash performed. M0 and M1 hardware completion remain open. [Checkpoint history](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FM1-first-boot.md), [reproduction commands](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot.md), [launch gates and conditional experiment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-boot-launch-gates.md).

## Baseline and configuration

Linux 6.18.0-y2-m1, upstream tag v6.18 / commit `7d0a66e4bb9081d75c82ec4957c50034cb0ea449`, plus the single [D09 Kconfig visibility patch](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fkernel-policy.md). Clang/LLD 20.1.8 from the checksum-locked Alpine userspace; full package revisions in `tools/build/inputs.lock.json`. Build epoch `1764542530` (tag time), fixed build counter 1, UTC/C locale and stable build paths. Git author/committer identity was preserved throughout.

ARMv7 ARM instruction mode, EABI little-endian, CPU0 only, MMU/non-LPAE, `PHYS_OFFSET=0x80000000`, `PAGE_OFFSET=0xc0000000`, no highmem or runtime physical-address patching. `ARM_APPENDED_DTB=y`, `ARM_ATAG_DTB_COMPAT=n`, `ARM_VIRT_EXT=n`, gzip kernel/external newc initramfs, OF/GIC/sysirq/GPT, proc/sysfs and 8250/MT6577 candidate console. SMP, block/eMMC, networking, USB, display, sound, input, peripheral DMA, CMA, kexec and watchdog driver are disabled. Kernel fallback is `rdinit=/init`; DT supplies the controlled diagnostic command line. Full resolved config SHA-256: `27d41c25ab84cdbff5d134323ca386707ee8b64655cf904dd526b3387c01e7c0`.

## Artifact inventory``````````````

| Artifact | Exact bytes | SHA-256 |
| --- | --- | --- |
| Image | 2,543,296 | 293a252637578f004a941cc20940043d041114a174ae5cb5789253df8ed257b9 |
| zImage | 1,076,072 | 798f398d5190e86e3fb2d4a60fdaae625b2394ec2439634d7dd40035f610b8a1 |
| y2.dtb | 1,835 | 3582a3b9b683c141602492e125aa254ba9414f5be0dc1e362bb58dcb4c3f2235 |
| zImage-dtb | 1,077,912 | a737850794478c057dc8703f9ef0ff4d0e9f33bfcb44d7235981ad7ba84afd76 |
| initramfs.cpio.gz | 1,582 | 6abce20dd5e27475045b1242b0947c9abb5c570966d84fa09dc388bd676f6de5 |
| init | 2,740 | eb9a5dc82e26803c772298bd232568efd3f388bb8ce1bfabaa548c804e823a4e |
| BOOTIMG.img | 1,089,536 | 574061649e10266927267b68afbc95da7fe0761dc9823e88767741bac9363fd9 |

DTB totalsize is 1,835 bytes, padded to 1,840 when appended. Uncompressed newc is 4,096 bytes containing one 2,740-byte static executable and fixed directories/device nodes; gzip is 1,582 bytes. The image is unsigned; Android SHA-1 ID is only legacy metadata.

## Exact D08 map and actual occupied intervals

All addresses below are physical and half-open. DT memory is `[0x80000000,0x81800000)` + `[0x84000000,0x84080000)`, 24.5 MiB described RAM; permanent FDT reservation `[0x80000000,0x80004000)`. Page directory is `[0x80004000,0x80008000)`. Excluded from all memory nodes: `[0x81800000,0x84000000)` and `[0x84080000,0xc0000000)`, preserving D08's loader/high-memory uncertainty and identified modem/connectivity/display/preloader storage. No RAM expansion or LK memory import occurred.``````````````````````

| Actual occupant / phase | Interval |
| --- | --- |
| zimage | [0x80008000,0x8010eb68) |
| appended_dtb | [0x8010eb68,0x8010f298) |
| image | [0x80008000,0x80274ec0) |
| resident_kernel | [0x80008000,0x8029d130) |
| relocated_copy | [0x80275700,0x8037c8c0) |
| relocated_dtb | [0x8037c188,0x8037c8b8) |
| compressed_bss | [0x8037c8b8,0x8037c8d8) |
| malloc | [0x8037d8d0,0x8038d8d0) |
| initramfs | [0x84000000,0x8400062e) |
| lk_staging | [0x80007e00,0x80111600) |
| staged_initramfs | [0x8010f800,0x8010fe2e) |

Relocation delta is `0x26d620`; actual compressed code allowance Q is `0x900`. LC1 stack top is `0x8037d8d0`; 64 KiB malloc ends at `0x8038d8d0`, below the fixed low-bank end `0x81800000`. The compressed BSS interval includes clear-loop rounding. Kernel BSS is 164,464 bytes and resident `_text.._end` is 2,707,760 bytes. Relocated DTB is beyond the whole resident kernel; no second relocation or live decompressor/output overlap is needed. Kernel BSS may later reuse discarded decompressor code, as allowed by D08.

BOOTIMG has 2048-byte header/pages and 512-byte KERNEL/ROOTFS wrappers. Declared legacy addresses remain `0x10008000`/`0x11000000`/`0x10000100`; LK runtime entry/copy addresses are the physical map above. The complete partition-relative LK read ends at `0x0010a000`, exactly covered by the file and below `0x01000000`. All trailing read padding is explicitly zero. BOOTIMG partition is `[0x01d80000,0x02d80000)`; a later file write would occupy `[0x01d80000,0x01e8a000)` before any transport-specific erase behavior, which must be separately reviewed.

## Validation evidence and limits
  - [Actual symbol/layout/DT/package report](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m1-layout.json): PASS every D08 cap and collision/workspace/DTB-survival constraint, config/ELF/Image/gzip/DTB agreement, wrappers, checksums and overread/partition bounds.
  - [Reproducibility report](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m1-reproducibility.json): PASS, 11 outputs byte-identical in two separate clean build directories, including both ELFs, full config and all deployable bytes.
  - [Full source verification](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m1-source-verification.json): PASS, 91,166 files/links match the locked release archive (redundant relative-link syntax normalized by safe extraction). The only build-time overlay is the reviewed Kconfig line.
  - Nine tests pass with no skips in complete builds, including 22 real-artifact mutation cases (including rejection of the superseded UART3 base and IRQ), 25 package mutation/extent cases, fixed-policy boundaries and bounded gzip/cpio checks. QEMU 10.0.0 Cortex-A7 user-mode self-test passes. Kernel and dtc builds have no warning/error diagnostics.

Artifacts, both required ELFs, config, logs and provenance are retained locally under `out/m1-uart0-first-boot/` in the canonical Y2Linux checkout; caches/products are deliberately excluded from Git. Committed reports contain exact hashes and reproduction instructions. These are host verification results, not hardware execution, measured MemTotal, authenticated-loader acceptance, DMA containment or recovery backups. Runtime working set and board GIC/GPT/UART behavior remain untested. No full dt-schema claim is made.

## Stop boundary and proposed first experiment

Y2E-145 follow-up: NO-GO.[Updated launch assessment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md) identifies nominal 10-second watchdog arming on normal package LK initialization without an established handoff disable. The unchanged no-watchdog artifact is not approved for the requested 60-second run. Observation, installed authentication and current-device backups also remain missing. All 28 retained artifact members were rehashed successfully; no rebuild or product change occurred.

The [launch-gate review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-boot-launch-gates.md) leaves U07b (installed loader/authentication), U07c (inherited DMA/secure/SVC and watchdog state), U10a (physical console/voltage/routing and stock capture), and same-device independent backups/exact recovery procedure/trusted power unresolved. Owner-proven SPFT recovery remains accepted; no broad re-test is imposed.

After these proofs and separate authorization, the proposed experiment is one BOOTIMG-only deployment through the owner's proven, precisely recorded SPFT/DA route, one normal LK launch, captured Linux/CPU0/D08 diagnostics and at least three heartbeats within a reviewed 60-second observation window, followed by BOOTIMG-only stock restoration and checks. No preloader/LK, table, calibration, Android/system/userdata or rootfs change. The exact DA/entry/readback/wiring recipe remains blocked on those proofs; no verified temporary fastboot boot route is assumed. No experimental launch: all remaining gates and separate authorization are still required.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
