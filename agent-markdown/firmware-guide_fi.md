---
title: "Laiteohjelmiston asennus- ja palautusopas | Innioasis Updater CE - Innioasis Laiteohjelmistolataukset"
description: "Asenna mukautettu laiteohjelmisto tai palauta virallinen tehtaan laiteohjelmisto Innioasis Y1, Y2, G1, G3, G5, R1, PR1 ja Timmkoo Q5, Q3 Innioasis Updater CE:n avulla."
language: "fi"
source: "https://innioasis.app/firmware-guide_fi.html"
---

# Laiteohjelmiston asennus- ja palautusopas | Innioasis Updater CE - Innioasis Laiteohjelmistolataukset

Laiteohjelmiston asennus- ja palautusopas

# Asenna tai palauta laiteohjelmisto laitteellesi

Valitse soittimeen painettu malli. Noudata sitten Updater CE:n ohjeita. Se hoitaa loput.[Hanki Updater CE](guide_fi.html#platform)[Selaa laiteohjelmistoarkistoa](firmware_fi.html)[Vianetsintä](troubleshooting_fi.html)

Valitse soittimeen painettu malli ja haluamasi ohjelmisto ja avaa sitten tämä opas. [Selaa ohjelmistoja ja laiteohjelmistoja mallin mukaan](firmware_fi.html).

## 

[Hanki Updater CE](guide_fi.html#download-updater)[Koko kirjallinen opetusohjelma](guide_fi.html)

## Hanki Innioasis Updater CE

Aloita tästä, jos sinulla ei vielä ole Updater CE:tä.Hanki se Updater CE:lläohjatulla asennuksella

### Windows

Lataa asennusohjelma, avaa se ja seuraa asennusohjeita.[Lataa ja asenna ohjain](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Lataa sovellus ja ajurit](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Edge estänyt?](#)

Jos Windows estää sinua suorittamasta sovellusta tai ei käynnistä sitä, avaa Asetukset, napsauta Tietosuoja ja suojaus → Windowsin suojaus → Sovellusten ja selaimen hallinta ja kytke Smart App Control pois päältä. [Windows ei käynnistä sovellusta? Auttaa](#smart-app-control)

Sinun on käynnistettävä tietokoneesi uudelleen asennuksen jälkeen, jotta se toimii.

### macOS

Lataa sovellus ja siirrä se Sovellukset-kohtaan. Jos macOS estää sen, avaa Järjestelmäasetukset, sitten Tietosuoja ja suojaus ja napsauta Avaa silti. [Miten tämä toimii](https://support.apple.com/en-gb/102445#openanyway)[Lataa Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Lataa AppImage Intel- ja AMD-järjestelmille, tee siitä suoritettava ja suorita se.[Lataa AppImage Intel/AMD:lle](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Linuxin asennusohjeet](drivers_fi.html#linux)Toinen alusta?

Tarvitsetko pidemmät tietokoneen asennusohjeet? Avaa [Windows](drivers_fi.html#windows) tai [Linux](drivers_fi.html#linux) asennusopas.

## Paluu alkuperäiseen ohjelmistoon

Palaa takaisin valitsemalla mallisi, valitsemalla Alkuperäinen ohjelmisto, juokse sitten Asenna / Palauta. Siinä kaikki. Updater korvaa järjestelmäohjelmiston puolestasi.[Y1 palautusopas](guides/restore-original-y1.html)[Y2 palautusopas](guides/restore-original-y2.html)

## Ohjelmisto-oppaat malleittain

Valitse mallisi ja avaa sitten ohjelmistosi opas.

### Innioasis Y1

Ohjelmisto Y1:

### Innioasis Y2

Ohjelmisto Y2:

Huomautus kahdesta työkalusta

## Mitä työkalua minun pitäisi käyttää?

Innioasis Päivittäjä CE on turvallisin tapa päivittää soittimesi. Se säilyttää musiikkisi, videosi ja Bluetooth-pariliitokset. Se kertoo, kun päivitykset ovat valmiita. Se toimii Windowsissa, macOS:ssä ja Linuxissa. Innioasis Universal Flash Tool pyyhkii soittimesi ja toimii harvemmilla tietokoneilla.[Avaa koko vertailu](updater-comparison_fi.html)

### Windows ei käynnistä sovellusta? Kuinka sammuttaa Smart App Control

Windows Defender SmartScreen tai Smart App Control voivat estää äskettäin ladatut yhteisösovellukset ennen kuin allekirjoituksen maine leviää. Smart App Control vaikuttaa tällä hetkellä suosittuihin sovelluksiin, kuten Epic Overlay Service (Fortniten käyttämä) – Updater CE on turvallinen ja varmennettu käytettäväksi. Smart App Controlin kytkeminen pois päältä sallii Updater CE:n avautua ja toimia normaalisti.
  - Avaa Asetukset Windows-tietokoneellasi (paina Win + I).
  - Napsauta Yksityisyys ja turvallisuus vasemmassa sivupalkissa ja napsauta sitten Windows Security.
  - Napsauta Sovellusten ja selaimen hallinta.
  - Under Smart App Control, napsauta Smart App Control -asetukset.
  - Aseta kytkin asentoon Pois sallia Updater CE:n käynnistymisen.

Edge estänyt? Jos Microsoft Edge estää itse latauksen, napsauta Lisää vaihtoehtoja -painiketta (…) → Pidä → Näytä lisää → Pidä joka tapauksessa.

Smart App Controlin ottaminen uudelleen käyttöön myöhemmin: Kun haluat ottaa Smart App Controlin takaisin käyttöön, voit ottaa sen uudelleen käyttöön alla olevan Windowsin rekisterin kautta `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` asettamalla `VerifiedAndReputablePolicyState` to `1` (Päällä) tai `2` (Evaluation Mode) ja käynnistä uudelleen.Sulje ohje

## Oliko tästä hyötyä?

Vastauksesi auttaa parantamaan tätä opasta.Kyllä, pidin siitä hyödyllistäEi vielä[Kerro meille, kuinka voimme parantaa](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
