---
title: "Käynnistymättömän MediaTek-soittimen palauttaminen MTKclient-vian jälkeen · Innioasis Yhteisö"
description: "Vaiheittainen opas ei-käynnistyvien Innioasis Y1-, Y2-, G1-, Timmkoo- ja MediaTek-soittimien poistamiseen ja palauttamiseen sen jälkeen, kun MTKclient keskeytti flash-osion Linuxissa tai macOS:ssä."
language: "fi"
source: "https://innioasis.app/recover-non-booting-device_fi.html"
---

# Käynnistymättömän MediaTek-soittimen palauttaminen MTKclient-vian jälkeen · Innioasis Yhteisö

Vianetsintä ja laitteen palautus

# Käynnistymättömän laitteen palauttaminen MTKclientin vilkkumisen jälkeen

Jos Innioasis Y1-, Y2- tai MediaTek-laitteesi ei käynnisty tai näyttää mustan näytön vilkkuttuaan MTKclientin kanssa macOS- tai Linux-käyttöjärjestelmässä, älä panikoi. Laitteiston BootROM (BROM) on pysyvä, eikä sitä voi tuhota.

## Miksi MTKclient voi pysähtyä tai jättää mustan näytön?

MTKclient luottaa ohjelmiston hyötykuormiin (kamakiri / amonet) ohittaakseen DA-todennuksen ja raaka USB-viestinnän libusbin kautta. MacOS- ja Linux ARM64 -järjestelmissä:
  - USB kättelyn viive tai portin aikakatkaisut macOS:ssä voivat keskeyttää DA:n hyötykuorman lisäyksen kesken siirron.
  - Puuttuvat tai epätäydelliset osion otsikot jättävät käynnistyslataimen (preloader / lk) reagoimattomaan tilaan.
  - Soitin näyttää täysin kuolleelta – ei LEDiä, ei latauskuvaketta, ei näytön taustavaloa.

Jopa tässä tilassa MediaTek-piirisarja putoaa takaisin BROM-tila (USB VID 0e8d, PID 0003), valmis viralliseen matalan tason palautukseen.

## Lopullinen palautusmenetelmä: SP Flash Tool Moottori Updater CE:ssä

Turvallisin ja luotettavin tapa palauttaa muurattu soitin on käyttää Päivittäjä CE virkamiehen kanssa määritettynä SP Flash Tool tausta.

### Tarkat vaiheet Updater CE:ssä:
  - Avaa Päivittäjä CE.
  - Napsauta Asetukset vasemmassa navigointisivupalkissa.
  - Vieritä alas Lisäasetukset-osioon ja ota se käyttöön Näytä lisäasetukset.
  - Under Asennusmenetelmä (tai Vilkkuu moottori MediaTek asentajalle), etsi Flash-menetelmä pudotusvalikosta.
  - Muuta valintaa Automaattinen (suositus) tai MTKClient to SP Flash Tool.
  - Vahvista kehote ja palaa pääasennusprosessiin.

## Alustan arkkitehtuuri ja käyttöjärjestelmävaatimukset SP Flash Tool

MediaTek:n virkamies `SP Flash Tool` binääri on käännetty natiivimuodossa an x86_64 ELF-binaari Linuxille ja a PE32+ suoritettava Windows x64:lle.Tärkeä laitteistohuomautus macOS- ja ARM64 Linux -käyttäjille:
 Koska MediaTek ei käännä SP Flash Tool macOS:lle (Darwin) tai Linux ARM64:lle (aarch64), macOS-käyttäjien ja ARM64 Linux -käyttäjien (kuten Raspberry Pi tai Apple Silicon, jossa on Asahi Linux) täytyy yhdistää soitin: 
  - An x64 Windows PC (Windows 10/11 64-bittinen) tai
  - An x86_64 Linux PC (Ubuntu, Debian, Fedora, Arch 64-bittinen).

## Vaiheittainen laitteiston poistamisprosessi
  - Irrota soitin: Irrota USB-kaapeli soittimesta ja tietokoneesta kokonaan.
  - Kova virrankatkaisu: Pidä virtapainiketta (tai virtapainiketta + äänenvoimakkuuden vähennyspainiketta) painettuna 15 sekuntia varmistaaksesi, että piirisarjan virta on katkaistu kokonaan eikä se juuttunut vähätehoiseen USB-silmukkaan.
  - Käynnistä Updater CE SP Flash Tool-tilassa: Valitse laitteesi malli (esim. Innioasis Y1 tai Innioasis Y2) ja valitse Alkuperäinen ohjelmisto palauttaaksesi varastoosioita.
  - Aloita asennus/palautus: Napsauta Asenna / Palauta Updater CE:ssä. Odota, kunnes tilakehote sanoo Pelaajaa odotellessa...
  - Liitä USB kaapeli käynnistämään BROM:in: Kun laite on pois päältä, kytke USB-kaapeli suoraan nopeaan emolevyn USB-porttiin (vältä virrattomia USB-keskittimiä).
  - Järjestelmä tunnistaa MediaTek VCOM-portin, työntää latausagentin (DA), kirjoittaa uudelleen osiotaulukot ja palauttaa kaikki laiteohjelmistokuvat puhtaasti.

## Permutaatiot mallin ja käyttöjärjestelmän mukaan

| Malli | Epäonnistunut alusta | Suositeltu palautusasetus | Moottori ja tila |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y1 Osake ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 tai Windows x64 PC | SP Flash Tool + Yhteisön DA |
| Innioasis Y2 | macOS (MTK-asiakas pysähtynyt) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y2 Scatter Recovery |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 PC VCOM-ajureilla | SP Flash Tool + Tehdasohjelmisto |
| Mechen H1 / Timmkoo A5 | Mikä tahansa alusta | Windows x64 tai Linux x86_64 PC | SP Flash Tool + Scatter-tiedosto |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
