---
title: "Platform Rust: from Python behaviour to Rust behaviour — plan (2026-10-30) - Innioasis Updater"
description: "Platform Rust: from Python behaviour to Rust behaviour — plan 2026-10-30 Owner 2026-10-30:"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-platform-rust-idiomatic-plan.html"
---

# Platform Rust: from Python behaviour to Rust behaviour — plan (2026-10-30) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform Rust: from Python behaviour to Rust behaviour — plan (2026-10-30)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform Rust: from Python behaviour to Rust behaviour — plan (2026-10-30)

Owner (2026-10-30): "stuff has not to be byte identical anymore, but of course it should still work, make a plan so that all code which is not extremely critical can be moved to rust logic. dont spawn other agents, work alone on this."

One agent, alone, in the order below. Read this file, then §2 and §3 of [PLATFORM-RUST-NEXT-AGENT-HANDOFF.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-NEXT-AGENT-HANDOFF.md) (rules and method that still apply where this plan does not replace them).

## 0. Where it starts (2026-10-30, after test build 179)

No Python runs on the player. `platform/` is ~51,300 non-test Rust lines. Every output was kept byte-identical to the Python platform (json.dumps spacing and key order, Python float repr, argparse and Python error texts, Python's `==` and truthiness on records). That rule is what keeps the Python logic in place:````````````````````````````````````````````

| measure (non-test code) | count |
| --- | --- |
| serde_json::Value mentions | 1,601 |
| json! literals | 793 |
| .get("field") lookups | 479 |
| Python emulation calls (py_eq, truthy, PyValue, python_int, Py::, pyops, py::) | 892 (453 in reports) |
| typed Serialize / Deserialize structs | 119 / 21 |
| compatibility modules | y2p_core::pyjson 694 lines (the Py value type and json.dumps), y2p_core::py 383, y2p_core::lenient 128, y2p_core::os_text 150, cli.rs 863 + argparse/ 522 (argparse emulation), reports/pyops.rs 181 |

Per group: reports 7,900 lines (Py 453), observation 6,800 (Value 510, json! 230), service 6,200 (197/90), suspend 5,000 (199/74), storage 4,400 (129/96), connectivity 4,000 (106/136, of which `scenarios.rs` 73 json! are test fixtures), power 3,800 (113/2), devices 2,100 (49/29).

Files with the most untyped JSON and Python semantics (Value + json! + get + py): observation/bluetooth.rs 156, observation/snapshot/wifi.rs 106, observation/system.rs 106, reports/upload.rs 101, connectivity/scenarios.rs 92, suspend/receipt.rs 86, suspend/receipt/transition.rs 83, reports/build/facts.rs 77, observation/evidence/mod.rs 74, reports/checks.rs 61, reports/maintenance/execute.rs 60, observation/snapshot/storage.rs 55, storage/observe.rs 53, sleep.rs 52, service/update/staging.rs 51, suspend/admission.rs 49, service/radiofw/copy.rs 47, reports/state.rs 46, service/update/health.rs 45.

## 1. The new rules

### What must keep working (the contract that stays)
  - Reborn ↔ platform. Reborn parses every answer with serde, so spacing and key order do not matter to it; what

matters is kept exactly: - the commands and options Reborn calls (`crates/reborn-platform/src/client.rs``call`): `status --reborn`, `status wifi`, `health`, `capabilities`, `update check|apply|cancel|rollback`, `report status|enable|disable|new-id|send|save`,`media repair`,`internal-media setup …`,`export-state --include-database`,`export-diagnostics`,`codec-settings --sbc-quality|--aac-quality|…`,`time-set `, `sleep request`; - their exit codes, field names, value types (a number stays a number) and the state/reason texts (Reborn maps reasons by text, e.g. `charger` → `ChargerActive`); - the files Reborn reads: /run/y2/{usb-transfer, media-mount, network, power, time-status, internal-media, coexistence, codec-runtime, application-ready, update-progress, report-progress, shutdown, bt-codec-uncertain}.json, update-check-progress, the power socket, the lock files, bt-intent/bt-control.ini, /data/bluetooth/{codec-history, codec-policy}.json, /data/network/enabled, /data/bluetooth/enabled, /data/system/platform/maintenance-pending; - the shared `y2p-contract` crate (schemas, boot stages): a change is made in Y2Linux, synced with `release.py sync-contract`, and committed in Y2Reborn in the same step.
  - Shell consumers on the player. Exit codes and the files they test stay. Three read JSON as text:

`S43y2-time` (`grep -q '"state":"Online"' /run/y2/network.json`: compact form only, fix in P0), `usr/libexec/sftp-server` (`'"state": ?"Ready"'`: tolerant already), and the initramfs (`init`, `recovery.sh`) reading records of the C update core (`buildroot/package/y2-update/core.c`), which this plan does not touch. `connectivity` reads `codec-runtime --record`'s stdout as arguments: that output stays as it is.
  - Records on /data survive an update and a rollback. An older build must read what a newer one wrote: field

names and value types stay; new fields may be added; nothing is renamed, removed or retyped without a migration that the older build tolerates. Formatting (spacing, key order, float spelling) is free. The records: /data/system/platform/{boot, maintenance-state, reset-plan, power-features, power-policy, rtc-policy, battery-profile, battery-ui, panel, previous-boot-evidence, product-sleep-guard, reports, sd-admissions, sd-repair-last, suspend-last, time-last, usb-mode}.json, the journals (power-journal, sleep-diagnostics, wifi-journal .jsonl and their .previous), /data/system/internal-media-setup.json, /data/network/power-save.json, /data/updates/{channel, download, last-check, restart}.json (state.json is the C core's), /data/settings.json.
  - The error report bundle sent to reports.schulzcode.dev (the receiver is not in this repository): its

members, their names and fields stay; their JSON formatting may change only if the receiver parses JSON (check the receiver before changing it; until then, reports keeps its writer).
  - Behaviour towards the kernel and hardware: every sysfs/procfs write, its order and timing, every

refusal that protects the player (battery, charger, D-state SD card, sleep admission). Nothing in this plan changes what the platform does to the hardware.

### What is dropped
  - Byte identity of stdout, stderr and written files: spacing, key order (struct order or sorted, whichever is

simpler), float spelling (serde/ryu: `1e-5`, not `1e-05`), trailing newlines where nothing depends on them.
  - Python's error wording where no consumer reads it: `invalid literal for int() with base 10: '…'`, `TypeError` /

`ValueError` class names, argparse usage and error texts. Refusals keep a stable reason code; the free text next to it may change.
  - Python semantics on the platform's own records: `1 == 1.0 == True`, truthiness of `""`/`0`/`[]`, `int()` of

`"1_000"` or Unicode digits. A record field is read into its Rust type; a value of another type is a broken record and is handled once, the same way for the whole record (absent → default, or the record is refused), documented on the struct.
  - Tolerances that existed only for old Python-era records that no supported build writes any more (e.g.

network.json `status_query_failures` as a bool, decision 6 of 2026-10-30), after checking that no record on a player in the field can still hold them (a rollback target counts).

### What stays as it is (extremely critical; outside this plan except mechanical changes)

These keep their logic. Allowed in them: the shared writer's new formatting (their records are parsed as JSON by everything that reads them; checked per record), typed reads that give the identical decision for every value an in-field build can write, and nothing else. Each such change is its own commit with its own device test.
  - Update and recovery: `service/update/{apply, staging, health}.rs` decisions, the health-ack/rollback path,

everything that talks to `y2-update-core`, recovery, the initramfs.
  - Sleep entry and wake: `suspend/helper*` (kernel PM writes, wakeup_count, the backstop), `suspend/admission.rs`,

`suspend/receipt/transition.rs` (the receipt's state machine), `sleep.rs` product rules.
  - Power safety: `power/policy.rs` (low battery, shutdown thresholds), `power/coordinator*` (the shutdown

intent), the charger and battery reads that feed them.
  - Storage that writes: SD repair/format/fsck, mount claims and SD admission (`storage/media/*`,

`storage/internal/setup.rs`), reset execute (`reports/maintenance/execute.rs`).
  - Boot: `boot.rs` stage journal, `cpu_idle.rs` policy, `time` floor and RTC writes.

Everything else is converted: observation (status, health, evidence, diagnostics, bench), connectivity (except the supervisor's wpa_supplicant lifecycle, which only gets typing), devices (ssh, transfer, timekeeping reads), the read side of storage (observe, records, inventory), service (daemon loop, USB service, radio firmware scan, jobs), power's journal and daemon record, suspend's journal rows and audit, reports (status, checks scheduling, build, upload, scrub), the argument layer, the shared core.

## 2. Method (replaces handoff §3 for converted code)
  - Two gates.`platform-gate.sh` keeps fmt, clippy, the armv7 check and cargo test. The byte comparison

(`platform-raw-goldens.py`) stays only for the pinned outputs (§1: `codec-runtime --record`, S43's network.json test until P0 fixes it, the report bundle members until the receiver is checked, the critical code's records). For converted code the golden suite (`tests/platform_golden.py`: parsed JSON, sorted, semantic) is the check.
  - Deliberate re-recording. A step that changes outputs re-records exactly its goldens

(`Y2_RECORD_GOLDENS=1 …`, handoff §3.3) and the commit message lists what changed in meaning (not only formatting): a renamed free text, a dropped tolerance, a refused odd value. A small script (`tools/development/golden-diff.py`, P0) prints a re-record's semantic differences so the review is of meaning, not of spacing.
  - Contract checks that did not exist before (P0):
    - Reborn reads it: a test in Y2Reborn that feeds every golden output of a command Reborn calls (and every

golden of a file Reborn reads) through `reborn-platform`'s parsers and fails on a parse error or a changed typed result; run after each re-record (goldens are copied into Y2Reborn's test data by a script, not by hand).
    - Rollback reads it: `tools/development/rollback-read.sh`: the previous test build's `y2-platform`

(extracted from its rootfs in `out/release-N/`) runs `status`, `health`, `boot-evidence` and the daemons' one-tick modes below a fixture root holding the /data records the new build wrote; any refusal or crash fails.

  - One concern per commit (formatting, typing, semantics are separate commits). Host suite before each build.
  - Device check per test build: `platform-device-check.sh`, plus the commands Reborn calls run once on the

player and parsed by Reborn's own parsers (`rebornctl` has no such mode; use the Y2Reborn test binary built for armv7 or check Reborn's UI and log for platform errors after an hour), and an idle measurement after ≥ 30 min.

## 3. The work, in order

Sizes: S < 1 h, M ≈ half a day, L ≈ a day. Each phase ends with a test build and its device check.

### P0. Ground (S–M) — done 2026-10-30

Results: S43y2-time accepts both spellings (ebd849d1); `tools/development/golden-diff.py`; Reborn's contract test (Y2Reborn 4bed622, `tools/development/reborn-contract.py`; 491 cases, 596 typed results recorded from the Python-identical outputs); `rollback-read` became `tools/development/record-compat.py` (every /data record in the goldens, 83 kinds, keeps its fields and types against the last release commit: what an older build's readers need, checked without running an old binary); `platform-gate.sh` with no argument is the semantic gate (goldens + record-compat + Reborn contract), with a baseline it is the old byte gate (c7be0361). Plain-text outputs (e.g. `codec-runtime --record`) are compared exactly by the golden suite already, so nothing needs a byte pin. P0.4: the receiver (`tools/reports/worker`) checks method, size, gzip magic, schema and IDs and stores the tar.gz without parsing its members: the bundle's JSON formatting is free; member names and fields stay.
  - `S43y2-time`: `grep -Eq '"state": ?"Online"'` (or drop the check: the service daemon starts S43 only while

Online and ntpd is not running — verify, then remove the grep). Then network.json is no longer pinned.
  - `golden-diff.py` (semantic diff of a re-record), the Reborn contract test, `rollback-read.sh` (§2.3).
  - `platform-gate.sh --pinned <list>`: the byte comparison limited to the pinned cases; the semantic suite for the

rest.
  - Check the report receiver: does it parse JSON members (then the bundle's formatting is free) or compare text?

Record the answer here.

### P1. One JSON writer (M) — done 2026-10-30 (d82f1426)

Compact serde_json everywhere; the SD media identity digest keeps Python's sorted spaced encoding (`json::python_dumps_sorted`: admitted cards keep their id); reset execute hashes `record::encode`'s bytes. Shell matches made spacing-tolerant (reborn-supervise, platform-device-check.sh, S43y2-time).

`reply::atomic_json` / `atomic_json_mode`, `Reply::sorted` and every `pyjson::dumps(…, Style::…)` / `json::PythonFormatter` / `Separators::Spaced` outside the pinned outputs write with `serde_json` (compact for files, one form for stdout: `to_writer_pretty` or compact, chosen once; keys in struct order, maps sorted by `BTreeMap` where order matters to nobody). Python float repr goes (`y2p_core::json::float_repr` only for pinned outputs). Verify: semantic goldens unchanged (formatting only), Reborn contract test, rollback-read. Byte goldens move for every converted command: re-recorded once, reviewed with `golden-diff.py` (expected: no semantic difference).

### P2. The argument layer (L) — done 2026-10-30 (5bb70fe9)

cli.rs already was a Rust parser (exact names, ASCII integers); what remained was three groups parsing its canonical output again: replaced by `cli::given` (the command's own table). Routing on the canonical argv stays (idiomatic pattern matching; the command lines Reborn and the scripts use are unchanged).

`cli.rs` + `argparse/` emulate Python's argparse (abbreviations, `--opt=value`, its usage and error texts) and hand the groups a canonical `Vec<String>`, which observation, reports and devices parse a second time (`observation/mod.rs``parse`/`Spec`, `reports/mod.rs``options`, `devices/mod.rs``options`). Replace with one declarative table (`cli.rs` already holds every command's options) whose parser returns typed values per command (`enum Invocation { Status(StatusArgs), … }`), and route on that instead of string patterns (`commands/mod.rs``route` and the eight group `route`s). Keep: every command and option name Reborn and the scripts use, exit code 2 for a usage error, `--help` text in a plain form. Drop: abbreviations (check no caller abbreviates: grep the overlay, Reborn and tools), argparse's exact texts. No new crate (only serde/regex are vendored): the parser is ~300 lines. Verify: argument goldens re-recorded (texts change, exit codes do not), every Reborn and script invocation listed in §1 run against the new binary on the host.

### P3. Python semantics out of the platform's own records (M per group) — done for non-critical code

Commits 27c07cb6 … 551ca5c8: lenient helpers (number/integer/flag) Rust-typed; network.json's count a u64; Wi-Fi look, Bluetooth, storage read side, Y2Media claim, radio firmware, USB service, power/suspend journals, power socket refusals; `py::{eq_int, number}` strict, `root::parse_int` (i64::from_str) for kernel text. Critical code keeps Python's number rules explicitly (`py::{python_eq_int, python_number}`: power policy, update health/journal, sleep deadlines, SD write windows, boot journal) and its truth tests (sleep receipt product, power.json battery for admission). Fixtures that held Python-only values (1.0 for 1, true for 1) now hold what their writers write; the golden recorder became type-strict (ca1b84a6).

Group by group, outside §1's critical list: each record read with `.get("x")` + `py_eq`/`truthy`/`is_true`/ `python_int` becomes a `#[derive(Deserialize)]` struct with `#[serde(default)]` fields of the real types (a `lenient` field type only where a record written by an in-field build can really hold two forms). `get_eq(…)` and `py_eq` on own records go; `y2p_core::lenient::{number, integer, truthy, is_true}` shrink to what parsing sysfs and foreign files needs. Integer parsing of sysfs/procfs text becomes `trim().parse()` (handoff item H's note: pid files checked). Order: connectivity (record, wifi monitor, radio policy), devices (ssh, transfer, timekeeping), storage read side (observe, records, inventory, sys), service (daemon loop, usb, radiofw scan/copy, jobs), power (daemon record, journal), suspend (journal rows, audit, sleep-diagnostics; not admission/helper/transition), observation (evidence, collect, health, readiness, bench). Verify per group: goldens re-recorded where an odd value is now refused or defaulted (listed in the commit), Reborn contract test, rollback-read, device check.

### P4. The remaining untyped JSON (M per group) — partly done

Done: the Bluetooth section (Section/Adapter/Device/Pcm/Transport/Encoder). Left on purpose: storage/observe's volume map (read by key by the critical SD operations in storage/media.rs; its decisions are plain Rust now); connectivity/scenarios.rs was already test-only.

Built with `json!`/`insert` and read back by key → structs, per the ranking in §0:
  - observation/bluetooth.rs: y2-bt-observe's answer parsed into structs (`Observed { bluez, bluealsa, manager, … }`)

and the section a struct (today maps step by step);
  - observation/evidence/mod.rs + previous-boot-evidence.json readers; observation/snapshot/wifi.rs internals

(properties map → struct);
  - storage/observe.rs volumes (the snapshot's Volume type already exists: share it), storage/records.rs;
  - service/usb (views and transfer record are typed; the gadget/responder state), service/radiofw/copy.rs,

service/update/staging.rs reads (read side only), service/download.rs;
  - suspend journal rows (`power/journal` + `suspend/journal`: one row type, no `plain` re-sort), the audit samples;
  - connectivity/scenarios.rs moves under `#[cfg(test)]` / the test-support module (fixtures, not product code).

Verify as P3.

### P5. The status snapshot as one type (M) — done 2026-10-30 (01c484d2)

`observation::snapshot::Snapshot` is a struct (schema, record, cpu, memory, thermal, power, storage, wifi, bluetooth, system, audio, readiness, reborn_metrics); `audio` is typed, the other sections are the JSON their modules build from their own structs. readiness, health, collect, network-check and the diagnostics export read fields instead of looking sections up by key; `status <section>` reduces the serialised snapshot as before. Not done (smaller next step): the section functions returning their structs (`Power`, `Storage`, `Wifi`, …) so readiness/health read typed fields inside the sections too (`storage.volumes[].state`, `wifi.state`, `system.update`).

Plan as written:

`observation/snapshot` assembles a `Map<String, Value>` of sections that are now structs; make it `struct Snapshot { power: Power, cpu: Cpu, … }` (each section `Option` where `status <section>` builds only one), `status <section>` prints that section, readiness and health read typed fields (today ~36 lookups by key), diagnostics export serialises the struct. `utilization_percent` becomes a field set by the caller.

### P6. Reports without `Py` (L, after P0.4) — done 2026-10-30 (76675310, 585566fa)

`Py`/`pyjson` are gone from the reports group: records are `serde_json::Value` (`pyops` keeps the shape checks a record of another shape is refused with), the crash signature and the reset plan confirmation keep CPython's bytes (`python_dumps_sorted`), marker text keeps the `None`/`True` spellings (`text_of`), the scrubber finds a known value both as serde writes it inside JSON and `\u`-escaped (older records). Not done: reports.json as a typed struct (it is a `Value` with shape checks; a struct is the next step, rollback-readable field names/types).

Plan as written:

Size (2026-10-30): ~520 `Py`/`pyops`/`pyjson` uses in 17 files; maintenance/* (reset) is critical and stays; the rest (upload 95, build/facts 66, diagnostics 56, state 55, checks 43, build 34, scrub 15, media 15, secrets 14, mod 11, upload/curl 9, volume 4, scrub/files 4) ≈ 420. Start with state.rs (reports.json as a typed record, rollback readable: keep field names/types), then checks (seen markers), upload, build/facts, diagnostics. The crash-signature digest (checks.rs) must keep its encoding (stored in reports.json `seen`), as the SD media identity did in P1.

`reports` (7,900 lines) runs on `y2p_core::pyjson::Py`, a Python value type, and `pyops` (Python operators): records become structs (reports.json, the queue entries, report-progress, the bundle manifest and facts), `Py` and `pyops` go, the bundle is written with serde. The bundle's member names and fields stay (§1.4); its formatting follows P0.4's answer. `reports/maintenance/execute.rs` is critical: its plan/state records get typed reads with identical decisions, nothing more.

### P7. Clean-up (S–M) — done as far as non-critical code goes (ffd6ff52)

Done: `json::{dumps, dumps_sorted}` take only the value (3bcdd46c); `y2p_core::pyjson` deleted (694 lines; its digest proof is now a test against CPython's bytes); observation's kernel-number parsing is plain ASCII decimal (`root::parse_int`, `[0-9]` in the counter regexes: a non-ASCII digit leaves a field unread instead of refusing the snapshot); CONTRACT.md's stdout rule points at §1. What stays and why: `y2p_core::py`'s `truthy`/`is_true`/`PyValue`/`python_*` (used by the critical code: suspend, power policy/coordinator, SD operations, update, boot), `suspend/pyjson.rs` (the receipt RPC), `argparse/python.rs` (the suspend group's internal commands `__suspend-record`/`__power-audit` read their own arguments as the Python scripts did, plus `repr` for refusal texts), `json::PythonFormatter` (only behind `python_dumps_sorted`), `os_text` (path texts in records).

Delete what no longer has users: `y2p_core::pyjson` (except what a pinned output needs), most of `y2p_core::py`, `os_text`'s surrogate escapes where no path text is printed, `json::PythonFormatter`, `argparse/`. Update `platform/CONTRACT.md` (the contract is now §1 of this file) and the handoff.

### Finishing (Q1–Q5), owner decisions 2026-10-30 evening

Owner: "no more loose JSON", more breaking changes accepted. Decided: (1) critical code is converted too, last, with its own test build and the owner's hardware round (sleep, overnight drain, OTA + rollback, SD, reset); (2) /data records stay rollback-safe (structs keep field names/types, new fields allowed); (3) the status/health JSON Reborn reads may change shape, Reborn's parser and contract test change in the same commit pair.

Size at the start: ≈3,470 `Value`/`json!`/`.get("…")` in non-test code; ≈55 % own records and sections, ≈30 % critical code, ≈10–15 % real boundaries (y2-bt-observe's answer, /etc audio profiles, pcm_contract, Reborn metrics, files copied into the report bundle: these stay `Value`).
  - Q1 observation: section functions return their structs (`Cpu`, `Memory`, `Thermal`, `Power`, `Storage`,

`Wifi`, `System`, `Bluetooth`, `Readiness`); `Snapshot` holds them; readiness/health/collect read typed fields; `status <section>` serialises one field; evidence, bench typed. scenarios.rs under `#[cfg(test)]`.
  - Q2 reports: reports.json, queue entries, report-progress, facts, checks, upload as structs; `pyops` goes.
  - Q3 service/connectivity/storage read sides: update staging/health reads, radiofw copy, download, Wi-Fi

monitor, storage observe volume map and records.
  - Q4 critical: typed records with identical decisions (suspend receipt/transition/admission, sleep.rs, power

coordinator/policy, update journal/health/staging, SD write ops, internal setup, reset execute); then `y2p_core::{py, lenient}`, `suspend/pyjson.rs`, `argparse/python.rs` deleted.
  - Q5: clean-up, measure, CONTRACT.md.

Test builds after Q1+Q2, after Q3, after Q4 (hardware round).

Progress (2026-10-30 night): Q1 — every snapshot section returns its struct (92494f00, 47ca4a78, b8034e00), records are `y2p_contract::ObservationRecord` (bb523a82), health is `y2p_contract::Health` (d6296172), readiness typed (fc778448), previous-boot-evidence.json one typed record (d37b9e53), system section's reset cause / boot stages / USB (fc8bace0), one update-status and one reset-cause implementation (57f73c67), netlink answers typed (71fa7b72). Behaviour changes, all reviewed: unmounted volumes and the unavailable Bluetooth section carry every key; a broken evidence record or odd `ip` output leaves `status` readable. Left in Q1: Bluetooth internals, Wi-Fi's records (network.json signal cache, wifi-events/-power, coexistence), storage internal setup, power's policy record, bench, `status <section>` reduction.

Later the same night: Q1 also Bluetooth answer (bf6156cc), power record (a1c7d63b); Q2 reports.json (a97b74f4), report index (09032b20), triggers (34c9ac43), upload gate/answers (04d33cd8, 2db80593), diagnostics (fb733801); test build 182 Acknowledged. Q3: codec module (7a64dcc0), radio firmware (90e44555), wifi-failure record (95d097d1), the Wi-Fi look as one typed `Wifi` through status, network.json, DNS probe, recovery and the service daemon (d590c239), power-save policy/record (b69813c9). Loose JSON in product code (test-only modules excluded): ≈2,380. Left for Q3: devices transfer/time/ssh records, capabilities template, storage observe/records/sys read sides, service usb/download, coexistence record, then Q4.

Q4 (2026-10-30, after midnight). Part 1, in test build 184 (seq 11290, Acknowledged): update health-ack, time floor, update restart/channel (one power-socket client), SD records (one `MediaRecord` for media.json, the mount claim and the lifecycle; card `Identity`; `Check`; write windows), USB hand-off (usb-transfer views, one mtp-roots and one mtp-events record), Y2Media (setup note/status, resume record keeps unknown fields, marker/claim), battery profile loader (shared with the setup gate), boot journal, CPU idle policy, power policy, shutdown `Intent` (one `ProcessIdentity`). Found on the way: the USB tick and radiofw read the write-window answer's `holders` as an object (it is a list), so USB re-opened its SD window every tick and never closed it on unplug. Owner decision for part 2 (2026-10-30): a corrupted /data record on the remaining critical path fails closed with ONE refusal reason; no Python error-text parity. Part 2: Reborn's sleep answer typed and `suspend/pyjson.rs` deleted (83778bce); suspend `Receipt`/`Product`/`Moment`/`StageRow` for sleep status, the transition, record/progress, the helper and both journals (2f2a4658; an unreadable receipt refuses as `suspend_receipt_unreadable`, and the failure is still recorded in a new receipt); sleep admission (4d1903df); reset `Plan`/`FileIdentity`/`ResetRecord` with the confirmation still a hash over the plan as read, `pyops` deleted (a9c67d19); one journal row for the power daemon and the suspend stages, one sleep-diagnostics row (a683b584). `Failure::Crash` (Python's uncaught-exception emulation) is gone. Boundaries left as they are: the native update core's journal and answers (a C program's records, shown as is), Reborn's session file in a settings reset (only its settings are replaced), versions.json and power.json's battery copied into rows. Small leftovers: Python truthiness inside a few typed readers (`py::truthy`, `python_number`), `argparse/python.rs`.

Q5 (2026-10-30, after 185): the native update core's journal typed on the platform side (`CoreJournal`: the fields the platform and Reborn read; the core's install records kept as written) and one `y2p_contract::Versions` for versions.json (status, journal rows, observation records, capabilities, CPU idle, the sleep guard) (d7a909d2); CONTRACT.md "Typed records"; the plan in the documentation catalog. Tried and dropped: typing power.json's battery copy in the receipt (a reading of another shape lost fields and gained defaults; it stays a copy). Left on purpose: Python truthiness inside a few lenient readers, `argparse/python.rs` (CLI error texts), `py::os_error` texts (shown failure reasons), report bundles' copies.

Measured on 185 (2026-10-30, screen off, charging, 6 min uptime):````````

|  | Python (165) | port end (≈171) | 185 |
| --- | --- | --- | --- |
| daemons RSS / PSS | 58.4 / 35.0 MB | 15.2 / 4.6 MB | 17.3 / 5.5 MB (binary 4.2 MB) |
| daemons idle CPU | ≈92 s/h | ≈11–19.6 s/h | 12.0 s/h (power 4.4, service 5.5, ssh 1.9, connectivity 0.2) |
| Reborn idle CPU | ≈45 s/h | ≈14 s/h | 15.7 s/h (early uptime) |
| simple call (sleep status, update status) | 0.53 s | 8–17 ms | 6 / 8 ms |
| status (any section) | — | — | 330 ms: ≈170 ms is the bounded wakeup_count read, which blocks while the charger holds a wakeup event |
| application_ready | ≈44 s | 37.4 s | 37.0 s |

After Beta 9.0 (2026-10-30, owner: "do all of it, no extra testing from me for now"; not built or installed yet):
  - Reborn on the contract types (R-A–G): `y2p-contract` gained `sleep`, `update`, `power`, `network`,

`storage`, `usb`, `reports` and `radio`, moved out of the platform (the daemon writes the shared `PowerRecord`; its borrowing copy and the media hand-off's own `UsbState` are gone); Reborn's update page, battery, shutdown intent, Wi-Fi readiness, SD and Y2Media checks, USB receipt, report progress, Internal Storage setup and radio firmware read them (CONTRACT.md "Records Reborn reads in the platform's types"). Reborn's recorded contract is unchanged except for the removed `download_percent`. Left as JSON on purpose: the rest of the status snapshot and the diagnostics page (it shows whatever a field holds).
  - Reborn split without a code change:`main.rs` 8,268 → 947 lines (Runtime's methods in `runtime/`, `run` in

`main_loop.rs`, tests in `main_tests/`), `playback.rs` 3,725 → 1,565, `reborn-ui/src/lib.rs` 4,493 → 1,069; the same tests run. Still long single functions: `run` (2,086 lines) and `Playback::with_sink` (1,007), whose closures share state; shortening them is a real change, best done with a player at hand.
  - Platform leftovers:`py::truthy` is the contract's `lenient::is_truthy`; `sys::pipe` and `sys::signal_note`

(both signal handlers' errno-keeping wakeup write) and the existing `sys` wrappers replace hand-written calls; `unsafe` outside y2p-core 82 → 63.
  - Not started: the update core in Rust.`tools/update/core.c` is the signed rescue's trust boundary

(`rescue_tools.py` requires a full paired build when it changes), runs in the recovery image too, and needs Ed25519 vendored (`ed25519-dalek`, a legal-info change). A port is checkable on the host against the core's 22 tests in `tests/test_platform_update.py`, but cannot ship before a hardware round including recovery boots; owner decision pending.

After Beta 9.1 (2026-10-31, test build 190): an audit of both repositories by measurement (function and file length, duplication, `unsafe`, raw JSON lookups, markers), then the fixes the owner chose — one command runner, one screen dispatch, `effect_inner` as a table, the Bluetooth thread as a worker, stale tools archived — and the [coding standard](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCODING-STANDARD.md) with a ratchet in the gate (`tools/development/code-quality.py`), so the measured figures can only improve from here.

## 4. Test builds

| build | content |
| --- | --- |
| 180 | P0 + P1 (one writer) |
| 181 | P2 (arguments) |
| 182–184 | P3 + P4, two or three groups each (connectivity+devices, storage+service, power+suspend journal+observation) |
| 185 | P5 (Snapshot type) |
| 186 | P6 (reports) |
| 187 | P7 clean-up |

Each: host suite, staged OTA (handoff §6), device check, Reborn contract test against the build's goldens, rollback-read against the previous build, an hour on the player with Reborn's log checked for platform errors, idle after ≥ 30 min. Next free label at the start: 180, sequence above 11240.

## 5. What is decided and what is not

Decided by the owner: byte identity is dropped (§1); critical code keeps its logic (§1 list, which the owner may shorten or extend). Open, to be settled in the step where it comes up (the agent decides, records the choice here, and keeps it reversible): the stdout JSON form (pretty or compact), sorted vs struct order for maps nobody orders, the exact list of tolerances dropped in P3 (each one named in its commit).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
