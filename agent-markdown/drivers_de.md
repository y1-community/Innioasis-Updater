---
title: "Innioasis Y1 und Y2 USB Treiber | Windows-Treiber- und Linux-Berechtigungen – Innioasis Updater"
description: "Richten Sie Ihren Computer für Innioasis Updater ein: Windows MediaTek-Treiber und Linux USB-Berechtigungen – plus Kabel- und Timing-Korrekturen."
language: "de"
source: "https://innioasis.app/drivers_de.html"
---

# Innioasis Y1 und Y2 USB Treiber | Windows-Treiber- und Linux-Berechtigungen – Innioasis Updater

Computer-Setup

# Machen Sie den Computer vor dem Player bereit.

Die meisten Verbindungsprobleme sind auf Treiber, Berechtigungen, Kabel oder Timing zurückzuführen. Für Windows muss der Treiber MediaTek installiert sein. Linux benötigt die richtigen USB-Berechtigungen. Finden Sie unten Ihre Plattform.[Updater CE holen](guide_de.html#platform)[Fehlerbehebung](troubleshooting_de.html)

## Windows
  - Laden Sie unten das MediaTek-Treiberinstallationsprogramm herunter.
  - Führen Sie das Installationsprogramm aus und erlauben Sie Windows, den Treiber zu installieren.
  - Starten Sie den Computer neu.
  - Öffnen Sie Updater CE und warten Sie auf die Verbindungsaufforderung, bevor Sie den ausgeschalteten Player anschließen.

Einige Windows-Systeme blockieren den Treiber durch Core-Isolation (Speicherintegrität). Wenn Updater CE den Player nach einem Neustart immer noch nicht sehen kann, schalten Sie die Speicherintegrität in der Windows-Sicherheit aus, starten Sie neu und installieren Sie den Treiber neu. Schalten Sie die Einstellung wieder ein, wenn Sie fertig sind, sofern Ihr System dies zulässt.

Windows startet die App nicht? Wenn Windows Security oder Smart App Control das Öffnen von Updater CE verhindert, öffnen Sie es Einstellungen (drücken Win + I) → Datenschutz und Sicherheit → Windows Security → App- und Browsersteuerung → Smart App Control-Einstellungen und stellen Sie es ein Aus. Smart App Control wirkt sich derzeit auf beliebte Anwendungen wie den Epic Overlay Service (von Fortnite verwendet) aus – Updater CE ist sicher und für die Verwendung verifiziert. Um sie später wieder zu aktivieren, setzen Sie `VerifiedAndReputablePolicyState` an `1` (Ein) oder `2` (Bewertungsmodus) unter `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` im Registrierungseditor.[Laden Sie den Windows-Treiber herunter](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Zurück zum Hauptführer](guide_de.html#windows) · [Software-Downloads](firmware_de.html)

## Linux USB-Berechtigungen

Linux benötigt Ihr Benutzerkonto, um mit dem MediaTek USB-Chip im Player kommunizieren zu können. Updater CE regelt dies normalerweise während der Installation, und die gleiche Berechtigung gilt auch für SP Flash Tool, also behandeln Sie dies als einen Fix-it-Schritt und nicht als einen normalen Schritt.
  - Führen Sie Updater CE als Ihr normaler Benutzer aus, nicht als Root. Das Installationsprogramm fragt nur dann nach Administratorzugriff, wenn es diesen benötigt.
  - Überprüfen Sie, ob der Player überhaupt sichtbar ist. Schalten Sie den Player aus, schließen Sie das Kabel an und führen Sie den Befehl lsusb in einem Terminal aus. Ein verbundener Player wird als MediaTek-Gerät mit der Hersteller-ID 0e8d angezeigt.
`lsusb`
  - Wenn es in lsusb erscheint, aber Innioasis Updater CE oder SP Flash Tool sagt, dass die Berechtigung verweigert wurde oder der Port nicht geöffnet werden kann, hat Ihr Benutzer keinen Zugriff auf das Gerät USB. Die gleiche udev-Regel gilt für beide Tools. Fügen Sie also eines hinzu, das es der Benutzergruppe ermöglicht, es zu lesen.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Speichern Sie diese Zeile in einer neuen Datei mit dem Namen /etc/udev/rules.d/51-innioasis.rules und führen Sie dann Folgendes aus:`sudo udevadm control --reload && sudo udevadm trigger`
  - Trennen Sie den Player vollständig vom Stromnetz, schließen Sie ihn wieder an und versuchen Sie die Installation erneut.
  - Wenn SP Flash Tool eine serielle Berechtigung oder ein Port-Race meldet, ziehen Sie den Stecker vollständig heraus und schließen Sie ihn erst dann wieder an, wenn Sie dazu aufgefordert werden.
Improvisieren Sie keine Blitzversätze.Wenn Sie zu einem manuellen Wiederherstellungstool wechseln, verwenden Sie die mit dem Projekt gelieferten Dateien und modellspezifischen Konfigurationen.

[Zurück zum Hauptführer](guide_de.html#linux) · [Software-Downloads](firmware_de.html) · [SP Flash Tool Anleitung](sp-flash-tool_de.html)

## Kabel und Timing
  - Verwenden Sie ein bekanntes USB-Datenkabel.
  - Vermeiden Sie Hubs bei der Fehlerbehebung.
  - Schalten Sie das richtige Modell vollständig aus.
  - Verbinden Sie sich nur, wenn Sie dazu aufgefordert werden.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
