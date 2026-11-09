---
title: "Een niet-opstartende MediaTek-speler herstellen na een MTKclient-fout · Innioasis Community"
description: "Stapsgewijze handleiding voor het ontkoppelen en herstellen van niet-opstartende Innioasis Y1, Y2, G1, Timmkoo en MediaTek spelers nadat MTKclient flashes op Linux of macOS heeft onderbroken."
language: "nl"
source: "https://innioasis.app/recover-non-booting-device_nl.html"
---

# Een niet-opstartende MediaTek-speler herstellen na een MTKclient-fout · Innioasis Community

Probleemoplossing en apparaatherstel

# Een niet-opstartapparaat herstellen na MTKclient-flashen

Als uw Innioasis Y1-, Y2- of MediaTek-apparaat niet kan worden ingeschakeld of een zwart scherm wordt weergegeven na het flashen met MTKclient op macOS of Linux, raak dan niet in paniek. De hardware BootROM (BROM) is permanent en kan niet worden vernietigd.

## Waarom MTKclient vastloopt of een zwart scherm achterlaat

MTKclient vertrouwt op software-exploit-payloads (kamakiri / amonet) om DA-authenticatie en onbewerkte USB-communicatie via libusb te omzeilen. Op macOS- en Linux ARM64-systemen:
  - USB Handshakelatentie of poorttime-outs op macOS kunnen de injectie van DA-payload halverwege de overdracht vertragen.
  - Ontbrekende of onvolledige partitieheaders zorgen ervoor dat de bootloader (preloader / lk) niet reageert.
  - De speler lijkt volledig dood: geen LED, geen oplaadpictogram, geen schermverlichting.

Zelfs in deze staat valt de MediaTek-chipset terug BROM-modus (USB VID 0e8d, PID 0003), klaar voor officieel herstel op laag niveau.

## De definitieve herstelmethode: SP Flash Tool Engine in Updater CE

De veiligste en meest betrouwbare manier om uw gemetselde speler te herstellen is door gebruik te maken van Updater CE geconfigureerd met de ambtenaar SP Flash Tool backend.

### Exacte stappen in Updater CE:
  - Openen Updater CE.
  - Klik Instellingen in de linker navigatiezijbalk.
  - Blader omlaag naar het gedeelte Geavanceerd en schakel in Toon geavanceerde instellingen.
  - Onder Installatiemethode (of Knipperende engine voor MediaTek installatieprogramma), zoek de Flash-methode vervolgkeuzelijst.
  - Wijzig de selectie van Automatisch (aanbevolen) of MTKClient aan SP Flash Tool.
  - Bevestig de vraag en keer terug naar de hoofdinstallatiestroom.

## Platformarchitectuur en besturingssysteemvereisten voor SP Flash Tool

De ambtenaar van MediaTek `SP Flash Tool` binary wordt native gecompileerd als een x86_64 ELF binair voor Linux en een PE32+ uitvoerbaar bestand voor Windows x64.Belangrijke hardware-opmerking voor macOS- en ARM64 Linux-gebruikers:
 Omdat MediaTek SP Flash Tool niet compileert voor macOS (Darwin) of Linux ARM64 (aarch64), moeten macOS-gebruikers en ARM64 Linux-gebruikers (zoals Raspberry Pi of Apple Silicon met Asahi Linux) die een brick ervaren, hun speler verbinden met: 
  - Een x64 Windows-pc (Windows 10/11 64-bit), of
  - Een x86_64 Linux-pc (Ubuntu, Debian, Fedora, Arch 64-bit).

## Stapsgewijs proces voor het ontkoppelen van hardware
  - Koppel de speler los: Koppel de USB-kabel volledig los van de speler en de pc.
  - Harde uitschakeling: Houd de aan/uit-knop (of aan/uit + volume omlaag) 15 seconden ingedrukt om er zeker van te zijn dat de chipset volledig is uitgeschakeld en niet vastzit in een USB-lus met laag vermogen.
  - Start Updater CE met SP Flash Tool-modus: Selecteer uw apparaatmodel (bijv. Innioasis Y1 of Innioasis Y2) en kies Originele software om voorraadpartities te herstellen.
  - Start installatie / herstel: Klik Installeren / Herstellen in Updater CE. Wacht tot de statusprompt dit zegt Wachten op speler...
  - Steek USB kabel in om BROM te activeren: Terwijl het apparaat UIT staat, sluit u de USB-kabel rechtstreeks aan op een snelle moederbord-USB-poort (vermijd niet-aangedreven USB-hubs).
  - Het systeem zal de VCOM-poort MediaTek detecteren, de Download Agent (DA) pushen, partitietabellen herschrijven en alle firmware-images netjes herstellen.

## Permutaties per model en besturingssysteem

| Model | Mislukt platform | Aanbevolen herstelconfiguratie | Motor en modus |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon/Intel) | Windows x64 / Linux x86_64-pc | SP Flash Tool + Y1 Voorraad ROM |
| Innioasis Y1 | LinuxARM64/x86_64 | Linux x86_64 of Windows x64-pc | SP Flash Tool + Community-DA |
| Innioasis Y2 | macOS (MTKclient vastgelopen) | Windows x64 / Linux x86_64-pc | SP Flash Tool + Y2 Verspreidingsherstel |
| Innioasis G1 / G3 / G5 | macOS / Linux MTK-client | Windows x64-pc met VCOM-stuurprogramma's | SP Flash Tool + Fabrieksfirmware |
| Mechen H1 / Timmkoo A5 | Elk platform | Windows x64 of Linux x86_64 pc | SP Flash Tool + Scatterbestand |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
