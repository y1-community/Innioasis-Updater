---
title: "Innioasis Y1 Lässt sich nicht einschalten | Innioasis Firmware-Archiv – Innioasis Firmware-Downloads"
description: "Innioasis Y1 lässt sich nicht einschalten oder laden? Erzwingen Sie einen Neustart, prüfen Sie, ob ein Computer ihn erkennt, und stellen Sie dann die Y1-Firmware wieder her oder verwenden Sie die manuelle SP Flash Tool-Wiederherstellung."
language: "de"
source: "https://innioasis.app/guides/y1-wont-turn-on_de.html"
---

# Innioasis Y1 Lässt sich nicht einschalten | Innioasis Firmware-Archiv – Innioasis Firmware-Downloads

Spielerwiederherstellung · Innioasis Y1

# Innioasis Y1 lässt sich nicht einschalten

Ein schwarzer Bildschirm bedeutet nicht immer, dass ein Spieler tot ist. Arbeiten Sie den Ladevorgang, einen erzwungenen Neustart und die Erkennung auf einem Computer durch, bevor Sie einen manuellen Blitz versuchen.[Updater CE holen](../guide_de.html#platform)[Firmware-Downloads](../firmware_de.html)[Wiederherstellungsanleitung](recovery_de.html)

## Laden Sie den Y1 vor allem anderen ordnungsgemäß auf

Bei den meisten „Y1 lässt sich nicht einschalten“-Meldungen handelt es sich um einen leeren Akku, ein Nur-Ladekabel oder ein Ladegerät, das nicht genügend Strom liefern kann. Bei einem stark entladenen Y1 kann es im eingeschalteten Zustand 20 bis 30 Minuten dauern, bis auf dem Bildschirm etwas angezeigt wird. Geben Sie ihm also Zeit, bevor Sie ihn als tot bezeichnen.
  - Verwenden Sie ein bekanntes USB Daten Kabel, kein reines Ladekabel.
  - Versuchen Sie es mit einem Wandladegerät und dann direkt mit einem Computer-USB-Anschluss – nicht mit einem Hub.
  - Lassen Sie es 30 bis 60 Minuten lang angeschlossen und achten Sie auf ein Ladesymbol oder eine Hintergrundbeleuchtung.
  - Versuchen Sie es mit einem zweiten Kabel und Ladegerät, bevor Sie fortfahren.

## Erzwinge einen Neustart

Halten Sie den Netzschalter etwa 15 Sekunden lang gedrückt, lassen Sie ihn los, warten Sie fünf Sekunden und drücken Sie dann einmal die Netztaste. Dadurch wird ein hängengebliebener Bootvorgang behoben und kann problemlos wiederholt werden.

Wenn auf dem Bildschirm das Logo angezeigt wird und dann schwarz wird, startet der Player und schlägt fehl. Fahren Sie mit der Firmware-Wiederherstellung unten fort. Wenn überhaupt nichts passiert, lassen Sie das Gerät aufgeladen und versuchen Sie es nach einer halben Stunde erneut.

## Überprüfen Sie, ob ein Computer den Player sehen kann

Verbinden Sie das ausgeschaltete Y1 mit einem Datenkabel und öffnen Sie den Geräte-Manager unter Windows. `lsusb` unter Linux oder MTKClient unter macOS. Ein funktionierender Player wird als MediaTek Gerät mit Hersteller-ID angezeigt `0e8d`. Wenn es erscheint, ist die Hardware aktiv genug, um erneut zu blinken, auch wenn der Bildschirm dunkel bleibt.

Wenn nichts angezeigt wird, installieren Sie zuerst den MediaTek-Treiber unter Windows – den [Fahrerführer](../drivers_de.html) deckt Windows- und Linux-Berechtigungen ab.

## Stellen Sie die Standard-Firmware Y1 wieder her

Wenn der Player erkannt wird, aber nicht startet, installieren Sie die Originalsoftware Y1 neu. Verwenden Sie nur ein Y1-Paket; Ein Y2-Build startet nicht auf Y1-Hardware.
  - Offen [Updater CE](../guide_de.html#platform) auf Ihrem Computer.
  - Satz Gerätemodell an Y1.
  - Wählen Sie Original-Software In Software und wählen Sie eine stabile Y1-Version aus – das manuelle Paket ist es `rom.zip`.
  - Klicken Sie Installieren / Wiederherstellen und lassen Sie das Paket extrahieren.
  - Schalten Sie Y1 vollständig aus, schließen Sie das Datenkabel USB nur an, wenn der Updater Sie dazu auffordert, und lassen Sie es bis zur Erfolgsmeldung.
Halten Sie die Stromversorgung stabil. Wenn der Blitz ausfällt, kann der Player unbrauchbar werden. Laden Sie es zunächst auf und schließen Sie es direkt an den Computer an.

## Manuelle Wiederherstellung, wenn der Updater den Player nicht sehen kann

Updater CE enthält manuelle Wiederherstellungstools für den Fall, dass die geführte Installation nicht abgeschlossen werden kann. [SP Flash Tool](../sp-flash-tool_de.html) ist unter Windows und Linux x86 gebündelt und die MTKClient-Route deckt macOS ab. Beide benötigen ein zum Modell passendes Firmware-Paket von [Firmware-Downloads](../firmware_de.html) Seite.

Befolgen Sie die Tool-Anleitung für Ihre Plattform, anstatt Streudateien oder Offsets zu improvisieren. Wenn der Player von keinem Tool erkannt wird, liegt der Fehler wahrscheinlich am Akku, am Ladeanschluss oder an der Platine.

## Wenn es immer noch nicht startet

Hören Sie auf zu blinken und behandeln Sie es als Hardware. Öffnen Sie nicht das Gehäuse und drücken Sie nicht auf den Akku. Fragen Sie die Community nach dem Modell, was der Bildschirm macht, ob ein Computer ihn erkennt und welche Pakete Sie ausprobiert haben – das [Discord Gemeinschaft](https://discord.gg/zHrT2zrcek) kann dabei helfen, eine Serviceroute zu identifizieren.

Eine Bestandswiederherstellung ersetzt das System. Sichern Sie daher vor dem Flashen alle im internen Speicher des Players gespeicherten Daten. Musik auf einer MicroSD-Karte wird von der Wiederherstellung nicht berührt.

## Innioasis Y1 FAQ zur Stromversorgung

### Warum lässt sich mein Innioasis Y1 nicht einschalten?

Die häufigsten Ursachen sind ein vollständig entladener Akku, ein Nur-Ladekabel oder ein schwaches Ladegerät, ein Firmware-Absturz, der den Startvorgang stoppt, oder ein Hardwarefehler. Laden Sie es 30 Minuten lang mit einem bekannten Datenkabel auf, bevor Sie davon ausgehen, dass der Player tot ist.

### Wie erzwinge ich einen Neustart einer Innioasis Y1?

Halten Sie den Netzschalter etwa 15 Sekunden lang gedrückt, lassen Sie ihn los, warten Sie fünf Sekunden und drücken Sie dann einmal die Netztaste. Wenn nichts angezeigt wird, laden Sie das Gerät auf und versuchen Sie es nach 30 Minuten erneut.

### Kann ich eine Y1 wiederherstellen, die sich nicht einschalten lässt?

Oft ja. Wenn ein Computer das Gerät MediaTek immer noch erkennt, installieren Sie das Originalsoftwarepaket Y1 mit Updater CE neu. Wenn es nicht erkannt wird, verwenden Sie die in Updater CE enthaltene Wiederherstellung SP Flash Tool oder MTKClient und eine zum Modell passende Firmware-Datei Y1.

### Muss ein Y1 vor dem Blinken aufgeladen werden?

Ja. Wenn der Blitz ausfällt, kann der Player unbrauchbar werden. Laden Sie es zuerst auf und schließen Sie es direkt an den Computer an, anstatt über einen Hub.

## Verwandte Korrekturen
  - [Y2 lässt sich nicht einschalten](y2-wont-turn-on_de.html) — die gleichen Prüfungen für das Y2
  - [Y1-Scrollrad funktioniert nicht](y1-scroll-wheel-not-working_de.html) – wenn es bootet, das Rad aber nicht
  - [Innioasis Wiederherstellungsanleitung](recovery_de.html) – alle Symptomführer an einem Ort
  - [SP Flash Tool Anleitung](../sp-flash-tool_de.html) — manuelles Flashen unter Windows und Linux
  - [Fehlerbehebung bei einer Installation](../troubleshooting_de.html) – wie ein fehlgeschlagener Flash aussieht

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
