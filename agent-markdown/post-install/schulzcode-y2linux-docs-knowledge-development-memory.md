---
title: "DEV-01 practical RAM reconciliation - Innioasis Updater"
description: "DEV-01 practical RAM reconciliation <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-development-memory.html"
---

# DEV-01 practical RAM reconciliation - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# DEV-01 practical RAM reconciliation

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# DEV-01 practical RAM reconciliation > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## Physical DEV-02 result — 2026-09-10

[Live qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) measures MemTotal954660KiB (932.285MiB), HighTotal228352KiB and a completed256MiB allocator-backed short test. The difference from951MiB minus16KiB before kernel reservations is19148KiB of ordinary kernel/early-allocation overhead. HIGHMEM is substantially consumed through the allocator; no physical-address sweep. The separate exhaustive run was capped at600seconds, not a full-suite pass. Full DMA/long-run qualification remains open. The original offline reconciliation below is retained as history.

2026-09-10; successor to [D08](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md), authorized by the owner for one integrated development candidate. This is an implemented, offline-validated map. Its actual MemTotal, HIGHMEM operation and allocator stability remain to be measured on the Y2. The latest physical evidence remains BASELINE-03 capture-02.

All intervals are physical, hexadecimal and half-open. Retained stock iomem establishes the main bank `[80000000,be000000)` (992 MiB). DEV-01 describes that bank directly, without importing LK ATAG sizes or reclaiming the high 2 MiB island.``````````````````````````````````````

| Occupant | Reservation or lifetime decision |
| --- | --- |
| Boot tags / low control data | Reserve [80000000,80004000) (16 KiB). Initial kernel page directory occupies the next 16 KiB and is owned by ARM startup. |
| Kernel and decompressor | Entry 80008000; exact Image, BSS, relocated compressed input/DTB, stack and malloc intervals come from the built ELF in layout.json. All relocation remains below 81800000; the historical 6 MiB kernel+DTB and 14 MiB resident-kernel caps remain enforced. |
| LK text, BSS, stack, initial heap | Reserve [81800000,84000000) (40 MiB). This includes LK at 81e00000, BSS/heap start 81e55434, and the uncertainty immediately above it. 84000000 is LK's established ramdisk copy destination, not a newly invented address. |
| Other LK heap allocations | Their exact former upper extent is unresolved. LK does not execute after its normal branch to Linux; dead CPU-only heap allocations are reusable. The 40 MiB reservation is a retained guard, not a proved maximum heap extent. Any surviving device-owned target requires separate containment; see below. |
| BOOTIMG staging | Existing LK wrapper/page/overread formulas are applied to the actual larger rescue payload. Staging is below 81800000 and may be reclaimed after the ramdisk copy. It is not a permanent allocation. |
| Rescue initramfs | Starts 84000000, exact gzip end supplied in DT after packing. Kernel memblock reserves it until unpacking; initramfs pages/files subsequently belong to Linux. Caps: gzip 4 MiB, regular archive payload 8 MiB. |
| Donor connectivity alternative | Reserve [bdf00000,be000000) (1 MiB) inside the bank. This accommodates the donor's reservation without pretending it resolves the conflicting stock allocation. |
| Modem / shared memory | [be000000,bf800000) stays outside Linux RAM: inferred 22 MiB modem + 2 MiB shared from retained FM/default allocation, with historical modem overwrite evidence at be000000/be800000. |
| Alignment gap and display scratch | [bf800000,bfa00000) is not reclaimed. LK's framebuffer-minus-4-MiB scratch pointer bf700000 and its uncertain extent remain in the excluded high envelope. |
| Stock connectivity alternative | [bfa00000,bfb00000) remains excluded, retaining both the stock-inferred and donor candidates. |
| LK framebuffer / preloader scratch / page tables | [bfb00000,c0000000) remains excluded. Includes the observed 5 MiB mtkfb resource, preloader scratch and top page-table base bff00000. The old diagnostic pixel aperture remains a guarded I/O mapping, never allocator RAM. |

The DT combines high ownership into a no-map reservation `[bdf00000,c0000000)`. The portion inside the declared bank is 1 MiB; the rest also documents containment for inherited display/modem/connectivity traffic. The allocator therefore starts with 951 MiB minus 16 KiB, before the kernel, page tables, memmap, initramfs and other ordinary kernel reservations. This number is an arithmetic budget, not a claimed observed MemTotal.

`PHYS_OFFSET=80000000`, `PAGE_OFFSET=c0000000`, non-LPAE ARM and `VMSPLIT_3G` remain coherent. `CONFIG_HIGHMEM=y` allows pages above the kernel's chosen linear-map limit to remain usable. The exact lowmem/highmem split depends on ARM's vmalloc boundary and must be recorded from boot logs, `/proc/zoneinfo` and `/proc/meminfo`. There is no guessed direct virtual mapping for high pages. No CMA, raw `/dev/mem`, swap, crash kernel or hypervisor reservation is introduced.

## Bus masters and ownership
  - OVL/RDMA/DSI inherit LK's excluded high display buffers until the bounded park

and Linux commit. Linux DRM GEM uses the DMA API with a 32-bit mask; diagnostics compare the GEM physical address to actual OVL address after programming. Coherent scanout buffers are Linux allocations, not a fixed carveout in free RAM.
  - Internal eMMC's native controller is disabled in DT; the original command

firewall remains on its read-only compatible. Retained LK normal storage paths stop DMA and poll idle before returning. No internal disk is a root candidate.
  - Removable MSDC1 at `11240000` checks inherited DMA-idle state before acquisition,

then uses the upstream controller's descriptor/buffer DMA ownership. It uses the live decoded crystal source, maximum 13 MHz, one-bit SD; no eMMC/SDIO client or new regulator voltage is enabled.
  - I2C APDMA uses only the exact controller channel and Linux DMA mappings. On the

MT6582 error path reset now precedes unmapping/freeing the transfer buffers. One transfer per wheel interrupt; no added retry. The diagnostic records both controller and DMA state before reset.
  - USB remains peripheral PIO, including ACM and ECM. No USB DMA or host mode.

Endpoint FIFO allocation occupies 2144 bytes of the evidenced 8192-byte RAM.
  - No new audio, GPU, camera, modem, connectivity or radio driver is enabled.

Disabling a driver alone does not prove inherited DMA idle. Full secure-world or arbitrary bus-master containment is not established; retained known high targets are excluded and there is no claim that the reservations prove all RAM safe. This is an explicitly requested development qualification candidate.

After owner deployment, collect CPU online mask, dmesg, iomem, zoneinfo, meminfo, buddyinfo and interrupts in one pass. Then `/usr/sbin/y2-memory-check` requests 128 MiB through the normal allocator, tests it once with memtester and frees it. It refuses to start below 256 MiB MemAvailable. There is no physical-address sweep, reserved-memory access or automatic repeated stress. Record failures with the display, wheel, SD and USB findings for the same integrated iteration.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
