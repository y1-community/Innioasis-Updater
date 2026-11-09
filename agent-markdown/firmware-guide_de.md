---
title: "Anleitung zur Firmware-Installation und Bestandswiederherstellung | Innioasis Updater CE – Innioasis Firmware-Downloads"
description: "Installieren Sie benutzerdefinierte Firmware oder stellen Sie die offizielle Werksfirmware auf Innioasis Y1, Y2, G1, G3, G5, R1, PR1 und Timmkoo Q5, Q3 mit Innioasis Updater CE wieder her."
language: "de"
source: "https://innioasis.app/firmware-guide_de.html"
---

# Anleitung zur Firmware-Installation und Bestandswiederherstellung | Innioasis Updater CE – Innioasis Firmware-Downloads

Anleitung zur Firmware-Installation und Bestandswiederherstellung

# Installieren oder wiederherstellen Sie die Firmware auf Ihrem Gerät

Wählen Sie das auf Ihrem Player aufgedruckte Modell aus. Befolgen Sie dann die Schritte in Updater CE. Es erledigt den Rest.[Updater CE holen](guide_de.html#platform)[Durchsuchen Sie das Firmware-Archiv](firmware_de.html)[Fehlerbehebung](troubleshooting_de.html)

Wählen Sie das auf Ihrem Player aufgedruckte Modell und die gewünschte Software aus und öffnen Sie dann diese Anleitung. [Durchsuchen Sie Software und Firmware nach Modell](firmware_de.html).

## 

[Updater CE holen](guide_de.html#download-updater)[Vollständiges schriftliches Tutorial](guide_de.html)

## Holen Sie sich Innioasis Updater CE

Hier erfahren Sie, wo Sie anfangen können, wenn Sie Updater CE noch nicht haben.Holen Sie es sich auf Updater CEmit geführter Installation

### Windows

Laden Sie das Installationsprogramm herunter, öffnen Sie es und befolgen Sie die Installationsanweisungen.[Laden Sie den Treiber herunter und installieren Sie ihn](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Laden Sie die App und Treiber herunter](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Von Edge blockiert?](#)

Wenn Windows Sie daran hindert, die App auszuführen oder sie nicht startet, öffnen Sie bitte die Einstellungen, klicken Sie auf Datenschutz und Sicherheit → Windows-Sicherheit → App- und Browsersteuerung und schalten Sie die intelligente App-Steuerung aus. [Windows startet die App nicht? Helfen](#smart-app-control)

Damit es funktioniert, müssen Sie Ihren PC nach der Installation neu starten.

### macOS

Laden Sie die App herunter und verschieben Sie sie in „Anwendungen“. Wenn macOS es blockiert, öffnen Sie „Systemeinstellungen“, dann „Datenschutz und Sicherheit“ und klicken Sie auf „Trotzdem öffnen“. [Wie das funktioniert](https://support.apple.com/en-gb/102445#openanyway)[Herunterladen Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Laden Sie das AppImage für Intel- und AMD-Systeme herunter, machen Sie es ausführbar und führen Sie es aus.[Laden Sie AppImage für Intel/AMD herunter](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Hinweise zum Linux-Setup](drivers_de.html#linux)Eine andere Plattform?

Benötigen Sie längere Hinweise zur Computereinrichtung? Öffnen Sie die [Windows](drivers_de.html#windows) oder [Linux](drivers_de.html#linux) Setup-Anleitung.

## Zurück zur Originalsoftware

Um zurückzugehen, wählen Sie Ihr Modell aus, wählen Sie Original-Software, dann rennen Installieren / Wiederherstellen. Das ist alles. Der Updater ersetzt die Systemsoftware für Sie.[Y1-Wiederherstellungsanleitung](guides/restore-original-y1.html)[Y2-Wiederherstellungsanleitung](guides/restore-original-y2.html)

## Softwarehandbücher nach Modell

Wählen Sie Ihr Modell aus und öffnen Sie dann die Anleitung für Ihre Software.

### Innioasis Y1

Software für Y1:

### Innioasis Y2

Software für Y2:

Eine Anmerkung zu den beiden Tools

## Welches Werkzeug soll ich verwenden?

Innioasis Updater CE ist der sicherste Weg, Ihren Player zu aktualisieren. Es behält Ihre Musik, Videos und Bluetooth-Kopplungen bei. Es sagt Ihnen, wann Updates bereit sind. Es läuft unter Windows, macOS und Linux. Das Innioasis Universal Flash Tool löscht Ihren Player und funktioniert auf weniger Computern.[Öffnen Sie den vollständigen Vergleich](updater-comparison_de.html)

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
