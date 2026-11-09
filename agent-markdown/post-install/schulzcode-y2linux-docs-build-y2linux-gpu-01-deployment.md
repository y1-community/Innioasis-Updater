---
title: "Y2LINUX-GPU-01 — manual deployment receipt - Innioasis Updater"
description: "Y2LINUX-GPU-01 — manual deployment receipt <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-gpu-01-deployment.html"
---

# Y2LINUX-GPU-01 — manual deployment receipt - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-GPU-01 — manual deployment receipt

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-GPU-01 — manual deployment receipt > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Owner deployed; hardware rendering passed, deep suspend failed qualification. Source commit `7c43557a38fac6bbdb0ab5628cffe131ebda6360`. One integrated BOOTIMG/Y2ROOT candidate is at `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-gpu-01`. The assistant has not flashed it. [GPU #34](https://github.com/SchulzCode/Y2Linux/issues/34) stays open; Y2Linux is not yet ready to begin Reborn. [Physical result and targeted suspend corrections](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md). The table below preserves the pre-deployment receipt; its pending identity fields are resolved by that evidence. GPU-01 image bytes/hashes are unchanged.

The pre-deployment fallback baseline was CONNECTIVITY-10 with CONNECTIVITY-07 root, accepted M4, and preserved Y2DATA. The owner keeps remaining M5 connection/audio tests pending. Reborn and M6/OTA implementation are outside this candidate.

## Required platform receipt``````````````````````````````````````````````````````````

| Item | GPU-01 implementation / evidence / remaining physical gate |
| --- | --- |
| 1. Source | 7c43557a38fac6bbdb0ab5628cffe131ebda6360; identical kernel/root build receipts. |
| 2. Exact GPU | Mali-400 MP2: own stock GP, L2, two active PP cores and three MMU resources, reconciled with the actual Y2 stock kernel. |
| 3. Revision | Not yet read. GPU is off on CONNECTIVITY-10. Normal Lima probe and y2-gpu-check will print GP/PP version registers; no revision is invented. MMU behavior/self-tests will be recorded; no separate MMU revision register is established. |
| 4. MMIO | GPU 0x13010000/0x10000: GP +0, L2 +0x1000, GP MMU +0x3000, PP0/1 MMU +0x4000/+0x5000, PP0/1 +0x8000/+0xa000. MFGCFG gate 0x13000000/0x10. Existing SPM 0x10006000, domain control +0x214. |
| 5. IRQs | GIC hwirq 202–207 / DT SPI 170–175, active-low: GP, GP-MMU, PP0, PP0-MMU, PP1, PP1-MMU. Existing sysirq owns polarity. |
| 6. Clocks | Existing CCF: MMPLL → MFG selector 1/top gate bit 23 at TOPCKGEN +0x50 → G3D MFGCFG bit 0. Bus uses existing mm_smi_common; its inherited rate remains unresolved, without retuning. |
| 7. Reset/domain | Existing sole SPM owner exports MFG genpd. Stock dual power ACK, clock isolation, domain reset and SRAM ACK sequence. Source clock spans the entire domain transition; Lima owns G3D usage. No independent guessed reset or duplicate register owner. |
| 8. Frequency | One inherited 500.5 MHz register-derived rate, nominal stock 500 MHz. This Y2's retained LK devinfo[3] bit 19 is physically 0, selecting the stock MMPLL branch. No PLL retuning, overclock or guessed DVFS table. Other loader PLL/mux states fail activation. |
| 9. Voltage | Preserve inherited supply. No established dedicated GPU regulator; no mali-supply or voltage/OPP write. Stock profiling's nominal 1.2 V is not a measured rail voltage. |
| 10. Kernel/Lima | Linux 6.18, CONFIG_DRM_LIMA=y, DRM_GEM_SHMEM_HELPER=y, DRM_SCHED=y, PM_GENERIC_DOMAINS=y, PM_GENERIC_DOMAINS_OF=y, PM_GENERIC_DOMAINS_SLEEP=y. Standard arm,mali-400 binding with mediatek,mt6582-mali. Small Lima probe PM-reference fix enables initial idle. |
| 11. Mesa | 24.0.9, pinned by Buildroot 2025.02.17 and source hashes. |
| 12. Mesa Lima | Actual Meson gallium-drivers=[lima,kmsro], llvm=disabled, osmesa=false, vulkan-drivers=[]; no software rasterizer. |
| 13. EGL | egl=enabled, GBM platform selected through the standard EGL extension/API. Actual EGL vendor/version/config ID await the hardware run. |
| 14. GLES | gles1=enabled, gles2=enabled; qualification explicitly creates GLES 2.0. Exact GL version/renderer/extensions and texture limits await GPU-01. |
| 15. GBM/libdrm | gbm=enabled, libdrm 2.4.124, ARM hard-float. glx=disabled, no X11/Wayland desktop platforms. Actual lima_dri.so and mediatek_dri.so installed. |
| 16. Memory/MMU | Lima GEM/shmem, standard DMA/PRIME, 32-bit DMA contract and [0,2^32) GPU VA, 4-KiB MMU pages; noncoherent ARM DMA API. No GPU carveout, CMA addition or changed RAM exclusions. KMS scanout needs small contiguous buffers; large allocations/fragmentation limits remain physical measurements. |
| 17. Presentation | Existing Mediatek KMS allocates linear XRGB8888 scanout; Mesa kmsro exports dma-buf and Lima imports/renders into it. Native 480×360, one outstanding page flip, completion before buffer reuse. No CPU presentation copy. Physical sharing/presentation is still a qualification gate. |
| 18. Runtime PM | Mainline Lima 200-ms autosuspend and job lifetime references; G3D gate then MFG domain off, source gated only after ACKs. Initial no-client idle is requested. ACK faults are bounded and refuse unsafe GPU access without a global reboot. |
| 19. Suspend | Lima force-suspend/resume plus genpd; quiesce jobs before existing M4 deep suspend. Test live static EGL context, then no-client suspend, same-session wake and rendering again. Existing charging suspend policy remains authoritative. |
| 20. Buildroot changes | Add Mesa Lima/kmsro, EGL/GLES/GBM and y2-gpu-check/y2-gpu-collect; retain connectivity, ALSA and existing production services. Libraries/tools are in Y2ROOT; kernel/DT/display module are in BOOTIMG. No OTA implementation. |

Hardware detail, source provenance, license policy and provisional Reborn API: [production GPU contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fgpu-platform.md). The [physical clock/bin capture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu-contract%2FREADME.md) did not power the GPU. Its read-only observation modules left only external-module taint 4096 in the earlier inspection boot. Owner-deployed GPU-01 starts with taint 0.

## 21–24. Images, preservation and fallback

Paths below are relative to `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-gpu-01`.````````````````

| Role | File | Bytes | SHA256 |
| --- | --- | --- | --- |
| New BOOTIMG | BOOTIMG.img | 6203392 | c8a27f021ddea92ffb9e97beaa3c327c53f1141b2d7e47d8f63060ea7c02adce |
| New Y2ROOT | Y2ROOT.img | 536870912 | b4a57fe7defd1132ab635d5496076df80e8af2880ebe04eb32282213bf44a5cf |
| CONNECTIVITY-10 fallback BOOTIMG | fallback/BOOTIMG.img | 6150144 | d7fbb0808db953a7c8d26f3846815b7b5fbc67caa1b86248d7f992dba51f30a7 |
| CONNECTIVITY-07 fallback Y2ROOT | fallback/Y2ROOT.img | 536870912 | c5031c2e87e02258d9da16a424ba727001d367ce76aa3366b5c70f6bef2d68fd |

Y2DATA is preserved in place. No Y2DATA image, formatting, seed or migration is provided. USRDATA is unchecked with filename NONE. Wi-Fi preferences, Bluetooth bonds, machine/radio identity and user files retain their existing storage. Retained data metadata describes the existing layout/template contract, not a claim that mutable live data equals its original seed hash.

The fallback pair is the established CONNECTIVITY-10/07 physical baseline; restoring these exact copies remains an operator action, not a newly tested rollback. Both fallback images use their own preserving scatter. No prior image is overwritten. Original FM/M4 recovery artifacts remain where retained.

## Host validation
  - Linux ARM build and emitted BOOTIMG/rescue/DT/kernel bounds passed.
  - 92 regression tests passed (56 production/core/storage/audio + 36

power/connectivity/GPU), including domain ACK fault injection and emitted DT IRQ/MMIO/reservation mutation rejection; no skipped GPU DT test.
  - dtschema 2026.6 validates the patched Lima binding and the emitted GPU

node. DTB SHA256: `c988d2d9316ca3cb8529ae39e576c502d0d2b2f373acc2667c9ea86282b69c6b`.
  - ARM/QEMU checks passed for the renderer's dynamic linking, help and bounded

arguments, telemetry shell syntax and existing ABI/ALSA tools. These are not hardware EGL/rendering results.
  - Package/root validation passed: clean ext4, label/UUID, new graphics ARM ELF

and hard-float ABI, raw ext4/tar agreement, no software renderer, preserved radio/SSH identity paths, exact fallback bytes and preserving scatter.
  - 9 isolated package rejection cases passed, covering data payload/selection,

schema/identity reset, protected writes, source mismatch, fallback lies and unestablished firmware redistribution. All package hashes verify.

Detailed [build receipts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-gpu-01%2FREADME.md) distinguish these host results from the still-pending physical milestone. Graphics license/source receipts are also shipped under `metadata/graphics-licenses`.

## 25. Exact manual installation
  - Check the package on the host:
` cd /home/luca/Dokumente/Code/Y2Linux/out/y2linux-gpu-01 sha256sum -c SHA256SUMS`
  - Shut down the Y2 by the established owner procedure. Use the previously

proven SP Flash Tool v5.2032.00 and matching `MTK_AllInOne_DA.bin`, with the established USB/power entry sequence.
  - Load this package's `MT6582_preserve_data_scatter.txt` and select

Download Only. Review the rows after loading:
````

| SPFT row | Selection | File |
| --- | --- | --- |
| BOOTIMG | checked | package BOOTIMG.img |
| ANDROID | checked | package Y2ROOT.img |
| USRDATA and every other row | unchecked | NONE |

 Keep PRELOADER, partition tables, protected/calibration partitions, LK, recovery and media unchecked. No Format, Firmware Upgrade or raw address entry. Use the unchanged scatter coordinates and raw image files.
  - Perform the manual Download operation, then boot normal Linux. This updates

both BOOTIMG and Y2ROOT; do not mix GPU-01 with the old root. Keep the existing initialized Y2DATA. No SD installation or data reset is needed.
  - Report “GPU-01 running”. The expected kernel is

`6.18.0-y2linux-gpu-01`, root marker `/etc/y2linux/build-id` is `Y2LINUX-GPU-01`, and existing SSH authorization/host identity is preserved. Qualification proceeds over the existing pinned connection after that report.

If a fallback is needed, load `fallback/MT6582_preserve_data_scatter.txt` in Download Only and select only its BOOTIMG and ANDROID files. Preserve USRDATA and all other rows exactly as above. A green SPFT result is transport evidence, not a claim of GPU qualification.

## 26. One coherent physical qualification

After the owner reports deployment, use the ordered procedure in the [GPU contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fgpu-platform.md%23physical-qualification-after-owner-deployment&anchor=physical-qualification-after-owner-deployment):
  - Record markers, boot ID, taint, Lima GP/PP revisions, MMU/L2 probe, render node

and initial no-client idle. Check both MFG power bits and clock references.
  - Run `y2-gpu-check --seconds 20`; record EGL/GL identity, hardware Mali renderer,

actual EGL config/texture limits and owner-visible colors, texture, alpha, geometry and animation at 480×360. Check page-flip/vblank completion.
  - Repeat five clean starts/exits, bounded TERM and one KILL/restart. Inspect

retained memory, display restoration, scheduler errors and application recovery.
  - Run `--static --seconds 300`; verify no continuing GPU work and runtime/domain

idle. USR1 requests exactly one redraw using the existing context.
  - Run `--seconds 120 --fps 30` with `y2-gpu-collect 125` in parallel. Record

frame-time percentiles, CPU/RSS, CPU/PMIC temperature, clock state and charging watchdog/health. No GPU temperature or battery power number is fabricated.
  - During rendering check all controls and existing quiet ALSA/CS43131 playback,

including audible quality, XRUNs and DMA/clock errors.
  - Quiesce to static, perform the existing deep-suspend/RTC-or-Power-wake procedure,

confirm same boot ID, then USR1 redraw. Repeat with no GPU client. Respect existing M4 charging inhibition/unplug policy; do not bypass a suspend refusal.
  - Verify KMS/panel/backlight and the existing offline-charge display path with

the targeted M4 procedure. Avoid a whole M4 requalification unless a regression is actually observed.
  - Check the established Wi-Fi scan/concurrent Bluetooth-power baseline during

rendering and zero radio errors/recoveries; restore original radio state. **Association/WPA2/DHCP/network reconnect, real peer pairing/SBC/AVRCP and sustained/full Wi-Fi-traffic + Bluetooth-audio + GPU tests remain pending by owner choice.** Do not reopen connectivity architecture.
  - Inspect kernel, storage/filesystem, thermal and power errors; record actual

passes/limits and fill the final Reborn DRM/KMS + GBM + EGL + GLES contract.

Stop at an actual failure for a targeted fix. No broad GPU re-audit after deployment. GPU #34 closes only on real Lima/Mesa rendering, presentation, power/resume and coexistence evidence. Reborn is not started by this handoff.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
