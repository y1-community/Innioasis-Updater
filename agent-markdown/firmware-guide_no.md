---
title: "Fastvareinstallasjon og lagergjenopprettingsveiledning | Innioasis Updater CE - Innioasis Fastvarenedlastinger"
description: "Installer tilpasset fastvare eller gjenopprett offisiell fabrikkfastvare på Innioasis Y1, Y2, G1, G3, G5, R1, PR1 og Timmkoo Q5, Q3 med Innioasis Updater CE."
language: "no"
source: "https://innioasis.app/firmware-guide_no.html"
---

# Fastvareinstallasjon og lagergjenopprettingsveiledning | Innioasis Updater CE - Innioasis Fastvarenedlastinger

Veiledning for fastvareinstallasjon og lagergjenoppretting

# Installer eller gjenopprett fastvare på enheten

Velg modellen som er trykt på spilleren din. Følg deretter trinnene i Updater CE. Den klarer resten.[Få Updater CE](guide_no.html#platform)[Bla gjennom fastvarearkivet](firmware_no.html)[Feilsøking](troubleshooting_no.html)

Velg modellen som er trykt på spilleren og programvaren du ønsker, og åpne deretter denne veiledningen. [Bla gjennom programvare og lagerfastvare etter modell](firmware_no.html).

## 

[Få Updater CE](guide_no.html#download-updater)[Full skriftlig opplæring](guide_no.html)

## Få Innioasis Updater CE

Her er hvor du skal begynne hvis du ikke allerede har Updater CE.Få den på Updater CEmed veiledet installasjon

### Windows

Last ned installasjonsprogrammet, åpne det og følg oppsettinstruksjonene.[Last ned og installer driveren](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Last ned app og drivere](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Blokkert av Edge?](#)

Hvis Windows stopper deg fra å kjøre appen eller ikke starter den, åpner du Innstillinger, klikker på Personvern og sikkerhet → Windows Sikkerhet → App- og nettleserkontroll, og slår av Smart App Control. [Vil ikke Windows starte appen? Hjelp](#smart-app-control)

Du må starte PC-en på nytt etter installasjonen for å få den til å fungere.

### macOS

Last ned appen og flytt den til Applikasjoner. Hvis macOS blokkerer det, åpner du Systeminnstillinger, deretter Personvern og sikkerhet, og klikker Åpne likevel. [Hvordan dette fungerer](https://support.apple.com/en-gb/102445#openanyway)[Last ned Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Last ned AppImage for Intel- og AMD-systemer, gjør det kjørbart og kjør det.[Last ned AppImage for Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Notater om Linux-oppsett](drivers_no.html#linux)En annen plattform?

Trenger du de lengre notatene om datamaskinoppsett? Åpne [Windows](drivers_no.html#windows) eller [Linux](drivers_no.html#linux) oppsettsveiledning.

## Går tilbake til original programvare

For å gå tilbake, velg din modell, velg Original programvare, så løp Installer / Gjenopprett. Det er alt. Updater erstatter systemprogramvaren for deg.[Y1 gjenopprettingsveiledning](guides/restore-original-y1.html)[Y2 gjenopprettingsveiledning](guides/restore-original-y2.html)

## Programvareguider etter modell

Velg din modell, og åpne deretter veiledningen for programvaren din.

### Innioasis Y1

Programvare for Y1:

### Innioasis Y2

Programvare for Y2:

En merknad om de to verktøyene

## Hvilket verktøy bør jeg bruke?

Innioasis Oppdaterer CE er den sikreste måten å oppdatere spilleren på. Den beholder musikken, videoene og Bluetooth-sammenkoblingene dine. Den forteller deg når oppdateringer er klare. Den kjører på Windows, macOS og Linux. Innioasis Universal Flash Tool tørker av spilleren din og fungerer på færre datamaskiner.[Åpne hele sammenligningen](updater-comparison_no.html)

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
