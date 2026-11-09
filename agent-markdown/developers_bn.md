---
title: "Developers | Add custom firmware to Innioasis Updater CE - Innioasis Firmware Downloads"
description: "Developer documentation for adding a custom Innioasis Y1 or Y2 firmware to Updater CE: fork the repository, publish rom.zip assets, edit slidia_manifest.xml, test, and open a pull request."
language: "bn"
source: "https://innioasis.app/developers_bn.html"
---

# Developers | Add custom firmware to Innioasis Updater CE - Innioasis Firmware Downloads

For firmware developers

# Add your firmware to Updater CE.

Updater CE is the community catalogue and installer for custom firmware. Develop your project from a base ROM, publish it as a public repository with the correct release assets, add the model entries to `slidia_manifest.xml`, test the model filters, and open a pull request. One repository can serve every model it supports.[View the Updater CE source](https://github.com/y1-community/Innioasis-Updater)[সফটওয়্যার ডাউনলোড ব্রাউজ করুন](firmware_bn.html)

## Start from a base ROM

Base ROMs give custom firmware developers a clean Android foundation with the wireless radio chips enabled. On the Y1 they enable Wi-Fi and GPS alongside the factory Bluetooth and FM; on the Y2 they enable Wi-Fi, GPS, and FM alongside the factory Bluetooth.Base ROM downloads for custom firmware development, with the Android version and wireless features each one enables[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| ডাউনলোড | Device | Android | Wireless features |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Adds Wi-Fi and GPS to the factory Bluetooth and FM (FM already works on the Y1 from the factory). For Y1 players that shipped with OS 2.0.0 or later. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Adds Wi-Fi and GPS to the factory Bluetooth and FM (FM already works on the Y1 from the factory). For Y1 players that shipped with an OS earlier than 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Adds Wi-Fi, GPS, and FM to the factory Bluetooth. The Y2 radio chip is fully enabled, so FM is available here too. |

These images are the stock Android base (AOSP) with the device wireless radios enabled, so a custom firmware can add network features instead of replacing the radio stack. They are the practical starting point for the publishing steps below.

## Use these release asset names

The filename is part of the compatibility signal. Keep the names exact and put the ZIP files in the project's release assets, not only in the repository source tree.Firmware ZIP asset names and supported devices``````

| Asset | Device | হার্ডওয়্যার | Meaning |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 devices that shipped with OS 2.0.0 or later. |
| rom_type_b.zip | Y1 | Type B | Y1 devices that shipped with an OS earlier than 2.0.0. |
| rom_y2.zip | Y2 | Y2 | The Y2 full-install package. Keep it separate from Y1 assets. |
Do not rename a package to make it fit another model. Y1 and Y2 use different MediaTek platform files and flashing configuration. Publish the package for the hardware it actually supports.

## How the connection works

Updater CE reads the manifest as its catalogue. Each `<package>` line tells it the project name, repository, model, and handler. When a user chooses that project, Updater checks the repository’s published releases and looks for a `rom*.zip` asset.

### Manifest

Names the project and maps it to a model. Y1 and Y2 need separate lines, even when they share a repository.

### Published release

Contains the installable ZIP assets. A single release may contain the Y1 Type A, Y1 Type B, and Y2 packages together.

### Updater CE install

Uses the selected model to choose the matching package and model-specific flashing path. The user should not have to guess a filename.

## Publish a project in five steps
  - Fork the Updater CE repository. Create your own fork of [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), then clone your fork locally.
  - Prepare a public firmware repository. Make sure the repository is public and its release contains the correct ZIP assets. You can put `rom.zip`, `rom_type_b.zip`, এবং `rom_y2.zip` on the same release when they belong to the same version.
  - Edit the manifest. খোলা `slidia_manifest.xml` in the root of your Updater CE fork. Add one line for each model the release supports (Y1 and Y2 are the common pair). The `repo` value is the repository's `owner/repository`; `url` is the public project page.
  - Test the catalogue. Run Updater from the edited checkout. Select Y1 and confirm the project shows the Y1 assets. Select Y2 and confirm it shows the Y2 release. Check Type A and Type B separately when both are published.
  - Open a pull request. Push the manifest change to your fork and open a pull request against the upstream Updater CE repository. Include the project link, supported models, release tag, asset names, and the devices you tested.

## Generate your manifest lines

Fill in the repository and tick every model the release supports. The generator writes one `<package>` line per model and only includes the attributes you set, so the result matches the current `slidia_manifest.xml` format. Every attribute Updater CE reads is available below — the optional ones are under More options.Repository URLThe public GitHub repository. The generator extracts `owner/repository` from the URL.Software nameShown in the app and the site catalogue.Project URLHuman-facing page for the project or its release notes.BrandClear this to use the model's default brand. SR1, Q3, Q5 and Q3e are Timmkoo models.Devices (one line each)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eOther modelsFor a model that is not listed above. Known models keep their catalogue spelling.Flags`do_not_keep_data` — never offer Keep Data for this firmwareBuilt from Original Software — adds `derivative="y1-community/y1-stock-rom"`

Keep Data is only offered when the incoming firmware and the installed firmware are the same or share a `derivative` root. Use the flag only when user data genuinely cannot carry over.More options: icon, artwork, release assets, post-install and mirrors

#### Icon and artworkIcon fileChoose the image you will commit to the repository. This previews it and builds its raw URL; it does not upload anything.Icon path in repositoryPath to the committed image, relative to the repository root.Icon branchIcon URLA direct image URL. When empty, the app uses the release's `updater.png` or a generated icon.Selected icon preview

Dark-mode icon URLOptional dark-theme icon. `image_dark` is an accepted alias.Light artwork URLSecondary artwork, tried after the release image and `icon`.Dark artwork URL

#### Release assetsRelease asset nameOne name for every selected model. Leave empty to use `rom.zip` on Y1 and `rom_<model>.zip` elsewhere.Asset patternGlob used when the release's zips are not named `rom*.zip`.Type A assetGlob for the Y1 Type A package when its name does not say so.Type B assetGlob for the Y1 Type B package when its name does not say so.Minimum app versionHide the entry from older Updater CE builds.

#### Links, mirrors and Keep Data familyPost-install pageOpened after a successful install.Second post-install pageOptional second step for a multi-page setup guide.Portable zip mirrorsComma-separated `*-mirror` repositories that build Portable Flashing Zip packages.Derivative repositoryThe firmware this release is built from. Related firmwares share a data partition, which is what Keep Data checks.Info repositoryApp repo whose releases describe the apps in this firmware. It also needs a post-install page.APK repositoryApp repo whose APK the app downloads and installs after the firmware.

#### Catalogue extrasSlugStable identifier for links and saved install records. The model is appended automatically when several models are selected.Description`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Copy lines

Loading the latest manifest…Preview the latest manifest with your lines added

The generator fetched the current `slidia_manifest.xml` from this repository and inserted your generated lines just before `</slidia>`.

One line is not enough for a shared repository. If the Y2 line is missing, Y2 users will not get a model-matched entry even when `rom_y2.zip` exists in the project's release. The same is true for every other model your release supports.

### Every attribute the manifest reads

These are the attributes current Updater CE builds understand. The generator writes only the ones you fill in; the app falls back to sensible defaults for the rest.slidia_manifest.xml package attributes and their meaning``````````````````````````````````````````````````````````````````````````````````````````````

| Attribute | Needed | What it does |
| --- | --- | --- |
| name | হ্যাঁ | Software name shown in the catalogue and on install cards. |
| repo | হ্যাঁ | owner/repo. The app reads that repository's GitHub releases. |
| device | হ্যাঁ | Target model, uppercase (Y1, Y2, G1, Q3e, …). Keep one entry per model. |
| url | Recommended | Project page or release notes opened from the catalogue. |
| type, handler | Yes in practice | type="img" এবং handler="Custom Firmware". Other types and non-firmware handlers are skipped. |
| brand | ঐচ্ছিক | Catalogue brand (Innioasis, Timmkoo). Empty uses the model's default brand. |
| package_name | ঐচ্ছিক | Release asset filename. Defaults to rom.zip on Y1 and rom_<model>.zip on other models. |
| asset_pattern | ঐচ্ছিক | Case-insensitive glob for releases whose firmware zips are not named rom*.zip (for example my-firmware-*.zip). |
| type_a_asset, type_b_asset | ঐচ্ছিক | Globs that identify the Y1 Type A and Type B zips when their filenames do not contain the usual markers. |
| icon | ঐচ্ছিক | Logo URL. Used after the release's own updater.png / updater.jpg, and as the fallback for every release. |
| icon_dark | ঐচ্ছিক | Dark-theme logo. image_dark is an accepted alias. |
| image | ঐচ্ছিক | Secondary light artwork, tried after icon. |
| post_install, post_install2 | ঐচ্ছিক | Page(s) opened after a successful install. The second one covers a multi-step guide. |
| portable_zips | ঐচ্ছিক | Comma-separated *-mirror repos that publish ready-to-run portable packages. |
| derivative | ঐচ্ছিক | Repository the firmware is built from. Firmware with the same derivative root can keep user data. |
| info_repo | ঐচ্ছিক | App repository whose releases describe what the firmware deploys. Requires post_install বা post_install2. |
| apk_repo | ঐচ্ছিক | App repository whose APK the app installs after the firmware. |
| min_version | ঐচ্ছিক | Hide the entry when Updater CE is older than this version. |
| do_not_keep_data | ঐচ্ছিক | true (also 1 / yes) blocks Keep Data completely for this firmware. |
| slug | ঐচ্ছিক | Stable identifier for links and saved install records. Generated from the name and model when empty. |
| description | ঐচ্ছিক | Short catalogue description. It can be the attribute value or the element's text. |

Legacy names are still read for compatibility: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` এবং `image_dark`. New entries should use the current names above.

### Submit the lines as a pull request
  - Copy the generated lines above. They already match the latest manifest format.
  - Edit `slidia_manifest.xml` in the repository. Use the edit link below; the repository host creates a fork and a branch for you automatically.
  - Paste the lines just before `</slidia>`, keeping the existing entries unchanged.
  - Commit to a new branch (for example `add-your-firmware`), then open a pull request against the Updater CE repository.
  - In the PR, include the project link, supported models, release tag, asset names, and the devices you tested.
[Edit the Updater CE manifest](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[See the latest manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Keep the model names uppercase, use the exact URL of your public repository, and keep `type="img"` এবং `handler="Custom Firmware"` for a firmware entry.

## Make the release easy to verify

Give the release a clear tag and release note. The tag is useful to people, but the ZIP asset names are what Updater CE uses to identify the install packages.

### Release checklist
  - Publish the release publicly.
  - Attach the ZIP files as release assets.
  - State the supported model and Type A or Type B in the notes.
  - List any required preparation or known limits.

### One release, three assets

A shared release can contain `rom.zip`, `rom_type_b.zip`, এবং `rom_y2.zip`. Updater classifies them separately and chooses from the model and hardware filters.

### Do not bundle guesses

Do not include a Y1 package under the Y2 filename, or add untested scatter, preloader, or partition data just to make an asset appear.

## Why the model entries matter during flashing

The manifest is not just a download menu. After extraction, Updater CE uses the resolved model to prepare the matching install path. Y1 and Y2 have different platform files, preloaders, scatter configuration, and device layouts.
  - Y1: the updater prepares the Y1 path and uses the device’s named partitions when MTKClient is used.
  - Y2: the updater prepares the Y2 path and uses the Y2 MT6582 configuration. Full recovery can use physical addresses from the model-correct scatter data.
  - Cross-Platform Support: Updater CE handles native flashing directly across Windows, Linux, and macOS (supporting both Intel and Apple Silicon Macs) without extra flashing tools.
Contributors should provide correct firmware files, not flash offsets. Do not edit scatter addresses, preloaders, DA files, or partition commands to work around a bad package. Fix the release asset and test on the intended model.

## Before you request a merge
  - Validate the XML with an XML parser. A missing quote or closing `/>` can hide every entry after it.
  - Launch the updater from your checkout so it loads the local manifest before the remote refresh.
  - Check Y1 and Y2 independently. Confirm that the project appears only where its package is supported.
  - Check the release list for `rom.zip`, `rom_type_b.zip`, এবং `rom_y2.zip` as applicable.
  - Test the actual install on the intended device, with a reliable USB data cable and a recovery plan for returning to Original Software.
  - In the pull request, explain what you tested. Do not describe an untested model as supported.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

For a local check, run that command from the repository root. It verifies XML syntax only; it does not prove that a release contains valid firmware or that a device is safe to flash.

## Useful project links[Fork Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[See the manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Community contribution notes](support_devs_bn.html)[সমস্যা সমাধান](troubleshooting_bn.html)

## Modding skills for AI agents

The repository's `skills/` directory is a source-grounded knowledge base for agents working on Y1 and Y2 hardware, firmware, themes and apps. Each skill names the project files its claims come from, so an agent can check a fact before changing a device.Start here

### [Skills index and safety rules](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

How to load a skill, which model a fact applies to, and the partitions no package should write.হার্ডওয়্যার

### [Y1 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, the wheel as key events, 480x360 display, FM/audio paths, storage and the Type A/B partition map.হার্ডওয়্যার

### [Y2 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582 board, device tree, GC9503V/ST7701S panels, PMIC/DAC rails, partitions and the boot image.Firmware

### [Firmware packages](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomy, scatter files, Class A update contracts and the release checklist.Themes

### [Theme and skin authoring](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json themes, Rockbox WPS/SBS, Reborn skins and Y2Player skin format v2.All skills

### [Browse the skills folder](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, stock Android ROMs, Y2Linux, Android apps, launchers, release notes and site publishing.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
