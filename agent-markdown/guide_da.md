---
title: "Kom godt i gang med Innioasis Updater CE | Installer eller gendan firmware på enhver Innioasis eller Timmkoo afspiller - Innioasis Updater"
description: "Download Innioasis Updater CE til Windows, macOS eller Linux, og installer eller gendan derefter firmware på enhver Innioasis eller Timmkoo afspiller i nogle få guidede trin."
language: "da"
source: "https://innioasis.app/guide_da.html"
---

# Kom godt i gang med Innioasis Updater CE | Installer eller gendan firmware på enhver Innioasis eller Timmkoo afspiller - Innioasis Updater

Hurtig start

# Kom godt i gang med Innioasis Updater CE

Fungerer med alle Innioasis og Timmkoo lydafspillere. Installer Innioasis Updater CE på din computer, vælg din model og den ønskede software, og følg derefter vejledningen.

## 

[Få Updater CE](guide_da.html#download-updater)[Fuld skriftlig tutorial](guide_da.html)

## Få Innioasis Updater CE

Innioasis Opdaterer CE er appen, der installerer officielle opdateringer og community-software på din afspiller. Den beholder din musik og dine indstillinger, og den kører på Windows, macOS og Linux.

### Windows

Download installationsprogrammet, kør det, og genstart derefter din pc, når det er færdigt.[Hent drivere](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Download Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

Hvis Windows forhindrer dig i at køre appen eller ikke starter den, skal du åbne Indstillinger, klikke på Privatliv og sikkerhed → Windows Sikkerhed → App- og browserkontrol og slå Smart App Control fra. Smart App Control påvirker i øjeblikket populære applikationer som Epic Overlay Service (brugt af Fortnite) - Updater CE er sikker og verificeret at bruge. [Vil Windows ikke starte appen? Hjælp](#smart-app-control)

Genstart din pc efter installation. Driver hjælp er i [Windows opsætningsnoter](drivers_da.html#windows).

### macOS[Download Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Hvis din Mac forhindrer dig i at køre appen for første gang, skal du åbne Systemindstillinger, klikke på Privatliv og sikkerhed, rulle ned til Sikkerhed og klikke på [Åben alligevel](https://support.apple.com/en-gb/102445#openanyway). Du kan også Ctrl-klikke (eller højreklikke) på appen i Finder og vælge Åbn.

Fungerer på Intel og Apple Silicon Macs med macOS Monterey og nyere.

### Linux

Download AppImage til Intel- og AMD-systemer, gør det eksekverbart, og kør det.[Download AppImage til Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Noter til Linux-opsætning](drivers_da.html#linux)En anden platform?

Du skal bruge din afspiller, et USB datakabel, der bærer data (et kabel, der kun kan oplades), og et par minutter. Hold kablet tilsluttet, indtil Updater CE siger, at det er gjort.

## Vælg din model og software
  - Enhedsmodel: vælg den model, der er trykt på afspilleren, Y1 eller Y2. Software lavet til den ene model kan ikke installeres på den anden.
  - Software og udgivelse: vælg Original Software, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player, eller Koensayr, når det er angivet for din model, og vælg derefter en udgivelse. Stabil er det sikre valg.
  - Installer: klik Installer / Gendan, sluk for afspilleren helt, og tilslut kun USB-kablet, når Updater CE spørger.
  - Afslut: lad afspilleren og kablet være i fred indtil succesmeddelelsen, afbryd derefter og start afspilleren.

Y1 spillere, der blev leveret med original software før 2.0.0 har brug for Enhed Type B. Alle andre beholder standard Type A.Opdateringsvejledning til tilslutning af en slukket afspillerFølg den live Updater CE-prompt for din model.

## Går tilbage til original software

Brugerdefineret software er reversibel. I Updater CE, vælg din model, vælg Original software, vælg en stabil udgivelse, og kør derefter Installer / Gendan på samme måde. Der er ikke noget at slette i hånden.[Y1-gendannelsesvejledning](guides/restore-original-y1.html)[Y2-gendannelsesvejledning](guides/restore-original-y2.html)

Hvis et blitz stopper før USB-prompten, skal du først kontrollere kablet, platformsopsætningen og modellen. Se [fejlfinding](troubleshooting_da.html) for rettelser, den [Y1 og Y2 gendannelsesvejledning](guides/recovery.html) for strøm- og hjulfejl, og [SP Flash Tool](sp-flash-tool_da.html) for avanceret genopretning.

## Softwarevejledninger efter model

Åbn vejledningen til din model og den software, du har valgt.

### Innioasis Y1

Software til Y1:

### Innioasis Y2

Software til Y2:

## Hvilket værktøj skal jeg bruge?

Denne vejledning bruger Innioasis Updater 2.5.1, også kaldet Updater CE. Det holder dine sange, videoer og Bluetooth-parringer sikre. Den fortæller dig, når opdateringer er klar. Innioasis Universal Flash Tool tørrer din afspiller og kræver manuelle trin. [Sammenlign værktøjerne →](updater-comparison_da.html)

## Vil Windows ikke starte appen? Smart App Control-løsning

Windows Defender SmartScreen eller Smart App Control kan blokere nyligt downloadede fællesskabsapplikationer, før signaturomdømmet breder sig. Smart App Control påvirker i øjeblikket populære applikationer som Epic Overlay Service (brugt af Fortnite) - Updater CE er sikker og verificeret at bruge. Hvis du slår Smart App Control fra, kan Updater CE åbne og køre normalt.
  - Åbn Indstillinger på din Windows-pc (tryk på Win + I).
  - Klik Privatliv og sikkerhed i venstre sidebjælke, og klik derefter Windows Security.
  - Klik App og browser kontrol.
  - Under Smart app kontrol, klik Indstillinger for Smart App Control.
  - Indstil kontakten til Slukket for at tillade Updater CE at starte.

Downloadet via Edge? Hvis Edge blokerer selve overførslen, skal du klikke på knappen Flere muligheder (…) → Behold → Vis mere → Behold alligevel.

Genaktiver Smart App Control senere: Når du vil slå Smart App Control til igen, kan du genaktivere den via Windows-registreringsdatabasen under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` ved indstilling `VerifiedAndReputablePolicyState` til `1` (Til) eller `2` (Evalueringstilstand) og genstart.

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
