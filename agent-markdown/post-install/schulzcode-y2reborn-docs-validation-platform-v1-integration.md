---
title: "Platform v1 application integration - Innioasis Updater"
description: "Platform v1 application integration Historical software candidate. The pair below remains exact for that build, not the Fix01 image. Current Reborn state ../CURRENT REBOR"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-platform-v1-integration.html"
---

# Platform v1 application integration - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Platform v1 application integration

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Platform v1 application integration

Historical software candidate. The pair below remains exact for that build, not the Fix01 image. [Current Reborn state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FCURRENT_REBORN_STATE.md) and the [Fix01 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md) now show all eight real workload producers and bounded wired playback, while the paired CPU platform fails deeper idle, high-OPP and suspend acceptance.

The validated candidate source pair is Linux `d04b95aaff713edf943042d97a4c6134ca19fc24` / Reborn `6c8aa128550ec80addd08ef3145e9d5a846ddf2e`. Closing commits change documentation only. Final Reborn host workspace tests: 155 passed, formatting and strict all-target clippy passed. Fresh Buildroot/Reborn ARM, eight QEMU userspace checks, installed defaults and the real 1k ARM database/scanner/UI benchmark pass. The platform image/package validation includes these exact installed binaries. Historical ARM-pending notes below describe original checkpoints and are superseded by those receipts. No physical application/Bluetooth qualification or target performance acceptance occurred; larger 10k/20k results are host measurements until owner qualification.

Started 2026-09-23 from Reborn `d9ba0549e6b34eff029bd13f7c33a491fee09e66`; Y2Linux starts at `5f6b4468fb43605ca1da679420823afa72cea73f`. Existing untracked review/audit/codec documents in the original checkout are preserved. Work is in an isolated local branch while the previous committed pair builds. No device access, flashing, push or identity change. Later correctness-closure fixes are retained; no older repaired defect is reintroduced as an outstanding issue.

`reborn-bench` measures the actual library schema/open/list/upsert/scan code at 1k, 10k and 20k tracks plus current UI catalog/wheel and queue operations. It requires an inherited empty scratch directory FD and refuses an existing DB. The platform creates and pins that directory. No real media/DB/state is used. SQLite WAL/NORMAL and 64-track batching stay unchanged. First-connection and warm reopen are labelled without claiming a cold OS cache or cold device. Synthetic short-WAV scanning is metadata work, not playback throughput.

`cargo test -p reborn-library --locked benchmark::tests -- --nocapture`: passed the real-schema/count/existing-DB refusal case. `cargo build -p reborn --bin reborn-bench --release --locked`: passed fresh host release build. ARM, target performance and physical qualification remain pending. Host workload results and subsequent integration changes are recorded below as they are completed.

Host runs completed 1k/10k/20k synthetic database and scanner workloads with no failures. Raw output is in Y2Linux `out/platform-v1-host-measurements/`. At 20k, initial synthetic-WAV scan was 11.705 s; unchanged scan was 0.411 s. These are x86 host filesystem/cache results during an unrelated ARM build, not Y2 budgets. No SQLite schema, index, cache or durability policy was tuned from these numbers.

Measured wheel row generation at 1k/10k/20k had medians 0.129370 / 1.333516 / 2.712791 ms. The focused correction counts matches without allocating each row, formats only the visible song page, and temporarily borrows the model's library for semantic input instead of cloning every Track. After a fresh release build, wheel medians were 0.002074 / 0.016462 / 0.032904 ms. UI output remains bounded by the existing visible layout, with original catalog indices retained. Queue and SQLite remain authoritative; no cache hierarchy or ORM was added.

`cargo test -p reborn-ui -p reborn --bin reborn --lib --locked`: 13 UI and 27 runtime tests passed. New 20k filtered-page test checks visible focus, final row identity, modal bounds and restoration of the exact library allocation. New platform images also require a matching SD mount claim/UUID/boot before an SD source is advertised, while older images retain the existing compatibility path. ARM and physical latency/UI/card qualification are still pending.

Power integration: normal shutdown requests use the platform socket when its contract is installed. Current-boot intent triggers audio/session/SQLite close; acknowledgement reports failures truthfully. The database worker checkpoints and closes before replying. Runtime/library/platform host suites and targeted real checkpoint/close test pass. Hardware transitions/low-battery thresholds remain Y2Linux owner-controlled qualification; no electrical limit is chosen here.

Network/storage integration: fresh platform network readiness is distinct from wpa_supplicant association; Online requires platform IP/route/DNS observation. Boot/time freshness is validated. Platform media maintenance owns automatic mount/unmount; Reborn no longer initiates those actions on new platform images. Source claims validate the sysfs instance in addition to mount/boot/UUID, rejecting same-minor reuse. Targeted freshness and four storage tests pass. ARM validation for this revision follows separately; phase-2 QEMU evidence is not transferred.

AVRCP: BlueZ Media1 registration exports Reborn's existing playback model and metadata. An eight-command bounded queue delivers semantic Play/Pause/Next/ Previous actions; only the current BlueZ owner can invoke them. Two host tests pass, including private D-Bus registration, authorized control, unauthorized sender rejection and unchanged metadata until the actual model changes. No remote playback or physical radio qualification is claimed; ARM build pending.

Bluetooth user actions now share the platform reconnect operation lock. Pending connect/power intents inhibit automatic recovery; successful explicit completion re-arms it. Client timeout or D-Bus loss stays inhibited until owner retry. 34 platform tests pass; ARM/image validation follows in the next build.

`rebornctl bluetooth codec Auto|SBC ADDRESS` submits a bounded explicit codec session while playback is stopped. The platform inventory, runtime manager and GetCodecs intersection determine typed eligibility. Auto requires physical and distribution approval; this unqualified candidate therefore fails Auto closed. Manual SBC remains available for owner qualification. The policy tries at most two preferred codecs plus conformant SBC, never revisits a candidate and never automatically promotes after fallback. Optional encoders are absent.

PCM probes/handles hold shared leases; selection requires an exclusive lease. Unknown selection outcome retains an on-disk gate until BlueALSA owner replacement, including app death during the request. Negotiated codec/format/rate/channels always come from the actual PCM; selection success is AwaitingNegotiatedObservation. The existing transport invalidation logic still governs playback. Codec controls are exposed through the stable control API/CLI; a richer preferences UI is deferred.

Application boot readiness is emitted only after actual KMS first-frame success and runtime worker creation, with boot ID/PID/start ticks. The platform verifies current generation, responsiveness, core interfaces and update source identity before acknowledging boot health. Headless/QEMU startup never supplies a fake physical first-frame receipt. Reborn exposes typed versioned platform capability reading with absent flags false, plus `--default-settings` so settings-only reset uses the installed schema/defaults without discarding queue or position. Incomplete owner maintenance prevents application startup until explicit resume.

Bluetooth Auto/AVRCP, shutdown and SD/readiness contracts are platform foundations, not a second application authority. The existing FFmpeg DSP, SQLite single writer, semantic Actions and bounded workers remain. Optional codec preferences UI, target library/performance budgets and physical validation remain follow-up application/owner work; unsupported platform features must stay explicit.

See Y2Linux's [completion ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FPLATFORM-V1-COMPLETION.md) and [owner qualification sessions](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FPLATFORM-V1-OWNER-QUALIFICATION.md) for separate software, ARM/image and physical/endurance evidence. Return general application development here after the owner qualifies the advertised core; do not reopen gated hardware scope as incidental application work.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
