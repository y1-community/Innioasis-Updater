---
title: "Platform service: port from Python to Rust, then remove Python from the player - Innioasis Updater"
description: "Platform service: port from Python to Rust, then remove Python from the player Status: All phases implemented on main 2026-10-29: the whole platform is Rust and the image"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-platform-rust-port-plan.html"
---

# Platform service: port from Python to Rust, then remove Python from the player - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform service: port from Python to Rust, then remove Python from the player

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform service: port from Python to Rust, then remove Python from the player

Status: All phases implemented on `main` (2026-10-29): the whole platform is Rust and the image has no Python; test build 169 is on the owner's player (Acknowledged), the owner's hardware checks (incl. two overnight runs) are next. Handoff: [PLATFORM-RUST-PORT-HANDOFF.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-PORT-HANDOFF.md). Owner's goal: everything that runs on the player is Rust (Reborn), C (kernel, early boot, installer) or shell (init scripts); no Python in the image. Host-side tooling (release, build, validation, the test harness) may stay Python.

This plan is written for an agent picking the work up cold. Read it fully, then [AGENTS.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2FAGENTS.md), [CURRENT_PLATFORM_STATE](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) and the top entry of [NEXT-SESSION-HANDOFF](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md) before changing code.

## 1. Why

Measured on the owner's player (Beta 8.44 test build 165, 37 min awake on the charger, 2026-10-28):````````

|  | Python platform (4 daemons) | Reborn (Rust) |
| --- | --- | --- |
| RSS | service 20.3 + connectivity 15.3 + power 12.8 + ssh 11.5 ≈ 60 MB (shared pages counted per process) | 27.5 MB |
| CPU time | 67 s (power-daemon 38 s, service-daemon 23 s) | 28 s |
| Image | Python 3.15 ≈ 22 MB (usr/lib/python3.15 17 MB, libpython3.15.so 4.9 MB) + 12 334 lines of source | 8.6 MB binary |
| One CLI call | python3 -I -c pass 0.15 s; y2-platform sleep status 0.52 s | — |

Every CLI call is a new Python process: Reborn's polling (`status --reborn --pss` every 4–15 s), every `wpa-event`/`dhcp-event`/`ntp-event`, every boot-stage journal write (two per shutdown, ≈0.5 s each, see the F39 trail). Awake CPU costs battery; the 22 MB and the RAM come back only when Python is gone entirely.

Also wanted: one language with Reborn and shared contract types. Reborn and the platform exchange JSON whose field and reason strings are matched by hand on both sides; F52 ("not_authenticated" read as a wrong password) was such a mismatch. A shared `serde` crate makes the compiler check it.

## 2. What exists (inventory, 2026-10-28)

Source:`tools/platform/y2_platform/` (43 modules, 12 334 lines), entry `tools/platform/main.py`, helpers `product-sleep.py`, `suspend-record.py`, scripts `y2-platform`, `y2-health`, `y2-power-audit` (Python), `y2-power-command`, `y2-status`, `y2-suspend-record`. Installed to `/usr/lib/y2-platform` + `/usr/sbin`. Biggest modules: report 1420, media 902, observe 758, update 695, product_sleep 571, internal_media 571, radiofw 568, network 550, usb 483, power 458, cli 430, maintenance 423, bench 396, service 354, battery 337.

Daemons (started by `S03y2-platform` / `platform-supervise` / `connectivity`): `power-daemon` (battery, charger, sleep, maintenance wakes, shutdown coordinator), `service-daemon` (media/SD admission, updates, reports, internal storage, time), `connectivity-daemon` (Wi-Fi/BT supervision, radio policy, F52/F53 heal), `ssh-daemon`.

CLI subcommands (`cli.py`): status, health, capabilities, boot-evidence, boot-stage, cpu-idle-policy, bluetooth-power, sleep {request,status,prepare}, power-daemon, service-daemon, connectivity-daemon, usb-mode, codec-runtime, codec-settings, wifi-power-policy, ssh-daemon, transfer, reset, export-diagnostics, report {…}, export-state, firmware, update {check,apply,cancel,rollback,stage,status,…}, time-bootstrap, time, time-set, time-remember, rtc-alarm, ntp-event, wifi-event, dhcp-event, network-check, shutdown, media {…}, internal-media {…}, bench-storage, space, bench-library, collect.

Callers on the player: Reborn `crates/reborn-platform/src/client.rs` (`/usr/sbin/y2-platform` with capabilities, codec-settings, export-diagnostics, export-state, health, internal-media setup, media repair, report {enable,disable,new-id,save,send,status}, sleep request, status --reborn --pss, status wifi, time-set, update {apply,cancel,check,rollback}); `storage.rs` → `/usr/sbin/y2-media`; `power.rs`. Overlay scripts (`buildroot/board/y2/production-overlay`): `etc/init.d/S02y2-media`, `S03y2-platform`, `S03y2-time`, `S05y2-cpu-idle`, `usr/libexec/y2/{platform-supervise,connectivity,wpa-event,dhcp-event,ntp-event}`, `usr/sbin/{y2-media,y2-radio,y2-suspend}`. initramfs: `/sbin/y2-platform-start` and the platform contract marker `/etc/y2linux/platform-contract` = `y2-platform-v1`.

State contract (files other parts read; keep paths and shapes): `/run/y2/*.json` (power.json, network.json, media.json, media-mount.json, storage.json, wifi-events.json, application-ready.json, boot-stages.jsonl, …), `/data/system/platform/*` (boot.json, power-journal.jsonl, previous-boot-evidence.json, sd-admissions.json, sleep-diagnostics.jsonl, battery-ui.json, wifi-journal.jsonl, reports/…), `/data/updates/*` (state.json, …), pmsg/kmsg trail lines (`shutdown begin …`, `platform …`), versions `platform_api_version` 1, `feature_contract_version` 2, `capabilities.json`. The error-report scrubber/uploader, the report Worker and the review tooling (`tools/reports`, `UserReports/REVIEWED.md` analyses) parse these: field names are an API.

Python elsewhere on the player: none found besides the platform (`grep -rlI '^#!.*python'` in the target finds only `y2-power-audit`). Buildroot: `BR2_PACKAGE_PYTHON3=y` (+ `_PY_ONLY`, `_SQLITE`, `_SSL`, `_ZLIB`) in `buildroot/configs/y2_production_defconfig`. Verify nothing else selects it before removal (§5 phase 6).

Tests: 46 test modules import `y2_platform` (e.g. test_platform_power_contract, test_battery_soc, test_product_auto_sleep, test_platform_update, test_error_reports, test_connectivity_supervisor, test_wifi_failure_evidence, test_platform_evidence, test_sleep_product, test_internal_media, test_platform_storage_tools, …; ≈28 700 lines of Python tests overall). Most build a fake root tree and call functions through `ctx` (`common.py`: `ctx.path`, `ctx.read`, `ctx.json`, `ctx.command`, atomic JSON writes).

## 3. Principles
  - Strangler, not big bang. One Rust multicall binary becomes `/usr/sbin/y2-platform` early. Subcommands it

implements run in Rust; the rest `exec` the Python entry (`python3 -I /usr/lib/y2-platform/main.py …`) with the same arguments. Move command by command, daemon by daemon. Python is removed only in the last phase.
  - The contract does not change. Same CLI arguments, exit codes, stdout JSON, file paths, file shapes (field

names, types, enum strings), timeouts, lock files and lock protocol (flock on the same paths), atomic-write semantics (temp + fsync + rename, no randomness at boot: see `test_platform_records_do_not_need_the_random_pool`), pmsg/kmsg line texts. Reborn and the report tooling must notice nothing. Contract changes, if ever wanted, are a separate step after parity. This includes known defects (owner, 2026-10-28: "port 1:1 then fix"): the suspected defects in [CONTRACT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fplatform%2FCONTRACT.md%23suspected-defects-found-while-inventorying-not-changed-in-phase-0&anchor=suspected-defects-found-while-inventorying-not-changed-in-phase-0) are ported as they are, marked with a `// DEFECT (CONTRACT.md): …` comment, and fixed in Rust after Phase 6, when no Python is left in the image.
  - Python and Rust coexist safely. During the transition a Python daemon and a Rust CLI may touch the same state:

identical locking and write order are mandatory, not optional.
  - Port behaviour, including the fixes. Every F-number fix in the Python code (comments name them: F13, F23,

F34, F36, F38, F39, F46–F57 …) is behaviour to keep. Port the comment with the code. Read the ledger row (`UserReports/REVIEWED.md`, private) when a comment names one.
  - Differential testing is the safety net. For each ported piece, run Python and Rust on the same fake root

trees and compare outputs and resulting files exactly (normalise only timestamps that are inputs).
  - Hardware gates. Power, sleep, battery, charging, update and shutdown pieces each need a test build on the

owner's player and an overnight run before the next phase (AGENTS.md: broader qualification for architecture changes; repeat the roadmap gap audit at milestone boundaries).
  - Small and boring Rust. No async runtime unless a daemon really needs it (the Python daemons are loops with

sleeps and subprocesses; mirror that with threads/poll). Dependencies: `serde`, `serde_json`, `libc` (or `rustix`), maybe `rusqlite` (only if a ported command needs SQLite). Keep using the `curl` binary for HTTPS as Reborn does (`radio.rs`, `lastfm.rs`): no TLS stack in the binary. Release profile `opt-level = "s"`, LTO, `panic = "abort"` only if no code relies on unwinding.

## 4. Layout and build
  - New Cargo workspace in Y2Linux: `platform/` with
    - `y2p-contract` — serde types for every JSON the platform writes or prints (status, network, power, media,

update state, sleep, report status …), enum reason strings as Rust enums with `#[serde(rename = …)]`.
    - `y2p-core` — root-prefixed paths (`Y2_ROOT` / `--root` for tests, like `ctx.path`), atomic JSON, command runner

with deadlines and D-state-aware timeout reporting (port `common.command`), flock helpers, kmsg/pmsg trail, monotonic/boottime clocks.
    - `y2-platform` — the multicall binary (one crate per area is fine: power, service, connectivity, media, update,

report, time, usb, ssh).

  - Toolchain: the same pinned Rust as Reborn (`rust-toolchain.toml` 1.99); vendored crates (`cargo vendor`) as Reborn

does; a Buildroot package `buildroot/package/y2-platform` modelled on `buildroot/package/reborn`.
  - Contract sharing with Reborn: Reborn should depend on `y2p-contract` instead of its hand-written structs in

`reborn-platform`. Options: (a) Reborn vendors `y2p-contract` from Y2Linux at a pinned commit, (b) the crate lives in Y2Reborn and Y2Linux vendors it. Pick one in phase 1 and write it down; release tooling (`tools/production/release.py`) must keep both repos' commits consistent. Decided (owner, 2026-10-28: "deem as you think is best"): (a). The crate lives in Y2Linux (`platform/y2p-contract`): the platform writes the records, its Python goldens and the differential harness are here, and most contract changes start on the platform side. Reborn keeps building on its own (as now: `cargo vendor`, no network, contributors without a Y2Linux checkout) from a vendored copy `vendor/y2p-contract` plus a stamp file naming the Y2Linux commit and the tree hash; a small `release.py sync-contract` copies it, and `release.py build` refuses to build when Reborn's copy differs from Y2Linux HEAD's crate (the same way publish already refuses a Reborn HEAD that is not the built commit). The crate carries `platform_api_version`/`feature_contract_version` as constants, and the platform's golden JSON fixtures are its tests.
  - Install: Rust binary at `/usr/sbin/y2-platform`; Python moves to `/usr/lib/y2-platform/main.py` only (the

fallback). `capabilities.json` and the contract marker unchanged.

## 5. Phases

Each phase ends with: host tests green (`tools/development/host-tests.sh`), Reborn tests green, a test build (`release.py build --label N`, see docs/BUILDING.md §7) installed on the owner's player by staged OTA and Acknowledged, the phase's device checks, a handoff entry. Publish only when the owner says so.

### Phase 0 — Baseline and contract inventory (no product change)
  - Measure on the player: RSS and CPU of each daemon over 1 h awake idle and 1 h playing; awake current (charger

register or battery delta); CLI latency for every command Reborn calls; boot stages (`platform_start` → `services_started` → `application_ready`); overnight drain. Write them into this plan (§7 table).
  - Generate a machine-readable contract inventory: for every subcommand its arguments, exit codes, stdout schema,

files read/written, locks, timeouts, subprocesses. Start from `cli.py` and the tests; record it as `platform/CONTRACT.md` (or JSON) and keep it updated.
  - Build the differential harness: a host test helper that runs a subcommand under Python and under a host build

of the Rust binary against the same fake root (copy of the fixture tree), then diffs stdout, exit code and the resulting tree.
  - Done 2026-10-28: measurements in §7; inventory [platform/CONTRACT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fplatform%2FCONTRACT.md) +

`platform/contract.json` (106 entries, argument table checked against the parser); harness `tests/platform_differential.py` (+ launcher), `tests.test_platform_differential` in `tools/production/tests.sh` (16 cases Python vs Python, perturbation checks, hermeticity audit; Rust comparison skipped without `Y2_PLATFORM_RUST`). The inventory found six suspected defects (CONTRACT.md), one confirmed on the player.

### Phase 1 — Skeleton and dispatcher
  - Workspace, `y2p-core`, `y2p-contract` (start with the types of `status`, `health`, `capabilities`, boot stages),

Buildroot package, multicall binary that implements nothing yet and execs Python for every subcommand.
  - Device check: everything behaves exactly as before (one boot, sleep, update restart).
  - Implemented 2026-10-28 (entry audit "PLATFORM-RUST phase 1"): `platform/` workspace with vendored serde,

serde_json, libc, ryu (Reborn's pins) and Rust 1.99.0; `y2p-core` (root paths and `ctx.read`/`integer`/`json`, `json.dumps`-identical output incl. float `repr` checked against host Python on 20 000 random values, `atomic_json`, `private_directory`, flock helpers checked against a Python holder, monotonic/boottime clocks); `y2p-contract` (schema names, boot stage/line/record, health, capabilities, status envelope, error record; round-trip tests on Python goldens from `tools/development/platform-goldens.py`); `y2-platform` (dispatcher: `exec` of the same Python command; with `Y2_ROOT` the harness may name its interpreter/entry). Buildroot package `y2-platform`, post-build checks that `/usr/sbin/y2-platform` is the ELF, `validate.py` checks it in tar and ext4; the shell wrapper `tools/platform/y2-platform` is gone. Reborn: `crates/y2p-contract` (copy + `Y2LINUX-SOURCE` stamp), `reborn-platform` uses its schema names; `release.py sync-contract`, and `build` refuses a differing copy. `host-tests.sh` builds the host binary, so `tests.test_platform_differential` compares Rust with Python (all 16 cases identical). Device-checked on test build 166 (seq 11110, audit "PLATFORM-RUST phase 1"): Acknowledged after a staged OTA, a restart through the dispatcher (shutdown trail 2.57 s, orderly), Settings/About data, one unplugged sleep cycle (261.6 s, same boot, result 0); the dispatcher adds 4–22 ms per call.

### Phase 2 — Hot short-lived commands (largest CPU win, low risk)
  - `status` (incl. `--reborn --pss`, `wifi`), `health`, `capabilities`, `boot-stage`, `boot-evidence`,

`time-remember`, `time`, `sleep status`, `wifi-event`, `dhcp-event`, `ntp-event`, `network-check`, `codec-runtime`, `cpu-idle-policy`.
  - Device checks: Reborn screens that show platform state (Settings, About, Wi-Fi, Storage), shutdown trail timing,

Wi-Fi connect/reconnect events, CPU before/after.
  - Part 1 implemented 2026-10-28:`capabilities`, `sleep status`, `time`, `time-remember`, `ntp-event`,

`boot-stage` (with the power features at `application_ready`), `codec-runtime`, `wifi-event`, `dhcp-event`, `cpu-idle-policy` in Rust ([CONTRACT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fplatform%2FCONTRACT.md%23ported-to-rust-platformcratesy2-platformsrccommands&anchor=ported-to-rust-platformcratesy2-platformsrccommands): exact argument forms, fallbacks, accepted differences); `y2p-core` gained the bounded command runner (fixture answers below `Y2_ROOT`), Python value rules (`is True`, bools as ints, `1.0 == 1`), `OSError` texts and uuid4. 62 differential cases, all identical Rust vs Python, each checked to run in Rust or fall back as intended. Device-checked on test build 168 (167 carried phase 1's binary: fixed package version, now the git tree of `platform/`): ported calls 8–17 ms instead of 527–541 ms, restart trail 1.20 s instead of 2.57 s, plain boot application_ready 40.59 s instead of 44.44 s, records as before. Part 2 (next):`status` (incl. `--reborn --pss`, `wifi`), `health`, `boot-evidence`, `network-check`: they sit on `observe.py` and most other modules (the largest single piece of phase 2).

### Phase 3 — Small daemons and remaining simple commands
  - `ssh-daemon`, `connectivity-daemon` (network.py, connectivity.py, radio_policy, bt_control, bluetooth, the F52/F53

heal and wifi-journal), `usb-mode`, `wifi-power-policy`, `bluetooth-power`, `codec-settings`, `time-set`, `time-bootstrap`, `rtc-alarm`, `space`, `transfer`.
  - Device checks: Wi-Fi join/wrong password/heal, Bluetooth on/off/reconnect, USB modes (MTP/ECM), SSH.

### Phase 4 — Service daemon, media, update, reports
  - `service-daemon` (service.py, maintenance.py), `media` + `y2-media` (SD admission, F49 background verify,

repair, write windows), `internal-media`, `update` (check/stage/apply/cancel/rollback; works with the C `y2-update-core`), `report` (scrubber, save, send via curl, schedule), `export-diagnostics`, `export-state`, `firmware` (radiofw), `collect`, `reset`.
  - Device checks: SD insert/remove/repair/large card, Internal Storage setup on a wiped data image (owner decides),

a full OTA update + rollback, report save and send, firmware import from system.img.

### Phase 5 — Power daemon (last, most sensitive)
  - `power-daemon`, `sleep request/prepare`, product sleep, sleep diagnostics, power journal, suspend record,

battery/SOC (F36, F54, F55), charger state (F38, F42, F46), maintenance wakes, `shutdown` coordinator (F39/F50 watchdog, long-press reset, per-step pmsg trail), `y2-power-audit`, `product-sleep.py`, `suspend-record.py`.
  - Device checks: 10 sleep/wake cycles, charger plug/unplug during sleep, low battery to power-off, power off on a

charger (charging screen), update restart, two overnight runs with drain compared to the Phase 0 baseline.

### Phase 6 — Remove Python
  - Done on `main` (2026-10-29): no command hands itself to Python (Python's errors and crashes are reproduced,

`Failure::Crash`; arguments that are not UTF-8 are parsed as `os.fsdecode` reads them); the dispatcher has no Python path (feature, exec and `Failure::Fallback` removed; main.rs's route test requires a route for every subcommand and action); `BR2_PACKAGE_PYTHON3*` removed (the only other Python option, alsa-lib's, is off); post-build links the programme names to `y2-platform` and refuses an image with Python; validators updated. The host keeps `tools/platform` (Python) as the reference of the differential tests until the defects carried 1:1 are fixed after parity (§8); then the reference goes with them. Test build 169 (seq 11140): see §7 and the audit entry "PLATFORM-RUST phases 2–6".
  - Remove the dispatcher fallback, `/usr/lib/y2-platform`, Python scripts, `BR2_PACKAGE_PYTHON3*` from the production

defconfig; confirm with `make … show-depends`/the legal-info manifest that nothing else pulls Python; firmware scan and package validation still pass; image size and RAM measured (§7).
  - Host tests: the differential harness has no Python side any more; convert the remaining white-box Python tests

that only tested internals into Rust unit tests, keep black-box tests (they drive the Rust binary via `--root`).
  - Device: full qualification as for a release candidate (AGENTS.md), then the owner decides on publishing.

## 5a. Remaining port groups (from 2026-10-28, owner: "continue till all phases are done")

Phases 2–5 are carried out as eight groups that can be ported side by side, each in its own module `platform/crates/y2-platform/src/commands/<group>/` (with its own `route`, already chained in `commands/mod.rs`) and its own differential cases `tests/platform_cases/<group>.py` (`CASES`, `fixture(root)`), so they never edit the same lines. Device checks follow per test build; power and sleep keep their overnight gates.``````````````````````````````````````````````````````````````````````````````````

| Group | Subcommands / programs | Python |
| --- | --- | --- |
| observation | status (all sections, --reborn, --pss, --pid, --interval), health, boot-evidence, network-check, collect, bench-storage, bench-library | observe, health, boot (capture_previous), boot_retained, network_check, collect, bench, workload |
| connectivity | connectivity-daemon, wifi-power-policy, bluetooth-power | connectivity, network (rest), radio_policy.wifi_policy, bt_control, bluetooth |
| devices | ssh-daemon, usb-mode, transfer, codec-settings, time-set, time-bootstrap, rtc-alarm | ssh, usb, transfer, codec_controls, timekeeping (rest) |
| storage | media (all actions), internal-media, space, /usr/sbin/y2-media | media, internal_media, space |
| service | service-daemon, update (all actions), firmware | service, update, radiofw |
| reports | report (all actions), export-diagnostics, export-state, reset | report, diagnostics, diagnostic_fields, maintenance |
| power | power-daemon, shutdown | power, battery, charger_state, power_journal |
| suspend | sleep request, sleep prepare, product-sleep.py, suspend-record.py, y2-suspend-record, y2-power-audit, y2-status, y2-health, y2-power-command | sleep, product_sleep, sleep_diagnostics, suspend_record, the scripts |

Rules for every group (the phase 2 part 1 code is the pattern: `commands/*.rs`, `reply.rs`, `y2p-core`):
  - Port 1:1, including every F-number comment and the CONTRACT.md defects (marked `// DEFECT (CONTRACT.md): …`).

The contract inventory (`platform/contract.json`, the group's entries) lists paths, locks, timeouts, subprocesses and trail lines to keep.
  - (Until the refactor, test build 171, which replaced it by `src/cli.rs`.) The dispatcher parses every command line

as main.py's argparse parser does (`src/argparse.rs`, the parser as data in `src/argparse.json` from tools/development/platform-argparse.py; tests/test_platform_argparse.py compares a corpus of ~5 700 argument lists with Python 3.15's parser): it prints `--help` and argument errors itself, and a group's `route` sees only the canonical form of a parsed command: the subcommand, the positionals given, then the optionals given in definition order with full names (`status --reborn --pss` is `status --pss --reborn`, `--opt=v` is `--opt v`, a repeated option once with its last value, an append option once per value, ints as `str(int())`, floats as `repr(float())`). Forms no route takes still go to Python with the arguments as given.
  - A command may hand itself to Python (`Failure::Fallback`) only before it changed anything Python would not

change the same way again. Daemons never fall back.
  - Python inside the platform's own work goes in its port: the DNS probe (`network.probe_dns` runs `python3 -c

getaddrinfo`) becomes an in-process lookup on a bounded worker thread on the real root, while below a fixture root it still records Python's argv as a fixture command so the harness compares; report uploads (urllib) go through `curl` with the same request (no redirects, no proxy, the same timeouts and headers).
  - Daemons: the loop body is testable as one tick; below a fixture root `Y2_DAEMON_TICKS=n` ends the loop after

n iterations (exit 0), and the case's `Y2_LAUNCHER_PATCH` stops the Python daemon at the same point.
  - Every command, action and programme of the group gets differential cases (success, refusal, error, fallback;

`ported` True/False); `tests.test_platform_differential` must pass with `Y2_PLATFORM_RUST` set.
  - Edit only the group's files; a helper several groups need goes into `y2p-core` in a new file

`src/<group>_<name>.rs`. Python under `tools/platform` stays the unchanged reference until phase 6.

## 6. Risks and how to handle them````````

| Risk | Handling |
| --- | --- |
| Re-introducing fixed bugs (sleep, battery, charging, updates) | F-comments ported with code; differential tests; power last; overnight gates |
| A field or reason string changes and Reborn/report tooling misreads it | y2p-contract shared with Reborn; golden JSON fixtures from the Python side |
| Python daemon and Rust CLI race on shared files | same flock paths and write order; a test that runs both concurrently on one tree |
| Faster code exposes timing races (things that relied on 0.5 s startups) | watch for it in device checks; the F39 shutdown and F47/F48 sleep paths are timing-sensitive |
| Update/recovery breakage | Phase 4 tests full OTA + rollback on the player before publishing; the recovery image is C/shell and not touched |
| Slower debugging (no copying a .py onto the player) | keep --root, verbose logging and the trail lines; host builds for quick repro |
| Binary size | one multicall binary, opt-level = "s", LTO, curl subprocess instead of TLS crates |

## 7. Success criteria (fill in Phase 0 and Phase 6)``````````````

| Metric | Phase 0 (Python) | Target | Phase 6 (Rust) |
| --- | --- | --- | --- |
| Platform RSS (all daemons) | 58.4 MB RSS, 35.0 MB PSS (power 12.5, service 19.8, connectivity 14.9, ssh 11.2 MB RSS) | < 15 MB | 15.2 MB RSS, 4.6 MB PSS (power 4.2, service 4.2, connectivity 3.4, ssh 3.3 MB RSS; 169) |
| Platform CPU, 1 h awake idle | ≈92 s/h (2.5 % of the one online core; power-daemon 60, service 24, ssh 7, connectivity 1) | ≥ 5× less | 19.6 s/h, 4.7× less, with Wi-Fi on (power 9.1, service 8.1, ssh 2.4, connectivity 0.2; 612 s on 169) |
| Platform CPU, playing | ≈109 s/h (power 62, service 38; Wi-Fi on in this window) | ≥ 5× less |  |
| y2-platform status --reborn --pss latency | 1.49 s wall, 1.37 s CPU (a Reborn refresh with capabilities and report status: ≈3.0 s CPU) | < 50 ms | 0.48 s wall, 0.32 s CPU, nearly all in Reborn's rebornctl metrics --json (≈0.36 s CPU on its own); capabilities 16 ms, report status 14 ms |
| Root image size | 130 MB tree, Python 21.3 MB (stdlib 16.1, libpython 5.1) + platform 0.7 MB | −22 MB or more | 111 MB tree (−19 MB; the binary is part of it); OTA root 50.3 MB instead of 56.5 MB |
| Awake idle current | not measurable on the charger (no current_now; the player only runs unplugged when asleep) | lower |  |
| Overnight drain | ≈2 mA (161, estimate); 165 overnight owed (owner unplugs) | not worse | owed (owner, two nights on 169) |
| Host tests / container suite | host 967 tests OK (2 skips incl. the Rust comparison); container not run | green | host suite OK; release build 169's container suite, package and first-install validation, ELF and installed-ARM checks pass |

### Phase 0 measurements (owner's player, test build 165, 2026-10-28)

On the USB charger, screen off, one CPU online. Per-process `utime+stime` and RSS/PSS from `/proc` every 60 s (`/data/logs/phase0/{idle,play}.log` on the player). The owner stopped the idle run early: awake idle 551 s (uptime 2759–3310 s, Wi-Fi off, Bluetooth off); its rates equal the since-boot averages (power-daemon 54.9 s in 55 min). Playing 614 s (MP3 320k, 10-band EQ + limiter, wired headphones, Wi-Fi on and online). Python platform vs the rest, CPU seconds per hour:

| Process | Idle s/h | Playing s/h | RSS MB | PSS MB |
| --- | --- | --- | --- | --- |
| power-daemon (Python) | 59.9 | 62.2 | 12.5 | 7.4 |
| service-daemon (Python) | 23.5 | 37.6 | 19.8 | 13.1 |
| ssh-daemon (Python) | 7.2 | 7.4 | 11.2 | 6.3 |
| connectivity-daemon (Python) | 1.3 | 1.4 | 14.9 | 8.2 |
| platform total | 91.8 | 108.6 | 58.4 | 35.0 |
| reborn | 43.5 | 744 (20.7 % CPU) | 26.9 / 33.7 | 24.7 / 31.0 |
| everything else (observer, dbus, bluetoothd, wpa, bluealsa, bt-reconnect, umtprd) | 6.2 | 7.4 | 24.3 | 10.8 |

System busy: 3.0 % idle, 6.9 % playing. With the screen off Reborn does not poll the platform, so these are the daemons' own loops; every platform screen Reborn shows adds ≈3 s CPU per refresh (below).

CLI latency (10 runs each, median wall / CPU, while nothing else ran). Read-only commands for real; state-changing ones only as a floor (`<command> --help`, and `import` of the module):``````````````````````````````

| Call | Wall | CPU |
| --- | --- | --- |
| python3 -I -c pass | 0.152 | 0.150 |
| status --reborn --pss (Reborn refresh) | 1.492 | 1.366 |
| capabilities (Reborn refresh) | 0.547 | 0.540 |
| report status (Reborn refresh) | 1.007 | 0.993 |
| health | 1.617 | 1.500 |
| status wifi | 1.584 | 1.476 |
| update status | 0.871 | 0.867 |
| media status / internal-media status / firmware status | 0.719 / 0.599 / 0.566 | ≈ wall |
| sleep status / time / codec-runtime | 0.564 / 0.572 / 0.541 | ≈ wall |
| floor for any state-changing call (--help) | ≈0.84 | ≈0.83 |
| import cli / update / report / maintenance / network | 0.43 / 0.77 / 0.84 / 0.81 / 0.47 | ≈ wall |

`status` itself starts 4 helpers per call (`/bin/cat /sys/power/wakeup_count`, `y2-bt-observe`, `ip -4 -o …`, `rebornctl metrics --json`); importing `report.py` alone costs 0.84 s, so `report status` is 1 s for a few file reads. The shell-called hot paths pay ≥0.54 s each: `boot-stage` (0.84 floor, twice per shutdown and three times per boot), `time-remember`, `wifi-event`/`dhcp-event`/`ntp-event`.

Boot stages (both are first boots after an update, 165's and 8.43's, and agree within 0.1 s; pmsg trail): `rc S03y2-platform` 12.09 s → `platform_start` 12.50 → `services_started` 27.74 → `application_ready` 48.61. A plain restart (measured on 166, whose dispatcher still runs all of this in Python, so the same baseline): `platform_start` 8.72 → `services_started` 23.75 → `application_ready` 44.44 s; shutdown of the previous boot `shutdown_pending` 4042.50 → `shutdown_complete` 4044.53 (2.03 s). Earlier boots keep no stage times (`boot.json` history has none).

## 8. After Phase 6
  - Fix the defects carried 1:1 (CONTRACT.md list, plus any found during the port), each as its own change with a

test and, where the hardware is involved, a device check.

## 9. Out of scope / later
  - Host tooling in Python (release, build, validation, report fetch) stays.
  - Plugin system (separate plan): the Rust platform makes a shared plugin SDK possible.
  - Contract version changes (`platform_api_version` 2) only after parity is reached.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
