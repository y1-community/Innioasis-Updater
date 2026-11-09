---
title: "POWER-FINAL-26 — Bluetooth codec auto-selection - Innioasis Updater"
description: "POWER-FINAL-26 — Bluetooth codec auto-selection Status: INSTALLED, BLUETOOTH CODEC CHECK OPEN 2026-10-13; archive 121. Package out/y2linux-platform-v1-power-final-candida"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-26.html"
---

# POWER-FINAL-26 — Bluetooth codec auto-selection - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-26 — Bluetooth codec auto-selection

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-26 — Bluetooth codec auto-selection

Status: INSTALLED, BLUETOOTH CODEC CHECK OPEN (2026-10-13; archive 121). Package `out/y2linux-platform-v1-power-final-candidate-26/` (fallback = 25), receipts `out/deep-sleep-final/build26-receipts/`. BOOTIMG `f4ca442b185a6a8561ef12901d68c9662c630a5be65f554776fbe885fe1d585a`, Y2ROOT `66efd3ed0d4f727edeffa9dd6571f3d9c3e4ebe02647d8074b04c7cf09c2405f`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-26`, kernel `6.18.56-y2linux-platform-v1-power-final-26`, root `2026.08-platform-v1.56`, release `1.0.0-platform-v1-power-final-candidate.26`; Linux `64b3cc4`, Reborn `1c9edd4`. Platform as 25.

## 25 on the device (first check, archives 119–120)

Boot `f0cc8b34` healthy, taint 0, DSI hand-over dark (`backlight off until the first Linux frame` → `restored`). The owner's card now scans complete: 311 files discovered, 0 failures (24: "11 traversal failures"). Cover Flow frame rate not measured (the owner filmed it instead; the sampler caught only one 60-fps burst). The framebuffer stream tool reads ≈10 fps whatever the transport (raw 9.8, gzip 9.3; SSH chacha20 carries ≈19 MB/s), so it cannot show a 60-fps glide.

## Why only SBC was chosen

The platform already starts BlueALSA with every compiled codec (`--codec=AAC --codec=aptX --codec=aptX-HD --codec=LDAC`,`/run/y2/codec-runtime.json`). Live`org.bluealsa.Manager1.Codecs`=`A2DP-source:SBC`,`…:AAC`, `…:aptX`, `…:aptX-HD`, `…:LDAC`. Reborn accepted only the lowercase prefix `a2dp-source:`, so every codec, SBC included, was `runtime_enabled=false`; the policy failed (`no_eligible_codec_PHYSICAL_GATE_or_distribution_gate`), the codec choice (Auto included) stayed hidden and the saved preference was the old default, SBC. The AirPods Pro were on AAC only because BlueZ negotiated it at connect.

## What 26 changes (Reborn `1c9edd4`)
  - The A2DP-source profile in `Codecs` matches case-insensitively (`a2dp_source_codecs`).
  - Default codec preference is Auto: LDAC → aptX-HD → aptX → AAC among mutually usable codecs, SBC fallback, requested

only while the PCM is idle (unchanged policy code).
  - Sessions saved before `codec_revision` 1 that hold SBC (the old default; the choice was never offered) move to Auto

once; another saved codec, or SBC chosen afterwards, is kept.

## Tests

Reborn fmt, clippy `-D warnings`, workspace tests pass; the discovery test now uses the BlueALSA 5.0.0 names seen on the Y2, and both codec tests fail without the fix. Platform: `validate.py` PASS, ELF closure 354 PASS, installed ARM PASS, privacy clean, inventory 108 packages, container suite 693 OK.

## Owner checks after the flash
  - Settings → Bluetooth codec shows Auto, SBC, AAC for the AirPods Pro; Auto selected.
  - Status `bluetooth.codec_policy`: `runtime_enabled` true for all five, `selected`/`pcms[0].codec` AAC after a

reconnect with playback stopped.
  - aptX / aptX-HD / LDAC need headphones that offer them (NOT_RUN).

## 26 on the device (archive 121, boot `9f7fe545`)

Kernel `…power-final-26`, taint 0, Reborn running with the new session (`codec_preference` Auto, `codec_revision` 1: the SBC → Auto migration worked). The owner could not play music: Reborn's output was still the AirPods Pro (`14:14:7D:AA:34:47`) and every play press failed with `operation_failed "connected A2DP peer required"`. The AirPods were paired, bonded and trusted but never connected this boot: the platform reconnect (`/run/y2/bt-reconnect.json`) made two `ConnectProfile` calls, both ended without a reply (`completion_unknown_user_retry_required`), so automatic reconnect is `Inhibited` until a manual connect (`tools/connectivity/reconnect.c`, unchanged since 25). Reborn metrics: 0 Bluetooth connects, 0 disconnects; `pcms` empty, `codec_policy` none; codec history unchanged since 25 (last negotiated AAC). So 26's codec code never ran; the likely cause is the AirPods being in their case, out of range or held by the phone at boot.

Still open (device was unplugged for the overnight test before a manual connect was checked):
  - Manual connect (Settings → Bluetooth → AirPods Pro → Connect) works and lifts the inhibit.
  - Auto then requests AAC (26 is the first image that actually issues `SelectCodec` on connect) **without dropping the

link**; watch `metrics.bluetooth_disconnects` and the log right after the connect. If the request drops the link: skip `SelectCodec` when the negotiated codec already equals Auto's choice.
  - Design gap regardless of 26: when the saved Bluetooth output is not connected, Reborn only reports "connected A2DP

peer required"; it neither retries the connect on play nor falls back to the Y2's own output.

## Overnight test start: refused sleep looked like a self-wake (archive 122)

From 20:16 to 21:17 every sleep request was refused because the cable was attached (`suspend_refused_charger_or_usb_active`, once a minute). The owner unplugged at ≈21:18:38; the next attempt read `/sys/power/wakeup_count`, quiesced the radios (≈4–5 s), and at 21:18:42 the charger noticed the missing source (`status=2`, `NO_SOURCE`) and published a `BAT0` change (the only wakeup source with `wakeup_count` 1). At 21:18:44 the count store failed, so the helper refused (`product_refused`, `wake_event_in_progress`, no kernel entry) and restored the screen and radios: the "self-wake". The same refusal appears twice in the archived journals, both on 13; none on 14–25. The platform reconnect also tried the AirPods a third time after the radio restore and failed again (`failures` 3, still `Inhibited`).

Proposed platform fix (not made; needs the owner's OK and a 27 build): when the count store fails and neither the Power nor the RTC interrupt count changed, start a new handshake with a fresh count (bounded, e.g. 3 tries), as the maintenance-wake path already does after its `BAT0` tick, instead of restoring the screen.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
