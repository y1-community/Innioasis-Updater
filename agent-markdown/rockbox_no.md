---
title: "Slik installerer du Rockbox på Innioasis Y1 eller Y2 - Innioasis Updater"
description: "Installer Rockbox på en Innioasis Y1 eller Y2 med Updater: temaer, stabile utgivelser, Type A og Type B notater, og hvordan du gjenoppretter original programvare etterpå."
language: "no"
source: "https://innioasis.app/rockbox_no.html"
---

# Slik installerer du Rockbox på Innioasis Y1 eller Y2 - Innioasis Updater

Rockbox referanse

# Få Rockbox på Y1 eller Y2

Rockbox endrer spillerprogramvaren og åpner opp et dypere musikkspillergrensesnitt, avspillingskontroller, sortering og temaalternativer. Installasjonen er veiledet, men Y1 og Y2 er separate reiser.[Rockbox på Y1](guides/rockbox-y1.html)[Rockbox på Y2](guides/rockbox-y2.html)[Hvorfor Rockbox?](rockbox-benefits_no.html)

## Hva installasjonen endrer

Rockbox er tilpasset programvare. Det fjerner ikke muligheten til å gå tilbake til lagergrensesnittet når den samsvarende originale programvarepakken er tilgjengelig. Det kan forbedre musikksurfing og tilpasning, men funksjoner, oppløsning, batterilevetid og temakompatibilitet avhenger av konstruksjonen.Ikke bland modeller. Velg Y1 for en Y1-spiller og Y2 for en Y2-spiller. Et utgivelsesnavn som ser lignende ut er ikke nok bevis på at en pakke er kompatibel.

## Se videoen

Video av Frawgeeys. Den viser Innioasis Updater-ruten; bruk de modellspesifikke skriftlige trinnene nedenfor for Y1 eller Y2.

Video av [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (spansk), viser Rockbox på en Y1. Bruk de modellspesifikke trinnene nedenfor for spilleren din.

## Den delte Updater-ruten
  - Installer Updater og koble ingenting før den spør.
  - Velg modellen som er trykt på spilleren i Enhetsmodell.
  - Velg Rockbox inn Programvare.
  - Velg en stabil utgivelse med mindre du bevisst tester en nattlig build.
  - Klikk Installer / Gjenopprett, følg deretter strømmen av og USB tilkoblingsmeldingen.
  - Koble fra først etter suksessmeldingen.

## 240p, 360p og temaer

Eldre Rockbox temasamlinger kan lages for 240p. Y1 fellesskapsbygg bruker også 360p-kompatibilitetsetiketter. Les versjonsnotatene og temakilden før du velger en build. Et tema laget for én oppløsning eller programvarefamilie fungerer kanskje ikke på en annen.[Bla gjennom fellesskapstemaer](https://themes.innioasis.app/?lang=no)[Temaverktøy](https://themes.innioasis.app/?lang=no)

## Gå tilbake til original programvare

Velg samme modell igjen, velg Original programvare, velg en stabil utgivelse og bruk Installer / Gjenopprett. Hvis feilen skjedde før USB-ledeteksten, sjekk datamaskinen og de utpakkede filene. Hvis spilleren ble oppdaget, men blitsen mislyktes, start med [feilsøking](troubleshooting_no.html).[Y1 gjenopprette](guides/restore-original-y1.html)[Y2 gjenopprette](guides/restore-original-y2.html)

## Vanlige spørsmålJeg installerte Rockbox på nytt, og det fikset ingenting.

Å installere Rockbox på nytt skriver den samme builden over de samme filene, så den kan ikke tilbakestille tingene Rockbox beholder på MicroSD. Hvis problemet er en ødelagt innstilling, tema, spilleliste eller database som finnes på kortet, vil ikke reinstallering fjerne det. Den pålitelige tilbakestillingen sletter `.rockbox` mappe fra MicroSD — Rockbox bygger en ny ved neste oppstart.
  - Slå spilleren helt av og fjern MicroSD-kortet, eller koble til spilleren som en USB-stasjon.
  - Vis skjulte filer på datamaskinen din slik at mappen er synlig. Hvordan vise skjulte filerVis punktfiler på datamaskinen dinWindows: i Filutforsker åpne Visning tabulator og huk av Skjulte gjenstander.macOS: i Finder trykk Cmd+Shift+. for å bytte skjulte filer.Linux · GNOME-filer: trykk Ctrl+H, eller åpne menyen og velg Vis skjulte filer.Linux · KDE Dolphin: trykk Ctrl+H, eller bruk Vis → Vis skjulte filer.
  - Slett `.rockbox` mappe fra kortroten.
  - Sett inn kortet igjen og start spilleren. Rockbox gjenskaper mappen med standardinnstillinger.
  - Bruk temaet og innstillingene på nytt. Hvis problemet først kommer tilbake etter et spesifikt tema, er det temaet som er årsaken.

Sletter `.rockbox` avinstallerer ikke Rockbox og berører ikke musikken din – mappen inneholder innstillinger, temaer og cacher, og gjenoppbygges automatisk. Hvis du vil beholde temaene dine, kopierer du mappen ut av `.rockbox` før du sletter den, eller endre navn på mappen til `.rockbox-old` først.Hvorfor kan jeg ikke se .rockbox-mappen på MicroSD?

Mapper hvis navn starter med en prikk er skjult som standard på de fleste datamaskiner. Du trenger ikke å se den for å installere Rockbox — Updater håndterer filene. Hvis du feilsøker og ønsker å slette den, slår du på skjulte filer først. Hvordan vise skjulte filerVis punktfiler på datamaskinen dinWindows: i Filutforsker åpne Visning tabulator og huk av Skjulte gjenstander.macOS: i Finder trykk Cmd+Shift+. for å bytte skjulte filer.Linux · GNOME-filer: trykk Ctrl+H, eller åpne menyen og velg Vis skjulte filer.Linux · KDE Dolphin: trykk Ctrl+H, eller bruk Vis → Vis skjulte filer.Vil sletting av .rockbox tilbakestille temaet og innstillingene mine?

Ja - `.rockbox` inneholder Rockboxs innstillinger, tema, spillelister og hurtigbufrede database. Sletting returnerer Rockbox til en ren standardtilstand. Sikkerhetskopier hele mappen (eller gi den nytt navn til `.rockbox-old`) hvis du kanskje vil ha noe av det tilbake, start spilleren og Rockbox oppretter en ny mappe.

## Flere Rockbox-Y1 og Rockbox-Y2 guider

Utforsk trinnvise veiledninger for installasjon, nedlasting, tema, gjenoppretting og feilsøking Rockbox på begge modellene:[Rockbox-Y1-hub](rockbox-y1/)[Rockbox-Y2-hub](rockbox-y2/)[Rockbox ROM-nedlastinger](rockbox-rom-download_no.html)[Rockbox for Y1](rockbox-for-y1_no.html)[Rockbox for Y2](rockbox-for-y2_no.html)[Rockbox-Y1 vs. Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1-temaer](rockbox-y1-themes.html)[Rockbox-Y2-temaer](rockbox-y2-themes.html)

## Var denne referansen nyttig?

Svaret ditt bidrar til å forbedre denne veiledningen.JaIkke ennå[Fortell oss hvordan vi kan forbedre oss](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
