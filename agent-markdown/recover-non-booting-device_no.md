---
title: "Hvordan gjenopprette en ikke-oppstartende MediaTek-spiller etter MTK-klientfeil · Innioasis fellesskap"
description: "Trinn-for-trinn veiledning for å fjerne murstein og gjenopprette ikke-oppstartende Innioasis Y1, Y2, G1, Timmkoo og MediaTek spillere etter MTKclient avbrutt flash på Linux eller macOS."
language: "no"
source: "https://innioasis.app/recover-non-booting-device_no.html"
---

# Hvordan gjenopprette en ikke-oppstartende MediaTek-spiller etter MTK-klientfeil · Innioasis fellesskap

Feilsøking og enhetsgjenoppretting

# Gjenopprette en enhet som ikke starter etter at MTKclient blinker

Hvis enheten Innioasis Y1, Y2 eller MediaTek ikke slår seg på eller viser en svart skjerm etter å ha blinket med MTKclient på macOS eller Linux, ikke få panikk. Maskinvaren BootROM (BROM) er permanent og kan ikke ødelegges.

## Hvorfor MTKclient kan stoppe eller la en svart skjerm

MTKclient er avhengig av programvareutnyttelse (kamakiri / amonet) for å omgå DA-autentisering og rå USB kommunikasjon via libusb. På macOS og Linux ARM64-systemer:
  - USB ventetid for håndtrykk eller porttidsavbrudd på macOS kan stoppe DA-nyttelastinjeksjon midt i overføringen.
  - Manglende eller ufullstendige partisjonshoder forlater oppstartslasteren (preloader / lk) i en ikke-responsiv tilstand.
  - Spilleren ser helt død ut – ingen LED, ingen ladeikon, ingen bakgrunnsbelysning på skjermen.

Selv i denne tilstanden faller MediaTek-brikkesettet tilbake til BROM-modus (USB VID 0e8d, PID 0003), klar for offisiell gjenoppretting på lavt nivå.

## Den endelige gjenopprettingsmetoden: SP Flash Tool Engine i Updater CE

Den sikreste og mest pålitelige måten å gjenopprette den murede spilleren er å bruke Oppdaterer CE konfigurert med den offisielle SP Flash Tool backend.

### Nøyaktige trinn i Updater CE:
  - Åpne Oppdaterer CE.
  - Klikk Innstillinger i venstre navigasjonssidefelt.
  - Rull ned til Avansert-delen og aktiver Vis avanserte innstillinger.
  - Under Installasjonsmetode (eller Blinkende motor for MediaTek installatør), finn Flash-metode rullegardinmenyen.
  - Endre utvalget fra Auto (anbefalt) eller MTKClient til SP Flash Tool.
  - Bekreft forespørselen og gå tilbake til hovedinstallasjonsflyten.

## Plattformarkitektur og OS-krav for SP Flash Tool

MediaTek sin offisielle `SP Flash Tool` binær er kompilert naturlig som en x86_64 ELF binær for Linux og a PE32+ kjørbar for Windows x64.Viktig maskinvaremerknad for macOS- og ARM64 Linux-brukere:
 Fordi MediaTek ikke kompilerer SP Flash Tool for macOS (Darwin) eller Linux ARM64 (aarch64), må macOS-brukere og ARM64 Linux-brukere (som Raspberry Pi eller Apple Silicon som kjører Asahi Linux) som opplever en kloss koble spilleren til: 
  - An x64 Windows PC (Windows 10 / 11 64-bit), eller
  - An x86_64 Linux PC (Ubuntu, Debian, Fedora, Arch 64-bit).

## Trinn-for-trinn prosess for fjerning av maskinvare
  - Koble fra spilleren: Koble USB-kabelen helt fra spilleren og PC-en.
  - Hard Power Off: Hold Power-knappen (eller Power + Volum ned) i 15 sekunder for å sikre at brikkesettet er helt slått av og ikke sitter fast i en USB-sløyfe med lavt strømforbruk.
  - Start Updater CE med SP Flash Tool-modus: Velg enhetsmodellen din (f.eks. Innioasis Y1 eller Innioasis Y2) og velg Original programvare for å gjenopprette lagerpartisjoner.
  - Start installasjon/gjenoppretting: Klikk Installer / Gjenopprett i Updater CE. Vent til statusmeldingen sier Venter på spiller...
  - Sett inn USB kabel for å utløse BROM: Mens enheten er AV, kobler du USB-kabelen direkte til en høyhastighets hovedkortport USB (unngå strømløse USB-huber).
  - Systemet vil oppdage MediaTek VCOM-porten, skyve nedlastingsagenten (DA), omskrive partisjonstabeller og gjenopprette alle fastvarebilder rent.

## Permutasjoner etter modell og operativsystem

| Modell | Mislykket plattform | Anbefalt gjenopprettingsoppsett | Motor og modus |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y1 Aksje ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 eller Windows x64 PC | SP Flash Tool + Community DA |
| Innioasis Y2 | macOS (MTKclient stoppet) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y2 Scatter-gjenoppretting |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 PC med VCOM-drivere | SP Flash Tool + Fabrikkfastvare |
| Mechen H1 / Timmkoo A5 | Enhver plattform | Windows x64 eller Linux x86_64 PC | SP Flash Tool + Scatter-fil |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
