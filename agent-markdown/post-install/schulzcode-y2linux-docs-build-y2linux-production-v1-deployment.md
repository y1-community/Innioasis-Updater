---
title: "First manual Production Storage v1 deployment - Innioasis Updater"
description: "First manual Production Storage v1 deployment <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-production-v1-deployment.html"
---

# First manual Production Storage v1 deployment - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# First manual Production Storage v1 deployment

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# First manual Production Storage v1 deployment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Withdrawn from retry use: ANDROID sparse transfer failed 3154. Use the [Storage02 retry checklist](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-r2-deployment.md). Everything below records the historical first package; it is not current deployment guidance.

READY at the manual package boundary; NOT physically qualified. No assistant physical eMMC write or SPFT operation. First actual eMMC/rootfs qualification belongs to the owner. The latest live system remains SD-backed AUDIO-02.
  - Build Git commit:`f2ef297a81cc0229155ba5d96f1955bdd230f11d`.

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

PRELOADER is EMMC_BOOT_1: the scatter's20MiB span is a vendor abstraction, not a physical readback length; each boot hardware region is4MiB. BMTPOOL's sentinels remain UNKNOWN/unapproved. FAT's zero scatter span resolves physically to0x15dc00000 bytes and may contain user media; leave it alone. EMMC_USER capacity is7,784,103,936 bytes. Preserve MBR/EBR1/EBR2; no repartitioning occurs.

[Full source-backed classification/dependencies](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fproduction-storage-v1.md) · [Machine-readable map](https://github.com/schulzcode/y2linux/blob/HEAD/docs/architecture/production-partitions.json).
  - Y2ROOT choice: ANDROID, ext4 LABEL=Y2ROOT.
  - Original purpose/name: stock ANDROID `/system`, historically stock Linux p5.
  - Physical start: 0x05180000 =85,458,944 bytes; scatter linear0x06580000.
  - Partition size: 0x33400000 =859,832,320 bytes (820MiB).
  - Raw Y2ROOT image size: 536,870,912 bytes (512MiB).
  - Raw Y2ROOT SHA256:`041fbd7fbe0a2966e178649ff958cb3ad3cfea1610ef75aa580ba2391b1f5be8`.
  - Y2DATA: stock USRDATA (`/data`, historical p7), physical0x40380000

=1,077,411,840 bytes, size0x32000000 =838,860,800 bytes (800MiB). ext4 LABEL=Y2DATA mounted /data; initializes Android data on first install. UUIDs are79324c69-6e75-4801-8000-000000000101 (root) and 79324c69-6e75-4801-8000-000000000102 (data). Root detection checks native internal host and stock geometry, not fixed mmcblk numbers.
  - BOOTIMG, 12. scatter, 13. manifest, and filesystem transports:

All files below are in `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-production-v1/`.``````````````````

| File | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 5187584 | ca77a6767a1cbcbd36e5fdbcd6dfaeaa1c95a85aaab767b3146fd59831235e12 |
| Y2ROOT.img | 536870912 | 041fbd7fbe0a2966e178649ff958cb3ad3cfea1610ef75aa580ba2391b1f5be8 |
| Y2ROOT.spft.img | 27271092 | 2ce33a55faa34ef6e9119f5500bc67154d3cb97e68bf554422557d37f2d1d5ee |
| Y2DATA.img | 838860800 | 9e5eaa8345453d90d41a914dcc50e96302049382a8b082e49170c14fcce708b9 |
| Y2DATA.spft.img | 7352832 | 66a659f42f67e277410e6ccb6b53ad9999d173a52549db7c1dce90f1a974e039 |
| MT6582_Android_scatter.txt | 7626 | 83a60acc0a4ddebe14c4d4132d4ac3ac9d6d2b70c382fc422226705c925b7b36 |
| MT6582_preserve_data_scatter.txt | 7627 | d9d2bd550abc94f8a74b6ab4b4860a754cea82458f44ec272db5efe4db3c1808 |
| manifest.json | 7412 | a81e0b3017a26326483e162effa466144cc78e5b5ea8ae0a128d5c2e6e58cb92 |
| SHA256SUMS | 2207 | bf80adfa37d6bdd47804d4501b0af3ad5be57e9b1e880dd2b7fa76061db794ad |

The scatter maps the .spft.img filesystem files. Their expanded content is byte-for-byte identical to the raw .img; never compare sparse-file hashes with physical eMMC hashes. BOOTIMG is raw, at physical0x01d80000 within its16MiB span. The first scatter selects BOOTIMG/ANDROID/USRDATA; the preserving profile selects BOOTIMG/ANDROID only.
  - Restoration material for every overwritten partition: verified original

FM sources below exist locally in `/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/`. They restore factory Android, not personalized installed Android state. Preserve a private USRDATA readback before install if original settings/apps must be recoverable; likewise ANDROID if its modifications matter. Keep an independent accessible copy of recovery material. No full-ROM rebackup needed.
``````

| Overwritten partition | Verified stock source | Bytes | SHA256 |
| --- | --- | --- | --- |
| BOOTIMG | boot.img | 5656576 | 5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6 |
| ANDROID | system.img | 518590232 | 5a7a92f3a95374f31abe8b3ddbd68c5c2ce5677547db3d1cbc21653d24c76989 |
| USRDATA | userdata.img | 15290768 | 552e325ecf2faffeb9351022147bbfda3b7cebe25df491b2d732e85c5c68f27c |

  - SPFT boxes to select: BOOTIMG→BOOTIMG.img,

ANDROID→Y2ROOT.spft.img, USRDATA→Y2DATA.spft.img for FIRST installation only.
  - Boxes NEVER selected in this installation: PRELOADER, MBR, EBR1,

PRO_INFO, NVRAM, PROTECT_F, PROTECT_S, SECCFG, UBOOT/LK, RECOVERY, SEC_RO, MISC, LOGO, EBR2, EXPDB, CACHE, FAT, BMTPOOL.
  - Download Only procedure: use owner-proven SPFTv5.2032 and its DA, verify

package checksums, retain before readbacks/table identity, load the package's first-install scatter, review all21 rows, select exactly the3 above, choose Download Only, and use the established owner USB/power entry sequence. No Format All + Download, Firmware Upgrade, Write Memory, table changes or workaround if SPFT reports an identity/table/image error. Remove SD before first normal production boot. [Exact install procedure](https://innioasis.app/guides/reborn-y2linux-y2.html).
  - Readback/verification: before the write capture the13 bounded EMMC_USER

KEEP ranges in metadata/readback-plan.json. The verifier checks original MBR/EBR prefixes with `--before-only`; after download recapture these ranges plus full BOOTIMG16MiB, ANDROID820MiB and USRDATA800MiB, before boot. Compare protected ranges exactly and target raw-image prefixes by SHA256:
`python3 tools/production/verify_readback.py --package out/y2linux-production-v1 --before /path/to/before --before-only python3 tools/production/verify_readback.py --package out/y2linux-production-v1 --before /path/to/before --after /path/to/after`

Physical starts are BOOTIMG0x1d80000, ANDROID0x5180000, USRDATA0x40380000; scatter linear starts are0x3180000,0x6580000,0x41780000. SPFT normal Download uses its original scatter mapping; EMMC_USER Readback uses physical offsets. Linux whole-disk offsets are those same physical values, while a partition node starts at offset0. No custom DA/global offsets are guessed. Preserve logs proving which device/DA/region was read; file hashes alone cannot establish that.
  - Expected first boot: stock ROM→preloader→LK→Linux6.18.0-y2linux-storage01

rescue→internal Y2ROOT/Y2DATA→switch_root→Buildroot. Discovery allows40s.
  - Expected no-SD boot: identical boot path; removable SD is ignored by the

root resolver. Later SD serves media through explicit `y2-media mount`; nothing autoformats it. Old SD root labels cannot hijack production boot.
  - Expected SSH/USB: initial ACM diagnostics and usb0 at10.42.0.1/24,

key-only SSH after normal Buildroot boot. New per-owner client private key lives OUTSIDE the package at `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-production-private/id_ed25519`. Keep it private and backed up separately. Only its new public key is inside Y2DATA. Dropbear generates new host keys on-device and persists them on /data. First key generation can wait for kernel entropy; historical delay was~154s. Use a separate host alias for the new production identity:
`ssh -F /dev/null -o HostKeyAlias=y2linux-production-v1 -i /home/luca/Dokumente/Code/Y2Linux/out/y2linux-production-private/id_ed25519 root@10.42.0.1`

Verify the new host key. No development private key or universal production credential is packaged. USB cable reconnect remains a known deferred limitation.
  - Rescue failure behavior: missing/ambiguous/wrong label/UUID/geometry,

root/data marker failure, failed executable preflight, unrepairable fsck or mount failure retains rescue PID1 and ACM diagnostics. No automatic format, SD fallback or reboot loop. There is no rescue SSH service. Stock UART/console shell remains where usable; ACM keeps one log writer. Final handover crashes and pre-gadget faults are outside this fallback's guarantee. A torn BOOTIMG can require SPFT because its own rescue may no longer load.
  - Exact restoration: quickest Linux fallback: original scatter,

Download Only, deselect all, BOOTIMG only→the preserved AUDIO-02 image (4816896bytes, SHA256b9dbf6b528e4afbee2a5ffb2fc65df7f6a076564e92960332e24cee3809b5842), verify readback prefix, insert original SD and boot. It disables eMMC and leaves new internal root/data intact. Factory Android restoration instead selects ONLY BOOTIMG→FM boot.img, ANDROID→FM system.img, USRDATA→FM userdata.img; it destroys Y2DATA. Never restore loaders/tables/ calibration as part of either route. [Full restoration/readback procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fproduction-recovery.md).
  - Future OTA support: independent kernel/root/app versions and hashes,

stable layout1 geometry, explicit component/partition allowlists and ABI/schema requirements. BOOTIMG-only updates must supply/validate matching DRM modules; Y2ROOT image replacement preserves /data. Future app bundles can live under /data/apps/y2player/releases with atomic activation and /data/y2player state, alongside a future built-in Buildroot package. No app partition or app/updater code is implemented. Staged rescue updates are preferred to forced A/B; interrupted BOOTIMG uses external SPFT recovery. No repartition is needed for this direction. [Update/installer contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fupdate-model.md).

## Validation and remaining physical boundary

PASS24 regression tests, emitted kernel/DT/D08 memory/BOOTIMG checks, matching DRM module, ARM ABI and ALSA utilities, rescue shell syntax, ext4 e2fsck checks, label/UUID, root/data contents and ownership, sparse RAW/FILL expansion hashes, all21 stock scatter coordinates/no overlap, allowlists, versions and package hash inventory. Synthetic readback tests reject both root-image corruption and protected-byte mutation; they are explicitly not physical readbacks.

Production Storage v1/#33/milestone3 remains ACTIVE. M3's44.1kHz result stands, 48kHz/LR/repeat remain pending. No-SD boot, native internal MMC filesystems, writability/persistence, display/input/audio retention, protected-byte readbacks and rescue-negative behavior must be physically demonstrated. Expected RAM is comparable to live AUDIO-02's954384KiB, with four CPUs; record the actual new value. Do not close the milestone from SPFT completion. M4/M5 remain unstarted and Y2PlayerNative remains deferred. STOP here for the owner's manual operation.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
