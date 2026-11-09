---
title: "So installieren Sie Rockbox auf Ihrem Innioasis Y1 oder Y2 - Innioasis Updater"
description: "Installieren Sie Rockbox auf einem Innioasis Y1 oder Y2 mit Updater: Themen, stabile Versionen, Hinweise zu Type A und Type B und wie Sie die Originalsoftware danach wiederherstellen."
language: "de"
source: "https://innioasis.app/rockbox_de.html"
---

# So installieren Sie Rockbox auf Ihrem Innioasis Y1 oder Y2 - Innioasis Updater

Rockbox Referenz

# Erhalten Sie Rockbox auf Ihrem Y1 oder Y2

Rockbox ändert die Player-Software und öffnet eine umfassendere Musik-Player-Benutzeroberfläche, Wiedergabesteuerung, Sortierung und Themenoptionen. Die Installation ist geführt, aber Y1 und Y2 sind separate Reisen.[Rockbox am Y1](guides/rockbox-y1.html)[Rockbox am Y2](guides/rockbox-y2.html)[Warum Rockbox?](rockbox-benefits_de.html)

## Was sich durch die Installation ändert

Rockbox ist kundenspezifische Software. Ihre Möglichkeit, zur Standardschnittstelle zurückzukehren, wenn das entsprechende Originalsoftwarepaket verfügbar ist, wird dadurch nicht beeinträchtigt. Es kann das Durchsuchen und Anpassen von Musik verbessern, aber Funktionen, Auflösung, Akkulaufzeit und Themenkompatibilität hängen vom Build ab.Mischen Sie keine Modelle. Wählen Sie Y1 für einen Y1-Spieler und Y2 für einen Y2-Spieler. Ein ähnlich aussehender Release-Name ist kein ausreichender Beweis dafür, dass ein Paket kompatibel ist.

## Sehen Sie sich das Video an

Video von Frawgeeys. Es zeigt die Route Innioasis Updater; Verwenden Sie die folgenden modellspezifischen schriftlichen Schritte für Ihr Y1 oder Y2.

Video von [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (Spanisch), zeigt Rockbox auf einem Y1. Führen Sie die folgenden modellspezifischen Schritte für Ihren Player aus.

## Die freigegebene Updater-Route
  - Installieren Sie Updater und verbinden Sie nichts, bis Sie dazu aufgefordert werden.
  - Wählen Sie das auf dem Player aufgedruckte Modell aus Gerätemodell.
  - Wählen Sie Rockbox In Software.
  - Wählen Sie eine stabile Version, es sei denn, Sie testen absichtlich einen nächtlichen Build.
  - Klicken Sie Installieren / Wiederherstellen, und folgen Sie dann der Aufforderung zum Ausschalten und USB-Verbindung.
  - Trennen Sie die Verbindung erst nach der Erfolgsmeldung.

## 240p, 360p und Themen

Ältere Rockbox Themensammlungen können für 240p erstellt werden. Y1 Community-Builds verwenden auch 360p-Kompatibilitätsbezeichnungen. Lesen Sie die Versionshinweise und die Theme-Quelle, bevor Sie einen Build auswählen. Ein für eine Auflösung oder Softwarefamilie erstelltes Theme funktioniert möglicherweise nicht für eine andere.[Durchsuchen Sie Community-Themen](https://themes.innioasis.app/?lang=de)[Theme-Tools](https://themes.innioasis.app/?lang=de)

## Rückkehr zur Originalsoftware

Wählen Sie das gleiche Modell erneut aus, wählen Sie aus Original-Software, wählen Sie eine stabile Version und verwenden Sie sie Installieren / Wiederherstellen. Wenn der Fehler vor der Eingabeaufforderung USB aufgetreten ist, überprüfen Sie den Computer und die extrahierten Dateien. Wenn der Player erkannt wurde, der Flash jedoch fehlgeschlagen ist, beginnen Sie mit [Fehlerbehebung](troubleshooting_de.html).[Y1 wiederherstellen](guides/restore-original-y1.html)[Y2 wiederherstellen](guides/restore-original-y2.html)

## FAQIch habe Rockbox neu installiert und es hat nichts behoben.

Durch die Neuinstallation von Rockbox wird derselbe Build über dieselben Dateien geschrieben, sodass die Dinge, die Rockbox auf dem MicroSD behält, nicht zurückgesetzt werden können. Wenn das Problem eine fehlerhafte Einstellung, ein Thema, eine Wiedergabeliste oder eine Datenbank auf der Karte ist, lässt sich das Problem durch eine Neuinstallation nicht beheben. Der zuverlässige Reset löscht die `.rockbox` Ordner aus MicroSD – Rockbox erstellt beim nächsten Start einen neuen Ordner.
  - Schalten Sie den Player vollständig aus und entfernen Sie die MicroSD-Karte oder schließen Sie den Player als USB-Laufwerk an.
  - Zeigen Sie versteckte Dateien auf Ihrem Computer an, damit der Ordner sichtbar ist. So zeigen Sie versteckte Dateien anPunktedateien auf Ihrem Computer anzeigenWindows: Öffnen Sie im Datei-Explorer die Sicht Tab und Häkchen Versteckte Gegenstände.macOS: im Finder drücken Cmd+Shift+. um versteckte Dateien umzuschalten.Linux · GNOME-Dateien: drücken Ctrl+H, oder öffnen Sie das Menü und wählen Sie Versteckte Dateien anzeigen.Linux · KDE Dolphin: drücken Ctrl+H, oder verwenden Ansicht → Versteckte Dateien anzeigen.
  - Löschen Sie die `.rockbox` Ordner aus dem Stammverzeichnis der Karte.
  - Legen Sie die Karte erneut ein und starten Sie den Player. Rockbox erstellt den Ordner mit den Standardeinstellungen neu.
  - Wenden Sie Ihr Design und Ihre Einstellungen erneut an. Tritt das Problem erst nach einem bestimmten Thema wieder auf, ist dieses Thema die Ursache.

Löschen `.rockbox` deinstalliert Rockbox nicht und berührt Ihre Musik nicht – der Ordner enthält Einstellungen, Themen und Caches und wird automatisch neu erstellt. Wenn Sie Ihre Themes behalten möchten, kopieren Sie den Ordner aus `.rockbox` bevor Sie ihn löschen, oder benennen Sie den Ordner in um `.rockbox-old` zuerst.Warum kann ich den .rockbox-Ordner auf meinem MicroSD nicht sehen?

Ordner, deren Name mit einem Punkt beginnt, werden auf den meisten Computern standardmäßig ausgeblendet. Sie müssen es nicht sehen, um Rockbox zu installieren – Updater verwaltet die Dateien. Wenn Sie eine Fehlerbehebung durchführen und diese löschen möchten, aktivieren Sie zunächst die versteckten Dateien. So zeigen Sie versteckte Dateien anPunktedateien auf Ihrem Computer anzeigenWindows: Öffnen Sie im Datei-Explorer die Sicht Tab und Häkchen Versteckte Gegenstände.macOS: im Finder drücken Cmd+Shift+. um versteckte Dateien umzuschalten.Linux · GNOME-Dateien: drücken Ctrl+H, oder öffnen Sie das Menü und wählen Sie Versteckte Dateien anzeigen.Linux · KDE Dolphin: drücken Ctrl+H, oder verwenden Ansicht → Versteckte Dateien anzeigen.Werden durch das Löschen von .rockbox mein Theme und meine Einstellungen zurückgesetzt?

Ja - `.rockbox` enthält die Einstellungen, das Thema, die Wiedergabelisten und die zwischengespeicherte Datenbank von Rockbox. Durch das Löschen wird Rockbox in einen sauberen Standardzustand zurückversetzt. Sichern Sie den gesamten Ordner (oder benennen Sie ihn um in `.rockbox-old`) Wenn Sie etwas davon zurückhaben möchten, starten Sie den Player und Rockbox erstellt einen neuen Ordner.

## Weitere Rockbox-Y1- und Rockbox-Y2-Anleitungen

Entdecken Sie Schritt-für-Schritt-Anleitungen zum Installieren, Herunterladen, Designen, Wiederherstellen und zur Fehlerbehebung Rockbox für beide Modelle:[Rockbox-Y1-Hub](rockbox-y1/)[Rockbox-Y2-Hub](rockbox-y2/)[Rockbox ROM-Downloads](rockbox-rom-download_de.html)[Rockbox für Y1](rockbox-for-y1_de.html)[Rockbox für Y2](rockbox-for-y2_de.html)[Rockbox-Y1 vs. Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1-Themen](rockbox-y1-themes.html)[Rockbox-Y2-Themen](rockbox-y2-themes.html)

## War dieser Hinweis nützlich?

Ihre Antwort trägt zur Verbesserung dieses Leitfadens bei.JaNoch nicht[Lassen Sie uns wissen, wie wir uns verbessern können](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
