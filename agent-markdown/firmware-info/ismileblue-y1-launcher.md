---
title: "About JJ Launcher (Y1, Y2) - README.md - Innioasis Updater"
description: "A launcher Software for Y1."
language: "en"
source: "https://innioasis.app/firmware-info/ismileblue-y1-launcher.html"
---

# About JJ Launcher (Y1, Y2) - README.md - Innioasis Updater

[← Firmware Downloads](../firmware.html)

Firmware README · Y1 · Y2

# About JJ Launcher

A launcher Software for Y1.

Also known as: README.md · ismileblue/y1_launcher · y1_launcher · JJ Launcher · ismileblue-y1-launcherY1 · Y2[Open the JJ Launcher guide](../guides/jj-launcher-y1.html)[Install with Updater CE](../firmware.html?model=Y1&software=jj-launcher-y1)[Why JJ Launcher?](../jj-launcher-benefits.html)Downloads from Firmware Archive24,591

Screenshot_20260701_103518Screenshot_20260704_234025Screenshot_20260729_005123Screenshot_20260712_224805Screenshot_20260711_225933Screenshot_20260615_172516Screenshot_20260615_172223Screenshot_20260624_181608Screenshot_20260624_181513

## ☕ Support / Donation

If you like my project, consider buying me a coffee!

[Ko-fi](https://ko-fi.com/ismileblue)

# JJ Launcher (MO-ON Launcher)

for innioasis y1

PlatformStatus

[!WARNING]⚠️ IMPORTANT: This has only been tested on System Software version 2.1.9. It is highly recommended to check your own firmware version before proceeding with the installation.

## 🛠️ Note for Users / Bug Reports

⚠️ Important Notice Please note that this launcher is currently in its Alpha stage, and you may encounter unexpected bugs or stability issues.

If you find any bugs or have suggestions, please open an Issue in this repository. I will do my best to address them and release updates whenever my schedule allows. Thank you for your patience and support! 🙏

## 🌟 Key Features
  - Custom Embedded Media Scanner
    - Automatically and rapidly categorizes large music libraries without relying on the Android system scanner.

  - Advanced Playback & EQ Controls
    - Full support for shuffle, repeat modes, and built-in device Equalizer (EQ) presets.

  - Global Hardware Key Mapping
    - Skip to the previous or next track using physical hardware buttons from any screen within the app.

  - Real-time Main Screen Sync
    - The album art and track information on the main screen sync instantly whenever the active song changes.

  - Infinite Custom Themes
    - Easily add and apply your own custom color themes simply by copying files.

  - Dynamic HD Blur Background
    - Generates a high-definition blurred wallpaper dynamically matching the currently playing album art.

  - In-App Bluetooth Pairing
    - Scan and pair Bluetooth devices instantly within the launcher settings without needing to leave the app.

  - Wheel-Optimized Virtual Keyboard
    - Type Wi-Fi passwords and connect directly using a specialized keyboard tailored for wheel-input devices.

  - Wireless PC File Upload
    - Host a local Wi-Fi Web Server to wirelessly upload music files directly from your PC browser without cables.

## 🚀 Installation & Update Guide

You can easily install the launcher using the Innioasis Updater. Please perform the update using the updater program provided at [https://innioasis.app/](https://innioasis.app/)Installation Screenshot

## 🎧 Bluetooth Connection & Pairing

Bluetooth headphone connection testing has been successfully completed, and it works perfectly!Bluetooth Pairing Screenshot

[!CAUTION] ⚠️ Important Security Permission Note If you encounter a security-related error message when trying to connect after pairing, you must grant the secure settings permission via ADB by running the following script:`adb shell pm grant com.themoon.y1 android.permission.WRITE_SECURE_SETTINGS`

# 🎨 Y1 Theme Editor User Manual
  - You can easily design and customize your own themes using the web editor below:

👉 [Go to Theme Editor](https://theme-editor-gules.vercel.app/)
스크린샷 2026-06-24 220127

⚠️ Note: This manual and the themes created are only compatible with Launcher version 0.8 or higher.

The Y1 Theme Editor is a powerful web-based tool that allows you to intuitively design and build custom themes for your Android device directly from your smartphone or PC browser. Even without coding knowledge, you can create a complete theme package (.zip) simply by dragging, dropping, and adjusting properties.

## 🚀 1. Basic Interface (Modes)

You can toggle between two main modes using the buttons at the top left of the editor.
  - 🛠️ Edit Mode: A design mode where you can click to select elements and freely move them around the screen using drag and drop.
  - ▶️ Play Mode: A mode to simulate how elements will react to wheel scrolling or touching on the actual device. Hover over buttons to preview their focused colors and icon changes.

## 🌍 2. Global Settings

Define the core rules and color palette that apply to the entire theme.
  - Theme Name: Name your theme. (This will also be used as the generated `.zip` file name.)
  - Custom Font: Upload a custom font (`.ttf`, `.otf`, etc.) to use on the device. It will be applied to the preview window immediately.
  - Colors & Styles (Android Hex): Set colors using Android's Hex format (`#AARRGGBB`). The editor provides a slider to easily adjust transparency (Alpha).
    - Text Primary / Secondary: Main and sub-text colors.
    - Bg Overlay: A translucent overlay color placed over the main background wallpaper.
    - Status Bar Bg: Background color of the top status bar.
    - Btn Normal / Focused: Button background colors for default and selected (focused) states.

  - Default Button Radius: The default corner roundness applied to all buttons in the theme.

## 🧩 3. Element Settings & Types

These are the components (elements) you can place on the screen. Click [Add New Element] and change the `Type` to use them. (Note: The editor automatically renders overlapping items in this order: Design Box ➔ Widget ➔ Button)

### 1) Standard Button
  - Interactive elements that the user can click or navigate to.
  - You can add text and icons, and dictate the wheel scrolling order using the `Focus Index`.

### 2) Widgets
  - Digital Clock: Displays the current time and date in text format.
  - Analog Clock: An analog clock with a smooth second hand that inherits your theme's color settings.
  - Circular Battery: A circular battery gauge with the percentage in the center.
  - Battery Bar: A horizontal, pill-shaped battery bar.
  - Album Art: Displays the cover, title, and artist of the currently playing track. You can flexibly align the text relative to the album image (Top, Bottom, Left, Right).

### 3) Design Box
  - A pure design element used to partition the screen or create an aesthetic background/frame behind buttons.
  - Beyond solid colors, you can upload high-resolution photos from your PC. The editor will automatically optimize (compress) them to prevent device overload and create a perfect 'Center Crop' frame matching the box's radius.

## 🎯 4. Key Properties Guide

### 📌 Layout & Coordinates
  - Gravity (Anchor): Determines the reference point for the element's position. (e.g., Selecting `bottom|center_horizontal` and setting Y to 15 will fix the element 15px above the bottom-center of the screen).
  - X / Y: The offset distance from the chosen Gravity anchor point.
  - Width / Height: The dimensions of the element. Entering `0` will automatically adjust the size based on its contents (Auto).

### 📌 Text Align
  - Specifies the alignment and position of the text inside a button or widget (`Left`, `Center`, `Right`, `Top`, `Bottom`).

### 📌 Focus Index
  - A crucial setting exclusively for standard buttons (`Type: button`)!
  - It explicitly dictates the exact order in which the focus moves when spinning the physical wheel on the Android device. Start from `0` and assign numbers sequentially (`1, 2, 3...`).

### 📌 Action

The direct shortcut command executed on the device when a button is clicked.
  - `Now Playing` (Current playback screen)
  - `Music Library` (Audio browser)
  - `Root Folder` (Device's overall file manager)
  - `Bluetooth`, `Wi-Fi Settings`, `Settings Menu`
  - `Web Server` (Wireless file transfer server)
  - `Display Brightness`, `Storage Info`, `Date & Time Settings`, etc.

## 💾 5. Export & Application
  - Once your design is complete, click the [Download Theme (.zip)] button at the bottom right.
  - The editor will gather all the custom fonts, icons, and background images you uploaded and bundle them perfectly into a single `.zip` file.
  - Unzip (extract) the downloaded `.zip` file, and move the extracted folder into the `/Y1_Themes/` directory on your Android device. Then, open the app's theme settings and select your new theme to apply it instantly!

💡 Tip (Import Config): If you want to modify a theme later, simply extract your downloaded `.zip` file and load the `config.json` file inside it using the [Import Config] button. Your workspace and layout will be perfectly restored!

# How to Create a Custom Theme for JJ Launcher for v0.6

Creating a custom theme is the ultimate way to make this DAP (Digital Audio Player) truly yours! The launcher dynamically loads theme resources (colors, icons, and fonts) directly from the device's internal storage.

## 🛠️ Step 1: Create the Theme Folder
  - Connect your device to a PC or open your file manager app.
  - Navigate to the root theme directory: `/storage/sdcard0/Y1_Themes/`
  - Create a new folder inside it and give it a name without spaces (e.g., `/storage/sdcard0/Y1_Themes/Cyberpunk_Dark/`).

## 🛠️ Step 2: Prepare Custom Icons & Fonts (Optional)

Drop your custom assets directly into your new theme folder.
  - Custom Icons: Must be `.png` files with a transparent background. Name them exactly as follows:
    - `icon_now_playing.png` (Now Playing menu)
    - `icon_music.png` (All Songs / Library menu)
    - `icon_bluetooth.png` (Bluetooth setup)
    - `icon_setting.png` (Settings menu)
    - `icon_radio.png` (FM Radio)
    - `icon_server.png` (Web Server menu)
    - `icon_default_album.png` (Fallback image for missing album art)

  - Custom Font: Drop a `.ttf` or `.otf` font file into the folder (e.g., `myfont.ttf`).

## 🛠️ Step 3: Create the `config.json` File

This is the core of your theme. Create a text file named exactly `config.json` inside your theme folder and paste the following template:`{ "name": "My Awesome Theme", "font": "myfont.ttf", "textPrimary": "#FFFFFF", "textSecondary": "#88AADD", "bgOverlay": "#DD0F172A", "statusBarBg": "#99002255", "btnNormal": "#221E40AF", "btnFocused": "#DD3B82F6", "btnFocusedText": "#000000", "button_radius": 30 }`

## 🛠️ Step 4: Understanding the Configuration Values
  - `name`: The display name of your theme in the Settings menu.
  - `font`: The exact filename of the custom font (delete this line to use the system default font).
  - `textPrimary`: Color for main titles, active text, and the clock.
  - `textSecondary`: Color for artist names and inactive text.
  - `bgOverlay`: Background color for menus. The first two characters dictate transparency (e.g., `DD`).
  - `statusBarBg`: Background color for the top status bar. (Delete this line to default to `bgOverlay`).
  - `btnNormal`: Default background color of list buttons.
  - `btnFocused`: Highlight color when a button is selected (also applies to battery ring and volume bars).
  - `btnFocusedText`: Text color inside a highlighted button.
  - `button_radius`: Controls button roundness (`0` = sharp square, `10` = slightly rounded, `30+` = fully rounded pill).

💡 Quick Tip: Always use 8-character Hex Codes (e.g., `#DD0F172A`) for background colors if you want transparency. The first two characters (`DD`) control the opacity (`00` for invisible, `FF` for solid).

## ☕ Support / Donation

If you like my project, consider buying me a coffee!

[Ko-fi](https://ko-fi.com/ismileblue)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
