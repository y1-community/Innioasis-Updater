---
title: "Y2LINUX-GPU-02 — targeted suspend correction - Innioasis Updater"
description: "Y2LINUX-GPU-02 — targeted suspend correction <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-gpu-02-deployment.html"
---

# Y2LINUX-GPU-02 — targeted suspend correction - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-GPU-02 — targeted suspend correction

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-GPU-02 — targeted suspend correction > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Built and validated; STOP for owner manual deployment. Source commit `7e318afbffe640c6bf9da458f61ac2108f7d5bde`. The integrated package is `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-gpu-02`.

[GPU-01 physically renders correctly](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md) with Lima/Mesa, runtime power-off, clean wired audio and zero radio errors. Its suspend check exposes incorrect secondary-CPU status masks and a userspace all-off status mismatch. GPU-02 corrects only those checks and release identities. No PCM, GPU/display/radio architecture, voltage, clock policy or RAM map changes. GPU #34 remains OPEN; Y2Linux is not ready to begin Reborn.

The assistant has not flashed or replaced installed production code. The live GPU-01 boot remains on CPUs 0–2 with SPM broken=1 after the bounded failure; do not attempt more hotplug/deep sleep on that boot. Normal charging and SSH remain operational. GPU-01 artifacts remain immutable.

## Required platform receipt````````````````````````````````````````

| Item | Implementation and physical evidence |
| --- | --- |
| 1. Source | 7e318afbffe640c6bf9da458f61ac2108f7d5bde, matching kernel/root receipts. This commit also records GPU-01 physical evidence. |
| 2. Exact GPU | Mali-400 MP2, established from own stock and physically probed/rendered by mainline Lima on GPU-01. |
| 3. Revision | r1p1, GP 0x0b070101, PP 0x0cd070101; both PP cores version 1.1. No independent MMU revision register is established. All three MMU initialization handshakes and real rendering succeed on GPU-01. |
| 4. MMIO | Mali 0x13010000/0x10000: GP +0, L2 +0x1000, GP MMU +0x3000, PP MMUs +0x4000/+0x5000, PP cores +0x8000/+0xa000. MFGCFG 0x13000000/0x10. Existing SPM 0x10006000, MFG control +0x214. |
| 5. IRQs | GIC hwirq 202–207 / DT SPI 170–175, active-low: GP, GP-MMU, PP0, PP0-MMU, PP1, PP1-MMU. Existing sysirq owns polarity. |
| 6. Clocks | Existing CCF: MMPLL → MFG selector 1/top gate bit23 at TOPCKGEN +0x50 → G3D MFGCFG bit0. Bus uses existing mm_smi_common; its inherited reported rate is unresolved and not retuned. |
| 7. Reset/domain | Sole SPM owner exports MFG genpd, stock dual power ACK/isolation/reset/SRAM sequence. Source clock spans domain transitions; Lima gates G3D. GPU-02 corrects CPU ACK/boot masks to 0x800/0x400/0x200 and combined deep-entry guard to 0xe00, as proved by the actual Y2 stock binary and physical CPU3 bit9 transition. MFG sequencing is unchanged. |
| 8. Frequency | One inherited 500.5 MHz register-derived rate, nominal stock 500 MHz. This Y2's retained devinfo[3] bit19 is 0, selecting stock MMPLL. No retuning/overclock/guessed DVFS. Unexpected loader PLL/mux state fails activation. |
| 9. Voltage | Preserve inherited supply. No established separate GPU regulator, mali-supply or voltage/OPP writes. Stock profiling's nominal 1.2 V is not a measured rail. |
| 10. Kernel/Lima | Linux 6.18, DRM_LIMA=y, DRM_GEM_SHMEM_HELPER=y, DRM_SCHED=y, PM_GENERIC_DOMAINS=y, PM_GENERIC_DOMAINS_OF=y, PM_GENERIC_DOMAINS_SLEEP=y. Compatible mediatek,mt6582-mali, arm,mali-400. Standard Lima with initial probe PM-reference balancing. |
| 11. Mesa | 24.0.9, pinned by Buildroot/source hashes; unchanged from physically working GPU-01. |
| 12. Mesa Lima | gallium-drivers=[lima,kmsro], LLVM disabled, OSMesa false, Vulkan drivers empty; no software rasterizer or proprietary Android Mali userspace. |
| 13. EGL | Enabled; GBM platform. GPU-01 physically reports Mesa Project / EGL 1.4 / config 7. |
| 14. GLES | GLES1/GLES2 enabled; tested OpenGL ES 2.0 Mesa 24.0.9, GL vendor Mesa, renderer Mali400, maximum texture edge 4096, 16 texture units. |
| 15. GBM/libdrm | GBM enabled, libdrm 2.4.124, ARM hard-float; Lima and Mediatek kmsro DRI libraries. No GLX/X11/Wayland desktop. |
| 16. Memory/MMU | GEM/shmem, normal pages, standard noncoherent ARM DMA/PRIME, 32-bit DMA and GPU VA, 4-KiB pages. No carveout/CMA addition or changed RAM exclusions. Small KMS scanout allocations require contiguous DMA; large allocation/fragmentation limits remain untested. |
| 17. Presentation | Existing Mediatek KMS allocates linear XRGB8888, kmsro exports dma-buf to Lima for direct rendering/scanout. Native 480×360, reported mode 63 Hz, 30-FPS utility cap, one page flip outstanding. No CPU presentation copy. GPU-01 proves correct textures/alpha/layers and 3599 flips in 120 seconds. |
| 18. Runtime PM | Mainline Lima 200-ms autosuspend, job references, G3D gating then MFG off. GPU-01 proves initial idle, post-render idle and live-static-context domain-off idle plus on-demand redraw. |
| 19. Suspend | Lima force-suspend/resume and genpd callbacks return successfully in the retained staged test. Corrected CPU masks and radio zero matcher remove concrete blockers. Real same-session deep resume and EGL preservation are still unqualified. Existing charging inhibition policy remains authoritative. |
| 20. Buildroot | 2025.02.17, Mesa/Lima/kmsro, EGL/GLES/GBM and bounded y2-gpu-check/y2-gpu-collect. GPU-02 only updates y2-suspend and build markers in Y2ROOT; BOOTIMG owns kernel/DT/display module. Existing ALSA/connectivity/persistent-state paths remain. |

[Full GPU hardware/API/license contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fgpu-platform.md). Reborn will use DRM/KMS + GBM + EGL + GLES2, with RGBA8888 textures and GLES source-alpha blending into XRGB8888 scanout (EGL config7 has alpha bits0). Query configs/extensions at runtime. Render on change, cap normal animation at 30 FPS and stop drawing when static. Deep-resume context preservation is still a gate; support standard EGL_CONTEXT_LOST recreation, not Mali registers.

## 21–24. Images, Y2DATA and fallback

All paths are relative to `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-gpu-02`.````````````````

| Role | File | Bytes | SHA256 |
| --- | --- | --- | --- |
| GPU-02 BOOTIMG | BOOTIMG.img | 6203392 | 2e5f7e785e80dfc646e57d0ccfadff683d54a2c5303671c819ea4e42863089a9 |
| GPU-02 Y2ROOT | Y2ROOT.img | 536870912 | 1dec3b9c462587d804a022ef97e45222329065d263f53c2159ce00f728db145f |
| CONNECTIVITY-10 fallback BOOTIMG | fallback/BOOTIMG.img | 6150144 | d7fbb0808db953a7c8d26f3846815b7b5fbc67caa1b86248d7f992dba51f30a7 |
| CONNECTIVITY-07 fallback Y2ROOT | fallback/Y2ROOT.img | 536870912 | c5031c2e87e02258d9da16a424ba727001d367ce76aa3366b5c70f6bef2d68fd |

Preserve Y2DATA in place. No data payload, format, seed or migration. USRDATA and all protected rows stay unchecked/filename NONE. Saved networks, Bluetooth bonds, machine/radio identities, SSH keys and user files remain. BOOTIMG/Y2ROOT retain the existing OTA component boundary; OTA is not implemented. Fallback copies restore the accepted connectivity baseline, not a newly tested suspend result. The newly exposed CPU-mask defect predates GPU integration.

Host validation: 94 tests (56 + 38), corrected CPU ACK/guard failure replay, radio helper status replay, emitted DT/kernel/rescue/BOOTIMG checks, ARM ABI and bounded utility arguments, raw-ext4 root helper/marker/source agreement, clean ext4/UUID, graphics libraries, exact fallbacks and nine package rejection cases. The emitted DTB is byte-identical to GPU-01, SHA256 `c988d2d9316ca3cb8529ae39e576c502d0d2b2f373acc2667c9ea86282b69c6b`; dtschema2026.6 validation passes. [Build receipts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-gpu-02%2FREADME.md). These checks do not prove the corrected physical sleep path.

## 25. Exact manual installation
  - On the host verify the complete package:
` cd /home/luca/Dokumente/Code/Y2Linux/out/y2linux-gpu-02 sha256sum -c SHA256SUMS`
  - Use the established owner shutdown/USB/power entry procedure and proven

SP Flash Tool v5.2032.00 with the matching `MTK_AllInOne_DA.bin`.
  - Load this package's `MT6582_preserve_data_scatter.txt`. Use

Download Only and review exactly these selections:
````

| SPFT row | Selection | File |
| --- | --- | --- |
| BOOTIMG | checked | GPU-02 BOOTIMG.img |
| ANDROID | checked | GPU-02 Y2ROOT.img |
| USRDATA and every other row | unchecked | NONE |

 Keep PRELOADER, partition tables, LK, recovery, calibration/protected rows and media unchecked. No Format, Firmware Upgrade or raw-address entry.
  - Manually download both payloads and boot normal Linux, preserving existing

Y2DATA. Do not mix GPU-02 BOOTIMG with GPU-01 root; both contain a correction.
  - Report “GPU-02 running”. Expected markers are `6.18.0-y2linux-gpu-02`,

`/etc/y2linux/build-id` = `Y2LINUX-GPU-02`, and source `7e318af…` above. Existing pinned SSH identity/authorization remains.

If restoring the fallback, use `fallback/MT6582_preserve_data_scatter.txt` with its own two files, Download Only, and the same preservation selections. All physical installation/recovery remains the owner's operation.

## 26. Targeted physical qualification

Keep the completed GPU-01 rendering/performance/thermal evidence. Do not restart discovery or run another entry audit. Retain logs on the host and in a dedicated Y2DATA qualification directory before any sleep attempt.
  - Confirm both markers/source, taint0, all four CPUs, SPM broken=0, healthy

charging, saved preferences and Lima revision/render node. Run one short visible GLES animation.
  - Start a bounded static EGL client and wait for its first `STATIC_READY`.

Verify runtime/domain idle. With existing charge inhibition, run installed `y2-suspend` under `pm_test=core`. Require successful CPU3/2/1 off, all four CPUs restored, SPM broken=0, unchanged boot ID and same-context USR1 redraw. Restore `pm_test=none`; stop on any failure before actual deep sleep.
  - Schedule an RTC alarm only when none exists and perform real deep sleep

with the static client quiesced. Require meaningful residency, SPM entry/ resume increments, unchanged boot ID and redraw using the same EGL context. Restore prior charging policy and clear only the test alarm. Check panel, backlight and SSH; record any EGL context loss.
  - Repeat with no GPU client, using brief Power wake when the owner is ready

and a bounded RTC backup, then start a fresh renderer. A new boot, black screen, crash or required cable recovery does not pass same-session resume.
  - During a clearly timed animation, verify all controls overlap rendering;

the GPU-01 input observation window extended past its animation. Check quiet wired audio and radio counters after resume, preserving saved preferences.
  - Owner performs the existing targeted offline-charge animation/normal-boot

check. Record panel/backlight restoration without a full M4 rerun.
  - Check root/data, charging watchdog, temperatures, GPU/kernel errors and radio

zero-error/zero-recovery counters; restore original runtime settings.

Association/WPA2/DHCP/DNS/reconnect, Bluetooth real-peer/SBC/AVRCP and sustained Wi-Fi traffic + Bluetooth audio + GPU remain pending by owner choice. GPU #34 stays OPEN and Reborn readiness stays NO until the remaining physical gates pass. Do not start Reborn or M6/OTA.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
