---
title: "Executive assessment - Innioasis Updater"
description: "Executive assessment <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-01_executive_summary.html"
---

# Executive assessment - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Executive assessment

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Executive assessment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Keep the architecture; stabilize its integration contracts. This is a substantial working embedded-platform foundation with a credible application skeleton, not a production-ready music player. The largest problems are specific lifecycle/state/data-integrity defects and unclosed physical qualification—not a need for another framework, another UI rewrite, or more abstraction layers.

Assessment: platform layering is generally sound; application layering is promising but incompletely enforced; release engineering and validation are behind implementation. Overall PARTIAL / HIGH confidence. Public beta or stable claims would be premature. A tightly scoped owner/developer alpha becomes credible after the P0 correctness work and P1 installation, power, persistence and audio evidence gates.

## What is genuinely good

The boot path fails closed on unexpected storage identity, preserves a rescue environment, distinguishes data initialization from preserving updates, and limits production image targets. Native Linux subsystem use is real: DRM/KMS/Lima, ASoC/ALSA, evdev, cfg80211, HCI/BlueZ, power_supply/regulator/thermal interfaces. These are valuable foundations to retain.

Reborn has a shared FFmpeg processing path for wired and Bluetooth output, bounded channels, cancellation generations, a single SQLite worker, explicit semantic input, a largely hardware-free presentation layer, atomic session-file replacement, and bounded diagnostic infrastructure. These are inspected implementations, not merely architecture diagrams. See GOOD findings G01–G10 in the [master table](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F13_MASTER_FINDINGS.md).

## The small set of decisive problems
  - Playback lifecycle is not coherent.`Runtime::load` probes an exclusive ALSA device before stopping the existing sink; volume, seek and other normal controls call this path. Controls can fail with the old stream still alive, and successful changes rebuild playback. F02.
  - The visible queue is not the playing queue. A worker receives a copied queue, while subsequent UI edits mutate only the model. Repeat-one, duplicates and album selection also have concrete semantic defects. F03/F08.
  - The media boundary leaks an AVFrame allocation per decoded source frame. The caller never frees the moved-from frame shell. A cached-host repeated-decode probe supports the source finding; target growth is unmeasured. F01.
  - Every normal nonzero UI crossfade duration can exceed the real ALSA sink's block bound. The UI offers 5/10/15 seconds; overlap is emitted as one block, whereas a 44.1-kHz S16 block is limited to about 2.97 seconds. The 50-ms fake-sink test misses this. F04.
  - Persistence success is overstated. Scanner writes are not acknowledged before successful completion/pruning, corrupt DB recovery is absent, and the entire session/queue is synchronously rewritten every 15 seconds even when unchanged. F05/F06/F07.

These are fixable integration defects, not grounds for discarding Rust, FFmpeg, SQLite or the current UI boundary.

## Claims that must be narrowed now
  - Wired production output is S16_LE stereo at 44.1 kHz. The AFE exposes S16 at 44.1/48 kHz, and the release profile admits only 44.1 kHz. A 24/96 FLAC is decoded, processed and reduced to the qualified output. S32 hardware output and preserved 24-bit output are MISSING, not awaiting only a listening test. F10.
  - FFmpeg really is 9.0.1 in the inspected build; its selected codec set is sensible. But the scanner excludes AIFF, APE and WavPack, despite decoder fixtures. F09.
  - Gapless has meaningful sample-count/boundary evidence for two synthetic same-rate FLAC files. Universal sample-accurate lossy/mixed-rate/real-device gapless is UNKNOWN. F11.
  - Bluetooth audio codecs enabled in the inspected image build: SBC. AAC, aptX, aptX HD and LDAC are not enabled. Wi-Fi scanning and concurrent adapter power are physically evidenced; association/DHCP/DNS, pairing/A2DP and sustained coexistence are not. F18/F19.
  - Older owner power acceptance does not qualify current charger changes, cell-temperature behavior, unattended charging or same-boot deep suspend. GPU01 recorded a genuine CPU3 suspend blocker; a subsequent correction is not equivalent to successful physical resume. F16/F17.

## Biggest entirely missing pieces

There is no meaningful wired S32/high-rate AFE implementation, usable EQ band/preset configuration despite the toggle, Reborn AVRCP player/control integration, application-level low-battery shutdown policy, corrupt-library recovery workflow, or public redistribution/compliance bundle. exFAT is absent from the supported SD mounting path. Some are stable-release requirements; some can be explicitly excluded from a truthful alpha. See the missing-functionality matrix in [release gaps](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F10_RELEASE_GAPS.md); do not treat every absent feature as P0.

## Release decision

| Dimension | Current judgment |
| --- | --- |
| Installation/recovery | Strong owner tooling; public install/update instructions and artifact contract still weak. |
| Core audio/controls | Blocking lifecycle, queue, crossfade and memory defects. |
| Library/persistence | Useful baseline; failure handling and large-library behavior insufficient. |
| UI | Redesignable without replacing services, but several displayed/action semantics are wrong. |
| Connectivity | Native stack exists; peer/network qualification open. |
| Power | Conservative mechanisms exist; safety and current regression evidence incomplete. |
| Diagnostics | Useful and appropriately bounded; some counters/status claims need correction. |
| Licensing/reproducibility | Private owner build path is much stronger than public redistribution path. |

## Top 10 things already good—keep stable
  - Fail-closed root/data identity and rescue selection (G01).
  - Protected partition policy and preserve-data package concept (G02).
  - Standard Linux hardware subsystem ownership (G03).
  - Real Lima/GBM/EGL/GLES2/KMS rendering path (G04).
  - One FFmpeg decode/processing authority across outputs (G05).
  - Single SQLite writer with transactional batches and stable source/path IDs (G06).
  - Semantic physical-input boundary and power-only screen wake policy (G07).
  - Presentation/service separation and typed actions/effects (G08).
  - Atomic state-file replacement primitive (G09).
  - Bounded logs/control/diagnostics and private calibration handling (G10).

## Top 10 problems deserving the next development effort
  - Audio sink ownership and live control transitions (F02).
  - Queue identity, live mutation, repeat and collection playback (F03/F08).
  - Native media allocation lifetime (F01).
  - Crossfade delivery bounds and transition fault behavior (F04).
  - DB write acknowledgement, safe scan completion and corruption recovery (F05/F07).
  - Session checkpoint cadence, size and restore diagnostics (F06).
  - End-to-end audio correctness tests, seek/gapless/RG and physical baseline (F11/F12).
  - Current power/suspend safety and regression evidence (F16/F17).
  - Reproducible paired artifacts, truthful manifests and public install/legal package (F13/F14/F15).
  - Real Wi-Fi/Bluetooth use and reconnect/control integration (F18/F19).

This ordering is decision support, not approval to perform it. The [priority roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F12_PRIORITY_ROADMAP.md) gives exit criteria and explicit scope gates.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
