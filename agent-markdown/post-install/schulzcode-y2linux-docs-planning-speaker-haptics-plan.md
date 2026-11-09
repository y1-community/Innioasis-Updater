---
title: "Internal speaker and haptic feedback — research and plan - Innioasis Updater"
description: "Internal speaker and haptic feedback — research and plan Status: implemented and published in Beta 8.41 Baseline 159: haptics as stock's key press 60 ms per button, no wh"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-speaker-haptics-plan.html"
---

# Internal speaker and haptic feedback — research and plan - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Internal speaker and haptic feedback — research and plan

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Internal speaker and haptic feedback — research and plan

Status: implemented and published in Beta 8.41 (Baseline 159): haptics as stock's key press (60 ms per button, no wheel ticks, owner's choice), speaker steps S1–S3 as planned (jack by polling, no IRQ). See the [Beta 8.41 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.41.md). The sections below are the research as written.

Research 2026-10-27 for the next update. Sources: the stock FM kernel through REA (`out/rea/fm-kernel.elf`, sha256 `329466b3…`, Ghidra 12.1.2 + llvm-objdump), the stock `system.img` (MyLauncher.apk strings only), the donor tree (`donorSource/`, Chris Hendrickson, GPL-2.0) and our current kernel/Reborn. Nothing was built, flashed or run on a player. Issue: #28 (haptics); no issue for the speaker yet.

This adds two hardware subsystems, so per AGENTS.md the roadmap/gap audit must be repeated before implementation starts. This document is research, not authorization.

## Summary``````````

|  | Haptics | Speaker |
| --- | --- | --- |
| Hardware | ERM motor on the MT6323 VIBR LDO | CS43131 HP outputs → AW87559 (or OCA72559) class-D amp → speaker |
| Stock driver | MTK timed_output "vibrator": switch VIBR on, hrtimer off | vendor CS43131 driver + aw87559_on/off, jack detect on EINT16 |
| Upstream/donor reuse | upstream regulator-haptic + mt6323-regulator (same registers as stock) | donor aw87559.c (tables verified identical to stock) + donor speaker DAPM widget |
| Effort | small: DT + config + one PMIC bit + Reborn | medium: amp driver, machine-driver route, jack detection, Reborn output + downmix |
| Main risk | none known; voltage above stock untested | jack detect needs the codec powered (we power it off when idle) |

Recommendation: ship haptics first (one small, self-contained kernel step plus a Reborn setting). Do the speaker as a second step, starting with jack detection, because automatic switching depends on it.

## 1. Haptics (vibration motor)

### What stock does (REA, observed)
  - `vib_mod_init` (0xc0492784) calls `vibr_power_set` once: `upmu_set_rg_vibr_vosel(cust.vib_vol)`.

`get_cust_vibrator_hw` returns `{vib_timer = 50, vib_limit = 9, vib_vol = 5}` at 0xc0a01500. VOSEL 5 = 2.8 V (`dct_pmic_VIBR_sel`: 2800 mV → 5). The voltage never changes.
  - `vibrator_enable(ms)` (0xc0492a0c): 0 = off; a request of 10–49 ms is raised to

50 ms; ≤ 9 ms passes unchanged; capped at 15 000 ms. An hrtimer ends it.
  - `update_vibrator` → `vibr_Enable_HW` → `dct_pmic_VIBR_enable(1)` →

`upmu_set_rg_vibr_en` = PMIC 0x542 bit 15. Off clears the same bit.
  - Voltage field: `upmu_set_rg_vibr_vosel` = PMIC 0x544 bits 7:5.
  - Stock PMIC init also sets 0x542 bit 2 (`vibr_ther_shen_en`, VIBR thermal

shutdown). Our golden comparison already lists this as a mismatch (`docs/validation/data/y2-stock-suspend-golden-20261011.json`, stock 1, ours 0).
  - LK does not touch the motor (no vibrator strings in `fm-lk.elf`).
  - The stock app has a "Key Vibration On/Off" setting (`getKeyVibrationOn/Off`,

`icon_setting_vibrate_on/off`, `android.permission.VIBRATE`). The durations it uses are not known: decompiling the APK needs jadx, which the permission classifier blocked in this session.

### What we have
  - Upstream `drivers/regulator/mt6323-regulator.c``ldo_vibr`: enable

`DIGLDO_CON39` (0x542) bit 15, voltage `DIGLDO_CON40` (0x544) mask 0xE0, table 1.2/1.3/1.5/1.8/2.0/2.8/3.0/3.3 V. These are the same registers stock uses.
  - `kernel/dts/innioasis-y2.dts` declares no `ldo_vibr` and no haptics node.

`kernel/config/production.config` has no `INPUT_REGULATOR_HAPTIC`.
  - Donor DT has both (`mt6323_vibr_reg` + `regulator-haptic`, 1.8–3.3 V). Its

3.3 V top is above stock's fixed 2.8 V; the motor rating is unknown.

### Plan
  - DT: `ldo_vibr` regulator (`regulator-name = "vibr"`, 1.8–2.8 V) and

`haptics { compatible = "regulator-haptic"; haptic-supply = <&vibr>; min-microvolt = <1800000>; max-microvolt = <2800000>; }`. Cap at the stock 2.8 V; a "strong" setting = stock strength.
  - Config: `CONFIG_INPUT_MISC=y`, `CONFIG_INPUT_REGULATOR_HAPTIC=y` (selects

`INPUT_FF_MEMLESS`).
  - PMIC: set 0x542 bit 2 (thermal shutdown) once at probe, as stock does. This

is the existing golden-table row, so the change is stock parity.
  - Reborn: open the input device named `regulator-haptic`, upload one

`FF_RUMBLE` effect, and play it on a wheel detent (`reborn-platform/src/input.rs``WheelCadence::detent`) and on button presses. Settings > Customize (or Sound): Haptics Off / Light / Strong (magnitude → voltage between 1.8 and 2.8 V). Rate-limit to about one tick per 25–30 ms so a fast spin doesn't hum continuously. No haptics while the screen is dark.
  - Tick length: start at 20 ms and 50 ms (stock floor) and choose on the player.

An ERM motor needs time to spin up, so very short pulses may not be felt.

### Device checks owed
  - Motor runs at all (`fftest` / a 200 ms rumble), Light vs Strong both felt.
  - A fast wheel spin stays responsive and does not delay UI frames.
  - Sleep: the regulator is off after suspend (regulator-haptic disables it on

suspend); overnight drain is unchanged.

## 2. Internal speaker

### Hardware path (stock + donor, observed)

CS43131 HPOUTA/HPOUTB → AW87559 input (I2C1 0x58, enable = GPIO8) → speaker. Stock bound `1-0058 aw87559_pa`. Some units have the pin-compatible OCA72559 (chip ID 0x09); the donor unit reported ID 0x09. Stock and donor handle both.

### What stock does (REA, observed)

Amplifier — `Sound_Speaker_Turnon` (0xc04a2900) → `aw87559_on` (0xc054acc4): GPIO8 mode 0, output, low → 10 ms → high → 100 ms, read ID (0x5A AW87559 / 0x09 OCA72559, up to 5 retries with the same pulse), write the register table, then wait 80 ms. `aw87559_off`: SYSCTRL 0x01 = 0x30, GPIO8 low. If neither ID answers, stock falls back to pulsing GPIO8 three times (a one-wire mode for a different amp); not needed for I2C parts. **The donor `sound/soc/codecs/aw87559.c` tables are identical to stock, write for write** (both AW87559 and OCA72559), and so are its timings.

DAC route — `cs43131_apply_route` (0xc054baa8):``````

|  | Headphones | Speaker |
| --- | --- | --- |
| PCM_PATH_CTL_2 (0x90004) | 0x00 (L-R) | 0x05 (L-L + bit 2, i.e. L and −L, differential) |
| ASP_CH_1_SZ_EN (0x5000A) | 0x06 | 0x06 |
| ASP_CH_2_SZ_EN (0x5000B) | 0x0E | 0x06 |
| HP_OUT_CTL_1 OUT_FS (0x80000 bits 5:4) | cs43131_hp_gain_fs[level] (0x10 default) | 0x30 (1.73 Vrms) |
| PCM volume (0x90001/2) | cs43131_vol_table[i] | (15 − i) × 4 + 6 half-dB steps: −3 dB at top, 0xFF mute at 0 |

The speaker gets only the left channel: channel B carries inverted left. Our side must downmix (L+R)/2 before the DAC, otherwise right-only content is lost. That is a conclusion from the register values; the exact meanings of PCM_PATH_CTL_2 bit 2 and ASP_CH_2 bit 3 are not in the upstream header.

Switching — `cs43131_hp_switch_to_hp` / `…_to_speaker`: mute (PCM volume 0xFF), amp off or on, `apply_route`, 10 ms, restore the route volume. Order: premute → amp → route → unmute.

Jack detection — EINT16 (GPIO16, input, no pull, level-low, debounce 0x20) → `cs43131_hp_work_callback`: sleep 200 ms, read HP_STATUS (0xD0001) bit 6. Plugged → speaker off, headphone route. Unplugged → mute, route state = speaker, report the `h2w` switch as 0. The Android app pauses on that event ("becoming noisy"). The amp only comes on when playback is routed to the speaker (`AudDrv_ioctl` → `Sound_Speaker_Turnon`). Re-plugging within 350 ms is debounced by `cs43131_hp_deferred_check_callback`.

Codec power — `cs43131_off` only sets PDN bits and keeps power on. Stock removes codec power (`cs43131_power_down_hw`: mask EINT16, GPIO 15/18/20 low, VGP2 off) only at `cs43131_early_suspend` (screen off, not playing) and restores it at `late_resume`. **So stock jack detection works only while the codec is powered: screen on, or playing.**

App — MyLauncher has "Speaker On/Off" (`getSpeakerOn/Off`, `icon_setting_speaker_on/off`) and listens for `HEADSET_PLUG`.

### What we have
  - `kernel/dts/innioasis-y2.dts:123`: GPIO8 is a gpio-hog held low

(`speaker-disabled-m3`). There is no amp node and no amp driver.
  - `kernel/audio/y2-cs43131.c`: one `Headphone` widget/pin, HPOUTA/B only, codec

idle bias off, codec runtime PM + `vgp2_idle_off` (stock-like rail switching). HP Output Level control writes OUT_FS at HiFi DAC PRE_PMU.
  - No jack detection: the CS43131 node has no `interrupts`, so upstream cs43130

runs with `has_irq_line = 0`. Upstream already supports the jack: its IRQ thread reports HP plug/unplug to a card jack named "Headphone" via `snd_soc_jack_report`.
  - Reborn `AudioOutput { Wired, Bluetooth }`. The sink restores `Master` and the

`Headphone` switch on close (`reborn-audio/native/audio.c`).

### Plan

Step S1 — jack detection (useful on its own: auto pause on unplug, #12/PHY-011)
  - DT: CS43131 `interrupts-extended = <&pio 16 IRQ_TYPE_LEVEL_LOW>` plus a pinctrl

state for GPIO16 as EINT (stock: no pull, hw debounce).
  - Codec power: detection needs the codec powered while the screen is on (stock

parity). Options: (a) hold a codec runtime-PM reference and VGP2 while the screen is on and release both at screen-off, as stock does; (b) read GPIO16 directly as a mechanical switch, if the line still changes with the codec unpowered (a device check decides). Measure the awake-idle cost of (a).
  - Reborn: watch the ALSA jack control ("Headphone Jack"); on unplug, pause

playback (stock behaviour, no surprise speaker playback).

Step S2 — amplifier + route
  - Add the donor `aw87559.c` as `kernel/audio/aw87559.c` (GPL-2.0, tables

verified against stock). Remove the GPIO8 hog. Add the `amplifier@58` node (`enable-gpios = <&pio 8 GPIO_ACTIVE_HIGH>`, `sound-name-prefix = "PA"`) and make it an aux device of the Y2 card.
  - `y2-cs43131.c`: add `SND_SOC_DAPM_SPK("Speaker", event)` + pin switch, routes

HPOUTA/B → "PA IN" → "PA OUT" → Speaker. The event writes the stock speaker registers (PCM_PATH_CTL_2 0x05, ASP_CH_2 0x06, OUT_FS 0x30) at POST_PMU and restores 0x00 / 0x0E / the HP level at PRE_PMD. It must coordinate with the existing HP Output Level write (one owner for OUT_FS).
  - The kernel enforces that Headphone and Speaker pins are never both on. Mute

around the switch (stock premute/unmute); the amp's 190 ms start-up happens while the DAC is muted, so it does not pop.
  - `ignore_pmdown_time` already powers the amp down when the stream closes.

Step S3 — Reborn
  - `AudioOutput::Speaker`; chosen automatically when no headphones and no

Bluetooth are connected and Speaker is On (setting like stock's "Speaker On/Off"; Off = never play from the speaker).
  - Downmix to mono (L+R)/2 in the DSP chain when the speaker is active; skip Balance,

Headphone Profile and HP level. Use a separate speaker volume curve with stock's −3 dB top as the cap. Consider a high-pass filter (about 200–300 Hz) for the small driver; tune it by ear.
  - Plug in → switch to Wired; unplug → pause (S1).

### Device checks owed
  - Which amp the owner's unit has (ID 0x5A or 0x09): first probe log line.
  - Speaker audible at a low level; no pop on start, stop, plug or unplug.
  - Whether plugging in headphones physically cuts the speaker (the donor note

says "speaker audibility depended on jack removal").
  - GPIO16/HP_STATUS with the codec powered and unpowered (decides S1 a vs b).

Reading GPIO16 needs the owner's OK.
  - Awake idle current and overnight drain with the S1 power policy.
  - Both amps if a second unit is available (OCA72559 table untested by us).

## Open questions
  - Stock app tick duration/pattern: needs the APK decompiled (jadx was blocked

by the permission classifier this session). It only tunes the default.
  - Motor voltage rating: stay at stock's 2.8 V max until known.
  - PCM_PATH_CTL_2 bit 2 / ASP_CH_2_SZ_EN bit 3 exact semantics: the CS43131

datasheet would confirm the "inverted left" reading; the on-device listen test settles it either way.
  - Speaker power budget/thermal: stock has no speaker protection; mirror stock

limits only.

## Evidence index (stock FM kernel addresses)

| Function | Address |
| --- | --- |
| vib_mod_init / vibr_power_set | 0xc0492784 / 0xc056316c |
| vibrator_enable / update_vibrator | 0xc0492a0c / 0xc0492bf8 |
| dct_pmic_VIBR_enable / dct_pmic_VIBR_sel | 0xc04b7024 / 0xc04b7818 |
| cust vibrator struct | 0xc0a01500 = {50, 9, 5} |
| Sound_Speaker_Turnon / Turnoff | 0xc04a2900 / 0xc04a29f0 |
| aw87559_on / aw87559_off | 0xc054acc4 / 0xc054b080 |
| cs43131_apply_route / apply_out_fs | 0xc054baa8 / 0xc054b78c |
| cs43131_refresh_volume_for_route | 0xc054b304 |
| cs43131_hp_switch_to_hp / to_speaker | 0xc054bdc0 / 0xc06edc90 |
| cs43131_hp_work_callback / deferred_check | 0xc054bf30 / 0xc054c060 |
| cs43131_on / off / early_suspend / power_down_hw | 0xc054c648 / 0xc054c7a0 / 0xc054bed0 / 0xc054b620 |
| cs43131_vol_table / hp_gain_fs | 0xc0760918 (ff 6e 68 62 5c 56 50 4a 44 3b 32 29 20 17 0e 06) / 0xc0760928 (00 10 20 30) |

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
