---
title: "Storage lifecycle, space and measurements - Innioasis Updater"
description: "Storage lifecycle, space and measurements <!-- knowledge-base-scope: source-contract -- Source-contract scope. This page describes software ownership and interface behavi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-storage-v1.html"
---

# Storage lifecycle, space and measurements - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Storage lifecycle, space and measurements

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Storage lifecycle, space and measurements > **Source-contract scope.** This page describes software ownership and > interface behavior. See [current state](../CURRENT_PLATFORM_STATE.md) for the exact latest image > and physical limits; implemented or enabled does not mean qualified. 

`/data` is persistent internal Y2DATA; `/media/sd` is optional removable media. The root/data identity checks and partition geometry remain unchanged. All SD mounts use the existing 11240000.mmc controller, one unique supported filesystem, and `nosuid,nodev,noexec`. FAT/exFAT also use private file/directory masks. FAT uses `utf8=1` for UTF-8 long filenames; the kernel retains CP437 short-name support.

Mount claims use `block:<major>:<minor>:diskseq:<N>`. The Linux disk sequence number persists across kernfs inode reclamation and changes on every card re-enumeration, including reinsertion of the same CID. Missing diskseq fails closed. Reborn must ship the matching claim consumer; update both together. Managed SD library source keys include the validated CID/geometry/filesystem identity hash so two cards with the same filesystem UUID do not share a library source. Existing UUID-only source records are retained offline; the first scan with the paired update creates the physical-card source. UUID remains the user-visible filesystem identity. UUID-less whole-card FAT is identified by CID, size and a zero start offset. No data or schema migration is performed here. Playback checks the live validated source ID for the current and queued tracks, then walks from a pinned source directory without following symlinks. Root mount ID, each parent and final file must remain on that mount/device; only regular files are admitted, with nonblocking opens to reject FIFOs without waiting. The decoder opens the pinned file through `/proc/self/fd` and retains file/parent descriptors until native close. Header probing preserves all 33 valid audio fixtures without a filename extension. Sidecar artwork uses a similarly checked regular file in the pinned parent; JPEG/PNG/WebP decode identically. The bounded local image loader uses a 12-byte signature fallback for descriptor paths without a suffix, retaining the same codecs, limits and ABI. Ship app/native media together. An old UUID-only queue cannot reopen a same-named file on another card; no automatic rebinding. Symlink music/sidecars and nested mounts are deliberately unavailable through this managed-source admission.

`y2-media mount|unmount|status|check` is the lifecycle interface. Before mounting, a bounded 60-second read-only filesystem check must pass; reported uncorrected faults, timeouts and card-instance changes prevent mounting. Mount preflight uses `e2fsck -n`, `fsck.fat -n` or `fsck.exfat -n`; explicit ext4 `check` forces a complete `e2fsck -f -n` pass. Checker success follows that tool's filesystem semantics; no repair command is invoked. Normal ext4 journal behavior remains the kernel's responsibility. Large media may require an owner-directed offline check when the bounded preflight times out. Mount publishes a boot-scoped mount ID, major/minor, UUID and CID claim. Status rejects missing sources, changed UUIDs, missing claims and replacement mounts. Failed unmount retains its claim and reports failure; there is no force/lazy unmount or new mount stacked over the old one. Insertion callers must retry only after the old mount has gone. `check` is an explicit, bounded, read-only check of unmounted media. Repair and formatting are never automatic.

exFAT uses Linux 6.18's in-tree driver and Buildroot's pinned exfatprogs 1.2.5: source SHA-256 `f27160dcc1ddd17c96cd41a6ceef7037adc2796ab5c5633d3d85cf532c3ee2f0`, license hash `8177f97513213526df2cf6184d8ff986c675afb514d4e68a404010521b880643`. No proprietary implementation is introduced. Upstream supplies the [GPL tools](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fexfatprogs%2Fexfatprogs%2Fblob%2Fmaster%2FREADME.md); Microsoft documents [Linux exFAT integration](https://opensource.microsoft.com/blog/2019/08/28/exfat-linux-kernel). ARM/image validation and actual cards remain separately gated. No bus mode, clock, voltage or electrical assumption changes with this filesystem option.

`y2-platform space` publishes admission decisions in `/run/y2/storage.json`. Cache, diagnostic and update allocations require Normal space and at least 96 MiB remaining; user-state/database checkpoints may use the reserve down to 32 MiB. Neither policy can make a failing filesystem writable. Applications must retain write failures as failures and may not promise persistence based only on this advisory snapshot. An allocation can race another writer.

`y2-platform space --cleanup` acts only on verified Y2DATA in LowSpace or CriticalSpace. It removes at most 64 files / 8 MiB per invocation, only old named Reborn artwork-cache files, old named diagnostic archives (retaining the newest two), and named platform temporary cache files. All must be at least one day old. Descriptor-relative opens refuse symlinks and subordinate mounts; music, database, settings, bonds, keys and update transactions are excluded. No image's nominal total flash size substitutes for Y2DATA's actual budget.

`y2-platform bench-storage --volume /data` or `--volume /media/sd` creates a unique run directory under that volume's `.y2-bench`. Only newly created files are accessed or removed. Directory descriptors pin operations to the original filesystem; mount generation is rechecked between operations. Bounds are 1–128 MiB, 1–1024 operations and a 1–1800 second deadline (defaults 16 MiB, 64 operations, 300 seconds). At least max(96 MiB, 10%) remains reserved before starting. No raw block test, global cache drop, format or real-library write.

Sequential and random read/write use 4/16/64 KiB and 1 MiB transfers with nonzero readback verification. Results distinguish buffered operations and file-scoped advisory cache eviction. Write throughput includes final fdatasync; operation latency distributions describe individual calls. Separate file fsync/fdatasync, create/stat/rename/delete and file-fsync/rename/directory-fsync transactions have p50/p95/p99/max, operations/sec and decimal MB/sec. Unsupported directory fsync is Unavailable, never a durability pass. Collection/identity-check overhead is included in throughput. An I/O error or deadline retains completed results and marks the run FAILED. Kernel uninterruptible I/O remains outside userspace deadline guarantees. Scratch remnants from killed runs are not auto-deleted.

Each storage measurement records passive aggregate CPU busy percent (all cores, idle and iowait excluded), IRQ deltas and negotiated MMC state/error counter deltas. Missing/reset counters are unavailable, never zero. A positive fault/fallback/reset delta stops the benchmark even if kernel retries completed the request. Small-file creation includes file fsync and final directory fsync. Five distinct offset/size regions are fsynced, then file-scoped cache eviction is requested and SHA256 verified after all writes to detect address aliasing. Platform status also exposes cached media operation/checker failures, passive runtime-PM counters, runtime status and recorded tuning maps; it never reads the register diagnostic that resumes MMC. The driver's passive mode line includes fallback origin/reason and card driver type. Existing detailed raw register/fault diagnostics remain explicit reads.

These are measurement tools, not target measurements. Physical SD removal, full media, filesystem errors, card compatibility, long I/O tails and flush / electrical power-loss durability remain PHYSICAL_GATE. Host process-crash recovery must never be presented as electrical durability.

Resource/library collection: `y2-platform bench-library --tracks 20000 --scan` uses only a new `/data/.y2-bench/run-*` directory (or explicit `--volume /media/sd`). `y2-platform collect --seconds 28800 --interval 10 --warmup 300 --pid PID --pss --reborn --workload wired-playback` streams records to stdout. Redirect output on the SSH host, not onto nearly full Y2DATA. The collector does not start playback. A process in uninterruptible kernel I/O can outlive a userspace deadline; mount identity checks and FD-relative cleanup prevent writing to its replacement.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
