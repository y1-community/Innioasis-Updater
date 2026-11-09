---
title: "Release readiness and missing functionality - Innioasis Updater"
description: "Release readiness and missing functionality <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-10_release_gaps.html"
---

# Release readiness and missing functionality - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Release readiness and missing functionality

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Release readiness and missing functionality > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## Release envelope, not a binary verdict

The present image is appropriate for controlled owner/developer investigation with known recovery. It is not yet a credible public beta or stable release. A public alpha can be deliberately narrow—wired S16/44.1, supported SD formats and manual updates—provided normal controls/data safety work and excluded features are honestly described. Optional feature exclusion cannot waive charging or install safety.

| Dimension | CURRENT | Minimum credible public alpha | GAP / finding |
| --- | --- | --- | --- |
| Installation | Owner-specific images/scatters and validation | Explicit supported hardware, first-install vs preserve-data instructions, independent successful installation | Wrong-profile data loss, incomplete paired artifact provenance; F13/F14/F31 |
| Recovery | Strong RAM rescue/stock-preservation architecture | Operator-tested recovery from bad root/boot/update without protected-data writes | Public workflow/evidence, not a demand for A/B; F31 |
| Stability | Bounded workers/supervision, short host tests | Long-session memory/XRUN stability and controlled failure behavior | Native leak, lifecycle/state faults; F01–F05 |
| Audio | Working narrow hardware baseline, shared FFmpeg engine | Reliable wired play/volume/seek/skip/pause with truthful precision and supported formats | F02/F04/F09–F12; high-resolution expansion can be excluded |
| Library | SQLite, incremental scanning and sources | Correct collections, commit-aware scans, recoverable errors | F05/F07/F08; disclose tested size ceiling F23 |
| UI | Hardware renderer and good presentation boundary | Truthful values, usable focus/navigation and physical legibility | F21/F22; no aesthetic redesign required |
| Controls | Semantic device-aware input | No delayed-input long/short misclassification; reliable global controls | F02/F20 |
| Connectivity | Scans/adapters plus unqualified connection/audio paths | Qualify WPA2/SBC if offered, or explicitly experimental/off | F18/F19; optional codecs not required |
| Power | Charging/offline/suspend mechanisms | Current safe operating envelope, low-battery plan, verified poweroff; qualify sleep if enabled | F16/F17; cannot be waived by UI polish |
| Persistence | Atomic session replacement, WAL DB | Bounded dirty checkpoints, visible restore failures, corrupt/full-volume recovery | F05–F07/F26 |
| Diagnostics | Useful bounded local infrastructure | Correct states/counters, reproducible private/public evidence recipe | F25/F27/F32 |
| Licensing | Owner-local source notice and provisioned firmware | Actual binary/source/license/asset rights package | F15 |
| Documentation | Extensive historical knowledge | One current capability/evidence/install contract naming exact source pair | F14/F27/F30 |

## Missing ENTIRELY, distinguished from weak or unproven

“Missing” below is scoped to the named production behavior. It does not mean all adjacent infrastructure is absent. Conceptual complexity is small/medium/large, not an estimate of hours. No implementation is authorized.

| Missing behavior | Why it matters | Release importance | Dependency | Conceptual complexity |
| --- | --- | --- | --- | --- |
| Wired S32/high-rate AFE output and complete clock/format support | Needed for genuine preserved 24-bit/native-high-rate claims | Required only for that promised feature; not a truthful S16 alpha prerequisite | Hardware format/clock evidence, ASoC changes, qualification | Large |
| User-operable EQ band/preset configuration | Current toggle with empty default bands can do nothing | Implement a minimal truthful feature or withhold/label control before advertising EQ | Existing FFmpeg EQ path, settings/action design | Medium |
| Reborn AVRCP player/control/metadata service | Headset transport controls do not automatically drive AppModel | Required if remote playback controls are promised | BlueZ Media API, semantic action integration, peer tests | Medium |
| Normal-runtime graceful low-battery shutdown policy | Protects session/DB and defines behavior before hardware cutoff | Power/product release requirement | Reliable battery-voltage/pack evidence and shutdown sequencing | Medium |
| Calibrated battery-cell temperature/current/SOC reporting | Needed for accurate battery display and a defensible charge envelope | Measurement/pack protection is safety-relevant; percentage display itself optional | Actual sensor/pack topology and calibration, not guessed values | Large |
| Corrupt-library quarantine/rebuild/restore workflow | Current startup can repeatedly fail on the same DB | Before public testing | DB worker and startup/error UI; preserve source music and evidence | Medium |
| exFAT in supported SD path | Many large cards arrive in that format | Can explicitly exclude from alpha; important broader compatibility | Kernel/userspace filesystem policy and media tests | Medium |
| Open-network connection in Reborn's connect path | Displayed open APs cannot use current WPA-PSK-only function | Can explicitly limit alpha to WPA2 personal | Connection type in action/service contract | Small |
| Correct full Unicode glyph/rendering path | Real music metadata is not restricted to the current small atlas | Stable product quality; documented alpha limitation possible | Font asset pipeline/lookup, bounded glyph strategy and tests | Medium |
| Browse beyond first 20k loaded records | Larger collections otherwise remain invisible | Required for a 20k+ claim, not a narrower tested alpha | Query-backed pagination and stable selection/queue IDs | Medium |
| Public third-party compliance/firmware/asset permission package | Source accessibility and owner extraction are not redistribution rights | Public release blocker | Exact image inventory, legal-info review, rights/source/notices decision | Medium, with external permission uncertainty |
| Atomic A/B update/automatic rollback | Reduces interrupted-update recovery burden | Not necessary for explicitly manual alpha; decision for later update scope | Storage/boot architecture and hardware authorization | Large |

Not in this table: Wi-Fi association machinery, Bluetooth audio routing, gapless, crossfade, ReplayGain, SQLite persistence and rescue exist. They are partial/weak/unqualified, not entirely missing. Pack temperature measurement being missing does not prove there is no hardware pack protection; that physical fact is UNKNOWN. Signed OTA is not silently made a required new feature here.

## Physical questions that cannot be answered from a host

The audit cannot establish actual current charging current/pack temperature, low-battery shutdown/cutoff behavior, connected poweroff, same-boot deep wake, real current-image DAC output format/electrical quality, pop/click behavior over repeated transitions, RF association/throughput, remote SBC quality/reconnect, coexistence or battery endurance. Historical observations are retained as evidence, not erased; they do not cover every current change.

Likewise, host maximum RSS is not Y2 RAM; GPU checker CPU is not Reborn CPU. Before claiming an embedded performance envelope, record idle, static UI, navigation, 16/44 playback, 24/96 source downsampling, EQ, scanner/artwork and SBC workloads with exact source/image and temperature/power conditions.

## Stable-release delta beyond alpha

Stable means defined and tested media/error behavior, bounded long-run resources, resilient persistence and recovery, accessible/accurate metadata presentation, a supported library-size envelope, measured battery behavior, and a maintainable release recipe. It does not automatically mean every optional Bluetooth codec, streaming service, touchscreen-style UI or OTA infrastructure. Resolve the success-determining integration defects before expanding that scope.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
