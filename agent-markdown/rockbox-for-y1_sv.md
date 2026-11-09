---
title: "Rockbox för Y1 (Rockbox-Y1): översikt, bygg- och installationsguide"
description: "Rockbox för Y1, Rockbox-Y1 och rockbox-y1 hänvisar alla till gemenskapens Rockbox firmware för Innioasis Y1. Lär dig vad den lägger till, vilken version du ska välja och hur du installerar den med Innioasis Updater CE."
language: "sv"
source: "https://innioasis.app/rockbox-for-y1_sv.html"
---

# Rockbox för Y1 (Rockbox-Y1): översikt, bygg- och installationsguide

[← Nedladdning av fast programvara](firmware_sv.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox för Y1 (Rockbox-Y1)

“Rockbox”, “Rockbox-Y1” och “Rockbox för Y1” hänvisar alla till samma community Rockbox firmware för Innioasis Y1. Här är vad det tillför din spelare, vilken konstruktion du ska välja och hur du installerar den med Innioasis Updater CE.[Installera Rockbox-Y1](rockbox-y1/install.html)[Ladda ner ROM](rockbox-y1/download.html)[Skriftlig handledning](guides/rockbox-y1.html)[Rockbox-Y1 nav](rockbox-y1/)

## En firmware, flera namn

I Innioasis Updater CE visas denna firmware som Rockbox när du väljer enhetsmodell Y1. Guider, videor och release notes kallar det också Rockbox-Y1 eller Rockbox för Y1 så det är tydligt att konstruktionen är för Y1 och inte Y2.

Kontrollera alltid modellen som är tryckt på din spelare innan du installerar: Y1 och Y2 firmwarepaket är inte utbytbara.

## Vad Rockbox-Y1 lägger till din Y1

Rockbox-Y1 är en gemenskapsport för open-source Rockbox musikspelarens firmware för Innioasis Y1:
  - Taggbaserat musikbibliotek — bläddra efter artist, album, genre och år med ljudtaggar, eller bläddra direkt i mappar.
  - Avancerad ljuduppspelning — uppspelning utan mellanrum, övertoning, ReplayGain och en fullständig equalizer.
  - Anpassade teman — välj bland hundratals 240p- och 360p-gemenskapsteman, inklusive klassiska iPod-layouter.
  - FM-radio — inbyggt stöd för FM-radio.
  - Tillval — poddnedladdningar via Wi-Fi och Last.fm / ListenBrainz / Maloja scrobbling på versioner som stöds.
  - Dubbel stövel — växla tillbaka till originalprogramvaran från fabriken utan återhämtning på byggda versioner som stöds.

## Vilken Y1 build ska jag välja?
  - 240p mot 360p — 240p-byggen fungerar med klassiska 320×240 Rockbox-teman; 360p-byggen använder skarpare 480×360 Y1 teman. Matcha byggupplösningen till de teman du vill använda ([240p kontra 360p guide](rockbox-y1/resolution.html)).
  - Type A kontra Type B — Type A är för Y1 spelare som levereras med fabriksprogramvara 2.0.0 eller senare; Type B är för tidigare Y1 enheter. Välj Type A om du inte vet att din Y1 är Type B.
  - Stabil vs. Nightly — Välj en stabil konstruktion för vardagslyssning, eller en nattlig konstruktion för att testa de senaste ändringarna.

## Direktnedladdningar från communityutvecklarna

Innioasis Updater CE laddar alltid ner firmware-paket direkt från community-firmware-utvecklarna ([rockbox-y1/rockbox](firmware_sv.html?model=Y1&software=rockbox-y1)), och utvecklarna själva är ensamma ansvariga för att lista sina programvaruversioner i Updater CE.

Du kan låta Updater CE ladda ner och installera firmware automatiskt, eller ladda ner ROM-paketen från vår [Rockbox-Y1 nedladdningssida](rockbox-y1/download.html) och [Rockbox ROM nedladdningssida](rockbox-rom-download_sv.html).[Rockbox-Y1 nedladdningar](rockbox-y1/download.html)[Installera från en lokal ZIP](rockbox-y1/portable-zip.html)

## Hur man installerar Rockbox-Y1
  - Öppna Innioasis Updater CE och ställ in Enhetsmodell till Y1.
  - Välj Rockbox i Programvara.
  - Välj en stabil version (eller aktivera nattbyggen för att testa en förhandsvisning).
  - Klicka Installera / Återställ så Updater CE laddar ner paketet direkt från utvecklaren.
  - Stäng av Y1 helt och anslut den med en USB datakabel när Updater CE uppmanar dig.
  - Vänta på meddelandet om slutförandet, koppla sedan bort och slå på din spelare.

För skärmdumpar och detaljerade installationstips, läs [fullständig Rockbox-Y1 handledning](guides/rockbox-y1.html).

## Återställer den ursprungliga programvaran Y1

Du kan återgå till fabriksmjukvaran när som helst: välj Y1 och Originalprogramvara i Updater CE, välj en stabil version och klicka Installera / Återställ. Din musik på MicroSD-kortet bevaras. Se den [återställningsguide](rockbox-y1/restore-stock.html) och [Y1 Sida för originalprogramvara](original-software-y1_sv.html).

## Vanliga frågorÄr Rockbox för Y1 detsamma som Rockbox-Y1?

Ja. Rockbox, Rockbox-Y1, Rockbox för Y1, och `rockbox-y1` alla hänvisar till samma community Rockbox-port för Innioasis Y1.Var hämtar Updater CE Rockbox-Y1 från?

Updater CE laddar alltid ner firmware-paket direkt från community-firmware-utvecklarnas egna releaser (`rockbox-y1/rockbox`). Utvecklarna är ensamma ansvariga för att lista sina programvaruversioner i Updater CE.Kan jag installera Rockbox-Y1 på en Y2?

Nej. Y2 har sin egen separata fasta programvara. Använd [Rockbox för Y2](rockbox-for-y2_sv.html) istället.Kommer installationen av Rockbox-Y1 att radera min musik?

Nej. Musik lagras på MicroSD-kortet och påverkas inte när spelarens interna firmware blinkar.

## Relaterade guider

### [Rockbox-Y1 nav](rockbox-y1/)

Alla Y1 guider: installation, nedladdningar, teman, återställning, dubbelstart och felsökning.

### [Rockbox-Y1 mot Rockbox-Y2](rockbox-y1-vs-y2.html)

Hur byggnaderna Y1 och Y2 Rockbox skiljer sig åt.

### [Rockbox-Y1-teman](rockbox-y1-themes.html)

Hur man överför 240p- och 360p-teman med Updater CE.

### [Rockbox översikt](rockbox_sv.html)

Introduktion till Rockbox på Innioasis Y1 och Y2 spelare.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
