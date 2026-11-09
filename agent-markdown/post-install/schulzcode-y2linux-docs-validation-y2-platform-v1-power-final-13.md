---
title: "POWER-FINAL-13 — stock suspend power parity (golden master from the Y2's own firmware) - Innioasis Updater"
description: "POWER-FINAL-13 — stock suspend power parity golden master from the Y2's own firmware Status: FLASHED, FIRST SLEEP PASSED, USB-AFTER-WAKE DEFECT OPEN published as Baseline"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-13.html"
---

# POWER-FINAL-13 — stock suspend power parity (golden master from the Y2's own firmware) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-13 — stock suspend power parity (golden master from the Y2's own firmware)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-13 — stock suspend power parity (golden master from the Y2's own firmware)

Status: FLASHED, FIRST SLEEP PASSED, USB-AFTER-WAKE DEFECT OPEN (published as Baseline 13, tag `baseline-13`; see [physical result](#physical-result-2026-10-11)). Sealed as IMPLEMENTATION_READY_PHYSICAL_NOT_RUN. Branch `codex/platform-v1-power-final-13` (worktrees `~/Dokumente/Code/worktrees/platform-v1-power-final-13/{Y2Linux,Y2Reborn}`), Linux build commit `47c1cf225dc140d151366f9e6309a3a07556fa67` (later test-only `tests:` commit), Reborn unchanged (`71ddb0d`). Package `out/y2linux-platform-v1-power-final-candidate-13/` (fallback = sealed 12), symbols `…-13-symbols/`, receipts `out/deep-sleep-final/build13-receipts/`. BOOTIMG `f73c24da3abe5978f2c234bd9501a929415fc156fc5ab79ebc7755390dddc178`, Y2ROOT `e62cb6c7bab621e6f791359e5b56bba3a21f065d2ba864f4917b3ae808c01915`; kernel `-power-final-13`, root v1.43. Offline: container suite 651 cases PASS (10 host-dependency skips), 32 packaging-host + 27 splash PASS, package/ELF 385/1416/installed-ARM/inventory/privacy PASS. Scope audit: POWER-FINAL-13 entry in `docs/planning/roadmap-gap-audit.md` (13 branch). Data: `docs/validation/data/y2-stock-suspend-golden-20261011.json` (13 branch).

## Why 13
  - Defect A on 12 (owner's second sleep 9 s after a Power wake failed in the radio quiesce) left the product

guard pending. Admission matched the guard by build identity only, so every sleep was refused across reboots: archive 98 shows boot `09ce553a` awake with the screen dark for 4.2 h, 301 refusals, 78% to 56% (≈4.9 points/h, voltage-derived). The failing command was `bluetooth-power off`: the reconnect daemon (`tools/connectivity/reconnect.c`) holds `/run/y2/bt-operation.lock` while it reconnects after a wake, and `bt_control.power()` refuses at once.
  - Drain: 12's first good night was ≈2.2 points/h asleep, against ≈4.9 points/h awake-dark: sleep only halves

the drain. The owner's target is stock parity (≈1% per night, ≈0.1 points/h). No current sensor exists; every number here is voltage-derived and indicative only.

## Golden master: the stock FM kernel

Source: `evidence-private/20260908-ram-map/fm-decompressed.bin` (the Y2's stock kernel, base 0xc0008000) with `fm-symbols.json`, disassembled with llvm-objdump (armv7). Decoded:````````````````````````

| Stock object | Address | Finding |
| --- | --- | --- |
| PMIC_INIT_SETTING_V1 (E2) | 0xc04b81f8 | 80 field writes; 55 differ from the live 12 PMIC (archive 99, read-only debugfs dump). Power-relevant: VPROC sleep voltage set (8 fields), LP_SEL on VMC/VMCH/VEMC3V3, BAT_L/thermal interrupt enables, EFUSE/AUXADC clock PDN. Not power: ADC trim selects (would shift Y2's battery calibration), charger/speaker/start-up fields. |
| mt6323_power_gs_suspend_data | 0xc0757cd0 | 44 PMIC rows; identical to the vendor table the 05 report used. |
| mt6582_power_gs_suspend_data | 0xc0759c98 | 57 SoC rows: clock muxes powered down, INFRA/PERI clock gates, DCM, MAIN/UNIV/MM/MSDC PLL software-enable 0 and AP_PLL_CON3 hardware control, CLK_SCP_CFG 0x3ff/0x11. Never read on Y2 before 13. |
| tpd_suspend / tpd_resume | 0xc04a41c0 / 0xc04a3088 | APT32F wheel: reg6 firmware; 1..19 gets the sleep command reg5=1, else GPIO56 (reset) held low; resume pulses GPIO56 and writes reg5=0. This unit reads reg6 = 0x01. Y2 never slept the controller. |
| usb_phy_savecurrent_internal | 0xc04d98f0 | Full PHY power-down whenever no cable is present. Y2 only ran the recover half at boot. |
| pmic_mt6323_suspend | 0xc04b3dd4 | AUXADC hardware mode and VREF18 off in suspend (not adopted: would change Y2's ADC). |
| cs43131_early_suspend | 0xc054bed0 | DAC GPIOs low and hwPowerDown of VGP2 (refcounted). Y2 already keeps the GPIOs low; VGP2 stays on (not adopted). |
| GC9503 lcm_suspend | 0xc04a24f4 | Display off, sleep in, power-register tail and AF=02, reset left high (Y2: off, sleep in, reset held). Not adopted. |
| slp_suspend_ops_enter | 0xc0035bd4 | Only spm_go_to_sleep; the PLL/clock state comes from the static configuration above. |

## Changes in 13 (each switchable at run time)``````````````````````

| Change | Switch | Restored / non-fatal |
| --- | --- | --- |
| Radio quiesce waits up to 25 s for the Bluetooth operation lock; the failure reason names the radio. The guard is cleared whenever the kernel was not entered; only a kernel_entry record quarantines. | — | host-tested (test_product_auto_sleep, 3 new cases) |
| Stock VPROC sleep voltage 0.85 V: 8 stock fields applied only inside y2_spm_enter (one CPU, IRQs off) around the PCM sleep, VOSEL_ON preset to the live selector, live voltage re-verified, every word restored mode-bit first before the normal PCM. | /sys/module/pwrap/parameters/vproc_sleep, state in vproc_sleep_state | refusal or failure keeps 1.15 V and sleeps anyway |
| LP_SEL on VMC, VMCH, VEMC3V3 (stock init). Enables stay unwritable. | /sys/firmware/y2_pmic/lp_sel | readback-verified |
| Stock USB PHY save-current in the y2-usb suspend_noirq (no cable, no session); byte-exact restore in recover order in resume_noirq. | .../y2-usb/phy_savecurrent (counters) | mismatches counted and logged |
| APT32F sleep command / reset pulse on wake (stock sequence); GPIO56 admitted with the latch preset high. | /sys/bus/i2c/devices/0-0051/sleep (bus number can swap) | failed sleep never blocks suspend; wake retries 5× |
| Maintenance wake 600 s to 1800 s (stock uses a dynamic period). | — | PCM watchdog timer + 30 s |
| Read-only stock golden capture at every suspend entry. | cat /sys/devices/platform/10006000.power-controller/golden (root) | reads only always-on/INFRA blocks |

## Owner test after flashing
  - Plugged in: `cat` the four switches above; `golden` shows `captures=0` and the awake `now` values.
  - Unplug, screen times out, leave ≥ 35 min (one 30-min maintenance wake), press Power once. Then read

`vproc_sleep_state` (entries = restores, failures 0), `phy_savecurrent` (saves = restores, mismatches 0), wheel `sleep` (sleeps = wakes, failures 0) and that the wheel scrolls, USB reconnect works, `y2_infra/state` (`restores>0` means INFRA really powers down), `golden` (entry rows that still differ from stock).
  - Overnight drain against 12's ≈2.2 points/h. If anything misbehaves, switch the suspect item off at run time

(`echo 0 > …`) and compare the next night.

## Not done (next steps decided by the `golden` capture)

PLL hardware control (AP_PLL_CON3 / CLK_SCP_CFG) and the DIS/MMSYS power domain, eMMC supply removal in suspend, VGP2/DAC rail, panel deep-standby table, PMIC low-battery interrupt instead of timer wakes, AUXADC clocking, and the awake-dark drain (Reborn blanks only the backlight; the display pipeline keeps scanning out).

## Physical result (2026-10-11)
  - First check (archive `100-power13-first-check`, read-only): boot `604bc0e6`, taint 0, `pm_async` 0;

`vproc_sleep` = Y, `lp_sel` applied on all eight rails, `phy_savecurrent` enabled, wheel `sleep` enabled (firmware 1, sleep command), SPM `SPM_CPU_SHUTDOWN_INFRA_PDN` with 1800 s maintenance. Awake `golden`: PLL hardware-control bits (APMIXED+0x00c = 0x780000) and CLK_SCP_CFG already match stock. MAIN/UNIV/MM/MSDC PLL are software-enabled, VENCPLL is on, and AP_PLL_CON1 and the INFRA/PERI DCM differ (all candidates for 14).
  - First unplugged sleep (archive `104-power13-first-sleep-coldstart-archive`; device clock = host minus 37.9 min):

host 15:17:30 to 18:39:33, 12,104 s suspended, 7 kernel suspends, 6 clean 1800 s maintenance wakes, Power wake, `complete_result_0`. 76% to 76% (4.036 V to about 4.007 V at the maintenance wakes) in 3.4 h: indicative only, from voltage.
  - Defect B reproduced on a clean wake: the gadget enumerated 5 s after the wake (`udc configured`,

`detached=0`), but the host received 0 bytes for 3 min. Owner power-off (`shutdown_execute`), offline charging, power-on (boot `8cdde856`, taint 0) recovered it. That lost the in-memory counters (`vproc_sleep_state`, `phy_savecurrent`, wheel `sleep`, `y2_infra/state`, the `golden` capture at sleep entry), and the boot's syslog was not persisted past start-up. Next: repeat the sleep, and if USB is dead, read the counters another way before any restart.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
