---
title: "Innioasis Y2 Nie włącza się | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego"
description: "Innioasis Y2 nie włącza się ani nie ładuje? Wymuś ponowne uruchomienie, sprawdź, czy komputer go widzi, a następnie przywróć Y2 oprogramowanie sprzętowe lub skorzystaj z ręcznego SP Flash Tool odzyskiwania."
language: "pl"
source: "https://innioasis.app/guides/y2-wont-turn-on_pl.html"
---

# Innioasis Y2 Nie włącza się | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego

Odzyskiwanie gracza · Innioasis Y2

# Innioasis Y2 nie włącza się

Czarny ekran nie zawsze oznacza martwego gracza. Zanim spróbujesz ręcznego flashowania, przeprowadź ładowanie, wymuś ponowne uruchomienie i wykrycie na komputerze.[Pobierz Updater CE](../guide_pl.html#platform)[Pobieranie oprogramowania sprzętowego](../firmware_pl.html)[Przewodnik odzyskiwania](recovery_pl.html)

## Naładuj Y2 prawidłowo, zanim cokolwiek innego

Większość raportów „Y2 nie włącza się” dotyczy rozładowanej baterii, kabla przeznaczonego tylko do ładowania lub ładowarki, która nie dostarcza wystarczającej ilości prądu. Głęboko wyczerpany Y2 może potrzebować od 20 do 30 minut, zanim ekran zacznie cokolwiek pokazywać.
  - Użyj znanego USB dane kabel, a nie kabel przeznaczony wyłącznie do ładowania.
  - Wypróbuj ładowarkę ścienną, a następnie bezpośrednio port komputera USB — a nie koncentrator.
  - Pozostaw podłączony na 30 do 60 minut i obserwuj ikonę ładowania lub podświetlenie.
  - Zanim przejdziesz dalej, wypróbuj drugi kabel i ładowarkę.

## Wymuś ponowne uruchomienie

Przytrzymaj przycisk zasilania przez około 15 sekund, zwolnij go, odczekaj pięć sekund, a następnie naciśnij raz przycisk zasilania. Usuwa to zawieszony but i można go bezpiecznie powtórzyć.

Jeśli na ekranie pojawia się logo, a następnie gaśnie, odtwarzacz uruchamia się i ulega awarii — przejdź do przywracania oprogramowania sprzętowego poniżej. Jeśli nic się nie dzieje, trzymaj go naładowany i spróbuj ponownie za pół godziny.

## Sprawdź, czy komputer widzi odtwarzacz

Podłącz wyłączony Y2 kablem do transmisji danych i otwórz Menedżera urządzeń w systemie Windows, `lsusb` w systemie Linux lub MTKClient w systemie macOS. Działający odtwarzacz pojawia się jako urządzenie MediaTek z identyfikatorem dostawcy `0e8d`. Jeśli się pojawi, oznacza to, że sprzęt jest na tyle aktywny, że można go przeflashować nawet wtedy, gdy ekran pozostaje ciemny.

Jeśli nic się nie pojawi, najpierw zainstaluj sterownik MediaTek w systemie Windows — plik [przewodnik kierowcy](../drivers_pl.html) obejmuje uprawnienia Windows i Linux.

## Przywróć standardowe oprogramowanie sprzętowe Y2.

Jeśli odtwarzacz zostanie wykryty, ale nie uruchomi się, zainstaluj ponownie Y2 oryginalne oprogramowanie. Używaj tylko pakietu Y2; kompilacja Y1 nie uruchomi się na sprzęcie Y2.
  - Otwórz [Aktualizator CE](../guide_pl.html#platform) na Twoim komputerze.
  - Zestaw Model urządzenia do Y2.
  - Wybierz Oprogramowanie oryginalne w Oprogramowanie i wybierz stabilną wersję Y2 — pakiet ręczny to `rom_y2.zip`.
  - Kliknij Zainstaluj / Przywróć i pozwól pakietowi wyodrębnić się.
  - Całkowicie wyłącz urządzenie Y2, podłącz kabel danych USB tylko wtedy, gdy program aktualizujący o to poprosi, i pozostaw go do czasu pojawienia się komunikatu o powodzeniu.
Utrzymuj stabilną moc. Lampa błyskowa, która utraci moc, może sprawić, że odtwarzacz będzie bezużyteczny. Najpierw naładuj go i podłącz bezpośrednio do komputera.

## Odzyskiwanie ręczne, gdy program aktualizujący nie widzi odtwarzacza

Updater CE zawiera narzędzia do ręcznego odzyskiwania w przypadkach, gdy instalacja z przewodnikiem nie może zostać ukończona. [SP Flash Tool](../sp-flash-tool_pl.html) jest dołączony do systemów Windows i Linux x86, a trasa MTKClient obejmuje system macOS. Obydwa wymagają pakietu oprogramowania sprzętowego dopasowanego do modelu z [Pobieranie oprogramowania sprzętowego](../firmware_pl.html) strona.

Postępuj zgodnie z przewodnikiem po narzędziach dla swojej platformy, zamiast improwizować pliki rozproszone lub przesunięcia. Jeśli odtwarzacz nie zostanie wykryty przez żadne narzędzie, przyczyną problemu jest prawdopodobnie akumulator, port ładowania lub płyta główna.

## Jeśli nadal się nie uruchomi

Przestań flashować i traktuj to jak sprzęt. Nie otwieraj obudowy ani nie naciskaj na baterię. Zapytaj społeczność posiadającą model, co robi ekran, czy komputer go wykrywa i jakie pakiety wypróbowałeś — [Discord społeczność](https://discord.gg/zHrT2zrcek) może pomóc w określeniu trasy serwisowej.

Przywrócenie zapasów powoduje wymianę systemu, więc przed flashowaniem wykonaj kopię zapasową wszystkiego, co jest zapisane w pamięci wewnętrznej odtwarzacza. Przywracanie nie ma wpływu na muzykę na karcie MicroSD.

## Innioasis Y2 Często zadawane pytania dotyczące zasilania

### Dlaczego mój Innioasis Y2 nie włącza się?

Typowe przyczyny to całkowicie rozładowana bateria, kabel przeznaczony tylko do ładowania lub słaba ładowarka, awaria oprogramowania sprzętowego, która uniemożliwia rozruch, lub usterka sprzętowa. Ładuj go przez 30 minut za pomocą znanego kabla do transmisji danych, zanim założysz, że gracz nie żyje.

### Jak wymusić ponowne uruchomienie Innioasis Y2?

Przytrzymaj przycisk zasilania przez około 15 sekund, zwolnij go, odczekaj pięć sekund, a następnie naciśnij raz przycisk zasilania. Jeśli nic się nie pojawi, pozostaw urządzenie do ładowania i spróbuj ponownie po 30 minutach.

### Czy mogę odzyskać Y2, który się nie włącza?

Często tak. Jeśli komputer nadal wykrywa urządzenie MediaTek, zainstaluj ponownie oryginalny pakiet oprogramowania Y2 za pomocą narzędzia Updater CE. Jeśli nie zostanie wykryty, użyj narzędzia odzyskiwania SP Flash Tool lub MTKClient dołączonego do narzędzia Updater CE i pliku oprogramowania sprzętowego Y2 dopasowanego do modelu.

### Czy Y2 musi zostać naładowany przed flashowaniem?

Tak. Lampa błyskowa, która utraci moc, może sprawić, że odtwarzacz będzie bezużyteczny. Najpierw naładuj go i podłącz bezpośrednio do komputera, a nie przez koncentrator.

## Powiązane poprawki
  - [Y1 nie włącza się](y1-wont-turn-on_pl.html) — te same kontrole dla Y1
  - [Kółko przewijania Y2 nie działa](y2-scroll-wheel-not-working_pl.html) — jeśli uruchamia się, ale koło nie
  - [Innioasis przewodnik odzyskiwania](recovery_pl.html) — wszystkie przewodniki po objawach w jednym miejscu
  - [SP Flash Tool przewodnik](../sp-flash-tool_pl.html) — ręczne flashowanie w systemach Windows i Linux
  - [Rozwiązywanie problemów z instalacją](../troubleshooting_pl.html) — jak wygląda nieudany flash

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
