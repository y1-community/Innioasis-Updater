---
title: "Rockbox for Y2 (Rockbox-Y2): oversigt, builds og installationsvejledning"
description: "Rockbox for Y2, Rockbox-Y2 og rockbox-y2 henviser til fællesskabets Rockbox firmwareport for Innioasis Y2. Lær, hvad det indeholder, og hvordan du installerer det med Innioasis Updater CE."
language: "da"
source: "https://innioasis.app/rockbox-for-y2_da.html"
---

# Rockbox for Y2 (Rockbox-Y2): oversigt, builds og installationsvejledning

[← Firmware-downloads](firmware_da.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox for Y2 (Rockbox-Y2)

Rockbox-Y2 (også kaldet "Rockbox for Y2") er den dedikerede community Rockbox firmwareport til Innioasis Y2. Den bruger sin egen ROM pakke (`rom_y2.zip`) og installeres direkte gennem Innioasis Updater CE.[Installer Rockbox-Y2](rockbox-y2/install.html)[Download ROM](rockbox-y2/download.html)[Skriftlig vejledning](guides/rockbox-y2.html)[Rockbox-Y2 hub](rockbox-y2/)

## Bygget specielt til Innioasis Y2

I Innioasis Updater CE er denne firmware angivet som Rockbox hvornår Y2 er valgt. Dens udgivelser er udgivet af [spycemagic/y2-rockbox](firmware_da.html?model=Y2&software=rockbox-y2) projekt med pakkenavnet `rom_y2.zip`.

Installer aldrig en Y1-firmwarepakke på en Y2. Vælger Y2 i Updater CE filtrerer automatisk udgivelseslisten til kun Y2-kompatible builds.

## Hvad Rockbox-Y2 tilbyder
  - Tag-baseret musikbibliotek — gennemse album, kunstnere og genrer fra dine lydfil-tags, eller gennemse mapper direkte.
  - Afspilningskontroller — indstillinger for afspilning uden mellemrum, crossfade, ReplayGain og equalizer.
  - Brugerdefinerede temaer - installer temaer, der er kompatible med din Rockbox-Y2 build ([Y2 temaguide](rockbox-y2-themes.html)).
  - 100 % offline — afspiller lokale filer fra dit MicroSD-kort uden konti eller abonnementer.
  - Nem fabriksgendannelse — vend tilbage til Y2 Original Software til enhver tid i Updater CE.

## Valg af en Rockbox-Y2 udgivelse
  - Vælg altid Y2 ind Enhedsmodel først.
  - Vælg den seneste udgivelse, medmindre du tester en bestemt version.
  - Læs [Rockbox-Y2 release notes](release-notes/rockbox-y2/index_da.html) for at se, hvad der ændrede sig i hver bygning.

## Direkte downloads fra community-udviklerne

Innioasis Updater CE downloader altid firmwarepakker direkte fra fællesskabets firmwareudviklere ([spycemagic/y2-rockbox](firmware_da.html?model=Y2&software=rockbox-y2)), og disse udviklere er eneansvarlige for at angive deres softwareudgivelser i Updater CE.

Du kan lade Updater CE downloade og flashe `rom_y2.zip` automatisk, eller download pakken fra vores [Rockbox-Y2 downloads side](rockbox-y2/download.html) og [Rockbox ROM downloadside](rockbox-rom-download_da.html).[Rockbox-Y2 downloads](rockbox-y2/download.html)[Installer fra en lokal ZIP](rockbox-y2/portable-zip.html)

## Sådan installeres Rockbox-Y2
  - Åbn Innioasis Updater CE og indstil Enhedsmodel til Y2.
  - Vælg Rockbox ind Software.
  - Vælg en Y2 udgivelse fra listen.
  - Klik Installer / Gendan så Updater CE downloader pakken direkte fra udvikleren.
  - Sluk Y2 helt, og tilslut den med et USB datakabel, når Updater CE spørger.
  - Vent på fuldførelsesmeddelelsen, tag derefter stikket ud og tænd for din Y2.

For den fulde trin-for-trin gennemgang, læs [Rockbox-Y2 tutorial](guides/rockbox-y2.html).

## Gendannelse af den originale Y2-software

For at gå tilbage til fabriksfirmwaren skal du vælge Y2 og Original software i Updater CE, vælg en stabil udgivelse, og klik Installer / Gendan. Se den [guide til gendannelse](rockbox-y2/restore-stock.html) og [Y2 Original softwareside](original-software-y2_da.html).

## Ofte stillede spørgsmålHvor downloader Updater CE Rockbox-Y2 fra?

Updater CE downloader altid firmwarepakker direkte fra fællesskabets firmwareudvikleres egne udgivelser (`spycemagic/y2-rockbox`). Udviklerne er alene ansvarlige for at liste deres softwareudgivelser i Updater CE.Hvorfor hedder pakken rom_y2.zip?

Udvikleren navngiver Y2 firmwarearkivet `rom_y2.zip` så det kan ikke forveksles med Y1'erne `rom.zip`.Fungerer Y1-temaer på Y2?

Ikke altid. Tjek udgivelsesbemærkningerne til din Y2 build og se [Rockbox-Y2 temaguide](rockbox-y2-themes.html).

## Relaterede guider

### [Rockbox-Y2 hub](rockbox-y2/)

Alle Y2 guider: installation, downloads, temaer, gendannelse, dual boot og fejlfinding.

### [Rockbox-Y1 mod Rockbox-Y2](rockbox-y1-vs-y2.html)

Hvordan Y1 og Y2 Rockbox builds adskiller sig.

### [Rockbox-Y2 temaer](rockbox-y2-themes.html)

Installation og nulstilling af temaer på Rockbox-Y2.

### [Rockbox for Y1](rockbox-for-y1_da.html)

Oversigt og installationsvejledning til Innioasis Y1-porten.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
