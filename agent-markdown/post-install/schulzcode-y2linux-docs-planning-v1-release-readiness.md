---
title: "Y2Linux / Y2Reborn 1.0 release readiness audit — 2026-10-17 (code reviews completed 2026-10-18) - Innioasis Updater"
description: "Y2Linux / Y2Reborn 1.0 release readiness audit — 2026-10-17 code reviews completed 2026-10-18 2026-10-18: the six area code reviews are done; see V1-CODE-REVIEW V1-CODE-R"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-v1-release-readiness.html"
---

# Y2Linux / Y2Reborn 1.0 release readiness audit — 2026-10-17 (code reviews completed 2026-10-18) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux / Y2Reborn 1.0 release readiness audit — 2026-10-17 (code reviews completed 2026-10-18)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux / Y2Reborn 1.0 release readiness audit — 2026-10-17 (code reviews completed 2026-10-18)

2026-10-18: the six area code reviews are done; see [V1-CODE-REVIEW](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FV1-CODE-REVIEW.md). They add one more blocker, A19 below: one undecodable song makes every OTA roll back after 180 s (host-reproduced).

Beta 8.0 (2026-10-18) fixed A3, A4 (documented; hashes stay strict), A5, A7, A12, A13, A19, A20 ([report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.0.md)). A6 waits for the 1.0 label itself. Still open: A1, A2, A8–A11 (hardware or other people) and the owner decisions A14, A16, A18; A17 is feature work.

Read-only audit of Y2Linux `main` (e771867, tag `baseline-74`) and Y2Reborn `main` (a0b1a50). Frame: the [standing milestone-boundary rule](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule). Nothing was built, flashed, committed or sent to the player. Status: partial. The session hit its usage limit while six area code reviews (kernel, platform tools, release/update pipeline, Reborn app/platform, Reborn UI/core/library, Reborn native C) were still running; their findings are not in this file. Everything below was verified by hand against code, docs, GitHub and the local release workspace.

## Verdict

Not ready to be called 1.0 yet; close, but with two hard problems and a long list of owed hardware checks. The software and process are in good shape: Reborn passes fmt/clippy/514 tests, the Y2Linux host suite passes 793 tests, the OTA path is signed (Ed25519, sequence anti-rollback), rollback is implemented, public images carry no SSH key or MediaTek firmware, and the GPL source chain is intact. What blocks a 1.0 label is (1) standby battery drain: ≈8–9 mA on the maintainer's unit (6–7× stock) and ≈30–41 mA on the one other unit that has reported (issue #42, a new player, battery dead in about 1.5 days asleep), and (2) the amount of behaviour that has only ever been exercised on the maintainer's player and machine (install from stock, build from source, going back to stock, USB after sleep over many wakes, cable pull during the new DMA receive path, Bluetooth listening checks). Several documentation defects would also mislead a first-time installer (the first-install zip ships an internal historical runbook as `install.md`; readme and BUILDING point at old tags).

## Part A findings

Severity: BLOCKER = fix before 1.0; SHOULD = fix or document clearly before 1.0; LATER = fine after 1.0. HW = needs testing on a real player.``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| ID | Area | Sev. | What is wrong | Evidence | HW | Effort |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Hardware / power | BLOCKER | Sleep drain is 6–7× stock on the maintainer's unit (≈7.8–9.4 mA vs ≈1.3 mA) and ≈30–41 mA on a second, new unit on a pure Beta 1 image; the second unit shows two states (≈11 mA and ≈30 mA) in one boot with identical golden/PMIC rows. No doc tracks #42. A 1.0 music player that empties its battery in 1.5 days in a bag needs either the leak found or a mitigation (e.g. automatic power-off after N h asleep, documented) plus a prominent known issue. | GitHub #42 and its three comments; readme Known issues; docs/validation/Y2-LINUX-1.0-BETA-7.md:39; no hit for "#42" in NEXT-SESSION-HANDOFF.md, CURRENT_PLATFORM_STATE.md, roadmap-gap-audit.md | yes (second unit; captures of panel sleep-in, unclaimed GPIOs, VIO/VA rails) | L |
| A2 | Install by a stranger | BLOCKER | The whole first-install path (SP Flash Tool, first boot, firmware drive) has run on one player and one host; BUILDING.md says the build has never run on a second machine; going back to stock is untested. One of these needs a second person's confirmed run before 1.0. | readme.md:120-122; docs/BUILDING.md:7-8; docs/INSTALL.md "This full restore has not yet been tested" | yes (another owner) | M (coordination) |
| A3 | Docs / install | SHOULD | The first-install zip ships docs/architecture/production-install.md as install.md, a file that opens with "Historical record… Storage04 production candidate… Storage01 sparse transport failed", not the user guide. recovery.md and ota-layout.md in the zip are historical too. | tools/production/package.py:116; out/release-74/first-install/install.md:1-15 | no | S |
| A4 | Install by a stranger | SHOULD | Radio firmware extraction accepts only the exact SHA-256 of the v3.2.0 FM files; any other Innioasis package version fails with firmware_mismatch/not_the_y2_firmware_package. When Innioasis changes its download, new owners cannot get Wi-Fi/Bluetooth. Document the exact version loudly and keep a per-version hash table or accept structurally valid files. | tools/platform/y2_platform/radiofw.py:277-311; docs/INSTALL.md:16 | yes (another firmware version) | M |
| A5 | Docs | SHOULD | readme table says tag baseline-70 (previous baseline-67) for Beta 7.11; the tag is baseline-74. BUILDING.md tells builders to check out baseline-67. | readme.md:18; docs/BUILDING.md:49-50 | no | S |
| A6 | Docs / "Beta" wording | SHOULD | Status lines and conditions written for the beta: readme:9, Reborn readme:8, INSTALL:15 ("1.0 Beta 1 or later"), STORAGE:5 ("Beta 7.9 and later"), release-notes template "Known issues (beta)". Code is ready: release.py bump accepts 1.0.0, pages.rs:1263 short_version renders "1.0". | listed lines; tools/production/release.py:81-82; crates/reborn-ui/src/pages.rs:1261-1275 | no | S |
| A7 | Licensing | SHOULD | Buildroot legal-info saves no source for the Bootlin external toolchain (glibc LGPL, libgcc/libstdc++); manifest.csv lists it as "unknown" with no licence files. The images ship glibc, so the source or a pinned link+hash belongs in the release like the third-party tar does. | out/release-74/assets/…legal-info.tar: legal-info/manifest.csv row toolchain-external-bootlin, legal-info/README warnings | no | S |
| A8 | Hardware / USB | SHOULD | Multi-packet receive DMA is on by default since 7.11 but untested with the cable pulled mid-copy, across sleep/wake, and with Windows Explorer; USB after deep-sleep wake "not yet confirmed over many wakes". | docs/validation/Y2-LINUX-1.0-BETA-7.11.md Known gaps; readme.md:114-116 | yes | S (tests) |
| A9 | Hardware / Bluetooth | SHOULD | AAC with AirPods negotiated but never listening-checked; Beta 2 reconnect fix and Beta 6.1 pause fix await device checks; saved headphones are not reconnected on play; range dropouts at 2–4 m (hardware, stock too). | readme.md:117-120; Reborn readme Known limits; handoff lines 206, 238, 243 | yes | S (tests) |
| A10 | Hardware / jack | SHOULD | No wired-headphone detection; "jack" means "not Bluetooth". Stock uses GPIO16/EINT16 + HP_STATUS (see memory of PR #11 review). Document as a 1.0 limitation or implement. | readme.md:119-120; Y2Reborn PRs #11/#12 open (CONFLICTING / UNKNOWN) | yes | M |
| A11 | Process | SHOULD | 34 "owed" device checks accumulate in the handoff (Last.fm offline send after sleep, thermal zone after a night, Beta 7 UI tour, 7.2 frame rate was measured, radio checks…). A 1.0 needs one consolidated pass with results recorded, not a backlog. | grep -c owed docs/planning/NEXT-SESSION-HANDOFF.md = 34 | yes | M |
| A12 | Docs | SHOULD | docs/release/Y2-COMMUNITY-BETA-FEATURE-AUDIT.md (named as the feature audit) last changed 2026-10-04 and still reads "FEATURE COMPLETION IN PROGRESS", before every public beta; the per-beta rows live only in roadmap-gap-audit.md. Either retire it or add a 1.0 closing row. | section headers lines 3–57, 1050 | no | S |
| A13 | Docs | LATER | check-docs.py: catalog omits docs/planning/LASTFM-SCROBBLE-PLAN.md (1 problem, Y2Linux); Reborn 0 problems. | tool output | no | S |
| A14 | Security | LATER | Production image includes strace, iperf3, memtester, evtest, i2c-tools; kernel has CONFIG_DEBUG_FS=y; bootargs user_debug=31, panic=0 (a kernel panic hangs until a 10 s Power hold; the MT6582 watchdog driver is built but nothing in userspace feeds /dev/watchdog). None is reachable without the owner's SSH key; tidy for 1.0 or accept. | buildroot/configs/y2_production_defconfig:33-99; kernel/config/production.config:137-229; kernel/dts/innioasis-y2.dts:183-185 | no | S |
| A15 | Security / privacy | LATER (accepted) | The Last.fm API key+secret are in the public rootfs.ext4.gz (root-only file, but anyone can extract it). Documented as inherent; rotation plan exists. | buildroot/board/y2/post-build-production.sh:78-80; docs/LASTFM.md; Reborn readme "The app key" | no | — |
| A16 | Licensing / trademarks | LATER | Skin names and looks reference Walkman, Winamp, Zune and iPod-style "Classic/Mini/Nano"; fonts are all OFL with licence files present; icons are original. Consider renaming before a 1.0 that gets wider attention. | skins/*/skin.json; assets/icons/README.md | no | S |
| A17 | Library | LATER | #40 multi-artist tags ("A;B") listed as one artist; #41 Album Artist browsing requested. | GitHub #40, #41 | no | M |
| A19 | Update / library | BLOCKER | One audio file FFmpeg cannot open leaves Reborn's library.error set after every scan; health_ack then never acknowledges and rolls the update back after 180 s. The same accounting stops songs deleted over USB from leaving the library. Code review B3/B4. | Y2Reborn reborn-library/src/lib.rs:1268, main.rs:4219-4227; Y2Linux update.py:571; host repro in V1-CODE-REVIEW | no (fix); yes (one OTA with a broken file) | S |
| A20 | Storage / SD | SHOULD | An SD card whose read-only check outlasts the 7 s media reconcile limit never mounts, and checkers pile up. Code review B5. | service.py:193-194, common.py:62-104 | yes (large card) | S |
| A18 | Contributions | LATER | Open PRs: Y2Linux #43 (Gallery font licences, must merge after Y2Reborn #18); Y2Reborn #11 and #17 CONFLICTING, #12/#13 unknown mergeability. Decide before 1.0 so the licence lines match what ships. | gh pr list both repos | no | S |

### Verified as fine (so nobody re-checks)
  - OTA signing: libsodium Ed25519, private key must live outside the repo in a 0700 directory, 0600 file

(`tools/update/package.py:35-74`); release key `platform-v1-release-20261015` with `minimum_sequence` 3500 and `allow_downgrade: false` (`tools/update/trust.json`); device compares the manifest sequence via `y2-update-core check-manifest` and treats "downgrade/replay" as up to date (`y2_platform/update.py:341-360`); redirects limited to GitHub hosts (`tools/update/channel.json`); TLS waits for a trusted clock and entropy (`update.py:316-318`). Moving from `1.0.0-beta.7.11` to `1.0.0` only needs a higher sequence, which `bump` does.
  - Publish is atomic enough: `gh release create` with assets creates a draft, uploads, then publishes; release.py

then verifies `releases/latest/download/manifest.json` byte-for-byte (`tools/production/release.py:431-436`).
  - Public data image has no SSH key; dropbear binds `10.42.0.1:22` on `usb0`, key-only; root password locked,

no getty (`production-overlay/etc/default/dropbear`; `y2_production_defconfig:17-18`; `validate.py:418-420`).
  - `privacy.py` rejects private keys, Wi-Fi PSKs, Bluetooth link keys, Last.fm session, library DB and history files

in every delivered tree and scans raw ext4 bytes including free blocks.
  - GPL sources: kernel tarball (`linux-6.18.56.tar.xz`) and the 381 MB third-party package tar are linked by name+SHA-256

from `baseline-52`; patches are in the repo at the tag; legal-info tar carries licences, manifests and this project's four packages. AAC really is the stripped `fdk-aac-free` 2.0.3 tarball (`codec-sources.json`, `modernize_buildroot.py:174-199`); aptX is excluded from `--public` builds and checked (`build.py:155-163`, `validate.py:367-379`).
  - `Instant::now() - Duration::from_secs(30)` at boot (main.rs:3689, bluetooth.rs:1273) does not panic on Rust 1.99:

`Timespec::checked_sub_duration` allows negative seconds. Clippy pedantic flags it, but it is safe.

## Known issues for the 1.0 release notes (if accepted rather than fixed)
  - Standby drain ≈8 mA (stock ≈1.3 mA); on some units far higher (#42). Battery percentage is voltage-estimated.
  - No wired-headphone detection; the jack is used whenever no Bluetooth headphones are connected.
  - Bluetooth range is hardware-limited; AAC quality with AirPods not listening-verified.
  - Rare slow display start after a restart (hold Power 10 s and restart).
  - Going back to stock does not restore the stock storage format; copy music off first; untested by the project.
  - Only Innioasis firmware v3.2.0 FM is accepted for the radio firmware copy.
  - Multi-artist tags are one artist; no Album Artist view; no 12/24-hour clock switch; FM radio not included.

## Suggested order of work (Part A; Part B in V1-CODE-REVIEW)
  - A19 (B3/B4) and A20 (B5): code fixes, no hardware to write them; see V1-CODE-REVIEW Top 10.
  - A3, A5, A6, A13: doc and packaging fixes (one session, no hardware).
  - A1: capture plan for the second unit (#42) and decide mitigation; overnight A/B nights.
  - A8, A9, A11: one consolidated device-check pass with results recorded in a 1.0 report.
  - A4, A7: firmware-version policy and toolchain sources in the release.
  - A2: recruit one external install + one external build and record both.
  - A10, A16, A18: decide (implement/document/rename/merge).

## What I could not do
  - The six parallel code reviews did not report before the usage limit on 2026-10-17. They were redone on

2026-10-18 (`V1-CODE-REVIEW.md`), including the data-safety trace of the recovery installer and the Internal Storage resume record (both sound); what they did not cover is listed there under Coverage.
  - No hardware evidence was taken (rules of the audit).
  - `cppcheck`, `ruff`, `pyflakes` are not installed on this host; `clang-tidy` was delegated to the native-code review.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
