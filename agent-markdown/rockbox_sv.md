---
title: "Så här installerar du Rockbox på din Innioasis Y1 eller Y2 - Innioasis Updater"
description: "Installera Rockbox på en Innioasis Y1 eller Y2 med Updater: teman, stabila utgåvor, Type A och Type B anteckningar och hur man återställer originalprogramvaran efter."
language: "sv"
source: "https://innioasis.app/rockbox_sv.html"
---

# Så här installerar du Rockbox på din Innioasis Y1 eller Y2 - Innioasis Updater

Rockbox referens

# Få Rockbox på din Y1 eller Y2

Rockbox ändrar spelarens programvara och öppnar upp ett djupare gränssnitt för musikspelare, uppspelningskontroller, sortering och temaalternativ. Installationen är guidad, men Y1 och Y2 är separata resor.[Rockbox på Y1](guides/rockbox-y1.html)[Rockbox på Y2](guides/rockbox-y2.html)[Varför Rockbox?](rockbox-benefits_sv.html)

## Vad installationen ändrar

Rockbox är anpassad programvara. Det tar inte bort din möjlighet att återgå till lagergränssnittet när det matchande originalprogramvarupaketet är tillgängligt. Det kan förbättra musiksökning och anpassning, men funktioner, upplösning, batteritid och temakompatibilitet beror på konstruktionen.Blanda inte modeller. Välj Y1 för en Y1-spelare och Y2 för en Y2-spelare. Ett releasenamn som ser liknande ut är inte tillräckligt som bevis för att ett paket är kompatibelt.

## Se videon

Video av Frawgeeys. Den visar Innioasis Updater-rutten; använd de modellspecifika skrivna stegen nedan för din Y1 eller Y2.

Video av [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (spanska), visar Rockbox på en Y1. Använd de modellspecifika stegen nedan för din spelare.

## Den delade Updater-rutten
  - Installera Updater och anslut ingenting tills den frågar.
  - Välj den modell som är tryckt på spelaren i Enhetsmodell.
  - Välj Rockbox i Programvara.
  - Välj en stabil version såvida du inte medvetet testar en nattlig konstruktion.
  - Klicka Installera / Återställ, följ sedan avstängning och USB anslutningsprompten.
  - Koppla från endast efter framgångsmeddelandet.

## 240p, 360p och teman

Äldre Rockbox temasamlingar kan göras för 240p. Y1 gemenskapsbyggen använder också 360p-kompatibilitetsetiketter. Läs versionskommentarerna och temakällan innan du väljer ett bygge. Ett tema gjort för en upplösning eller programvarufamilj kanske inte fungerar på en annan.[Bläddra bland gemenskapsteman](https://themes.innioasis.app/?lang=sv)[Temaverktyg](https://themes.innioasis.app/?lang=sv)

## Återgå till originalprogramvaran

Välj samma modell igen, välj Originalprogramvara, välj en stabil version och använd Installera / Återställ. Om felet inträffade före USB-prompten kontrollerar du datorn och de extraherade filerna. Om spelaren upptäcktes men blixten misslyckades, börja med [felsökning](troubleshooting_sv.html).[Y1 återställa](guides/restore-original-y1.html)[Y2 återställa](guides/restore-original-y2.html)

## Vanliga frågorJag installerade om Rockbox och det fixade ingenting.

Om du installerar om Rockbox skrivs samma build över samma filer, så det kan inte återställa de saker som Rockbox har kvar på MicroSD. Om problemet är en trasig inställning, tema, spellista eller databas som finns på kortet, kommer ominstallation inte att lösa det. Den pålitliga återställningen tar bort `.rockbox` mapp från MicroSD — Rockbox bygger en ny vid nästa uppstart.
  - Stäng av spelaren helt och ta bort MicroSD-kortet, eller anslut spelaren som en USB-enhet.
  - Visa dolda filer på din dator så att mappen är synlig. Hur man visar dolda filerVisa dotfiler på din datorWindows: i File Explorer öppnar du Visa tabb och bock Dolda föremål.macOS: i Finder press Cmd+Shift+. för att växla dolda filer.Linux · GNOME-filer: tryck Ctrl+H, eller öppna menyn och välj Visa dolda filer.Linux · KDE Dolphin: tryck Ctrl+H, eller använd Visa → Visa dolda filer.
  - Ta bort `.rockbox` mapp från kortroten.
  - Sätt tillbaka kortet och starta spelaren. Rockbox återskapar mappen med standardinställningar.
  - Använd ditt tema och dina inställningar igen. Om problemet bara kommer tillbaka efter ett specifikt tema är det temat som är orsaken.

Tar bort `.rockbox` avinstallerar inte Rockbox och rör inte din musik – mappen innehåller inställningar, teman och cacheminne och byggs om automatiskt. Om du vill behålla dina teman, kopiera mappen ur `.rockbox` innan du tar bort den, eller byt namn på mappen till `.rockbox-old` först.Varför kan jag inte se .rockbox-mappen på min MicroSD?

Mappar vars namn börjar med en punkt är dolda som standard på de flesta datorer. Du behöver inte se den för att installera Rockbox — Updater hanterar filerna. Om du felsöker och vill ta bort det, aktivera dolda filer först. Hur man visar dolda filerVisa dotfiler på din datorWindows: i File Explorer öppnar du Visa tabb och bock Dolda föremål.macOS: i Finder press Cmd+Shift+. för att växla dolda filer.Linux · GNOME-filer: tryck Ctrl+H, eller öppna menyn och välj Visa dolda filer.Linux · KDE Dolphin: tryck Ctrl+H, eller använd Visa → Visa dolda filer.Kommer mitt tema och inställningar att återställas om jag raderar .rockbox?

Ja — `.rockbox` innehåller Rockboxs inställningar, tema, spellistor och cachad databas. Om du raderar den återgår Rockbox till ett rent standardläge. Säkerhetskopiera hela mappen (eller byt namn på den till `.rockbox-old`) om du kanske vill ha tillbaka något av det, starta sedan spelaren och Rockbox skapar en ny mapp.

## Fler Rockbox-Y1 och Rockbox-Y2 guider

Utforska steg-för-steg-guider för installation, nedladdning, tema, återställning och felsökning Rockbox på båda modellerna:[Rockbox-Y1 nav](rockbox-y1/)[Rockbox-Y2 nav](rockbox-y2/)[Rockbox ROM-nedladdningar](rockbox-rom-download_sv.html)[Rockbox för Y1](rockbox-for-y1_sv.html)[Rockbox för Y2](rockbox-for-y2_sv.html)[Rockbox-Y1 mot Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1-teman](rockbox-y1-themes.html)[Rockbox-Y2-teman](rockbox-y2-themes.html)

## Var denna referens användbar?

Ditt svar hjälper till att förbättra den här guiden.JaInte än[Låt oss veta hur vi kan förbättra](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
