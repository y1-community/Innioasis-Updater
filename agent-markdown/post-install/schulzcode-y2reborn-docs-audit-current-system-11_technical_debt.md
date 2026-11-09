---
title: "Concrete technical debt and architectural drift - Innioasis Updater"
description: "Concrete technical debt and architectural drift <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-11_technical_debt.html"
---

# Concrete technical debt and architectural drift - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Concrete technical debt and architectural drift

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Concrete technical debt and architectural drift > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## Drift that materially affects behavior

| Area | Drift | Consequence | Appropriate correction scope |
| --- | --- | --- | --- |
| Queue | AppModel queue plus copied worker schedule without revision protocol | Display/edits/repeat diverge from actual playback | Entry identity + ownership/update contract; F03 |
| Audio lifecycle | UI/runtime probes real ALSA while audio worker owns it | EBUSY and restart-style controls | One serialized sink owner; F02 |
| Precision | Canonical FLTP description hides limiter DBL negotiation and transition S32 round trips | Misleading precision/cost claims | Trace/explicit format policy, retain FFmpeg authority; F10/F12 |
| Artwork | Next-decoder preparation publishes current-generation art | UI changes before audible track boundary | Track/entry identity on artwork events; F24 |
| Collection identity | UI filter reduced to global index; album identity reduced to label | Play Album enqueues library; same-title albums merge | Carry stable collection/queue intent; F08/F21 |
| Persistence | Whole model snapshot becomes a 15-second heartbeat | Idle flash writes and oversized restore failures | Dirty durable state with coherent bounds; F06 |
| Scanner | Enqueue/order barrier treated as successful commit | False completion/pruning after failed writes | Acknowledged scan transaction outcome; F05 |
| Release metadata | Old Y2PlayerNative “unimplemented” contract survives Reborn integration | Validator blesses obsolete facts | Current paired payload contract; F14 |
| Evidence | Historical baseline FFmpeg6/QEMU/font metadata presented beside FFmpeg9/current UI | Readers overestimate current qualification | Version-bound receipts and one current index; F27 |

Evidence/symbols for every row are in the corresponding detailed report and [master table](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F13_MASTER_FINDINGS.md). None requires splitting the repositories into unrelated products.

## Overengineering / opportunities to simplify
  - Do not build a second DSP engine. There is currently one FFmpeg authority; the improvement is fewer transition conversions and explicit negotiation, not a new Rust equalizer/resampler.
  - Full Track records are copied through views, queues and worker jobs. Use identity where it reduces measured cost and duplicated authority; do not add an ORM/cache hierarchy first.
  - Recomputing row collections/counts and serializing snapshots at fixed intervals does work without a state change. Remove needless repeated work before adding background threads to hide it.
  - Health/metrics/event-ring infrastructure is justified, but diagnostics should describe actual state rather than multiplying near-duplicate JSON projections. Correct cumulative packet accounting and failed-scan semantics before adding counters.
  - A general async runtime, event-sourced store, plugin layer or multi-process service bus has no demonstrated benefit for the current player. The bounded worker design is understandable and should remain.
  - The current font/icon bitmap approach is efficient for a fixed embedded UI. Improve character coverage/asset provenance without automatically introducing a full desktop text/UI stack.

## Underengineering
  - Native frame-shell ownership, long-overlap chunking and seek-to-sample behavior lack the tests their risk deserves.
  - A robust scan state machine was added for radios, but equivalent connect/IP/peer-audio and commit-success state is incomplete.
  - User-visible toggles/actions can exceed implementation: EQ without configurable bands; queue edits without worker updates; Rebuild Library without corrupt-DB recovery.
  - Storage/full-filesystem/power-cut failure handling is less complete than normal-path metadata extraction.
  - The build records many hashes yet lacks an independently demonstrated clean paired-source/cache recipe and current public compliance closure.
  - Host input tests omit kernel event backlog/SYN_DROPPED and service error paths; the real UI can block long enough for those to matter.

## Modules worth attention, not automatic splitting

`main.rs` and `playback.rs` are the primary integration-risk modules. Extract a responsibility only when it makes a queue/lifecycle/state contract testable. Native media C needs a lifetime/error audit, not wholesale language replacement. The densely formatted database dispatch deserves local readability work when changing acknowledgements. UI screen layout length alone is not a refactoring priority. The imported Wi-Fi core deserves continued narrow integration testing and maintained provenance; rewriting it is a large separate hardware project.

## Legacy/dead candidates: F30
  - `assets/fonts/reborn-font.rgba` has no current source/preview reference; current code uses `reborn-ui.rgba` and `reborn-display.rgba`. Candidate DEPRECATED / DEAD, not deleted here.
  - `font8x8` in `docs/architecture/dependencies.json`/baseline documentation is stale relative to Cargo/current atlas use; it is not proof of an active second font engine.
  - Y2PlayerNative manifest fields/paths are obsolete placeholders, but removing them requires coordinated validator/consumer changes.
  - Old baseline/dev configs and reports are historical evidence, not necessarily dead implementation. Label and index them, do not erase recovery provenance.
  - Source UI packs/reference tokens may be useful design inputs; their presence does not mean every duplicate token file controls the production theme. Document the authoritative runtime theme and keep rights information.

TODO count is not a useful debt score here. Several serious incomplete behaviors have no TODO marker. Conversely, explicit reserved/unsupported branches in hardware policy are safer than silently claiming support.

## Debt that should not be “paid” now

Do not reclaim reserved memory, widen charging current/voltage envelopes, rewrite bootloader/storage translation, replace Linux subsystems, replace SQLite/FFmpeg, rename the entire workspace, chase zero unsafe code across FFI, or redesign the UI during stabilization. These changes would add new qualification scope without fixing the identified player contracts. Preserve author/committer identity and source/license provenance.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
