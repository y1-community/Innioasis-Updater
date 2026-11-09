---
title: "Platform Rust port — handoff (2026-10-29, updated after test build 170) - Innioasis Updater"
description: "Platform Rust port — handoff 2026-10-29, updated after test build 170 Update 2026-10-29 afternoon: test build 170 is on the owner's player. The ten defects carried 1:1 ar"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-platform-rust-port-handoff.html"
---

# Platform Rust port — handoff (2026-10-29, updated after test build 170) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform Rust port — handoff (2026-10-29, updated after test build 170)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform Rust port — handoff (2026-10-29, updated after test build 170)

Update 2026-10-29 (afternoon): test build 170 is on the owner's player. The ten defects carried 1:1 are fixed (CONTRACT.md table), the Python reference platform (`tools/platform`) is deleted, its ≈630 unit tests are Rust tests (608 Rust tests in all), the differential harness is a golden suite against the Rust binary (`tests/platform_golden.py`, `tests/platform_goldens/`, 1 063 goldens recorded from Python), host tools live in `tools/host/` and `tools/production/`. 170 (sequence 11150) was installed by the **first Rust `update stage`/`apply` on a player** (stage 8.8 s, apply to Acknowledged 86 s, application_ready 37.7 s) and Acknowledged; SFTP opens Internal Storage there (the fixed defect, checked over a real SFTP session). Owed: the owner's hardware checks (§6 A) on 170. Next after them: [PLATFORM-RUST-REFACTOR-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-REFACTOR-PLAN.md). Next free label 171, sequence above 11150. Sections below are from the port's end (build 169) where not updated.

Read this first when you pick the platform port up again. It says where things stand, where everything lives, how to build, test and install, what the owner decided, what is owed, and what we learned. The plan is [PLATFORM-RUST-PORT-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-PORT-PLAN.md), the contract and the accepted differences are in [platform/CONTRACT.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fplatform%2FCONTRACT.md), and the device evidence is in [roadmap-gap-audit.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md) (entries "PLATFORM-RUST phase 1", "phase 2 part 1", "phases 2–6").

## 1. Where it stands
  - All phases (0–6) are implemented. The whole platform (`/usr/sbin/y2-platform`, its four daemons, the sleep

helper and the scripts) is Rust. The image has no Python interpreter or library; post-build refuses one.
  - Test build 169 (label 169, version 1.0.0-beta.8.44, sequence 11140) is installed on the owner's player by

staged OTA and was Acknowledged by the Rust `update health-ack`. Not published.
  - Commits are on `main`, not pushed: Y2Linux `470cbad` (code at `5640949`), Y2Reborn `dc38c55`. No tags, no

GitHub release, no posts. Pushing or publishing needs the owner's explicit word.
  - Git trees are clean; all agent worktrees and branches are removed.
  - Next free label 170, sequence above 11140.

## 2. What the owner decided``````````

| Date | Question | Decision |
| --- | --- | --- |
| 2026-10-28 | Where does the shared contract crate live? | "deem as you think is best" → platform/crates/y2p-contract in Y2Linux (MIT); Y2Reborn vendors a copy stamped Y2LINUX-SOURCE; release.py sync-contract copies it, release.py build refuses a mismatch |
| 2026-10-28 | Fix the defects found in the inventory during the port? | "port 1:1 then fix … so that when the port is finished no more python is in the build and everything is rust" → ported unchanged, marked // DEFECT, fixed after the port (§6) |
| 2026-10-28 | Overnight drain on the Python build first? | Could not be done; the port went ahead without it |
| 2026-10-29 | Scope | "continue till all phases are done and python is removed from the platform"; "i will test that, but i want a full implementation" — the owner runs the hardware tests himself |

## 3. Results on the player (169 against the Python platform on 165/166)````````

| Measure | Python | Rust (169) |
| --- | --- | --- |
| Memory, 4 platform daemons | 58.4 MB RSS / 35.0 MB PSS | 15.2 MB RSS / 4.6 MB PSS |
| Idle CPU, 4 daemons | 91.8 s per hour | 19.6 s per hour (Wi-Fi on) |
| status --reborn --pss (Reborn's call) | 1.49 s | 0.48 s |
| capabilities / report status | 0.55 s / 1.0 s | 16 ms / 14 ms |
| Restart trail (shutdown steps) | 2.57 s | 0.46 s, every step in order |
| Boot to application_ready (plain restart) | 44.4 s | 36.8 s |
| Root file system | 130 MB | 111 MB |

Measured with the idle sampler (600 s window, 11 samples) and the restart/boot trail, as in plan §7. Per daemon on 169: power-daemon 9.1 s/h, service-daemon 8.1 s/h, ssh-daemon 2.4 s/h, connectivity-daemon 0.2 s/h; each 3.3–4.2 MB RSS. Reborn itself (45 s/h, 26.7 MB) is now the largest consumer. On 173 (screen off, charging, 300 s): Reborn 19.0 s/h (main thread 9.4, watchdog 3.4), ~34 process starts/min (≈140 on 172: the Wi-Fi look's wpa_cli/ip are gone), `rebornctl metrics` 0.01 s instead of ≈0.36 s (Reborn's control thread answers it).

## 4. Where everything lives
  - `platform/` — the Cargo workspace (Rust 1.99.0 in `rust-toolchain.toml`, vendored crates in `vendor/`, offline via

`.cargo/config.toml`). Vendored: serde, serde_json, libc, ryu, regex, flate2, tar, sha2, hmac. SQLite is loaded at run time (`libsqlite3.so.0`, `y2p_core::reports_sqlite`); keep `BR2_PACKAGE_SQLITE`. - `crates/y2p-core` — shared helpers: fixture root (`Root`, glob/fnmatch), Python-identical JSON (`json.rs`, float repr via ryu, ordered objects, `atomic_json`), records, locks, clocks, subprocesses (`command.rs`), Python value rules (`py.rs`), OSError texts and `os.fsdecode` (`os_text.rs`), `wide()` for the 32-bit ARM `time_t`/`c_long`, plus one support file per group (`power_*.rs`, `storage_media.rs`, `suspend_text.rs`, …). - `crates/y2p-contract` — schema names and constants shared with Reborn, with `tests/golden`. - `crates/y2-platform` — the binary. `main.rs` (argv[0] multicall via `commands::suspend::program`, hidden programmes, the parser, route; an unrouted command line exits 127), `cli.rs` (the argument table and parser since the refactor; `argparse.rs`/`argparse.json` until 170), `reply.rs` (`Failure`), `commands/*.rs` and `commands/<group>/` for observation, connectivity, devices, storage, service (update, firmware, service-daemon), reports, power, suspend.
  - `platform/CONTRACT.md` + `platform/contract.json` — the contract inventory (106 entries), callers, locks, the

accepted differences, the defect list.
  - `tools/platform/` — deleted 2026-10-29 (the former Python reference; the goldens and recordings were made

from it). Host tools that lived beside it: `tools/host/` (transfer, diagnostics, qualify, sftp_check, audio_precision) and `tools/production/codec_manifest.py`; `platform/capabilities.json`.
  - Tests: `tests/platform_golden.py` (harness), goldens in `tests/platform_goldens/`, cases in

`tests/test_platform_differential.py` and `tests/platform_cases/<group>.py`, and `tests/test_platform_{argparse,devices,power_rpc,observation,suspend,reports}.py`, all in `tools/production/tests.sh` (platform/CONTRACT.md "Golden suite").
  - Tools: `tools/development/platform-contract.py --check|--write` (contract.json against `y2-platform

__arguments`, cli.rs's table),`platform-goldens.py [--check]`(y2p-contract goldens),`platform-raw-goldens.py` (the golden cases with key order and spacing, for a byte comparison of two builds), `host-tests.sh`.
  - Packaging: `buildroot/package/y2-platform/` (version = git tree hash of `HEAD:platform`, so every change rebuilds),

`buildroot/configs/y2_production_defconfig` (no `PYTHON3*`), `buildroot/board/y2/post-build-production.sh` (links `y2-status`, `y2-health`, `y2-suspend-record`, `y2-power-audit`, `/sbin/poweroff`, `/sbin/reboot` to y2-platform; fails if Python is present), `tools/production/validate.py`, `composition.py`, `check_installed_arm.py` (runs the ARM binary under qemu on a fixture root).
  - Y2Reborn: `crates/y2p-contract` (stamped copy), `reborn-platform` uses its schema constants.

## 5. How to build, test and install

Host check (≈1 min; builds the host binary, type-checks for armv7, runs the release-gate modules with the Rust comparison on):`tools/development/host-tests.sh`

Only the platform:`cd platform && cargo test --offline --locked && cargo clippy --offline --locked cd platform && cargo check --offline --locked --target armv7-unknown-linux-gnueabihf Y2_PLATFORM_RUST=$PWD/platform/target/debug/y2-platform python3 -m unittest tests.test_platform_differential tools/development/host-tests.sh tests.test_platform_differential tests.test_platform_argparse … # only these`

Harness environment contract: `Y2_ROOT` (fixture root), `Y2_FIXTURE_COMMANDS` (subprocess answers), `Y2_FIXTURE_CALLS` (recorded requests), `Y2_DAEMON_TICKS` (bounded daemon loops), `Y2_FIXTURE_TOKEN` (update staging token), `Y2_PLATFORM_RUST` (the host build the goldens are checked against; skipped without it), `Y2_RECORD_GOLDENS=1` (re-record the goldens that differ), `Y2_ARGPARSE_ECHO` (prints the parse, only below a fixture root).

After changing Y2Linux's contract crate: `python3 tools/production/release.py sync-contract`, then commit Reborn (with the identity env vars, see §8).

Test build (do not touch the Y2Linux tree while it runs):`Y2_STOCK_PACKAGE=$PWD/donorSource/y2_v3.2.0_FM-20260813 python3 tools/production/release.py build --label 170`

Add `--clean` after enabling/disabling a Buildroot package (a disabled package stays in the target otherwise). Output: `out/release-170/{ota,update,first-install,assets,receipts,summary.json}`.

Install on the player (staged OTA only; player at `10.42.0.1` over USB networking):`Y2="ssh -F /dev/null -o HostKeyAlias=y2linux-production-v1 -o BatchMode=yes -i ~/.ssh/y2linux_ed25519 root@10.42.0.1" $Y2 'rm -rf /data/updates/owner-169; mkdir -p /data/updates/owner-170' scp -F /dev/null -o HostKeyAlias=y2linux-production-v1 -i ~/.ssh/y2linux_ed25519 -q out/release-170/ota/* root@10.42.0.1:/data/updates/owner-170/ $Y2 'y2-platform update stage --package /data/updates/owner-170; y2-platform update apply'`

After the restart: `y2-platform update status` must show Acknowledged; check the supervisor logs are empty and `ps` shows `/usr/sbin/y2-platform <name>-daemon` for the four daemons.

## 6. What is owed

A. The owner's hardware tests (now on 170) (sleep, battery and charging are now Rust, so these matter most):
  - Several sleep/wake cycles, then two overnight runs off the charger — the drain comparison (Python reference:

Beta 6.3 ≈7.8 mA, Beta 1 ≈9.4 mA; read the power journal afterwards).
  - Low battery all the way to power-off.
  - Charger plug/unplug, awake and asleep; power off on a charger (must open the charging screen, F46).
  - SD card insert, remove and Repair; Internal Storage; copying over MTP; SSH/SFTP.
  - An OTA from 170 to the next build, and a rollback (169 → 170 by OTA worked).
  - Save and send an error report (upload now goes through `curl`).
  - Wi-Fi join and a wrong password; Bluetooth headphones.

B. DONE 2026-10-29: the defects carried 1:1 are fixed, each with a test and the goldens re-recorded (CONTRACT.md has the fix per row; the table below is the original list, its line numbers are gone).``````````````````````````````````````````````````````

| Defect | Where |
| --- | --- |
| SFTP never roots at Internal Storage: usr/libexec/sftp-server greps "state": "Ready" but the record is compact ("state":"Ready") — confirmed on the player | the script, not Rust |
| media status exits 1 for a Degraded card; media write exits 0 with failure for not_mounted | commands/storage/mod.rs:213 |
| A second update check/stage meeting the busy .stage.lock overwrites download.json with Failed [Errno 11] while the first download continues | commands/service/update.rs:769 |
| update rollback asks the core before the battery gate: a battery refusal leaves the journal RollbackPending | commands/service/update.rs:1265 |
| update auto-check prints null when nothing was due | commands/service/update.rs:1548 |
| firmware scan exits 0 with install errors | commands/service/radiofw.rs:761 |
| Battery: after a sample with BAT0 capacity and then one without, ui is None (found during the port) | commands/power/battery.rs:318 |
| An expired media write window is re-protected only when a reconcile runs, which is skipped when nothing changed | storage reconcile; device check owed |
| A DHCP renew deletes dns.json: Wi-Fi may show dns_unavailable for up to 300 s | connectivity, dhcp-event |

Callers rely on some of these exit codes (Reborn, scripts): check every caller (CONTRACT.md "Callers") before changing one.

C. After the fixes: plan §9 for later work (plugin SDK, `platform_api_version` 2). The host tests no longer use the Python reference (`tools/platform`): the goldens were recorded from it.

D. Smaller follow-ups:
  - `status --reborn --pss` now spends most of its time in Reborn's `rebornctl metrics --json` (≈0.36 s CPU): the

next speed-up is on Reborn's side.
  - Done: the product-sleep cases that failed when the host was busy shared `/dev/null` as the helper's inherited

lock (any other process's flock on it refused the sleep); each case now has its own lock file.
  - Before publishing: a release (bump, build, docs, `release.py publish`) only on the owner's word; the release notes

should say the platform is Rust and Python is gone (smaller image, lower idle CPU).

## 7. Lessons from the port
  - Compile for the player, not only the host. The agents built only for x86-64; build 169's first try failed on

32-bit ARM. Use the 64-bit file calls (`stat64`, `fstat64`, `fstatat64`, `statvfs64`, `fstatvfs64`, `open64`, `pread64`, `pwrite64`, `off64_t`): the plain ones fail with EOVERFLOW above 2 GiB. `time_t` and `c_long` are 32 bits there; use `y2p_core::wide()`. `host-tests.sh` now type-checks armv7.
  - Package version must change with the code. Build 167 shipped the old binary because the Buildroot version was

fixed; it is now the `HEAD:platform` tree hash, and `release.py` prunes old `y2-platform-*` build dirs.
  - The build container (musl) cannot run host binaries: neither the build's host `python3.15` nor the project's

glibc debug `y2-platform`; tools treat a binary that does not run as absent (platform-contract.py, build 171).
  - Python's float repr needs `ryu` (Rust's `{:e}` picks other shortest digits); checked on 20 000 random floats.
  - Fixtures per group (`CASE_GROUP`), goldens regenerated from the base root, or groups collide (storage vs

observation SD card).
  - Arguments reach routes in canonical form (subcommand, positionals, then given options in definition order,

full names): Reborn's `status --reborn --pss` arrives as `status --pss --reborn`.
  - Where Python would crash, Rust ends the same way (`Failure::Crash`: traceback on stderr, exit 1, after the same

file changes) instead of guessing a nicer answer — fix such paths deliberately later, not by accident.
  - `pkill -f <pattern>` matched my own shell; match on argv. A test writer into a pipe needs its own thread.
  - `validate.py`'s tar/ext4 agreement check must name a regular file (`usr/sbin/y2-platform`), not a link.

## 8. Rules that still apply
  - Git: Y2Linux has the identity configured; Y2Reborn has none — commit there with

`GIT_AUTHOR_NAME=Luca GIT_AUTHOR_EMAIL=116190857+SchulzCode@users.noreply.github.com GIT_COMMITTER_NAME=Luca GIT_COMMITTER_EMAIL=116190857+SchulzCode@users.noreply.github.com`. Never change git config, never add model attribution or Co-Authored-By, never use `git stash`.
  - Commit locally in focused commits. No push, tag, `release.py publish` or GitHub post without the owner's word.
  - Install test builds only by staged OTA. Ask the owner before anything that powers the player off or needs button

presses. Never run the capture tool without `head` (it streams forever).
  - F-numbers (F36, F46, F53, …) are explained in the private `UserReports/REVIEWED.md`.
  - Before closing this milestone or publishing, repeat the roadmap/gap audit with the hardware results (AGENTS.md).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
