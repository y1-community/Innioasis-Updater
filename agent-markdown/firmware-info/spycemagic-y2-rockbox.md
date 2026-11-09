---
title: "About Rockbox (Y2) - README.md - Innioasis Updater"
description: "The Y2 Rockbox build. Select Y2 before choosing this Software."
language: "en"
source: "https://innioasis.app/firmware-info/spycemagic-y2-rockbox.html"
---

# About Rockbox (Y2) - README.md - Innioasis Updater

[← Firmware Downloads](../firmware.html)

Firmware README · Y2

# About Rockbox

The Y2 Rockbox build. Select Y2 before choosing this Software.

Also known as: README.md · spycemagic/y2-rockbox · y2-rockbox · Rockbox · spycemagic-y2-rockboxY2[Open the Rockbox guide](../guides/rockbox-y2.html)[Install with Updater CE](../firmware.html?model=Y2&software=rockbox-y2)[Why Rockbox?](../rockbox-benefits.html)Downloads from Firmware Archive3,469

# Y2 RockBox

Rockbox for the Innioasis Y2, hosted inside its original Android 4.4.2 firmware. The project adds a full-screen Rockbox player, selectable cold-boot routes, USB mass-storage return, and normal Rockbox theme support while retaining the Stock Y2 interface and its guarded recovery path.

[!WARNING] Firmware flashing can erase data or leave the player temporarily unbootable. Beta V2 supports only the Innioasis Y2 on the official Stock 3.1.7 lineage. Back up first, verify the exact release checksum, and use only an updater explicitly carrying the guarded Y2 Class A route.

## Current release

Beta V2 is available as a GitHub prerelease:

[v0.2.0-beta](https://innioasis.app/release_notes.html?author=SPYCEMAGIC&project=Y2-Rockbox&version=v0.2.0-beta&software=rockbox-y2).

The files are public for manual download and checksum verification. Direct installation through the public Updater CE catalogue remains pending [Updater CE PR #45](https://github.com/y1-community/Innioasis-Updater/pull/45). Downloading a ZIP manually does not make an old or generic updater safe.

Choose the exact platform asset:````

| Platform | Asset |
| --- | --- |
| macOS | Y2-Rockbox-Beta-v0.2.0-UPDATE-ONLY.zip |
| Windows | Y2-Rockbox-Beta-v0.2.0-Windows-UPDATE-ONLY.zip |

Both files are byte-identical, 361,774,260 bytes, with SHA-256:

`409DDB4D2D18111FB8C3AB619F10F04B916B6B2A3FC04D1D38011324563F326A`

Do not rename either file to `rom_y2.zip`. Do not use a withdrawn Beta V2 archive, `InnioasisUpdater_Setup_1.1.2.exe`, a Y1 package, or a generic full-format route.

The accepted archive contains only the Y2 scatter, five permitted payloads (UBOOT, BOOTIMG, RECOVERY, LOGO, and ANDROID), its update contract, and internal checksums. It excludes PRELOADER, partition-table images, SEC_RO, CACHE, USRDATA, and protected/runtime partitions.

Read the complete [installation guide](https://innioasis.app/guides/rockbox-y2.html), [release record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fspycemagic%2Fy2-rockbox%2Fblob%2FHEAD%2F00_project_docs%2FY2_ROCKBOX_BETA_V2_RELEASE.md), and [updater-format contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fspycemagic%2Fy2-rockbox%2Fblob%2FHEAD%2F00_project_docs%2FY2_BETA_V2_UPDATER_FORMATS.md) before installing.

## Supported hardware`Device: Innioasis Y2 Official firmware: Stock 3.1.7 Android: 4.4.2 / SDK 19 Platform: MediaTek MT6582 Board: eastaeon82_wet_kk`

## What is new in Beta V2
  - Bluetooth Settings, pairing, A2DP playback, media controls, disconnect, and

reconnect work from both Rockbox and Stock.
  - Holding Previous/Next seeks within a track. An optional setting lets held

Volume buttons skip tracks while short presses continue to change volume.
  - Time/date changes persist without freezing the Rockbox UI.
  - Rockbox wheel vibration is adjustable through true-off and remains

independent from Stock's key-vibration setting.
  - First-connect and repeated USB Storage flows are stable on Rockbox and Stock.
  - Clean boot reaches a responsive Rockbox root in approximately 28 seconds.
  - Centre wake, long-Centre Now Playing context, improved Back/Database

navigation, PictureFlow recovery, and saved Rockbox/Stock routing are proven.

The final power-down animation can look imperfect, although shutdown works. Beta V3 priorities include that polish, lyrics/theme diagnostics, high-resolution FLAC stability, DAC and wired-audio qualification, PictureFlow polish, and database/playlist presentation controls.

## Back up before flashing
  - Copy internal-storage and microSD content to the computer.
  - Back up the complete hidden `.rockbox` directory, including themes,

playlists, settings, and databases.
  - Keep an extracted, hash-verified official Y2 Stock 3.1.7 recovery package.
  - Charge the Y2, use a reliable data cable, and avoid hubs.
  - Close other software that may claim MediaTek or Android USB devices.

## Mandatory post-flash reset

After the updater reports completed verification:
  - Unplug the Y2 completely.
  - Power it off if necessary.
  - Press and release the bottom pinhole once while unplugged.
  - Start the Y2 normally.

The updater-attached automatic boot can inherit temporary MediaTek loader or display state, visible as upper-screen artifacts or broken screen sleep. That is not the qualified first boot. The clean post-pinhole boot should reach the responsive Rbox root in about 28 seconds without upper artifacts.

## Cold-boot routes

Start from a fully powered-off Y2. Hold a route button before pressing Power and keep it held until the normal haptic release cue.

| Input | Destination |
| --- | --- |
| No Volume button | Saved normal player; Rockbox by default |
| Volume Up | Opposite player; Stock by default |
| Volume Down | Boot Settings |

Boot Settings changes the no-button route. Volume Up automatically remains the opposite player. Simultaneously holding both Volume buttons is unsupported and is not a Beta V2 feature.

## Controls and storage
  - Centre confirms selections and wakes the display.
  - On Now Playing, short Centre toggles play/pause and long Centre opens the

standard context menu.
  - Previous/Next navigate; holding them seeks within a track.
  - Short Back returns from the database to Now Playing; long Back from Now

Playing returns to the database context.
  - Play/Pause controls playback; the wheel navigates lists and adjusts volume.

For USB Storage, safely eject every mounted Y2 volume on the computer before turning USB storage off or unplugging. Rockbox does not automatically resume a paused track after USB; this is normal.

Use complete 480x360 Rockbox themes. Merge a theme's complete `.rockbox` subtree into the existing directory; never replace or delete the whole tree.

## Recovery

Stop and restore the official complete Y2 Stock 3.1.7 package after a failed install, persistent boot loop, repeated wrong route, missing storage, or persistent crash dialog. Never substitute a preloader, scatter, or recovery file from another device.

Development evidence and generated firmware are deliberately excluded from the public Git history. See [SAFETY.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fspycemagic%2Fy2-rockbox%2Fblob%2FHEAD%2F00_project_docs%2FSAFETY.md) and [PUBLIC_INSTALL_STRATEGY.md](https://innioasis.app/guides/rockbox-y2.html) for the engineering and distribution rules.

## Licensing

Original parent-project code and documentation are licensed under GPL-2.0-or-later; see [LICENSE](https://github.com/spycemagic/y2-rockbox/blob/HEAD/LICENSE) and [NOTICE.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fspycemagic%2Fy2-rockbox%2Fblob%2FHEAD%2FNOTICE.md). The modified Rockbox submodule retains its upstream licenses. Binary releases carry the corresponding source archive and applicable notices.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
