---
title: "Community beta feature completion implementation pass - Innioasis Updater"
description: "Community beta feature completion implementation pass <!-- knowledge-base-scope: historical-implementation-receipt; baseline02-sync 2026-10-03 -- Dated implementation rec"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-community-beta-implementation-pass.html"
---

# Community beta feature completion implementation pass - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Community beta feature completion implementation pass

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Community beta feature completion implementation pass

Dated implementation receipt. The campaign identities, test counts and pending actions below belong to the recorded source cut. The newest sealed integrated candidate is [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md). [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) now proves bounded C1/C2/C3. Baseline02 new-image/automatic cold boot and unrelated release gates remain open.

Started 2026-10-02. This is an owner-authorized implementation campaign, not a release qualification. No flash, device mutation, push or Git identity change. Existing unrelated dirty documentation is preserved. All233 feature records and release requirements remain; lower modes are fallbacks, not scope waivers.

## Source and evidence

Starting Y2Linux: `9ac2c0b7018ce707ec15f8845daf58ce38ec18a0`. Starting Reborn: `eb64b8b21058eacb1ef183f7570cca8100cbbb46`. Integration source Y2Linux: `02eb7359cff1d1e6eec725d496078338d1e7d601`. Integration source Reborn: `72e94b2d8eb13dcb7e2677bff2846edec3ddf81a`. Final documentation commits may follow these exact embedded build identities.

Read-only SSH identified installed Candidate4 (`dcbd7d1` / `b92d312`), boot `159f7c81-ab89-4440-bc89-df827dd8bc34`, taint0. Both buses negotiate near200MHz, but this is not integrity/endurance proof. Its PM records contain no valid current attempt. Fix02 remains the latest broad physical qualification; candidate3's CRC/clock observations remain the storage evidence. No stale binary is used to certify the new source.

## Ten workstreams

| Priority | Result | Implementation and remaining gate |
| --- | --- | --- |
| 1 Full resume | BLOCKED_BY_HARDWARE_PROOF | Invalid cold SRAM evidence suppressed; typed sleep lifecycle and exact same-boot/kernel-exit/Reborn restoration contract added. Actual post-SPM stall still unlocalized. Existing Fix03 breadcrumbs cover the interval. New RTC/Power trace required. |
| 2 C2/C3 | BLOCKED_BY_HARDWARE_PROOF | Existing C2 baseline/runtime-clock corrections and C3 runtime PCM/vector/deadline path retained. No source-backed reason to weaken ownership/topology/domain predicates. Natural C2 and controlled C3 entry/resume await hardware; C3 remains disabled by default. |
| 3 Storage | PARTIAL | Search all32 tuning taps/windows; restore failed latch clock; runtime retune failure schedules claimed-worker timing renegotiation, with payload rejection until safe mode. Production lab mutations removed. HS200 and200MHz SDR104 remain intended ceilings; sustained integrity/fallback/hotplug/resume proof pending. |
| 4 USB/power | PARTIAL | Retain Fix03 progress-aware DMA guard, PIO/off fallback and conservative charger/low-voltage policy. No new unobserved hardware defect invented. Product shutdown/save path preserved. Exact stock current/coulomb functions are stubs; NTC/sense wiring/calibration unproven. Loaded USB and electrical tests pending. |
| 5 Native24 | PARTIAL | Fixed real userspace S32 mapping/constraint negotiation and tested packed24→FFmpeg→floatDSP→S24/S32 low bits. Exact MT6582 wider DL1/AFE path remains unproven, so native wired24 remains NOT_IMPLEMENTED. Source/electrical capture procedure prepared. |
| 6 Native high rates | BLOCKED_BY_HARDWARE_PROOF | Exact research does not establish safe MT6582/Y2 PLL/divider/rate programming. No adjacent-SoC constants copied.44.1/48 native;88.2→44.1 and96→48 conversion remains. Requirement retained; not declared impossible. |
| 7 Classic codecs | PARTIAL | All viable encoder endpoints privately integrated; actual SBC-XQ bitpool and LDAC bitrate/ABR counters, persisted requested/effective quality, bounded qualified/history/load-aware Auto and reconnect preferences. Peer/RF/thermal/coexistence proof and optional-codec distribution clearance remain. |
| 8 Reborn | PARTIAL | Productv2 wheel-friendly EQ, truthful source/output details, typed sleep/refusal, codec preference versus actual state, SBC-only quality, saved once-per-connection preference, estimatedSOC and diagnostic export. Ready-frame splash/shutdown preserved.238 host tests, fmt and strictClippy pass; physical UX/restoration proof pending. |
| 9 Tester operations | PARTIAL | Fresh personal-key data seed, separate redacted export/retrieval, music guide, preserving update/recovery guide, one guarded SSH/Wi-Fi harness. Host first-owner/privacy tests pass; actual first install/update/recovery rehearsal pending. |
| 10 Release composition | PARTIAL | Actual-config capability/source manifests, whole-image private-byte rejection including deleted keys, protected extras rejection, fail-closed public gate, pinned source/legal-info delivery tooling. Final build/package receipts below; legal review remains open. |

Detailed starting states, root causes, changed files, tests, primary sources and remaining proof: [platform](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2Fimplementation-platform.md), [audio/codecs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2Fimplementation-audio-codecs.md), [Reborn/power](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2Fimplementation-reborn-power.md). Tester/release files: `tools/platform/y2_platform/diagnostics.py`, `diagnostic_fields.py`, `tools/host/diagnostics.py`, `tools/development/qualify-feature-completion.py`, `tools/production/first_owner.py`, `privacy.py`, `composition.py`, `system_update.py`, `check_installed_arm.py`, `check_elf.py`, `seal_sources.py`, `tests.sh` and matching tests. [Tester guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-TESTER-GUIDE.md), [source/distribution obligations](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-SOURCE-DELIVERY.md).

## Precise capability conclusions

Full resume: no verified root cause or corrective post-SPM fix. Existing RTC and Power wake source paths plus retained-vector/kernel/device breadcrumbs are ready for a decision run. Source can recognize complete restoration; restoration itself is not proven. Normal product deep sleep refuses until qualified; the explicit owner diagnostic helper remains available. Charger refusal, CONSYS one isolated retry, USB protections and safe abort/unwind remain.

C2 requires naturally idle owned clocks and valid timers. C3 additionally requires CPU0-only topology/secondaries physically off, admitted lowOPP, idle media/radio and bus domains, armed CIRQ, future GPT4 deadline, valid PCM/vector/context and exact restoration. Read-only observation still blocked by highOPP/domains/clocks. `y2.cpuidle=off`, `y2.deep_idle=off`, `y2.cpu_safe=1` remain.

Wired output currently remains S16_LE,16 meaningfulbits,32-bit I2S slots/64fs, 16-bit DAC payload.44.1/48 are native;88.2/96 are family-converted. User-space S32 support is not a native24 hardware claim. Physical low-bit/rate fixture is `tools/host/audio_precision.py`; source register evidence is required first.

Battery remains estimatedSOC.70/450/650mA ceilings,4.175V target, charger hold, termination/recharge guards, low/critical handling and3.4V hard floor remain conservative. Shutdown saves Reborn, stops audio, closes SQLite and syncs. Real pack-current/coulomb/NTC units are not exposed without wiring/calibration proof.

| Codec/policy | Built/enabled/integrated | Software evidence | Physical/distribution |
| --- | --- | --- | --- |
| SBC | yes | encoder/endpoint/observedPCM | candidate peer/reconnect pending; notices required |
| SBC XQ | SBC quality policy, user-selectable | dual-channel bitpool38/47 recognized | compatible peer and link margin pending; same SBC source obligations |
| AAC | yes, private experimental | real encoder44.1/48 and endpoint contracts | peer/CPU/thermal pending; distribution unresolved |
| aptX | yes, private experimental | separate real encoder contract | peer/CPU/thermal pending; distribution unresolved |
| aptX HD | yes, private experimental | separate real encoder contract | peer/CPU/thermal pending; distribution unresolved |
| LDAC | yes, private experimental | real encoder both rate families | peer/CPU/thermal pending; distribution unresolved |
| LDAC qualities | yes | 303/606/909 and330/660/990 family mapping | RF/quality comparison pending; LDAC distribution gate |
| LDAC ABR | yes | actual library queue-driven adaptation plus exported counters | over-air adaptation/coexistence still pending |
| Auto | yes | bounded attempts→SBC, actual/preference separate, bounded history, no PCM-generation flapping | qualification-driven promotion and real peers pending |

## Validation and candidate

Final current-source validation and artifact receipts follow. No RC or feature-complete qualification is asserted by this implementation report.

## Sealed integration handoff

Verdict: READY FOR HARDWARE DECISION RUN. Feature completion remains open; this is not an integrated RC or public beta. Candidate: `out/y2linux-community-beta-feature-completion-candidate/`.

Fresh source: Linux `02eb7359cff1d1e6eec725d496078338d1e7d601`; Reborn `72e94b2d8eb13dcb7e2677bff2846edec3ddf81a`. Kernel `6.18.0-y2linux-feature-completion-01`, Buildroot2025.02.18, root `2025.02.18-platform-v1.16`, API1/featurecontract2.

BOOTIMG SHA256: `060145e3931e1d23f0b9805c0f12417d47f1589cf4489010705876a1ade7b098`. Y2ROOT SHA256: `2039d61e30bd02d0f3fd8006808e7dbc95bbaabce7f1834fa12d57bcccd81995`.

Software: fresh kernel/config/DT/modules/ABI and Buildroot/Reborn ARM build; production suite 345PASS/5environmentSKIP (350collected), all5 environment-skipped cases PASS on the host, Reborn238PASS, fmt and strictClippy PASS. ARM/QEMU, installed Python/SQLite/ALSA/codec contracts, FFmpeg checks, ELF/dependency closure, configuration/codec inventory, package validation, actual-image privacy scans and protected partitions pass. Individual logs and exit codes are retained in `validation/`; skips are listed in the production log and are not hardware passes. Real encoder contract covers12cases; software LDAC ABR is exercised with synthetic queue pressure, not RF loss.

`manifest.json`, `metadata/release-composition.json`, `metadata/delivered-capabilities.json`, `sources/manifest.json` and SHA256SUMS bind the payload/source/configuration identities. `sources/` includes exact Git archives, pinned Linux/Buildroot and legal-info sources/licenses/limitations. Collector success is not legal clearance; optional codecs and owner firmware remain public-distribution blockers. Public packaging fails closed.

Next owner action: flash only this paired BOOTIMG/Y2ROOT with `MT6582_preserve_data_scatter.txt`, preserving Y2DATA. Do not select any protected partition or data initialization. Then use the single integrated harness:`python3 tools/development/qualify-feature-completion.py \ --package out/y2linux-community-beta-feature-completion-candidate \ --host y2 --wifi-host y2-wifi --run --exercise --sleep`

The two preconfigured verified SSH aliases must address the same player through USB and independent Wi-Fi. It gates sleep on awake/retention checks and prompts only for unavoidable physical actions. Codec peers, I2S/electrical equipment and installation/update/recovery choices remain explicit owner-dependent cases, not automatic passes. Private harness evidence stays separate from redacted exports.

Local implementation commits:

Y2Linux:
  - `02eb735` release: bind shutdown capability to the installed power coordinator
  - `e7019ae` release: resolve the generated Buildroot image alias within its build directory
  - `1cd7908` release: fail closed on incomplete codec distribution evidence and run integrated regressions
  - `8e84e9a` bluetooth: preserve observed transport when quality settings are invalid
  - `df2fa49` release: bind private-state scans and capabilities to preserving packages
  - `ccca66a` testers: export redacted telemetry and integrate physical qualification
  - `2d06d93` platform: retire completed sleep state after a later normal boot
  - `0bfda9a` docs: record initial Bluetooth capability discovery repair
  - `a0ba1f7` release: retain reproducible ARM validation and exact source-delivery tooling
  - `e5f11b9` release: track the full feature-completion campaign and tester workflows
  - `d52dd2b` release: identify the feature-completion integration candidate
  - `b6e66dd` platform: expose sleep, codec settings and redacted tester export commands
  - `b5cd762` audio: integrate private Classic codecs with encoder evidence and precision checks
  - `a195426` docs: record platform feature-completion fixes and physical gates
  - `a4d0d8a` platform: report typed sleep refusal and verified same-boot restoration
  - `4ecba3a` power: reject undefined cold SRAM resume evidence
  - `56e020c` msdc: reconcile failed runtime tuning and close public lab controls

Y2Reborn:
  - `4bcd9fd` docs: record final 238-test Product v2 validation
  - `72e94b2` Product: discover codec eligibility and apply saved preferences without flapping
  - `fffc06c` Audio: honor observed S32 sinks and qualified codec fallback policy
  - `25b074b` Product v2: integrate EQ, typed sleep, codec quality and tester diagnostics

Packaging integration also corrected the bounded Buildroot ext4 alias resolution and bound shutdown capability to its actual power coordinator. Both have regressions and the final full build/tests/package were repeated after correction. All350 production cases pass (345 isolated,5 host dependency cases). ELF closure covers383files/1403edges. Source/license attachment contains445files.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
