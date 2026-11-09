---
title: "Sådan installeres Rockbox på din Innioasis Y1 eller Y2 - Innioasis Updater"
description: "Installer Rockbox på en Innioasis Y1 eller Y2 med Updater: temaer, stabile udgivelser, Type A og Type B noter, og hvordan man gendanner original software efter."
language: "da"
source: "https://innioasis.app/rockbox_da.html"
---

# Sådan installeres Rockbox på din Innioasis Y1 eller Y2 - Innioasis Updater

Rockbox reference

# Få Rockbox på din Y1 eller Y2

Rockbox ændrer afspillersoftwaren og åbner en dybere musikafspillergrænseflade, afspilningskontroller, sortering og temaindstillinger. Installationen er guidet, men Y1 og Y2 er separate rejser.[Rockbox på Y1](guides/rockbox-y1.html)[Rockbox på Y2](guides/rockbox-y2.html)[Hvorfor Rockbox?](rockbox-benefits_da.html)

## Hvad installationen ændrer

Rockbox er brugerdefineret software. Det fjerner ikke din mulighed for at vende tilbage til lagergrænsefladen, når den matchende originale softwarepakke er tilgængelig. Det kan forbedre gennemsyn og tilpasning af musik, men funktioner, opløsning, batterilevetid og temakompatibilitet afhænger af bygningen.Bland ikke modeller. Vælg Y1 for en Y1-afspiller og Y2 for en Y2-afspiller. Et udgivelsesnavn med lignende udseende er ikke nok bevis for, at en pakke er kompatibel.

## Se videoen

Video af Frawgeeys. Den viser Innioasis Updater-ruten; brug de modelspecifikke skriftlige trin nedenfor for din Y1 eller Y2.

Video af [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (spansk), viser Rockbox på en Y1. Brug de modelspecifikke trin nedenfor for din afspiller.

## Den delte Updater-rute
  - Installer Updater og tilslut intet, før det spørger.
  - Vælg den model, der er trykt på afspilleren i Enhedsmodel.
  - Vælg Rockbox ind Software.
  - Vælg en stabil udgivelse, medmindre du bevidst tester en natlig build.
  - Klik Installer / Gendan, og følg derefter sluk- og USB-forbindelsesprompten.
  - Afbryd først forbindelsen efter succesmeddelelsen.

## 240p, 360p og temaer

Ældre Rockbox temasamlinger kan laves til 240p. Y1 community builds bruger også 360p-kompatibilitetsetiketter. Læs udgivelsesbemærkningerne og temakilden, før du vælger en build. Et tema lavet til én opløsning eller softwarefamilie fungerer muligvis ikke på en anden.[Gennemse fællesskabstemaer](https://themes.innioasis.app/?lang=da)[Temaværktøjer](https://themes.innioasis.app/?lang=da)

## Tilbage til original software

Vælg den samme model igen, vælg Original software, vælg en stabil udgivelse, og brug Installer / Gendan. Hvis fejlen skete før USB-prompten, skal du kontrollere computeren og de udpakkede filer. Hvis afspilleren blev registreret, men flashen mislykkedes, skal du starte med [fejlfinding](troubleshooting_da.html).[Y1 gendan](guides/restore-original-y1.html)[Y2 gendan](guides/restore-original-y2.html)

## Ofte stillede spørgsmålJeg geninstallerede Rockbox, og det rettede ikke noget.

Geninstallering af Rockbox skriver den samme build over de samme filer, så det kan ikke nulstille de ting, Rockbox beholder på MicroSD. Hvis problemet er en ødelagt indstilling, et tema, en afspilningsliste eller en database, der findes på kortet, vil geninstallation ikke fjerne det. Den pålidelige nulstilling sletter `.rockbox` mappe fra MicroSD — Rockbox bygger en ny ved næste boot.
  - Sluk for afspilleren helt, og fjern MicroSD-kortet, eller tilslut afspilleren som et USB-drev.
  - Vis skjulte filer på din computer, så mappen er synlig. Sådan viser du skjulte filerVis dotfiler på din computerWindows: i File Explorer åbner Visning tabulator og flueben Skjulte genstande.macOS: i Finder tryk Cmd+Shift+. for at skifte skjulte filer.Linux · GNOME-filer: tryk Ctrl+H, eller åbn menuen og vælg Vis skjulte filer.Linux · KDE Dolphin: tryk Ctrl+H, eller brug Vis → Vis skjulte filer.
  - Slet `.rockbox` mappe fra kortets rod.
  - Indsæt kortet igen og start afspilleren. Rockbox genskaber mappen med standardindstillinger.
  - Anvend dit tema og dine indstillinger igen. Hvis problemet først kommer tilbage efter et bestemt tema, er det dette tema, der er årsagen.

Sletter `.rockbox` afinstallerer ikke Rockbox og rører ikke din musik - mappen indeholder indstillinger, temaer og caches og genopbygges automatisk. Hvis du vil beholde dine temaer, skal du kopiere mappen ud af `.rockbox` før du sletter den, eller omdøb mappen til `.rockbox-old` først.Hvorfor kan jeg ikke se .rockbox-mappen på min MicroSD?

Mapper, hvis navn starter med en prik, er som standard skjult på de fleste computere. Du behøver ikke se det for at installere Rockbox — Updater håndterer filerne. Hvis du fejlfinder og vil slette det, skal du først slå skjulte filer til. Sådan viser du skjulte filerVis dotfiler på din computerWindows: i File Explorer åbner Visning tabulator og flueben Skjulte genstande.macOS: i Finder tryk Cmd+Shift+. for at skifte skjulte filer.Linux · GNOME-filer: tryk Ctrl+H, eller åbn menuen og vælg Vis skjulte filer.Linux · KDE Dolphin: tryk Ctrl+H, eller brug Vis → Vis skjulte filer.Vil sletning af .rockbox nulstille mit tema og mine indstillinger?

Ja - `.rockbox` indeholder Rockboxs indstillinger, tema, afspilningslister og cachelagrede database. Sletning returnerer Rockbox til en ren standardtilstand. Sikkerhedskopier hele mappen (eller omdøb den til `.rockbox-old`) hvis du måske vil have noget af det tilbage, så start afspilleren og Rockbox opretter en ny mappe.

## Flere Rockbox-Y1 og Rockbox-Y2 guider

Udforsk trin-for-trin guider til installation, download, tematisering, gendannelse og fejlfinding Rockbox på begge modeller:[Rockbox-Y1 hub](rockbox-y1/)[Rockbox-Y2 hub](rockbox-y2/)[Rockbox ROM-downloads](rockbox-rom-download_da.html)[Rockbox for Y1](rockbox-for-y1_da.html)[Rockbox for Y2](rockbox-for-y2_da.html)[Rockbox-Y1 vs. Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 temaer](rockbox-y1-themes.html)[Rockbox-Y2 temaer](rockbox-y2-themes.html)

## Var denne reference nyttig?

Dit svar hjælper med at forbedre denne vejledning.JaIkke endnu[Fortæl os, hvordan vi kan forbedre os](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
