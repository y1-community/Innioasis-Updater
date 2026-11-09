---
title: "Y2Linux + Reborn Platform 1.0 baseline - Innioasis Updater"
description: "Y2Linux + Reborn Platform 1.0 baseline Independent software-seal verification, 2026-10-04. READY FOR PLATFORM V1 PHYSICAL QUALIFICATION . One owner-local baseline; SOFTWA"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-platform-v1-baseline.html"
---

# Y2Linux + Reborn Platform 1.0 baseline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux + Reborn Platform 1.0 baseline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux + Reborn Platform 1.0 baseline

Independent software-seal verification, 2026-10-04. READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION. One owner-local baseline; SOFTWARE_VALIDATED / INTEGRATED_PHYSICAL_NOT_RUN. During software sealing this session did not access a device, flash, push, merge main or qualify public distribution.

Later owner-installed qualification is PARTIAL / INTERRUPTED. Bounded smoke/C1/hotplug/OPPs/C2 and DATA/SD hashes pass. Owner restart interrupted an overlong intentional USB-off topology wait, with no recorded C3 armed/entered cycle. Earlier post-flash USB trouble and recovered-boot DRM WARNING/C3 policy Skipped remain open. The owner prioritizes completing a separate audio test; USB/boot diagnosis follows its lease release. Host-only qualification corrections do not change these sealed image/source identities. See the [current physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BASELINE-PHYSICAL.md).

## 1. PLATFORM 1.0 BASELINE IDENTITY

Build `Y2LINUX-PLATFORM-V1-BASELINE-01`. Release `1.0.0-platform-v1-baseline-candidate.1`. Kernel `6.18.0-y2linux-platform-v1-baseline-01`, root `2025.02.18-platform-v1.24`, Buildroot 2025.02.18, Reborn 0.2.0, FFmpeg 9.0.2. Existing version sequence advances v1.23 to v1.24; API 1, feature contract 2, data/layout schema 1, battery profile 1 and low-battery policy 2 remain. On-device versions/build-id distinguish this baseline from Baseline02, subsystem images and the master's integration candidate.

Canonical package: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-baseline-candidate`. Final paired worktrees are `/home/luca/Dokumente/Code/worktrees/platform-v1-baseline-final/{Y2Linux,Y2Reborn}`, branches `codex/platform-v1-baseline-final`. Owner main and original worktrees remain unchanged; the owner's pre-existing dirty Linux documentation is preserved.

## 2. SOURCE COMMITS

Compiled and archived Linux: `98daf3f0220f4a1580bb4893094ee9f0e02362a5`.

Compiled and archived Reborn: `9cd12baeeb70b204e08299bd4c91c8c35604c304`.

Master compiled Linux `4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2` / Reborn `dd73dcc3243045cd33e319dda2f76918ed37ea31`. Later master tips were `de9f26d6dc85a417e1f7f4febf5317cfbef04236` / `9cd12baeeb70b204e08299bd4c91c8c35604c304`; every intervening changed path is under docs/. Reborn runtime source is unchanged from dd73dcc. Final Linux adds release identity, the smoke/Power handoff and test reconciliation. Later report commits are documentation only and are recorded separately in package `metadata/documentation-heads.json`; they do not relabel the compiled images. Exact source archives and locked upstream archives are supplied.

## 3. 12 SESSION SUMMARY

[Authoritative session results](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-FINAL-SESSION-RESULTS.md) explains each goal, exact branch/start/final commit, changed files, fixes, optimization, software/hardware evidence, no-change decisions and selected integration units. The machine ledger enumerates every Git diff/blob and test addition. Goals are reconstructed from retained admissions, not invented verbatim original prompts; the expected orchestrator directory is absent.

| Session | Actual accomplishment / classification |
| --- | --- |
| 1 Bluetooth | Event/deadline reconnect and observation, correct discovery/PCM epochs; OPTIMIZED, HARDENED, BETTER_OBSERVABILITY; actual headset remains open |
| 2 Wi-Fi | Fresh readiness/DNS/RSSI, bounded slow replies and shared service wake; BUG_FIXED, OPTIMIZED, HARDENED; changed-policy hardware/coexistence pending |
| 3 FFmpeg/metadata | Bounded demux/artwork/custom I/O, truthful source precision and extractor revision; SIGNIFICANTLY_IMPROVED, HARDENED; one DB scanner |
| 4 High-res audio | Correct final rounding and truthful precision layers; BUG_FIXED, BETTER_OBSERVABILITY, INVESTIGATED_NO_CHANGE_JUSTIFIED; native S16 retained |
| 5 USB | Confined MTP with ECM, durable transfer refresh and one filesystem owner; SIGNIFICANTLY_IMPROVED, HARDENED; real desktop acceptance pending |
| 6 Suspend | Checked restores/quarantine, codec refusal rollback and acknowledged quiescence; HARDENED, BUG_FIXED, BETTER_OBSERVABILITY; RTC FAIL remains open |
| 7 Storage | diskseq/CID identity, file/parent pins, UTF-8 and safe hotplug claims; BUG_FIXED, HARDENED; old high-speed evidence retained |
| 8 Reborn performance | Static-frame suppression, ordered batching, async observations, partial-write pacing; SIGNIFICANTLY_IMPROVED, OPTIMIZED; temporary exact ARM measurements only |
| 9 Graphics | Checked JPEG reduction, working GPU/display PM preserved; OPTIMIZED, INVESTIGATED_NO_CHANGE_JUSTIFIED; new renderer belongs to performance |
| 10 Library DB | TEMP scan/token protocol, conditional writes, bounded catalog paging and no-op preservation; SIGNIFICANTLY_IMPROVED, OPTIMIZED, HARDENED |
| 11 Input | Monotonic provenance, bounded reads, stable rebind, cancellation and canonical actions; BUG_FIXED, HARDENED, BETTER_OBSERVABILITY; counted controls untested |
| 12 Master | Reconciled 34 cross-owner concerns and selected one buildable pair; BUG_FIXED, HARDENED, OPTIMIZED; no integrated physical acceptance |

Every subsystem also retains PARTIAL_REMAINS_OPEN for its hardware, endurance or distribution limits. No-change GPU/AFE/CPU decisions are valid outcomes. [Human changelog](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-BASELINE-CHANGELOG.md) separates before/finding/change/result/hardware.

## 4. MASTER INTEGRATION SUMMARY

All eleven selected handoffs are present, with semantic adapters rather than blind branch replacement. Rejected duplicate FFmpeg scanner, weaker Bluetooth polling, competing event clocks/cache/workers and unproved wider native audio remain absent. The Reborn b71b468 scanout-release foundation is retained ahead of owner main. USB/storage identities, radio codec intent/observation, source/PCM precision, paired native ABI, diagnostics and sleep ACK barriers have one coherent contract. [Independent concern matrix](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INDEPENDENT-VERIFICATION.md) traces C01–C34.

## 5. INDEPENDENT VERIFICATION RESULT

PASS for source integration and software/package handoff. No runtime integration defect requiring new hardware behavior was found. Source ancestry, owner blob retention, shared adapters and current artifact composition were checked directly.

Corrections after master: repository-consistent baseline identity; mandatory short smoke gate before child actions; explicit separate Power/RTC choice; four smoke regressions; old telemetry timeout assertion reconciled to accepted three-second Wi-Fi STATUS, preserving unavailable/failure checks and adding radio-off no-query coverage; five existing telemetry regressions added to production; stale “current” planning passages marked historical. No runtime C3, battery, audio admission, partition or recovery policy changed. A second completely empty build output was used after the test reconciliation; the final package contains that source.

Production review confirms effective config has configfs ACM/ECM/FunctionFS and no MSC or /dev/mem. Dangerous MSDC lab controls are compiled out; performance tracing is opt-in. Read-only diagnostics, failure quarantine, bounded workers, safe fallbacks and product telemetry stay. No forced qualification budget becomes the normal boot default. Initial environment and legacy-profile failures are retained and distinguished from passing final gates, not removed or called PASS.

## 6. CPU FOUNDATION

Direct comparison to physical UART01 e9e8d63 proves sixteen idle/timer/CIRQ/DVFS/ PWRAP source files and three protected SPM idle functions byte-identical. The seven rebuilt CPU foundation objects also match the master's objects byte for byte. C1, C2, C3, stock global UART request/ACK, CIRQ, GPT4 deadline handoff, GPT6/local timer restore, hotplug, DVFS and parking guards are preserved.

UART01 same boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0: C1 physically working; C2 6,971 entries, 84.3473% screen-off residency, zero clock restore failures; C3 21 guarded genuine context-loss returns plus 3,624 normal entries, 65.2450% normal-window residency. Final 3,647 successful entries/resumes, UART ACKs/CIRQ/timer restores agree; zero restore faults. These are inherited evidence on UART01, not observations of this baseline.

Release C3 policy: POLICY_ENABLED. Kernel starts guarded off/budget zero; inherited `S05y2-cpu-idle` performs static admission/readback/rollback once per boot and enables qualified CPU0 DORMANT with normal budget -1. All dynamic clock/radio/USB/OPP/topology/deadline/UART/battery guards remain. Safe/off/manual stop settings are respected. New-image automatic cold-boot behavior still needs hardware proof. Users do not receive an unconditional C3 promise.

## 7. POWER / SUSPEND

Ordinary product deep sleep refuses unqualified hardware. Reborn preparation quiesces scanner, artwork, observations, playback/render and checkpoints; no pending USB refresh restarts work after ACK. Input closes/reopens queues and suppresses the wake gesture. Full suspend has checked restores and failure quarantine separate from unchanged runtime idle.

Baseline02 RTC wake remains FAILED and unresolved. One 12-second full trial changed boot `27e6d684-3794-4490-95db-a489027cd4f4` to watchdog-recovered `88b85fa3-2282-4d93-b0b8-818a105ddd0a`. Retained DEVICES_RESUMING, wake 0x20, full PCM 596/reset 0x59325253, no COMPLETE/EXIT; CS43131 1-0030 resume entry 7407 has no leave through 7422. Internal stalled instruction/root cause UNKNOWN. New refusal-rollback repair/regcache replay, checked restores and retained substeps are real source changes, but not a demonstrated fix for that RTC stall. Post-reboot scratch hashes/ext4 zero errors prove recovery only. Power and RTC full wake are separately NOT_RUN on the new baseline; staged PM/awake RTC are not full suspend acceptance.

## 8. STORAGE

Linux alone mounts/writes filesystems. Live block dev_t/diskseq and persistent CID-qualified UUID IDs are distinct. Playback/sidecars/artwork retain no-follow file/parent pins during admission and recheck live source; cache pixels own no FD. FAT UTF-8 and claim/teardown/recovery diagnostics compose with scanning and MTP. Old bounded eMMC/SD mode/hash evidence remains historical. Different cards, cloned UUIDs, absent boot, existing FAT/exFAT and integrated hotplug/endurance remain physical gates. Partition geometry, logical/native addressing and Y2DATA schema are preserved; no new format/partition/clock ceiling is introduced.

## 9. USB

Consumer MTP and Developer ACM/ECM use configfs; both retain ECM. MTP is a confined file-level view of reviewed media roots, with no-follow pinned Linux mount claims and durable completed refresh generations. System partitions are never MTP roots; MSC is disabled, so there is no simultaneous raw/live filesystem export. SD release/unbind and scanner busy/sleep barriers share the mount model. Fresh ARM responder and real native confinement/protocol/fsync fixtures pass. Desktop enumeration, large/small/reconnect integrity and selected host/backend acceptance remain NOT_RUN. SFTP over ECM is not desktop MTP acceptance.

## 10. WI-FI

Supplicant/fullmac/DHCP retain radio ownership. Readiness/DNS/RSSI is bounded by boot, epoch, peer and address freshness. Three-second STATUS accommodates historical replies above two seconds without inventing Online/disconnected. One select handles supplicant and USB/signal/control wakes. Old RX/TX hash rates and latency are historical; invalid FAST_PSP comparison and TX iperf reset stay documented. New-policy AP reconnect/coexistence/screen-off/cold boot remain open.

## 11. BLUETOOTH

Bounded event/deadline worker owns reconnect intent; Reborn submits commands and observes actual BlueZ/BlueALSA state without competing polling. Paired/Bonded/ Trusted/Connected/ServicesResolved and codec preference/negotiation/PCM epochs are separate. New fake-bus/restart/JSON cases pass; older disconnected samples never qualified the changed worker or a headset. Real peer/SBC and optional codec/reconnect/coexistence/listening/endurance remain open. Distribution rights are not inferred from local compilation.

## 12. AUDIO / HIGH-RES

Source precision, canonical FLTP DSP precision, final integer conversion/container, meaningful bits, I2S payload/slot and actual sink precision stay distinct. FLTP has about 24 significant binary bits; f64 VolumeRamp does not recreate lost source information. S16/S24/S32 software narrowing uses nearest ties-even and saturation. Native kernel policy still admits S16_LE stereo 44100/48000; S24/S32/88.2/96 kHz remain refused. S32 is a container, never proof of true 32-bit output. Actual serial low bits/clocks/analog precision require hardware. Wired readiness pacing preserves accepted prefixes, recovery/discard and bounded control latency; real baseline XRUN/listening/BT transport remain required.

## 13. FFMPEG / METADATA

Exactly FFmpeg 9.0.2, required decoder/demuxer/filter/local-file protocols; no encoder/network enablement inferred from configure history. Demux-only local inspection, bounded artwork/tag/I/O/cancellation, truthful source bit depth, date/genre/timing fields and paired C/Rust structures ship in one media membrane. One shared checked JPEG reduction wrapper composes graphics and limits. Installed ARM/QEMU version/dependency/ABI tests pass. Wider product tag/UI scope was not added. The native media membrane's target bytes match the master's build.

## 14. LIBRARY / SQLITE

One DB worker owns TEMP scan_seen/candidates and Begin/Probe/Batch/Finish tokens, conditional durable transactions/pruning and 512-row keyset catalog pages. Metadata revision 2 is an additive migration retaining user_version/schema 1 and row IDs. Old UUID-only queues fail closed; rescanning admits new CID IDs, preserving offline history. Four-cover ownership/freshness and USB generations do not create another scanner. Native target SQLite is 3.53.4. Historical 50k workload improvements remain scoped; 250k is an unqualified ceiling. Ingest/prune tradeoffs and unavailable target /proc/self/io prevent a zero-flash-write claim.

## 15. GPU / DISPLAY

DRM/Lima/Mesa/GBM/EGL and scanout-release/runtime PM are preserved. Graphics adds checked reduced JPEG decode; performance adds adjacent-texture batches in original order with 49,152-byte staging. One UI loop schedules visible-state frames; static UI no longer forces periodic drawing. Splash/shutdown ownership and no-normal-readback contracts pass. Historical temporary ARM JPEG/display results and slightly different pixels retain exact source/tolerance; integrated awake/off/wake, blend/order/brightness/optical/full-resume remain required.

## 16. INPUT

One physical WheelCadence owns 8 ms duplicate filtering and cadence acceleration, with pause/reversal reset and isolated detents remaining one action. Successfully selected monotonic evdev clock authorizes kernel_mono_us; synthetic/unknown timestamps are None. Sixteen reads/device, stable identity/rebind and typed Cancel cover backlog/overflow/malformed held keys. Semantic PowerHold opens shutdown confirmation, short paused Power requests guarded sleep and playing Power blanks. Physical capture had zero events and no changed app execution; counted detents, buttons/holds and mechanical latency remain NOT_RUN.

## 17. REBORN PERFORMANCE

Visible-state frames, descriptor waits, existing-watchdog capacity-one observations, bounded trace opt-in, successful-only cache eviction and wired partial-write pacing are selected. Historical exact 069415a app playing CPU 87.95→11.21% of one core, audio thread 82.63→5.11%, static Home 14→0 frames/10 seconds, wheel KMS p95 59.93→17.52 ms are useful evidence, not new baseline measurements. Synthetic timings exclude mechanical IRQ/photon latency; small capture differences, cold layout/startup and initial two-sample Play/Pause tradeoffs are retained.

## 18. SOFTWARE TEST RESULTS

Fresh production: **475 cases, 465 passed, 10 dependency skips; all ten exact skipped cases separately PASS** within a native 60-case run with zero skips. Reborn: 324 passed, zero failures/ ignored, fmt and strict workspace all-target locked Clippy PASS; fresh ARM build PASS.

Supplementary current contracts: 25 isolated source cases, 34 native splash/update cases, 4 emitted watchdog/syscall cases, all PASS/zero skips. These overlap production and are not added into a fictitious unique total. Fresh kernel/modules/DT/ABI and shell checks PASS; Cortex-A7 QEMU executes eight Reborn commands. Installed ARM Python imports 33 platform modules, SQLite/WAL/SSL/codec/default-settings/1k scan and sixteen ALSA-null constraints PASS; none is reported as device evidence. **384 ELF files, 1411 dependency edges**, ARM hard-float/closure and no build RPATH PASS. 106 package records, locked source hashes, capability manifest, preserving new/fallback root privacy and package validation PASS. Legal-info succeeds with collector warnings retained; source archive and complete checksum validation are supplied in package receipts.

Initial isolated source symlink and host bc prerequisites were corrected before rerunning. The extra old `tests.test_evdev` development fixture fails against an unchanged eight-FD navigation structure; it is byte-unchanged at campaign start and excluded from the established production profile, not weakened to pass. Missing host QEMU/elftools/libdrm/e2fs/sodium prerequisites in exploratory runs were covered in the correct isolated/native environments. Initial failures and the old telemetry assertion are retained in private verification receipts.

## 19. INHERITED PHYSICAL EVIDENCE

UART01 is the physical CPU authority and fallback, with exact source/boot above. Baseline02 supplies bounded storage/radio/staged PM plus its unresolved RTC FAIL. Temporary graphics, DB and exact performance ARM binaries supply only their documented workloads; input's zero-event capture and absent BT peer are not passes. No ingredients qualify the combined images. The session ledger carries complete scope/limitations and points to committed receipts rather than copying prose alone.

## 20. INTEGRATED PHYSICAL TESTS STILL REQUIRED

One [physical campaign](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-PHYSICAL-QUALIFICATION.md) starts with a short source/partition/kernel/app/owner smoke gate, then guarded actual CPU entries. Only after acceptance proceed to A–J boot/recovery, CPU, storage, real desktop USB, connectivity, audio, Reborn/display/input, battery, separately staged and full Power/RTC suspend, and preserving update/diagnostics. Same-boot taint-zero and explicit restoration are required. No new device command was executed here.

## 21. KNOWN ISSUES

Baseline02 RTC same-boot resume failure; full integrated physical NOT_RUN; automatic new-image cold-boot C3 policy, actual desktop MTP, counted input/peer/ coexistence/whole-app and endurance/electrical battery evidence remain open. Native wider AFE precision/rates need evidence, not guessed limits. TX iperf reset, invalid power-save comparison, historical startup/ingest/prune tradeoffs and 250k capacity limit stay documented. No new runtime integration blocker was found. Corrected handoff/test gaps are closed in source; software success waives none of these hardware requirements.

## 22. DISTRIBUTION ISSUES

OWNER_LOCAL qualification ready; PUBLIC_DISTRIBUTION_NOT_READY. Retain owner radio firmware permission questions and AAC/aptX/aptX HD/LDAC rights. Exact source, locked archives, notices/licenses and legal-info are included, but collector limitations remain: external toolchain license collection, local y2-connectivity/ y2-update license-file declarations and libtool/collector scope. Explicit upstream archives supplement Buildroot's omitted own source; this is not a legal conclusion or proof that every redistribution obligation is satisfied.

## 23. IMAGE HASHES

BOOTIMG.img: `531e23a7d4c94f0a7f2aa18c3c5eb1a486f481cf4806c79bf1956453375e6719`.

Y2ROOT.img: `565b8338b00b59ab91ff3fa33efde7674992d9d7d07358d0c2c7eabc043b2ee3`.

The master hashes were independently verified and differ from this baseline. Target inventory: 1413 regular files identical, 19 changed, no file additions/removals. Changes are release/kernel/root/build/commit epoch identity and absolute build/ SDK paths in FFmpeg/Rust/codec rodata and GCC/Python metadata. Every changed userspace ELF executable .text is identical; seven CPU foundation objects match. The 2,322 root tar members retain identical timestamps, modes, ownership and symlinks; only the same nineteen file contents change. Ext4 superblock fields are identical. This is an explained rebuild with a new identity, not an unexplained binary regression. Whole-image bit reproducibility is not claimed. Complete section/ string/file differences are in `validation/master-candidate-comparison.json`.

## 24. FLASH PROCEDURE

Verify canonical `SHA256SUMS` and read `OWNER-HANDOFF.md`. Open canonical `MT6582_preserve_data_scatter.txt` in SP Flash Tool. Select Download Only. Check BOOTIMG → BOOTIMG.img and ANDROID → Y2ROOT.img only. Leave **USRDATA/Y2DATA, preloader, LK, NVRAM, PROTECT, calibration, factory, partition tables and every other partition unselected**. Never use Format All or Firmware Upgrade. The validated scatter enables only those two entries and supplies no Y2DATA payload; unchanged DATA is a compatibility reference, never a flash image. The owner performs the flash.

## 25. FALLBACK

Preserve `out/y2linux-cpu-c3-uart-candidate` and the matching packaged `fallback/` BOOTIMG/Y2ROOT/scatter. UART01 Linux e9e8d63 / Reborn b71b4688, kernel 6.18.0-y2linux-cpu-c3-uart-01, root v1.20; BOOT SHA `a35e7ccb11dfcc642089e422d48a274ab2c700dbba15d00b21cce7b463e4006a`, ROOT SHA `d3a8282a9f5d1b0046283bce1b595eb5797b62c2bff90a62260e80bbfafb5d98`. Matching fallback is validated and byte-preserved; historical candidates are not overwritten. Stock loader/SPFT recovery identity remains retained. Fallback is not authorization to write protected partitions or waive physical acceptance.

## 26. POST-FLASH COMMAND`python3 /home/luca/Dokumente/Code/worktrees/platform-v1-baseline-final/Y2Linux/tools/development/qualify-platform-v1-integration.py \ --run --cpu --smoke-only \ --package /home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-baseline-candidate \ --ssh-config /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix01-physical-qualification/20260927T205514Z/ssh-config \ --host y2 --wifi-host y2-owner-wifi \ --output /home/luca/Dokumente/Code/Y2Linux/out/platform-v1-physical/baseline-01-smoke`

Existing owner SSH config/host keys are used. If the Wi-Fi DHCP address changed, correct its alias to this device's observed address while retaining the pin. Missing/stale connectivity stops; no host-key bypass is prepared. Seven actual observations are requested before CPU actions. Keep playback stopped afterward. This first invocation does not launch USB stress or full-system suspend.

## 27. CURRENT VERDICT

READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION.

One canonical newest owner-local software baseline, exact preserving pair and one smoke-gated campaign. Integrated physical/endurance acceptance is NOT_RUN; main promotion and public release remain separate controlled boundaries.

Final canonical seal: [independent machine receipt](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-baseline-final.json).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
