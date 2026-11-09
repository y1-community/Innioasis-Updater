---
title: "Y2 Platform 1.0 USB / desktop file transfer - Innioasis Updater"
description: "Y2 Platform 1.0 USB / desktop file transfer Date: 2026-10-04. Branch: codex/platform-v1-usb , isolated Y2Linux and Y2Reborn worktrees. No flash, push, filesystem migratio"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-usb.html"
---

# Y2 Platform 1.0 USB / desktop file transfer - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Platform 1.0 USB / desktop file transfer

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Platform 1.0 USB / desktop file transfer

Date: 2026-10-04. Branch: `codex/platform-v1-usb`, isolated Y2Linux and Y2Reborn worktrees. No flash, push, filesystem migration or owner-main modifications. Status: MORE_WORK_REQUIRED pending exact-image physical/desktop acceptance. Software evidence and candidate identity are recorded in `out/usb-validation/`.

## Evidence and previous behavior

The preceding qualified hardware reference is UART01 Linux `e9e8d63`, Reborn `b71b4688`, kernel `6.18.0-y2linux-cpu-c3-uart-01`, root v1.20, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0. Its retained receipt proves three bounded 1 MiB bidirectional checksum rounds and C1/C2/C3, not throughput or a portable-media device. Baseline02 software qualification is separate from that preceding image. A later retained locked Bluetooth receipt now identifies installed Baseline02, compiled Linux `8584ccd8` / Reborn `b71b4688`, root v1.21, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint0. Its saved identity receipt SHA256 `eb2fd0f0377e25c5a848b6aa02e9cabe3bf6af4a2089ed146670d36f6999f07d` matches the subsystem evidence. This is another session’s locked observation, not a USB benchmark or a new automatic C3 cold-boot qualification. See [UART01 physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

Previously the built-in `g_cdc` exposed ACM serial and ECM networking. Dropbear and OpenSSH SFTP served authenticated root access over usb0. Those descriptors contain no storage/MTP interface: a desktop has no disk or portable-media function to mount. Knowing an IP address and having an authorized SSH key were prerequisites.

All attempted current-device batches acquire `/tmp/y2-platform-v1-device.lock` with nonblocking flock. The lock has been occupied; the scratch baseline receipt records `NOT_RUN_DEVICE_LOCK_BUSY`. No device access occurred outside that lock. There is no current enumeration, negotiated-speed or transfer-performance claim.

## Protocol decision

| Approach | Evidence / decision |
| --- | --- |
| MSC/BOT, exclusive handoff | Normal disk discovery, but ext4 internal data lacks native Windows/macOS mounting; Y2DATA also holds settings, SSH and library state. Raw Y2DATA would expose private contents and stop the player. SD would need playback/scan quiescence, verified unmount, host eject/dirty-removal checks and remount. Rejected for this product pass. |
| MTP, file-level | Hides filesystem implementation and app-private data; Linux remains the only block owner; playback can continue using completed files. Lightweight C FunctionFS responder selected with additional confinement/durability/error patches. |
| Existing ECM + SFTP | Useful authenticated advanced path retained unchanged in security policy. Manual network discovery does not satisfy normal desktop use. No measured bottleneck authorizes TCP/cipher/fsync tuning. |
| Composite MTP + ECM | Fits current four nonzero MUSB endpoints using two bulk pairs and two 16-byte interrupt endpoints. MTP is linked first, with Windows compatible-ID OS descriptors. Actual host/controller enumeration remains a physical gate. |
| ACM + ECM + MTP | Exceeds the current endpoint/FIFO allocation; rejected. Disconnected-session developer mode retains ACM + ECM. |

The controller has five endpoints including EP0. EP1/EP3 provide 512-byte TX/RX; EP2/EP4 provide 16-byte TX. Existing 2,144-byte FIFO allocation is unchanged. FunctionFS remaps logical descriptor endpoint numbers. FS bulk descriptors use 64 bytes, HS 512 bytes; interrupts use 16 bytes. No SuperSpeed claim. OS descriptor compatible ID `MTP`, interface class 6/subclass 1/protocol 1 support Windows WPD binding; enumeration must be checked on Windows. Configfs binds only after the responder has written descriptors and exposed all three endpoints. Binding or responder failure is explicit and retries at most five times. A readiness restart unbinds its existing configfs gadget before configuring; parent death kills the old responder to release endpoint/root FDs. The legacy boot-controlled g_cdc is disabled in production; configfs serves both product and developer selections.

Upstream uMTP-Responder is pinned at `2241a803c27f1fff7537cb9504befeb810b880d3`, source SHA256 `077ef6f4745d599bda7db0fff2993e21b969bbf414784c4ab3adf0f664177d2b`. It is a small GPL-3.0+ C program using pthread/rt, without a desktop framework. The older external-toolchain UAPI is supplemented with pinned Linux 6.18 openat2 definitions and the freshly generated ARM EABI syscall header, preserving fail-closed confinement instead of using a weaker path-resolution fallback. 64 KiB USB buffers and the existing 1 MiB cache setting are bounded; the process has a 64 MiB address-space ceiling. Handles are discovered lazily. The ceiling is a protection, not measured RSS or proof of arbitrary library-size acceptance. Partial-edit vendor extensions are not advertised or accepted; complete object copy, directory creation, deletion, rename and downloads are supported.

Primary references: [kernel mass-storage backing-file contract](https://docs.kernel.org/usb/mass-storage.html), [FunctionFS descriptors and lifecycle](https://docs.kernel.org/usb/functionfs.html), [uMTP-Responder source/project](https://github.com/viveris/uMTP-Responder), [Windows MTP driver association](https://learn.microsoft.com/en-us/windows-hardware/drivers/portable/the-mtp-setup-information---inf--file).

## Storage, ownership and compatibility````````

| Host view | Backing identity | Access |
| --- | --- | --- |
| Y2 / Internal Storage | Only /data/music within ext4 Y2DATA, UUID 79324c69-6e75-4801-8000-000000000102, internal 11230000.mmc partition start 2,104,320 sectors, length 1,638,400 sectors (800 MiB) | Completed user files only. No /data/reborn, SSH, settings or other private directories. |
| Y2 / SD Card | /media/sd, only after the existing validated SD mount claim, boot/mount ID, dev_t, sysfs instance, controller 11240000.mmc and CID/UUID/filesystem identity | Existing ext4, FAT32 or exFAT card. Missing, failed/dirty/unmounted/replaced card has no view. Read-only media is advertised read-only. |

Protected partitions, raw complete eMMC, BOOTIMG/Y2ROOT, preloader/LK, calibration, NVRAM/PROTECT, factory data and partition tables have no host view. MSC is disabled in the production config and no block-export function is selectable. UUID alone cannot select an internal view: geometry, controller, mount and ext4 must match. No card or internal data is reformatted or migrated.

Linux owns the block devices before, during and after transfer. The host owns an MTP session and never mounts the filesystem block device. Consequently there is no block handoff, live dual writable mount, filesystem remount or post-host fsck. The existing platform refuses checks on mounted media and uses non-destructive checks on unmounted SD; a dirty/failed mount is not promoted by USB.

The responder pins approved directory file descriptors once per lifetime and uses Linux `openat2` with BENEATH/NO_SYMLINKS/NO_MAGICLINKS/NO_XDEV. Traversal, symlinks, nested mounts, device/special files, internal root/private paths and regular hardlinks are refused. Directory mutations use verified parent FDs. Media identity changes first unbind the gadget and stop the old responder, then create a fresh view; pinned old roots cannot resolve into a replacement card. Device-side SD eject refuses a connected host, drops the disconnected responder's SD pins via the readiness owner, and calls ordinary unmount. Active local handles or failed unmount remain failures; no forced/lazy unmount exists.

Physical USB access intentionally grants management of these user files without an SSH key, like a portable media player. Advanced ECM/SFTP stays key-only with pinned host keys, entropy gating, no password/forwarding and usb0 binding. The existing owner-local development VID/PID and serial are retained; this is not a new public USB identity allocation. Charger voltage/current policy is unchanged.

## Host experience``

| Host | Intended behavior / exact requirements | Qualification |
| --- | --- | --- |
| Linux GNOME | Standard portable-media discovery through GVfs MTP/libmtp; Files shows Y2 and storage views. Install distribution gvfs-mtp support if absent. MTP is a file-manager virtual location, not a kernel block mount. | GIO/libmtp tools present; GVfs MTP backend absent on this host. Exact new-image desktop discovery NOT_RUN. |
| Linux KDE | Dolphin uses its MTP KIO/libmtp support; install the distribution MTP KIO worker if absent. UDisks block automount is not involved. | KDE MTP plugins are installed on this host; enumeration NOT_RUN. |
| Windows | Explorer portable-device view expected through inbox WPD/MTP driver and compatible-ID descriptors. ECM networking support is separate and unnecessary for music copies. | Descriptor bytes tested; Windows enumeration NOT_RUN. |
| macOS | Finder does not natively provide this MTP view; a standard MTP client such as OpenMTP is required. Advanced SFTP remains an option where ECM is usable. | NOT_RUN; native Finder mounting is an explicit limitation. |

See [GNOME GVfs MTP backend](https://wiki.gnome.org/Projects%282f%29gvfs%282f%29backends.html), [Windows portable-device drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/portable/wpd-drivers-overview) and [OpenMTP project](https://github.com/ganeshrvel/openmtp). Windows/macOS filesystem support does not affect the MTP view: Linux interprets ext4/exFAT/FAT32. FAT32's per-file size limit still applies. SD >4 GiB object sizes use 64-bit accounting/streaming; actual large-file and client acceptance is pending.

## Integrity, cancellation and errors

Uploads go to private `.y2-mtp-PID-serial.part` files under the pinned destination parent. The host/library cannot list them as music. Known-size copies must match exactly; cancellation, short/disconnected input, write failures and low-space failures abort staging. Unknown-size uploads use 64-bit counters and short/ZLP termination. Before success: fsync file, atomic no-replace rename, fsync parent. A racing writer/existing destination is preserved. The 96 MiB and 128-inode reserve is checked at admission and every write. Storage-full/read-only causes are preserved across cleanup and mapped to protocol errors; admission failures also publish a bounded error receipt for Reborn. Replacing an existing filename requires an explicit delete or a new name; no in-place truncating overwrite.

Downloads use a pinned verified inode, range checks, checked pread/write loops and negotiated endpoint ZLP handling. Concurrent local truncation is a failed transfer, never stale/zero-padded bytes reported as success. Local playback can continue; deleting a playing file has normal Linux open-inode behavior.

Normal cancellation/disconnect discards only the private incomplete stage. An abrupt process kill or device power loss may retain a hidden `.part` file; it is not published or automatically destructively repaired/deleted. Inspect it when needed. A directory fsync failure after rename returns an error; a complete published file may exist without acknowledged durability. Inspect its hash before retrying. No storage device can guarantee protection against electrical power loss; this design removes concurrent host/Linux block ownership and acknowledges success only after checked filesystem durability.

A host session close/eject ends file transfers without removing Linux ownership. Cable removal triggers a library generation and the responder rebuilds session handles on reconnect. Mid-copy failure is explicit. SD removal errors stop the old view; I/O or remount/check failure is surfaced through existing storage state. Transfer error records contain errno/state, no filenames or secrets. Reborn uses friendly ready/copying/interrupted messages and reconnect/retry guidance.

## DMA, PIO, link and power audit

Current source uses Inventra RX mode 0 (packet-sized DMA) and existing upstream TX handling/cache mapping/alignment/short/ZLP/abort mechanics. The existing DMA bus-error abort and progress-aware storm guard are preserved. Fix03 counts successful DMA programming as progress; unchanged no-progress limit 512 IRQs/jiffy and hard rate ceiling bound stalled/status storms. Successful PIO FIFO reads/writes were missing from this progress counter. Patch 0065 adds actual moved bytes as progress and separate RX/TX byte diagnostics. Zero-byte moves do not reset a stall. Regression tests distinguish DMA/PIO progress from stalled sources and verify terminal protection, disconnect/reconnect and PIO fallback.

Negotiated speed is reported from actual UDC `current_speed`, never inferred from nominal USB 2.0 capability. Diagnostics expose mode/functions, errors, DMA programs, PIO bytes and IRQ guard counters. Current physical speed is NOT_OBSERVED. PIO-disabled-DMA acceptance and RX/TX performance are PHYSICAL_NOT_RUN. No DMA/FIFO/cipher/buffer optimization is justified without a real baseline.

Existing cable-session runtime PM is preserved. Disconnected USB can gate and allow deep CPU idle; attached session references retain existing conservative power policy. No new periodic polling thread is added: USB supervision shares readiness cadence (3 s awake / 10 s dark); SD eject has a signal wake. No new attached-idle power improvement, electrical measurement or full-suspend claim.

## Performance and test results

| Workload | Before: SFTP/ECM read/write MB/s | After: MTP read/write MB/s | CPU / IRQ/s / switches/s |
| --- | --- | --- | --- |
| 1, 16, 128, 512 MiB sequential | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED |
| 100 and 1,000 small files | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED |
| Real mixed FLAC/MP3 corpus, sustained copy | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED |

The physical lock prevented the installed-image baseline, and the candidate is not installed. Retained 1 MiB checksums are integrity evidence only. There is no claimed performance gain, DMA ceiling or arbitrary target. The harness records actual speed, bytes/time (decimal MB/s), independent upload/download SHA256, aggregate CPU average, IRQ/context-switch deltas, memory snapshots, USB counters and storage statistics, per-process CPU/RSS with PID-reuse rejection and process-lifetime HWM labels, and actual frequency snapshots. It leaves uncertain scratch data after failure; identity changes refuse further copy/cleanup. SFTP uses one authenticated session per workload so small-file numbers are not SSH-login-per-file benchmarks.

Native tests compile the pinned patched responder and execute actual FunctionFS FS/HS/MS-OS descriptor emission, SendObjectInfo/SendObject and download code. Fault injection covers EINTR/short writes, ENOSPC, fsync failure, cancellation, truncated data, disconnect/new session, local truncation, racing publication, traversal/symlinks/special files, 64-bit accounting and 100 small-file hashes. Platform tests cover protected geometry/functions, descriptor-before-bind, Linux-only ownership, missing/dirty/RO/replaced media, bind/death retry bounds, connected SD eject refusal, durable rescan generations and restart/disconnect. Reborn coalesces durable events, waits for copy/scanner/media stability and queues the existing incremental scan; it preserves the database and duplicate prevention. No scan sees an unfinished music file. Full Reborn fmt/clippy/workspace tests and rendered ready/copying/error/refresh fixtures are part of software verification.

## Candidate and owner acceptance boundary

Fresh kernel/Buildroot/Reborn ARM build and config/DT/modules/ABI checks PASS. Compiled Linux `08019df44c8a7fbc249fc49a5a41f7ac906429ba`, Reborn `51d477b2f30edfc90418d8d0c3fa5fad8de6f581`. Kernel `6.18.0-y2linux-platform-v1-usb`, root `2025.02.18-platform-v1.22`, release `1.0.0-usb-candidate.1`, build `Y2LINUX-PLATFORM-V1-USB`. The responder ARM binary is 96,092 bytes; runtime RSS remains unmeasured.

411 production checks: 406 PASS, 5 minimal-host dependency skips. Separate native host filesystem/GIO (27) and ALSA (3) checks cover those dependencies. Focused USB/storage/DMA/platform tests (79), final harness guards (6), Reborn tests (240), fmt/clippy, Cortex-A7 QEMU, installed ARM tools/library scan, ELF dependencies, release inventory and legal-info PASS. UI detection found no reported issues; rendered ready/copying/error/refresh fixtures were inspected. No warning-free, public-distribution or physical acceptance claim follows from legal collection.

One final preserving candidate: `out/y2linux-platform-v1-usb-candidate/`. The compiled source pair remains the image identity. Later documentation and qualification-harness revisions are attached separately and do not change images. Only BOOTIMG and ANDROID/Y2ROOT are selected; preserve USRDATA/Y2DATA and every protected partition. Keep the accepted UART01 fallback pair. No agent flash/push. Candidate software/package receipts do not qualify new-image hardware.

After owner-controlled preserving installation, the single harness is:`python3 tools/usb/qualify.py --run --protocol sftp --package out/y2linux-platform-v1-usb-candidate --output out/usb-validation/installed-sftp python3 tools/usb/qualify.py --run --protocol mtp --mtp-uri 'mtp://[usb:BUS,DEVICE]/Internal Storage' --package out/y2linux-platform-v1-usb-candidate --music-corpus /owner/test-music --output out/usb-validation/installed-mtp`

To measure SD, add `--volume sd` and use the SD Card URI. Writable validated mount identity is required before creating scratch directories. The harness records each file's host-before, device-after-write and host-after-read SHA256. Use the actual GIO URI shown by the desktop, pinned owner SSH config if needed (`--ssh-config PATH`), and a fresh output each run. The four-minute batch deadline may report partial coverage; run remaining cases separately with `--sizes` / `--small-files` and record skipped reserve limits. No existing music is deleted.

Remaining physical acceptance: verify first cable enumeration and both views in normal Linux Files/Dolphin; compare both matrices; host eject and reconnect ten sessions; interrupt a scratch copy by pulling cable; verify no published partial, no filesystem error and subsequent hash-matching copies; SD absent/RO/replaced using owner test media without formatting; verify incremental Reborn refresh/new music/playback after copies; PIO fallback with DMA disabled through the existing qualified control; bound USB errors and CPU/IRQ/memory load; record actual Windows and macOS client results where available. Full-system suspend and electrical charger/idle measurements remain separate platform gates.

Until those exact-image checks pass: MORE_WORK_REQUIRED. MTP/macOS client support, existing-file no-overwrite behavior, external Linux directory changes requiring host refresh/reconnect (inotify disabled to hide staging) and public USB identity allocation remain explicit product limitations. Five consecutive responder/bind failures exhaust the retry budget; restart Y2/readiness to retry a persistent service failure. Ordinary interrupted sessions recover on reconnect.

## Changed files and local commits

Y2Linux (33 files, including the final evidence record):
  - `buildroot/Config.in`
  - `buildroot/configs/y2_production_defconfig`
  - `buildroot/package/y2-mtp/0001-y2-safe-media-transfers.patch`
  - `buildroot/package/y2-mtp/Config.in`
  - `buildroot/package/y2-mtp/y2-mtp.hash`
  - `buildroot/package/y2-mtp/y2-mtp.mk`
  - `docs/architecture/platform-usb-v1.md`
  - `docs/planning/platform-v1-roadmap.md`
  - `docs/planning/roadmap-gap-audit.md`
  - `docs/validation/Y2-PLATFORM-V1-USB.md`
  - `kernel/config/production.config`
  - `kernel/patches/0065-y2-musb-pio-progress.patch`
  - `kernel/patches/manifest.json`
  - `kernel/platform/usb.c`
  - `kernel/usb/fault.h`
  - `tests/test_cpu_fix03.py`
  - `tests/test_usb_product.py`
  - `tests/usb_mtp_fs.c`
  - `tests/usb_mtp_protocol.c`
  - `tools/platform/capabilities.json`
  - `tools/platform/y2_platform/cli.py`
  - `tools/platform/y2_platform/media.py`
  - `tools/platform/y2_platform/observe.py`
  - `tools/platform/y2_platform/service.py`
  - `tools/platform/y2_platform/usb.py`
  - `tools/production/build.py`
  - `tools/production/release.json`
  - `tools/production/tests.sh`
  - `tools/usb/mtp-safe.c`
  - `tools/usb/mtp-safe.h`
  - `tools/usb/qualify.py`
  - `tools/validation/dev_artifacts.py`
  - `docs/validation/evidence/platform-v1-usb.json`

Y2Reborn (7 files):
  - `app/reborn/src/bin/reborn-preview.rs`
  - `app/reborn/src/main.rs`
  - `crates/reborn-core/src/platform.rs`
  - `crates/reborn-platform/src/client.rs`
  - `crates/reborn-platform/src/storage.rs`
  - `crates/reborn-ui/src/pages.rs`
  - `crates/reborn-ui/src/tests.rs`

Local implementation commits: Linux `418723d` (MTP/media/product integration), `5cb5be0` (configfs-only selection and supervisor lifetime), `6fcd1b2` (preserved error causes and latest retained evidence), `08019df` (pinned kernel UAPI/ARM ABI). Reborn `51d477b` implements typed states and incremental refresh. Linux `d9ea222` records qualification and the guarded transfer matrix; the subsequent closing commit adds expanded harness diagnostics, path inventory and this final evidence. Images compile exactly Linux08019df / Reborn51d477b; later qualification/docs commits are not represented as newly compiled binaries. All commits are local; existing configured owner identity is preserved, with no model attribution or push.

Final payload SHA256:
  - BOOTIMG: `b1b9dc1ec000159cb9d9c75327ab6d60aa32f29ffe476ab8450f7850e76fc9c4`
  - Y2ROOT: `cf0a4eccbd30cb556bb28d3ca7d145a8a75e968e24b1fbaf70d31b3dcaed9c52`

The preserving package, source/license seal and final checksum/rootfs/package validation PASS. Source delivery contains449 source/license records and their collector limitations; public distribution/USB identity/legal approval is not claimed. Native hardware proofs remain scoped to their preceding artifacts. The latest exact-image transfer harness is attached separately with its own revision and SHA256. No physical flash, push or modification to owner-main files was performed by this pass. Candidate handoff is `USB-OWNER-HANDOFF.md` inside `out/y2linux-platform-v1-usb-candidate/`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
