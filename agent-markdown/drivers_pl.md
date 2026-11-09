---
title: "Innioasis Y1 i Y2 USB sterowniki | Uprawnienia sterownika Windows i systemu Linux - Innioasis Aktualizator"
description: "Skonfiguruj komputer dla narzędzia Innioasis Updater: uprawnienia do sterownika dla systemu Windows MediaTek i systemu Linux USB — a także poprawki dotyczące kabli i taktowania."
language: "pl"
source: "https://innioasis.app/drivers_pl.html"
---

# Innioasis Y1 i Y2 USB sterowniki | Uprawnienia sterownika Windows i systemu Linux - Innioasis Aktualizator

Konfiguracja komputera

# Przygotuj komputer przed graczem.

Większość problemów z połączeniem wynika ze sterownika, uprawnień, kabla lub taktowania. System Windows wymaga zainstalowania sterownika MediaTek. Linux potrzebuje odpowiednich USB uprawnień. Znajdź swoją platformę poniżej.[Pobierz Updater CE](guide_pl.html#platform)[Rozwiązywanie problemów](troubleshooting_pl.html)

## Windows
  - Pobierz poniższy instalator sterownika MediaTek.
  - Uruchom instalator i pozwól systemowi Windows zainstalować sterownik.
  - Uruchom ponownie komputer.
  - Otwórz Updater CE i poczekaj na monit o połączenie, zanim podłączysz wyłączony odtwarzacz.

Niektóre systemy Windows blokują sterownik poprzez izolację rdzenia (integralność pamięci). Jeśli Updater CE nadal nie widzi odtwarzacza po ponownym uruchomieniu, wyłącz integralność pamięci w Zabezpieczeniach Windows, uruchom ponownie i ponownie zainstaluj sterownik. Po zakończeniu włącz to ustawienie ponownie, jeśli system na to pozwala.

System Windows nie uruchamia aplikacji? Jeśli zabezpieczenia systemu Windows lub funkcja Smart App Control uniemożliwiają otwarcie narzędzia Updater CE, otwórz Ustawienia (naciskać Win + I) → Prywatność i bezpieczeństwo → Windows Security → Kontrola aplikacji i przeglądarki → Ustawienia inteligentnej kontroli aplikacji i ustaw to Wyłączony. Inteligentna kontrola aplikacji ma obecnie wpływ na popularne aplikacje, takie jak Epic Overlay Service (używana przez Fortnite) — Updater CE jest bezpieczny i zweryfikowany. Aby włączyć ponownie później, ustaw `VerifiedAndReputablePolicyState` do `1` (Wł.) lub `2` (Tryb oceny) pod `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` w Edytorze rejestru.[Pobierz sterownik dla systemu Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Powrót do głównego przewodnika](guide_pl.html#windows) · [Pobieranie oprogramowania](firmware_pl.html)

## Uprawnienia w systemie Linux USB

Linux potrzebuje Twojego konta użytkownika, aby móc komunikować się z chipem MediaTek USB wewnątrz odtwarzacza. Updater CE zwykle rozwiązuje ten problem podczas instalacji i te same uprawnienia obejmują SP Flash Tool, więc traktuj to jako krok naprawczy, a nie normalny etap.
  - Uruchom Updater CE jako zwykły użytkownik, a nie jako root. Instalator prosi o dostęp administratora tylko wtedy, gdy tego potrzebuje.
  - Sprawdź, czy odtwarzacz jest w ogóle widoczny. Wyłącz odtwarzacz, podłącz kabel i uruchom polecenie lsusb w terminalu. Podłączony odtwarzacz pojawia się jako urządzenie MediaTek z identyfikatorem dostawcy 0e8d.
`lsusb`
  - Jeśli pojawia się w lsusb, ale Innioasis Updater CE lub SP Flash Tool wyświetla komunikat odmowy uprawnień lub nie może otworzyć portu, oznacza to, że Twój użytkownik nie ma dostępu do urządzenia USB. Ta sama reguła udev dotyczy obu narzędzi, więc dodaj takie, które pozwoli grupie użytkowników je przeczytać.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Zapisz tę linię w nowym pliku o nazwie /etc/udev/rules.d/51-innioasis.rules, a następnie uruchom:`sudo udevadm control --reload && sudo udevadm trigger`
  - Odłącz całkowicie odtwarzacz, podłącz go ponownie i ponów próbę instalacji.
  - Jeśli SP Flash Tool zgłosi pozwolenie na port szeregowy lub wyścig portów, odłącz całkowicie i podłącz ponownie tylko po wyświetleniu monitu.
Nie improwizuj przesunięć flash.Jeśli przejdziesz na narzędzie do ręcznego odzyskiwania, użyj plików i konfiguracji specyficznej dla modelu dostarczonej z projektem.

[Powrót do głównego przewodnika](guide_pl.html#linux) · [Pobieranie oprogramowania](firmware_pl.html) · [SP Flash Tool przewodnik](sp-flash-tool_pl.html)

## Kabel i rozrządu
  - Użyj znanego kabla do transmisji danych USB.
  - Podczas rozwiązywania problemów unikaj koncentratorów.
  - Całkowicie wyłącz odpowiedni model.
  - Połącz się tylko po wyświetleniu monitu.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
