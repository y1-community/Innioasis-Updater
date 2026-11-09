---
title: "Rockbox for Y1 (Rockbox-Y1): yleiskatsaus, koonti- ja asennusopas"
description: "Rockbox for Y1, Rockbox-Y1 ja rockbox-y1 viittaavat kaikki yhteisön Rockbox laiteohjelmistoon Innioasis Y1:lle. Opi, mitä se lisää, mikä koontiversio valitaan ja kuinka se asennetaan Innioasis Updater CE:n avulla."
language: "fi"
source: "https://innioasis.app/rockbox-for-y1_fi.html"
---

# Rockbox for Y1 (Rockbox-Y1): yleiskatsaus, koonti- ja asennusopas

[← Laiteohjelmiston lataukset](firmware_fi.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox Y1 (Rockbox-Y1)

"Rockbox", "Rockbox-Y1" ja "Rockbox for Y1" viittaavat kaikki samaan yhteisön Rockbox laiteohjelmistoon Innioasis Y1:lle. Tässä on, mitä se lisää soittimeesi, minkä koontiversion voit valita ja kuinka se asennetaan Innioasis Updater CE:llä.[Asenna Rockbox-Y1](rockbox-y1/install.html)[Lataa ROM](rockbox-y1/download.html)[Kirjallinen opetusohjelma](guides/rockbox-y1.html)[Rockbox-Y1-keskitin](rockbox-y1/)

## Yksi laiteohjelmisto, useita nimiä

Innioasis Updater CE:ssä tämä laiteohjelmisto näkyy muodossa Rockbox kun valitset laitemallin Y1. Oppaat, videot ja julkaisutiedot kutsuvat myös sitä Rockbox-Y1 tai Rockbox Y1:lle joten on selvää, että rakenne on Y1 eikä Y2.

Tarkista aina soittimeen painettu malli ennen asennusta: Y1 ja Y2 laiteohjelmistopaketit eivät ole keskenään vaihdettavissa.

## Mitä Rockbox-Y1 lisää Y1

Rockbox-Y1 on yhteisöportti avoimen lähdekoodin Rockbox musiikkisoittimen laiteohjelmistolle Innioasis Y1:
  - Tunnistepohjainen musiikkikirjasto — Selaa esittäjän, albumin, genren ja vuoden mukaan äänitunnisteiden avulla tai selaa kansioita suoraan.
  - Edistynyt äänentoisto — välitön toisto, ristihäivytys, ReplayGain ja täysi taajuuskorjain.
  - Mukautetut teemat — Valitse sadoista 240p- ja 360p-yhteisöteemoja, mukaan lukien klassiset iPod-tyyliset asettelut.
  - FM-radio - sisäänrakennettu FM-radion tuki.
  - Valinnaiset lisävarusteet — podcast-lataukset Wi-Fi-yhteydellä ja Last.fm / ListenBrainz / Maloja sccrobbing tuettujen koontiversioiden kautta.
  - Kaksoiskäynnistys — vaihda takaisin tehtaan alkuperäiseen ohjelmistoon ilman päivittämistä tuetuissa versioissa.

## Mikä Y1-versio minun pitäisi valita?
  - 240p vs. 360p — 240p-koontiversiot toimivat klassisilla 320×240 Rockbox-teemoilla; 360p-koontiversiot käyttävät terävämpiä 480 × 360 Y1 teemoja. Yhdistä koontiresoluutio niihin teemoihin, joita haluat käyttää ([240p vs. 360p -opas](rockbox-y1/resolution.html)).
  - Type A vs. Type B — Type A on Y1-soittimille, joiden mukana toimitetaan tehdasohjelmisto 2.0.0 tai uudempi; Type B on aikaisemmille Y1 yksiköille. Valitse Type A, ellet tiedä, että Y1 on Type B.
  - Stable vs. Nightly — Valitse vakaa rakenne jokapäiväiseen kuunteluun tai öinen versio testataksesi uusimpia muutoksia.

## Suorat lataukset yhteisön kehittäjiltä

Innioasis Updater CE lataa aina laiteohjelmistopaketit suoraan yhteisön laiteohjelmistokehittäjiltä ([rockbox-y1/rockbox](firmware_fi.html?model=Y1&software=rockbox-y1)), ja kehittäjät itse ovat yksin vastuussa ohjelmistojulkaisujensa luetteloimisesta Updater CE:ssä.

Voit antaa Updater CE:n ladata ja asentaa laiteohjelmiston automaattisesti tai ladata ROM-paketit sivustoltamme [Rockbox-Y1 lataussivu](rockbox-y1/download.html) ja [Rockbox ROM lataussivu](rockbox-rom-download_fi.html).[Rockbox-Y1 latausta](rockbox-y1/download.html)[Asenna paikallisesta ZIP-tiedostosta](rockbox-y1/portable-zip.html)

## Kuinka asentaa Rockbox-Y1
  - Avaa Innioasis Updater CE ja aseta Laitteen malli to Y1.
  - Valitse Rockbox sisään Ohjelmisto.
  - Valitse vakaa julkaisu (tai ota käyttöön öiset koontiversiot testataksesi esikatselua).
  - Napsauta Asenna / Palauta joten Updater CE lataa paketin suoraan kehittäjältä.
  - Virta Y1 kokonaan pois päältä ja liitä se USB-datakaapelilla, kun Updater CE pyytää sinua.
  - Odota valmistumisviestiä, katkaise sitten soitin ja käynnistä se.

Katso kuvakaappaukset ja yksityiskohtaiset asennusvinkit kohdasta [koko Rockbox-Y1 opetusohjelma](guides/rockbox-y1.html).

## Alkuperäisen Y1-ohjelmiston palauttaminen

Voit palata tehdasohjelmistoon milloin tahansa: valitse Y1 ja Alkuperäinen ohjelmisto Valitse Updater CE:ssä vakaa julkaisu ja napsauta Asenna / Palauta. Kortilla MicroSD oleva musiikki säilyy. Katso [palautusopas](rockbox-y1/restore-stock.html) ja [Y1 Alkuperäinen ohjelmistosivu](original-software-y1_fi.html).

## Usein kysytyt kysymyksetOnko Rockbox kohteelle Y1 sama kuin Rockbox-Y1?

Kyllä. Rockbox, Rockbox-Y1, Rockbox, Y1 ja `rockbox-y1` kaikki viittaavat samaan yhteisön Rockbox porttiin Innioasis Y1:lle.Mistä Updater CE lataa Rockbox-Y1:n?

Updater CE lataa aina laiteohjelmistopaketit suoraan yhteisön laiteohjelmistokehittäjien omista julkaisuista (`rockbox-y1/rockbox`). Kehittäjät ovat yksin vastuussa ohjelmistojulkaisujensa luetteloimisesta Updater CE:ssä.Voinko asentaa Rockbox-Y1:n Y2-laitteeseen?

Ei. Y2:lla on oma erillinen laiteohjelmistoversionsa. Käytä [Rockbox Y2:lle](rockbox-for-y2_fi.html) sen sijaan.Poistaako Rockbox-Y1:n asentaminen musiikkini?

Ei. Musiikki tallennetaan MicroSD-kortille, eikä soittimen sisäisen laiteohjelmiston vilkkuminen vaikuta siihen.

## Aiheeseen liittyviä oppaita

### [Rockbox-Y1-keskitin](rockbox-y1/)

Kaikki Y1 oppaat: asennus, lataukset, teemat, palautus, kaksoiskäynnistys ja vianetsintä.

### [Rockbox-Y1 vs Rockbox-Y2](rockbox-y1-vs-y2.html)

Kuinka Y1- ja Y2 Rockbox-koontiversiot eroavat toisistaan.

### [Rockbox-Y1-teemat](rockbox-y1-themes.html)

Kuinka siirtää 240p- ja 360p-teemoja Updater CE:n avulla.

### [Rockbox yleiskatsaus](rockbox_fi.html)

Rockbox:n esittely Innioasis Y1- ja Y2-soittimissa.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
