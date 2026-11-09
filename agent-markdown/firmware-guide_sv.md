---
title: "Guide för installation av firmware och lageråterställning | Innioasis Updater CE - Innioasis Firmware-nedladdningar"
description: "Installera anpassad firmware eller återställ officiell fabriksfast programvara på Innioasis Y1, Y2, G1, G3, G5, R1, PR1 och Timmkoo Q5, Q3 med Innioasis Updater CE."
language: "sv"
source: "https://innioasis.app/firmware-guide_sv.html"
---

# Guide för installation av firmware och lageråterställning | Innioasis Updater CE - Innioasis Firmware-nedladdningar

Guide för installation av firmware och lageråterställning

# Installera eller återställa firmware på din enhet

Välj den modell som är tryckt på din spelare. Följ sedan stegen i Updater CE. Den sköter resten.[Hämta Updater CE](guide_sv.html#platform)[Bläddra i firmware-arkiv](firmware_sv.html)[Felsökning](troubleshooting_sv.html)

Välj den modell som är tryckt på din spelare och den programvara du vill ha och öppna sedan den här guiden. [Bläddra bland programvara och lagerfirmware efter modell](firmware_sv.html).

## 

[Hämta Updater CE](guide_sv.html#download-updater)[Fullständig skriftlig handledning](guide_sv.html)

## Skaffa Innioasis Updater CE

Här är var du ska börja om du inte redan har Updater CE.Skaffa den på Updater CEmed guidad installation

### Windows

Ladda ner installationsprogrammet, öppna det och följ installationsanvisningarna.[Ladda ner och installera drivrutinen](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Ladda ner app och drivrutiner](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Blockerad av Edge?](#)

Om Windows stoppar dig från att köra appen eller inte startar den, öppna Inställningar, klicka på Sekretess och säkerhet → Windows Säkerhet → App- och webbläsarkontroll och stäng av Smart App Control. [Windows startar inte appen? Hjälp](#smart-app-control)

Du måste starta om datorn efter installationen för att den ska fungera.

### macOS

Ladda ner appen och flytta den till Applikationer. Om macOS blockerar det, öppna Systeminställningar, sedan Sekretess och säkerhet och klicka på Öppna ändå. [Hur det här fungerar](https://support.apple.com/en-gb/102445#openanyway)[Ladda ner Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Ladda ner AppImage för Intel- och AMD-system, gör den körbar och kör den.[Ladda ner AppImage för Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Anteckningar om Linux-installation](drivers_sv.html#linux)En annan plattform?

Behöver du de längre anteckningarna om datorinstallation? Öppna [Windows](drivers_sv.html#windows) eller [Linux](drivers_sv.html#linux) inställningsguide.

## Går tillbaka till originalprogramvaran

För att gå tillbaka, välj din modell, välj Originalprogramvara, spring sedan Installera / Återställ. Det är allt. Updater ersätter systemprogramvaran åt dig.[Y1 återställningsguide](guides/restore-original-y1.html)[Y2 återställningsguide](guides/restore-original-y2.html)

## Programvaruguider efter modell

Välj din modell och öppna sedan guiden för din programvara.

### Innioasis Y1

Programvara för Y1:

### Innioasis Y2

Programvara för Y2:

En anteckning om de två verktygen

## Vilket verktyg ska jag använda?

Innioasis Uppdaterare CE är det säkraste sättet att uppdatera din spelare. Den behåller din musik, videor och Bluetooth-parningar. Den talar om när uppdateringar är klara. Den körs på Windows, macOS och Linux. Innioasis Universal Flash Tool torkar din spelare och fungerar på färre datorer.[Öppna hela jämförelsen](updater-comparison_sv.html)

### Windows startar inte appen? Hur man stänger av Smart App Control

Windows Defender SmartScreen eller Smart App Control kan blockera nyladdade community-applikationer innan signaturrykte sprids. Smart App Control påverkar för närvarande populära applikationer som Epic Overlay Service (används av Fortnite) — Updater CE är säker och verifierad att använda. Genom att stänga av Smart App Control kan Updater CE öppnas och köras normalt.
  - Öppna Inställningar på din Windows-dator (tryck på Win + I).
  - Klicka Sekretess & säkerhet i det vänstra sidofältet och klicka sedan Windows Security.
  - Klicka App- och webbläsarkontroll.
  - Under Smart appkontroll, klicka Smart App Control-inställningar.
  - Ställ omkopplaren på Av för att tillåta Updater CE att starta.

Blockerad av Edge? Om Microsoft Edge blockerar själva nedladdningen, klicka på knappen Fler alternativ (…) → Behåll → Visa mer → Behåll ändå.

Återaktivera Smart App Control senare: När du vill aktivera Smart App Control igen kan du återaktivera den via Windows-registret under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` genom att ställa in `VerifiedAndReputablePolicyState` till `1` (På) eller `2` (Utvärderingsläge) och omstart.Nära hjälp

## Var detta användbart?

Ditt svar hjälper till att förbättra den här guiden.Ja, jag tyckte det var användbartInte än[Låt oss veta hur vi kan förbättra](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
