---
title: "Beta V2 Updater Package Formats - Innioasis Updater"
description: "Beta V2 Updater Package Formats Updated: 2026-09-06 Distribution decision Beta V2 is distributed only as a Class A state-preserving update: Platform Filename Size SHA-256"
language: "en"
source: "https://innioasis.app/post-install/spycemagic-y2-rockbox-00_project_docs-y2_beta_v2_updater_formats.html"
---

# Beta V2 Updater Package Formats - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=rockbox-y2)

Post-install setup · Rockbox-Y2 · Y2

# Beta V2 Updater Package Formats

The Y2 Rockbox build. Select Y2 before choosing this Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=rockbox-y2)[Install guide](../guide.html?model=Y2&software=rockbox-y2)

# Beta V2 Updater Package Formats

Updated: 2026-09-06

## Distribution decision

Beta V2 is distributed only as a Class A state-preserving update:````````

| Platform | Filename | Size | SHA-256 |
| --- | --- | --- | --- |
| macOS | Y2-Rockbox-Beta-v0.2.0-UPDATE-ONLY.zip | 361,774,260 | 409DDB4D2D18111FB8C3AB619F10F04B916B6B2A3FC04D1D38011324563F326A |
| Windows | Y2-Rockbox-Beta-v0.2.0-Windows-UPDATE-ONLY.zip | 361,774,260 | 409DDB4D2D18111FB8C3AB619F10F04B916B6B2A3FC04D1D38011324563F326A |

The files are byte-identical. Different filenames let each guarded updater bind to an exact platform-qualified contract without relying on a generic filename.

## Archive contract

The ZIP contains exactly eight members:
  - `MT6582_Android_scatter.txt`
  - `lk.bin`
  - `boot.img`
  - `recovery.img`
  - `logo.bin`
  - `system.img`
  - `UPDATE-MANIFEST.json`
  - `SHA256SUMS.txt`

It excludes PRELOADER, MBR, EBR1, SEC_RO, EBR2, CACHE, USRDATA, and every protected/runtime partition. The only permitted write set is UBOOT, BOOTIMG, RECOVERY, LOGO, and ANDROID.

Format All, Firmware Upgrade, whole-device erase, omitted-partition cleanup, protected-partition writes, and automatic retry are forbidden. The updater must verify the exact release repository, tag, filename, size, digest, device identity, and Stock 3.1.7 layout before writing. It must then complete all five readbacks before reporting success.

## Why `rom_y2.zip` is forbidden

`rom_y2.zip` is not a Beta V2 asset. Testing proved that the legacy name enters an unqualified generic full-firmware path. That path produced non-booting and looping devices even though the underlying Rockbox runtime itself was valid. The withdrawn packages and old `InnioasisUpdater_Setup_1.1.2.exe` must not be used.

The reviewed Updater CE V30 route accepts only:
  - repository `SPYCEMAGIC/Y2-Rockbox`;
  - release `v0.2.0-beta`;
  - Windows filename `Y2-Rockbox-Beta-v0.2.0-Windows-UPDATE-ONLY.zip`;
  - size 361,774,260 bytes; and
  - SHA-256 `409DDB4D2D18111FB8C3AB619F10F04B916B6B2A3FC04D1D38011324563F326A`.

It explicitly rejects the retired community mirror, `rom_y2.zip`, any changed payload identity, and any write plan outside the five permitted targets.

## Qualification

The macOS and Windows routes each passed from a fresh official Stock 3.1.7 restore through write, full readback, mandatory unplugged pinhole reset, and the complete functional matrix. The Windows source correction compiled and passed 25/25 focused tests plus a final offline Windows publication-source receipt.

These are Rockbox-Y2's own instructions, shown here word for word.

Published by the [spycemagic/y2-rockbox](https://innioasis.app/firmware.html?model=Y2&software=rockbox-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=spycemagic%2Fy2-rockbox&software=rockbox-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aspycemagic)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
