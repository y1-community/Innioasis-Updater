---
title: "Bluetooth codec audit: evidence, tests and qualification contract - Innioasis Updater"
description: "Bluetooth codec audit: evidence, tests and qualification contract <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-bluetooth-codecs-2026-09-22-evidence-and-tests.html"
---

# Bluetooth codec audit: evidence, tests and qualification contract - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Bluetooth codec audit: evidence, tests and qualification contract

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Bluetooth codec audit: evidence, tests and qualification contract > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Date: 2026-09-22. Read together with the [architecture and Auto design](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fbluetooth-codecs.md).

This file records what was inspected/executed and separately specifies future tests. A table of expected outcomes is not a passing test suite. No new codec framework, runtime policy tests, cross-build, firmware image, installation, radio activation, pairing or physical measurement was performed.

## 1. Source and artifact identities````````````````````````````````

| Repository / artifact | Identity and scope |
| --- | --- |
| Y2Linux HEAD | be7e64c5dd5c6bdfe39c35e8fbd70e6b4b2c4717; initially clean |
| Y2Reborn HEAD | 011884b7ef13187171225f252c213afeeb6da851; pre-existing untracked docs/audit/ from the completed system review retained |
| Retained platform output inspected | Y2Linux/out/y2linux-reborn-audio-final/buildroot/; an existing local build, not a build produced or installed by this audit |
| BlueALSA source/config | build/bluez-alsa-4.3.1, generated config.h, src/bluealsa-iface.xml, src/bluealsa-dbus.c, src/a2dp*.c, src/codec-*.c, version-specific manuals |
| BlueZ source/config | build/bluez5_utils-5.79, generated config.h, profiles/audio/a2dp.c, MediaEndpoint/MediaTransport documentation |
| Target executable/config | target/usr/bin/bluealsa; target/etc/alsa/conf.d/20-bluealsa.conf |
| Pinned Buildroot package source | Y2Linux/.cache/sources/buildroot-2025.02.17/package/ |
| Running device | Not accessed in this audit. Current installed commit and connected headphone are UNKNOWN |

Relevant history inspected, not treated as validation:
  - Y2Linux `f55fff4`: hardware-identity-scoped extended-feature-page quirk.
  - Y2Linux `72d4831`: Reborn/Buildroot/native media integration.
  - Y2Linux `79a3d38`, `270dba3`, `80df0ff`: FFmpeg 9 integration/configuration.
  - Y2Reborn `77e6732`: current BlueALSA ObjectManager and exact-peer PCM rates.
  - Y2Reborn `a8ae8b6`: radio scan lifecycle.
  - Y2Reborn `65c6ea0`: shared FFmpeg 9 media path.

No root `README.md` exists in either checkout; architecture, knowledge, version-specific upstream manuals, validation evidence and actual source were used. Missing guessed filenames during discovery were corrected by file listing; they were not counted as product defects or test failures.

### Production-source anchors[](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/configs/y2_production_defconfig)[](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/inputs.lock.json)[](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/libexec/y2/connectivity)``[](https://github.com/SchulzCode/Y2Linux/blob/main/tools/connectivity/reconnect.c)[](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/hci.c)````````[](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/stp.c)[](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/btif.c)[](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/firmware.c)[](https://github.com/SchulzCode/Y2Linux/blob/main/tools/connectivity/factory.c)[](https://github.com/SchulzCode/Y2Linux/blob/main/docs/knowledge/evidence/m5-firmware-inventory.json)[](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/bluetooth.rs)````[](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-audio/src/native.rs)````[](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-media/native/media.c)````[](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs)````[](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/playback.rs)[](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs)[](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-core/src/lib.rs)``[](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/ctl.rs)``

| Question | Authoritative source |
| --- | --- |
| Image package selection | defconfig, input lock |
| Actual Bluetooth service | connectivity service: both launch/restart use /usr/bin/bluealsa -p a2dp-source --loglevel=warning |
| Connection retry owner | reconnect.c: trusted preferred AudioSink, intentional-disconnect handling, 45-s call timeout, rate-limited recurring retries |
| Controller identity/quirk and data path | hci.c: setup, controller_quirks, send, y2_hci_receive; STP, BTIF |
| Firmware and private calibration | firmware.c, factory.c, inventory |
| Current app observation | bluetooth.rs: Status::playback_rate, status, tests; no GetCodecs/SelectCodec/typed codec policy |
| Current Bluetooth PCM format | native.rs: output_name, AlsaSink::plan_named; S16 preference for Bluetooth |
| Shared media precision | media.c: canonical_swr, output_swr, graph and crossfade paths |
| Playback lifecycle | main.rs: Runtime::load, output_rate; playback.rs: load/stop, generation/cancellation and sink tests |
| UI codec string / disconnected state | main.rs PCM codec binding; coreEvent::BluetoothDisconnected |
| Actual command grammar | ctl.rs: Bluetooth commands currently on/off/scan, not bluetooth status |

## 2. Sanitized hardware evidence

These are selected non-identifying fields read from retained own-Y2 logs. The original source is local/private; no full captures are copied, and no link keys, peer addresses, pairing passkeys or calibration payloads were inspected.

Source: `Y2Linux/evidence-private/20260917-m5-protocol/connectivity08-hci-baseline.txt`.``````

| Lines | Response | Selected fields |
| --- | --- | --- |
| 39–84 | Read Local Supported Features, status success | bf 3e 8d fe db ff 5b 87; EDR ACL 2/3 Mbps, 3-/5-slot EDR ACL, AFH central/peripheral, LE controller, simultaneous LE/BR-EDR, SSP |
| 89–94 | Read Local Version Information, status success | HCI 4.0 0x06, revision 0; LMP 4.0 0x06, subversion 0; MediaTek manufacturer 70 |
| 266–269 | Read Buffer Size, status success | ACL MTU 1021, ACL packets 4; SCO MTU 184, SCO packets 1 |

The independently retained `y2-hci-quirk-capped.txt` reports the same capabilities after the diagnostic feature-page correction. That does not mean its tainted diagnostic boot was production-qualified. The [CONNECTIVITY-09 public summary](https://github.com/SchulzCode/Y2Linux/blob/main/docs/hardware-evidence/2026-09-17-m5-connectivity09/adapter-result.json) records durable native-quirk power-on with no diagnostic module, taint 0 and zero errors/recoveries. The [CONNECTIVITY-10 summary](https://github.com/SchulzCode/Y2Linux/blob/main/docs/hardware-evidence/2026-09-17-m5-connectivity10/adapter-result.json) records scans with both radios powered, not A2DP data.

The raw HCI features settle advertised capability, not the controller's actual air packet type with a particular sink. No retained connection packet- type, retransmission, sustained credit-progress or headphone transport trace establishes usable EDR audio throughput. Do not convert the 1021×4 buffer report into a throughput benchmark.

### Actual peer evidence

[Reborn's September 18 inspection](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2F2026-09-18-radio-inspection.md) used an older deployed Reborn revision `6209f48402a00a077759df042916f0ae2c89783a`. Its Bluetooth service check found no connected peer; discovery completed with zero discoverable peers. The retained [BlueALSA ObjectManager response](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/bluealsa-objectmanager.txt) is an empty PCM array. It proves the API exists, not a working audio stream.

Therefore the current connected-headphone make/model, advertised optional codecs, accepted rate/format, negotiated codec and heard audio are UNKNOWN. A headset marketing specification cannot substitute for its actual SEP advertisement; multipoint/firmware modes may change what it offers. No peer was connected by this audit just to fill that cell.

## 3. Ten distinct capability levels

"Plausible" below means a portability assessment, not a build result. "Pending" legal assessment does not assert illegality. "Not observed" does not prove a codec fails.

| Level | SBC | AAC | aptX / HD | LDAC |
| --- | --- | --- | --- | --- |
| 1. Upstream BlueALSA source support | Yes | Yes | Yes / Yes | Yes |
| 2. Linux encoder/library available | libsbc | FDK-AAC | Several distinct implementations | AOSP encoder + ABR |
| 3. ARMv7 target build evidence | Yes, retained ARM image | Buildroot ARM supported; not built here | Buildroot portable recipe / alternate library plausible; not built here | Portable source; no Y2 package/build |
| 4. Enabled in reviewed image | Yes, normal high setting | No | No / No | No |
| 5. Negotiated with real Y2 peer | Not observed | Not observed | Not observed | Not observed |
| 6. Real-time MT6582 encoder measurement | Missing | Missing | Missing | Missing |
| 7. Stable over actual Y2 radio | Unqualified | Unqualified | Unqualified | Unqualified |
| 8. Stable with active Wi-Fi | Unqualified | Unqualified | Unqualified | Unqualified |
| 9. Public binary distribution cleared | Library terms known; product/firmware obligations open | Patent/FDK obligations pending | Exact library/IP decision pending | NOTICE/certification/product decision pending |
| 10. Production-ready Y2 feature | No evidence sufficient | No | No | No |

The full codec matrix in the architecture document covers LHDC, LC3plus, MP3, Opus, FastStream, aptX extensions and LE Audio separately.

## 4. Checks actually executed in this focused audit

All commands were host-side. Existing binaries were run without recompilation; their relationship to HEAD was not independently rebuilt/proven. No result is reported as a fresh production build or physical qualification.

### Focused cached tests

Working directory `/home/luca/Dokumente/Code/Y2Reborn`:`./target/debug/deps/reborn_platform-a0dab0805802cc10 bluetooth::tests:: --test-threads=1 ./target/debug/deps/reborn_audio-610cef8b7603caee --test-threads=1 ./target/debug/deps/reborn-569a8d6f5e5b2b9d --test-threads=1`

| Existing suite | Result | What it actually tests |
| --- | --- | --- |
| Bluetooth adapter | 5 passed, 0 failed, 15.15 s | Discovery deadline/order/failure; fake-D-Bus worker; exact peer/direction/stereo-rate matching; unavailable/unsupported rejection |
| Audio adapter | 2 passed, 0 failed | Address cannot inject PCM options; nonexistent PCM returns error |
| Playback worker | 6 passed, 0 failed, 2.21 s | Synthetic sink/source continuity, separate crossfade behavior, bad-next skip, sink failure propagation, stop/output-switch generation handling |

Total: 13 cached host tests passed. They do not test optional encoder initialization, actual SBC streaming, BlueZ/BlueALSA reconfiguration against real daemons, codec ranking, hysteresis or RF conditions. No Auto policy tests exist as an implementation yet. The playback fixture limitations and known failures identified by the previous broad audit are not dismissed by these passes; see [validation audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F09_TEST_VALIDATION_AUDIT.md).

A preliminary audio-test invocation used a nonexistent cached-binary suffix and returned exit 127. File discovery corrected it to the command above. This was an invocation error, not a failed codec test. The nonexistent-PCM test emits an expected ALSA error line while passing its assertion.

### Build/configuration inspection

Working directory `/home/luca/Dokumente/Code/Y2Linux`:`rg -n 'VERSION|ENABLE_.*(AAC|APTX|LDAC|MPEG|MP3|SBC|LC3|OPUS|FAST)' out/y2linux-reborn-audio-final/buildroot/build/bluez-alsa-4.3.1/config.h rg -n '^#define (VERSION|PACKAGE_VERSION)' out/y2linux-reborn-audio-final/buildroot/build/bluez5_utils-5.79/config.h readelf -d out/y2linux-reborn-audio-final/buildroot/target/usr/bin/bluealsa`

Observed BlueALSA version v4.3.1, BlueZ 5.79; optional codec macros undefined. ELF NEEDED list: libasound, libbluetooth, libgio, libgobject, libglib, libsbc, libm, libc, ARM hard-float loader. No FDK/aptX/LDAC/Opus dependency. Generated configuration and source checks complement the ELF result: the absence of a shared dependency alone would not rule out a static encoder.

Additional read-only inspection: Git status/revisions and focused history; Buildroot recipes/config; HCI/BTIF/STP/firmware/reconnect code; BlueZ SEP source; BlueALSA D-Bus/XML/codec source/manuals; Reborn media/PCM/UI/ctl paths; sanitized retained HCI fields. Upstream primary-source browsing checked current codec support, official encoder source and licensing notices. For AOSP pages that the browser could not fetch, read-only `curl ...?format=TEXT | base64 -d` was used; no dependencies were downloaded into or installed in either repository.

### Explicitly not executed

No `cargo build/test` compilation, Buildroot/kernel build, target codec benchmark, SSH/device access, scan, pair, connect, transport reconfiguration, suspend, flash, partition access or calibration change. No legal clearance was obtained. No new candidate artifact or commit was produced. Documentation links/structure and final worktree scope are checked separately before handoff.

## 5. Deterministic policy tests to implement — NOT EXECUTED

Tests must call the future production policy/state machine, not an independent lookalike implementation embedded in the test. Use fake monotonic time and a fake backend with recorded calls; no sleeps, network, HCI or real headphone needed. Freeze policy revision and build/qualification allowlists in each case.``

| ID | Input / event sequence | Required assertion |
| --- | --- | --- |
| P01 | Local/remote SBC only, production allowlist SBC | Choose conformant SBC High; actual remains unknown until PCM observation |
| P02 | Remote SBC/AAC/LDAC, local same, all gates pass, baseline-known peer, quiet context, quality extension present | Capped Adaptive Standard LDAC selected; not 990, not automatically 96 kHz |
| P03 | Same codecs, first unknown device | SBC baseline this session; no high-codec exploration without lab profile |
| P04 | Remote LDAC, local SBC/AAC only | LDAC never a candidate; remote list still honestly records it |
| P05 | Local compiled LDAC but runtime Manager1 disables it | LDAC absent from usable candidates; UI cannot request it as available |
| P06 | LDAC legal or context-qualification gate false | Exclude LDAC even when library/remote support exists |
| P07 | SBC/AAC/LDAC, LDAC already suppressed, AAC allowed | AAC then SBC High/Conservative; no LDAC retry this session |
| P08 | Manual AAC, both sides and gates support it | Attempt AAC first; preference separate from observed active codec |
| P09 | Manual LDAC but peer lacks it | Reject newly requested setting without interrupting working audio; retained old preference marked unavailable, explicit fallback status |
| P10 | Preference LDAC, SelectCodec returns success, observed codec SBC | Report actual SBC, reason negotiated-different; never display LDAC active |
| P11 | Remote SEP inventory missing, currently observed working SBC | Capabilities Unknown, not fabricated singleton; keep actual SBC |
| P12 | Device has two equal codec IDs with disjoint rates | No invented union configuration; use supported API-representable endpoint or skip candidate |
| P13 | Unknown vendor ID / too short / oversized / wrong-type capability blob | Bounded rejection or diagnostic Unknown; no panic or selectable arbitrary string |
| P14 | Only remote HFP PCM or wrong device/direction present | Never open it as A2DP playback |
| P15 | LDAC PCM S32 observed | SinkSpec S32; no S16 intermediate; rate from actual PCM |
| P16 | aptX HD PCM 0x8418 | Signed 24-in-4-byte packing, not S24_3LE/S32 alias; unsupported adapter fails candidate |
| P17 | Actual PCM format/channel/rate is unsupported | Explicit failure, no silent ALSA plug conversion represented as native support |
| P18 | 24/96 source, LDAC peer allows 48 and 96, only 48 qualified | Choose 48 sink; single final resampling; no source precision narrowing before final conversion |
| P19 | Queue moves 44.1→48→96 sources during stable 48-kHz session | Bluetooth codec/rate unchanged; no avoidable gapless renegotiation |
| P20 | One Wi-Fi scan and no audio failures | No codec reconnect or persistent penalty |
| P21 | Active-traffic classifier crosses threshold then briefly falls | Congested context held 60 s; no context flapping or live codec promotion |
| P22 | Active Wi-Fi, no coex-qualified high codec | AAC → aptX → SBC candidate ordering after gates |
| P23 | Measured CPU budget excludes AAC/LDAC/HD | Candidate set constrained; no claim that aptX is cheaper without measured evidence |
| P24 | Stock 4.3.1 API without quality extension | No capped-adaptive candidate; fixed experimental LDAC only if explicitly configured; bitrate unknown |
| P25 | SBC XQ requested but peer/config unsupported | Normal SBC preserved; no NonConformant call or global fallback restriction |
| P26 | Compiled codec inventory disagrees with daemon/version | Fail closed for optional codecs; SBC only if actually usable; actionable inventory mismatch |
| P27 | Firmware/encoder/capability fingerprint changes | Device learning marked stale; old success does not waive new gates |
| P28 | First SBC session reaches 30 stable minutes, then next connection session begins | No upgrade during baseline session; next session may select qualified optional codec. Baseline success alone never permanently locks Auto to SBC |

### Fallback and no-flapping tests — NOT EXECUTED

| ID | Injected sequence | Required outcome |
| --- | --- | --- |
| F01 | SelectCodec explicit unsupported | One failed attempt, then next candidate; bounded reason |
| F02 | Encoder startup error | Immediate candidate failure; no false Running or invented detailed encoder code |
| F03 | Select accepted but PCM never appears | Startup deadline fires, total 45-s budget respected |
| F04 | First candidate fails; final SBC opens and advances | Playback resumes same logical track/settings; preferred/actual remain distinct |
| F05 | One recoverable XRUN | Local recovery only, no downgrade |
| F06 | Three independently attributed stalls at 0/20/40 s | One downgrade, not three; symptoms within 2 s count once |
| F07 | Source queue empty from SD removal / corrupt decode | Pause/source error; zero codec penalties |
| F08 | BlueALSA loses bus owner then returns | Old callbacks invalid; inventory refreshed; at most one same-candidate retry |
| F09 | PCM path reused after reconfiguration | New owner/connection/sink epoch required; old Format cannot leak into new open |
| F10 | Disconnect while selection pending, then user Stop | No open/resume after Stop even if late SelectCodec succeeds |
| F11 | User pauses during fallback | Restored sink remains paused |
| F12 | Manual radio Off / Forget | All timers cancel; no retry, re-pair or stale cache resurrection |
| F13 | Two near-start unexplained disconnects in 120 s | Suppress suspect candidate across rapid reconnect; do not create competing Connect loop |
| F14 | Headphone intentionally switched off | No codec failure penalty based on known intentional reason; audio pauses safely |
| F15 | Every candidate fails | ≤6 distinct candidates, ≤7 total attempts including restart retry; ≤45 s startup; one exhausted event and no automatic restart loop |
| F16 | Fatal write failure during cooldown | May move to untried candidate immediately; cannot retry a visited one |
| F17 | Working but suspect stream before 60-s reconfigure limit | No early codec switch; available in-encoder quality reduction may proceed |
| F18 | For 600 simulated seconds, oscillate scan/traffic/CPU flags after LDAC→AAC→SBC failures | No return to LDAC/AAC; no background upgrade; candidate attempts and call count bounded |
| F19 | Reconnect repeatedly less than five minutes apart | Same session visited set persists; reconnect cannot defeat F18 |
| F20 | Reboot after two recorded failures | Suppression/session counter retained; not a fresh high-mode experiment |
| F21 | User explicitly Retry preferred | Exactly one new bounded attempt set; serialized with existing work |
| F22 | Platform helper reconnects after codec Exhausted | Link may reconnect, but no automatic codec-audio restart; exhausted state persists |
| F23 | Bluetooth fallback would select wired output | No unexpected audible speaker/wired playback; pause intent and volume safety preserved |
| F24 | Rapid queue edit/skip/output switch during reconfiguration | Latest authoritative queue/intent wins; stale PCM discarded; no deadlock or orphan writer |
| F25 | LDAC ABR tries above qualified ceiling | Encoder-side cap enforced; if enforcement unavailable, mode cannot be advertised as capped |
| F26 | ABR mode feedback absent | UI/JSON bitrate null; no 660-kbps claim from requested preference |
| F27 | Optional codec timeouts consume first 30 s | Reserve final 15 s for SBC; no optional attempt consumes the mandatory fallback window |
| F28 | Timed-out remote SelectCodec completes late | No concurrent selection race; reconcile or exhaust within budget; stale completion never replaces active truth |
| F29 | Codec fails after hours of successful playback | New recovery deadline is 45 s from that failure, not the expired startup deadline; session visited/attempt budgets are retained |
| F30 | Successful SBC/optional codec reconnects within five minutes without codec failure | Reopen validated current PCM once in the new epoch, no new SelectCodec or forced downgrade merely because it was previously visited; preserve pause intent |
| F31 | Unexpected link loss and both automatic profile reconnect requests time out | Connection owner stops within its 25-s budget; no overlapping remote calls, recurring minute timer or reset of codec failures |

No-flapping property: automatic visited sets are monotone for a fallback session; next candidate is always unvisited; finite budget implies termination. Property- based event sequences must check that invariant, finite queues, preserved Stop, and at most one live sink writer. Test late/reordered/duplicate D-Bus events, clock jumps, device changes and service restarts—not only happy-path ranking.

### Persistence and real-format integration tests — NOT EXECUTED
  - Truncated JSON, unknown schema, atomic-write interruption, full/read-only

filesystem: safe Unknown/Auto behavior, existing bonds untouched, bounded errors.
  - 33rd paired device and oversized codec arrays: documented eviction/bounds;

repeated status polling does not write state; unchanged state does not fsync.
  - Forget removes only that device's profile; no raw address/key in exported JSON.
  - Actual BlueALSA/BlueZ test harness captures versioned D-Bus signatures and

SelectCodec-caused object replacement; fake fixtures must be based on captured sanitized real responses, not assumed capabilities invented by the test.
  - S16/S24-in-4/S32 boundary vectors: zero, ±full scale, ±one LSB, clipping,

channel order, silence and dither/noise expectations. Verify exact slave format and samples before encoder; ALSA plug acceptance alone is inadequate.
  - Decode both 16/44.1 and 24/96 fixture signals through the same RG/EQ path

to wired/Bluetooth sink capture; compare pre-sink canonical samples, accounting for intentional sink quantization/rate changes. No second BT DSP path.
  - Gapless/crossfade at constant negotiated rate with real media fixtures, encoder

delay/padding, queue edits and decoder cancellation; separate codec-change interruption from normal track-boundary continuity. Do not claim no regression from synthetic short fixtures alone.

## 6. Physical qualification plan — NOT EXECUTED

### Entry gates and test identity

Follow Y2Linux's [standing milestone audit rule](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) before expanding codec/production scope. Use owner-authorized installation and radio actions. An outstanding power/thermal/suspend safety gate is not waived by this plan. Do not conduct unbounded heat/battery stress on an unqualified charging/thermal platform, and do not invent safe temperature thresholds from the currently unqualified sensor readings.

Record board/controller identity, kernel/rootfs/Reborn commits, manifest and artifact hashes, BlueZ/BlueALSA/encoder versions/options, headphone model and firmware, distance/orientation, negotiated SEP/PCM/rate/codec, AP/channel/RSSI and traffic description. Use private peer IDs; anonymize public evidence. Use boot/session IDs and monotonic time—retained Y2 wall time is unreliable.

Start with a fresh SBC-only or SBC-capable bond and a second independent peer; then use real AAC, aptX/HD and LDAC peers as available. For each codec report which exact peers were tested, not "all Bluetooth headphones". If no matching peer exists, mark that codec BLOCKED/UNKNOWN, not passed with a mock.

### Cross-product matrix

Each enabled production codec/mode runs every applicable lifecycle row in all four Wi-Fi conditions. This is a matrix, not four separate unrelated milestones.

| Wi-Fi state | Controlled condition | Additional acceptance evidence |
| --- | --- | --- |
| Off | Wi-Fi off, BT audio active | Baseline radio/encoder budget |
| Connected idle | Real WPA2 association/DHCP complete, no intentional transfer | Confirm background traffic and negotiated network state, not scanning alone |
| Active traffic | Controlled bidirectional LAN transfer with measured rates; record AP channel | Audio remains usable; measure Wi-Fi throughput degradation, not just audio |
| Repeated scans | Bounded repeated scans at recorded cadence, e.g. every 15 s for 10 min | Audio/credit progress during scans; no global-radio reset or codec flapping |

| Lifecycle / fault | Minimum proposed exercise | Pass evidence |
| --- | --- | --- |
| Fresh pair/bond | Clear only owner-approved test peer bond, pair normally, verify trust choice | Pairing confirmation, private persistence, A2DP capability/codec observed |
| Initial connect / reconnect | 10 cycles each per representative peer | No manual daemon restart, false active state or competing retry owner |
| Y2 reboot | 5 cycles with existing bond | Correct preference, actual codec and history; no key leakage |
| Headphone reboot / range loss | 5 cycles each, user stop/off also exercised | Bounded recovery; intentional off respected; no surprise wired playback |
| Track changes | At least 100 boundaries including 44.1/48/96 source mixture | Constant sink where intended, no queue corruption, no codec reconfigure per track |
| Pause/resume / seek / skip | 30 operations each including transition races | No stale audio, deadlock, stuck transport or incorrectly resumed pause |
| Screen on/off | 30 cycles during sustained audio | Input/render/power activity does not starve encoder; no dependency on visible UI |
| Output switching | 20 wired↔Bluetooth cycles, including remote loss | Sink closed before new open, correct format/volume, one writer, bounded interruption |
| Long playback | At least 2 h per codec/context; 8-h SBC and selected Auto soak | No audible unexplained dropouts, transport reset, memory growth or unbounded retry |
| DSP load | RG Off/Track/Album, EQ, gapless and crossfade fixtures | Same pre-sink processing; no codec-dependent bypass |
| Source loss | Owner-approved SD removal/corrupt media test | Classified as source failure; Bluetooth history not poisoned |
| Service failure | Controlled bluealsa/BlueZ restart in test environment | Epoch invalidation, honest status and bounded recovery |
| Suspend/resume | Only where platform policy permits; otherwise assert playback veto | Same-boot resume/reconnect qualified or explicit unsupported/vetoed result |

Do not force deep suspend while playback owns an active radio if the platform contract vetoes it. "Veto correctly applied" and "Bluetooth playback survives deep suspend" are different results. Headphone AVRCP controls are another currently missing application integration; codec qualification does not prove them.

### LDAC matrix

Test each independently at 44.1 and 48 kHz first; add 88.2/96 only in a separate experimental high-rate pass. Repeat every Wi-Fi context above.

| Mode | Payload family | What to verify |
| --- | --- | --- |
| Connection Priority fixed | 303/330 kbps | Actual encoded rate, listening/stability; not simply an option string |
| Standard fixed | 606/660 kbps | EDR/credit progress and sustained sharing |
| High fixed | 909/990 kbps | Stress/error margin, distance/orientation, coexistence; never infer pass from a 30-s clip |
| Stock ABR | Can reach high and intermediate modes | Queue response, actual mode over time, oscillation, dropouts; do not call it capped |
| Proposed capped ABR | Enforced maximum Standard or device-tested lower cap | Cap never exceeded, same-codec adaptation before fallback, actual mode telemetry and no repeated reconnects |

Measure disconnects, audible dropout count/duration, ALSA XRUNs, output starvation, BlueALSA write failures, HCI credit progress, kernel transport errors/recoveries, CPU per process/thread, RSS, temperature validity, power and available battery data. Actual over-air packet loss may be unavailable; label local proxies.

### MT6582 CPU/memory benchmark

No usable per-codec target measurements were found or made. Cortex-A7 has NEON and the current toolchain targets hard-float `neon-vfpv4`; portable C buildability does not guarantee enough single-thread deadline margin at the production CPU frequency. Do not reuse a Cortex-A53/x86 encoder result as a Y2 number.

Benchmark two things separately:
  - Encoder-only fixed PCM input at 16/44.1, 16/48, 24-bit sink input where

applicable, and LDAC 24/96 experimental. Pin exact encoder build/options; measure CPU-time/audio-time ratio, frame-time distribution and memory. A faster-than-real-time offline encode is necessary but not sufficient.
  - End-to-end playback, same tracks through actual FFmpeg/RG/EQ/resampler,

ALSA plugin, encoder, radio and headphones. Measure bluealsa threads, Reborn, kernel/IRQ cost, source scanning and UI load concurrently. Measure effective CPU frequency/throttling, not just aggregate utilization across four cores.

Compare SBC High and Conservative, AAC 220/256 with afterburner off/on as an engineering variable, aptX, aptX HD, LDAC fixed modes and ABR. Include silence, music, transient-rich and high-entropy inputs; warm up 60 s, then collect at least 10 min steady-state CPU statistics and the longer RF soak above.

Initial engineering acceptance targets, **proposed and subject to platform budget review**: encoder average ≤35% of one available core at qualified production frequency; 99th-percentile encode time ≤50% of its frame deadline; no missed deadlines, unbounded queue/RSS growth or critical playback-thread starvation under UI/scanner/Wi-Fi load. Record maximum and tail, not just mean. A mode exceeding the allocated power/CPU budget stays experimental even if it can play briefly. Do not hide a saturated single encoder thread inside a low four-core aggregate percentage.

Memory expectations are modest streaming frames for SBC/aptX; FDK/LDAC/Opus have additional encoder state; LC3plus exposes size/scratch queries. These estimates are not measured RSS. At 48 kHz stereo, 100 ms of PCM is 19.2 kB for S16 or 38.4 kB for S32; at 96 kHz S32 it is 76.8 kB. Those simple bounds show that seconds of speculative PCM and duplicate pipelines are unnecessary. Measure actual ALSA/pipe/socket buffers and allocations; library working state and thread stacks are additional. Do not allocate encoders for every candidate simultaneously.

### Battery and thermal comparison

Compare codec settings against SBC on the same device/peer/source, screen off, same Wi-Fi condition, listening level, ambient temperature and measured CPU frequency. Repeat runs and report variance. Include 16/44.1 and 24/96 source decode/resampling costs separately from encoder-only cost. If battery current telemetry is not calibrated/reliable, use a qualified external power method or mark energy UNKNOWN; do not infer a battery-life percentage from CPU alone.

Record surface/validated sensor temperature and platform charging state; do not perform a prolonged connected-charger soak until the charging/thermal boundary is safe. A proposed initial quality-mode budget is ≤15% energy increase over SBC under matched conditions; this is a product decision to validate, not a measured result or safety limit. A much costlier mode should be manual/experimental or excluded rather than chosen automatically for branding.

## 7. Manual inspection and installation guidance

### Safe current inventory, no new installation required

On an already owner-accessible Y2, these read-only commands can identify the actual current stack. They were not executed on hardware in this audit:`bluealsa --version bluetoothd --version bluealsa-cli status bluealsa-cli list-pcms rebornctl status --json rebornctl audio --json dbus-send --system --print-reply --dest=org.bluealsa /org/bluealsa org.freedesktop.DBus.Properties.GetAll string:org.bluealsa.Manager1`

Some installations put `bluetoothd` outside PATH; resolve its known installed service executable first rather than claiming a missing daemon. If PCMs exist, use their actual returned path with `bluealsa-cli info PCM_PATH` and `bluealsa-cli -v codec PCM_PATH`without a CODEC argument. In 4.3.1 that is query-only. Adding a codec argument is a state-changing operation that terminates the existing PCM. Do not use `--force`. Keep peer identifiers/private state out of shared output.

Remote MediaEndpoint1 capability observation is via BlueZ ObjectManager on the system bus; no need to read bond files. Do not run `scan on`, power commands, connect, trust or pair as part of a read-only inventory. If no PCM exists, report that fact; do not invent the remote capability list.

### Later owner-controlled qualification/install sequence
  - Confirm current recovery arrangement and platform safety gates. The existing

[installation overview](https://innioasis.app/guides/reborn-y2linux-y2.html) distinguishes first initialization from preserve-data updates and warns about historical coordinate errors. Use the chosen candidate package's verified install/recovery metadata, not historical addresses or a generic scatter/flash recipe from this codec document.
  - Collect current readonly inventory and agree on actual test headphones.
  - After separate implementation/legal approval, build one codec candidate at a

time through the existing Y2Linux production workflow. Record both commits, source/encoder hashes, generated manifest, image sizes/hashes and recovery fallback. No candidate exists from this audit.
  - The owner chooses/executes the validated userspace/root-image installation

workflow. Codec work should not require preloader/LK, partition-table, NVRAM, protected-data or calibration updates. If it appears to, stop and re-audit the scope rather than improvise flashing commands.
  - Owner authorizes radio activation, fresh test-device pairing/trust and quiet-

volume playback. Capture capability and actual negotiated PCM before any benchmark. Run the relevant matrix; retain sanitized receipts, not secrets.
  - If failures occur, stop on SBC or pause audio, preserve diagnostic evidence,

and use the existing known-good recovery path. Do not solve RF instability by modifying calibration or hiding EDR feature bits.

There is deliberately no `dd`, scatter-file edit, protected-partition instruction or installation command here. The output of this task is a review/design and qualification contract, not a flashable release.

## 8. What to keep stable

Keep one kernel CONSYS owner, standard HCI/BlueZ interfaces, private read-only calibration provisioning, mandatory SBC, explicit-peer PCM matching, the common FFmpeg media/DSP path, generation-based playback cancellation, bounded worker channels, and the existing structured observability framework. Extend the real service boundary; do not create another decoder, another radio owner, a codec "AI" selector, or a background fleet of encoders.

## 9. Handoff scope

Documents created by this focused task:
  - `docs/architecture/bluetooth-codecs.md`.
  - `docs/audit/bluetooth-codecs/2026-09-22-evidence-and-tests.md`.

The previous system connectivity audit's daemon spelling is corrected to the actual v4.3.1 name and linked to this focused review. All other previous audit material and all production files remain untouched. No commits were made; HEADs remain the identities above. No production artifact or installable package was built. The next implementation decision belongs after the documented hardware and distribution gates, not after treating this document as a passing test.

Final documentation checks: 59 relative local links resolve; 21 Markdown tables have consistent column counts; fenced blocks are closed; the illustrative JSON parses. A targeted scan found no copied Bluetooth addresses, key material or unfinished placeholders. These are documentation checks, not codec validation.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
