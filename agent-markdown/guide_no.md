---
title: "Komme i gang med Innioasis Updater CE | Installer eller gjenopprett fastvare på hvilken som helst Innioasis- eller Timmkoo-spiller - Innioasis Updater"
description: "Last ned Innioasis Updater CE for Windows, macOS eller Linux, og installer eller gjenopprett deretter fastvaren på en hvilken som helst Innioasis- eller Timmkoo-spiller i noen få veilede trinn."
language: "no"
source: "https://innioasis.app/guide_no.html"
---

# Komme i gang med Innioasis Updater CE | Installer eller gjenopprett fastvare på hvilken som helst Innioasis- eller Timmkoo-spiller - Innioasis Updater

Rask start

# Komme i gang med Innioasis Updater CE

Fungerer med alle Innioasis og Timmkoo lydspillere. Installer Innioasis Updater CE på datamaskinen din, velg modell og programvare du ønsker, og følg deretter instruksjonene.

## 

[Få Updater CE](guide_no.html#download-updater)[Full skriftlig opplæring](guide_no.html)

## Få Innioasis Updater CE

Innioasis Oppdaterer CE er appen som installerer offisielle oppdateringer og fellesskapsprogramvare på spilleren din. Den beholder musikken og innstillingene dine, og den kjører på Windows, macOS og Linux.

### Windows

Last ned installasjonsprogrammet, kjør det og start PC-en på nytt når det er ferdig.[Skaff deg drivere](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Last ned Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

Hvis Windows stopper deg fra å kjøre appen eller ikke starter den, åpner du Innstillinger, klikker på Personvern og sikkerhet → Windows Sikkerhet → App- og nettleserkontroll, og slår av Smart App Control. Smart App Control påvirker for tiden populære applikasjoner som Epic Overlay Service (brukt av Fortnite) - Updater CE er trygg og verifisert å bruke. [Vil ikke Windows starte appen? Hjelp](#smart-app-control)

Start PC-en på nytt etter installasjon. Sjåførhjelp er i [Windows-oppsettnotater](drivers_no.html#windows).

### macOS[Last ned Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Hvis Mac-en din stopper deg fra å kjøre appen for første gang, vennligst åpne Systeminnstillinger, klikk på Personvern og sikkerhet, bla ned til Sikkerhet og klikk [Åpne uansett](https://support.apple.com/en-gb/102445#openanyway). Du kan også Ctrl-klikke (eller høyreklikke) appen i Finder og velge Åpne.

Fungerer på Intel og Apple Silicon Mac-maskiner med macOS Monterey og nyere.

### Linux

Last ned AppImage for Intel- og AMD-systemer, gjør det kjørbart og kjør det.[Last ned AppImage for Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Notater om Linux-oppsett](drivers_no.html#linux)En annen plattform?

Du trenger spilleren din, en USB datakabel som bærer data (en kabel som kun kan lades kan ikke installeres), og noen få minutter. Hold kabelen tilkoblet til Updater CE sier at det er gjort.

## Velg modell og programvare
  - Enhetsmodell: velg modellen som er trykt på spilleren, Y1 eller Y2. Programvare laget for én modell kan ikke installeres på den andre.
  - Programvare og utgivelse: velg Original Software, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player, eller Koensayr når den er oppført for modellen din, og velg deretter en utgivelse. Stall er det sikre valget.
  - Installer: klikk Installer / Gjenopprett, slå spilleren helt av og koble til USB-kabelen bare når Updater CE ber om det.
  - Fullfør: la spilleren og kabelen være i fred frem til suksessmeldingen, koble deretter fra og start spilleren.

Y1 spillere som ble levert med original programvare før 2.0.0 trenger Enhet Type B. Alle andre beholder standard Type A.Oppdateringsinstruksjoner for tilkobling av en avslått spillerFølg live Updater CE-ledeteksten for din modell.

## Går tilbake til original programvare

Tilpasset programvare er reversibel. I Updater CE, velg din modell, velg Original programvare, velg en stabil utgivelse, og løp Installer / Gjenopprett på samme måte. Det er ingenting å slette for hånd.[Y1 gjenopprettingsveiledning](guides/restore-original-y1.html)[Y2 gjenopprettingsveiledning](guides/restore-original-y2.html)

Hvis en blits stopper før USB-meldingen, kontroller kabelen, plattformoppsettet og modellen først. Se [feilsøking](troubleshooting_no.html) for reparasjoner [Y1 og Y2 gjenopprettingsveiledning](guides/recovery.html) for strøm- og hjulfeil, og [SP Flash Tool](sp-flash-tool_no.html) for avansert utvinning.

## Programvareguider etter modell

Åpne veiledningen for modellen din og programvaren du valgte.

### Innioasis Y1

Programvare for Y1:

### Innioasis Y2

Programvare for Y2:

## Hvilket verktøy bør jeg bruke?

Denne veiledningen bruker Innioasis Oppdaterer 2.5.1, også kalt Updater CE. Det holder sangene, videoene og Bluetooth-sammenkoblingene dine trygge. Den forteller deg når oppdateringer er klare. Innioasis Universal Flash Tool tørker av spilleren og trenger manuelle trinn. [Sammenlign verktøyene →](updater-comparison_no.html)

## Vil ikke Windows starte appen? Løsning for smart appkontroll

Windows Defender SmartScreen eller Smart App Control kan blokkere nylig nedlastede fellesskapsapplikasjoner før signaturomdømmet sprer seg. Smart App Control påvirker for tiden populære applikasjoner som Epic Overlay Service (brukt av Fortnite) - Updater CE er trygg og verifisert å bruke. Ved å slå av Smart App Control kan Updater CE åpne og kjøre normalt.
  - Åpne Innstillinger på din Windows-PC (trykk Win + I).
  - Klikk Personvern og sikkerhet i venstre sidefelt, og klikk deretter Windows Security.
  - Klikk App- og nettleserkontroll.
  - Under Smart appkontroll, klikk Smart App Control-innstillinger.
  - Sett bryteren til Av for å la Updater CE starte.

Lastet ned via Edge? Hvis Edge blokkerer selve nedlastingen, klikker du på knappen Flere alternativer (…) → Behold → Vis mer → Behold uansett.

Aktiverer Smart App Control på nytt senere: Når du vil slå på Smart App Control igjen, kan du aktivere den på nytt via Windows-registeret under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` ved innstilling `VerifiedAndReputablePolicyState` til `1` (På) eller `2` (Evalueringsmodus) og omstart.

### Vil ikke Windows starte appen? Slik slår du av Smart App Control

Windows Defender SmartScreen eller Smart App Control kan blokkere nylig nedlastede fellesskapsapplikasjoner før signaturomdømmet sprer seg. Smart App Control påvirker for tiden populære applikasjoner som Epic Overlay Service (brukt av Fortnite) - Updater CE er trygg og verifisert å bruke. Ved å slå av Smart App Control kan Updater CE åpne og kjøre normalt.
  - Åpne Innstillinger på din Windows-PC (trykk Win + I).
  - Klikk Personvern og sikkerhet i venstre sidefelt, og klikk deretter Windows Security.
  - Klikk App- og nettleserkontroll.
  - Under Smart appkontroll, klikk Smart App Control-innstillinger.
  - Sett bryteren til Av for å la Updater CE starte.

Blokkert av Edge? Hvis Microsoft Edge blokkerer selve nedlastingen, klikker du på knappen Flere alternativer (…) → Behold → Vis mer → Behold uansett.

Aktiverer Smart App Control på nytt senere: Når du vil slå på Smart App Control igjen, kan du aktivere den på nytt via Windows-registeret under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` ved innstilling `VerifiedAndReputablePolicyState` til `1` (På) eller `2` (Evalueringsmodus) og omstart.Nær hjelp

## Var dette nyttig?

Svaret ditt bidrar til å forbedre denne veiledningen.Ja, jeg fant det nyttigIkke ennå[Fortell oss hvordan vi kan forbedre oss](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
