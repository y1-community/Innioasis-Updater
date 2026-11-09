---
title: "Rockbox for Y2 (Rockbox-Y2): oversikt, bygg og installasjonsveiledning"
description: "Rockbox for Y2, Rockbox-Y2 og rockbox-y2 refererer til fellesskapets Rockbox fastvareport for Innioasis Y2. Finn ut hva den inkluderer og hvordan du installerer den med Innioasis Updater CE."
language: "no"
source: "https://innioasis.app/rockbox-for-y2_no.html"
---

# Rockbox for Y2 (Rockbox-Y2): oversikt, bygg og installasjonsveiledning

[← Fastvarenedlastinger](firmware_no.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox for Y2 (Rockbox-Y2)

Rockbox-Y2 (også kalt “Rockbox for Y2”) er den dedikerte fellesskapet Rockbox fastvareporten for Innioasis Y2. Den bruker sin egen ROM-pakke (`rom_y2.zip`) og installeres direkte gjennom Innioasis Updater CE.[Installer Rockbox-Y2](rockbox-y2/install.html)[Last ned ROM](rockbox-y2/download.html)[Skriftlig veiledning](guides/rockbox-y2.html)[Rockbox-Y2-hub](rockbox-y2/)

## Bygget spesielt for Innioasis Y2

I Innioasis Updater CE er denne fastvaren oppført som Rockbox når Y2 er valgt. Utgivelsene er publisert av [spycemagic/y2-rockbox](firmware_no.html?model=Y2&software=rockbox-y2) prosjekt med pakkenavnet `rom_y2.zip`.

Installer aldri en Y1 fastvarepakke på en Y2. Velger Y2 i Updater CE filtrerer utgivelseslisten automatisk til kun Y2-kompatible bygg.

## Hva Rockbox-Y2 tilbyr
  - Tag-basert musikkbibliotek – bla gjennom album, artister og sjangere fra lydfiltaggene dine, eller bla direkte gjennom mapper.
  - Avspillingskontroller — innstillinger for avspilling uten gap, crossfade, ReplayGain og equalizer.
  - Egendefinerte temaer – installer temaer som er kompatible med din Rockbox-Y2 build ([Y2 temaguide](rockbox-y2-themes.html)).
  - 100 % offline — spiller av lokale filer fra MicroSD-kortet ditt uten kontoer eller abonnementer.
  - Enkel fabrikkgjenoppretting — gå tilbake til Y2 Original Software når som helst i Updater CE.

## Velge en Rockbox-Y2 utgivelse
  - Velg alltid Y2 inn Enhetsmodell først.
  - Velg den nyeste utgivelsen med mindre du tester en spesifikk versjon.
  - Les [Rockbox-Y2 versjonsnotater](release-notes/rockbox-y2/index_no.html) for å se hva som endret seg i hvert bygg.

## Direkte nedlastinger fra fellesskapsutviklerne

Innioasis Updater CE laster alltid ned fastvarepakker direkte fra fellesskapets fastvareutviklere ([spycemagic/y2-rockbox](firmware_no.html?model=Y2&software=rockbox-y2)), og disse utviklerne er eneansvarlige for å føre opp programvareutgivelsene deres i Updater CE.

Du kan la Updater CE laste ned og flashe `rom_y2.zip` automatisk, eller last ned pakken fra vår [Rockbox-Y2 nedlastingsside](rockbox-y2/download.html) og [Rockbox ROM nedlastingsside](rockbox-rom-download_no.html).[Rockbox-Y2 nedlastinger](rockbox-y2/download.html)[Installer fra en lokal ZIP](rockbox-y2/portable-zip.html)

## Hvordan installere Rockbox-Y2
  - Åpne Innioasis Updater CE og still inn Enhetsmodell til Y2.
  - Velg Rockbox inn Programvare.
  - Velg en Y2 utgivelse fra listen.
  - Klikk Installer / Gjenopprett så Updater CE laster ned pakken direkte fra utvikleren.
  - Slå Y2 helt av og koble den til med en USB datakabel når Updater CE spør.
  - Vent på fullføringsmeldingen, koble fra og slå på Y2.

For hele trinn-for-trinn-gjennomgangen, les [Rockbox-Y2 veiledning](guides/rockbox-y2.html).

## Gjenoppretter den originale Y2-programvaren

For å gå tilbake til fabrikkfastvare, velg Y2 og Original programvare i Updater CE, velg en stabil utgivelse og klikk Installer / Gjenopprett. Se [gjenopprettingsveiledning](rockbox-y2/restore-stock.html) og [Y2 Original programvareside](original-software-y2_no.html).

## Ofte stilte spørsmålHvor laster Updater CE ned Rockbox-Y2 fra?

Updater CE laster alltid ned fastvarepakker direkte fra fellesskapsfastvareutviklernes egne utgivelser (`spycemagic/y2-rockbox`). Utviklerne er alene ansvarlige for å liste programvareutgivelsene deres i Updater CE.Hvorfor heter pakken rom_y2.zip?

Utvikleren navngir Y2 fastvarearkivet `rom_y2.zip` så det kan ikke forveksles med Y1-ene `rom.zip`.Fungerer Y1-temaer på Y2?

Ikke alltid. Sjekk utgivelsesnotatene for Y2-bygget ditt og se [Rockbox-Y2 temaguide](rockbox-y2-themes.html).

## Relaterte guider

### [Rockbox-Y2-hub](rockbox-y2/)

Alle Y2 guider: installering, nedlastinger, temaer, gjenoppretting, dobbel oppstart og feilsøking.

### [Rockbox-Y1 mot Rockbox-Y2](rockbox-y1-vs-y2.html)

Hvordan bygningene Y1 og Y2 Rockbox er forskjellige.

### [Rockbox-Y2-temaer](rockbox-y2-themes.html)

Installere og tilbakestille temaer på Rockbox-Y2.

### [Rockbox for Y1](rockbox-for-y1_no.html)

Oversikt og installasjonsveiledning for Innioasis Y1-porten.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
