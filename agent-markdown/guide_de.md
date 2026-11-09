---
title: "Erste Schritte mit Innioasis Updater CE | Firmware auf einem beliebigen Innioasis- oder Timmkoo-Player installieren oder wiederherstellen – Innioasis Updater"
description: "Laden Sie Innioasis Updater CE für Windows, macOS oder Linux herunter und installieren oder stellen Sie dann in wenigen geführten Schritten die Firmware auf einem beliebigen Innioasis- oder Timmkoo-Player wieder her."
language: "de"
source: "https://innioasis.app/guide_de.html"
---

# Erste Schritte mit Innioasis Updater CE | Firmware auf einem beliebigen Innioasis- oder Timmkoo-Player installieren oder wiederherstellen – Innioasis Updater

Schnellstart

# Erste Schritte mit Innioasis Updater CE

Funktioniert mit allen Innioasis- und Timmkoo-Audioplayern. Installieren Sie Innioasis Updater CE auf Ihrem Computer, wählen Sie Ihr Modell und die gewünschte Software aus und folgen Sie dann den Anweisungen.

## 

[Updater CE holen](guide_de.html#download-updater)[Vollständiges schriftliches Tutorial](guide_de.html)

## Holen Sie sich Innioasis Updater CE

Innioasis Updater CE ist die App, die offizielle Updates und Community-Software auf Ihrem Player installiert. Es behält Ihre Musik und Einstellungen und läuft unter Windows, macOS und Linux.

### Windows

Laden Sie das Installationsprogramm herunter, führen Sie es aus und starten Sie anschließend Ihren PC neu.[Holen Sie sich Treiber](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Herunterladen Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

Wenn Windows Sie daran hindert, die App auszuführen oder sie nicht startet, öffnen Sie bitte die Einstellungen, klicken Sie auf Datenschutz und Sicherheit → Windows-Sicherheit → App- und Browsersteuerung und schalten Sie die intelligente App-Steuerung aus. Smart App Control wirkt sich derzeit auf beliebte Anwendungen wie den Epic Overlay Service (von Fortnite verwendet) aus – Updater CE ist sicher und für die Verwendung verifiziert. [Windows startet die App nicht? Helfen](#smart-app-control)

Starten Sie Ihren PC nach der Installation neu. Fahrerhilfe ist in der [Hinweise zum Windows-Setup](drivers_de.html#windows).

### macOS[Herunterladen Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Wenn Ihr Mac Sie daran hindert, die App zum ersten Mal auszuführen, öffnen Sie bitte die Systemeinstellungen, klicken Sie auf Datenschutz und Sicherheit, scrollen Sie nach unten zu Sicherheit und klicken Sie auf [Trotzdem geöffnet](https://support.apple.com/en-gb/102445#openanyway). Sie können auch im Finder bei gedrückter Ctrl-Taste (oder mit der rechten Maustaste) auf die App klicken und „Öffnen“ wählen.

Funktioniert auf Intel- und Apple-Silicon-Macs mit macOS Monterey und höher.

### Linux

Laden Sie das AppImage für Intel- und AMD-Systeme herunter, machen Sie es ausführbar und führen Sie es aus.[Laden Sie AppImage für Intel/AMD herunter](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Hinweise zum Linux-Setup](drivers_de.html#linux)Eine andere Plattform?

Sie benötigen Ihren Player, ein USB Datenkabel, das Daten überträgt (ein reines Ladekabel kann nicht installiert werden) und ein paar Minuten. Lassen Sie das Kabel angeschlossen, bis Updater CE meldet, dass es fertig ist.

## Wählen Sie Ihr Modell und Ihre Software
  - Gerätemodell: Wählen Sie das auf dem Player aufgedruckte Modell aus. Y1 oder Y2. Software, die für ein Modell erstellt wurde, kann nicht auf dem anderen installiert werden.
  - Software und Release: Wählen Sie Originalsoftware, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player oder Koensayr, wenn sie für Ihr Modell aufgeführt ist, und wählen Sie dann eine Version aus. Stabil ist die sichere Wahl.
  - Installieren: klicken Installieren / Wiederherstellen, schalten Sie den Player vollständig aus und schließen Sie das USB-Kabel erst an, wenn Updater CE Sie dazu auffordert.
  - Beenden: Lassen Sie den Player und das Kabel bis zur Erfolgsmeldung in Ruhe, trennen Sie dann die Verbindung und starten Sie den Player.

Y1 Spieler, die vor 2.0.0 mit Originalsoftware ausgeliefert wurden, benötigen Gerät Type B. Alle anderen behalten den Standardwert Type A.Anleitung zum Updater-Anschluss zum Anschließen eines ausgeschalteten PlayersBefolgen Sie die Live-Eingabeaufforderung Updater CE für Ihr Modell.

## Zurück zur Originalsoftware

Kundenspezifische Software ist reversibel. Wählen Sie in Updater CE Ihr Modell aus, wählen Sie aus Original-Software, wählen Sie eine stabile Version aus und führen Sie sie dann aus Installieren / Wiederherstellen auf die gleiche Weise. Es gibt nichts, was manuell gelöscht werden muss.[Y1-Wiederherstellungsanleitung](guides/restore-original-y1.html)[Y2-Wiederherstellungsanleitung](guides/restore-original-y2.html)

Wenn ein Blitz vor der Eingabeaufforderung USB stoppt, überprüfen Sie zuerst das Kabel, die Plattformeinrichtung und das Modell. Sehen [Fehlerbehebung](troubleshooting_de.html) für Korrekturen die [Y1 und Y2 Wiederherstellungsanleitung](guides/recovery.html) für Leistungs- und Radfehler und [SP Flash Tool](sp-flash-tool_de.html) für eine fortgeschrittene Genesung.

## Softwarehandbücher nach Modell

Öffnen Sie die Anleitung für Ihr Modell und die von Ihnen gewählte Software.

### Innioasis Y1

Software für Y1:

### Innioasis Y2

Software für Y2:

## Welches Werkzeug soll ich verwenden?

Dieser Leitfaden verwendet Innioasis Updater 2.5.1, auch Updater CE genannt. Es schützt Ihre Songs, Videos und Bluetooth-Kopplungen. Es sagt Ihnen, wann Updates bereit sind. Der Innioasis Universal Flash Tool löscht Ihren Player und erfordert manuelle Schritte. [Vergleichen Sie die Werkzeuge →](updater-comparison_de.html)

## Windows startet die App nicht? Problemumgehung für die intelligente App-Steuerung

Windows Defender SmartScreen oder Smart App Control können neu heruntergeladene Community-Anwendungen blockieren, bevor sich Signaturreputationen verbreiten. Smart App Control wirkt sich derzeit auf beliebte Anwendungen wie den Epic Overlay Service (von Fortnite verwendet) aus – Updater CE ist sicher und in seiner Verwendung verifiziert. Wenn Sie Smart App Control deaktivieren, kann Updater CE normal geöffnet und ausgeführt werden.
  - Offen Einstellungen auf Ihrem Windows-PC (drücken Sie Win + I).
  - Klicken Sie Datenschutz und Sicherheit in der linken Seitenleiste und klicken Sie dann auf Windows Security.
  - Klicken Sie App- und Browsersteuerung.
  - Unter Intelligente App-Steuerung, klicken Smart App Control-Einstellungen.
  - Stellen Sie den Schalter auf Aus um den Start von Updater CE zu ermöglichen.

Über Edge heruntergeladen? Wenn Edge den Download selbst blockiert, klicken Sie auf die Schaltfläche Weitere Optionen (…) → Halten → Mehr anzeigen → Behalte es trotzdem.

Smart App Control später wieder aktivieren: Wenn Sie Smart App Control wieder aktivieren möchten, können Sie es über die Windows-Registrierung unten erneut aktivieren `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` durch Einstellung `VerifiedAndReputablePolicyState` an `1` (Ein) oder `2` (Bewertungsmodus) und Neustart.

### Windows startet die App nicht? So deaktivieren Sie Smart App Control

Windows Defender SmartScreen oder Smart App Control können neu heruntergeladene Community-Anwendungen blockieren, bevor sich Signaturreputationen verbreiten. Smart App Control wirkt sich derzeit auf beliebte Anwendungen wie den Epic Overlay Service (von Fortnite verwendet) aus – Updater CE ist sicher und in seiner Verwendung verifiziert. Wenn Sie Smart App Control deaktivieren, kann Updater CE normal geöffnet und ausgeführt werden.
  - Offen Einstellungen auf Ihrem Windows-PC (drücken Sie Win + I).
  - Klicken Sie Datenschutz und Sicherheit in der linken Seitenleiste und klicken Sie dann auf Windows Security.
  - Klicken Sie App- und Browsersteuerung.
  - Unter Intelligente App-Steuerung, klicken Smart App Control-Einstellungen.
  - Stellen Sie den Schalter auf Aus um den Start von Updater CE zu ermöglichen.

Von Edge blockiert? Wenn Microsoft Edge den Download selbst blockiert, klicken Sie auf die Schaltfläche Weitere Optionen (…) → Halten → Mehr anzeigen → Behalte es trotzdem.

Smart App Control später wieder aktivieren: Wenn Sie Smart App Control wieder aktivieren möchten, können Sie es über die Windows-Registrierung unten erneut aktivieren `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` durch Einstellung `VerifiedAndReputablePolicyState` an `1` (Ein) oder `2` (Bewertungsmodus) und Neustart.Enge Hilfe

## War das nützlich?

Ihre Antwort trägt zur Verbesserung dieses Leitfadens bei.Ja, ich fand es nützlichNoch nicht[Lassen Sie uns wissen, wie wir uns verbessern können](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
