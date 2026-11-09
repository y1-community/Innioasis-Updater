---
title: "Napraw Innioasis aktualizator i Y1 pomocnik za pomocą czystej instalacji - Innioasis aktualizator"
description: "Czysta instalacja krok po kroku dla Innioasis Updatera i Y1 Helpera: usuń pozostałe pliki, zainstaluj ponownie i wróć do flashowania oprogramowania sprzętowego."
language: "pl"
source: "https://innioasis.app/Troubleshooting/clean_install_pl.html"
---

# Napraw Innioasis aktualizator i Y1 pomocnik za pomocą czystej instalacji - Innioasis aktualizator

## Potwierdź, że potrzebujesz czystej instalacji

Ręczna ponowna instalacja jest zalecana w przypadku zaobserwowania któregokolwiek z następujących symptomów:
  - Uruchomienie programu aktualizującego zajmuje kilka minut lub zawiesza się podczas sprawdzania dostępności aktualizacji.
  - Aktualizacje przestają przychodzić, mimo że istnieją nowsze wersje.
  - Aktualizacje oprogramowania sprzętowego urządzenia nie są pobierane ani stosowane, mimo że są dostępne.
  - Pominąłeś wiele wydań i nie korzystałeś z narzędzia aktualizującego od dłuższego czasu.

## Windows: Wykonaj czystą ponowną instalację

Użyj oficjalnego instalatora systemu Windows, aby odświeżyć narzędzie Updater w systemie Windows 10 lub Windows 11 (64-bitowym). To całkowicie zastępuje starsze kompilacje i przywraca kanał samodzielnej aktualizacji.

Zanim uruchomisz instalator, otwórz Ustawienia > Aplikacje > Zainstalowane aplikacje (lub dziedzictwo Dodaj/Usuń programy panel) i odinstaluj istniejącą kopię Innioasis Updatera. Rozpoczęcie czyszczenia zapobiega konfliktom plików.[ Pobierz czysty instalator dla systemu Windows ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)Krok 1

### Pobierz najnowszy instalator

Zapisz instalator w folderze Pobrane. Zamknij Innioasis Aktualizator, jeśli jest aktualnie uruchomiony.Krok 2

### Usuń istniejącą instalację

Otwórz Ustawienia > Aplikacje > Zainstalowane aplikacje (lub dziedzictwo Panel sterowania › Dodaj/Usuń programy) i odinstaluj Innioasis Updater, aby ponowna instalacja rozpoczęła się od nowa.Krok 3

### Zainstaluj i uruchom ponownie

Uruchom pobrany instalator — system Windows wyświetli monit o pozwolenie. Po zakończeniu instalacji uruchom Innioasis Updater; powinien teraz automatycznie wykryć wersję 1.8.2.8 i ponownie pobrać aktualizacje.

 Naprawia to również powolne uruchamianie i powoduje, że narzędzie Updater ponownie pobiera aktualizacje oprogramowania sprzętowego bezpośrednio od programistów. 

## macOS: Odśwież za pomocą instalatora DMG

Instalator macOS usuwa stare pliki i instaluje wersję 1.8.2.8.[ Pobierz Innioasis Aktualizator DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - Otwórz pobrany plik DMG i rozwiń okno Findera, aby zobaczyć plik Zainstaluj ponownie opcja.
  - Uruchom polecenie Zainstaluj ponownie, aby odświeżyć istniejącą kopię narzędzia Updater. Spowoduje to usunięcie starszych plików pomocniczych, które mogą blokować nowe funkcje.
  - Uruchom ponownie Innioasis Updater z poziomu aplikacji. Potwierdź wersję panelu Informacje 1.8.2.8.
 Jeśli po ponownej instalacji zobaczysz komunikat „Innioasis Aktualizatora nie można otworzyć”, przejdź do Ustawienia systemowe > Prywatność i bezpieczeństwo i wybierz Otwórz mimo to aby zatwierdzić aplikację. 

## Po aktualizacji do wersji 1.8.2.8

Po przejściu na najnowszą wersję uzyskasz dostęp do poniższych funkcji. Są one dostępne tylko w bieżących kompilacjach.
  - Instaluje jednym kliknięciem dla oryginalnego oprogramowania sprzętowego, wydań społeczności i kompilacji Rockbox pobranych bezpośrednio z wydań programistów.
  - Przejrzyste kroki z przewodnikiem informujące o tym, kiedy podłączyć odtwarzacz i kiedy można bezpiecznie odłączyć go od prądu.
  - Ogólna poprawa stabilności i znacznie krótsze czasy uruchamiania na obu platformach.

 Potrzebujesz pomocy w zweryfikowaniu swojej wersji? Otwórz Innioasis Aktualizator, wybierz Pomoc › Informacjei potwierdź pokazy kompilacji 1.8.2.8. 

## Nadal potrzebujesz pomocy?

Jeśli czysta instalacja nie powiedzie się, przechwyć wszystkie komunikaty o błędach i skontaktuj się z kanałami pomocy społeczności Innioasis. Dołącz wersję systemu operacyjnego, wersję narzędzia Updater (jeśli jest dostępna) i kroki, które już wypróbowałeś.

Aktualizowanie instalacji gwarantuje, że zawsze będziesz otrzymywać najnowsze pakiety oprogramowania sprzętowego i narzędzia w miarę ich wdrażania.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
