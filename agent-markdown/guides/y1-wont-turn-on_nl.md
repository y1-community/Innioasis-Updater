---
title: "Innioasis Y1 Kan niet worden ingeschakeld | Innioasis Firmware-archief - Innioasis Firmware-downloads"
description: "Innioasis Y1 gaat niet aan of laadt niet op? Forceer een herstart, controleer of een computer dit ziet en herstel vervolgens de Y1 firmware of gebruik handmatig SP Flash Tool herstel."
language: "nl"
source: "https://innioasis.app/guides/y1-wont-turn-on_nl.html"
---

# Innioasis Y1 Kan niet worden ingeschakeld | Innioasis Firmware-archief - Innioasis Firmware-downloads

Spelerherstel · Innioasis Y1

# Innioasis Y1 gaat niet aan

Een zwart scherm betekent niet altijd een dode speler. Werk door het opladen, een gedwongen herstart en detectie op een computer voordat u handmatig flitst.[Updater CE downloaden](../guide_nl.html#platform)[Firmware-downloads](../firmware_nl.html)[Herstelgids](recovery_nl.html)

## Laad eerst de Y1 goed op

De meeste "Y1 gaat niet aan"-meldingen hebben betrekking op een lege batterij, een kabel die alleen kan worden opgeladen of een oplader die niet voldoende stroom kan leveren. Het kan 20 tot 30 minuten duren voordat een diep uitgeputte Y1 aan staat voordat het scherm iets weergeeft, dus wacht even voordat je hem dood noemt.
  - Gebruik een bekende USB gegevens kabel, geen kabel die alleen kan worden opgeladen.
  - Probeer een wandlader en vervolgens rechtstreeks een computer USB-poort - geen hub.
  - Laat hem 30 tot 60 minuten aangesloten en let op een oplaadpictogram of achtergrondverlichting.
  - Probeer een tweede kabel en oplader voordat u verder gaat.

## Forceer een herstart

Houd de aan/uit-knop ongeveer 15 seconden ingedrukt, laat hem los, wacht vijf seconden en druk vervolgens één keer op de aan/uit-knop. Hiermee wordt een vastgelopen laars gewist en kan deze veilig worden herhaald.

Als het scherm het logo toont en vervolgens zwart wordt, start de speler op en mislukt deze. Ga verder naar het firmwareherstel hieronder. Als er helemaal niets gebeurt, laat hem dan opladen en probeer het na een half uur opnieuw.

## Controleer of een computer de speler kan zien

Sluit de uitgeschakelde Y1 aan met een datakabel en open Apparaatbeheer op Windows, `lsusb` op Linux, of MTKClient op macOS. Een werkende speler verschijnt als een MediaTek-apparaat met leveranciers-ID `0e8d`. Als dit verschijnt, is de hardware levend genoeg om te reflashen, zelfs als het scherm donker blijft.

Als er niets verschijnt, installeer dan eerst het MediaTek-stuurprogramma op Windows — het [chauffeur gids](../drivers_nl.html) omvat Windows- en Linux-machtigingen.

## Herstel de Y1 standaardfirmware

Als de speler wordt gedetecteerd maar niet wil opstarten, installeer dan de Y1 originele software opnieuw. Gebruik alleen een Y1-pakket; een Y2-build start niet op Y1-hardware.
  - Openen [Updater CE](../guide_nl.html#platform) op uw computer.
  - Instellen Apparaatmodel aan Y1.
  - Kies Originele software binnen Software en kies een stabiele Y1-release – het handmatige pakket is dat `rom.zip`.
  - Klik Installeren / Herstellen en laat het pakket uitpakken.
  - Schakel de Y1 volledig uit, sluit de USB datakabel alleen aan als Updater daarom vraagt, en wacht totdat de succesmelding verschijnt.
Houd de stroom stabiel. Een flitser die geen stroom meer heeft, kan de speler onbruikbaar maken. Laad hem eerst op en sluit hem direct aan op de computer.

## Handmatig herstel wanneer Updater de speler niet kan zien

Updater CE bevat handmatige herstelhulpmiddelen voor gevallen waarin de begeleide installatie niet kan worden voltooid. [SP Flash Tool](../sp-flash-tool_nl.html) is gebundeld op Windows en Linux x86, en de MTKClient-route omvat macOS. Beide hebben een op het model afgestemd firmwarepakket nodig van de [Firmware-downloads](../firmware_nl.html) pagina.

Volg de gereedschapsgids voor uw platform in plaats van spreidingsbestanden of offsets te improviseren. Als de speler door geen enkel hulpmiddel wordt gedetecteerd, ligt de fout waarschijnlijk bij de batterij, de oplaadpoort of het bord.

## Als hij nog steeds niet wil starten

Stop met knipperen en behandel het als hardware. Open de behuizing niet en druk niet op de batterij. Vraag de gemeenschap met het model wat het scherm doet, of een computer het detecteert en welke pakketten je hebt geprobeerd — de [Discord gemeenschap](https://discord.gg/zHrT2zrcek) kan helpen bij het identificeren van een serviceroute.

Een voorraadherstel vervangt het systeem, dus maak een back-up van alles wat in het interne geheugen van de speler is opgeslagen voordat u gaat flashen. Muziek op een MicroSD-kaart wordt niet beïnvloed door het herstel.

## Innioasis Y1 Veelgestelde vragen over energie

### Waarom gaat mijn Innioasis Y1 niet aan?

De gebruikelijke oorzaken zijn een volledig lege batterij, een oplaadkabel of een zwakke oplader, een firmware-crash waardoor het opstarten stopt, of een hardwarefout. Laad hem gedurende 30 minuten op met een bekende datakabel voordat u ervan uitgaat dat de speler dood is.

### Hoe kan ik een Innioasis Y1 geforceerd opnieuw opstarten?

Houd de aan/uit-knop ongeveer 15 seconden ingedrukt, laat hem los, wacht vijf seconden en druk vervolgens één keer op de aan/uit-knop. Als er niets verschijnt, laat hem dan opladen en probeer het na 30 minuten opnieuw.

### Kan ik een Y1 herstellen die niet kan worden ingeschakeld?

Vaak wel. Als een computer het MediaTek-apparaat nog steeds detecteert, installeer dan het Y1 originele softwarepakket opnieuw met Updater CE. Als het niet wordt gedetecteerd, gebruik dan het SP Flash Tool of MTKClient herstel dat bij Updater CE wordt geleverd en een op het model afgestemd Y1 firmwarebestand.

### Moet een Y1 worden opgeladen voordat hij kan flitsen?

Ja. Een flitser die geen stroom meer heeft, kan de speler onbruikbaar maken. Laad hem eerst op en sluit hem rechtstreeks aan op de computer in plaats van via een hub.

## Gerelateerde oplossingen
  - [Y2 gaat niet aan](y2-wont-turn-on_nl.html) — dezelfde controles voor de Y2
  - [Y1 scrollwiel werkt niet](y1-scroll-wheel-not-working_nl.html) - als het opstart, maar het stuur niet
  - [Innioasis herstelgids](recovery_nl.html) — alle symptoomgidsen op één plek
  - [SP Flash Tool gids](../sp-flash-tool_nl.html) — handmatig knipperen op Windows en Linux
  - [Problemen met een installatie oplossen](../troubleshooting_nl.html) – hoe een mislukte flitser eruit ziet

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
