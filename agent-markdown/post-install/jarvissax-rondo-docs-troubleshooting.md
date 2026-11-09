---
title: "Troubleshooting - Innioasis Updater"
description: "Troubleshooting Installing and updating Innioasis Updater CE doesn't find the Y1 - Try another cable. Many USB-C cables only charge. - Follow the Updater's steps exactly:"
language: "en"
source: "https://innioasis.app/post-install/jarvissax-rondo-docs-troubleshooting.html"
---

# Troubleshooting - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=rondo-y1)

Post-install setup · Rondo · Y1

# Troubleshooting

A lightweight, custom audio operating system for the Innioasis Y1.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=rondo-y1)[Install guide](../guide.html?model=Y1&software=rondo-y1)

# Troubleshooting

## Installing and updating

### Innioasis Updater CE doesn't find the Y1
  - Try another cable. Many USB-C cables only charge.
  - Follow the Updater's steps exactly: the Y1 has to be completely off before you plug it in.

If it's on, hold Power and choose Shut down, or use the reset hole between the headphone and USB ports with a paperclip.
  - Windows: let the Updater install its drivers, and restart the computer once.
  - Close other programs that use the Y1's USB connection (adb, Android Studio).

### The Y1 stays dark after installing

It doesn't switch itself on after an install. Press the Power button. The first start takes a couple of minutes; after the Rondo logo you'll see a spinning click wheel until the main menu appears.

### Rondo isn't in the Updater's list, or has nothing to install

Rondo is for the Y1, Type A. Check that the Updater is set to Y1 and Type A, or [install from a file](https://innioasis.app/guides/rondo-y1.html). Rondo isn't built for the Type B, so with Type B there's nothing to install.

### Software update says Rondo "needs a new firmware"

That release changes the firmware around Rondo, not just Rondo, so it can't install over Wi-Fi or USB. Install it with Innioasis Updater CE, [the same way as the first time](https://innioasis.app/guides/rondo-y1.html). If the Updater offers Keep Data, choose it to keep your settings, Wi-Fi and server connection.

### Software update says "Couldn't check"

The Y1 asks your Rondo server, so it needs Wi-Fi and a connected server (Settings › Server). Without a server, update [from the dashboard or over USB](https://innioasis.app/guides/rondo-y1.html).

### The update page doesn't list the Y1, or can't connect
  - Use Chrome or Edge. Firefox and Safari can't talk to USB devices.
  - Only one program can use the Y1's USB connection: close the Innioasis Updater, and run

`adb kill-server` if you have adb. If the Y1 offers the USB drive, choose Not now. Then unplug the Y1 and plug it back in.
  - Windows: install Google's [USB driver](https://developer.android.com/studio/run/win-usb)

for the Y1; without it, the browser can't see it.
  - Linux: give your user access to USB ID `0bb4:0c03` with a udev rule.

### "That APK isn't signed by Rondo's key"

Only Rondo's own releases install over the Rondo in the firmware. A build you made yourself is signed with your key; put it in a firmware of your own instead ([Building Rondo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fbuilding.md)).

## YouTube Music and YouTube

### "No music server yet"

The Y1 isn't connected to a server. Set one up and connect it in Settings › Server ([server guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md%23finish-the-setup&anchor=finish-the-setup)).

### Settings › Server says "Unreachable"
  - At home: the Y1 and the server must be on the same network, and the server's address must

not have changed. Give the server a fixed address in your router.
  - On a VPS: check the HTTPS from a computer with the `openssl` command in the

[server guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md%23on-a-vps&anchor=on-a-vps). If you use Cloudflare, the record must be "DNS only".
  - Check the address in Settings › Server: `http://` for home, `https://` for a VPS,

and the right port.

### "Token refused"

The server no longer knows this Y1. Another Rondo may have been connected, or the server was set up again. Connect again with a new code from the admin page (Device › Connect a Rondo).

### Songs or videos won't play, or stop partway

YouTube changes things often. On the admin page, open Resolver and press Update now, then Test playback. Activity shows the errors behind it. Settings › Server on the Y1 says "Playback failing" while this is the problem.

### Library, Subscriptions or History are missing

They only appear when the server has a YouTube account. Sign in with a code on the admin page ([details](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md%23your-youtube-account-optional&anchor=your-youtube-account-optional)).

### YouTube Music's home looks generic

Your own YouTube Music home and history need a cookies.txt on the server. If you uploaded one and it stopped working, the admin page's Activity says the cookies were signed out. Export new ones in a private window, and close the window right after.

## The Y1

### The FM radio says "Plug in wired headphones"

The radio needs wired headphones plugged in, because their cable is the antenna. Bluetooth headphones don't work for FM.

### The radio plays but I hear nothing

The radio has its own volume, separate from music. Turn the wheel up on the FM screen. If it's set to Speaker in the options, the sound comes from the Y1's speaker instead.

### My Wi-Fi network isn't listed

The Y1 only sees 2.4 GHz networks. Many routers can switch on 2.4 GHz alongside 5 GHz, or give it its own network name.

### The dashboard won't open
  - The phone or computer must be on the same Wi-Fi as the Y1, and Settings › Dashboard must

stay open on the Y1.
  - macOS: browsers need permission to reach devices on your network. Check System Settings ›

Privacy & Security › Local Network, and switch it on for your browser.
  - Some guest and office networks keep devices from seeing each other. Use a home network.

### Bluetooth headphones aren't found

Put them in pairing mode first (usually by holding the power button until a light flashes), then search on the Y1 or in the dashboard.

### The wheel feels too fast or too slow

Try Settings › Wheel acceleration: Off moves one step per wheel pulse, Fast jumps further on long spins. Wheel vibration and Click sound change how each step feels.

### Getting back to the Y1's original software

Install Original Software (or Rockbox, or another firmware) with Innioasis Updater CE, the same way you installed Rondo. See [Going back](https://innioasis.app/guides/rondo-y1.html).

## Still stuck?

[Open an issue](https://github.com/jarvissax/rondo/issues). Say what you did and what happened. If you can, include Rondo's log. adb works on the Rondo firmware: plug the Y1 in (choose Not now when it offers the USB drive) and run`adb logcat -d -v time -s Y1 > rondo-log.txt`

These are Rondo's own instructions, shown here word for word.

Published by the [jarvissax/rondo](https://innioasis.app/firmware.html?model=Y1&software=rondo-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=jarvissax%2Frondo&software=rondo-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Ajarvissax)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
