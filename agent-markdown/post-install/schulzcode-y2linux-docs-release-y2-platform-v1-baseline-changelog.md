---
title: "Platform 1.0 baseline — human engineering changelog - Innioasis Updater"
description: "Platform 1.0 baseline — human engineering changelog The work produced concrete fixes, bounded optimizations and safer contracts. It did not establish integrated hardware"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-platform-v1-baseline-changelog.html"
---

# Platform 1.0 baseline — human engineering changelog - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform 1.0 baseline — human engineering changelog

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform 1.0 baseline — human engineering changelog

The work produced concrete fixes, bounded optimizations and safer contracts. It did not establish integrated hardware acceptance. Historical measurements below belong to the exact subsystem binaries and images listed in [the twelve-session ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-FINAL-SESSION-RESULTS.md).

## 1. Bluetooth

BEFORE: Periodic reconnect/observation work and unreliable discovery fields.

WHAT THE PARALLEL SESSION FOUND: Off/disconnected evidence did not test a real headset; observer owner changes were ambiguous.

WHAT CHANGED: Event/deadline waits, bounded reconnect intents, restart/PCM generation handling and fixed JSON.

RESULT: Less idle polling; hardened codec/peer observation.

WHAT STILL NEEDS HARDWARE TESTING: Real headset/codec/reconnect/coexistence and endurance.

## 2. Wi-Fi

BEFORE: Slow real STATUS replies could appear disconnected; repeated signal queries.

WHAT THE PARALLEL SESSION FOUND: Replies took 1.48–2.08 seconds; stale readiness/DNS and duplicate cleanup could survive epochs.

WHAT CHANGED: Bounded three-second STATUS, freshness-bound readiness/RSSI, shared service wake and DNS scheduling.

RESULT: Bug fixes and bounded repeated work; no new throughput/power claim.

WHAT STILL NEEDS HARDWARE TESTING: AP loss, changed-policy cold boot, radio coexistence and unresolved TX iperf reset.

## 3. FFmpeg / metadata

BEFORE: Metadata/artwork inspection could do unnecessary decoder work and reuse stale extraction.

WHAT THE PARALLEL SESSION FOUND: Malformed/huge artwork, duplicate parsing and sidecar-only opens needed explicit bounds.

WHAT CHANGED: Demux-only bounded inspection, metadata ABI/revision 2, cancellable local I/O and one DB scanner.

RESULT: Safer ingestion and faster owner host scan; exact FFmpeg remains 9.0.2.

WHAT STILL NEEDS HARDWARE TESTING: Integrated formats, tags/artwork edits, removal/cancellation and whole-app scans.

## 4. High-resolution audio

BEFORE: Software narrowing and generic container reporting could mislead about precision.

WHAT THE PARALLEL SESSION FOUND: Native intersection only admitted S16 stereo 44.1/48 kHz; wider hardware was unproved.

WHAT CHANGED: Correct final ties-even narrowing and separate source/DSP/container/meaningful/sink diagnostics.

RESULT: Software precision bug fixed; justified preservation of native S16.

WHAT STILL NEEDS HARDWARE TESTING: Actual low bits/I2S clocks and analog output before admitting wider modes/rates.

## 5. USB / desktop transfer

BEFORE: A coherent consumer transfer product and safe mount ownership were incomplete.

WHAT THE PARALLEL SESSION FOUND: MTP needed confinement, durable refresh, hotplug/release handling and real ARM UAPI.

WHAT CHANGED: Configfs MTP plus ECM; Developer ACM/ECM; Linux-only mounts, no raw MSC, pinned responder and PIO progress repair.

RESULT: Significant safe transfer implementation; desktop acceptance remains open.

WHAT STILL NEEDS HARDWARE TESTING: Actual desktop large/small files, reconnect/hash integrity, SD release and host matrix.

## 6. Full-system suspend

BEFORE: Staged PM existed but full same-boot restore was not established.

WHAT THE PARALLEL SESSION FOUND: Baseline02 RTC watchdog-rebooted in device resume; precise CS43131 internal stall unknown.

WHAT CHANGED: Checked restores/quarantine, codec refusal rollback/substeps, acknowledged worker/player/UI quiescence and wake input reset.

RESULT: Hardening and observability; RTC failure not proved fixed.

WHAT STILL NEEDS HARDWARE TESTING: Power and RTC separately, staged PM first, complete restored same boot and repeated acceptance.

## 7. Storage / filesystems

BEFORE: Path/UUID-only identity could accept a replacement card or symlinked file.

WHAT THE PARALLEL SESSION FOUND: Live block lifetime, mount claims and playback/artwork pins needed a single ownership model.

WHAT CHANGED: diskseq live claims, CID-qualified persistent IDs, no-follow file/parent pins, FAT UTF-8 and bounded diagnostics.

RESULT: Source replacement/hotplug hazards hardened; measured speed modes preserved.

WHAT STILL NEEDS HARDWARE TESTING: Different card/cloned UUID, absent boot, existing FAT/exFAT, hotplug and endurance.

## 8. Reborn performance

BEFORE: Static redraw, UI-thread observations and ALSA partial-write busy work wasted CPU.

WHAT THE PARALLEL SESSION FOUND: Exact temporary ARM comparison isolated rendering and audio pacing costs.

WHAT CHANGED: Visible-state frames, descriptor waits, ordered texture batches, existing-watchdog observations, correct cache eviction and readiness pacing.

RESULT: Owner app playing CPU 87.95→11.21%; static Home 14→0 frames/10 seconds; source integrated, measurements historical.

WHAT STILL NEEDS HARDWARE TESTING: Exact baseline latency/listening/XRUNs, startup tradeoffs and normal whole-app workloads.

## 9. GPU / display / graphics

BEFORE: Full-size JPEG decoding cost memory/CPU despite small cover output.

WHAT THE PARALLEL SESSION FOUND: Working display/runtime PM needed preservation; measured JPEG reduction was useful.

WHAT CHANGED: Checked reduced JPEG decode in one bounded media wrapper; existing GPU/scanout architecture retained.

RESULT: Owner temporary ARM median 492.637→75.332 ms and RSS 29,920→9,320 KiB.

WHAT STILL NEEDS HARDWARE TESTING: Integrated GPU/display off/wake, blend/order/pixels and full-resume; no electrical claim.

## 10. SQLite / library DB

BEFORE: Scan-wide maps, row rewrites and full catalog reloads scaled poorly.

WHAT THE PARALLEL SESSION FOUND: No-op scans and removable-source cancellation needed TEMP/token ownership and bounded paging.

WHAT CHANGED: DB TEMP seen/candidate sets, conditional writes, 512-row pages and composed extractor migration.

RESULT: Owner native 50k catalog 8641.27→999.53 ms, unchanged scan 25471.03→3845.16 ms; ingest/prune tradeoffs retained.

WHAT STILL NEEDS HARDWARE TESTING: Whole app and endurance; 250k is a ceiling, not measured capacity; actual flash I/O unavailable.

## 11. Input / wheel

BEFORE: Backlog/clock/rebind and held-key recovery could create wrong actions.

WHAT THE PARALLEL SESSION FOUND: The physical capture had zero events and the changed app never executed.

WHAT CHANGED: Monotonic provenance, stable identity, bounded reads, typed cancellation and one duplicate/acceleration owner.

RESULT: Timing/recovery bugs fixed in source; canonical Power routing composed.

WHAT STILL NEEDS HARDWARE TESTING: Counted mechanical detents/buttons, hold exclusivity, wake gesture and real latency.

## 12. Master integration

BEFORE: Eleven overlapping source pairs could not be assembled by blind merges.

WHAT THE PARALLEL SESSION FOUND: 34 concerns crossed scanner, waits, clocks, caches, USB/storage, ABI, privacy and sleep boundaries.

WHAT CHANGED: Composed selected work, rejected weaker/duplicate implementations and built one paired candidate.

RESULT: 324 Rust cases and a sealed software candidate; independent baseline rebuild supersedes its handoff.

WHAT STILL NEEDS HARDWARE TESTING: Every integrated acceptance area remains NOT_RUN; historical subsystem results keep their own identities.

The independent final verifier adds the baseline version identity, a smoke-first handoff, separate Power/RTC selection, and reconciliation of an old telemetry test with the accepted three-second Wi-Fi timeout. No new hardware capability or runtime C3 policy is enabled by finalization.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
