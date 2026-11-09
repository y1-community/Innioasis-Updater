---
title: "SP Flash Tool voor Innioasis en Timmkoo spelers"
description: "Zoek SP Flash Tool gebundeld met Innioasis Updater op Windows en Linux, pak rom.zip of rom_y2.zip uit en flash een Innioasis Y1 of Y2 met het overeenkomende scatterbestand."
language: "nl"
source: "https://innioasis.app/sp-flash-tool_nl.html"
---

# SP Flash Tool voor Innioasis en Timmkoo spelers

Handmatig knipperen

# Flash Tool voor Innioasis en Timmkoo spelers

SP Flash Tool komt binnen Innioasis Updater aan [Windows](drivers_nl.html#windows) en [Linux](drivers_nl.html#linux). Je hebt het al. Deze gids toont de veilige manier om het te gebruiken op een Innioasis Y1 of Y2, en de Updater-route voor Timmkoo-spelers.[Keer terug naar de Updater-handleiding](guide_nl.html)[Firmware-downloads](firmware_nl.html)[Probleemoplossing](troubleshooting_nl.html)

Begin met Innioasis Updater

## Updater doet het hele werk in één keer

Updater voert de meeste installaties in één keer uit. Kies de software, volg de stappen en je bent klaar. Het vertelt je ook wanneer er een oplossing of een nieuwe release beschikbaar is. SP Flash Tool bevindt zich in Updater's Toolkit voor de zeldzame gevallen dat Updater niet kan voltooien. De onderstaande stappen vormen een uitzondering.

## Waar dit hulpmiddel voor is

Updater flasht de speler voor u. SP Flash Tool is dezelfde motor, zonder de vangrails. Gebruik het wanneer Updater niet start, wanneer de speler geen verbinding wil maken of wanneer u de weg weet in een verspreidingsbestand.Probeer eerst Updater. Voor de meeste installaties en de meeste herstelbewerkingen wordt het begeleid [Updater-route](guide_nl.html) is de veiligere keuze. Gebruik SP Flash Tool als je weet waarom je het nodig hebt, en houd een opgeladen batterij en een USB datakabel bij de hand.

## Flash-tool voor Innioasis spelers

Innioasis Updater is de flashtool voor Innioasis-spelers. Het installeert officiële software, updates en herstelpakketten via de op het model afgestemde stroom, en het behoudt uw muziek en instellingen.

### Innioasis Y1 Flash-tool

Kies de release Y1 in Updater en sluit vervolgens de uitgeschakelde speler aan wanneer de app daarom vraagt. Dezelfde Y1-pakketten werken met SP Flash Tool wanneer u de handmatige route nodig heeft.

### Innioasis Y2 Flash-tool

Kies een release vermeld voor Y2. Y2-pakketten zijn niet uitwisselbaar met Y1-pakketten, dus controleer het model voordat u begint.

## Flash-tool voor Timmkoo spelers

Timmkoo spelers gebruiken hetzelfde Updater-installatieproces. Het leest de ZIP- en RAR-pakketten van Timmkoo rechtstreeks, dus je hebt geen aparte flashtool of scatterbestand nodig.

### Timmkoo Q5 Flash-tool

Selecteer het Q5-model in Updater, kies het Timmkoo-pakket, voer Install/Restore uit en sluit de speler aan wanneer daarom wordt gevraagd.

### Timmkoo Q3 en Q3E flashtool

De vermelding Q3 heeft betrekking op zowel Q3 als Q3E. Updater kiest de overeenkomende bestanden uit het pakket dat het project publiceert.

### Timmkoo A5 Flash-tool

Selecteer het A5-model voordat u een pakket kiest en volg dezelfde installatieprompt.

## Waar Updater het plaatst

SP Flash Tool wordt geleverd met de Updater-installatiemap, niet als afzonderlijke download. Open het vanaf daar wanneer je het nodig hebt.

### Windows

Open de Updater-installatiemap en voer deze uit `flash_tool.exe`. De map staat meestal onder `%LOCALAPPDATA%\Innioasis Updater`. Bij sommige instellingen is een Toolkit-map met een snelkoppeling SP Flash Tool inbegrepen.

### Linux

Voer de gebundelde uit `flash_tool` binair in de map Updater-app op x86 / x86_64. Het projectinstallatieprogramma bereidt USB-rechten voor met udev-regels, zodat de speler moet verschijnen wanneer deze is verbonden.

### macOS

SP Flash Tool is niet gebundeld op macOS. Updater gebruikt daar in plaats daarvan de route MTKClient. Gebruik de [begeleide installatie](guide_nl.html) op een Mac en behoud SP Flash Tool voor een Windows- of Linux-machine.

De tool wordt geleverd met de MediaTek downloadagent en modelspecifieke configuratie, zodat u geen DA hoeft te verzamelen of bestanden van elders hoeft te verspreiden.

## Bereid de firmware voor
  - Pak de gewenste release [Firmware-downloads](firmware_nl.html). Kiezen `rom.zip` voor een Y1 of `rom_y2.zip` voor een Y2.
  - Pak de ZIP uit in een eigen map. Windows kan Alles uitpakken gebruiken. Gebruik op Linux uw archiefbeheerder of `unzip` in een terminal.
  - Controleer of het verspreidingsbestand zich in de uitgepakte map bevindt. Meestal wordt het genoemd `MT6572_Android_scatter.txt` voor Y1 pakketten en `MT6582_Android_scatter_def.txt` voor Y2-pakketten, hoewel een release dit naar zijn project kan noemen.
Houd de modellen gescheiden. De spreiding Y1 beschrijft een MT6572-apparaat en de spreiding Y2 beschrijft een MT6582-apparaat. Door met de verkeerde te knipperen, worden spelers gemetseld. Als de spreiding in de ZIP niet overeenkomt met uw model, stop dan en gebruik in plaats daarvan een pakket dat voor uw model vermeld staat.

## Laad de scatter en flits
  - Open SP Flash Tool vanuit de Updater-installatiemap.
  - Klik op het tabblad Downloaden Kies naast Scatter-loading File en selecteer het scatterbestand uit de uitgepakte map. De partitielijst wordt ingevuld.
  - Laat de flitsmodus ingeschakeld Alleen downloaden tenzij u opzettelijk een volledig herstel uitvoert, wat nodig is Firmware-upgrade.
  - Klik Downloaden. De tool wacht op de speler.
  - Schakel de speler volledig uit en sluit vervolgens de USB-datakabel aan. Zet de speler neer en verplaats hem niet.
  - Wacht op het groene vinkje. Koppel dan pas de kabel los en start de speler.

Houd u aan dezelfde USB-kabel- en timingregels als bij de begeleide route: een datakabel, geen hub, en sluit alleen aan als het gereedschap gereed is.

## Als het niet knippert
  - Controleer of de scatter en ZIP overeenkomen met het model dat op de speler is afgedrukt.
  - Controleer of de speler volledig is uitgeschakeld voordat u verbinding maakt.
  - Bevestig in Windows dat het MediaTek-stuurprogramma is geïnstalleerd met de Updater-installatie; bevestig op Linux de udev-regels van het projectinstallatieprogramma.
  - Sluit de kabel pas opnieuw aan als het gereedschap wacht. Voor een havenrace kan een volledige ontkoppeling en een nieuwe nodig zijn Downloaden klik.

Voor alles daarbuiten, open [probleemoplossing](troubleshooting_nl.html). En onthoud: Updater is nog steeds de normale route, en [Y1](guides/restore-original-y1.html) en [Y2](guides/restore-original-y2.html) herstelhandleidingen gebruiken het ook.

## Was dit nuttig?

Uw antwoord helpt deze handleiding te verbeteren.Ja, ik vond het nuttigNog niet[Laat ons weten hoe we kunnen verbeteren](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
