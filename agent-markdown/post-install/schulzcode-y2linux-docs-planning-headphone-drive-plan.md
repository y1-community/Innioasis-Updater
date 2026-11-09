---
title: "Headphone drive plan: loud enough for every headphone, safe by default - Innioasis Updater"
description: "Headphone drive plan: loud enough for every headphone, safe by default Status 2026-10-25: Phases 1–3 published in Beta 8.35 Baseline 136, report (../validation/Y2-LINUX-1"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-headphone-drive-plan.html"
---

# Headphone drive plan: loud enough for every headphone, safe by default - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Headphone drive plan: loud enough for every headphone, safe by default

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Headphone drive plan: loud enough for every headphone, safe by default

Status 2026-10-25: Phases 1–3 published in Beta 8.35 (Baseline 136, [report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.35.md)); device-checked on the owner's player. The owner has no meter, so Phase 0 was skipped and one level table that works for both cases was chosen: Low 0.35, Medium 0.71, High 1.73 Vrms, picked by ear (current behaviour: [HEADPHONE-OUTPUT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FHEADPHONE-OUTPUT.md)). No kernel change. Owner decisions 2–4 taken as recommended. Two safety refinements: a level change raises the volume number only for the new stream (never on the old, louder one), and the volume can't go above the safe level through rebornctl either. The restore path now also gives the wired volume back after a Bluetooth absolute-volume session (it played wired at the headphones' level before). Asked by the owner after the FiiO FH7 (19 Ω hybrid IEM) played too quietly even at Headphone Level High. Builds on [HEADPHONE-OUTPUT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FHEADPHONE-OUTPUT.md) (Beta 8.5/8.6) and audit row HP-LEVEL-EQ in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## 1. Assessment

### What limits the level today (software)````````

| Stage | Today | Source |
| --- | --- | --- |
| Amplifier full scale (OUT_FS) | Low 1.0 / Medium 1.41 / High 1.73 Vrms | kernel 0030-cs43130-system-pm.patch, y2_hp_out_fs |
| DAC Master (digital) | fixed −19.5 dB on every wired stream | Reborn crates/reborn-audio/native/audio.c:67 |
| Reborn volume | gain = (volume/100)², so 100 = 0 dB, 50 = −12 dB, 10 = −40 dB | Reborn app/reborn/src/volume.rs:65 |
| Optional cuts | Headphone Profile preamp (−3…−8 dB), Normalize/ReplayGain, Balance | Settings → Sound |

Maximum at the chip pins, 0 dBFS: Low 0.106, Medium 0.149, High 0.183 Vrms. Stock firmware reaches ≈0.71 Vrms (OUT_FS 1.0, top volume step −3 dB), 11.8 dB more than our High. The chip itself reaches 1.73 Vrms, **19.5 dB more**. Beta 8.5 picked the −19.5 dB Master so that no setting played louder than older Y2Linux builds. It was a cautious migration choice, not a hardware limit.

### What may limit it in hardware: a ≈100 Ω series resistance (unconfirmed)

The chip's own DC load measurement reads every load about 102 Ω high (commit `c852008`, #37): an 18 Ω IEM read 121/120 Ω, two 32 Ω headphones read 135 and 134 Ω. A constant offset across loads is what a resistor between the chip and the jack produces. If that resistance is real, the player has an output impedance of ≈100 Ω:
  - Low-impedance loads lose the most: 19 Ω gets 19/121 of the voltage (−16 dB), 32 Ω −12 dB, 300 Ω −2.5 dB.
  - Multi-driver IEMs (the FH7 has one dynamic and four balanced-armature drivers, so its impedance changes with

frequency) change their tonal balance. A single EQ cannot correct this for every IEM.
  - Stock firmware has the same board, so stock pays the same penalty. Stock just starts from 12 dB more.

The FH7 complaint fits the resistor theory. Without a resistor, our current High would give the FH7 about 113 dB SPL at full scale, which is loud. With it, the FH7 gets about 97 dB, which is quiet for real music (average levels sit 12–20 dB below full scale). Phase 0 settles this.

### Evidence: report 94debfc2 (install 02f46e9f, Beta 8.34, 2026-10-24)

The reporter said they could "barely hear" a loud song at volume 85 with the FH7. Their mixer and Reborn state are exactly as designed, with no errors and no xruns:
  - Level High (requested and live), Master 216 = −19.5 dB, volume 83 (−3.2 dB on the squared curve)
  - Headphone Profile Focal Clear (an over-ear headphone, not the FH7), preamp −6.9 dB; ReplayGain off; DAC filter

Slow; S16 sink

A 0 dBFS peak leaves the chip at ≈0.057 Vrms, 29.6 dB below what the chip can deliver. Music averaging −10 dBFS then gives the FH7 about 93 dB SPL without a series resistor, or 77 dB with one. "Barely hear" fits the second case better (an IEM tip seal that is not tight would also cost level, mostly in the bass). Ledger: F45 in `UserReports/REVIEWED.md`.

### Peak SPL at 0 dBFS (calculated, not measured)

Sensitivity in dB SPL/mW. Typical classes plus the FH7 from FiiO's spec (19 Ω, 111 dB/mW). "Loud enough" here means ≥ 110 dB peak, so average music reaches about 90–98 dB.

Without series resistance

| Headphone | now Low | now High | stock | 0.5 V | 1.0 V | 1.41 V | 1.73 V |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sensitive IEM 16 Ω / 112 | 110 | 115 | 127 | 124 | 130 | 133 | 135 |
| FiiO FH7 19 Ω / 111 | 109 | 113 | 125 | 122 | 128 | 131 | 133 |
| Portable 32 Ω / 102 | 97 | 102 | 114 | 111 | 117 | 120 | 122 |
| Planar 32 Ω / 94 | 89 | 94 | 106 | 103 | 109 | 112 | 114 |
| Studio 80 Ω / 96 | 87 | 92 | 104 | 101 | 107 | 110 | 112 |
| 250 Ω / 96 | 83 | 87 | 99 | 96 | 102 | 105 | 107 |
| HD 600-class 300 Ω / 97 dB/V | 78 | 82 | 94 | 91 | 97 | 100 | 102 |

With 102 Ω series resistance

| Headphone | now Low | now High | stock | 0.5 V | 1.0 V | 1.41 V | 1.73 V |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sensitive IEM 16 Ω / 112 | 93 | 98 | 110 | 107 | 113 | 116 | 117 |
| FiiO FH7 19 Ω / 111 | 93 | 97 | 109 | 106 | 112 | 115 | 117 |
| Portable 32 Ω / 102 | 85 | 90 | 102 | 98 | 105 | 107 | 109 |
| Planar 32 Ω / 94 | 77 | 82 | 94 | 90 | 97 | 99 | 101 |
| Studio 80 Ω / 96 | 80 | 85 | 97 | 94 | 100 | 103 | 105 |
| 250 Ω / 96 | 80 | 84 | 96 | 93 | 99 | 102 | 104 |
| HD 600-class 300 Ω / 97 dB/V | 75 | 80 | 91 | 88 | 94 | 97 | 99 |

### Verdict
  - Software can fix most of it. Using the chip's full range (up to 1.73 Vrms) makes every IEM and most portable and

studio headphones loud enough, whether or not the series resistance exists.
  - Hardware caps the rest. Low-sensitivity planars and 250–600 Ω studio headphones end up around 100–107 dB peak.

That is fine for most music but not "loud" for quiet classical recordings. No software can go past 1.73 Vrms. For those headphones the honest answer is an external amplifier (or USB audio output, not supported yet).
  - The danger is at the other end. Without the series resistance, a sensitive IEM at 1.73 Vrms reaches ~135 dB peak.

The fix must therefore come with gain staging, a safe-volume warning and loudness-preserving migration. Unlocking the ceiling alone is not enough.

## 2. Design goals
  - Every headphone gets the chip's full voltage when needed (High = 1.73 Vrms at volume 100).
  - Sensitive IEMs keep fine volume steps, low hiss, and no blast on accidental volume-up (Low stays a low range).
  - Nothing gets louder by itself: not after the update, not on plug-in, restart or gain change.
  - Going past today's maximum loudness needs one deliberate confirmation (safe-volume warning).
  - Bluetooth output is unchanged (absolute volume is the headphone's).

## 3. Plan

### Phase 0: measure (decides the gain table)

One multimeter with AC volts, a 3.5 mm breakout and a 33 Ω resistor (or the player's own `hpload_measure` plus a known resistor) are enough:
  - Play a steady 0 dBFS sine at 400 Hz (many cheap meters are only accurate at low frequencies) at High, volume 100.

Measure tip–sleeve with nothing connected, then across the 33 Ω resistor. - Same voltage (±10 %) → no series resistance. Variant B. - About ¼ of the voltage → ≈100 Ω series resistance is real. Variant A.
  - Do the same for left and right. Also check crosstalk (one channel driven, the other loaded). A shared resistor in

the ground return would show up as crosstalk, not only as loss.
  - Developer check only, never with headphones on: `amixer -c Y2Audio sset Master 0dB` after the stream starts, at

each level. Measure the full-scale voltage into 33 Ω and open circuit, then into 16 Ω at −1 dBFS to check for clipping. Do this once on a full battery and once at ≈3.5 V (HV_EN needs VP ≥ 3.3 V, and the real VP rail is not known).
  - Optional, by ear: FH7 on stock at the top step vs. Y2Linux High at 100. Expect stock to be about 12 dB louder.

The full measurement matrix in [HEADPHONE-OUTPUT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FHEADPHONE-OUTPUT.md%23measurement-plan&anchor=measurement-plan) stays the long-term goal. Phase 0 is the minimum needed to pick a variant.

### Phase 1: gain table (kernel small, Reborn Master per level)

Reborn sets Master per level instead of one fixed −19.5 dB. The kernel gains a fourth OUT_FS option (0x00 = 0.5 Vrms) only if Variant B needs it. Proposed levels, final values after Phase 0:

| Level | Meant for | Variant A (series R real) | Variant B (no series R) |
| --- | --- | --- | --- |
| Low | IEMs | 1.0 FS, Master −3 dB → 0.71 V (= stock) | 0.5 FS (new), Master −3 dB → 0.35 V |
| Medium | portable headphones | 1.41 FS, Master 0 → 1.41 V | 1.0 FS, Master −3 dB → 0.71 V (= stock) |
| High | planar / 80–600 Ω | 1.73 FS, Master 0 → 1.73 V | 1.73 FS, Master 0 → 1.73 V |

The level descriptions in the UI name the use ("IEMs and sensitive earphones", …), not voltages. HV_EN keeps the upstream pairing (off for Low/0.5/1.0 FS, on for 1.41/1.73 FS).

### Phase 2: volume curve with even steps (Reborn)

The squared curve gives 0.35 dB per wheel click near 100 but 12 dB between volume 2 and 4. With a higher ceiling, IEM users would spend their time at the coarse bottom. Proposal: 0 = mute, 1…100 = −60…0 dB in 0.6 dB steps (wheel step 2 = 1.2 dB per click, about one just-noticeable difference), with a short taper below 5 so 1 is really quiet. This applies only to the wired sink gain (`VolumeRamp::gain`). Bluetooth absolute volume keeps its own mapping. The sleep-timer fade and the 5 ms ramps still work because they act on the gain, not on the step size.

### Phase 3: safety
  - No louder after the update (migration). On first start with the new table, convert the saved wired volume so

the output level in dBV at the chip stays the same: `new_dB(volume') = old_dB(volume) + old_ceiling_dB − new_ceiling_dB`. Example: old High at 100 (0.183 V) becomes about volume 68 on new High (1.73 V, −19.5 dB). The saved level is kept. One host test per level and both variants.
  - Gain changes keep the loudness. Switching Low → High lowers the volume by the dB difference before the stream

restarts (and High → Low raises it, clamped at 100). The existing 2 s fade-in stays as a second guard.
  - Safe-volume warning. The reference is the output in dBV at the chip, the same for all levels:

threshold = today's maximum (0.183 Vrms ≈ −14.7 dBV), so nothing users can do today asks anything. Volume up past the threshold stops at it and shows "Listening at high volume for a long time can damage your hearing. Raise the volume?". Select confirms; it is asked again after 20 h of listening above the threshold (the Android rule; counted in the session state, survives restarts). The threshold is close to the 150 mV figure that EU player rules use for unknown headphones, which makes it a defensible default.
  - Start below the threshold. At boot, on wired output start and after switching from Bluetooth to wired, a

volume above the threshold starts at the threshold. The user raises it again in one step after the warning has been accepted. The warning is not asked twice in one session.
  - Wheel and key repeat stay bounded (existing tests). With 1.2 dB per click, a held volume-up needs several

seconds to cover 20 dB.

### Phase 4 (optional, later): help picking the level
  - Shipped Headphone Profiles get an optional impedance/sensitivity line. Choosing a profile suggests a level, but

never raises one by itself.
  - Once jack detection exists (#11/#12, parked), `hpload_measure` on plug-in can suggest Low for loads under ~50 Ω.

It only ever suggests or lowers, never raises.
  - Variant A only: a "player correction" for the series resistance cannot be one EQ for all IEMs (it depends on each

IEM's impedance curve). Not planned. Document it as a hardware property instead.

## 4. Validation
  - Host: extend `tests/test_hp_level.py` if the kernel gains the 0.5 V level. Reborn unit tests for the new curve

(monotonic, 0 = silence, step sizes), migration (same dBV per level and variant), gain-change compensation, warning threshold and re-arm, start cap.
  - Device, targeted: amixer readback of Master/`HP Output Level Live` per level. Meter readings at volume 100 per

level against the table (±0.5 dB). Migration check: old High 100 → same voltage after the update. Warning flow over the SSH input-event method. FH7 by ear on all three levels. One low-battery clipping pass at High.
  - Docs: HEADPHONE-OUTPUT.md (levels, curve, safety), audit row HP-LEVEL-EQ, release report.

## 5. Owner decisions
  - Run Phase 0 (needs a meter and a resistor, about 15 minutes), or decide the variant without measuring. Without

measuring, Variant B values are the safe choice; Variant A plays louder.
  - The safe-volume threshold (proposed: today's maximum) and when to re-arm it (proposed: 20 h above the threshold).
  - The new volume curve (changes how the wheel feels for everyone on wired output).
  - Whether High's full 1.73 Vrms is open to everyone after the warning (proposed: yes).

## 6. Effort

Kernel: none (Variant A) or one table entry plus a test (Variant B). Reborn: the Master per level, the curve, migration, compensation, warning UI and session counter, about a day with tests. One test build, then a release.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
