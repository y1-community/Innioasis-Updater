---
title: "Storage06 internal boot and owner SSH — accepted on hardware - Innioasis Updater"
description: "Storage06 internal boot and owner SSH — accepted on hardware <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate ide"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-production-v1-r6-deployment.html"
---

# Storage06 internal boot and owner SSH — accepted on hardware - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Storage06 internal boot and owner SSH — accepted on hardware

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Storage06 internal boot and owner SSH — accepted on hardware > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The owner flashed the single corrected Storage06 BOOTIMG, then the corrected initial Y2DATA image. SSH now authenticates with the existing `~/.ssh/y2linux_ed25519` identity. Internal Y2ROOT and Y2DATA mount read-write without an SD block device. No further flash is needed for this fix. [Authenticated physical evidence](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage06-owner/ssh-result.json) and [retained data-package checks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-production-v1-r6-owner-key%2FREADME.md).

## Root cause and production correction

The production eMMC port omitted the stock logical disk translation. Linux sector 0 was reading the reserved native prefix instead of the intact MBR. The actual stock driver adds 23552 sectors and exposes a 15203328-sector disk. Storage06 restores that mapping once for CMD17/18/24/25, leaves EXT_CSD and companion command arguments intact, and keeps writes limited to the original ANDROID/USRDATA spans. Upstream Linux parses the existing MTK tables; no table, DT, hardware clock or memory change was needed. See the [source and stock-binary proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage06-addressing-correction.md).

The original data template separately authorized a public key whose private counterpart was missing. The corrected seed uses the owner's existing `.pub` file exactly. No client identity was generated, inspected or copied. Normal production packaging now defaults to that existing public file and validates the authorization inside the completed Y2DATA filesystem before publication. `/root/.ssh` resolves into persistent Y2DATA; BOOTIMG/Y2ROOT updates preserve it.

## Exact artifacts

All paths below are relative to the repository root.````````````````````

| Artifact | Path | Bytes | SHA256 |
| --- | --- | --- | --- |
| Working BOOTIMG | out/y2linux-production-v1-r6/BOOTIMG.img | 5193728 | 3ba809e44bd9c945c994209d1d93f41fe0da9259a303487dd6ecf49724bf49a8 |
| Unchanged Y2ROOT | out/y2linux-production-v1-r4/Y2ROOT.img | 536870912 | 814a5b2543931e01cee2eb6f641c3b6e02317bd6308d2d663aea78f618bd554f |
| Corrected owner-key Y2DATA seed | out/y2linux-production-v1-r6-owner-key/Y2DATA.img | 838860800 | 9e0f6b063b2ccfe7bb97bd229f0140cd47aebd917ed636b36e7fa6740ab22fe1 |
| Historical Storage04 rescue fallback | out/y2linux-production-v1-r6/fallback/BOOTIMG-storage04.img | 5193728 | 2f9d27a9d306ef5d49a1378f5063a7178edc18dec777340bf78330a23ac3a4f6 |
| Original data seed, wrong owner key | out/y2linux-production-v1-r4/Y2DATA.img | 838860800 | 01bcf65da1716081707202af074969e21fc1196540cb1de6ca76ef9098d44079 |

Kernel source: `bea30cd5883f524a252d8b94d7e914d9d2f7cbdb`. Owner-key packaging source: `dcb7f45fd7fbe0adffc10195239f8df934491c8b`. The root filesystem retains its Storage04 build metadata; the running kernel and its BOOTIMG-owned modules are Storage06. The independent component contract permits this unchanged userspace reuse.

The BOOTIMG digest above now matches a complete 5193728-byte read through the running Linux block device. The Y2DATA digest identifies the unused flash seed; mounted data subsequently changes as the system creates persistent host keys. The old rescue fallback restores the known rescue/ACM state, not working internal boot. The original data seed restores its old authorization failure.

## Manual selections used for this correction

Storage repair: SPFT Download Only, load `out/y2linux-production-v1-r6/MT6582_BOOTIMG_only_scatter.txt`, select BOOTIMG only.

Owner-key initialization: SPFT Download Only, load `out/y2linux-production-v1-r6-owner-key/MT6582_Y2DATA_only_scatter.txt`, select USRDATA → `Y2DATA.img` only. BOOTIMG, ANDROID and every other row stay unchecked. Never select Format or Firmware Upgrade. This initialization replaces Y2DATA, including its initial state and generated server host keys; the owner confirmed there were no saved files or settings to retain. It is not a normal system update.

Both manual flashes have now been reported complete. MBR/EBR1/EBR2 remain byte-identical to the stock fixtures through Linux reads. Y2ROOT is p5 at 166912 + 1679360 sectors; Y2DATA is p7 at 2104320 + 1638400 sectors.

## Physical acceptance

The completed test is a boot with no SD block device followed by:`ssh -i ~/.ssh/y2linux_ed25519 root@10.42.0.1`

Authenticated read-only commands confirm Linux 6.18.0-y2linux-storage06, both internal ext4 mounts, exact geometry/UUIDs, four CPUs, 954376 KiB RAM and USB ECM 10.42.0.1/24. The public file in live Y2DATA has SHA256 `bf9cc937fb5dcee8569514b674fb9b3d5ba25396162efac7e8854f88bfe98c25`, matching `~/.ssh/y2linux_ed25519.pub` and fingerprint `SHA256:IS9HhrmQKRtlEEbrcJjZa0XQHVwnRXRUzQQ61/7XAb8`. The host USB profile is 10.42.0.2/24 with no default route. The host's obsolete 10.42.0.1 server-key entry was replaced with the public key verified after initialization; the normal SSH configuration now succeeds too.

54 firmware regressions, ARM shell/ABI checks, BOOTIMG bounds and 13 package rejection cases passed before the kernel flash. The localized SSH change passed five focused source tests, ARM filesystem identification, ext4 integrity checks, exact public-key validation and 11 isolated data-package rejection cases.

Two synthetic ext4 buddy-cache inode warnings remain recorded; filesystem checks complete cleanly and the system boots. No deliberate physical scratch write, protected-region write, stress or power-fail test was performed. Those wider qualification gates and #33 remain open; this pass activates no later subsystem.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
