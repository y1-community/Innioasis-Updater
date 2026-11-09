---
title: "Kuinka asentaa Rockbox Innioasis Y1 tai Y2 - Innioasis Updater"
description: "Asenna Rockbox Innioasis Y1- tai Y2-sovellukseen, jossa on Updater: teemat, vakaat julkaisut, Type A- ja Type B-muistiinpanot sekä alkuperäisen ohjelmiston palauttaminen sen jälkeen."
language: "fi"
source: "https://innioasis.app/rockbox_fi.html"
---

# Kuinka asentaa Rockbox Innioasis Y1 tai Y2 - Innioasis Updater

Rockbox viite

# Rockbox saaminen Y1 tai Y2

Rockbox muuttaa soittimen ohjelmistoa ja avaa syvemmän musiikkisoittimen käyttöliittymän, toistosäätimet, lajittelun ja teemavaihtoehdot. Asennus on ohjattua, mutta Y1 ja Y2 ovat erillisiä matkoja.[Rockbox Y1](guides/rockbox-y1.html)[Rockbox Y2](guides/rockbox-y2.html)[Miksi Rockbox?](rockbox-benefits_fi.html)

## Mitä asennus muuttaa

Rockbox on mukautettu ohjelmisto. Se ei poista mahdollisuuttasi palata varastoliittymään, kun vastaava alkuperäinen ohjelmistopaketti on saatavilla. Se voi parantaa musiikin selaamista ja mukauttamista, mutta ominaisuudet, resoluutio, akun kesto ja teeman yhteensopivuus riippuvat koontiversiosta.Älä sekoita malleja. Valitse Y1 Y1-soittimelle ja Y2 Y2-soittimelle. Samannäköinen julkaisunimi ei riitä todisteeksi paketin yhteensopivuudesta.

## Katso video

Video: Frawgeeys. Se näyttää Innioasis Updater-reitin; käytä alla olevia mallikohtaisia ​​kirjallisia ohjeita Y1:lle tai Y2:lle.

Videon tekijä [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (espanja), näyttää Rockbox Y1. Käytä soittimellesi alla olevia mallikohtaisia ​​ohjeita.

## Jaettu Updater-reitti
  - Asenna Updater ja yhdistä mitään ennen kuin se kysyy.
  - Valitse soittimeen painettu malli Laitteen malli.
  - Valitse Rockbox sisään Ohjelmisto.
  - Valitse vakaa julkaisu, ellet tarkoituksella testaa öistä versiota.
  - Napsauta Asenna / Palauta, noudata sitten virrankatkaisu- ja USB yhteyskehotetta.
  - Katkaise yhteys vasta onnistumisviestin jälkeen.

## 240p, 360p ja teemat

Vanhemmat Rockbox teemakokoelmat voidaan tehdä 240p:lle. Y1 yhteisörakennuksissa käytetään myös 360p-yhteensopivuustunnisteita. Lue julkaisutiedot ja teemalähde ennen koontiversion valitsemista. Yhdelle resoluutiolle tai ohjelmistoperheelle tehty teema ei välttämättä toimi toisessa.[Selaa yhteisön teemoja](https://themes.innioasis.app/?lang=fi)[Teeman työkalut](https://themes.innioasis.app/?lang=fi)

## Paluu alkuperäiseen ohjelmistoon

Valitse sama malli uudelleen, valitse Alkuperäinen ohjelmisto, valitse vakaa vapautus ja käytä Asenna / Palauta. Jos virhe tapahtui ennen USB-kehotetta, tarkista tietokone ja puretut tiedostot. Jos soitin tunnistettiin, mutta salama epäonnistui, aloita [vianetsintä](troubleshooting_fi.html).[Y1 palauttaa](guides/restore-original-y1.html)[Y2 palauttaa](guides/restore-original-y2.html)

## UKKAsensin Rockbox uudelleen, eikä se korjannut mitään.

Rockbox:n uudelleenasentaminen kirjoittaa saman koontiversion samojen tiedostojen päälle, joten se ei voi nollata asioita, joita Rockbox säilyttää MicroSDissa. Jos ongelma on rikkinäinen asetus, teema, soittolista tai kortilla oleva tietokanta, uudelleenasennus ei poista sitä. Luotettava nollaus poistaa `.rockbox` kansio MicroSD - Rockbox rakentaa uuden seuraavan käynnistyksen yhteydessä.
  - Virta soittimesta täysin pois päältä ja poista MicroSD-kortti tai liitä soitin USB-asemaksi.
  - Näytä piilotetut tiedostot tietokoneellasi, jotta kansio näkyy. Kuinka näyttää piilotetut tiedostotNäytä pistetiedostot tietokoneellasiWindows: avaa File Explorerissa Näytä välilehti ja rasti Piilotetut kohteet.macOS: Finderissa Cmd+Shift+. vaihtaaksesi piilotetut tiedostot.Linux · GNOME-tiedostot: paina Ctrl+Htai avaa valikko ja valitse Näytä piilotetut tiedostot.Linux · KDE Dolphin: paina Ctrl+H, tai käytä Näytä → Näytä piilotetut tiedostot.
  - Poista `.rockbox` kansio kortin juuresta.
  - Aseta kortti takaisin paikalleen ja käynnistä soitin. Rockbox luo kansion uudelleen oletusasetuksilla.
  - Ota teema ja asetukset uudelleen käyttöön. Jos ongelma palaa vasta tietyn teeman jälkeen, tämä teema on syynä.

Poistetaan `.rockbox` ei poista Rockbox asennusta eikä koske musiikkiisi – kansio sisältää asetukset, teemat ja välimuistit, ja se rakennetaan uudelleen automaattisesti. Jos haluat säilyttää teemasi, kopioi kansio pois `.rockbox` ennen sen poistamista tai nimeä kansio uudelleen `.rockbox-old` ensin.Miksi en näe .rockbox-kansiota MicroSD:ssani?

Kansiot, joiden nimi alkaa pisteellä, on oletusarvoisesti piilotettu useimmissa tietokoneissa. Sinun ei tarvitse nähdä sitä asentaaksesi Rockbox — Updater käsittelee tiedostot. Jos olet vianetsintää ja haluat poistaa sen, ota piilotetut tiedostot käyttöön ensin. Kuinka näyttää piilotetut tiedostotNäytä pistetiedostot tietokoneellasiWindows: avaa File Explorerissa Näytä välilehti ja rasti Piilotetut kohteet.macOS: Finderissa Cmd+Shift+. vaihtaaksesi piilotetut tiedostot.Linux · GNOME-tiedostot: paina Ctrl+Htai avaa valikko ja valitse Näytä piilotetut tiedostot.Linux · KDE Dolphin: paina Ctrl+H, tai käytä Näytä → Näytä piilotetut tiedostot.Nollaako .rockboxin poistaminen teemani ja asetukset?

kyllä — `.rockbox` sisältää käyttäjän Rockbox asetukset, teeman, soittolistat ja välimuistin tietokannan. Sen poistaminen palauttaa Rockbox puhtaaseen oletustilaan. Varmuuskopioi koko kansio (tai nimeä se uudelleen `.rockbox-old`), jos haluat ehkä jonkin niistä takaisin, käynnistä soitin ja Rockbox luo uuden kansion.

## Lisää Rockbox-Y1 ja Rockbox-Y2 oppaita

Tutustu vaiheittaisiin oppaisiin asennusta, lataamista, teemaa, palauttamista ja vianmääritystä varten Rockbox molemmissa malleissa:[Rockbox-Y1-keskitin](rockbox-y1/)[Rockbox-Y2-keskitin](rockbox-y2/)[Rockbox ROM-lataukset](rockbox-rom-download_fi.html)[Rockbox Y1:lle](rockbox-for-y1_fi.html)[Rockbox Y2:lle](rockbox-for-y2_fi.html)[Rockbox-Y1 vs. Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1-teemat](rockbox-y1-themes.html)[Rockbox-Y2-teemat](rockbox-y2-themes.html)

## Oliko tästä viitteestä hyötyä?

Vastauksesi auttaa parantamaan tätä opasta.KylläEi vielä[Kerro meille, kuinka voimme parantaa](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
