---
title: "Platform v1 owner qualification - Innioasis Updater"
description: "Platform v1 owner qualification <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-platform-v1-owner-qualification.html"
---

# Platform v1 owner qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform v1 owner qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform v1 owner qualification > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

This plan is for the exact pair in the candidate's `metadata/versions.json` and `manifest.json`, with image identities in `SHA256SUMS`. No physical test has been performed by the completion pass. Record each result as PHYSICALLY_QUALIFIED only for the observed scope; endurance needs its own duration/workload receipt. An untested or failed row remains PHYSICAL_GATE. Do not generalize one peer, card, PC, power source or short playback to all devices or long-term reliability.

## Before the first session
  - Preserve important state with the current supported backup/export procedure.

Review the candidate and fallback hashes locally with `sha256sum -c SHA256SUMS`. Preserve the owner recovery path and existing protected-partition backups.
  - The owner may install the paired BOOTIMG + Y2ROOT through the established

preserve-data SPFT procedure. Only BOOTIMG and ANDROID are selected. There is no Y2DATA replacement, repartition or protected-partition write. Single-slot BOOTIMG replacement can lose rescue if torn; it remains a separately controlled manual action. This plan does not make that operation atomic.
  - Use the existing owner key and independently verified host key. USB host

address is 10.42.0.2/24, never-default; device is 10.42.0.1. No Wi-Fi SSH is enabled. Confirm `y2-status system --json` identifies the exact candidate kernel, both commits, rootfs release and boot ID before doing a test.
  - Save `y2-platform capabilities`, `y2-health --full --json` and private

`dmesg -r` before/after each session. Unknown readings stay unknown. Save `y2-platform boot-evidence` after an unexpected restart; it may contain private log text. Do not export calibration, NVRAM or bond material with public logs.

Stop a session on unexpected heat, voltage/protection fault, repeated reset, filesystem error/read-only transition, kernel warning/Oops, lost recovery access, or behavior outside its declared operating envelope. Preserve evidence and return to the known recovery procedure; do not retry destructive steps blindly. No automatic watchdog, suspend, battery threshold or unsupported audio/USB mode is enabled by this plan.

## Collection and acceptance records

Local planning does not contact Y2:`python3 tools/host/qualify.py capture --profile wired-8h \ --versions out/y2linux-platform-v1-candidate/metadata/versions.json`

The owner can add `--run --output PRIVATE_FRESH_DIRECTORY --private-key KEY --known-hosts VERIFIED_FILE` to collect over USB. It polls readonly status every 30 seconds, reports SSH cost, retains disconnect gaps, and refuses a changed source pair. Profiles select labels/duration/instructions; they do not start a workload or operate hardware. `analyze samples.jsonl` reports measured maxima, counter deltas, resets, boot/mount transitions and per-process growth after a 60-second warmup. It never declares physical or endurance success automatically. A source change during OTA needs a new capture bound to the new versions file.

For lower collection overhead during a continuous connection, the owner may stream `y2-platform collect --seconds 28800 --interval 30 --warmup 60 --reborn --pss --workload wired-8h` directly to a private host file through pinned SSH. This automatically follows the actual Reborn PID/start time. A disconnect ends that stream, so use the polling profile for cable/reboot cycles. Both paths cap JSON output at 64 MiB. A cap, interruption or missing samples is incomplete coverage. No automatic data-volume fill or unbounded local log is needed.

Annotate workload/media format/hash, dataset count, card/peer/source/PC identity, settings, wall and monotonic time, manual actions, audible/visible results and expected recovery deadline. Standard counters do not measure radio packet loss, pack current or energy. Compare collection overhead itself and repeat a short baseline without polling before attributing wakeups or performance to the app.

## Session A — core (short, supervised)
  - Verify normal boot, root/data UUID/controller/geometry, separate mounts and

clean filesystem counters. Compare all boot stages through actual first frame and library readiness. Perform three owner-requested normal reboots and retain boot IDs, shutdown acknowledgement and previous-boot journal.
  - Verify rescue entry and owner return using the established procedure before

risky update tests; no active-root write or protected partition is involved.
  - Exercise UI, wheel/navigation/buttons, artwork, scan status and renderer

recovery. Confirm no old UI data after source replacement.
  - Query `y2-audio-contract`, then verify the allowed S16 stereo 44.1 profile at

a safe owner-selected level, both channels, pause/seek/next and screen-off. Save actual ALSA hw_params, Reborn metrics and audible observations.
  - Verify ACM, ECM and key-only SSH. Check on the PC that only 10.42.0.1:22 is

reachable; attempting the Y2's Wi-Fi address must not reach this listener. Confirm ordinary root/data access and platform readiness from the app.

Acceptance: exact image identity, recoverable boot, valid persistence, responsive UI/input, baseline audio and authenticated USB all work without new faults.

## Session B — storage/performance (disposable scratch, supervised first)
  - Run `y2-platform bench-storage --volume /data`, then `/media/sd`, saving JSON.

The implementation creates a private descriptor-pinned scratch directory and checks reserve/generation; it never targets music, state or a database. Record sequential/random 4/16/64 KiB and 1 MiB results, metadata and durability p50/p95/p99/max, MB/s and operations/sec, plus card UUID/filesystem/bus identity.
  - Use disposable ext4, FAT and exFAT cards. Check insertion, platform mount,

unmount success, busy unmount refusal, unplugged source, reinsertion and a different card at the same mountpoint. A surviving directory is insufficient. Deliberate surprise removal may damage the disposable card; never use the sole copy of real media. Record I/O-error and read-only behavior; no forced unmount.
  - Run `y2-platform bench-library --tracks 1000 --scan`, then 10000 and 20000,

saving each record. Compare DB/population/incremental/query/search/commit/ checkpoint/reopen/size and actual scanner/UI timings, memory and thread count. Warm/cold process reopen is not a physically cold disk/cache claim.
  - Compare declared idle/playback/artwork/scan/crossfade/Wi-Fi/BT workloads using

`cpu-memory-thermal`. Observe LOWMEM/HIGHMEM, page cache/slab and per-core residency/wakeups. Do not change voltage, reclaim RAM or alter thermal trips.
  - Near-full behavior is first proven with host ENOSPC injection. On hardware,

admit only disposable scratch within a declared owner budget, retain reserve, verify transfer/staging refusal and database/state survivability, then delete that exact scratch. Never fill unknown space or delete user music automatically.

Acceptance: correct identity/lifecycle and durability semantics, no cross-source reconciliation, bounded errors and measured performance. Electrical power-loss durability is a separate test; process termination and fsync completion are not it.

## Session C — Wi-Fi

Use a dedicated AP/network. Start with the owner's normal saved-network UI or standard supplicant configuration; never put a password in a public receipt. Check Off → Starting/Scanning → Associating → Authenticated → AcquiringIP → Online. Online must have an address, default route and recent matching DNS observation. Test wrong credentials, absent AP, DHCP timeout and unavailable DNS separately; record the distinct reason. Restore the AP and verify the sole supplicant owner recovers, including service restart and owner reboot.

On an owner-controlled peer, start an iperf3 server bound to the intended test network. Run `y2-platform network-check --peer PEER_IPV4 --seconds 30 --throughput` on Y2. Save ping and actual TCP throughput, then a longer bounded transfer, screen-off run and AP loss/recovery. The tool binds to wlan0. No synthetic packet loss or energy estimate is acceptable. Confirm standard NTP establishes a plausible clock and that TLS readiness is false before a valid time anchor.

## Session D — Bluetooth/coexistence

Fresh discovery/pair/trust/bond one known peer; save BlueZ readiness, exact selected peer, BlueALSA owner/PCM generation, negotiated codec and PCM format/ rate/channels. Begin with manual SBC. Prove actual sound, pause/resume and volume behavior. Reconnect after peer loss and service restart; verify explicit user disconnect inhibits automatic reconnect and only y2-bt-reconnect owns retries. Test a peer disappearing after selection and stale PCM removal.

Use remote Play/Pause/Next/Previous and confirm existing Reborn Actions and matching metadata/playback state. Reborn remains playback authority. Auto is implemented but has no production-eligible codec until matching platform qualification is deliberately recorded; refusal is expected for this candidate. AAC/aptX/aptX HD/LDAC are not built. SBC XQ is a quality mode, not another codec. Do not display a requested codec as negotiated, or claim live LDAC bitrate.

Run Wi-Fi idle/scans/transfer alongside SBC. Save actual throughput, XRUNs, reconnects/controller recoveries, CPU and CPU/PMIC die temperature. After shorter sessions pass, use the declared Bluetooth 8-hour profile. Do not infer packet loss from XRUNs or successful pairing from an adapter existing.

## Session E — power (separately controlled)

Observe battery voltage, source type/presence, charger state/configured limits, CPU/PMIC die sensors, RTC and clock behavior. Pack temperature/current/SOC remain unavailable. Qualify charging and low-voltage operation against known pack/source limits and protection behavior; do not infer chemistry or a safe cutoff by exhausting an unidentified battery. No charger limit is changed by this pass.

First replay synthetic shutdown tests: ignored app, failed checkpoint and bounded sync failure. Then owner normal shutdown/reboot with actual state/DB recovery. Only after pack/sag/shutdown-reserve evidence exists should the owner populate `power-policy.json` as documented in `architecture/platform-power-v1.md`. Qualify the chosen warning/critical/recovery values under representative load and source-connected behavior; a configuration reference is not certification.

Verify RTC persistence across owner power cycles and NTP/RTC clock policy. RTC alarm wake, deep suspend and AP watchdog recovery remain separate experiments with established recovery access. Deep suspend's default refusal is expected. The explicit owner-only helper does not prove same-boot resume. Do not arm an AP watchdog, copy SPM sequences or program unknown wake/VBUS paths as part of ordinary candidate qualification.

## Session F — audio hardware boundary

For this candidate only S16/44.1 is enabled in the product profile. Query direct 44.1/48 constraints and retain native 48 qualification as a separate controlled extension. S24/S32 and 88.2/96 are unavailable; their tests are BLOCKED_BY_EVIDENCE until a source-backed AFE fetch/interconnect/clock implementation exists.

`tools/host/audio_precision.py` supplies low-bit/channel fixtures and exact 24-in-32/S32 words for that future milestone. Required proof is ALSA hw_params, DMA/sample packing, valid low bits, both channels, actual MCLK/BCLK/LRCLK, each rate family, switching, XRUNs and analog pop/click behavior. A 32-bit slot or a successful file decoder cannot satisfy any missing part. No speculative gain or impedance policy is enabled for CS43131.

## Session G — signed root OTA and recovery

Perform only after Session A establishes the exact candidate rescue and normal shutdown path. Ensure adequate external power and Y2DATA reserve. The bundled root-only development update requires this candidate's exact kernel/rescue, contains no BOOTIMG/data payload and is not a first-install substitute.
  - Save update status and current source identity. Check a locally staged signed

package with `y2-platform update check --package DIRECTORY`; invalid signature, wrong product/kernel/schema, truncated or altered payload must refuse without root mutation. Retain the host/ARM fake-file fault receipts as a prerequisite.
  - Stage with `y2-platform update stage --package DIRECTORY` (or the documented

exact HTTPS manifest URL after valid time). Check actual staging and backup space. Interrupt only staging first, verify no queued partial install, and explicitly discard/retry under the documented state policy.
  - Owner invokes `y2-platform update apply`. This requests the common bounded

reboot contract. Rescue validates everything, creates/verifies the previous root, writes offline and verifies readback. Normal boot must publish exact first-frame/process readiness and acknowledge health within the bounded window.
  - On a disposable qualification cycle, use the explicit missing-application

derivative below; timeout should queue rollback. The next owner reboot restores the verified previous root. There is no automatic reboot loop. `RescueRequired` must remain in rescue rather than retry forever.
  - Demonstrate explicit verified rollback and fallback recovery, then restore

normal services. An electrical interruption during root writing is a separate owner-approved destructive qualification after all local protections pass. It is never simulated by pretending a process-kill test is power loss.

Prepare that failure on the host, in a fresh private output directory:`python3 tools/update/qualification_root.py \ --candidate out/y2linux-platform-v1-candidate --output PRIVATE_FAULT_DIRECTORY`

This checks the original root hash, copies only to a new regular file, deliberately removes `/usr/bin/reborn`, updates the derived rootfs identity and checks ext4. It never installs or signs anything and never alters the original. Inspect `fixture.json` and `e2fsck.log`. The resulting `INTENTIONALLY-BROKEN-APP.ext4` is not a release. Only for the approved recovery session, the owner can use `tools/update/package.py package` with that image, `fault-versions.json`, a fresh output, an off-device trusted development key/key ID, an allowed sequence greater than the current accepted sequence and `--rollback-allowed`. Stage/apply that signed package through the normal commands. Keep USB/power/recovery available; the app is intentionally absent. Wait for `RollbackPending`, save status and use the normal platform reboot to restore the verified previous root. Bind its capture to `fault-versions.json`; start a separate capture after restoration. The real host ext4 fixture test proves preparation/preservation only, not recovery on physical flash. Do not distribute or install this fixture as ordinary firmware.

A torn BOOTIMG cannot be fixed by root-only OTA. Development downgrade permission is signed/key-policy controlled; production replay policy, release keys and trust rotation/revocation require deliberate owner release management. Never copy the private signing key to Y2. Current rescue keys can only be changed by a separately controlled trusted BOOTIMG update; mutable root policy cannot revoke old rescue.

## Long runs and freeze acceptance

After the relevant short session passes, run wired 8h, Bluetooth 8h, scan+playback, Wi-Fi transfer+playback, Wi-Fi+Bluetooth, SD/USB cycles, file transfer, renderer/service recovery, repeated boots and near-full behavior. Suspend and electrical OTA interruption remain separately gated. Keep workload parameters and manual observations with each capture, including gaps/failures. Set measurable product budgets from these results before claiming performance or endurance. Only owner-reviewed evidence promotes the exact advertised capability.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
