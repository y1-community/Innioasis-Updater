---
title: "Y2 production GPU platform - Innioasis Updater"
description: "Y2 production GPU platform The 2026-10-04 Platform 1.0 graphics pass ../validation/Y2-PLATFORM-V1-GRAPHICS.md audits current Reborn rendering, artwork and display power i"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-gpu-platform.html"
---

# Y2 production GPU platform - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 production GPU platform

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 production GPU platform

The [2026-10-04 Platform 1.0 graphics pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-GRAPHICS.md) audits current Reborn rendering, artwork and display power in isolated worktrees. It preserves this Lima/Mesa/GBM/KMS foundation and records a measured JPEG decode reduction with source/host/ARM validation and fresh Y2 measurements. Current screen-off runtime PM, scanout gating, five wakes and brightness readback pass; static UI still redraws and the performance pass owns its correction. Remaining handoff/system-resume gates are stated in that receipt. The historical GPU-01 limits below still belong to their exact tested image. > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

**GPU-01 physically renders with Lima/Mesa; GPU #34 remains open for the failed suspend gate.** [Physical evidence and exact corrections](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md). GPU-02 carries only the observed CPU-status-mask/suspend-helper fixes and release identity. Reborn is not implemented. Only the owner deploys; Y2DATA is preserved. M4 and CONNECTIVITY-10 are the accepted foundations. M5 network/peer/audio tests remain pending by owner choice and do not block this implementation.

## Hardware contract and evidence

The own September 8 stock iomem and interrupt captures establish one GP, L2, two PP cores and three MMUs, with active GP/PP interrupt counts. The retained actual FM stock kernel has the Mali-400 MP2 platform resource array. Its `mali_platform_power_mode_change` at `0xc059890c` enables SMI_COMMON then G3D; `spm_mtcmos_ctrl_mfg` at `0xc0035230` supplies the exact domain sequence. The matching MediaTek GPL platform source is retained in the source receipt. This is stronger evidence than assuming every MT6582 has the same GPU.

| Block | Physical resource | GIC hwirq / DT SPI |
| --- | --- | --- |
| GP | 0x13010000, registers +0x0000 | 202 / 170 |
| L2 | 0x13011000, +0x1000 | none |
| GP MMU | 0x13013000, +0x3000 | 203 / 171 |
| PP0 MMU | 0x13014000, +0x4000 | 205 / 173 |
| PP1 MMU | 0x13015000, +0x5000 | 207 / 175 |
| PP0 | 0x13018000, +0x8000 | 204 / 172 |
| PP1 | 0x1301a000, +0xa000 | 206 / 174 |
| G3D clock gate | MFGCFG 0x13000000, CON/SET/CLR +0/+4/+8 bit 0 | none |
| Domain/reset | existing SPM 0x10006000, MFG_PWR_CON +0x214 | existing SPM owner |

DT maps the standard 64-KiB Mali-400 window. All six GPU IRQs are active-low through the existing sysirq provider. Compatible is `mediatek,mt6582-mali`, `arm,mali-400`; the Linux 6.18 binding receives that SoC compatible without changing the mainline Lima match. There is no fictional `arm,mali-utgard` fallback, PMU IRQ, RGU reset number or external IOMMU.

GPU-01 proves Mali-400 MP2 r1p1. Probe and standard GET_PARAM return GP `0x0b070101`, PP `0x0cd070101`, two PP cores; all three probe versions are 1.1. The old stock driver version is not a GPU revision. Utgard GP/PP MMUs have no separately identified revision register in the supported interface; report their self-tests and paging behavior, not an invented MMU revision. Mainline Lima performs the DTE mask test, hard reset and paging-enable handshake on each MMU.

A bounded read-only snapshot on CONNECTIVITY-10 found `CLK_CFG_1=0x00010100`, `MMPLL_CON0=0x00000111`, `MMPLL_CON1=0x0009a000`, `UNIVPLL_CON0=0xfd000001`, `UNIVPLL_CON1=0x800c0000`, `PLL_HP_CON0=0`. Existing stock-derived CCF decoding returns 500.5 MHz MMPLL, MFG selector 1. The stock MT6582 Mali platform reports nominal 500 MHz; the fixed policy retains this inherited selector and PLL without retuning. The donor's fixed 286 MHz and guessed MMPLL/2 are not used. This is a register-derived rate, not an oscilloscope measurement.

The generic `arch/arm/mach-mt6582/mt_gpufreq.c` references a different CLK_CFG_0/HYD layout and is not compiled into the retained Y2's GPU policy: its utilization callback is a no-op. Do not import its 156–476 MHz table. The real stock platform also contains a devinfo-index-3 bit-19 UNIVPLL branch; reading that single flag from this Y2's bounded retained LK ATAG data returned 0, so its stock driver keeps the MMPLL branch. No raw eFuse, calibration or identifier dump was needed. See the [physical contract capture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu-contract%2FREADME.md). GPU-01 only accepts this observed loader selector-1/MMPLL state. Other selector or PLL states fail GPU activation and require a targeted evidence check.

Voltage remains inherited. The stock platform performs no per-GPU regulator write and annotates nominal 1.2 V only in profiling data; this is **not a measured GPU supply voltage** or authorization to set that voltage. No separately controllable Y2 GPU supply is established, so DT omits mali-supply and OPPs. PWRAP/regulator ownership and all existing voltage restrictions remain intact.

## Ownership, power and memory

The sole existing SPM driver now provides the MFG genpd. Power-on sets both rails, checks both status words, releases clock isolation/reset and wakes SRAM with an ACK. Power-off follows the exact stock reverse sequence after Lima quiescence and CCF gating, including SRAM ACK and both power-off ACKs. Every poll is bounded. The domain holds the MFG source clock from before power-on until after power-off ACKs; Lima gates the G3D child before domain shutdown. No duplicate SPM mapping or donor power shim is installed. Domain reset is intrinsic to this sequence; no independent reset property is needed. SMI_COMMON remains held by the authoritative display clock provider. Its inherited bus rate remains unresolved in that existing provider; a zero reported bus rate is not a measured stopped clock. GPU integration does not retune the display/bus PLL. The GPU core source has the separate 500.5-MHz register-derived contract above.

The existing CCF owner controls only MFG's top gate bit 23, preserving the selector and all adjacent fields. A separate nonoverlapping MFGCFG CCF provider owns G3D bit 0. It never reads MFGCFG while the domain is off. Shared PLLs stay under existing CCF ownership; no undocumented PLL shutdown or DVFS is attempted.

Mainline Lima runtime PM retains its 200-ms autosuspend and scheduler lifetime references. A small generic probe fix balances an initial PM reference after DRM publication so the GPU also idles when no client has ever submitted a job. It does not wait for a first application to trigger power-down. System sleep uses Lima's force-suspend/resume hooks and genpd. Jobs must be quiesced; active work can reject suspend rather than silently lose rendering. MMU/L2/GP/PP are restored through Lima. Normal job timeout/MMU recovery is local to Lima/DRM, not a platform reboot. A domain hardware-ACK fault is reported separately.

Buffers use Lima GEM/shmem and normal Linux pages with a 32-bit DMA address contract, 4-KiB MMU pages and Mali-400's standard `[0, 2^32)` GPU VA range. That address range is not an allocation guarantee. There is no GPU carveout, reserved RAM change, coherent-DMA claim or loader/radio/display memory reclamation. DMA API and PRIME synchronization retain the existing noncoherent ARM cache handling. Allocation failures must return cleanly; the utility has bounded textures and at most the normal GBM front/back buffer set. Larger production limits require measurement, not a promise based on the GPU's virtual-address width. KMS scanout allocations still require physically contiguous pages; under RAM fragmentation those can fail with ENOMEM. At native size they are small (about 0.7 MiB each). This candidate does not claim arbitrary large allocation success.

## Graphics userspace and presentation

Buildroot 2025.02.17 adds its pinned Mesa 24.0.9, Gallium lima + kmsro, GBM, EGL and GLES, using libdrm 2.4.124. No X11, Wayland desktop, LLVM, llvmpipe/softpipe, Vulkan or Android Mali libraries are selected. [Mesa's Lima documentation](https://docs.mesa3d.org/drivers/lima.html) identifies GLES 2.0 and kmsro for sharing with a separate display controller.

The existing Mediatek DRM/KMS device allocates linear scanout storage; Mesa kmsro exports its GEM buffers through PRIME/dma-buf and imports them into Lima. The GPU renders into those buffers and the existing OVL/RDMA/DSI/panel path scans them out directly. This allocation direction is essential: arbitrary page-backed Lima allocations cannot be imported into this display engine unless DMA-contiguous. There is no CPU framebuffer copy, glReadPixels presentation, new display driver, CMA or large reserved-memory pool. GPU-01 physically confirms this render/scanout path at 480x360, with owner-visible correct textures/blending and 3599 page flips in the 120-second run.

`y2-gpu-check` locates drivers by DRM identity, never by a fixed card number. It queries mainline Lima identity, opens the existing KMS device, selects its 480x360 mode, creates linear XRGB8888 GBM storage, EGL and an ES2 context, then renders textured moving/scaling geometry, scrolling translucent layers and RGB/alpha reference patches. It rejects any non-Mali400 renderer. One page flip is outstanding at a time and its event must complete before buffer reuse. A three-second event timeout fails the test; it never runs an uncontrolled loop. Default is 20 seconds at a 30-FPS cap; hard limits are 300 seconds and 60 FPS. Exit restores the original CRTC and closes all standard resources.

`--static` draws once and sleeps. SIGUSR1 requests one further frame, including a same-context redraw after suspend. SIGTERM/SIGINT exits cleanly. The program prints EGL/GL vendor/version/renderer, configs, texture limits/extensions, presentation counts and frame submit-to-present percentiles, process CPU and RSS. These timings include synchronization; they are not GPU-only timings. `y2-gpu-collect 1..300` collects read-only thermal, runtime-PM, charging, clock, KMS and IRQ observations. No GPU temperature is fabricated.

## Physical qualification after owner deployment

Keep one coherent log directory under private evidence, recording source, installed markers, kernel release, boot ID and test order. Stop on the first actual failure and make a targeted correction. Do not repeat the entry review.
  - Confirm boot/root markers, taint 0, Lima GP/PP/L2/MMU probe logs, render node,

two PP cores, GP/PP revisions and no IRQ storm. Check idle before any client: runtime suspended, MFG gates off and bit 4 clear in both SPM status words.
  - Run `y2-gpu-check --seconds 20`; capture strings and owner-visible correct

RGB/geometry/texture/alpha/animation. Check linear PRIME buffer path, vblank and page-flip counts; reject llvmpipe/softpipe or a CPU-copy workaround.
  - Repeat start/exit five times; verify fbcon/panel restoration, stable available

RAM, no hangs or DRM errors. Send TERM during a 60-second run, restart, then one bounded KILL/restart test. KILL is not the normal application shutdown.
  - Run `y2-gpu-check --static --seconds 300`; inspect PM after >1 second. Keep

the image visible with no growing GPU-job IRQ count. Send USR1 to redraw.
  - Render for 120 seconds at 30 FPS while collecting 1-Hz telemetry. Record

frame percentiles, CPU/RSS, CPU/PMIC temperatures and CPU/GPU clocks. Inspect charger fault/health and advancing watchdog service while externally powered. Do not infer net battery current from configured charger current.
  - Verify wheel/navigation/volume/Power events during animation with evtest;

no grabs or remapping. Play the existing quiet 44.1-kHz ALSA/CS43131 fixture concurrently and check audible output, XRUN/kernel logs and clock conflicts.
  - With the static GPU context and no pending job, use the existing y2-suspend

procedure, RTC/Power wake and same boot ID. Request a USR1 redraw. Verify runtime/domain off during suspend, restored GPU, KMS/panel/backlight and input/audio. Repeat suspend once with no GPU client. If EGL reports context loss, record it; recreate via standard EGL only and investigate the limit.
  - Targeted display/offline-charge check using the existing manual M4 procedure:

panel/backlight and charging animation still work; no whole M4 test rerun unless evidence shows a regression. Restore normal Linux and charge policy.
  - Check CONNECTIVITY-10 counters and a bounded scan/concurrent BlueZ power

regression without reopening bring-up. Network association/traffic + GPU, Bluetooth SBC/AVRCP + GPU and full triple coexistence remain pending until credentials/peer are available; the owner currently defers those tests.
  - Inspect kernel errors, filesystem/storage state, remaining memory, radio

errors/recoveries and charger health. Return radios to their starting state, preserve preferences/bonds and record which physical gates actually passed.

## Reborn API contract (rendering proven; system resume still open)

Use DRM/KMS + GBM + EGL + GLES2. Open KMS and the Mesa-selected render node; never depend on Mali registers, physical addresses, proprietary ioctls or SoC power controls. Render at native 480x360 into linear XRGB8888 scanout. RGBA8888 textures and GLES source-alpha blending provide layered UI composition; scanout need not have an alpha channel. Query the actual EGL config and maximum texture size. POT RGBA8888 is the baseline; non-power-of-two and compressed formats are permitted only when the actual GL extension/capability query allows that use. GPU-01 reports EGL 1.4 / Mesa Project, OpenGL ES 2.0 Mesa 24.0.9, GL vendor Mesa, renderer Mali400, EGL config 7 (scanout alpha 0), maximum texture edge 4096 and 16 texture units. Query capabilities at runtime instead of hardcoding config IDs. RGBA8888 and linear filtering are physically exercised; ETC1, NPOT and other reported extensions are capabilities, not an exhaustive format-performance qualification. Ordinary UI textures should stay far below the maximum edge; allocation/fragmentation stress remains untested.

Present through DRM page-flip events/atomic KMS semantics, waiting for completion before releasing the previous GBM front buffer. Default UI animation cap is 30 FPS, at most panel refresh when justified by measurement. Static content submits no work; wake on damage/input. Quiesce rendering before system suspend; retain a context only if the qualified driver restores it. Handle standard EGL_CONTEXT_LOST by recreating EGL resources and reuploading textures. GPU-01 does not establish context retention across real deep suspend: the CPU-hotplug status-mask defect blocks qualification. Preserve this as a pending GPU-02 test, including standard EGL recreation handling; do not promise seamless resume from the runtime-PM success alone.

## Licenses and provenance

Linux 6.18 is GPL-2.0-only with its normal syscall exception; Lima files are GPL-2.0 or MIT as marked, and its UAPI header is GPL-2.0 WITH Linux-syscall-note OR MIT. `tools/graphics/include/lima_drm.h` is byte-identical to Linux 6.18, used only to print standard driver identity because libdrm omits that header. The qualification program is MIT. Mesa is MIT/SGI/Khronos per Buildroot's `docs/license.rst` inventory; libdrm is MIT. GPU domain semantics are reconstructed from the MediaTek GPL source and actual Y2 stock disassembly; the donor is only a corroborating lead, not a copied permanent-power shim. No proprietary Mali userspace is included. Existing owner-only connectivity firmware/provenance and redistribution restrictions are unchanged by the graphics work. The candidate includes source archive hashes and the Mesa, libdrm, qualification tool and Lima UAPI license texts under `metadata/graphics-licenses` alongside the existing Linux/Buildroot receipts.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
