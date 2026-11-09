---
title: "Hardware 02 — coherent hardware ceiling candidate - Innioasis Updater"
description: "Hardware 02 — coherent hardware ceiling candidate <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-platform-v1-hardware-02.html"
---

# Hardware 02 — coherent hardware ceiling candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Hardware 02 — coherent hardware ceiling candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Hardware 02 — coherent hardware ceiling candidate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

IMAGE_VALIDATED_PHYSICAL_PENDING, 2026-09-26. The installed unit still runs Physical 01. This is a single preserving BOOTIMG + root update, not a frozen hardware platform or a qualified performance ceiling.

Local package: `out/y2linux-hardware-02-candidate/`. Read its `install.md`, `qualification.md`, `manifest.json` and `validation/summary.json`. Exact fallback is the currently installed Physical 01 pair; no Y2DATA payload, formatting, repartitioning or protected-region write.

## Identity and images
  - Linux `76bc8229580ec8d101008c5bad47419f2c110eae`
  - Reborn `95747e0a36c7b27beb44b8cdd54feda1813f2f3a`
  - Build `Y2LINUX-HARDWARE-02`, release `1.0.0-candidate.4`
  - Kernel `6.18.0-y2linux-hardware-02`, root `2025.02.18-platform-v1.4`
````````

| Image | Bytes | SHA-256 |
| --- | --- | --- |
| BOOTIMG.img | 6782976 | b2a2c3bcb7cc7783828882e447e8b867453cb5b65846ce63577076b1ca4afeea |
| Y2ROOT.img | 536870912 | 63dbd0a198cd86e847c10ed163fd14b2cbe269595fa1988c99ac8393160bb547 |
| fallback/BOOTIMG.img | 6768640 | f3309fd98e204da9013636c67a3cff9ab359cf92eae6f320d8c536853115a151 |
| fallback/Y2ROOT.img | 536870912 | e21ee81570a1beef7ea007bb992abcebfb78992686c66124aa3b0f357fcb2840 |

## Included scope
  - eMMC/SD retain 8/4-bit wiring and 3.3 V, adding source-backed SDR high-speed

negotiation with a 25 MHz initial cap and bounded 13/25/50 MHz qualification controls. Failed clock changes restore the previous state; unrecoverable clock restoration rejects requests before command/DMA. Boot parameter `y2.mmc_safe=1` retains the crystal/legacy path. No DDR/UHS/HS200 mode.
  - MUSB uses upstream Inventra DMA, 32-bit addressing, exact stock interrupt

ownership, DMA bus-fault teardown and overflow observations. Boot parameter `y2.usb_dma=off` and allocation failure retain PIO. No host VBUS activation.
  - GPT6 is initialized through its existing owner and checked against GPT2

before registering the physical architectural timer on PPI29. This provides the implementation for local high-resolution/NO_HZ timers. Initialization failure or `y2.local_timer=off` retains GPT/dummy behavior. Integrated physical continuity, interrupt delivery and hotplug remain acceptance gates.
  - Reborn includes the physically tested native PCM device-name contract repair.

The suspend helper now reports radio restoration failure instead of rc=0. USB overflow snapshots improve diagnosis; the suspend fault is not fixed.

## Validation and limits

170 locked production tests pass; three additional tests are explicitly skipped for absent native dependencies and covered by passing packaging-host runs (18 filesystem/preservation tests and nine GIO/ALSA tests). Reborn's workspace passes 180 tests. Eight Reborn ARM/QEMU checks, target ABI/shell checks, 20 target Python module imports, SQLite WAL/checkpoint, ALSA null queries, a 1k target library scan, and three actual ARM SFTP protocol/failure cases pass.

Kernel/config/DT, zero-fuzz overlay identities, D08/LK read extent, BOOTIMG, rescue/module release, regulatory database equality, root contents/clean ext4, protected-storage policies, preserving scatter and exact fallback validate. Inventory covers 102 packages. Source bundles, source pins, license collection results and failed-attempt explanations accompany the package. Byte-identical userspace rebuilds and firmware redistribution permission are not established.

The real unit recovered after the suspend incident with a fresh boot, exact Physical 01 identity, taint 0 and zero ext4 error counters. Its persistent log proves CPU3/2/1 restart but exposes USB overflow and radio restore timeout; core/SPM entry and deep wake remain open. Checked DNS passes; a transient supplicant observer timeout remains. RTC standard UTC write/read/ticking pass, while retention/alarm wake remain pending.

## First physical acceptance

After the owner flashes once, verify the exact new source pair and boot ID, root/data recovery, pinned USB SSH, taint, MMC errors/IOS and conservative cap, checked DNS/TCP, menu, wired/BT audio and thermal/memory telemetry. Inspect actual DMA counters and per-CPU clockevents before interpreting performance.

Then measure 25 MHz storage repeatedly with readback/fsync/metadata/SQLite, qualify the SD's negotiated mode, and only raise the host cap to an evidenced 50 MHz after clean results. Repeat RAM/storage-separated USB tests, timer continuity/NO_HZ and core cycles with safe fallbacks. Record failures rather than promoting modes merely because they boot. Further suspend uses one detached, persistently recorded stage and verified subsystem/host recovery before the next stage. No unattended multi-stage suspend loop.

[Campaign measurements](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-HARDWARE-CEILING.md), [issue evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-ISSUES.md), [admission audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23hardware-02-candidate-handoff--2026-09-26&anchor=hardware-02-candidate-handoff--2026-09-26).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
