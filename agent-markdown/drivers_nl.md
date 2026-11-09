---
title: "Innioasis Y1 en Y2 USB stuurprogramma's | Windows-stuurprogramma en Linux-machtigingen - Innioasis Updater"
description: "Stel uw computer in voor Innioasis Updater: Windows MediaTek-stuurprogramma en Linux USB-rechten — plus kabel- en timingoplossingen."
language: "nl"
source: "https://innioasis.app/drivers_nl.html"
---

# Innioasis Y1 en Y2 USB stuurprogramma's | Windows-stuurprogramma en Linux-machtigingen - Innioasis Updater

Computeropstelling

# Maak de computer gereed vóór de speler.

De meeste verbindingsproblemen worden veroorzaakt door het stuurprogramma, de machtigingen, de kabel of de timing. Voor Windows is het stuurprogramma MediaTek geïnstalleerd. Linux heeft de juiste USB-rechten nodig. Vind hieronder uw platform.[Updater CE downloaden](guide_nl.html#platform)[Probleemoplossing](troubleshooting_nl.html)

## Windows
  - Download hieronder het MediaTek stuurprogramma-installatieprogramma.
  - Voer het installatieprogramma uit en laat Windows het stuurprogramma installeren.
  - Start de computer opnieuw op.
  - Open Updater CE en wacht op de verbindingsprompt voordat u de uitgeschakelde speler aansluit.

Sommige Windows-systemen blokkeren de driver via Core-isolatie (geheugenintegriteit). Als Updater CE de speler na een herstart nog steeds niet kan zien, schakel dan de Geheugenintegriteit uit in Windows Beveiliging, start opnieuw op en installeer het stuurprogramma opnieuw. Schakel de instelling weer in als u klaar bent, als uw systeem dit toestaat.

Windows start de app niet? Als Windows Security of Smart App Control Updater CE niet kan openen, open dan Instellingen (druk Win + I) → Privacy en veiligheid → Windows Security → App- en browsercontrole → Instellingen voor Smart App-bediening en stel deze in Uit. Smart App Control heeft momenteel invloed op populaire applicaties zoals de Epic Overlay Service (gebruikt door Fortnite) — Updater CE is veilig en geverifieerd. Om later weer in te schakelen, stelt u `VerifiedAndReputablePolicyState` aan `1` (Aan) of `2` (Evaluatiemodus) onder `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` in Register-editor.[Windows-stuurprogramma downloaden](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Terug naar de hoofdgids](guide_nl.html#windows) · [Softwaredownloads](firmware_nl.html)

## Linux USB-rechten

Linux heeft je gebruikersaccount nodig om met de MediaTek USB chip in de speler te kunnen praten. Updater CE lost dit meestal op tijdens de installatie, en dezelfde toestemming geldt voor SP Flash Tool, dus behandel dit als een reparatiestap in plaats van als een normale fase.
  - Voer Updater CE uit als uw normale gebruiker, niet als root. Het installatieprogramma vraagt ​​alleen om beheerderstoegang wanneer dit nodig is.
  - Controleer of de speler überhaupt wordt gezien. Schakel de speler uit, sluit de kabel aan en voer de opdracht lsusb uit in een terminal. Een verbonden speler wordt weergegeven als een MediaTek-apparaat met de leveranciers-ID 0e8d.
`lsusb`
  - Als het in lsusb verschijnt, maar Innioasis Updater CE of SP Flash Tool zegt dat de toestemming is geweigerd of kan de poort niet worden geopend, dan heeft uw gebruiker geen toegang tot het USB-apparaat. Dezelfde udev-regel geldt voor beide tools, dus voeg er een toe waarmee de gebruikersgroep deze kan lezen.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Sla die regel op in een nieuw bestand met de naam /etc/udev/rules.d/51-innioasis.rules en voer vervolgens uit:`sudo udevadm control --reload && sudo udevadm trigger`
  - Koppel de speler volledig los, sluit hem weer aan en probeer de installatie opnieuw.
  - Als SP Flash Tool een seriële toestemming of poortrace meldt, koppelt u de stekker volledig los en sluit u deze alleen opnieuw aan als daarom wordt gevraagd.
Improviseer geen flitscorrecties.Als u overstapt op een handmatige hersteltool, gebruikt u de bestanden en de modelspecifieke configuratie die bij het project zijn geleverd.

[Terug naar de hoofdgids](guide_nl.html#linux) · [Softwaredownloads](firmware_nl.html) · [SP Flash Tool gids](sp-flash-tool_nl.html)

## Kabel en timing
  - Gebruik een bekende USB-datakabel.
  - Vermijd hubs tijdens het oplossen van problemen.
  - Schakel het juiste model volledig uit.
  - Maak alleen verbinding als daarom wordt gevraagd.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
