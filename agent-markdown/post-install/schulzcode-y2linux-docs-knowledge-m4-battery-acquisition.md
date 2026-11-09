---
title: "M4 charging prerequisite: this Y2's battery sensor - Innioasis Updater"
description: "M4 charging prerequisite: this Y2's battery sensor <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m4-battery-acquisition.html"
---

# M4 charging prerequisite: this Y2's battery sensor - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M4 charging prerequisite: this Y2's battery sensor

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M4 charging prerequisite: this Y2's battery sensor > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Historical checkpoint. The owner’s later charging authorization and the reconstructed stock protection architecture are recorded in [M4 charging](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-charging.md). The sensor results below remain valid; the former unconditional BATON gate is superseded.

2026-09-14. Charging completion is blocked before the first active charge. The first missing physical fact is whether this Y2's BATON input measures the pack temperature with the resistor network assumed by its stock firmware. The owner does not know the battery label or wire count; the device is at room temperature, without an independent numeric temperature reference.

The source audit and live M4-01 reads are retained under ignored `evidence-private/20260914-m4-battery/` with their SHA256 manifest. Entry source was `444e7eda99dc1f7d90d0d591ebda4f3219efe0c9`. Last read in this pass, at uptime 2074.16 s: BAT0 present, Not charging, 3544189 uV, USB online, configured 70000 uA / 4175000 uV. No new BATON/ISENSE acquisition or charging occurred. The configured current is not a measurement of current flowing into the pack.

## Owner-deployed ADC result — same day

The owner manually booted `6.18.0-y2linux-m4-adc-01`. SSH confirms the new channels, CPUs 0–3, 954044 KiB MemTotal, internal p5 root/p7 data and charging inhibited. The kernel release matches the built candidate; the flashed BOOTIMG was not read back byte for byte in this sensor test.

120 successful samples in four bounded sets, uptime 119.89–455.24 s:

| Measurement | Actual result | Interpretation |
| --- | --- | --- |
| BATON1 | Raw 10387–10388, nominal 570.575–570.630 mV | Not saturated; request/ready acquisition works. No resolved response to normal handling |
| ISENSE minus bracketing BATSNS | Mean -0.081 mV, standard deviation 1.638 mV; samples -2.747 to +2.966 mV | Both voltage paths respond; this is neither calibrated charging current nor net battery current |
| Battery voltage | Lowest sample 3472778 uV; final standard read 3475415 uV | Charging remained off throughout; configured limits stayed 70 mA / 4.175 V |

The owner confirms holding the closed player normally for about 60 seconds, then returning it to the surface. Exact handling timestamps and actual pack temperature were not independently measured. The BATON means before, during the response window and afterward differ by less than one ADC count. This is inconclusive for a thermistor, not proof of a two-wire battery or an absent sensor. A fixed detection resistor and an insulated NTC that did not measurably warm remain possible. Applying the stock resistor model would yield roughly 22.5 C, but that is a hypothesis and is not published as BAT0 temperature.

Read-only register confirmation: CHR_CON0=0x0063 (charge engines off), CHR_CON7=0x0005 (BATON/TDET enabled), CHR_CON16=0x0005 (external test-mux selectors clear), ADC request register=0x00e8 and BATON1 ready/result=0xa893. Inherited trim selector register 0x0756=0x0042 is unchanged. AUXADC_CON19 and ADC19 were both zero: the BSP's pending decimation-delay workaround was not active in that snapshot. One initially miscalculated debugfs line index read 0x079a instead of ADC19; it returned zero, was not interpreted, and was corrected with the documented 0x073a read. There were no direct PMIC writes.

The complete host capture and original stock extracts are retained under `evidence-private/20260914-m4-adc-physical/` with a SHA256 manifest. The public [result and samples](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-14-m4-adc/result.json) preserve the measured limits. The boot log retains the already tracked synthetic ext4 inode warnings during initramfs unmount, followed by clean journal recovery and normal p5/p7 mounts. This test does not qualify suspend, playback or storage stress and does not declare M4 complete.

Charging remains blocked at pack thermometry. The next useful evidence is BATON-to-pack sensor wiring/NTC identification, or a repeatable response after equilibration at two independently measured normal room temperatures. A brief closed-case handling test did not establish the actual pack temperature change. The existing ADC kernel can record the next response test without another diagnostic image. Do not keep sampling an uncharged battery indefinitely, change routing selectors by guesswork, or enable charging to warm the pack for a test.

## Why this needs an owner kernel deployment

The live M4-01 driver exposes only channels 3 and 7. Its built-in PWRAP write policy also restricts AUXADC request register 0x076e to mask 0x88. A new IIO consumer or module cannot request channels 5/6 through that transport: the request is rejected with EPERM. PWRAP suppresses unbind, regmap debugfs is read-only, and this kernel has no kexec/livepatch route. Rebinding the ADC child does not replace its parent's compiled guard. A competing raw WACS client or live kernel patch would defeat the intended ownership/protection.

Y2LINUX-M4-ADC-01 is the now owner-deployed production sensor extension, still inhibited. It changes the same ADC driver and admits only two additional request bits (mask 0xe8). Current, CV, charger enable, watchdog and protection permissions stay unchanged. No NTC constants are installed as board calibration. It is not a charging candidate and cannot replace Android for recharging yet. Storage06, existing root/data and all other M4 drivers are retained. No rootfs update is needed.

## What the new standard interface means

Discover `/sys/bus/iio/devices/iio:device*/name` equal to `mt6323-auxadc`.````````````

| Pin | Channel / result register | IIO attributes | Meaning |
| --- | --- | --- | --- |
| BATON1 | 5 / 0x071a | in_voltage5_raw, in_voltage5_scale | Nominal pin mV = raw × 1800 / 32768; not battery Celsius |
| ISENSE | 6 / 0x0716 | in_voltage6_raw, in_voltage6_scale | Nominal pin mV = raw × 7200 / 32768; not amperes |
| BATSNS | 7 / 0x0714 | Existing in_voltage7_raw, in_voltage7_scale | Nominal battery pin mV = raw × 7200 / 32768 |

Each raw read enables the ADC buffer, clears then sets its request bit, waits at least 1 ms, polls ready bit 15 for at most 20 ms, and restores the saved buffer state. Conversion and regmap errors propagate; not-ready data is never returned as a successful sample. The existing mutex serializes all four ADC channels, including the die sensor, through the one parent regmap. Existing hardware trim selection is preserved; absolute accuracy is not independently calibrated. The raw API deliberately allows endpoint readings for diagnosis.

BAT0 still reports voltage, presence, status, health and inherited configured limits. No `temp`, `current_now`, `capacity`, time estimate or FULL claim is added. No watchdog servicing or new charging/suspend/reboot policy is added.

## Evidence already reconciled

Retained stock Y2 kernel SHA256: `7287acf1b397d243c927dde5c6ef9d5d871c9c158207cdd98e0e820923f4c197`.
  - Stock `read_adc_v_bat_temp` at 0xc04cab08 requests channel 5. Its table at

0xc09d0b04 is a 10 kohm NTC table (10 kohm at 25 C). `BattVoltToTemp` at 0xc039b194 assumes a 16.9 kohm pull-up, 27 kohm pull-down and 1.8 V supply. The public stock temperature functions return a literal 25 C. The compiled raw path remains real, but these constants do not prove the board wiring.
  - BATON/TDET were enabled (0x000e = 0x0005); BATON hot detection was disabled.

BATON1 and ISENSE result registers both had ready=0 in two snapshots. That proves neither a missing NTC nor zero charging current.
  - Stock `battery_meter_get_charging_current` at 0xc039cb00 samples ISENSE and

BATSNS, trims outliers, and divides their voltage difference by an assumed 68 mohm resistor. Pin routing, resistor value and channel offset are not yet verified. It would at most establish charger-path current until topology proves that all battery current flows through the sense resistor.
  - This unit's own 0x063a/0x063c words (0x46da/0x800f) calibrate PMIC die

temperature only. Neither those nor the SoC fuses calibrate an unknown NTC network. No calibration/NVRAM was written or another device's fixture used.
  - No working hardware coulomb counter/SOC path was established. Stock FG

current/columb functions are stubs; displayed percentage uses a software battery model. SOC is a separate follow-up.

Primary source for channels, request/ready and scales: [pinned MediaTek MT6323 AUXADC implementation](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/power/mt6582/pmic_mt6323.c). Stock binary extracts and the fuller audit preserve the separate Y2-specific evidence. No other board's calibration is treated as this board's data.

## Smallest controlled experiment after manual deployment

The agent performs the commands over SSH after the owner reports the new kernel booted. The sampling script performs no sysfs writes, direct PMIC access, charging, RTC operations or persistent device writes. Standard IIO reads execute the bounded ADC requests in the kernel.
  - Confirm the kernel is `6.18.0-y2linux-m4-adc-01`, Storage06 root/data are

mounted, BAT0 is present/Not charging and current/CV remain 70 mA/4.175 V.
  - Capture 30 samples on a room-temperature surface using

`tools/development/sample-battery-adc.sh`. It records BATON and ISENSE, bracketing them with BATSNS samples to show sequential measurement drift. On ADC error, saturation, battery absence or voltage below the existing 3.4 V observation cutoff, stop. This cutoff is not a pack protection limit.
  - If the readings are usable, the owner holds the closed player normally for

about a minute; acquire another bounded set, then allow it to return to the surface. No heater, cold source, opening, pack manipulation or stress load.
  - Look for a repeatable response consistent with an NTC. Fixed/saturated

readings or no discernible response leave the path UNKNOWN; they do not automatically prove absence. A plausible room-temperature voltage alone cannot establish the NTC resistance curve or resistor values. A calibrated ambient/reference comparison or board evidence may still be necessary.
  - Assess paired ISENSE/BATSNS offset with charging disabled. This alone does

not calibrate a 68 mohm resistor or prove net battery-current measurement.

Example agent capture from the host repository (retain strict host-key checking and the established verified host-key file if the owner's default is stale):`ssh -T -o BatchMode=yes -o ConnectTimeout=5 -o StrictHostKeyChecking=yes \ -i "$HOME/.ssh/y2linux_ed25519" root@10.42.0.1 \ 'timeout 75 sh -s -- 30' < tools/development/sample-battery-adc.sh \ > out/m4-battery-room.tsv`

## Gates remaining even if BATON responds

There is no validated temperature window yet. The actual stock Y2 `do_batt_temp_state_machine` at 0xc03a0608 rejects the sentinel 255, stops at 50 C and resumes below 47 C. That compiled function has no cold cutoff, and the public temperature provider returns a literal 25 C. This establishes compiled upper-limit logic, not a physically validated charging window. `BAT_BatteryFullAction` at 0xc03a2328 selects recharge below 4110 mV in the stock 4.2 V policy. Neither threshold is installed as a Linux charge rule. Sprout's example thresholds are not automatically Y2 limits. Retain the conservative 70 mA / 4.175 V target unless contrary physical evidence requires stopping. Current sensing and percentage must not block a safely bounded policy if independent regulation/termination can be justified.

The live USB gadget advertises self-powered / 0 mA. BC1.1 is inactive and CHRDET gives presence only. Total system input demand and a valid USB budget are not established by the 70 mA charge selector. The battery OVP enable is set but its inherited selector 0 threshold is unresolved; input OVP selector 15 maps to 10.5 V in the BSP. PMIC thermal hardware power-down enable is clear. Preserve the existing protections while resolving these facts; do not label unarmed protection autonomous or a high OVP threshold a valid USB budget.

The charger watchdog is enabled with a BSP nominal 4 s timeout and needs verified driver ownership before charging. Active lifecycle, fault handling, suspend strategy, termination and recharge rules still need implementation. Stock's 150 mA termination threshold cannot be used with a 70 mA setpoint. Powered-off USB insertion/recovery has not been physically qualified. None of these open gates is solved by adding raw ADC channels.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
