---
title: "SP Flash Tool Innioasis ja Timmkoo pelaajille"
description: "Etsi SP Flash Tool mukana Innioasis Updater Windowsissa ja Linuxissa, pura rom.zip tai rom_y2.zip ja flash-tiedosto Innioasis Y1 tai Y2 vastaavalla scatter-tiedostolla."
language: "fi"
source: "https://innioasis.app/sp-flash-tool_fi.html"
---

# SP Flash Tool Innioasis ja Timmkoo pelaajille

Manuaalinen vilkkuminen

# Flash-työkalu Innioasis- ja Timmkoo-soittimille

SP Flash Tool tulee sisään Innioasis Päivitys päällä [Windows](drivers_fi.html#windows) ja [Linux](drivers_fi.html#linux). Sinulla on jo se. Tämä opas näyttää turvallisen tavan käyttää sitä Innioasis Y1- tai Y2-pelissä sekä Updater-reitin Timmkoo-pelaajille.[Palaa Updater-oppaaseen](guide_fi.html)[Laiteohjelmiston lataukset](firmware_fi.html)[Vianetsintä](troubleshooting_fi.html)

Aloita Innioasis Updater

## Updater tekee koko työn yhdellä kertaa

Updater suorittaa useimmat asennukset yhdellä kertaa. Valitse ohjelmisto, seuraa ohjeita ja olet valmis. Se kertoo myös, kun korjaus tai uusi julkaisu saapuu. SP Flash Tool on Updater's Toolkitissä niitä harvinaisia ​​tapauksia varten, joita Updater ei voi suorittaa loppuun. Alla olevat vaiheet ovat poikkeus.

## Mihin tämä työkalu on tarkoitettu

Updater vilkkuu soittimen puolestasi. SP Flash Tool on sama moottori ilman suojakaiteita. Käytä sitä, kun Updater ei käynnisty, kun soitin ei muodosta yhteyttä tai kun tiedät kulkusi hajontatiedostossa.Kokeile ensin Updateria. Useimmissa asennuksissa ja palautuksissa on opastettu [Päivittäjän reitti](guide_fi.html) on turvallisempi valinta. Käytä SP Flash Tool, kun tiedät, miksi tarvitset sitä, ja pidä ladattu akku ja USB datakaapeli valmiina.

## Flash-työkalu Innioasis pelaajille

Innioasis Updater on flash-työkalu Innioasis pelaajille. Se asentaa virallisia ohjelmistoja, päivittää ja palauttaa paketteja mallin mukaisen virran kautta ja säilyttää musiikkisi ja asetuksesi.

### Innioasis Y1 flash-työkalu

Valitse Y1-julkaisu Updaterissä ja yhdistä sitten sammutettu soitin, kun sovellus pyytää. Samat Y1-paketit toimivat SP Flash Tool:n kanssa, kun tarvitset manuaalista reittiä.

### Innioasis Y2 flash-työkalu

Valitse luettelosta julkaisu Y2. Y2-paketit eivät ole keskenään vaihdettavissa Y1-pakettien kanssa, joten tarkista malli ennen aloittamista.

## Flash-työkalu Timmkoo pelaajille

Timmkoo pelaajat käyttävät samaa Updater-asennuskulkua. Se lukee Timmkoo:n ZIP- ja RAR-paketit suoraan, joten et tarvitse erillistä flash-työkalua tai scatter-tiedostoa.

### Timmkoo Q5 flash-työkalu

Valitse Q5-malli Updaterissä, valitse Timmkoo-paketti, suorita Asenna/Palauta ja liitä soitin kehotteessa.

### Timmkoo Q3 ja Q3E flash-työkalu

Q3-merkintä kattaa sekä Q3 että Q3E. Updater poimii vastaavat tiedostot projektin julkaisemasta paketista.

### Timmkoo A5 flash-työkalu

Valitse malli A5 ennen paketin valitsemista ja noudata sitten samaa asennuskehotetta.

## Minne Updater sen laittaa

SP Flash Tool toimitetaan Updater-asennuskansion mukana, ei erillisenä latauksena. Avaa se sieltä, kun tarvitset sitä.

### Windows

Avaa Updater-asennuskansio ja suorita `flash_tool.exe`. Kansio on yleensä alla `%LOCALAPPDATA%\Innioasis Updater`. Joihinkin asetuksiin sisältyy Toolkit-kansio, jossa on SP Flash Tool-pikakuvake.

### Linux

Suorita paketti `flash_tool` binaaritiedosto Updater-sovelluskansiossa x86 / x86_64:ssä. Projektin asennusohjelma valmistelee USB käyttöoikeudet udev-säännöillä, joten soittimen pitäisi ilmestyä, kun se on yhdistetty.

### macOS

SP Flash Tool ei ole mukana macOS:ssä. Updater käyttää sen sijaan MTKClient reittiä siellä. Käytä [ohjattu asennus](guide_fi.html) Macissa ja säilytä SP Flash Tool Windows- tai Linux-konetta varten.

Työkalu toimitetaan MediaTek latausagentin ja mallikohtaisen kokoonpanon kanssa, joten sinun ei tarvitse kerätä DA- tai hajottaa tiedostoja muualta.

## Valmistele laiteohjelmisto
  - Nappaa haluamasi julkaisu [Laiteohjelmiston lataukset](firmware_fi.html). Valitse `rom.zip` Y1 tai `rom_y2.zip` Y2:lle.
  - Pura ZIP omaan kansioonsa. Windows voi käyttää Pura kaikki. Linuxissa käytä arkiston hallintaa tai `unzip` terminaalissa.
  - Tarkista, että scatter-tiedosto on puretussa kansiossa. Se on yleensä nimetty `MT6572_Android_scatter.txt` Y1 paketeille ja `MT6582_Android_scatter_def.txt` Y2-paketeille, vaikka julkaisu voi nimetä sen projektin mukaan.
Pidä mallit erillään. Scatter Y1 kuvaa MT6572-laitetta ja Y2-hajonta kuvaa MT6582-laitetta. Vilkkuminen väärällä on se, kuinka pelaajat muurataan. Jos ZIP:n sisällä oleva hajonta ei vastaa malliasi, lopeta ja käytä sen sijaan mallillesi listattua pakettia.

## Lataa hajonta ja salama
  - Avaa SP Flash Tool Updater-asennuskansiosta.
  - Napsauta Lataa-välilehdellä Valitse Scatter-loading File -kohdan vieressä ja valitse hajontatiedosto puretusta kansiosta. Osioluettelo täyttyy.
  - Jätä salamatila päälle Vain lataus ellet tee tarkoituksella täydellistä toipumista, mikä vaatii Laiteohjelmiston päivitys.
  - Napsauta Lataa. Työkalu odottaa pelaajaa.
  - Virta soittimesta täysin pois päältä ja liitä sitten USB-datakaapeli. Aseta soitin alas äläkä liikuta sitä.
  - Odota vihreää valintamerkkiä. Vasta sitten irrota kaapeli ja käynnistä soitin.

Säilytä samat USB-kaapeli- ja ajoitussäännöt kuin opastetulla reitillä: datakaapeli, ei keskitintä, ja yhdistä vasta, kun työkalu on valmis.

## Jos se ei vilku
  - Tarkista, että scatter ja ZIP vastaavat soittimeen painettua mallia.
  - Varmista, että soittimen virta on katkaistu kokonaan ennen liittämistä.
  - Windowsissa vahvista MediaTek-ohjain asennettuna Updater-asennuksen yhteydessä; Linuxissa, vahvista udev-säännöt projektin asennusohjelmasta.
  - Kytke kaapeli takaisin vain, kun työkalu odottaa. Porttikilpailu voi vaatia täyden irrotuksen ja uuden Lataa napsauta.

Kaikessa sen lisäksi, avoin [vianetsintä](troubleshooting_fi.html). Ja muista: Updater on edelleen normaali reitti, ja [Y1](guides/restore-original-y1.html) ja [Y2](guides/restore-original-y2.html) myös palautusoppaat käyttävät sitä.

## Oliko tästä hyötyä?

Vastauksesi auttaa parantamaan tätä opasta.Kyllä, pidin siitä hyödyllistäEi vielä[Kerro meille, kuinka voimme parantaa](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
