---
title: "Innioasis Y1 en Y2 Herstelhandleiding | Innioasis Firmware-archief - Innioasis Firmware-downloads"
description: "Herstelgids voor Innioasis Y1 en Y2 spelers die niet kunnen worden ingeschakeld of een scrollwiel hebben dat niet meer werkt na een update. Reset- en firmwarestappen."
language: "nl"
source: "https://innioasis.app/guides/recovery_nl.html"
---

# Innioasis Y1 en Y2 Herstelhandleiding | Innioasis Firmware-archief - Innioasis Firmware-downloads

Spelerherstel · Y1 en Y2

# Innioasis Y1 en Y2 herstelgids

Kan niet worden ingeschakeld, het stuur werkt niet of een installatie die halverwege is gestopt. Begin met het symptoom en volg vervolgens de stappen in de juiste volgorde, in plaats van direct over te gaan tot een handmatige flitser.[Updater CE downloaden](../guide_nl.html#platform)[Firmware-downloads](../firmware_nl.html)[Probleemoplossing](../troubleshooting_nl.html)

Begin met Innioasis Updater

## De begeleide installatie lost de meeste hiervan op

Updater doet het in één keer. Kies de software, volg de stappen op het scherm en je bent klaar. Het vertelt je ook wanneer er een oplossing of een nieuwe release beschikbaar is.

## Begin met het symptoom

Deze handleidingen behandelen de twee mislukkingen die mensen het vaakst tegenkomen na een update of een flash. Kies degene die overeenkomt met wat u ziet en werk deze vervolgens in de juiste volgorde door.

### Scrollwiel werkt niet

Het wiel draait maar de speler negeert het, of het stopte direct na een update.

[Y1 scrollwielgeleider](y1-scroll-wheel-not-working_nl.html) · [Y2 scrollwielgeleider](y2-scroll-wheel-not-working_nl.html)

### Speler gaat niet aan

Een zwart scherm, geen oplaadlampje of een logo dat verschijnt en verdwijnt.

[Y1 vermogensgids](y1-wont-turn-on_nl.html) · [Y2 vermogensgids](y2-wont-turn-on_nl.html)

### Installatie halverwege gestopt

Updater is mislukt vóór of na de USB-prompt, of de releaselijst ziet er verkeerd uit.

[Gids voor probleemoplossing](../troubleshooting_nl.html)

### Ik heb de bestanden nodig

Originele software en aangepaste pakketten voor elk model.

[Firmware-downloads](../firmware_nl.html)

## Y1 en Y2 pakketten zijn niet uitwisselbaarCrossflash nooit met een model. Een Y1 `rom.zip` is geen Y2-pakket en een Y2 `rom_y2.zip` werkt niet op een Y1. Het flashen van het verkeerde model is een van de meest voorkomende redenen waarom een ​​speler dode besturingselementen of een opstartlus krijgt.

Controleer het model dat op de speler is afgedrukt en vergelijk het vervolgens in Updater CE voordat u een release kiest.

## Herstel eerst de overeenkomende originele software

Voordat u met handmatig gereedschap begint, plaatst u de standaardfirmware voor het juiste model terug op de speler. Hiermee worden de meeste update-gerelateerde wiel- en opstartfouten opgelost.

Y1: selecteer Y1, kies Originele software, kies een stabiele Y1-release en voer vervolgens Installeren/Herstellen uit. [Volledige Y1 herstelgids](restore-original-y1_nl.html).

Y2: selecteer Y2, kies Originele software, kies een stabiele Y2-release en voer vervolgens Installeren/Herstellen uit. [Volledige Y2 herstelgids](restore-original-y2_nl.html).

Schakel de speler alleen uit en sluit de USB-datakabel aan als Updater daarom vraagt. Laat hem aangesloten totdat het succesbericht verschijnt.

## Handmatig herstel dat wordt meegeleverd met Updater CE

Wanneer Updater de taak niet kan voltooien, bevat dezelfde installatie de handmatige hulpmiddelen. [SP Flash Tool](../sp-flash-tool_nl.html) is gebundeld op Windows- en Linux x86-machines, en de MTKClient-route omvat macOS. Beide hebben een firmwarepakket nodig dat overeenkomt met het model, beschikbaar op de [Firmware-downloads](../firmware_nl.html) pagina.

Gebruik de gids voor uw platform en houd de speler opgeladen. Als helemaal geen tool de speler detecteert, is de fout waarschijnlijk hardwarematig en niet firmware.

## Wat u moet vermelden als u om hulp vraagt
  - Het model — Y1 of Y2 — afgedrukt op de speler.
  - Wat het scherm doet: niets, een logo, een opstartlus of het startscherm.
  - Of een computer de speler detecteert als een MediaTek-apparaat.
  - Het exacte Updater-bericht en het pakket dat u hebt geselecteerd.
  - Wat je al hebt geprobeerd, inclusief eventuele handmatige tools.

Plaats geen privétokens of niet-gerelateerde systeembestanden. De [gemeenschap Discord](https://discord.gg/zHrT2zrcek) en [r/innioasis](https://reddit.com/r/innioasis) zijn de snelste plaatsen om notities te vergelijken.

## Innioasis veelgestelde vragen over herstel

### Hoe repareer ik een Innioasis-speler die niet aangaat?

Laad hem 30 minuten op met een bekende datakabel, forceer een herstart door de stroom 15 seconden ingedrukt te houden en controleer vervolgens of een computer hem detecteert. Als dit het geval is, herstel dan de originele software die overeenkomt met het model; Als dit niet het geval is, gebruikt u de handmatige herstelhulpmiddelen die bij Updater CE zijn geleverd.

### Waarom werkt mijn Y1 of Y2 scrollwiel niet?

Als het stuur na een update stopt, is er meestal sprake van een firmware-mismatch. Installeer de originele software die overeenkomt met het model en test opnieuw. Als het stuur in elke firmware dood is, behandel het dan als een hardwarefout.

### Waar kan ik firmware downloaden voor herstel?

De Firmware Downloads-pagina op innioasis.app/firmware.html host originele en aangepaste pakketten voor elk model. Kies altijd het Y1- of Y2-pakket dat bij de speler past.

### Welke hersteltools worden meegeleverd met Updater CE?

Updater CE bevat SP Flash Tool op Windows en Linux, en de route MTKClient inclusief macOS, voor handmatig herstel wanneer de normale installatie niet kan worden voltooid.

## Gerelateerde oplossingen
  - [Y1 scrollwiel werkt niet](y1-scroll-wheel-not-working_nl.html) — klikwiel reageert niet meer na een update
  - [Y2-scrollwiel werkt niet](y2-scroll-wheel-not-working_nl.html) — dezelfde controles voor de Y2
  - [Y1 gaat niet aan](y1-wont-turn-on_nl.html) — opladen, opnieuw opstarten en handmatig herstel
  - [Y2 gaat niet aan](y2-wont-turn-on_nl.html) — dezelfde controles voor de Y2
  - [SP Flash Tool gids](../sp-flash-tool_nl.html) — handmatig knipperen op Windows en Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
