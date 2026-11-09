---
title: "POWER-FINAL-19 — PMICWRAP clock gated for the PCM sleep - Innioasis Updater"
description: "POWER-FINAL-19 — PMIC WRAP clock gated for the PCM sleep Status: INSTALLED, FIRST BOOT AND A 47-MIN SLEEP CLEAN 2026-10-13. Package out/y2linux-platform-v1-power-final-ca"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-19.html"
---

# POWER-FINAL-19 — PMICWRAP clock gated for the PCM sleep - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-19 — PMICWRAP clock gated for the PCM sleep

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-19 — PMIC_WRAP clock gated for the PCM sleep

Status: INSTALLED, FIRST BOOT AND A 47-MIN SLEEP CLEAN (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-19/` (fallback = 18 = `baseline-18`), receipts `out/deep-sleep-final/build19-receipts/`. BOOTIMG `494948998c45326501945b7ff00f782f1ff3c7264a4bdea70ef938e111ef44ed`, Y2ROOT `1e6a61fcc1f61345a1e5f79ae40540e3566bba060a13594c3732272d31c2f4d5`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-19`, kernel `6.18.56-y2linux-platform-v1-power-final-19`, root `2026.08-platform-v1.49`, release `1.0.0-platform-v1-power-final-candidate.19`; Linux `0fa5135` on `main`, Reborn unchanged (`217e28d`). Flash BOOTIMG + ANDROID only with `MT6582_preserve_data_scatter.txt`, Download Only. Scope audit: "POWER-FINAL-19 PMIC_WRAP clock gate scope audit" in the [roadmap gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## Why

After 18 the only INFRA clock gate that still differs from stock at sleep entry is INFRA_PDN bit 23, the AP's PMIC_WRAP clock ([ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstock-suspend-re-ledger.md) F17). Stock's suspend checklist has it gated (and even awake video playback does). Y2 had kept it on, assuming the sleep firmware needs it; stock does not support that. The owner-authorised live test on 18 showed that gating it makes the AP-side wrapper read as 0 (every PMIC transfer fails, no bus hang) and that ungating restores it at once. INFRA has never powered down on any candidate (`last_lost=0x0`), and one INFRA clock left running is a plausible reason.

## What 19 changes
  - Inside `y2_spm_enter`, after the VPROC and PMIC sleep steps and the PMIC golden capture (the last AP PMIC access),

INFRA_PDN_SET bit 23 is written right before the PCM is armed. It is cleared (verified, up to 3 tries) right after `cpu_suspend` returns (after the backstop re-arm, before the INFRA restore and every PMIC/VPROC restore), and again on the arm-failure path. It never takes over a gate it did not set.
  - Switch `spm.pwrap_gate` (kernel default off), armed by userspace with the other power features; owner switch

`{"pwrap_gate": false}` in `/data/system/platform/power-features.json`.
  - State line in `/sys/devices/platform/10006000.power-controller/state`: `pwrap_gate pwrap_gates pwrap_ungates

pwrap_gate_failures pwrap_gate_sta pwrap_gated` (also in every sleep-diagnostics row).

## Tests

Locked-container production suite: 689 cases, exit 0 (18: 685). The two suspend harnesses that compile the real `y2_spm_enter()` now model the gated wrapper and assert that no PMIC step runs while it is gated and that it is never left gated on any abort path; `test_pwrap_gate` pins the order. Package validation, ELF, installed ARM, privacy and inventory PASS. (The first 19 build `2b38a28` ungated before the backstop re-arm, which an existing test pins first; fixed in `0fa5135` and rebuilt.)

## Risk

If the PCM itself needed the AP-gated wrapper during sleep, a sleep could stall: the 30-s RGU backstop resets the device and the persistent rows record it. Recovery: `{"pwrap_gate": false}` after a hold-Power restart, or flash `fallback/` (18). Stock sleeps with the same PCM and this clock gated.

## Hardware results

First boot (boot `d4f9a0f1`, archive 115): kernel `-power-final-19`, taint 0, `application_ready` 44.3 s, `pwrap_gate=1`, all 16–18 features armed, Wi-Fi/Bluetooth/USB/SSH up, charging; known log lines only.

47-min sleep (archive `out/deep-sleep-final/evidence/20261013/116-power19-short-sleep/`): 14:05:04 → Power 14:52:26, 2 entries / 2 resumes / 0 aborts (one maintenance wake), USB fine after the replug.
  - PMIC_WRAP gate works:`pwrap_gates=2 pwrap_ungates=2 pwrap_gate_failures=0`; `pwrap_gate_sta=0x80bfe6` —

INFRA_PDN_STA at the kick is now exactly the stock golden value. PMIC step 2/2 restored.
  - INFRA still retained:`last_lost=0x0`, PERICFG PDN0 `0x2fcffff` kept on both restores. So no INFRA clock gate

was the blocker.
  - Remaining PERI gate difference at entry: PDN0 `0x2fcffff` vs stock `0x2feffff` = bit 17, UART1. UART1 has no

Linux owner (LK leaves its clock on; the idle path only defers it); stock gates it in every scenario checklist (idle, deep idle and suspend). Next candidate.
  - Audio after the wake: no playback logged before the capture.

## What to check after the flash
  - Boot, display, audio, Wi-Fi, Bluetooth, USB as on 18; `state` shows `pwrap_gate=1`.
  - A short sleep first (≈35 min, one maintenance wake): `pwrap_gates` = `pwrap_ungates` = sleep entries,

`pwrap_gate_failures=0`, `pwrap_gate_sta` has bit 23 (0x800000); wake and audio fine; `pmic_sleep_state` as on 18.
  - The key read: `y2_infra/state last_lost` — non-zero would mean INFRA finally powers down (then also check the

PERICFG restore counters and that USB, SD and audio survive).
  - Then the overnight drain against 16's ≈8.6 mA.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
