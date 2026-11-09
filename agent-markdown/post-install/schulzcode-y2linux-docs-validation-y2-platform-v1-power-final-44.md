---
title: "POWER-FINAL-44 — dark recovery screen: DSI register reads lag one word - Innioasis Updater"
description: "POWER-FINAL-44 — dark recovery screen: DSI register reads lag one word Status: FLASHED by the owner 2026-10-16; cold start lit, archive 20261016/148 ; tested over the air"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-44.html"
---

# POWER-FINAL-44 — dark recovery screen: DSI register reads lag one word - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-44 — dark recovery screen: DSI register reads lag one word

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-44 — dark recovery screen: DSI register reads lag one word

Status: FLASHED by the owner (2026-10-16; cold start lit, archive `20261016/148`); tested over the air with 45. Package `out/y2linux-platform-v1-power-final-candidate-44/` (fallback = 43, which the player runs), receipts `out/deep-sleep-final/build44-receipts/`. BOOTIMG `f2c19f69980a6ea2491503437db29d0e32cd25a40cff6d4a28c9799242437385`, Y2ROOT `d53db06a9d54ebf89a6e49a6bd0c559b11dca95218c23c812dbe493bdf30d0a9`, RECOVERY `56fdf20b07eb7f4fe61ec92f33aad8a958118578a870ddcc8ca2916500d6a77f`. Kernel `6.18.56-y2linux-platform-v1-power-final-44`, release `…candidate.44`, update sequence 4400. Container suite 718 OK, all seal checks PASS. Signed OTA (release key): `…-44-ota-release/`; development reinstall: `…-44-ota-devtest/`.

## 43 results
  - Install without a Power press PASSED (43 development reinstall, restart switch on): restart into recovery,

install 53 s (verify 1.7 s → backup 3.7 → system 34.9 → check 48.0 → boot 52.6 → installed 53.3), restart into the new system (boot reason 4), display lit (vblank 16 → 219), health `Acknowledged`.
  - The recovery's progress screen stayed dark (owner: "only the update display did not show with usb

connected"). The restart into the result was lit.

## Why the recovery screen was dark

The recovery's kernel log (`/data/logs/recovery-last.log`) has the 43 SMI hold, an idle larb0 at the hand-over and a clean mutex reset, but no vblank after the first modeset (`vblank wait timed out`, `flip_done timed out`). Its DSI scan line reads the register file shifted by one word: each read returns the previous read's data (`vactive=198048` is PSCTRL's `0x305a0`, `lcc=0x168` is VACT_NL's 360). The only earlier boot with this signature is archive `20261016/143` (42, cold start with USB plugged in, early hand-over at 0.49 s): its snapshot differs from the lit restart 147 in 77 DSI words and nothing else that matters (SMI, MMSYS gates, PHY, mutex identical). The real CON_CTRL reads 0: every read-modify-write of the DSI (`mtk_dsi_mask()`) stored a neighbour's value, DSI_EN never stuck, no frame started. 144 (the larb0 wedge fixed in 43) reads DSI correctly, so this is a second, intermittent failure mode. USB enumeration is not concurrent with the modeset (5 s in 143). Why the register port lags is still unknown.````````````

| Change | Detail |
| --- | --- |
| mtk_dsi_poweron() (patch 0017) | After the timing setup, reads PSCTRL then VACT_NL; if VACT_NL is not the mode's vactive (Y2SCAN DSI read-back …), power-cycles PHY and DSI clocks and repeats the setup, at most 3 times (DSI register reads lag one register; power-cycling the DSI (attempt n)). A correct read-back costs two register reads. |
| Hand-over | handoff: clocks on; park video (ps=… vact=…): the same read-back of LK's timing shows whether the lag comes from the loader. |
| Recovery | Saves /sys/kernel/debug/y2_display_snapshot as /data/logs/recovery-display.txt with its kernel log. |

## Owner steps
  - With the owner's OK: install 44 over the air (restart switch on): staged `…-44-ota-devtest` or the release

package, Turn Off and Install in Reborn (with the switch on it restarts instead). Watch the recovery screen.
  - The agent checks the recovery log for the read-back lines, `Acknowledged`, and the new boot's display.
  - If the recovery screen is dark again: the agent saves `recovery-display.txt` and the log (archive), and a

recovery probe (`y2-update-core probe`, restart switch on) repeats the restart-entered recovery without installing anything.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
