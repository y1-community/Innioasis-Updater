---
title: "Guide til installation af firmware og lagergendannelse | Innioasis Updater CE - Innioasis Firmware-downloads"
description: "Installer brugerdefineret firmware eller gendan officiel fabriksfirmware på Innioasis Y1, Y2, G1, G3, G5, R1, PR1 og Timmkoo Q5, Q3 med Innioasis Updater CE."
language: "da"
source: "https://innioasis.app/firmware-guide_da.html"
---

# Guide til installation af firmware og lagergendannelse | Innioasis Updater CE - Innioasis Firmware-downloads

Guide til installation af firmware og lagergendannelse

# Installer eller gendan firmware på din enhed

Vælg den model, der er trykt på din afspiller. Følg derefter trinene i Updater CE. Den klarer resten.[Få Updater CE](guide_da.html#platform)[Gennemse firmwarearkivet](firmware_da.html)[Fejlfinding](troubleshooting_da.html)

Vælg den model, der er trykt på din afspiller og den software, du ønsker, og åbn derefter denne vejledning. [Gennemse software og lagerfirmware efter model](firmware_da.html).

## 

[Få Updater CE](guide_da.html#download-updater)[Fuld skriftlig tutorial](guide_da.html)

## Få Innioasis Updater CE

Her er hvor du skal starte, hvis du ikke allerede har fået Updater CE.Hent det på Updater CEmed guidet installation

### Windows

Download installationsprogrammet, åbn det, og følg opsætningsvejledningen.[Download og installer driver](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Download app og drivere](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Blokeret af Edge?](#)

Hvis Windows forhindrer dig i at køre appen eller ikke starter den, skal du åbne Indstillinger, klikke på Privatliv og sikkerhed → Windows Sikkerhed → App- og browserkontrol og slå Smart App Control fra. [Vil Windows ikke starte appen? Hjælp](#smart-app-control)

Du skal genstarte din pc efter installationen for at få den til at fungere.

### macOS

Download appen og flyt den til applikationer. Hvis macOS blokerer det, skal du åbne Systemindstillinger, derefter Privatliv og sikkerhed og klikke på Åbn alligevel. [Hvordan dette virker](https://support.apple.com/en-gb/102445#openanyway)[Download Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Download AppImage til Intel- og AMD-systemer, gør det eksekverbart, og kør det.[Download AppImage til Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Noter til Linux-opsætning](drivers_da.html#linux)En anden platform?

Har du brug for de længere noter til computeropsætning? Åbn [Windows](drivers_da.html#windows) eller [Linux](drivers_da.html#linux) opsætningsvejledning.

## Går tilbage til original software

For at gå tilbage, vælg din model, vælg Original software, så løb Installer / Gendan. Det er alt. Updater erstatter systemsoftwaren for dig.[Y1-gendannelsesvejledning](guides/restore-original-y1.html)[Y2-gendannelsesvejledning](guides/restore-original-y2.html)

## Softwarevejledninger efter model

Vælg din model, og åbn derefter guiden til din software.

### Innioasis Y1

Software til Y1:

### Innioasis Y2

Software til Y2:

En note om de to værktøjer

## Hvilket værktøj skal jeg bruge?

Innioasis Opdaterer CE er den sikreste måde at opdatere din afspiller på. Det gemmer din musik, videoer og Bluetooth-parringer. Den fortæller dig, når opdateringer er klar. Det kører på Windows, macOS og Linux. Innioasis Universal Flash Tool sletter din afspiller og virker på færre computere.[Åbn den fulde sammenligning](updater-comparison_da.html)

### Vil Windows ikke starte appen? Sådan slår du Smart App Control fra

Windows Defender SmartScreen eller Smart App Control kan blokere nyligt downloadede fællesskabsapplikationer, før signaturomdømmet breder sig. Smart App Control påvirker i øjeblikket populære applikationer som Epic Overlay Service (brugt af Fortnite) - Updater CE er sikker og verificeret at bruge. Hvis du slår Smart App Control fra, kan Updater CE åbne og køre normalt.
  - Åbn Indstillinger på din Windows-pc (tryk på Win + I).
  - Klik Privatliv og sikkerhed i venstre sidebjælke, og klik derefter Windows Security.
  - Klik App og browser kontrol.
  - Under Smart app kontrol, klik Indstillinger for Smart App Control.
  - Indstil kontakten til Slukket for at tillade Updater CE at starte.

Blokeret af Edge? Hvis Microsoft Edge blokerer selve overførslen, skal du klikke på knappen Flere muligheder (…) → Behold → Vis mere → Behold alligevel.

Genaktiver Smart App Control senere: Når du vil slå Smart App Control til igen, kan du genaktivere den via Windows-registreringsdatabasen under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` ved indstilling `VerifiedAndReputablePolicyState` til `1` (Til) eller `2` (Evalueringstilstand) og genstart.Tæt hjælp

## Var dette nyttigt?

Dit svar hjælper med at forbedre denne vejledning.Ja, jeg fandt det nyttigtIkke endnu[Fortæl os, hvordan vi kan forbedre os](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
