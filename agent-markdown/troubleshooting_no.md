---
title: "Innioasis Feilsøking for oppdatering | Installasjonsproblemer Innioasis og Timmkoo - Innioasis Oppdaterer"
description: "Fiks Innioasis Updater-installasjoner på hvilken som helst Innioasis- eller Timmkoo-spiller. Sjekk modellen, kabelen, driveren, tidspunktet for avslåing og hvor installasjonen stoppet - og få den til å blinke igjen."
language: "no"
source: "https://innioasis.app/troubleshooting_no.html"
---

# Innioasis Feilsøking for oppdatering | Installasjonsproblemer Innioasis og Timmkoo - Innioasis Oppdaterer

Feilsøking

# Finn punktet der installasjonen stoppet.

Hvor stoppet det? Det forteller deg hva du skal fikse.[Gå tilbake til den vanlige veiledningen](guide_no.html)[Sjekk fastvaren](firmware_no.html)

## Den stoppet før USB-meldingen

Dette er et dataproblem, ikke et kabelproblem. Sjekk modellen din. Pakk ut filen igjen. Så prøv Installer / Gjenopprett. Hvis utgivelseslisten er tom, åpner du [fastvarekatalog](firmware_no.html).

## Den kan ikke kobles til spilleren
  - Slå av riktig Y1 eller Y2 helt.
  - Koble fra kabelen, lukk andre flash- eller Android-verktøy, og start installasjonen på nytt.
  - Koble bare til når Updater sier at den er klar.
  - Bruk en kort USB datakabel direkte i datamaskinen, ikke en hub hvis mulig.
  - På Windows, installer MediaTek-driveren på nytt og start på nytt. På Linux, sjekk USB/serietillatelser.
Oppdaterer-tilkoblingsforespørselLive Updater-forespørselen er autoritativ for gjeldende modell og plattform.

## Den oppdaget spilleren, men blitsen mislyktes

Stopp her. Ikke prøv en annen modell. Lukk andre verktøy, sjekk at du valgte riktig Y1 eller Y2, og bruk den tilhørende originalprogramvaren hvis spilleren ikke vil starte. [SP Flash Tool](sp-flash-tool_no.html) og MTKClient er inkludert hvis du trenger dem, og filene er på [firmware side](firmware_no.html).

## Windows-drivermerknader

Noen Windows-installasjoner blokkerer MediaTek-driveren på grunn av kjerneisolasjon. Følg gjeldende Windows-sikkerhetsveiledning før du endrer minneintegritet, og slå den på igjen når du er ferdig hvis systemet tillater det.[Åpne førerveiledningen](drivers_no.html)[Ren installasjonsveiledning](Troubleshooting/clean_install.html)

## Hjulet fungerer ikke, eller spilleren starter ikke

Inngangs- og strømfeil trenger forskjellige trinn enn et mislykket blits. Disse veiledningene dekker de vanlige Y1 og Y2 tilfellene.[Y1 rullehjul](guides/y1-scroll-wheel-not-working.html)[Y2 rullehjul](guides/y2-scroll-wheel-not-working.html)[Y1 vil ikke slå seg på](guides/y1-wont-turn-on.html)[Y2 vil ikke slå seg på](guides/y2-wont-turn-on.html)[Gjenopprettingsguide](guides/recovery.html)

## Fortsatt fast?

Når du ber om hjelp, ta med modellen, operativsystemet, den nøyaktige oppdateringsmeldingen, om spilleren ble oppdaget og pakken/prosjektet du valgte. Ikke legg ut private tokens eller urelaterte systemfiler.[Be om hjelp](https://discord.gg/zHrT2zrcek)[Støtte vedlikehold](support_devs_no.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
