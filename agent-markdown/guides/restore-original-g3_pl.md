---
title: "Przywróć oryginalne oprogramowanie na Innioasis G3 – krok po kroku"
description: "Jak przywrócić oficjalne oryginalne oprogramowanie na Innioasis G3 za pomocą Innioasis Updater CE lub SP Flash Tool, używając zweryfikowanego pakietu rom_g3.zip."
language: "pl"
source: "https://innioasis.app/guides/restore-original-g3_pl.html"
---

# Przywróć oryginalne oprogramowanie na Innioasis G3 – krok po kroku

Przewodnik przywracania · Innioasis G3

# Przywróć oryginalne oprogramowanie na Innioasis G3

Czysty powrót do oprogramowania dostarczonego z odtwarzaczem. Użyj go po nieudanej aktualizacji, przed sprzedażą odtwarzacza lub gdy niestandardowy system nie jest dla Ciebie.[Pobierz Updater CE](../guide_pl.html#platform)[G3 pobrań](../firmware_pl.html?model=G3)[G3 instrukcja](../manuals/g3.html)

Przewodnik instalacji dla Twojego komputera

## Przywróć oryginalne oprogramowanie na swoim G3 za pomocą komputera

Wybierz przewodnik dla komputera, którego używasz. Każda wersja ma konfigurację platformy, Updater CE kroki i drogę powrotną do stanu magazynowego.[Przewodnik po Windowsie](/install/original-g3-windows.html)[przewodnik po macOS-ie](/install/original-g3-mac.html)[Przewodnik po Linuksie](/install/original-g3-linux.html)

[Wszystkie przewodniki Innioasis G3.](/install/g3.html) · [Wszystkie oryginalne instrukcje dotyczące oprogramowania](/install/original-software.html)

## Czego potrzebujesz
  - Komputer z systemem Windows, macOS lub Linux. Updater CE działa na wszystkich trzech.
  - Kabel USB do transmisji danych dostarczony z odtwarzaczem. Kable przeznaczone wyłącznie do ładowania nie będą działać.
  - Urzędnik `rom_g3.zip` pakiet, który Updater pobierze dla Ciebie, lub kopię z pliku [G3 archiwum](../firmware_pl.html?model=G3) jeśli wolisz flashować ręcznie.
  - Ładowanie w odtwarzaczu. Przywrócenie, które powoduje utratę mocy, jest jedynym powszechnym sposobem na pogorszenie złej sytuacji.

Spowoduje to zastąpienie systemu i wymazanie pamięci wewnętrznej. Najpierw skopiuj muzykę, nagrania i zdjęcia na komputer.

## Trasa A: Updater CE (zalecane)
  - Zainstaluj [Innioasis Aktualizator CE](../guide_pl.html#platform) i otwórz go.
  - Zestaw Model urządzenia do G3. Model musi dokładnie pasować do odtwarzacza.
  - Wybierz Oprogramowanie oryginalne na liście oprogramowania.
  - Wybierz wydanie. Najnowsza stabilna wersja jest bezpieczną wersją domyślną.
  - Naciśnij Zainstaluj / Przywróć i poczekaj, aż pakiet zostanie pobrany i rozpakowany.
  - Całkowicie wyłącz odtwarzacz, a następnie podłącz kabel USB tylko wtedy, gdy Updater o to poprosi.
  - Nie dotykaj odtwarzacza ani kabla, dopóki nie pojawi się komunikat o powodzeniu. Odłącz i uruchom odtwarzacz.
Nigdy nie wybieraj innego modelu, żeby „sprawić, żeby zadziałał”. G3 potrzebuje pakietu G3. Mieszanie modeli powoduje, że gracze potrzebują ręcznego odzyskiwania.

## Trasa B: SP Flash Tool (ręczna)

Użyj tej opcji, jeśli komputer nie może uruchomić Updater CE lub jeśli masz już pakiet i wolisz klasyczne narzędzie.
  - Pobierz `rom_g3.zip` z [G3 archiwum](../firmware_pl.html?model=G3) i rozpakuj go.
  - Zachowaj plik rozproszony obok obrazów. Nie zmieniaj nazw ani nie przesuwaj obrazów.
  - Otwórz SP Flash Tool, wybierz Pobierz tylkoi załaduj plik rozproszenia.
  - Wyłącz odtwarzacz, naciśnij Pobierz, a następnie podłącz kabel.
  - Przed rozłączeniem poczekaj na zielony znak sukcesu.

The [SP Flash Tool przewodnik](../sp-flash-tool_pl.html) opisuje bardziej szczegółowo sterowniki i monity systemu Windows. W systemach Linux i macOS Updater CE jest łatwiejszą trasą, ponieważ zapewnia własną obsługę USB.

## Po przywróceniu
  - Odłącz odtwarzacz i pozwól mu uruchomić się samodzielnie.
  - Wybierz język i ustaw zegar.
  - Połącz się ponownie z Wi-Fi lub Bluetooth, jeśli z nich korzystasz.
  - Skopiuj swoją muzykę z powrotem. The [przewodnik po transferze](../manuals/transfer-music.html) ma nazwy folderów.

Jeśli odtwarzacz uruchamia się, ale ekran, pokrętło lub przyciski nadal działają nieprawidłowo, oznacza to, że przywracanie zadziałało; to jest kwestia sprzętu lub konfiguracji, a nie oprogramowania. The [przewodnik rozwiązywania problemów](../troubleshooting_pl.html) to kolejny przystanek.

## Jeśli to nie zadziała

### Aktualizator nigdy nie widzi odtwarzacza

Zmień kabel, a następnie port USB. Unikaj węzłów. W systemie Windows zainstaluj sterownik MediaTek z pliku [strona ze sterownikami](../drivers_pl.html).

### Błysk kończy się wcześniej

Podłącz ponownie, naładuj odtwarzacz i zacznij od nowa. Nie przełączaj się na pakiet innego modelu.

### Gracz pozostaje czarny

Ładuj przez godzinę, a następnie przytrzymaj moc przez dziesięć sekund. Jeśli nadal nie żyje, przeczytaj [przewodnik odzyskiwania](../guides/recovery_pl.html) zanim spróbujesz ponownie.

## Pytania, które zadają ludzie

### Czy to usunie moją muzykę?

Tak, pamięć wewnętrzna została wymazana. Pliki na karcie microSD zwykle zostają zachowane, ale najpierw skopiuj je w bezpieczne miejsce.

### Czy mogę później wrócić do Rockbox?

Tak. Przywracanie oryginalnego oprogramowania nie jest rozwiązaniem jednostronnym; niestandardowa strona oprogramowania dla Twojego modelu może zainstalować je ponownie.

### Czy potrzebuję ustawienia Type A / Type B?

Tylko Y1 ma taki wybór i tylko w przypadku oryginalnego oprogramowania. W każdym innym modelu używany jest jeden pakiet.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
