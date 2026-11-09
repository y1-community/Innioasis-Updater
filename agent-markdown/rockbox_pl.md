---
title: "Jak zainstalować Rockbox na swoim Innioasis Y1 lub Y2 - Innioasis aktualizatorze"
description: "Zainstaluj Rockbox na Innioasis Y1 lub Y2 z aktualizatorem: motywy, wydania stabilne, uwagi Type A i Type B oraz sposób późniejszego przywrócenia oryginalnego oprogramowania."
language: "pl"
source: "https://innioasis.app/rockbox_pl.html"
---

# Jak zainstalować Rockbox na swoim Innioasis Y1 lub Y2 - Innioasis aktualizatorze

Rockbox odniesienie

# Pobieram Rockbox na swoim Y1 lub Y2

Rockbox zmienia oprogramowanie odtwarzacza i otwiera głębszy interfejs odtwarzacza muzyki, sterowanie odtwarzaniem, sortowanie i opcje motywu. Instalacja jest prowadzona z przewodnikiem, ale Y1 i Y2 to oddzielne procesy.[Rockbox na Y1](guides/rockbox-y1.html)[Rockbox na Y2](guides/rockbox-y2.html)[Dlaczego Rockbox?](rockbox-benefits_pl.html)

## Co zmienia instalacja

Rockbox to oprogramowanie niestandardowe. Nie eliminuje to możliwości powrotu do standardowego interfejsu, gdy dostępny jest pasujący oryginalny pakiet oprogramowania. Może usprawnić przeglądanie muzyki i dostosowywanie, ale funkcje, rozdzielczość, czas pracy baterii i zgodność motywów zależą od wersji.Nie mieszaj modeli. Wybierz Y1 dla odtwarzacza Y1 i Y2 dla odtwarzacza Y2. Podobnie wyglądająca nazwa wydania nie jest wystarczającym dowodem na to, że pakiet jest kompatybilny.

## Obejrzyj wideo

Film autorstwa Frawgeeys. Pokazuje trasę Innioasis Aktualizatora; wykonaj poniższe pisemne kroki dotyczące konkretnego modelu dla swojego Y1 lub Y2.

Film autorstwa [Plac Krystiana](https://www.youtube.com/@CristianPlaza) (hiszpański), pokazując Rockbox na Y1. Wykonaj poniższe czynności dotyczące konkretnego modelu odtwarzacza.

## Udostępniona trasa narzędzia Updater
  - Zainstaluj Updater i nie podłączaj niczego, dopóki nie zapyta.
  - Wybierz model wydrukowany na odtwarzaczu Model urządzenia.
  - Wybierz Rockbox w Oprogramowanie.
  - Wybierz stabilną wersję, chyba że celowo testujesz wersję nocną.
  - Kliknij Zainstaluj / Przywróć, a następnie postępuj zgodnie z instrukcjami dotyczącymi wyłączenia zasilania i połączenia USB.
  - Rozłącz dopiero po wyświetleniu komunikatu o powodzeniu.

## 240p, 360p i motywy

Starsze Rockbox kolekcje motywów można tworzyć w rozdzielczości 240p. Y1 kompilacje społecznościowe również korzystają z etykiet zgodności 360p. Zanim wybierzesz kompilację, przeczytaj informacje o wydaniu i źródło motywu. Motyw stworzony dla jednej rozdzielczości lub rodziny oprogramowania może nie działać na innej.[Przeglądaj tematy społeczności](https://themes.innioasis.app/?lang=pl)[Narzędzia tematyczne](https://themes.innioasis.app/?lang=pl)

## Powrót do oryginalnego oprogramowania

Wybierz ponownie ten sam model, wybierz Oprogramowanie oryginalne, wybierz stabilną wersję i użyj Zainstaluj / Przywróć. Jeżeli awaria wystąpiła przed pojawieniem się monitu USB, sprawdź komputer i wyodrębnione pliki. Jeśli odtwarzacz został wykryty, ale flashowanie nie powiodło się, zacznij od [rozwiązywanie problemów](troubleshooting_pl.html).[Y1 przywróć](guides/restore-original-y1.html)[Y2 przywróć](guides/restore-original-y2.html)

## Najczęstsze pytaniaZainstalowałem ponownie Rockbox i nic to nie naprawiło.

Ponowna instalacja Rockbox zapisuje tę samą kompilację w tych samych plikach, więc nie może zresetować rzeczy, które Rockbox trzyma na MicroSD. Jeśli problemem są uszkodzone ustawienia, motyw, lista odtwarzania lub baza danych znajdująca się na karcie, ponowna instalacja nie usunie problemu. Niezawodny reset polega na usunięciu `.rockbox` folder z MicroSD — Rockbox tworzy nowy przy następnym uruchomieniu.
  - Wyłącz całkowicie odtwarzacz i wyjmij kartę MicroSD lub podłącz odtwarzacz jako dysk USB.
  - Pokaż ukryte pliki na swoim komputerze, aby folder był widoczny. Jak wyświetlić ukryte plikiPokaż pliki dot na swoim komputerzeWindows: w Eksploratorze plików otwórz plik Pogląd zakładkę i zaznacz Ukryte przedmioty.macOS: w prasie Findera Cmd+Shift+. aby przełączyć ukryte pliki.Linux · Pliki GNOME: naciśnij Ctrl+Hlub otwórz menu i wybierz Pokaż ukryte pliki.Linux · KDE Dolphin: naciśnij Ctrl+Hlub użyj Widok → Pokaż ukryte pliki.
  - Usuń `.rockbox` folder z katalogu głównego karty.
  - Włóż ponownie kartę i uruchom odtwarzacz. Rockbox odtwarza folder z ustawieniami domyślnymi.
  - Zastosuj ponownie motyw i ustawienia. Jeśli problem powraca dopiero po określonym motywie, przyczyną jest ten motyw.

Usuwanie `.rockbox` nie odinstalowuje Rockbox i nie ma wpływu na Twoją muzykę — folder zawiera ustawienia, motywy i pamięć podręczną oraz jest automatycznie odbudowywany. Jeśli chcesz zachować swoje motywy, skopiuj folder z `.rockbox` przed jego usunięciem lub zmień nazwę folderu na `.rockbox-old` pierwszy.Dlaczego nie widzę folderu .rockbox na moim MicroSD?

Foldery, których nazwa zaczyna się od kropki, są domyślnie ukryte na większości komputerów. Nie musisz go widzieć, aby zainstalować Rockbox — Aktualizator obsługuje pliki. Jeśli rozwiązujesz problem i chcesz go usunąć, najpierw włącz ukryte pliki. Jak wyświetlić ukryte plikiPokaż pliki dot na swoim komputerzeWindows: w Eksploratorze plików otwórz plik Pogląd zakładkę i zaznacz Ukryte przedmioty.macOS: w prasie Findera Cmd+Shift+. aby przełączyć ukryte pliki.Linux · Pliki GNOME: naciśnij Ctrl+Hlub otwórz menu i wybierz Pokaż ukryte pliki.Linux · KDE Dolphin: naciśnij Ctrl+Hlub użyj Widok → Pokaż ukryte pliki.Czy usunięcie .rockbox zresetuje mój motyw i ustawienia?

Tak - `.rockbox` przechowuje ustawienia, motyw, listy odtwarzania i bazę danych w pamięci podręcznej Rockbox. Usunięcie go przywraca Rockbox do czystego stanu domyślnego. Utwórz kopię zapasową całego folderu (lub zmień jego nazwę na `.rockbox-old`), jeśli chcesz coś z tego odzyskać, uruchom odtwarzacz, a Rockbox utworzy nowy folder.

## Więcej przewodników Rockbox-Y1 i Rockbox-Y2.

Zapoznaj się ze szczegółowymi przewodnikami dotyczącymi instalowania, pobierania, tworzenia motywów, przywracania i rozwiązywania problemów Rockbox w obu modelach:[Rockbox-Piasta Y1](rockbox-y1/)[Rockbox-Y2 piasta](rockbox-y2/)[Rockbox Pobieranie ROM-u](rockbox-rom-download_pl.html)[Rockbox dla Y1](rockbox-for-y1_pl.html)[Rockbox dla Y2](rockbox-for-y2_pl.html)[Rockbox-Y1 kontra Y2](rockbox-y1-vs-y2.html)[Rockbox-Motywy Y1](rockbox-y1-themes.html)[Rockbox-Motywy Y2](rockbox-y2-themes.html)

## Czy to odniesienie było przydatne?

Twoja odpowiedź pomoże ulepszyć ten przewodnik.TakJeszcze nie[Daj nam znać, jak możemy się ulepszyć](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
