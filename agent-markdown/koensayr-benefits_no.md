---
title: "Why Koensayr for your Innioasis Y1 | Koensayr benefits - Innioasis Firmware Downloads"
description: "Koensayr patches the stock Y1 firmware: Artist to Album navigation and AVRCP 1.3 Bluetooth metadata and controls for car stereos, without changing the interface."
language: "no"
source: "https://innioasis.app/koensayr-benefits_no.html"
---

# Why Koensayr for your Innioasis Y1 | Koensayr benefits - Innioasis Firmware Downloads

Custom software · Koensayr

# Why Koensayr for your Innioasis Y1

Koensayr keeps the interface you know and fixes what annoys you. Music browses by artist, and Bluetooth shows track names and works with your car controls.[Get Koensayr in Updater](guide_no.html?model=Y1&software=koensayr-y1)[Y1 installasjonsside](koensayr-y1-software_no.html)

## Modelltilgjengelighet

Hvilke Innioasis modeller kjører den?[Y1 · Tilgjengelig](koensayr-y1-software_no.html)Y2 · Not available

Y1- og Y2-bygg er separate, så hent den som er laget for spilleren din i Programvarenedlastinger – aldri bytt ut den ene med den andre.

## Hvorfor velger folk det

Keep the stock player. Fix the annoying parts.
  - Artist → Album navigation — The stock music app gains the Artist-to-Album flow it was missing — no more digging through folders.
  - Bluetooth that works in the car — Spec-compliant AVRCP 1.3 metadata and controls: your head unit sees track titles, the playhead, and repeat/shuffle state.
  - Pairing that actually pairs — Audio and pairing config tuned for car stereos and headsets, including auto-pairing fixes.
  - Root when you need it — A minimal setuid su is installed for adb escalation — useful for diagnostics and tinkering.
  - Less bloat — Never-used system apps are removed to free RAM and reduce background work.
  - No learning curve — The interface is the Y1 interface. Koensayr changes behaviour, not looks.

## Fellesskap

Hva samfunnet sier

Koensayr is the software for people who like the stock Y1 interface and simply want it fixed where it is frustrating. Its name is a Star Wars deep cut — Koensayr built the Y-Wing, and Y-Wing leads to Y1.

The most-talked-about win in the community is Bluetooth: proper track metadata and controls on car stereos and headsets (AVRCP 1.3), which stock software famously gets wrong. If you live in your car, this is the software people point you to.
  - [r/innioasis · Koensayr and car Bluetooth](https://www.reddit.com/r/innioasis/)

## Hva prosjektet tilbyr
  - Artist → Album navigation patched into the system music APK
  - AVRCP 1.3 metadata and control: full track metadata, ms-precision playhead, track and battery notifications, and bidirectional repeat/shuffle
  - Bluetooth pairing fixes: audio.conf, auto_pairing.conf, blacklist.conf, and build.prop edits for car and headset pairing
  - Root access via a minimal setuid su for adb escalation; stock adbd stays untouched
  - System debloat — preinstalled bloatware removed
  - Optional ADB enablement in build.prop
  - Diagnostic tooling for investigating Bluetooth behaviour on real hardware

## Ting å vite først
  - Currently Y1 only, and it keeps the stock interface — it is a patcher, not a launcher
  - It is the most technical route: the patcher runs on a Linux host and flashes via MTKClient, so it suits confident users
  - The project only patches known stock softwares — check your software version matches
  - Restoring Original Software for your model is still the way back if you change your mind

## Kom i gang

Select Y1 in Updater, choose Koensayr, and follow the release notes. The tutorial walks through the patcher flow in order.[Browse Koensayr releases](firmware_no.html?model=Y1&software=koensayr-y1)[Y1 opplæring](guides/koensayr-y1.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
