---
title: "Disclaimer - Innioasis Updater"
description: "Disclaimer The Innioasis Y1 runs an outdated version of Android. Going online with it has inherent risks. The connections this plugin makes should be save, as they use up"
language: "en"
source: "https://innioasis.app/post-install/rockbox-y1-rockbox-internet.html"
---

# Disclaimer - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=rockbox-y1)

Post-install setup · Rockbox-Y1 · Y1

# Disclaimer

A music-first custom Software with deep playback and theme options.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=rockbox-y1)[Install guide](../guide.html?model=Y1&software=rockbox-y1)

# Disclaimer

The Innioasis Y1 runs an outdated version of Android. Going online with it has inherent risks. The connections this plugin makes should be save, as they use up-to-date certificates and only make secure connections to official Last.fm API servers. With such old software you never know though. Please make your own judgement calls if you are fine with this risk.

# Podcasts

## Adding podcasts
  - Find your feed URL: [https://rss.com/tools/find-my-feed/](https://rss.com/tools/find-my-feed/)
  - Download the wifi config [here](https://github.com/rockbox-y1/rockbox/blob/y1/android/scripts/wifi.cfg)
  - Follow the instructions in the `wifi.cfg` and add 
  - Also make sure to fill your wifi credentials
  - Copy `wifi.cfg` to `.rockbox/wifi.cfg` on the SD card
  - Go to Plugins > Applications > podcast_downloader
  - Controls:

  - Clicking podcast: Loads episodes
  - Long-press on podcast: Context menu - Download all episodes (takes a long time and shows no progress bar)
  - Clicking Episode: Downloads episode
  - Long-press on podcast: Context menu - Play, Re-download, Delete

# Scrobbling: Last.fm, ListenBrainz, Maloja,...

### Last.fm
  - Login to Last.fm
  - Create an application [here](https://www.last.fm/api/account/create) (you only need to enter an application name, e.g. `rockbox`)
  - Save the API key and the Shared secret that is displayed after creating the application
  - Download the wifi config [here](https://github.com/rockbox-y1/rockbox/blob/y1/android/scripts/wifi.cfg)
  - Follow the instructions in `wifi.cfg` and fill all the values necessary
  - Also make sure to fill your wifi credentials
  - Keep this file safe, don't share it online
  - Copy `wifi.cfg` to `.rockbox/wifi.cfg` on the SD card

### ListenBrainz
  - Login to ListenBrainz
  - Copy the user token from your settings page
  - Download the wifi config [here](https://github.com/rockbox-y1/rockbox/blob/y1/android/scripts/wifi.cfg)
  - Follow the instructions in `wifi.cfg` and fill all the values necessary
  - Also make sure to fill your wifi credentials
  - Keep this file safe, don't share it online
  - Copy `wifi.cfg` to `.rockbox/wifi.cfg` on the SD card

Hint: This works for ListenBrainz compatible servers too, just change the apiUrl.

### Scrobble Songs
  - Go to Plugins > Applications > lastfm_scrobbler
  - Follow general setup instructions
  - Upload Scrobbles > Yes
  - (Listen to some music)
  - Press Export

Hint: Set the timezone setting to 0 if it was configured to something else before. The time and time zone is setup automatically once you connect to the internet if you didn't change any time/date settings in the Android System Menus.

These are Rockbox-Y1's own instructions, shown here word for word.

Published by the [rockbox-y1/rockbox](https://innioasis.app/firmware.html?model=Y1&software=rockbox-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=rockbox-y1%2Frockbox&software=rockbox-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Arockbox-y1)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
