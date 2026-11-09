---
title: "SP Flash Tool für Innioasis und Timmkoo Spieler"
description: "Suchen Sie unter Windows und Linux nach SP Flash Tool gebündelt mit Innioasis Updater, extrahieren Sie rom.zip oder rom_y2.zip und flashen Sie ein Innioasis Y1 oder Y2 mit der passenden Scatter-Datei."
language: "de"
source: "https://innioasis.app/sp-flash-tool_de.html"
---

# SP Flash Tool für Innioasis und Timmkoo Spieler

Manuelles Blinken

# Flash-Tool für Innioasis- und Timmkoo-Spieler

SP Flash Tool kommt innerhalb von Innioasis Updater an [Windows](drivers_de.html#windows) und [Linux](drivers_de.html#linux). Du hast es bereits. Diese Anleitung zeigt die sichere Verwendung auf einem Innioasis Y1 oder Y2 und die Updater-Route für Timmkoo-Spieler.[Kehren Sie zum Updater-Handbuch zurück](guide_de.html)[Firmware-Downloads](firmware_de.html)[Fehlerbehebung](troubleshooting_de.html)

Beginnen Sie mit Innioasis Updater

## Der Updater erledigt die gesamte Arbeit in einem Durchgang

Der Updater führt die meisten Installationen in einem Durchgang durch. Wählen Sie die Software aus, befolgen Sie die Schritte, und schon sind Sie fertig. Außerdem erfahren Sie, wann ein Fix oder eine neue Version verfügbar ist. SP Flash Tool befindet sich im Updater-Toolkit für die seltenen Fälle, in denen Updater nicht fertig werden kann. Die folgenden Schritte sind eine Ausnahme.

## Wofür dieses Tool gedacht ist

Der Updater flasht den Player für Sie. SP Flash Tool ist der gleiche Motor, ohne Leitplanken. Verwenden Sie es, wenn der Updater nicht startet, der Player keine Verbindung herstellt oder wenn Sie sich mit einer Scatter-Datei auskennen.Probieren Sie zuerst Updater aus. Für die meisten Installationen und Wiederherstellungen gilt die Anleitung [Updater-Route](guide_de.html) ist die sicherere Wahl. Verwenden Sie SP Flash Tool, wenn Sie wissen, warum Sie es brauchen, und halten Sie einen geladenen Akku und ein USB Datenkabel bereit.

## Flash-Tool für Innioasis Spieler

Innioasis Updater ist das Flash-Tool für Innioasis Spieler. Es installiert offizielle Software, Updates und Wiederherstellungspakete über den modellangepassten Ablauf und behält Ihre Musik und Einstellungen bei.

### Innioasis Y1 Flash-Tool

Wählen Sie im Updater die Version Y1 und schließen Sie dann den ausgeschalteten Player an, wenn die App Sie dazu auffordert. Die gleichen Y1-Pakete funktionieren mit SP Flash Tool, wenn Sie die manuelle Route benötigen.

### Innioasis Y2 Flash-Tool

Wählen Sie eine für Y2 aufgeführte Version aus. Y2-Pakete sind nicht mit Y1-Paketen austauschbar. Überprüfen Sie daher das Modell, bevor Sie beginnen.

## Flash-Tool für Timmkoo Spieler

Timmkoo Spieler verwenden denselben Updater-Installationsablauf. Es liest die ZIP- und RAR-Pakete von Timmkoo direkt, sodass Sie kein separates Flash-Tool oder Scatter-Datei benötigen.

### Timmkoo Q5 Flash-Tool

Wählen Sie im Updater das Modell Q5 aus, wählen Sie das Paket Timmkoo aus, führen Sie dann „Installieren/Wiederherstellen“ aus und schließen Sie den Player an der Eingabeaufforderung an.

### Timmkoo Q3 und Q3E Flash-Tool

Der Eintrag Q3 deckt sowohl Q3 als auch Q3E ab. Updater wählt die passenden Dateien aus dem Paket aus, das das Projekt veröffentlicht.

### Timmkoo A5 Flash-Tool

Wählen Sie das Modell A5 aus, bevor Sie ein Paket auswählen, und folgen Sie dann derselben Installationsaufforderung.

## Wo Updater es ausdrückt

SP Flash Tool wird mit dem Updater-Installationsordner geliefert, nicht als separater Download. Öffnen Sie es von dort aus, wenn Sie es benötigen.

### Windows

Öffnen Sie den Updater-Installationsordner und führen Sie ihn aus `flash_tool.exe`. Der Ordner befindet sich normalerweise unter `%LOCALAPPDATA%\Innioasis Updater`. In einigen Setups ist ein Toolkit-Ordner mit der Verknüpfung SP Flash Tool enthalten.

### Linux

Führen Sie das Paket aus `flash_tool` binär im Updater-App-Ordner auf x86 / x86_64. Das Projektinstallationsprogramm bereitet USB-Berechtigungen mit udev-Regeln vor, sodass der Player angezeigt werden sollte, wenn eine Verbindung besteht.

### macOS

SP Flash Tool ist unter macOS nicht gebündelt. Updater verwendet dort stattdessen die Route MTKClient. Benutzen Sie die [Geführte Installation](guide_de.html) auf einem Mac und behalten Sie SP Flash Tool für einen Windows- oder Linux-Rechner.

Das Tool wird mit dem Download-Agenten MediaTek und einer modellspezifischen Konfiguration geliefert, sodass Sie keine DA-Dateien sammeln oder Dateien von anderswo verteilen müssen.

## Bereiten Sie die Firmware vor
  - Schnappen Sie sich die gewünschte Veröffentlichung [Firmware-Downloads](firmware_de.html). Wählen `rom.zip` für ein Y1 oder `rom_y2.zip` für ein Y2.
  - Extrahieren Sie die ZIP-Datei in einen eigenen Ordner. Windows kann „Alle extrahieren“ verwenden. Verwenden Sie unter Linux Ihren Archivmanager oder `unzip` in einem Terminal.
  - Überprüfen Sie, ob sich die Scatter-Datei im extrahierten Ordner befindet. Es wird normalerweise benannt `MT6572_Android_scatter.txt` für Y1 Pakete und `MT6582_Android_scatter_def.txt` für Y2 Pakete, obwohl eine Veröffentlichung es nach seinem Projekt benennen kann.
Halten Sie die Modelle getrennt. Die Streuung Y1 beschreibt ein MT6572-Gerät und die Streuung Y2 beschreibt ein MT6582-Gerät. Mit dem Falschen zu blinken führt dazu, dass Spieler geblockt werden. Wenn die Streuung in der ZIP-Datei nicht mit Ihrem Modell übereinstimmt, stoppen Sie und verwenden Sie stattdessen ein für Ihr Modell aufgeführtes Paket.

## Laden Sie den Scatter und den Flash
  - Öffnen Sie SP Flash Tool im Updater-Installationsordner.
  - Klicken Sie auf der Registerkarte „Download“ auf Wählen Sie neben Scatter-loading File und wählen Sie die Scatter-Datei aus dem extrahierten Ordner aus. Die Partitionsliste wird ausgefüllt.
  - Lassen Sie den Blitzmodus eingeschaltet Nur herunterladen es sei denn, Sie führen absichtlich eine vollständige Wiederherstellung durch, was erforderlich ist Firmware-Upgrade.
  - Klicken Sie Herunterladen. Das Tool wartet auf den Spieler.
  - Schalten Sie den Player vollständig aus und schließen Sie dann das Datenkabel USB an. Legen Sie den Player ab und bewegen Sie ihn nicht.
  - Warten Sie auf das grüne Häkchen. Ziehen Sie erst dann das Kabel ab und starten Sie den Player.

Behalten Sie die gleichen USB Kabel- und Zeitregeln wie bei der geführten Route bei: ein Datenkabel, kein Hub, und schließen Sie es nur an, wenn das Werkzeug bereit ist.

## Wenn es nicht blinkt
  - Überprüfen Sie, ob Scatter und ZIP mit dem auf dem Player aufgedruckten Modell übereinstimmen.
  - Stellen Sie sicher, dass der Player vollständig ausgeschaltet ist, bevor Sie ihn anschließen.
  - Bestätigen Sie unter Windows, dass der Treiber MediaTek mit dem Updater-Setup installiert wurde. Bestätigen Sie unter Linux die udev-Regeln im Projektinstallationsprogramm.
  - Schließen Sie das Kabel erst wieder an, wenn das Werkzeug wartet. Bei einem Hafenrennen kann es nötig sein, den Stecker komplett auszustecken und neu zu erfrischen Herunterladen klicken.

Für alles, was darüber hinausgeht, offen [Fehlerbehebung](troubleshooting_de.html). Und denken Sie daran: Updater ist immer noch der normale Weg, und [Y1](guides/restore-original-y1.html) und [Y2](guides/restore-original-y2.html) Wiederherstellungsanleitungen verwenden es auch.

## War das nützlich?

Ihre Antwort trägt zur Verbesserung dieses Leitfadens bei.Ja, ich fand es nützlichNoch nicht[Lassen Sie uns wissen, wie wir uns verbessern können](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
