---
title: "Stock boot structure and loader handoff - Innioasis Updater"
description: "Stock boot structure and loader handoff <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-boot-chain.html"
---

# Stock boot structure and loader handoff - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Stock boot structure and loader handoff

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Stock boot structure and loader handoff > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-08 hardware update: [Y2B-240 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment-result.md) records owner-observed green PID1 evidence and successful BOOTIMG-only Android recovery using the owner-selected boot-adb image. Timed heartbeats, cutoff and exact FM restoration were not verified. Historical pre-launch unknowns below must be read with this narrower new evidence.

Date: 2026-09-08. [Y2E-125](https://github.com/SchulzCode/Y2Linux/issues/6) extends [Y2E-115](https://github.com/SchulzCode/Y2Linux/issues/4). Status: package loader contract CONFIRMED by static analysis; Linux launch INFERRED, not tested. Captures: `20260908-boot`, `20260908-handoff`. Original image analysis below is retained with its original package scope.

## Exact package input analysis

Both original images were read without modification. The existing `tools/adb/build_adb_boot.py` parser was inspected and imported with Python bytecode writes disabled; no build/patch/pack entrypoint ran. Parser source SHA-256: `4ad50feb81ede3f83419bdcc8e395fda1b20cd45303b210403fc85ad39e54fc3`. Host-only scratch analysis checked component bounds and decompressed gzip/parsed cpio in memory with size limits. No extracted program was executed and no archive-controlled pathname was written to the filesystem.

| Field | Stock boot | Stock recovery |
| --- | --- | --- |
| Image bytes | 5,654,528 | 6,039,552 |
| Page size | 2,048 | 2,048 |
| Kernel offset / size | 2,048 / 4,942,168 | same |
| Ramdisk offset / size | 4,945,920 / 707,660 | 4,945,920 / 1,092,308 |
| Second stage / declared DT / trailing bytes | 0 / 0 / 0 | 0 / 0 / 0 |
| Header command line | empty | empty |
| Ramdisk MTK wrapper name | ROOTFS | RECOVERY |
| Cpio entries including trailer | 44 | 61 |

The wrapper magic is `0x58881688`. The kernel wrapper is 512 bytes and names KERNEL; its declared payload is 4,941,656 bytes. The boot ramdisk's declared gzip payload is 707,148 bytes; recovery's is 1,091,796. Lengths and gzip termination validate. The reference helper rejects RECOVERY by design; analysis therefore checked its actual wrapper magic/name/length separately and used only the existing cpio parser. This is not an image modification.

Both extracted wrapped kernels exactly match `OriginalFirmware/kernel` and `kernel_eastaeon82_wet_kk.bin`, SHA-256 `b026b2859e9bf977eca0b5f8506f67024143fbadb18e9c28c23f5e7b6a51118d`. Each ramdisk exactly matches its corresponding loose package file. Gzip begins at wrapped-kernel offset 19,172 and produces 10,544,388 bytes, SHA-256 `5f284fade5e9ab4f146ed9e7bd2464d1e1a4d04a8eafb43abb4a909738666355`. This exactly reproduces `reverse/ghidra/exports/y2-kernel-image.bin`, establishing that derivative's lineage from this stock kernel. The symbolized ELF's hash is verified separately; symbol recovery itself was not rerun.

## Header/runtime addresses: resolved by LK analysis

Both headers record kernel load `0x10008000`, ramdisk load `0x11000000`, second-stage address `0x10f00000` despite zero second-stage size, and tags `0x10000100`. The current `/proc/iomem` instead reports System RAM at `0x80000000–0xbdffffff` plus `0xbf800000–0xbf9fffff`, kernel code at `0x80008000–0x80955fff`, and kernel data at `0x8098e000–0x80dc818f`.

The newly traced normal LK path hardcodes kernel entry `0x80008000`, ramdisk destination `0x84000000` and tags `0x80000100`; these choices do not come from the header address fields. No RAM alias or arithmetic translation is needed to explain the discrepancy. The ramdisk destination in particular is not the header value plus `0x70000000`. The historical reason for the packager's template addresses is unknown but no longer blocks the strategy. Memory exclusions remain unresolved; do not infer usable DRAM solely from MemTotal.

## Config and device-tree search limits

The exact whole boot/recovery images, wrapped kernels and independently decompressed kernel were searched for `IKCFG_ST`, `IKCFG_ED` and big-endian FDT magic `d00dfeed`: no occurrences were found in these scopes. The legacy parser's declared DT size is zero and there are no trailing bytes. Runtime exported config/DT paths are unavailable. `dtc` and `extract-ikconfig` are not on this host's PATH; no tools were installed and no DTS was authored.

Result: no candidate found in the stated inputs/search, not proof that a DT/config cannot exist in another artifact or vendor encoding. Y2E-125 now confirms ATAG construction in the package LK and compiled board fixups in the original kernel. Never invent missing nodes or pin numbers.

## Ramdisk observations

Stock defaults set `ro.secure=1`, `ro.debuggable=0`, `ro.adb.secure=1`, and USB `mass_storage`. The current device reports `mass_storage,adb`; exact installed boot lineage is still unconfirmed. The package fstab describes `/emmc@usrdata` and writable protect filesystems. Init references WMT/connection loaders and `/system/etc/firmware/`. The `service console /system/bin/sh` entry is disabled and its start trigger requires `ro.debuggable=1`, unlike the observed 0. This does not establish a usable serial console, physical UART routing or safe access. The ttyMT2 connectivity comment is not a verified diagnostic console pinout.

## Historical Y2E-115 review

Y2E-115 is complete as bounded structure/availability research. Exact stock kernel and ramdisk lineage is established; header/runtime address interpretation and missing config/DT evidence block Linux boot construction. Y2E-120 may now assess recovery capability using these findings. It may not execute a flasher, upload a download agent, change boot mode or read/write partition contents.

The remainder supersedes the unresolved address/ATAG assessment above while preserving its history.

## Y2E-125 provenance and method

The owner reports successfully flashing this Y2 with SP Flash Tool and `y2_v3.2.0_FM-20260813/`. All 24 current ROM files were rehashed in [handoff-artifacts.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/handoff-artifacts.tsv). This is strong same-device recovery evidence, not proof of exact currently installed partition bytes. See [recovery.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md).

FM and OriginalFirmware LK are byte-identical: 242,440 bytes, SHA-256 `bb1a93b4c1f02eab09ebad1314a8fdc25d94d3ca99771fc14e21cb18a289964a`. Preloaders differ: FM `1df1b62498754aab0c7ddc80a79d310a92fcf81f29b515730c562aaeeb6a884a`; OriginalFirmware `4621b206b4211bf6f4bc14b7a52564a54ec87b0386fed0e3f6679f3f34caa1e7`. Do not mix them.

Capstone 5.0.7 was used for offline ARM/Thumb decoding. Literal/GOT annotations are navigation aids, not a decompiler proof: linear dumps include data and wrong-mode spans. The register flows cited below were checked manually against bytes, callers and callees. Research helpers, disassembly and provenance remain private and are pinned by [capture-index.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/capture-index.tsv). No device command or firmware execution occurred in this investigation.

## Most likely chain`MT6582 Boot ROM → stock preloader (early setup / DRAM) → UBOOT partition / stock LK at 0x81e00000 → BOOTIMG: legacy Android header + MTK KERNEL / ROOTFS wrappers → ARM zImage at 0x80008000 r0 = 0, r1 = 0x19b6 (6582), r2 = 0x80000100 (ATAGs) external ramdisk = 0x84000000 → kernel decompression / board initialization → ramdisk /init`

ROM hardware-boot selection remains INFERRED; exact eMMC hardware-boot configuration is unobserved. Preloader-to-LK and normal LK-to-kernel paths are CONFIRMED within the analyzed binaries.

FM preloader GFH fields record load address `0x00200d00`, content/jump offset `0x300`, file length `0x1d640`; its build string is `20260813-133850`. File `0x651e–0x654a` supplies `0x81e00000` to the UBOOT load path and passes a `0x6c`-byte argument structure to the jump routine. Thumb veneer `0x2178e4` switches to ARM and branches to `0x2010e0` (file `0x3e0`): `mov r4,r1; mov r5,r2; mov pc,r0`. LK saves incoming r4 at `0x81e00020`, copies the structure, and reads rank count/sizes from offsets `0x18`/`0x1c`. Preloader DRAM training paths corroborate its role; actual runtime rank values are unknown.

LK has a 512-byte MTK wrapper. Reset/relocation fixes its base at `0x81e00000`, clears BSS through `0x81e55434`, and enters predominantly Thumb code. LK file offset = runtime address − `0x81e00000` + `0x200`; GOT base is `0x81e3aef8`.````````````````````````````````````````````

| LK address / file offset | Confirmed normal-path behavior |
| --- | --- |
| 0x81e01754 / 0x1954 | Validates legacy Android header; calculates component pages using 2,048-byte arithmetic. |
| 0x81e01826–0x81e0182e / 0x1a26–0x1a2e | Stores hardcoded kernel address 0x80008000, not header kernel_addr. |
| 0x81e183e4–0x81e18404 / 0x185e4–0x18604 | Normal BOOTIMG caller passes 0x80008000 to header/payload loaders. |
| 0x81e01c6c–0x81e01cb8 / 0x1e6c–0x1eb8 | Skips four 512-byte sectors of Android header; reads into 0x80007e00, leaving the 512-byte KERNEL wrapper immediately before the real zImage at 0x80008000. |
| 0x81e01cc2–0x81e01cee | Validates KERNEL/ROOTFS MTK headers and records inner payload lengths. |
| 0x81e1841a–0x81e18432 / 0x1861a–0x18632 | Copies inner ROOTFS from staging after the page-aligned kernel to 0x84000000. |
| 0x81e18476–0x81e18490 | Passes kernel, tags, internal command line, machine ID and ramdisk pointer/length to boot_linux. Machine-ID helper 0x81e1ef80 returns 0x19b6. |
| 0x81e181f8–0x81e181fe / 0x183f8–0x183fe | Sets r0=0, r1=machine ID, r2=tags; blx r8 launches ARM zImage. |

FM BOOTIMG is 5,656,576 bytes: wrapped kernel 4,944,888 bytes, wrapped ramdisk 707,837 bytes at file offset 4,947,968, 2,048-byte pages. Its inner kernel/ramdisk lengths are 4,944,376 / 707,325. Header addresses match the old package, command line is empty, second/declared DT sizes are zero. FM recovery is 6,041,600 bytes, uses the same kernel and a RECOVERY wrapper.

For wrapped sizes K and R and page P=2,048, LK computes `(ceil(K/P) + ceil(R/P) + 2) * P` as its payload-read length after skipping the header. Its read reaches beyond the standalone image into partition padding. A later artifact verifier must account for that read footprint, the 16 MiB BOOTIMG boundary, LK live memory, staging, decompression/DT workspace and ramdisk destination. File-size-only validation is insufficient.

## Tags, command line and rootfs

boot_linux (`0x81e17fe4`) writes CORE `0x54410001` with a two-word header. Helpers at `0x81e0204c`, `0x81e02278`, `0x81e022d0` write MEM `0x54410002`, CMDLINE `0x54410009` and INITRD2 `0x54420005`; INITRD2 carries the relocated inner ramdisk pointer/length. Vendor tags `0x41000802–0x41000806` and a vendor interpretation of `0x54410008` carry additional information, including framebuffer data. Two zero words end the list. This normal path is ATAG, not a loader-supplied FDT.

LK passes its internal writable command-line buffer at `0x81e35aac`, initially `console=tty0 console=ttyMT3,921600n1 root=/dev/ram`. It adds LCM/fps, boot timing/reason and conditional UART/hibernation fields. A conditional helper can change ttyMT to port 0. The full live command line is unknown; existing non-root access was denied. Changing the Android header alone does not control this path's command line. No string proves accessible UART pins.

ROOTFS is an MTK payload label, not a demand for Debian, ext4 or a partition called ROOTFS. Stock transports a gzip/cpio ramdisk; Android /init later mounts Android storage. A Linux initramfs with its own /init can supply first userspace without Android. LK need not understand the distribution filesystem.

## Y2E-125 memory findings (superseded by Y2E-130)

Archived iomem reports 992 MiB at `0x80000000–0xbdffffff` plus 2 MiB at `0xbf800000–0xbf9fffff`. Within a hypothesized 1 GiB window, `0xbe000000–0xbf7fffff` and `0xbfa00000–0xbfffffff` are unaccounted for. Rank topology and the meaning of every hole are not established. System RAM reporting is not an exhaustive reserved/DMA-region inventory.

LK builds MEM tags from preloader rank sizes. The symbolized OriginalFirmware kernel proves that `mt_fixup` edits those sizes, consumes vendor display information and calls `DISP_GetVRamSizeBoot` when shrinking the final bank. `mt_reserve` invokes connectivity and modem reservations: connectivity requests 1 MiB with 1 MiB alignment; modem size is configuration-dependent with 32 MiB allocator alignment. These do not establish physical carveout addresses.

FM's decompressed kernel is independently hashed: 10,544,516 bytes, SHA-256 `7287acf1b397d243c927dde5c6ef9d5d871c9c158207cdd98e0e820923f4c197`. Same-offset comparisons find mt_reserve identical but several other old symbol windows different. Old symbols must be remapped before claiming exact FM reservation functions. Stock-family analysis explains the risk, not the complete current map.

LK performs platform cleanup, cache clean/disable and MMU disable before entry (`0x81e1686c`, `0x81e16ed0`), consistent with ARM boot requirements. This does not prove all DMA engines quiescent. Active framebuffer, preloader scratch/possible secure-world memory and retained bus masters need bounded evidence.

A security-policy function (`0x81e207d0`) precedes loading. It has both no-check and authenticated-partition paths dependent on configuration/hardware state. Owner-confirmed stock flashing does not prove acceptance of arbitrary unsigned kernels. Exact installed loader/policy evidence is a separate pre-launch requirement; no security state was changed or bypass attempted.

## Y2E-125 candidate architecture and evidence boundary

D05: preserve preloader/LK; use a legacy 2 KiB-page BOOTIMG with upstream 6.18 ARM zImage + appended Y2 DTB inside KERNEL, and a small external initramfs inside ROOTFS. Begin on CPU0 with a bounded memory description and observable console, preserving eMMC. No old Android board-file port is presently justified. The reported Debian/replacement-BOOTIMG approach is consistent with this mechanism, but supplies no verified patch set, logs or upstream-version proof.

The [upstream audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flinux-6.18-support.md) confirms appended-DTB and ATAG conversion support. Conversion imports raw MEM tags but not vendor reservations, so enabling it blindly could overwrite a conservative DT memory map. Remaining architecture choice: import tags with adequate exclusions, or use a completely specified static memory/initrd description without ATAG import. Experiment command-line policy must explicitly override Android defaults.

Smallest remaining artifact-design proof: establish the exact safe initial RAM envelope and required exclusions at LK exit, including inherited DMA. This fixes DT-memory/ATAG-import policy and validates every load/decompression/initrd interval. A proven conservative envelope may suffice; full peripheral reverse engineering is unnecessary. Remap the FM reservation functions and review existing memory/display evidence next; obtain a passive stock boot log only when its observation route is established.

Installed loader/security state, a usable physical console and recovery backups separately gate launch. There is no honest single-unknown claim for overall readiness. No kernel/DTS change, Linux artifact or implementation-ready issue was created.

## Y2E-130: fixed initial RAM policy

[Y2E-130](https://github.com/SchulzCode/Y2Linux/issues/7) supersedes the memory uncertainty and pending ATAG choice above for offline artifact design. The complete [initial RAM policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md) is authoritative for FM symbol remapping, evidence confidence, exact interval formulas and rejection limits.

FM kallsyms were recovered independently (54,692 symbols). FM `mt_fixup`/`mt_reserve` and allocator flows establish normal framebuffer subtraction, connectivity's 1 MiB steal and the default 22 MiB modem + 2 MiB shared allocation. The retained iomem also reports a 5 MiB `mtkfb.0` resource at `[0xbfb00000,0xc0000000)`, omitted in the earlier summary. Modem/connectivity placement explains the remaining holes but is still inferred from defaults plus runtime layout. Individual live preloader rank sizes are not known.

D08: describe only `[0x80000000,0x81800000)` plus `[0x84000000,0x84080000)` in DT (24.5 MiB); retain the first 16 KiB for boot data. Preserve appended DTB, disable `ARM_ATAG_DTB_COMPAT`, specify actual initramfs start/end in `/chosen` and use controlled DT bootargs. LK header addresses and command-line tags do not choose these values. Kernel+DTB cap 6 MiB, whole decompressed kernel including BSS cap 14 MiB, external compressed initramfs cap 512 KiB. Exact decompressor relocation/workspace checks and LK overread checks are mandatory; these caps do not describe an already built image.

LK control state starts at `0x81e00000`, heap at `0x81e55434`; heap upper/live extent remains unresolved and broadly excluded. Display initialization also records a scratch pointer 4 MiB below its framebuffer. Preloader scratch/page-table placement is near DRAM top. This policy excludes those locations and all high modem/connectivity/possible secure storage, without asserting that iomem enumerates every bus-master target.

The loader has an eMMC DMA stop-and-idle-wait path, but final interrupt/cache cleanup is not proof that all DMA or secure-world accesses stop. U07a memory policy is resolved; U07c inherited DMA/secure-state assurance remains a launch gate. Offline work can be specified against the fixed policy; device launch still needs installed-loader/security, console, recovery/backup and power evidence. No Linux artifact, DTS/kernel implementation or implementation issue was created by this research.

## Later persistent rootfs

The [partition map](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fpartition-map.md) permits investigating reuse of a specifically selected filesystem after backup and authorization: ANDROID (runtime p5, physical `0x5180000`, 820 MiB), CACHE (p6, `0x38580000`, 126 MiB), USRDATA (p7, `0x40380000`, 800 MiB) and FAT (p8, `0x72380000`, larger media area). Upstream numbering and vendor aliases must be verified anew; `/emmc@usrdata` is not an upstream interface.

Space after BOOTIMG is not disposable as a whole: RECOVERY, SEC_RO, MISC, LOGO, EBR2 and EXPDB intervene before ANDROID. Preserve recovery, tables, security and calibration. Later initramfs can mount a specifically reviewed filesystem and switch root after MMC/clock/power support and capacity are proven. Debian is an engineering lead, not a selected release or demonstrated fit for these small partitions. No rootfs write/repartitioning decision is made in M0.

## M1 offline artifact boundary (2026-09-08)

The owner authorized direct offline implementation after D08. The [first-boot result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md) now supplies actual Image/zImage/DTB/initramfs/BOOTIMG hashes and symbol-derived intervals. Legacy wrapper/header semantics were independently checked against FM, including its wrapped-section SHA-1 ID. The output includes zero padding through LK's full extra read. No installed loader was changed or device accessed.

One Kconfig prompt-visibility patch is needed to enforce D08's no-hyp option on v6.18; [D09](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fkernel-policy.md) documents the source review and exact change. Header `0x100...` fields remain compatibility metadata, while physical entry/copy addresses remain `0x80008000`/`0x84000000`. No legacy board-file code or ATAG import is added. [Launch-gate research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-boot-launch-gates.md) retains the installed-authentication, DMA/secure-entry, physical-console and backup/recovery requirements. Earlier no-artifact statements above describe their dated research checkpoints.

## Y2E-140 console correction (2026-09-08)

The package default `ttyMT3` string is not the installed controller selection. Fresh read-only stock console/sysfs/resource evidence identifies ttyMT0 / hardware UART0 at 0x11002000. Remapped FM driver code confirms index-to-MMIO identity. This matches the conditional UART0 path in package LK; exact installed loader and live preloader arguments remain U07b. [Full evidence, expected 1.8 V domain/921600 8N1, physical blockers and alternative research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md). D10 updates/revalidates only the DT controller/IRQ and associated packaging. No handoff, memory or loader change, and no actual serial boot capture yet.

## Y2E-145 installed-policy and watchdog boundary

[Launch readiness](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md) now traces FM ROM_INFO m_sec_boot=0x22 to LK's hardware security-bit decision, rather than assuming that value disables verification. Normal platform initialization also arms a nominal 10-second AP watchdog interval; the identified disable calls belong to Download/Fastboot paths. No normal-handoff disable is established. This is adverse evidence for the current no-watchdog candidate's proposed 60-second run. Installed loader identity/security and inherited DMA/secure state remain unproved. NO-GO; no image, loader or memory-architecture change.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
