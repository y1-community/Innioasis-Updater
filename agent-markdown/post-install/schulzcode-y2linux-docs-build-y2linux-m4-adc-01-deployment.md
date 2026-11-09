---
title: "Y2LINUX-M4-ADC-01 — owner boot confirmed, charging inhibited - Innioasis Updater"
description: "Y2LINUX-M4-ADC-01 — owner boot confirmed, charging inhibited <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate ide"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m4-adc-01-deployment.html"
---

# Y2LINUX-M4-ADC-01 — owner boot confirmed, charging inhibited - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2LINUX-M4-ADC-01 — owner boot confirmed, charging inhibited

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2LINUX-M4-ADC-01 — owner boot confirmed, charging inhibited > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The owner has already deployed this kernel; no repeat flash is requested. It adds production IIO raw BATON1/ISENSE acquisition under the existing PMIC owner. [Physical result and charging gate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-battery-acquisition.md). It does not enable charging or report battery temperature/current/percentage.

Source commit: `bbd0664dcbc1190a5e16e3b3f5889f2154cb04fd`. [Build/package evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-adc-01%2FREADME.md).````````

| Item | Saved artifact |
| --- | --- |
| BOOTIMG | out/y2linux-m4-adc-01/BOOTIMG.img |
| Size | 5355520 bytes |
| SHA256 | c3c9778e396413fced69364190eb892456dd71c66a0c23fa650be2dcd30e7461 |
| Rootfs/data update | None; preserve Storage06 p5/p7 and existing SSH authorization |
| Fallback | out/y2linux-m4-adc-01/fallback/BOOTIMG-previous.img (M4-01) |
| Fallback size | 5355520 bytes |
| Fallback SHA256 | 5b2bdfa784aa790a81cd4c4f495ffcb1bd2dbfd2e26ffa33c0881c67967cb883 |

Reproduction from the clean source commit uses the normal production pipeline:`python3 tools/production/build.py --output out/y2linux-m4-adc-01-build --reuse-userspace out/y2linux-production-v1-r4 python3 tools/production/boot_update.py --build out/y2linux-m4-adc-01-build --base out/y2linux-production-v1-r4 --fallback-package out/y2linux-m4-01 --output out/y2linux-m4-adc-01`

For a future owner restoration of this saved package:
  - In its directory, run `sha256sum -c SHA256SUMS`.
  - Use the established SPFT/DA setup and Download Only; load

`MT6582_BOOTIMG_only_scatter.txt` from this package.
  - Select BOOTIMG only, pointing to `BOOTIMG.img`. Every other row stays

unchecked, including PRELOADER, LK/UBOOT, MBR/EBR, NVRAM, ANDROID and USRDATA. Do not use Format or Firmware Upgrade.
  - To restore M4-01 instead, use the same BOOTIMG-only selection with

`fallback/BOOTIMG-previous.img`. Neither image provides active charging.

The bounded SSH sampler and next physical sensor gate are documented in the linked knowledge page. No RTC setting, suspend, reboot/poweroff, raw-register write or active charge test belongs to this inhibited sensor qualification.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
