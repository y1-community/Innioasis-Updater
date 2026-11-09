---
title: "Innioasis Y2 Kółko przewijania nie działa po aktualizacji | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego"
description: "Innioasis Y2 kółko przewijania lub kółko kliknięcia nie działa po aktualizacji? Zainstaluj ponownie Y2 oryginalne oprogramowanie, sprawdź pierścień i oddziel oprogramowanie sprzętowe od usterek sprzętowych."
language: "pl"
source: "https://innioasis.app/guides/y2-scroll-wheel-not-working_pl.html"
---

# Innioasis Y2 Kółko przewijania nie działa po aktualizacji | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego

Odzyskiwanie gracza · Innioasis Y2

# Innioasis Y2 kółko przewijania nie działa po aktualizacji

Koło obraca się, ale gracz je ignoruje lub kółko klikania zatrzymało się zaraz po błysku. Oto jak odróżnić błąd oprogramowania sprzętowego od błędu sprzętowego na Y2.[Pobierz Updater CE](../guide_pl.html#platform)[Y2 pobrania oprogramowania](../firmware_pl.html?model=Y2&software=original-y2)[Przewodnik odzyskiwania](recovery_pl.html)

## Sprawdź, czy wina leży po stronie koła, czy oprogramowania sprzętowego

W Y2 koło jest fizycznym wejściem, ale oprogramowanie sprzętowe decyduje, co zrobi każdy obrót i kliknięcie. Koło, które zatrzymało się po aktualizacji lub flashowaniu, wskazuje na oprogramowanie. Koło, które ignoruje każde oprogramowanie — zapasowe, Rockbox lub ekran odzyskiwania — wskazuje część.
  - Działa w jednym oprogramowaniu, nie działa w innym: błąd oprogramowania sprzętowego.
  - Martwy na każdym ekranie, łącznie z odzyskiwaniem: koło, wstążka lub tablica.
  - Brakuje tylko jednego kierunku: zwykle zanieczyszczenia pod pierścieniem lub zużycie.
  - Koło się kręci, ale nic się nie wyróżnia: gracz może zostać zamrożony — najpierw wymuś ponowne uruchomienie.

## Szybkie kontrole przed ponowną instalacją oprogramowania sprzętowego
  - Przytrzymaj przycisk zasilania przez około 15 sekund, aby wymusić wyłączenie odtwarzacza, a następnie uruchom go normalnie.
  - Przetestuj kierownicę na ekranie głównym, w Ustawieniach i w odtwarzaczu muzyki.
  - Naciśnij fizyczne przyciski. Jeśli moc i tył reagują, ale koło nie, przyczyną jest samo koło.
  - Ładuj odtwarzacz przez 30 minut za pomocą znanego kabla do transmisji danych.
  - If you installed Rockbox for Y2 or another custom build, return to Original Software and test again.

## Zainstaluj ponownie oprogramowanie sprzętowe Y2 pasujące do Twojego odtwarzacza

Kierownica jest napędzana przez oprogramowanie sprzętowe, więc awarię związaną z aktualizacją można naprawić poprzez ponowne zainstalowanie prawidłowego Y2 oryginalnego oprogramowania w odtwarzaczu. Nigdy nie używaj pakietu Y1 na Y2 i nie wybieraj wersji, która jest „wystarczająco bliska” — pakiety Y2 są budowane dla sprzętu Y2.
  - Otwórz [Aktualizator CE](../guide_pl.html#platform) na Twoim komputerze.
  - Zestaw Model urządzenia do Y2.
  - Wybierz Oprogramowanie oryginalne w Oprogramowanie i wybierz stabilną wersję Y2 — pakiet ręczny to `rom_y2.zip`.
  - Kliknij Zainstaluj / Przywróć i pozwól pakietowi wyodrębnić się.
  - Całkowicie wyłącz urządzenie Y2, podłącz kabel danych USB tylko wtedy, gdy program aktualizujący o to poprosi, i pozostaw go do czasu pojawienia się komunikatu o powodzeniu.
Dopasuj model i wydanie. Jeśli lista wersji wygląda jak oprogramowanie Y1, zatrzymaj się i wybierz ponownie Y2. Pełne kroki znajdują się w [Przewodnik przywracania Y2](restore-original-y2_pl.html).

## Sprawdź pierścień koła pod kątem zanieczyszczeń lub uszkodzeń

Jeśli koło jest sztywne, zacina się lub pęka tylko w jednym kierunku, pomiędzy pierścieniem a obudową mogą osadzać się kłaczki i piasek. Wyłącz odtwarzacz i wytrzyj pierścień suchą ściereczką z mikrofibry. Nie wlewaj środków czyszczących ani alkoholu do szczeliny i nie podważaj pierścienia.

Jeśli pierścień jest luźny, pęknięty lub nie klika, odtwarzacz wymaga serwisu. Oprogramowanie sprzętowe nie może naprawić uszkodzonej tarczy, odłączonej taśmy ani uszkodzeń spowodowanych przez ciecz.

## Jeśli odtwarzacz również nie uruchomi się

Nieudana aktualizacja może uniemożliwić uruchomienie Y2, co wygląda na awarię koła, ponieważ brak reakcji na dane wejściowe. Pracuj poprzez [Y2 nie włącza przewodnika](y2-wont-turn-on_pl.html) do ładowania, wymuszonego ponownego uruchomienia i ręcznego odzyskiwania.

## Innioasis Y2 kółko przewijania – często zadawane pytania

### Dlaczego moje kółko przewijania Innioasis Y2 przestało działać po aktualizacji?

Aktualizacja może spowodować, że sterownik koła nie będzie współpracował z resztą oprogramowania sprzętowego, zwłaszcza jeśli przerwano flashowanie lub użyto pakietu Y1. Zainstaluj ponownie oryginalną wersję oprogramowania Y2 dla swojego modelu i przetestuj kierownicę na standardowym ekranie głównym.

### Jak mogę sprawdzić, czy kółko klikania Y2 jest uszkodzone lub czy oprogramowanie sprzętowe jest wadliwe?

Przetestuj kierownicę w więcej niż jednym oprogramowaniu. Jeśli działa w standardowym oprogramowaniu, ale nie w Rockbox, jest to problem z mapowaniem oprogramowania sprzętowego. Jeśli nie powoduje to żadnego działania na żadnym ekranie, łącznie z menu odzyskiwania, podejrzewaj koło, jego wstążkę lub tablicę.

### Czy przywrócenie oryginalnego oprogramowania naprawi kółko przewijania Y2?

Naprawia awarie spowodowane aktualizacją lub niedopasowanym pakietem i jest to pierwsza rzecz, którą należy wypróbować. Nie naprawi fizycznie uszkodzonego koła, luźnej taśmy ani uszkodzeń spowodowanych przez ciecz.

### Czy mogę użyć pakietu oprogramowania sprzętowego Y1, aby rozwiązać problem z kołem Y2?

Nie. Pakiety Y1 i Y2 nie są zamienne, a flashowanie niewłaściwego modelu może pogorszyć sterowanie. Dopasuj model i wersję przed uruchomieniem instalacji/przywracania.

## Powiązane poprawki
  - [Kółko przewijania Y1 nie działa](y1-scroll-wheel-not-working_pl.html) — te same kontrole dla Y1
  - [Y2 nie włącza się](y2-wont-turn-on_pl.html) — przywracanie zasilania i rozruchu
  - [Innioasis przewodnik odzyskiwania](recovery_pl.html) — wszystkie przewodniki po objawach w jednym miejscu
  - [Rozwiązywanie problemów z instalacją](../troubleshooting_pl.html) — jak wygląda nieudany flash
  - [Przywróć Y2 oryginalne oprogramowanie](restore-original-y2_pl.html) — instrukcja pełnego przywracania

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
