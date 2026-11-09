---
title: "Problemen met het opstarten van Windows 10/11-apps en oplossing voor Smart App Control - Innioasis Updater"
description: "Als Windows 10/11 of Smart App Control ervoor zorgt dat u de app niet kunt starten, volgt u hier de oplossing."
language: "nl"
source: "https://innioasis.app/notices/2026-11-07-codesigning_nl.html"
---

# Problemen met het opstarten van Windows 10/11-apps en oplossing voor Smart App Control - Innioasis Updater

Van 25-10-2026 · tot 31-12-2026 · Modellen: Y1,Y2

# Problemen met het opstarten van Windows 10/11-apps en oplossing voor Smart App Control

Als Windows 10/11 of Smart App Control ervoor zorgt dat u de app niet kunt starten, volgt u hier de oplossing.

Van 25-10-2026 · tot 31-12-2026 · Modellen: Y1,Y2

Er zijn vals-positieve rapporten ingediend bij Microsoft voor `installer.exe` en `InnioasisUpdater.exe` en actie ondernomen, maar als Windows Endpoint Protection of Smart App Control de applicatie op uw computer nog steeds blokkeert, gebruikt u deze oplossing:

### Tijdelijke oplossing: schakel Smart App Control uit
  - Open Windows Instellingen (druk `Win + I`).
  - Ga naar Privacy en veiligheid > Windows-beveiliging > App- en browsercontrole.
  - Onder Slimme app-bediening, klik Instellingen voor Smart App-bediening.
  - Stel Slimme app-bediening in op Uit. Hierdoor kan de app onmiddellijk worden geopend en uitgevoerd.

Als Windows of Edge verhindert dat u Updater CE downloadt, klikt u op meer opties (…) Dan Houden > Laat meer zien > Hoe dan ook behouden.

### Slimme app-bediening opnieuw inschakelen

Wanneer de fout-positieve definities op uw computer zijn bijgewerkt, kunt u Smart App Control opnieuw inschakelen via het Windows-register:
  - Druk op Windows-toets + R, typ `regedit`en druk op Enter om de Register-editor als beheerder te openen.
  - Navigeer naar: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (of `Policies`).
  - Lokaliseren `VerifiedAndReputablePolicyState` in het rechterdeelvenster.
  - Dubbelklik `VerifiedAndReputablePolicyState` en verander de waardegegevens in:

  - `1` = Aan (afgedwongen)
  - `2` = Evaluatiemodus

  - Klik op OK, sluit de Register-editor en start uw computer opnieuw op.

[Zie het installer.exe-rapport aan Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Zie het rapport InnioasisUpdater.exe aan Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Open de gekoppelde pagina](https://innioasis.app/notices.html)

[← Alle mededelingen](index_nl.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
