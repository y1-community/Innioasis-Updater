---
title: "Production Storage v1 — Storage03 manual correction candidate - Innioasis Updater"
description: "Production Storage v1 — Storage03 manual correction candidate <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate id"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-production-v1-r3-deployment.html"
---

# Production Storage v1 — Storage03 manual correction candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Production Storage v1 — Storage03 manual correction candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Production Storage v1 — Storage03 manual correction candidate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

All three payloads are rebuilt/generated and validated offline. Physical boot, USB enumeration and power-entry correction are NOT established. The owner cannot provide further device data; no additional evidence request is required to build this candidate. [Correction rationale](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage03-corrections.md).

Storage03 corrects cable-present USB startup with checked MT6582 PHY recovery, handles bounded MMC transfers and idempotent user-area reselection, avoids boot partition probing and makes rescue readable without SD. The exact rejected command in DIAG01 remains unknown because the photo truncates it. The reported off-state button/power behaviour has no proven cause or verified fix; stock loaders, PMIC power entry and battery controls remain unchanged.

Use the new Storage03 folder. BOOTIMG and Y2ROOT must match because the root contains its DRM module. Y2DATA remains schema 1 and is compatible with Storage02: the generated template is for explicit fresh initialization, not a required persistent-data reset. Use the preserve-data profile to retain existing Y2DATA. No assistant physical write or SPFT execution occurred.
  - Build Git commit:`48458605db5f53bd188921d53359e470f1e8bf05`.

Canonical project SchulzCode/Y2Linux; existing Luca/SchulzCode identity retained. Later evidence-only commits do not change these built bytes.
  - Exact stock map and 3. classification of every entry follow. All normal

starts are physical EMMC_USER bytes; the full machine-readable map includes distinct scatter linear values, stock runtime mappings and provenance.
``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| Stock partition | Class | Physical start | Scatter linear start | Stock span |
| --- | --- | --- | --- | --- |
| PRELOADER | KEEP | 0x0 | 0x0 | 0x1400000 |
| MBR | KEEP | 0x0 | 0x1400000 | 0x80000 |
| EBR1 | KEEP | 0x80000 | 0x1480000 | 0x80000 |
| PRO_INFO | KEEP | 0x100000 | 0x1500000 | 0x300000 |
| NVRAM | KEEP | 0x400000 | 0x1800000 | 0x500000 |
| PROTECT_F | KEEP | 0x900000 | 0x1d00000 | 0xa00000 |
| PROTECT_S | KEEP | 0x1300000 | 0x2700000 | 0xa00000 |
| SECCFG | KEEP | 0x1d00000 | 0x3100000 | 0x20000 |
| UBOOT | KEEP | 0x1d20000 | 0x3120000 | 0x60000 |
| BOOTIMG | REUSE | 0x1d80000 | 0x3180000 | 0x1000000 |
| RECOVERY | KEEP | 0x2d80000 | 0x4180000 | 0x1000000 |
| SEC_RO | KEEP | 0x3d80000 | 0x5180000 | 0x600000 |
| MISC | KEEP | 0x4380000 | 0x5780000 | 0x80000 |
| LOGO | KEEP | 0x4400000 | 0x5800000 | 0x300000 |
| EBR2 | KEEP | 0x4700000 | 0x5b00000 | 0x80000 |
| EXPDB | LEGACY | 0x4780000 | 0x5b80000 | 0xa00000 |
| ANDROID | REUSE | 0x5180000 | 0x6580000 | 0x33400000 |
| CACHE | LEGACY | 0x38580000 | 0x39980000 | 0x7e00000 |
| USRDATA | REUSE | 0x40380000 | 0x41780000 | 0x32000000 |
| FAT | LEGACY | 0x72380000 | 0x73780000 | 0x0 |
| BMTPOOL | UNKNOWN | 0xffff00a8 | 0xFFFF00a8 | 0x1500000 |

PRELOADER is EMMC_BOOT_1: the scatter's20MiB span is a vendor abstraction, not a physical readback length; each boot hardware region is4MiB. BMTPOOL's sentinels remain UNKNOWN/unapproved. FAT's zero scatter span resolves physically to0x15dc00000 bytes and may contain user media; leave it alone. EMMC_USER capacity historically exported by Android is 7,784,103,936 bytes (0x1cff80000). DA reports physical capacity 7,818,182,656 bytes (0x1d2000000). The unallocated difference remains untouched; DIAG01 physically confirms the same 15269888-sector native Linux capacity. Preserve MBR/EBR1/EBR2; no repartitioning occurs.

[Full source-backed classification/dependencies](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fproduction-storage-v1.md) · [Machine-readable map](https://github.com/schulzcode/y2linux/blob/HEAD/docs/architecture/production-partitions.json).
  - Y2ROOT choice: ANDROID, ext4 LABEL=Y2ROOT.
  - Original purpose/name: stock ANDROID `/system`, historically stock Linux p5.
  - Physical start: 0x05180000 =85,458,944 bytes; scatter linear0x06580000.
  - Partition size: 0x33400000 =859,832,320 bytes (820MiB).
  - Raw Y2ROOT image size: 536,870,912 bytes (512MiB).
  - Raw Y2ROOT SHA256:`9bca0d4492568f96a24beecc65ded88005e9eccb0ae214a4cc3084861fcc44ed`.
  - Y2DATA: stock USRDATA (`/data`, historical p7), physical0x40380000

=1,077,411,840 bytes, size0x32000000 =838,860,800 bytes (800MiB). ext4 LABEL=Y2DATA mounted /data; initializes Android data on first install. UUIDs are79324c69-6e75-4801-8000-000000000101 (root) and 79324c69-6e75-4801-8000-000000000102 (data). Root detection checks native internal host and stock geometry, not fixed mmcblk numbers.
  - BOOTIMG, 12. scatter, 13. manifest, and filesystem transports:

All files below are in `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-production-v1-r3/`.``````````````

| File | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 5193728 | 499d7c3f839eeaafc4c3f79d0b38bc9af9ff1589cce368f24f7f9802380e9190 |
| Y2ROOT.img | 536870912 | 9bca0d4492568f96a24beecc65ded88005e9eccb0ae214a4cc3084861fcc44ed |
| Y2DATA.img | 838860800 | 01bcf65da1716081707202af074969e21fc1196540cb1de6ca76ef9098d44079 |
| MT6582_Android_scatter.txt | 7616 | 68ef5f895da993d40b720243c58b7591809ec39fce32626d39e628475fe57909 |
| MT6582_preserve_data_scatter.txt | 7617 | efb04b860e6a1e907e25d407bdb3f98d29b1da7651b0dbe55a2dd679ddd1e9e3 |
| manifest.json | 7304 | 87e51da6f1b84b382a020516bf64b06a637643ea66408ce43453f2a67d47e58c |
| SHA256SUMS | 2143 | 1a83d5e4094dab868e04d481b33dbd5123a749d8fbdc61e3bf8b928deeaed432 |

The scatter maps Y2ROOT.img and Y2DATA.img directly as raw ext4; there are no .spft.img payloads in this package. The transfers are 512 MiB and 800 MiB, respectively, and take longer than the failed compressed transport. Every written image byte has a defined hash. BOOTIMG is raw at physical 0x01d80000 within its 16 MiB span. The first scatter selects BOOTIMG/ANDROID/USRDATA; the preserving profile selects BOOTIMG/ANDROID only.
  - Restoration material for every overwritten partition: verified original

FM sources below exist locally in `/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/`. They restore factory Android, not personalized installed Android state. Preserve a private USRDATA readback before install if original settings/apps must be recoverable; likewise ANDROID if its modifications matter. Keep an independent accessible copy of recovery material. No full-ROM rebackup needed.
``````

| Overwritten partition | Verified stock source | Bytes | SHA256 |
| --- | --- | --- | --- |
| BOOTIMG | boot.img | 5656576 | 5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6 |
| ANDROID | system.img | 518590232 | 5a7a92f3a95374f31abe8b3ddbd68c5c2ce5677547db3d1cbc21653d24c76989 |
| USRDATA | userdata.img | 15290768 | 552e325ecf2faffeb9351022147bbfda3b7cebe25df491b2d732e85c5c68f27c |

  - SPFT boxes to select: BOOTIMG→BOOTIMG.img,

ANDROID→Y2ROOT.img, USRDATA→Y2DATA.img only for explicit fresh initialization; USRDATA erases existing persistent data. For preserving retry select BOOTIMG and ANDROID using the preserve-data scatter.
  - Boxes NEVER selected in this installation: PRELOADER, MBR, EBR1,

PRO_INFO, NVRAM, PROTECT_F, PROTECT_S, SECCFG, UBOOT/LK, RECOVERY, SEC_RO, MISC, LOGO, EBR2, EXPDB, CACHE, FAT, BMTPOOL.
  - Download Only procedure: use owner-proven SPFTv5.2032 and its DA, verify

package checksums, retain before readbacks/table identity, load the package's first-install scatter, review all21 rows, select exactly the3 above, choose Download Only, and use the established owner USB/power entry sequence. No Format All + Download, Firmware Upgrade, Write Memory, table changes or workaround if SPFT reports an identity/table/image error. Remove SD before first normal production boot. [Exact install procedure](https://innioasis.app/guides/reborn-y2linux-y2.html).
  - Readback/verification: before the write capture the13 bounded EMMC_USER

KEEP ranges in metadata/readback-plan.json. The verifier checks original MBR/EBR prefixes with `--before-only`; after download recapture these ranges plus full BOOTIMG16MiB, ANDROID820MiB and USRDATA800MiB, before boot. Compare protected ranges exactly and target raw-image prefixes by SHA256:
`python3 tools/production/verify_readback.py --package out/y2linux-production-v1-r3 --before /path/to/before --before-only python3 tools/production/verify_readback.py --package out/y2linux-production-v1-r3 --before /path/to/before --after /path/to/after`

If pre-failure captures exist, retain and compare those too. Captures taken only after the failed attempt establish preservation across the retry; they cannot prove the earlier attempt left every protected byte unchanged.

Physical starts are BOOTIMG0x1d80000, ANDROID0x5180000, USRDATA0x40380000; scatter linear starts are0x3180000,0x6580000,0x41780000. SPFT normal Download uses its original scatter mapping; EMMC_USER Readback uses physical offsets. Linux whole-disk offsets are those same physical values, while a partition node starts at offset0. No custom DA/global offsets are guessed. Preserve logs proving which device/DA/region was read; file hashes alone cannot establish that.
  - Expected first boot: stock ROM→preloader→LK→Linux6.18.0-y2linux-storage03

rescue→internal Y2ROOT/Y2DATA→switch_root→Buildroot. Discovery allows40s.
  - Expected no-SD boot: identical boot path; removable SD is ignored by the

root resolver. Later SD serves media through explicit `y2-media mount`; nothing autoformats it. Old SD root labels cannot hijack production boot.
  - Expected SSH/USB: cable-present or later-attached startup is now supported in code;

initial ACM diagnostics and usb0 at10.42.0.1/24 are expected, key-only SSH after normal Buildroot boot. New per-owner client private key lives OUTSIDE the package at `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-production-private/id_ed25519`. Keep it private and backed up separately. Only its new public key is inside Y2DATA. Dropbear generates new host keys on-device and persists them on /data. First key generation can wait for kernel entropy; historical delay was~154s. Use a separate host alias for the new production identity:
`ssh -F /dev/null -o HostKeyAlias=y2linux-production-v1 -i /home/luca/Dokumente/Code/Y2Linux/out/y2linux-production-private/id_ed25519 root@10.42.0.1`

Verify the new host key. No development private key or universal production credential is packaged. USB cable reconnect remains a known deferred limitation.
  - Rescue failure behavior: missing/ambiguous/wrong label/UUID/geometry,

root/data marker failure, failed executable preflight, unrepairable fsck or mount failure retains rescue PID1, readable on-screen status and ACM logging intent. No automatic format, SD fallback or reboot loop. There is no rescue SSH service. Stock UART/console shell remains where usable; ACM keeps one log writer. Final handover crashes and pre-gadget faults are outside this fallback's guarantee. A torn BOOTIMG can require SPFT because its own rescue may no longer load.
  - Exact restoration: quickest Linux fallback: original scatter,

Download Only, deselect all, BOOTIMG only→the preserved AUDIO-02 image (4816896bytes, SHA256b9dbf6b528e4afbee2a5ffb2fc65df7f6a076564e92960332e24cee3809b5842), verify readback prefix, insert original SD and boot. It disables eMMC and leaves new internal root/data intact. Factory Android restoration instead selects ONLY BOOTIMG→FM boot.img, ANDROID→FM system.img, USRDATA→FM userdata.img; it destroys Y2DATA. Never restore loaders/tables/ calibration as part of either route. [Full restoration/readback procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fproduction-recovery.md).
  - Future OTA support: independent kernel/root/app versions and hashes,

stable layout1 geometry, explicit component/partition allowlists and ABI/schema requirements. BOOTIMG-only updates must supply/validate matching DRM modules; Y2ROOT image replacement preserves /data. Future app bundles can live under /data/apps/y2player/releases with atomic activation and /data/y2player state, alongside a future built-in Buildroot package. No app partition or app/updater code is implemented. Staged rescue updates are preferred to forced A/B; interrupted BOOTIMG uses external SPFT recovery. No repartition is needed for this direction. [Update/installer contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fupdate-model.md).

## Validation and remaining physical boundary

PASS 33 regression tests plus a separate linked-kernel USB test, emitted kernel/DT/D08 memory/BOOTIMG checks, matching DRM module, ARM ABI and ALSA utilities, rescue shell syntax, ext4 e2fsck checks, label/UUID, root/data contents and ownership, raw ext4 transport identity, all21 stock scatter coordinates/no overlap, allowlists, versions and package hash inventory. The retained readback verifier still requires owner captures. No physical readbacks or protected-data preservation result are asserted for this candidate.

Production Storage v1/#33/milestone3 remains ACTIVE. M3's44.1kHz result stands, 48kHz/LR/repeat remain pending. No-SD boot, native internal MMC filesystems, writability/persistence, display/input/audio retention, protected-byte readbacks and rescue-negative behavior must be physically demonstrated. Expected RAM is comparable to live AUDIO-02's954384KiB, with four CPUs; record the actual new value. Do not close the milestone from SPFT completion. M4/M5 remain unstarted and Y2PlayerNative remains deferred. STOP here for the owner's manual operation.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
