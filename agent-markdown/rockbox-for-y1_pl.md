---
title: "Rockbox dla Y1 (Rockbox-Y1): przegląd, kompilacje i przewodnik instalacji"
description: "Rockbox dla Y1, Rockbox-Y1 i rockbox-y1 odnoszą się do oprogramowania sprzętowego społeczności Rockbox dla Innioasis Y1. Dowiedz się, co dodaje, jaką kompilację wybrać i jak ją zainstalować za pomocą Innioasis Updater CE."
language: "pl"
source: "https://innioasis.app/rockbox-for-y1_pl.html"
---

# Rockbox dla Y1 (Rockbox-Y1): przegląd, kompilacje i przewodnik instalacji

[← Pobieranie oprogramowania sprzętowego](firmware_pl.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox dla Y1 (Rockbox-Y1)

„Rockbox”, „Rockbox-Y1” i „Rockbox dla Y1” odnoszą się do tego samego oprogramowania społecznościowego Rockbox dla Innioasis Y1. Oto, co dodaje do odtwarzacza, jaką kompilację wybrać i jak ją zainstalować za pomocą Innioasis Updater CE.[Zainstaluj Rockbox-Y1](rockbox-y1/install.html)[Pobierz ROM](rockbox-y1/download.html)[Napisany poradnik](guides/rockbox-y1.html)[Rockbox-Piasta Y1](rockbox-y1/)

## Jedno oprogramowanie, kilka nazw

W Innioasis Updater CE to oprogramowanie pojawia się jako Rockbox po wybraniu modelu urządzenia Y1. Przewodniki, filmy i informacje o wydaniu również to nazywają Rockbox-Y1 lub Rockbox dla Y1 więc jest jasne, że kompilacja dotyczy Y1, a nie Y2.

Przed instalacją zawsze sprawdź model wydrukowany na odtwarzaczu: Pakiety oprogramowania sprzętowego Y1 i Y2 nie są zamienne.

## Co Rockbox-Y1 dodaje do Twojego Y1

Rockbox-Y1 to port społecznościowy oprogramowania sprzętowego odtwarzacza muzycznego Rockbox o otwartym kodzie źródłowym dla Innioasis Y1:
  - Biblioteka muzyczna oparta na tagach — przeglądaj według wykonawcy, albumu, gatunku i roku za pomocą znaczników audio lub bezpośrednio przeglądaj foldery.
  - Zaawansowane odtwarzanie dźwięku — odtwarzanie bez przerw, przenikanie, funkcja ReplayGain i pełny korektor.
  - Niestandardowe motywy — wybieraj spośród setek motywów społecznościowych w rozdzielczości 240p i 360p, w tym klasycznych układów w stylu iPoda.
  - Radio FM — wbudowana obsługa radia FM.
  - Opcjonalne dodatki — pobieranie podcastów przez Wi-Fi i przeglądanie Last.fm / ListenBrainz / Maloja w obsługiwanych kompilacjach.
  - Podwójny rozruch — przywróć oryginalne oprogramowanie fabryczne bez konieczności ponownego flashowania w obsługiwanych wersjach.

## Którą Y1 kompilację powinienem wybrać?
  - 240p kontra 360p — Kompilacje 240p działają z klasycznymi motywami 320×240 Rockbox; W kompilacjach 360p używane są ostrzejsze motywy 480×360 Y1. Dopasuj rozdzielczość kompilacji do motywów, których chcesz użyć ([Przewodnik po rozdzielczości 240p i 360p](rockbox-y1/resolution.html)).
  - Type A kontra Type B — Type A dotyczy odtwarzaczy Y1 dostarczonych z oprogramowaniem fabrycznym w wersji 2.0.0 lub nowszej; Type B dotyczy wcześniejszych Y1 jednostek. Wybierz Type A, chyba że wiesz, że twoje Y1 to Type B.
  - Stabilne vs. nocne — Wybierz stabilną wersję do codziennego słuchania lub wersję nocną, aby przetestować najnowsze zmiany.

## Bezpośrednie pliki do pobrania od twórców społeczności

Innioasis Updater CE zawsze pobiera pakiety oprogramowania bezpośrednio od twórców oprogramowania sprzętowego społeczności ([rockbox-y1/rockbox](firmware_pl.html?model=Y1&software=rockbox-y1)), a sami programiści ponoszą wyłączną odpowiedzialność za umieszczanie wydań swoich programów w serwisie Updater CE.

Możesz pozwolić Updaterowi CE na automatyczne pobranie i zainstalowanie oprogramowania sprzętowego lub pobrać pakiety ROM z naszego [Rockbox-Y1 strona pobierania](rockbox-y1/download.html) i [Rockbox ROM strona pobierania](rockbox-rom-download_pl.html).[Rockbox-Y1 pobrań](rockbox-y1/download.html)[Zainstaluj z lokalnego pliku ZIP](rockbox-y1/portable-zip.html)

## Jak zainstalować Rockbox-Y1
  - Otwórz Innioasis Updater CE i ustaw Model urządzenia do Y1.
  - Wybierz Rockbox w Oprogramowanie.
  - Wybierz stabilną wersję (lub włącz nocne kompilacje, aby przetestować podgląd).
  - Kliknij Zainstaluj / Przywróć dlatego Updater CE pobiera pakiet bezpośrednio od programisty.
  - Całkowicie wyłącz urządzenie Y1 i podłącz je za pomocą kabla do transmisji danych USB, gdy program Updater CE wyświetli monit.
  - Poczekaj na komunikat o zakończeniu, a następnie odłącz i włącz odtwarzacz.

Aby uzyskać zrzuty ekranu i szczegółowe wskazówki dotyczące konfiguracji, przeczytaj [pełny Rockbox-Y1 samouczek](guides/rockbox-y1.html).

## Przywracanie oryginalnego oprogramowania Y1.

W każdej chwili możesz wrócić do oprogramowania fabrycznego: wybierz Y1 i Oprogramowanie oryginalne w Updater CE wybierz wersję stabilną i kliknij Zainstaluj / Przywróć. Twoja muzyka na karcie MicroSD zostanie zachowana. Zobacz [przewodnik przywracania](rockbox-y1/restore-stock.html) i [Y1 Strona oryginalnego oprogramowania](original-software-y1_pl.html).

## Często zadawane pytaniaCzy Rockbox dla Y1 jest takie samo jak Rockbox-Y1?

Tak. Rockbox, Rockbox-Y1, Rockbox dla Y1 i `rockbox-y1` wszystkie odnoszą się do tego samego portu społeczności Rockbox dla Innioasis Y1.Skąd można pobrać Updater CE Rockbox-Y1?

Updater CE zawsze pobiera pakiety oprogramowania sprzętowego bezpośrednio z własnych wydań twórców oprogramowania sprzętowego społeczności (`rockbox-y1/rockbox`). Twórcy ponoszą wyłączną odpowiedzialność za umieszczenie swoich wersji oprogramowania w Updater CE.Czy mogę zainstalować Rockbox-Y1 na Y2?

Nie. Y2 ma własną, oddzielną wersję oprogramowania sprzętowego. Używać [Rockbox dla Y2](rockbox-for-y2_pl.html) Zamiast.Czy instalacja Rockbox-Y1 usunie moją muzykę?

Nie. Muzyka jest przechowywana na karcie MicroSD i nie ma na nią wpływu flashowanie wewnętrznego oprogramowania odtwarzacza.

## Powiązane przewodniki

### [Rockbox-Piasta Y1](rockbox-y1/)

Wszystkie poradniki Y1: instalacja, pobieranie, motywy, przywracanie, podwójny rozruch i rozwiązywanie problemów.

### [Rockbox-Y1 kontra Rockbox-Y2](rockbox-y1-vs-y2.html)

Czym różnią się kompilacje Y1 i Y2 Rockbox.

### [Rockbox-Motywy Y1](rockbox-y1-themes.html)

Jak przenieść motywy 240p i 360p za pomocą narzędzia Updater CE.

### [Rockbox przegląd](rockbox_pl.html)

Wprowadzenie do Rockbox na odtwarzaczach Innioasis Y1 i Y2.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
