---
title: "Rockbox dla Y2 (Rockbox-Y2): przegląd, kompilacje i przewodnik instalacji"
description: "Rockbox dla Y2, Rockbox-Y2 i rockbox-y2 odnoszą się do portu oprogramowania sprzętowego społeczności Rockbox dla Innioasis Y2. Dowiedz się, co zawiera i jak go zainstalować za pomocą Innioasis Updater CE."
language: "pl"
source: "https://innioasis.app/rockbox-for-y2_pl.html"
---

# Rockbox dla Y2 (Rockbox-Y2): przegląd, kompilacje i przewodnik instalacji

[← Pobieranie oprogramowania sprzętowego](firmware_pl.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox dla Y2 (Rockbox-Y2)

Rockbox-Y2 (nazywany także „Rockbox dla Y2”) to dedykowany port oprogramowania społecznościowego Rockbox dla Innioasis Y2. Używa własnego pakietu ROM (`rom_y2.zip`) i jest instalowany bezpośrednio poprzez Innioasis Updater CE.[Zainstaluj Rockbox-Y2](rockbox-y2/install.html)[Pobierz ROM](rockbox-y2/download.html)[Napisany poradnik](guides/rockbox-y2.html)[Rockbox-Y2 piasta](rockbox-y2/)

## Zbudowany specjalnie dla Innioasis Y2

W Innioasis Updater CE to oprogramowanie jest wymienione jako Rockbox Kiedy Y2 jest wybrany. Jej publikacje publikowane są przez wydawnictwo [spycemagic/y2-rockbox](firmware_pl.html?model=Y2&software=rockbox-y2) projekt z nazwą pakietu `rom_y2.zip`.

Nigdy nie instaluj pakietu oprogramowania sprzętowego Y1 na Y2. Wybieranie Y2 w Updater CE automatycznie filtruje listę wydań, wybierając tylko kompilacje kompatybilne z Y2.

## Co oferuje Rockbox-Y2.
  - Biblioteka muzyczna oparta na tagach — przeglądaj albumy, wykonawców i gatunki na podstawie znaczników plików audio lub bezpośrednio przeglądaj foldery.
  - Sterowanie odtwarzaniem — odtwarzanie bez przerw, przenikanie, ReplayGain i ustawienia korektora.
  - Niestandardowe motywy — zainstaluj motywy kompatybilne z twoją kompilacją Rockbox-Y2 ([Y2 przewodnik tematyczny](rockbox-y2-themes.html)).
  - 100% offline — odtwarza pliki lokalne z Twojej karty MicroSD bez kont i subskrypcji.
  - Łatwe przywracanie ustawień fabrycznych — w dowolnym momencie wróć do Y2 Oryginalnego oprogramowania w Updater CE.

## Wybór wersji Rockbox-Y2.
  - Zawsze wybieraj Y2 w Model urządzenia pierwszy.
  - Wybierz najnowszą wersję, chyba że testujesz konkretną wersję.
  - Przeczytaj [Rockbox-Y2 Informacje o wersji](release-notes/rockbox-y2/index_pl.html) aby zobaczyć, co zmieniło się w każdej kompilacji.

## Bezpośrednie pliki do pobrania od twórców społeczności

Innioasis Updater CE zawsze pobiera pakiety oprogramowania bezpośrednio od twórców oprogramowania sprzętowego społeczności ([spycemagic/y2-rockbox](firmware_pl.html?model=Y2&software=rockbox-y2)), a ci programiści ponoszą wyłączną odpowiedzialność za umieszczanie swoich wersji oprogramowania w serwisie Updater CE.

Możesz zezwolić na pobranie i flashowanie narzędzia Updater CE `rom_y2.zip` automatycznie lub pobierz pakiet z naszego [Rockbox-Y2 strona pobierania](rockbox-y2/download.html) i [Rockbox ROM strona pobierania](rockbox-rom-download_pl.html).[Rockbox-Y2 pobrań](rockbox-y2/download.html)[Zainstaluj z lokalnego pliku ZIP](rockbox-y2/portable-zip.html)

## Jak zainstalować Rockbox-Y2
  - Otwórz Innioasis Updater CE i ustaw Model urządzenia do Y2.
  - Wybierz Rockbox w Oprogramowanie.
  - Wybierz wydanie Y2 z listy.
  - Kliknij Zainstaluj / Przywróć dlatego Updater CE pobiera pakiet bezpośrednio od programisty.
  - Całkowicie wyłącz urządzenie Y2 i podłącz je za pomocą kabla do transmisji danych USB, gdy program Updater CE o to poprosi.
  - Poczekaj na komunikat o zakończeniu, a następnie odłącz i włącz urządzenie Y2.

Aby zapoznać się z pełną instrukcją krok po kroku, przeczytaj [Rockbox-Y2 samouczek](guides/rockbox-y2.html).

## Przywracanie oryginalnego oprogramowania Y2.

Aby wrócić do oprogramowania fabrycznego, wybierz Y2 i Oprogramowanie oryginalne w Updater CE wybierz wersję stabilną i kliknij Zainstaluj / Przywróć. Zobacz [przewodnik przywracania](rockbox-y2/restore-stock.html) i [Y2 Strona oryginalnego oprogramowania](original-software-y2_pl.html).

## Często zadawane pytaniaSkąd można pobrać Updater CE Rockbox-Y2?

Updater CE zawsze pobiera pakiety oprogramowania sprzętowego bezpośrednio z własnych wydań twórców oprogramowania sprzętowego społeczności (`spycemagic/y2-rockbox`). Twórcy ponoszą wyłączną odpowiedzialność za umieszczenie swoich wersji oprogramowania w Updater CE.Dlaczego pakiet ma nazwę rom_y2.zip?

Deweloper nadaje nazwę archiwum oprogramowania układowego Y2. `rom_y2.zip` więc nie można go pomylić z Y1. `rom.zip`.Czy motywy Y1 działają na Y2?

Nie zawsze. Sprawdź informacje o wersji dla swojej kompilacji Y2 i zobacz [Rockbox-Y2 przewodnik tematyczny](rockbox-y2-themes.html).

## Powiązane przewodniki

### [Rockbox-Y2 piasta](rockbox-y2/)

Wszystkie poradniki Y2: instalacja, pobieranie, motywy, przywracanie, podwójny rozruch i rozwiązywanie problemów.

### [Rockbox-Y1 kontra Rockbox-Y2](rockbox-y1-vs-y2.html)

Czym różnią się kompilacje Y1 i Y2 Rockbox.

### [Rockbox-Motywy Y2](rockbox-y2-themes.html)

Instalowanie i resetowanie motywów na Rockbox-Y2.

### [Rockbox dla Y1](rockbox-for-y1_pl.html)

Omówienie i instrukcja instalacji dla portu Innioasis Y1.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
