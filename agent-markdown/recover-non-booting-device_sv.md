---
title: "Hur man återställer en icke-startande MediaTek spelare efter MTK-klientfel · Innioasis Community"
description: "Steg-för-steg-guide för att ta upp och återställa icke-startande Innioasis Y1, Y2, G1, Timmkoo och MediaTek spelare efter att MTKclient avbrutna flashar på Linux eller macOS."
language: "sv"
source: "https://innioasis.app/recover-non-booting-device_sv.html"
---

# Hur man återställer en icke-startande MediaTek spelare efter MTK-klientfel · Innioasis Community

Felsökning och enhetsåterställning

# Återställa en enhet som inte startar efter att MTKclient blinkar

Om din Innioasis Y1, Y2 eller MediaTek enhet inte kan slås på eller visar en svart skärm efter att ha blinkat med MTKclient på macOS eller Linux, få inte panik. Maskinvarans BootROM (BROM) är permanent och kan inte förstöras.

## Varför MTKclient kan stanna eller lämna en svart skärm

MTKclient förlitar sig på mjukvaruexploateringsnyttolaster (kamakiri/amonet) för att kringgå DA-autentisering och rå USB-kommunikation via libusb. På macOS och Linux ARM64-system:
  - USB handskakningslatens eller porttimeout på macOS kan stoppa DA-nyttolastinjektion mitt i överföringen.
  - Saknade eller ofullständiga partitionsrubriker lämnar starthanteraren (preloader / lk) i ett icke-responsivt tillstånd.
  - Spelaren verkar helt död – ingen LED, ingen laddningsikon, ingen bakgrundsbelysning på skärmen.

Även i detta tillstånd faller MediaTek-kretsuppsättningen tillbaka till BROM-läge (USB VID 0e8d, PID 0003), redo för officiell återställning på låg nivå.

## Den definitiva återställningsmetoden: SP Flash Tool Engine i Updater CE

Det säkraste och mest pålitliga sättet att återställa din spelare är att använda Uppdaterare CE konfigurerad med tjänstemannen SP Flash Tool backend.

### Exakta steg i Updater CE:
  - Öppna Uppdaterare CE.
  - Klicka Inställningar i sidofältet till vänster.
  - Rulla ned till avsnittet Avancerat och aktivera Visa avancerade inställningar.
  - Under Installationsmetod (eller Blinkande motor för MediaTek installatör), lokalisera Flash-metod rullgardinsmenyn.
  - Ändra urvalet från Auto (rekommenderas) eller MTKClient till SP Flash Tool.
  - Bekräfta uppmaningen och återgå till huvudinstallationsflödet.

## Plattformsarkitektur och OS-krav för SP Flash Tool

MediaTeks tjänsteman `SP Flash Tool` binär kompileras inbyggt som en x86_64 ELF binär för Linux och a PE32+ körbar för Windows x64.Viktig maskinvaruanmärkning för macOS- och ARM64 Linux-användare:
 Eftersom MediaTek inte kompilerar SP Flash Tool för macOS (Darwin) eller Linux ARM64 (aarch64), måste macOS-användare och ARM64 Linux-användare (som Raspberry Pi eller Apple Silicon som kör Asahi Linux) som upplever en kloss ansluta sin spelare till: 
  - En x64 Windows PC (Windows 10/11 64-bitars), eller
  - En x86_64 Linux PC (Ubuntu, Debian, Fedora, Arch 64-bitars).

## Steg-för-steg process för att lossa hårdvara
  - Koppla bort spelaren: Koppla bort USB-kabeln från spelaren och datorn helt.
  - Hård avstängning: Håll Power-knappen (eller Power + Volym ned) i 15 sekunder för att säkerställa att chipsetet är helt avstängt och inte fastnat i en slinga med låg effekt USB.
  - Starta Updater CE med SP Flash Tool läge: Välj din enhetsmodell (t.ex. Innioasis Y1 eller Innioasis Y2) och välj Originalprogramvara för att återställa lagerpartitioner.
  - Initiera installation/återställning: Klicka Installera / Återställ i Updater CE. Vänta tills statusprompten säger Väntar på spelare...
  - Sätt i USB kabel för att trigga BROM: Medan enheten är AV, anslut USB-kabeln direkt till en höghastighetsmoderkortsport USB (undvik strömlösa USB-hubbar).
  - Systemet kommer att upptäcka MediaTek VCOM-porten, trycka på Download Agent (DA), skriva om partitionstabeller och återställa alla firmware-bilder rent.

## Permutationer efter modell och operativsystem

| Modell | Misslyckad plattform | Rekommenderad återställningsinställning | Motor & läge |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y1 Aktie ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 eller Windows x64 PC | SP Flash Tool + Community DA |
| Innioasis Y2 | macOS (MTKclient avstannat) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y2 Scatter-återställning |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 PC med VCOM-drivrutiner | SP Flash Tool + Fabriksfirmware |
| Mechen H1 / Timmkoo A5 | Vilken plattform som helst | Windows x64 eller Linux x86_64 PC | SP Flash Tool + Scatter-fil |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
