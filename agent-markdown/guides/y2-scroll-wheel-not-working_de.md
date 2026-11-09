---
title: "Innioasis Y2 Scrollrad funktioniert nach Update nicht | Innioasis Firmware-Archiv – Innioasis Firmware-Downloads"
description: "Innioasis Y2 Scrollrad oder Klickrad funktionieren nach einem Update nicht? Installieren Sie die Originalsoftware Y2 neu, überprüfen Sie den Ring und trennen Sie die Firmware von Hardwarefehlern."
language: "de"
source: "https://innioasis.app/guides/y2-scroll-wheel-not-working_de.html"
---

# Innioasis Y2 Scrollrad funktioniert nach Update nicht | Innioasis Firmware-Archiv – Innioasis Firmware-Downloads

Spielerwiederherstellung · Innioasis Y2

# Innioasis Y2 Scrollrad funktioniert nach einem Update nicht

Das Rad dreht sich, aber der Player ignoriert es, oder das Klickrad blieb direkt nach einem Aufblitzen stehen. Hier erfahren Sie, wie Sie einen Firmware-Fehler von einem Hardware-Fehler auf dem Y2 unterscheiden können.[Updater CE holen](../guide_de.html#platform)[Y2 Software-Downloads](../firmware_de.html?model=Y2&software=original-y2)[Wiederherstellungsanleitung](recovery_de.html)

## Finden Sie heraus, ob das Rad oder die Firmware fehlerhaft ist

Bei einem Y2 ist das Rad eine physische Eingabe, aber die Firmware entscheidet, was jede Drehung und jedes Klicken bewirkt. Ein Rad, das angehalten hat, sobald Sie die Software aktualisiert oder aktualisiert haben. Ein Rad, das jede Software ignoriert – Lagerbestand, Rockbox oder ein Wiederherstellungsbildschirm – zeigt auf das Teil.
  - Funktioniert in einer Software, in einer anderen nicht: Firmware-Fehler.
  - Auf jedem Bildschirm tot, einschließlich Wiederherstellung: Rad, Band oder Brett.
  - Nur eine Richtung fehlt: normalerweise Schmutz unter dem Ring oder Verschleiß.
  - Das Rad dreht sich, aber es werden keine Highlights angezeigt: Der Player ist möglicherweise eingefroren. Erzwingen Sie zunächst einen Neustart.

## Kurze Überprüfungen vor der Neuinstallation der Firmware
  - Halten Sie den Netzschalter etwa 15 Sekunden lang gedrückt, um den Player auszuschalten, und starten Sie ihn dann normal.
  - Testen Sie das Rad auf dem Startbildschirm, in den Einstellungen und im Musikplayer.
  - Drücken Sie die physischen Tasten. Wenn Strom und Rückseite reagieren, das Rad aber nicht, liegt der Fehler beim Rad selbst.
  - Laden Sie den Player 30 Minuten lang mit einem bekannten Datenkabel auf.
  - Wenn Sie Rockbox für Y2 oder einen anderen benutzerdefinierten Build installiert haben, kehren Sie zur Originalsoftware zurück und testen Sie erneut.

## Installieren Sie die Y2-Firmware neu, die zu Ihrem Player passt

Das Rad wird von der Firmware angetrieben, so dass ein updatebedingter Fehler behoben werden kann, indem die richtige Y2 Originalsoftware wieder auf dem Player installiert wird. Verwenden Sie niemals ein Y1-Paket auf einem Y2 und wählen Sie keine Version aus, die „nahe genug“ ist – Y2-Pakete werden für Y2-Hardware erstellt.
  - Offen [Updater CE](../guide_de.html#platform) auf Ihrem Computer.
  - Satz Gerätemodell an Y2.
  - Wählen Sie Original-Software In Software und wählen Sie eine stabile Y2-Version aus – das manuelle Paket ist es `rom_y2.zip`.
  - Klicken Sie Installieren / Wiederherstellen und lassen Sie das Paket extrahieren.
  - Schalten Sie Y2 vollständig aus, schließen Sie das Datenkabel USB nur an, wenn der Updater Sie dazu auffordert, und lassen Sie es bis zur Erfolgsmeldung.
Passen Sie das Modell und die Version an. Wenn die Release-Liste wie Y1 Software aussieht, stoppen Sie und wählen Sie Y2 erneut aus. Vollständige Schritte finden Sie in der [Y2-Wiederherstellungsanleitung](restore-original-y2_de.html).

## Überprüfen Sie den Radring auf Ablagerungen oder Beschädigungen

Wenn das Rad steif ist, klemmt oder nur in eine Richtung versagt, können sich Taschenflusen und Sand zwischen dem Ring und dem Gehäuse festsetzen. Schalten Sie den Player aus und wischen Sie den Ring mit einem trockenen Mikrofasertuch ab. Lassen Sie keine Reinigungsmittel oder Alkohol in den Spalt tropfen und hebeln Sie den Ring nicht hoch.

Wenn der Ring locker oder gerissen ist oder nicht mehr klickt, muss der Player gewartet werden. Die Firmware kann ein beschädigtes Rad, ein nicht angeschlossenes Farbband oder einen Flüssigkeitsschaden nicht reparieren.

## Wenn der Player auch nicht startet

Ein fehlgeschlagenes Update kann dazu führen, dass Y2 nicht gestartet werden kann, was wie ein Radfehler aussieht, da keine Eingabe reagiert. Arbeiten Sie durch [Y2 schaltet die Anleitung nicht ein](y2-wont-turn-on_de.html) zum Laden, zum erzwungenen Neustart und zur manuellen Wiederherstellung.

## Innioasis Y2 Häufig gestellte Fragen zum Scrollrad

### Warum funktioniert mein Innioasis Y2 Scrollrad nach einem Update nicht mehr?

Ein Update kann dazu führen, dass der Radtreiber nicht mehr mit der restlichen Firmware übereinstimmt, insbesondere wenn der Flash unterbrochen wurde oder ein Y1-Paket verwendet wurde. Installieren Sie die Y2 Original-Softwareversion für Ihr Modell neu und testen Sie das Rad auf dem Standard-Startbildschirm.

### Wie kann ich feststellen, ob das Klickrad Y2 defekt oder die Firmware fehlerhaft ist?

Testen Sie das Rad in mehr als einer Software. Wenn es in der Standardsoftware funktioniert, aber nicht in Rockbox, handelt es sich um ein Problem mit der Firmware-Zuordnung. Wenn auf keinem Bildschirm etwas passiert, einschließlich eines Wiederherstellungsmenüs, liegt der Verdacht auf das Rad, sein Band oder die Platine.

### Wird das Y2-Scrollrad durch die Wiederherstellung der Originalsoftware repariert?

Es behebt Fehler, die durch ein Update oder ein nicht übereinstimmendes Paket verursacht wurden, und ist das erste, was Sie ausprobieren sollten. Ein physisch beschädigtes Rad, ein loses Farbband oder ein Flüssigkeitsschaden werden nicht repariert.

### Kann ich ein Y1-Firmware-Paket verwenden, um ein Y2-Radproblem zu beheben?

Nein. Die Pakete Y1 und Y2 sind nicht austauschbar und das Flashen des falschen Modells kann die Steuerung verschlechtern. Passen Sie das Modell und die Version an, bevor Sie „Installieren/Wiederherstellen“ ausführen.

## Verwandte Korrekturen
  - [Y1-Scrollrad funktioniert nicht](y1-scroll-wheel-not-working_de.html) — die gleichen Prüfungen für Y1
  - [Y2 lässt sich nicht einschalten](y2-wont-turn-on_de.html) — Strom- und Boot-Wiederherstellung
  - [Innioasis Wiederherstellungsanleitung](recovery_de.html) – alle Symptomführer an einem Ort
  - [Fehlerbehebung bei einer Installation](../troubleshooting_de.html) – wie ein fehlgeschlagener Flash aussieht
  - [Y2 Originalsoftware wiederherstellen](restore-original-y2_de.html) – die vollständige Anleitung zur Wiederherstellung

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
