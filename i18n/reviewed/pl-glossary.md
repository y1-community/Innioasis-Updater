# Polish (pl) glossary and style guide

Used for the reviewed Polish catalog (`i18n/reviewed/pl.json`). Anyone editing
Polish copy should follow it so the site reads as one voice.

## Audience and tone

The readers are owners of small music players (Innioasis Y1/Y2 and similar)
installing community firmware. Write the way a Polish tech forum or a good
Polish software UI talks: plain, practical, natural. Not academic, not
grandiose, not word-for-word English.

- Address the reader with informal **ty** throughout (never "Pan/Pani", never
  impersonal "należy" chains when "musisz" / imperative reads better).
- Buttons and links: imperative, 2nd person singular: **Pobierz**,
  **Zainstaluj**, **Otwórz**, **Przeglądaj**, **Wesprzyj**.
- Headings and titles use Polish sentence case: only the first word and proper
  nouns are capitalised ("Pobieranie firmware", not "Pobieranie Firmware").
- Use Polish quotation marks „…” in prose. Keep straight quotes inside code.
- Translate meaning, not word order. Rebuild the sentence if needed.
- Safety warnings (power off, back up, do not disconnect) stay as strong and
  unambiguous as the English.

## Never translate

- Product, firmware, ROM, app and brand names, **even when they look like
  ordinary English words**: Classy, Solar, Rondo, Lithium, Reborn, Nugget,
  Koensayr, Inniclassic, Better-Y, JJ Launcher, Y2Player, Y2Linux, Rockbox,
  Rockbox-Y1/-Y2, Innioasis, Innioasis Updater, Updater CE, Timmkoo, Mechen,
  SP Flash Tool, MTKClient, Homebrew (as product), Discord, GitHub, Ko-fi,
  PayPal, etc. Device models: Y1, Y2, G1, G3, G5, PR1, R1, D1, Q3, Q5, A5, SR1.
- Version numbers and dates stay right after the name they belong to:
  "Classy 20261117" → "Classy 20261117"; "Classy (formerly Inniclassic for Y2)"
  → "Classy (dawniej Inniclassic dla Y2)".
- File names, extensions, paths, commands, code: `.zip`, `rom.zip`,
  `scatter.txt`, APK, ROM, USB, microSD.
- App UI labels that Updater CE shows in English, when quoted in step-by-step
  instructions: "Keep Data", "Device Model", "Software", "Install / Restore",
  "Show Advanced Settings", "Type A" / "Type B", and "Original Software" when it
  names the dropdown option. In ordinary prose, "original software" is
  "oryginalne oprogramowanie".
- Code-like fragments that wrap `_t("…")`: the argument is a catalog key, so it
  stays in English.

## Terms

| English | Polish | Notes |
| --- | --- | --- |
| firmware | firmware | indeclinable: "pobierz firmware", "wersja firmware", "aktualizacje firmware". **Never** "oprogramowanie sprzętowe". |
| custom firmware | custom firmware | or "nieoficjalny firmware" where it reads better |
| Original Software (stock firmware) | oryginalne oprogramowanie | fabryczne oprogramowanie in prose is fine |
| stock | fabryczny | |
| software | oprogramowanie | |
| Software Updates and Firmware | Aktualizacje oprogramowania i firmware | |
| theme | motyw | **never** "temat" (= topic) |
| Theme Gallery | Galeria motywów | |
| skin | skórka | |
| Get (button / link) | Pobierz / Zainstaluj / Sprawdź (by context) | **never** "Zdobądź" |
| Download (verb, button) | Pobierz | |
| Downloads (section) | Pliki do pobrania | |
| Downloads: N (counter) | Liczba pobrań: N | |
| download (noun, a file) | plik do pobrania / pobieranie | |
| flash (verb) | wgrać / wgrywać | "flashować" acceptable in technical how-tos |
| flashing tool | narzędzie do wgrywania firmware | |
| install / installer | zainstaluj / instalator | |
| restore | przywróć / przywracanie | |
| update / updater | aktualizacja / zaktualizuj | the app name "Innioasis Updater" stays |
| release | wydanie | |
| release notes | informacje o wydaniu | |
| build (a release) | wersja / build | **never** "budowa"; "kompilacja" only for compiling |
| base ROM | bazowy ROM | |
| player | odtwarzacz | |
| device | urządzenie | |
| guide | poradnik | "przewodnik" only for long multi-page guides |
| troubleshooting | rozwiązywanie problemów | |
| driver | sterownik | |
| mirror (download mirror) | serwer lustrzany / mirror | never a looking-glass |
| zip (archive) | ZIP / plik ZIP | never a zipper |
| archive | archiwum | |
| community | społeczność | |
| support (help) | pomoc | |
| support (donate) / Donate | Wesprzyj / wsparcie | |
| donation | darowizna / wpłata | |
| dock (bottom toolbar) | pasek narzędzi | |
| settings | ustawienia | |
| light / dark mode | jasny / ciemny motyw | |
| accent colour | kolor akcentu | |
| beta | beta | "wersja beta" in prose |
| homebrew | homebrew | |
| launcher | launcher | |
| click wheel | kółko dotykowe (click wheel) | |
| Platform (OS picker) | System | |
