---
title: "Fix Innioasis Updater &amp; Y1 Helper mit einer Neuinstallation – Innioasis Updater"
description: "Schritt-für-Schritt-Neuinstallation für Innioasis Updater und den Y1-Helper: Entfernen Sie übrig gebliebene Dateien, installieren Sie sie neu und kehren Sie zum Flashen der Firmware zurück."
language: "de"
source: "https://innioasis.app/Troubleshooting/clean_install_de.html"
---

# Fix Innioasis Updater &amp; Y1 Helper mit einer Neuinstallation – Innioasis Updater

## Bestätigen Sie, dass Sie die Neuinstallation benötigen

Eine manuelle Neuinstallation wird empfohlen, wenn eines der folgenden Symptome auftritt:
  - Es dauert einige Minuten, bis der Updater gestartet wird, oder er bleibt beim Suchen nach Updates stehen.
  - Es werden keine Updates mehr angezeigt, obwohl es neuere Versionen gibt.
  - Geräte-Firmware-Updates können nicht heruntergeladen oder angewendet werden, obwohl sie verfügbar sind.
  - Sie haben mehrere Veröffentlichungen übersprungen und den Updater schon lange nicht mehr verwendet.

## Windows: Führen Sie eine saubere Neuinstallation durch

Verwenden Sie das offizielle Windows-Installationsprogramm, um Updater unter Windows 10 oder Windows 11 (64-Bit) zu aktualisieren. Dadurch werden ältere Builds vollständig ersetzt und der Selbstaktualisierungskanal wiederhergestellt.

Bevor Sie das Installationsprogramm ausführen, öffnen Sie es Einstellungen › Apps › Installierte Apps (oder das Erbe Programme hinzufügen/entfernen Panel) und deinstallieren Sie alle vorhandenen Kopien von Innioasis Updater. Ein sauberer Start verhindert Dateikonflikte.[ Laden Sie Clean Installer für Windows herunter ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)Schritt 1

### Laden Sie das neueste Installationsprogramm herunter

Speichern Sie das Installationsprogramm in Ihrem Download-Ordner. Schließen Sie Innioasis Updater, wenn es gerade ausgeführt wird.Schritt 2

### Entfernen Sie alle vorhandenen Installationen

Offen Einstellungen › Apps › Installierte Apps (oder das Erbe Systemsteuerung › Programme hinzufügen/entfernen) und deinstallieren Sie Innioasis Updater, damit die Neuinstallation von vorne beginnt.Schritt 3

### Installieren und neu starten

Führen Sie das heruntergeladene Installationsprogramm aus – Windows wird Sie um Erlaubnis bitten. Wenn das Setup abgeschlossen ist, starten Sie Innioasis Updater; Es sollte nun 1.8.2.8 automatisch erkennen und Updates erneut abrufen.

 Dies behebt auch langsame Startvorgänge und sorgt dafür, dass der Updater Firmware-Versionen wieder direkt von den Entwicklern abruft. 

## macOS: Aktualisieren Sie mit dem DMG-Installer

Das macOS-Installationsprogramm löscht die alten Dateien und installiert 1.8.2.8.[ Laden Sie Innioasis Updater DMG herunter ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - Öffnen Sie die heruntergeladene DMG und erweitern Sie das Finder-Fenster, damit Sie die Datei sehen können Neu installieren Option.
  - Führen Sie den Befehl „Neu installieren“ aus, um die vorhandene Kopie von Updater zu aktualisieren. Dadurch werden ältere Hilfsdateien entfernt, die möglicherweise neue Funktionen blockieren.
  - Starten Sie Innioasis Updater erneut über Anwendungen. Bestätigen Sie die Version der Info-Panel-Listen 1.8.2.8.
 Wenn nach der Neuinstallation die Meldung „Innioasis Updater kann nicht geöffnet werden“ angezeigt wird, gehen Sie zu Systemeinstellungen › Datenschutz und Sicherheit und wählen Trotzdem geöffnet um die App zu genehmigen. 

## Nach dem Update auf 1.8.2.8

Sobald Sie die neueste Version installiert haben, erhalten Sie Zugriff auf die folgenden Funktionen. Diese sind nur in aktuellen Builds verfügbar.
  - One-Click-Installationen für Original-Firmware, Community-Releases und Rockbox Builds, die direkt von den Entwickler-Releases heruntergeladen wurden.
  - Klare geführte Schritte die Ihnen sagen, wann Sie den Player anschließen müssen und wann es sicher ist, den Stecker zu ziehen.
  - Allgemeine Stabilitätsverbesserungen und deutlich schnellere Startzeiten auf beiden Plattformen.

 Benötigen Sie Hilfe bei der Überprüfung Ihrer Version? Öffnen Sie Innioasis Updater und wählen Sie Hilfe › Über, und bestätigen Sie die Build-Shows 1.8.2.8. 

## Brauchen Sie noch Hilfe?

Wenn die Neuinstallation fehlschlägt, erfassen Sie alle Fehlermeldungen und wenden Sie sich an die Innioasis Community-Supportkanäle. Geben Sie Ihre Betriebssystemversion, den Updater-Build (falls verfügbar) und die Schritte an, die Sie bereits ausprobiert haben.

Wenn Sie Ihre Installation auf dem neuesten Stand halten, stellen Sie sicher, dass Sie bei der Einführung immer die neuesten Firmware-Pakete und Tools erhalten.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
