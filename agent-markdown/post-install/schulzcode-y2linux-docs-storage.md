---
title: "Storage on the Y2 - Innioasis Updater"
description: "Storage on the Y2 Where your music, settings and the system live on a Y2 running Y2Linux, what happens to the player's own storage when Y2Linux starts for the first time,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-storage.html"
---

# Storage on the Y2 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Storage on the Y2

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Storage on the Y2

Where your music, settings and the system live on a Y2 running Y2Linux, what happens to the player's own storage when Y2Linux starts for the first time, and how files get on and off the player over USB. Applies to Y2Linux 1.0 Beta 7.9 and later (Internal Storage is set up by itself since 7.9; moving and copying over USB since 7.10).

## The layout: the same on every player

The Y2 has 8 GB of internal memory (eMMC). Y2Linux uses three of its partitions; everything else (bootloaders, calibration, MAC addresses) is never written.``````

| Partition | Name | Size | What is on it | Visible over USB |
| --- | --- | --- | --- | --- |
| system | Y2ROOT | 820 MiB | Y2Linux and the Reborn player; replaced by every update | no |
| data | Y2DATA | 800 MiB | settings, the music library database, logs, the Last.fm sign-in, Wi-Fi and Bluetooth state, the radio firmware, downloaded updates | no |
| music | Y2MEDIA | 5.4 GiB | Internal Storage: your music, playlists, skins | **yes, as *Internal Storage*** |
| microSD card | (your card) | your card | more music | yes, as SD Card |

Every player gets exactly the same layout: the same names, sizes and positions, and the same filesystem settings. `Y2MEDIA` is the partition the stock Innioasis firmware used as the player's own storage; Y2Linux replaces its stock FAT format with ext4 (journalled, so a sudden power loss does not damage it).

## The first start: the old storage becomes Internal Storage

When Y2Linux starts and finds the stock storage still in its Innioasis format, it first looks at what is on it (read-only, nothing is written yet) and then decides:``````

| The old storage holds | What happens | How long |
| --- | --- | --- |
| nothing, or only leftovers (empty folders such as DCIM or Ringtones, thumbnail caches, Windows/macOS index files) | set up at once | a few seconds |
| your files, up to about 400 MB | kept: copied to the data partition and checked, the storage is set up, the files are moved onto it and checked again. They appear in Internal Storage → Old Player Files, with their folders | up to a couple of minutes |
| more than that (a real music library), or the old storage cannot be read | nothing changes (see below) | — |

While it runs, the start screen says Setting up storage, then Keeping your old files, Preparing Internal Storage and Moving your old files. Afterwards Reborn says *Internal Storage is ready* (with the number of kept files). Old music in `Old Player Files` is in the library straight away; delete the folder over USB when you no longer need it.

"Leftovers" are only: empty folders, `.thumbnails` folders, Android's thumbnail cache (`Android/data/com.android.providers.media/albumthumbs`), `.android_secure`, `.nomedia`, `System Volume Information`, `.Spotlight-V100`, `.Trashes`, `.fseventsd`, `.DS_Store`, `Thumbs.db`, `desktop.ini` and `._…` files. Everything else counts as yours and is kept, including `LOST.DIR`, old skins in `Themes` and app folders.

### A large old library

If more than about 400 MB is on the old storage, Y2Linux does not touch it:
  - Reborn asks once: Set Up Internal Storage? — Cancel keeps everything as it is.
  - Over USB the old files appear as a read-only drive Old Storage: copy them to a computer.
  - Settings → Library → Storage → Set Up Internal Storage (it shows how many old files there are) sets

the storage up when you are ready. This erases the old files; the player restarts afterwards. It is refused while a computer is connected (unplug first).
  - Until then music goes on the SD card, and the radio firmware has its own drive (below).

### Players that update from an earlier beta

The update itself never touches your storage. If the player still has the old storage, the setup runs at the first restart after the update is confirmed — never during the update's own health check (a slow start there could make the update roll back). Until then Settings → Library → Storage says Restart to finish setting up. It also waits while the battery is below 25 % and no charger is connected; Settings → Library → Storage then says Connect a charger and restart, and the setup runs at the next start with the charger connected (any USB port is enough).

### Safe against power loss

Every step is recorded on the data partition. If the battery runs out or the player is switched off in the middle, the next start continues where it stopped: kept files are only removed from the data partition after every one of them was checked on Internal Storage. A storage that is not the stock one, and a storage left unreadable without that record, is never formatted automatically.

## The SD card
  - FAT32, exFAT and ext4 cards work. Each card is checked read-only before it is used.
  - Protected between writes (since Beta 8.27). The player keeps the card read-only and makes

it writable only while something writes to it: a computer connected by USB, a change to a playlist stored on the card, an error report saved to it. Taking the card out while music from it plays (or with the player off) leaves it clean. Take it out only when no computer is connected and no playlist on it is being changed.
  - A card that was pulled out while in use (it carries a "not cleanly unmounted" mark) is used

again normally, as are the harmless leftovers of an interrupted copy that Windows ignores too.
  - A large card is checked while it plays (F49). A FAT32 or exFAT card whose check takes longer

than 20 s (about 70 000 songs on a 1 TB exFAT card take a minute) is used at once, read-only, and checked in the background; when the check passes it is writable as usual. Until then a computer sees it read-only.
  - A FAT32 or exFAT card whose check finds real damage (or whose background check has not

finished after 30 minutes) still plays, but read-only: Settings → Library → Storage says Has errors · Playing only and nothing is written to it, so the damage cannot spread. Repair SD Card (Settings → Library → Storage) fixes it on the player: keep it on the charger or above 30 %. Damaged files may be shortened or removed; the rest stays. A copy of the card's tables is kept on the player for support. A computer can repair it too (Windows: Properties → Tools → Check; macOS: Disk Utility → First Aid), but First Aid does not always fix what the player finds; reformatting (back up first) always does.
  - An ext4 card with damage is not mounted (Needs repair); Repair SD Card works for it too.
  - Copying to the card from a computer: use the USB cable (the card is a drive next to Internal

Storage) rather than a card reader; with a reader, switch the player off before taking the card out and eject it on the computer before unplugging.

## Copying music: USB

Connect the player to a computer: it appears like a phone (MTP) with Internal Storage and SD Card. It works with Windows Explorer, Linux file managers (Dolphin, Nautilus) and MTP apps on macOS (for example OpenMTP). Music apps that read a device's song list over MTP (Strawberry and other libmtp programs) see the songs of both storages with the title, artist, album and length the player's library read; a song just copied shows its file name until the player has scanned it.
  - Copy, rename, move, delete files and folders, also between Internal Storage and the SD card

(since 7.10). Moving inside one storage is instant; between the two storages each file is copied and the original removed only after the complete copy.
  - A copy is written under a hidden name and appears only once it is complete; nothing ever

overwrites a file of the same name.
  - The player keeps about 100 MB free on each storage; a copy that would not leave that much is

refused before anything is written (the computer shows an error, nothing is left behind).
  - Speed: about 38 MB/s from the player to the computer; to the player about 25–30 MB/s on

Internal Storage and about 23 MB/s on the SD card (since 7.11; before: 9–10 MB/s).
  - New songs show up in the library by themselves a moment after the copy.
  - Only one program on the computer can use the player at a time (on Linux, close the file

manager before using another MTP tool).

### The radio firmware

Wi-Fi and Bluetooth need the radio firmware from the Innioasis firmware package, once ([INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html)). While it is missing, Internal Storage contains a folder `Firmware`: copy `system.img` there (any size fits); the player takes the five radio files and removes the folder. On a player whose Internal Storage is not set up yet (large old library) a separate drive Firmware appears instead; it has room for the file from the Innioasis zip (about 520 MB) but not for an unpacked copy (about 860 MB) — Reborn then says Not Enough Space for That File, and a folder named `Firmware` on the SD card works too.

## What survives what``

| Action | Music (Internal Storage, SD) | Settings and library | Radio firmware |
| --- | --- | --- | --- |
| Update over Wi-Fi | kept | kept | kept |
| Settings → System → Reset & Maintenance → Reset Reborn Settings | kept | settings reset, library kept | kept |
| Reinstall Y2Linux with SP Flash Tool (first-install package) | kept (Internal Storage is not in the flash package) | erased | erased (copy system.img again) |
| Going back to stock Android | see below | erased | erased |

## Going back to stock

Restoring the stock firmware ([INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html)) does not restore the old FAT format of the player's storage: the stock package has no image for it, and stock Android cannot read Internal Storage's ext4 format. Copy your music to a computer first. Stock Android then has to format that storage before it can use it. This path has not been tested by the project yet.

## For developers`y2-platform internal-media status # partition, filesystem, mount cat /run/y2/internal-media-setup.json # what the setup did at this start y2-media status # the SD card (writable, read_only_reason) y2-media write --holder reborn --seconds 60 # a write window on the protected card (--release ends it) y2-media verify # the background check of a card mounted while its check ran (read_only: checking) cat /data/system/platform/sd-admissions.json # the last 10 checks: time, verdict, elapsed_ms, background y2-media repair # what Settings > Storage > Repair SD Card runs cat /data/system/platform/sd-repair-last.json # the last repair, no names`

Design, safety rules and evidence: [internal storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finternal-storage.md), the [setup plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FINTERNAL-STORAGE-SETUP-PLAN.md), the [Beta 7.9](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.9.md) and [Beta 7.10](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.10.md) reports.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
