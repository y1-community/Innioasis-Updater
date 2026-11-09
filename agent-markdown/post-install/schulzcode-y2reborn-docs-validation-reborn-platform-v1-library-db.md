---
title: "Reborn Platform 1.0 library/database performance pass - Innioasis Updater"
description: "Reborn Platform 1.0 library/database performance pass 2026-10-04. Branch codex/platform-v1-library-db , isolated Reborn and Linux worktrees. Host and bounded native Y2 li"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-platform-v1-library-db.html"
---

# Reborn Platform 1.0 library/database performance pass - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Platform 1.0 library/database performance pass

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Platform 1.0 library/database performance pass

2026-10-04. Branch `codex/platform-v1-library-db`, isolated Reborn and Linux worktrees. **Host and bounded native Y2 library/database PASS through 50,000 tracks; ARM build PASS.** This is a bounded library/database verdict, not whole-platform milestone closure. No flash, push, production database access, installed binary replacement or identity setting change occurred. FFmpeg metadata parsing remains another session's ownership.

## Current schema, ownership and Product v2 workload

Schema version 1, unchanged persistent file format:
  - `sources`: `id TEXT PRIMARY KEY`, `root TEXT NOT NULL`, `online INTEGER NOT NULL`.
  - `tracks`: integer primary-key `id`; `source_id` foreign key to `sources(id)`;

`path`, `filename`, `size`, `mtime`, `title`, `artist`, `album`, `album_artist`, `track`, `disc`, `duration_ms`, `codec`, `sample_rate`, `channels`, `bitrate`, `artwork`, `seen`, `deleted`; unique `(source_id,path)`. Required fields are non-null, numeric values are read into checked Rust types. No cascade deletion.
  - One connection, owned by the existing database worker after initialization;

bounded FIFO command channel (32), single scanner worker, asynchronous replies polled by the render loop. No new connections or ORM.

The actual product exposes Songs, Albums, Artists, folders, album/artist contents, Now Playing/track information and the playback queue. It does not expose genre, album-artist, recently-added or text-search routes. Albums use album artist in their identity; that is a grouping field, not a separate browse screen. SQL DISTINCT/search/primary-key lookups below are diagnostics, not navigation SQL. Product navigation uses one resident `AppModel.library.tracks` and cached row identities. Wheel input and drawing format only the visible rows. Now Playing reads the current queue item; collection queue population copies selected Tracks. There is no per-album/per-artist SQL N+1 loop.

## Changes and query plans

The original ordered browse path was already indexed and fast. Preserved indexes:````````````````````

| Index | Columns / predicate | Decision |
| --- | --- | --- |
| implicit source primary key | sources(id) | retain |
| implicit track identity | tracks(source_id,path) unique | retain; scanner seeks this |
| tracks_album | (album_artist,album,disc,track) | retain, including old-reader compatibility |
| tracks_artist | (artist) | retain; no measured removal benefit required |
| tracks_browse | (artist,album,disc,track,title,path) WHERE deleted=0 | retain; ordered pages and artist seek |
| tracks_browse_album | (album) WHERE deleted=0 | retain; small album seek |

No persistent index added or removed; no schema migration introduced. The existing atomic v0 creation and additive v1 index repair remain. New temporary tables are connection-local: `scan_candidates` holds at most 64 file fingerprints; `scan_seen(id INTEGER PRIMARY KEY)` holds only the current source's visited IDs. `temp_store=MEMORY` keeps these disposable presence records off flash. The main page cache target is explicit 2 MiB (`cache_size=-2048`), close to the previous SQLite default -2000 KiB. Temp presence scales with IDs, not cloned metadata.

Important EXPLAIN results and stable tests:``

| Workload | Plan / remaining cost |
| --- | --- |
| ordered song page | browse-index scan; source PK lookup; no sort B-tree |
| artist contents | browse-index seek on artist; no sort B-tree |
| album-name contents | partial album-index seek; temp order B-tree for the matched album(s) |
| artists DISTINCT | covering browse-index scan, no per-artist query |
| albums DISTINCT | tracks_album scan; must examine records because deleted is not covered |
| diagnostic substring search | covering browse-index scan; a leading wildcard cannot seek |
| Now Playing diagnostic ID | integer primary-key lookup; product actually uses memory |
| scan fingerprint batch | scan at most 64 temp candidates; seek unique source/path for each |
| prune | source/path index narrows source; temp integer-PK membership checks |
| catalog cursor | browse-index range seek; rowid tie-breaker makes equal tags/paths across media safe |

List statements are cached and limited to 512 rows. Catalog snapshots read 512-row keyset pages in one read transaction, preserving a coherent source online state and avoiding repeated OFFSET walks. The product still needs a resident catalog for its existing grouping and queue semantics; the scanner no longer duplicates that entire catalog. The existing 250k discovery safety limit also bounds catalog publication and fails explicitly rather than truncating. Only 50k is qualified here. Startup requests the saved catalog before scanning; completion reloads it only when a scan publishes changes, removes rows or fails. An unchanged scan preserves the resident catalog and navigation cache. Source changes request a fresh online-state snapshot before scanning. The old app waited for the scan and then silently loaded only 20k rows. SQL stays off normal navigation and off the render thread after initialization. Startup open still performs `quick_check(10)`; this pass preserves its corruption detection.

The main repeated-work defect was an O(N) count after every worker command, including reads and each 64-track write. Counts now update once per source Finish or explicit diagnostics. The scan-wide `Vec<Track>` → `BTreeMap<PathBuf,Track>` copy and per-track cloning/upsert on unchanged scans are removed. The only per-track insertion loop on reuse writes fingerprints into a bounded TEMP table; identity checks use set joins, not per-file RPCs or statement preparation.

## Incremental updates, transactions and durability

A Begin command assigns a connection-local scan generation and clears abandoned TEMP presence. Each 64-file probe compares source identity, path, byte size and nanosecond mtime; unchanged live rows only mark temporary presence. New/changed files retain the existing decoder/tag construction. Only those rows enter the existing 64-track atomic transactions. Conditional upserts skip identical metadata, preserve IDs at unchanged paths, resurrect soft-deleted files and mark presence atomically with successful publication. Source updates likewise skip unchanged root/online values. No one-fsync-per-track design is introduced.

Complete Finish prunes only live rows absent from presence, in a transaction with temporary cleanup. Incomplete traversal, cancellation, read/decode error, mount replacement or publication failure cannot prune old usable rows. A worker rechecks mount identity before pruning; directory-descriptor traversal remains pinned to the original filesystem. A retry gets a fresh presence set; interrupted scans preserve both old rows and any validated committed new batches. Renames appear as a new path plus a soft-deleted old path after successful completion; this pass does not invent content hashes or transfer IDs across ambiguous moves. Same paths on different source IDs cannot reuse each other's fingerprints.

Storage-pass integration is anticipated without editing its files: legacy `uuid:<UUID>`, UUID-less `uuid:cid:<64 hex>` and `uuid:<UUID>:cid:<64 hex>` source IDs retain UUID and mount-ID guards. CID derivation/validation belongs to the platform storage owner; this pass merely accepts its qualified source ID and keeps those identities separate. UUID-only legacy rows remain retained/offline when that paired storage change introduces a new qualified identity; old saved queue snapshots are not auto-rebound. Duplicate UUID physical media qualification belongs to that session, not these generic identity tests.

WAL + synchronous=NORMAL remains unchanged, with foreign keys ON and the 2-second busy timeout retained. The database lives on ext4 Y2DATA/eMMC; SD is read as source media and does not own the database. Metadata is reproducible by rescan. NORMAL in WAL preserves consistency but can lose recent commits after power loss; this pass makes no electrical power-loss certification. FULL is appropriate if irreplaceable user data is later added. OFF is never selected. See [SQLite synchronous policy](https://www.sqlite.org/pragma.html#pragma_synchronous) and [WAL durability](https://www.sqlite.org/wal.html).

Explicit safe shutdown still performs `wal_checkpoint(TRUNCATE)`, closes the connection and acknowledges any error. The default 1000-page auto-checkpoint (~4 MiB WAL at 4096-byte pages) remains; no forced per-scan checkpoint. No VACUUM or ANALYZE on boot or after scans: current seek plans need neither for this workload, and soft-deleted/offline rows intentionally preserve identity. Reclamation for prolonged multi-card churn remains an explicit future maintenance policy; this pass does not silently discard historical libraries. Full-database quick checks remain at open/diagnostic, not every scan completion.

## Reproducible measurement

[Checked-in results](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-library-db-host.json) contain all operation samples, median/p95/worst, query plans, SQLite settings, memory and binary identities for 100, 1k, 10k and 50k. Base implementation is Reborn `b71b468`; instrumentation-only commit `9152005` gives a reproducible before checkout. The measured host implementation is `b0b114e`; later commits add compatibility/assertions and avoid the app's unchanged-scan catalog reload. No main worktree was edited.

Host: Ryzen 7 7800X3D, x86_64 Linux 7.2.8, SQLite 3.53.4, real Btrfs/NVMe output directory, release profile, CPU affinity 6 for both binaries. OS cache and other host activity are uncontrolled; opens are warm/reopened, not cold boot. Timing uses whole operations in milliseconds, not nanosecond claims. Initial population has 5 trials; query operations 41, open 21, catalog 7, unchanged scan 7, mixed mutation scan 7, media switching 21, pruning 7. A small sample's p95 can equal its worst; this is empirical timing, not a tail-latency guarantee.

Fixtures contain 24-track two-disc releases, 127 artist names, compilations, missing tags every 29 releases, repeated titles and album names, distinct source identities and real filesystem entries. Initial population times SQLite ingest of synthetic tags, not FFmpeg initial parsing. Reuse scans exercise the real scanner with size/mtime matching fixture files. Each mutation sample adds a new file, changes a file, removes a file and moves a file; three files decode and N-3 reuse. The first mutation also includes lazy loading the unchanged FFmpeg membrane. Pruning separately times removal of roughly 1% after preparing presence; it intentionally excludes enumeration. Media switching measures source online updates and a FIFO read barrier, not formatting or physically inserting SD.

The before full-catalog timing uses explicit 512-row OFFSET pages to measure all N rows. The old production app itself displayed only the first 20k; its 50k database was not fully exposed. The after timing uses the new keyset snapshot. SQL album/artist filters cap results at 512, page workloads use 64; full product collection behavior is measured by the separate resident UI catalog. Playback queue samples deliberately use `min(N,MAX_QUEUE)`; the existing 20k queue and 8 MiB session limits remain independent product limits. Play All above 20k still rejects the oversized queue. This is not a 50k-queue qualification.

To reproduce the baseline with the current instrumentation, archive the original production code and overlay only the benchmark/CLI adapters:`python3 tools/build/library_db_baseline.py --output out/library-db/baseline cargo build --release --locked --bin reborn-bench \ --manifest-path out/library-db/baseline/Cargo.toml`

Build the current checkout and run either executable through the host runner:`cargo build --release --locked --bin reborn-bench python3 tools/build/library_db_bench.py --binary target/release/reborn-bench \ --output out/library-db/reproduce --cpu 6`

The runner inherits a fresh empty directory FD. For constrained target volumes, `reborn-bench --scratch-fd FD --media-fd MEDIA_FD --tracks 50000 --platform-db` accepts two empty pinned roots: half the fixture files on each source, with all databases in the first root. The 50k target baseline is original `b71b468` production code with this current instrumentation overlay; the after executable is `c161404`. Initial parser throughput and codec-specific scan improvements remain with the separate FFmpeg pass.

### 1,000 tracks: host before/after

Milliseconds. Each cell is median / p95 / worst.

| Operation | Before | After |
| --- | --- | --- |
| SQLite initial population | 5.481 / 5.620 / 5.620 | 5.128 / 5.253 / 5.253 |
| Songs page (64) | 0.063 / 0.094 / 0.107 | 0.051 / 0.056 / 0.099 |
| Deep OFFSET page (64) | 0.128 / 0.155 / 0.718 | 0.116 / 0.125 / 0.213 |
| Album contents (≤512) | 0.045 / 0.050 / 0.084 | 0.036 / 0.041 / 0.062 |
| Artist contents (≤512) | 0.041 / 0.067 / 0.474 | 0.031 / 0.034 / 0.048 |
| Artists SQL diagnostic | 0.032 / 0.035 / 0.056 | 0.032 / 0.034 / 0.038 |
| Albums SQL diagnostic | 0.078 / 0.095 / 0.103 | 0.078 / 0.087 / 0.204 |
| Substring-search diagnostic | 0.088 / 0.110 / 0.526 | 0.089 / 0.093 / 0.100 |
| Full catalog load | 0.803 / 1.372 / 1.372 | 0.673 / 0.910 / 0.910 |
| DB open including quick_check | 0.444 / 0.524 / 0.889 | 0.466 / 0.517 / 0.594 |
| Unchanged real scanner rescan | 9.768 / 14.670 / 14.670 | 3.094 / 3.540 / 3.540 |
| Mixed incremental update | 11.567 / 40.231 / 40.231 | 3.799 / 26.115 / 26.115 |
| Replace media identity + read | 0.069 / 0.134 / 0.204 | 0.038 / 0.044 / 0.135 |
| Delete missing ~1% (prune only) | 0.234 / 0.378 / 0.378 | 0.345 / 0.360 / 0.360 |

### 10,000 tracks: host before/after

Milliseconds. Each cell is median / p95 / worst.

| Operation | Before | After |
| --- | --- | --- |
| SQLite initial population | 114.445 / 118.678 / 118.678 | 107.688 / 108.707 / 108.707 |
| Songs page (64) | 0.065 / 0.116 / 0.367 | 0.054 / 0.064 / 0.137 |
| Deep OFFSET page (64) | 1.220 / 1.632 / 1.787 | 1.196 / 1.254 / 1.308 |
| Album contents (≤512) | 0.046 / 0.080 / 0.587 | 0.035 / 0.038 / 0.069 |
| Artist contents (≤512) | 0.090 / 0.120 / 0.125 | 0.080 / 0.086 / 0.127 |
| Artists SQL diagnostic | 0.261 / 0.338 / 0.647 | 0.256 / 0.264 / 0.329 |
| Albums SQL diagnostic | 0.831 / 1.244 / 1.378 | 0.818 / 0.875 / 1.129 |
| Substring-search diagnostic | 0.521 / 0.883 / 0.916 | 0.519 / 0.567 / 0.665 |
| Full catalog load | 21.827 / 22.681 / 22.681 | 6.867 / 7.814 / 7.814 |
| DB open including quick_check | 3.512 / 3.842 / 3.934 | 3.109 / 3.243 / 3.276 |
| Unchanged real scanner rescan | 188.252 / 194.633 / 194.633 | 32.227 / 34.810 / 34.810 |
| Mixed incremental update | 183.824 / 212.426 / 212.426 | 34.353 / 69.966 / 69.966 |
| Replace media identity + read | 0.187 / 0.264 / 0.334 | 0.037 / 0.043 / 0.136 |
| Delete missing ~1% (prune only) | 2.902 / 19.788 / 19.788 | 4.186 / 9.098 / 9.098 |

### 50,000 tracks: host before/after

Milliseconds. Each cell is median / p95 / worst.

| Operation | Before | After |
| --- | --- | --- |
| SQLite initial population | 869.373 / 1275.767 / 1275.767 | 847.918 / 877.863 / 877.863 |
| Songs page (64) | 0.066 / 0.072 / 0.185 | 0.057 / 0.119 / 0.190 |
| Deep OFFSET page (64) | 7.293 / 7.639 / 7.846 | 7.328 / 7.765 / 9.013 |
| Album contents (≤512) | 0.133 / 0.199 / 0.213 | 0.125 / 0.148 / 0.251 |
| Artist contents (≤512) | 0.287 / 0.385 / 0.527 | 0.276 / 0.373 / 0.501 |
| Artists SQL diagnostic | 1.952 / 2.104 / 2.295 | 1.977 / 2.238 / 2.350 |
| Albums SQL diagnostic | 6.417 / 6.738 / 7.036 | 6.531 / 6.727 / 7.189 |
| Substring-search diagnostic | 0.483 / 0.590 / 0.607 | 0.432 / 0.563 / 0.695 |
| Full catalog load | 398.885 / 399.813 / 399.813 | 39.637 / 40.416 / 40.416 |
| DB open including quick_check | 15.113 / 15.458 / 16.282 | 15.835 / 16.615 / 16.838 |
| Unchanged real scanner rescan | 1184.822 / 1217.071 / 1217.071 | 188.897 / 190.095 / 190.095 |
| Mixed incremental update | 1198.459 / 1227.331 / 1227.331 | 190.115 / 213.913 / 213.913 |
| Replace media identity + read | 0.713 / 0.773 / 0.789 | 0.038 / 0.043 / 0.147 |
| Delete missing ~1% (prune only) | 29.836 / 32.921 / 32.921 | 44.238 / 56.741 / 56.741 |

The no-op source update/read barrier improves because read commands no longer count the whole library. Ordinary indexed browse queries stay in the same range. Isolated pruning is slower (50k median 29.836 → 44.238 ms): a temporary presence membership check replaces persistent generation comparison. Complete unchanged rescans still improve 6.3× and mixed updates 6.3× at 50k. No extra persistent index was justified by that bounded finish cost.

### Memory, size and write behavior

Process high-water RSS includes the entire isolated fixture benchmark, seven catalog replacements, decoder/library loading, UI and up to a 20k queue. It is not whole-Y2 RAM, a native allocator breakdown or a simultaneous render/ playback stress qualification. Seed metadata is released before scanner testing. No artwork cache is introduced or enlarged.

| Tracks | Peak RSS before → after (MiB) | DB before → after (MiB) | Seven unchanged rescans: process write_bytes before → after (MiB) |
| --- | --- | --- | --- |
| 1,000 | 49.28 → 48.52 | 0.465 → 0.418 | 8.012 → 0.008 |
| 10,000 | 77.91 → 63.63 | 4.359 → 4.125 | 200.820 → 0.008 |
| 50,000 | 168.17 → 112.78 | 21.371 → 20.203 | 1534.879 → 0.008 |

The after write counter is 8192 bytes per seven-scan run, including observability logs. Trigger tests independently prove unchanged scans do not UPDATE persistent track/source rows. `/proc/self/io write_bytes` measures process-issued storage I/O, excludes physical NAND amplification and may miss already-dirty page rewrites. It is not an fsync count. New fixture file creation and synthetic population are outside this reuse-write window. Initial/update write totals are not claimed. Removing seen/metadata/index churn substantially reduces wear. The smaller measured DB is a fresh-fixture outcome after the entire workload; existing deployed databases do not automatically shrink. No VACUUM was used.

Cached wheel navigation is below 0.01 ms on this host and is preserved; no speedup claim is made from that tiny timing. At 50k, rebuilding Songs/Albums/Artists catalogs has after medians 5.133 / 3.475 / 0.519 ms; up-to-20k queue construction 3.074 ms. Live rendered-frame latency remains outside this standalone measurement. Global SQL substring search and deep OFFSET remain linear diagnostics; actual catalog publication uses keyset pages and ordinary navigation uses cached row identities.

## Native Y2 before/after

[Target samples and artifact identities](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-library-db-y2.json) retain median/p95/worst and every sample. These are standalone native ARM tools in private scratch, not an installed app, rendered-frame or cold-boot measurement. Installed Baseline02: Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`; boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0, MemTotal 951824 KiB. SQLite is 3.53.4 on both sides. All six completed runs verify the same boot, taint and mount generation. Y2DATA uses ext4/eMMC; private benchmark binaries live in `/tmp`, no installed binary is replaced.

1k and 10k have files and DB on Y2DATA. **50k uses two sources: 25k files on Y2DATA, 25k on SD, every SQLite database on Y2DATA.** Available filesystem inodes cannot admit 50k files plus ~2084 album directories on either stock filesystem. The first single-volume 50k attempt exited 1 and cleaned its owned scratch; its older wrapper lost stderr, so the precise failed syscall is unknown. Capacity checks now require free bytes, free inodes and reserves before creating fixtures. No filesystem was resized/formatted or mount/media mode changed. First-source pruning removes roughly 1% of 25k in the split case, rather than 1% of the total 50k. 1k/10k use the pre-split instrumentation; 50k overlays current instrumentation on archived `b71b468` using the checked-in baseline helper. 50k SHA256 transfers are verified and recorded; earlier after-binary hashes were not separately retained. Caches and CPU scheduling/OPP are uncontrolled; no tiny timing speedup is claimed. The observer after the optimized final scan reads ext4 errors_count 0 on DATA, SD and root, taint 0. Both stages finish and clean successfully. At 50k, catalog loading improves 8.6× and no-op/mixed scans 6.6×. Initial population median is 5.7% slower (17.53 → 18.53 s); its p95/worst differs by 1.5%. Prune-only median rises 85.50 → 155.21 ms. These costs are recorded rather than attributed to an unmeasured fsync count.

Milliseconds. Each cell is median / p95 / worst.

### 1,000 tracks: Y2 before/after

| Operation | Before | After |
| --- | --- | --- |
| SQLite initial population | 87.02 / 92.70 / 92.70 | 95.94 / 96.38 / 96.38 |
| Songs page (64) | 1.67 / 2.55 / 3.94 | 1.40 / 1.52 / 2.01 |
| Deep OFFSET page (64) | 3.76 / 4.22 / 4.54 | 3.54 / 4.11 / 4.49 |
| Album contents (≤512) | 1.20 / 1.34 / 1.58 | 0.99 / 1.27 / 1.59 |
| Artist contents (≤512) | 1.06 / 1.20 / 3.23 | 0.87 / 0.99 / 1.20 |
| Artists SQL diagnostic | 0.81 / 0.86 / 1.18 | 0.82 / 0.88 / 1.06 |
| Albums SQL diagnostic | 2.15 / 2.21 / 2.50 | 2.16 / 2.25 / 2.57 |
| Substring-search diagnostic | 4.07 / 4.15 / 4.33 | 4.09 / 4.25 / 4.40 |
| Full catalog load | 20.26 / 20.79 / 20.79 | 17.96 / 19.66 / 19.66 |
| DB open including quick_check | 7.11 / 13.81 / 13.90 | 8.01 / 13.54 / 15.32 |
| Unchanged scan | 168.28 / 341.04 / 341.04 | 62.83 / 82.24 / 82.24 |
| Add + change + remove + move scan | 178.36 / 391.87 / 391.87 | 86.52 / 109.80 / 109.80 |
| Replace identity + read | 1.36 / 1.51 / 2.36 | 0.82 / 2.03 / 2.42 |
| Delete missing (prune only) | 2.94 / 5.01 / 5.01 | 5.61 / 6.81 / 6.81 |

### 10,000 tracks: Y2 before/after

| Operation | Before | After |
| --- | --- | --- |
| SQLite initial population | 2365.02 / 2764.06 / 2764.06 | 2304.26 / 2752.19 / 2752.19 |
| Songs page (64) | 1.70 / 3.69 / 4.28 | 1.47 / 2.59 / 4.42 |
| Deep OFFSET page (64) | 28.77 / 29.55 / 30.27 | 29.01 / 29.82 / 30.52 |
| Album contents (≤512) | 1.20 / 1.36 / 1.72 | 1.01 / 1.51 / 1.76 |
| Artist contents (≤512) | 2.53 / 3.12 / 3.45 | 2.37 / 2.79 / 3.02 |
| Artists SQL diagnostic | 8.31 / 8.58 / 9.14 | 8.43 / 8.59 / 9.35 |
| Albums SQL diagnostic | 24.28 / 24.95 / 27.61 | 24.69 / 25.69 / 29.56 |
| Substring-search diagnostic | 24.21 / 24.64 / 25.34 | 24.25 / 25.08 / 25.50 |
| Full catalog load | 453.41 / 459.60 / 459.60 | 194.49 / 204.90 / 204.90 |
| DB open including quick_check | 50.43 / 53.74 / 54.41 | 51.00 / 52.27 / 54.72 |
| Unchanged scan | 3409.33 / 3569.94 / 3569.94 | 708.30 / 719.72 / 719.72 |
| Add + change + remove + move scan | 3485.70 / 3524.44 / 3524.44 | 720.65 / 752.58 / 752.58 |
| Replace identity + read | 3.91 / 3.98 / 5.15 | 0.74 / 0.82 / 2.46 |
| Delete missing (prune only) | 31.33 / 327.04 / 327.04 | 57.35 / 60.34 / 60.34 |

### 50,000 tracks: Y2 before/after

| Operation | Before | After |
| --- | --- | --- |
| SQLite initial population | 17533.84 / 18511.43 / 18511.43 | 18531.16 / 18797.86 / 18797.86 |
| Songs page (64) | 1.79 / 1.86 / 2.96 | 1.59 / 2.68 / 2.99 |
| Deep OFFSET page (64) | 154.59 / 155.57 / 156.27 | 151.76 / 154.55 / 160.20 |
| Album contents (≤512) | 3.70 / 4.12 / 4.41 | 3.43 / 3.58 / 4.38 |
| Artist contents (≤512) | 8.12 / 9.04 / 9.56 | 7.88 / 8.87 / 9.20 |
| Artists SQL diagnostic | 46.53 / 47.34 / 47.44 | 46.20 / 48.27 / 49.18 |
| Albums SQL diagnostic | 147.40 / 148.41 / 148.86 | 146.85 / 149.92 / 150.97 |
| Substring-search diagnostic | 20.00 / 20.47 / 21.09 | 20.01 / 20.69 / 21.31 |
| Full catalog load | 8641.27 / 8692.88 / 8692.88 | 999.53 / 1047.37 / 1047.37 |
| DB open including quick_check | 235.29 / 239.87 / 248.72 | 233.95 / 236.40 / 247.12 |
| Unchanged scan | 25471.03 / 26626.81 / 26626.81 | 3845.16 / 3902.77 / 3902.77 |
| Add + change + remove + move scan | 25731.81 / 28819.76 / 28819.76 | 3873.91 / 3918.75 / 3918.75 |
| Replace identity + read | 14.82 / 16.80 / 17.92 | 0.83 / 0.96 / 2.64 |
| Delete missing (prune only) | 85.50 / 85.58 / 85.58 | 155.21 / 160.31 / 160.31 |

### Native memory, size and navigation

Peak process RSS includes the full workload, metadata decoder, catalog and up-to-20k queue; it excludes the installed player, compositor/platform services and simultaneous rendering/playback stress. Both sides retain N live rows and N+14 historical rows after seven remove/move mutation samples.

| Tracks | Peak RSS before → after (MiB) | DB before → after (MiB) |
| --- | --- | --- |
| 1,000 | 9.47 → 8.70 | 0.449 → 0.418 |
| 10,000 | 20.92 → 17.52 | 4.227 → 4.125 |
| 50,000 | 49.72 → 38.68 | 21.617 → 20.457 |

The target kernel lacks `/proc/self/io`: target write bytes are unavailable. The original 1k/10k zero sentinel is normalized to null in checked-in evidence; it must not be interpreted as zero eMMC writes. Host I/O counters and persistent UPDATE-abort tests establish the write reduction independently.

| After: native UI catalog workload | 1k median (ms) | 10k median (ms) | 50k median (ms) |
| --- | --- | --- | --- |
| Cold Songs row cache | 3.39 | 29.02 | 178.69 |
| Cold Albums row cache | 1.03 | 17.46 | 115.95 |
| Cold Artists row cache | 0.41 | 6.68 | 32.73 |
| Queue population (at most 20k) | 6.00 | 66.90 | 131.15 |

Cached wheel calls are below 0.01 ms at the median on Y2; the first sample can include a cold route rebuild. Cold grouping and queue construction remain CPU work in the existing Product v2 model, and are not a rendered latency guarantee. The no-op scan now preserves these caches. SQLite requests run on the existing worker; no extra database connection blocks a normal browse route.

## Integrity and validation
  - `cargo fmt --all -- --check`: PASS.
  - `cargo clippy --workspace --all-targets --locked -- -D warnings`: PASS.
  - `cargo test --workspace --locked`: 251 passed, zero failures; library 40.
  - Production SDK `tools/build/cross.sh`: PASS, entire workspace release build for

`armv7-unknown-linux-gnueabihf`, Cortex-A7/NEON hard float, locked/offline. SDK: retained Baseline02 Buildroot output; no kernel or rootfs package built.
  - New 50k test proves full publication, bounded list requests and no duplicates/

omissions at equal-tag/equal-path page boundaries across online/offline media.
  - Real SQLite `max_page_count` exhaustion proves SQLITE_FULL rolls back a whole

batch, including temporary publication markers; restart keeps the old library. Existing injected ENOSPC-style failure remains separately tested. Actual filesystem-full/electrical Y2 destructive experiments are NOT_RUN.
  - A child process is killed with a write transaction open; reopen/quick_check

retains the committed row. Restart before Finish retains old and published new rows; a complete retry prunes correctly with a new TEMP presence set.
  - Malformed negative numeric data rejects catalog reads without quarantine or

deletion; a valid update repairs it. A prior published model remains available on load failure. No silent row-skipping policy is introduced.
  - Additive-index migration collision rolls back the partially created index,

retains user_version/evidence rows and is not misclassified as corruption. Existing v1 index repair, future-schema refusal, corrupt-page quarantine, artifact-set rollback, busy/read-only/permission/I/O and shutdown tests pass.
  - Existing cancellation, decoder failure, root/mount identity loss, replacement

mount, final-writer identity check and finish failure tests pass. New media tests retain offline old-card rows and isolate same-path replacement tracks.
  - Stable EXPLAIN assertions cover ordered/artist seek, identity join and temporary

pruning lookup. Exact planner output text is not frozen as a cross-version API.

Logs/raw runs are retained in the isolated Reborn `out/library-db/`. Host evidence above is checked in; private live-device receipts stay in `out/`. Sanitized target samples are checked in alongside the host results.

## Hardware boundary and remaining limitations

Entry audit used retained real [UART01 evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md). The closing audit/roadmap now use the installed Baseline02 identity above and actual private Y2 measurements. This supersedes the earlier database NOT_RUN label only. It does not supersede UART01 CPU/suspend authority or qualify a whole new image/cold boot. All live access acquired the shared `/tmp/y2-platform-v1-device.lock`; both scratch roots, exact mounted filesystems and boot identity were checked. Owned fixtures and temporary binaries cleaned successfully before normal release. No lock was removed or forced. GitHub #28/#29/#31/#32/#33/#34 remain OPEN at read-only closing review; no epic or milestone is closed. Source-ID production and replacement-card playback lifetime checks remain the separate storage session's integration responsibility. This pass proves generic DB identity isolation and accepts its CID-qualified IDs. Electrical power-loss, actual filesystem-full, sustained endurance, whole-app frame timing, full suspend/battery and 250k physical qualification remain separate.

Intentionally unchanged: schema/file format/index set, WAL/NORMAL, busy timeout, 64-track writes, single connection/service ownership, persistent offline and soft-deleted rows, parser/decoder behavior, file size/mtime reuse criterion, root-FD/mount guards, cached Product v2 route design, queue/session limits, artwork caches, safe shutdown and corruption quarantine. Content-hash rename matching, a fully SQL-paged UI, FTS/genres/recent additions, automatic compaction, irreplaceable playlist data and 250k physical acceptance are outside this pass.

## Files, commits and verdict

Reborn changes: `crates/reborn-library/src/lib.rs`, `platform_tests.rs`, `benchmark.rs`; `app/reborn/src/main.rs`, `app/reborn/src/bin/reborn-bench.rs`; `tools/build/library_db_bench.py`, `tools/build/library_db_baseline.py`; this report, host/target evidence JSON and the report link in `docs/README.md`. Linux changes only its standing gap audit and Platform v1 roadmap. No main-tree edits or external writes.

Commits: `9152005` reproducible baseline instrumentation; `b0b114e` bounded scan/catalog implementation and fault tests; `eca41fc` UUID-less compatibility; `25d4ea4` schema/durability assertions; `d6c92b1` unchanged-scan catalog preservation; `c161404` split-source fixture and baseline adapter; the validation/documentation commit is recorded in the handoff. Existing configured Linux identity matches Reborn's prior author/committer and is used for commits without changing Git settings.

**Platform 1.0 library/database: PASS for the measured host and bounded native Y2 workloads through 50k.** Changes preserve the existing SQLite ownership, schema and index set. Large no-op/mixed scans and complete catalog loading improve substantially; ordinary seek queries are preserved, prune-only costs regress and are recorded. Production integration must combine the separate storage SourceID/playback guard and FFmpeg parser revision work before release. This does not close the whole Platform 1.0 milestone or certify electrical power loss, cold boot or 20k+ queues.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
