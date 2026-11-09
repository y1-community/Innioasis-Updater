---
title: "Konfiguracja Wi-Fi, Bluetooth i radia FM dla Reborn (Y2Linux) - Innioasis Aktualizacja"
description: "Krótka instrukcja poinstalacyjna dla Reborn (Y2Linux / Y2Reborn) na Innioasis Y2: skopiuj plik system.img, a następnie skonfiguruj Wi-Fi, Bluetooth i radio FM."
language: "pl"
source: "https://innioasis.app/y2reborn_wifibt_pl.html"
---

# Konfiguracja Wi-Fi, Bluetooth i radia FM dla Reborn (Y2Linux) - Innioasis Aktualizacja

Innioasis Y2 · Reborn Po instalacji

# Skonfiguruj Wi-Fi, Bluetooth i radio FM.

Skopiuj jeden plik do odtwarzacza. Reborn zajmuje się resztą.[Pobierz system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Przewodnik instalacji](guides/reborn-y2linux-y2.html)[Dlaczego Y2Reborn?](reborn-y2linux-benefits_pl.html)

## Dlaczego ten plik?

Wi-Fi, Bluetooth i radio FM wymagają pięciu MediaTek modułów oprogramowania sprzętowego, których Reborn nie może dostarczyć. Znajdują się one w oficjalnym Y2 `system.img`. Reborn wyodrębnia je raz, sprawdza i usuwa plik.

## Organizować coś
  - Pobierz system.img

Pobierz wersję 3.2.0 FM `system.img` do swojego komputera.[ Pobierz system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Uruchom Reborn raz

Włącz odtwarzacz. Czekać na Konfigurowanie magazynu aby zakończyć, a następnie uruchom ponownie raz.
  - Połącz się z komputerem

Użyj kabla do transmisji danych USB. Gracz pojawia się jako Pamięć wewnętrzna.Na Macu?

Zainstaluj [OtwórzMTP](https://openmtp.ganeshrvel.com/) przeglądać odtwarzacz. Windows i Linux montują go automatycznie.
  - Skopiuj plik system.img do oprogramowania sprzętowego

Utwórz folder o nazwie `Firmware` w katalogu głównym pamięci wewnętrznej. Kopia `system.img` w to.
  - Poczekaj na zakończenie konfiguracji

Reborn automatycznie instaluje oprogramowanie radia i usuwa je `system.img`. Zajmuje to około 10–20 sekund. Czekać na Wi-Fi i Bluetooth są gotowe.
  - Podłącz Wi-Fi, Bluetooth i radio FM
    - Wi-Fi: Ustawienia → System → Sieć → Wi-Fi. Wybierz sieć 2,4 GHz.
    - Bluetooth: Przełącz słuchawki w tryb parowania. Ustawienia → Bluetooth → wybierz je.
    - Radio FM: Podłącz słuchawki przewodowe jako antenę, a następnie otwórz Radio FM.

  - Aktualizuj przez Wi-Fi

Przyszłe aktualizacje Reborn instaluje się z Ustawienia → System → Aktualizacja oprogramowania. Oprogramowanie sprzętowe radia pozostaje niezmienione.

## Czy ten przewodnik był pomocny?

Czy ten przewodnik konfiguracji po instalacji był dla Ciebie pomocny? Tak, pomogło! [ Potrzebujesz pomocy w sprawie Discord ](https://discord.gg/zHrT2zrcek) Dziękujemy za Twoją opinię! Ciesz się bezprzewodowym słuchaniem na Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
