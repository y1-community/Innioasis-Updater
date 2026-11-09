---
title: "Storage02 DIAG01 deployment - Innioasis Updater"
description: "Storage02 DIAG01 deployment <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-storage-diag-01-deployment.html"
---

# Storage02 DIAG01 deployment - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Storage02 DIAG01 deployment

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Storage02 DIAG01 deployment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The installed Storage02 rescue reports missing/invalid internal Y2ROOT or Y2DATA. Linux USB remains absent, including after the latest reported restart/attachment. This temporary diagnostic shows the cached USB state, internal block identity, root/data signature checks and kernel log tail on three rotating console pages. It stays in rescue and mounts no block filesystem. It is not a root/USB fix.

Rescue source commit: `8bf2d6404ee7f93c9244b124d7acea035e37e6c3`. Kernel/module source remains `c2db4893b79eca25458b6adc318232c80dd99872` and their bytes are unchanged. DT differences are limited to log verbosity and initrd extent. Package: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-storage-diag-01/`.````````

| File | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 5189632 | b45be7027c3b02186ec2e20cf1fec9cbb2a438bd9d4677b3528f905b6b869748 |
| MT6582_Android_scatter.txt | 7606 | fe45a3f1d94b8cf7a8f127c3120b6b595db7a9644927693b5aecabf656c5b7a1 |
| manifest.json | 2013 | 232019962913ab3d3bf9dcc8aa4bcc9bb516c0e555d16f34383cc2e1c5972814 |
| SHA256SUMS | 511 | b34afb5e19a55f6c3561cbd0e700b153fba5649cf413532bc2d20a0650c6cb0d |

SPFT v5.2032 Download Only, package scatter, BOOTIMG only selected. ANDROID, USRDATA and every other partition must remain unchecked. Never Format All or Firmware Upgrade. Stock BOOTIMG physical EMMC_USER start 0x01d80000, span 0x01000000; scatter linear/global start 0x03180000 is not a physical readback offset. Read back the 16 MiB span and compare its first manifest payload size bytes to the BOOTIMG hash above, retaining original target/DA identity evidence.

After flashing, disconnect USB. Boot unplugged; attach once at least ten seconds after Linux starts. No SD is required. Photograph PAGE 1, PAGE 2 and PAGE 3 as they rotate at roughly twelve-second intervals. There is no SSH/root handover. Expected empty-slot warnings stay in the kernel log without obscuring the screen.

[Complete install and exact BOOTIMG-only restoration](https://innioasis.app/guides/reborn-y2linux-y2.html). Returning to Storage02 uses its original 5187584-byte BOOTIMG with SHA256 6dfe7ff5de30f39581cc3479ed17d9a2fbf6671619741924d563f29114228d7d. The known AUDIO-02 + original SD fallback is also documented there. No root/data, loader/table/calibration restoration is part of either BOOTIMG-only path.

PASS seven targeted tests, ARM reader/rejections/blkid, shell syntax, exact base kernel/module, unchanged DT hardware fields, newc/D08/BOOTIMG/scatter and hashes. Physical display of these diagnostic pages is pending. Storage #33 remains active; no internal-root acceptance or new protected-byte readback is claimed. Stop for the owner's manual diagnostic flash. No assistant device write.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
