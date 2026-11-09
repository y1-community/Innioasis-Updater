---
title: "Przewodnik po instalacji oprogramowania sprzętowego i przywracaniu zapasów | Innioasis Aktualizator CE - Innioasis Pobieranie oprogramowania sprzętowego"
description: "Zainstaluj niestandardowe oprogramowanie sprzętowe lub przywróć oficjalne oprogramowanie fabryczne na Innioasis Y1, Y2, G1, G3, G5, R1, PR1 i Timmkoo Q5, Q3 za pomocą Innioasis Updater CE."
language: "pl"
source: "https://innioasis.app/firmware-guide_pl.html"
---

# Przewodnik po instalacji oprogramowania sprzętowego i przywracaniu zapasów | Innioasis Aktualizator CE - Innioasis Pobieranie oprogramowania sprzętowego

Przewodnik po instalacji oprogramowania sprzętowego i przywracaniu zapasów

# Zainstaluj lub przywróć oprogramowanie sprzętowe na swoim urządzeniu

Wybierz model wydrukowany na odtwarzaczu. Następnie postępuj zgodnie z instrukcjami w Updater CE. Zajmuje się resztą.[Pobierz Updater CE](guide_pl.html#platform)[Przeglądaj archiwum oprogramowania sprzętowego](firmware_pl.html)[Rozwiązywanie problemów](troubleshooting_pl.html)

Wybierz model wydrukowany na odtwarzaczu i żądane oprogramowanie, a następnie otwórz ten przewodnik. [Przeglądaj oprogramowanie i oprogramowanie sprzętowe według modelu](firmware_pl.html).

## 

[Pobierz Updater CE](guide_pl.html#download-updater)[Pełny, napisany poradnik](guide_pl.html)

## Zdobądź Innioasis Updater CE

Oto, od czego zacząć, jeśli nie masz jeszcze narzędzia Updater CE.Pobierz go na Updater CEz instalacją kierowaną

### Windows

Pobierz instalator, otwórz go i postępuj zgodnie z instrukcjami instalacji.[Pobierz i zainstaluj sterownik](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Pobierz aplikację i sterowniki](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Zablokowany przez Edge'a?](#)

Jeśli system Windows uniemożliwia uruchomienie aplikacji lub jej nie uruchamia, otwórz Ustawienia, kliknij Prywatność i bezpieczeństwo → Zabezpieczenia systemu Windows → Kontrola aplikacji i przeglądarki, a następnie wyłącz Inteligentną kontrolę aplikacji. [System Windows nie uruchamia aplikacji? Pomoc](#smart-app-control)

Po instalacji musisz ponownie uruchomić komputer, aby zadziałało.

### macOS

Pobierz aplikację i przenieś ją do aplikacji. Jeśli macOS to blokuje, otwórz Ustawienia systemu, następnie Prywatność i bezpieczeństwo i kliknij Otwórz mimo to. [Jak to działa](https://support.apple.com/en-gb/102445#openanyway)[Pobierz Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Pobierz AppImage dla systemów Intel i AMD, nadaj mu charakter wykonywalny i uruchom go.[Pobierz AppImage dla Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Uwagi dotyczące konfiguracji Linuksa](drivers_pl.html#linux)Inna platforma?

Potrzebujesz dłuższych notatek dotyczących konfiguracji komputera? Otwórz [Windows](drivers_pl.html#windows) lub [Linux](drivers_pl.html#linux) przewodnik konfiguracji.

## Wracając do oryginalnego oprogramowania

Aby wrócić, wybierz swój model, wybierz Oprogramowanie oryginalne, a następnie biegnij Zainstaluj / Przywróć. To wszystko. Updater zastępuje oprogramowanie systemowe za Ciebie.[Przewodnik przywracania Y1](guides/restore-original-y1.html)[Przewodnik przywracania Y2](guides/restore-original-y2.html)

## Przewodniki po oprogramowaniu według modelu

Wybierz swój model, a następnie otwórz przewodnik po swoim oprogramowaniu.

### Innioasis Y1

Oprogramowanie dla Y1:

### Innioasis Y2

Oprogramowanie dla Y2:

Uwaga dotycząca obu narzędzi

## Którego narzędzia powinienem użyć?

Innioasis Aktualizator CE to najbezpieczniejszy sposób aktualizacji odtwarzacza. Przechowuje Twoją muzykę, filmy i połączenia Bluetooth. Informuje Cię, kiedy aktualizacje są gotowe. Działa na systemach Windows, macOS i Linux. Opcja Innioasis Universal Flash Tool czyści odtwarzacz i działa na mniejszej liczbie komputerów.[Otwórz pełne porównanie](updater-comparison_pl.html)

### System Windows nie uruchamia aplikacji? Jak wyłączyć inteligentną kontrolę aplikacji

Funkcja Windows Defender SmartScreen lub Smart App Control może blokować nowo pobrane aplikacje społecznościowe, zanim reputacja sygnatur zacznie się rozprzestrzeniać. Inteligentna kontrola aplikacji ma obecnie wpływ na popularne aplikacje, takie jak usługa Epic Overlay Service (używana przez Fortnite) — użycie narzędzia Updater CE jest bezpieczne i zweryfikowane. Wyłączenie inteligentnej kontroli aplikacji umożliwia normalne otwieranie i działanie narzędzia Updater CE.
  - Otwórz Ustawienia na komputerze z systemem Windows (naciśnij Win + I).
  - Kliknij Prywatność i bezpieczeństwo na lewym pasku bocznym, a następnie kliknij Windows Security.
  - Kliknij Kontrola aplikacji i przeglądarki.
  - Pod Inteligentna kontrola aplikacji, kliknij Ustawienia inteligentnej kontroli aplikacji.
  - Ustaw przełącznik na Wyłączony aby umożliwić uruchomienie Updatera CE.

Zablokowany przez Edge'a? Jeśli Microsoft Edge blokuje samo pobieranie, kliknij przycisk Więcej opcji (…) → Trzymać → Pokaż więcej → Mimo to zachowaj.

Ponowne włączenie inteligentnej kontroli aplikacji później: Jeśli chcesz ponownie włączyć funkcję Smart App Control, możesz ją ponownie włączyć za pośrednictwem rejestru systemu Windows w obszarze `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` poprzez ustawienie `VerifiedAndReputablePolicyState` do `1` (Wł.) lub `2` (Tryb ewaluacyjny) i ponowne uruchomienie.Zamknij pomoc

## Czy to było przydatne?

Twoja odpowiedź pomoże ulepszyć ten przewodnik.Tak, uznałem to za przydatneJeszcze nie[Daj nam znać, jak możemy się ulepszyć](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
