---
title: "Y2LINUX-M4-01 — integrated power candidate, manual deployment pending - Innioasis Updater"
description: "Y2LINUX-M4-01 — integrated power candidate, manual deployment pending <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, cand"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m4-01-deployment.html"
---

# Y2LINUX-M4-01 — integrated power candidate, manual deployment pending - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-M4-01 — integrated power candidate, manual deployment pending

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-M4-01 — integrated power candidate, manual deployment pending > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

This BOOTIMG retains the physically accepted Storage06 internal boot layout: Y2ROOT on eMMC p5, Y2DATA on p7, existing SSH identity and Buildroot userspace. No rootfs/data update is required. An SD card is optional. This is an M4 test candidate, not completed hardware qualification.

The [architecture and source reconciliation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-power-platform.md) records the live baseline, exact register/units/calibration assumptions, vendor references and limitations. The [activation audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md) keeps every physical acceptance gate open. M3's period-notification startup correction, commit 137b3f2, is retained.

## Implemented interfaces````````````

| Area | Candidate behavior |
| --- | --- |
| PMIC | One serialized MT6582 PWRAP → regmap → MT6323 MFD; regulator/key/RTC/poweroff plus ADC/charger/backlight children |
| Battery | /sys/class/power_supply/BAT0/: present, status, health, voltage_now; configured constant_charge_current/voltage are read-only limits, not measured current |
| USB | /sys/class/power_supply/y2-usb-presence/online, CHRDET event and polling |
| Charging | Inhibited. No validated pack thermometry/profile/input policy. Inherited current/CV retained; live baseline 70 mA/4.175 V. No capacity, current_now, battery temp or claimed full-charge detection |
| Thermal | thermal_zone*/type = cpu-thermal and pmic-thermal; calibrated temperatures in m°C only with valid own efuses; otherwise unavailable. CPU passive110°C/critical120°C, PMIC critical150°C from BSP |
| CPU frequency | One policy0 for CPUs 0–3:598000/747500/1040000kHz, all 1.15 V; default powersave; no VPROC write or overclock |
| Idle / suspend | Architectural WFI only; mem selects s2idle, freeze also available. No SPM/deep/DRAM power-down; retained eMMC controller/card state |
| Wake | Brief Power key; RTC alarm if valid and armed. USB, wheel and volume are not selected wake sources |
| Display / audio | DRM/panel/backlight PM, ordered ASoC/codec/AFE PM. VGP2 retained1.8 V. Physical repeat playback and resume tests still required |
| RTC | /dev/rtc0, standard read/set/alarm APIs; no automatic system/RTC time writes and no RTC spare/boot-state writes |
| Reboot / off | Upstream MediaTek AP watchdog software reset for reboot; MT6323 RTC BBPU/WRTGR power controller for actual poweroff. Charger watchdog is separate and untouched |

Battery voltage uses the MT6323 15-bit1.8 V ADC with hardware4:1 divider and inherited factory trim. There is no claim of independently measured absolute accuracy or external power consumption. PMIC die temperature is not pack temperature. The charger watchdog needs servicing for a future active charging policy; an inhibited charge engine requires no pet/re-enable loop.

## Build and package

The [final build receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-01%2FREADME.md) records the exact checks and retained logs. Kernel source commit: `f2d2ac641ee67cd94cd2c57c9f5201b6e78841fc`.

BOOTIMG: `out/y2linux-m4-01/BOOTIMG.img`, 5355520 bytes, SHA256 `5b2bdfa784aa790a81cd4c4f495ffcb1bd2dbfd2e26ffa33c0881c67967cb883`.

Rootfs update: NO. The unchanged reference image is `out/y2linux-production-v1-r4/Y2ROOT.img`, SHA256 `814a5b2543931e01cee2eb6f641c3b6e02317bd6308d2d663aea78f618bd554f`. The running Y2DATA, including its corrected owner SSH authorization, is preserved. Manifest root/data identities describe historical build inputs, not a hash claim about the subsequently mounted live filesystems.

The reproducible commands, run from the repository root with reviewed clean Git:`python3 tools/production/build.py --output out/y2linux-m4-01-build --reuse-userspace out/y2linux-production-v1-r4 python3 tools/production/boot_update.py --build out/y2linux-m4-01-build --base out/y2linux-production-v1-r4 --fallback-package out/y2linux-production-v1-r6 --output out/y2linux-m4-01`

The package contains `BOOTIMG.img`, `MT6582_BOOTIMG_only_scatter.txt`, manifest, hashes, and `fallback/BOOTIMG-previous.img`. The fallback is the working Storage06 BOOTIMG, SHA256 `3ba809e44bd9c945c994209d1d93f41fe0da9259a303487dd6ecf49724bf49a8`, 5193728bytes. The prior Storage04 rescue image is not the selected fallback.

## Owner's exact manual deployment
  - In `out/y2linux-m4-01`, verify `sha256sum -c SHA256SUMS`.
  - Use the established SPFT/DA procedure, Download Only. Load

`MT6582_BOOTIMG_only_scatter.txt` from that directory.
  - Select BOOTIMG → BOOTIMG.img only. All other rows remain unchecked,

including PRELOADER, LK/UBOOT, MBR/EBR, ANDROID, USRDATA and NVRAM. Do not select Format or Firmware Upgrade.
  - Perform the manual BOOTIMG flash and boot normally. Preserve existing

Y2ROOT/Y2DATA; no SD image and no rootfs installation are involved.
  - Keep USB connected for the main qualification. If the candidate cannot boot,

use the same BOOTIMG-only selection with `fallback/BOOTIMG-previous.img`.

The agent stops before deployment. The commands below are for the one physical qualification after the owner reports deployment; they have not been run on the current Storage06 kernel.

## Exact SSH qualification sequence

Host terminal, from the repository root:`y2ssh() { ssh -T -o BatchMode=yes -o ConnectTimeout=5 -o StrictHostKeyChecking=yes -i "$HOME/.ssh/y2linux_ed25519" root@10.42.0.1 "$@"; } y2ssh 'cat > /tmp/qualify-m4.sh' < tools/development/qualify-m4.sh y2ssh 'sh /tmp/qualify-m4.sh begin' y2ssh 'sh /tmp/qualify-m4.sh audio' y2ssh 'sh /tmp/qualify-m4.sh rtc' y2ssh 'sh /tmp/qualify-m4.sh dvfs' y2ssh 'sh /tmp/qualify-m4.sh idle' y2ssh 'sh /tmp/qualify-m4.sh display'`

`begin` records boot ID, four CPUs/RAM, exact internal mounts, power/thermal/ clock/regulator state, IRQs and logs in `/data/y2linux-m4-01/`. It writes a 256 KiB ordinary-file integrity sentinel in Y2DATA; no raw storage or mounted-fs fsck. `audio` repeats the proven 44.1 kHz stereo fixture at the existing -24 dB mixer setting, with output disabled between plays. Observe clean audible output twice. `dvfs` refuses load unless both calibrated die zones work and remain below 60°C and battery voltage is at least 3.4 V. These are conservative test-stop thresholds, not asserted battery/SoC protection limits. Each transition runs at most 5 seconds of four CPU loops, checks temperature each second, and restores powersave on exit. Failure is an acceptance result, not permission to bypass a guard.

Inspect `/proc/bus/input/devices` from the record. Test each identified event node with `y2ssh 'timeout 15 evtest /dev/input/eventN'`, replacing N with the actual Power/navigation/volume/wheel node. Press briefly; do not test emergency long-press shutdown. Observe display/backlight off/on and restored framebuffer without a black-screen or DRM warning.

Keep USB connected. First suspend uses the Power key alone:`y2ssh 'sh /tmp/qualify-m4.sh suspend' # Wait about 10 seconds with the display dark, then briefly press Power. y2ssh 'sh /tmp/qualify-m4.sh post-resume' y2ssh 'sh /tmp/qualify-m4.sh audio'`

The original SSH command should return after wake. Boot ID must stay identical; sentinel hash and both ext4 mounts must survive. Inspect PM wake IRQ, dmesg, USB, input and display. An early wake without the intended Power event is a failure to investigate. A USB session failure alone is not proof of reboot; CDC ACM diagnostics and the persistent logs can distinguish it. Do not repeatedly hard-reset a mounted rootfs. No alarm is silently installed as a rescue for the Power test because that would obscure its wake-source result.

RTC is read-first. If time is valid and no alarm was already configured:`y2ssh 'sh /tmp/qualify-m4.sh rtc-alarm'`

It programs only a 15 second alarm through the RTC API and tests a second s2idle entry. Do not press Power during this test. If the RTC was uninitialized, first record its original state, then deliberately set time using the host's UTC epoch and the normal API (no raw RTC/PMIC write):`y2_epoch=$(date -u +%s) y2ssh "date -u -s @$y2_epoch; hwclock -w -u; hwclock -r -u"`

Retain an existing alarm; do not clear it just to run the test. Record RTC again after the following reboot to assess persistence. No automatic boot-time write is installed.

Test a single cable cycle at the end, since the separately deferred USB reconnect issue can lose SSH. This explicitly schedules an orderly reboot after 40 seconds so the recorded observations can be recovered:`y2ssh 'nohup sh /tmp/qualify-m4.sh cable-reboot > /data/y2linux-m4-01/cable.log 2>&1 < /dev/null &' # Disconnect after about 5 seconds, leave disconnected 10 seconds, reconnect. # Wait for the scheduled reboot and normal USB enumeration. y2ssh 'cat > /tmp/qualify-m4.sh' < tools/development/qualify-m4.sh y2ssh 'sh /tmp/qualify-m4.sh post-reboot' y2ssh 'cat /data/y2linux-m4-01/cable.log; sh /tmp/qualify-m4.sh rtc' y2ssh 'sh /tmp/qualify-m4.sh audio'`

The log should show USB ONLINE1→0→1 with STATUS Not charging→Discharging→Not charging. No battery charge-current measurement or charge completion is claimed. If skipping the cable test, use `y2ssh 'sh /tmp/qualify-m4.sh reboot'` instead, then reload the `/tmp` script and run `post-reboot`. Verify the new boot ID, internal root/data, retained file hash, RTC, display, input and audio.

Finally test real hardware-off with USB disconnected to distinguish charger insertion/auto-boot behavior from failure to remove power:`y2ssh 'nohup sh /tmp/qualify-m4.sh poweroff > /data/y2linux-m4-01/poweroff.log 2>&1 < /dev/null &' # Disconnect USB during the 15-second delay. Observe actual hardware-off. # Briefly press Power for normal power-on, reconnect USB, then: y2ssh 'cat > /tmp/qualify-m4.sh' < tools/development/qualify-m4.sh y2ssh 'sh /tmp/qualify-m4.sh post-reboot'`

A halted kernel or dark display alone does not prove hardware-off. Record the physical outcome and subsequent normal power-on. No external current draw is invented. Retrieve the software records with:`y2ssh 'tar -C /data -czf - y2linux-m4-01' > out/y2linux-m4-01-physical.tgz`

The owner must observe: normal visible boot, clean audio before/after idle and resume, working controls, backlight/panel off/on, sustained suspend followed by the intended wake, safe cable behavior, normal reboot, actual poweroff and subsequent power-on. Missing calibration, charging inhibit, shallow retention and any failed hardware test remain explicit M4 limitations; driver probe alone does not close the milestone.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
