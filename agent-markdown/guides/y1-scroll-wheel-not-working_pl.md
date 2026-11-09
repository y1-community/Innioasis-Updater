---
title: "Innioasis Y1 Kółko przewijania nie działa po aktualizacji | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego"
description: "Innioasis Y1 kółko przewijania lub kółko kliknięcia nie działa po aktualizacji? Zainstaluj ponownie Y1 oryginalne oprogramowanie, sprawdź pierścień i oddziel oprogramowanie sprzętowe od usterek sprzętowych."
language: "pl"
source: "https://innioasis.app/guides/y1-scroll-wheel-not-working_pl.html"
---

# Innioasis Y1 Kółko przewijania nie działa po aktualizacji | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego

Odzyskiwanie gracza · Innioasis Y1

# Innioasis Y1 kółko przewijania nie działa po aktualizacji

Koło obraca się, ale nic się nie porusza lub kółko klikające przestało reagować zaraz po mignięciu. Oto, jak oddzielić usterkę oprogramowania sprzętowego od usterki sprzętowej i co zrobić w pierwszej kolejności.[Pobierz Updater CE](../guide_pl.html#platform)[Y1 pobrania oprogramowania](../firmware_pl.html?model=Y1&software=original-y1)[Przewodnik odzyskiwania](recovery_pl.html)

## Sprawdź, czy wina leży po stronie koła, czy oprogramowania sprzętowego

W Y1 koło jest fizycznym wejściem, ale oprogramowanie sprzętowe decyduje, co zrobi każdy obrót i kliknięcie. Jeśli kierownica zatrzymała się w momencie aktualizacji lub flashowania odtwarzacza, prawdopodobną przyczyną jest oprogramowanie, a nie uszkodzona część. Jeśli ignoruje każde wypróbowane oprogramowanie — zapasowe, Rockbox lub ekran odzyskiwania — traktuj je jako sprzęt.
  - Działa w jednym oprogramowaniu, nie działa w innym: błąd oprogramowania sprzętowego.
  - Martwy na każdym ekranie, łącznie z odzyskiwaniem: koło, wstążka lub tablica.
  - Brakuje tylko jednego kierunku: zwykle zanieczyszczenia pod pierścieniem lub zużycie.
  - Koło się kręci, ale nic się nie wyróżnia: gracz może zostać zamrożony — najpierw wymuś ponowne uruchomienie.

## Szybkie kontrole przed ponowną instalacją oprogramowania sprzętowego
  - Przytrzymaj przycisk zasilania przez około 15 sekund, aby wymusić wyłączenie odtwarzacza, a następnie uruchom go normalnie.
  - Przetestuj kierownicę na ekranie głównym, w Ustawieniach i w odtwarzaczu muzyki.
  - Naciśnij fizyczne przyciski. Jeśli moc i tył reagują, ale koło nie, przyczyną jest samo koło.
  - Ładuj odtwarzacz przez 30 minut za pomocą znanego kabla do transmisji danych — niski poziom naładowania baterii może powodować nieprawidłowe działanie wejść.
  - If you installed Rockbox or another custom build, return to Original Software and test again.

## Zainstaluj ponownie oprogramowanie sprzętowe Y1 pasujące do Twojego odtwarzacza

Ponieważ kierownica jest napędzana przez oprogramowanie sprzętowe, awarię związaną z aktualizacją można naprawić poprzez ponowne zainstalowanie prawidłowego Y1 oryginalnego oprogramowania w odtwarzaczu. Nie używaj pakietu Y2 i nie wybieraj wydania, które jest „wystarczająco bliskie” — pakiety Y1 są zbudowane dla sprzętu Y1, a kompilacja Y2 na Y1 może spowodować nieprawidłowe odwzorowanie elementów sterujących.
  - Otwórz [Aktualizator CE](../guide_pl.html#platform) na Twoim komputerze.
  - Zestaw Model urządzenia do Y1.
  - Wybierz Oprogramowanie oryginalne w Oprogramowanie i wybierz stabilną wersję Y1 — pakiet ręczny to `rom.zip`.
  - Kliknij Zainstaluj / Przywróć i pozwól pakietowi wyodrębnić się.
  - Całkowicie wyłącz urządzenie Y1, podłącz kabel danych USB tylko wtedy, gdy program aktualizujący o to poprosi, i pozostaw go do czasu pojawienia się komunikatu o powodzeniu.
Dopasuj model i wydanie. Jeśli lista wersji wygląda jak oprogramowanie Y2, zatrzymaj się i wybierz ponownie Y1. Pełne kroki znajdują się w [Przewodnik przywracania Y1](restore-original-y1_pl.html).

## Sprawdź pierścień koła pod kątem zanieczyszczeń lub uszkodzeń

Jeśli koło jest sztywne, zacina się lub pęka tylko w jednym kierunku, pomiędzy pierścieniem a obudową mogą osadzać się kłaczki i piasek. Wyłącz odtwarzacz i wytrzyj pierścień suchą ściereczką z mikrofibry. Nie wlewaj środków czyszczących ani alkoholu do szczeliny i nie podważaj pierścienia.

Jeśli pierścień jest luźny, pęknięty lub nie klika, odtwarzacz wymaga serwisu. Ponowna instalacja oprogramowania sprzętowego nie naprawi uszkodzonej tarczy, odłączonej taśmy ani uszkodzeń spowodowanych przez ciecz.

## Jeśli odtwarzacz również nie uruchomi się

Nieudana aktualizacja może uniemożliwić uruchomienie Y1, co wygląda na problem z kołem, ponieważ nic nie odpowiada. Pracuj poprzez [Y1 nie włącza przewodnika](y1-wont-turn-on_pl.html) dla etapów ładowania, wymuszonego ponownego uruchomienia i ręcznego odzyskiwania.

## Innioasis Y1 kółko przewijania – często zadawane pytania

### Dlaczego moje kółko przewijania Innioasis Y1 przestało działać po aktualizacji?

Aktualizacja może spowodować, że sterownik koła nie będzie współpracował z resztą oprogramowania sprzętowego, zwłaszcza jeśli przerwano flashowanie lub użyto pakietu Y2. Zainstaluj ponownie oryginalną wersję oprogramowania Y1 dla swojego modelu i przetestuj kierownicę na standardowym ekranie głównym.

### Jak mogę sprawdzić, czy kółko klikania Y1 jest uszkodzone lub czy oprogramowanie sprzętowe jest wadliwe?

Przetestuj kierownicę w więcej niż jednym oprogramowaniu. Jeśli działa w standardowym oprogramowaniu, ale nie w Rockbox, jest to problem z mapowaniem oprogramowania sprzętowego. Jeśli nie powoduje to żadnego działania na żadnym ekranie, łącznie z menu odzyskiwania, podejrzewaj koło, jego wstążkę lub tablicę.

### Czy przywrócenie oryginalnego oprogramowania naprawi kółko przewijania Y1?

Naprawia awarie spowodowane aktualizacją lub niedopasowanym pakietem i jest to pierwsza rzecz, którą należy wypróbować. Nie naprawi fizycznie uszkodzonego koła, luźnej taśmy ani uszkodzeń spowodowanych przez ciecz.

### Czy mogę użyć pakietu oprogramowania sprzętowego Y2, aby rozwiązać problem z kołem Y1?

Nie. Pakiety Y1 i Y2 nie są zamienne, a flashowanie niewłaściwego modelu może pogorszyć sterowanie. Dopasuj model i wersję przed uruchomieniem instalacji/przywracania.

## Powiązane poprawki
  - [Kółko przewijania Y2 nie działa](y2-scroll-wheel-not-working_pl.html) — te same kontrole dla Y2
  - [Y1 nie włącza się](y1-wont-turn-on_pl.html) — przywracanie zasilania i rozruchu
  - [Innioasis przewodnik odzyskiwania](recovery_pl.html) — wszystkie przewodniki po objawach w jednym miejscu
  - [Rozwiązywanie problemów z instalacją](../troubleshooting_pl.html) — jak wygląda nieudany flash
  - [Przywróć Y1 oryginalne oprogramowanie](restore-original-y1_pl.html) — instrukcja pełnego przywracania

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
