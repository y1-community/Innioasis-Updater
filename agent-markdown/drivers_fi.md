---
title: "Innioasis Y1 ja Y2 USB kuljettajat | Windows-ohjain ja Linux-käyttöoikeudet - Innioasis Updater"
description: "Määritä tietokoneellesi Innioasis Updater: Windows MediaTek-ohjain ja Linuxin USB käyttöoikeudet – sekä kaapeli- ja ajoituskorjaukset."
language: "fi"
source: "https://innioasis.app/drivers_fi.html"
---

# Innioasis Y1 ja Y2 USB kuljettajat | Windows-ohjain ja Linux-käyttöoikeudet - Innioasis Updater

Tietokoneen asetukset

# Valmistele tietokone ennen soitinta.

Useimmat yhteysongelmat johtuvat ohjaimesta, käyttöoikeuksista, kaapelista tai ajoituksesta. Windows tarvitsee MediaTek-ohjaimen asennettuna. Linux tarvitsee oikeat USB käyttöoikeudet. Etsi alustasi alta.[Hanki Updater CE](guide_fi.html#platform)[Vianetsintä](troubleshooting_fi.html)

## Windows
  - Lataa MediaTek ohjaimen asennusohjelma alta.
  - Suorita asennusohjelma ja anna Windowsin asentaa ohjain.
  - Käynnistä tietokone uudelleen.
  - Avaa Updater CE ja odota yhdistämiskehotetta, ennen kuin kytket pois päältä kytketyn soittimen.

Jotkut Windows-järjestelmät estävät ohjaimen Core-eristyksen (muistin eheyden) avulla. Jos Updater CE ei vieläkään näe soitinta uudelleenkäynnistyksen jälkeen, poista Muistin eheys käytöstä Windowsin suojauksessa, käynnistä uudelleen ja asenna ohjain uudelleen. Kytke asetus takaisin päälle, kun olet valmis, jos järjestelmäsi sallii sen.

Windows ei käynnistä sovellusta? Jos Windows Security tai Smart App Control estää Updater CE:tä avautumasta, avaa Asetukset (paina Win + I) → Yksityisyys ja turvallisuus → Windows Security → Sovellusten ja selaimen hallinta → Smart App Control -asetukset ja aseta se päälle Pois. Smart App Control vaikuttaa tällä hetkellä suosittuihin sovelluksiin, kuten Epic Overlay Service (Fortniten käyttämä) – Updater CE on turvallinen ja varmennettu käytettäväksi. Ota käyttöön myöhemmin uudelleen määrittämällä `VerifiedAndReputablePolicyState` to `1` (Päällä) tai `2` (Arviointitila) alla `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` Rekisterieditorissa.[Lataa Windows-ohjain](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Takaisin pääoppaaseen](guide_fi.html#windows) · [Ohjelmiston lataukset](firmware_fi.html)

## Linuxin USB käyttöoikeudet

Linux tarvitsee käyttäjätunnuksesi voidakseen puhua soittimen sisällä olevan MediaTek USB-sirun kanssa. Updater CE yleensä selvittää tämän asennuksen aikana, ja sama lupa kattaa SP Flash Tool, joten pidä tätä korjausvaiheena normaalin vaiheen sijaan.
  - Suorita Updater CE tavallisena käyttäjänäsi, ei pääkäyttäjänä. Asennusohjelma pyytää järjestelmänvalvojan käyttöoikeuksia vain silloin, kun se tarvitsee sitä.
  - Tarkista, näkyykö soitin ollenkaan. Katkaise soittimesta virta, kytke kaapeli ja suorita lsusb-komento liittimessä. Yhdistetty soitin näkyy MediaTek-laitteena, jonka toimittajatunnus on 0e8d.
`lsusb`
  - Jos se näkyy lsusb:ssä, mutta Innioasis Updater CE tai SP Flash Tool sanoo, että lupa on estetty tai ei voi avata porttia, käyttäjältä puuttuu pääsy USB-laitteeseen. Sama udev-sääntö kattaa molemmat työkalut, joten lisää yksi, jonka avulla käyttäjäryhmät voivat lukea sen.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Tallenna tämä rivi uuteen tiedostoon nimeltä /etc/udev/rules.d/51-innioasis.rules ja suorita:`sudo udevadm control --reload && sudo udevadm trigger`
  - Irrota soitin kokonaan, kytke se takaisin ja yritä asennusta uudelleen.
  - Jos SP Flash Tool ilmoittaa sarjaluvasta tai porttikilpailusta, irrota pistoke kokonaan ja yhdistä uudelleen vain pyydettäessä.
Älä improvisoi salamapoikkeamia.Jos siirryt manuaaliseen palautustyökaluun, käytä projektin mukana toimitettuja tiedostoja ja mallikohtaisia määrityksiä.

[Takaisin pääoppaaseen](guide_fi.html#linux) · [Ohjelmiston lataukset](firmware_fi.html) · [SP Flash Tool opas](sp-flash-tool_fi.html)

## Kaapeli ja ajoitus
  - Käytä tunnettua USB datakaapelia.
  - Vältä keskittimiä vianmäärityksen aikana.
  - Oikean mallin virta kokonaan pois päältä.
  - Yhdistä vain kehotteessa.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
