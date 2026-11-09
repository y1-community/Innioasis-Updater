---
title: "Rockbox for Y1 (Rockbox-Y1): oversigt, builds og installationsvejledning"
description: "Rockbox for Y1, Rockbox-Y1 og rockbox-y1 henviser alle til fællesskabets Rockbox firmware til Innioasis Y1. Lær, hvad det tilføjer, hvilken build du skal vælge, og hvordan du installerer det med Innioasis Updater CE."
language: "da"
source: "https://innioasis.app/rockbox-for-y1_da.html"
---

# Rockbox for Y1 (Rockbox-Y1): oversigt, builds og installationsvejledning

[← Firmware-downloads](firmware_da.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox for Y1 (Rockbox-Y1)

"Rockbox", "Rockbox-Y1", og "Rockbox for Y1" refererer alle til den samme community Rockbox firmware for Innioasis Y1. Her er, hvad den tilføjer til din afspiller, hvilken build du skal vælge, og hvordan du installerer den med Innioasis Updater CE.[Installer Rockbox-Y1](rockbox-y1/install.html)[Download ROM](rockbox-y1/download.html)[Skriftlig vejledning](guides/rockbox-y1.html)[Rockbox-Y1 hub](rockbox-y1/)

## Én firmware, flere navne

I Innioasis Updater CE vises denne firmware som Rockbox når du vælger enhedsmodel Y1. Guider, videoer og release notes kalder det også Rockbox-Y1 eller Rockbox for Y1 så det er klart, at bygningen er til Y1 og ikke Y2.

Kontroller altid den model, der er trykt på din afspiller, før du installerer: Y1 og Y2 firmwarepakker er ikke udskiftelige.

## Hvad Rockbox-Y1 tilføjer til din Y1

Rockbox-Y1 er en fællesskabsport til open source Rockbox musikafspillerens firmware til Innioasis Y1:
  - Tag-baseret musikbibliotek — gennemse efter kunstner, album, genre og år ved hjælp af lydmærker, eller gennemse mapper direkte.
  - Avanceret lydafspilning — afspilning uden mellemrum, crossfade, ReplayGain og en fuld equalizer.
  - Brugerdefinerede temaer — vælg mellem hundredvis af 240p- og 360p-fællesskabstemaer, inklusive klassiske iPod-layouts.
  - FM radio — indbygget FM-radiounderstøttelse.
  - Ekstraudstyr — podcast-downloads over Wi-Fi og Last.fm / ListenBrainz / Maloja scrobbling på understøttede builds.
  - Dobbelt støvle — Skift tilbage til den originale fabrikssoftware uden at genindlæse understøttede builds.

## Hvilken Y1 build skal jeg vælge?
  - 240p vs. 360p — 240p builds arbejde med klassiske 320×240 Rockbox-temaer; 360p builds bruger skarpere 480×360 Y1 temaer. Match byggeopløsningen til de temaer, du vil bruge ([240p vs. 360p guide](rockbox-y1/resolution.html)).
  - Type A mod Type B — Type A er til Y1 spillere, der blev leveret med fabrikssoftware 2.0.0 eller nyere; Type B er for tidligere Y1 enheder. Vælg Type A, medmindre du ved, at din Y1 er Type B.
  - Stabil vs. natlig — Vælg en stabil build til hverdagslytning eller en natlig build for at teste de nyeste ændringer.

## Direkte downloads fra community-udviklerne

Innioasis Updater CE downloader altid firmwarepakker direkte fra fællesskabets firmwareudviklere ([rockbox-y1/rockbox](firmware_da.html?model=Y1&software=rockbox-y1)), og udviklerne selv er eneansvarlige for at angive deres softwareudgivelser i Updater CE.

Du kan lade Updater CE downloade og installere firmwaren automatisk eller downloade ROM-pakkerne fra vores [Rockbox-Y1 downloads side](rockbox-y1/download.html) og [Rockbox ROM downloadside](rockbox-rom-download_da.html).[Rockbox-Y1 downloads](rockbox-y1/download.html)[Installer fra en lokal ZIP](rockbox-y1/portable-zip.html)

## Sådan installeres Rockbox-Y1
  - Åbn Innioasis Updater CE og indstil Enhedsmodel til Y1.
  - Vælg Rockbox ind Software.
  - Vælg en stabil udgivelse (eller aktivér natlige builds for at teste en forhåndsvisning).
  - Klik Installer / Gendan så Updater CE downloader pakken direkte fra udvikleren.
  - Sluk for Y1 helt, og tilslut den med et USB-datakabel, når Updater CE beder dig om det.
  - Vent på fuldførelsesmeddelelsen, afbryd derefter forbindelsen og tænd for din afspiller.

For skærmbilleder og detaljerede opsætningstip, læs [fuld Rockbox-Y1 tutorial](guides/rockbox-y1.html).

## Gendannelse af den originale Y1-software

Du kan til enhver tid vende tilbage til fabrikssoftwaren: vælg Y1 og Original software i Updater CE, vælg en stabil udgivelse, og klik Installer / Gendan. Din musik på MicroSD-kortet er bevaret. Se den [guide til gendannelse](rockbox-y1/restore-stock.html) og [Y1 Original softwareside](original-software-y1_da.html).

## Ofte stillede spørgsmålEr Rockbox for Y1 det samme som Rockbox-Y1?

Ja. Rockbox, Rockbox-Y1, Rockbox for Y1, og `rockbox-y1` alle refererer til den samme community Rockbox port for Innioasis Y1.Hvor downloader Updater CE Rockbox-Y1 fra?

Updater CE downloader altid firmwarepakker direkte fra fællesskabets firmwareudvikleres egne udgivelser (`rockbox-y1/rockbox`). Udviklerne er alene ansvarlige for at liste deres softwareudgivelser i Updater CE.Kan jeg installere Rockbox-Y1 på en Y2?

Nej. Y2 har sin egen separate firmware build. Brug [Rockbox for Y2](rockbox-for-y2_da.html) i stedet for.Vil installation af Rockbox-Y1 slette min musik?

Nej. Musik er gemt på MicroSD-kortet og påvirkes ikke, når afspillerens interne firmware blinker.

## Relaterede guider

### [Rockbox-Y1 hub](rockbox-y1/)

Alle Y1 guider: installation, downloads, temaer, gendannelse, dual boot og fejlfinding.

### [Rockbox-Y1 mod Rockbox-Y2](rockbox-y1-vs-y2.html)

Hvordan Y1 og Y2 Rockbox builds adskiller sig.

### [Rockbox-Y1 temaer](rockbox-y1-themes.html)

Sådan overføres 240p- og 360p-temaer med Updater CE.

### [Rockbox oversigt](rockbox_da.html)

Introduktion til Rockbox på Innioasis Y1 og Y2 spillere.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
