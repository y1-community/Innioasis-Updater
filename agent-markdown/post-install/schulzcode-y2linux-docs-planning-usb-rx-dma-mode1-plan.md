---
title: "Faster uploads over USB: multi-packet receive DMA — plan (2026-10-17) - Innioasis Updater"
description: "Faster uploads over USB: multi-packet receive DMA — plan 2026-10-17 Status: RELEASED, on by default, in Y2Linux 1.0 Beta 7.11 ../validation/Y2-LINUX-1.0-BETA-7.11.md Base"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-usb-rx-dma-mode1-plan.html"
---

# Faster uploads over USB: multi-packet receive DMA — plan (2026-10-17) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Faster uploads over USB: multi-packet receive DMA — plan (2026-10-17)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Faster uploads over USB: multi-packet receive DMA — plan (2026-10-17)

Status: RELEASED, on by default, in [Y2Linux 1.0 Beta 7.11](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.11.md) (Baseline 74, sequence 6352). Owner: "i would like to do multi packet and fix the kernel". Audit row USB-RX-DMA in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md). Results: [below](#results-2026-10-17).

## Evidence (owner's player, Beta 7.10, 2026-10-17, `mtpbench`, libusb direct, SHA-256 verified)

|  | Internal Storage | SD card |
| --- | --- | --- |
| Download (player → computer), TX DMA | 37.7 MB/s | 37.7 MB/s |
| Upload (computer → player), RX PIO | 8.7–10.3 MB/s | 9.0 MB/s |
| Storage write ceiling (handoff, candidate 11) | eMMC 30 MiB/s | SD 26 MiB/s |

  - `/sys/devices/platform/11200000.usb/status`: `dma_rx_programs=0`, `pio_rx_bytes=255 MB`, `dma_tx_programs=15789`:

every upload byte is read from the FIFO by the CPU, every download byte goes by DMA.
  - Upload with the interrupt on CPU0: CPU0 100 % busy, ≈23 800 musb interrupts/s. Interrupt pinned to CPU3 (live test,

restored afterwards): CPU3 96 % busy, ≈21 500/s, upload unchanged (9.3–9.6 MB/s). One endpoint is strictly sequential, so ≈45 µs of CPU per 512-byte packet is the ceiling; spreading over cores cannot help.
  - Already in place: double-buffered bulk FIFOs (raised receive from ≈7 MB/s), 32-bit FIFO reads (`ioread32_rep`), CPU at

1.3 GHz during the transfer.

## Why receive DMA is off today

`kernel/platform/usb.c` (`y2_dma_is_compatible`) keeps bulk-OUT requests unmapped: Mentor/Inventra mode-0 receive DMA costs two interrupts per packet (no gain over PIO), CPU-FIX02 hit the interrupt-storm guard with it (FIX03: the guard counted the normal two-per-packet load; corrected), and a packet the host had already ACKed was lost when it followed an IN completion within microseconds. The runtime switch `rx_dma` (sysfs) re-enables mode 0 for comparison only.

## Design: mode 1 for MTP bulk OUT

Mode 1 lets the DMA engine move consecutive full packets with no CPU work per packet; the CPU acts once per request. Upstream musb has this path only for mass storage (`short_not_ok`), because a mode-1 transfer gets no DMA completion for a short last packet. MTP data ends with a short packet or a zero-length packet, so the Y2 version adds:
  - Start: a FunctionFS bulk-OUT request with at least two packets left and a full first packet is programmed as one

mode-1 DMA transfer of the remaining length (multiple of 512, capped at the channel maximum), with AUTOCLEAR, DMAENAB and the Inventra DMAREQMODE sequence.
  - Full packets: moved by DMA; one DMA interrupt at the end gives the request back.
  - Short packet or ZLP before the end: the endpoint interrupt fires (RXPKTRDY, count < 512) while the channel is

busy. The CPU stops the channel, reads how many bytes it moved (whole packets), takes the short packet by PIO and gives the request back with the exact length. The order (stop, read the count, then the FIFO) decides correctness and is the main thing the tests prove.
  - Request boundaries: packets that arrive before the next request is queued wait in the double-buffered FIFO (the

host is NAKed, nothing is lost); the existing `late_pio` path takes the waiting packet, mode 1 continues after it.
  - Unchanged: IN (download) DMA, the 16-byte event endpoint, ECM networking, PIO as fallback whenever DMA cannot be

programmed, the storm guard (it counts per accepted DMA program).

Reference before writing it: the stock MediaTek kernel (`out/rea/fm-kernel.elf`, REA) for how MTK's own musb driver programmed RX DMA on this exact controller (mode, RXCSR sequence, short-packet handling, errata workarounds).

## Safety
  - First build: mode 1 behind the runtime switch, default off (`rx_dma=2`); behaviour is unchanged until it is switched

on, so the build can be released and A/B-tested live on the player without another install.
  - Default on only after the device tests below pass; PIO stays the fallback.
  - Every new path keeps the existing receive event ring and counters (`dma_rx_programs`, aborts, short-packet count) so

a failure is diagnosable from `status`.

## Device tests (owner's player; hashes on every byte)
  - `mtpbench` uploads at 1–200 packets with every ending: exact multiples (ZLP), one byte short, one byte over, 0 bytes.
  - 2 000 files of random sizes up and back; 600-file folders (the `mtp-file-ops` suite) with mode 1 on.
  - Uploads interleaved with downloads, listings and events (the earlier IN-completion race), Internal Storage and SD.
  - 4 GB sustained upload soak; throughput and CPU recorded; storm guard and fault counters must stay at 0.
  - Cable pulled mid-upload, then reconnect; deep sleep and wake with mode 1 on; Windows Explorer and Dolphin copies.

Expected result: uploads near the storage limit (≈20–30 MB/s), CPU mostly idle during uploads.

## Steps
  - Owner approves this plan.
  - Stock reference (REA), implementation, kernel build, host checks (patch zero-fuzz, ABI, existing tests).
  - Release with the switch off; owner installs; live A/B with `rx_dma=2` (a runtime write the owner authorises).
  - Fix what the tests find; repeat 3.
  - Default on in the following release; audit row and report updated.

## Results (2026-10-17)

Stock reference (REA, `out/rea/fm-kernel.elf`, Linux 3.4.67): MediaTek's `rxstate` is upstream's. Mode 1 only when `short_not_ok` and the first packet is full (RXCSR AUTOCLEAR, then DMAENAB, then a DMAMODE set/clear pulse), otherwise one mode-0 program per packet; `dma_channel_pause/resume/check_residue` are stubs. Stock MTP uploads therefore never used mode 1, and the short-packet ending below is our own.

Implementation (`kernel/patches/0065-y2-musb-pio-progress.patch`, `0055-musb-abort-bus-error.patch`, `kernel/platform/usb.c`):
  - `y2_rx_mode1_start()` (from `rxstate`, also for a packet already waiting when the request is queued): full first

packet → one mode-1 program of the request's whole packets (≤ 1 MiB); the upstream AUTOCLEAR/DMAENAB/DMAMODE sequence, left in request mode 1. If neither the address nor the count register nor RXPKTRDY moves within 20 µs, DMAMODE is pulsed again (twice), then the channel is stopped and the packet goes to PIO (`m1_kick`, `m1_fallback`).
  - `y2_rx_mode1_end()` (endpoint interrupt while the channel is busy): a short or zero-length packet is believed only

when RXCOUNT and the DMA progress (`y2_hsdma_moved()`, address register) agree in two samples 2 µs apart on a whole packet; then the channel is stopped, the buffer unmapped, the short packet read by the CPU and the request given back. A finished channel is left to its pending completion; a count that moves after the stop fails the request (`-EIO`), never silently.
  - `musb_g_rx`: a mode-1 completion below the request length continues the same request.
  - sysfs: `rx_dma` 0 PIO / 1 mode 0 (comparison) / 2 multi-packet (default); `rx_dma_eps` endpoint mask (default

all OUT endpoints); `rxdiag` counters `m1_prog`, `m1_end`, `m1_kick`, `m1_fallback`. A request mapped while DMA was on goes to PIO after `rx_dma=0`, never to mode 0.

Defect found on the device: RXCOUNT counts down while the engine unloads a full packet. The first build (sequence
  - took one such sample for a short packet and ended a 64 MiB upload after 9.6 MB (`m1_end=1` with no short packet

on the wire; uMTP lost the container). Fixed by the two-sample rule; a moving count is now seen and ignored.

Measurements (owner's player, `tools/usb/mtpbench.c`, every byte SHA-256 verified):

|  | PIO (7.10 / 7.11 switch off) | Multi-packet DMA |
| --- | --- | --- |
| Internal Storage, 1 GiB | ≈10 MB/s | 29.6 MB/s |
| Internal Storage, 256 MiB | ≈10 MB/s | 25.7–27.2 MB/s |
| SD card, 512 MiB | ≈9 MB/s | 23.3 MB/s |
| ECM (100 MB through SSH) | 6.1–8.1 MB/s | 9.9–13.9 MB/s |
| musb interrupts during upload | ≈22 000/s, one core 96–100 % | ≈1 450/s, CPU ≈80 % idle |

Integrity: boundary sizes 0, 1, 499, 500, 501, 511, 512, 1012, 1024, 65523–65536, 131060/1, 200000, 1048564/5/77, 3145716 on both storages; 100 random sizes; `tools/usb/mtp-file-ops.c` 26/26 (with the switch on and with the default build); 1 GiB + 512 MiB soak; 300 MB over ECM; host abort mid-upload recovers exactly like PIO. Counters always balance (`m1_prog` = `dma_done` + `m1_end`), no kick, no fallback, no DMA bus error, storm-guard burst ≤ 22.

`mtpbench` itself lost the closing zero-length packet of a download that fills its last 1 MiB read (fails in PIO too); fixed in the tool.

Still owed (owner): cable pulled mid-upload, sleep and wake with it on, copies from Dolphin and Windows Explorer.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
