---
title: "Sådan gendannes en ikke-opstartende MediaTek-afspiller efter MTK-klientfejl · Innioasis Fællesskab"
description: "Trin-for-trin guide til at fjerne mursten og gendanne ikke-opstartende Innioasis Y1, Y2, G1, Timmkoo og MediaTek spillere efter MTKclient afbrudte flash på Linux eller macOS."
language: "da"
source: "https://innioasis.app/recover-non-booting-device_da.html"
---

# Sådan gendannes en ikke-opstartende MediaTek-afspiller efter MTK-klientfejl · Innioasis Fællesskab

Fejlfinding og enhedsgendannelse

# Gendannelse af en enhed, der ikke starter, efter at MTKclient blinker

Hvis din Innioasis Y1, Y2 eller MediaTek enhed ikke kan tænde eller viser en sort skærm efter at have blinket med MTKclient på macOS eller Linux, skal du ikke gå i panik. Hardware BootROM (BROM) er permanent og kan ikke ødelægges.

## Hvorfor MTKclient muligvis går i stå eller efterlader en sort skærm

MTKclient er afhængig af softwareudnyttelse (kamakiri / amonet) til at omgå DA-godkendelse og rå USB kommunikation via libusb. På macOS og Linux ARM64-systemer:
  - USB håndtryksforsinkelse eller porttimeout på macOS kan stoppe DA-nyttelastinjektion midt i overførslen.
  - Manglende eller ufuldstændige partitionsoverskrifter efterlader bootloaderen (preloader / lk) i en ikke-responsiv tilstand.
  - Afspilleren ser helt død ud - ingen LED, intet opladningsikon, ingen baggrundsbelysning på skærmen.

Selv i denne tilstand falder MediaTek-chipsættet tilbage til BROM-tilstand (USB VID 0e8d, PID 0003), klar til officiel gendannelse på lavt niveau.

## Den endelige gendannelsesmetode: SP Flash Tool Engine i Updater CE

Den sikreste og mest pålidelige måde at gendanne din murede afspiller på er at bruge Opdaterer CE konfigureret med embedsmanden SP Flash Tool backend.

### Præcise trin i Updater CE:
  - Åbn Opdaterer CE.
  - Klik Indstillinger i venstre navigationssidebjælke.
  - Rul ned til sektionen Avanceret og aktiver Vis avancerede indstillinger.
  - Under Installationsmetode (eller Blinkende motor til MediaTek installatør), find Flash metode dropdown.
  - Skift valget fra Auto (anbefales) eller MTKClient til SP Flash Tool.
  - Bekræft prompten og vend tilbage til hovedinstallationsflowet.

## Platformarkitektur og OS-krav til SP Flash Tool

MediaTeks officielle `SP Flash Tool` binær er kompileret indbygget som en x86_64 ELF binær til Linux og en PE32+ eksekverbar til Windows x64.Vigtig hardwarenote til macOS- og ARM64 Linux-brugere:
 Fordi MediaTek ikke kompilerer SP Flash Tool til macOS (Darwin) eller Linux ARM64 (aarch64), skal macOS-brugere og ARM64 Linux-brugere (såsom Raspberry Pi eller Apple Silicon, der kører Asahi Linux), der oplever en klods, forbinde deres afspiller til: 
  - An x64 Windows-pc (Windows 10/11 64-bit), eller
  - An x86_64 Linux-pc (Ubuntu, Debian, Fedora, Arch 64-bit).

## Trin-for-trin proces til at fjerne mursten af hardware
  - Afbryd afspilleren: Tag USB-kablet helt ud af afspilleren og pc'en.
  - Hard Power Off: Hold Power-knappen (eller Power + Volume Down) nede i 15 sekunder for at sikre, at chipsættet er helt slukket og ikke sidder fast i et lavt strømforbrug USB-løkke.
  - Start Updater CE med SP Flash Tool tilstand: Vælg din enhedsmodel (f.eks. Innioasis Y1 eller Innioasis Y2) og vælg Original software for at genoprette lagerpartitioner.
  - Start installation/gendannelse: Klik Installer / Gendan i Updater CE. Vent, indtil statusprompten siger Venter på spiller...
  - Indsæt USB kabel for at udløse BROM: Mens enheden er slukket, skal du tilslutte USB-kablet direkte til en højhastighedsbundkort USB-port (undgå strømløse USB-hubs).
  - Systemet vil registrere MediaTek VCOM-porten, skubbe Download Agent (DA), omskrive partitionstabeller og gendanne alle firmwarebilleder rent.

## Permutationer efter model og operativsystem

| Model | Mislykket platform | Anbefalet genoprettelsesopsætning | Motor og tilstand |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Windows x64 / Linux x86_64 pc | SP Flash Tool + Y1 Aktie ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 eller Windows x64 pc | SP Flash Tool + EF DA |
| Innioasis Y2 | macOS (MTKclient stoppet) | Windows x64 / Linux x86_64 pc | SP Flash Tool + Y2 Scatter-gendannelse |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 pc med VCOM-drivere | SP Flash Tool + Fabriksfirmware |
| Mechen H1 / Timmkoo A5 | Enhver platform | Windows x64 eller Linux x86_64 pc | SP Flash Tool + Scatter-fil |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
