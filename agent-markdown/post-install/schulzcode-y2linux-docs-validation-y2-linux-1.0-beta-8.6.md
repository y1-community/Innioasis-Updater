---
title: "Y2Linux 1.0 Beta 8.6 (Baseline 94) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.6 Baseline 94 Status: PUBLISHED as GitHub release baseline-94 2026-10-18. Release 1.0.0-beta.8.6 , Reborn 1.0.0-beta.8.6 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.6.html"
---

# Y2Linux 1.0 Beta 8.6 (Baseline 94) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.6 (Baseline 94)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.6 (Baseline 94)

Status: PUBLISHED as GitHub release `baseline-94` (2026-10-18). Release `1.0.0-beta.8.6`, Reborn `1.0.0-beta.8.6`, kernel `6.18.56-y2linux-1.0.0-beta.8.6`, update sequence 6800, Linux `fd32cdb`, Reborn `cefcc8a`. Built with `tools/production/release.py` (148 s): container suite 778 OK, host suite 805 OK, Reborn 539 tests, fmt and strict Clippy; all seal checks PASS, no MediaTek firmware in any image. Test build 94 on the owner's player is exactly this release. Milestone audits AUDIO-REVIEW-8.5 and BETA-8.6 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md); guide: [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FHEADPHONE-OUTPUT.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 51a5c6a30065cf7f62393eb875c8f5d4f068fd28cdb34fd772f6a727d67f17fc |
| Y2ROOT | 91b1d6162c476f064d74eccf2438e871b248e9d1217bfe99a75332c0da3f37cc |
| RECOVERY | 7da688f91abd681116b0dd5ca3a626caa42f0ad234ae218cceb0b7569e4abf19 |
| Y2DATA (no SSH key) | d2a777efd876a08f6b8695193a90863d74e23655109ed4a92af377fa5d0430db |

## What changed

A review of everything in audio playback after Beta 8.5 (owner: "do it all").````````

| Part | Change |
| --- | --- |
| Kernel level write | The headphone level's PDN_HP check and the OUT_FS/HV_EN write run under the card's DAPM mutex: a stream powering up at that moment can no longer get the level written with the amplifier on (DS1155F2). y2_hp/hpload_measure refuses an open stream (EBUSY) and holds DAPM while it measures. Linux 0c8e7f5, tests/test_hp_level.py models the lock. |
| No loudness jumps | A fade-in carries over when the stream restarts during it (Next, a seek, another rate); volume up during a fade keeps fading; sound settings that play ≥ 1 dB louder (a profile turned off, a boosting preset, Normalize changed) fade in over 2 s. |
| Held pause | Every sound-settings change gives a held pause's stream back, so Play uses the new settings; choosing the Headphone Level already in use no longer restarts the song. |
| Battery | An equalizer or profile no longer asks for the heavy playback class (747.5 MHz floor, 1 ms wake-up limit); only crossfade does. The FFmpeg filter graph runs on one thread (bit-identical output). |
| Profiles | The clip-safe preamp covers source rates 44.1–384 kHz (six shipped profiles 0.1–0.4 dB lower, e.g. AirPods Pro −6.0 → −6.1, Sony WF-1000XM4 −7.7 → −8.1; HD 650 unchanged). The license file no longer appears as a profile. |
| Tests | FFI layouts pinned on both sides, sanitize idempotence, hi-res preamp, a full 10-filter profile with ReplayGain +6 dB on a new near-full-scale fixture at S24/S16 (limiter holds; without it the output clips), the real shipped-folder scan. |

## Device results (owner's player, test build 94 = this release, 2026-10-18)

Buttons were pressed over SSH by writing input records to the player's own input devices; the screen was read with the capture tool.````````````

| Check | Result |
| --- | --- |
| Install | Stage + apply over SSH, ≈16 s, Acknowledged 6800; SMI hold at boot as in 8.4/8.5 |
| Profile list | K → M without "LICENSE-AutoEq" |
| Profile off / on while playing | Off: dsp_rise_fade 2000 ms; on: no fade, preamp −6.1 dB (AirPods Pro) |
| EQ change in a held pause | pause_released, position kept |
| Checked level pressed again | No restart |
| High while playing, Next after 0.7 s | level_raise_fade, then fade_continued with 907 ms left |
| Registers | Playing Low 0xA6 / 0x10 / 0x1C, High 0x30 / 0x1E, Live matches, Master −19.5 dB, 0 xruns |
| hpload_measure during playback | EBUSY |
| AirPods Pro profile, 60 s, same song | 8.5: CPU floor 747.5 MHz throughout, Reborn 17.9 % of one core (playback 12.0 %), 68 248 idle entries/min. 8.6: floor 598 MHz (average 608), playback thread ≈75 MHz (≥16 % fewer cycles), 30 443 idle entries/min. Profile off: playback ≈29 MHz |

## Known gaps
  - Battery current with a profile not measured (USB stayed connected); deep idle is blocked during any playback either

way (audio keeps INFRA up), so the gain is the lower CPU floor and fewer wake-ups.
  - A 10-filter profile still costs ≈46 MHz of the decode thread on the device.
  - Not run on the player: volume up during a fade (host test), a DAC Filter change by ear, sleep with a level set.
  - Files below 44.1 kHz rely on the limiter (FFmpeg skips filters above Nyquist).
  - Unchanged from 8.5: no output measurement yet, maximum output ≈0.18 Vrms, the sleep drain (#42), GC9503V (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
