---
title: "Hoe installeer je Rockbox op je Innioasis Y1 of Y2 - Innioasis Updater"
description: "Installeer Rockbox op een Innioasis Y1 of Y2 met Updater: thema&#39;s, stabiele releases, Type A en Type B opmerkingen, en hoe u daarna de originele software kunt herstellen."
language: "nl"
source: "https://innioasis.app/rockbox_nl.html"
---

# Hoe installeer je Rockbox op je Innioasis Y1 of Y2 - Innioasis Updater

Rockbox referentie

# Rockbox verkrijgen op uw Y1 of Y2

Rockbox verandert de spelersoftware en opent een diepere interface voor de muziekspeler, afspeelbediening, sortering en thema-opties. De installatie wordt begeleid, maar Y1 en Y2 zijn afzonderlijke trajecten.[Rockbox op Y1](guides/rockbox-y1.html)[Rockbox op Y2](guides/rockbox-y2.html)[Waarom Rockbox?](rockbox-benefits_nl.html)

## Wat de installatie verandert

Rockbox is maatwerksoftware. Het ontneemt niet uw mogelijkheid om terug te keren naar de standaardinterface wanneer het overeenkomende Originele Softwarepakket beschikbaar is. Het kan het browsen en aanpassen van muziek verbeteren, maar functies, resolutie, batterijduur en thema-compatibiliteit zijn afhankelijk van de build.Meng geen modellen. Selecteer Y1 voor een Y1-speler en Y2 voor een Y2-speler. Een gelijksoortige releasenaam is niet voldoende bewijs dat een pakket compatibel is.

## Bekijk de video

Video van Frawgeeys. Het toont de Innioasis Updater-route; gebruik de modelspecifieke schriftelijke stappen hieronder voor uw Y1 of Y2.

Video door [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (Spaans), met Rockbox op een Y1. Gebruik de onderstaande modelspecifieke stappen voor uw speler.

## De gedeelde Updater-route
  - Installeer Updater en sluit niets aan totdat dit wordt gevraagd.
  - Kies het model dat op de speler is afgedrukt Apparaatmodel.
  - Kies Rockbox binnen Software.
  - Kies een stabiele release, tenzij je opzettelijk een nachtelijke build test.
  - Klik Installeren / Herstellenen volg vervolgens de prompt voor het uitschakelen en USB-verbinding.
  - Verbreek de verbinding pas na het succesbericht.

## 240p, 360p en thema's

Oudere Rockbox themacollecties kunnen voor 240p worden gemaakt. Y1 communitybuilds gebruiken ook 360p-compatibiliteitslabels. Lees de releaseopmerkingen en de themabron voordat u een build kiest. Een thema dat voor de ene resolutie of softwarefamilie is gemaakt, werkt mogelijk niet op een andere.[Blader door communitythema's](https://themes.innioasis.app/?lang=nl)[Themahulpmiddelen](https://themes.innioasis.app/?lang=nl)

## Terugkeren naar originele software

Kies opnieuw hetzelfde model, selecteer Originele software, kies een stabiele release en gebruik Installeren / Herstellen. Als de fout plaatsvond vóór de USB-prompt, controleer dan de computer en de uitgepakte bestanden. Als de speler is gedetecteerd maar de flitser is mislukt, begint u met [probleemoplossing](troubleshooting_nl.html).[Y1 herstellen](guides/restore-original-y1.html)[Y2 herstellen](guides/restore-original-y2.html)

## Veelgestelde vragenIk heb Rockbox opnieuw geïnstalleerd, maar er is niets opgelost.

Als u Rockbox opnieuw installeert, wordt dezelfde build over dezelfde bestanden geschreven, zodat de dingen die Rockbox op MicroSD bewaart, niet kunnen worden gereset. Als het probleem een ​​kapotte instelling, thema, afspeellijst of database op de kaart is, zal het opnieuw installeren het probleem niet oplossen. De betrouwbare reset is het verwijderen van de `.rockbox` map uit de MicroSD — Rockbox bouwt een nieuwe op bij de volgende keer opstarten.
  - Schakel de speler volledig uit en verwijder de MicroSD-kaart, of sluit de speler aan als een USB-station.
  - Toon verborgen bestanden op uw computer zodat de map zichtbaar is. Hoe verborgen bestanden te tonenToon dotbestanden op uw computerWindows: in Verkenner opent u het Weergave tabblad en vink aan Verborgen voorwerpen.macOS: in Finder druk op Cmd+Shift+. om verborgen bestanden te schakelen.Linux · GNOME-bestanden: druk Ctrl+H, of open het menu en kies Toon verborgen bestanden.Linux · KDE Dolphin: druk Ctrl+H, of gebruik Beeld → Verborgen bestanden tonen.
  - Verwijder de `.rockbox` map uit de kaartroot.
  - Plaats de kaart opnieuw en start de speler. Rockbox maakt de map opnieuw met de standaardwaarden.
  - Pas uw thema en instellingen opnieuw toe. Als het probleem pas na een bepaald thema terugkomt, is dat thema de oorzaak.

Verwijderen `.rockbox` verwijdert Rockbox niet en raakt uw muziek niet aan: de map bevat instellingen, thema's en caches en wordt automatisch opnieuw opgebouwd. Als u uw thema's wilt behouden, kopieert u de map eruit `.rockbox` voordat u deze verwijdert, of hernoem de map naar `.rockbox-old` eerst.Waarom kan ik de map .rockbox niet zien op mijn MicroSD?

Mappen waarvan de naam met een punt begint, zijn op de meeste computers standaard verborgen. U hoeft het niet te zien om Rockbox te installeren — Updater verwerkt de bestanden. Als u problemen oplost en deze wilt verwijderen, schakelt u eerst verborgen bestanden in. Hoe verborgen bestanden te tonenToon dotbestanden op uw computerWindows: in Verkenner opent u het Weergave tabblad en vink aan Verborgen voorwerpen.macOS: in Finder druk op Cmd+Shift+. om verborgen bestanden te schakelen.Linux · GNOME-bestanden: druk Ctrl+H, of open het menu en kies Toon verborgen bestanden.Linux · KDE Dolphin: druk Ctrl+H, of gebruik Beeld → Verborgen bestanden tonen.Zal het verwijderen van .rockbox mijn thema en instellingen resetten?

Ja - `.rockbox` bevat de instellingen, het thema, de afspeellijsten en de in de cache opgeslagen database van Rockbox. Als u het verwijdert, keert Rockbox terug naar een schone standaardstatus. Maak een back-up van de hele map (of hernoem deze naar `.rockbox-old`) als je er misschien iets van terug wilt, start dan de speler en Rockbox maakt een nieuwe map aan.

## Meer Rockbox-Y1 en Rockbox-Y2 handleidingen

Ontdek stapsgewijze handleidingen voor het installeren, downloaden, thema's toevoegen, herstellen en probleemoplossing Rockbox op beide modellen:[Rockbox-Y1-hub](rockbox-y1/)[Rockbox-Y2-hub](rockbox-y2/)[Rockbox ROM-downloads](rockbox-rom-download_nl.html)[Rockbox voor J1](rockbox-for-y1_nl.html)[Rockbox voor J2](rockbox-for-y2_nl.html)[Rockbox-Y1 versus Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1-thema's](rockbox-y1-themes.html)[Rockbox-Y2-thema's](rockbox-y2-themes.html)

## Was deze verwijzing nuttig?

Uw antwoord helpt deze handleiding te verbeteren.JaNog niet[Laat ons weten hoe we kunnen verbeteren](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
