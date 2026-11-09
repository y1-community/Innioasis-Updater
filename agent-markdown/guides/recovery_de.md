---
title: "Innioasis Y1 und Y2 Wiederherstellungshandbuch | Innioasis Firmware-Archiv – Innioasis Firmware-Downloads"
description: "Wiederherstellungsanleitung für Innioasis Y1- und Y2-Player, die sich nach einem Update nicht mehr einschalten lassen oder deren Scrollrad nicht mehr funktioniert. Reset- und Firmware-Schritte."
language: "de"
source: "https://innioasis.app/guides/recovery_de.html"
---

# Innioasis Y1 und Y2 Wiederherstellungshandbuch | Innioasis Firmware-Archiv – Innioasis Firmware-Downloads

Spielerwiederherstellung · Y1 und Y2

# Innioasis Y1 und Y2 Wiederherstellungsanleitung

Lässt sich nicht einschalten, das Rad funktioniert nicht oder die Installation ist auf halbem Weg abgebrochen. Beginnen Sie mit dem Symptom und befolgen Sie dann die Schritte der Reihe nach, anstatt direkt zu einem manuellen Blitz zu springen.[Updater CE holen](../guide_de.html#platform)[Firmware-Downloads](../firmware_de.html)[Fehlerbehebung](../troubleshooting_de.html)

Beginnen Sie mit Innioasis Updater

## Die geführte Installation behebt die meisten dieser Probleme

Der Updater erledigt dies in einem Durchgang. Wählen Sie die Software aus, befolgen Sie die Schritte auf dem Bildschirm, und schon sind Sie fertig. Außerdem erfahren Sie, wann ein Fix oder eine neue Version verfügbar ist.

## Beginnen Sie mit dem Symptom

Diese Leitfäden behandeln die beiden Fehler, die nach einem Update oder einem Flash am häufigsten auftreten. Wählen Sie diejenige aus, die mit dem übereinstimmt, was Sie sehen, und gehen Sie sie dann der Reihe nach durch.

### Scrollrad funktioniert nicht

Das Rad dreht sich, aber der Spieler ignoriert es, oder es blieb direkt nach einem Update stehen.

[Y1 Scrollrad-Anleitung](y1-scroll-wheel-not-working_de.html) · [Y2 Scrollrad-Anleitung](y2-scroll-wheel-not-working_de.html)

### Player lässt sich nicht einschalten

Ein schwarzer Bildschirm, keine Ladeanzeige oder ein Logo, das erscheint und verschwindet.

[Y1 Energieführer](y1-wont-turn-on_de.html) · [Y2 Energieführer](y2-wont-turn-on_de.html)

### Die Installation wurde teilweise gestoppt

Der Updater ist vor oder nach der Eingabeaufforderung USB fehlgeschlagen oder die Release-Liste sieht falsch aus.

[Anleitung zur Fehlerbehebung](../troubleshooting_de.html)

### Brauche die Dateien

Originalsoftware und benutzerdefinierte Pakete für jedes Modell.

[Firmware-Downloads](../firmware_de.html)

## Die Pakete Y1 und Y2 sind nicht austauschbarFühren Sie niemals einen Cross-Flash eines Modells durch. Ein Y1 `rom.zip` ist kein Y2-Paket und ein Y2 `rom_y2.zip` läuft nicht auf einem Y1. Das Flashen des falschen Modells ist einer der häufigsten Gründe dafür, dass bei einem Spieler die Steuerung ausfällt oder eine Boot-Schleife auftritt.

Überprüfen Sie das auf dem Player aufgedruckte Modell und passen Sie es dann in Updater CE an, bevor Sie eine Version auswählen.

## Stellen Sie zunächst die passende Originalsoftware wieder her

Installieren Sie vor jedem manuellen Werkzeug die Standard-Firmware für das richtige Modell wieder auf dem Player. Dadurch werden die meisten Update-bezogenen Wheel- und Boot-Fehler behoben.

Y1: Wählen Sie Y1, wählen Sie Originalsoftware, wählen Sie eine stabile Version Y1 und führen Sie dann „Installieren/Wiederherstellen“ aus. [Vollständige Y1 Wiederherstellungsanleitung](restore-original-y1_de.html).

Y2: Wählen Sie Y2, wählen Sie Originalsoftware, wählen Sie eine stabile Version Y2 und führen Sie dann „Installieren/Wiederherstellen“ aus. [Vollständige Y2 Wiederherstellungsanleitung](restore-original-y2_de.html).

Schalten Sie den Player aus und schließen Sie das Datenkabel USB nur an, wenn der Updater Sie dazu auffordert. Lassen Sie die Verbindung bis zur Erfolgsmeldung bestehen.

## Manuelle Wiederherstellung im Lieferumfang von Updater CE

Wenn Updater den Job nicht abschließen kann, werden in derselben Installation auch die manuellen Tools enthalten. [SP Flash Tool](../sp-flash-tool_de.html) ist auf Windows- und Linux-x86-Rechnern gebündelt und die MTKClient-Route deckt macOS ab. Beide benötigen ein zum Modell passendes Firmware-Paket, das auf der Website verfügbar ist [Firmware-Downloads](../firmware_de.html) Seite.

Nutzen Sie die Anleitung für Ihre Plattform und halten Sie den Player aufgeladen. Wenn überhaupt kein Tool den Player erkennt, liegt der Fehler wahrscheinlich eher an der Hardware als an der Firmware.

## Was Sie angeben sollten, wenn Sie um Hilfe bitten
  - Das auf dem Player aufgedruckte Modell – Y1 oder Y2.
  - Was der Bildschirm macht: nichts, ein Logo, eine Boot-Schleife oder der Startbildschirm.
  - Ob ein Computer den Player als MediaTek-Gerät erkennt.
  - Die genaue Updater-Meldung und das von Ihnen ausgewählte Paket.
  - Was Sie bereits ausprobiert haben, einschließlich aller manuellen Werkzeuge.

Veröffentlichen Sie keine privaten Token oder nicht verwandte Systemdateien. Der [Gemeinschaft Discord](https://discord.gg/zHrT2zrcek) und [r/innioasis](https://reddit.com/r/innioasis) sind die schnellsten Orte, um Notizen zu vergleichen.

## Innioasis FAQ zur Wiederherstellung

### Wie behebe ich einen Innioasis-Player, der sich nicht einschalten lässt?

Laden Sie es 30 Minuten lang mit einem bekannten Datenkabel auf, erzwingen Sie einen Neustart, indem Sie die Stromversorgung 15 Sekunden lang gedrückt halten, und prüfen Sie dann, ob ein Computer es erkennt. Wenn dies der Fall ist, stellen Sie die zum Modell passende Originalsoftware wieder her. Wenn nicht, verwenden Sie die manuellen Wiederherstellungstools, die in Updater CE enthalten sind.

### Warum funktioniert mein Scrollrad Y1 oder Y2 nicht?

Wenn das Rad nach einem Update stehen bleibt, liegt in der Regel eine Firmware-Diskrepanz vor. Installieren Sie die zum Modell passende Originalsoftware neu und testen Sie sie erneut. Wenn das Rad in jeder Firmware tot ist, behandeln Sie es als Hardwarefehler.

### Wo lade ich Firmware zur Wiederherstellung herunter?

Auf der Seite „Firmware-Downloads“ unter innioasis.app/firmware.html finden Sie Original- und benutzerdefinierte Pakete für jedes Modell. Wählen Sie immer das Paket Y1 oder Y2 aus, das zum Player passt.

### Welche Wiederherstellungstools sind in Updater CE enthalten?

Updater CE umfasst SP Flash Tool unter Windows und Linux und die MTKClient-Route einschließlich macOS für die manuelle Wiederherstellung, wenn die normale Installation nicht abgeschlossen werden kann.

## Verwandte Korrekturen
  - [Y1-Scrollrad funktioniert nicht](y1-scroll-wheel-not-working_de.html) – Das Click Wheel reagiert nach einem Update nicht mehr
  - [Y2-Scrollrad funktioniert nicht](y2-scroll-wheel-not-working_de.html) — die gleichen Prüfungen für das Y2
  - [Y1 lässt sich nicht einschalten](y1-wont-turn-on_de.html) — Laden, Neustart und manuelle Wiederherstellung
  - [Y2 lässt sich nicht einschalten](y2-wont-turn-on_de.html) — die gleichen Prüfungen für das Y2
  - [SP Flash Tool Anleitung](../sp-flash-tool_de.html) — manuelles Flashen unter Windows und Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
