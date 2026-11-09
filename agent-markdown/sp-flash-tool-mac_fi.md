---
title: "SP Flash Tool Macille · MediaTek Scatter Flashing Guide &amp; Alternatives"
description: "SP Flash Tool:n käyttäminen Macissa Updater CE:n avulla ja hajatiedostojen selaaminen flash-MediaTek-laitteille, kuten Mechen H1, Innioasis Y1/Y2, Timmkoo ja MT6580/MT6572 MP3-soittimille ja puhelimille."
language: "fi"
source: "https://innioasis.app/sp-flash-tool-mac_fi.html"
---

# SP Flash Tool Macille · MediaTek Scatter Flashing Guide &amp; Alternatives

MediaTek Työkalut ja alustojen välinen vilkku

# SP Flash Tool Macille: Täydellinen opas ja scatter-selain

Toimiiko virallinen MediaTek SP Flash Tool macOS:ssä? Tässä on tarkka tila, miten Päivittäjä CE tarjoaa alkuperäisen MediaTek-flashin Macissa ja minkä tahansa hajontapohjaisen MediaTek-MP3-soittimen tai älypuhelimen flash-toiminnon.

## Totuus SP Flash Tool:sta macOS:ssä

MediaTek ei koskaan julkaissut virallista macOS-versiota Smart Phone Flash Tool (SP Flash Tool). Työkalu on koskaan ollut olemassa vain 32-/64-bittisenä Windows-sovelluksena ja x86_64 Linux-binaarina. SP Flash Tool:n emulointi macOS:ssä Winen tai CrossOverin kautta epäonnistuu, koska macOS-ytimen USB-laajennukset eivät salli USB-sarjan läpikulkua BROM-käynnistyksen kättelyssä vaaditulla tarkkuudella.

Ratkaisu:Päivittäjä CE kattaa tämän aukon yhdistämällä alkuperäiset Apple Silicon- ja Intel macOS -flash-kirjastot (matalien tason protokollamoottorin MTKclient kautta) automatisoidun hajonnan havaitsemisen ohella!

## Vilkkuu mikä tahansa MediaTek laite, jossa on "Asenna tiedostosta" (Scatter-selain)

Updater CE ei ole rajoitettu Innioasis pelaajille. Voit käyttää sitä tehokkaana yleiskäyttöisenä MediaTek-scatter-vilkkuna mihin tahansa sitä vaativaan laitteeseen SP Flash Tool v5 tai aikaisempi:
  - Mechen H1 & H11: MT6580 kannettavat HiFi Android-soittimet.
  - Timmkoo Q3, Q5, G1, A5: MediaTek kosketusnäytölliset digitaaliset äänisoittimet.
  - Oilsky, Phueut, Luoran: MediaTek MT6572 / MT6582 musiikkisoittimet.
  - Vanhat MediaTek älypuhelimet ja ominaisuuspuhelimet: Laitteet, joissa on MT6572, MT6580, MT6582, MT6735, MT6737, MT6739, MT6753 ja MT8163.

### Kuinka ladata mukautettuja scatter-tiedostoja Updater CE:ssä:
  - Lataa tehdasohjelmiston arkisto (`.zip` tai `.rar`) tai pura sen kansio, joka sisältää `*scatter*.txt` tiedosto.
  - Valitse Updater CE:ssä Selaa tiedostoja… laiteohjelmiston valintanäytössä.
  - Valitse hajontatekstitiedosto (esim. `MT6580_Android_scatter.txt`) tai laiteohjelmiston zip-paketti.
  - Updater CE jäsentää muistin siirtymät, osion osoitteet (esilataaja, käynnistys, palautus, järjestelmä, käyttäjätiedot) ja tarkistaa siron eheyden.
  - Noudata näytön ohjeita: sammuta laite ja liitä USB-kaapeli salamaan.

## Kun tarvitset x64-tietokoneen lohkon purkamiseen

Vaikka macOS käsittelee normaalin vilkkumisen ja mukautetut ROM-asennukset puhtaasti MTK-asiakkaan kautta, syvästä käynnistyssilmukan virheistä toipuminen (jos esilatausosio pyyhittiin tai se ei täsmää) vaatii SP Flash Tool:n täyden osiotaulukon uudelleenmuodostuksen.

Jos kohtaat virhehäiriöitä Macissa, vaihda 64-bittiseen Windows PC- tai x86_64 Linux -työasemaan, valitse Asetukset > Näytä lisäasetukset > Flash-menetelmä > SP Flash Tool, ja flash-tehdashajotuspaketti.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
