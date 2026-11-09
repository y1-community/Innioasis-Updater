---
title: "Wi-Fi-, Bluetooth- ja FM-radion asetukset: Reborn (Y2Linux) - Innioasis Päivitys"
description: "Lyhyt asennuksen jälkeinen opas Reborn:lle (Y2Linux / Y2Reborn) Innioasis Y2: kopioi system.img ja määritä sitten Wi-Fi, Bluetooth ja FM-radio."
language: "fi"
source: "https://innioasis.app/y2reborn_wifibt_fi.html"
---

# Wi-Fi-, Bluetooth- ja FM-radion asetukset: Reborn (Y2Linux) - Innioasis Päivitys

Innioasis Y2 · Reborn Asennuksen jälkeen

# Määritä Wi-Fi, Bluetooth ja FM-radio.

Kopioi yksi tiedosto soittimellesi. Reborn hoitaa loput.[Lataa system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Asennusopas](guides/reborn-y2linux-y2.html)[Miksi Y2Reborn?](reborn-y2linux-benefits_fi.html)

## Miksi tämä tiedosto?

Wi-Fi, Bluetooth ja FM-radio tarvitsevat viisi MediaTek laiteohjelmistomoduulia, joita Reborn ei voi toimittaa. He ovat virallisessa Y2 `system.img`. Reborn purkaa ne kerran, tarkistaa ne ja poistaa tiedoston.

## Asennus
  - Lataa system.img

Lataa v3.2.0 FM `system.img` tietokoneellesi.[ Lataa system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Käynnistä Reborn kerran

Kytke soitin päälle. Odota Tallennustilan määrittäminen loppuun, ja käynnistä se sitten uudelleen kerran.
  - Yhdistä tietokoneeseen

Käytä USB-datakaapelia. Soitin näkyy muodossa Sisäinen tallennustila.Macilla?

Asenna [OpenMTP](https://openmtp.ganeshrvel.com/) selataksesi soitinta. Windows ja Linux asentavat sen automaattisesti.
  - Kopioi system.img laiteohjelmistoon

Luo kansio nimeltä `Firmware` sisäisen tallennustilan juurella. Kopioi `system.img` siihen.
  - Odota, että asennus on valmis

Reborn asentaa radion laiteohjelmiston automaattisesti ja poistaa `system.img`. Tämä kestää noin 10-20 sekuntia. Odota Wi-Fi ja Bluetooth ovat valmiina.
  - Yhdistä Wi-Fi, Bluetooth ja FM-radio
    - Wi-Fi: Asetukset → Järjestelmä → Verkko → Wi-Fi. Valitse 2,4 GHz:n verkko.
    - Bluetooth: Aseta kuulokkeet pariliitostilaan. Asetukset → Bluetooth → valitse ne.
    - FM-radio: Liitä langalliset kuulokkeet antenniksi ja avaa sitten FM-radio.

  - Päivitä Wi-Fin kautta

Tulevat Reborn-päivitykset asennetaan kohdasta Asetukset → Järjestelmä → Ohjelmistopäivitys. Radiosi laiteohjelmisto pysyy paikallaan.

## Oliko tästä oppaasta apua?

Oliko tästä asennuksen jälkeisestä asennusoppaasta apua? Kyllä, se auttoi! [ Tarvitsen apua Discord ](https://discord.gg/zHrT2zrcek) Kiitos palautteestasi! Nauti langattomasta kuuntelusta Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
