---
title: "Ontwikkelaars | Voeg aangepaste firmware toe aan Innioasis Updater CE - Innioasis Firmwaredownloads"
description: "Ontwikkelaarsdocumentatie voor het toevoegen van een aangepaste Innioasis Y1 of Y2 firmware aan Updater CE: fork de repository, publiceer rom.zip assets, bewerk slidia_manifest.xml, test en open een pull-verzoek."
language: "nl"
source: "https://innioasis.app/developers_nl.html"
---

# Ontwikkelaars | Voeg aangepaste firmware toe aan Innioasis Updater CE - Innioasis Firmwaredownloads

Voor firmware-ontwikkelaars

# Voeg uw firmware toe aan Updater CE.

Updater CE is de communitycatalogus en het installatieprogramma voor aangepaste firmware. Ontwikkel uw project vanuit een basis ROM, publiceer het als een openbare repository met de juiste release-items, voeg de modelgegevens toe aan `slidia_manifest.xml`, test de modelfilters en open een pull-aanvraag. Eén repository kan elk model ondersteunen dat het ondersteunt.[Bekijk de Updater CE-bron](https://github.com/y1-community/Innioasis-Updater)[Blader door softwaredownloads](firmware_nl.html)

## Begin vanuit een basis ROM

Basis-ROM's geven ontwikkelaars van aangepaste firmware een schone Android-basis met de draadloze radiochips ingeschakeld. Op de Y1 schakelen ze Wi-Fi en GPS in naast de fabrieks-Bluetooth en FM; op de Y2 schakelen ze Wi-Fi, GPS en FM in naast de fabrieks-Bluetooth.Basis ROM downloads voor aangepaste firmware-ontwikkeling, waarbij de Android-versie en draadloze functies allemaal mogelijk zijn[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Downloaden | Apparaat | Android | Draadloze functies |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Voegt Wi-Fi en GPS toe aan de fabrieks-Bluetooth en FM (FM werkt al af fabriek op de Y1). Voor Y1 spelers die zijn geleverd met OS 2.0.0 of hoger. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Voegt Wi-Fi en GPS toe aan de fabrieks-Bluetooth en FM (FM werkt al af fabriek op de Y1). Voor Y1 spelers die zijn geleverd met een besturingssysteem ouder dan 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Voegt Wi-Fi, GPS en FM toe aan de fabrieks-Bluetooth. De Y2 radiochip is volledig ingeschakeld, dus FM is hier ook beschikbaar. |

Deze afbeeldingen zijn de standaard Android-basis (AOSP) waarbij de draadloze radio's van het apparaat zijn ingeschakeld, zodat aangepaste firmware netwerkfuncties kan toevoegen in plaats van de radiostack te vervangen. Ze vormen het praktische startpunt voor de onderstaande publicatiestappen.

## Gebruik deze release-itemnamen

De bestandsnaam maakt deel uit van het compatibiliteitssignaal. Houd de namen exact en plaats de ZIP-bestanden in de release-assets van het project, niet alleen in de bronstructuur van de repository.Firmware ZIP-itemnamen en ondersteunde apparaten``````

| Bezit | Apparaat | Hardware | Betekenis |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 apparaten geleverd met OS 2.0.0 of hoger. |
| rom_type_b.zip | Y1 | Type B | Y1 apparaten die zijn geleverd met een eerder besturingssysteem dan 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Het Y2 volledige installatiepakket. Houd het gescheiden van Y1 bezittingen. |
Hernoem een ​​pakket niet om het in een ander model te laten passen. Y1 en Y2 gebruiken verschillende MediaTek platformbestanden en knipperende configuratie. Publiceer het pakket voor de hardware die het daadwerkelijk ondersteunt.

## Hoe de verbinding werkt

Updater CE leest het manifest als catalogus. Elk `<package>` line vertelt de projectnaam, repository, model en handler. Wanneer een gebruiker dat project kiest, controleert Updater de gepubliceerde releases van de repository en zoekt naar een `rom*.zip` bezit.

### Duidelijk

Geeft het project een naam en wijst het toe aan een model. Y1 en Y2 hebben aparte regels nodig, zelfs als ze een repository delen.

### Gepubliceerde uitgave

Bevat de installeerbare ZIP-middelen. Eén enkele release kan de pakketten Y1 Type A, Y1 Type B en Y2 samen bevatten.

### Updater CE-installatie

Gebruikt het geselecteerde model om het bijpassende pakket en het modelspecifieke knipperpad te kiezen. De gebruiker hoeft geen bestandsnaam te raden.

## Publiceer een project in vijf stappen
  - Fork de Updater CE-repository. Maak je eigen vork van [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater)en kloon vervolgens uw fork lokaal.
  - Bereid een openbare firmwareopslagplaats voor. Zorg ervoor dat de repository openbaar is en dat de release de juiste ZIP-items bevat. Je kunt zetten `rom.zip`, `rom_type_b.zip`, en `rom_y2.zip` op dezelfde release als ze tot dezelfde versie behoren.
  - Bewerk het manifest. Openen `slidia_manifest.xml` in de root van uw Updater CE-vork. Voeg één regel toe voor elk model dat de release ondersteunt (Y1 en Y2 zijn het gemeenschappelijke paar). De `repo` waarde is die van de repository `owner/repository`; `url` is de openbare projectpagina.
  - Test de catalogus. Voer Updater uit vanuit de bewerkte kassa. Selecteer Y1 en bevestig dat het project de Y1 activa toont. Selecteer Y2 en bevestig dat de release Y2 wordt weergegeven. Vink Type A en Type B afzonderlijk aan als beide zijn gepubliceerd.
  - Open een pull-aanvraag. Push de manifestwijziging naar uw fork en open een pull-aanvraag in de upstream Updater CE-repository. Vermeld de projectlink, ondersteunde modellen, releasetag, itemnamen en de apparaten die u hebt getest.

## Genereer uw manifestlijnen

Vul de repository in en vink elk model aan dat de release ondersteunt. De generator schrijft er een `<package>` regel per model en bevat alleen de attributen die u instelt, zodat het resultaat overeenkomt met het huidige `slidia_manifest.xml` formaat. Elk attribuut dat Updater CE leest, is hieronder beschikbaar; de optionele staan ​​hieronder Meer opties.Repository-URLDe openbare GitHub-opslagplaats. De generator trekt `owner/repository` van de URL.SoftwarenaamWeergegeven in de app en de sitecatalogus.Project-URLMensgerichte pagina voor het project of de release-opmerkingen.MerkWis dit om het standaardmerk van het model te gebruiken. SR1, Q3, Q5 en Q3e zijn Timmkoo-modellen.Apparaten (elk één lijn)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAndere modellenVoor een model dat hierboven niet vermeld staat. Bekende modellen behouden hun catalogusspelling.Vlaggen`do_not_keep_data` — bied nooit Keep Data aan voor deze firmwareGebouwd op basis van originele software - voegt toe `derivative="y1-community/y1-stock-rom"`

Gegevens behouden wordt alleen aangeboden als de binnenkomende firmware en de geïnstalleerde firmware hetzelfde zijn of een delen `derivative` wortel. Gebruik de vlag alleen als gebruikersgegevens echt niet kunnen worden overgedragen.Meer opties: pictogram, artwork, release-items, post-installatie en mirrors

#### Icoon en kunstwerkPictogrambestandKies de afbeelding die u aan de repository wilt toevoegen. Dit geeft een voorbeeld ervan en bouwt de onbewerkte URL op; er wordt niets geüpload.Pictogrampad in de repositoryPad naar de vastgelegde afbeelding, relatief ten opzichte van de hoofdmap van de repository.Icoon takIcoon-URLEen directe afbeeldings-URL. Indien leeg gebruikt de app de release's `updater.png` of een gegenereerd pictogram.Geselecteerd pictogramvoorbeeld

Pictogram-URL voor donkere modusOptioneel pictogram met een donker thema. `image_dark` is een geaccepteerde alias.URL voor lichte illustratiesSecundair artwork, geprobeerd na de release-afbeelding en `icon`.Donkere artwork-URL

#### Geef activa vrijNaam van item vrijgevenEén naam voor elk geselecteerd model. Laat leeg om te gebruiken `rom.zip` op Y1 en `rom_<model>.zip` elders.ActivapatroonGlob gebruikt wanneer de ritsen van de release geen naam hebben `rom*.zip`.Type A itemGlob voor het pakket Y1 Type A als de naam dit niet zegt.Type B itemGlob voor het pakket Y1 Type B als de naam dit niet zegt.Minimale app-versieVerberg de vermelding voor oudere Updater CE-builds.

#### Links, mirrors en Keep Data-familiePagina na installatieGeopend na een succesvolle installatie.Tweede post-installatiepaginaOptionele tweede stap voor een installatiehandleiding van meerdere pagina's.Draagbare spiegels met ritssluitingDoor komma's gescheiden `*-mirror` repositories die Portable Flashing Zip-pakketten bouwen.Afgeleide opslagplaatsDe firmware waaruit deze release is opgebouwd. Gerelateerde firmwares delen een gegevenspartitie, wat Keep Data controleert.Info-opslagplaatsApp-opslagplaats waarvan de releases de apps in deze firmware beschrijven. Het heeft ook een post-installatiepagina nodig.APK opslagplaatsApp-opslagplaats waarvan APK de app downloadt en installeert na de firmware.

#### Catalogus extra'sNaaktslakStabiele identificatie voor links en opgeslagen installatierecords. Het model wordt automatisch toegevoegd wanneer er meerdere modellen zijn geselecteerd.Beschrijving`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Kopieer regels

Het nieuwste manifest laden...Bekijk een voorbeeld van het nieuwste manifest waaraan uw regels zijn toegevoegd

De generator haalde de stroom op `slidia_manifest.xml` vanuit deze repository en plaatste uw gegenereerde regels vlak daarvoor `</slidia>`.

Eén regel is niet genoeg voor een gedeelde repository. Als de regel Y2 ontbreekt, krijgen Y2-gebruikers geen invoer die overeenkomt met het model, zelfs als `rom_y2.zip` bestaat in de release van het project. Hetzelfde geldt voor elk ander model dat door uw release wordt ondersteund.

### Elk attribuut dat in het manifest staat

Dit zijn de kenmerken die de huidige Updater CE-builds begrijpen. De generator schrijft alleen degene die u invult; voor de rest valt de app terug op verstandige standaardinstellingen.slidia_manifest.xml pakketkenmerken en hun betekenis``````````````````````````````````````````````````````````````````````````````````````````````

| Attribuut | Nodig | Wat het doet |
| --- | --- | --- |
| name | Ja | Softwarenaam weergegeven in de catalogus en op installatiekaarten. |
| repo | Ja | owner/repo. De app leest de GitHub-releases van die repository. |
| device | Ja | Doelmodel, hoofdletter (Y1, Y2, G1, Q3e, …). Bewaar één inzending per model. |
| url | Aanbevolen | Projectpagina of release-opmerkingen geopend vanuit de catalogus. |
| type, handler | Ja in de praktijk | type="img" en handler="Custom Firmware". Andere typen en niet-firmware-handlers worden overgeslagen. |
| brand | Optioneel | Catalogusmerk (Innioasis, Timmkoo). Leeg gebruikt het standaardmerk van het model. |
| package_name | Optioneel | Bestandsnaam van item vrijgeven. Standaard ingesteld op rom.zip op Y1 en rom_<model>.zip op andere modellen. |
| asset_pattern | Optioneel | Hoofdletterongevoelige glob voor releases waarvan de firmware-zips geen naam hebben rom*.zip (Bijvoorbeeld my-firmware-*.zip). |
| type_a_asset, type_b_asset | Optioneel | Globs die de zips Y1 Type A en Type B identificeren wanneer hun bestandsnamen niet de gebruikelijke markeringen bevatten. |
| icon | Optioneel | Logo-URL. Gebruikt na de eigen release updater.png / updater.jpg, en als reserve voor elke release. |
| icon_dark | Optioneel | Logo met donker thema. image_dark is een geaccepteerde alias. |
| image | Optioneel | Secundair lichtkunstwerk, geprobeerd na icon. |
| post_install, post_install2 | Optioneel | Pagina('s) geopend na een succesvolle installatie. De tweede behandelt een meerstappengids. |
| portable_zips | Optioneel | Door komma's gescheiden *-mirror repo's die kant-en-klare draagbare pakketten publiceren. |
| derivative | Optioneel | Repository waaruit de firmware is opgebouwd. Firmware met dezelfde afgeleide root kan gebruikersgegevens bewaren. |
| info_repo | Optioneel | App-repository waarvan de releases beschrijven wat de firmware implementeert. Vereist post_install of post_install2. |
| apk_repo | Optioneel | App-repository waarvan APK de app installeert na de firmware. |
| min_version | Optioneel | Verberg de vermelding als Updater CE ouder is dan deze versie. |
| do_not_keep_data | Optioneel | true (Ook 1 / yes) blokkeert Gegevens volledig bewaren voor deze firmware. |
| slug | Optioneel | Stabiele identificatie voor links en opgeslagen installatierecords. Gegenereerd op basis van de naam en het model wanneer leeg. |
| description | Optioneel | Korte catalogusbeschrijving. Dit kan de attribuutwaarde zijn of de tekst van het element. |

Verouderde namen worden nog steeds gelezen op compatibiliteit: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` en `image_dark`. Nieuwe vermeldingen moeten de huidige namen hierboven gebruiken.

### Dien de regels in als een pull-aanvraag
  - Kopieer de gegenereerde regels hierboven. Ze komen al overeen met het nieuwste manifestformaat.
  - Bewerking `slidia_manifest.xml` in de repository. Gebruik de onderstaande bewerkingslink; de repositoryhost maakt automatisch een fork en een branch voor u.
  - Plak de lijnen net ervoor `</slidia>`, de bestaande vermeldingen ongewijzigd laten.
  - Zich engageren voor een nieuwe vestiging (Bijvoorbeeld `add-your-firmware`) en open vervolgens een pull-aanvraag voor de Updater CE-repository.
  - In de PR, opnemen de projectlink, ondersteunde modellen, releasetag, itemnamen en de apparaten die u hebt getest.
[Bewerk het Updater CE-manifest](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Zie het laatste manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Houd de modelnamen in hoofdletters, gebruik de exacte URL van uw openbare repository en bewaar deze `type="img"` en `handler="Custom Firmware"` voor een firmware-invoer.

## Zorg ervoor dat de vrijgave eenvoudig te verifiëren is

Geef de release een duidelijke tag en releasenote. De tag is handig voor mensen, maar de ZIP-itemnamen zijn wat Updater CE gebruikt om de installatiepakketten te identificeren.

### Controlelijst vrijgeven
  - Publiceer de release openbaar.
  - Voeg de ZIP-bestanden toe als release-items.
  - Vermeld het ondersteunde model en Type A of Type B in de opmerkingen.
  - Vermeld eventuele vereiste voorbereidingen of bekende limieten.

### Eén release, drie activa

Een gedeelde release kan bevatten `rom.zip`, `rom_type_b.zip`, en `rom_y2.zip`. Updater classificeert ze afzonderlijk en kiest uit de model- en hardwarefilters.

### Bundel geen gissingen

Voeg geen Y1-pakket toe onder de bestandsnaam Y2, en voeg niet-geteste scatter-, preloader- of partitiegegevens toe alleen maar om een ​​asset te laten verschijnen.

## Waarom de modelgegevens van belang zijn tijdens het knipperen

Het manifest is niet alleen een downloadmenu. Na extractie gebruikt Updater CE het opgeloste model om het overeenkomende installatiepad voor te bereiden. Y1 en Y2 hebben verschillende platformbestanden, preloaders, verspreidingsconfiguratie en apparaatindelingen.
  - Y1: de updater bereidt het pad Y1 voor en gebruikt de benoemde partities van het apparaat wanneer MTKClient wordt gebruikt.
  - Y2: de updater bereidt het pad Y2 voor en gebruikt de Y2 MT6582-configuratie. Bij volledig herstel kunnen fysieke adressen uit de modelcorrecte spreidingsgegevens worden gebruikt.
  - Ondersteuning voor meerdere platforms: Updater CE verwerkt native flashen rechtstreeks in Windows, Linux en macOS (ondersteunt zowel Intel- als Apple Silicon Macs) zonder extra flashtools.
Bijdragers moeten correcte firmwarebestanden aanleveren, geen flash-offsets. Bewerk geen verspreidingsadressen, preloaders, DA-bestanden of partitieopdrachten om een ​​slecht pakket te omzeilen. Repareer het release-item en test het op het beoogde model.

## Voordat u een fusie aanvraagt
  - Valideer de XML met een XML-parser. Een ontbrekend citaat of afsluiting `/>` kan elk item erna verbergen.
  - Start de updater vanuit uw kassa, zodat deze het lokale manifest laadt vóór de externe vernieuwing.
  - Controleer Y1 en Y2 onafhankelijk van elkaar. Bevestig dat het project alleen verschijnt als het pakket ervan wordt ondersteund.
  - Controleer de releaselijst voor `rom.zip`, `rom_type_b.zip`, en `rom_y2.zip` zoals van toepassing.
  - Test de daadwerkelijke installatie op het beoogde apparaat, met een betrouwbare USB datakabel en een herstelplan voor terugkeer naar de originele software.
  - Leg in het pull-verzoek uit wat u hebt getest. Beschrijf een niet-getest model niet als ondersteund.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Voor een lokale controle voert u die opdracht uit vanuit de hoofdmap van de repository. Het verifieert alleen de XML-syntaxis; het bewijst niet dat een release geldige firmware bevat of dat een apparaat veilig kan worden geflasht.

## Handige projectlinks[Vorkupdater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Zie het manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Aantekeningen bij bijdragen van de gemeenschap](support_devs_nl.html)[Probleemoplossing](troubleshooting_nl.html)

## Moddingvaardigheden voor AI-agenten

Die van de opslagplaats `skills/` directory is een brongebaseerde kennisbank voor agenten die werken aan Y1 en Y2 hardware, firmware, thema's en apps. Elke vaardigheid noemt de projectbestanden waar de claims vandaan komen, zodat een agent een feit kan controleren voordat hij een apparaat wijzigt.Begin hier

### [Vaardigheidsindex en veiligheidsregels](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Hoe u een vaardigheid laadt, op welk model een feit van toepassing is en op welke partities geen pakket mag schrijven.Hardware

### [Y1 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, het wiel als belangrijkste gebeurtenissen, 480x360 weergave, FM/audiopaden, opslag en de Type A/B-partitiekaart.Hardware

### [Y2 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582-kaart, apparaatboom, GC9503V/ST7701S-panelen, PMIC/DAC-rails, partities en de opstartimage.Firmware

### [Firmware-pakketten](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomie, verspreidingsbestanden, klasse A-updatecontracten en de vrijgavechecklist.Thema's

### [Thema- en skin-auteuring](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json-thema's, Rockbox WPS/SBS, Reborn skins en Y2Player skinformaat v2.Alle vaardigheden

### [Blader door de vaardighedenmap](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, standaard Android-ROM's, Y2Linux, Android-apps, draagraketten, release-opmerkingen en sitepublicatie.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
