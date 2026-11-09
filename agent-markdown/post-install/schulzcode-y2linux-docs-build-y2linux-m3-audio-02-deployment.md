---
title: "M3-AUDIO-02 — corrected PCM notification candidate - Innioasis Updater"
description: "M3-AUDIO-02 — corrected PCM notification candidate <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m3-audio-02-deployment.html"
---

# M3-AUDIO-02 — corrected PCM notification candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M3-AUDIO-02 — corrected PCM notification candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M3-AUDIO-02 — corrected PCM notification candidate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Post-deployment update: AUDIO-02 is owner-flashed and now has [clean 44.1 kHz physical playback](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-01-live-result.md), including the period-notification correction. The [ALSA tools are now installed persistently on SD](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Faudio-tools-sd.md). Use standard `aplay`/`amixer` paths; the temporary-tool instructions below record the original artifact handoff and are superseded for this device.

Owner manual deployment only. Built on 2026-09-10 from the startup fix in `137b3f2`, with release `6.18.0-y2linux-m3audio02`. M3-AUDIO-01 produced audible headphone sound with clicking; clean playback is not yet qualified. This fixes positive ALSA constraint success skipping substream attachment and therefore period notifications. No route, clock, voltage, gain, memory or DT source change.

## Flash this image

`/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m3-audio-02/BOOTIMG.img`

Size: 4816896 bytes. SHA256:`b9dbf6b528e4afbee2a5ffb2fc65df7f6a076564e92960332e24cee3809b5842`
  - In the established SP Flash Tool scatter/download-agent setup choose

Download Only. Deselect everything, then select BOOTIMG only.
  - Select the exact file above. PRELOADER, LK and every other partition remain

unchecked; never choose Format All or Firmware Upgrade.
  - Owner powers off the Y2, clicks Download and uses the established connection

sequence. Wait for success, disconnect USB, boot with the existing SD, then attach USB once after startup. The assistant does not flash or reboot.

No SD update is required for this kernel correction. The matching DRM module is embedded in the rescue initramfs and loaded before SD handoff. Existing SD content and SSH keys remain usable. SD is still DEV-01 without permanent ALSA utilities: after boot we restage the reproducible temporary ALSA bundle via SSH. The previously built M3-AUDIO-01 rootfs remains the optional persistent utility update; no rootfs rebuild/image is produced for AUDIO-02. USB reconnect #27 stays deferred. Do not reuse AUDIO-01 BOOTIMG for this correction.

## First inspection and controlled playback`ssh -i /home/luca/.ssh/y2linux_ed25519 root@10.42.0.1 uname -r cat /proc/asound/cards cat /proc/asound/pcm cat /sys/bus/platform/devices/11220000.audio-controller/state dmesg`

Expected release: `6.18.0-y2linux-m3audio02`; card `Y2Audio`, PCM0 `Y2 Headphone Playback`, `hw:CARD=Y2Audio,DEV=0`. Initial format/rates remain stereo S16_LE at 44100/48000 Hz. Once tools are restaged at `/tmp/y2-m3-audio-aa3c949` and the owner confirms headphone readiness:`cd /tmp/y2-m3-audio-aa3c949 ./amixer -c Y2Audio cset name='PCM Ch Select' 0 ./amixer -c Y2Audio sset Master 207,207 ./amixer -c Y2Audio sget Master ./amixer -c Y2Audio sset Headphone on ./aplay -D hw:CARD=Y2Audio,DEV=0 --period-size=1024 --buffer-size=8192 audio/headphone-44100.wav ./amixer -c Y2Audio sset Headphone off`

Master 207 is -24 dB; the three-second fixture peaks at -30 dBFS with fades. During the supervised test use the retained shell watchdog/cleanup pattern: old SD has no `timeout` utility. Correlate playback elapsed time, PCM hw_ptr, AFE IRQ/period count and DMA CUR, CON3/CONN0, XRUNs, regulator/ASoC state and dmesg; confirm VGP2 1.8 V and no DAC reset. Require clean owner listening feedback, then short stop/restart/repeated runs and 48 kHz before accepting wired audio. A watchdog-triggered exit0 is not a completed WAV. Speaker/jack/high-resolution paths remain separately unqualified.

## Reproduction and validation

Reuse AUDIO-01's isolated kernel output via an independent reflink/copy into a fresh AUDIO-02 directory, and copy its Buildroot target and three rescue helpers. Run the canonical `configure.sh` (only LOCALVERSION differs), then one incremental `make -C /src O=/build/kernel -j12 Image zImage modules` through `tools/build/run.py --output out/y2linux-m3-audio-02`. Reuse pinned userspace; do not rebuild Buildroot. Then in that isolated environment, from `/project`:`python3 -m tools.build.dev_initramfs sh tools/build/dtb.sh python3 -m tools.validation.dev_artifacts /build --package Y2_ARTIFACT_TEST_ROOT=/build python3 -m unittest discover -s tests -p 'test_audio*.py' -v`

PASS: four targeted production-code/DT tests; exact ELF/Image/zImage, rescue module ABI, RAM/decompressor/reservation layout, eMMC-disabled DT and BOOTIMG validation. Resolved config equals AUDIO-01 except LOCALVERSION; rescue helper hashes are unchanged. Full build/validation logs retained as compressed evidence. This is offline validation, not physical acceptance of the correction.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
