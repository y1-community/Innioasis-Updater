---
title: "Fix Innioasis Updater &amp; Y1 Helper with a Clean Install - Innioasis Updater"
description: "Step-by-step clean install for Innioasis Updater and the Y1 Helper: remove leftover files, reinstall, and get back to flashing firmware."
language: "en"
source: "https://innioasis.app/Troubleshooting/clean_install.html"
---

# Fix Innioasis Updater &amp; Y1 Helper with a Clean Install - Innioasis Updater

## Confirm You Need the Clean Install

Manual reinstallation is recommended when you see any of the following symptoms:
  - Updater takes minutes to launch or stalls while checking for updates.
  - Updates stop arriving even though newer releases exist.
  - Device firmware updates fail to download or apply even though they’re available.
  - You skipped multiple releases and haven’t used the Updater in a long time.

## Windows: Perform a Clean Reinstall

Use the official Windows installer to refresh Updater on Windows 10 or Windows 11 (64-bit). This fully replaces older builds and restores the self-update channel.

Before you run the installer, open Settings › Apps › Installed Apps (or the legacy Add/Remove Programs panel) and uninstall any existing copy of Innioasis Updater. Starting clean prevents file conflicts.[ Download Clean Installer for Windows ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)Step 1

### Download the latest installer

Save the installer to your Downloads folder. Close Innioasis Updater if it is currently running.Step 2

### Remove any existing install

Open Settings › Apps › Installed Apps (or the legacy Control Panel › Add/Remove Programs) and uninstall Innioasis Updater so the reinstall starts from a clean slate.Step 3

### Install and relaunch

Run the installer you downloaded—Windows will prompt for permission. When setup finishes, launch Innioasis Updater; it should now detect 1.8.2.8 automatically and pick up updates again.

 This also fixes slow startups and gets Updater fetching firmware releases directly from the developers again. 

## macOS: Refresh with the DMG Installer

The macOS installer clears out the old files and installs 1.8.2.8.[ Download Innioasis Updater DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - Open the downloaded DMG and expand the Finder window so you can see the Reinstall option.
  - Run the Reinstall command to refresh the existing copy of Updater. This removes older helper files that may block new features.
  - Launch Innioasis Updater again from Applications. Confirm the About panel lists version 1.8.2.8.
 If you see “Innioasis Updater cannot be opened” after reinstalling, go to System Settings › Privacy & Security and choose Open Anyway to approve the app. 

## After You Update to 1.8.2.8

Once you are on the latest version, you gain access to the features below. These are only available on current builds.
  - One-click installs for original firmware, community releases, and Rockbox builds downloaded directly from the developers' releases.
  - Clear guided steps that tell you when to connect the player and when it is safe to unplug.
  - General stability improvements and dramatically faster launch times across both platforms.

 Need help verifying your version? Open Innioasis Updater, choose Help › About, and confirm the build shows 1.8.2.8. 

## Still Need Assistance?

If the clean install fails, capture any error messages and reach out to the Innioasis community support channels. Include your OS version, Updater build (if available), and the steps you have already tried.

Keeping your install current ensures you always receive the newest firmware packages and tools as they roll out.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
