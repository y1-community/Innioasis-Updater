---
title: "Configurare Wi-Fi, Bluetooth și Radio FM pentru Reborn (Y2Linux) - Innioasis Updater"
description: "Scurt ghid post-instalare pentru Reborn (Y2Linux / Y2Reborn) pe Innioasis Y2: copiați system.img, apoi configurați Wi-Fi, Bluetooth și radio FM."
language: "ro"
source: "https://innioasis.app/y2reborn_wifibt_ro.html"
---

# Configurare Wi-Fi, Bluetooth și Radio FM pentru Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Post-instalare

# Configurați Wi-Fi, Bluetooth și radio FM.

Copiați un fișier pe player. Reborn se ocupă de restul.[Descărcați system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Ghid de instalare](guides/reborn-y2linux-y2.html)[De ce Y2Reborn?](reborn-y2linux-benefits_ro.html)

## De ce acest fisier?

Wi-Fi, Bluetooth și radioul FM au nevoie de cinci module de firmware MediaTek pe care Reborn nu le poate livra. Sunt în interiorul Y2 oficial `system.img`. Reborn le extrage o dată, le verifică și șterge fișierul.

## Configurare
  - Descărcați system.img

Descărcați v3.2.0 FM `system.img` la computerul dvs.[ Descărcați system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Porniți Reborn o dată

Porniți playerul. Așteaptă Configurarea stocării pentru a termina, apoi reporniți-l o dată.
  - Conectați-vă la computer

Utilizați un cablu de date USB. Jucătorul apare ca Stocare internă.Pe un Mac?

Instalați [OpenMTP](https://openmtp.ganeshrvel.com/) pentru a naviga pe player. Windows și Linux îl montează automat.
  - Copiați system.img în Firmware

Creați un folder numit `Firmware` la rădăcina stocării interne. Copiere `system.img` în ea.
  - Așteptați ca configurarea să se termine

Reborn instalează automat firmware-ul radio și îl șterge `system.img`. Acest lucru durează aproximativ 10-20 de secunde. Așteaptă Wi-Fi și Bluetooth sunt gata.
  - Conectați Wi-Fi, Bluetooth și radio FM
    - Wifi: Setări → Sistem → Rețea → Wi-Fi. Alegeți rețeaua dvs. de 2,4 GHz.
    - Bluetooth: Pune căștile în modul de asociere. Setări → Bluetooth → selectați-le.
    - Radio FM: Conectați căștile cu fir ca antenă, apoi deschideți Radio FM.

  - Actualizați prin Wi-Fi

Actualizările viitoare Reborn se instalează din Setări → Sistem → Actualizare software. Firmware-ul radioului tău rămâne pe loc.

## A fost util acest ghid?

Ți s-a părut util acest ghid de configurare după instalare? Da, a ajutat! [ Am nevoie de ajutor pe Discord ](https://discord.gg/zHrT2zrcek) Vă mulțumim pentru feedback! Bucurați-vă de ascultarea fără fir pe Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
