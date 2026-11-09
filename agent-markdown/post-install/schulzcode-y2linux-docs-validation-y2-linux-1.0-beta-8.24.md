---
title: "Y2Linux 1.0 Beta 8.24 (Baseline 123) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.24 Baseline 123 Status: PUBLISHED as GitHub release baseline-123 2026-10-23. Release 1.0.0-beta.8.24 , Reborn 1.0.0-beta.8.24 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.24.html"
---

# Y2Linux 1.0 Beta 8.24 (Baseline 123) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.24 (Baseline 123)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.24 (Baseline 123)

Status: PUBLISHED as GitHub release `baseline-123` (2026-10-23). Release `1.0.0-beta.8.24`, Reborn `1.0.0-beta.8.24`, kernel `6.18.56-y2linux-1.0.0-beta.8.24`, update sequence 8800, root `2026.08-platform-v1.163`, Linux `2a21690`, Reborn `e199d9c`. Built with `tools/production/release.py` (136 s, resumed workspace, update based on `baseline-122`): container suite 867 OK, host suite 894 OK, Reborn workspace 626 tests, clippy and fmt clean; all seal checks PASS, no MediaTek firmware in any image. Installed on the owner's player before publishing. Milestone audit BETA-8.24 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 3d59f0ac40f78efaaa3c6c5f32ede081bc1d801001418a18253ce68737ee1607 |
| Y2ROOT | 2b803ed645b8c4317c01c862cc779612dc6c1386f9792318d98e08b19e53f5ce |
| RECOVERY | 861437fa5911566a22bdfdd713bf8222ea4b25f437bc5c200686c01b19b70118 |
| Y2DATA (no SSH key) | 7b87a7eb3d68f5021693910b5def632dbb357cbbe2ecc3028184973b356bed85 |

## Why 8.23 was not enough (#52)``````````````

| Evidence | What it shows |
| --- | --- |
| #52 report y2linux-report-20261022-220205 (install 2813306c, 8.23, first boot after the OTA) | the crystal came up in 30 ms and the player took about 4.5 min of skipping (95 kept-sink reuses), then failed at a 48 kHz start (PLL_READY -110, ALSA -110) followed by XTAL_ERR (status1=49, errors=5). In this player's 8.21, 8.22 and 8.23 sessions every failure is a 48 kHz start; 44.1 kHz starts never failed. Reporter: three to four times more skips than before, and a restart did not bring the sound back |
| Stock system.img/etc/audio_policy.conf | the primary output (speaker, wired headset/headphone) has sampling_rates 44100 only: Android resamples 48 kHz before the HAL. With the stock kernel's set_freq (rate bits only, no PLL), stock never runs the CS43131's PLL |
| Y2Linux 8.17–8.23 | 48 kHz sources played at 48 kHz through the codec PLL (fed by the crystal); the one thing stock never does is where #52's crystal falls over |

## What changed since Beta 8.23``````````````````````

| Area | Change | Evidence |
| --- | --- | --- |
| No codec PLL (#52) | The AFE front end and I2S back end offer 44.1 kHz only (stock's only output rate), and the codec refuses any rate its 22.5792 MHz crystal does not clock (-EINVAL before any clock work, logged). Reborn's wired plan always asks for 44.1 kHz; the decoder converts 48, 96 kHz and other rates (as stock's mixer did). Every track now plays on in the one open headphone sink, whatever its rate | Linux f66d71d (kernel/audio/mt6582-afe.c, overlay 0030, tools/platform/capabilities.json, tests/test_codec_clock.py); Reborn 83f0082 |
| Self-healing (#52) | A crystal error flag seen at a stream start power-cycles the codec (rails off 500 ms, then the stock power-up) before that stream, which waits for the restarted crystal. y2_hp/xtal gains cycles= | Linux f66d71d (register model) |
| Cold start at probe | A probe that finds the codec's rails on switches them off for 500 ms before powering up, and logs cold start. Correction: the commit and code comment assume a restart leaves VGP2 on; on the owner's player a software restart and an OTA restart both reset VGP2 (it comes up at its 2.5 V reset value and off), so a restart already cold-starts the DAC and this path does not trigger (cold_start=0). It stays as a safety net | owner's player, two restarts |

## Device results (owner's player, build 123)````````````````````

| Check | Result |
| --- | --- |
| OTA 8705 → 8800 | restarted by itself 73 s after Update, Acknowledged on health boot 1 |
| After boot | ready_ms=30, cycles=0, cold_start=0, SYS_CLK_CTL_1=04, PWDN_CTL=f0 |
| Rates | 48 kHz FLAC, 96 kHz FLAC and 44.1 kHz MP3 each play at 44100 Hz (hw_params), crystal selected (SYS_CLK_CTL_1=04), no PLL line |
| Skips across rates | 4 × 20 Next/Previous 0.3 s apart ending on 48 and 44.1 kHz alternately, 10 alternating 48/44.1 kHz starts: all play; sink_reused +50, sink_reopened 0; no crystal/ASoC kernel line (13/13 PASS) |
| Software restart | VGP2 enabled (4 users) before, at its 2.5 V reset value and off at the next probe: cold_start=0 |

## Open
  - #52/#54 confirmation from the reporters. The self-healing cycle could not be triggered on the owner's player (its

crystal never flags an error); host register model only. Crystal errors during a kept sink (same-stream track changes) are seen only at the next stream start.
  - Not checked on a player: a real sleep and wake, a full power-off, the click check by ear (unchanged from 8.23).
  - The overlay comment on the cold start stated the disproven VGP2 assumption; corrected on main after the build (in the next release).
  - Owner decision (2026-10-23): the crystal changes of 8.21–8.23 stay. Most copy stock, and which of them fixed #52 is

unknown. After the reporters confirm 8.24, only non-stock parts that prove unnecessary are trimmed: the probe cold start first, then the power cycle if no report shows `cycles>0`, then the ready wait once `ready_ms` is no longer needed. The screen-on hold's battery cost is measured before it is touched.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
