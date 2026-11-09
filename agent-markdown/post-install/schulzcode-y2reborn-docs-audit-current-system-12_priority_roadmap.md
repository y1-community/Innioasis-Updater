---
title: "Proposed correction sequence — no implementation authorization - Innioasis Updater"
description: "Proposed correction sequence — no implementation authorization <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-12_priority_roadmap.html"
---

# Proposed correction sequence — no implementation authorization - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Proposed correction sequence — no implementation authorization

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Proposed correction sequence — no implementation authorization > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

This is the audit's proposed order, not a newly activated implementation milestone. Before activating/closing/crossing a major boundary or expanding hardware/memory/production scope, repeat the [standing roadmap/gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) with real evidence and update the authoritative roadmap. Owner selection is required after this audit. Do not infer permission to flash, change charging, reclaim memory or enable S32 from this list.

## P0 — must fix before continuing feature work

Keep this group small: five correctness contracts, with regression tests at their actual failure boundaries.
  - Native media lifetime (F01). Close the AVFrame ownership defect and audit adjacent error paths. Exit: allocator-aware repeated decode/seek/transition tests show bounded live allocations; current codec fixtures still pass. Do not rebuild the media architecture.
  - Single audio sink lifecycle (F02). Make planning/reconfiguration consistent with the audio worker's exclusive handle ownership; define failure rollback. Exit: realistic exclusive-sink tests for active volume/seek/skip/RG/output changes, followed by targeted wired behavior. Preserve direct hardware format authority.
  - One queue/entry contract (F03/F08). Stable queue-entry identity, live edit propagation, repeat-one and collection playback semantics. Exit: runtime-driven tests for duplicates, reorder/remove/insert, transition races and album-only play, not only reducer tests.
  - Crossfade delivery and fallback (F04). The offered durations must meet the sink's real block contract and preserve next-track samples on error. Exit: all offered durations, short tracks, mixed source rates, cancellation and mix failure exercised with bounded output chunks. The owner may instead choose to keep crossfade explicitly unavailable until ready.
  - Scan completion equals successful persistence (F05). Surface batch failures and prevent deletion/pruning after incomplete or uncommitted scans. Exit: injected transaction failures/ENOSPC/source loss preserve old records and report failure accurately.

In parallel as a decision gate, narrow unsupported capability claims and freeze hardware-scope expansion. Current charging and suspend uncertainty must remain explicit. This does not authorize hardware experiments as part of P0 software fixes.

## P1 — must fix before public testing

Group these into four acceptance packages rather than many independent feature tickets:

### A. Trustworthy basic player

Resolve seek-to-sample/RG/headroom semantics and strengthen gapless tests (F11/F12); explicitly define the supported format/precision subset (F09/F10). Physical exit: current image plays/pauses/seeks/skips/changes volume without unintended restarts/errors, screen-off audio remains stable, and a meaningful long-session run shows bounded memory and no unexplained XRUNs. High-resolution hardware expansion is not required for a truthful S16 alpha.

### B. Durable data and truthful interaction

Bound/dirty-check session writes and make failed restores visible (F06); provide corrupt-DB recovery (F07); handle SD/full-volume errors (F26); fix delayed-input/action/context mismatches that affect ordinary use (F20/F21/F24). Exit: full filesystem, source removal and interrupted writes have defined outcomes; queue/library/state survive or recover without silent success. Preserve atomic replacement and the single DB writer.

### C. Safe platform envelope

Reconcile current charger policy with current-image, independent voltage/current/temperature and pack evidence; define low-battery and connected-poweroff behavior (F16). Close GPU02/suspend regression if deep sleep is offered (F17/F22). Exit: the owner-approved physical procedure demonstrates the narrowly promised envelope. If deep suspend remains unqualified, exclude it explicitly rather than claiming it works from an older milestone.

### D. Releasable artifact and evidence

Clean-machine paired-source/cache recipe, embedded identity for reused payloads, corrected manifest/application contract, independent install/preserve-data/recovery exercise, rights/source/notices bundle, and version-bound validation index (F13–F15/F27/F31). Exit: another maintainer can build the intended pair and follow the release instructions without private undocumented steps. Owner firmware must have a lawful provision/distribution route.

If Wi-Fi/Bluetooth are included in the public feature set, association/IP/DNS and fresh pairing/SBC/reconnect/coexistence are also P1 (F18/F19). Otherwise label them experimental/off and defer their broader claims; adapter scanning is not sufficient acceptance.

## P2 — should fix before stable release
  - Establish the real 10k/20k library performance envelope and query-backed pagination/identity as needed (F23).
  - Complete metadata/glyph coverage, album identity, navigation restoration and artwork invalidation appropriate to a music product (F21/F24).
  - Correct diagnostic metric/status semantics and refine idle wakeups based on target measurements (F25/F28).
  - Finish supported storage/network/peer interoperability and scoped recovery; add exFAT/open-network/AVRCP/EQ configuration only where selected for the product contract (F09/F12/F18/F19/F26).
  - Qualify repeated renderer/device/service recovery and long-term PM behavior, not only clean boots (F17/F22/F29).
  - Plan native high-resolution output as a separate hardware/audio milestone only if still selected, with explicit AFE/clock/codec/electrical acceptance (F10). It is not a JSON/profile toggle.

## P3 — nice cleanup / future

Label/de-duplicate obsolete reference assets and old capability summaries (F30); improve dense local code when already changing its behavior; evaluate rendering batching/extra caching only if measurements justify it. Optional Bluetooth codecs, a new UI design, signed remote updates/A-B rollback, more elaborate DSP and aggressive DVFS are future scope decisions, not implicit stabilization work.

## Sequence and stop criteria`owner chooses scope / reconcile evidence and claims -> P0 playback + queue + lifetime + DB correctness contracts -> current-source targeted host/native integration tests -> P1 persistence/input + narrow real-device player/power qualification -> clean paired build + public installation/recovery/legal closure -> scoped alpha -> measured scale/interoperability/endurance -> beta/stable decision`

Do not use a large passing regression count to skip a failed targeted test. Retain the failing fixture/physical observation and resolve or explicitly remove the affected capability from the release contract. Do not update milestone status merely because a correction was committed or an image built.

## Leave-alone guardrail

Keep stock bootloader/protected storage policy, strict rescue selection, standard subsystem ownership, existing memory reservations, Linux/Buildroot integration, shared FFmpeg engine, SQLite single-writer design, semantic input boundary, UI service separation, atomic file-write primitive and bounded diagnostics stable. The target is a smaller set of reliable contracts around those foundations—not another broad rewrite.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
