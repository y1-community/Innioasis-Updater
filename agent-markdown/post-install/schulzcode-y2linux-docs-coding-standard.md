---
title: "Coding standard: Y2Linux platform and Y2Reborn - Innioasis Updater"
description: "Coding standard: Y2Linux platform and Y2Reborn Production code only. This is how the platform platform/crates and Reborn ../Y2Reborn are written since Beta 9.1; every rul"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-coding-standard.html"
---

# Coding standard: Y2Linux platform and Y2Reborn - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Coding standard: Y2Linux platform and Y2Reborn

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Coding standard: Y2Linux platform and Y2Reborn

Production code only. This is how the platform (`platform/crates`) and Reborn (`../Y2Reborn`) are written since Beta 9.1; every rule below is already true of the code, and the gate keeps it so. New code meets it from its first commit; old code that does not is listed in the ratchet's baseline and only ever gets better.

## 1. What the gate enforces

`tools/development/platform-gate.sh` must print `GATE OK` before any commit (Reborn work included: the gate builds Reborn's contract test and measures Reborn's code). It runs:````````````

| Check | Rule |
| --- | --- |
| cargo fmt | formatted; and rustfmt must be able to format it (see long lines below) |
| cargo clippy --all-targets | no warning |
| cargo check --target armv7-unknown-linux-gnueabihf | builds for the player |
| tools/development/code-quality.py | the ratchet (section 2) |
| cargo test and the golden suites | no failure; every recorded answer of every command unchanged unless re-recorded on purpose |
| tools/development/record-compat.py | an older build can still read every /data record this one writes |
| Reborn contract test | Reborn reads every recorded platform answer as before |

Reborn on its own: `cargo fmt --all`, `cargo clippy --workspace --all-targets` (no warning), `cargo test --workspace` (no failure), then the gate.

## 2. The ratchet (`code-quality.py`)

Measured on production code (tests excluded) against `tools/development/code-quality-baseline.json`. Nothing may get worse; an improvement is recorded with `--update` and its baseline diff is part of the commit.

The length limits are ceilings, not targets (owner, 2026-10-31): a function or file between the aim and the ceiling passes, so a small fix never has to start with a refactor. Split code when it reads better, not to win a line back.````````````````````````````

| Measure | Limit for new code | Existing exceptions |
| --- | --- | --- |
| Function length | aim for ≤ 100 lines; the gate stops at 150 | over 150: listed; may only shrink |
| File length | aim for ≤ 1000 lines; the gate stops at 1500 | over 1500: listed; may only shrink |
| unsafe | only in the crates that have it today, never more | per crate |
| .unwrap() / .expect( | none in production paths (an invariant gets expect("why it holds")) | per crate |
| panic! / todo! / unimplemented! / unreachable! | none | per crate |
| #[allow(…)] | none without a comment why | per crate |
| Raw JSON field lookups ["field"] | none: read records in their types | per file |
| Code lines over 100 columns | none (rustfmt gives up on a function containing one) | per file |
| TODO / FIXME / XXX / HACK | none, ever | — |

## 3. Shape of the code

Functions do one thing and are named for it. A long sequence becomes named steps, not comments:
  - A loop with state is a struct holding that state and a `pass` calling one method per step; an early end of

a pass is a `ControlFlow` value, never a `continue` hidden in a helper. Examples: `MainLoop::pass` (`app/reborn/src/main_loop.rs`), `SinkWorker::pass` (`app/reborn/src/playback/output.rs`), the Bluetooth `Session` (`crates/reborn-platform/src/bluetooth/worker.rs`).
  - A thread is a worker struct owning what it uses, spawned as `move || worker.run()`; no 500-line closures.

Examples: `DecodeWorker`, `SinkWorker`, `BluetoothWorker`, `Watchdog`.
  - A dispatcher is an exhaustive `match` with one line per case, delegating to a method named for it; the

compiler then names every case a new variant leaves unhandled. Example: `Runtime::effect_inner` with `runtime/effects/*.rs`. Never `_ =>` over an enum we own.
  - One definition per fact. A second copy of a dispatch, a runner or a record type is a bug waiting (the

skin path's screen dispatch had lost Music; the bench runner had its own copy of the command runner).

Modules are named for what they do (`playback/decode.rs`, `runtime/sleep.rs`), tests live next to them in `*_tests.rs` or a `tests/` module, and a file's first line (`//!`) says what it is for.

## 4. Records and the platform contract
  - Every record that crosses the platform/Reborn boundary is a type in `y2p-contract` (edited in Y2Linux only,

copied with `release.py sync-contract`). The platform writes it, Reborn reads it; neither looks up JSON fields. No device paths in the contract (Reborn's architecture guard).
  - Read leniently where another version may have written the record (`lenient::*`: a field of another type

reads as absent), strictly where this build is the only writer.
  - /data stays rollback-safe: keep field names and types an earlier build wrote; new fields are fine.
  - The critical path fails closed with one reason (sleep, update, reset): an unreadable record refuses with a

single named reason and starts fresh next time.
  - An answer whose shape changes re-records its goldens and Reborn's contract in the same change, reviewed.

## 5. Errors, `unsafe`, panics
  - Errors are values with a reason the owner or Reborn can act on (`Failure`, `Result<_, String>` with a stable

reason text). No `unwrap` on input from disk, the kernel, D-Bus or the network.
  - `unsafe` lives behind safe wrappers in `y2p-core::sys` (platform) and in the FFI crates (Reborn: media, audio,

graphics, platform native code). Every block has a `// SAFETY:` comment saying why it holds. A new wrapper is preferred to a new block (`sys::pipe`, `sys::signal_note`).
  - A panic is a bug. Reborn's panic hook records one in its log and error report; the code is written so that

none can happen.

## 6. Comments and documentation
  - Comments say why (the report, measurement or hardware behaviour behind a decision), not what the next line

does. Name the evidence: a report id, a test build, a ledger entry.
  - Open work goes into `docs/planning/`, not into the code.
  - A release has an owner-readable report in `docs/validation/` and the state documents are updated with it.

## 7. Changing code
  - Behaviour and structure change in separate commits. A pure move (split, extract, rename) is made

mechanically and verified by comparing the moved text with the original token for token; a behaviour change comes with a test that fails without it.
  - Every fix gets a test. A refactor keeps the test count; a renamed test is named in the commit.
  - Commit messages say what changed and why, in plain words; commit only after `GATE OK`, under the owner's

identity, without attribution lines.
  - Nothing is pushed, tagged or published without the owner's word.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
