---
title: "Risk-accepted first-boot diagnostic result - Innioasis Updater"
description: "Risk-accepted first-boot diagnostic result <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-risk-diagnostic-result.html"
---

# Risk-accepted first-boot diagnostic result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Risk-accepted first-boot diagnostic result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Risk-accepted first-boot diagnostic result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-08, Y2E-150 [#18](https://github.com/SchulzCode/Y2Linux/issues/18). **GO for one risk-accepted BOOTIMG-only diagnostic experiment, pending separate owner hardware authorization. No flash, DA upload, experimental boot, physical pin probing or live framebuffer/register write was performed.**

This supersedes the old no-watchdog UART-only candidate for the proposed test. The original artifacts remain historical. [D11–D13 research and architecture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md), [exact experiment/restore procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment.md).

Research checkpoint: `3aeeb03`. Final implementation/build source: `1234f857810f979bae821649c3202c2a9f132e0a`. Git author/committer and GitHub account remain the owner's existing identity.

## Baseline, configuration and scope

Audited upstream v6.18, commit `7d0a66e4bb9081d75c82ec4957c50034cb0ea449`, Linux release 6.18.0-y2-m1. Clang/LLD 20.1.8, locked Alpine environment, Python 3.12.14, QEMU user 10.0.0 for ARM instruction/PID1 selftests. Full dependency revisions remain in `tools/build/inputs.lock.json`.

D09 Kconfig visibility overlay remains. Three further exact-base/exact-result patches add the explicit Y2 diagnostic Kconfig flag, include the project board helper in the built-in MediaTek object, and stop AP_RGU in compressed entry. Every overlay is applied with zero fuzz and checked hashes; the source cache remains pristine. The temporary helper includes use `/project`, the fixed read-only project mount in the locked build environment. This is not a generic upstream driver submission or an Android source port.

CPU0/ARMv7 little-endian/non-LPAE, static D08 memory, appended DTB enabled, ATAG-to-DTB import disabled, no SMP/HIGHMEM/hyp stub. UART0/IRQ51/26 MHz stays additional output, normal console 921600 8N1; earlycon retains LK baud. `CONFIG_Y2_BOOT_DIAGNOSTIC=y`; ordinary watchdog, display, USB, eMMC/block, network/audio/input and peripheral DMA stacks remain off. Procfs permits only the implemented volatile diagnostic writes from PID1; no persistent filesystem is mounted. Sysfs remains read-only. There is no shell, adbd, rootfs install, display reinitialization or automatic reset/rollback.

## Exact artifact inventory``````````````````

| Artifact | Bytes | SHA-256 |
| --- | --- | --- |
| Image | 2,543,296 | 7b678ab7a60068531a19112a4bcdc97e339d4e164385c1f6d6c79ae57f72919a |
| zImage | 1,076,776 | 4328b65b46eb0c7ee4fb176ea9b04fcd5f02edf120bd27b74380517c07a85364 |
| y2.dtb | 1,835 | 22b6f95f09802c3ef79f7f2bcfce5d5140f978877171ca69cefff2f22a61c07c |
| zImage-dtb | 1,078,616 | a4145743d79f210c4f400bbc0788017a4725fc9c2a839cc7ab1f7b370812afbb |
| init | 3,304 | 96e41536bd2bd6d419dbed394a963b278a7095719eeacdf39828904adbc4ff17 |
| initramfs.cpio | 4,608 | 78b72a316149f24fe29e03dc5a5bf48ae0778c34ac7be3b0320efd2294b8fc3d |
| initramfs.cpio.gz | 1,860 | 7600b0d245b0f3abe4dd8b7f385f31f2a4c83c9db1f0ca4d9453a2fcab9e376b |
| BOOTIMG.img | 1,089,536 | db7d8a5cf082b37f77c8732bd8e1ab742e4205f9383e421b051917f17364ab7e |
| kernel.config | 35,355 | bb3f61066c098bb3f0a601ea3cbc9f1b06e6a8ae43972dc9c2790ee882e2b43c |

DTB totalsize 1835, appended padded size 1840. Legacy Android page size 2048; MTK KERNEL/ROOTFS wrappers and zero-filled LK over-read tail validated. BOOTIMG is 1,089,536 bytes in the 16,777,216-byte EMMC_USER BOOTIMG partition, [0x01d80000,0x02d80000). It is unsigned. No stock loader was patched.

Local retained bundle: `/home/luca/Dokumente/Code/Y2Linux/out/m1-risk-accepted-diagnostic/`. 37 members have a SHA256SUMS inventory, including ELFs, config, image components, logs, input/overlay manifests, diagnostic sources, entry disassembly and FM boot/scatter convenience copies. The build source commit is in BUILD_COMMIT. Development outputs outside this bundle are not launch candidates.

## D08 and actual occupied intervals

DT RAM remains [0x80000000,0x81800000) plus [0x84000000,0x84080000), with [0x80000000,0x80004000) reserved. No imported LK memory ATAGs or RAM expansion.````````````````````

| Object | Half-open physical interval |
| --- | --- |
| zimage | [0x80008000,0x8010ee28) |
| appended_dtb | [0x8010ee28,0x8010f558) |
| image | [0x80008000,0x80274ec0) |
| resident_kernel | [0x80008000,0x8029d130) |
| relocated_copy | [0x80275700,0x8037cb60) |
| relocated_dtb | [0x8037c428,0x8037cb58) |
| compressed_bss | [0x8037cb58,0x8037cb78) |
| malloc | [0x8037db70,0x8038db70) |
| initramfs | [0x84000000,0x84000744) |
| lk_staging | [0x80007e00,0x80111600) |

Stack top 0x8037db70; workspace ends 0x8038db70, below the fixed 0x81800000 boundary. Kernel BSS 164,464 bytes; resident span 2,707,760 bytes. D13 maps only visible RGB565 pixels [0xbfb00000,0xbfb54600), 345,600 bytes, inside already excluded high display storage. I/O mappings round to pages, but writes stay strictly within the visible interval. This does not add allocator RAM.

## Validation and review
  - Two fresh builds `diagnostic-reviewed-1` and `diagnostic-reviewed-2` match

byte-for-byte across 12 outputs, including both ELFs, actual Image/zImage, DTB, init/archive, BOOTIMG and full layout report. Both complete build logs contain no compiler warnings/errors; all 11 tests pass in both trees.
  - Existing D08 boundary/arithmetic, actual-artifact corruption and BOOTIMG

wrapper/partition tests continue to pass (22 artifact mutations and 25 package cases). No validation threshold or RAM bound was loosened.
  - New compiled policy test rejects wrong/changed base, dimensions, offset,

stride, format/source/alpha/key state, enabled watchdog, stopped/wrong DSI modes and invalid stage sequences. All five pixel patterns are checked at the exact visible-buffer bounds, with sentinel protection.
  - Actual emitted ARM watchdog bytes and continuation branch are validated.

QEMU executes the real block including the branch over linker padding against mock registers for four initial MODE values; r7/r8/r9 preservation and keyed enable-bit clearing pass. This is not a watchdog hardware model.
  - Manual final disassembly: stop at zImage offset 0x90, write at 0xa4, readback

at 0xac, fail loop at 0xb4, branch at 0xb8 to continuation 0xc0. Loader r1/r2 have already been preserved in r7/r8; MMU-off SVC contract is unchanged. A development padding fall-through hazard was caught before approval, fixed, and both final builds rerun. No affected development image was flashed.
  - PID1 ARM EABI selftest passes. Source review confirms writable volatile

procfs for the root/PID1-only stage endpoint, checked timed heartbeat sleeps, finite ten-transition protocol and no block/device/reset operations.
  - All 91,166 source files/links match the audited upstream archive. All 24 FM

ROM files plus SPFT executable and bundled DA rehash successfully. Local preloader/LK files are byte-identical to the baseline; no device write occurred.

[Layout report](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/risk-diagnostic-layout.json), [reproducibility](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/risk-diagnostic-reproducibility.json), [source verification](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/risk-diagnostic-source-verification.json). Private research captures and exact artifact slices are indexed in [capture-index.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/capture-index.tsv).

Reproduce in the locked environment with unused output directories:`python3 tools/build/prepare.py --offline python3 tools/build/full_source_check.py python3 tools/build/run.py --output out/repro-a -- sh /project/tools/build/build.sh python3 tools/build/run.py --output out/repro-b -- sh /project/tools/build/build.sh python3 tools/observation/verify_recovery.py`

For an empty cache, run prepare.py without --offline to fetch checksum-locked inputs first. Source/overlay mismatch or any D08 failure stops the build; never enlarge memory automatically.

## Risk-accepted launch assessment

Watchdog: the upstream driver cannot cover its pre-probe interval. The minimal entry stop uses the upstream/LK MODE operation before inflation and rechecks it before any visible stage. Other watchdogs, pending resets and protected register access remain unmeasured risks.

Observation: inherited sync-pulse DSI video, LK layer 2 at 0xbfb00000, 480x360 RGB565/960-byte rows, with final normal boot convergence to that base and no normal backlight-off. Read-only register guards precede every paint; only pixels are written. This is a firmware/source-supported path, **not an already successful Linux hardware capture**. Guard refusal can be silent without UART; no guessed register reinitialization is attempted.

Expected sequence: LK logo → kernel black/white stripes → PID1 green after a short hold → alternating white half on green every five seconds (ten times) → terminal checkerboard. A 60-second host observation cutoff includes startup latency and takes precedence over completion of all stages. At least three ordered timed heartbeat changes are the minimum useful success evidence.

Failure after a successful stop can remain frozen indefinitely. No automatic rollback/reset or Linux power-button driver exists. Before entry/rejection or if the stop fails, inherited watchdog IRQ/dual-mode resets may occur; exact reset timing is not promised. The owner must use the proven power/recovery sequence and restore FM BOOTIMG only after the single trial.

Fallback FM boot.img SHA-256: `5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6`. It restores known-good FM boot state, not exact current kernel/ramdisk changes. The owner accepts rejection, failed boot, incomplete installed-loader/DMA/ secure-state proof and possible need for later FM recovery. Full-ROM recovery can lose system/userdata and requires separate authorization; unique calibration cannot be recreated from a generic ROM. All non-BOOTIMG targets remain forbidden.

**GO means the bounded risk-accepted diagnostic is ready for separate owner review/authorization. Hardware success, stock serial capture and M1 hardware completion are still unproved.** The next action is the prepared Y2B-240 issue, not further features, automatic flashing or an unattended reset loop.

Execution checkpoint: [Y2B-240 / #19](https://github.com/SchulzCode/Y2Linux/issues/19), awaiting separate owner hardware authorization.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
