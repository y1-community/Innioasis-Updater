---
title: "About Android 4.2 (Dev) (Y1) - README.md - Innioasis Updater"
description: "Android 4.2 development ROM for Innioasis Y1."
language: "en"
source: "https://innioasis.app/firmware-info/y1-community-y1-ata-rom.html"
---

# About Android 4.2 (Dev) (Y1) - README.md - Innioasis Updater

[← Firmware Downloads](../firmware.html)

Firmware README · Y1

# About Android 4.2 (Dev)

Android 4.2 development ROM for Innioasis Y1.

Also known as: README.md · y1-community/y1-ata-rom · y1-ata-rom · Android 4.2 (Dev) · y1-community-y1-ata-romY1[Open the Android 4.2 (Dev) guide](../guides/android-4-2-y1.html)[Install with Updater CE](../firmware.html?model=Y1&software=android-4-2-y1)Downloads from Firmware Archive664

# Y1 Firmware Package Preparation Information:

Step one is crucial to ensuring your firmware package can be installed with any operating system, such as macOS where MTKclient is used to install firmwares on Y1 (Y1-only for now in Updater for Mac until Y2 flashing via MTKclient is figured out)

1: Ensure cache.img, userdata.img and system.img are desparsed using simg2img (MTKclient which is used to install mediatek firmwares on macOS and Linux prefers desparsed images as opposed to the sparseimages)
  - Gather all the partition images for your firmware, for Y1 these are:

EBR1, EBR2, MBR, kernel, kernel_g368_nyx.bin, ramdisk-recovery.img, ramdisk.img, secro.img, system.img, userdata.img, boot.img, cache.img, lk.bin, logo.bin, preloader_g368_nyx.bin for, Y2 these are: EBR1, EBR2, kernel, kernel_eastaeon82_wet_kk.bin, ramdisk-recovery.img, ramdisk.img, secro.img, system.img, userdata.img, boot.img, cache.img, lk.bin, logo.bin, preloader_eastaeon82_wet_kk.bin
  - ( Zip Template Here ) Include your files as above and a copy of SP Flash Tool and the pre-configured [history.ini](https://www.innioasis.app/history.ini) file - this offers users a portable, one-click install for SP Flash Tool on Windows systems without needing updater, they can extract directly from Zip if they like, by including these in your rom_y2.zip - Including History.ini also helps ensure that when users opt to trigger the SP Flash Tool GUI from Updater (often done for trouble shooting purposes) they'll be presented with a pre-configured SP Flash GUI which due to history.ini's relative file paths will correctly find the files needed for flashing without displaying any error messages about files not being found)
  - Compress the collective package as an appropriately named zip archive with the Deflate compression method on max settings, this will minimize a user's download time for the ROM
  - Name the file as below depending on the hardware your firmware targets:

Y1 Type A (Most common hardware variants, came with OS 2.0.0 and later): rom.zip Y1 Type B (Early hardware revision in low numbers) rom_type_b.zip Y2: rom_y2.zip
  - Host your zip(s) on a GitHub Repository, to do this, you'll need to fork the Innioasis-Updater repo and submit a PR with your manifest changes.

7, Point [Updater's manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml) to your Repo - this adds your firmware to the list of firmwares available - one line per model supported, all zips for each hardware model / revision can be placed in same release if you like - or as separate releases / different repos etc)

Once the 6 steps are completed users and the PR merged by the maintainers of Updater, users will see their firmware listed in Updater in 24-48 hours as their Updater clients grab new manifests - this will usually happen instantly on their next launch of Updater unless they use Updater frequently.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
