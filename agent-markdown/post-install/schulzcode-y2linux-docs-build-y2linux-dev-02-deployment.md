---
title: "DEV-02: BOOTIMG-only correction for the existing SD root - Innioasis Updater"
description: "DEV-02: BOOTIMG-only correction for the existing SD root <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identit"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-dev-02-deployment.html"
---

# DEV-02: BOOTIMG-only correction for the existing SD root - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# DEV-02: BOOTIMG-only correction for the existing SD root

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# DEV-02: BOOTIMG-only correction for the existing SD root > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Use `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-dev-02/BOOTIMG.img`. It is 4,683,776 bytes, SHA-256: `3afbc15950e75d0477036709aabf32ceb2101ff090a6625ba5e9f7d5e840df05`.

The SD card already mounts and its Y2ROOT was verified on the Y2. **Keep its contents; no Mac transfer or SD rewrite is needed for this test.** Companion rootfs.ext4/rootfs.tar are the unchanged DEV-01 base, with the same public key.
  - Owner uses the existing SP Flash Tool workflow: Download Only, BOOTIMG only,

selecting this new file. No Format/Firmware Upgrade, PRELOADER, LK, partition table, NVRAM/calibration, other Android partitions or internal rootfs writes.
  - Leave the prepared SD installed. Boot USB unplugged and attach to the Linux

PC after ten seconds, so logging can begin before the root transition.
  - If the host again denies tty access, run `sudo setfacl -m u:luca:rw /dev/ttyACM0`

for the actual current Y2 ACM device. Device permissions can reset on reconnect.
  - Tell the assistant it is deployed. It can start a fresh 180-second capture and

collect Ethernet/SSH, memory, input and SD state together. No separate register test image is needed.

Expected new kernel release: 6.18.0-y2linux-dev02. USB serial and LOG1 header intentionally retain Y2LINUX-DEV-01, the installed userspace identity. The capture command therefore remains:`cd /home/luca/Dokumente/Code/Y2Linux python3 tools/observation/usb_log_capture.py --build Y2LINUX-DEV-01 \ --seconds 180 --output out/y2linux-dev-02/capture-01`

The new child probe should log Y2ABI checks for Thumb signals, kernel helpers, threads/TLS, floating point and allocation, then PASS. Failed probes keep rescue PID1 alive and log the failure. Unknown subsequent faults print registers and instruction information with `user_debug=31`; if the screen stops, retain a photo of the final output. A passed preflight is not proof that every init path works.

Observe the color pattern and console, exercise the wheel and all buttons. After Y2ROOT switches, the expected target remains 10.42.0.1/24 and key-only SSH. The matching private key must be available through the owner's SSH agent; the assistant uses only the public identity path and never inspects the private file.

DRM loads the exact DEV-02 module from rescue before switching root. The installed SD module directory still names DEV-01, so avoid unloading/reloading DRM before its module directory is refreshed. `sd-module-update.tar` contains only the matching `/display.ko` and `/lib/modules/6.18.0-y2linux-dev02/` files/indexes. After SSH works and `/` is verified as the removable Y2ROOT, the assistant can apply that small update there. No whole SD rewrite is required.

All offline checks pass. Physical correction of the SIGILL and wheel regression, pattern visibility, persistent USB reconnect, Ethernet and SSH remain unproved until this deployment is observed. Internal eMMC stays disabled.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
