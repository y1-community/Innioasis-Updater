---
title: "Y2Linux 1.0 Beta 8.5 (Baseline 93) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.5 Baseline 93 Status: PUBLISHED as GitHub release baseline-93 2026-10-18. Release 1.0.0-beta.8.5 , Reborn 1.0.0-beta.8.5 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.5.html"
---

# Y2Linux 1.0 Beta 8.5 (Baseline 93) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.5 (Baseline 93)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.5 (Baseline 93)

Status: PUBLISHED as GitHub release `baseline-93` (2026-10-18). Release `1.0.0-beta.8.5`, Reborn `1.0.0-beta.8.5`, kernel `6.18.56-y2linux-1.0.0-beta.8.5`, update sequence 6752, Linux `04e2dc8`, Reborn `b694670`. Built with `tools/production/release.py`: container suite 778 OK, host suite 804 OK (before the last three commits; their tests run in the container suite), Reborn 530 tests and strict Clippy; all seal checks PASS, no MediaTek firmware in any image. Test builds 91–93 (6750–6752) ran on the owner's player; 93 is exactly this release. Milestone audits HP-LEVEL-EQ and BETA-8.5 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md); the feature guide and measurement plan are in [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FHEADPHONE-OUTPUT.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 45f9b89b22fcabcd54e0d27aa49ddff3a63e6386db7d26529fa695dfb27d5912 |
| Y2ROOT | aaefe3897537a7146b315b7db8e5f493f9856fee289abf8bb64aa87b0c62f11d |
| RECOVERY | 1b19f504916aa8d2f684b8a7c5dfbd3752f65d304cd356de9561faf2506c5ba5 |
| Y2DATA (no SSH key) | 6dfafaecea36f6bb5267f952ddfdc17ab234fd9ef0eb4050f48c7c921f51af50 |

## What changed

The question came from an email about stock's bass roll-off and "output gain switching with impedance".``````````````````````````

| Part | Change |
| --- | --- |
| Headphone level | Kernel ALSA control HP Output Level (Low/Medium/High = CS43131 OUT_FS 1.0/1.41/1.73 Vrms with upstream hv_seq's HV_EN) and HP Output Level Live. Written only while the amplifier is down (DS1155F2), otherwise at the next power-up; probe default Low, the stock headphone level (before: High). Linux 2c59a31, test tests/test_hp_level.py (C harness on the real driver functions). |
| Loudness | Reborn's DAC Master −19.5 dB with the control (was −24 dB): Low plays 0.26 dB below the old level, never louder; Medium +2.7 dB, High +4.5 dB. A higher level restarts wired playback and fades in over 2 s. |
| Headphone profiles | Equalizer → Headphone Profile: AutoEq ParametricEQ.txt (peaking, low/high shelf with Q, up to 10 filters), clip-safe preamp (the file's or lower), limiter kept. 47 profiles of common headphones and IEMs come with the image (/usr/share/reborn/eq, AutoEq 7ae0f56, MIT); more from an EQ folder on Internal Storage or the SD card. FFmpeg gains lowshelf and highshelf. |
| DAC filter | Fast (default), Fast/Slow phase compensated, Slow, Nonoversampling (upstream codec controls). |
| Settings layout | Sound fits one screen: Equalizer, Normalize Volume, Gapless, Crossfade and the Output card ("Level Low · Filter Fast"); the card opens the Output page (outputs, Headphone Level, DAC Filter). Owner chose this of three layouts. |
| Build | 5de9c95: a resumed build rebuilds FFmpeg when its component options change (it never compiled new filters before). |
| Tools | tools/audio/test_signals.py: 88-s headphone measurement signal; Reborn tools/assets/fetch_eq_profiles.py. |

## Device results (owner's player, test builds 91–93, 2026-10-18)``````

| Check | Result |
| --- | --- |
| Install | Each by stage + apply over SSH, 16 s, Acknowledged; SMI hold at boot as in 8.4 |
| Default level | HP_OUT_CTL_1 0x10, CLASS_H 0x1C (8.4: 0x30/0x1E) |
| Wired play at Low | PWDN 0xA6, 0x10/0x1C, Master −19.5 dB, hp_level_live 0 |
| Level requested during playback | Registers unchanged; a silent stream afterwards came up at 0x30/0x1E (Live High); a request while down is written at once |
| High + Slow phase compensated + HD 650 profile (session edit, owner-approved) | Startup wrote 0x30/0x1E and PCM_FILT_OPT 0xC2; play at High without a fade (saved level); graph EQ=configured,preamp=-6.4dB,alimiter (file −6.1 dB lowered); 0 xruns, filter or decode errors |
| CPU of a 10-band profile (same song) | Decode + filter threads 4.4 % → 11.7 % of one core (second thread = FFmpeg's EQ slice thread) |
| Broken profile file | Refused with its line (owner: "it works") |
| Shipped profiles | 47 in /usr/share/reborn/eq, identical to the fetched files; license in legal-info |

## Known gaps
  - Not measured: the real output voltage, noise and frequency response per level and load, and the cause of stock's

bass roll-off (plan and test signal in [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FHEADPHONE-OUTPUT.md)).
  - Not run on the player: the level and the fade after a raise from the Settings screen, a level kept across a full

sleep (needs USB unplugged), the new Output page with the buttons.
  - Even High plays at most about 0.18 Vrms at full volume (stock about 0.71 Vrms): the Master limit is unchanged.
  - A 10-band profile costs about 7 % of one core while it plays; one filter thread may be cheaper.
  - Unchanged from 8.4: the restart fix over many restarts, the sleep drain (#42), the GC9503V panel (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
