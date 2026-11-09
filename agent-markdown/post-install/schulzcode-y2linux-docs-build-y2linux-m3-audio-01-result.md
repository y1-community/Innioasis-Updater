---
title: "M3-AUDIO-01 integrated candidate — offline result - Innioasis Updater"
description: "M3-AUDIO-01 integrated candidate — offline result <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m3-audio-01-result.html"
---

# M3-AUDIO-01 integrated candidate — offline result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M3-AUDIO-01 integrated candidate — offline result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M3-AUDIO-01 integrated candidate — offline result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Historical build result. AUDIO-01 was deployed and exposed a PCM notification bug. AUDIO-02 fixes it and now has clean44.1kHz physical playback. See the [current audio result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-01-live-result.md). The original artifact hashes and offline status below describe packaging time only.

2026-09-10. PASS offline; physical M3 audio remains untested. Owner manual BOOTIMG-only deployment is the next boundary. No device flash, reboot, raw codec or PMIC write, reconnect experiment or Y2PlayerNative implementation occurred.

Qualified DEV-02 baseline `d76e57f`; current source commit is the Git revision containing this result and the implementation. Final output `result.json` records that exact Git HEAD after commit; `source-manifest.json` hashes only the changed source delta against DEV-02. No complete donor/kernel/ROM hash pass was repeated.

[Architecture/source review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-architecture.md) · [Exact deployment and first commands](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m3-audio-01-deployment.md) · [Retained validation](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/evidence/y2linux-m3-audio-01/) · [Physical entry evidence](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-10-m3-entry/).

Output: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m3-audio-01/`. Kernel `6.18.0-y2linux-m3audio01`, Buildroot2025.02.17, ALSA utilities1.2.13.``````

| Artifact | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 4816896 | 126243845ef3ecdc5ac81f654e8ef0d09d2782dbce48117a4c5b65a8b0d5f92e |
| rootfs.ext4 | 536870912 | 742bf915ec74cd2f5bc8c5a8f5be40eff8d2c5d5b1b12fb881c84c59e9bd4610 |
| rootfs.tar | 23296000 | 732c10ad77f58867c434bc53dd870a39f089c4eb836d7cf1f540498b3adad3c3 |

ALSA card Y2Audio, PCM0 Y2 Headphone Playback, endpoint `hw:CARD=Y2Audio,DEV=0`; initially stereo S16_LE at44100/48000Hz. DL1->O00/O01-> CON3->upstream CS43131, VGP2 regulator1.8V, ordered GPIO20/18/15. SpeakerGPIO8 held low; headphone disabled until manually enabled. Master207=-24dB, generated three-second WAV=-30dBFS with fades. No speaker/jack/high-resolution acceptance.

## Validation actually performed

One clean kernel tree and one fresh Buildroot tree; in-place fixes for Linux6.18 API differences and reviewed allocation/shutdown behavior. Final kernel compile has no warnings/errors. Historical failed compilation diagnostics remain in the complete compressed log. Buildroot completed, including ALSA/libdrm test utilities. A harmless missing documentation formatter in a host dependency was ignored by that upstream build; it did not affect installed artifacts.

All 13 targeted tests passed, covering production trigger/IRQ fault injection, 32-bit DMA/ring boundaries, both rate codes, CCF preservation of adjacent SD fields, actual PWRAP masks/failures, resolved audio DT mutations, preserved RAM and eMMC protections, rescue isolation, I2C combined transfers and ARM ABI. Cortex-A7 QEMU runs pass the ABI check and aplay/amixer version execution. Shell scripts pass target-BusyBox syntax checking. No software test claims real DMA timing, I2S pads or analog sound.

Emitted ELF/Image/zImage/module/DT/rescue and BOOTIMG checks pass. Linux bank and all reservations match DEV-02. Before kernel reservations, allocator-described RAM remains997179392bytes (951MiB minus16KiB). Resident kernel span grows from 10626240 to10910080bytes, about277KiB; next-boot actual MemTotal must be recorded, not forced to equal DEV-02's954660KiB. Four CPUs/HIGHMEM/core config stay enabled. BOOTIMG is below the16MiB partition limit, including validated LK read padding.

Both rootfs tar and512MiB ext4 contents pass checks; read-only e2fsck passes. ELF ABI, key permissions/policy, matching module, aplay/amixer/speaker-test/evtest, fixture formats/duration/peaks and no mixer auto-restore are checked. SSH host keys are not generated into the image; the owner's authorized public key is retained. Existing removable SD content needs an offline update from rootfs.tar, preserving its persistent SSH keys. No partitioning/formatting is required.

## Boundary audit and actual physical status

Rechecked current coverage against DEV-02 physical evidence and explicit owner M3 authorization. Core SD/SSH/initial USB, four CPUs/expanded RAM, visible display, wheel/buttons and PMIC/core buses retain their narrow physical acceptance. M3 source/build readiness advances, physical audio does not. #29 stays open and active. #27 reconnect remains explicitly deferred under #28 for later whole- platform qualification. #30 full power, #31 connectivity and #32 GPU/final platform work precede Y2PlayerNative. No older research task reopens qualified core acceptance. After owner deployment, classify A–G failures by layer and require clean audible output plus stable DMA/IRQ/CON3/power and repeated start/stop/rates.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
