---
title: "Platform Rust refactor: from ported Python to idiomatic Rust - Innioasis Updater"
description: "Platform Rust refactor: from ported Python to idiomatic Rust Status 2026-10-30 morning: the follow-up work is tracked in PLATFORM-RUST-NEXT-AGENT-HANDOFF.md §0 has the st"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-platform-rust-refactor-plan.html"
---

# Platform Rust refactor: from ported Python to idiomatic Rust - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform Rust refactor: from ported Python to idiomatic Rust

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform Rust refactor: from ported Python to idiomatic Rust

Status (2026-10-30 morning): the follow-up work is tracked in PLATFORM-RUST-NEXT-AGENT-HANDOFF.md (§0 has the state: A–F done (with stated exceptions), G partly, I/J2 need the owner; test builds 176–179 on the player). Earlier status: done 2026-10-29: test build 171 (sequence 11160) is on the owner's player, Acknowledged. Both waves are merged on `main`; the resume-point and progress notes below are history. Owed: the owner's hardware checks on 171 (170 is the comparison point); open owner questions: Python wording left in some refusal texts, whether the remaining radios are restored after a failed Wi-Fi restore after sleep, whether service-daemon should skip odd records (now) or end with an error record, whether an unreadable queued error report should be dropped. Still open from the plan: event-driven daemons (§2.5, needs drain measurements), merging the Python text helpers that remain per group (suspend_text, power_text, observation util, reports pyre, storage_media), the reset plan and diagnostics input as `Py`, the duplicate journal code in suspend and power.

Progress (2026-10-29, stopped at the usage limit): wave 1 is merged on `main` (2f5b5075): the argparse emulation is replaced by `crates/y2-platform/src/cli.rs` (table-driven, `y2-platform __arguments` feeds platform-contract.py) and one shared core exists (y2p-core `json::{Object, ObjectExt, dumps_sorted}` with serde_json `preserve_order`, `py::PyValue`, `mounts`, `Root::boot_id`, `record::atomic_json`, `lock`, `volume`, `sys` libc wrappers, `Runner`/ `Clock` carried by `Root` with `Root::fixture(..).with_answers(..)`); goldens unchanged except the parser's deliberate ones. The golden suite sorts JSON before comparing: key order/spacing must be checked by comparing raw output against a baseline binary (wave 1 did this for all 1 063 cases). Next: wave 2, one agent per group (observation, connectivity, devices, storage, service, reports, power, suspend): adopt the core, typed records, tests from `scripted` to `Root` injection (then delete the thread-local and `#[cfg(test)]` seams), crash paths → refusal records, split long modules, merge the duplicated Python text helpers (suspend_text, power_text, observation util, reports pyre), per-tick work in the daemons, connectivity: same-lease renew no-op and the DNS fixture argv. Then host suite, build 171, OTA. Not built or installed yet; the player runs 170.

Resume point (2026-10-29, evening, usage limit near): wave 2 runs as eight agents in git worktrees under `.claude/worktrees/agent-*`, one branch per group. Merged on main: all eight groups (plus wave 1); next: the cleanup, checks, CONTRACT.md, build 171 and OTA below. Still on their branches (each commits per step; continue or merge what is there):
  - `worktree-agent-a0b52a2b44f9ce140` (reports, 13 commits ahead)
    - `worktree-agent-a115c1c7ce4e9d7b8` (observation, 4 commits ahead)
    - `worktree-agent-a1c2243b5ac75c531` (connectivity, 0 commits ahead)
    - `worktree-agent-a477aa6d9dcdec7ee` (service, 14 commits ahead)
    - `worktree-agent-ac8c4198751694718` (devices, 0 commits ahead)
    - `worktree-agent-ac93928f7eee6d545` (storage, 6 commits ahead)
    - `worktree-agent-ad5a8d3f056847cef` (suspend, 9 commits ahead)
    - `worktree-agent-adb52e26588f16add` (power, 8 commits ahead)

To resume in a fresh session: for each remaining branch, check `git log main..<branch>` and whether its worktree has uncommitted changes (`git -C .claude/worktrees/<agent> status`); merge finished branches into main (`git merge --no-edit <branch>`; conflicts so far were only test-module include lines and docs), or let a new agent finish a group from its branch with this plan's wave-2 brief (the step list in the progress note above). After all groups: delete `crate::testing::scripted` and the thread-local in `y2p_core::command::testing`, remove `codec::not_iterable` if unused, run `cargo test`/clippy/armv7, the golden suite and the byte check (`tools/development/platform-raw-goldens.py` against a pre-wave-2 build of main 342d08e0: only crash-path refusal, same-lease renew and DNS-argv cases may differ), update CONTRACT.md (refusal reasons, dhcp.json `prefix_length`/ `routes`, same-lease renew, parser), the host suite, then `release.py build --label 171` (bump sequence above 11150 first) and install by staged OTA (PLATFORM-RUST-PORT-HANDOFF.md §5).

Quick wins after 171 (2026-10-29, test build 172): atomic_json no longer deletes after a successful rename; one `y2p_core::text` (Python's whitespace and line rules) instead of five copies; one Wi-Fi observer for `status wifi`and the daemons (observation`snapshot::wifi::observe`, lenient for the daemons); one workload lease (`commands::workload`) instead of five; `time-set` shares `time`'s status and RTC policy; the codec inventory refuses itself (Python's AttributeError text gone); the split modules import explicitly (no `use super::*` outside tests); stale Python references fixed in the living docs; one USB state, idle counters and sleep-diagnostics parts for the power journal and the suspend group (`power::journal::{usb, counters, state}`). Every step byte-identical against 171 (`tools/development/platform-raw-goldens.py`). Measured and skipped: sorting `power.json` while printing (≈3 µs per write on the PC, ~0.1–0.2 s CPU per hour on the player) and the second `versions.json` read per status (tens of µs) — not worth the code. Known: `update_tests::space_cleanup_stale_package_and_cancel_free_the_data_volume` failed once under a full parallel run (passes alone and in 8 later full runs; not in the release gate).

Duplication pass and idle gains after 172 (2026-10-29, test build 173): one `y2p_core::paths` (name, parent_name, realpath), `y2p_core::digest` (hex, sha256_hex), `clock::wall`, battery `interpolate_int`, update `journal_state`, `time::record`, `sys::openat`, `json::python_error`, suspend `E::private_directory`/`E::atomic_json` — every step byte-identical against 171. Left as they are, on purpose: `u16/u32_at` (different readers), reports' `update_state` (own error), suspend's `pyjson` vs `y2p_core::pyjson::Py` (parser vs value). Tests: the flaky update tests had two causes (a forked child holding `.stage.lock`: `lock::try_fd` got the test-build retry; the wake tests' process-wide SIGTERM during stage: `testing::process_signals`). Logic: the Wi-Fi look and ssh-daemon's usb0 address start no process on the player (`connectivity::direct`: wpa_supplicant control socket STATUS/SIGNAL_POLL, rtnetlink addresses and default route; below a fixture root the same fixture commands); power.json meant to be rewritten on change and at least every 2 s — no effect on 173 (10 writes in 10 s: the raw ADC voltage in the record changes every sample; see the next pass, P1); the service daemon's minute `S43y2-time start` only when `ntp.pid` names no live process; `status --reborn` reads Reborn's metrics from its control socket (Reborn's control thread answers them); Reborn dark and quiet: a full main-loop pass on an event or a due timer, at most every 5 s, watchdog every 5 s, observation 10 s, snapshot 30 s. Left on purpose:`space --cleanup` stays its own process (statvfs of the SD card can block in D state; that must not stop Wi-Fi), ssh.json keeps its 5-s renewal (`status` refuses one 10 s old).

Next pass — review of 2026-10-30 — DONE in test builds 174/175 except where marked left: P1, P2 and P8 done; P3 done for netlink, pidfd, kill/alive, new_session, dir_names, *at, unix sockets, BorrowedFd in transfer (left: the five poll loops, which round differently on purpose; the bench scratch layer); P4 done as per-target probes and the space policy in process (left: merging the three observers, byte change); P5 done for the USB tick's media.lock (left: synchronous health-ack until settled, a Job type for the child slots); P6 done for the usb0 address and one snapshot in diagnostics export (left: the cats, blkid in status, report children); P7 done for health's CheckState (left: the typed records and state enums, see "What still follows Python"); P9 done for iw's readback (left: rare wpa_cli/ip/date/rebornctl starts). Original findings:

What still follows Python (2026-10-30 count, non-test code): ~1,650 `Value` mentions, ~910 `json!`, ~500 `.get("field")` against ~70 typed Serialize records; worst observation (539 Value, 300 json!, 0 typed), then service and suspend; reports carries a Python value type (`Py`, 544 uses) for byte-identical bundles. Owner discussion: gains are correctness and maintainability, not speed; recommended selectively — type the records written and read across components (ssh.json, network.json, power.json readers, media-mount.json, the update journal, the status sections Reborn reads) and convert a group when it is next changed.

Original next-pass findings (2026-10-30, four read-only reviewers, spot-checked). Ranked by gain per risk; "byte" = needs the raw byte comparison, "owner" = needs an owner decision.
  - P1 power daemon sample (S, none): of the 9 BAT0 files read every second, `capacity`, `current_now`, `temp`,

`charge_counter` do not exist (checked on 173); `charging_state` (≈1.2 KB under the charger mutex + regex) is used only while Charging; `voltage_ocv` only in the first 120 s. Remember absence on the real root only. Then the power.json change test on the typed record, serialised once; leaving raw voltage out of the test halves the writes (owner: suspend admission and Reborn read the voltage, both accept ≤ 2 s old).
  - P2 errors (M, none): one `OsError` with `From<io::Error>`/`.at(path)` and `From` for the 7 error types (133

`py::os_error` calls, ~150 hand-written map_err closures, 5 copies of the no-path helper).
  - P3 safe syscall wrappers (M–L, none): `y2p_core::sys::{SignalPipe, poll, netlink_route, unix_connect, pidfd,

Dir(OwnedFd), kill/alive, detached spawn}`: ~130 of 185 unsafe blocks into ~15 audited wrappers; the signal self-pipe is copied verbatim (connectivity/daemon/wait.rs, service/daemon/signals.rs, ssh/wake.rs), five poll loops, five `*at` layers, six `pre_exec(setsid)`. Fixes a real leak: reports/maintenance/purge.rs forgets the dup'd fd when `fdopendir` fails and never checks errno after `readdir`.
  - P4 one volume probe (M, byte for calls lists):`y2p_core::volume`, storage/observe.rs and snapshot/storage.rs are

three volume observers; every question probes all four volumes (blkid + statvfs, SD card included), also `space --cleanup`, which needs only /data. One per-target probe and one UUID/geometry table (5 copies); then `space --cleanup` could run in process (owner: the D-state reason goes away once the SD card is not touched).
  - P5 service loop never blocks (M, owner/safety): the USB tick waits up to 5 s for `media.lock` and 10 s for a

remount, and statvfs/blkid's the SD card in the daemon (views.rs); maintenance commands run synchronously (health-ack 8 s). Try-lock and polled children. One `Job` type for the 5 hand-rolled child slots in jobs.rs.
  - P6 status cost (M–L, byte): a snapshot starts up to 8 processes (`cat` timer_list and wakeup_count, up to 4

`blkid -p`, `ip … usb0`, `y2-bt-observe`); `status <section>` builds all sections; export-diagnostics and the error report build the snapshot 2–3 times (the report runs `y2-platform status/health` and `rebornctl metrics` as children). Measure `y2-bt-observe`, `wakeup_count` and `blkid` on the player first.
  - P7 enums and typed records (M, byte): volume/space/update/LowBattery/shutdown/battery-source states as enums with

the same Serialize text; `y2p_contract::CheckState` exists but health builds "OK"/"DEGRADED" by hand; typed previous-boot-evidence, report.json index, USB views, download.json, the Y2Media claim (4 copies with different equality rules).
  - P8 duplicates (S each): low-battery policy re-implemented in suspend/admission.rs (safety logic, parity test);

power and suspend journal rows; reports' SD write-window copy (use `storage::media::write_window`); UTC ISO formatting ×4; `/proc/locks` holders ×3; `/proc/interrupts` ×3; strerror ×3; process_time ×2; bounded journal append ×2 (its error text still says power_journal); SHA-256 hex leftovers; 46 `OnceLock<Regex>` → one `regex!`; dead `power_text::{key_values, trie_address, python_hex}`; boot id re-read per pass (16 hand-written "this boot" checks).
  - P9 remaining spawns (M, device test):`iw` power save every 30 s while connected → nl80211; wpa_cli in scan

evidence/recovery/global commands → control socket (`direct::wpa_cli` must upper-case only the verb); `ip` flush/ addr/route on DHCP events → rtnetlink; `busybox date -s` → clock_settime; `rebornctl status` in health-ack → socket. Must stay external: curl, fsck/mkfs/resize2fs, y2-update-core, init scripts, dropbear, umtprd, every SD mount.
  - Checked and wrong in a review: Reborn does not call `status wifi` periodically (`NetworkCheck` is a user action; 25 is

its timeout). Idle process starts on 173 after start-up are ≈10/min, mostly kernel workers.

Owner decisions (2026-10-29, §7): replace the argparse emulation with a small declarative parser (exact option names and `--opt=value`, errors exit 2, help says y2-platform); every fake-traceback crash path becomes a refusal record (exit 1, JSON `{"state": "Failed", "failure": …}`); keep the exact JSON output format (json.dumps spacing, key order, Python float repr) — only the internal types are unified; a DHCP renew of the same lease changes nothing (no flush and re-add).

Owner (2026-10-29): put the Rust-only build on the player, review what works and what not, then "another pass regarding refactoring / code quality" because the code is "more like ported python and not really well written / optimised rust". This plan is written for a session that picks this up cold.

## 0. Read first
  - [PLATFORM-RUST-PORT-HANDOFF.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-PORT-HANDOFF.md): layout, build/test/install commands, rules

(git identity, no push or publish without the owner, OTA-only installs).
  - [platform/CONTRACT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fplatform%2FCONTRACT.md): who calls what (Reborn, scripts, the platform itself), the

fixed defects, the golden suite.
  - The top entry of [NEXT-SESSION-HANDOFF.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md) and the device results of the newest test

build in [roadmap-gap-audit.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).
  - AGENTS.md: this is an architecture change of the platform; repeat the roadmap/gap audit before starting and

before a build that carries the result.

## 1. Where the code stands (2026-10-29, main after the Rust-only merge)
  - `platform/`: Cargo workspace, Rust 1.99.0, 37 locked crates (vendored, offline). Crates: `y2p-core` (shared

helpers), `y2p-contract` (schemas shared with Reborn, a stamped copy lives in Y2Reborn), `y2-platform` (the one binary, 3.7 MB on the ARM target, multicall for y2-status, y2-health, y2-suspend-record, y2-power-audit, /sbin/poweroff, /sbin/reboot).
  - ≈51 000 lines of non-test Rust, ≈17 800 lines of test Rust, 608 Rust tests (unit + integration), plus the

golden command suite (tests/platform_goldens, run by tests/test_platform_differential.py against the Rust binary) and recordings (`crates/*/tests/recorded`, made while the Python platform still agreed).
  - The Python platform (`tools/platform`) is deleted; the Rust code was ported 1:1 from it (owner decision

2026-10-28: port first, fix after). The port was proven equal on ≈400 command cases and ≈5 700 argument lists.
  - Largest files: service/update.rs 1775, observation/snapshot.rs 1748, storage/media.rs 1347,

storage/internal.rs 1254, argparse.rs 1242, reports/maintenance.rs 1212, observation/bench.rs 1167, suspend/audit.rs 1162, connectivity/wifi.rs 1134, reports/fields.rs 1057, power/battery.rs 1027.

Device numbers to beat or keep (build 169): 4 daemons 15.2 MB RSS / 4.6 MB PSS, 19.6 s CPU per hour awake idle (power 9.1, service 8.1, ssh 2.4, connectivity 0.2), `status --reborn --pss` 0.48 s (mostly Reborn's own `rebornctl metrics --json`), restart trail 0.46 s, boot to application_ready 36.8 s.

## 2. What makes it "ported Python" (the debt, with locations)

Counts are rough (grep over non-test files, 2026-10-29).

### 2.1 Emulation of Python itself (≈3 200 lines)

Written so the output stayed byte-identical to Python's, including where nobody depends on it:
  - `y2p-core/src/py.rs` (int()/float() parsing, truthiness, `exact_int`, uuid4, Python's `round`), `os_text.rs`

(os.fsdecode surrogates for non-UTF-8 argv/env), `PyRandom` in observation_support.rs (CPython's Mersenne Twister, for the same random bytes as Python).
  - `y2-platform/src/argparse.rs` + `argparse/python.rs` + `argparse/unicode.rs` + `argparse.json`: a reimplementation

of CPython 3.15 argparse (abbreviations, ambiguity, "maybe you meant", usage text naming `main.py`).
  - `commands/reports/pyjson.rs`, `pyops.rs`, `pyre.rs` (Python json/str/re semantics for the scrubber),

`commands/suspend/pyjson.rs`, `commands/service/python.rs` (realpath, `str()` of JSON, `json.loads(strict=False)`).
  - `Failure::Crash` / `Raise::Crash` (≈60 sites): where Python would have died with a traceback, Rust prints a fake

traceback and exits 1 after the same file changes. Each is a place where the real answer should be a proper refusal record.
  - ≈350 comments that explain behaviour as "as Python did" instead of saying why.

### 2.2 Several implementations of the same thing
  - Five JSON value types: `serde_json::Value`, `y2p_core::json::Ordered` (key order kept), `power_json::{Json,

Object}`,`connectivity::wifi::Json`,`reports::pyjson::Py`(+`reports_sqlite::Value`). Each group's agent made its own.
  - mountinfo parsers / Mount types: boot.rs, observation/snapshot.rs, devices/storage.rs, reports/media.rs,

storage/sys.rs, service/python.rs, connectivity_journal.rs; `mounts()` again in storage/media.rs and storage/internal.rs.
  - boot_id() in 9 modules (some return `Value`, some `Option<String>`).
  - atomic_json in y2p-core/record.rs, reply.rs, storage/sys.rs (`atomic_json_mode`), suspend/receipt.rs.
  - data volume (verified /data) in service/storage.rs, reports/volume.rs, devices/transfer.rs.
  - Locks: `y2p_core::lock`, reply.rs `lock`, storage/sys.rs `try_lock`/`lock_within`, and raw `libc::flock` in

maintenance.rs, transfer.rs, suspend/helper.rs, plus `File::try_lock` in update.rs and suspend.

### 2.3 Untyped records

Records are `Map<String, Value>` navigated with `get(..).and_then(..)` chains and Python truthiness, not structs. y2p-contract has the schema names but few types. Typed `serde` structs for the records (power.json, media-mount.json, sd-write.json, download.json and the update journal, boot.json, network/dhcp/dns/wifi records, suspend receipts, report state) would remove most `get`/`truthy` code and make field typos compile errors.

### 2.4 Structure, errors, idioms
  - Very long functions mirroring the Python ones (update stage/apply, media lifecycle, internal setup, snapshot).
  - `unwrap()` ≈330 and `expect(` ≈190 outside `_tests.rs` files (many in in-file test modules; audit the rest:

a panic aborts, `panic = "abort"`), `.clone()` ≈430, `unsafe` ≈230 (libc calls: flock, statvfs64, ioctl, signals; wrap each family once in y2p-core with a safe API).
  - Test seams: ≈75 files with `#[cfg(test)]` hooks (per-thread replacements for clocks, `command`, PM stores,

`launch`, space, tokens, network waits, renames) that the Python tests used to patch. Replace with explicit injected interfaces (a `Clock`, a command `Runner`, a `System` for sysfs/PM writes) passed in a context.
  - Configuration as environment for tests (`Y2_ROOT`, `Y2_FIXTURE_COMMANDS`, `Y2_FIXTURE_CALLS`,

`Y2_DAEMON_TICKS`, `Y2_FIXTURE_TOKEN`, `Y2_ARGPARSE_ECHO`) read deep inside the code: gather in one context.

### 2.5 Efficiency (measure first; only where the player gains)
  - The daemons poll: power-daemon samples BAT0 every second, service-daemon ticks every 3 s (dark: longer),

connectivity waits on fds. Candidates: uevent/netlink for power_supply and block changes, timerfd deadlines instead of fixed ticks, fewer sysfs reads per tick. Target: idle CPU well below 19.6 s/h, and longer CPU-off stretches awake (deep idle is blocked by other things too: see the awake-idle memory/notes).
  - `status --reborn --pss` spends its time in `rebornctl metrics --json` (Reborn side).
  - Binary size 3.7 MB (opt-level "s", LTO): check what the regex/flate2/tar/argparse tables cost.

### 2.6 Leftovers of the Python era (small, do first)
  - Fixture argv for the DNS lookup still spells the Python one-liner (`/usr/bin/python3 -I -c …getaddrinfo…`,

connectivity/wifi.rs and its goldens/recordings); on the player the lookup is Rust `getaddrinfo` already.
  - `Y2_PLATFORM_PYTHON` in tests/dispatcher.rs; usage texts say `main.py` (part of the CLI contract: help text

only, no caller parses it — owner decision whether to rename to y2-platform).
  - Development scripts that run Python on the player with the old platform modules can no longer work (no

Python there since build 169): tools/development/power-session/{deepsleep-clean-session.py, deepsleep-idle-followup.py, deepsleep-product-session.py, power-press.sh, power-screen.py}, qualify-cpu-fix02.py / qualify-cpu-fix03.py (`charger()`), tools/usb/qualify.py (remote status script), observe-platform-v1.py (pins a deleted file). Retire them or give the platform the commands they need.
  - Docs that still name deleted tests or tools/platform paths: docs/release/Y2-COMMUNITY-BETA-FEATURE-AUDIT.md,

Y2-COMMUNITY-BETA-FEATURES.json, docs/planning/CLAUDE-DEEP-SUSPEND-PROMPT.md, tools/reports/worker comment.

## 3. What must not change (the contract)

Before changing any output, check CONTRACT.md "Callers". Fixed points:
  - Reborn (`reborn-platform/src/client.rs`, `storage.rs`, `power.rs`) parses stdout JSON and matches

`failure`/`reason` strings by hand (F52 was such a mismatch); exit 0 vs non-zero decides success except for `health` (exit 1 is evidence). y2p-contract schema names are shared and stamped.
  - Shell scripts grep compact JSON (`S43y2-time`: `"state":"Online"` in network.json;

sftp-server: `"state": ?"Ready"`): compact separators of those records are contract.
  - initramfs`/sbin/y2-platform-start` and the marker `y2-platform-v1`.
  - Persistent file formats on /data (journals, receipts, boot.json, update journal, report state, power journal):

readers are Reborn, the error-report scrubber/Worker, tools/reports and the UserReports analyses. A format change needs a migration or a version.
  - The multicall names and the subcommand/argument forms callers use (CONTRACT.md tables).

Free to change (nobody depends on it, verify per case): JSON key order and spacing on stdout where only Reborn reads it as JSON, Python float repr where no reader compares text, argparse corner cases (abbreviations, "maybe you meant", exact error wording) beyond exit code 2, fake tracebacks (become refusal records), PyRandom streams. Each such change shows up as a golden diff: review and re-record it in the same commit.

## 4. Safety net and how to use it
  - `cd platform && cargo test --offline --locked && cargo clippy --offline --locked --all-targets` and

`cargo check --offline --locked --target armv7-unknown-linux-gnueabihf` (the player is 32-bit: time_t/c_long, 64-bit file calls; use `y2p_core::wide()`).
  - Golden command suite: `tools/development/host-tests.sh tests.test_platform_differential …` (see the harness

docstring for the re-record command). A pure refactor changes no golden and no recording.
  - Recordings: `Y2_RECORD_GOLDENS=1 cargo test …` re-records `crates/*/tests/recorded`; only for an intended change,

with the diff reviewed.
  - Full host suite before a build: `tools/development/host-tests.sh`.
  - Device: anything touching power, sleep, charging, storage, update or radios needs a test build and the owner's

check (OTA install only; ask before anything that powers the player off or needs button presses).

## 5. Phases (each its own commits; never behaviour and structure in one commit)
  - Leftovers (§2.6) and an `unwrap/expect/unsafe` audit list (no changes yet).
  - One core in y2p-core: `Mount`/mountinfo, boot_id, atomic records (with mode and durability options), the

lock API (exclusive, try, within-deadline, shared), the verified data volume, safe wrappers for the libc families. Replace the copies group by group; goldens unchanged.
  - One JSON model: serde_json with `preserve_order` (vendor indexmap) or `Ordered` everywhere; delete

power_json::Json, wifi::Json, pyjson::Py where the order/float behaviour is not contract.
  - Typed records in y2p-contract (shared with Reborn where Reborn reads them; re-stamp with

`release.py sync-contract`, commit Reborn with the identity env vars).
  - Context and injection: one `Context { root, clock, runner, system }` passed down; remove the `#[cfg(test)]`

seams and env-var plumbing; tests construct a context.
  - Python emulation out where §3 allows: argparse → a small declarative parser keeping exit code 2 and the

argument forms (owner decides on help text); Crash paths → refusal records (each a behaviour change: list them, owner reviews the list); py.rs/os_text/pyre/pyops reduced to what the contract needs.
  - Split the long modules along their responsibilities (update: source/download, staging, journal, apply;

media: lifecycle, check, window, repair, format; snapshot: per section).
  - Efficiency (§2.5): measure on the player (plan §7 method in PLATFORM-RUST-PORT-PLAN.md: idle sampler 600 s,

per-daemon CPU/RSS), then event-driven waits; a test build and an overnight drain to prove no regression.
  - Docs: CONTRACT.md as the Rust contract (drop "as Python" wording), comments say why, not "as Python did".

Each phase: entry note in roadmap-gap-audit.md when it reaches a test build; numbers before/after on the player.

## 6. Test quality follow-ups (from the 2026-10-29 test port)

The Python unit tests were ported by eight agents; where Rust had no hook for what Python patched they adapted:
  - Real clocks instead of fake ones (power coordinator grace, report retry times, supplicant timeout duration,

update network wait 0.05 s under test); some waits are real (Wi-Fi removal 2–3 s, wakeup_count 2 s, collect 3 s).
  - Source-text pins instead of behaviour (shutdown order "panel dark before Reborn stops", transfer check order,

reborn-last init order, service loop gating, media inventory identity, failure_output kwarg).
  - Dropped sub-cases: cpu-idle `budget_readback` (-1 write ignored), PM store returning None, internal

`music_root` assertions (function never ported), `configure(sbc_abr='on')` (not expressible in Rust types).
  - Faults made with files instead of patches (0444 files, directories in place of files, symlinks to /dev/null);

one rollback test runs only as non-root.
  - `#[cfg(test)]` seams in suspend/helper.rs, service/update.rs + mod.rs, reports/maintenance.rs,

storage/media.rs, internal.rs, observation/bench.rs, service/process.rs (`launching`), and a 0.2 s busy-lock retry in test builds (y2p_core::lock::settle, storage/sys.rs): a forked child shares a test's lock until exec.

Phase 5 (injection) should turn most of these back into direct tests.

## 7. Owner decisions to ask for (when the phase comes)
  - Rename `main.py` in usage/help texts to `y2-platform`? (No caller parses help.)
  - Replace the argparse emulation (abbreviations like `--hol` for `--holder` would stop working; no caller uses

them)?
  - Turn each fake-traceback crash path into a refusal record (list per command)?
  - JSON spacing/order on stdout: keep `json.dumps` style or switch to compact everywhere (Reborn parses JSON;

scripts grep only the records named in §3)?
  - DHCP renew flushes and re-adds the same address (brief outage, Python behaviour kept): change to a no-op renew?

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
