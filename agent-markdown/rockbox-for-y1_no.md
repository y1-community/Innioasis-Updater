---
title: "Rockbox for Y1 (Rockbox-Y1): oversikt, bygg og installasjonsveiledning"
description: "Rockbox for Y1, Rockbox-Y1 og rockbox-y1 refererer alle til fellesskapets Rockbox fastvare for Innioasis Y1. Finn ut hva den legger til, hvilken versjon du bør velge, og hvordan du installerer den med Innioasis Updater CE."
language: "no"
source: "https://innioasis.app/rockbox-for-y1_no.html"
---

# Rockbox for Y1 (Rockbox-Y1): oversikt, bygg og installasjonsveiledning

[← Fastvarenedlastinger](firmware_no.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox for Y1 (Rockbox-Y1)

"Rockbox", "Rockbox-Y1", og "Rockbox for Y1" refererer alle til samme fellesskap Rockbox-fastvaren for Innioasis Y1. Her er hva den legger til spilleren din, hvilken versjon du skal velge, og hvordan du installerer den med Innioasis Updater CE.[Installer Rockbox-Y1](rockbox-y1/install.html)[Last ned ROM](rockbox-y1/download.html)[Skriftlig veiledning](guides/rockbox-y1.html)[Rockbox-Y1-hub](rockbox-y1/)

## Én fastvare, flere navn

I Innioasis Updater CE vises denne fastvaren som Rockbox når du velger enhetsmodell Y1. Guider, videoer og utgivelsesnotater kaller det også Rockbox-Y1 eller Rockbox for Y1 så det er klart at konstruksjonen er for Y1 og ikke Y2.

Sjekk alltid modellen som er trykt på spilleren din før du installerer: Y1 og Y2 fastvarepakker kan ikke byttes ut.

## Hva Rockbox-Y1 legger til din Y1

Rockbox-Y1 er en fellesskapsport for åpen kildekode Rockbox musikkspillerfastvaren for Innioasis Y1:
  - Tag-basert musikkbibliotek – bla etter artist, album, sjanger og år ved å bruke lydetiketter, eller bla direkte gjennom mapper.
  - Avansert lydavspilling — gapløs avspilling, crossfade, ReplayGain og en full equalizer.
  - Egendefinerte temaer — velg blant hundrevis av 240p- og 360p-fellesskapstemaer, inkludert klassiske oppsett i iPod-stil.
  - FM-radio — innebygd FM-radiostøtte.
  - Tilleggsutstyr — podcastnedlastinger over Wi-Fi og Last.fm / ListenBrainz / Maloja scrobbling på støttede bygg.
  - Dobbel støvel — bytt tilbake til originalprogramvaren fra fabrikken uten å gjenopprette på støttede bygg.

## Hvilken Y1 build skal jeg velge?
  - 240p vs. 360p — 240p-bygg fungerer med klassiske 320×240 Rockbox-temaer; 360p-bygg bruker skarpere 480×360 Y1-temaer. Tilpass byggeoppløsningen til temaene du vil bruke ([240p vs. 360p guide](rockbox-y1/resolution.html)).
  - Type A vs. Type B — Type A er for Y1 spillere som ble levert med fabrikkprogramvare 2.0.0 eller nyere; Type B er for tidligere Y1 enheter. Velg Type A med mindre du vet at din Y1 er Type B.
  - Stabil vs. nattlig — Velg en stabil konstruksjon for hverdagslytting, eller en nattlig konstruksjon for å teste de nyeste endringene.

## Direkte nedlastinger fra fellesskapsutviklerne

Innioasis Updater CE laster alltid ned fastvarepakker direkte fra fellesskapets fastvareutviklere ([rockbox-y1/rockbox](firmware_no.html?model=Y1&software=rockbox-y1)), og utviklerne selv er eneansvarlige for å føre opp programvareutgivelsene deres i Updater CE.

Du kan la Updater CE laste ned og installere fastvaren automatisk, eller laste ned ROM-pakkene fra vår [Rockbox-Y1 nedlastingsside](rockbox-y1/download.html) og [Rockbox ROM nedlastingsside](rockbox-rom-download_no.html).[Rockbox-Y1 nedlastinger](rockbox-y1/download.html)[Installer fra en lokal ZIP](rockbox-y1/portable-zip.html)

## Hvordan installere Rockbox-Y1
  - Åpne Innioasis Updater CE og still inn Enhetsmodell til Y1.
  - Velg Rockbox inn Programvare.
  - Velg en stabil utgivelse (eller aktiver nattlige bygg for å teste en forhåndsvisning).
  - Klikk Installer / Gjenopprett så Updater CE laster ned pakken direkte fra utvikleren.
  - Slå av Y1 helt og koble den til med en USB datakabel når Updater CE ber deg om det.
  - Vent på fullføringsmeldingen, koble fra og slå på spilleren.

For skjermbilder og detaljerte oppsetttips, les [full Rockbox-Y1 veiledning](guides/rockbox-y1.html).

## Gjenoppretter den originale Y1-programvaren

Du kan gå tilbake til fabrikkprogramvaren når som helst: velg Y1 og Original programvare i Updater CE, velg en stabil utgivelse og klikk Installer / Gjenopprett. Musikken din på MicroSD-kortet er bevart. Se [gjenopprettingsveiledning](rockbox-y1/restore-stock.html) og [Y1 Original programvareside](original-software-y1_no.html).

## Ofte stilte spørsmålEr Rockbox for Y1 det samme som Rockbox-Y1?

Ja. Rockbox, Rockbox-Y1, Rockbox for Y1, og `rockbox-y1` alle refererer til den samme fellesskapet Rockbox-porten for Innioasis Y1.Hvor laster Updater CE ned Rockbox-Y1 fra?

Updater CE laster alltid ned fastvarepakker direkte fra fellesskapsfastvareutviklernes egne utgivelser (`rockbox-y1/rockbox`). Utviklerne er alene ansvarlige for å liste programvareutgivelsene deres i Updater CE.Kan jeg installere Rockbox-Y1 på en Y2?

Nei. Y2 har sin egen separate fastvarebygging. Bruk [Rockbox for Y2](rockbox-for-y2_no.html) i stedet.Vil installasjon av Rockbox-Y1 slette musikken min?

Nei. Musikk er lagret på MicroSD-kortet og påvirkes ikke når spillerens interne fastvare blinker.

## Relaterte guider

### [Rockbox-Y1-hub](rockbox-y1/)

Alle Y1 guider: installering, nedlastinger, temaer, gjenoppretting, dobbel oppstart og feilsøking.

### [Rockbox-Y1 mot Rockbox-Y2](rockbox-y1-vs-y2.html)

Hvordan bygningene Y1 og Y2 Rockbox er forskjellige.

### [Rockbox-Y1-temaer](rockbox-y1-themes.html)

Hvordan overføre 240p og 360p temaer med Updater CE.

### [Rockbox oversikt](rockbox_no.html)

Introduksjon til Rockbox på Innioasis Y1 og Y2 spillere.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
