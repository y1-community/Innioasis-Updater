---
title: "Y2Linux 1.0 Beta 8.29 (Baseline 128) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.29 Baseline 128 Status: PUBLISHED as GitHub release baseline-128 2026-10-24, not installed on a player before publishing owner's decision; see Device r"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.29.html"
---

# Y2Linux 1.0 Beta 8.29 (Baseline 128) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.29 (Baseline 128)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.29 (Baseline 128)

Status: PUBLISHED as GitHub release `baseline-128` (2026-10-24), not installed on a player before publishing (owner's decision; see Device results). Release `1.0.0-beta.8.29`, Reborn `1.0.0-beta.8.29`, kernel `6.18.56-y2linux-1.0.0-beta.8.29`, update sequence 9300, root `2026.08-platform-v1.169`, Linux `4d97301`, Reborn `e58980c`. Built with `tools/production/release.py` (139 s, resumed workspace, update based on `baseline-127`): container suite 879 OK; host power/charger modules (`test_power`, `test_charger`, `test_charge_limits`, `test_power_policy`) 27 OK; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.29 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | a95c3528fa072fc6870ab3c4053a8bbe92073abee3d09b87961061371ce37094 |
| Y2ROOT | b485165600e9afd82c37d0f6bcb2215f3c8bb5debf3bcdc4e776cbef67c0d452 |
| RECOVERY | f88ffa48eda1d84f7694331e78f319a53eedf755c5fa1dcc8eebd2f379d69dcb |
| Y2DATA (no SSH key) | 0d6223ef27dea7180b87382aed7a407fef131170be1f831b7e1177a3a0df3d15 |

## Why

A user on Beta 8.28 could not charge at all (reports 09888d70, 8fc8eea6 and ba0bb428, install 047f2c1a, three boots on 2026-10-23). From 0.3 s after every boot the charger driver logged `first fault=0x3 sample_error=-61 chr=0x1`: the cable was detected, but BAT0 read health "Unspecified failure", status Unknown, 70 mA programmed, and the battery fell 3.70 → 3.64 → 3.61 V over the day.

Cause: the boot log also said `mt6323-auxadc: no valid die calibration; temperature unavailable`. This player's MT6323 (CID `0x2023`, a known revision) does not have its die-temperature calibration-enable fuse set (efuse `0x63a` bit 1). `y2_pmic_calibrate` refused that, so the PMIC die temperature channel returned `-ENODATA`; the charger reads it in every sample, counted the failure as an ADC/IO fault and inhibited charging before it ever looked at the cable, so the fault never cleared. It is the only one of about 45 installs in the stored reports with `die calibration=0`.

The stock kernel (`mtk_ts_pmic.c`, `pmic_cali_prepare()`) reads the same fuses and, when the bit is clear, uses nominal values: VTS 3698 at 25 °C, slope 0. Setting the fuse is not possible (one-time programmable; the register is a copy reloaded at power-on) and would not help: a clear bit means the calibration words were never written.

## What changed since Beta 8.28``````````

| Change | Detail | Evidence |
| --- | --- | --- |
| A PMIC without its die calibration fuse charges again | With a known CID and the calibration fuse clear, the die sensor uses the stock nominal (VTS 3698, 25 °C, slope 0) instead of returning no data, and reads 10 °C high (owner's choice): nominal reads about 8 °C low through our own player's fuses, so the margin makes the derating steps (60/70/80/90 °C) and both 150 °C stops act early, never late. The PMIC thermal zone is registered in that case too | Linux 1a51503; tests/test_power.py |
| Calibrated players unchanged | The fused path computes exactly what it did; an unknown CID still returns no data | test_conversion_units_calibration_and_protection (27 °C at the own fuses' reference point, nominal never below own) |
| Boot log | die calibration=2 for the nominal case and a warning with the CID and both efuse words, so the next report shows the fuse contents | Linux 1a51503 |

## Device results``````

| Check | Result |
| --- | --- |
| Owner's player | not installed before publishing: SSH to the player was not available in this session. It has its own calibration fuses, so it would only exercise the unchanged path |
| Affected player | owed: the reporter (install 047f2c1a) updates by OTA; expected boot lines die calibration=2 and no first fault, BAT0 Charging on a cable |

## Open
  - The nominal path has not run on a player yet; confirmation from the reporter is owed.
  - A persistent charger fault is still not shown in Reborn (the user only sees no charging).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
