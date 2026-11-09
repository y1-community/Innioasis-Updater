---
title: "Reborn Product UI v2 candidate receipt - Innioasis Updater"
description: "Reborn Product UI v2 candidate receipt <!-- knowledge-base-scope: scoped-validation-record -- Software receipt, 2026-10-01. Built and software-validated. Not flashed, not"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-reborn-product-ui-v2.html"
---

# Reborn Product UI v2 candidate receipt - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Reborn Product UI v2 candidate receipt

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Reborn Product UI v2 candidate receipt > **Software receipt, 2026-10-01.** Built and software-validated. **Not > flashed, not physically qualified.** The [Fix02 physical report](Y2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md) > remains the latest observed hardware state; the [Fix03 receipt](Y2-CPU-FINAL-FIX03.md) > remains the CPU platform change set this candidate is built on. 

This candidate is the CPU Final Fix03 platform with the Reborn Product UI v2 pass ([product UI](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V2.md), [navigation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-NAVIGATION-V2.md), [platform boundary](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fplatform-api-boundary.md), [pass record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Freview%2FREBORN-PRODUCT-PASS-V2.md)).

## Platform changes in this candidate````````````````````

| Change | Source | Effect |
| --- | --- | --- |
| Early splash shows the Reborn mark | tools/graphics/reborn-splash.c, reborn-splash-mark.h, make-splash-mark.py | The mark is generated from Reborn's own boot frame; a test proves the splash frame and Reborn's hand-off frame are pixel-identical. Only the gold rule breathes while startup continues. Console policy, handoff protocol, charger/voltage gate and 60 s failure timeout unchanged. |
| Backlight off before power-down | tools/platform/y2_platform/power.py | After stopping or killing Reborn and before busybox poweroff/reboot, every backlight's bl_power is set to 4. A crashed or hung Reborn can no longer leave the fbdev-restored buffer lit. |
| Release identity | tools/production/release.json | Release 1.0.0-reborn-product-ui-v2-candidate.1, root 2025.02.18-platform-v1.10, build Y2LINUX-REBORN-PRODUCT-UI-V2. |

The kernel, its configuration and modules are the Fix03 source: the built `zImage` and `display.ko` are byte-identical to Fix03's. In the initramfs only `sbin/reborn-splash` changed intentionally. `sbin/blkid` differs because Buildroot overwrites the build-time RPATH with `X` filler of the build directory's length (a different worktree path). Symbols, versions and behaviour are identical. The device tree differs only in `/chosen/linux,initrd-end`.

## Identity````````````````

| Field | Value |
| --- | --- |
| Linux built source | 5cfe04cb2fe9e1177df99f3113b7a17ee7d442f5 |
| Reborn built source | bd8436dd2afcdbe4a45b9140aa98e4d20307482b (0.2.0) |
| Kernel | 6.18.0-y2linux-cpu-final-fix03 (unchanged) |
| Root / release / build | 2025.02.18-platform-v1.10 / 1.0.0-reborn-product-ui-v2-candidate.1 / Y2LINUX-REBORN-PRODUCT-UI-V2 |
| Fallback | Exact Hardware02 pair (6.18.0-y2linux-hardware-02, 2025.02.18-platform-v1.4) |

## Fresh validation``````````````

| Check | Result |
| --- | --- |
| Reborn cargo fmt --check, clippy --workspace --all-targets --locked -D warnings | PASS |
| Reborn cargo test --workspace --locked | PASS, 211 tests (incl. architecture guard) |
| Production/platform regression (tools/production/tests.sh, container) | PASS, 268 tests, 3 explicit native-dependency skips |
| Native host-dependency tests (test_system_update_fallback) | PASS |
| Splash protocol, pixels and hand-off identity (test_reborn_splash) | PASS, 10 tests |
| Reborn ARM QEMU check, installed ARM modules | PASS |
| ELF dependency closure, no build RPATH | PASS |
| Release inventory, legal-info | PASS |
| Preserving package (system_update.py) | PASS: clean ext4, BOOTIMG/Y2ROOT only, no Y2DATA payload, exact Hardware02 fallback |

A first build from Reborn `94e79d8` was superseded before sealing by a wording fix (two empty states) and documentation; its logs are kept in `out/reborn-product-ui-v2/superseded-94e79d8/`.

## Candidate

`out/y2linux-reborn-product-ui-v2-candidate/` — `MT6582_preserve_data_scatter.txt` selects only BOOTIMG and ANDROID/Y2ROOT. No Y2DATA/USRDATA, preloader, LK, NVRAM, PROTECT, calibration or factory payload. Nothing was flashed or pushed.````````````````

| File | SHA-256 |
| --- | --- |
| BOOTIMG.img | 8a974cb5dc672dd0f2a6589a3b8da08a7225879ee7c60e929ed398bbd293e7bf |
| Y2ROOT.img | a5c2914ed688ff1bc5eecad276a071d084995b47c1ad8c2b1de21182e79f474c |
| fallback/BOOTIMG.img | b2a2c3bcb7cc7783828882e447e8b867453cb5b65846ce63577076b1ca4afeea |
| fallback/Y2ROOT.img | 63dbd0a198cd86e847c10ed163fd14b2cbe269595fa1988c99ac8393160bb547 |

## What the owner should look at on the device
  - Power-on: stock LK logo, then the Reborn mark on a dark background with a

slowly breathing gold rule, no console text, no white frame, then a short dissolve into Home.
  - The wheel: one detent moves exactly one row in Settings and short lists;

only a sustained spin in a long library list moves faster.
  - Hold Power → Quick Settings → Power Off → Power Off: UI fades, the mark

shows, the screen goes black and dark, then the device turns off with no white or console frame.
  - Settings → System → Diagnostics holds every technical detail previously

on normal screens.

The Fix03 CPU qualification plan (`qualify-cpu-fix03.py`) is unaffected and can run on this candidate. A first boot of the new splash after flashing is the only way to measure splash-visible, Reborn first-frame and ready times.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
