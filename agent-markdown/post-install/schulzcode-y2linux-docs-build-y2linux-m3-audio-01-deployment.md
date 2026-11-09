---
title: "Y2LINUX-M3-AUDIO-01 — owner deployment - Innioasis Updater"
description: "Y2LINUX-M3-AUDIO-01 — owner deployment <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m3-audio-01-deployment.html"
---

# Y2LINUX-M3-AUDIO-01 — owner deployment - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-M3-AUDIO-01 — owner deployment

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-M3-AUDIO-01 — owner deployment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

This is an unqualified audio candidate, not an M3 completion claim. The qualified DEV-02 core configuration and RAM reservations are retained. USB reconnect remains deferred as #27; do not cycle the development cable in this pass. No assistant flashing or live codec/PMIC register writes are authorized.

Artifact directory: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m3-audio-01/`. Exact sizes/hashes are in `SHA256SUMS` and `result.json`; verify before deployment:`cd /home/luca/Dokumente/Code/Y2Linux/out/y2linux-m3-audio-01 sha256sum -c SHA256SUMS`

## Update the removable SD content

Yes, the SD rootfs needs updating for ALSA utilities, fixtures, runtime fixes and the matching DRM module. Keep the existing Y2ROOT partition/filesystem and its persistent SSH host keys. `rootfs.tar` is the update source; `rootfs.ext4` is an independently validated fresh filesystem image, not an internal eMMC image. Do not write a whole filesystem image onto the currently mounted/live root.

Owner: shut down the Y2, remove its microSD and attach it to a Linux SD reader. Identify the actual removable card and its existing Y2ROOT partition with:`lsblk -o NAME,PATH,TRAN,RM,SIZE,FSTYPE,LABEL,UUID,MOUNTPOINTS`

Select only the physical SD reader/card whose ext4 partition has LABEL=Y2ROOT and UUID `79324c69-6e75-4801-8000-000000000001`. Do not guess a `/dev/sdX` target; do not use the PC system disk or any Y2 internal partition. Substitute that identified partition path below; these commands preserve files absent from the new tar, including old module trees and retained hardware logs:`Y2_SD_PARTITION=/dev/REPLACE_WITH_IDENTIFIED_SD_PARTITION sudo mkdir -p /mnt/y2root sudo mount "$Y2_SD_PARTITION" /mnt/y2root findmnt /mnt/y2root sudo tar -C /mnt/y2root --numeric-owner --overwrite \ --exclude='./etc/dropbear' --exclude='./etc/dropbear/*' \ --exclude='./root/.ssh' --exclude='./root/.ssh/*' \ -xpf /home/luca/Dokumente/Code/Y2Linux/out/y2linux-m3-audio-01/rootfs.tar sudo cat /mnt/y2root/etc/y2linux/build-id sudo test -s /mnt/y2root/root/.ssh/authorized_keys sudo test -x /mnt/y2root/usr/bin/aplay sync sudo umount /mnt/y2root`

Expected build-id is `Y2LINUX-M3-AUDIO-01`. This updates files without formatting or repartitioning. Keep the SD installed for the next boot.

## BOOTIMG-only SP Flash Tool procedure
  - Use the existing known-working Y2 scatter/download-agent workflow. Select

Download Only. Deselect every partition, then select BOOTIMG only.
  - Set BOOTIMG's file to this candidate's `BOOTIMG.img`. Inspect that PRELOADER,

LK, partition table, NVRAM/calibration and all other partitions are unchecked. Never select Format All or Firmware Upgrade.
  - With the Y2 powered off, click Download and perform the established connection

sequence. Wait for successful completion. The owner performs this operation.
  - Disconnect USB, boot with the updated SD, wait approximately ten seconds, then

attach USB once to the development PC. Expected kernel is `6.18.0-y2linux-m3audio01`. USB serial/observer tags retain DEV-01 compatibility.

## First SSH inspection — no playback yet

On the PC:`ssh -i /home/luca/.ssh/y2linux_ed25519 root@10.42.0.1`

On the Y2:`uname -a cat /etc/y2linux/build-id cat /proc/asound/cards cat /proc/asound/pcm cat /proc/asound/devices aplay -l aplay -L amixer -c Y2Audio cat /sys/kernel/debug/regulator/regulator_summary cat /sys/kernel/debug/clk/clk_summary dmesg`

Expected ALSA card ID/name: Y2Audio. PCM device 0 is Y2 Headphone Playback; use `hw:CARD=Y2Audio,DEV=0`. Initial CPU/PCM capabilities are **stereo S16_LE, 44100 and 48000 Hz**, not yet physically qualified. No capture or speaker PCM. AFE's internal back end is Y2 Second I2S, CPU DAI `I2S`, upstream codec DAI `cs43130-asp-pcm`. VGP2 must report 1800 mV, with the GPIO supply dependency chain present. The speaker GPIO8 hog must stay low.

If the card is missing, a supply enable failed, or dmesg reports a DAC reset, clock-ready timeout or I2C errors, collect evidence and stop before playback. Do not use i2cset/devmem, whole regmap dumps, or a high-gain speaker test.

## First controlled headphone test

Owner: insert headphones; keep them off your ears for the first short run. Headphone pin is disabled at card registration. Upstream PCM reset gain is -60 dB; no mixer state is automatically restored. Set a known conservative level, stereo routing, then enable the headphone endpoint:`amixer -c Y2Audio cset name='PCM Ch Select' 0 amixer -c Y2Audio sset Master 207,207 amixer -c Y2Audio sget Master amixer -c Y2Audio sset Headphone on`

Raw Master value 207/255 = -24 dB (0.5 dB steps). Confirm both channels show -24 dB. The fixture adds -30 dBFS peak, lasts three seconds and has 50 ms fades; left is 440 Hz and right 660 Hz. No sustained or full-scale tone.

In one SSH terminal, capture bounded live state during the test:`for n in 1 2 3 4 5; do cat /proc/uptime cat /sys/bus/platform/devices/11220000.audio-controller/state cat /proc/asound/card0/pcm0p/sub0/status sleep 1 done`

In the playback terminal, the exact first command is:`aplay -D hw:CARD=Y2Audio,DEV=0 --period-size=1024 --buffer-size=8192 /usr/share/y2linux/audio/headphone-44100.wav`

After it finishes:`y2-audio-collect > /tmp/m3-after-first.txt amixer -c Y2Audio sset Headphone off`

Report whether physical headphone output is audible/clean and whether each side is correct. Do not raise gain automatically if silent. After a clean first run, repeat two short 44.1 kHz runs, interrupt one with Ctrl-C and restart, then test `headphone-48000.wav` with the same command and constraints. Disable Headphone between test groups. Stop on loud noise/pops, DAC reset, corruption or kernel errors. Speaker, EINT16 jack/ACCDET and high-resolution formats remain separate.

## Evidence to correlate

Retain full `y2-audio-collect` output over SSH in repository hardware evidence before/during/after playback. Inspect ALSA hw_params/status and XRUNs, AFE IRQ counts in `/proc/interrupts`, cumulative period callbacks and current DMA pointer, CONN0, CON3, DMA bounds, codec probe/clock messages, regulator usage/1.8 V and CCF states. AFE `state` is a bounded read-only attribute that guards MMIO with runtime PM; do not dump its raw regmap when clock-gated. `/sys/kernel/debug/asoc/` exposes DAPM/card state. Do not equate DMA progress to external pad activity or audible output. Actual LRCK/BCLK accuracy may require physical clock measurement.

Classify failures before changing a layer: A card probe; B PCM/DMA; C wrong I2S with advancing DMA; D codec brownout/reset; E analog route/mute; F userspace underruns; G rate/clock accuracy. No M3 closure until physical playback, safe stop/restart, repeated runs and supported-rate checks pass without kernel errors.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
