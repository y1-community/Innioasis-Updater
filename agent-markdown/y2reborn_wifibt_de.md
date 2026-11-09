---
title: "WLAN-, Bluetooth- und UKW-Radio-Setup für Reborn (Y2Linux) – Innioasis Updater"
description: "Kurze Anleitung nach der Installation für Reborn (Y2Linux / Y2Reborn) auf Innioasis Y2: Kopieren Sie system.img und richten Sie dann WLAN, Bluetooth und UKW-Radio ein."
language: "de"
source: "https://innioasis.app/y2reborn_wifibt_de.html"
---

# WLAN-, Bluetooth- und UKW-Radio-Setup für Reborn (Y2Linux) – Innioasis Updater

Innioasis Y2 · Reborn Nach der Installation

# Richten Sie WLAN, Bluetooth und UKW-Radio ein.

Kopieren Sie eine Datei auf Ihren Player. Reborn erledigt den Rest.[System.img herunterladen (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Installationsanleitung](guides/reborn-y2linux-y2.html)[Warum Y2Reborn?](reborn-y2linux-benefits_de.html)

## Warum diese Datei?

Für Wi-Fi, Bluetooth und UKW-Radio sind fünf MediaTek Firmware-Module erforderlich, die Reborn nicht ausliefern kann. Sie befinden sich im offiziellen Y2 `system.img`. Reborn extrahiert sie einmal, prüft sie und löscht die Datei.

## Aufstellen
  - Laden Sie system.img herunter

Laden Sie die FM-Version 3.2.0 herunter `system.img` an Ihren Computer.[ Laden Sie system.img herunter ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Booten Sie Reborn einmal

Schalten Sie den Player ein. Warten Sie Speicher einrichten Um den Vorgang abzuschließen, starten Sie ihn dann einmal neu.
  - Stellen Sie eine Verbindung zu Ihrem Computer her

Verwenden Sie ein USB-Datenkabel. Der Player erscheint als Interner Speicher.Auf einem Mac?

Installieren [OpenMTP](https://openmtp.ganeshrvel.com/) um den Player zu durchsuchen. Windows und Linux mounten es automatisch.
  - Kopieren Sie system.img in die Firmware

Erstellen Sie einen Ordner mit dem Namen `Firmware` im Stammverzeichnis des internen Speichers. Kopie `system.img` hinein.
  - Warten Sie, bis die Einrichtung abgeschlossen ist

Reborn installiert die Radio-Firmware automatisch und löscht sie `system.img`. Dies dauert etwa 10–20 Sekunden. Warten Sie WLAN und Bluetooth sind bereit.
  - Verbinden Sie WLAN, Bluetooth und UKW-Radio
    - W-lan: Einstellungen → System → Netzwerk → WLAN. Wählen Sie Ihr 2,4-GHz-Netzwerk.
    - Bluetooth: Versetzen Sie Ihre Kopfhörer in den Pairing-Modus. Einstellungen → Bluetooth → wählen Sie sie aus.
    - UKW-Radio: Schließen Sie kabelgebundene Kopfhörer als Antenne an und öffnen Sie dann FM-Radio.

  - Update über WLAN

Zukünftige Reborn-Updates werden über Einstellungen → System → Software-Update installiert. Die Firmware Ihres Radios bleibt erhalten.

## War dieser Leitfaden hilfreich?

Fanden Sie diese Installationsanleitung nach der Installation hilfreich? Ja, es hat geholfen! [ Brauche Hilfe zu Discord ](https://discord.gg/zHrT2zrcek) Vielen Dank für Ihr Feedback! Genießen Sie kabelloses Hören auf Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
