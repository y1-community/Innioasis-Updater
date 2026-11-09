---
title: "y2-platform contract inventory (Phase 0 of the Rust port) - Innioasis Updater"
description: "y2-platform contract inventory Phase 0 of the Rust port What y2-platform promises to its callers. Written down from the Python platform Linux 4684423 , Beta 8.44, test bu"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-platform-contract.html"
---

# y2-platform contract inventory (Phase 0 of the Rust port) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# y2-platform contract inventory (Phase 0 of the Rust port)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# y2-platform contract inventory (Phase 0 of the Rust port)

What `y2-platform` promises to its callers. Written down from the Python platform (Linux `4684423`, Beta 8.44, test build 165, 2026-10-28) before it was ported ([plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-PORT-PLAN.md), §3 principle 2: the contract does not change); since 2026-10-29 the Rust crates in this directory are the only implementation and the Python platform is deleted (the goldens below were recorded from it).
  - [contract.json](https://github.com/schulzcode/y2linux/blob/HEAD/platform/contract.json) is the machine-readable inventory: `arguments` (39 subcommands, generated

from the parser) and `entries` (106, one per subcommand/action, plus the helper scripts and boot scripts that call the platform). Each entry gives handler (file:line), arguments, exit codes, stdout (format, `schema` value, keys, enum/reason strings, failure shapes), files read and written (and how), locks, timeouts, subprocesses, kmsg/pmsg trail lines, signals, F-numbers on the code path, environment and porting notes; daemons also have `loop`.
  - `tools/development/platform-contract.py --check` (run by `tests.test_platform_differential`) fails when the

parser's table (`crates/y2-platform/src/cli.rs``COMMANDS`, printed by `y2-platform __arguments`) and the `arguments` table differ or a subcommand/action has no entry; `cargo test` compares the same (`contract_json_holds_this_table`). After changing `COMMANDS`: build, `--write`, then review that subcommand's entry by hand.
  - The golden suite that checks the platform against this contract is `tests/platform_golden.py`

(see [below](#golden-suite)).
  - The Rust side of the contract: `crates/y2p-contract` (types and names, shared with Reborn, checked by its

`cargo test` against the goldens in `crates/y2p-contract/tests/golden`, first the Python platform's output; `tools/development/platform-goldens.py --check` keeps them equal to the suite's goldens, without `--check` it rewrites them from the Rust host build) and `crates/y2p-core` (the shared rules below; byte for byte until 2026-10-30, now as the plan's §1 says).

The entries were read from the source by five readers (A observation/boot, B power/sleep/time, C connectivity, USB, SSH, D service/media/update/firmware, E reports/diagnostics/maintenance) and spot-checked against the code and the player; treat an entry as a map to the code, and re-read the code it cites before porting it.

## Rules every subcommand shares

Entry and errors.`/usr/sbin/y2-platform` is the Rust binary (it was `exec /usr/bin/python3 -I /usr/lib/y2-platform/main.py "$@"` until test build 169). An error no command turns into its own record gives `{"schema": "org.y2linux.error/v1", "state": "Failed", "reason": <message>, "type": <class name>}` and exit 1; since the refactor (test build 171) that includes input of an unexpected type, which the Python platform (and the 1:1 port) ended with a traceback on stderr and empty stdout. Argument errors exit 2 with usage on stderr ([Arguments](#arguments)). Several commands catch their own errors first and print a different shape: `{"state": "Failed", "failure": str(error)}` (export-state, reset, firmware, update, time-set, time-remember), `{"failure": "report_failed", "reason": <class name>}` (report), `{"state": "Failed", "failure": "diagnostic_export_failed"}`(export-diagnostics),`{"schema": "org.y2linux.codec-settings/v1", "failure": …}`. `str(error)` of an `OSError` is Python's text (`[Errno 11] Resource temporarily unavailable`, with the path for file errors): callers only show or log it, but a port must decide per command whether to reproduce it (the goldens record it).

Reborn's reading of exit codes (`crates/reborn-platform/src/client.rs``run`): stdout must be one JSON object (≤ 1 MiB); a non-zero exit is an error and Reborn shows `value["failure"]` or `operation_failed`, except `health`, whose exit 1 is evidence. So the `org.y2linux.error/v1` shape (it has `reason`, no `failure`) always reaches the owner as `operation_failed`, e.g. every busy `media.lock`/`internal-media.lock` and `sleep_operation_in_progress` (D). Reborn checks `schema` for status, capabilities, health and sleep.

stdout. One line of compact serde JSON (since 2026-10-30, docs/planning/PLATFORM-RUST-IDIOMATIC-PLAN.md P1; it was Python's `json.dumps` with `", "`/`": "` and `ensure_ascii=True` before): UTF-8 as it is, serde/ryu float spelling. Sorted keys for the generic commands (status, health, capabilities, media, internal-media, space, bench-*, boot-stage) and for sleep, boot-evidence, cpu-idle-policy, report, update, firmware, transfer, network-check, export-*, reset; struct order for the others. `codec-runtime` prints shell tokens (consumed by `usr/libexec/y2/connectivity` under `set -e`); `collect` streams lines; daemons print nothing. JSON callers are order- and spacing-insensitive; shell callers that grep JSON accept both spacings (`'"state": ?"Online"'`). Since the idiomatic-Rust plan the contract is that plan's §1 (Reborn's commands, fields, types and reason texts; the files it and the shell read; /data records an older build must still read; the report bundle; the hardware behaviour). Byte identity is no longer part of it, except the pinned digests: the SD media identity, the reports crash signature and the reset plan confirmation hash Python's sorted `json.dumps` bytes (`y2p_core::json::python_dumps_sorted`, checked against CPython's output), the reset settings digest hashes `record::encode`'s bytes.

Files.`common.atomic_json`: temp `.<name>.<pid>.<monotonic_ns>.tmp` in the same directory (no randomness: the CRNG may not be ready at boot, `test_platform_records_do_not_need_the_random_pool`), `O_EXCL|O_NOFOLLOW| O_CLOEXEC`, mode set by`fchmod`(default 0600), compact`(',', ':')` separators, sorted keys, newline, `os.replace`; `durable=True` adds fsync of the file and then of the directory. `boot.private_directory` creates each missing parent 0700, refuses a non-directory and chmods the target 0700 on every call. `ctx.read` strips and returns `None` above its limit (128 KiB); `ctx.json` returns the default when the type differs; `ctx.glob` sorts and stops at 256 and, unlike most Rust globs, matches dot-files. Journals (`power-journal.jsonl`, `sleep-diagnostics.jsonl`, `wifi-journal.jsonl`) are bounded appends with one `.previous` rotation under their lock.

Subprocesses.`common.command(argv, timeout=1.0, limit=65536)`: no shell, `stdin` and `stderr` to `/dev/null`, own session, `env` exactly `PATH=/usr/sbin:/usr/bin:/sbin:/bin LC_ALL=C`; on overrun the whole tree is SIGKILLed (`kill_tree`, V1 code review B5) and a D-state child is left; result `{ok, reason, output}` with reasons `command_unavailable`, `command_timeout`, `command_output_limit`, `command_failed`. Exceptions to the rule (direct `subprocess.Popen`): service-daemon's children (`media reconcile|verify`, `update auto-check`, `report work`, `firmware scan`), ssh-daemon's dropbear (inherits the environment), the shutdown steps in `power.py`.

Clocks. CLOCK_MONOTONIC for most deadlines, records (`monotonic_ns`, `monotonic_s`) and write windows; CLOCK_BOOTTIME for battery state, the sleep retry gate and "did a sleep happen" (`boottime − monotonic` grew: F49 verify). Wall clock for report names (UTC queue, local time when saved), the daily update check, space cleanup ages, and `record.wall_timestamp`. Monotonic floats are compared across processes (power.json freshness ≤ 10 s for sleep admission, Wi-Fi events).

## Locks (flock; a port must take the same paths in the same mode)````````````````````````````````````````````````

| Lock | Taken by |
| --- | --- |
| /run/y2/activity.lock (shared lease; Reborn holds it while playing; sleep takes it exclusively) | export-state, media repair/write, network-check, report send/upload/work, reset purge, transfer commit, update apply/rollback/probe-recovery, product-sleep, y2-suspend |
| /run/y2/suspend.lock | sleep request, product-sleep, y2-suspend |
| /run/y2/media.lock | media (all but status), firmware scan, report save |
| /run/y2/internal-media.lock | internal-media mount/unmount/provision/setup |
| /run/y2/dhcp.lock (blocking, no timeout) | wifi-event, dhcp-event |
| /run/y2/time.lock (blocking) | time-set, time-remember, ntp-event, service-daemon |
| /run/y2/{power,service,ssh,connectivity-monitor}.lock (single instance) | the four daemons |
| /run/y2/{codec-settings,cpu-idle-policy,rtc-alarm}.lock | codec-settings, cpu-idle-policy, rtc-alarm |
| /run/y2/radiod.lock (single instance) | y2-radiod, the radio daemon (Bluetooth and both radios' power; its clients use /run/y2/radiod.sock, y2p_contract::radiod) |
| /data/system/platform/.boot.lock (blocking) | boot-stage, update health-ack |
| /data/system/platform/.power-journal.lock, .sleep-diagnostics.lock | power-daemon, sleep, product-sleep, suspend-record |
| /data/system/platform/.maintenance.lock, .wifi-journal.lock | reset + product-sleep; connectivity-daemon |
| /data/updates/.lock, /data/updates/.stage.lock | update (all writers); product-sleep checks .stage.lock |
| /data/system/platform/reports/.upload.lock, /data/exports/.diagnostics.lock | report send/upload/work; export-diagnostics |
| /data/transfer-staging/<id>/lock, /data/reset-quarantine/<id> (directory fd) | transfer commit/discard; reset purge |

Most are `LOCK_EX|LOCK_NB` with a named refusal (`*_in_progress`, `busy`); the blocking ones are marked.

## Callers (who must notice nothing)
  - Reborn (`client.rs`, one worker thread, fixed argv): `status --reborn --pss` (25 s) + `capabilities` (10 s)
    - `report status` (10 s) per refresh while a platform screen is visible, `health` (30), `status wifi` (25),

  - Boot and shell scripts (production overlay): `S02y2-media` (internal-media setup --automatic, mount),

`S03y2-platform` (boot-stage platform_start → kmsg), `S03y2-time` (time-bootstrap), `S05y2-cpu-idle`, `platform-supervise` / `power-supervise` / `readiness-supervise` / `ssh-supervise` (a daemon's exit 0 ends its supervision for good), `connectivity` (connectivity-daemon), `wpa-event`, `dhcp-event`, `ntp-event`, `y2-media`, `y2-suspend` (sleep prepare). `y2-radiod` runs `codec-runtime --record` when it starts BlueALSA; `y2-radio` hands every request to `y2-radiod ctl`. `S43y2-time` greps `network.json` for the literal `"state":"Online"`, so compact separators in that file are part of the contract.
  - The platform itself: power-daemon runs `boot-stage shutdown_pending|shutdown_complete` and `time-remember`

as shutdown steps (each a new Python process today, ≈0.5 s: F39 trail); service-daemon starts `media reconcile`, `media verify`, `update auto-check`, `report work`, `firmware scan`, `space --cleanup`, `update health-ack`, `boot-stage application_ready`; connectivity-daemon runs `wifi-event SERVICE_RESTART`.
  - initramfs: `/sbin/y2-platform-start` (C) and the marker `/etc/y2linux/platform-contract` = `y2-platform-v1`.
  - Readers of state files: the error-report scrubber and Worker, `tools/reports`, the `UserReports` analyses

(power journal, previous-boot evidence, sleep diagnostics, wifi journal field names).

## What a port must not miss (collected from the entries)
  - Python inside the platform's own subprocesses (done in phase 6): the DNS probe ran `/usr/bin/python3 -I -c

'socket.getaddrinfo…'`and is Rust's`getaddrinfo`now; the report upload used in-process`urllib` (no redirects, no proxy, 30 s socket timeout, 16 KiB streamed body) and runs `curl` with the same limits.
  - Byte-exact Python JSON inside values: the reset plan `confirmation` and the settings-result sha256 hash

`json.dumps(sort_keys=True)` (compact), the media identity id hashes `json.dumps(sort_keys=True)` with the default separators. A plan made by Python must still confirm under Rust: reproduce these encodings exactly.
  - The scrubber (report): Python regex semantics (lookbehinds, Unicode `\b`), a prefix-tree regex, a per-report

random HMAC key with 6-hex tokens, archive members in order with `report.json` first, gzip mtime 0, a 2 MiB budget reached by halving the largest section. Port it with golden archives from the Python side.
  - bench-storage draws data and offsets from Python's Mersenne Twister seeded with 6582: port the generator or

declare the bytes outside the contract.
  - Suspend-path writes stay single unbuffered writes in order: `wakeup_count`, backstop 30, `mem`, backstop 0;

`/sys/power/wakeup_count` is read through a killable `/bin/cat` with a 0.1 s limit (an in-process read can block).
  - Shutdown timing (F39/F50): the steps add up to ≈29 s against the 31 s watchdog fed when a step begins; while

`execute()` runs the daemon accepts no clients (`shutdown` callers time out after 1 s); a Failed intent is not retried. Faster steps change these margins: watch the pmsg trail on the device.
  - Ordering:`boot-evidence` must run before any `boot-stage` of a boot (`previous_boot_capture_missed_early_boundary`);

`boot-stage application_ready` writes power features to sysfs while holding the blocking `.boot.lock` and its callers kill it after 2–3 s; the wpa restart order (DHCP teardown → SERVICE_RESTART → stop the action daemon → supplicant); `update stage` SIGTERM handling changes three times (default during the manifest, cancel during the payload, ignored after commit); `cpu-idle-policy start` writes its once-per-boot marker before its checks.
  - Randomness: uuid4/urandom/getrandom for the Wi-Fi epoch, transfer and install ids, the shutdown intent id,

bench run names, resolv.conf temp names, report keys. Early-boot callers must not block on the CRNG.
  - Real-root-only branches (`ctx.root == '/'`): pidfd SIGKILL, product-sleep launch, `getrandom`;

`os.kill(pid, 0)` in connectivity-daemon and `/proc/self/fd/N` in transfer commit are used even under a test root; `y2-power-audit` opens every path directly.

## Ported to Rust (`platform/crates/y2-platform/src/commands`)

The dispatcher parses the arguments first ([Arguments](#arguments)), then runs every subcommand from its canonical form. There is no Python platform any more (phase 6, 2026-10-29): every subcommand and action has a route (main.rs's test `every_command_line_the_parser_takes_has_a_route`), the image has no Python, and `y2-status`, `y2-health`, `y2-suspend-record`, `y2-power-audit`, `/sbin/poweroff` and `/sbin/reboot` are links the binary answers to by argv[0] (`commands::suspend::program`). The internal programmes (`__product-sleep`, `__suspend-record`, `__power-command`, `__power-audit`) read their own arguments, as the Python scripts did (`os.fsdecode` for bytes that are not UTF-8, `y2p_core::os_text`); environment values (dhcp-event, ntp-event) too. `y2-platform __arguments` prints the argument table (for `platform-contract.py`).

### Arguments

Since 2026-10-29 (owner decision "replace, keep exit 2"; it replaced an emulation of CPython 3.15's argparse) the parser is `src/cli.rs`: a table of every subcommand's arguments (`COMMANDS`: type str/int/float, choices, default, required, flag or append, help) and a small parser over it.
  - Forms: `--opt value` and `--opt=value` (any text after `=`, also one starting with `-`), exact option names

only; a flag takes no value; an option given twice keeps the last value, an append option (`--pid`) every one; positionals in order, options anywhere; `--` ends the options (for a subcommand without positionals it is an argument too many); a token starting with `-` is a value when it is a negative number or holds a space.
  - Numbers: plain decimal integers with an optional sign that fit 64 bits; plain finite decimal floats (`1`, `.5`,

`5.`, `1e-3`). An int choice (`--tracks`) compares the number (`01000` is `1000`).
  - The canonical form handed to `commands::route`: the subcommand, the positionals given, then each option given in

table order under its full name (a flag bare, `--opt value` as two tokens, an append option once per value); ints in plain decimal, floats in Python's repr (`1.0`, `1e-05`), which the routes read.
  - `-h`/`--help` anywhere before `--` prints that subcommand's help on stdout (exit 0), unless an argument before

it was already refused. The help texts are argparse's 80-column layout with `y2-platform` for `main.py`.
  - Errors: exit 2, nothing on stdout, the usage and one `y2-platform <cmd>: error: <message>` line on stderr

(values quoted). Refused since the decision (Python took them): abbreviations and ambiguous prefixes (`--reb`), short-option clusters (`-hx`), Python's int()/float() spellings (spaces, `_`, non-ASCII digits, `inf`, `nan`), numbers beyond 64 bits or out of float range, and arguments that are not UTF-8 (no caller passes one: CONTRACT "Callers"; a non-UTF-8 `transfer --name` or owner path failed later before). No caller used any of them (checked: Reborn's client.rs, the overlay scripts, the platform's own children; `cli_tests.rs``what_callers_pass_parses_as_given`).

Where Python raises an exception main.py catches, Rust prints main.py's error record with Python's exact `str(error)` and class (`ipaddress`'s `AddressValueError` and `NetmaskValueError`, `int()`'s `ValueError`, `UnicodeEncodeError`), or the command's own failure shape where the command catches it; where Python crashes (`TypeError`, `AttributeError`, `KeyError`, `IndexError`), the port ended the same way; since the refactor these are refusal records (see [the refactor](#refactor-2026-10-29-test-build-171)). Each command has golden cases, recorded from the Python platform before it was removed (see [below](#golden-suite)).``````````````````````````````````````````````````

| Command (forms) | Module | Python |
| --- | --- | --- |
| capabilities [--json] | capabilities.rs, codec.rs | capabilities.status + cli tail |
| sleep status | sleep.rs | sleep.status/product |
| time | time.rs | timekeeping.status |
| time-remember | time.rs | timekeeping.remember(every=0) |
| ntp-event step\|stratum\|periodic\|unsync | time.rs | timekeeping.ntp_event |
| boot-stage <stage> | boot.rs, power_features.rs | boot.mark, power_features.apply |
| codec-runtime [--record] | codec.rs | radio_policy.codec_runtime |
| wifi-event CONNECTED\|DISCONNECTED\|SERVICE_RESTART | network.rs | network.lease_event |
| dhcp-event deconfig\|leasefail\|nak\|bound\|renew | network.rs | network.dhcp_event |
| cpu-idle-policy start\|stop | cpu_idle.rs | cpu_idle.apply |
| every other subcommand, the four daemons, the sleep helper and the scripts (plan §5a groups) | commands/<group>/ | the module named in each file's header |

Known, accepted differences (none reachable from the platform's own records): JSON input with `NaN`, `Infinity` or integers beyond 64 bits reads as unreadable (Python reads them); an `OSError` while writing a record names the record, not Python's temporary file; `str.splitlines` separators other than `\n`/`\r\n` in sysfs text; a valid UTF-8 argument of an internal programme holding U+10DC80..U+10DCFF reads as an escaped byte; a `y2-suspend-record` result beyond 64 bits is refused like a non-number (y2-suspend passes exit codes). Compressed report archives differ in bytes from zlib's (their members do not). File calls use the 64-bit interfaces on the 32-bit player (`stat64`, `statvfs64`, …), as Python does; `time_t` stays 32 bits there (dates after 2038, as the rest of the 32-bit userspace).

## Refactor (2026-10-29, test build 171)

[PLATFORM-RUST-REFACTOR-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-REFACTOR-PLAN.md): one shared core, typed records, split modules, tests through the root's runner and clock. Outputs stay byte-identical (checked against the build before it with `tools/development/platform-raw-goldens.py`, key order and spacing included) except these owner decisions and fixes, each a re-recorded golden:
  - Arguments:`cli.rs` replaces the argparse emulation ([Arguments](#arguments)): exact option names and

`--opt=value`, errors exit 2; abbreviations and Python's number spellings are refused.
  - Crash paths are refusal records: every input of an unexpected type that ended in a traceback now prints a

failure record and exits 1 (the command's own shape, e.g. `{"state": "Failed", "failure": "invalid_…"}`, or the error record). Reasons by group: observation `invalid_timer_list`, `invalid_power_record`, `invalid_sleep_receipt`, `invalid_ip_output`, `invalid_network_record`, `invalid_update_journal`, `invalid_previous_boot_evidence`, `invalid_codec_inventory`, `invalid_capabilities_template`, `evidence_record_too_large`; connectivity/devices `invalid_codec_inventory`, `invalid_codec_runtime_record`, `invalid_transfer_manifest` (checked before anything is sealed or published); storage `usb_transfer_views_invalid`, `sd_write_holders_invalid`, `card_identity_invalid`, `power_battery_invalid`, `filesystem_check_invalid`, `setup_record_incomplete`; service `update_channel_unreadable`, `update_health_record_unreadable`, `record_unreadable: …`, `responder_stop_timeout`; reports (as the `reason` of `report_failed`) `report_state_unreadable`, `queued_report_unreadable`, `reborn_health_unreadable`, `power_record_unreadable`, `session_unreadable`, `update_state_unreadable`, `reset_plan_unreadable`, `reset_record_unreadable`, `scrubber_pattern_too_large`; power `invalid_power_response`. Some texts still carry Python's message (owner review open).
  - Daemons survive odd records: power-daemon notes an unwritable power.json/shutdown.json or a damaged

acknowledgement and carries on (a shutdown still runs every step); service-daemon skips a report retry time, traffic counter or USB mode of the wrong type; connectivity-daemon keeps the other helpers when the codec inventory is unreadable. The sleep helper's restore runs every step even when one fails.
  - DHCP: a renew that repeats this boot's and epoch's Authenticated lease (address, prefix length, routes, DNS)

runs no `ip` command and keeps resolv.conf and dns.json; dhcp.json and the event's stdout gain `prefix_length` and `routes` (`[[destination, gateway]]`) to compare with.
  - Fixture argv: below a fixture root the DNS probe records `["getaddrinfo", <host>]` (it named the Python

one-liner).

## Typed records (2026-10-30, test builds 181–185)

[PLATFORM-RUST-IDIOMATIC-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-IDIOMATIC-PLAN.md) (P0–P7, Q1–Q5): every record the platform owns is a Rust struct, read leniently where a field may be missing and written in its fields' types; the Python emulation (`pyjson`, `pyops`, `Failure::Crash`, the dict/`json.loads` error texts) is gone. Owner rules:
  - /data stays rollback-safe: a struct keeps the field names and types an earlier build wrote (new fields are

allowed); `tools/development/record-compat.py` (in the gate) compares every /data file the goldens write with the release before, reviewed odd-fixture exceptions in `tools/development/record-compat-allow.txt`. Digests over stored JSON keep their encoding (the reset plan's `confirmation` is checked over the plan as read).
  - Status and health answers may change shape (Reborn's parser and its contract test change in the same step):

a field that does not read is left out or `null`; a broken record makes its section Unavailable/Failed instead of refusing the whole `status` (an update journal whose state is no text: update Unavailable, no longer `invalid_update_journal`).
  - The critical path fails closed with one reason (owner decision for Q4): a sleep receipt that does not read

refuses as `suspend_receipt_unreadable` (the failure and the restore are still recorded, in a new receipt; the next request starts a new one), Reborn's sleep answer that is no JSON object as `reborn_sleep_answer_unreadable`, a corrupted quarantine guard as `sleep_recovery_required`, a reset plan that does not read as `reset_plan_unreadable` before anything moves, a reset record as `reset_record_unreadable`, Reborn's saved session as `invalid_saved_session`. The refusal reasons listed under the refactor above that named Python's messages (`record_unreadable: …`, dict/`int()` texts) are these now.
  - Shared types:`y2p_contract::{Versions, Capabilities, Health, ObservationRecord, …}`; one record type per

file where several commands read it (the SD `MediaRecord`, the shutdown `Intent`, the suspend `Receipt`, the power-journal row, the sleep-diagnostics row, `ProcessIdentity`, the battery profile, the mtp records).
  - Boundaries kept as written: the native update core's journal and answers (typed fields the platform reads,

its install records as written), Reborn's session file in a settings reset (only `settings` is replaced), power.json's battery as copied into the receipt, report bundles' copies of release.json/versions.json.

## Records Reborn reads in the platform's types (2026-10-30, after Beta 9.0)

The records Reborn decides on are now `y2p-contract` types the platform writes and Reborn reads, so a field renamed or retyped on one side no longer compiles on the other. Each module keeps the platform's own reading rules (lenient where a record of another version may be read, strict where the platform is the only writer); what needs the player (a root, the clock, a failure text) stays in the platform as free functions or a trait (`storage::records::OnPlayer`).````````````````````````````````````````````````````````````````````````````````````````````````

| Module | Types | Platform | Reborn |
| --- | --- | --- | --- |
| lenient | the lenient field readers, BootId, Shaped | y2p-core re-exports it | client, power, storage |
| sleep | Product, ProductState, WakeSource | the suspend receipt | sleep state |
| update | Status, CoreJournal, Records, Download, LastCheck, DownloadProgress, DownloadPhase | update status, download.json, last-check.json, the live download record | Software Update page, download progress |
| power | PowerRecord, BatteryStatus, Estimate, BatterySource, Confidence, BatteryState, Intent, IntentState, ShutdownAction, Acknowledgement, Step, ProcessIdentity | power.json (the daemon writes the shared record), shutdown.json | battery level, voltage reuse, shutdown intent |
| network | Published | network.json's readers | Wi-Fi readiness |
| storage | MediaRecord, ReadOnly, Check, Identity, Geometry, Y2MediaClaim, SetupStatus | the SD records, internal-media.json, the setup note | SD source checks, internal music folder, Internal Storage setup |
| usb | Receipt, View | the media hand-off's view check | USB screen, library refresh |
| reports | ReportProgress, ReportPhase | report-progress.json | report progress |
| radio | FirmwareStatus | firmware status | Wi-Fi/Bluetooth firmware state |

Still read as JSON on purpose: the status snapshot's other sections (volumes, USB controller states, health, capabilities, the diagnostics page, which shows whatever a field holds), and the platform's own writers that borrow (`connectivity::published::Record`, `service::usb::Transfer`), whose readers are the types above. The recorded contract (`crates/reborn-platform/tests/platform-contract.expected.json`) did not change in these steps except for the removed `download_percent` (download.json never carried a byte count).

## Defects found while inventorying and porting (fixed 2026-10-29)

Ported 1:1 first (owner decision 2026-10-28: port, then fix), fixed in Rust after Phase 6, each with a test.````````````````````````````````````````````````````

| Finding | Fix |
| --- | --- |
| usr/libexec/sftp-server grepped internal-media.json for "state": "Ready" (with a space); the record is compact, so SFTP always opened /data/music (confirmed on the player) | the grep takes both forms (tests/test_sftp_root.py) |
| media status exited 1 for a Degraded (read-only) or Failed card | exits 0 for every state it reports (storage::media_exit) |
| media write exited 0 with failure set for not_mounted | exits 1 whenever it sets failure; Reborn's write window treats it as no window |
| A second update check/stage meeting the busy .stage.lock overwrote download.json with Failed [Errno 11] while the first download went on | refused as update_in_progress before anything is written; auto-check leaves the record alone; Reborn: "An update check is already running." |
| update rollback asked the core before the battery gate: a battery refusal left the journal RollbackPending | the battery gate comes first |
| update auto-check printed null when it did not check | prints {"schema": 1, "result": "skipped", "reason": …} (not_due, update_pending, no_channel, offline, clock_not_ready) |
| firmware scan exited 0 when the owner's copy could not be installed | exits 1 with state Failed, as firmware install |
| Battery: a voltage sample after fuel-gauge samples had no display value (Python's power daemon ended on a TypeError; found during the port) | it starts as a first sample |
| An expired media write window was re-protected only by a reconcile, which the service started only on an insertion, removal or retry | the service also starts one when media::window_expired (protected, mounted rw, no live holder); device check owed |
| A DHCP renew deleted dns.json: Wi-Fi showed dns_unavailable for up to 300 s | a renew of the same lease (boot, epoch, address, DNS servers) keeps it |

## Golden suite

`tests/platform_golden.py` runs one subcommand as the Rust host build (`Y2_PLATFORM_RUST`) on a fresh copy of a fixture root and compares the normalised result with the case's golden, `tests/platform_goldens/<base|group>/ .json`: argv, exit code, stdout (parsed, root and checkout paths replaced), the subprocess requests and the tree difference against the root as the command found it (paths added, changed or removed, with type, mode, contents parsed per JSON line, symlink targets), after normalising clock readings by key name (`monotonic_ns`, `wall_timestamp`, …), today's date and per-case patterns (uuids). The binary must honour `Y2_ROOT`, `Y2_FIXTURE_COMMANDS`, `Y2_FIXTURE_CALLS`, `Y2_DAEMON_TICKS` and `Y2_FIXTURE_TOKEN` (module docstring). The cases are `tests/test_platform_differential.py`'s and `tests/platform_cases/.py`'s; the groups' modules (`tests/test_platform_{devices,observation,reports,suspend,power_rpc}.py`) add the runs a plain one cannot give (renamed random names, archive listings, a plan made first, a fake Reborn socket, held locks, a live power daemon). `tests/test_platform_argparse.py` runs the 5 729 argument lists of `tests/platform_goldens/ argparse.jsonl.gz` (the parse only: `Y2_ARGPARSE_ECHO` prints the canonical form below a fixture root); each line holds Python's argparse outcome with the canonical form routes got then (fixed) and today's outcome (`rust`, re-recorded). A list without a feature the [Arguments](#arguments) decision dropped must keep Python's exit code and canonical form (3 517 lists), one with such a feature is refused now (1 207) or unchanged (1 005). Every golden was first recorded from the Python platform (Linux `3ac47c6`, the Rust build of that commit matched each). All are in `tools/production/tests.sh`; without a host build (the release container has no cargo) the runs are skipped and the goldens' own checks run. 

A deliberate behaviour change (a defect fix) re-records the goldens it touches and shows in the git diff:`cd platform && cargo build --offline --locked && cd .. Y2_RECORD_GOLDENS=1 Y2_PLATFORM_RUST=$PWD/platform/target/debug/y2-platform \ python3 -m unittest tests.test_platform_differential tests.test_platform_argparse tests.test_platform_devices \ tests.test_platform_observation tests.test_platform_reports tests.test_platform_suspend tests.test_platform_power_rpc git diff --stat tests/platform_goldens`

Recording writes only goldens that differ and removes goldens no case names; without it a missing golden fails. Add a case (and record its golden) for each changed command.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
