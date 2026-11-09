---
title: "POWER-FINAL-33 — Reborn skins (themes) - Innioasis Updater"
description: "POWER-FINAL-33 — Reborn skins themes Status: INSTALLED 2026-10-14; owner: themes work; superseded by 34. Package out/y2linux-platform-v1-power-final-candidate-33/ fallbac"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-33.html"
---

# POWER-FINAL-33 — Reborn skins (themes) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-33 — Reborn skins (themes)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-33 — Reborn skins (themes)

Status: INSTALLED (2026-10-14; owner: themes work; superseded by 34). Package `out/y2linux-platform-v1-power-final-candidate-33/` (fallback = 32), receipts `out/deep-sleep-final/build33-receipts/`. BOOTIMG `1d19f28869cee65203c7e68bdae639e4bc3be523e0cbe77ba31cedd0a43d3eb2`, Y2ROOT `2d9b07a61c24b0f26f3d3a23be5d069efec7cb7a43c09f4ec9d132aeff1d7788`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-33`, kernel `6.18.56-y2linux-platform-v1-power-final-33`, root `2026.08-platform-v1.63`, release `1.0.0-platform-v1-power-final-candidate.33`; Linux `b42a391`, Reborn `76e681d` (skins `e4b175b`, vendor `cfd21df`, CLI fix `76e681d`). Contains 27–32; kernel and platform unchanged from 32 apart from the identity.

## Why

Owner: keep Reborn's own UI, but let people choose themes that give it a totally different look (e.g. a classic click-wheel player), switchable in Reborn and addable on the device. Scope audit: `docs/planning/roadmap-gap-audit.md` (POWER-FINAL-33). Steps 1 (engine, format, Classic) and 2 (every screen, TTF fonts, picker, install from storage); the web editor and polish are later steps.

## What 33 changes````````````

| Area | Change |
| --- | --- |
| Skin format | Folder with skin.json, PNG/JPEG/WebP pictures (≤480×360), TTF/OTF fonts; strict validation, contrast check, limits. Author guide: Y2Reborn docs/skins.md. |
| Screens | Layouts per screen with category fallback (home, now_playing, list, page, sheet/dialog, toast, volume, one name per screen). Undescribed screens and built-in parts (Cover Flow, equalizer, text entry, USB, Power hold) are Reborn's own drawing in the skin's palette. |
| Picker | Settings → Display → Theme; list rescanned on open; live switch; refused skins keep the current look and say why; choice persisted (Settings.theme). `rebornctl theme [ID |
| Install | Shipped: /usr/share/reborn/skins/classic (Open Sans, OFL in legal-info). User: a skin folder in Themes on Internal Storage or the SD card (via MTP). |
| Default look | Unchanged: every host preview state byte-identical to Reborn 0892bf2 except Display (new Theme row). |

## Tests

Reborn: 397 tests (skin compiler/interpreter, folder containment, picture decode, picker), clippy `-D warnings`, the architecture guard (UI does no I/O). Host headless run: list, switch to a `Themes` skin, refuse a broken one with the reason, back to Reborn, restore after restart (load 95 ms debug build on the host). Platform: `validate.py` PASS, ELF closure 354 PASS, installed ARM PASS (40 modules), privacy clean, inventory 108 packages, container suite 713 OK (`test_power_final_33` added to the suite after the build; passes on the host).

## Owner checks after the flash
  - Settings → Display → Theme: Reborn and Classic listed; choose Classic, browse Home, Songs, Albums (Cover Flow),

Now Playing, Settings, a song's options, volume; screen off/on and one sleep with Classic active.
  - Copy a skin folder (e.g. a copy of Classic renamed and with another `name`) into `Themes` on Internal Storage

over MTP; reopen the picker; it appears and applies. Same on the SD card.
  - Restart (hold Power): the chosen theme comes back. Choose Reborn: the original look returns.
  - `rebornctl theme --json` over SSH shows `load_ms` in the log event `skin_loaded`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
