---
title: "M3 headphone-first architecture and source review - Innioasis Updater"
description: "M3 headphone-first architecture and source review <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m3-audio-architecture.html"
---

# M3 headphone-first architecture and source review - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M3 headphone-first architecture and source review

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M3 headphone-first architecture and source review > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-10; qualified core baseline `d76e57f`; current deployed candidate Y2LINUX-M3-AUDIO-02 (`8f93e44`), including notification fix `137b3f2`. [Owner-authorized activation audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23m3-activation-audit--2026-09-10&anchor=m3-activation-audit--2026-09-10). [Physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-01-live-result.md): clean S16 stereo44.1kHz headphones confirmed;48kHz, explicit L/R and stop/restart/repeat remain. **M3 is open and near completion.**32-bit I2S slots do not provide32-bit PCM;24/32-bit and higher rates remain unimplemented later enhancements.

## Reconciled evidence

The focused review used the pinned donor MT6582 AFE common/header/PCM/machine files, local Linux 6.18 MediaTek FE/platform/DPCM/codec/regulator source, retained vendor `mt_clkmgr.c`, artificerchris porting history and our stock HAL/runtime report. No donor inventory, complete source hashing or ROM/recovery audit was repeated. Donor directories and upstream ASoC core/codec bytes remain unchanged. GPL attribution is retained in adapted files.````````

| Contract | Evidence and decision |
| --- | --- |
| Native controller | Donor/vendor AFE 0x11220000, size0x1000; GIC SPI104 level-low. DL1 base/current/end 0x40/44/48; MCU IRQ CON/STATUS/CLR/CNT1 0x3a0/a4/a8/ac. |
| External route | Our Y2Player/docs/Y2_AUDIO_PATH_PHASE4_SECOND_I2S.md, backed by stock capture 2026-07-30_135519, reports CONN0=0x00400020, CON3=0x90b playing/0x90a idle, CON1=0 throughout ten states. HAL hash5c5162f6a68f7db57febd050ee88cc886779dcce5948937149d6cd211eb0e6de; no repeat full HAL hash. Donor and external pad proof agree on I05/I06 -> O00/O01 -> CON3. |
| Source limit | The stock report's PMIC ABB/AUDTOP activity does not prove the PMIC analog output lies in the headphone signal chain. We do not reproduce those analog writes. If DAC/I2S work but headphones remain silent, this remains class E routing evidence to resolve. |
| I2S pins | External history identifies GPIO43 BCK,44 WS,46 data using LK's mux. Claim/retain/report those muxes; fail if a pad is still GPIO mode0. No unverified pin function number or drive strength is programmed. Own-unit clean headphone playback now confirms the route operates; no independent electrical pad/clock measurement is claimed. |
| FPGA_CFG1 | External history says bit4 does not read back on silicon. Omit the ineffective fidelity-only write; do not assume it establishes external routing. |
| Clocks | Vendor CLK_CFG_3 uses audio bits16/23 and audintbus bits24–26/31; infracfg audio gate5. Both muxes select documented 26MHz parent0 through CCF. Adjacent SD fields and inherited gate retention are tested. No PLL retune or approximate fixed donor PLL rates. |
| Rate contract | Both rates use the same source: DL1, IRQ1 and CON3 code9 at44100 / code10 at48000; 32-bit I2S slots, 64 BCLK/frame. Nominal BCLK2.8224/3.072MHz. DAC crystal22.5792MHz, upstream codec PLL/clock-family handling for48k. No end-to-end accuracy claim until measured. |
| DAC | Stock I2C1:0x30 and upstream cirrus,cs43131 ID support. Use unmodified Linux6.18 cs43130.c, five supply consumers and cs43130-asp-pcm DAI. Its ready-status polling avoids an unqualified EINT16 dependency. |
| Power | Live DEV-02 VGP2 selector2.5V with no consumer matches historical brownout cause. MT6323 framework constrains1.8V; only DIGLDO_CON8 enable0x8000 and CON29 selector0xe0 are newly writable through PWRAP. No raw PMIC pokes or other analog/charger/reset permissions. |
| GPIO supply ordering | Reproduce stock/donor20 ->18 ->15 via standard fixed-regulator dependencies VGP2 ->20 ->18 ->15, 50ms each. GPIO-backed voltages are nominal enable models, not independently measured rails. Bulk-enable dependency references force order and reverse teardown; common VGP2 stays on pending shared-rail qualification. |
| Amplifier | Stock1:0x58 aw87559 naming versus external OCA72559 ID09 remains unresolved. GPIO8 is claimed as output-low at boot; no amplifier I2C client, tables, high gain or speaker endpoint. Headphone target does not require enabling it. |
| Jack | Upstream creates its normal Headphone jack object. With no IRQ described, asynchronous insertion/removal reporting is not qualified; static ALSA headphone routing is used. EINT16 and MediaTek ACCDET remain future investigation, with no UI policy in kernel. |

External retained reference: artificerchris reverse-engineering revision `f96d4c7dddbcafeb31919fe1fbe2dab99c4bd641`, `archive/notes/porting/audio.md`. Its audible/rail/pad results belong to that device and do not promote our status.

## Driver boundaries and lifecycle

`kernel/audio/mt6582-afe.c` provides DL1 front end and second-I2S back end using current DPCM, regmap-MMIO, managed coherent ALSA DMA and runtime PM conventions. It deliberately implements the small MT6582 PCM callbacks locally: generic MediaTek helper assumptions around optional register fields, fixed-IRQ substream clearing and ignored register errors are not copied into this new port. Existing ASoC/common core is not replaced. Build overlays only add the directory and its Kconfig/Makefile entries.

One playback ring, DMA mask32, stereo S16_LE, 44.1/48k, max256KiB, 16-byte buffer and period alignment, periods2–256, period512–131072bytes. Allocation comes from `snd_pcm_set_managed_buffer_all(...SNDRV_DMA_TYPE_DEV...)`, and its error is propagated. No SRAM carveout, physical-address allocator, virt_to_phys, generic DMAengine fiction or codec-datasheet-based high-resolution advertising. Inclusive END is validated against wrap at4GiB; pointer offsets must be in the allocated ring. No reserved RAM is exposed to the DMA allocator.

Start programs count/rate, clears pending IRQ1, enables DL1 and IRQ1 under the private lock. Any failed start disables both. IRQ acknowledges its snapshot before `snd_pcm_period_elapsed`, never holding the private lock during that ALSA callback. Stop/free/close and `.sync_stop` drain the interrupt before DMA/runtime release; no stale substream callback after close. Runtime suspend disables the Linux IRQ before clock gating. Resume restores quiet hardware before unmasking. Managed component teardown precedes PM cleanup and IRQ free. AFE IRQ registration failure quiesces the block and releases clocks.

The second-I2S prepare sequence selects only the DL1 sources for O00/O01 and programs CON3 while disabled before enabling it. It clears that connection on shutdown. I2S clocks run through codec preparation and DAPM shutdown; no delayed five-second analog power-down is requested by this card. Severe pops/noise still require physical detection and are a stop condition.

`kernel/audio/y2-cs43131.c` owns per-device card/link/phandle lifetime, headphone routes and DAC clock relationship. No board routing is in the AFE. CardID/name `Y2Audio`, PCM0 `Y2 Headphone Playback`, back end `Y2 Second I2S`. Codec is BCLK/LRCK consumer; Linux6.18 flips that format for the CPU DAI, which requires provider mode. Initial port compilation found and corrected the removed `dpcm_playback` field (`playback_only` now) and the upstream codec header's regulator dependency. Corrections used the same build tree, not another clean kernel build.

## Safe development userspace and observability

Buildroot adds alsa-lib, aplay/amixer/speaker-test, evtest and modetest already queued from DEV-02. No sound server or mixer auto-restore. Generated three-second stereo WAVs at44.1/48k contain -30dBFS peaks and50ms fades; Master207 gives -24dB. Headphone is disabled initially; owner enables it only for a controlled test.

`y2-audio-collect` collects standard ALSA, interrupts, dmesg, regulators and clocks. AFE's read-only `state` attribute guards bounded MMIO reads with runtime PM and exposes DMA range/current, CONN0/CON3, rate/count and cumulative running IRQ events. The counter alone does not prove ALSA callbacks occurred, as AUDIO-01 demonstrated; correlate ALSA pointer progress and playback timing. Use it instead of clock-gated raw regmap dumps. It reports nominal register state, not an electrical BCLK/LRCK measurement. No register-writing userspace helper.

## Qualification and remaining boundaries

Offline checks cover real trigger/IRQ failure paths, range/wrap/rate helpers, CCF preservation, actual PWRAP write firewall, resolved DT/rail dependencies, ARM ABI, current expanded-RAM/reservation/relocation layout, emitted BOOTIMG and rootfs/fixture contents. Kernel and Buildroot logs retain failed compilation attempts followed by the resolved pass; no hardware success follows from these.

For remaining tests classify A card-probe, B PCM/DMA, C DMA-with-wrong-I2S, D DAC brownout/reset, E route/mute, F userspace underrun, G clock/rate faults. Required physical evidence: stable DMA/IRQ + correct second-I2S + powered DAC + clean audible headphones, then stop/restart/repeated44.1k and48k runs, no severe pop/noise/reset/kernel error. Speaker/jack/high resolution remain separately qualified. M4/M5/GPU/final platform work precedes Y2PlayerNative. USB reconnect#27 is explicitly deferred throughout this pass.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
