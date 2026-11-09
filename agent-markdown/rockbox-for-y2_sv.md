---
title: "Rockbox för Y2 (Rockbox-Y2): översikt, bygg- och installationsguide"
description: "Rockbox för Y2, Rockbox-Y2 och rockbox-y2 hänvisar till gemenskapens Rockbox firmware-port för Innioasis Y2. Lär dig vad den innehåller och hur du installerar den med Innioasis Updater CE."
language: "sv"
source: "https://innioasis.app/rockbox-for-y2_sv.html"
---

# Rockbox för Y2 (Rockbox-Y2): översikt, bygg- och installationsguide

[← Nedladdning av fast programvara](firmware_sv.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox för Y2 (Rockbox-Y2)

Rockbox-Y2 (även kallad “Rockbox för Y2”) är den dedikerade community Rockbox firmware-porten för Innioasis Y2. Den använder sitt eget ROM-paket (`rom_y2.zip`) och installeras direkt via Innioasis Updater CE.[Installera Rockbox-Y2](rockbox-y2/install.html)[Ladda ner ROM](rockbox-y2/download.html)[Skriftlig handledning](guides/rockbox-y2.html)[Rockbox-Y2 nav](rockbox-y2/)

## Byggd speciellt för Innioasis Y2

I Innioasis Updater CE är denna firmware listad som Rockbox när Y2 är valt. Dess utgåvor publiceras av [spycemagic/y2-rockbox](firmware_sv.html?model=Y2&software=rockbox-y2) projekt med paketnamnet `rom_y2.zip`.

Installera aldrig ett Y1 firmwarepaket på en Y2. Väljer Y2 i Updater filtrerar CE automatiskt versionslistan till endast Y2-kompatibla versioner.

## Vad Rockbox-Y2 erbjuder
  - Taggbaserat musikbibliotek — bläddra bland album, artister och genrer från dina ljudfiltaggar, eller bläddra direkt i mappar.
  - Uppspelningskontroller — gapfri uppspelning, crossfade, ReplayGain och equalizerinställningar.
  - Anpassade teman – installera teman som är kompatibla med din Rockbox-Y2 build ([Y2 temaguide](rockbox-y2-themes.html)).
  - 100 % offline — spelar upp lokala filer från ditt MicroSD-kort utan konton eller prenumerationer.
  - Enkel fabriksåterställning — gå tillbaka till Y2 originalprogramvara när som helst i Updater CE.

## Att välja en Rockbox-Y2 release
  - Välj alltid Y2 i Enhetsmodell först.
  - Välj den senaste versionen om du inte testar en specifik version.
  - Läs [Rockbox-Y2 release notes](release-notes/rockbox-y2/index_sv.html) för att se vad som förändrades i varje byggnad.

## Direktnedladdningar från communityutvecklarna

Innioasis Updater CE laddar alltid ner firmware-paket direkt från community-firmware-utvecklarna ([spycemagic/y2-rockbox](firmware_sv.html?model=Y2&software=rockbox-y2)), och dessa utvecklare är ensamma ansvariga för att lista sina programvaruversioner i Updater CE.

Du kan låta Updater CE ladda ner och flasha `rom_y2.zip` automatiskt, eller ladda ner paketet från vår [Rockbox-Y2 nedladdningssida](rockbox-y2/download.html) och [Rockbox ROM nedladdningssida](rockbox-rom-download_sv.html).[Rockbox-Y2 nedladdningar](rockbox-y2/download.html)[Installera från en lokal ZIP](rockbox-y2/portable-zip.html)

## Hur man installerar Rockbox-Y2
  - Öppna Innioasis Updater CE och ställ in Enhetsmodell till Y2.
  - Välj Rockbox i Programvara.
  - Välj en Y2 release från listan.
  - Klicka Installera / Återställ så Updater CE laddar ner paketet direkt från utvecklaren.
  - Stäng av Y2 helt och anslut den med en USB datakabel när Updater CE frågar.
  - Vänta på meddelandet om slutförandet, koppla sedan ur och slå på din Y2.

För den fullständiga steg-för-steg-genomgången, läs [Rockbox-Y2 handledning](guides/rockbox-y2.html).

## Återställer den ursprungliga programvaran Y2

För att gå tillbaka till fabriksfast programvara, välj Y2 och Originalprogramvara i Updater CE, välj en stabil version och klicka Installera / Återställ. Se den [återställningsguide](rockbox-y2/restore-stock.html) och [Y2 Sida för originalprogramvara](original-software-y2_sv.html).

## Vanliga frågorVar hämtar Updater CE Rockbox-Y2 från?

Updater CE laddar alltid ner firmware-paket direkt från community-firmware-utvecklarnas egna releaser (`spycemagic/y2-rockbox`). Utvecklarna är ensamma ansvariga för att lista sina programvaruversioner i Updater CE.Varför heter paketet rom_y2.zip?

Utvecklaren namnger Y2 firmware-arkivet `rom_y2.zip` så det kan inte förväxlas med Y1 `rom.zip`.Fungerar Y1 teman på Y2?

Inte alltid. Kontrollera versionskommentarerna för din Y2-byggnad och se [Rockbox-Y2 temaguide](rockbox-y2-themes.html).

## Relaterade guider

### [Rockbox-Y2 nav](rockbox-y2/)

Alla Y2 guider: installation, nedladdningar, teman, återställning, dubbelstart och felsökning.

### [Rockbox-Y1 mot Rockbox-Y2](rockbox-y1-vs-y2.html)

Hur byggnaderna Y1 och Y2 Rockbox skiljer sig åt.

### [Rockbox-Y2-teman](rockbox-y2-themes.html)

Installera och återställa teman på Rockbox-Y2.

### [Rockbox för Y1](rockbox-for-y1_sv.html)

Översikt och installationsguide för Innioasis Y1-porten.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
