---
title: "Rockbox for Y2 (Rockbox-Y2): yleiskatsaus, koonti- ja asennusopas"
description: "Rockbox Y2:lle, Rockbox-Y2 ja rockbox-y2 viittaa yhteisön Rockbox laiteohjelmistoporttiin Innioasis Y2:lle. Opi, mitä se sisältää ja kuinka se asennetaan Innioasis Updater CE:n avulla."
language: "fi"
source: "https://innioasis.app/rockbox-for-y2_fi.html"
---

# Rockbox for Y2 (Rockbox-Y2): yleiskatsaus, koonti- ja asennusopas

[← Laiteohjelmiston lataukset](firmware_fi.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox Y2 (Rockbox-Y2)

Rockbox-Y2 (kutsutaan myös "Rockbox for Y2") on yhteisön Rockbox laiteohjelmistoportti Innioasis Y2:lle. Se käyttää omaa ROM-pakettiaan (`rom_y2.zip`) ja asennetaan suoraan Innioasis Updater CE:n kautta.[Asenna Rockbox-Y2](rockbox-y2/install.html)[Lataa ROM](rockbox-y2/download.html)[Kirjallinen opetusohjelma](guides/rockbox-y2.html)[Rockbox-Y2-keskitin](rockbox-y2/)

## Rakennettu erityisesti Innioasis Y2

Innioasis Updater CE:ssä tämä laiteohjelmisto on listattu nimellä Rockbox milloin Y2 on valittu. Sen julkaisut julkaisee [spycemagic/y2-rockbox](firmware_fi.html?model=Y2&software=rockbox-y2) projekti paketin nimellä `rom_y2.zip`.

Älä koskaan asenna Y1-laiteohjelmistopakettia Y2-laitteeseen. Valitseminen Y2 Updater CE suodattaa julkaisuluettelon automaattisesti vain Y2-yhteensopiviin koontiversioihin.

## Mitä Rockbox-Y2 tarjoaa
  - Tunnistepohjainen musiikkikirjasto — Selaa albumeita, artisteja ja genrejä äänitiedostotunnisteista tai selaa kansioita suoraan.
  - Toistosäätimet — välitön toisto, ristihäivytys, ReplayGain ja taajuuskorjainasetukset.
  - Mukautetut teemat — asenna Rockbox-Y2 koontiversiosi kanssa yhteensopivia teemoja ([Y2 teemaopas](rockbox-y2-themes.html)).
  - 100 % offline-tilassa — toistaa paikallisia tiedostoja MicroSD-kortilta ilman tilejä tai tilauksia.
  - Helppo tehdaspalautus — palaa Y2 alkuperäiseen ohjelmistoon milloin tahansa Updater CE:ssä.

## Rockbox-Y2-julkaisun valitseminen
  - Valitse aina Y2 sisään Laitteen malli ensin.
  - Valitse uusin versio, ellet testaa tiettyä versiota.
  - Lue [Rockbox-Y2 julkaisutiedot](release-notes/rockbox-y2/index_fi.html) nähdäksesi, mikä muuttui kussakin rakennuksessa.

## Suorat lataukset yhteisön kehittäjiltä

Innioasis Updater CE lataa aina laiteohjelmistopaketit suoraan yhteisön laiteohjelmistokehittäjiltä ([spycemagic/y2-rockbox](firmware_fi.html?model=Y2&software=rockbox-y2)), ja nämä kehittäjät ovat yksin vastuussa ohjelmistojulkaisujensa luetteloimisesta Updater CE:ssä.

Voit antaa Updater CE:n ladata ja vilkkua `rom_y2.zip` automaattisesti tai lataa paketti sivustoltamme [Rockbox-Y2 lataussivu](rockbox-y2/download.html) ja [Rockbox ROM lataussivu](rockbox-rom-download_fi.html).[Rockbox-Y2 latausta](rockbox-y2/download.html)[Asenna paikallisesta ZIP-tiedostosta](rockbox-y2/portable-zip.html)

## Kuinka asentaa Rockbox-Y2
  - Avaa Innioasis Updater CE ja aseta Laitteen malli to Y2.
  - Valitse Rockbox sisään Ohjelmisto.
  - Valitse Y2-julkaisu luettelosta.
  - Napsauta Asenna / Palauta joten Updater CE lataa paketin suoraan kehittäjältä.
  - Virta Y2 kokonaan pois päältä ja liitä se USB-datakaapelilla, kun Updater CE pyytää.
  - Odota valmistumisviestiä, irrota sitten verkkojohto ja käynnistä Y2.

Saat täydellisen vaiheittaisen esittelyn lukemalla [Rockbox-Y2 opetusohjelma](guides/rockbox-y2.html).

## Alkuperäisen Y2-ohjelmiston palauttaminen

Voit palata tehdasohjelmistoon valitsemalla Y2 ja Alkuperäinen ohjelmisto Valitse Updater CE:ssä vakaa julkaisu ja napsauta Asenna / Palauta. Katso [palautusopas](rockbox-y2/restore-stock.html) ja [Y2 Alkuperäinen ohjelmistosivu](original-software-y2_fi.html).

## Usein kysytyt kysymyksetMistä Updater CE lataa Rockbox-Y2:n?

Updater CE lataa aina laiteohjelmistopaketit suoraan yhteisön laiteohjelmistokehittäjien omista julkaisuista (`spycemagic/y2-rockbox`). Kehittäjät ovat yksin vastuussa ohjelmistojulkaisujensa luetteloimisesta Updater CE:ssä.Miksi paketin nimi on rom_y2.zip?

Kehittäjä nimeää Y2 laiteohjelmistoarkiston `rom_y2.zip` joten sitä ei voida sekoittaa Y1:iin `rom.zip`.Toimivatko Y1-teemat Y2:ssä?

Ei aina. Tarkista Y2-koontiversiosi julkaisutiedot ja katso [Rockbox-Y2 teemaopas](rockbox-y2-themes.html).

## Aiheeseen liittyviä oppaita

### [Rockbox-Y2-keskitin](rockbox-y2/)

Kaikki Y2 oppaat: asennus, lataukset, teemat, palautus, kaksoiskäynnistys ja vianetsintä.

### [Rockbox-Y1 vs Rockbox-Y2](rockbox-y1-vs-y2.html)

Kuinka Y1- ja Y2 Rockbox-koontiversiot eroavat toisistaan.

### [Rockbox-Y2-teemat](rockbox-y2-themes.html)

Asenna ja nollaa teemoja Rockbox-Y2.

### [Rockbox Y1:lle](rockbox-for-y1_fi.html)

Yleiskatsaus ja asennusopas Innioasis Y1-portille.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
