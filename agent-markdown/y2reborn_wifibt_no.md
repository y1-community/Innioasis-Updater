---
title: "Wi-Fi, Bluetooth og FM-radiooppsett for Reborn (Y2Linux) - Innioasis Oppdaterer"
description: "Kort etterinstallasjonsveiledning for Reborn (Y2Linux / Y2Reborn) på Innioasis Y2: kopier system.img, og sett opp Wi-Fi, Bluetooth og FM-radio."
language: "no"
source: "https://innioasis.app/y2reborn_wifibt_no.html"
---

# Wi-Fi, Bluetooth og FM-radiooppsett for Reborn (Y2Linux) - Innioasis Oppdaterer

Innioasis Y2 · Reborn Etterinstallering

# Sett opp Wi-Fi, Bluetooth og FM-radio.

Kopier én fil til spilleren din. Reborn tar seg av resten.[Last ned system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Installasjonsveiledning](guides/reborn-y2linux-y2.html)[Hvorfor Y2Reborn?](reborn-y2linux-benefits_no.html)

## Hvorfor denne filen?

Wi-Fi, Bluetooth og FM-radio trenger fem MediaTek fastvaremoduler som Reborn ikke kan sendes. De er inne i den offisielle Y2 `system.img`. Reborn trekker dem ut én gang, sjekker dem og sletter filen.

## Oppsett
  - Last ned system.img

Last ned v3.2.0 FM `system.img` til datamaskinen din.[ Last ned system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Boot Reborn én gang

Slå på spilleren. Vent på Setter opp lagring for å fullføre, og start den på nytt én gang.
  - Koble til datamaskinen

Bruk en USB datakabel. Spilleren vises som Intern lagring.På en Mac?

Installer [ÅpneMTP](https://openmtp.ganeshrvel.com/) for å bla gjennom spilleren. Windows og Linux monterer den automatisk.
  - Kopier system.img til fastvare

Opprett en mappe kalt `Firmware` ved roten til intern lagring. Kopier `system.img` inn i det.
  - Vent til oppsettet er ferdig

Reborn installerer radiofastvaren automatisk og sletter `system.img`. Dette tar omtrent 10–20 sekunder. Vent på Wi-Fi og Bluetooth er klare.
  - Koble til Wi-Fi, Bluetooth og FM-radio
    - Wi-Fi: Innstillinger → System → Nettverk → Wi-Fi. Velg ditt 2,4 GHz-nettverk.
    - Bluetooth: Sett hodetelefonene i sammenkoblingsmodus. Innstillinger → Bluetooth → velg dem.
    - FM-radio: Koble til kablede hodetelefoner som antenne, og åpne deretter FM-radio.

  - Oppdater over Wi-Fi

Fremtidige Reborn-oppdateringer installeres fra Innstillinger → System → Programvareoppdatering. Radiofastvaren forblir på plass.

## Var denne veiledningen nyttig?

Syntes du denne oppsettsveiledningen etter installasjon var nyttig? Ja, det hjalp! [ Trenger hjelp på Discord ](https://discord.gg/zHrT2zrcek) Takk for tilbakemeldingen! Nyt din trådløse lytting på Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
