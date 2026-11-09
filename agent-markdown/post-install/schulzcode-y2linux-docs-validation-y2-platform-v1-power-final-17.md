---
title: "POWER-FINAL-17 — modem request gate and screen-first wake - Innioasis Updater"
description: "POWER-FINAL-17 — modem request gate and screen-first wake Status: INSTALLED, FIRST BOOT AND FIRST SLEEP CLEAN; tagged baseline-17 2026-10-13. Package out/y2linux-platform"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-17.html"
---

# POWER-FINAL-17 — modem request gate and screen-first wake - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-17 — modem request gate and screen-first wake

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-17 — modem request gate and screen-first wake

Status: INSTALLED, FIRST BOOT AND FIRST SLEEP CLEAN; tagged `baseline-17` (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-17/` (fallback = 16), receipts `out/deep-sleep-final/build17-receipts/`. BOOTIMG `2ddd8d384cf6d9336d1a3505944f6a787764e982f7327400b5e886a41ea52d9a`, Y2ROOT `dc1f057a6c1d5768cbe3822893b5f71d3c3615bfbb3848e78491d9f0882a3e76`. Flash BOOTIMG + ANDROID only with `MT6582_preserve_data_scatter.txt`, Download Only. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-17`, kernel `6.18.56-y2linux-platform-v1-power-final-17`, root `2026.08-platform-v1.47`, release `1.0.0-platform-v1-power-final-candidate.17`; Linux `0459116` on `main` (later: a test-only commit), Reborn unchanged (`217e28d`). Base: Baseline 16 ([16 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-16.md)). Scope audit: "POWER-FINAL-17 sleep-floor and wake-latency scope audit" in the [roadmap gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

Goal set by the owner: stock sleep parity, ≈0.1 points/h (≈1.3 mA), with deep suspend and resume working every time, and a faster wake (screen first, radios afterwards). 16's first night drew ≈8.6 mA.

## What 17 changes[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstock-suspend-re-ledger.md)``````

| Area | Change | Switch |
| --- | --- | --- |
| Modem (MD1) clock requests | The never-used modem's 26 peripheral clock requests are gated (PERICFG MD1_SET 0x20, readback MD1_STA 0x30) once the UI is up, and re-checked at every sleep entry. Stock golden has them all gated; 16 read 0 at all 33 sleep entries. Proven AP-writable and harmless by the live test on 16 (ledger F11). Main suspect for INFRA never powering down. | md1_gate |
| Wake order | After a wake by the owner, the sleep helper asks Reborn to light the screen first and restores Wi-Fi and Bluetooth afterwards. On 16 the screen waited ≈1.9 s for the radios' firmware and calibration (archive 110: SPM return 217.92 s, screen ≈220.45 s). Expected: screen ≈1 s after Power. | — (a failed early restore is retried at completion, as before) |
| From 16's follow-ups (d1953fa) | The MMSYS part of the stock DCM now reaches the image; the USB DMA-unmask readback uses bits 15..8 (no more false dma_unmask_lost). | — |

`md1_gate` lives in `/data/system/platform/power-features.json` with the 16 switches, e.g. `{"md1_gate": false}`; the SPM `state` shows `md1_gate=1 md1_result=0 md1_sta=0x3ffffff md1_regates=N`.

## Tests

Locked-container production suite: 682 cases, exit 0 (16: 676; new: MD1 gate policy/wiring/switch, wake order, early restore reuse). The overlay-hash test added after 16 failed on its first container run because the container's `/src` already carries the overlays (the kernel was fine: it contains the 0011 MMSYS DCM hook); the test now reverses each patch first (`ebdfcf8`). Package validation, ELF closure (354 files), installed ARM (40 modules), privacy and inventory PASS.

## Hardware results

First boot (2026-10-13, boot `de37f6bc`, archive `out/deep-sleep-final/evidence/20261013/111-power17-first-check/`): kernel `-power-final-17`, build `0459116`, taint 0. First frame at 24 s, `application_ready` at 44.7 s (16: 40.9 s). `md1_gate=1 md1_result=0 md1_sta=0x3ffffff` (dmesg `Y2SPM: MD1 requests gated result=0`), `dcm_result=0`, `golden_apply=0xf`, `dis_pdn=1`. Wi-Fi (`wlan0`) and Bluetooth (`hci0`) up, USB gadget configured (stage 6) and SSH working, charging from a PC port. Known and unchanged from 16: reborn-splash `/dev/kmsg` EINVAL at 25 s, `mmc_erase` group start error, `thermal_zone1` -61. Not yet seen: a sleep, the wake time, audio.

First sleep (2026-10-13, archive `out/deep-sleep-final/evidence/20261013/112-power17-short-sleep/`): owner reports audio works and the wake feels faster. Unplugged sleep 11:08:39 → Power 11:26:32 (18 min), 1 entry / 1 resume / 0 aborts, wake `0x20`; USB worked after the replug.
  - Wake: screen ≈0.5 s after the SPM return (SPM 373.19 s → DSI modeset 373.70–373.72 s; radios after it, WMT

374.06–375.40 s, `wlan0` 376.41 s). 16: ≈2.5 s (archive 110).
  - MD1 gated at entry: golden `PERI_PDN0_MD1_STA e=3ffffff 1`, `md1_regates=0`; SoC golden differences 11 → 10,

PMIC 15/44 unchanged.
  - INFRA still never powers down:`last_lost=0x0`, `pdn0 0x2fcffff` unchanged. The modem requests were not the (only)

blocker; next: SRCLKENA, PCM R13 `0xe8060000` bits, MD_MASK 0x38 = 3.
  - USB unmask really lost once: with the readback fixed, `dma_unmask_rearms` 1 → 4 and `dma_unmask_lost` 0 → 1

across the unplug/sleep/restore (journal 11:03 vs 11:26). The re-arm restored it and USB worked: first direct support for the Defect B theory (which of the three re-arms found it lost is not recorded).
  - Two automatic sleep requests right after the unplug (11:08:12, 11:08:20) were refused after the radio quiesce

(`complete_result_2`); the third (11:08:36) entered. The refusal reason is not persisted (journal rows have no reason field and `suspend-last.json` is overwritten): diagnostics gap for 18.
  - 18 min is too short for a drain figure.

## What to check after the flash
  - `cat /sys/devices/platform/10006000.power-controller/state`: `md1_gate=1 md1_result=0 md1_sta=0x3ffffff`; USB,

Wi-Fi, Bluetooth, charger and audio as on 16.
  - Wake: press Power after a sleep and judge the time to the screen; read `restoring_radios` vs the DSI modeset in

`dmesg` (screen now before the radios).
  - After one sleep: `golden` row `PERI_PDN0_MD1_STA` now matches (`e=3ffffff 1`), and `y2_infra/state``last_lost`

(non-zero = INFRA finally powers down).
  - Overnight drain against 16's ≈8.6 mA.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
