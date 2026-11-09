---
title: "SP Flash Tool dla Innioasis i Timmkoo graczy"
description: "Znajdź SP Flash Tool w pakiecie z Innioasis Updaterem w systemach Windows i Linux, wyodrębnij rom.zip lub rom_y2.zip i flashuj Innioasis Y1 lub Y2 z pasującym plikiem rozproszonym."
language: "pl"
source: "https://innioasis.app/sp-flash-tool_pl.html"
---

# SP Flash Tool dla Innioasis i Timmkoo graczy

Ręczne flashowanie

# Narzędzie Flash dla graczy Innioasis i Timmkoo.

SP Flash Tool wchodzi do środka. Innioasis Aktualizator włączony [Windows](drivers_pl.html#windows) i [Linux](drivers_pl.html#linux). Już to masz. Ten przewodnik pokazuje bezpieczny sposób korzystania z niego na Innioasis Y1 lub Y2 oraz trasę Aktualizatora dla graczy Timmkoo.[Wróć do przewodnika po programie Updater](guide_pl.html)[Pobieranie oprogramowania sprzętowego](firmware_pl.html)[Rozwiązywanie problemów](troubleshooting_pl.html)

Zacznij od Innioasis Updater

## Updater wykonuje całą pracę w jednym przebiegu

Updater wykonuje większość instalacji w jednym przebiegu. Wybierz oprogramowanie, postępuj zgodnie z instrukcjami i gotowe. Informuje również, kiedy pojawi się poprawka lub nowa wersja. SP Flash Tool znajduje się w zestawie narzędzi aktualizatora w rzadkich przypadkach, gdy aktualizator nie może zakończyć. Poniższe kroki stanowią wyjątek.

## Do czego służy to narzędzie

Aktualizator flashuje odtwarzacz za Ciebie. SP Flash Tool to ten sam silnik, bez poręczy. Użyj go, gdy Updater nie uruchomi się, gdy odtwarzacz nie będzie mógł się połączyć lub gdy znasz się na pliku rozproszonym.Wypróbuj najpierw narzędzie Updater. W przypadku większości instalacji i większości odzyskiwania, plik z przewodnikiem [Trasa aktualizacji](guide_pl.html) jest bezpieczniejszym wyborem. Używaj SP Flash Tool, gdy wiesz, dlaczego go potrzebujesz, i miej pod ręką naładowaną baterię oraz kabel do transmisji danych USB.

## Narzędzie Flash dla Innioasis graczy

Innioasis Updater to narzędzie Flash dla graczy Innioasis. Instaluje oficjalne oprogramowanie, aktualizuje i przywraca pakiety w ramach procesu dopasowanego do modelu, a także zachowuje Twoją muzykę i ustawienia.

### Innioasis Y1 narzędzie flash

Wybierz wersję Y1 w Aktualizatorze, a następnie podłącz wyłączony odtwarzacz, gdy aplikacja o to poprosi. Te same pakiety Y1 współpracują z SP Flash Tool, gdy potrzebujesz trasy ręcznej.

### Innioasis Y2 narzędzie flash

Wybierz wersję wymienioną dla Y2. Pakiety Y2 nie są zamienne z pakietami Y1, dlatego przed rozpoczęciem sprawdź model.

## Narzędzie Flash dla Timmkoo graczy

Timmkoo gracze korzystają z tego samego procesu instalacji Aktualizatora. Odczytuje bezpośrednio pakiety ZIP i RAR Timmkoo, więc nie potrzebujesz osobnego narzędzia Flash ani pliku rozproszonego.

### Timmkoo Q5 narzędzie flash

Wybierz model Q5 w Updaterze, wybierz pakiet Timmkoo, następnie uruchom Instalację/Przywracanie i podłącz odtwarzacz po wyświetleniu monitu.

### Timmkoo Q3 i Q3E narzędzie flash

Wpis Q3 obejmuje zarówno Q3, jak i Q3E. Aktualizator wybiera pasujące pliki z pakietu publikowanego przez projekt.

### Timmkoo A5 narzędzie flash

Wybierz model A5 przed wybraniem pakietu, a następnie postępuj zgodnie z tymi samymi instrukcjami instalacji.

## Gdzie Updater to umieścił

SP Flash Tool jest dostarczany z folderem instalacyjnym narzędzia Updater, a nie jako osobny plik do pobrania. Otwórz go stamtąd, kiedy go potrzebujesz.

### Windows

Otwórz folder instalacyjny narzędzia Updater i uruchom `flash_tool.exe`. Folder zwykle znajduje się pod `%LOCALAPPDATA%\Innioasis Updater`. W przypadku niektórych konfiguracji dołączony jest folder Toolkit ze skrótem SP Flash Tool.

### Linux

Uruchom pakiet `flash_tool` binarny w folderze aplikacji Updater na x86 / x86_64. Instalator projektu przygotowuje uprawnienia USB z regułami udev, więc odtwarzacz powinien pojawić się po podłączeniu.

### macOS

SP Flash Tool nie jest dołączone do systemu macOS. Aktualizator używa zamiast tego trasy MTKClient. Skorzystaj z [instalacja z przewodnikiem](guide_pl.html) na komputerze Mac i zachowaj SP Flash Tool w przypadku komputera z systemem Windows lub Linux.

Narzędzie jest dostarczane z agentem pobierania MediaTek i konfiguracją specyficzną dla modelu, więc nie musisz zbierać DA ani rozpraszać plików z innego miejsca.

## Przygotuj oprogramowanie sprzętowe
  - Chwyć wydanie, z którego chcesz [Pobieranie oprogramowania sprzętowego](firmware_pl.html). Wybierać `rom.zip` dla Y1 lub `rom_y2.zip` dla Y2.
  - Wyodrębnij plik ZIP do własnego folderu. System Windows może używać funkcji Wyodrębnij wszystko. W systemie Linux użyj menedżera archiwów lub `unzip` w terminalu.
  - Sprawdź, czy plik rozproszony znajduje się w wyodrębnionym folderze. Zwykle ma nazwę `MT6572_Android_scatter.txt` dla pakietów Y1 i `MT6582_Android_scatter_def.txt` dla pakietów Y2, chociaż wydanie może nazwać je na cześć swojego projektu.
Trzymaj modele oddzielnie. Rozproszenie Y1 opisuje urządzenie MT6572, a rozproszenie Y2 opisuje urządzenie MT6582. Flashowanie z niewłaściwym sposobem powoduje, że gracze zostają zamurowani. Jeśli rozproszenie wewnątrz pliku ZIP nie pasuje do Twojego modelu, zatrzymaj się i zamiast tego użyj pakietu wymienionego dla Twojego modelu.

## Załaduj scatter i flash
  - Otwórz SP Flash Tool z folderu instalacyjnego narzędzia Updater.
  - W zakładce Pobierz kliknij Wybierz obok opcji Plik ładowania rozproszonego i wybierz plik rozproszony z wyodrębnionego folderu. Lista partycji zostanie wypełniona.
  - Pozostaw tryb lampy błyskowej włączony Pobierz tylko chyba że celowo przeprowadzasz pełne odzyskiwanie, co jest potrzebne Aktualizacja oprogramowania sprzętowego.
  - Kliknij Pobierz. Narzędzie będzie czekać na gracza.
  - Całkowicie wyłącz odtwarzacz, a następnie podłącz kabel danych USB. Połóż odtwarzacz i nie ruszaj go.
  - Poczekaj na zielony znacznik wyboru. Dopiero wtedy odłącz kabel i uruchom odtwarzacz.

Zachowaj te same zasady USB dotyczące kabla i czasu, co w przypadku trasy prowadzonej: kabel do transmisji danych, bez koncentratora i podłączaj dopiero wtedy, gdy narzędzie będzie gotowe.

## Jeśli nie miga
  - Sprawdź, czy symbol scatter i ZIP odpowiadają modelowi wydrukowanemu na odtwarzaczu.
  - Przed podłączeniem upewnij się, że odtwarzacz jest całkowicie wyłączony.
  - W systemie Windows potwierdź, że sterownik MediaTek został zainstalowany wraz z konfiguracją Aktualizatora; w systemie Linux potwierdź reguły udev w instalatorze projektu.
  - Podłącz kabel ponownie tylko wtedy, gdy narzędzie czeka. Wyścig portowy może wymagać pełnego odłączenia i świeżego Pobierz trzask.

Na wszystko poza tym otwórz się [rozwiązywanie problemów](troubleshooting_pl.html). I pamiętaj: Updater jest nadal normalną trasą i [Y1](guides/restore-original-y1.html) i [Y2](guides/restore-original-y2.html) przewodniki przywracania też z niego korzystają.

## Czy to było przydatne?

Twoja odpowiedź pomoże ulepszyć ten przewodnik.Tak, uznałem to za przydatneJeszcze nie[Daj nam znać, jak możemy się ulepszyć](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
