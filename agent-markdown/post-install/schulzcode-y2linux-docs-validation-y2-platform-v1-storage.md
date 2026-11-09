---
title: "Y2 Platform 1.0 storage and filesystem pass - Innioasis Updater"
description: "Y2 Platform 1.0 storage and filesystem pass <!-- knowledge-base-scope: scoped-validation-record -- 2026-10-04. Retain eMMC HS200 and the existing SD production ladder. Th"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-storage.html"
---

# Y2 Platform 1.0 storage and filesystem pass - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Platform 1.0 storage and filesystem pass

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Platform 1.0 storage and filesystem pass

2026-10-04. Retain eMMC HS200 and the existing SD production ladder. The installed Baseline02 passes bounded transport, scratch integrity, fsync, runtime-PM and same-card hotplug checks. Source fixes address media identity, removable-mount admission and diagnostics. **Platform 1.0 storage is PARTIALLY READY; full qualification is not established.** Repeated cold boots, full system suspend, card/filesystem diversity and endurance remain independent gates.

## Scope and reconciliation

Both repositories use isolated `codex/platform-v1-storage` worktrees, based on Linux `b5aea93` and Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. The [activation audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23storage-platform-10-optimization-admission--2026-10-04&anchor=storage-platform-10-optimization-admission--2026-10-04) and [mount-gate audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23storage-removable-mount-gate-audit--2026-10-04&anchor=storage-removable-mount-gate-audit--2026-10-04) precede their implementation boundaries. Playback admission and the final [closing audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23storage-platform-10-closing-audit--2026-10-04&anchor=storage-platform-10-closing-audit--2026-10-04) retain source versus physical qualification limits. No main-worktree writes, flash or push. Concurrent sessions may have their own main-worktree changes.````````````````````````

| Actual installed hardware identity | Value |
| --- | --- |
| Linux compiled source | 8584ccd85f052f351fe51650b2348c83ca894ed4 |
| Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 |
| Kernel / root / build | 6.18.0-y2linux-baseline-02 / 2025.02.18-platform-v1.21 / Y2LINUX-BASELINE-02 |
| Boot / taint | 27e6d684-3794-4490-95db-a489027cd4f4 / 0 throughout both storage slots |
| eMMC | FNX2MB, CID 150100464e58324d4206ec82a80434f9, card capability 0x57 |
| SD | SD128, CID 035344534431323885d04dba410192c7, capability 0x1f, 119 GiB card |
| Actual filesystems | /data ext4 808,058,880 bytes; /media/sd ext4 511,266,816 bytes |

The SD partition spans 249,735,168 sectors at sector 2048, but its ext4 filesystem is only about 512 MB. It was neither resized nor formatted. Capacity decisions use actual filesystem space/inodes. Y2DATA had about 51k free inodes and SD about 32k: a 50k-file corpus cannot simply move wholesale to this SD filesystem.

Current source/DT, tuning/fallback policy, runtime retention, root/data fsck and media helpers, Reborn source guards and validation history were reconciled first. [Candidate 3](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-SD-SDR104-DIAG.md) really failed sustained 200 MHz SD reads; its lower-clock result is retained. Candidate 4 changed exact MT6582 stock pads and exposed card driver selection; its original package was software-only. Baseline02 includes that later policy. The current clean 4 GiB result supersedes the older failure for this installed configuration and this card, without erasing its history or proving which individual electrical change caused the improvement. No stale failing tuning sweep was repeated.

Physical access uses `/tmp/y2-platform-v1-device.lock` with non-blocking admission. An initial read-only identity probe raced another session's lock acquisition; that probe is excluded from qualification. All measurements/mutations followed successful lock ownership. Mode changes used the existing SD lab interface only while SD was unmounted. Internal mounted root/data were never reset. Raw access was read-only: known Y2DATA partition or the identified, unmounted SD to `/dev/null`. Writes used new descriptor-pinned scratch files with free-space reserves. No user music, installed database, radios, services or CPU policy were changed.

The new benchmark ran as a temporary process importing its own source; installed platform files and legacy claim admission stayed intact. Its process-local scratch instance check used dev_t/diskseq. New claim consumers, mount gate and passive fallback fields are software-tested and not installed by this pass.

## 1. eMMC selected production mode

HS200, 200 MHz requested / 199,999,771 Hz actual, 8-bit, 1.8 V IO. Negotiation, CMD21 tuning and readback verification passed. Tuning ran once, with zero failures, CRC, timeout, controller/voltage/verify events, fallback or reset. Existing DMA request/recovery guards are unchanged. The card's advertised HS400 capability does not authorize an MT6582 HS400 implementation.

Retain fallback **HS200 → DDR52 at 50 MHz DDR → HS52 at 50 MHz → HS at 25 MHz → legacy at 13 MHz**. DDR52/HS52 capability, clock and fallback paths pass source checks. Physical renegotiation of those eMMC modes is NOT_RUN: root and data were mounted and this pass does not reset them or flash a diagnostic boot image.

## 2. eMMC measured performance

Decimal MB/s. Direct reads and guarded filesystem workloads are separate. Aggregate CPU is all-core `/proc/stat` busy time, excluding idle and iowait; background system work is included. IRQ deltas are counted over each measured interval, including background interrupts; IDs are local to this boot.

| eMMC workload | Size/count | Result | CPU busy | IRQ 220 / 221 delta |
| --- | --- | --- | --- | --- |
| Direct sequential read, 1 MiB transfers | 512 MiB total, eight 64 MiB chunks | 98.717 MB/s | 5.26–9.80% per chunk | 3076 / 6 |
| Guarded sequential write + final fdatasync | 32 MiB, 1 MiB transfers | 26.800 MB/s | 7.8% | 270 / 1 |
| Guarded sequential read + content verification | 32 MiB, advisory eviction | 64.617 MB/s | 24.9% | 192 / 0 |
| 4 KiB write + fsync | 64 operations | 0.504 MB/s; p99 6.250 ms | 24.4% | 800 / 1 |
| Small files, 4 KiB + file/directory fsync | 64 files | 0.280 MB/s; p99 10.661 ms | 22.6% | 896 / 1 |
| File fsync + rename + directory fsync + unlink | 64 transactions | 0.127 MB/s; p99 47.162 ms | 21.5% | 2180 / 2 |

All measured controller fault/reset/fallback deltas are zero. The compact [receipt](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-storage-20261004.json) contains all 24 workloads, p50/p95/p99/max, CPU and every recorded IRQ/counter delta, plus raw receipt hashes. These include mount/card safety checks and Python overhead. Individual call latencies exclude the preceding guard; throughput includes it and final syncing. They are bounded workload measurements, not a hardware write ceiling. Smaller 4/16/64 KiB transfers and random I/O are recorded separately. No guard was weakened to inflate numbers. Historical 128 MiB read figures are not directly comparable.

## 3. SD selected production ladder

**SDR104 at 200 MHz → DDR50 at 50 MHz DDR → SDR50 at 100 MHz → HS at 50 MHz, 3.3 V → HS at 25 MHz → legacy at 13 MHz.** Retain the core's existing DDR50/SDR50 ordering: the bounded read difference is only about 2.7%, and short cached writes are not evidence to reorder a robust fallback. Voltage failure retains its existing skip to the 3.3 V rung. No advertised mode alone is treated as qualification.

| SD rung physically exercised | Actual clock | Bus / IO | Direct read | Coverage |
| --- | --- | --- | --- | --- |
| SDR104 | 199,999,771 Hz | 4-bit / 1.8 V | 81.255 MB/s, 4 GiB | Four offset ranges; scratch/fsync/hash; fresh negotiation after reinsert |
| DDR50 | 49,999,942 Hz DDR | 4-bit / 1.8 V | 43.282 MB/s, 1 GiB | Scratch/fsync/hash |
| SDR50 | 99,999,885 Hz | 4-bit / 1.8 V | 44.451 MB/s, 1 GiB | Scratch/fsync/hash |
| HS | 49,999,942 Hz | 4-bit / 3.3 V | 23.234 MB/s, 1 GiB | Scratch/fsync/hash |

Three intentional, unmounted SD lab resets select the lower rungs. They are not transport failures. No automatic reset/fallback occurred during any measured workload. Physical removal clears the temporary rung and the reinserted card negotiates SDR104 automatically; final state is mounted SDR104.

## 4. SDR104 conclusion and exact MT6582 evidence

Retain SDR104 for this card/configuration. Default card driver type B (driver_type 0), host CLK/CMD/DAT drive requested/read back 4/4/4, stock Schmitt inputs 1/1/1, RDSEL 0, TDSEL 0, VQMMC 1800 mV, VMMC 3300 mV. The earlier candidate retained LK's Schmitt=0, RDSEL=12, TDSEL=5. Those earlier pads are not the current production policy. Types A/C/D were not swept because B already passes; no unsupported later-SoC fields were copied or enabled.

The exact 32-tap, non-circular MT6582 tuner uses three attempts per tap and a minimum four-tap eye. Command and data picks are separate:

| Recorded SDR104 tuning | Rising-edge passing range | Selected delay / margin |
| --- | --- | --- |
| Command | 0–31, open 32-tap eye | 15; 15/16 |
| Command internal delay after reinsert | 0–23 | 11; 11/12 |
| Data | 0–30, 31-tap eye | 15; 15/15 |

After reinsert, the data tap 31 passes some attempts but not all; the pick remains inside the all-pass window. Falling-edge maps have holes and were not chosen. RXDLYSEL and later SoC transmit/latch fields retain their existing MT6582 policy. The test reads 1 GiB at each of card offsets 0, 1, 4 and 64 GiB, in 64 MiB direct chunks: 4 GiB total, zero CRC/timeouts/controller faults/verify faults/fallbacks. This is bounded single-card evidence; temperature/card diversity and long endurance are not proved. Runtime retention and post-reinsert scratch hashes also pass.

## 5. SD filesystem performance

| SD rung | Guarded seq write / read, MB/s | fsync p99, ms | Small-file fsync p99, ms | CPU write / read | IRQ 221 write / read |
| --- | --- | --- | --- | --- | --- |
| SDR104, 16 MiB | 18.854 / 56.768 | 6.420 | 12.145 | 6.4 / 19.2% | 108 / 96 |
| DDR50, 4 MiB | 30.498 / 39.658 | 5.040 | 14.586 | 11.9 / 16.7% | 33 / 24 |
| SDR50, 4 MiB | 23.784 / 40.114 | 6.712 | 14.701 | 8.0 / 13.0% | 30 / 24 |
| HS, 4 MiB | 8.905 / 22.088 | 63.753 | 16.075 | 5.2 / 14.6% | 33 / 25 |

All use 1 MiB sequential transfers and 64 fsync/small-file operations. Payload sizes differ, and card cache/flush tails affect short writes; do not rank modes from these write numbers. Sustained direct reads provide the comparison above. Direct-read CPU ranges are SDR104 4.02–24.92%, DDR50 3.37–11.40%, SDR50 2.35–8.83%, HS 2.10–8.48%. Corresponding IRQ 221 deltas are 24621, 6168, 6168,
  - Full IRQ/counter deltas and metadata create/stat/rename/delete rates are

in the receipt. All measured errors, CRCs and timeouts are zero.

The separate mixed corpus has 1,000 files, 23,703,609 bytes, 15 format variants across 10 extensions. Each copied file and created directory is fsynced, then file-scoped advisory eviction and SHA256 readback verify all 1,000 files on each volume. The standalone stock Reborn scanner uses a new private database and the installed native media library. Product source is byte-identical to installed `b71b468`; scanner ELF, harness, corpus manifest/archive and wrapper hashes are in the receipt. No installed database or services are changed.

| Mixed music workload | DATA, HS200 | SD, SDR104 |
| --- | --- | --- |
| Copy + file/directory fsync | 1.731 MB/s; 13.691 s | 1.532 MB/s; 15.468 s |
| Read + all-file SHA256, advisory eviction | 3.078 MB/s; 7.700 s | 3.034 MB/s; 7.813 s |
| Initial metadata/library scan | 5.526 s; 180.96 tracks/s | 5.495 s; 181.97 tracks/s |
| Incremental scan | 0.393 s; all 1,000 reused | 0.401 s; all 1,000 reused |
| Aggregate CPU, copy / read / combined scans | 21.68 / 25.50 / 27.28% | 19.08 / 26.34 / 27.11% |
| IRQ 220 / 221, copy | 14883 / 13 | 0 / 12715 |
| IRQ 220 / 221, read | 3020 / 8 | 10 / 3023 |
| IRQ 220 / 221, combined scans | 367 / 5 | 0 / 326 |
| Scanner maximum VmHWM | 10,656 KiB | 10,936 KiB |

Both scans complete with 1,000 tracks and zero failures; every controller fault, CRC, timeout, reset and fallback delta is zero. Scan CPU/IRQ is measured around the combined initial/incremental invocation, including its startup overhead. Short repeated fixtures measure metadata and small-file behavior; they do not qualify full-length audio bandwidth or playback. Fresh cleanup leaves both scratch directories empty, SD mounted at SDR104 and both controllers gated. These are installed stock measurements, not physical acceptance of new source.

## 6. Filesystem support and admission````````````

| Filesystem | Platform support and gates | Actual validation / remaining gap |
| --- | --- | --- |
| ext4 | Built-in; fixed root/data identity and boot fsck preserved. Removable preflight e2fsck -n; explicit check uses -f -n. | Physical data/SD mount, fsync, SHA, eject/remount; SD explicit read-only check passes. New mount preflight is software-tested. |
| FAT/FAT32 | Built-in FAT/VFAT, CP437 short names; SD UTF-8 long names now use utf8=1. fsck.fat -n preflight. | New host FAT32 image: long Unicode name and 1 MiB SHA roundtrip; dirty bit refuses read-only checker, unchanged image hash. Physical FAT card NOT_RUN. |
| exFAT | Built-in Linux driver, UTF-8 default; pinned exfatprogs; fsck.exfat -n preflight. | New host image read-only checker preserves its SHA; helper/source tests cover mount/eject. Physical exFAT card NOT_RUN. |

All removable mounts remain `rw,nosuid,nodev,noexec`; FAT/exFAT retain `fmask=0177,dmask=0077`. The bounded 60-second preflight rejects reported faults, timeouts and identity/diskseq changes. Missing/unsupported/ambiguous media are not autoformatted. Checker success follows tool semantics; normal ext4 journal behavior remains the kernel's responsibility. Large media can time out and need an owner-directed offline check; platform mounting remains unavailable if its checker still exceeds the admission deadline. Repair commands are never automatically invoked for SD. Internal root/data's existing identity-gated boot `e2fsck -p` remains.

The installed helper performs identity admission and an explicit fsck only; it did not automatically fsck the card on the physical reinsert. The new gate has not been deployed. Known dirty FAT refusal is host evidence; dirty user media was not deliberately created, repaired or mounted for testing.

UUID-less/zero-serial media use CID plus filesystem/geometry identity. Whole-card FAT uses start=0; no missing partition start is mistaken for invalid media. Nonzero duplicate UUID cards now get distinct CID-qualified Reborn source IDs. Tests cover geometry/CID change, missing diskseq, same-card reinsertion, ambiguous mounts, failed eject and replacement during fsck. No physical second card was available. ext4 physically passed a 191-byte UTF-8 long filename, 1 MiB fsync, advisory eviction and SHA256 on Y2DATA. Physical SD long names and physical FAT/exFAT Unicode remain untested.

FAT32's single-file limit remains 4 GiB minus one byte. ext4/exFAT large-file support is retained. ARM Python passed sparse scratch fsync/hash at offset 4 GiB+17 for 4,117 bytes under QEMU; that proves userspace offset ABI on a host filesystem. Target-media files over 4 GiB are NOT_RUN because the present filesystems are too small. No resize/format was used to manufacture that test.

## 7. Runtime-PM result

Five passive samples, two seconds apart: both hosts gated=1, mismatch=0, error=0, restored=0. eMMC retained-resume count 799; SD 3476–3485. SD detect polling occasionally resumes it between observations; it gates again. After physical reinsert and its benchmark, eMMC retained=839 and SD retained=4003, again gated with zero mismatch/error. Final mixed-corpus handoff records eMMC retained=2659 and SD retained=8096, both gated with zero mismatch/error. Its extra slow-blocker probe used a nonexistent sysfs path and is unavailable; the earlier successful passive samples below remain the blocker evidence. Existing request/DMA/controller/FIFO/interrupt admission and register retention remain intact. Active requests can legitimately defer suspend; `refused_request` is not a transport error.

Reading the detailed live register diagnostic resumes MMC; it was used explicitly for electrical/mode evidence, not for idle sampling. New platform status reads only passive mode, saved tuning and runtime-PM state for these fields. Whole status still may probe UUID via blkid and is not claimed to be entirely free of I/O.

## 8. C2/C3 compatibility

Storage clock-gate compatibility PASS; new C2/C3 entries NOT_OBSERVED. Passive slow blocker mask is `0x100800`: APDMA bit 11 and BTIF bit 20; MSDC0 bit 12 and MSDC1 bit 13 are clear. This USB/radio-attached, four-core Baseline02 boot records C2 entries=0 and C3 successes=0. Topology/frequency/other peripheral blockers remain effective; none were weakened or hidden.

The retained [UART01 physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) already proves real C2/C3 returns and matching post-return eMMC/SD hashes, including 21 guarded C3 trials. Current source tests cover the storage/idle interaction. Current runtime retention plus post-idle hashes are a storage regression, not a new physical C3 or full system-suspend qualification.

## 9. Hotplug result

Safe eject, empty slot, same-card insert and remount PASS on installed code. Owner reported no Reborn eject action, so `y2-media unmount` performed ordinary safe unmount. There was no force/lazy unmount or live removal. Explicit unmounted ext4 check passed. Owner then removed/reinserted the same card. Kernel reports slot empty, resets the next-card ceiling to SDR104, negotiates/tunes SDR104 and automatically mounts the same ext4 filesystem. Diskseq changes 2 → 3; CID and geometry identity stay the same. The final scratch benchmark passes all 24 workloads and five SHA regions. Mount ID 32 may be reused after the old mount is gone; descriptor pinning protects live operations from that reuse.

Installed Reborn emits `source_removed` sequence 64, `source_inserted` 68 and `scan_completed` 70: two discovered/reused SD tracks, zero failures, 120 ms. Earlier controlled eject/remounts also deliver clean source events. Existing real library has only three tracks; those tiny scans are not scale evidence. Physical replacement, unsafe live removal, absent cold boot and repeated boot are NOT_RUN. Present media was observed on the running boot, not subjected to a new controlled cold-boot test. Missing UI eject remains a product gap; the safe platform helper is available. New claim/source-ID code is host/ARM-tested only.

## 10. Integrity result

Zero detected corruption. Both 1,000-file mixed corpora pass fsync and SHA256 readback; all 2,000 comparisons match. Six additional scratch runs (eMMC, four SD modes and post-reinsert SDR104) each pass five independent SHA regions after all writes:

| Offset, bytes | Region size, bytes |
| --- | --- |
| 0 | 1 |
| 511 | 513 |
| 4093 | 4099 |
| 65543 | 65537 |
| 1049087 | 1048583 |

Different nonzero patterns catch offset aliasing. Each write is fsynced; readback requests file-scoped advisory DONTNEED. Sequential/random buffers also compare content. No global cache drop or raw write. The final software instrumentation also records CPU/IRQ/controller deltas around SHA regions and fails if a recovered CRC/reset/fallback occurred; the added recovery case passes. Physical raw before/ after counters were zero through SHA verification. Advisory eviction is not an absolute cold-media guarantee. Power-loss durability and long endurance are NOT_RUN. Scratch-only cleanup never resolves against a replacement mount.

## 11. Optimizations and fixes made
  - Replace unstable kernfs inode/ctime mount claims with dev_t + diskseq, matching

the existing stable media inventory. Missing sequence fails closed. This prevents false card changes under inode reclamation and detects identical-card reinsert.
  - Use validated CID/geometry/filesystem identity in managed Reborn SD source keys

even when UUID exists; duplicate UUID cards no longer alias cached library rows. Preserve mount/root-FD guard in the library's source-ID admission. Current and queued playback separately validate the live source, reject symlinks/special files/subordinate mounts, and retain file/parent descriptors for decoder/sidecar opens; file-entry or directory replacement cannot redirect to a new card.
  - Support UUID-less whole-card geometry and UTF-8 FAT long names; add read-only

preflight before removable mounts and reject changed card instances.
  - Add per-workload CPU/IRQ/error counters, fsynced small files, offset-specific

SHA256 and recovered-controller-fault failure to scratch diagnostics.
  - Expose passive fallback origin/reason, card driver type, runtime-PM state and

recorded tuning and cached mount/checker failures through platform status. No polling-induced register resume.

No throughput optimization is claimed. Existing transfer modes already pass; measurement and lifecycle integrity are the justified improvements. CID-qualified IDs require paired Linux/Reborn deployment, and pinned sidecars require the app's matching native media library. A bounded 12-byte header fallback selects the existing JPEG/PNG/WebP image decoders when the descriptor path has no suffix; regular/nonblocking file admission rejects special files before sniffing. Its ABI, image size bound and valid named-file behavior remain unchanged. Short/unknown headers and nonregular-file tests pass. Existing UUID-only rows stay offline; rescan/new queue selection is required once. Saved queues contain old Track snapshots. The reviewed pathname-only load gap is closed with fresh source admission and pinned regular files, including queued next tracks; no automatic rebind to an unproven card. No schema, SQLite pragma, indexing or database optimization is included. The database lane reviewed source-ID compatibility; only its small guard/test hunk is shared.

## 12. Intentionally unchanged

Production clocks/ceilings and fallback order; command/data tuner and tap/edge policy; MT6582 pads and default card type B; supplies/voltage switching; DMA and request recovery; runtime retention and CPU blocker masks; root/data/partition geometry, capacity and boot fsck; safe eject semantics and private mount masks; SQLite implementation, installed music/library, radios/services/CPU settings; release/fallback/protected partition and backup/calibration obligations.

No repeated experiments on old electrical defaults, speculative high-drive settings, later-SoC tuning fields or theoretical maximum benchmark pursuit. No flash, push, autoformat, mounted-media reset or owner-media resize.

## 13. Files changed

Linux: `tools/platform/y2_platform/{observe,media,bench}.py`; `kernel/patches/0009-y2-msdc-readonly.patch` and `manifest.json` (four diagnostic lines only; regenerated patch offsets/checksum); `tests/test_platform_contract.py`, `tests/test_platform_storage_tools.py`, new `tests/test_filesystems.py`, `tests/README.md`, `tools/production/tests.sh`; architecture/storage guide, roadmap/audit, documentation catalog, historical ceiling/SD superseding notes, this report and compact evidence JSON.

Reborn: `crates/reborn-platform/src/storage.rs` and `crates/reborn-library/src/lib.rs` (source-ID compatibility and test only), `app/reborn/src/main.rs` and `app/reborn/src/playback.rs` (validated current/queued playback admission and pinned decoder/sidecar paths); `crates/reborn-media/native/media.c` (bounded signature fallback for extension-free sidecar descriptors; regular/nonblocking admission, existing ABI/codecs preserved) and `crates/reborn-media/src/native.rs` (short/unknown/nonregular image tests).

## 14. Tests and artifacts
  - 134 affected source/artifact cases PASS with actual fresh production DT,

storage ceilings/tuning/MMC requests/context/transport/recovery, media/filesystem, C2/C3 guards, overlay, ABI, D08 memory and BOOTIMG. Subsequent mount-gate/extra SHA regression run: 40 affected cases PASS; no dependency skips.
  - Three native new-image filesystem tests PASS: ext4/exFAT no-write fsck;

FAT32 Unicode/long name/hash and unchanged dirty-media refusal. No device format.
  - Fresh locked production config + W=1 MSDC object: PASS without warnings.

Fresh full Image/zImage/modules build, actual DT, module allowlist/dependencies/ ARM vermagic, emitted-code ABI, rescue/D08 memory and BOOTIMG packing: PASS.
  - Reborn platform 77 + library 28 + media 22 + application/playback 38 tests PASS, including

stale-card/UUID/mount/path, root/intermediate/final symlink and FIFO/socket refusal, plus original bytes retained after file-entry/directory replacement. All 33 valid audio fixtures preserve metadata and first PCM/position through extension-free pinned file paths; JPEG/PNG/WebP sidecars preserve decoded pixels. Formatting and app/media/platform Clippy with warnings denied PASS; complete pinned Cortex-A7 hard-float ARM release build PASS. Final ARM ELF class/hard-float ABI, dependency closure and absent build RPATH pass; final QEMU native sidecar test produces identical JPEG/PNG/WebP pixels through file FDs. ARM QEMU ABI/TLS/VFP/thread and final settings checks PASS; these are host emulation.
  - ARM Python 24-workload scratch benchmark/five SHA regions and large-offset

sparse-file ABI PASS on host scratch. Final source-only gate/instrumentation changes remain physically uninstalled.
  - Retained Baseline02 preserving-package payload/scatter/fallback/contracts and

clean root ext4 validate PASS. No new paired release package or release qualification is claimed. Documentation links/catalog and whitespace checks pass at handoff.
````````

| Fresh offline artifact | Bytes | SHA256 |
| --- | --- | --- |
| Image | 12406144 | cec19ea4031b9068bdc6acabfd24dc527c0c3865d350ad39b67a196958b5c436 |
| zImage | 4522928 | 860cf3248df440e68ac4dd6cd2cad53f26444028919744936a43fd09e8abd991 |
| DT | 14682 | 67385472a7ee06d7fe2784bc7bde28d63a74c6d1e369d7e510ca581f0fb17eaa |
| BOOTIMG | 7149568 | c13df78b3eefad83b2c54e9efc95fb5331f37ab29ec1e3743876fe8aa52edeca |

The offline BOOTIMG uses the new diagnostic overlay, unchanged hash-verified Baseline02 rescue binaries and current unchanged production DT/config. It is not installed and does not establish new root/Reborn pairing acceptance. Full logs/receipts are local `out/platform-v1-storage/`; compact workload data and their hashes are committed [here](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-storage-20261004.json).

## 15. Commits and handoff

Linux implementation: `2a603c13193552c6e07e028fa10cb87b9848bb16`. Reborn source identity: `ee1c25a60a2e0d63a6a83dbd442b5486543ec46e`. Reborn playback/sidecar admission: `f726ae40bfd965d7f09cb37b3e317bfb532db0f2`. The subsequent report/audit commit is identifiable in this file's history. Both branches remain local; no push. Main worktrees are untouched by this pass. New changes need paired integration and target acceptance. Device handoff restores mounted SDR104, unchanged eMMC HS200, same boot and taint 0; newly created scratch and temporary harness files are cleaned before release.

## 16. Platform 1.0 verdict

PARTIALLY READY. Selected modes and installed single-card behavior pass this bounded storage sweep with zero corruption or transport faults. Source fixes and diagnostics are ready for review and paired integration. This does not close #28, #32, #33 or #34 or manufacture a general Platform 1.0 release acceptance.

Next smallest evidence boundary: paired-source integration and explicit target media admission/source-key migration, then repeated cold boots/absent boot, second-card replacement and physical FAT/exFAT/Unicode/large-file coverage. Full system-suspend recovery, real C2/C3 regression under the intended normal workload, temperature/card diversity, power-loss durability and longer endurance remain independent qualification gates. Existing recovery/fallback and backup/calibration obligations remain in force.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
