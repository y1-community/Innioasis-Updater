---
title: "Initial Linux RAM policy - Innioasis Updater"
description: "Initial Linux RAM policy <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-initial-ram-map.html"
---

# Initial Linux RAM policy - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Initial Linux RAM policy

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Initial Linux RAM policy > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

DEV-01 supersedes D08 for the owner-authorized integrated development candidate. See [practical RAM reconciliation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdevelopment-memory.md) for the built 992 MiB bank, explicit reservations, HIGHMEM and remaining physical qualification. Dated D08 constraints below remain historical provenance.

2026-09-10: [additional history](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md) records a stock modem load overwriting an excluded HYP trace/stub region at be000000/be800000. This strengthens the containment warning, not a heap bound or new free interval. #22 still needs LK lifetime, DMA and ARM lowmem/HIGHMEM reconciliation; D08 stays.

2026-09-09 donor review: the new 6.12 board DT agrees with the main 992 MiB stock bank, but its chosen connectivity reservation differs from our inferred stock allocation. [Reconciliation and large-bank direction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md%23ram-reconciliation&anchor=ram-reconciliation) now guide #22. D08 remains the current implementation until loader/DMA and ARM lowmem/HIGHMEM validation establish its successor.

Current hardware result: [owner-observed M1 runtime success](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md) confirms Linux 6.18, native PID1, increasing BEAT/uptime, working sleep, proc/sysfs mounts, CPU0, D08 RAM visibility, framebuffer diagnostics and stopped-watchdog status. M1 core achieved. Exact flashed hash and unreported diagnostic fields remain unverified. Earlier dated statements below are historical.

D13 diagnostic scope clarification: ordinary DT RAM, reservations and every D08 artifact cap remain unchanged. The owner additionally authorized a strictly guarded write-only pixel aperture [0xbfb00000,0xbfb54600) inside the excluded high framebuffer. It is mapped as I/O, never offered to the allocator; no display scratch or other high RAM is reclaimed. See [D13](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md).

Date: 2026-09-08. [Y2E-130](https://github.com/SchulzCode/Y2Linux/issues/7), following [Y2E-125](https://github.com/SchulzCode/Y2Linux/issues/6). D08: static DT memory, 24.5 MiB initially; no LK ATAG import. This closes U07a's offline memory-policy decision. It is a conservative design supported by package analysis and retained runtime observations, not a tested Linux RAM map or permission to boot. Inherited DMA/secure state remains a launch gate (U07c). All intervals below are physical, hexadecimal and half-open: `[start, end)`.

## Evidence and confidence

Private capture group `20260908-ram-map` is pinned in [capture-index.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/capture-index.tsv); upstream source hashes in [linux-6.18-sources.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/linux-6.18-sources.tsv). No device command, Linux build, DTS/kernel implementation, image modification or flasher execution occurred. The [boot-chain](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fboot-chain.md) identifies the exact FM inputs and original loader offsets.

FM wrapped kernel SHA-256 `8f250f5ce97ffd2d2a59455c0fb9eceff7e32b0e1ba34de84ae0d551a9f9e48e`; independently decompressed 10,544,516 bytes, SHA-256 `7287acf1b397d243c927dde5c6ef9d5d871c9c158207cdd98e0e820923f4c197`. Kallsyms recovered 54,692 symbols from these FM bytes, with addresses at decompressed offset `0x7649b0`, names `0x79a050`, token table `0x82d4b0`, token index `0x82d890`. Function addresses below are FM virtual addresses; file offset in the decompressed kernel is VA minus `0xc0008000`.````````````````````````````````````````````````

| Function | FM address | Meaning established from instructions |
| --- | --- | --- |
| mt_fixup | 0xc001cc68 | Processes MEM/vendor tags and edits bank sizes before ordinary ARM memory initialization. |
| mt_reserve | 0xc001d344 | Calls connectivity reserve first, modem reserve second. |
| parse_ccci_dfo_setting | 0xc004457c | Applies modem enable, size and shared-memory settings; rounds each size to 2 MiB; sums enabled MD1 sizes. |
| ccci_md_mem_reserve | 0xc0044524 | Allocates configured total with 32 MiB alignment. FM global base is 0xc0a25698, total at +0x3c8. |
| DISP_GetVRamSize | 0xc05128d4 | Computes display storage from selected driver/buffers, rounds to MiB and caches it. |
| DISP_GetVRamSizeBoot | 0xc051296c | Selects display path and returns the rounded amount; unknown-panel fallback actually returns 0x1400000 (20 MiB), despite a misleading 8 MiB log string. |
| mtk_wcn_consys_memory_reserve | 0xc0975948 | Requests 1 MiB with 1 MiB alignment. |
| arm_memblock_steal | 0xc0959c14 | Allocates, then calls memblock_free and memblock_remove; stolen memory disappears from ordinary RAM inventory. |
| memblock_find_in_range_node | 0xc00f9104 | Reverse free-range traversal, candidate (range_end - size) & -alignment; explains high-address carveouts. |

The old display addresses `0xc05124f8`/`0xc0512590` are not reused. Some functions retain their old entry address while their literal/global targets change. FM disassembly, default DFO values and symbol recovery are retained separately.

## Preloader banks and stock reservations

CONFIRMED package construction: FM preloader passes rank count at boot-argument offset `0x18`, up to four sizes at `0x1c..0x28`. LK `0x81e00174` copies these and creates contiguous bank entries beginning at `0x80000000`: bank i begins at `0x80000000 + sum(size[0:i])`. `0x81e0204c` emits MEM ATAGs from this table; `0x81e00268` sums it. Rank count and the individual live sizes have not been captured. A merged Linux System RAM resource cannot recover physical rank topology.

CONFIRMED retained runtime:`20260908-stock/iomem.stdout` reports `[0x80000000,0xbe000000)` and `[0xbf800000,0xbfa00000)` as System RAM, plus `[0xbfb00000,0xc0000000)` as `mtkfb.0`. The latter is an observed 5 MiB device resource; the preceding Y2E-125 account omitted that final line. Kernel code/data lie below `0x80dc8190` in that capture. This is a retained observation, not a new capture or proof that the running kernel is byte-identical to FM.

CONFIRMED FM normal fixup: MEM sizes are capped against an aggregate `0x80000000` budget (2 GiB, not the physical RAM base). The last accepted MEM tag is retained. `mt_fixup` zeroes its PMEM-size variable and subtracts `DISP_GetVRamSizeBoot()` from that last bank on the ordinary path (`0xc001ce74..0xc001ceb4`). Vendor tag `0x54410008` supplies framebuffer base/size at +`0x10`/+`0x14`; this is vendor use of an otherwise standard tag number. Factory mode 4 has an additional graphics reservation; it is not the selected normal BOOTIMG contract. DFO/vendor boot inputs can alter choices, so the default model is not asserted for every boot mode.

The default DFO block at FM `0xc09ab420` sets MD1 enabled, MD1 size `0x1600000` (22 MiB), shared size `0x200000` (2 MiB); MD2/MD5 disabled. Enabled MD1 therefore reserves 24 MiB including shared memory, not 24 MiB plus another shared allocation. With 1 GiB contiguous DRAM, a 5 MiB framebuffer and no intervening high allocation, the traced order reproduces every runtime hole:``````````

| Interval | Size | Classification / reason |
| --- | --- | --- |
| [0x80000000,0xbe000000) | 992 MiB | CONFIRMED runtime System RAM; only a small low subset is admitted initially. |
| [0xbe000000,0xbf800000) | 24 MiB | INFERRED modem allocation from FM defaults, top-down allocator and exact runtime hole. No runtime modem-base register or allocation log captured. Default subdivision would be 22 MiB private + 2 MiB shared; hardware remap details remain unproved. |
| [0xbf800000,0xbfa00000) | 2 MiB | CONFIRMED runtime System RAM left by the modem's 32 MiB alignment. Deliberately excluded initially. |
| [0xbfa00000,0xbfb00000) | 1 MiB | INFERRED connectivity allocation from first top-down steal, matching the runtime hole. |
| [0xbfb00000,0xc0000000) | 5 MiB | CONFIRMED runtime framebuffer resource; LK also computes framebuffer as DRAM end minus rounded display size. Actual last LK register contents are not captured. |

Thus 1 GiB contiguous backing is strongly supported, but a live preloader rank dump is unnecessary for this reduced policy. None of the inferred high carveouts is exposed even if the exact default attribution later changes.

## Loader, display scratch, secure state and DMA
  - LK executable/data/BSS and initial stacks/page table occupy the region beginning `0x81e00000`, with BSS end `0x81e55434`. Its heap initialization at `0x81e1b4a4` uses that BSS end as heap start. The runtime heap upper limit and live allocation extent are unresolved. The policy excludes everything above the low bank except a prefix of LK's own ramdisk destination; it does not guess that the heap ends at `0x82000000`.
  - LK display initialization `0x81e0a470` receives framebuffer base, stores a second scratch pointer framebuffer minus 4 MiB (`0x81e0a48a..0x81e0a4a0`) and programs display buffers from framebuffer-derived addresses. For the observed framebuffer this pointer is `0xbf700000`, outside the named mtkfb resource. Its full lifetime/extent is unresolved. This is an additional reason not to reclaim the high alignment gap or assume the 5 MiB resource describes all inherited display memory.
  - FM preloader `0x20289c` computes total D from DRAM ranks. At `0x2028fe..0x202912`, its DRAM scratch base is `0x80000000 + D - 0x500000`, structure length `0x194a78`, and page-table base is `0x80000000 + D - 0x100000`. For 1 GiB: scratch `[0xbfb00000,0xbfc94a78)`, page-table base `0xbff00000`. These are earlier-phase occupants later overlapped by framebuffer use, not additive permanent carveouts. All are excluded. The printed maximum-TEE-size argument is zero in this build; this does not prove absence of secure/shared RAM or prove installed firmware state.
  - LK normal eMMC DMA paths at `0x81e06358..0x81e0636c` and `0x81e063b6..0x81e063ca` start, wait, then invoke `0x81e05334`. That stop helper sets controller DMA control +`0x98` bit 1, waits for DMA status +`0x9c` bit 0 to clear, switches controller configuration bit 3, and clears transfer state. This establishes an actual storage-DMA stop mechanism in those paths, stronger than a successful read return alone; it is not a complete proof for every controller/path or the installed loader.
  - Final platform cleanup `0x81e00458` turns LEDs off and masks/drains GIC interrupts. Cache/MMU cleanup is separate. Interrupt masking and excluding RAM from DT do not stop DMA. Display fetch may remain live; modem/connectivity activity and secure-world behavior at entry have not been observed. The [ARM boot protocol](https://github.com/torvalds/linux/blob/v6.18/Documentation/arch/arm/booting.rst) requires DMA quiescence. Full bus-master quiescence or proven containment remains U07c before any hardware launch. Merely disabling Linux drivers is insufficient.

No independent secure carveout is confirmed in the selected low bank. Unknown secure aliases or DMA destinations cannot be disproved by iomem; this is a residual launch risk, not permission to invent a low-memory reservation. The admitted regions have positive stock RAM/load-use evidence, and all identifiable loader/high storage is outside them.

## D08: first-boot memory and import policy

The complete DT memory description shall contain exactly two ranges:````

| Admitted interval | Size | Use |
| --- | --- | --- |
| [0x80000000,0x81800000) | 24 MiB | Kernel, decompressor, DTB and ordinary Linux allocations after boot reservations. |
| [0x84000000,0x84080000) | 512 KiB | External initramfs destination and its small remaining/freeable RAM. Entire interval is within the FM stock inner ramdisk copy footprint (707,325 bytes). |

This is 24.5 MiB described RAM, not predicted MemTotal. Reserve `[0x80000000,0x80004000)` (16 KiB) permanently in the FDT reservation map for stock tags/low boot data. Kernel/page-table/FDT/initramfs reservations are additional; Linux handles their actual occupied lengths. The initramfs bank must remain ordinary mapped RAM, not `no-map`, so generic initrd validation and freeing work. Its fixed capacity is deliberately below stock's known copy length; no larger `0x840...` allocator bank is assumed safe.

Exclude `[0x81800000,0x84000000)` (40 MiB) and `[0x84080000,0xc0000000)` (959.5 MiB within the inferred 1 GiB). Omit them from all memory nodes; do not advertise 1 GiB and hope a `mem=` argument truncates it. The second exclusion includes otherwise usable stock RAM, loader heap uncertainty, modem/shared/connectivity, display and preloader storage. No hot-add/reclaim decision is made. Physical addresses outside the known DRAM window are not proposed RAM.

Set `ARM_APPENDED_DTB=y`, `ARM_ATAG_DTB_COMPAT=n`. The decompressor uses the appended DTB, replacing r2 for kernel entry without importing MEM/CMDLINE/INITRD2. The v6.18 converter would import raw MEM but omit vendor reservations and could overwrite the static memory description. `mt_fixup`/`mt_reserve` are not carried into the upstream kernel; their intent is accounted for by the smaller map.

Use a controlled DT `/chosen/bootargs`, not LK's Android command line. Set the compiled fallback `CMDLINE` to `rdinit=/init` and select ordinary DT command-line precedence (`CMDLINE_FROM_BOOTLOADER`, no EXTEND/FORCE); here “bootloader” means the FDT selected by the decompressor. Because ATAG conversion is off, LK's tags do not enter this path. The memory contract prohibits `mem=`, `initrd=`, crashkernel, CMA pools or other arguments/nodes that change these intervals. Include `rdinit=/init`; console-specific arguments await the separately reviewed console specification. No RAM-map choice is delegated to implementation.

Set `/chosen/linux,initrd-start = 0x84000000`; `linux,initrd-end = 0x84000000 + R`, exclusive, where R is the actual inner compressed initramfs byte count, excluding the 512-byte MTK wrapper and page padding. Build the initramfs before finalizing the DTB. No guessed end address, ATAG import or padding counted as file length. Linux [OF scanning](https://github.com/torvalds/linux/blob/v6.18/drivers/of/fdt.c) parses these properties and the explicit memory ranges; [ARM memory setup](https://github.com/torvalds/linux/blob/v6.18/arch/arm/mm/init.c) reserves the kernel and initrd.

## Exact artifact intervals and rejection rules

These are fixed permitted windows plus exact size-dependent formulas. There is no built Linux kernel/DTB/initramfs whose actual byte ends could honestly be supplied today. A later offline implementation must emit the actual interval manifest and reject any violation, not silently enlarge RAM.

Use ARMv7 little-endian, ARM instruction-set kernel, CPU0 only, non-LPAE, non-XIP, non-ZBOOT_ROM, no EFI stub/hypervisor startup, `AUTO_ZRELADDR=y`, `TEXT_OFFSET=0x8000`, gzip kernel and gzip/cpio external initramfs. Keep SMP, highmem, CMA, kexec/crash dumping and unresearched DMA-capable peripherals disabled for this first artifact. Existing MT6582 CPU/GIC/GPT infrastructure remains the candidate foundation. A minimal initramfs is required; a general Debian rootfs is not intended for this memory budget.

Definitions: `L=0x80008000`; Z = plain zImage file length; D = DTB totalsize rounded up to 8 bytes with zero padding; R = inner compressed initramfs length; J = uncompressed Linux Image length. All arithmetic must be checked for overflow. Caps: `Z+D <= 0x600000` (6 MiB), `D <= 0x10000` (64 KiB), `0 < R <= 0x80000` (512 KiB), `J <= 0xc00000` (12 MiB), kernel BSS <= 2 MiB, entire kernel `_text.._end` <= 14 MiB. Unpacked initramfs regular-file bytes capped at 2 MiB; actual boot-time working set remains untested.````````````````````````````````

| Occupant / phase | Exact interval or admitted cap |
| --- | --- |
| Low boot data, permanently retained | [0x80000000,0x80004000); LK tags begin 0x80000100. |
| ARM non-LPAE initial page directory | [0x80004000,0x80008000). The consumed KERNEL wrapper at [0x80007e00,0x80008000) may be overwritten in this later phase. |
| Initially loaded zImage | [L,L+Z); starts exactly 0x80008000. |
| Initially appended DTB | [L+Z,L+Z+D); zImage length must equal decompressor _edata - _start and be 8-byte aligned; DTB begins immediately there. Combined cap [0x80008000,0x80608000). |
| Decompressed Image | [L,L+J), end at most 0x80c08000. |
| Whole resident kernel including BSS | [L,L+(_end-_text)), end at most 0x80e08000. |
| All relocated decompressor/DTB/scratch | Must remain inside [0x80008000,0x81800000); exact relocation below. Initial page-table writes are the separate low interval above. |
| LK ramdisk destination | [0x84000000,0x84000000+R), cap [0x84000000,0x84080000). |

Source basis: exact v6.18 [compressed/head.S](https://github.com/torvalds/linux/blob/v6.18/arch/arm/boot/compressed/head.S), [compressed linker script](https://github.com/torvalds/linux/blob/v6.18/arch/arm/boot/compressed/vmlinux.lds.S), [Makefile](https://github.com/torvalds/linux/blob/v6.18/arch/arm/boot/compressed/Makefile) and [kernel/head.S](https://github.com/torvalds/linux/blob/v6.18/arch/arm/kernel/head.S). AUTO_ZRELADDR aligns initial PC to 128 MiB and adds TEXT_OFFSET, producing L. Its appended-DTB signature test skips loader-FDT memory validation. The compressed linker script aligns file size to 8 bytes; `_kernel_bss_size` comes from the actual kernel's BSS symbols.

For the selected in-place load, use the actual compressed ELF symbols, normalized as offsets from `_start`. Let s=`restart`, w=`wont_overwrite`, e=`_edata` (=Z), t=`reloc_code_end`, b=kernel BSS size and p=decompressor stack-top offset decoded from LC1. The first relocation is derived directly from head.S:
  - `adjusted_J = J + max(0, b - (e-w))`.
  - `Q = align_down(t-s+256,256)`; require `0 < Q <= 0x10000`.
  - `source = align_down(L+s,32)`; `target = align_down(L+adjusted_J+Q,256)`.
  - `copy_bytes = align_up(L+Z+D-source,32)`; `delta = target-source`.
  - Relocated DTB is `[L+Z+delta, L+Z+D+delta)`. Relocated stack top is `L+p+D+delta`; malloc is its following 65,536 bytes. BSS starts/ends are compressed-ELF offsets plus `L+D+delta`; include the clear loop's up-to-15-byte rounding and copy padding.

Validate the actual collision branches and positive delta; require the relocated second pass to reach `wont_overwrite` without another move. Require live compressed code/input/workspace not to overlap decompressed output while in use, and relocated DTB not to overlap the final kernel including BSS. Kernel BSS may later reuse discarded decompressor bytes; the DTB must survive. Require compressed BSS, stack and 64 KiB malloc together to extend no more than `0x40000` beyond padded compressed payload (include alignment/clear-loop slack). These symbol-based requirements are mandatory even when file-size caps pass.

A conservative arithmetic bound is `L + 14 MiB + 64 KiB + 6 MiB + 256 KiB + 32 = 0x81458020`, below `0x81800000` by more than 3 MiB. This bounds the relocation copy and workspace under the caps; actual symbol checks remain essential. Compressed ELF offsets, kernel `_text/_end/__bss_start/__bss_stop`, Image length and the embedded inflated-size word must agree. Missing symbols or mismatched layout fail closed.

For LK payload staging, let `K=512+Z+D`, `W=512+R`, `P=2048`. LK reads `T=align_up(K,P)+align_up(W,P)+2P` bytes into `[L-512,L-512+T)`, after the Android header. Inner ramdisk source is `[L+align_up(K,P), L+align_up(K,P)+R)`, copied before kernel entry. At all maximum caps: T=`0x682000`, destination ends `0x80689e00`, ramdisk staging is `[0x80608800,0x80688800)`. The relative BOOTIMG read reaches `P+T=0x682800`, comfortably below its 16 MiB partition limit. Validate wrappers, actual sizes, page arithmetic and overread padding against the final artifact/partition contract. These staging bytes can overlap the later decompression output after the ramdisk has been copied; they must never intersect live LK, the final ramdisk or low tags while loading.

## Boundary review

Offline memory specification complete: no physical-rank, high-carveout, heap-upper-limit or ATAG-policy choice remains for the implementation role. Offline implementation can begin with this fixed layout and rejection rules, after a tiny concrete implementation issue is specified. No implementation issue or artifact was created in Y2E-130, and no research is assigned to implementation.

Unresolved: actual binary sizes and whether the tiny userspace fits at runtime; live rank topology; live loader heap extent; display scratch lifetime; exact secure/shared aliases and all DMA engines at kernel entry. These are explicitly not “confirmed free RAM.” None requires enlarging the offline map. Do not treat a host bounds check as proof of physical DMA safety. Before a hardware experiment, resolve U07c sufficiently through bounded stock/loader evidence, establish installed loader/security lineage (U01/U07b), usable console (U10a), backups/recovery/power (U05/U06/U09), and review the actual artifact manifest. M0 remains open.

## M1 implementation cross-reference

The owner subsequently authorized offline implementation. [Actual validated intervals and hashes](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md) now instantiate the formulas above without changing D08. [D09](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fkernel-policy.md) adds only a Kconfig visibility patch to make ARM_VIRT_EXT=n selectable. The dated Y2E-130 statements about no existing build remain the historical research result; no hardware boot or RAM-safety observation has since been made.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
