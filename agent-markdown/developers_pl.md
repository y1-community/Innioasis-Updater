---
title: "Deweloperzy | Dodaj niestandardowe oprogramowanie sprzętowe do Innioasis Updater CE - Innioasis Pobieranie oprogramowania sprzętowego"
description: "Dokumentacja dla programistów dotycząca dodawania niestandardowego oprogramowania sprzętowego Innioasis Y1 lub Y2 do Updater CE: fork repozytorium, publikowanie zasobów rom.zip, edycja pliku slidia_manifest.xml, testowanie i otwieranie żądania ściągnięcia."
language: "pl"
source: "https://innioasis.app/developers_pl.html"
---

# Deweloperzy | Dodaj niestandardowe oprogramowanie sprzętowe do Innioasis Updater CE - Innioasis Pobieranie oprogramowania sprzętowego

Dla twórców oprogramowania sprzętowego

# Dodaj swoje oprogramowanie do Updater CE.

Updater CE to katalog społecznościowy i instalator niestandardowego oprogramowania sprzętowego. Opracuj swój projekt od bazy ROM, opublikuj go jako publiczne repozytorium z odpowiednimi zasobami wersji, dodaj wpisy modelu do `slidia_manifest.xml`, przetestuj filtry modelu i otwórz żądanie ściągnięcia. Jedno repozytorium może obsługiwać każdy model, który obsługuje.[Wyświetl źródło narzędzia Updater CE](https://github.com/y1-community/Innioasis-Updater)[Przeglądaj pliki do pobrania oprogramowania](firmware_pl.html)

## Zacznij od bazy ROM

Podstawowe pamięci ROM zapewniają twórcom niestandardowego oprogramowania sprzętowego czystą podstawę systemu Android z włączonymi bezprzewodowymi chipami radiowymi. W Y1 umożliwiają Wi-Fi i GPS wraz z fabrycznym Bluetooth i FM; w Y2 umożliwiają Wi-Fi, GPS i FM obok fabrycznego Bluetooth.Podstawowe ROM pliki do pobrania w celu opracowania niestandardowego oprogramowania sprzętowego, z wersją Androida i funkcjami bezprzewodowymi dostępnymi w każdym z nich[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Pobierz | Urządzenie | Android | Funkcje bezprzewodowe |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Dodaje Wi-Fi i GPS do fabrycznego Bluetooth i FM (FM działa już fabrycznie na Y1). Dla Y1 odtwarzaczy z systemem operacyjnym 2.0.0 lub nowszym. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Dodaje Wi-Fi i GPS do fabrycznego Bluetooth i FM (FM działa już fabrycznie na Y1). Dla Y1 graczy z systemem operacyjnym starszym niż 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Dodaje Wi-Fi, GPS i FM do fabrycznego Bluetooth. Układ radiowy Y2 jest w pełni włączony, więc FM jest dostępny również tutaj. |

Te obrazy przedstawiają standardową wersję systemu Android (AOSP) z włączoną łącznością bezprzewodową urządzenia, więc niestandardowe oprogramowanie sprzętowe może dodawać funkcje sieciowe zamiast zastępować stos radiowy. Stanowią one praktyczny punkt wyjścia dla poniższych etapów publikowania.

## Użyj tych nazw zasobów wersji

Nazwa pliku jest częścią sygnału zgodności. Zachowaj dokładne nazwy i umieść pliki ZIP w zasobach wersji projektu, a nie tylko w drzewie źródłowym repozytorium.Nazwy oprogramowania sprzętowego ZIP i obsługiwane urządzenia``````

| Zaleta | Urządzenie | Sprzęt | Oznaczający |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 urządzenia dostarczone z systemem operacyjnym 2.0.0 lub nowszym. |
| rom_type_b.zip | Y1 | Type B | Y1 urządzenia dostarczone z systemem operacyjnym starszym niż 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Pakiet pełnej instalacji Y2. Trzymaj go oddzielnie od Y1 zasobów. |
Nie zmieniaj nazwy pakietu, aby pasował do innego modelu. Y1 i Y2 używają różnych plików platformy MediaTek i konfiguracji flashowania. Opublikuj pakiet dla sprzętu, który faktycznie obsługuje.

## Jak działa połączenie

Updater CE odczytuje manifest jako swój katalog. Każdy `<package>` line podaje nazwę projektu, repozytorium, model i procedurę obsługi. Gdy użytkownik wybierze ten projekt, Updater sprawdza opublikowane wersje repozytorium i szuka pliku `rom*.zip` zaleta.

### Oczywisty

Nazywa projekt i przypisuje go do modelu. Y1 i Y2 wymagają oddzielnych wierszy, nawet jeśli współdzielą repozytorium.

### Opublikowane wydanie

Zawiera instalowalne zasoby ZIP. Pojedyncze wydanie może zawierać razem pakiety Y1 Type A, Y1 Type B i Y2.

### Instalacja aktualizatora CE

Używa wybranego modelu do wybrania pasującego pakietu i ścieżki flashowania specyficznej dla modelu. Użytkownik nie powinien zgadywać nazwy pliku.

## Publikowanie projektu w pięciu krokach
  - Forkuj repozytorium Updater CE. Stwórz swój własny widelec [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), a następnie sklonuj widelec lokalnie.
  - Przygotuj publiczne repozytorium oprogramowania sprzętowego. Upewnij się, że repozytorium jest publiczne i jego wersja zawiera prawidłowe zasoby ZIP. Możesz umieścić `rom.zip`, `rom_type_b.zip`, i `rom_y2.zip` w tym samym wydaniu, jeśli należą do tej samej wersji.
  - Edytuj manifest. Otwórz `slidia_manifest.xml` w katalogu głównym widelca Updater CE. Dodaj jedną linię dla każdego modelu obsługiwanego przez wydanie (Y1 i Y2 to wspólna para). The `repo` wartością jest repozytorium `owner/repository`; `url` to publiczna strona projektu.
  - Przetestuj katalog. Uruchom Updater z edytowanego koszyka. Wybierz Y1 i potwierdź, że projekt pokazuje zasoby Y1. Wybierz Y2 i potwierdź, że wyświetla się wersja Y2. Sprawdź osobno Type A i Type B, gdy oba zostaną opublikowane.
  - Otwórz żądanie ściągnięcia. Wypchnij zmianę manifestu do rozwidlenia i otwórz żądanie ściągnięcia względem nadrzędnego repozytorium Updater CE. Dołącz link do projektu, obsługiwane modele, znacznik wersji, nazwy zasobów i testowane urządzenia.

## Wygeneruj linie manifestu

Wypełnij repozytorium i zaznacz każdy model obsługiwany przez tę wersję. Generator zapisuje jeden `<package>` linii na model i zawiera tylko ustawione przez Ciebie atrybuty, więc wynik jest zgodny z bieżącym `slidia_manifest.xml` format. Każdy atrybut odczytany przez Updater CE jest dostępny poniżej — opcjonalne znajdują się poniżej Więcej opcji.Adres URL repozytoriumRepozytorium publiczne GitHub. Generator ekstraktów `owner/repository` z adresu URL.Nazwa oprogramowaniaWyświetlane w aplikacji i katalogu witryny.Adres URL projektuStrona projektu skierowana do ludzi lub informacje o jego wersji.MarkaWyczyść tę opcję, aby użyć domyślnej marki modelu. SR1, Q3, Q5 i Q3e to modele Timmkoo.Urządzenia (po jednej linii każde)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eInne modeleDla modelu, który nie jest wymieniony powyżej. Znane modele zachowują pisownię katalogową.Flagi`do_not_keep_data` — nigdy nie oferuj funkcji Keep Data dla tego oprogramowaniaZbudowany na podstawie oryginalnego oprogramowania — dodaje `derivative="y1-community/y1-stock-rom"`

Funkcja Keep Data jest oferowana tylko wtedy, gdy przychodzące i zainstalowane oprogramowanie sprzętowe są takie same lub udostępniają a `derivative` źródło. Używaj flagi tylko wtedy, gdy naprawdę nie można przenieść danych użytkownika.Więcej opcji: ikona, grafika, zasoby wersji, instalacja poinstalacyjna i kopie lustrzane

#### Ikona i grafikaPlik ikonyWybierz obraz, który zatwierdzisz w repozytorium. Spowoduje to wyświetlenie podglądu i utworzenie surowego adresu URL; nic nie wgrywa.Ścieżka ikony w repozytoriumŚcieżka do zatwierdzonego obrazu względem katalogu głównego repozytorium.Ikona gałęziAdres URL ikonyBezpośredni adres URL obrazu. Gdy jest pusty, aplikacja korzysta z wersji `updater.png` lub wygenerowaną ikonę.Podgląd wybranej ikony

Adres URL ikony trybu ciemnegoOpcjonalna ikona ciemnego motywu. `image_dark` jest akceptowanym pseudonimem.Adres URL lekkiej grafikiGrafika wtórna, wypróbowana po wydaniu obrazu i `icon`.Adres URL ciemnej grafiki

#### Zwolnij zasobyZwolnij nazwę zasobuJedna nazwa dla każdego wybranego modelu. Pozostaw puste do użycia `rom.zip` na Y1 i `rom_<model>.zip` gdzie indziej.Wzór aktywówGlob używany, gdy zamki błyskawiczne wydania nie są nazwane `rom*.zip`.Type A zasóbGlob dla pakietu Y1 Type A, jeśli jego nazwa tego nie mówi.Type B zasóbGlob dla pakietu Y1 Type B, jeśli jego nazwa tego nie mówi.Minimalna wersja aplikacjiUkryj wpis w starszych kompilacjach narzędzia Updater CE.

#### Linki, kopie lustrzane i rodzina Keep DataStrona poinstalacyjnaOtwarty po udanej instalacji.Druga strona po instalacjiOpcjonalny drugi krok w przypadku wielostronicowego przewodnika konfiguracji.Przenośne lusterka zapinane na zamekOddzielone przecinkami `*-mirror` repozytoria budujące pakiety Portable Flashing Zip.Repozytorium instrumentów pochodnychOprogramowanie sprzętowe, z którego zbudowana jest ta wersja. Powiązane oprogramowanie sprzętowe udostępnia partycję danych, co sprawdza Keep Data.Repozytorium informacjiRepozytorium aplikacji, którego wydania opisują aplikacje w tym oprogramowaniu. Potrzebuje także strony poinstalacyjnej.APK repozytoriumRepozytorium aplikacji, którego APK aplikacja pobiera i instaluje po oprogramowaniu sprzętowym.

#### Dodatki do kataloguŚlimakStabilny identyfikator linków i zapisanych rekordów instalacji. Model zostanie dodany automatycznie po wybraniu kilku modeli.Opis`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Skopiuj linie

Ładowanie najnowszego manifestu…Wyświetl podgląd najnowszego manifestu z dodanymi liniami

Generator pobierał prąd `slidia_manifest.xml` z tego repozytorium i wstawiłem wygenerowane linie tuż wcześniej `</slidia>`.

Jedna linia nie wystarczy na wspólne repozytorium. Jeśli brakuje wiersza Y2, użytkownicy Y2 nie otrzymają wpisu dopasowanego do modelu, nawet jeśli `rom_y2.zip` istnieje w wydaniu projektu. To samo dotyczy każdego innego modelu obsługiwanego przez Twoją wersję.

### Każdy atrybut odczytywany przez manifest

Są to atrybuty zrozumiałe dla obecnych wersji Updater CE. Generator zapisuje tylko te, które wypełnisz; w pozostałej części aplikacja powraca do rozsądnych ustawień domyślnych.Atrybuty pakietu slidedia_manifest.xml i ich znaczenie``````````````````````````````````````````````````````````````````````````````````````````````

| Atrybut | Wymagany | Co to robi |
| --- | --- | --- |
| name | Tak | Nazwa oprogramowania pokazana w katalogu i na kartach instalacyjnych. |
| repo | Tak | owner/repo. Aplikacja odczytuje wydania GitHub tego repozytorium. |
| device | Tak | Model docelowy, wielkie litery (Y1, Y2, G1, Q3e,…). Zachowaj po jednym wpisie na model. |
| url | Zalecony | Strona projektu lub informacje o wydaniu otwarte z katalogu. |
| type, handler | Tak w praktyce | type="img" i handler="Custom Firmware". Inne typy i procedury obsługi inne niż oprogramowanie sprzętowe są pomijane. |
| brand | Opcjonalne | Marka katalogowa (Innioasis, Timmkoo). Pusty używa domyślnej marki modelu. |
| package_name | Opcjonalne | Zwolnij nazwę pliku zasobu. Domyślnie rom.zip na Y1 i rom_<model>.zip w innych modelach. |
| asset_pattern | Opcjonalne | Glob nieuwzględniający wielkości liter dla wydań, których kody zip oprogramowania sprzętowego nie są nazwane rom*.zip (Na przykład my-firmware-*.zip). |
| type_a_asset, type_b_asset | Opcjonalne | Globy identyfikujące zamki Y1 Type A i Type B, gdy ich nazwy plików nie zawierają zwykłych znaczników. |
| icon | Opcjonalne | Adres URL logo. Używane po wydaniu własnym updater.png / updater.jpgi jako rozwiązanie awaryjne dla każdego wydania. |
| icon_dark | Opcjonalne | Logo z ciemnym motywem. image_dark jest akceptowanym pseudonimem. |
| image | Opcjonalne | Wtórna grafika świetlna, wypróbowana icon. |
| post_install, post_install2 | Opcjonalne | Strony otwarte po pomyślnej instalacji. Drugi obejmuje wieloetapowy przewodnik. |
| portable_zips | Opcjonalne | Oddzielone przecinkami *-mirror repozytoria publikujące gotowe do uruchomienia pakiety przenośne. |
| derivative | Opcjonalne | Repozytorium, z którego zbudowane jest oprogramowanie sprzętowe. Oprogramowanie sprzętowe z tym samym pochodnym katalogiem głównym może przechowywać dane użytkownika. |
| info_repo | Opcjonalne | Repozytorium aplikacji, którego wydania opisują wdrażane oprogramowanie sprzętowe. Wymaga post_install lub post_install2. |
| apk_repo | Opcjonalne | Repozytorium aplikacji, którego APK aplikacja instaluje po oprogramowaniu sprzętowym. |
| min_version | Opcjonalne | Ukryj wpis, jeśli Updater CE jest starszy niż ta wersja. |
| do_not_keep_data | Opcjonalne | true (Również 1 / yes) całkowicie blokuje funkcję Keep Data dla tego oprogramowania sprzętowego. |
| slug | Opcjonalne | Stabilny identyfikator linków i zapisanych rekordów instalacji. Generowane na podstawie nazwy i modelu, gdy jest puste. |
| description | Opcjonalne | Krótki opis katalogu. Może to być wartość atrybutu lub tekst elementu. |

Starsze nazwy są nadal odczytywane pod kątem zgodności: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` i `image_dark`. Nowe wpisy powinny używać aktualnych nazw podanych powyżej.

### Prześlij linie jako żądanie ściągnięcia
  - Skopiuj wygenerowane linie powyżej. Pasują już do najnowszego formatu manifestu.
  - Redagować `slidia_manifest.xml` w repozytorium. Skorzystaj z poniższego linku do edycji; Host repozytorium automatycznie tworzy dla Ciebie rozwidlenie i gałąź.
  - Wklej linie tuż przed `</slidia>`, pozostawienie istniejących wpisów bez zmian.
  - Zaangażuj się w nowy oddział (Na przykład `add-your-firmware`), a następnie otwórz żądanie ściągnięcia względem repozytorium Updater CE.
  - W PR uwzględnij łącze do projektu, obsługiwane modele, znacznik wersji, nazwy zasobów i testowane urządzenia.
[Edytuj manifest programu Updater CE](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Zobacz najnowszy manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Nazwy modeli zachowaj wielkimi literami, użyj dokładnego adresu URL swojego publicznego repozytorium i zachowaj `type="img"` i `handler="Custom Firmware"` dla wpisu oprogramowania sprzętowego.

## Spraw, aby wydanie było łatwe do sprawdzenia

Nadaj wydaniu wyraźny tag i informację o wydaniu. Znacznik jest przydatny dla ludzi, ale nazwy zasobów ZIP są tym, czego program Updater CE używa do identyfikacji pakietów instalacyjnych.

### Lista kontrolna wydania
  - Opublikuj publikację.
  - Dołącz pliki ZIP jako zasoby wersji.
  - Podaj obsługiwany model oraz Type A lub Type B w uwagach.
  - Wymień wszelkie wymagane preparaty lub znane limity.

### Jedno wydanie, trzy zasoby

Udostępniona wersja może zawierać `rom.zip`, `rom_type_b.zip`, i `rom_y2.zip`. Updater klasyfikuje je osobno i wybiera spośród filtrów modelowych i sprzętowych.

### Nie łącz domysłów

Nie dołączaj pakietu Y1 pod nazwą pliku Y2 ani nie dodawaj nieprzetestowanych danych rozproszenia, modułu wstępnego ładowania lub partycji tylko po to, aby pojawił się zasób.

## Dlaczego wpisy modelu mają znaczenie podczas flashowania

Manifest to nie tylko menu pobierania. Po wyodrębnieniu Updater CE wykorzystuje rozwiązany model do przygotowania pasującej ścieżki instalacji. Y1 i Y2 mają różne pliki platformy, programy wstępnego ładowania, konfigurację rozproszoną i układy urządzeń.
  - Y1: aktualizator przygotowuje ścieżkę Y1 i używa nazwanych partycji urządzenia, gdy używana jest MTKClient.
  - Y2: aktualizator przygotowuje ścieżkę Y2 i wykorzystuje konfigurację Y2 MT6582. Pełne odzyskiwanie może wykorzystywać adresy fizyczne z poprawnych dla modelu danych rozproszenia.
  - Obsługa wielu platform: Updater CE obsługuje natywne flashowanie bezpośrednio w systemach Windows, Linux i macOS (obsługujące zarówno komputery Mac z procesorem Intel, jak i Apple Silicon) bez dodatkowych narzędzi do flashowania.
Współautorzy powinni dostarczyć poprawne pliki oprogramowania sprzętowego, a nie offsety flash. Nie edytuj adresów rozproszonych, preloaderów, plików DA ani poleceń partycji, aby obejść uszkodzony pakiet. Napraw zasób wersji i przetestuj na zamierzonym modelu.

## Zanim poprosisz o połączenie
  - Sprawdź poprawność XML za pomocą parsera XML. Brakujący cytat lub zamknięcie `/>` może ukryć każdy wpis po nim.
  - Uruchom aktualizator ze swojej kasy, aby załadować lokalny manifest przed zdalnym odświeżeniem.
  - Sprawdź niezależnie Y1 i Y2. Upewnij się, że projekt pojawia się tylko tam, gdzie obsługiwany jest jego pakiet.
  - Sprawdź listę wydań `rom.zip`, `rom_type_b.zip`, i `rom_y2.zip` stosownie do przypadku.
  - Przetestuj rzeczywistą instalację na zamierzonym urządzeniu, korzystając z niezawodnego kabla do transmisji danych USB i planu odzyskiwania umożliwiającego powrót do oryginalnego oprogramowania.
  - W żądaniu ściągnięcia wyjaśnij, co przetestowałeś. Nie opisuj nieprzetestowanego modelu jako obsługiwanego.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Aby sprawdzić lokalnie, uruchom to polecenie z katalogu głównego repozytorium. Weryfikuje tylko składnię XML; nie dowodzi, że wersja zawiera prawidłowe oprogramowanie sprzętowe lub że urządzenie można bezpiecznie flashować.

## Przydatne linki do projektów[Aktualizator wideł CE](https://github.com/y1-community/Innioasis-Updater/fork)[Zobacz manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Notatki dotyczące wkładu Wspólnoty](support_devs_pl.html)[Rozwiązywanie problemów](troubleshooting_pl.html)

## Umiejętności modowania dla agentów AI

Repozytorium `skills/` katalog to oparta na źródłach baza wiedzy dla agentów pracujących na sprzęcie, oprogramowaniu sprzętowym, motywach i aplikacjach Y1 i Y2. Każda umiejętność nazywa pliki projektu, z których pochodzą jej roszczenia, dzięki czemu agent może sprawdzić fakt przed zmianą urządzenia.Zacznij tutaj

### [Indeks umiejętności i zasady bezpieczeństwa](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Jak załadować umiejętność, jakiego modelu dotyczy dany fakt i jakie partycje nie powinny być zapisywane przez żaden pakiet.Sprzęt

### [Y1 sprzęt](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, koło jako kluczowe zdarzenia, wyświetlacz 480x360, ścieżki FM/audio, pamięć i mapa partycji Type A/B.Sprzęt

### [Y2 sprzęt](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Płytka MT6582, drzewo urządzeń, panele GC9503V/ST7701S, szyny PMIC/DAC, partycje i obraz rozruchowy.Oprogramowanie sprzętowe

### [Pakiety oprogramowania sprzętowego](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomia, pliki rozproszone, umowy dotyczące aktualizacji klasy A i lista kontrolna wydania.Motywy

### [Tworzenie motywów i skórek](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 motywy config.json, Rockbox WPS/SBS, Reborn skórki i Y2Player format skórki v2.Wszystkie umiejętności

### [Przeglądaj folder umiejętności](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, standardowe ROMy na Androida, Y2Linux, aplikacje na Androida, programy uruchamiające, informacje o wydaniu i publikowanie witryn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
