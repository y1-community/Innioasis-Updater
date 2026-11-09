---
title: "Bluetooth reimplementation — plan - Innioasis Updater"
description: "Bluetooth reimplementation — plan Status: plan, 2026-11-03. Nothing built, flashed or run. Owner request:"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-bluetooth-reimplementation-plan.html"
---

# Bluetooth reimplementation — plan - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Bluetooth reimplementation — plan

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Bluetooth reimplementation — plan

Status: plan, 2026-11-03. Nothing built, flashed or run. Owner request: "not a refactor anymore, but a complete new reimplementation built on reliability, so that Bluetooth always works, without losing the codecs, bitrates and the fancy stuff". This changes the architecture of a hardware subsystem, so per `AGENTS.md` the roadmap/gap audit is repeated before implementation starts. This document is not implementation or hardware authorization.

Sources: Y2Linux `main` b8e78d3f (9.2.16), Y2Reborn 6fd259c, GitHub issues Y2Reborn #87 #92 #78 #22, field reports 0400eb78 (583b7c23 58e1456e a74ed186, 10-31 diag), 5692dd73 (962aac6c 46fcbe24), 3a1f5afc d833b3da f92f0093 aa96e00a e1db3cb0, the ledger `UserReports/REVIEWED.md` (F8 F14 F15 F20 F21 F22 F25 F28 F43 F51 F58 F61 F63, new F64 F65).

## 1. What the evidence says

### What is not broken
  - The kernel connectivity driver and firmware path. No hci/btif/stp/WMT error

in any report from 11-01 to 11-03, and none of the recent drops starts there.
  - BlueZ 5.87 and BlueALSA 5.0.0 themselves. Every failure we traced is our

control code around them or the radio link. The codecs (SBC, AAC via fdk-aac-free, LDAC, aptX/aptX HD in owner builds) and our three BlueALSA patches (encoder stats, AAC ABR, SBC ABR) are good and are kept.

### What is broken (ranked)
  - **The library is emptied by a Bluetooth failure (#92, F64, proven, two field

occurrences).** `abandon_pending_reconfiguration` (`Y2Reborn/app/reborn/src/runtime/audio.rs:152`) restores the pre-action snapshot, which `with_model_action` took with the tracks, shelf, chapters and platform data moved out (`:18-26`). It does not move them back, unlike `restore_failed_reconfiguration`. Any peer loss or transport change while a sink start is pending empties the library, the Audiobooks row disappears, and the next checkpoint writes an empty `state/books.json`. That is why the progress is lost. This is not an architecture problem. It is a few-line fix and ships first (H1).
  - Wake reconnect race (#92 "pairing froze", F65, strong). Every full sleep

powers Bluetooth off (the kernel refuses suspend while a function is held). On wake, four actors start at once: - the headphones reconnect on their own; - `y2-bt-reconnect` pages; - Reborn sends SelectCodec; - the auto-resume opens the sink.

 962aac6c shows the result in order: AVDTP `No pending request` ×2, then SelectCodec refused, then ALSA −5, then the PCM disappears, then a `local` disconnect. After that, Connect answered `InProgress` every 2 s for 1 min 45 s, through two Bluetooth power cycles. This is architectural: it comes back under any patch while several owners act on one link.
  - Air-time shortfall (#87 crackle, strong). The XM4 install shows the encoder

queue backing up at LDAC 606k and at AAC 192k: - LDAC ABR made 5 then 15 adjustments, and AAC fell to 144k; - two Bluetooth xruns; - zero link errors.

 The shared antenna, Wi-Fi in CAM (no power save), and a weak access point (−77/−83 dBm) all cost air time. The Wi-Fi ceiling does not cap LDAC or aptX. Lower rates only mitigate this, because the radio is shared. Policy has to treat air time as the scarce resource.
  - AVDTP Suspend+Start on every pause (F43 → F61 pattern, moderate). On

Bluetooth, a pause closes the PCM and Play reopens it. Some headphones answer Start slowly; BlueZ then times out and drops the link. The 10-31 drop (three pause→play cycles, lost 2 s after the last) fits this.
  - Disconnect after ~1 h on AAC with Wi-Fi off (#87): no report covers it yet.

We need a 9.2.16+ report taken right after it happens; the reason is logged now.

### Why patches keep failing: the structure

There are five owners of Bluetooth state:
  - Reborn's worker (directly over D-Bus);
  - `y2-platform bluetooth-power` (`bluetoothctl`);
  - `y2-bt-reconnect` (C, its own state machine);
  - the sleep helper (power off/on);
  - the kernel's own core recovery.

They coordinate through advisory `flock` files (`bt-operation.lock`, `bt-pcm.lock`) and an ini "intent" file with 30 s deadlines. No single component knows the truth, so:
  - "Connected" exists in at least 10 copies in Reborn alone. Examples:

`bt_state`, `ui.bluetooth`, `model.output`, `AutoOutput`, `CodecReconnect`, `BtVolume`, `LostPeer`, the transport generation.
  - An empty status reads as a peer loss. A failed observation or a D-Bus

reconnect produces an empty `Status`, and `main_loop.rs:1631` treats it as "peer lost". It ignores `available`.
  - Each layer has its own recovery budget, and several latch:
    - kernel: 3 recoveries per 5 min, then sticky;
    - supervisor: one restart per 30 s;
    - reconnect: 2 attempts in 25 s, then inhibited or exhausted until an intent

arrives;
    - the F25 codec-uncertain marker blocks all playback;
    - the worker's sticky `operation_error`.

  - `bluetoothd` is not supervised at all. If it dies, Bluetooth is gone until a

reboot. A `bluealsad` restart changes the PCM owner under an open stream.
  - Timeouts don't line up. A 45 s Connect call runs inside a 25 s reconnect

episode. `bluetoothctl` waits 15 s on a power-on that can include up to 90 s of modem calibration at first boot. Power "off" ignores the lock.
  - The worker blocks its own loop on synchronous D-Bus calls: Power 15 s,

discovery 15 s, codec selection up to 12 s. Meanwhile volume commands wait in the same 8-slot queue.
  - Codec changes need a bluealsad restart (in practice a reboot). SelectCodec

runs on every reconnect, even when the codec is already right.
  - Compensating code everywhere:
    - busy-retry loops (F14/F28/F58);
    - codec retry (F8) and deferral (#87);
    - `power_pending` hints, abort-by-Disconnect, the page-timeout override;
    - the lost-peer wait (F51);
    - the kept sink (F61), and pause by close (F43).

Git history: 58 Y2Linux and 69 Y2Reborn commits are about Bluetooth. Most of them add a rule to one owner to work around another owner.

## 2. Decision: what gets reimplemented, what is kept````````````````````````

| Layer | Decision | Why |
| --- | --- | --- |
| Kernel y2_connectivity (BTIF/STP/WMT/HCI) | keep, add counters + one control for the daemon | no field failure starts here; rewriting it risks the radio |
| Firmware, WMT_SOC.cfg, BT.defaults | keep | owner-supplied, hash-pinned |
| BlueZ 5.87 | keep (config only), now supervised | the A2DP/AVDTP/AVRCP protocol is not where we fail |
| BlueALSA 5.0.0 + patches 0001-0003 | keep, add --keep-alive handling, an LDAC/aptX ceiling, and a runtime rate control instead of restart | this is the codec and bitrate machinery the owner wants to keep |
| y2-bt-reconnect (C), bt_control.rs, intent ini, bt-operation.lock, bt-pcm.lock, bt-codec-uncertain.json, the sleep helper's radio steps for BT | replace | the five-owner structure |
| Reborn reborn-platform/src/bluetooth.rs + bluetooth/worker.rs (≈3800 lines), outputs.rs AutoOutput/CodecReconnect/LostPeer, AVRCP owner polling | replace with a thin client | ten copies of the truth, blocking worker |
| Reborn sink/playback for Bluetooth (pause by close, kept sink) | rewrite the Bluetooth part around a lease + stream generation | Suspend/Start drops |
| UI pages, settings, codec names, history, AVRCP projection (MPRIS) | keep (re-pointed at the new client) | users like them; they are not the problem |

Rejected: replacing BlueZ+BlueALSA with PipeWire or our own A2DP stack. PipeWire adds a session manager, more RAM and a new set of unknowns on a 948 MB device. It would not fix any traced failure, because none of them is inside BlueALSA. An own A2DP stack would rewrite exactly the part that works.

## 3. The new architecture: one owner` Reborn (UI, playback) y2-radiod (platform, Rust, new) system ─────────────────── ───────────────────────────────── ────── BtClient ── desired state ─────────▶ Desired { powered, preferred peer, bluetoothd (supervised) (one socket, never blocks) codec pref, quality, ... } bluealsad (supervised) BtClient ◀── BtSnapshot{gen} ─────── Reconciler ── one action at a time ──────────────▶ D-Bus sink opens only when Link state machine per peer kernel y2_connectivity snapshot says Ready(gen) Recovery ladder + budget (status, recover) Stream lease (who plays, keep-alive) sleep/wake ─────────────────────────▶ Power handoff (quiesce / restore) Wi-Fi daemon ── air-time state ─────▶ Rate policy (codec ceiling per Wi-Fi state)`

### 3.1 Principles (each one answers a failure class above)
  - One owner, one state machine.`y2-radiod` is the only process that

powers, pages, connects, disconnects, pairs, forgets, selects codecs, restarts BlueZ/BlueALSA or touches the CONSYS recovery. Everything else (Reborn, sleep, Wi-Fi, CLI) only states what it wants. (Fixes F14 F28 F58 F65; removes all locks and intents.)
  - Desired state, not commands. The daemon reconciles continuously toward a

desired state. A user tap replaces the desired state, and the daemon cancels whatever conflicts with it. There is never "operation in progress, try again": the busy-retry loops disappear because the request is the state.
  - One truth with a generation number. The daemon publishes a single

`BtSnapshot`: - adapter; - each peer's link state; - codec and rate; - stream readiness; - last failure with a typed reason; - `gen`.

 Reborn keeps exactly one copy. Every UI view, output choice and volume rule is derived from it. "Unknown" is a state of its own, never mistaken for "disconnected". (Fixes the empty-Status peer loss and F20.)
  - Playback only on a promise. Reborn opens the BlueALSA PCM only when the

snapshot says `Ready{peer, codec, gen}`. It opens it off the main thread and tags it with `gen`. A changed `gen` closes the stream cleanly; there is no rollback of the whole model. (Fixes the #92 class structurally, beside the H1 hotfix.)
  - Nothing latches without telling the user and offering a way out. Every

recovery path ends either back at the desired state or in one visible state: "Bluetooth needs a restart", with a button that runs the next ladder rung. No hidden marker files, no "inhibited until an intent".
  - Never block the owner. The daemon's loop is event-driven. Each D-Bus call is

async with a deadline sized from measurement. Volume runs on its own fast path and never waits behind a Connect.
  - Fewer AVDTP state changes. Every Suspend/Start is a chance for a slow

headphone to drop. The stream stays started across pause, track change and station change, within limits (§3.4).
  - Air time is a budget. The bitrate is chosen from the link's real capacity

(queue depth, learned per peer, Wi-Fi state), not from a static preference.

### 3.2 Link state machine (per peer)`Unpaired ─pair─▶ Paired ─▶ Idle ─(desired=connected)─▶ Paging ─▶ Connecting ─▶ ServicesResolved │ ┌────────────── Disconnected{reason: remote|timeout|local|sleep|user} ◀┤ ▼ ▼ Backoff ──(budget left)──▶ Paging CodecSettle (only if wrong) │ ▼ └─(budget gone)─▶ Parked (visible, retried on headphones' own connect, wake, tap) Ready{gen} ▼ Streaming ⇄ Held (paused, kept)`
  - Incoming connections. Headphones that reconnect on their own are adopted:

they are not raced by a page. The daemon waits a short adoption window (measured, ~3 s after power-on) before paging. That window removes the wake race.
  - Codec selection.`CodecSettle` runs once, before `Ready`, and only if the

negotiated codec differs from the policy's choice. A change asked for while streaming is scheduled at the next `Held` → (re)start boundary. Its outcome is read back from BlueALSA, never guessed; F25's "uncertain" becomes a short re-read.
  - Disconnect reasons are typed. HCI 0x15 (power-off) during our own quiesce

becomes `sleep`, not `unknown`. Only `timeout` and `local`-without-request count against the peer's reliability budget.
  - Per-device settings (#78). Each device can be set to Auto-connect or *Only

when I ask*.

### 3.3 Recovery ladder (one budget, owned by the daemon)``````````````

| Rung | Action | When |
| --- | --- | --- |
| R0 | retry the step after its deadline | single timeout |
| R1 | cancel: Device1.Disconnect + wait for idle | stuck page/connect (the 1 min 45 s InProgress) |
| R2 | adapter power cycle (Powered off/on) | R1 failed or the HCI is unresponsive |
| R3 | restart bluealsad (Reborn sees a new gen) | PCM missing/broken, encoder errors |
| R4 | restart bluetoothd | D-Bus API dead, R2 failed |
| R5 | CONSYS recover (both radios: Wi-Fi is told first) | HCI dead, R4 failed, kernel error counters |

  - Each rung records `{rung, cause, duration, success}` in the event log.
  - The budget is per episode, with exponential spacing. Running out ends in the

visible `Parked`/"needs a restart" state from principle 5, never in silence.
  - The ladder resets on any successful `Ready`.

### 3.4 Stream path (keeps every codec and bitrate)
  - Hold instead of close on pause.
    - BlueALSA's `--keep-alive=N` keeps the transport started for N seconds after

the PCM is closed.
    - Alternatively, Reborn writes silence into the open PCM for a measured hold

window (e.g. 20 s), then releases.
    - Both are tested against F43's "drained-and-prepared stream stays silent", which

is why pause became close in 8.38.
    - Resume within the window has no AVDTP Start at all.

  - Track, rate and station changes reuse the started stream (the F61 kept sink,

generalized). A sample-rate change resamples to the stream's rate rather than renegotiating, unless the user chose "bit-perfect".
  - Rate policy (air-time budget).
    - Inputs:
    - the encoder queue depth (patch 0001 stats);
    - Wi-Fi state from the Wi-Fi daemon (off / idle / associated-PS / CAM /

transferring);
    - RSSI of the BT link where readable;
    - the learned per-peer history.
    - Output: a ceiling per codec, LDAC/aptX included:
    - LDAC: 990 → 660 → 330;
    - AAC: 320 → 256 → 192 → 128;
    - SBC: bitpool steps.
    - How it is applied: at runtime over a small control socket into the patched

bluealsad, replacing the `access()` file check and the restart-to-apply settings.
    - Persistence: each peer remembers the highest level that stayed clean for

10 min, and starts there next time.
    - Settings: "High quality" stays available. It sets the starting level and the

ceiling; it does not disable the safety step-down unless the user picks "Fixed rate (expert)".

  - Wi-Fi only when needed (Y2Reborn #87 suggestion). While Bluetooth streams,

Wi-Fi is asked into power-save. Optionally (owner decision) it goes off unless something holds a Wi-Fi lease: radio, update check, Last.fm flush, report upload.
  - Absolute volume stays on `MediaTransport1.Volume`, on the daemon's fast path.

### 3.5 Sleep and wake

The sleep helper no longer powers Bluetooth itself.
  - Sleep: it asks the daemon for `quiesce`. The daemon:
    - holds new pages;
    - tells peers (disconnect reason `sleep`);
    - powers off and confirms within a deadline;
    - answers ready, or refused with reason.

  - Wake: it sends `restore`. The daemon owns the whole reconnect, including the

adoption window. Reborn's auto-resume waits for `Ready{gen}`, at most a bounded time, instead of racing it.

Research item (not a dependency): whether Bluetooth can stay powered across a sleep. That would need the kernel's held-function refusal lifted, plus wake-on-BT, plus a drain measurement. If yes, the wake race disappears entirely.

### 3.6 Observability
  - One event log (`/data/logs/bluetooth.jsonl`, rotated). Every state

transition, every D-Bus call with its duration and result, every ladder rung, every rate step with its queue depth, and each disconnect reason.
  - The error report carries the last 2 000 events plus the snapshot.
  - `y2-platform bluetooth status` prints the state machine. A "Bluetooth health"

line in Settings → System shows the last failure and its rung.

## 4. Phases

Each phase ends in a test build and a device check on the owner's player with at least two headsets (AirPods-class AAC, an LDAC headset). It ships only when its acceptance numbers are met.

### H — Hotfixes now (independent of the rewrite, next point release 9.2.17)
  - H1 (#92, F64): `abandon_pending_reconfiguration` moves the tracks, shelf,

chapters and platform data back into the restored model, as `restore_failed_reconfiguration` does. Test: a peer loss with a pending start keeps the library and `books.json`. Also reload the shelf when it is found empty but the database has books.
  - H2: an empty or failed Bluetooth observation (`available=false`) is never a

peer loss (`main_loop.rs:1631`).
  - H3: reason 21 (HCI 0x15) inside our own radio quiesce is logged `sleep`.
  - H4: the Wi-Fi ceiling also caps LDAC (mobile/330) and aptX HD → aptX.
  - H5: reply on #92 (cause found, fix in 9.2.17, Rebuild Library restores the

library but not lost progress) and on #87 (ABR evidence: LDAC was already being stepped down to 303k with Wi-Fi on).

### P0 — Measure before designing numbers (2–3 sessions, device)
  - Air-time matrix on the owner's player. Codec × level × Wi-Fi state (off,

idle, PS, CAM, transferring) × distance (1 m, 5 m, body-blocked). Record the encoder queue depth, ABR steps, xruns and audible dropouts. This yields the rate policy table and the per-Wi-Fi-state ceilings.
  - Timing table.
    - Real durations of power-on (cold, warm, first boot with calibration), page,

connect, ServicesResolved, SelectCodec and AVDTP Start for each headset.
    - Deadlines are set at measured p99 × 2, never guessed.

  - Keep-alive test.
    - `--keep-alive` and silence-hold against F43's silent resume, on AirPods and

XM4-class headsets.
    - Drain cost of a held stream.

  - Stock comparison (REA). Does the stock MediaTek BT stack send coex/AFH/PTA

parameters beyond `coex_wmt_ant_mode`? If yes, they may give back real air time and are worth more than any rate trick.
  - Sleep with Bluetooth on: feasibility only (§3.5 research item).

### P1 — Contract and specification
  - `docs/architecture/bluetooth-v2.md` (replacing `platform-bluetooth-v1.md`, which

is stale): - desired-state schema; - snapshot schema with `gen`; - the state machine; - the ladder; - the rate policy; - the sleep handshake; - the event log format.
  - `CONTRACT.md` and `capabilities.json` entries. Owner sign-off.

### P2 — Daemon on the host
  - `y2-radiod`: a new crate in `platform/crates`. It uses a single-threaded

async loop (zbus or the existing GIO binding, whichever the platform port already uses).
  - Host test harness. A fake BlueZ + BlueALSA on a private D-Bus bus, scriptable

per scenario: - slow Start; - `InProgress` storms; - the owner vanishing; - incoming connects during a page; - sleep/wake; - a wrong codec; - bluealsad crash.

 Every field failure F8–F65 becomes a scripted scenario that must pass.
  - Property tests on the state machine: no reachable state without an exit, and no

two actions in flight.

### P3 — Daemon on the device, behind a switch
  - `/data/bluetooth/stack` = `v2|v1`, default v1 (owner can flip it).
  - v2 supervises bluetoothd and bluealsad and replaces `y2-bt-reconnect`, the BT

part of `y2-radio`, `bt_control.rs` and the sleep helper's BT steps.
  - Reborn talks to it through a compatibility shim at first, so the UI needs no

changes yet.
  - Acceptance:
    - 200 scripted sleep/wake cycles with a headset: 0 stuck states, 0 library

effects, reconnect ≤ p99 × 1.5 of P0;
    - 50 forced faults per ladder rung, each recovering.

### P4 — Reborn client
  - Replace `bluetooth.rs`, `bluetooth/worker.rs`, `CodecReconnect`, `AutoOutput`,

`LostPeer` and the AVRCP owner polling with `BtClient` (one snapshot, one socket).
  - The Bluetooth sink opens on `Ready{gen}` only, off the main thread, and

hold-on-pause applies.
  - `with_model_action`'s whole-model snapshot is no longer used for output changes.

A failed Bluetooth start closes the stream and leaves the model alone.
  - UI: the same pages. "Busy" disappears; a device shows its state ("Connecting…",

"Waiting for headphones", "Needs restart [Restart Bluetooth]"). The per-device auto-connect switch (#78) goes in.
  - Acceptance:
    - a 4-hour soak per headset: pause/play every 30 s for 30 min, radio zapping, 50

track skips;
    - 0 drops not caused by the headset or by range, and 0 xruns at the steady

level.

### P5 — Rate policy and Wi-Fi coordination
  - Runtime rate control in the patched bluealsad, replacing the file-based

ceiling.
  - Per-peer learned levels, and the Wi-Fi power-save / lease policy.
  - Settings:
    - Quality: Auto (default), High, Fixed (expert);
    - the codec preference stays;
    - the hidden AAC/LDAC quality rows move to the new levels;
    - a "restart required" is no longer needed.

  - Acceptance:
    - the P0 matrix again, with no audible dropout at 1 m with Wi-Fi associated on

AAC Auto and LDAC Auto;
    - the XM4 install's scenario reproduced and clean.

### P6 — Beta, then delete v1
  - A public test build with v2 as default and v1 selectable for one release.
  - The ledger tracks Bluetooth findings per stack.
  - After one release without a v2-only regression, delete v1:
    - `reconnect.c`, the intents, the locks, the marker file;
    - the old worker;
    - the busy-retry code.

## 5. Owner decisions needed
  - Owner of the stack: the platform (`y2-radiod`, recommended: it must

supervise processes and coordinate sleep and Wi-Fi) or Reborn. The 2026-10-30 platform decisions allow the Reborn API to change.
  - Wi-Fi while Bluetooth streams:
    - power-save only (recommended default);
    - off unless leased (most reliable, but radio/Last.fm/update would switch Wi-Fi

on on demand);
    - user choice.

  - Default quality: Auto that steps down for air time (recommended), with High

and Fixed for people who never had problems (#87 MickEventide's concern).
  - Pause hold window: how long a paused stream stays started (drain vs

reliability); P0 gives the numbers.
  - Whether to pursue Bluetooth on through sleep (§3.5), which is a kernel and

power project of its own.

## 6. Risks
  - The air time is physical. No software makes LDAC 990 reliable on a shared

antenna with busy Wi-Fi. The promise is "never stuck, always recovers, automatically picks a rate that works", not "LDAC 990 everywhere".
  - Keep-alive could reintroduce F43 (silent resume) on some headsets. P0 tests

it first; the fallback is close-on-pause after the hold window.
  - **A bigger change to the platform/Reborn split means a double maintenance

window** while v1 and v2 coexist (P3–P6). The switch limits that to about two releases.
  - Headset diversity. We test only what the owner has. Typed reasons and the

event log are what make field reports conclusive instead of guesses.

## 7. Wi-Fi and the shared radio core (added 2026-11-03)

Owner question: Wi-Fi and Bluetooth share the MT6582 CONSYS core and one 2.4 GHz antenna. Is Wi-Fi broken the same way, and does it need its own worker or a shared one?

### Wi-Fi has the same structure

Wi-Fi state is acted on by eight parties:``````````````````````````````````````

| Actor | What it does to Wi-Fi |
| --- | --- |
| wpa_supplicant | associates and reconnects on its own (autoscan exponential:2:120) |
| Reborn reborn-platform/src/wifi.rs (1842 lines) | its own thread; talks to the supplicant control socket directly (scan, join, add/remove networks, disconnect); writes rfkill soft itself; persists /data/network/enabled |
| Reborn runtime/idle.rswifi_idle_tick | powers Wi-Fi down after 5 idle minutes and back up at wake/use |
| platform connectivity/wifi/recovery.rs | F52 reselects a saved network after 30 s DISCONNECTED; F60 cycles the same rfkill (block, wait for wlan0 to go, unblock) after 4 blind scans |
| platform connectivity/daemon/supervisor.rs | restarts the supplicant; F53 removes and re-adds wlan0 when it is INTERFACE_DISABLED; sets autoscan |
| platform connectivity/radio_policy.rs (service daemon, every 30 s) | power-save policy (iw) |
| sleep helper suspend/helper.rs:200, 405 | y2-radio wifi off-runtime before every sleep, on-runtime after |
| y2-radio (shell) + kernel core.c | rfkill per device; writes recover to the shared core; a Bluetooth HCI error's automatic recovery unbinds and rebinds the Wi-Fi driver too (recover_locked, device_release_driver(&c->wifi->dev)) |

As with Bluetooth, nothing owns the whole state. Two components switch the same rfkill. Two decide when to (re)select a network. The ledger shows the same patch chain:
  - F1, F27 and F35: cfg80211 warnings, fixed in the driver;
  - F13, F31, F52, F53 and F60: no connect after a wake;
  - F37: rfkill state after sleep.

Each fix added a self-heal to one actor. F60 is still open. After a wake the saved access point is seen but rejected for minutes. The first episode happened while the headphones reconnected and A2DP started (fa30bf96).

### It is less acute, but it shares the weak point
  - Wi-Fi is not real-time. A failure means a late connect, not audible

dropouts. `wpa_supplicant` is also a proper single owner of association, unlike our Bluetooth reconnect split, so its core is sound.
  - What is shared is the bad moment: the wake.
    - Every sleep powers the whole core off.
    - `restore_radios` switches Wi-Fi on and then Bluetooth immediately after,

because `y2-radio wifi` only unblocks and returns.
    - Then three things land in the same seconds on one antenna: Wi-Fi scan and

association, the headphones' own reconnect plus our page, and AVDTP start. Reborn's idle restore and the F52/F60 heals add to that.
    - F60's rejects and #92's freeze are both wake-time failures.

  - Recovery is shared whether we like it or not.
    - One kernel budget (3 recoveries / 5 min) covers both radios.
    - A Bluetooth fault drops Wi-Fi.
    - `recover` requires both functions off.

 No component today weighs one radio's recovery against the other's.

### Recommendation: one radio daemon, two independent controllers`y2-radiod ├── Core arbiter (shared, small) │ power/function lifecycle of CONSYS, sleep quiesce/restore handshake, │ wake ordering, kernel recover (R5) with both radios informed, │ air-time policy: Wi-Fi state → BT codec ceiling, BT streaming → Wi-Fi power-save/lease ├── Bluetooth controller (its own task: BlueZ/BlueALSA, §3) └── Wi-Fi controller (its own task: wpa_supplicant D-Bus/ctrl, DHCP, DNS readiness)`
  - Shared, because the hardware forces these decisions to be made together:
    - the power order at wake;
    - the recovery that kills both radios;
    - the sleep handshake;
    - the antenna time budget.

 Today these are spread over the sleep helper, `y2-radio`, the service daemon's coexistence file and the kernel. Only an arbiter that sees both radios can stagger the wake, for example:
  - Bluetooth first while music was playing, with its adoption window;
    - Wi-Fi association after `Ready` or after the window;
    - Wi-Fi first when nothing plays.

  - Separate controllers, because the protocols share nothing (BlueZ/BlueALSA vs

wpa_supplicant). Each runs its own reconcile loop, so a stuck Bluetooth call never delays a Wi-Fi join, and the reverse. They talk only through the arbiter.
  - One process, not two daemons. The two controllers need the arbiter on every

decision, so separate daemons would just bring back the lock/intent files this plan removes. - Crash isolation: the connectivity supervisor restarts the daemon. - Recovery after a restart: each controller is a reconciler, so a restart re-reads reality instead of trusting remembered state.
  - The Wi-Fi controller replaces:
    - Reborn's direct supplicant socket and rfkill writes (Reborn becomes a

desired-state client, as for Bluetooth: `wifi on/off`, join, forget, scan request, plus "I need the network" leases for radio, update, Last.fm and reports);
    - Reborn's idle power-down (it becomes "no lease for 5 min");
    - the F52/F60/F53 heals (they become the Wi-Fi controller's own recovery

ladder: reselect → rescan → reassociate → interface re-add → rfkill cycle → core recover via the arbiter);
    - the radio policy, `y2-radio` and the sleep helper's radio steps.
    - It keeps: `wpa_supplicant`, the driver, udhcpc/`dhcp-event`, the DNS readiness

check and the event monitor's evidence.

### Order
  - Bluetooth stays first. It has the user-visible failures: dropouts, a stuck

reconnect, the library loss.
  - The core arbiter is built in P2/P3 from the start, even before the Wi-Fi

controller exists, because the sleep handshake, wake ordering and recover decision belong to it, not to the Bluetooth controller. At first it drives the existing Wi-Fi path (y2-radio, Reborn's worker) through a narrow adapter.
  - The Wi-Fi controller follows as P7, after the Bluetooth beta (P6), with the

same pattern: - host simulation of a fake supplicant (F13/F52/F53/F60 as scripted scenarios); - a v1/v2 switch; - a soak of 200 wake cycles with the saved network in range, with connect time and failures per cycle.
  - P0 adds wake measurements: Wi-Fi association time and reject codes at wake

with and without Bluetooth reconnecting in parallel. That tests directly whether staggering fixes F60, before any rewrite.

Decision 1 in §5 becomes: radio daemon in the platform (recommended), with shared arbiter + two controllers.

## 8. As built (2026-11-03, owner: "do the full implementation in one step, build and install")

The owner asked for everything at once after reading §1–§7. What was built, and what deliberately was not:````````````````````````````````````````````````````````````````````````

| Plan | Built | Where |
| --- | --- | --- |
| H1 #92 library loss | rolled-back model keeps the whole live library and platform facts | Reborn runtime/audio.rskeep_live_parts, test a_rolled_back_output_change_keeps_the_library_and_book_progress |
| H2 empty status ≠ peer lost | bt_lost and the transport epoch ignore a status without the adapter | Reborn main_loop.rs |
| H3 sleep reason | a disconnect during the daemon's quiesce is sleep | y2-radiodbt/links.rsended |
| H4 LDAC ceiling | BlueALSA patch 0004: LDAC ≤ MQ (330 kbit/s) while Wi-Fi is on | buildroot/patches/bluez-alsa/0004-y2-ldac-codec-ceiling.patch |
| One owner | y2-radiod (new crate platform/crates/y2-radiod): arbiter + Bluetooth controller; y2-bt-reconnect, bluetooth-power, intents, bt-operation.lock, bt-pcm.lock, bt-codec-uncertain.json and Reborn's D-Bus worker are gone | §3 |
| Desired state, no "busy" | requests change a wish and are answered at once; Connect replaces a page | bt/requests.rs |
| One truth | y2p_contract::radiod::State over /run/y2/radiod.sock; Reborn's Status is built only from it; Device::settling gates playback | Reborn reborn-platform/src/bluetooth.rs |
| Adoption window, episodes | 3 s for headsets to return on their own; 3 tries (power-on, wake, tap, timeout/local loss), 1 after a remote end, none after the owner's disconnect or a sleep | bt/links.rs |
| Recovery ladder | cancel page → power cycle → BlueALSA restart → BlueZ restart, 3 each per 10 min, then Failed until "Restart Bluetooth" | bt/ladder.rs, bt/reconcile.rs |
| Supervision | bluetoothd (its init script) and bluealsad restarted when they end (5 per 10 min) | bt/supervise.rs |
| Codec at connect, never mid-stream | policy moved from Reborn unchanged; SelectCodec only when it differs, only while the stream is not running; no answer leaves the headset usable | bt/codec.rs, bt/settle.rs |
| Pause ends the stream | bluealsad --keep-alive=0 (9.3.12): a pause suspends at once as a phone's does, Play starts a new stream; builds 210–219 kept it 900 s (one Suspend in three unanswered when sent 10 s into an idle stream, 2026-11-03), but headphones left in a started stream without packets went silent after every gap longer than their buffer (AirPods, 2026-11-04, as F43 in Beta 6) | bt/supervise.rs |
| Wake order | Wi-Fi waits up to 12 s for the headset connected before the sleep | arbiter.rs |
| Wi-Fi power | y2-radio, Reborn's switch and the F60 restart go through the daemon (direct only when it does not run) | §7 |
| Journal | /data/system/platform/bluetooth-journal.jsonl, /run/y2/radiod-state.json, both in error reports | journal.rs |

Not built in this step (stays open): the P0 measurements (no device was reachable while building); a learned per-headset rate level and a runtime rate control socket in BlueALSA (the existing ABR plus the Wi-Fi ceiling, now including LDAC, remain the rate policy); the Wi-Fi association controller (P7); the per-device auto-connect switch in Reborn's UI (the daemon has `AutoConnect`, Reborn does not send it yet, #78); no v1/v2 switch on the player (rollback is the installer's kept previous package).

Tests:`y2-radiod` unit tests (episodes, reasons, ladder, codec ranking and history, generations, owner files, core status, ctl words) and an end-to-end test against a fake BlueZ/BlueALSA on a private bus (power-on, adoption, a stuck InProgress cancelled and retried, Ready with a generation, sleep); Reborn's client tests; platform gate and host tests.

### Measured on the owner's player (2026-11-03, builds 208/209, AirPods Pro, Wi-Fi on)``````````````````````

| What | Measured | Constant it informs |
| --- | --- | --- |
| Adapter power-on (warm, after boot) | 0.41 s (request → adapter on) | POWER_ON_DEADLINE 100 s is only for the first boot's calibration |
| Bluetooth on → AirPods Ready | 5.6 s (3 s adoption, page → connected 2.2 s) | AirPods never came back on their own within the 3 s ADOPTION: for them the window is pure delay; kept at 3 s until other headsets are measured |
| Wake (sleep helper's radio steps) → AirPods Ready | ≈6 s; Wi-Fi held, released when the headset was back (not by the 12 s limit) | WAKE_HOLD 12 s |
| Bluetooth power-down at a sleep | 0.17 s, chip functions 0 | quiesce deadline 15 s |
| bluealsad killed → Ready again | 7.7 s (BlueZ ends the link local, episode Lost(Local), page after 2 s) | supervision spacing 5 s |
| Reconnect where BlueALSA refused the configuration (A2DP.InvalidChannels) | connected without services, cancelled after STUCK 12 s, then Ready | STUCK 12 s (shorter would cut real slow set-ups) |
| Pause with a 10 s keep-alive | one AVDTP Suspend in three unanswered ("No reply to Suspend request"), link dropped 3 s later | keep-alive raised to 900 s (build 210) |
| Pause and resume inside a started stream (keep-alive 900, 9.3.7–9.3.11) | AirPods Pro silent after every pause/resume gap of 0.4–0.6 s and after track changes that followed one; packets ran on at 47/s with no gap at the skips themselves (btmon 21:10 2026-11-04), so the sink, not the sender, had stopped; a new stream (AVDTP Start) always played | keep-alive back to 0 (9.3.12): Suspend at the pause, Start at Play, as 9.2.16 ran; a kept sink keeps its audio at a track change |
| Daemon CPU while settled | 0 ticks in 30 s | — |
| Codec settings change with the headset connected (9.3.3 → 9.3.4) | 34 s (half set-up link) → 7–9 s (clean disconnect, restart, reconnect) | HALF_CONNECTED 8 s |
| Wake with AirPods reconnecting on their own (9.3.4) | ≈15 s: BlueALSA refuses their AAC configuration (A2DP.InvalidChannels), cancelled after 8 s, the daemon's own page works. btmon: their SetConfiguration sends AAC octet 3 = 0x07 (stereo plus the two bits A2DP 1.3 reserves and 1.4 reads as 5.1/7.1); ours sends 0x84 | BlueALSA patch 0006 reads stereo plus those bits as stereo (9.3.5, build 213) |
| Wake with AirPods reconnecting on their own (9.3.5) | configuration accepted, stream open after 0.2 s, yet cancelled after 8 s as half connected; wake 21 s once in five (others 5.8–7.8 s). BlueZ 5.87 resolves no services for a known headset that connects to us (ServicesResolved false for the whole connection) | set up = resolved services or a BlueALSA stream (9.3.6, build 214) |
| Wake with AirPods reconnecting on their own (9.3.6) | Ready 2.1 s and 2.6 s (paged wakes 5.2–7.6 s, 0 cancels in 19 wakes), audio plays; but the codec decision saw no mutually usable codec: BlueALSA listed the headset's codecs only after BlueZ asked them, ≈20 ms after the stream | wait up to 3 s for a codec list that contains the running codec (9.3.7, build 215) |
| Wake with AirPods reconnecting on their own (9.3.7) | four of four came back by themselves, Ready 2.5–4.9 s, AAC mutually usable and Settled every time, no page, no refusal | — |
| A pause longer than ≈22 s (9.3.7, Wi-Fi on or off, paged or self-reconnected link) | AirPods stop answering at the baseband ≈2 s after the pause (last packet from them at the pause, no sniff or role change), the link ends with a supervision timeout (HCI 0x08) 20 s later, AirPods reconnect within 0.4–3 s. A resume inside those 20 s plays into a dead link | open: what silences them (headset idle behaviour or our keep-alive stream without packets); link supervision timeout is the controller default 20 s. btmon on this platform shows no A2DP media packets (also on healthy links), so audio flow is not visible in captures |

After the owner's second round (2026-11-03): Bluetooth off and on is the owner's restart (no separate button); stream lease from Reborn; `ReloadCodecs` (no player restart for codec settings); Wi-Fi power save while streaming; learned start rates (patch 0005); AirPods' own AAC configuration accepted (patch 0006); `status` asks the daemon; #78 Connect Automatically in Reborn; six fake-BlueZ scenarios. Remaining from §8's list: the Wi-Fi association controller (P7), other headsets, an overnight.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
