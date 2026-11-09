---
title: "M4 production charging contract - Innioasis Updater"
description: "M4 production charging contract <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m4-charging.html"
---

# M4 production charging contract - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M4 production charging contract

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M4 production charging contract > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-14. Implemented candidate; active charging is not physically qualified. The current owner-installed M4-ADC-01 remains inhibited. No live charger writes, flash, suspend, reboot, calibration or RTC writes occurred in this pass. The owner's revised instruction permits the actual stock hardware protection architecture without a fabricated BATON temperature. M4 remains ACTIVE/PARTIAL.

Current charge-current policy, the full verified selector table and the measurement notes live in [charging-current-policy.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fcharging-current-policy.md) (POWER-FINAL-07).

## Premium-02 low-voltage policy update

The Premium-02 kernel candidate removes the former 70 mA clamp below 3.2 V. When the source is eligible for the configured 500 mA host profile, the MT6323 now keeps its validated 450 mA selector throughout deep-discharge recovery and the 3.2–3.4 V precharge range. The PMIC does not have a validated exact-500 mA selector in this board policy, so this is intentionally 450 mA at the hardware current-limit register, not an invented 500 mA claim. The source allowance, watchdog, input/battery OVP, 4.175 V charge target, 4.2 V safety guard, ADC and thermal checks remain unchanged. Dedicated sources retain their existing policy; unknown or insufficiently negotiated sources remain conservative/inhibited.

This is a host-validated source change only. Positive net battery gain from a depleted pack, charger stability and the historical overvoltage report still require attended physical qualification; the package must not be treated as proof that the battery or charger hardware is healthy.

## Actual stock Y2 reference

Primary behavioral evidence is the retained Y2 kernel, decompressed SHA256 `7287acf1b397d243c927dde5c6ef9d5d871c9c158207cdd98e0e820923f4c197`. Function boundaries and direct calls were followed in ARM disassembly, with register names/scales reconciled against the [pinned MediaTek charger implementation](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/power/mt6582/charging_hw_pmic.c) and [PMIC initialization](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/power/mt6582/pmic_mt6323.c). Those sources define field semantics; unrelated board profiles are not adopted. Original stock extracts stay in ignored `evidence-private/20260914-stock-charge-contract/`.``````````````````````````````````````

| Actual stock path | Reconstructed behavior |
| --- | --- |
| pmic_mt6323_probe 0xc04b88d4 → PMIC_INIT_SETTING_V1 0xc04b81f8 | Actual CID 0x2023 branch rejoins full initialization at 0xc04b8268. Input OVP selector 11 = 7 V, battery OVP selector 1 = 4.3 V. At 0xc04b830c–0xc04b831c, sets 0x003c bit5 THR_HWPDN_EN. This is autonomous PMIC die thermal shutdown. |
| charging_hw_init 0xc04cb170 | Charger WDT TD=0 (4 s), interrupt/enable/service; VCDT_MODE=0, input HV protection on; USB download SET=0/RST=1; BC1.1 reset/control; CSDAC mode; battery OVP on/selector1; BATON_EN=1, BATON_HT_EN=0; ULC enabled, low-current debounce=1. |
| charging_enable 0xc04cb698 | CSDAC delay4/step1/increment1/decrement2; current-sense comparator, hardware CV and battery CV comparator on; CSDAC_EN then CHR_EN. Off clears WDT controls, CSDAC/CHR and HWCV. Linux improves off ordering: verify both engines off before disabling WDT. |
| select_charging_curret 0xc03a1d88, pchr_turn_on_charging 0xc03a1ea4 | Unknown source selects 70 mA. Standard host requests 500 mA, floored to the 450 mA PMIC entry. Other detected source branches request 650/800/1100 mA. Compiled normal CV request is 4.2 V. Linux uses neither those higher currents nor 4.2 V. |
| charger_hv_detect_sw_thread_handler 0xc039fd70 | 2-second loop, 7 V hardware input OVP, disable on HV; services separate charger watchdog. charging_reset_watch_dog_timer 0xc04cb134 writes TD=0, WR=1, INT_EN=1, EN=1, FLAG_WR=1. |
| charging_get_battery_status 0xc04cb0e4 | BATON/TDET presence path. check_battery_exist exists, but its call must not be assumed from the generic BSP thread: the compiled Y2 watchdog thread does not call it. Linux checks presence every cycle. |
| BAT_PreChargeModeAction 0xc03a205c / BAT_ConstantCurrentModeAction 0xc03a2144 | Stock changes precharge state above 3400 mV; CC→top-off threshold is the Y2 global 4050 mV at 0xc09d2d6c. Includes a 1-second charging-off meter synchronization before restarting. Linux does not copy an unqualified current-offset calibration loop. |
| BAT_TopOffModeAction 0xc03a2208 | Six samples at/below stock 150 mA termination threshold (0xc09d2d70), or 10800 s top-off timeout. The 150 mA rule is invalid for a 70 mA profile and is not used. |
| BAT_BatteryFullAction 0xc03a2328 / BAT_thread 0xc03a0d90 | Recharge below 4110 mV. Compiled total-time guard compares against 0x1517f: stop at 86400 s (24 h), subject to stock test overrides. The BMT thread also stops at sampled charger voltage ≥6500 mV; Linux has no calibrated VCDT voltage yet and retains the 7 V autonomous input OVP, with charging restricted to a configured USB host. Linux has no timer-disable override. |
| mt_battery_charger_detect_check 0xc03a0b10 | CHRDET controls insertion/removal, source detection and USB connection; holds an AP wake lock with USB present, releases it on removal. battery_suspend cancels battery/watchdog timers; USB wake lock normally excludes this state. |
| mt_power_off 0xc04a1100 | Calls RTC BBPU power-down; with CHRDET still asserted, stock falls back to charger boot/reset. Linux retains its existing RTC poweroff mechanism, not this reset-as-poweroff fallback. |

Stock battery temperature APIs return constant 25°C. BATON hot detection is explicitly disabled by its charger init. Therefore stock did not establish continuous calibrated software pack-temperature protection. The evidenced alternative is PMIC die thermal shutdown plus the independent charger protections. This does not prove pack hot/cold protection, a pack protector circuit, or a valid safe Celsius window for the battery. BATON remains uncalibrated, not absent.

## Live entry and preserved protections

The latest read-only entry showed M4-ADC-01, battery present, Not charging, 3414990 uV, configured 70000 uA / 4175000 uV; CPU die 40450 m°C and PMIC die 9400 m°C. They are different sensors, not battery temperatures. Earlier 120 BATON/ISENSE samples and the inconclusive normal-handling experiment are retained in [the acquisition result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-battery-acquisition.md%23owner-deployed-adc-result--same-day&anchor=owner-deployed-adc-result--same-day). The [public register snapshot](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-14-stock-charge-contract/live-registers.txt) was read once through the existing read-only regmap debugfs, not a raw WACS client.

| Field | Entry | Candidate policy |
| --- | --- | --- |
| 0x000 CHR_EN/CSDAC_EN | Both off; HV_EN=1, automode=0 | Only the charger owner may enable; require HV protection, USB, valid source/sensors and no fault. Never alter automode/HV_EN. |
| 0x002 input OVP selector | 15, nominal 10.5 V | Set stock selector 11 / 7 V and read back, whatever was inherited (since #47, 2026-10-19). |
| 0x00c battery OVP | Enabled, selector0, exact threshold unestablished | Switch on at stock selector 1 / 4.3 V and read back (deglitch kept), whatever was inherited; refuse only while the detector (bit 6) reports an over-voltage (since #47, 2026-10-19). |
| 0x00e BATON | EN/TDET=1, hot detector=0, battery present | Preserve exact 0x0005 configuration, require presence. Unknown configuration inhibits. No fabricated thermistor conversion. |
| 0x03c thermal | 0; stock full kernel would set bit5 | Enable only stock THR_HWPDN_EN bit5, read back; never disable detection, change selectors or enter test mode. Any nonzero PMU_THR_STATUS at 0x044 inhibits. |
| 0x020 ADC routing/USBDL/UVLO | 0x0005 | Require and preserve. No test-mux, download charging, or undervoltage selector manipulation. |
| Current/CV, trim/emergency state | Selectors15/30; inherited trims | CV set to 4.175 V (selector 30) whatever was inherited: #47's player held 31 (4.1875 V) and the old check refused it, so it never charged. No calibration, OTP, OVP trim, battery profile, AP watchdog or emergency-reset writes. |

## Linux architecture and state machine

`PWRAP → single regmap → MT6323 MFD → IIO ADC + charger/power_supply`. USB glue publishes the standard power_supply `y2-usb-input`. Its `current_max` is the USB core's allocation in µA, not measured input or battery current. The charger binds to this supply through DT and a PM device link. USB callbacks never access PMIC hardware; they notify the sleeping charger owner.
  - Verified absence: both engines off, Status=Discharging; reset session faults/timers.
  - USB present without configured 500 mA allowance: Not charging. No BC1.1 claim.
  - Eligible source: verify engines off; tighten input OVP and restore stock PMIC

thermal shutdown; check preserved protections; program fixed selectors and stock DAC/comparator controls; arm WDT; reacquire critical sensors/source; recheck protection/regulation/watchdog; CSDAC_EN then CHR_EN, each read back.
  - Charging: one-second dedicated nonfreezable workqueue polls voltage, raw

BATON/ISENSE, calibrated PMIC die, presence, limits/protection bits and WDT.
  - Any fault: clear both engines and verify, then turn WDT/HWCV off. One bounded

retry handles failed inhibit IO without swallowing its error. If off cannot be verified, retain the last armed WDT, stop servicing it, keep AP awake and retry inhibition. No arbitrary userspace register recovery.
  - Manual `BAT0/charge_behaviour=inhibit-charge` synchronously inhibits. `auto`

restores automatic eligibility but cannot clear a fault or reset timers.

Limits: 3.4 V ≤ BATSNS < 4.175 V to start; a reading ≥4.2 V during charging is a fault. The lower boundary deliberately excludes depleted-pack revival; 3.4 V is both the documented MT6323 operating-range floor and stock precharge/CC transition, not an inferred pack damage threshold. The [MediaTek technical brief](https://www.nikom.biz/pic_info/A101018/MT6323.PDF) also identifies BATON/ISENSE; it does not establish this board's battery wiring. ADC timeout, unavailable die temperature (an unknown PMIC; a clear calibration fuse uses the vendor nominal read 10 °C high instead), saturated BATON/ISENSE, missing battery, PMIC IO error, altered critical configuration, OVP, hardware thermal alarm and watchdog errors all inhibit. The existing stock-derived 150°C PMIC critical limit is retained, with no assertion that it protects pack temperature.

## Watchdog, termination and PM

The charger WDT stays at 4 s; service target is 1 s, with a conservative 2.5 s software deadline. Service strobes are forced regmap writes, not potentially elided updates. Every service verifies TD/EN/INT_EN/OUT. An observed expiry or missed deadline latches a fault rather than restarting charging. Failed state/ADC/protection checks never pet it. Disabled charging does not pet it. Reboot/shutdown synchronously cancel work and inhibit before providers shut down.

Termination uses six qualifying samples at least 10 s apart: hardware CV comparator asserted and BATSNS ≥4.175 V. It stops and reports Not charging, not Full. A battery already at/above 4.175 V is also held without charging. Recharge requires six spaced samples below 4.110 V, checked protections and source permission. A one-sample drop or spike cannot qualify the normal transition. Missing valid taper/current measurement means this is a conservative voltage/CV stop, not verified full capacity. No 150 mA test is present.

Stock's 3-hour top-off budget begins once sampled voltage exceeds 4.05 V and cannot be reset by a voltage dip. Total charging is bounded at 24 hours per physical USB session, including recharge cycles. Either timeout latches a fault and reports Not charging. Neither timeout immediately restarts merely because voltage is below the recharge threshold. Faults require verified physical USB removal; USB reset/suspend, a manual policy toggle and bad samples do not reset them. Reboot loses software timers, but never raises CV/current or bypasses fresh checks.

Screen-off and WFI idle keep servicing normally. An active charge holds a wake source and the device PM prepare callback rejects `echo mem` with EBUSY. This is intentional, matching stock's charging wake-lock architecture. To enter s2idle, inhibit charging first; resume restores eligibility unless manual inhibition is still selected. CHRDET is the only additional intended wake IRQ, armed before MFD late suspend applies wake masks. It still needs physical qualification. No deep SPM, audio, storage, display, CPU OPP or regulator-policy change is made.

## Product limits and acceptance
  - BAT0 reports presence/status/health/voltage, configured current/CV and standard

`charge_behaviour`. `health=Unknown` with no known fault is deliberate: no continuously measured pack temperature. PMIC heat does not become battery TEMP.
  - No `temp`, `current_now`, `capacity`, estimated runtime or Full assertion.

Raw BATON1 and ISENSE remain IIO voltage channels. Their ADC errors still fail closed.
  - `BAT0/charging_state` is a read-only diagnostic snapshot, including fault mask,

raw values, configured-source allowance, hardware status, watchdog count and timers. Fault bits: 0x1 IO, 0x2 acquisition, 0x4 presence, 0x8 voltage, 0x10 OVP, 0x20 PMIC thermal, 0x40 watchdog/deadline, 0x80 protection/configuration, 0x100 time budget. Multiple bits can be present.
  - Gadget advertises bus power, maximum 500 mA. Only actual configuration permits

70 mA charging; reset/disconnect/suspend reduces allowance and inhibits. CHRDET alone and unclassified wall adapters do not permit charging. This unit's successful stock USB behavior used a higher charger selector; Linux reduces that demand. The allocation is not an external measurement of total demand.
  - 70 mA may not exceed running system consumption. Positive net battery gain,

source stability and screen-off behavior are physical acceptance tests. Do not call an enabled charger a successfully charging battery until the trend passes.
  - Cold/hot battery coverage, battery identity, calibrated NTC/current, BC1.1 wall

charging, and recovery below 3.4 V remain unresolved. No unattended first charge.
  - USB insertion while off retains PRELOADER/LK/RTC behavior. If it boots normally

and the battery/source pass the above checks, this kernel charges automatically. USB-triggered boot and deeply discharged recovery cannot be proved by these read-only live observations. No special charging OS or reset-as-poweroff hack.

[Manual deployment and exact qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m4-charge-01-deployment.md). M4 is not complete until the real device passes charging, removal/reconnect, PM/audio/display/storage regression and the other outstanding M4 criteria.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
