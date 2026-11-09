---
title: "Originalsoftware auf Innioasis PR1 wiederherstellen – Schritt für Schritt"
description: "So stellen Sie die offizielle Originalsoftware auf einem Innioasis PR1 mit Innioasis Updater CE oder SP Flash Tool unter Verwendung des verifizierten rom_pr1.zip-Pakets wieder her."
language: "de"
source: "https://innioasis.app/guides/restore-original-pr1_de.html"
---

# Originalsoftware auf Innioasis PR1 wiederherstellen – Schritt für Schritt

Wiederherstellungsanleitung · Innioasis PR1

# Originalsoftware wiederherstellen auf Innioasis PR1

Eine saubere Rückkehr zur Software, mit der der Player geliefert wurde. Verwenden Sie es nach einem fehlgeschlagenen Update, vor dem Verkauf des Players oder immer dann, wenn ein benutzerdefiniertes System nicht für Sie geeignet ist.[Updater CE holen](../guide_de.html#platform)[PR1 Downloads](../firmware_de.html?model=PR1)[PR1 Handbuch](../manuals/pr1.html)

Installationsanleitung für Ihren Computer

## Stellen Sie die Originalsoftware auf Ihrem PR1 mit Ihrem Computer wieder her

Wählen Sie die Anleitung für den Computer aus, den Sie verwenden. Jede Version verfügt über das Plattform-Setup, Updater CE Schritte und den Weg zurück zum Lagerbestand.[Windows-Anleitung](/install/original-pr1-windows.html)[macOS-Anleitung](/install/original-pr1-mac.html)[Linux-Anleitung](/install/original-pr1-linux.html)

[Alle Innioasis PR1 Anleitungen](/install/pr1.html) · [Alle Original-Softwarehandbücher](/install/original-software.html)

## Was Sie brauchen
  - Ein Windows-, macOS- oder Linux-Computer. Updater CE läuft auf allen dreien.
  - Das mit dem Player gelieferte USB-Datenkabel. Nur-Ladekabel funktionieren nicht.
  - Der Beamte `rom_pr1.zip` Paket, das Updater für Sie herunterlädt, oder eine Kopie von [PR1 Archiv](../firmware_de.html?model=PR1) wenn Sie lieber von Hand flashen möchten.
  - Laden Sie den Player auf. Eine Wiederherstellung, bei der die Stromversorgung verloren geht, ist die einzige Möglichkeit, eine schlechte Situation noch schlimmer zu machen.

Dadurch wird das System ersetzt und der interne Speicher gelöscht. Kopieren Sie Musik, Aufnahmen und Fotos zunächst auf einen Computer.

## Route A: Updater CE (empfohlen)
  - Installieren [Innioasis Updater CE](../guide_de.html#platform) und öffne es.
  - Satz Gerätemodell an PR1. Das Modell muss genau zum Spieler passen.
  - Wählen Sie Original-Software in der Softwareliste.
  - Wählen Sie eine Veröffentlichung. Der neueste stabile Build ist der sichere Standard.
  - Drücken Sie Installieren / Wiederherstellen und warten Sie, während das Paket heruntergeladen und extrahiert wird.
  - Schalten Sie den Player vollständig aus und schließen Sie das USB-Kabel erst an, wenn der Updater Sie dazu auffordert.
  - Berühren Sie weder den Player noch das Kabel, bis die Erfolgsmeldung erscheint. Trennen Sie den Player und starten Sie ihn.
Wählen Sie niemals ein anderes Modell, um „es zum Laufen zu bringen“. Ein PR1 benötigt ein PR1-Paket. Durch das Mischen von Modellen benötigen Spieler letztendlich eine manuelle Wiederherstellung.

## Route B: SP Flash Tool (manuell)

Verwenden Sie dies, wenn ein Computer Updater CE nicht ausführen kann oder wenn Sie das Paket bereits haben und das klassische Tool bevorzugen.
  - Herunterladen `rom_pr1.zip` aus dem [PR1 Archiv](../firmware_de.html?model=PR1) und entpacken Sie es.
  - Bewahren Sie die Scatter-Datei neben den Bildern auf. Benennen Sie die Bilder nicht um oder verschieben Sie sie nicht.
  - Öffnen Sie SP Flash Tool und wählen Sie Nur herunterladen, und laden Sie die Scatter-Datei.
  - Schalten Sie den Player aus und drücken Sie Herunterladen, und schließen Sie dann das Kabel an.
  - Warten Sie auf die grüne Erfolgsmarkierung, bevor Sie die Verbindung trennen.

Die [SP Flash Tool Anleitung](../sp-flash-tool_de.html) behandelt Treiber und die Windows-Eingabeaufforderungen ausführlicher. Unter Linux und macOS ist Updater CE der einfachere Weg, da es über ein eigenes USB-Handling verfügt.

## Nach der Wiederherstellung
  - Trennen Sie den Player vom Computer und lassen Sie ihn selbstständig starten.
  - Wählen Sie Ihre Sprache und stellen Sie die Uhr ein.
  - Stellen Sie erneut eine Verbindung zu WLAN oder Bluetooth her, wenn Sie diese verwenden.
  - Kopieren Sie Ihre Musik zurück. Die [Transferführer](../manuals/transfer-music.html) hat die Ordnernamen.

Wenn der Player startet, aber der Bildschirm, das Rad oder die Tasten immer noch nicht funktionieren, hat die Wiederherstellung funktioniert; Das ist eine Hardware- oder Setup-Frage, keine Software-Frage. Die [Anleitung zur Fehlerbehebung](../troubleshooting_de.html) ist die nächste Station.

## Wenn es nicht funktioniert

### Der Updater sieht den Player nie

Wechseln Sie das Kabel und dann den USB-Anschluss. Vermeiden Sie Hubs. Installieren Sie unter Windows den Treiber MediaTek von [Treiberseite](../drivers_de.html).

### Der Blitz stoppt vorzeitig

Stellen Sie die Verbindung wieder her, laden Sie den Player auf und beginnen Sie erneut. Wechseln Sie nicht zu einem anderen Modellpaket.

### Der Spieler bleibt schwarz

Laden Sie das Gerät eine Stunde lang auf und halten Sie es dann zehn Sekunden lang aufrecht. Wenn es immer noch tot ist, lesen Sie das [Wiederherstellungsleitfaden](../guides/recovery_de.html) bevor Sie es erneut versuchen.

## Fragen, die Menschen stellen

### Wird dadurch meine Musik gelöscht?

Ja, der interne Speicher wird gelöscht. Dateien auf einer microSD-Karte bleiben normalerweise erhalten, aber kopieren Sie sie zuerst an einen sicheren Ort.

### Kann ich danach zu Rockbox zurückkehren?

Ja. Die Wiederherstellung der Originalsoftware ist keine Einbahnstraße; Auf der Seite „Benutzerdefinierte Software“ für Ihr Modell können Sie es erneut installieren.

### Benötige ich die Einstellung Type A / Type B?

Nur das Y1 hat diese Wahl und nur für Originalsoftware. Jedes andere Modell verwendet ein einzelnes Paket.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
