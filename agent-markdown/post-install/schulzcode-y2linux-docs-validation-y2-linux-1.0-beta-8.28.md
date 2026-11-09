---
title: "Y2Linux 1.0 Beta 8.28 (Baseline 127) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.28 Baseline 127 Status: PUBLISHED as GitHub release baseline-127 2026-10-23, installed on the owner's player first. Release 1.0.0-beta.8.28 , Reborn 1."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.28.html"
---

# Y2Linux 1.0 Beta 8.28 (Baseline 127) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.28 (Baseline 127)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.28 (Baseline 127)

Status: PUBLISHED as GitHub release `baseline-127` (2026-10-23), installed on the owner's player first. Release `1.0.0-beta.8.28`, Reborn `1.0.0-beta.8.28`, kernel `6.18.56-y2linux-1.0.0-beta.8.28`, update sequence 9200, root `2026.08-platform-v1.168`, Linux `f3f938a`, Reborn `f6eb0b2`. Built with `tools/production/release.py` (137 s, resumed workspace, update based on `baseline-126`): container suite 879 OK, host suite 906 OK (the load-sensitive report tests failed once in one of three runs and pass alone, as before this change); Reborn workspace tests, clippy and fmt clean; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.28 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 31602ecf94b04ded09675185fd85d4660d57195abf19f694e55dc2e91a02c6f0 |
| Y2ROOT | 74f5ab30ab7c90ca020ff1059a60bc51482a11deec6d9e386e8a6f5887c6f3d4 |
| RECOVERY | 2aebe45061883f2d039fecb255c281fec46f8137f784a4f758878485f0c8ad49 |
| Y2DATA (no SSH key) | 88eb57a6df297917383c85b53288ad9254feaf33ba5eb8bda4e6a944feb80b68 |

## Why

[Y2Reborn #20](https://github.com/SchulzCode/Y2Reborn/issues/20): a user could not get online; the player said "Connecting…", then "Saved". After about 15 tries they found one wrong letter in the password: "the system never said the password was wrong". Report a19646dd (install aa96e00a, 8.21, 109 failed 4-way handshakes) is very likely the same player.

Reproduced on the owner's player (8.27) with a wrong password under the owner's network name (not saved): each try ended in `WRONG_KEY` about 10 s later and the platform recorded `wrong_credentials`, but its Wi-Fi state stayed `Scanning`/`Associating` (it used the failure only in the other supplicant states), and the "network not found" that follows each failure (the network is disabled for a while) replaced the record. Reborn shows "Check the password" only for `Failed`. Reborn also saved every typed password at once (`SAVE_CONFIG` before trying it), so the row said "Saved", added a new entry each time (15 tries, 15 saved copies, all tried), and its `SELECT_NETWORK` left every other saved network disabled in the saved configuration.

## What changed since Beta 8.27``````````````````````````````````

| Change | Detail | Evidence |
| --- | --- | --- |
| A wrong password is reported | The platform keeps the credential failure (wrong_credentials, authentication_failed, authentication_rejected) with the network id it belongs to until the next connect, through the "not found" that follows, and reports Wi-Fi as Failed with that reason (failed_network_id in network.json) | Linux eb6b4ce; tests/test_wifi_failure_evidence.py |
| A join is tried before it is saved | Reborn's Wi-Fi worker adds the entry, selects it and watches the supplicant: connected → kept, older entries of the same name removed, the other saved networks enabled again, saved; WRONG_KEY → wrong password; three "not found" → not in range; two other auth failures or 30 s → couldn't connect. A failed entry is removed and the previous network comes back. Selecting a saved network is checked the same way (never removed) | Reborn e5b54fb; a_join_is_saved_only_when_it_connects (fake supplicant) |
| The player says so | While checking, the row says Checking password…; a wrong typed password reopens the keyboard with the text kept and Wrong password (the eye key shows it); Connected to …, … is not in range, Couldn't connect otherwise. A saved network whose password stopped working says Wrong password on its row and asks for the new one when selected; Change Password in a saved network's menu | Reborn e5b54fb; a_wrong_wifi_password_reopens_the_keyboard_with_it_and_says_so; preview 26c-wifi-wrong-password |
| Diagnostics | rebornctl test wifi-join --saved ID (the page's join on a saved network) and wifi-join-wrong --saved ID (a wrong password under its name; nothing is left behind) | Reborn e5b54fb |

## Device results (owner's player)``````````````````````

| Check | Result |
| --- | --- |
| Reproduced on 8.27 first | a wrong password under the owner's network name (not saved): WRONG_KEY every ≈10 s, platform record wrong_credentials, Wi-Fi state Scanning/Associating for 90 s, never Failed; the record flipped to ap_unavailable between tries; network restored afterwards |
| OTA 9100 → 9200 | Acknowledged on health boot 1, taint 0, Wi-Fi Online |
| rebornctl test wifi-join-wrong --saved 0 (Reborn's join, wrong password) | WrongPassword after 5.8 s; saved networks 1 before, 1 after (the try removed); platform Failed / wrong_credentials / failed_network_id 1 (the removed try, which Reborn ignores), Online again 4 s later |
| rebornctl test wifi-join --saved 0 | Joined; the saved configuration still holds one network, none disabled |

## Open
  - The "saved network's password changed" path was host-tested only (the owner's saved password cannot be read back to

restore it after a test).
  - WPA3-only (SAE) networks are still not offered (`password_required` accepts PSK only).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
