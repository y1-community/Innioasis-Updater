---
title: "Handoff for 2026-10-02 — documentation and repository catch-up - Innioasis Updater"
description: "Handoff for 2026-10-02 — documentation and repository catch-up <!-- knowledge-base-scope: scoped-validation-record -- Working note, written 2026-10-01 evening. Tomorrow's"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-handoff-2026-10-02.html"
---

# Handoff for 2026-10-02 — documentation and repository catch-up - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Handoff for 2026-10-02 — documentation and repository catch-up

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Handoff for 2026-10-02 — documentation and repository catch-up > **Working note, written 2026-10-01 evening.** Tomorrow's job: bring the > documentation up to what is on the device, then bring the remote repositories > up to the local work. No code changes are pending; both working trees are > clean. 

## Where things stand

The device runs storage ceiling candidate 2:
  - Kernel `6.18.0-y2linux-storage-ceiling-02`, root `2025.02.18-platform-v1.12`.
  - Linux `4db6d6de`, Reborn `b92d312c`.
  - Package `out/y2linux-storage-ceiling-02-candidate/`: BOOTIMG `5c17f744…`, Y2ROOT `dc611011…`.

Quick device check on candidate 2, 2026-10-01, read-only 128 MiB direct reads:

| Host | Result |
| --- | --- |
| eMMC | HS200, 8-bit, 200 MHz, 1.8 V, tuning and readback pass. ~140 MB/s read. 0 CRC/timeout events, 0 fallbacks |
| SD (SD128 119 GiB UHS-I SDXC) | Boots at SDR104, 200 MHz, 1.8 V; tuning and readback pass, mounted. Under the first sustained read: 2 CRC errors, then automatic fallback SDR104 → DDR50 with card re-init and readback pass. ~40 MB/s at DDR50. No I/O errors reached the filesystem |

Candidate 1 booted earlier the same day. eMMC was fine, but SD never initialised: the PWRAP gate refused the VMC/VMCH writes. Commit `61a353b` fixed it.

## 1. Documentation to update

The candidate 2 section of [Y2-STORAGE-CEILING.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-STORAGE-CEILING.md) still says SD at the ceiling is "not yet observed". Update:
  - `docs/validation/Y2-STORAGE-CEILING.md`: add the candidate 2 device

result above. SDR104 negotiates but is not stable on this card/board under load. The fallback ladder worked as designed. Restate the per-host answers: - eMMC HS200: observed working. - SD 1.8 V UHS: observed working. - SD SDR104: negotiates, but CRC errors under load. - DDR50: observed stable in a short read.
  - `docs/CURRENT_PLATFORM_STATE.md`:
    - Candidate 2 is now the installed pair, not just "the candidate to flash".
    - Add the storage observations.
    - Decide whether this update also refreshes the "Latest physically observed

identity" table, which still shows Fix02. A full physical qualification was not run, so record this as a quick storage check only.

  - `docs/knowledge/candidate-index.md`: mark candidate 2 as

owner-flashed and booted, with the storage quick-check result.
  - `docs/validation/Y2-HARDWARE-FINAL-CAPABILITIES.md` (capability

ledger): eMMC/SD rows still describe 50 MHz. Add the new ceilings and the observed state.
  - `tools/platform/capabilities.json`: decide whether SD `ceiling` text

should say SDR104 is unstable on the tested card. Qualification flags stay `false`.
  - `docs/architecture/platform-storage-v1.md`: mention the

`y2_storage` status record, the `y2.emmc_mode`/`y2.sd_mode` boot controls and the fallback ladder.
  - Reborn docs:
    - Diagnostics → Storage now shows mode, card, tuning and fault lines (Reborn

`b92d312`).
    - Check `../Y2Reborn/docs/CURRENT_REBORN_STATE.md` and the platform boundary

doc for the new `storage.controllers[].mode` field.

  -  Run `python3 tools/development/check-docs.py` (both repos) and update

catalog counts for any new page.

## 2. Repository catch-up

Nothing has been pushed. Both `main` branches are ahead of `origin/main`:``````````

| Repo | Ahead | Includes |
| --- | --- | --- |
| Y2Linux | 42 commits | CPU Final Fix03, Product UI v2 platform changes, storage ceiling fe8d10a…5401943, this handoff |
| Y2Reborn | 7 commits | Product UI v2 (94e79d8…bd8436d), Diagnostics storage mode b92d312 |

  -  Review `git log origin/main..main` in both repos, then push once the

docs above are committed. Pushing is the owner's decision; nothing was pushed automatically.
  -  Optional cleanup: many build worktrees under `out/*-worktrees/` and

prunable ones under `/tmp/y2linux-*` (`git worktree prune` removes the prunable ones). Keep `out/storage-ceiling-worktrees/` until candidate 2 is accepted.

## 3. Open technical decision (not documentation)

SDR104 hits CRC errors under sustained reads. Every boot starts at SDR104 and falls back on the first load. Options:
  - Try the stock 1.8 V pad drive. LK leaves the SD pads at 1/1/1; the

driver's 1.8 V table is 4/4/4. Check whether the drive write took effect, or test stronger values.
  - Extend tuning (data-path delay), then re-test.
  - Or set the SD ceiling to DDR50/SDR50 (`y2.sd_mode=` or the default ladder)

so it never starts with errors. Throughput is about the same, ~40–50 MB/s.

## Known unrelated notes
  - `tests/test_baseline.py` fails locally on a clean tree too. It predates the

connectivity PMIC fields and is not in the production suite.
  - `test_hardware_final_contract`, `test_dev_*`, `test_bootimg` need

`pyelftools` and only run in the build container (`tools/production/tests.sh`).
  - The Y2Linux repo forbids model attribution in commits. Reborn has no local

git identity configured; commit with `git -c user.name=Luca -c user.email=116190857+SchulzCode@users.noreply.github.com`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
