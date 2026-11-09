---
title: "Platform v1 completion ledger - Innioasis Updater"
description: "Platform v1 completion ledger <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-platform-v1-completion.html"
---

# Platform v1 completion ledger - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform v1 completion ledger

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform v1 completion ledger > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Started 2026-09-23. **Y2Linux Platform v1 Candidate is declared as a software candidate**, following the final standing boundary audit and current-source validation. PHYSICALLY_QUALIFIED and ENDURANCE_QUALIFIED remain false for this candidate. No Y2 was contacted or flashed; no protected partition, calibration, NVRAM, loader, memory reservation or electrical limit was changed.````````````````

| Repository | Starting HEAD | Entry worktree |
| --- | --- | --- |
| Y2Linux | 5f6b4468fb43605ca1da679420823afa72cea73f | Modified docs/planning/roadmap-gap-audit.md; untracked docs/CURRENT_PLATFORM_STATE.md, docs/planning/platform-review-evidence-2026-09-23.md. Supplied review content preserved. |
| Y2Reborn | d9ba0549e6b34eff029bd13f7c33a491fee09e66 | Untracked docs/architecture/bluetooth-codecs.md, docs/audit/, docs/review/; preserved. |

`git status`, `git rev-parse HEAD`, and the latest 30 commits were inspected in both repositories before edits. Existing configured identities are unchanged. No reset, clean, forced checkout, history rewrite, push or physical flashing.

The [roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-v1-roadmap.md) orders implementation. The [September 23 evidence ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-review-evidence-2026-09-23.md) is the starting assessment. Reborn's later `LUNA-CORRECTNESS-CLOSURE-01.md` supersedes repaired R1–R10 findings; R9B's plug-hidden transport remains limited.

Every capability will retain separate implementation, host, ARM, image, physical and endurance evidence. DONE_SOFTWARE / HOST_VALIDATED / ARM_VALIDATED / IMAGE_VALIDATED are workflow labels; PHYSICAL_GATE / BLOCKED_BY_EVIDENCE / DEFERRED retain their literal limits. No previous image's physical qualification is transferred to the new candidate.

## Final candidate and validation

The built source pair is Y2Linux `d04b95aaff713edf943042d97a4c6134ca19fc24` and Reborn `6c8aa128550ec80addd08ef3145e9d5a846ddf2e`. Later repository HEADs contain only the closing documentation; the candidate's `metadata/final-heads.json` records those separately from compiled source. The [60-capability report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-CAPABILITY-REPORT.md) and [machine ledger](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/platform-v1-capabilities.json) record starting state, implementation, tests, commits, ARM/image results, physical gates and remaining risk. Unsupported capabilities do not inherit validation from their gate-reporting tools. The [freeze audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23platform-v1-software-freeze-boundary--2026-09-23-utc&anchor=platform-v1-software-freeze-boundary--2026-09-23-utc) reconciles every coverage area with retained real hardware evidence.

Candidate: `out/y2linux-platform-v1-candidate/`. Build/validation workspace: `out/y2linux-platform-v1-build/`. Release `1.0.0-candidate.1`, rootfs `2025.02.18-platform-v1.1`, build ID `Y2LINUX-PLATFORM-V1-CANDIDATE-01`, kernel `6.18.0-y2linux-platform-v1-candidate-01`, platform API/layout/data schema 1.

| Final check | Result and actual scope |
| --- | --- |
| Kernel/config/modules/ABI, rescue/DT/BOOTIMG | PASS current source, existing size/layout/protected-region contracts |
| Buildroot ARM + Reborn ARM | PASS current paired source; fresh final workspace, resumed after concrete packaging metadata fixes |
| Host platform/maintenance/update/qualification | 64 passed, no skips; real fault/control contracts |
| Locked platform suite | 56 cases: 54 passed, two native GIO/ALSA development-dependency skips covered by the host suite and installed ARM checks |
| Production tooling/kernel contracts | 68 passed |
| Power/radio/USB/GPU/suspend subsystem contracts | 39 passed |
| Reborn host workspace | 155 passed; formatting and strict all-target clippy passed |
| QEMU Cortex-A7 userspace | 8 passed; no physical hardware emulation claim |
| ARM native updater faults | 7 passed on private regular files; signature/device/schema, corruption, reserve, interrupted write, readback, missing health, revocation and rescue containment |
| Installed ARM SFTP | 3 protocol checks: write/close/readback, reserve refusal, interrupted session |
| Installed ARM platform/application tools | 20 Python modules import, unavailable fixture health, SQLite WAL/checkpoint, OpenSSL, readonly ALSA null constraints, actual defaults and 1k database/scanner/UI benchmark pass |
| Installed production ARM updater | Full signed 512 MiB root payload accepted; corrupted signature rejected before payload; no queue/block-device mutation |
| FFmpeg/ELF/dependencies/package | PASS exact versions, ARM/hard-float, ext4/tar agreement, no fixture writer, candidate qualified flags false, USB-only SSH and preserve-data package |
| Source and license inventory | 102 selected nonvirtual packages, 87 remote inputs with strong hashes; Buildroot legal-info passes with documented local/external-package collection warnings |

These suites overlap; counts are not added into a marketing total. QEMU null ALSA constraints do not validate Y2's wider formats. Synthetic ARM/host library results do not establish target timing budgets. The actual installed updater is separately tested from the explicitly test-compiled file fault harness.

Final packaging fixed an unanchored BlueZ `start()` guard that also matched `restart()`, and a validator that mistook the existing Dropbear `ssh` alias for an extra OpenSSH client. Both have targeted regression cases. FFmpeg's license hash now matches the pinned 9.0.2 archive. The supplicant top-level license pin was reverified and preserved after distinguishing it from the different nested README. The initial preflight and intermediate receipts remain labelled by their old source pairs; none substitutes for the final receipts. Host UID/ALSA config namespace and verifier-output harness mismatches were corrected without changing product behavior. No failed intermediate run is presented as a pass.

The installed tree contains 88,666,583 unique regular-file bytes. The inventory's 439,025,495 pathname-summed bytes include 32 repeated hard-link names, chiefly Mesa aliases; they are not that much unique storage. The 512 MiB root image uses 28,676 × 4096-byte ext4 blocks (about 112 MiB), including filesystem metadata. No package was removed from an ELF-reference guess. Buildroot legal-info omits some local/external license collections; Git bundles retain local licensed sources, and pinned Buildroot/Bootlin inputs remain documented. This is not a claim of exhaustive legal review, public firmware redistribution permission, byte-identical rebuilding or absence of all security defects.

## Exact artifacts and owner handoff

The package contains current BOOTIMG/Y2ROOT, one preserve-data scatter, verified previous BOOTIMG/Y2ROOT fallback, manifest and hashes, signed development root OTA, source bundles, build/package/license inventories, validation receipts, benchmark and qualification tools, precision fixtures and owner sessions. **No replacement Y2DATA image** is supplied. The fallback is the older correctness-closure software package, not a physically qualified fallback; it predates the current Reborn integration. Rescue's verified backup of the actually installed previous root is separate from those manual fallback files.````````````

| File | Bytes | SHA-256 |
| --- | --- | --- |
| BOOTIMG.img | 6756352 | f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622 |
| Y2ROOT.img | 536870912 | 970330d24f6a0bddb0cb685d37232b298566c5cd7025a45990566f03c3f66fa3 |
| updates/development-v1/rootfs.ext4.gz | 36852721 | 28a3f46883de71d3687920b5583ea54673a3470b9e02163bb49c834aa5c8ce23 |

`SHA256SUMS` covers the complete assembled package; `manifest.json` binds the manual image pair and `updates/development-v1/manifest.json` is separately signed with Ed25519. Key ID `platform-v1-development-20260923` is development trust, sequence 1, with explicit signed development downgrade and rollback permission. The private key remains outside repositories/artifacts/device in the owner's private signing directory; only its public registry is packaged. A release-key transition or revocation in old rescue requires separately controlled trusted BOOTIMG maintenance. Root-only OTA requires this exact kernel and is not a first-install substitute. Automatic BOOTIMG updates remain excluded because a torn single-slot write can destroy rescue availability.

Owner next actions are precisely grouped in [PLATFORM-V1-OWNER-QUALIFICATION.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-OWNER-QUALIFICATION.md): preserve state/recovery and verify hashes, review the paired manual preserve-data install, then Session A core/recovery/UI/input/S16/USB; B storage/SD/SQLite/library/resources; C Wi-Fi IP/route/DNS/throughput/reconnect; D manual SBC/AVRCP/coexistence. E power and G OTA are separately controlled after their prerequisites. F wider audio remains blocked by missing AFE packing/clock evidence. Complete short sessions before the corresponding 8-hour/cycle workloads. No threshold, watchdog, deep suspend, unsupported rate or VBUS path is enabled automatically.

After owner acceptance of the advertised core, return feature development to Y2Reborn and maintain the platform contract. All current-candidate hardware and endurance rows remain PHYSICAL_GATE until exact owner evidence promotes them. The read-only tracker inventory remains #16/#27/#28/#29/#31/#32/#33/#34 open and prior #30 closed; no remote issue, branch, account or Git identity was changed.

## Historical implementation checkpoints

The remaining entries preserve the order in which work was implemented and validated. Their contemporary pending notes are superseded by the final pair and evidence table above where the code was subsequently completed; they do not reopen fixed issues or grant higher evidence to an unimplemented hardware path.

## Entry audit

Read retained Storage06, GPU-01, CONNECTIVITY-10 and USB reconnect receipts. Internal boot and root/data identity, narrow wired audio and rendering have physical evidence. Same-boot deep resume failed; current USB PM ownership already exists. Association/DHCP/DNS, peer/SBC audio and current charging envelope remain unqualified. Read-only GitHub inventory confirms #16/#27/#28/#29/#31/#32/#33/#34 open, #30 closed; no tracker change is warranted or made. All implementation is owner-authorized by the completion request; no planning epic supplies hardware authorization.

## Implementation and validation

### Low-power/audio boundaries and early evidence

DONE_SOFTWARE / HOST_VALIDATED: readonly native ALSA combination query, exact 24-bit precision/channel fixtures, once-per-boot bounded private previous-log retention and default refusal of unqualified deep suspend. Sixteen targeted evidence/suspend/observation tests pass. No driver masks, voltage, trip point, reserved RAM or SPM code changed. The pinned vendor review and exact remaining proof are in `knowledge/platform-v1-hardware-gates.md`. ARM/image coverage for these new tools follows in the final fresh build.

The USB/update pair `1c2451e` / `f4b83b7` completed fresh kernel, Buildroot ARM, Reborn ARM, FFmpeg/ELF/artifact checks, 42 platform cases (one native host dependency case covered separately), 67 production and 38 subsystem tests, plus eight QEMU userspace checks. Seven actual ARM updater fault tests passed under Cortex-A7 QEMU. The installed ARM SFTP subsystem passed real protocol write/readback, reserve refusal and interrupted-session checks. Host UID and locked-host compiler harness mismatches were resolved without product changes. Receipts: `out/platform-v1-update-build`. These are not physical update/USB proof, and do not cover newer maintenance or phase-7 source.

### Telemetry, health, capability and boot record foundation

DONE_SOFTWARE / HOST_VALIDATED for the implemented observation contracts. `tools/platform/y2_platform` provides versioned JSON, CPU/residency/VM/PSS, die thermal/power, mount identity/space, Wi-Fi readiness, audio/USB/update state, capabilities, bounded queries and boot history. Rescue's stale charging statement is corrected without adding a Python dependency to rescue. Initramfs stages are instrumented, without removing any identity, fsck or recovery gate.

`python3 -m unittest tests.test_platform_contract -v`: 10 pass, exercising source disappearance/reinsertion, counter reset, missing measurements, DHCP timeout, stale DNS epochs, corrupt records, space reserves, previous boot retention, symlink refusal and subprocess deadlines/output bounds. Full health currently adds query-only checks; scratch/SQLite integration follows in phase 2.

ARM_BUILT and IMAGE_VALIDATED are pending a fresh build. No physical/endurance claims. Python target footprint/collection cost need measurement. D-Bus transport observation, richer service fault counters, time readiness and update readiness remain implementation work in their dependent streams. Persistent early crash cause and AP watchdog recovery remain PHYSICAL_GATE / BLOCKED_BY_EVIDENCE; unclean shutdown is never labelled panic or watchdog without evidence.

The first fresh phase-1 build completed the kernel and ARM ABI selftest, then exposed an unexercised BlueZ 5.87 headers-only recipe: Python selects it, but the old recipe installed `lib/*.h` after upstream moved headers to `lib/bluetooth`. The pinned modernization adapter now updates that path. This failed build is retained at `out/platform-v1-observation-build/buildroot-build.log`; it is not an ARM userspace pass. Validation resumes after the focused recipe correction.

### Space, SD lifecycle and storage benchmark tools

DONE_SOFTWARE / HOST_VALIDATED: platform mount claims, failed unmount handling, read-only unmounted checks, low/critical admission reserves, bounded disposable cleanup and descriptor-pinned scratch measurements. Added Linux exFAT and pinned exfatprogs; no controller/electrical change. `python3 -m unittest tests.test_platform_storage_tools tests.test_platform_contract -v`: 19 pass, including actual scratch I/O, generation loss, readback, ENOSPC error propagation, failed eject, exFAT selection, symlink refusal and cleanup exclusions. Tests use host files and fake mount command responses, not physical block devices.

ARM/image validation is pending for this stream. Physical card lifecycle, throughput/latency, flush semantics and endurance remain PHYSICAL_GATE. SQLite, Reborn scaling and long-run resource collection follow; no database policy was optimized without measurements. Detailed contract: `architecture/platform-storage-v1.md`.

### Fresh observation build and measurement continuation

The recipe correction completed the phase-1 build at Linux `82da3f9` / Reborn `d9ba054`. `out/platform-v1-observation-build` retains kernel/ABI, Buildroot ARM, Reborn/FFmpeg verification, artifact validation, production tests and an eight check QEMU userspace pass (`hardware_validation: false`). ARM Python 3.12.14 loaded SQLite 3.53.4/OpenSSL 3.5.8 and exercised fixture status under Cortex-A7 QEMU. Installed target is approximately 74 MiB, including 15 MiB Python standard library. This receipt does not cover subsequent phase-2 source changes or declare a final installation package/image qualified.

DONE_SOFTWARE / HOST_VALIDATED: `y2-platform bench-library` invokes the actual Reborn database, scanner and UI through an inherited, private scratch directory FD. It supports 1k/10k/20k tracks, optional generated short WAV scanning and reserve/inode/deadline checks. Reborn commits `8732287`, `17dd464` implement the benchmark and remove full Track cloning/per-wheel row allocations; track screens build only visible rows. SQLite schema/cache/checkpoint policy is unchanged. Host raw records are in `out/platform-v1-host-measurements`: 20k short-WAV scan 11.7 s, incremental 411 ms; wheel p50 before 2.713 ms / after 0.033 ms (1k: 0.129 / 0.002 ms; 10k: 1.334 / 0.016 ms). Host page cache was uncontrolled; these are neither cold-device nor Y2 budgets. Reborn library benchmark test, 13 UI + 27 runtime tests and four storage tests passed.

`collect` emits bounded JSONL for CPU/residency/memory/thermal/wakeups/services and optional Reborn metrics. Memory growth starts after a chosen warmup and uses boot/PID/start-time identity; its slope is not a leak diagnosis. No workload, radio, suspend or power transition is triggered by collection. The output limit is 64 MiB; retain output on the owner host for long physical runs.

22 platform tests pass, including real SQLite WAL and checkpoint ENOSPC at an injected pwrite boundary and recovery of committed rows after abrupt process exit. The test-only preload shim targets one new private scratch database and is never installed in the image. This is syscall fault injection, not electrical power-loss durability. Prior Reborn operational-error/corruption tests remain applicable; storage replacement tests protect the replacement card via pinned FDs. SD device-instance identity additionally rejects reused block minors.

### Shutdown and normal low-battery mechanism

DONE_SOFTWARE / HOST_VALIDATED: independent supervised power owner, private credential-checked request/ack socket, immutable monotonic deadline, bounded service/journal/sync steps and BusyBox init handoff. Reborn acknowledges only after audio/session/SQLite shutdown; ordinary commands share the platform path. Three focused platform tests exercise ignored app, failed sync/init, stale/PID reuse acknowledgements, daemon restart and synthetic debounce/hysteresis. Reborn runtime/library/platform suites passed, plus a real database checkpoint/close acknowledgement test. No final voltage thresholds or charger changes are made. ARM/image validation is pending. Threshold/reserve and physical power transitions remain PHYSICAL_GATE; see `architecture/platform-power-v1.md`.

### Wi-Fi, time/entropy and platform lifecycle integration

DONE_SOFTWARE / HOST_VALIDATED: epoch-checked DHCP configuration, passive Wi-Fi failure monitoring, bounded DNS probes and fresh service readiness, standard NTP, clock/TLS readiness, persistent per-device seedrng and owner network/throughput helper. Reborn distinguishes authenticated from Online and rejects stale records. SD lifecycle now runs independently of Reborn, including removed-device claim validation and five-attempt failed-unmount bounds. Four network/time and two new SD tests pass; the new Reborn freshness and SD-instance tests pass. This does not qualify RTC, Wi-Fi connections, SD removal or performance on Y2.

Fresh phase-2 ARM build at Linux `5049761` / Reborn `17dd464` completed under out/platform-v1-storage-build; eight QEMU userspace checks and the installed ARM 1k database/scanner/UI benchmark pass. Its first production test run exposed the locked host libc's lack of the obsolete off64_t name in the test-only ENOSPC shim; `44cf4ac` uses the explicit 64-bit ABI type. Rerun is required and recorded below. Phase-3 sources are not covered by this earlier ARM receipt.

### Bluetooth observation and AVRCP foundation

DONE_SOFTWARE / HOST_VALIDATED: native read-only D-Bus observer, typed exact PCM and runtime/mutual capability distinctions, generated build codec inventory that rejects unexpected optional encoder enablement. Four focused host tests pass, including native C compilation/private D-Bus missing-owner execution, peer loss, wrong direction, owner change, unsupported format and accidental AAC enablement. AVRCP in Reborn routes only approved BlueZ calls through semantic Actions; two host tests include real private D-Bus registration, control delivery, metadata projection and unauthorized-sender rejection. ARM/image proof follows later.

The phase-2 production rerun with current host/tooling source passed 32 platform, 67 production and 38 subsystem tests, plus ARM ABI/ALSA utility smoke. This does not promote phase-3 sources to ARM_BUILT: their separate fresh build is ongoing at Linux `ea50d53` / Reborn `ce55f89`, out/platform-v1-services-build.

The phase-3 services build (`ea50d53` / `ce55f89`) completed fresh kernel, Buildroot ARM, Reborn ARM, FFmpeg/package/ELF validation. Its 32 platform, 67 production, 38 subsystem tests and eight QEMU userspace checks passed. Receipts are in out/platform-v1-services-build. No physical qualification.

Reconnect now has bounded attempts, persistent same-boot inhibition, shared user/automatic operation exclusion, and unknown-completion containment. Native host compilation and six Bluetooth tests pass; Reborn's 34 platform tests pass. These newer Bluetooth changes still need the next fresh ARM/image receipt.

Codec Auto has a typed eligibility/session policy and actual SelectCodec control path through Reborn, plus stopped-playback/shared-PCM exclusion. Two policy tests exercise gate/fallback/peer generation/deadline/unknown-completion bounds; the real file-lock test proves open PCM and selection exclude each other. Requested codec never overwrites negotiated PCM. Optional codecs remain unbuilt and distribution-gated, not claimed implemented. See platform-bluetooth-v1.md.

### USB owner transfer and listener security

DONE_SOFTWARE / HOST_VALIDATED: supervised USB-interface-bound key-only SSH, kernel-CRNG startup gate, pinned OpenSSH SFTP subsystem with per-write reserve, private staged/hash-verified/durable/no-replace upload helper. Four contract tests cover interruption/hash/space/identity/symlink/old-FD mutation and SSH prerequisites. The actual patched native SFTP server passed protocol write/close/readback, injected low-space refusal and abrupt session termination. Receipt: /tmp/y2linux-platform-v1-pass/sftp-host-check.json (to be retained in candidate). ARM/image checks follow. ECM cross-OS, reconnect/sleep/transfer and VBUS/role hardware remain PHYSICAL_GATE. No USB mass-storage or host path is enabled.

### Signed staged root update and verified rescue restore

DONE_SOFTWARE / HOST_VALIDATED: native Ed25519/json-c/gzip verification in normal system and immutable rescue; strict root-only/kernel/schema/key policy; bounded HTTPS/local private staging; controller/geometry/exclusive offline writer; actual previous-root backup verified before mutation; fsync/readback, durable journal, exact boot/source/first-frame health and next-boot rollback. Development public trust provisioned; private key exists only outside repositories/artifacts. No BOOTIMG writer. Key rotation/revocation explicitly requires the trusted rescue boundary. See `architecture/platform-update-v1.md` for limitations and commands.

Seven actual C/authentication/stream/staging host fault tests pass, plus ten observation and six PID1 handover tests (including torn-root recovery ordering). Reborn's readiness/capability source passed 37 platform and 27 runtime tests and the library benchmark CLI test. No physical/block device was opened. ARM/image validation for USB/OTA/readiness is pending a new paired build.

The Bluetooth build at `1f54bd0` / `87a46cb` completed kernel, Buildroot ARM, Reborn ARM, FFmpeg/artifact checks, eight QEMU userspace checks and production suites: 38 platform cases (one host dependency case skipped in the locked host; covered separately on the maintainer host), 67 production and 38 subsystem cases. This receipt is `out/platform-v1-bluetooth-build`; USB/OTA code is newer.

### Scoped maintenance and private export

DONE_SOFTWARE / HOST_VALIDATED: distinct settings/network/bonds/library/cache/full logical user reset; confirmation bound to exact scope and inode inventory, quiescent consumer checks, durable quarantine, interrupted-reset startup hold, new-boot resume and explicit bounded purge. SSH/entropy/update/factory/unknown state is preserved. Full logical reset is not secure erasure. Private export includes consistent SQLite backup optionally; WPA credentials require a flag, private keys and Bluetooth bonds are excluded. Five meaningful host tests pass, plus the seven updater tests. Reborn `41214d0` exposes its own settings defaults and refuses normal startup during unfinished maintenance; 27 runtime tests pass. ARM/image validation follows separately. See platform-maintenance-v1.md.

### Integrated endurance and candidate reconstruction

DONE_SOFTWARE / HOST_VALIDATED: owner-controlled passive qualification profiles, exact pair checks, USB disconnect gaps, PID/boot/source generation separation, resource/counter analysis and no automatic physical/endurance acceptance. Reborn PID selection follows restarts; telemetry exposes actual CONSYS/taint without inventing warning/loss counts. Six qualification/measurement tests pass, including actual SQLite faults; 30 combined focused release/evidence/receipt cases pass. The sessions A–G plan is `PLATFORM-V1-OWNER-QUALIFICATION.md`.

Release identity, package contract validation, pinned Rust archive inventory and full selected-package/source/footprint inventory are prepared for the final fresh build. No package was removed on a guessed dependency or image-size basis. Byte-for-byte reproducibility, current-image physical and endurance qualification remain unclaimed. `build/platform-v1-reconstruction.md` records the exact source, owner firmware, signing, privilege and distribution boundaries.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
