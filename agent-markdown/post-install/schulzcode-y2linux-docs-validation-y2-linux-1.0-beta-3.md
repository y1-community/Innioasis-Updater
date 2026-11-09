---
title: "Y2Linux 1.0 Beta 3 (Baseline 52) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 3 Baseline 52 Status: PUBLISHED as GitHub release baseline-52 2026-10-15. Release 1.0.0-beta.3 , Reborn 1.0.0-beta.3 , kernel 6.18.56-y2linux-1.0.0-beta."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-3.html"
---

# Y2Linux 1.0 Beta 3 (Baseline 52) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 3 (Baseline 52)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 3 (Baseline 52)

Status: PUBLISHED as GitHub release `baseline-52` (2026-10-15). Release `1.0.0-beta.3`, Reborn `1.0.0-beta.3`, kernel `6.18.56-y2linux-1.0.0-beta.3`, update sequence 5200, Linux `2731169`, Reborn `8cd4362`, git tag `baseline-52` in both repositories. Built with `tools/production/release.py` (`--public`): container suite 739 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-3 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md). First release of the new pipeline: build and all checks 119 s (build 76 s incl. BlueALSA and Reborn, checks in parallel 27 s, signing/firmware scan/assets 15 s), 158 s with the clean-up scan.````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | ca90dda51376b0fa58da5d6950936e3faf75eccf855e0725a08e98cc05acaebd |
| Y2ROOT | 1e71564d7e1e80e81c293a6f5c0dc6e8eb4cb716479c2d9c7c95fb114e01e221 |
| RECOVERY | 20c665edab509fb26a164ca7480e9fb9f497c664b22f29fbe73bc146420b142d |
| Y2DATA (no SSH key) | 01a73f767a8883d1327c43d4cc0d05c0ea5b762092bdaca6c51b0771a091b078 |

## Evidence behind the changes (Beta 2 player, 2026-10-15, read-only)
  - AirPods Pro connected, AAC 44.1 kHz. BlueZ's cached endpoint `c0 01 8c 83 e8 00`: the AirPods accept AAC **VBR, up to

256 kbit/s; Beta 2 sent BlueALSA's default 220 kbit/s CBR** without the FDK afterburner (60-s HCI capture: 2588 packets of 651 bytes ≈ 224 kbit/s).
  - Link at close range, Wi-Fi associated and idle: median acknowledgement 46 ms, worst 78 ms, ≤ 4 packets in flight,

no gap above 100 ms. Encoder load ≈9 % of one core at 598 MHz (Reborn ≈14 %).
  - BlueALSA keeps a three-packet socket buffer and blocks while the radio cannot deliver; only LDAC adapts its rate

(ABR). A weak link therefore starved AAC headphones at the full rate.
  - Coexistence: our WMT start sends the stock shared-antenna setting (`01 10 02 00 01 01`, `coex_wmt_ant_mode=1` from the

owner's `WMT_SOC.cfg`), identical to the stock sequence for this chip; nothing missing was found there.
  - Page timeout: no `page timeout … slots` line appeared on Beta 2, so the controller already used 0x2000 (5.12 s); the

~18 s "Host is down" of Beta 1 comes from BlueZ's own sequence, and Beta 2's 45-s reconnect deadline is the fix.

## Since Beta 2````````````````````````````

| Change | Detail |
| --- | --- |
| AAC quality | --aac-afterburner, --aac-bitrate=320000, capped by the peer (AirPods 256 kbit/s) and by one packet per frame (y2_aac_mtu_bitrate: a 672-byte MTU keeps the tested 220 kbit/s; headsets that cannot reassemble fragmented frames keep working). CBR, not VBR (Android's default for compatibility). Setting aac_quality high (default) / standard. |
| AAC adaptive rate | BlueALSA patch 0002-y2-aac-adaptive-bitrate.patch: per frame the socket queue is read (as for LDAC ABR); two queued packets or a blocked write step the CBR rate down 8/8 → 6/8 → 5/8 → 4/8 (not below 128 kbit/s, at most every ~0.2 s), ~10 s of an empty queue steps it back up. FDK re-initialises its configuration between frames, no encoder restart. Decisions in y2-aac-abr.h, host-tested (tests/test_bluetooth_aac_abr.py). Setting aac_abr on (default) / off. |
| Observation | EncoderStats now covers AAC; platform status reports bitrate_bps, aac_abr_enabled, aac_abr_level, aac_abr_adjustments. |
| SBC XQ | XQ / XQ+ selectable without the experimental switch (default stays high). |
| Reborn | Service menu rows AAC Quality and AAC Auto Rate; SBC XQ codec choice no longer tied to the experimental switch. |
| Pipeline | First release through release.py (one workspace, parallel checks, unchanged sources linked, prune). |

## Device checks owed (after the owner's over-the-air install, read-only)

`uname -r` = `6.18.56-y2linux-1.0.0-beta.3`; with the AirPods playing: `y2-platform status bluetooth` → `encoder.bitrate_bps` 256000 (or the MTU-capped value), `aac_abr_enabled` true, `aac_abr_adjustments` 0 at close range; bluealsad CPU (was ≈9 %); a listening comparison against Standard; a walk-away test watching `aac_abr_level` and audible dropouts.

## Known gaps

Battery in sleep ≈9.4 mA vs stock ≈1.3 mA; the AAC changes are not yet heard or range-tested on the device; no headphone jack detection; rare slow display start after a restart; full install from stock run on one player only.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
