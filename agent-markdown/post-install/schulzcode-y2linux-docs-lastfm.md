---
title: "Last.fm scrobbling - Innioasis Updater"
description: "Last.fm scrobbling Since Y2Linux 1.0 Beta 7.7 the Reborn player can send the songs you listen to to your Last.fm https://www.last.fm profile"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-lastfm.html"
---

# Last.fm scrobbling - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Last.fm scrobbling

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Last.fm scrobbling

Since Y2Linux 1.0 Beta 7.7 the Reborn player can send the songs you listen to to your [Last.fm](https://www.last.fm) profile ("scrobbling"), straight from the player: no computer, no phone app, no extra service. It also works without Wi-Fi: plays are kept on the player and sent later.

## Set up
  - Settings → Library → Last.fm → Connect with Your Phone. The player shows a QR code.
  - Scan it with your phone's camera. Last.fm's own page opens and asks whether Y2Reborn may

scrobble for you (log in there first if needed). Choose Allow.
  - The player notices by itself within a few seconds: Scrobbling to Last.fm as ….

No phone at hand? Sign In with Password types your Last.fm username and password on the player's keyboard instead (see [Your password](#your-password) for how it is handled).

Settings → Library → Last.fm then shows your account and:

| Setting | What it does |
| --- | --- |
| Scrobble | Send counted plays (on by default). |
| Show Now Playing | Show the song you are listening to on your profile while it plays (on by default). It is sent again when you continue after a pause or play the song again. |
| Send Now | Send waiting plays at once; the line shows how many are waiting. |
| Also Write .scrobbler.log | Also keep a classic scrobbler log file (below); works without an account. |
| Disconnect | Sign out; forgets the sign-in and the plays still waiting. |

## What counts as a play

Reborn follows Last.fm's rules:
  - A song counts once you have heard half of it, or 4 minutes, whichever comes first.
  - Songs shorter than 30 seconds never count.
  - Only time you actually listened counts: paused time and skipping ahead add nothing. Going

back to the start of a song (Repeat, Previous) is a new play.
  - Each play carries the moment the song started.
  - Internet radio is not scrobbled, and neither are files without an artist and title tag

(fix the tags on a computer to have them counted).

## Offline and sending
  - A play is written to the player's storage the moment it counts, so sleep, an empty battery

or a system update lose nothing.
  - When Wi-Fi is connected, waiting plays are sent in groups of up to 50. Sending **never wakes the

player and never keeps Wi-Fi on** just for this: plays simply wait until the player is online anyway.
  - Last.fm only accepts plays from about the last two weeks; older waiting plays are dropped

when sent. For players that are rarely online, switch on the scrobbler log.
  - A play is only stamped once the player's clock is trustworthy (set from the internet or

continued by the clock chip since). Plays during an unknown clock are dated later or left out, never sent with a wrong date.
  - If Last.fm is unreachable, the player waits and tries again: 1 minute, then 2, 4 … up to an hour,

with a little random extra so that players do not all retry in the same second after an outage.
  - A play Last.fm refuses as invalid is left out, so it cannot hold back the plays after it.

## The scrobbler log (`.scrobbler.log`)

With Also Write .scrobbler.log on, every counted play is also appended to `.scrobbler.log` at the top of Internal Storage, in the AUDIOSCROBBLER/1.1 format that Rockbox players use. Copy it to a computer over USB and upload it with any tool that reads that format (to Last.fm, Libre.fm or ListenBrainz). It needs no account. Delete or replace the file after uploading; the player starts a new one.

## Your data and privacy
  - Nothing is recorded until you choose it: connect Last.fm or switch on the log.
  - What is sent per play: **artist, song title, album, album artist (when different), track

number, length and the start time**. Nothing else: no file names, no location, no device data. Now Playing sends the same for the current song.
  - The waiting plays live in the player's private data partition (not visible over USB); the log

file, if you switch it on, is on Internal Storage where you can see it.
  - Disconnect, Settings → System → Reset & Maintenance → Reset Reborn Settings and the platform's settings reset forget the

sign-in and every waiting play.
  - You can also remove the player's access on Last.fm at any time: last.fm → **Settings →

Applications → Y2Reborn → Revoke**. The player then says Sign in to Last.fm again and keeps the waiting plays for when the same account signs in again. If a different account signs in, they are discarded, never sent to the wrong person.

## Security

### Your password

With the QR code (recommended), the player never sees your password: you type it only into Last.fm's own page on your phone. With Sign In with Password, the password is sent once, over an encrypted connection, to Last.fm's sign-in service, and then forgotten: it is never saved, never written to a log, never shown on screen (the keyboard shows dots), and it never appears in the list of running programs.

### Your sign-in on the player

Last.fm gives the player a session key for your account. It is stored in one file in the player's private data partition, readable only by the system:
  - it is not reachable over USB (the computer only sees Internal Storage, the SD card and,

when needed, the Firmware drive or the read-only Old Storage);
  - it is never written to logs, diagnostics or update images (the release checks refuse any

image that contains it);
  - it only allows what Last.fm allows apps: scrobbling, Now Playing and similar music actions.

It cannot read or change your password or e-mail address;
  - Disconnect, a settings reset or revoking the app on last.fm ends it.

### The connection

Every request goes to Last.fm over HTTPS with certificate checking only; a connection that cannot be verified is refused, and requests are only made once the clock is trustworthy (which certificate checks depend on). Each request is signed the way Last.fm requires. The keys and your data travel in the body of the request, never on a command line other programs could read. Nothing from outside can make the player scrobble: only plays that happen on the player count.

### The app's key

Every app that talks to Last.fm identifies itself with an API key and a shared secret that its developer registered. Y2Reborn's are not in the public source code; the maintainer's build puts them into the player's system as a file only the system can read.

To be honest about the limits: like every music app that scrobbles directly (phone apps, desktop players, browser extensions), the released system image necessarily contains this key, so a determined person could extract it from a downloaded update. With it they could send requests in the name "Y2Reborn". They would not get access to anyone's account, password, sign-in or player. If the key were ever misused, the maintainer resets it and the next update carries the new one (players then sign in again).

## Limits

Normal listening makes about two requests per song (Now Playing and the scrobble), plus one Now Playing when you continue after a pause (at most every 30 seconds); a backlog is sent 50 plays per request; signing in asks Last.fm every 3 seconds for at most 15 minutes, only while the code is shown. That is far below what Last.fm allows, and every player has its own budget. Y2Linux is free, non-commercial software, as Last.fm's API terms require.

## Troubleshooting

| You see | Meaning |
| --- | --- |
| Last.fm Isn't Available | This build has no Last.fm key (for example your own build); the scrobbler log still works. |
| Connect to Wi-Fi first | Signing in needs Wi-Fi; plays are counted offline once you are signed in. |
| The clock isn't set yet | Right after Wi-Fi connects the player may still be setting its clock (secure connections need the right date); try again in a moment. |
| N plays waiting | They go out when Wi-Fi is connected; Send Now tries at once. |
| Sign in to Last.fm again | Last.fm ended the sign-in (for example you revoked it); waiting plays are kept for the same account. |
| The Last.fm sign-in timed out | The code was not approved within 15 minutes; start again. |
| A song did not count | It was shorter than 30 s, was heard less than half (and under 4 minutes), had no artist/title tag, or was internet radio. |

## For people who build Y2Linux themselves

A build only has Last.fm when it is given a key. Register your own API account at

[https://www.last.fm/api/account/create](https://www.last.fm/api/account/create) (use your own application name), then put the key and secret into `~/.local/share/y2linux/lastfm-api.json` as `{"api_key": "…", "shared_secret": "…"}` and run `chmod 600` on it. The build checks the format and the permissions and installs it as `/usr/share/reborn/lastfm-api.json` (root, mode 0600). Never commit this file. Details: [BUILDING](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FBUILDING.md); design and evidence: [Last.fm plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FLASTFM-SCROBBLE-PLAN.md) and the [Beta 7.7](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.7.md) and [Beta 7.8](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.8.md) reports. The code is in Y2Reborn: `crates/reborn-core/src/scrobble.rs` (rules), `crates/reborn-platform/src/scrobble.rs` (queue and log), `crates/reborn-platform/src/lastfm.rs` (Last.fm API) and `app/reborn/src/scrobbling.rs`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
