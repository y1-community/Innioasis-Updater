---
title: "Rockbox für Y1 (Rockbox-Y1): Übersicht, Builds und Installationsanleitung"
description: "Rockbox für Y1, Rockbox-Y1 und rockbox-y1 beziehen sich alle auf die Community-Firmware Rockbox für Innioasis Y1. Erfahren Sie, was es hinzufügt, welches Build Sie auswählen sollten und wie Sie es mit Innioasis Updater CE installieren."
language: "de"
source: "https://innioasis.app/rockbox-for-y1_de.html"
---

# Rockbox für Y1 (Rockbox-Y1): Übersicht, Builds und Installationsanleitung

[← Firmware-Downloads](firmware_de.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox für Y1 (Rockbox-Y1)

„Rockbox“, „Rockbox-Y1“ und „Rockbox für Y1“ beziehen sich alle auf dieselbe Community-Firmware Rockbox für Innioasis Y1. Hier erfahren Sie, was es Ihrem Player hinzufügt, welches Build Sie wählen sollten und wie Sie es mit Innioasis Updater CE installieren.[Installieren Sie Rockbox-Y1](rockbox-y1/install.html)[Laden Sie die ROM herunter](rockbox-y1/download.html)[Schriftliches Tutorial](guides/rockbox-y1.html)[Rockbox-Y1-Hub](rockbox-y1/)

## Eine Firmware, mehrere Namen

In Innioasis Updater CE erscheint diese Firmware als Rockbox wenn Sie das Gerätemodell auswählen Y1. Leitfäden, Videos und Versionshinweise nennen es auch Rockbox-Y1 oder Rockbox für Y1 Es ist also klar, dass der Build für Y1 und nicht für Y2 gedacht ist.

Überprüfen Sie vor der Installation immer das auf Ihrem Player aufgedruckte Modell: Die Firmware-Pakete Y1 und Y2 sind nicht austauschbar.

## Was Rockbox-Y1 zu Ihrem Y1 hinzufügt

Rockbox-Y1 ist ein Community-Port der Open-Source-Musik-Player-Firmware Rockbox für Innioasis Y1:
  - Tag-basierte Musikbibliothek – Durchsuchen Sie mithilfe von Audio-Tags nach Künstler, Album, Genre und Jahr oder durchsuchen Sie Ordner direkt.
  - Erweiterte Audiowiedergabe – lückenlose Wiedergabe, Crossfade, ReplayGain und ein vollständiger Equalizer.
  - Benutzerdefinierte Themen – Wählen Sie aus Hunderten von 240p- und 360p-Community-Themen, einschließlich klassischer iPod-Layouts.
  - UKW-Radio — integrierte FM-Radiounterstützung.
  - Optionale Extras – Podcast-Downloads über WLAN und Last.fm / ListenBrainz / Maloja suchen nach unterstützten Builds.
  - Dual-Boot – Wechseln Sie bei unterstützten Builds ohne erneutes Flashen zur werkseitigen Originalsoftware zurück.

## Welchen Y1 Build soll ich wählen?
  - 240p vs. 360p — 240p-Builds funktionieren mit klassischen 320×240 Rockbox-Themen; 360p-Builds verwenden schärfere 480×360 Y1-Themen. Passen Sie die Build-Auflösung an die Themes an, die Sie verwenden möchten ([240p vs. 360p Anleitung](rockbox-y1/resolution.html)).
  - Type A vs. Type B — Type A ist für Y1 Player, die mit der Werkssoftware 2.0.0 oder neuer ausgeliefert wurden; Type B gilt für frühere Y1-Einheiten. Wählen Sie Type A, es sei denn, Sie wissen, dass Ihr Y1 Type B ist.
  - Stabil vs. Nightly — Wählen Sie einen stabilen Build für das tägliche Hören oder einen nächtlichen Build, um die neuesten Änderungen zu testen.

## Direkte Downloads von den Community-Entwicklern

Innioasis Updater CE lädt Firmware-Pakete immer direkt von den Community-Firmware-Entwicklern herunter ([rockbox-y1/rockbox](firmware_de.html?model=Y1&software=rockbox-y1)), und die Entwickler selbst sind allein dafür verantwortlich, ihre Softwareversionen in Updater CE aufzulisten.

Sie können Updater CE die Firmware automatisch herunterladen und installieren lassen oder die ROM-Pakete von unserem herunterladen [Rockbox-Y1 Downloadseite](rockbox-y1/download.html) und [Rockbox ROM Download-Seite](rockbox-rom-download_de.html).[Rockbox-Y1 Downloads](rockbox-y1/download.html)[Von einer lokalen ZIP-Datei installieren](rockbox-y1/portable-zip.html)

## So installieren Sie Rockbox-Y1
  - Öffnen Sie Innioasis Updater CE und stellen Sie ein Gerätemodell an Y1.
  - Auswählen Rockbox In Software.
  - Wählen Sie eine stabile Version (oder aktivieren Sie nächtliche Builds, um eine Vorschau zu testen).
  - Klicken Sie Installieren / Wiederherstellen also lädt Updater CE das Paket direkt vom Entwickler herunter.
  - Schalten Sie Y1 vollständig aus und verbinden Sie es mit einem USB-Datenkabel, wenn Updater CE Sie dazu auffordert.
  - Warten Sie auf die Abschlussmeldung, trennen Sie dann die Verbindung zum Player und schalten Sie ihn ein.

Screenshots und detaillierte Einrichtungstipps finden Sie im [vollständiges Rockbox-Y1 Tutorial](guides/rockbox-y1.html).

## Wiederherstellen der ursprünglichen Y1-Software

Sie können jederzeit zur Werkssoftware zurückkehren: auswählen Y1 und Original-Software Wählen Sie in Updater CE eine stabile Version aus und klicken Sie Installieren / Wiederherstellen. Ihre Musik auf der Karte MicroSD bleibt erhalten. Siehe die [Anleitung zur Wiederherstellung](rockbox-y1/restore-stock.html) und [Y1 Original-Softwareseite](original-software-y1_de.html).

## Häufig gestellte FragenIst Rockbox für Y1 dasselbe wie Rockbox-Y1?

Ja. Rockbox, Rockbox-Y1, Rockbox für Y1 und `rockbox-y1` Alle beziehen sich auf denselben Community-Port Rockbox für Innioasis Y1.Woher lädt Updater CE Rockbox-Y1 herunter?

Updater CE lädt Firmware-Pakete immer direkt von den eigenen Versionen der Community-Firmware-Entwickler herunter (`rockbox-y1/rockbox`). Die Entwickler sind allein dafür verantwortlich, ihre Softwareversionen in Updater CE aufzulisten.Kann ich Rockbox-Y1 auf einem Y2 installieren?

Nein. Der Y2 verfügt über einen eigenen separaten Firmware-Build. Verwenden [Rockbox für Y2](rockbox-for-y2_de.html) stattdessen.Wird durch die Installation von Rockbox-Y1 meine Musik gelöscht?

Nein. Musik wird auf der Karte MicroSD gespeichert und ist beim Flashen der internen Firmware des Players nicht betroffen.

## Verwandte Leitfäden

### [Rockbox-Y1-Hub](rockbox-y1/)

Alle Y1-Anleitungen: Installation, Downloads, Designs, Wiederherstellung, Dual-Boot und Fehlerbehebung.

### [Rockbox-Y1 vs. Rockbox-Y2](rockbox-y1-vs-y2.html)

Wie sich die Builds Y1 und Y2 Rockbox unterscheiden.

### [Rockbox-Y1-Themen](rockbox-y1-themes.html)

So übertragen Sie 240p- und 360p-Themen mit Updater CE.

### [Rockbox Übersicht](rockbox_de.html)

Einführung in Rockbox für Innioasis Y1- und Y2-Spieler.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
