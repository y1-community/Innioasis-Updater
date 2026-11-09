---
title: "Innioasis Y2 Scrollwiel werkt niet na update | Innioasis Firmware-archief - Innioasis Firmware-downloads"
description: "Innioasis Y2 scrollwiel of klikwiel werkt niet na een update? Installeer Y2 originele software opnieuw, controleer de ring en scheid firmware van hardwarefouten."
language: "nl"
source: "https://innioasis.app/guides/y2-scroll-wheel-not-working_nl.html"
---

# Innioasis Y2 Scrollwiel werkt niet na update | Innioasis Firmware-archief - Innioasis Firmware-downloads

Spelerherstel · Innioasis Y2

# Innioasis Y2 scrollwiel werkt niet na een update

Het wiel draait maar de speler negeert het, of het klikwiel stopt direct na een flits. Hier leest u hoe u een firmwarefout kunt onderscheiden van een hardwarefout op Y2.[Updater CE downloaden](../guide_nl.html#platform)[Y2 softwaredownloads](../firmware_nl.html?model=Y2&software=original-y2)[Herstelgids](recovery_nl.html)

## Zoek uit of het stuur of de firmware de oorzaak is

Op een Y2 is het wiel een fysieke ingang, maar de firmware bepaalt wat elke draai en klik doet. Een wiel dat stopte zodra je een update uitvoerde of flitste, wijst op software. Een wiel dat elke software negeert (voorraad, Rockbox of een herstelscherm) wijst naar het onderdeel.
  - Werkt in de ene software, dood in de andere: firmwarefout.
  - Dood op elk scherm, inclusief herstel: wiel, lint of bord.
  - Slechts één richting mist: meestal vuil onder de ring of slijtage.
  - Wiel draait maar niets benadrukt: de speler is mogelijk bevroren. Forceer eerst een herstart.

## Snelle controles voordat u de firmware opnieuw installeert
  - Houd de aan/uit-knop ongeveer 15 seconden ingedrukt om de speler uit te schakelen en start hem vervolgens normaal op.
  - Test het stuur op het startscherm, in Instellingen en in de muziekspeler.
  - Druk op de fysieke knoppen. Als de voeding en de achterkant reageren, maar het wiel niet, ligt de fout bij het wiel zelf.
  - Laad de speler gedurende 30 minuten op met een bekende datakabel.
  - If you installed Rockbox for Y2 or another custom build, return to Original Software and test again.

## Installeer de Y2-firmware die bij uw speler past opnieuw

Het stuur wordt aangestuurd door de firmware, dus een update-gerelateerde fout wordt verholpen door de juiste Y2 originele software terug op de speler te plaatsen. Gebruik nooit een Y1-pakket op een Y2, en kies geen release die "dicht genoeg" is - Y2-pakketten zijn gebouwd voor Y2-hardware.
  - Openen [Updater CE](../guide_nl.html#platform) op uw computer.
  - Instellen Apparaatmodel aan Y2.
  - Kies Originele software binnen Software en kies een stabiele Y2-release – het handmatige pakket is dat `rom_y2.zip`.
  - Klik Installeren / Herstellen en laat het pakket uitpakken.
  - Schakel de Y2 volledig uit, sluit de USB datakabel alleen aan als Updater daarom vraagt, en wacht totdat de succesmelding verschijnt.
Match het model en de uitvoering. Als de releaselijst eruitziet als Y1-software, stop dan en selecteer opnieuw Y2. De volledige stappen staan ​​in de [Y2-herstelgids](restore-original-y2_nl.html).

## Controleer de wielring op vuil of schade

Als het wiel stijf is, blijft hangen of slechts in één richting faalt, kunnen zakpluisjes en gruis tussen de ring en de behuizing blijven zitten. Schakel de speler uit en veeg de ring schoon met een droge microvezeldoek. Druppel geen schoonmaakmiddelen of alcohol in de opening en wrik de ring niet omhoog.

Als de ring los zit, gebarsten is of niet meer klikt, heeft de speler service nodig. Firmware kan een beschadigd wiel, een losgekoppeld lint of vloeistofschade niet repareren.

## Als de speler ook niet wil starten

Door een mislukte update kan de Y2 niet meer opstarten, wat lijkt op een wielstoring omdat er geen invoer reageert. Werk door de [Y2 kan de gids niet inschakelen](y2-wont-turn-on_nl.html) voor opladen, geforceerde herstart en handmatig herstel.

## Innioasis Y2 Veelgestelde vragen over het scrollwiel

### Waarom werkte mijn Innioasis Y2 scrollwiel niet meer na een update?

Door een update kan de bestuurder uit de pas lopen met de rest van de firmware, vooral als de flitser werd onderbroken of een Y1-pakket werd gebruikt. Installeer de Y2 originele softwareversie voor uw model opnieuw en test het stuur op het standaard startscherm.

### Hoe weet ik of het Y2 klikwiel kapot is of dat de firmware defect is?

Test het stuur in meer dan één software. Als het werkt in standaardsoftware, maar niet in Rockbox, is er sprake van een probleem met de firmware-toewijzing. Als het op geen enkel scherm doet, inclusief een herstelmenu, vermoed dan het wiel, het lint of het bord.

### Zal het herstellen van de originele software het scrollwiel Y2 oplossen?

Het repareert fouten die worden veroorzaakt door een update of een niet-overeenkomend pakket, en het is het eerste dat u moet proberen. Het repareert geen fysiek beschadigd wiel, een los lint of vloeistofschade.

### Kan ik een Y1 firmwarepakket gebruiken om een ​​Y2 wielprobleem op te lossen?

Nee. Y1 en Y2 pakketten zijn niet uitwisselbaar, en het flashen van het verkeerde model kan de besturing verslechteren. Zorg ervoor dat het model en de release overeenkomen voordat u Installeren/Herstellen uitvoert.

## Gerelateerde oplossingen
  - [Y1 scrollwiel werkt niet](y1-scroll-wheel-not-working_nl.html) — dezelfde controles voor de Y1
  - [Y2 gaat niet aan](y2-wont-turn-on_nl.html) — stroom- en opstartherstel
  - [Innioasis herstelgids](recovery_nl.html) — alle symptoomgidsen op één plek
  - [Problemen met een installatie oplossen](../troubleshooting_nl.html) – hoe een mislukte flitser eruit ziet
  - [Herstel Y2 Originele software](restore-original-y2_nl.html) — de volledige herstelprocedure

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
