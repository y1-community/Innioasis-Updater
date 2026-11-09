---
title: "Entwickler | Fügen Sie benutzerdefinierte Firmware zu Innioasis Updater CE – Innioasis Firmware-Downloads hinzu"
description: "Entwicklerdokumentation zum Hinzufügen einer benutzerdefinierten Innioasis Y1- oder Y2-Firmware zu Updater CE: Forken des Repositorys, Veröffentlichen von rom.zip-Assets, Bearbeiten von slidia_manifest.xml, Testen und Öffnen einer Pull-Anfrage."
language: "de"
source: "https://innioasis.app/developers_de.html"
---

# Entwickler | Fügen Sie benutzerdefinierte Firmware zu Innioasis Updater CE – Innioasis Firmware-Downloads hinzu

Für Firmware-Entwickler

# Fügen Sie Ihre Firmware zu Updater CE hinzu.

Updater CE ist der Community-Katalog und Installer für benutzerdefinierte Firmware. Entwickeln Sie Ihr Projekt aus einer Basis ROM, veröffentlichen Sie es als öffentliches Repository mit den richtigen Release-Assets und fügen Sie die Modelleinträge hinzu `slidia_manifest.xml`, testen Sie die Modellfilter und öffnen Sie eine Pull-Anfrage. Ein Repository kann jedes unterstützte Modell bedienen.[Sehen Sie sich die Quelle Updater CE an](https://github.com/y1-community/Innioasis-Updater)[Durchsuchen Sie Software-Downloads](firmware_de.html)

## Beginnen Sie mit einer Basis ROM

Basis-ROMs bieten Entwicklern benutzerdefinierter Firmware eine saubere Android-Grundlage mit aktivierten drahtlosen Funkchips. Auf dem Y1 ermöglichen sie Wi-Fi und GPS neben dem werkseitigen Bluetooth und FM; Auf dem Y2 aktivieren sie neben dem werkseitigen Bluetooth auch Wi-Fi, GPS und FM.Basis ROM-Downloads für die benutzerdefinierte Firmware-Entwicklung, wobei jeweils die Android-Version und die WLAN-Funktionen aktiviert sind[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Herunterladen | Gerät | Android | Drahtlose Funktionen |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Fügt Wi-Fi und GPS zum werkseitigen Bluetooth und FM hinzu (FM funktioniert bereits ab Werk auf dem Y1). Für Y1 Spieler, die mit OS 2.0.0 oder höher ausgeliefert wurden. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Fügt Wi-Fi und GPS zum werkseitigen Bluetooth und FM hinzu (FM funktioniert bereits ab Werk auf dem Y1). Für Y1 Spieler, die mit einem Betriebssystem vor 2.0.0 ausgeliefert wurden. |
| rom_y2.zip | Y2 | Android 4.4.2 | Fügt dem werkseitigen Bluetooth WLAN, GPS und FM hinzu. Der Y2-Radiochip ist vollständig aktiviert, sodass auch hier FM verfügbar ist. |

Bei diesen Bildern handelt es sich um die Standard-Android-Basis (AOSP) mit aktivierten drahtlosen Funkgeräten des Geräts, sodass eine benutzerdefinierte Firmware Netzwerkfunktionen hinzufügen kann, anstatt den Funkstapel zu ersetzen. Sie sind der praktische Ausgangspunkt für die folgenden Veröffentlichungsschritte.

## Verwenden Sie diese Release-Asset-Namen

Der Dateiname ist Teil des Kompatibilitätssignals. Achten Sie auf genaue Namen und legen Sie die ZIP-Dateien in den Release-Assets des Projekts ab, nicht nur im Repository-Quellbaum.Firmware-ZIP-Asset-Namen und unterstützte Geräte``````

| Vermögenswert | Gerät | Hardware | Bedeutung |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 Geräte, die mit OS 2.0.0 oder höher ausgeliefert wurden. |
| rom_type_b.zip | Y1 | Type B | Y1 Geräte, die mit einem Betriebssystem vor 2.0.0 ausgeliefert wurden. |
| rom_y2.zip | Y2 | Y2 | Das Y2-Vollinstallationspaket. Bewahren Sie es getrennt von Y1 Vermögenswerten auf. |
Benennen Sie ein Paket nicht um, damit es zu einem anderen Modell passt. Y1 und Y2 verwenden unterschiedliche MediaTek Plattformdateien und Flash-Konfigurationen. Veröffentlichen Sie das Paket für die tatsächlich unterstützte Hardware.

## So funktioniert die Verbindung

Updater CE liest das Manifest als seinen Katalog. Jede `<package>` Zeile teilt ihm den Projektnamen, das Repository, das Modell und den Handler mit. Wenn ein Benutzer dieses Projekt auswählt, überprüft Updater die veröffentlichten Versionen des Repositorys und sucht nach einem `rom*.zip` Vermögenswert.

### Manifestieren

Benennt das Projekt und ordnet es einem Modell zu. Y1 und Y2 benötigen separate Zeilen, auch wenn sie sich ein Repository teilen.

### Veröffentlichte Veröffentlichung

Enthält die installierbaren ZIP-Assets. Eine einzelne Version kann die Pakete Y1 Type A, Y1 Type B und Y2 zusammen enthalten.

### Updater CE installieren

Verwendet das ausgewählte Modell, um das passende Paket und den modellspezifischen Flash-Pfad auszuwählen. Der Benutzer sollte keinen Dateinamen erraten müssen.

## Veröffentlichen Sie ein Projekt in fünf Schritten
  - Forken Sie das Updater CE-Repository. Erstellen Sie Ihre eigene Gabel [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), und klonen Sie dann Ihren Fork lokal.
  - Bereiten Sie ein öffentliches Firmware-Repository vor. Stellen Sie sicher, dass das Repository öffentlich ist und seine Version die richtigen ZIP-Assets enthält. Sie können setzen `rom.zip`, `rom_type_b.zip`, und `rom_y2.zip` auf derselben Version, wenn sie zur selben Version gehören.
  - Bearbeiten Sie das Manifest. Offen `slidia_manifest.xml` in der Wurzel Ihrer Updater CE-Gabel. Fügen Sie eine Zeile für jedes Modell hinzu, das die Version unterstützt (Y1 und Y2 sind das gemeinsame Paar). Der `repo` Der Wert ist der des Repositorys `owner/repository`; `url` ist die öffentliche Projektseite.
  - Testen Sie den Katalog. Führen Sie Updater über den bearbeiteten Checkout aus. Wählen Sie Y1 und bestätigen Sie, dass im Projekt die Y1 Assets angezeigt werden. Wählen Sie Y2 und bestätigen Sie, dass die Freigabe Y2 angezeigt wird. Überprüfen Sie Type A und Type B separat, wenn beide veröffentlicht werden.
  - Öffnen Sie eine Pull-Anfrage. Schieben Sie die Manifeständerung in Ihren Fork und öffnen Sie eine Pull-Anfrage für das Upstream-Repository Updater CE. Geben Sie den Projektlink, die unterstützten Modelle, das Release-Tag, die Asset-Namen und die von Ihnen getesteten Geräte an.

## Generieren Sie Ihre Manifestzeilen

Füllen Sie das Repository aus und kreuzen Sie jedes Modell an, das die Version unterstützt. Der Generator schreibt einen `<package>` Zeile pro Modell und enthält nur die von Ihnen festgelegten Attribute, sodass das Ergebnis mit dem aktuellen übereinstimmt `slidia_manifest.xml` Format. Jedes von Updater CE gelesene Attribut ist unten verfügbar – die optionalen sind unten Weitere Optionen.Repository-URLDas öffentliche GitHub-Repository. Der Generator extrahiert `owner/repository` von der URL.SoftwarenameWird in der App und im Site-Katalog angezeigt.Projekt-URLBenutzerfreundliche Seite für das Projekt oder seine Versionshinweise.MarkeDeaktivieren Sie diese Option, um die Standardmarke des Modells zu verwenden. SR1, Q3, Q5 und Q3e sind Timmkoo Modelle.Geräte (jeweils eine Zeile)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAndere ModelleFür ein Modell, das oben nicht aufgeführt ist. Bekannte Modelle behalten ihre Katalogschreibweise.Flaggen`do_not_keep_data` – Bieten Sie für diese Firmware niemals „Daten behalten“ anBasierend auf Originalsoftware – fügt hinzu `derivative="y1-community/y1-stock-rom"`

„Daten behalten“ wird nur angeboten, wenn die eingehende Firmware und die installierte Firmware identisch sind oder eine gemeinsame Firmware haben `derivative` Wurzel. Verwenden Sie die Flagge nur, wenn Benutzerdaten tatsächlich nicht übertragen werden können.Weitere Optionen: Symbol, Bildmaterial, Release-Assets, Nachinstallation und Spiegelungen

#### Ikone und KunstwerkSymboldateiWählen Sie das Bild aus, das Sie in das Repository übernehmen möchten. Dadurch wird eine Vorschau angezeigt und die Roh-URL erstellt. es lädt nichts hoch.Symbolpfad im RepositoryPfad zum festgeschriebenen Image, relativ zum Repository-Stamm.SymbolzweigSymbol-URLEine direkte Bild-URL. Wenn es leer ist, verwendet die App die Releases `updater.png` oder ein generiertes Symbol.Vorschau des ausgewählten Symbols

URL des Dunkelmodus-SymbolsOptionales Dark-Theme-Symbol. `image_dark` ist ein akzeptierter Alias.URL für LichtgrafikenSekundäres Artwork, nach dem Veröffentlichungsbild ausprobiert und `icon`.URL für dunkle Kunstwerke

#### Geben Sie Vermögenswerte freiName des Release-AssetsEin Name für jedes ausgewählte Modell. Zur Verwendung leer lassen `rom.zip` auf Y1 und `rom_<model>.zip` anderswo.VermögensmusterGlob wird verwendet, wenn die Zips der Version nicht benannt sind `rom*.zip`.Type A VermögenswertGlob für das Paket Y1 Type A, wenn der Name dies nicht sagt.Type B VermögenswertGlob für das Paket Y1 Type B, wenn der Name dies nicht sagt.Mindest-App-VersionDen Eintrag vor älteren Updater CE-Builds ausblenden.

#### Links, Spiegel und Keep Data-FamilieSeite nach der InstallationNach erfolgreicher Installation geöffnet.Zweite Seite nach der InstallationOptionaler zweiter Schritt für eine mehrseitige Einrichtungsanleitung.Tragbare ReißverschlussspiegelDurch Kommas getrennt `*-mirror` Repositorys, die Portable Flashing Zip-Pakete erstellen.Derivate-RepositoryDie Firmware, auf der diese Version basiert. Zugehörige Firmwares teilen sich eine Datenpartition, die von Keep Data überprüft wird.Info-RepositoryApp-Repository, dessen Releases die Apps in dieser Firmware beschreiben. Außerdem ist eine Seite nach der Installation erforderlich.APK-RepositoryApp-Repository, dessen APK die App nach der Firmware herunterlädt und installiert.

#### Katalog-ExtrasSchneckeStabile Kennung für Links und gespeicherte Installationsdatensätze. Das Modell wird automatisch angehängt, wenn mehrere Modelle ausgewählt werden.Beschreibung`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Zeilen kopieren

Das neueste Manifest wird geladen…Zeigen Sie eine Vorschau des neuesten Manifests mit Ihren hinzugefügten Zeilen an

Der Generator holte den Strom `slidia_manifest.xml` aus diesem Repository und haben Ihre generierten Zeilen kurz zuvor eingefügt `</slidia>`.

Für ein gemeinsames Repository reicht eine Zeile nicht aus. Wenn die Zeile Y2 fehlt, erhalten Y2-Benutzer auch dann keinen mit dem Modell übereinstimmenden Eintrag `rom_y2.zip` ist in der Version des Projekts vorhanden. Das Gleiche gilt für jedes andere Modell, das Ihr Release unterstützt.

### Jedes Attribut, das das Manifest liest

Dies sind die Attribute, die aktuelle Updater CE-Builds verstehen. Der Generator schreibt nur die, die Sie ausfüllen; Im Übrigen greift die App auf sinnvolle Standardeinstellungen zurück.slidia_manifest.xml-Paketattribute und ihre Bedeutung``````````````````````````````````````````````````````````````````````````````````````````````

| Attribut | Benötigt | Was es bewirkt |
| --- | --- | --- |
| name | Ja | Der Name der Software wird im Katalog und auf Installationskarten angezeigt. |
| repo | Ja | owner/repo. Die App liest die GitHub-Releases dieses Repositorys. |
| device | Ja | Zielmodell, Großbuchstabe (Y1, Y2, G1, Q3e, …). Behalten Sie einen Eintrag pro Modell. |
| url | Empfohlen | Über den Katalog geöffnete Projektseite oder Versionshinweise. |
| type, handler | Ja, in der Praxis | type="img" und handler="Custom Firmware". Andere Typen und Nicht-Firmware-Handler werden übersprungen. |
| brand | Optional | Katalogmarke (Innioasis, Timmkoo). Empty verwendet die Standardmarke des Modells. |
| package_name | Optional | Dateiname des Release-Assets. Standardmäßig ist rom.zip auf Y1 und rom_<model>.zip bei anderen Modellen. |
| asset_pattern | Optional | Glob ohne Berücksichtigung der Groß- und Kleinschreibung für Versionen, deren Firmware-ZIPs nicht benannt sind rom*.zip (Zum Beispiel my-firmware-*.zip). |
| type_a_asset, type_b_asset | Optional | Globs, die die Zips Y1 Type A und Type B identifizieren, wenn ihre Dateinamen nicht die üblichen Markierungen enthalten. |
| icon | Optional | Logo-URL. Wird nach der Veröffentlichung verwendet updater.png / updater.jpgund als Fallback für jede Veröffentlichung. |
| icon_dark | Optional | Logo mit dunklem Thema. image_dark ist ein akzeptierter Alias. |
| image | Optional | Sekundäres Lichtkunstwerk, danach ausprobiert icon. |
| post_install, post_install2 | Optional | Seite(n) wurden nach erfolgreicher Installation geöffnet. Der zweite Teil umfasst eine mehrstufige Anleitung. |
| portable_zips | Optional | Durch Kommas getrennt *-mirror Repos, die betriebsbereite portable Pakete veröffentlichen. |
| derivative | Optional | Repository, aus dem die Firmware erstellt wird. Firmware mit demselben abgeleiteten Root kann Benutzerdaten behalten. |
| info_repo | Optional | App-Repository, dessen Releases beschreiben, was die Firmware bereitstellt. Erfordert post_install oder post_install2. |
| apk_repo | Optional | App-Repository, dessen APK die App nach der Firmware installiert. |
| min_version | Optional | Blenden Sie den Eintrag aus, wenn Updater CE älter als diese Version ist. |
| do_not_keep_data | Optional | true (Auch 1 / yes) blockiert Keep Data vollständig für diese Firmware. |
| slug | Optional | Stabile Kennung für Links und gespeicherte Installationsdatensätze. Wird aus dem Namen und dem Modell generiert, wenn es leer ist. |
| description | Optional | Kurze Katalogbeschreibung. Dabei kann es sich um den Attributwert oder den Text des Elements handeln. |

Legacy-Namen werden aus Kompatibilitätsgründen weiterhin gelesen: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` und `image_dark`. Neue Einträge sollten die oben genannten aktuellen Namen verwenden.

### Senden Sie die Zeilen als Pull-Anfrage
  - Kopieren Sie die oben generierten Zeilen. Sie entsprechen bereits dem neuesten Manifestformat.
  - Bearbeiten `slidia_manifest.xml` im Repository. Verwenden Sie den Bearbeitungslink unten; Der Repository-Host erstellt automatisch einen Fork und einen Branch für Sie.
  - Fügen Sie die Zeilen direkt vorher ein `</slidia>`, Die vorhandenen Einträge bleiben unverändert.
  - Legen Sie einen neuen Zweig fest (Zum Beispiel `add-your-firmware`), und öffnen Sie dann eine Pull-Anfrage für das Updater CE-Repository.
  - In die PR einbeziehen den Projektlink, unterstützte Modelle, Release-Tag, Asset-Namen und die von Ihnen getesteten Geräte.
[Bearbeiten Sie das Updater CE-Manifest](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Sehen Sie sich das neueste Manifest an](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Schreiben Sie die Modellnamen in Großbuchstaben, verwenden Sie die genaue URL Ihres öffentlichen Repositorys und behalten Sie diese bei `type="img"` und `handler="Custom Firmware"` für einen Firmware-Eintrag.

## Sorgen Sie dafür, dass die Veröffentlichung leicht zu überprüfen ist

Geben Sie der Veröffentlichung ein klares Etikett und einen Veröffentlichungshinweis. Das Tag ist für Menschen nützlich, aber die ZIP-Asset-Namen werden von Updater CE verwendet, um die Installationspakete zu identifizieren.

### Release-Checkliste
  - Veröffentlichen Sie die Veröffentlichung öffentlich.
  - Hängen Sie die ZIP-Dateien als Release-Assets an.
  - Geben Sie in den Anmerkungen das unterstützte Modell und Type A oder Type B an.
  - Listen Sie alle erforderlichen Vorbereitungen oder bekannten Grenzwerte auf.

### Eine Veröffentlichung, drei Assets

Eine freigegebene Version kann enthalten `rom.zip`, `rom_type_b.zip`, und `rom_y2.zip`. Der Updater klassifiziert sie separat und wählt aus den Modell- und Hardwarefiltern aus.

### Bündeln Sie keine Vermutungen

Fügen Sie kein Y1-Paket unter dem Dateinamen Y2 ein und fügen Sie keine ungetesteten Scatter-, Preloader- oder Partitionsdaten hinzu, nur um ein Asset anzuzeigen.

## Warum die Modelleinträge beim Flashen wichtig sind

Das Manifest ist nicht nur ein Download-Menü. Nach der Extraktion verwendet Updater CE das aufgelöste Modell, um den passenden Installationspfad vorzubereiten. Y1 und Y2 haben unterschiedliche Plattformdateien, Preloader, Scatter-Konfigurationen und Gerätelayouts.
  - Y1: Der Updater bereitet den Pfad Y1 vor und verwendet die benannten Partitionen des Geräts, wenn MTKClient verwendet wird.
  - Y2: Der Updater bereitet den Pfad Y2 vor und verwendet die MT6582-Konfiguration Y2. Bei der vollständigen Wiederherstellung können physische Adressen aus den modellkorrekten Streudaten verwendet werden.
  - Plattformübergreifende Unterstützung: Updater CE übernimmt das native Flashen direkt unter Windows, Linux und macOS (unterstützt sowohl Intel- als auch Apple Silicon Macs) ohne zusätzliche Flash-Tools.
Mitwirkende sollten korrekte Firmware-Dateien bereitstellen, keine Flash-Offsets. Bearbeiten Sie keine Scatter-Adressen, Preloader, DA-Dateien oder Partitionsbefehle, um ein fehlerhaftes Paket zu umgehen. Korrigieren Sie das Release-Asset und testen Sie es am vorgesehenen Modell.

## Bevor Sie eine Zusammenführung beantragen
  - Validieren Sie das XML mit einem XML-Parser. Ein fehlendes Zitat oder Schluss `/>` kann jeden Eintrag danach ausblenden.
  - Starten Sie den Updater von Ihrem Checkout aus, damit er das lokale Manifest vor der Remote-Aktualisierung lädt.
  - Überprüfen Sie Y1 und Y2 unabhängig voneinander. Bestätigen Sie, dass das Projekt nur dort angezeigt wird, wo sein Paket unterstützt wird.
  - Überprüfen Sie die Release-Liste auf `rom.zip`, `rom_type_b.zip`, und `rom_y2.zip` soweit zutreffend.
  - Testen Sie die tatsächliche Installation auf dem vorgesehenen Gerät mit einem zuverlässigen USB-Datenkabel und einem Wiederherstellungsplan für die Rückkehr zur Originalsoftware.
  - Erklären Sie im Pull-Request, was Sie getestet haben. Beschreiben Sie ein ungetestetes Modell nicht als unterstützt.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Für eine lokale Prüfung führen Sie diesen Befehl im Repository-Stammverzeichnis aus. Es überprüft nur die XML-Syntax. Es beweist nicht, dass eine Version gültige Firmware enthält oder dass ein Gerät sicher geflasht werden kann.

## Nützliche Projektlinks[Gabel Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Siehe Manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Notizen zu Community-Beiträgen](support_devs_de.html)[Fehlerbehebung](troubleshooting_de.html)

## Modding-Fähigkeiten für KI-Agenten

Das Repository `skills/` Das Verzeichnis ist eine quellenbasierte Wissensdatenbank für Agenten, die an Y1 und Y2 Hardware, Firmware, Themes und Apps arbeiten. Jeder Skill benennt die Projektdateien, aus denen seine Ansprüche stammen, sodass ein Agent einen Sachverhalt überprüfen kann, bevor er ein Gerät wechselt.Beginnen Sie hier

### [Kompetenzindex und Sicherheitsregeln](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

So laden Sie einen Skill, auf welches Modell sich ein Fakt bezieht und auf welche Partitionen kein Paket schreiben soll.Hardware

### [Y1 Hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, das Rad als Schlüsselereignisse, 480x360-Anzeige, FM/Audiopfade, Speicher und die Type A/B-Partitionszuordnung.Hardware

### [Y2 Hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582-Board, Gerätebaum, GC9503V/ST7701S-Panels, PMIC/DAC-Schienen, Partitionen und das Boot-Image.Firmware

### [Firmware-Pakete](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip Anatomie, Scatter-Dateien, Update-Verträge der Klasse A und die Release-Checkliste.Themen

### [Theme- und Skin-Erstellung](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json-Themes, Rockbox WPS/SBS, Reborn Skins und Y2Player Skin-Format v2.Alle Fähigkeiten

### [Durchsuchen Sie den Skills-Ordner](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, Standard-Android-ROMs, Y2Linux, Android-Apps, Launcher, Versionshinweise und Website-Veröffentlichung.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
