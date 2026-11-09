---
title: "Problemy z uruchamianiem aplikacji w systemie Windows 10/11 i obejście Smart App Control — Innioasis Aktualizator"
description: "Jeśli system Windows 10/11 lub funkcja Smart App Control uniemożliwia uruchomienie aplikacji, skorzystaj z rozwiązania opisanego tutaj."
language: "pl"
source: "https://innioasis.app/notices/2026-11-07-codesigning_pl.html"
---

# Problemy z uruchamianiem aplikacji w systemie Windows 10/11 i obejście Smart App Control — Innioasis Aktualizator

Od 25.10.2026 · do 31.12.2026 · Modele: Y1,Y2

# Problemy z uruchamianiem aplikacji w systemie Windows 10/11 i obejście Smart App Control

Jeśli system Windows 10/11 lub funkcja Smart App Control uniemożliwia uruchomienie aplikacji, skorzystaj z rozwiązania opisanego tutaj.

Od 25.10.2026 · do 31.12.2026 · Modele: Y1,Y2

Fałszywie pozytywne raporty zostały przesłane do firmy Microsoft w sprawie `installer.exe` i `InnioasisUpdater.exe` i podjęto odpowiednie działania, ale jeśli funkcja Windows Endpoint Protection lub Smart App Control nadal blokuje aplikację na komputerze, użyj tego obejścia:

### Tymczasowe rozwiązanie: wyłącz inteligentną kontrolę aplikacji
  - Otwórz system Windows Ustawienia (naciskać `Win + I`).
  - Idź do Prywatność i bezpieczeństwo > Bezpieczeństwo systemu Windows > Kontrola aplikacji i przeglądarki.
  - Pod Inteligentna kontrola aplikacji, kliknij Ustawienia inteligentnej kontroli aplikacji.
  - Ustaw Inteligentną kontrolę aplikacji na Wyłączony. Dzięki temu aplikacja natychmiast się otworzy i uruchomi.

Jeśli system Windows lub Edge uniemożliwia pobranie narzędzia Updater CE, kliknij więcej opcji (…) Następnie Trzymać > Pokaż więcej > Mimo to zachowaj.

### Ponowne włączenie inteligentnej kontroli aplikacji

Kiedy aktualizacja fałszywych definicji na komputerze zakończy się, możesz ponownie włączyć funkcję Smart App Control za pośrednictwem rejestru systemu Windows:
  - Naciśnij Klawisz Windows + R, typ `regedit`i naciśnij klawisz Enter, aby otworzyć Edytor rejestru jako administrator.
  - Przejdź do: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (Lub `Policies`).
  - Lokalizować `VerifiedAndReputablePolicyState` w prawym panelu.
  - Kliknij dwukrotnie `VerifiedAndReputablePolicyState` i zmień jego dane wartości na:

  - `1` = Włączone (wymuszone)
  - `2` = Tryb oceny

  - Kliknij OK, zamknij Edytor rejestru i uruchom ponownie komputer.

[Zobacz raport installer.exe dla firmy Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Zobacz raport InnioasisUpdater.exe dla firmy Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Otwórz połączoną stronę](https://innioasis.app/notices.html)

[← Wszystkie powiadomienia](index_pl.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
