---
title: "Innioasis Updater fejlfinding | Innioasis og Timmkoo installationsproblemer - Innioasis Updater"
description: "Ret Innioasis Updater-installationer på enhver Innioasis- eller Timmkoo-afspiller. Tjek modellen, kablet, driveren, tidspunktet for slukning, og hvor installationen stoppede - og få det derefter til at blinke igen."
language: "da"
source: "https://innioasis.app/troubleshooting_da.html"
---

# Innioasis Updater fejlfinding | Innioasis og Timmkoo installationsproblemer - Innioasis Updater

Fejlfinding

# Find det punkt, hvor installationen stoppede.

Hvor stoppede det? Det fortæller dig, hvad du skal rette.[Vend tilbage til den normale guide](guide_da.html)[Tjek firmwaren](firmware_da.html)

## Det stoppede før USB prompten

Dette er et computerproblem, ikke et kabelproblem. Tjek din model. Pak filen ud igen. Så prøv Installer / Gendan. Hvis udgivelseslisten er tom, skal du åbne [firmware bibliotek](firmware_da.html).

## Den kan ikke oprette forbindelse til afspilleren
  - Sluk helt for den korrekte Y1 eller Y2.
  - Tag kablet ud, luk andre flash- eller Android-værktøjer, og start installationen igen.
  - Tilslut kun, når Updater siger, at den er klar.
  - Brug et kort USB datakabel direkte i computeren, ikke en hub, hvis det er muligt.
  - I Windows skal du geninstallere MediaTek-driveren og genstarte. På Linux skal du kontrollere USB/serielle tilladelser.
Updater-forbindelsespromptLive Updater-prompten er autoritativ for den aktuelle model og platform.

## Den registrerede afspilleren, men flashen mislykkedes

Stop her. Prøv ikke en anden model. Luk andre værktøjer, tjek at du har valgt det rigtige Y1 eller Y2, og brug den tilsvarende originale software, hvis afspilleren ikke starter. [SP Flash Tool](sp-flash-tool_da.html) og MTKClient er inkluderet, hvis du har brug for dem, og filerne er på [firmware side](firmware_da.html).

## Windows driver noter

Nogle Windows-installationer blokerer MediaTek-driveren på grund af Core-isolation. Følg den aktuelle Windows-sikkerhedsvejledning, før du ændrer hukommelsesintegritet, og tænd den igen, når du er færdig, hvis dit system tillader det.[Åbn driverguide](drivers_da.html)[Ren installationsvejledning](Troubleshooting/clean_install.html)

## Hjulet virker ikke, eller afspilleren starter ikke

Indgangs- og strømfejl kræver forskellige trin end et mislykket flash. Disse vejledninger dækker de almindelige Y1 og Y2 tilfælde.[Y1 rullehjul](guides/y1-scroll-wheel-not-working.html)[Y2 rullehjul](guides/y2-scroll-wheel-not-working.html)[Y1 vil ikke tænde](guides/y1-wont-turn-on.html)[Y2 vil ikke tænde](guides/y2-wont-turn-on.html)[Retableringsvejledning](guides/recovery.html)

## Stadig fast?

Når du beder om hjælp, skal du inkludere modellen, operativsystemet, den nøjagtige opdateringsmeddelelse, om afspilleren blev fundet, og den pakke/det projekt, du valgte. Indsend ikke private tokens eller ikke-relaterede systemfiler.[Bed om hjælp](https://discord.gg/zHrT2zrcek)[Støtte vedligeholdelse](support_devs_da.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
