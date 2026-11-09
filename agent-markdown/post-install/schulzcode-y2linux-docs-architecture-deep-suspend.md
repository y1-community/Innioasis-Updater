---
title: "Deep suspend (full system sleep) — developer architecture - Innioasis Updater"
description: "Deep suspend full system sleep — developer architecture Status: bring-up document for POWER-FINAL-06. It describes the code as it is in the bring-up candidate and names w"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-deep-suspend.html"
---

# Deep suspend (full system sleep) — developer architecture - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Deep suspend (full system sleep) — developer architecture

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Deep suspend (full system sleep) — developer architecture

Status: bring-up document for POWER-FINAL-06. It describes the code as it is in the bring-up candidate and names what is still unproven. Experiment history lives in `docs/validation/Y2-PLATFORM-V1-SUSPEND-POWER-OPTIMIZATION.md` and `docs/validation/Y2-PLATFORM-V1-DEEP-SLEEP-FINAL.md`; this file is meant to be read first.

## What "deep suspend" is on the Y2

MT6582 (4× Cortex-A7), MT6323 PMIC over PWRAP, 512 MB LPDDR, eMMC + SD. Full suspend is `echo mem > /sys/power/state` issued by the product sleep helper (`tools/platform/y2_platform/product_sleep.py`) after the screen is dark, playback is paused and the radios are off. The SoC power controller SPM runs a small microcode program (PCM) that removes CPU power, puts DRAM into self-refresh, switches clocks off and waits for a wake source. The 32 kHz domain, the SPM, PWRAP, GPIO/EINT, the RGU watchdog and the GPT timers stay powered.

This is separate from runtime idle (C1/C2/C3 `cpuidle`, the 480-word `pcm_dpidle` program): C3 keeps INFRA/DDRPHY powered and is not touched by anything here.

## The one authoritative implementation``````````````````````````````````

| Piece | File |
| --- | --- |
| PCM words (vendor pcm_suspend, 597 words, v34rc10, non-MT6333) | kernel/platform/spm-pcm.h (SHA-256 0ee71194…6ab94, identical to BSP d53dd75c and the stock firmware) |
| Arming sequence (wake mask, timer, PCM watchdog, infra_pdn) | kernel/platform/spm-suspend-policy.h |
| Platform entry/exit, CPU context, CIRQ replay | kernel/platform/spm.c (y2_spm_enter, y2_spm_finish, y2_spm_resume_syscore) |
| INFRASYS power-down state (PERICFG save/restore) | kernel/platform/infra-pdn-policy.h, infra-pdn.c |
| Retained black box + bounded RGU backstop | kernel/platform/pm-journal.c, pm-journal-policy.h |
| Resume entry (boot ROM → Linux) | kernel/platform/resume-vector.S |
| Product policy and receipts | tools/platform/y2_platform/product_sleep.py, suspend_record.py |

## Sequence
  - Preparation (userspace): admission checks (battery not charging, kernel not tainted/broken, backstop provider

present), Reborn quiescence, radios off, product guard written (`pending:true`).
  - Device suspension (kernel PM core): tasks frozen, filesystems synced, `dpm_suspend` (codec, MMC, I2C, USB

controller quiesced and detached, PERICFG clock gates set by each driver), secondary CPUs offlined.
  - PMIC/clock preparation:`y2_pmic_spm_prepare()`; CIRQ clones the GIC enables; SPM wake mask and the 600 s timer

are programmed; UART clock-off is requested and acknowledged (`spm-uart-policy.h`).
  - Infra decision (`y2_infra_pdn_save`): if INFRA power-down is wanted, PERICFG is snapshotted and the arm is told

`infra_pdn=1` (clears `CC_DISABLE_INFRA_PWR`, exactly the vendor `spm_kick_pcm_to_run`).
  - SPM entry:`cpu_suspend()` saves the CPU context, `y2_spm_finish()` verifies the boot vector, writes the last

retained mark (`INFRA_PDN_ENTRY` when applicable), pauses the RGU backstop, flushes caches and executes `WFI`. The PCM now powers the CPU (and, with `infra_pdn=1`, INFRASYS/DDRPHY) down.
  - Wake: SPM timer (600 s maintenance), USB cable (CHRDET), Power key (KP/PMIC), EINT, thermal.

The boot ROM jumps to `y2_cpu_resume` (DRAM, MMU off) → `cpu_resume`.
  - Hardware restoration:`y2_infra_pdn_restore()` rewrites what INFRASYS power-down reset (PERICFG gates,

resets, DCM, limiters, USB wake, UART clock source) and verifies it; the normal 28-word PCM is reinstalled and read back; GIC/timer/CIRQ are restored in `syscore_resume`.
  - Device resume (kernel PM core): drivers re-initialise from their resume callbacks (UART re-arms

`UART_SLEEP_EN`, USB detaches/reconnects with its own session logic, MSDC restores its saved registers).
  - Userspace: radios restored, Reborn resumed, receipt written, product guard cleared.

## What `infra_pdn=1` changes (the vendor default)

The stock kernel's `slp_infra_pdn` defaults to 1 (`0xc09b1084`: `01 01 01 00`, read from the retained FM kernel). `spm_go_to_sleep(cpu_pdn=1, infra_pdn=1)` differs from our previous `infra_pdn=0` in exactly two places: `CC_DISABLE_INFRA_PWR` is cleared before the PCM is kicked, and `mtk_uart_restore()` runs after `WFI`. The PCM itself handles DRAM self-refresh and DDRPHY. Per the MT6582 manual (2.3.2) INFRACFG and PERICFG live in the powered-down domain; PERICFG `PDN0` resets to 0 (all peripheral clocks ungated). Linux therefore restores PERICFG immediately after the CPU returns. Peripheral register windows are not read or restored by the platform (their drivers have suspended them and re-initialise), matching the vendor, which restores only the console UART.

## Failure handling
  - Every wait is bounded; the PCM has its own watchdog wake (timer + 30 s).
  - RGU backstop (`/sys/firmware/y2_pm/backstop_s`, ≤ 30 s) covers the pre-SPM and post-wake phases; it is paused

during SPM sleep by design (it must not count sleep time).
  - Retained journal (SRAM 0x0010dc00): stage record + 24-entry device-callback ring + notes. After a hard

reset the previous boot's last stage identifies where it stopped.
  - Never repeat a failed power-down by itself:`y2_infra_pdn_restore()` verifies every restored register; failure

sets `fallback` (retained mode for the rest of the boot) and returns `-EIO` (SPM marked broken, product guard quarantines). A boot whose predecessor ended on `Y2_PM_INFRA_PDN_ENTRY` starts in retained mode.
  - `/sys/firmware/y2_infra/mode` = `powerdown|retained` (root); writing `powerdown` is the only way to clear a fallback.

`state` and `diff` show the last restore; none of this is required for normal operation.
  - Product guard (`/data/system/platform/product-sleep-guard.json`) refuses automatic sleep after an unresolved

failure of the same image identity.

## USB, Wi-Fi and the parent-device lifetime rule
  - MUSB L1INTM keeps only the bits Y2 services (`kernel/usb/l1.h`); unowned PHY level conditions are masked at their

source, never counted toward the terminal storm guard.
  - A terminal USB stop parks the controller (detached, IRQs masked, bus clock gated); it never unregisters

`musb-hdrc`. The ECM netdev `usb0` holds the gadget device as `dev.parent` without a reference, so freeing it makes the next netlink query crash. Do not reintroduce `platform_device_unregister(y2_usb_child)`.

## Wake sources

Entry wake mask `~(KP | EINT | USB_CD | THERM | SYSPWREQ)` (0xfedfbfdb) plus the 600 s PCM timer. Physical wakes: USB cable, Power key, RTC alarm (via PMIC EINT), battery events. The software USB-budget power supply has no wakeup source (`no_wakeup_source`). The vendor mask additionally includes `CONN_WDT`, `CCIF_MD` and `CONN`; the modem and connectivity cores are off in this product.

## Production diagnostics (keep) and development-only (remove at production)

Keep: retained stage/ring, last wake reason (`/sys/firmware/y2_pm/state`), suspend/resume/abort counters (`/sys/firmware/y2_spm`), the RGU backstop, product receipts. Development-only and slated for removal in the production pass: the `WAIT`/`LOCK` ring phases and `dpm_stall` sampler (04), `/sys/firmware/y2_infra/diff` register dump, the suspend probe tools, external observer modules. See the POWER-FINAL-06 acceptance list.

## Remaining hardware limits
  - No on-device current sensor; SOC is voltage-derived. The only absolute drain figures need external measurement

(a USB meter gives a top-up integral, not suspend current).
  - Whether the 26 MHz oscillator really stops, and the true INFRASYS/DDRPHY power state, are unobservable during sleep.
  - PMIC sleep configuration (LP_SEL beyond the five always-on LDOs, VPROC/VSYS sleep voltage, eMMC supply, VGP2) is not

vendor-equivalent yet; each item needs its own design and approval.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
