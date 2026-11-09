---
title: "SP Flash Tool för Innioasis och Timmkoo spelare"
description: "Hitta SP Flash Tool medföljande Innioasis Updater på Windows och Linux, extrahera rom.zip eller rom_y2.zip, och flasha en Innioasis Y1 eller Y2 med den matchande scatter-filen."
language: "sv"
source: "https://innioasis.app/sp-flash-tool_sv.html"
---

# SP Flash Tool för Innioasis och Timmkoo spelare

Manuell blinkning

# Flash-verktyg för Innioasis och Timmkoo spelare

SP Flash Tool kommer inuti Innioasis Updater på [Windows](drivers_sv.html#windows) och [Linux](drivers_sv.html#linux). Du har det redan. Den här guiden visar det säkra sättet att använda det på en Innioasis Y1 eller Y2, och Updater-rutten för Timmkoo spelare.[Återgå till Updater-guiden](guide_sv.html)[Firmware-nedladdningar](firmware_sv.html)[Felsökning](troubleshooting_sv.html)

Börja med Innioasis Updater

## Updater gör hela jobbet i ett pass

Updater gör de flesta installationer i ett pass. Välj programvaran, följ stegen och du är klar. Den talar också om när en fix eller en ny release landar. SP Flash Tool finns i Updaters Toolkit för de sällsynta fallen Updater inte kan slutföra. Stegen nedan är undantaget.

## Vad det här verktyget är till för

Updater blinkar spelaren åt dig. SP Flash Tool är samma motor, utan skyddsräcken. Använd den när Updater inte startar, när spelaren inte ansluter eller när du känner dig runt en scatter-fil.Prova Updater först. För de flesta installationer och de flesta återställningar, den guidade [Uppdateringsrutt](guide_sv.html) är det säkrare valet. Använd SP Flash Tool när du vet varför du behöver det, och ha ett laddat batteri plus en USB datakabel redo.

## Flashverktyg för Innioasis spelare

Innioasis Updater är flashverktyget för Innioasis spelare. Den installerar officiell programvara, uppdateringar och återställer paket genom det modellmatchade flödet, och det behåller din musik och inställningar.

### Innioasis Y1 blixtverktyg

Välj Y1-versionen i Updater och anslut sedan den avstängda spelaren när appen frågar. Samma Y1-paket fungerar med SP Flash Tool när du behöver den manuella rutten.

### Innioasis Y2 blixtverktyg

Välj en version listad för Y2. Y2-paket är inte utbytbara med Y1-paket, så kontrollera modellen innan du börjar.

## Flashverktyg för Timmkoo spelare

Timmkoo spelare använder samma installationsflöde för Updater. Den läser Timmkoos ZIP- och RAR-paket direkt, så du behöver inte ett separat flashverktyg eller scatter-fil.

### Timmkoo Q5 blixtverktyg

Välj Q5-modellen i Updater, välj Timmkoo-paketet, kör sedan Install/Restore och anslut spelaren vid prompten.

### Timmkoo Q3 och Q3E blixtverktyg

Q3-posten täcker likadana Q3 och Q3E. Updater väljer de matchande filerna från paketet som projektet publicerar.

### Timmkoo A5 blixtverktyg

Välj A5-modellen innan du väljer ett paket och följ sedan samma installationsprompt.

## Där Updater uttrycker det

SP Flash Tool levereras med Updater-installationsmappen, inte som en separat nedladdning. Öppna den därifrån när du behöver den.

### Windows

Öppna installationsmappen för Updater och kör `flash_tool.exe`. Mappen ligger vanligtvis under `%LOCALAPPDATA%\Innioasis Updater`. En Toolkit-mapp med en SP Flash Tool-genväg ingår i vissa inställningar.

### Linux

Kör den medföljande `flash_tool` binär i Updater-appmappen på x86 / x86_64. Projektinstallationsprogrammet förbereder USB behörigheter med udev-regler, så spelaren bör visas när den är ansluten.

### macOS

SP Flash Tool är inte paketerat på macOS. Updater använder rutten MTKClient dit istället. Använd [guidad installation](guide_sv.html) på en Mac och behåll SP Flash Tool för en Windows- eller Linux-maskin.

Verktyget levereras med MediaTek nedladdningsagent och modellspecifik konfiguration, så du behöver inte samla in DA eller sprida filer från någon annanstans.

## Förbered firmware
  - Ta den version du vill ha från [Firmware-nedladdningar](firmware_sv.html). Välj `rom.zip` för en Y1 eller `rom_y2.zip` för en Y2.
  - Extrahera ZIP till sin egen mapp. Windows kan använda Extrahera alla. På Linux, använd din arkivhanterare eller `unzip` i en terminal.
  - Kontrollera att scatter-filen finns i den extraherade mappen. Det brukar kallas `MT6572_Android_scatter.txt` för Y1 paket och `MT6582_Android_scatter_def.txt` för Y2-paket, även om en utgåva kan döpa den efter sitt projekt.
Håll modellerna åtskilda. Y1-spridningen beskriver en MT6572-enhet och Y2-spridningen beskriver en MT6582-enhet. Att blinka med fel är hur spelare blir murade. Om spridningen inuti ZIP inte stämmer överens med din modell, sluta och använd ett paket som är listat för din modell istället.

## Ladda scatter och blixt
  - Öppna SP Flash Tool från Updater-installationsmappen.
  - Klicka på på fliken Ladda ner Välj bredvid Scatter-loading File och välj scatter-filen från den extraherade mappen. Partitionslistan kommer att fyllas i.
  - Lämna blixtläget på Endast nedladdning såvida du inte medvetet gör en fullständig återhämtning, vilket behöver Firmware uppgradering.
  - Klicka Ladda ner. Verktyget väntar på spelaren.
  - Stäng av spelaren helt och anslut sedan datakabeln USB. Lägg ner spelaren och flytta den inte.
  - Vänta på den gröna bocken. Först då koppla ur kabeln och starta spelaren.

Behåll samma USB kabel- och tidsregler som den guidade rutten: en datakabel, ingen hubb och anslut bara när verktyget är klart.

## Om den inte blinkar
  - Kontrollera att scatter och ZIP matchar modellen som är tryckt på spelaren.
  - Kontrollera att spelaren är helt avstängd innan du ansluter.
  - I Windows, bekräfta MediaTek-drivrutinen installerad med Updater-installationen; på Linux, bekräfta udev-reglerna från projektinstallationsprogrammet.
  - Återanslut endast kabeln när verktyget väntar. Ett hamnlopp kan behöva en fullständig urkoppling och en fräsch Ladda ner klicka.

För allt utöver det, öppna [felsökning](troubleshooting_sv.html). Och kom ihåg: Updater är fortfarande den normala vägen, och [Y1](guides/restore-original-y1.html) och [Y2](guides/restore-original-y2.html) återställningsguider använder det också.

## Var detta användbart?

Ditt svar hjälper till att förbättra den här guiden.Ja, jag tyckte det var användbartInte än[Låt oss veta hur vi kan förbättra](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
