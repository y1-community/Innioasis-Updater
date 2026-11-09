---
title: "Innioasis Y1 i Y2 Przewodnik odzyskiwania | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego"
description: "Przewodnik odzyskiwania dla odtwarzaczy Innioasis Y1 i Y2, które nie włączają się lub których kółko przewijania przestało działać po aktualizacji. Resetowanie i kroki oprogramowania sprzętowego."
language: "pl"
source: "https://innioasis.app/guides/recovery_pl.html"
---

# Innioasis Y1 i Y2 Przewodnik odzyskiwania | Innioasis Archiwum oprogramowania sprzętowego - Innioasis Pobieranie oprogramowania sprzętowego

Odzyskiwanie gracza · Y1 i Y2

# Innioasis Y1 i Y2 przewodnik odzyskiwania

Nie włącza się, koło nie działa lub instalacja zatrzymała się w połowie. Zacznij od objawu, a następnie postępuj zgodnie z instrukcjami w podanej kolejności, zamiast od razu przechodzić do ręcznego flashowania.[Pobierz Updater CE](../guide_pl.html#platform)[Pobieranie oprogramowania sprzętowego](../firmware_pl.html)[Rozwiązywanie problemów](../troubleshooting_pl.html)

Zacznij od Innioasis Updater

## Instalacja z przewodnikiem rozwiązuje większość z nich

Updater robi to w jednym przebiegu. Wybierz oprogramowanie, postępuj zgodnie z instrukcjami wyświetlanymi na ekranie i gotowe. Informuje również, kiedy pojawi się poprawka lub nowa wersja.

## Zacznij od objawu

W tych przewodnikach omówiono dwie awarie, na które ludzie najczęściej napotykają po aktualizacji lub flashowaniu. Wybierz ten, który pasuje do tego, co widzisz, a następnie przeglądaj go w odpowiedniej kolejności.

### Kółko przewijania nie działa

Koło się kręci, ale gracz je ignoruje lub zatrzymało się zaraz po aktualizacji.

[Y1 kółko przewijania](y1-scroll-wheel-not-working_pl.html) · [Y2 kółko przewijania](y2-scroll-wheel-not-working_pl.html)

### Odtwarzacz nie włącza się

Czarny ekran, brak lampki ładowania lub logo, które pojawia się i znika.

[Y1 przewodnik zasilania](y1-wont-turn-on_pl.html) · [Y2 przewodnik zasilania](y2-wont-turn-on_pl.html)

### Instalacja zatrzymana w trakcie

Program aktualizujący nie powiódł się przed lub po komunikacie USB lub lista wydań wygląda nieprawidłowo.

[Przewodnik rozwiązywania problemów](../troubleshooting_pl.html)

### Potrzebujesz plików

Oryginalne oprogramowanie i niestandardowe pakiety dla każdego modelu.

[Pobieranie oprogramowania sprzętowego](../firmware_pl.html)

## Pakiety Y1 i Y2 nie są zamienneNigdy nie flashuj modelu. Y1 `rom.zip` nie jest pakietem Y2 i Y2 `rom_y2.zip` nie będzie działać na Y1. Flashowanie niewłaściwego modelu jest jednym z najczęstszych powodów, dla których gracz kończy z martwym sterowaniem lub pętlą rozruchową.

Sprawdź model wydrukowany na odtwarzaczu, a następnie dopasuj go w programie Updater CE przed wybraniem wersji.

## Najpierw przywróć pasujące oryginalne oprogramowanie

Przed użyciem jakichkolwiek narzędzi ręcznych zainstaluj ponownie w odtwarzaczu standardowe oprogramowanie sprzętowe dla odpowiedniego modelu. Naprawia to większość błędów kół i bagażników związanych z aktualizacją.

Y1: wybierz Y1, wybierz Oryginalne oprogramowanie, wybierz stabilną wersję Y1, a następnie uruchom Instaluj / Przywróć. [Pełny Y1 przewodnik przywracania](restore-original-y1_pl.html).

Y2: wybierz Y2, wybierz Oryginalne oprogramowanie, wybierz stabilną wersję Y2, a następnie uruchom Instaluj / Przywróć. [Pełny Y2 przewodnik przywracania](restore-original-y2_pl.html).

Wyłącz odtwarzacz i podłącz kabel danych USB tylko wtedy, gdy program aktualizujący o to poprosi. Pozostaw podłączony do czasu pojawienia się komunikatu o powodzeniu.

## Ręczne odzyskiwanie dostarczane z narzędziem Updater CE

Jeśli program aktualizujący nie może dokończyć zadania, ta sama instalacja obejmuje narzędzia ręczne. [SP Flash Tool](../sp-flash-tool_pl.html) jest dostępny w pakiecie na komputerach z systemem Windows i Linux x86, a trasa MTKClient obejmuje system macOS. Obydwa wymagają pakietu oprogramowania sprzętowego pasującego do modelu, dostępnego na stronie [Pobieranie oprogramowania sprzętowego](../firmware_pl.html) strona.

Skorzystaj z przewodnika dla swojej platformy i dbaj o to, aby odtwarzacz był naładowany. Jeśli żadne narzędzie w ogóle nie wykryje odtwarzacza, przyczyną problemu jest prawdopodobnie sprzęt, a nie oprogramowanie sprzętowe.

## Co uwzględnić, prosząc o pomoc
  - Model — Y1 lub Y2 — wydrukowany na odtwarzaczu.
  - Co robi ekran: nic, logo, pętla rozruchowa lub ekran główny.
  - Czy komputer wykrywa odtwarzacz jako urządzenie MediaTek.
  - Dokładny komunikat aktualizatora i wybrany pakiet.
  - To, co już wypróbowałeś, łącznie z dowolnym narzędziem ręcznym.

Nie publikuj prywatnych tokenów ani niepowiązanych plików systemowych. The [społeczność Discord](https://discord.gg/zHrT2zrcek) i [r/innioasis](https://reddit.com/r/innioasis) to najszybsze miejsca do porównywania notatek.

## Innioasis Często zadawane pytania dotyczące odzyskiwania

### Jak naprawić odtwarzacz Innioasis, który się nie włącza?

Ładuj go przez 30 minut za pomocą znanego kabla do transmisji danych, wymuś ponowne uruchomienie, przytrzymując zasilanie przez 15 sekund, a następnie sprawdź, czy komputer go wykrywa. Jeśli tak, przywróć oryginalne oprogramowanie dopasowane do modelu; jeśli nie, skorzystaj z narzędzi do ręcznego odzyskiwania dołączonych do narzędzia Updater CE.

### Dlaczego moje kółko przewijania Y1 lub Y2 nie działa?

Jeśli kierownica zatrzymała się po aktualizacji, zwykle jest to spowodowane niezgodnością oprogramowania sprzętowego. Zainstaluj ponownie oryginalne oprogramowanie dopasowane do modelu i przetestuj ponownie. Jeśli w każdym oprogramowaniu sprzętowym kierownica nie działa, potraktuj to jako usterkę sprzętową.

### Skąd pobrać oprogramowanie sprzętowe do odzyskiwania?

Strona pobierania oprogramowania sprzętowego pod adresem innioasis.app/firmware.html zawiera oryginalne i niestandardowe pakiety dla każdego modelu. Zawsze wybieraj pakiet Y1 lub Y2 pasujący do odtwarzacza.

### Jakie narzędzia do odzyskiwania są zawarte w Updater CE?

Updater CE zawiera SP Flash Tool dla systemów Windows i Linux oraz trasę MTKClient, w tym dla systemu macOS, do ręcznego odzyskiwania, gdy nie można zakończyć normalnej instalacji.

## Powiązane poprawki
  - [Kółko przewijania Y1 nie działa](y1-scroll-wheel-not-working_pl.html) — kółko kliknięcia nie odpowiada po aktualizacji
  - [Kółko przewijania Y2 nie działa](y2-scroll-wheel-not-working_pl.html) — te same kontrole dla Y2
  - [Y1 nie włącza się](y1-wont-turn-on_pl.html) — ładowanie, ponowne uruchomienie i ręczne odzyskiwanie
  - [Y2 nie włącza się](y2-wont-turn-on_pl.html) — te same kontrole dla Y2
  - [SP Flash Tool przewodnik](../sp-flash-tool_pl.html) — ręczne flashowanie w systemach Windows i Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
