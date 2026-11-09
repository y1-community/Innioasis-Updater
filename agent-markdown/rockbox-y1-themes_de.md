---
title: "Rockbox-Y1-Themen: Übertragen von Themen mit Updater CE, 240p vs. 360p und Anwenden eines Themas"
description: "So übertragen Sie Themes mit Updater CE auf die Innioasis Y1 (automatischer Push, wenn verfügbar oder geführte Schritt-für-Schritt-Übertragung nach einem MTKClient-Flash unter macOS und Linux), plus 240p vs. 360p-Kompatibilität und Anwenden eines Themes."
language: "de"
source: "https://innioasis.app/rockbox-y1-themes_de.html"
---

# Rockbox-Y1-Themen: Übertragen von Themen mit Updater CE, 240p vs. 360p und Anwenden eines Themas

[← Rockbox-Y1 Hub](rockbox-y1/)

Rockbox-Y1 · Themen & Updater CE

# Rockbox-Y1 Themen: Übertragen Sie mit Updater CE, wählen Sie den Build und dann das Aussehen

Updater CE verwaltet Rockbox-Y1 Designs und Schriftarten für Sie – überträgt sie automatisch auf Y1, wann immer es möglich ist, und führt Sie Schritt für Schritt durch die Übertragung, wenn dies nicht unbeaufsichtigt erfolgen kann (z. B. direkt nach einer MTKClient-Firmware-Installation unter macOS oder Linux).[Holen Sie sich Rockbox & Updater CE](guides/rockbox-y1.html)[Durchsuchen Sie Community-Themen](https://themes.innioasis.app/)[240p vs. 360p](rockbox-y1/resolution.html)

## Übertragen von Themen auf Y1 mit Updater CE

Rockbox speichert seine Firmware im internen Flash von Y1, während Themen, Schriftarten und Benutzereinstellungen im Verborgenen gespeichert sind `.rockbox` Ordner im Speicher des Players (MicroSD-Karte). Da das Flashen eines ROM und das Kopieren von Dateien in den Speicher zwei verschiedene Verbindungen verwenden, Updater CE Passt sich automatisch an Ihr Betriebssystem und die Installationsmethode an:
  - Automatische Übertragung, wenn Updater CE den Player erreichen kann: Wenn Sie einen 360p-Build Rockbox-Y1 installieren (oder die automatische Theme-Synchronisierung in den Einstellungen aktivieren), lädt Updater CE das kuratierte 360p-Theme und Schriftartenpaket im Hintergrund herunter und führt es zusammen. Sobald Y1 über erreichbar ist ADB (Android Debug Bridge) oder als gemountet USB Laufwerk mit einem `.rockbox` Im Ordner Updater CE werden die Designs und Schriftarten für Sie direkt auf den Player übertragen, ohne dass eine manuelle Zip-Extrahierung erforderlich ist.
  - Geführte Schritt-für-Schritt-Übertragung, wenn sie nicht unbeaufsichtigt erfolgen kann (z. B. MTKClient unter macOS und Linux): Wenn Sie Rockbox mit einem blinken MTKClient Bei der Installationsmethode unter macOS oder Linux erfolgt der Flash, während Y1 im Low-Level-Preloader-/BROM-Modus ausgeschaltet ist – bevor Rockbox zum ersten Mal zum Erstellen gestartet wurde `.rockbox` und bevor der Speicher des Players auf Ihrem Computer bereitgestellt wird. Wenn Updater CE die Übertragung während des Flashs nicht unbeaufsichtigt abschließen kann, wird automatisch geöffnet Assistent für Themen und Schriftarten nach der Installation und führt Sie durch die Fertigstellung: 
    - Booten Sie zuerst Rockbox: Updater CE fordert Sie auf, bei Bedarf das USB-Kabel zu trennen und Y1 einzuschalten, damit Rockbox einmal startet und initialisiert `.rockbox` Ordner auf der Karte.
    - Über USB erneut verbinden: Schließen Sie den Y1 wieder an Ihren Mac oder Linux-PC an. Wenn ADB verfügbar ist, erkennt Updater CE den gestarteten Player und überträgt die Design- und Schriftartenpakete automatisch.
    - Oder verwenden Sie den Speichermodus USB mit der geführten Ordnerauswahl: Wenn ADB nicht aktiv ist oder Sie eine direkte Speicherübertragung bevorzugen, werden Sie durch Updater CE zum Aufrufen des Speichermodus USB auf Y1 geführt. Klicken Sie auf Wählen Sie den .rockbox-Ordner, versteckte Ordner anzeigen (Cmd+Shift+. im macOS-Dateidialog oder Ctrl+H unter Linux) und wählen Sie `.rockbox` auf dem Laufwerk Y1 – dann fügt Updater CE alle Designs und Schriftarten für Sie zusammen.

  - Fügen Sie bei Bedarf jederzeit Themen hinzu oder aktualisieren Sie sie: Sie können die gleiche automatisierte oder geführte Übertragung jederzeit ausführen, ohne die Firmware neu zu flashen – öffnen Sie Updater CE und wählen Sie Einstellungen → Rockbox 360p-Designs installieren (Cmd+T auf macOS, Ctrl+T unter Windows und Linux) oder ziehen Sie ein einzelnes Design `.zip` packt auf Updater CE's Smart Drop Fenster.

## 240p, 360p und warum das Etikett auf dem Build steht

Y1 Community-Builds werden mit einem Auflösungslabel veröffentlicht und die Themensammlungen tragen dasselbe Label. 240p-Builds bieten die größte Kompatibilität mit älteren Theme-Paketen; 360p-Builds werden für den neueren Theme-Pfad Y1 erstellt. Das eine zu installieren und das andere anzuwenden ist nicht gefährlich – es sieht nur falsch aus, mit abgeschnittenem Text, fehlenden Elementen oder einer nicht lesbaren Benutzeroberfläche.

Wenn Sie noch keine Theme-Präferenz haben, nehmen Sie den neueren stabilen Build und sein Standard-Theme und wählen Sie dann Themes aus, die seiner Bezeichnung entsprechen. Der [Auflösungsseite](rockbox-y1/resolution.html) geht tiefer; Die Faustregel ist einfach: Build-Label und Theme-Label müssen übereinstimmen.

## Wo Themen leben

Themen sind Dateien auf der Karte MicroSD im Inneren `.rockbox` Ordner – derselbe Ordner, der Einstellungen und Caches enthält. Die Firmware selbst befindet sich auf einem internen Flash, sodass das Hinzufügen, Ändern oder Entfernen eines Themes nie ein erneutes Flashen erfordert.
  - Kopieren Sie den eigenen Ordner des Themes in `.rockbox/themes` auf der Karte.
  - Wählen Sie es dann in den Designeinstellungen des Players aus und starten Sie es neu, damit es angewendet wird.
  - Behalten Sie eine Kopie eines Themes, das Ihnen gefällt, bevor Sie den Build aktualisieren – es handelt sich um eine Datei, nicht um eine Installation.

Aktivieren Sie zuerst versteckte Dateien, wenn Sie den Ordner nicht sehen können: macOS Cmd+Shift+., Windows-Ansicht → Versteckte Elemente, Linux Ctrl+H.

## Anwenden eines Themas in der richtigen Reihenfolge
  - Installieren und starten Sie zuerst Rockbox-Y1; Ein Theme benötigt einen laufenden Build.
  - Kopieren Sie den Theme-Ordner nach `.rockbox/themes` auf der Karte.
  - Öffnen Sie die Theme-Einstellungen und wählen Sie das Theme aus.
  - Starten Sie neu, damit die gesamte Benutzeroberfläche – nicht nur das Menü – es übernimmt.
  - Wenn es kaputt aussieht, wählen Sie ein anderes Thema aus. Die Dateien sind noch vorhanden, wenn Sie es später noch einmal versuchen möchten.

## Ein Thema rückgängig machen, das die Benutzeroberfläche beschädigt hat

Wenn der Player mit etwas Unbrauchbarem startet, müssen Sie die Firmware nicht neu installieren. Benennen Sie das um oder löschen Sie es `.rockbox` Ordner auf der Karte und starten Sie den Player: Der Build erstellt den Ordner mit Standardeinstellungen und einem Standardthema neu. Ihre Musik bleibt unberührt und Sie können die gewünschten Themen anschließend wieder kopieren.[Der .rockbox-Ordner](rockbox-y1/sd-card.html)[Erster Start](rockbox-y1/first-start.html)[Aktualisierung des Builds](rockbox-y1/update.html)

## Fragen, die Menschen stellenWarum führt mich Updater CE durch die Übertragung von Themes nach einer MTKClient-Installation unter macOS oder Linux?

MTKClient flasht den Rockbox ROM in den internen Speicher, während Ihr Y1 im Low-Level-Preloader-/BROM-Modus ausgeschaltet ist, bevor Rockbox gebootet hat, um den zu initialisieren `.rockbox` Ordner und bevor die MicroSD-Karte auf Ihrem Computer bereitgestellt wird. Immer wenn Updater CE den gebooteten Player direkt erreichen kann (über ADB oder ein gemountetes USB-Laufwerk), werden die Themen automatisch übertragen; Wenn dies während des Flashens nicht unbeaufsichtigt möglich ist, öffnet es direkt nach dem Flashen den Schritt mit den geführten Themen und Schriftarten, um Ihnen beim Einschalten des Y1 zu helfen und die Übertragung über ADB oder den USB-Speichermodus abzuschließen.Funktioniert ein Y2-Theme auf dem Y1?

Nein. Die Ports sind separat und die Theme-Unterstützung auf dem Y2 folgt seinen Beta-Builds. Sehen [Rockbox-Y2-Themen](rockbox-y2-themes_de.html).Überstehen Themes ein Update?

Normalerweise ja, weil sie auf der Karte leben und der Flash die ROM schreibt. Wenn ein neuer Build den Theme-Pfad ändert, wenden Sie ein Theme erneut an, das seiner Bezeichnung entspricht.Warum wird das Thema nur zur Hälfte angewendet?

Normalerweise wird das Problem durch einen Neustart behoben. Wenn nicht, sind die Dateien des Themes unvollständig. Kopieren Sie den Ordner erneut, anstatt einzelne Dateien zu bearbeiten.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
