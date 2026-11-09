---
title: "Wi-Fi, Bluetooth en FM-radio instellen voor Reborn (Y2Linux) - Innioasis Updater"
description: "Korte post-installatiehandleiding voor Reborn (Y2Linux / Y2Reborn) op Innioasis Y2: kopieer system.img en stel vervolgens Wi-Fi, Bluetooth en FM-radio in."
language: "nl"
source: "https://innioasis.app/y2reborn_wifibt_nl.html"
---

# Wi-Fi, Bluetooth en FM-radio instellen voor Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Na installatie

# Wi-Fi, Bluetooth en FM-radio instellen.

Kopieer één bestand naar uw speler. Reborn doet de rest.[Download systeem.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Installatiehandleiding](guides/reborn-y2linux-y2.html)[Waarom Y2Reborn?](reborn-y2linux-benefits_nl.html)

## Waarom dit bestand?

Wi-Fi, Bluetooth en FM-radio hebben vijf MediaTek firmwaremodules nodig die Reborn niet kunnen verzenden. Ze bevinden zich in de officiële Y2 `system.img`. Reborn extraheert ze één keer, controleert ze en verwijdert het bestand.

## Installatie
  - Download systeem.img

Download de v3.2.0 FM `system.img` naar uw computer.[ Download systeem.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Start Reborn één keer op

Zet de speler aan. Wacht op Opslag instellen om te voltooien en start het vervolgens één keer opnieuw.
  - Maak verbinding met uw computer

Gebruik een USB-datakabel. De speler verschijnt als Interne opslag.Op een Mac?

Installeren [OpenMTP](https://openmtp.ganeshrvel.com/) om door de speler te bladeren. Windows en Linux mounten het automatisch.
  - Kopieer system.img naar Firmware

Maak een map met de naam `Firmware` aan de basis van interne opslag. Kopiëren `system.img` erin.
  - Wacht tot het instellen is voltooid

Reborn installeert de radiofirmware automatisch en verwijdert deze `system.img`. Dit duurt ongeveer 10-20 seconden. Wacht op Wi-Fi en Bluetooth zijn klaar.
  - Verbind Wi-Fi, Bluetooth en FM-radio
    - Wifi: Instellingen → Systeem → Netwerk → Wi-Fi. Kies uw 2,4 GHz-netwerk.
    - Bluetooth: Zet uw hoofdtelefoon in de koppelingsmodus. Instellingen → Bluetooth → selecteer ze.
    - FM-radio: Sluit een bedrade hoofdtelefoon aan als antenne en open vervolgens FM-radio.

  - Updaten via wifi

Toekomstige Reborn updates worden geïnstalleerd via Instellingen → Systeem → Software-update. Uw radiofirmware blijft staan.

## Was deze gids nuttig?

Vond u deze installatiehandleiding na de installatie nuttig? Ja, het hielp! [ Hulp nodig op Discord ](https://discord.gg/zHrT2zrcek) Bedankt voor uw feedback! Geniet van draadloos luisteren op Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
