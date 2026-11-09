---
title: "Windows 10/11 app launch issues &amp; Smart App Control workaround - Innioasis Updater"
description: "If Windows 10/11 or Smart App Control stops you from launching the app, follow the workaround here."
language: "en"
source: "https://innioasis.app/notices/2026-11-07-codesigning.html"
---

# Windows 10/11 app launch issues &amp; Smart App Control workaround - Innioasis Updater

From 2026-10-25 · until 2026-12-31 · Models: Y1,Y2

# Windows 10/11 app launch issues & Smart App Control workaround

If Windows 10/11 or Smart App Control stops you from launching the app, follow the workaround here.

From 2026-10-25 · until 2026-12-31 · Models: Y1,Y2

False-positive reports were submitted to Microsoft for `installer.exe` and `InnioasisUpdater.exe` and actioned, but if Windows Endpoint Protection or Smart App Control is still blocking the application on your computer, use this workaround:

### Temporary Workaround: Turn Smart App Control Off
  - Open Windows Settings (press `Win + I`).
  - Go to Privacy & security > Windows Security > App & browser control.
  - Under Smart App Control, click Smart App Control settings.
  - Set Smart App Control to Off. This immediately allows the app to open and run.

If Windows or Edge prevents you from downloading Updater CE, click more options (…) then Keep > Show more > Keep anyway.

### Re-enabling Smart App Control

When false-positive definitions finish updating on your computer, you can re-enable Smart App Control via the Windows Registry:
  - Press Windows Key + R, type `regedit`, and press Enter to open Registry Editor as administrator.
  - Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (or `Policies`).
  - Locate `VerifiedAndReputablePolicyState` in the right-hand pane.
  - Double-click `VerifiedAndReputablePolicyState` and change its Value data to:

  - `1` = On (Enforced)
  - `2` = Evaluation Mode

  - Click OK, close the Registry Editor, and restart your computer.

[See the installer.exe report to Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[See the InnioasisUpdater.exe report to Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Open the linked page](https://innioasis.app/notices.html)

[← All notices](index.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
