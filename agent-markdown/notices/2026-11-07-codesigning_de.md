---
title: "Probleme beim Start von Windows 10/11-Apps und Problemumgehung für Smart App Control – Innioasis Updater"
description: "Wenn Windows 10/11 oder Smart App Control Sie daran hindert, die App zu starten, folgen Sie der Problemumgehung hier."
language: "de"
source: "https://innioasis.app/notices/2026-11-07-codesigning_de.html"
---

# Probleme beim Start von Windows 10/11-Apps und Problemumgehung für Smart App Control – Innioasis Updater

Vom 25.10.2026 · bis 31.12.2026 · Modelle: Y1, Y2

# Probleme beim Starten von Windows 10/11-Apps und Problemumgehung durch Smart App Control

Wenn Windows 10/11 oder Smart App Control Sie daran hindert, die App zu starten, folgen Sie der Problemumgehung hier.

Vom 25.10.2026 · bis 31.12.2026 · Modelle: Y1, Y2

Es wurden falsch positive Berichte an Microsoft übermittelt `installer.exe` und `InnioasisUpdater.exe` und Maßnahmen ergriffen, aber wenn Windows Endpoint Protection oder Smart App Control die Anwendung auf Ihrem Computer immer noch blockiert, verwenden Sie diese Problemumgehung:

### Vorübergehende Problemumgehung: Deaktivieren Sie die intelligente App-Steuerung
  - Öffnen Sie Windows Einstellungen (drücken `Win + I`).
  - Gehe zu Datenschutz und Sicherheit > Windows-Sicherheit > App- und Browsersteuerung.
  - Unter Intelligente App-Steuerung, klicken Smart App Control-Einstellungen.
  - Stellen Sie Smart App Control auf ein Aus. Dadurch kann die App sofort geöffnet und ausgeführt werden.

Wenn Windows oder Edge Sie daran hindern, Updater CE herunterzuladen, klicken Sie auf „Weitere Optionen“ (…) Dann Halten > Mehr anzeigen > Behalte es trotzdem.

### Smart App Control wird wieder aktiviert

Wenn die Aktualisierung falsch-positiver Definitionen auf Ihrem Computer abgeschlossen ist, können Sie Smart App Control über die Windows-Registrierung erneut aktivieren:
  - Drücken Sie Windows-Taste + R, Typ `regedit`und drücken Sie die Eingabetaste, um den Registrierungseditor als Administrator zu öffnen.
  - Navigieren Sie zu: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (oder `Policies`).
  - Lokalisieren `VerifiedAndReputablePolicyState` im rechten Bereich.
  - Doppelklicken `VerifiedAndReputablePolicyState` und ändern Sie die Wertdaten in:

  - `1` = Ein (erzwungen)
  - `2` = Bewertungsmodus

  - Klicken Sie auf OK, schließen Sie den Registrierungseditor und starten Sie Ihren Computer neu.

[Sehen Sie sich den installer.exe-Bericht an Microsoft an](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Sehen Sie sich den InnioasisUpdater.exe-Bericht an Microsoft an](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Öffnen Sie die verlinkte Seite](https://innioasis.app/notices.html)

[← Alle Mitteilungen](index_de.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
