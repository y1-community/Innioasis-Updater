---
title: "Innioasis Uppdateringsfelsökning | Innioasis och Timmkoo installationsproblem - Innioasis Updater"
description: "Fixa Innioasis Updater-installationer på valfri Innioasis eller Timmkoo spelare. Kontrollera modellen, kabeln, drivrutinen, tidpunkten för avstängning och var installationen slutade - och få den att blinka igen."
language: "sv"
source: "https://innioasis.app/troubleshooting_sv.html"
---

# Innioasis Uppdateringsfelsökning | Innioasis och Timmkoo installationsproblem - Innioasis Updater

Felsökning

# Hitta den punkt där installationen slutade.

Var tog det stopp? Det talar om vad du ska fixa.[Återgå till den normala guiden](guide_sv.html)[Kontrollera firmware](firmware_sv.html)

## Det slutade före USB prompten

Detta är ett datorproblem, inte ett kabelproblem. Kontrollera din modell. Packa upp filen igen. Försök sedan Installera / Återställ. Om releaselistan är tom, öppna [firmware katalog](firmware_sv.html).

## Den kan inte ansluta till spelaren
  - Stäng av rätt Y1 eller Y2 helt.
  - Koppla ur kabeln, stäng andra flash- eller Android-verktyg och starta installationen igen.
  - Anslut endast när Updater säger att den är klar.
  - Använd en kort USB datakabel direkt i datorn, inte en hubb om möjligt.
  - I Windows, installera om MediaTek-drivrutinen och starta om. På Linux, kontrollera USB/seriebehörigheter.
Uppmaning om uppdatering av anslutningLive Updater-prompten är auktoritativ för den aktuella modellen och plattformen.

## Den upptäckte spelaren men blixten misslyckades

Stanna här. Prova inte en annan modell. Stäng andra verktyg, kontrollera att du valde rätt Y1 eller Y2 och använd den matchande originalmjukvaran om spelaren inte startar. [SP Flash Tool](sp-flash-tool_sv.html) och MTKClient ingår om du behöver dem, och filerna finns på [firmware sida](firmware_sv.html).

## Anteckningar om Windows-drivrutinen

Vissa Windows-installationer blockerar MediaTek-drivrutinen på grund av Core-isolering. Följ nuvarande säkerhetsanvisningar för Windows innan du ändrar minnesintegritet och slå på den igen när du är klar om ditt system tillåter det.[Öppna förarguiden](drivers_sv.html)[Ren installationsguide](Troubleshooting/clean_install.html)

## Hjulet fungerar inte, eller spelaren startar inte

Ingångs- och strömfel kräver olika steg från en misslyckad blixt. Dessa guider täcker de vanliga fallen Y1 och Y2.[Y1 rullhjul](guides/y1-scroll-wheel-not-working.html)[Y2 rullhjul](guides/y2-scroll-wheel-not-working.html)[Y1 kommer inte att slås på](guides/y1-wont-turn-on.html)[Y2 kommer inte att slås på](guides/y2-wont-turn-on.html)[Återhämtningsguide](guides/recovery.html)

## Fortfarande fast?

När du ber om hjälp, inkludera modell, operativsystem, exakt Updater-meddelande, om spelaren upptäcktes och paketet/projektet du valde. Lägg inte upp privata tokens eller orelaterade systemfiler.[Be om hjälp](https://discord.gg/zHrT2zrcek)[Stöd underhåll](support_devs_sv.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
