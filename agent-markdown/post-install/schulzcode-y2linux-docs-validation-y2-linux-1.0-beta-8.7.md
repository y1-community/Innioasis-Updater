---
title: "Y2Linux 1.0 Beta 8.7 (Baseline 95) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.7 Baseline 95 Status: PUBLISHED as GitHub release baseline-95 2026-10-18. Release 1.0.0-beta.8.7 , Reborn 1.0.0-beta.8.7 identity only, kernel 6.18.56-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.7.html"
---

# Y2Linux 1.0 Beta 8.7 (Baseline 95) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.7 (Baseline 95)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.7 (Baseline 95)

Status: PUBLISHED as GitHub release `baseline-95` (2026-10-18). Release `1.0.0-beta.8.7`, Reborn `1.0.0-beta.8.7` (identity only), kernel `6.18.56-y2linux-1.0.0-beta.8.7`, update sequence 6900, Linux `f7b4fb5`, Reborn `82fe089`. Built with `tools/production/release.py` (151 s): container suite 778 OK, host suite 805 OK; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.7 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 81130491bf75928c06579e6820da1dd9b0298f83b09a858af601bacb9f787ce6 |
| Y2ROOT | 1543fbcfbfcbe8f228c0c330d75688af1c0c4ce8ed54ae6ec644f5a44ab6402d |
| RECOVERY | 6a646b689d1d643c67e71fb8558d363c7124cbbed4a883e7f2c16478f71fa874 |
| Y2DATA (no SSH key) | 7b9c5c7b907142726468c5fb5f50ee9a8c67a18ffb828cb180ac641c0a12eb93 |

## What changed``````````````````````````````````

| Part | Change |
| --- | --- |
| Panel identification (#45, #46) | REA of the stock LK (v3.2.0 lk.bin, bb1a93b4…): auto-detect 0x81e0af60 walks [gc9503v, st7701] (0x81e3821c) and names the first driver whose lcm_compare_id matched, else the last one (st7701); the lcm= digit is a separate DCS 0x0A read. The GC9503V compare (0x81e1eb60) only matches DCS 0x04 = xx 95 03/04, so lcm=0-gc9503v… is a positive identification. kernel/platform/boot-policy.h trusted only lcm=1-, so the #45 reporter's GC9503V (lcm=0- on a cold boot, DSI read lag at the ID read) was never identified. Now a gc9503v name counts with either digit; st7701 still needs lcm=1-. Linux 7046833, tests test_power_policy (mutation caught) and test_power_final_27. |
| Behaviour | ST7701S players: unchanged. GC9503V players: identified and recorded; the power-down stays opt-in (CONFIRMED_PANELS) until a GC9503V owner confirms it. |

## Device results

None on a GC9503V yet (the reporter's test is requested on #45). The owner's ST7701S player installs it by OTA; its panel path does not change.

## Known gaps
  - The reporter's LK comes from the 3.2.1 updater; its hash is requested on #45/#46 to confirm the same driver order.
  - Not done on purpose: skipping the power-down on boots with DSI register-read lag (the reporter's 7.10 run showed the

lag clears after the first screen-off).
  - Unchanged from 8.6: battery current with a profile, output measurements, sleep drain (#42).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
