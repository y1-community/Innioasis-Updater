---
title: "Platform Rust: the remaining refactor, for one agent (written 2026-10-30, after test build 175) - Innioasis Updater"
description: "Platform Rust: the remaining refactor, for one agent written 2026-10-30, after test build 175 One agent works through this alone, in order, without spawning others. Every"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-platform-rust-next-agent-handoff.html"
---

# Platform Rust: the remaining refactor, for one agent (written 2026-10-30, after test build 175) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform Rust: the remaining refactor, for one agent (written 2026-10-30, after test build 175)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform Rust: the remaining refactor, for one agent (written 2026-10-30, after test build 175)

One agent works through this alone, in order, without spawning others. Everything needed is here or linked. Read this file, then §1 and §3 of [PLATFORM-RUST-REFACTOR-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-REFACTOR-PLAN.md) (the contract and what was already done), then start at §4 below.

Superseded for the next work by [PLATFORM-RUST-IDIOMATIC-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-IDIOMATIC-PLAN.md) (owner 2026-10-30: byte identity dropped; §2–§3 here still apply where that plan does not replace them).

## 0. Status of this pass (2026-10-30/31, one agent overnight; updated as items finish)

Baseline: byte goldens recorded from 2e68d63e (test build 175's code). Owner decisions for §5 given up front (2026-10-30): 1 strictest equality that keeps every golden; 2 enums only, no typed shutdown intent; 3 do not merge the volume observers, share constants/helpers only; 4 keep blkid in status and y2-bt-observe; 5 keep the reports `Py` type; 6 keep the bool tolerance of `status_query_failures`; 7 keep renewing network.json/time-status.json on a cheap timer (no Reborn change).
  - A done (all byte-identical, gate OK each):
    - lenient record fields moved to `y2p_core::lenient` (+ `BootId`, `number`, `integer`, `truthy`, `is_true`,

`json_number`);
    - A1 ssh.json: `devices::ssh::Published` (is_this_boot, fresh);
    - A2 network.json: `connectivity::published::{Record, Published, QueryFailures}` (bool kept, decision 6);
    - A3 power.json readers: `power::published::{PowerState, Battery, BatteryReading}` (reports upload keeps `Py`);
    - A4 Y2Media claim: `storage::internal::{Claim, ready}` for all four copies; decision 1 → texts compared

exactly, mount id a JSON number compared as Python numbers (a golden holds `41.0`), never a bool; SD claim: `storage::records::Claim::checking` for the service daemon;
    - A5 `update::JournalState` (+ `TERMINAL` once) and `staging::Download` (download.json, one struct);
    - A6 `usb::views::View` + typed identity;
    - A7 previous-boot-evidence.json written from `evidence::Evidence`/`LogTail` (readers pass through / `Py`).

  - B done (byte-identical): `y2p_core::volume::{VolumeState, SpaceState}` (also in storage/observe.rs and the

status snapshot); `power::policy::BatteryState`, `power::battery::{BatterySource, Confidence}`; shutdown `IntentState`/`ShutdownAction`/`ShutdownReason` (intent record stays a map, decision 2); Internal Storage `SetupState`/`SetupPhase`; update `JournalState` (with A5).
  - C partly done: thermal, memory and readiness sections built from typed records (key order kept).

Left (time, the night's budget went to D–J and two device installs): power, cpu, idle, wifi, storage, system sections, and typed reads in readiness/health (they still read the snapshot map by key).
  - D partly done: one `jobs::poll` (Slot) for the job children + one `Timer` for the loop deadlines (the

base for I); reports `check` split into ten trigger functions; upload's print-then-parse → `time::tls_ready`. Left: cpu.rs table, maintenance `execute`, bluetooth `normalize`, `idle_completion`, arguments parsed twice (cli → typed values).
  - E partly done: one volume constant table (`y2p_core::volume`: controllers, UUIDs, Y2Media geometry,

`expected_uuid`, `controller`); one `space_state` budget (the observers stay separate, decision 3); bench `Error: From<io::Error>`; reports `isoformat` = `utc_isoformat`; "this boot" checks of the typed records go through `lenient::BootId` (A). Left: the remaining hand-written this-boot comparisons, sleep status twice (byte check), power vs suspend journal rows (byte), ssh wake fold, the five poll loops (rounding), the two repr/serialisers (byte decisions).
  - F partly done: transfer/fd.rs has no unsafe (new `sys::{linkat, read, write}`); bench scratch 9 → 2

(geteuid). Left: power/unix.rs (bind/listen with backlog 4 between them, SO_PEERCRED: std has no stable peer_cred), suspend/helper/kernel.rs.
  - H kept as is (decision 5: reports `Py` stays; the A readers replaced the record-level py_eq/truthy;

`python_int` → `parse` would change odd sysfs input the goldens pin).
  - Test build 176 (seq 11210, commit 6fd3e065: A–F above) built, host suite OK, staged (Queued) and applied

2026-10-30 03:48:30 by staged OTA. The player's USB network did not come back: the gadget enumerated (MTP + ECM, 03:49:23) and MTP answers from the PC (Internal Storage, SD Card), but usb0 carries nothing (host rx 0, ARP failed, SSH "No route to host" through 04:00). Acknowledgement and the device check could not be read. As the owner asked for this case: written down, device work stopped — no 177, no idle measurement.
  - After 176, committed but not built (gate OK, host suite OK on db11884f): I-groundwork from strace on 175

(a dark service pass ≈550 syscalls, mostly the SD inventory): `storage::sys::emmc_entry` skips the 11 eMMC class entries after one readlink in the inventory and the candidates scan, and the USB tick's change signature reads only non-eMMC entries; J1: the power daemon reads BAT0 voltage_now/present/status/ charging_state by pread from kept descriptors (`y2p_core::root::Attribute`; strace on 175: ≈46 calls/sample).
  - G not done: needs the player over SSH (the probes and the comparisons against wpa_cli/ip/date); stopped.
  - I not done beyond the groundwork above. Facts read on 175 before the install: kernel 6.18.56, UDC

`musb-hdrc.4.auto` (state `configured`), backlight `y2-backlight` (bl_power, no notify expected from the backlight core for bl_power), strace available on the player. USB plug, SD insert/remove and the dark/lit change need the owner's hands, so those sources stay polled (owner's rule); the gain must then come from a cheaper pass (the inventory/signature work above) rather than a longer interval.
  - J: J1 committed (not built); J2 (Reborn wifi/avrcp threads) and J3 (boot-stage profiling) not done

(device needed).
  - Morning (2026-10-30), second agent: the owner replugged USB at 07:34; 176 was Acknowledged. Cause class:

usb0 had its address from 10.7 s; the host's cdc_ether logged transmit-queue timeouts (the gadget's ECM bulk-OUT took nothing) until the re-enumeration; first such timeout in the host journal since 10-26, no controller fault counter set, 176 touches no gadget/ECM code → one-off, cause not found (if it repeats: read the controller's `rxdiag` and `status` before replugging). 176 device check OK; idle 176 (charging, 231 min): power 6.2, service 7.7, ssh 2.0, connectivity 0.1, Reborn 14.5 s/h.
  - Test build 177 (seq 11220, 9f708af2 = db11884f + bump: eMMC skip + BAT0 pread) staged and applied 07:46:49,

Acknowledged, USB clean, device check OK. strace: power daemon ≈29 calls/sample (≈46); service pass every 10 s ≈560 calls, eMMC entries one readlink each; left per pass: the SD sysfs path canonicalised 4×, media-mount.json 4×, mountinfo 3×. Idle 177 (battery Full, 30.6 min, builtin-only script): power 4.1, service 4.9, ssh 2.0, connectivity 0.2, Reborn 12.5 s/h; process starts 3.0/min.
  - Late morning (2026-10-30), same agent, test builds 178 and 179 (details: roadmap-gap-audit.md):
    - item 9 done: wlan0 counters by rtnetlink; `y2p_core::sys::real_path`; service 4.9 → 4.2 s/h dark.
    - J3 done as analysis + one fix: application_ready within a pass on plain restarts (was up to 30 s late); boot

profile in the audit; owner decisions there: the connectivity driver's fixed 5 s `msleep` in `pmic_prepare` (move to probe time?) and boot-gate holding Reborn until the radios are up.
    - C done: all six status sections built from types (power, cpu with IdleState, idle completion, wifi, storage,

system). Left on purpose: typed reads in readiness/health (the snapshot holds Values: `status <section>` prints sorted, diagnostics export walks insertion order; typed reads would re-deserialize or change every consumer).
    - D done except "arguments parsed twice" (left: the three re-parsers see only cli.rs's canonical form; typed

values from cli.rs means reworking all eight groups' routing). Bluetooth normalize and reset execute split into steps; idle_completion typed and split.
    - E done except the two repr/JSON serialisers (they differ for odd input: owner decision) and the ssh wake fold

(different signals/flags; its errno save moved into signal_wake! instead): Root::is_this_boot, one sys::poll, one sleep status, one setup_status.
    - F done: no unsafe in power/unix.rs and suspend/helper/kernel.rs (new sys wrappers).
    - G: health-ack's rebornctl → control socket; Reborn's once-a-minute `sleep request` on the cable stopped

(Reborn 764b024 + 68af9ac). Left on purpose (event-only, Wi-Fi/clock risk for a few starts per event): wpa_cli -g interface_add/remove/list and autoscan, ip flush/addr/route on DHCP/supplicant events, busybox date -s, the report build's children.
    - I and J2 not done: both need the owner's hands (event sources; Bluetooth headphones for avrcp).
    - 178 (seq 11230) and 179 (seq 11240, Reborn 68af9ac) Acknowledged, device checks OK; 179's health-ack went

through the control socket. Next free label 180, sequence above 11240.

  - Owed (owner): the hands-on event-source checks for I (USB plug/unplug, SD insert/remove, screen dark/lit with

a uevent/POLLPRI probe); the two boot decisions above; §7 below.

## 1. Where it stands
  - The platform is Rust only: `platform/` (crates `y2p-core`, `y2p-contract`, `y2-platform`), about 49,600

non-test lines, built into `/usr/sbin/y2-platform` (32-bit ARM, armv7). No Python runs on the player.
  - On the owner's player: test build 179 (sequence 11240, Reborn 68af9ac), installed 2026-10-30 11:21 (see

§0). All work is on local `main` (Y2Linux and Y2Reborn); nothing is pushed. Next free label 180, sequence above 11240.
  - Done so far (details in the refactor plan and `roadmap-gap-audit.md`): the port (170), the refactor plan's

waves 1–2 (171), quick wins (172), the duplication pass and idle gains (173), the "next pass" P1–P9 (174/175): shared helpers in `y2p_core` (paths, digest, text, clock, json, lock, sys, record, power_journal, regex!), From<io::Error> errors (`Failure`, `Raise`, suspend `E`, service errors) and `io::Result::at(path)`, safe syscall wrappers (`y2p_core::sys`: netlink, pidfd, kill/alive, `*at`, dir_names, unix sockets), one signal self-pipe macro (`signal_wake!`), direct kernel/supplicant reads (`connectivity::direct`: wpa control socket, rtnetlink addresses/routes, nl80211 power save), per-volume probes, the space policy inside the service daemon, the USB tick never waiting for `media.lock`, power.json written every 2 s.
  - Measured on the player (screen off, charging): Reborn 45 → 14–19 s/h; daemons power 7.3, service 7.7, ssh

1.9, connectivity 0.1 s/h; ≈10 process starts/min after start-up (was ≈140).

What still follows Python (2026-10-30 count, non-test code): ~1,650 `serde_json::Value` mentions, ~910 `json!`, ~500 `.get("field")` lookups against ~70 typed `Serialize` records; ~170 `&'static str` states.``````

| group | lines | Value | json! | Python emulation | typed records |
| --- | --- | --- | --- | --- | --- |
| reports | 7,700 | 22 | 23 | 544 (the Py value type) | 3 |
| observation | 6,300 | 539 | 300 | 56 | 0 |
| service | 6,000 | 215 | 117 | 65 | 1 |
| suspend | 5,000 | 207 | 81 | 35 | 21 |
| storage | 4,300 | 132 | 99 | 33 | 12 |
| connectivity | 3,900 | 132 | 143 | 15 | 6 |
| power | 3,600 | 115 | 2 | 26 | 9 |

The owner's view (2026-10-30): the gain of more typing is correctness and maintainability, not speed. Do it selectively: first the records written by one component and read by another, then a group when it is changed anyway. Leave stable, rarely touched code (report building, bench) unless an item below names it.

## 2. Rules (do not break)
  - Output contract: every command's stdout, exit code and written files stay byte-identical (json.dumps

spacing, key order, Python float repr, error texts) unless an item says "owner decision" and the owner said yes. Internals may change freely.
  - One concern per commit; never behaviour and structure in one commit. Commit messages describe the change and

end with what was verified ("outputs byte-identical" or which goldens were re-recorded and why).
  - Git: the configured identity, no model attribution, no `git stash`, no push, tag, `release.py publish` or

GitHub post without the owner's word. (AGENTS.md; memory "Git identity for commits".)
  - The player: install test builds only by staged OTA (§6). Ask before anything that powers it off, needs a

button press, or writes registers. Never run the capture tool without a head.
  - Do not touch the tree while `release.py build` runs.

## 3. Method (what made 173–175 safe)
  - Record the byte baseline once from the commit you start at:

`tools/development/platform-gate.sh --baseline <dir outside the repo>` (e.g. the session scratchpad).
  - After every change: `tools/development/platform-gate.sh <that dir>` must print `GATE OK` before the commit

(fmt, clippy with no warning, armv7 check, all cargo tests, byte comparison of every golden case).
  - A change that deliberately alters recorded calls (a process no longer started) or written files:
    - re-record: `Y2_PLATFORM_RUST=$PWD/platform/target/debug/y2-platform Y2_RECORD_GOLDENS=1 PYTHONPATH=.:tests

python3 -m unittest tests.test_platform_differential tests.test_platform_devices tests.test_platform_reports tests.test_platform_observation tests.test_platform_suspend tests.test_platform_power_rpc`;
    - review the git diff of `tests/platform_goldens/` (only `calls`/`tree` may change; compare old/new with a

small script, as in the 174 commits);
    - check that the gate's differing cases are exactly those goldens, copy them from `<dir>.now/` into the

baseline and note why;
    - say so in the commit message.

  - Before a build: `tools/development/host-tests.sh` (576 tests) must pass.
  - Traps seen: `cargo fix` removes imports only a `use super::*` test module needs (give the test module its own

`use`); a regex rewrite also catches the body of a new `impl From`/trait method (check for self-recursion); lock helpers retry 0.2 s in test builds (`lock::settle`), so timing asserts need slack; take kernel ABI numbers from a C compile, not from parsing headers.

## 4. The work, in order

Each item: where, what the Rust shape is, risk, how to verify. Sizes: S < 1 h, M ≈ half a day, L ≈ a day.

### A. Typed records shared between components (do first; S–M each, byte-identical)

Pattern: a `#[derive(Serialize, Deserialize)]` struct per record, defined once (writer's module or `y2p_contract`), field order = today's written order (records written by `atomic_json` are sorted anyway, so order is free there; printed unsorted records keep insertion order). Readers use a lenient load (missing or odd fields → the same fallback as today) — the pattern is `connectivity/record.rs`.
  - `/run/y2/ssh.json`: writer `devices/ssh.rs` (`struct State`), reader `observation/system.rs``fn system`

(`get_eq(&ssh, "boot_id", …)`, `fresh_seconds(… "monotonic_s" …)`). One `SshRecord` with `is_this_boot()` / `fresh(seconds)`.
  - `/run/y2/network.json`: written by `service/daemon.rs` (the Wi-Fi pass), read by

`connectivity/daemon/supervisor.rs` and `connectivity/wifi/recovery.rs` (untyped reads), observation, Reborn. `query_failures` keeps a bool from old records (owner decision to drop that tolerance — ask, else keep).
  - `/run/y2/power.json` readers: `suspend/admission.rs``fn battery_and_cable` (reads state, battery,

filtered voltage, percent, confidence untyped), `storage/media/repair.rs` battery check, reports upload. A lenient `PowerState` view next to `power/daemon.rs``PowerRecord`.
  - `/run/y2/media-mount.json` (the SD claim) and the Y2Media claim: the internal-media claim check exists 4

times with different equality rules — `observation/system.rs` (`internal_ready`), `devices/storage.rs`, `storage/internal.rs`, `service/radiofw/copy.rs`. One typed claim + one `ready(root)`. Byte-check carefully: the copies compare with `py_eq` vs `==` vs `eq_int` (differ only for odd values; pick the strictest that keeps every golden, note it).
  - Update journal state: `state_is(&status(root))` in `service/update/{apply,check,health,staging}.rs` builds

the whole status (download.json, /proc/locks, last-check.json, channel) just for `state`; use `update::journal_state` and a `JournalState` enum. `download.json` has 7 `json!` shapes in `staging.rs` → one struct.
  - USB views (`service/usb/views.rs`, built as `Object` and read back with `py_text`/truthy): a `struct View`

in the same field order.
  - previous-boot-evidence.json: written in `observation/evidence/mod.rs` (16 inserts), read in

`observation/system.rs`, `reports/checks.rs`, `reports/diagnostics.rs`.

### B. State enums (S each, byte-identical: unit variants serialize as the same text)
  - `y2p_core::volume::Volume.state` / `space_state` (`&'static str`) → `VolumeState`, `SpaceState`; the same in

`storage/observe.rs` and `observation/snapshot/storage.rs`.
  - Low battery and the daemon state (`power/policy.rs``LowBattery`, `power/daemon.rs`, `power/journal.rs`,

`suspend/admission.rs`); `BatteryStatus``source`/`confidence` (`power/battery/status.rs`, `soc.rs`).
  - Shutdown intent state/action/reason (`power/coordinator.rs`, `coordinator/steps.rs`). A fully typed intent

record is an owner decision: the socket reply is unsorted and a resumed intent has the file's sorted order.
  - Internal Storage setup phases (`storage/internal/setup.rs`; persisted on /data, keep the texts).
  - The update journal states (with A5). `TERMINAL` is defined twice (`service/update.rs`, `reports/maintenance.rs`).

### C. The `status` snapshot as types (L; byte check needed)

`observation/snapshot/*.rs` and `observation/system.rs` build ~270 maps; `readiness.rs` and `health.rs` read them back by key (18 lookups each). Status and health print sorted, but **diagnostics export projects the snapshot in insertion order**, so struct field order must equal today's insertion order. Go section by section (power, thermal, memory, cpu, idle, wifi, storage, system, readiness), one commit each.

### D. Control flow (M each, byte-identical)
  - Service daemon loop (`service/daemon.rs``fn serve`, 142 lines, 12 mutable loop variables) and the five

hand-written child slots in `service/daemon/jobs.rs` (`media_reconcile`, `media_verify`, `daily_update_check`, `error_reports`, `radio_firmware`): one `Job { child, started, retry_at, limit, backoff }` with `poll(now)`, one deadline struct for the timers. The goldens' `calls` lists pin the order — no re-record should be needed.
  - Long functions mixing I/O and decisions: `reports/checks.rs``fn check` (≈290 lines, 10 triggers → one

function each), `observation/snapshot/cpu.rs` (≈290; ~25 reads fit a table), `reports/maintenance/execute.rs``fn execute` (≈300), `observation/bluetooth.rs``fn normalize` (≈220), `observation/snapshot/idle.rs``fn idle_completion` (≈220).
  - Arguments parsed twice: `cli.rs` hands a canonical `Vec<String>` that `observation/mod.rs`,

`reports/mod.rs` and `devices/mod.rs` parse again; let the parser return typed values.
  - Print-then-parse: `reports/upload.rs` formats the time status and parses it back for `tls_ready`; use

`time::status_at(..)` directly.

### E. Remaining duplicates (S each unless noted)
  - Three volume observers (`y2p_core::volume`, `storage/observe.rs`, `observation/snapshot/storage.rs`), with

`space_state` ×3, `media_identity` ×2, `refused_card` ×2, and the UUID/geometry constants in 5 places (`y2p_core/volume.rs`, `storage/observe.rs`, `snapshot/storage.rs`, `service/usb/views.rs`, `storage/internal.rs`). One constant table first (S, byte-identical); merging the observers is L and changes bytes where their records differ → owner decision.
  - "This boot" checks: 16 hand-written comparisons in 5 spellings (`get_eq(…"boot_id"…)`, `py_eq`,

`this_boot` in `service/daemon.rs`, …). A `Root::this_boot(value)` helper; note the null case (an unreadable boot id equals a null record field in some spellings, not in others) — keep each site's behaviour.
  - Sleep status twice: `power/journal/sleep.rs``sleep_status` and `commands/sleep.rs``product` differ on odd

`product` values; merge only with a byte check.
  - Power vs suspend journal rows: device readings are shared now (`power::journal::devices`); the rest differs

in serialisation (suspend sorts nested values with `plain`) → leave unless the owner accepts a byte change.
  - The ssh daemon's own signal/netlink wake (`devices/ssh/wake.rs`, saves errno) vs `signal_wake!`: fold in if the

errno save can move into the macro.
  - Five poll-with-deadline loops (`connectivity/daemon/wait.rs`, `devices/ssh/wake.rs`, `power/unix.rs`,

`suspend/receipt/rpc.rs`, `service/download.rs`): they round the timeout differently (up vs down to ms) — one `y2p_core::sys::poll(fds, deadline, Rounding)` keeps each one's rounding.
  - Two `repr` (`y2p_core/py.rs` vs `argparse/python.rs`; the core one does not escape non-printable non-ASCII)

and two JSON serialisers (`y2p_core::pyjson::dumps` vs `json::PythonFormatter`, different `\udcXX` handling): byte decisions, merge only where the goldens prove them equal.
  - The bench `Error` type (`observation/bench/mod.rs`): `From<io::Error>` like the others.
  - UTC ISO formatting in `reports/clock.rs` (`isoformat`, libc gmtime) vs `y2p_core::devices_support::utc_isoformat`.

### F. Remaining `unsafe` (173 blocks; M)

`observation/bench/scratch.rs` (11, raw fds: give it `OwnedFd`/`BorrowedFd` like `devices/transfer/fd.rs`), `devices/transfer/fd.rs` read/write (a `ManuallyDrop<File>` over the borrowed fd removes two), `power/unix.rs` accept/peer credentials, `suspend/helper/kernel.rs`. Leave `y2p_core/reports_sqlite.rs` (behind a clean API).

### G. Process starts that remain (M each; device test required)
  - `wpa_cli` in `connectivity/wifi/scan.rs`, `wifi/recovery.rs`, and the global-socket commands in

`connectivity/daemon/supervisor.rs` (`interface_add/list/remove`, `autoscan`). `direct::wpa_cli` upper-cases the whole command — change it to upper-case only the verb and take the socket path (the global socket is `/run/wpa_supplicant/global`). `interface_add`'s tab format depends on the wpa_cli version → byte check. Must stay processes: `wpa_cli -a` (the action daemon), `wpa_supplicant -B`, `start-stop-daemon`, `wpa-event`.
  - `ip` flush/addr/route on DHCP and supplicant events (`commands/network.rs`) → rtnetlink writes. Device test:

connect, disconnect, sleep/wake, lease renew.
  - `busybox date -s` (`devices/timekeeping.rs`, `time.rs`) → `clock_settime` (safety: the clock floor; test NTP

and the manual time set).
  - `rebornctl status --json` in `service/update/health.rs` → Reborn's control socket (as

`observation::reborn_metrics` does).
  - The report build's children (`reports/build/sources.rs`: `y2-platform status`, `health`, `rebornctl

metrics`) → in process; byte check of the bundle members.
  - Leave: the two bounded `cat`s in `observation/snapshot/cpu.rs` (wakeup_count is a suspend handshake that can

block), curl, fsck/mkfs/resize2fs, y2-update-core, init scripts, dropbear, umtprd, every SD mount/remount.
  - Owner decision before doing: `blkid` in `status` storage → ext4 superblock read; `y2-bt-observe` gating

(measure its cost on the player first).

### H. The Python-emulation layer (decide per use)

Keep where it makes the output (`py::os_error` texts, Python float repr, `json.dumps` spacing, argparse error texts). Replace with plain Rust where it is not visible: `py::truthy`/`py_eq` on values the code itself wrote, `python_int` for sysfs/procfs numbers (`trim().parse()` gives the same; pid files need a check). The `reports` group's `Py` value type tolerates odd old records exactly as Python did; replacing it is an owner decision (refuse odd values instead of tolerating them).

### I. An event-driven service daemon (L; the one item left with a real CPU gain; device tests required)

Owner (2026-10-30): "nice to have, put it in the handoff". Do it after A–H, in its own commits, never mixed with a structural change.

Today:`service/daemon.rs``fn serve` runs a full pass every 3 s lit / 10 s dark (`INTERVAL_S`, `DARK_INTERVAL_S`), waking early only for supplicant events and signals (`monitor.wait(.., wake.fd())`). Each pass: `display_dark` (backlight glob + 2 reads), `usb.tick` (UDC glob and state, usb-mode.json, block and mount snapshots, write windows), the Wi-Fi look (cheap now: direct reads), coexistence, the 30-s radio policy, `network.json` and `time-status.json` writes, the media reconcile/verify, firmware and report job slots, NTP (60 s) and the maintenance pass (30 s lit / 300 s dark). Measured 7.7 s CPU/h dark on 174; the expected gain is about half of that, plus faster reactions (USB, SD card, Wi-Fi).

Shape: one poll set and one deadline:
  - what is already there: the supplicant event socket and the signal pipe;
  - new event sources:
    - rtnetlink link/address events (`y2p_core::sys::netlink_route(1 | 0x10, true)`, as the connectivity daemon

does);
    - kernel uevents (`y2p_core::sys::netlink(libc::NETLINK_KOBJECT_UEVENT, 1, true)`) for UDC, power_supply and

block add/remove (SD insert/remove);
    - `/proc/self/mountinfo` with POLLPRI (mount and remount);
    - POLLPRI on sysfs attributes that `sysfs_notify` (the UDC `state`).

  - Check each source on the player's kernel first (6.18 with the Y2 drivers; the `y2-backlight` driver and

`y2-usb` may not notify): a small probe that waits on each source and prints what arrives while the owner plugs USB, inserts the SD card and lets the screen go dark. A source that does not notify stays polled.
  - The display state: if `bl_power` does not notify, poll it alone (a two-file read) or have Reborn signal the

service daemon (SIGUSR1 already means "look now").
  - One `Deadlines` struct for the timers (maintenance, NTP, radio policy, job retries, report check) — this

overlaps with D's `Job` type; do D first.
  - A fallback full pass (e.g. every 30 s lit / 120 s dark) so a missed event costs at most that delay.

Constraints:
  - Reborn treats `network.json` as stale after 15 s (an Online record after 45 s); `time-status.json` is read by

Reborn's scrobbler (`tls_ready`). Either keep renewing both within those bounds (a cheap write on a timer, no full pass), or change Reborn's freshness rule in the same release — a coordinated Reborn change, **owner decision**.
  - The goldens run the loop for N ticks below a fixture root (`Y2_DAEMON_TICKS`): keep a tick-equivalent mode

for them so the recorded calls stay comparable; expect deliberate re-recordings and review them as in §3.

Verify on the player:
  - per-daemon CPU before/after (≥ 30 min uptime, screen off, as in §6), plus `voluntary_ctxt_switches` from

`/proc/<pid>/status` (wake-ups);
  - USB: plug and unplug (MTP appears and goes, and the screen lights within ~1 s);
  - SD card: insert and remove (admission, write window);
  - Wi-Fi: connect, disconnect, sleep and wake (Online again, `network.json` fresh);
  - the screen: lit vs dark cadence;
  - the daily update check and report check still due on time.

### J. Smaller idle items (S–M)
  - Power daemon (7.3 s/h): keep the BAT0 attribute descriptors open and `pread` at offset 0 each second instead

of open/read/close (≈40 → ≈10 syscalls per sample). Keep the 1-s cadence (the low-battery policy's timing).
  - Reborn (Y2Reborn repo, its own commits with the Luca identity env vars): the `wifi` thread (2.8 s/h) and

`avrcp` (1 s wait plus `GetNameOwner` every 3 s, 1.3 s/h) are the next polling candidates after 173's dark cadence.
  - Boot time (≈37–40 s to `application_ready`) was never profiled stage by stage; `/run/y2/boot-stages.jsonl`

and the boot journal give the stage times — likely the most noticeable gain left for the owner.

## 5. Owner decisions to ask for (only when the item comes)
  - A4: which equality the Y2Media claim uses when the copies disagree on odd values.
  - B: a fully typed shutdown intent (changes a resumed intent's reply order).
  - E: merging the three volume observers (byte changes where their records differ).
  - G: ext4 superblock instead of `blkid` in `status`; gating `y2-bt-observe`.
  - H: replacing the reports `Py` type (refuse odd old values).
  - A2: dropping the bool tolerance of `status_query_failures`.
  - I: keep renewing `network.json`/`time-status.json` on a timer, or change Reborn's 15-s freshness rule with

the event-driven daemon.

## 6. Build, install, verify`tools/development/host-tests.sh # bump "update_sequence" in tools/production/release.json above the installed one, commit (tree clean!) Y2_STOCK_PACKAGE=$PWD/donorSource/y2_v3.2.0_FM-20260813 python3 tools/production/release.py build --label 176 Y2="ssh -F /dev/null -o HostKeyAlias=y2linux-production-v1 -o BatchMode=yes -i ~/.ssh/y2linux_ed25519 root@10.42.0.1" $Y2 'rm -rf /data/updates/owner-175; mkdir -p /data/updates/owner-176' scp -F /dev/null -o HostKeyAlias=y2linux-production-v1 -i ~/.ssh/y2linux_ed25519 -q out/release-176/ota/* root@10.42.0.1:/data/updates/owner-176/ $Y2 'y2-platform update stage --package /data/updates/owner-176; y2-platform update apply' # wait (one ssh after ~3 min, not a polling loop): update status must say Acknowledged $Y2 'sh -s' < tools/development/platform-device-check.sh`

A packaging step refuses an uncommitted tree; a failed build resumes on the next run. Idle measurement: one script on the player (per-process utime+stime from `/proc/<pid>/stat` and Reborn's threads from `/proc/<pid>/task/*/stat`, `processes` from `/proc/stat`, before and after `sleep 300`), started with `nohup`, read back with a single `sleep 330; ssh …` — every ssh session itself starts processes. Measure after ≥ 30 min uptime (start-up work inflates the first minutes). Never `pkill -f` a pattern that occurs in your own ssh command line.

Afterwards: an entry in `roadmap-gap-audit.md` (as for 173–175), the START HERE block in `NEXT-SESSION-HANDOFF.md`, the refactor plan's status, and the memory file `y2-platform-rust-port-phase0.md`.

## 7. Still owed from 173–175 (not code)
  - A long-uptime idle measurement on 175 (power.json now every 2 s; compare the power daemon with 174's 7.3 s/h).
  - The owner's dark-wake checks: Power after > 1 min dark, a computer lighting the screen within ~1 s, Bluetooth

headphones connecting and their Play button, the automatic sleep ~60 s after dark on battery.
  - PLATFORM-RUST-PORT-HANDOFF.md §6 A hardware checks.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
