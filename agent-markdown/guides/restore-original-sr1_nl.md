---
title: "Herstel originele software op Timmkoo SR1 - stap voor stap"
description: "Hoe u de officiële originele software kunt herstellen op een Timmkoo SR1 met Innioasis Updater CE of SP Flash Tool, met behulp van het geverifieerde rom_sr1.zip-pakket."
language: "nl"
source: "https://innioasis.app/guides/restore-original-sr1_nl.html"
---

# Herstel originele software op Timmkoo SR1 - stap voor stap

Herstelgids · Timmkoo SR1

# Originele software herstellen op Timmkoo SR1

Een schone terugkeer naar de software waarmee de speler is geleverd. Gebruik het na een mislukte update, voordat u de speler verkoopt of wanneer een aangepast systeem niets voor u is.[Updater CE downloaden](../guide_nl.html#platform)[SR1 downloads](../firmware_nl.html?model=SR1)[SR1 handleiding](../manuals/sr1.html)

Installatiehandleiding voor uw computer

## Herstel originele software op uw SR1 met uw computer

Kies de handleiding voor de computer die u gebruikt. Elke versie heeft de platformconfiguratie, Updater CE stappen en de weg terug naar de voorraad.[Windows-gids](/install/original-sr1-windows.html)[macOS-gids](/install/original-sr1-mac.html)[Linux-gids](/install/original-sr1-linux.html)

[Alle Timmkoo SR1 gidsen](/install/sr1.html) · [Alle originele softwarehandleidingen](/install/original-software.html)

## Wat je nodig hebt
  - Een Windows-, macOS- of Linux-computer. Updater CE draait op alle drie.
  - De USB-datakabel die bij de speler is geleverd. Alleen-oplaadkabels zullen niet werken.
  - De ambtenaar `rom_sr1.zip` pakket dat Updater voor u downloadt, of een kopie van het [SR1 archief](../firmware_nl.html?model=SR1) als u liever met de hand flitst.
  - Laad de speler op. Een herstel waarbij stroom verloren gaat, is de enige gebruikelijke manier om een slechte situatie nog erger te maken.

Hiermee wordt het systeem vervangen en de interne opslag gewist. Kopieer muziek, opnames en foto's eerst naar een computer.

## Route A: Updater CE (aanbevolen)
  - Installeren [Innioasis Updater CE](../guide_nl.html#platform) en open het.
  - Instellen Apparaatmodel aan SR1. Het model moet exact bij de speler passen.
  - Kies Originele software in de Softwarelijst.
  - Kies een uitgave. De nieuwste stabiele build is de veilige standaard.
  - Druk op Installeren / Herstellen en wacht terwijl het pakket wordt gedownload en uitgepakt.
  - Schakel de speler volledig uit en sluit de USB-kabel alleen aan als Updater daarom vraagt.
  - Raak de speler of de kabel niet aan totdat het succesbericht verschijnt. Koppel de speler los en start deze.
Kies nooit een ander model om ‘het te laten werken’. Een SR1 heeft een SR1-pakket nodig. Door modellen te mixen hebben spelers uiteindelijk een handmatig herstel nodig.

## Route B: SP Flash Tool (handmatig)

Gebruik dit wanneer een computer Updater CE niet kan uitvoeren, of wanneer u het pakket al heeft en de voorkeur geeft aan de klassieke tool.
  - Downloaden `rom_sr1.zip` van de [SR1 archief](../firmware_nl.html?model=SR1) en rits het uit.
  - Bewaar het spreidingsbestand naast de afbeeldingen. Hernoem of verplaats de afbeeldingen niet.
  - Open SP Flash Tool, kies Alleen downloadenen laad het verspreidingsbestand.
  - Schakel de speler uit, druk op Downloadenen sluit vervolgens de kabel aan.
  - Wacht op het groene succesteken voordat u de verbinding verbreekt.

De [SP Flash Tool gids](../sp-flash-tool_nl.html) behandelt stuurprogramma's en de Windows-prompts in meer detail. Op Linux en macOS is Updater CE de gemakkelijkere route omdat het zijn eigen USB-verwerking met zich meebrengt.

## Na het herstel
  - Koppel de speler los en laat hem zelfstandig opstarten.
  - Kies uw taal en stel de klok in.
  - Maak opnieuw verbinding met Wi-Fi of Bluetooth als u deze gebruikt.
  - Kopieer je muziek terug. De [overdracht gids](../manuals/transfer-music.html) heeft de mapnamen.

Als de speler start maar het scherm, het wiel of de knoppen zich nog steeds niet goed gedragen, heeft het herstel gewerkt; dat is een hardware- of installatievraag, geen softwarevraag. De [gids voor probleemoplossing](../troubleshooting_nl.html) is de volgende halte.

## Als het niet werkt

### Updater ziet de speler nooit

Vervang de kabel en vervolgens de USB-poort. Vermijd hubs. In Windows installeert u het stuurprogramma MediaTek vanaf het [chauffeurspagina](../drivers_nl.html).

### De flits stopt vroeg

Sluit opnieuw aan, laad de speler op en begin opnieuw. Stap niet over op een pakket van een ander model.

### De speler blijft zwart

Laad een uur op en houd de stroom vervolgens tien seconden vast. Als het nog steeds dood is, lees dan de [herstel gids](../guides/recovery_nl.html) voordat u het opnieuw probeert.

## Vragen die mensen stellen

### Zal dit mijn muziek verwijderen?

Ja, de interne opslag is gewist. Bestanden op een microSD-kaart overleven meestal, maar kopieer ze eerst naar een veilige plek.

### Kan ik daarna teruggaan naar Rockbox?

Ja. Het herstellen van originele software is geen eenrichtingsverkeer; de aangepaste softwarepagina voor uw model kunt deze opnieuw installeren.

### Heb ik de instelling Type A/Type B nodig?

Alleen de Y1 heeft die keuze, en alleen voor Originele Software. Elk ander model gebruikt één pakket.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
