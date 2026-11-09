---
title: "Headphone output: level, equalizer profiles, DAC filter and measurement - Innioasis Updater"
description: "Headphone output: level, equalizer profiles, DAC filter and measurement Status 2026-10-25: released in Beta 8.5 Baseline 93, review fixes in Beta 8.6 Baseline 94; device"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-headphone-output.html"
---

# Headphone output: level, equalizer profiles, DAC filter and measurement - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Headphone output: level, equalizer profiles, DAC filter and measurement

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Headphone output: level, equalizer profiles, DAC filter and measurement

Status 2026-10-25: released in Beta 8.5 (Baseline 93), review fixes in Beta 8.6 (Baseline 94); device results in the [Beta 8.5](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.5.md) and [Beta 8.6](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.6.md) reports. Louder levels, the dB volume scale and the safe-volume warning are in Beta 8.35 (Baseline 136) ([headphone drive plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FHEADPHONE-DRIVE-PLAN.md), report F45). No output has been measured yet. Audit row HP-LEVEL-EQ in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## What the hardware does

The headphone jack is driven by a Cirrus Logic CS43131 (I2C1 0x30) with a ground-centred class-H amplifier. Datasheet DS1155F2, HP Output Control 1 (0x80000) OUT_FS:

| Setting | OUT_FS | Full scale | CLASS_H (0xB0000) | Y2Linux level |
| --- | --- | --- | --- | --- |
| 00 | 0x00 | 0.5 Vrms | — | not offered |
| 01 | 0x10 | 1.0 Vrms | 0x1C (HV_EN off) | Low: stock's register value, the default |
| 10 | 0x20 | 1.41 Vrms | 0x1E (HV_EN on) | Medium |
| 11 | 0x30 | 1.73 Vrms | 0x1E (HV_EN on) | High: what Y2Linux used before Beta 8.5 |

The HV_EN pairing follows the upstream driver's load table (`hv_seq`). The datasheet allows OUT_FS changes only while the amplifier is powered down (PDN_HP set). It specifies HV_EN = 1 for loads of 600 Ω and more and VP ≥ 3.3 V. Stock never writes CLASS_H, so stock runs 0x10 with the reset value 0x1E.

Stock (REA of the stock kernel's vendor driver `cs43131_apply_out_fs`): headphones get 0x10, the speaker route 0x30. It has no impedance measurement. The route comes from jack detection (HP_STATUS / EINT16). Stock's 16-step volume table tops out at −3 dB, so the stock maximum is about 0.71 Vrms.

## What Y2Linux does now
  - Kernel (`kernel/patches/0030-cs43130-system-pm.patch`): ALSA control `HP Output Level` (Low/Medium/High) on

card Y2Audio, and the read-only `HP Output Level Live` (what the output runs at, or `Other`). A requested level is written at once while the amplifier is down. Otherwise it is written right before the next power-up, in the "HiFi DAC" PRE_PMU event, while PDN_HP is still set. The card ignores pmdown_time, so the amplifier powers down when a stream closes. The request lives in the driver, not the register cache, so it survives runtime and system suspend. The PDN_HP check and the write run under the card's DAPM lock, so a stream starting at that moment cannot power the amplifier in between (audio review, 2026-10-18). The old sysfs switch `y2_hp/hp_gain` uses the same path. `y2_hp/hpload_measure` still measures the load but no longer changes the level; it refuses while a stream is open (`EBUSY`) and holds the DAPM lock while it measures. Host test: `tests/test_hp_level.py` (C harness on the real driver functions).
  - Reborn: Settings → Sound → Output → Headphone Level sets the control before each wired stream starts. Each

level has its own DAC Master (`HpLevel::master_db`), set right after the amplifier powers up for the level it really runs at (−24 dB until then, and when the live level is unknown):

| Level | Full scale | Master | At volume 100, 0 dBFS | Safe volume |
| --- | --- | --- | --- | --- |
| Low (earphones, IEMs) | 1.0 Vrms | −9 dB | ≈0.35 Vrms | 90 |
| Medium (most headphones) | 1.41 Vrms | −6 dB | ≈0.71 Vrms (stock's loudest) | 80 |
| High (hard to drive) | 1.73 Vrms | 0 dB | 1.73 Vrms (the chip's maximum) | 67 |

 Beta 8.5 to 8.34 held Master at −19.5 dB for every level, so the loudest output was 0.106 / 0.149 / 0.183 Vrms. That was too quiet for IEMs (report F45), and the board probably has ≈100 Ω in series with the jack (the load measurement reads 102 Ω high). Without a meter the series resistance is unconfirmed, so the levels are spread wide enough for either case and users pick by ear.

 The volume has even steps: 10–100 rise by 0.6 dB a step (a wheel click is 1.2 dB), 1–9 by 3 dB down to −81 dB, 0 is silence (before: a squared curve, 12 dB between 2 and 4). The safe level is the old loudest output, 0.183 Vrms ≈ −14.7 dBV at the chip. On the jack, volume up stops there and asks Raise the Volume? once. The agreement lapses after 20 hours of listening above it, and the volume returns to the safe level. Reborn starts on the jack at most at the safe volume (the headphones may have changed), and so does a return from Bluetooth. Changing the level moves the volume so the music stays as loud: lower at once for a higher level, higher only for the new stream at a lower level (never a loud moment on the old one). An old session's volume moves once to the same output level (High 100 → 67, Low 100 → 82). Bluetooth headphones with their own volume are unchanged. Changing the level during wired playback restarts the stream so the new level takes effect, and the first stream after a rise fades in over 2 s. A held pause gives its stream back, so the new level starts with Play. A fade carries over when the stream restarts during it (Next, a seek), and volume up during it keeps fading. Sound settings that play louder (a profile turned off, a boosting preset, Normalize changed) fade in the same way. On a kernel without the control, Master stays at −24 dB.
  - DAC Filter (Settings → Sound → Output): Fast (default, the chip's and stock's), Fast Phase Compensated, Slow, Slow Phase

Compensated, Nonoversampling. These are the upstream controls `PCM Filter Speed`, `PCM Phase Compensation` and `PCM Nonoversample Emulate`, applied at once.
  - Headphone Profile (Settings → Sound → Equalizer → Headphone Profile): 47 AutoEQ profiles of common headphones

and IEMs come with the image (`/usr/share/reborn/eq`, Reborn `assets/eq/SOURCES.md`, MIT). More: put AutoEQ `ParametricEQ.txt` files in a folder named `EQ` on Internal Storage or the SD card; a file there replaces a shipped profile of the same name. Up to 10 filters: PK (peaking), LSC (low shelf) and HSC (high shelf), with Q. These are the RBJ cookbook biquads that Equalizer APO and AutoEQ use, played by FFmpeg's `equalizer`, `lowshelf` and `highshelf`. The preamp is the file's own, or lower when the filters' combined response still rises above 0 dB between 10 Hz and Nyquist at any source rate from 44.1 to 384 kHz (the filters run before resampling; AutoEQ's HD 650 file says −6.1 dB; Reborn uses −6.4 dB). For files below 44.1 kHz FFmpeg skips filters above Nyquist and the limiter catches the rest. The limiter stays after the filters. Reborn keeps the imported profile when the file is removed. Choosing a preset turns the profile off.

## Measurement plan

Goal: measure the real output of each level into realistic loads, and find out where stock's bass roll-off comes from.

### Equipment
  - An audio interface or analyser whose input takes ≥ 2 Vrms without clipping (or a known attenuator); REW, ARTA or

an APx/QA403-class analyser.
  - Load resistors 16 Ω, 32 Ω and 300 Ω (and open circuit), with a 3.5 mm breakout. Optionally one real IEM

and one real headphone, through a coupler or as an electrical load.
  - The player on battery and USB unplugged (no ground loop, no charger noise). One extra pass with the charger

connected shows charger noise.

### Player settings

Y2Linux build with the level control (the next test build). Then: Equalizer Flat, Normalize Volume off, Crossfade off, DAC Filter Fast, Output Headphone Jack, volume 100 (Reborn's volume is digital; 100 = 0 dB). Copy `Y2 Headphone Test Signal.flac` (`tools/audio/test_signals.py`, timeline in its `sections.txt`) to Internal Storage and play it once per level and load.

| Time (s) | Section | Use |
| --- | --- | --- |
| 2–4 | 1 kHz −20 dBFS marker | sync |
| 4–34 | digital silence | idle noise (unweighted and A-weighted, 20 Hz–20 kHz) |
| 34–44 | 1 kHz −20 dBFS | level, THD+N, output impedance (loaded vs open) |
| 44–49 | 1 kHz −1 dBFS | highest output at this level, THD+N at full scale |
| 49–57 | 1 kHz −20 dBFS left only, then right only | crosstalk |
| 57–62 | 50 Hz −20 dBFS | bass level and bass output impedance (capacitor check) |
| 64–74, 76–86 | log sweep 20 Hz–20 kHz −12 dBFS | frequency response |

REW users can also export REW's own sweep file and play it from the player (file playback mode).

### Matrix and results

For Low, Medium and High × open, 300 Ω, 32 Ω and 16 Ω, record:
  - Vrms at 1 kHz −20 dBFS and −1 dBFS. Output impedance from open vs loaded: Zout = R_load × (V_open / V_load − 1),

at 1 kHz and at 50 Hz.
  - Frequency response, 20 Hz–20 kHz, left and right, normalised at 1 kHz (export as CSV or REW .mdat).
  - Idle noise: µV unweighted and A-weighted, plus the spectrum (hum, charge-pump or class-H tones).
  - THD+N at −20 and −1 dBFS, and crosstalk.
  - The same matrix on stock firmware (top volume step), at least FR and 1 kHz level into 16 Ω and 300 Ω.

### Reading the results
  - Bass roll-off that depends on the load (worse into 16 Ω than 300 Ω, and the 50 Hz Zout higher than at 1 kHz)

means an analog series capacitor or resistor on the board. It is then the same on stock and Y2Linux. The kernel's load measurement already reads about 102 Ω high on this board (commit `c852008`), so check series resistance.
  - Roll-off on stock only means Android audio processing, which Y2Linux bypasses.
  - Roll-off the same into every load comes from the digital path or the DAC filter. Compare DAC Filter settings.
  - Level changes with the load beyond what Zout explains would be real "gain switching". The stock kernel has no

load measurement, so stock should not do this.

### Building a player correction
  - Average L/R per level and load and normalise at 1 kHz; the deviation from flat is the player's own response.
  - A load-independent deviation becomes one fixed correction for the wired output, a low shelf or one or two

peaking filters, fitted the same way AutoEQ fits headphones.
  - A load-dependent deviation (series C/R) cannot be fixed by one EQ. Fit R and C from the curves:

H(f) = Z_L / (Z_L + R + 1/(j2πfC)). Then compute the inverse for a load class (IEM ≈ 16–32 Ω, headphone ≈ 32–300 Ω) and approximate it with one or two biquads. The load class comes from a user choice or, once jack detection works (#11/#12), from the kernel's `hpload_measure`.
  - Reborn would apply this "player correction" before the headphone profile (≤ 2 filters plus AutoEQ's 10; the

engine limit would rise to 12), with the clip-safe preamp covering both. Re-measure with the correction on.

Safety: measure into loads, never with headphones on someone's head while testing levels or Master changes. A developer-only full-scale test can raise the DAC Master over SSH once playback has started (`amixer -c Y2Audio sset Master 0dB`; Reborn sets Master again at every stream start). That plays up to 1.73 Vrms, High's own maximum; at Low it is 9 dB above Reborn's maximum.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
