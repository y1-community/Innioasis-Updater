---
title: "Innioasis Päivittimen vianmääritys | Innioasis ja Timmkoo asennusongelmat - Innioasis Updater"
description: "Korjaa Innioasis Updater -asennukset mihin tahansa Innioasis- tai Timmkoo-soittimeen. Tarkista malli, kaapeli, ajuri, virrankatkaisun ajoitus ja asennus lopetuspaikka – saat sen jälkeen vilkkumaan uudelleen."
language: "fi"
source: "https://innioasis.app/troubleshooting_fi.html"
---

# Innioasis Päivittimen vianmääritys | Innioasis ja Timmkoo asennusongelmat - Innioasis Updater

Vianetsintä

# Etsi kohta, jossa asennus pysähtyi.

Missä se pysähtyi? Se kertoo, mitä korjata.[Palaa normaaliin ohjeeseen](guide_fi.html)[Tarkista laiteohjelmisto](firmware_fi.html)

## Se pysähtyi ennen USB-kehotetta

Tämä on tietokoneongelma, ei kaapeliongelma. Tarkista mallisi. Pura tiedosto uudelleen. Yritä sitten Asenna / Palauta. Jos julkaisuluettelo on tyhjä, avaa [laiteohjelmistohakemisto](firmware_fi.html).

## Se ei voi muodostaa yhteyttä soittimeen
  - Sammuta oikea Y1 tai Y2 kokonaan.
  - Irrota kaapeli, sulje muut flash- tai Android-työkalut ja aloita asennus uudelleen.
  - Yhdistä vain, kun Updater sanoo, että se on valmis.
  - Käytä lyhyttä USB datakaapelia suoraan tietokoneessa, älä keskitintä, jos mahdollista.
  - Windowsissa asenna MediaTek-ohjain uudelleen ja käynnistä uudelleen. Tarkista Linuxissa USB/sarjaoikeudet.
Päivitysohjelman yhteyskehoteLive Updater -kehote on pätevä nykyiselle mallille ja alustalle.

## Se havaitsi soittimen, mutta salama epäonnistui

Pysähdy tähän. Älä kokeile toista mallia. Sulje muut työkalut, tarkista, että valitsit oikean Y1 tai Y2, ja käytä vastaavaa alkuperäistä ohjelmistoa, jos soitin ei käynnisty. [SP Flash Tool](sp-flash-tool_fi.html) ja MTKClient ovat mukana, jos tarvitset niitä, ja tiedostot ovat [laiteohjelmiston sivu](firmware_fi.html).

## Windows-ohjaimen muistiinpanot

Jotkut Windows-asennukset estävät MediaTek-ohjaimen Core-eristyksen vuoksi. Noudata voimassa olevia Windowsin suojausohjeita, ennen kuin muutat muistin eheyttä, ja käynnistä se uudelleen, kun olet valmis, jos järjestelmäsi sallii sen.[Avaa kuljettajan opas](drivers_fi.html)[Puhdas asennusohje](Troubleshooting/clean_install.html)

## Pyörä ei toimi tai soitin ei käynnisty

Tulo- ja tehohäiriöt vaativat eri vaiheita kuin epäonnistunut salama. Nämä oppaat kattavat yleiset Y1 ja Y2 tapaukset.[Y1 vierityspyörä](guides/y1-scroll-wheel-not-working.html)[Y2 vierityspyörä](guides/y2-scroll-wheel-not-working.html)[Y1 ei käynnisty](guides/y1-wont-turn-on.html)[Y2 ei käynnisty](guides/y2-wont-turn-on.html)[Palautusopas](guides/recovery.html)

## Vieläkö jumissa?

Kun pyydät apua, ilmoita malli, käyttöjärjestelmä, tarkka Updater-viesti, tunnistettiinko soitin ja valitsemasi paketti/projekti. Älä lähetä yksityisiä tunnuksia tai asiaankuulumattomia järjestelmätiedostoja.[Pyydä apua](https://discord.gg/zHrT2zrcek)[Tuki ylläpitoon](support_devs_fi.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
