---
title: "Y2Linux 1.0 Beta 8.22 (Baseline 121) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.22 Baseline 121 Status: PUBLISHED as GitHub release baseline-121 2026-10-22. Release 1.0.0-beta.8.22 , Reborn 1.0.0-beta.8.22 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.22.html"
---

# Y2Linux 1.0 Beta 8.22 (Baseline 121) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.22 (Baseline 121)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.22 (Baseline 121)

Status: PUBLISHED as GitHub release `baseline-121` (2026-10-22). Release `1.0.0-beta.8.22`, Reborn `1.0.0-beta.8.22`, kernel `6.18.56-y2linux-1.0.0-beta.8.22`, update sequence 8607 (test builds 8600–8606 found the issues below on the owner's player), root `2026.08-platform-v1.156`, Linux `073aa0c`, Reborn `e196033`. Built with `tools/production/release.py` (114 s, resumed workspace, update based on `baseline-120`): container suite 866 OK, host suite 893 with two load-flaky report tests that pass alone (45/45), Reborn workspace tests, clippy and fmt clean; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.22 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 2ed4cd218f1e8d430d42d0fb20977cef1291d840e8ac628791e473dfd1b14090 |
| Y2ROOT | 61322e2169ed87ad3a60b0b8c800d74efcca4abe06a8275647b3b717ae560008 |
| RECOVERY | 6a30f2d6be48c3607ab00ef08809043ccd7709cdf9e60b650d5c0858d0845f19 |
| Y2DATA (no SSH key) | 50b3c6edd0223539f06ee3010615e505fa7238060b64478ce1bda479b94d35aa |

## What changed since Beta 8.21

All fourteen uploaded reports pending on 2026-10-22 (8.10–8.20, nine players) were reviewed; findings F23–F31 in the review ledger, plus a user's message (F32) and GitHub #53.````````````````````````````````````````````````````````````````````````````````````````````

| Finding | Change | Evidence |
| --- | --- | --- |
| F23: an update rolled back — the new system's first boots died before the system logger (d0337717, 8.16→8.17, "new system did not confirm health"; 5f8082dd needed two boots), both GC9503V; no trace survived | Evidence: init, every rcS script and the platform's boot stages are written to pstore's message buffer (/dev/pmsg0, 128 KiB of the existing 1 MiB ramoops region, CONFIG_PSTORE_PMSG); the RAM console alone held only critical lines (loglevel=3, 41 bytes). Each update health boot keeps the previous boot's trail, console and oops record plus this boot's battery voltage, LK boot reason, data check and boot-check record in /data/updates/health/ (newest 4; reports collect them). Until health is confirmed the console takes every kernel message and a CPU stall panics into a ramoops record and a restart; confirmed health restores both. Fix candidate: the recovery stopped neither its UI (≈9 frames/s) nor the backlight before reboot -f; it now does both, as the normal restart. Cause still unproven | Linux f977ab5, 0d0712c; tests/test_production_handover.py, tests/test_platform_update.py |
| F24: headphones refused with ALSA -16 1–3 s after a wake | Reborn's sink open takes a shared activity.lock; the sleep helper held it exclusively through the ≈1.6 s radio restore. It now releases it as soon as the screen is back (other operation locks stay). Reborn retries a busy output for 2 s (100–250 ms steps) inside the 5-s open deadline and names the holder (holders: PCM owner, lease holders) | Linux 6053d9c, Reborn ef1acbc |
| F25: Bluetooth playback refused "codec outcome unknown" until a restart | The uncertain-codec marker records PCM, device and address and clears once the headphones disconnect, reconnect (new PCM sequence) or BlueALSA restarts, only while nobody holds the PCM; plain wording | Reborn ef1acbc |
| F26: one kernel WARN disabled sleep (and deep idle) for the boot | A WARN-only taint (512) is allowed; every other taint bit still refuses | Linux 6053d9c |
| F27: WARN _cfg80211_unregister_wdev when Wi-Fi powers down while connected | wlanRemove reports a live link gone before unregistering | Linux 6053d9c, 9cd6e8b |
| F28: Pair refused while the reconnect daemon pages | Pair busy-retries and posts connect_pending like Connect | Reborn ef1acbc |
| F29: quick Next logged every queued track as unreadable | The pre-open stops on cancellation without logging | Reborn ef1acbc |
| F30: per-frame scanout lines filled 27–99 % of the system log | Logged once per layout or when the address did not land | Linux 6053d9c (overlay 0014) |
| F31: Wi-Fi failure evidence lost at the next connect | wifi-failure.json keeps wpa_supplicant's reason code and a last_failure block | Linux 6053d9c |
| F32 (user message, 8.17): "Downloading Update… Keep Wi-Fi on." for a day, Wi-Fi toggles and restarts no help | A download writes a durable Staging record first; a download that dies without its handler left it, the page had neither Cancel nor Check for Updates, and a failed background check wrote it back. A Staging/Checking record without a live stage-lock holder now reads as download_interrupted ("Update Didn't Finish", Check for Updates); a failed check never restores it | Linux f977ab5 |
| #52/#54 on 8.21: the crystal still failed (#52: XTAL_ERR at 9 track starts while skipping, then silence; after a restart never ready and PLL_READY -110 — the PLL needs the crystal, so it was not oscillating; #54: never ready, silence) | Stock RE (kernel, system.img HAL, GPIO dumps): XTI is a 22.5792 MHz crystal on every Y2 (stock: "22.5792M XTAL input"; MT6582 has no audio PLL, no clock output toward the codec). Stock starts the crystal at probe/screen-on and keeps it until screen-off while idle, never reads its flags, never switches the clock source. Now: the crystal starts at probe, the codec keeps power two idle minutes (was 5 s), the running clock source stays selected between streams (RCO only at runtime suspend; a source that does not fit is left via RCO before set_pll), the ready flag is read every 20 ms (was 1 ms), y2_hp/xtal gains ready_ms. The amplifier still power-cycles at every stream (DPCM stops the back end at the front end's close; a power-down delay does not apply) | Linux c6970db…073aa0c (overlay 0030, tests/test_codec_clock.py, tests/test_suspend_audio.py) |
| #53: no way to set the clock | Settings → Display → Date & Time (year, month, day, time; 12/24 h as the zone), y2-platform time-set: range-checked, never TLS-trusted, kept durably (next boot starts from it, labelled manual), saved hourly and at shutdown. Refused while this boot's clock is network time (the page then shows the clock only); a running time server is restarted after a manual set | Linux bdd171a, a98df07, 18ccf60; Reborn e9a5295, e196033 |

## Device results (owner's player, test builds 8600–8603)``````````````````````````````````````

| Check | Result |
| --- | --- |
| OTA 8500→8600, then 8601 … 8607 | each Acknowledged on health boot 1 (install ≈17 s) |
| F23 health evidence (8603 path) | /data/updates/health/<time>-boot1-previous-boot.txt: battery, boot_reason=4, data check clean, boot-check record, the recovery boot's trail (init initramfs/recovery/recovery_install) and console (reboot: Restarting system); after confirmation printk 3 4 1 7, panic 0, panic_on_rcu_stall 0 |
| pmsg trail of a normal boot (software restart) | next boot read every init stage, all 24 rcS scripts with times, platform_start … shutdown_complete |
| F30 | 1 scanout line per boot (was ≈9 per second) |
| F32 | a Staging record without a download → Failed / download_interrupted; original record restored afterwards |
| #53 | set +2 h before network time: applied, manual, not TLS-ready, durable; out of range refused (date_out_of_range); with network time refused (network_time_active); a fresh ntpd stepped back to network time within 21 s; shutdown saved the clock |
| F27 | Wi-Fi off while Online and on again: no WARN, taint 0, Online after 12 s |
| Playback regression | 12/12 (cold start, 50 quick Next/Previous, pauses, 48/96 kHz incl. from a powered-down codec), y2_hp/xtal ready every power-up |
| F29 | 0 next_track_open_failed after 50 quick skips |
| #52/#54 lifecycle (8607) | crystal on at boot (PWDN_CTL=f6 before any Play), 15/15 playback steps incl. 100 Next/Previous 0.3 s apart and 10 alternating 48/44.1 kHz opens, crystal source kept between streams (SYS_CLK_CTL_1=04 after a stop), codec down 145 s after a stop, cold start ready in 10 ms (ready_ms=10) |

Found and fixed on the player during this release (why the sequence is 8607): build 8604 kept a PLL selected while `set_pll` stopped it (48 → 44.1 kHz: the codec's control port NACKed until a restart); the initramfs links few BusyBox applets (`date`, `head`, `ls`, `sort`, `rm` went missing: empty file name, empty trail), printk's tab-separated levels made the saved settings unreadable JSON (not restored after confirmation), and a running busybox ntpd did not step a 2-h manual jump for minutes while its callbacks relabelled the clock as network time.

## Open
  - Not checked on a player: F24 after a real sleep (product sleep refuses with USB attached, SSH needs USB), F25, F26,

F28 and F31 in their failure cases (host tests only), the Date & Time page by hand (preview renders only).
  - F23's cause stays open: the next failing health boot's file names where it stopped. The recovery display change is

a candidate, not a proven fix.
  - #52/#54: confirmation from the reporters (`y2_hp/xtal``ready_ms`, `errors`, `unconfirmed`); if 8.22 still fails, a test build with stock's exact power-up (PLL/CLKOUT on, rails in one burst) is next; car AVRCP metadata, long-book seek, #42, #45, #47 unchanged.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
