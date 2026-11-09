---
title: "SP Flash Tool for Innioasis og Timmkoo spillere"
description: "Find SP Flash Tool bundtet med Innioasis Updater på Windows og Linux, udpak rom.zip eller rom_y2.zip, og flash en Innioasis Y1 eller Y2 med den matchende scatter-fil."
language: "da"
source: "https://innioasis.app/sp-flash-tool_da.html"
---

# SP Flash Tool for Innioasis og Timmkoo spillere

Manuel blink

# Flash-værktøj til Innioasis og Timmkoo spillere

SP Flash Tool kommer inde i Innioasis Updater tændt [Windows](drivers_da.html#windows) og [Linux](drivers_da.html#linux). Du har det allerede. Denne guide viser den sikre måde at bruge den på en Innioasis Y1 eller Y2, og Updater-ruten for Timmkoo spillere.[Vend tilbage til opdateringsvejledningen](guide_da.html)[Firmware downloads](firmware_da.html)[Fejlfinding](troubleshooting_da.html)

Start med Innioasis Updater

## Updater klarer hele jobbet i én omgang

Updater udfører de fleste installationer på én gang. Vælg softwaren, følg trinene, og du er færdig. Den fortæller dig også, hvornår en rettelse eller en ny udgivelse lander. SP Flash Tool er inde i Updater's Toolkit i de sjældne tilfælde Updater ikke kan afslutte. Trinene nedenfor er undtagelsen.

## Hvad er dette værktøj til

Updater blinker afspilleren for dig. SP Flash Tool er den samme motor uden rækværk. Brug det, når Updater ikke starter, når afspilleren ikke vil oprette forbindelse, eller når du kender din vej rundt i en scatter-fil.Prøv Updater først. For de fleste installationer og de fleste gendannelser er den guidede [Opdateringsrute](guide_da.html) er det sikreste valg. Brug SP Flash Tool, når du ved, hvorfor du har brug for det, og hold et opladet batteri plus et USB datakabel klar.

## Flash-værktøj til Innioasis spillere

Innioasis Updater er flashværktøjet til Innioasis spillere. Det installerer officiel software, opdateringer og gendannelsespakker gennem det model-matchede flow, og det beholder din musik og dine indstillinger.

### Innioasis Y1 flashværktøj

Vælg Y1-udgivelsen i Updater, og tilslut derefter den slukkede afspiller, når appen spørger. De samme Y1-pakker fungerer med SP Flash Tool, når du har brug for den manuelle rute.

### Innioasis Y2 flashværktøj

Vælg en udgivelse, der er angivet for Y2. Y2-pakker kan ikke udskiftes med Y1-pakker, så tjek modellen, før du starter.

## Flash-værktøj til Timmkoo spillere

Timmkoo spillere bruger det samme Updater installationsflow. Den læser Timmkoos ZIP- og RAR-pakker direkte, så du behøver ikke et separat flashværktøj eller scatter-fil.

### Timmkoo Q5 flashværktøj

Vælg Q5-modellen i Updater, vælg Timmkoo-pakken, kør derefter Installer/Gendan og tilslut afspilleren ved prompten.

### Timmkoo Q3 og Q3E flashværktøj

Indgangen Q3 dækker både Q3 og Q3E. Updater vælger de matchende filer fra den pakke, som projektet udgiver.

### Timmkoo A5 flashværktøj

Vælg A5-modellen, før du vælger en pakke, og følg derefter den samme installationsprompt.

## Hvor Updater udtrykker det

SP Flash Tool leveres med Updater-installationsmappen, ikke som en separat download. Åbn det derfra, når du har brug for det.

### Windows

Åbn Updater installationsmappen og kør `flash_tool.exe`. Mappen er normalt under `%LOCALAPPDATA%\Innioasis Updater`. En Toolkit-mappe med en SP Flash Tool-genvej er inkluderet i nogle opsætninger.

### Linux

Kør den medfølgende `flash_tool` binær inde i Updater-appmappen på x86 / x86_64. Projektinstallationsprogrammet forbereder USB tilladelser med udev-regler, så afspilleren skulle vises, når den er tilsluttet.

### macOS

SP Flash Tool er ikke bundtet på macOS. Updater bruger MTKClient-ruten dertil i stedet. Brug [guidet installation](guide_da.html) på en Mac og behold SP Flash Tool til en Windows- eller Linux-maskine.

Værktøjet leveres med MediaTek download-agent og modelspecifik konfiguration, så du ikke behøver at indsamle DA eller scatter-filer fra andre steder.

## Forbered firmwaren
  - Grib den udgivelse, du ønsker fra [Firmware downloads](firmware_da.html). Vælg `rom.zip` for en Y1 eller `rom_y2.zip` for en Y2.
  - Udpak ZIP i sin egen mappe. Windows kan bruge Extract All. På Linux skal du bruge din arkivhåndtering eller `unzip` i en terminal.
  - Kontroller, at scatter-filen er i den udpakkede mappe. Det hedder normalt `MT6572_Android_scatter.txt` for Y1 pakker og `MT6582_Android_scatter_def.txt` for Y2 pakker, selvom en udgivelse kan navngive den efter sit projekt.
Hold modellerne adskilt. Y1-spredningen beskriver en MT6572-enhed, og Y2-spredningen beskriver en MT6582-enhed. At blinke med den forkerte er, hvordan spillere bliver muret. Hvis spredningen inde i ZIP ikke matcher din model, skal du stoppe og bruge en pakke, der er angivet til din model i stedet.

## Indlæs scatter og flash
  - Åbn SP Flash Tool fra Updater installationsmappen.
  - Klik på fanen Download Vælg ud for Scatter-loading File og vælg scatter-filen fra den udpakkede mappe. Partitionslisten udfyldes.
  - Lad blitztilstanden være tændt Kun download medmindre du bevidst laver en fuld genopretning, hvilket har brug for Firmware opgradering.
  - Klik Download. Værktøjet venter på afspilleren.
  - Sluk for afspilleren helt, og tilslut derefter USB-datakablet. Læg afspilleren ned og flyt den ikke.
  - Vent på det grønne flueben. Først derefter frakobles kablet og afspilleren startes.

Hold de samme USB kabel- og timingregler som den guidede rute: et datakabel, ingen hub, og tilslut kun, når værktøjet er klar.

## Hvis den ikke blinker
  - Kontroller, at scatter og ZIP matcher modellen trykt på afspilleren.
  - Bekræft, at afspilleren er helt slukket, før du tilslutter.
  - I Windows skal du bekræfte driveren MediaTek installeret med Updater-opsætningen; på Linux skal du bekræfte udev-reglerne fra projektinstallationsprogrammet.
  - Tilslut kun kablet igen, når værktøjet venter. Et havneløb kan have brug for et helt stik og en frisk Download klik.

For alt ud over det, åben [fejlfinding](troubleshooting_da.html). Og husk: Updater er stadig den normale rute, og [Y1](guides/restore-original-y1.html) og [Y2](guides/restore-original-y2.html) gendannelsesguider bruger det også.

## Var dette nyttigt?

Dit svar hjælper med at forbedre denne vejledning.Ja, jeg fandt det nyttigtIkke endnu[Fortæl os, hvordan vi kan forbedre os](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
