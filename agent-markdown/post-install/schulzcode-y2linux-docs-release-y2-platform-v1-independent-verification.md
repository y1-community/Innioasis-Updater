---
title: "Independent Platform 1.0 integration verification - Innioasis Updater"
description: "Independent Platform 1.0 integration verification Scope: source composition, production configuration, fresh software/package evidence and release handoff. No new feature"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-platform-v1-independent-verification.html"
---

# Independent Platform 1.0 integration verification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Independent Platform 1.0 integration verification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Independent Platform 1.0 integration verification

Scope: source composition, production configuration, fresh software/package evidence and release handoff. No new feature audit or device campaign. The twelve-session Git ledger enumerates every changed path and distinguishes exact owner bytes from semantic adapters. Main and original worktrees remain untouched.````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| Concern | Independent source finding | Evidence path(s) |
| --- | --- | --- |
| C01 | One EventMonitor.select includes SignalWake pipe; no competing waits. | tools/platform/y2_platform/service.py, tools/platform/y2_platform/network.py, tests/test_platform_integration.py |
| C02 | One DB TEMP scan_seen/scan_candidates and scan-token protocol; one sd_id_matches_uuid helper. | R:crates/reborn-library/src/lib.rs, R:crates/reborn-library/src/platform_tests.rs |
| C03 | One limits-aware embedded/external artwork decode wrapper and checked reduced JPEG header/receive path. | R:crates/reborn-media/native/media.c, R:crates/reborn-media/src/native.rs |
| C04 | Input queues close/reopen completely; typed Cancel, monotonic provenance and wake-edge suppression composed. | R:crates/reborn-platform/src/input.rs, R:crates/reborn-platform/src/input.rs |
| C05 | App Runtime/AppState and main loop own catalog/scanner/frame/sleep changes; workers return bounded results. | R:app/reborn/src/main.rs, R:app/reborn/src/background.rs, R:app/reborn/tests/architecture_guard.rs |
| C06 | One status schema unions USB, diskseq, Wi-Fi observations and audio PCM truth. | tools/platform/y2_platform/observe.py, R:crates/reborn-platform/src/client.rs, tests/test_platform_integration.py |
| C07 | Linux sole mount owner; SD claim/root release occurs before eject; durable completed refresh is coalesced. | tools/platform/y2_platform/media.py, tools/platform/y2_platform/usb.py, R:crates/reborn-platform/src/storage.rs, tests/test_usb_product.py |
| C08 | Reviewed fixed diagnostic field union preserves useful observations without private free text. | tools/platform/y2_platform/diagnostic_fields.py, tools/platform/y2_platform/diagnostics.py, tests/test_diagnostic_export.py |
| C09 | C/Rust metadata and limits structures ship from one paired media source; software rounding independent of native admission. | R:crates/reborn-media/native/media.c, R:crates/reborn-media/src/native.rs, tests/test_audio_precision_contract.py |
| C10 | Pinned patch digests and effective kernel/Buildroot configs are freshly validated. | kernel/patches/manifest.json, kernel/config/production.config, buildroot/configs/y2_production_defconfig, tests/test_overlays.py, tests/test_release_composition.py |
| C11 | Typed Ready/Copying/Developer and sleep lifecycle remain additive; legacy restoring parses conservatively. | R:crates/reborn-core/src/platform.rs, R:crates/reborn-platform/src/client.rs, R:crates/reborn-ui/src/pages.rs, R:crates/reborn-ui/src/tests.rs |
| C12 | Historical admissions retained; new final audit and roadmap precede release boundary; current seal has explicit precedence. | docs/planning/roadmap-gap-audit.md, docs/planning/platform-v1-roadmap.md |
| C13 | Sixteen foundation files and three protected functions directly match physically proven UART01; full suspend is separately guarded. | kernel/platform/spm.c, kernel/platform/idle.c, kernel/platform/spm-idle-policy.h, tests/test_cpu_c3_uart.py, tests/test_suspend_policy.py |
| C14 | kernel_mono_us is the only canonical input timing field; successful CLOCK_MONOTONIC selection required. | R:crates/reborn-platform/src/input.rs, R:app/reborn/src/performance.rs, R:crates/reborn-platform/src/input.rs |
| C15 | Bluetooth owner event worker retained byte-identically; weaker performance polling hunk omitted. | R:crates/reborn-platform/src/bluetooth.rs, R:crates/reborn-platform/src/bluetooth.rs |
| C16 | One baseline release/root/kernel identity; configfs MTP/Developer both preserve ECM observer. | tools/production/release.json, kernel/config/production.config, tools/platform/y2_platform/usb.py, tests/test_release_composition.py |
| C17 | No queued USB generation starts a scan after sleep ACK; pending work waits for restoration. | R:app/reborn/src/main.rs, R:app/reborn/src/background.rs, R:app/reborn/tests/architecture_guard.rs |
| C18 | Boolean bonded exception is type-restricted; USB/sleep enums and Wi-Fi observations project safely; bond secrets still redacted. | tools/platform/y2_platform/diagnostic_fields.py, tools/platform/y2_platform/diagnostics.py, tests/test_diagnostic_export.py |
| C19 | UUID-only old queues stay unavailable; rescan creates CID-qualified online source; legacy offline IDs/catalog capacity preserved. | R:crates/reborn-library/src/lib.rs, R:crates/reborn-platform/src/storage.rs, R:crates/reborn-library/src/platform_tests.rs |
| C20 | Newer Baseline02 installed receipt supersedes older USB installed label; UART01 remains physical CPU/fallback authority. | docs/release/Y2-PLATFORM-V1-INTEGRATION-STATUS.md |
| C21 | Ordered adjacent-texture batching/staging bytes match performance owner; no new render worker or capture default. | R:crates/reborn-graphics/native/graphics.c, R:crates/reborn-graphics/src/native.rs, R:app/reborn/tests/architecture_guard.rs |
| C22 | Exact pinned FFmpeg 9.0.2 paired headers/libraries rebuilt and checked; no inherited device-version claim. | R:FFMPEG_VERSION, tools/production/verify-ffmpeg.py, tools/production/check_installed_arm.py |
| C23 | MTP ARM UAPI generated from pinned Linux 6.18; fresh responder builds with confinement intact. | buildroot/package/y2-mtp/y2-mtp.mk, tools/usb/mtp-safe.c, tests/usb_mtp_fs.c, tests/usb_mtp_protocol.c |
| C24 | Schema/user_version 1 preserved; additive metadata_revision=0 migration and revision 2 reuse policy compose into TEMP scanner. | R:crates/reborn-library/src/lib.rs, R:crates/reborn-library/src/platform_tests.rs |
| C25 | Capacity-one background observations validate source freshness and quiesce before ACK; UI owns result mutations. | R:app/reborn/src/background.rs, R:app/reborn/src/main.rs, R:app/reborn/tests/architecture_guard.rs |
| C26 | Playback current/queued/gapless and sidecars use no-follow live file/parent pins, local custom AVIO and post-open/source checks. | R:app/reborn/src/playback.rs, R:crates/reborn-platform/src/storage.rs, R:crates/reborn-media/native/media.c, R:crates/reborn-platform/src/storage.rs |
| C27 | Four-cover cache evicts only upon successful cacheable insert; failed/sidecar-only work cannot evict useful embedded pixels. | R:app/reborn/src/artwork.rs, R:app/reborn/src/artwork.rs |
| C28 | Codec refusal rollback/regcache replay and retained substeps are present; actual old RTC inner stall remains UNKNOWN. | kernel/patches/0030-cs43130-system-pm.patch, kernel/platform/pm-journal.c, tests/test_suspend_audio.py, tests/test_platform_v1_suspend.py |
| C29 | Wired WritePacing bytes match reviewed owner; bounded wait follows control poll; accepted prefix/BT behavior and precision unchanged. | R:crates/reborn-audio/src/native.rs, R:tools/qualification/reborn-audio-write-profile.c |
| C30 | Collection artwork admission pins live source during decode; immutable cache evidence owns no FD; publication rechecks lifetime. | R:app/reborn/src/artwork.rs, R:crates/reborn-platform/src/storage.rs, R:app/reborn/src/artwork.rs |
| C31 | Package audio metadata separates implemented software S16/S24/S32 from enabled native S16 and unqualified hardware. | tools/production/system_update.py, tools/host/audio_precision.py, tests/test_release_composition.py |
| C32 | MTP delivery requires kernel/configfs/FunctionFS/ECM plus Buildroot package/responder/sole USB policy. | tools/production/composition.py, tests/test_release_composition.py |
| C33 | Buildroot Reborn version queries canonical workspace 0.2.0; source commit recorded independently. | buildroot/package/reborn/reborn.mk, tools/production/application.py, tests/test_release_composition.py |
| C34 | Minimal GIO/ALSA/filesystem skips retained explicitly; every skipped test is rerun unchanged on native host. | tests/test_platform_bluetooth.py, tools/production/tests.sh, tests/native/bt-reconnect-events.c, tests/native/bt-observe-json.c |

All 34 concerns are reconciled in source; their physical gates remain open. Fresh commands/counts and the final source pair are recorded in the baseline. The verifier found no runtime integration defect requiring new hardware behavior. The old telemetry timeout assertion and release handoff were corrected; no assertion of readiness/failure meaning was removed.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
