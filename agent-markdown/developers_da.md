---
title: "Udviklere | Tilføj tilpasset firmware til Innioasis Updater CE - Innioasis Firmware-downloads"
description: "Udviklerdokumentation til tilføjelse af en tilpasset Innioasis Y1 eller Y2 firmware til Updater CE: Fork the repository, publicer rom.zip aktiver, rediger slidia_manifest.xml, test og åbn en pull-anmodning."
language: "da"
source: "https://innioasis.app/developers_da.html"
---

# Udviklere | Tilføj tilpasset firmware til Innioasis Updater CE - Innioasis Firmware-downloads

For firmwareudviklere

# Tilføj din firmware til Updater CE.

Updater CE er fællesskabskataloget og installationsprogrammet til tilpasset firmware. Udvikl dit projekt fra en base ROM, udgiv det som et offentligt lager med de korrekte udgivelsesaktiver, tilføj modelposterne til `slidia_manifest.xml`, test modelfiltrene, og åbn en pull-anmodning. Et lager kan betjene hver model, det understøtter.[Se Updater CE-kilden](https://github.com/y1-community/Innioasis-Updater)[Gennemse softwaredownloads](firmware_da.html)

## Start fra en base ROM

Base ROM'er giver brugerdefinerede firmwareudviklere et rent Android-grundlag med de trådløse radiochips aktiveret. På Y1 aktiverer de Wi-Fi og GPS sammen med fabrikkens Bluetooth og FM; på Y2 aktiverer de Wi-Fi, GPS og FM sammen med fabriks Bluetooth.Grundlæggende ROM downloads til tilpasset firmwareudvikling, med Android-versionen og trådløse funktioner, som hver enkelt muliggør[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Download | Enhed | Android | Trådløse funktioner |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Tilføjer Wi-Fi og GPS til fabrikkens Bluetooth og FM (FM fungerer allerede på Y1 fra fabrikken). For Y1 spillere, der blev leveret med OS 2.0.0 eller nyere. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Tilføjer Wi-Fi og GPS til fabrikkens Bluetooth og FM (FM fungerer allerede på Y1 fra fabrikken). For Y1 spillere, der blev leveret med et OS tidligere end 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Tilføjer Wi-Fi, GPS og FM til fabrikkens Bluetooth. Radiochippen Y2 er fuldt aktiveret, så FM er også tilgængelig her. |

Disse billeder er standard Android-basen (AOSP) med enhedens trådløse radioer aktiveret, så en brugerdefineret firmware kan tilføje netværksfunktioner i stedet for at erstatte radiostakken. De er det praktiske udgangspunkt for udgivelsestrinene nedenfor.

## Brug disse udgivelsesaktivnavne

Filnavnet er en del af kompatibilitetssignalet. Hold navnene nøjagtige, og sæt ZIP-filerne i projektets udgivelsesaktiver, ikke kun i lagerkildetræet.Firmware ZIP-aktivnavne og understøttede enheder``````

| Aktiv | Enhed | Hardware | Betydning |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 enheder, der blev leveret med OS 2.0.0 eller nyere. |
| rom_type_b.zip | Y1 | Type B | Y1 enheder, der blev leveret med et OS tidligere end 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Y2 fuldinstallationspakken. Hold det adskilt fra Y1 aktiver. |
Omdøb ikke en pakke for at få den til at passe til en anden model. Y1 og Y2 bruger forskellige MediaTek platformsfiler og blinkende konfiguration. Udgiv pakken for den hardware, den faktisk understøtter.

## Hvordan forbindelsen fungerer

Updater CE læser manifestet som sit katalog. hver `<package>` linje fortæller projektets navn, lager, model og handler. Når en bruger vælger det pågældende projekt, tjekker Updater depotets offentliggjorte udgivelser og leder efter en `rom*.zip` aktiv.

### Manifest

Navngiver projektet og knytter det til en model. Y1 og Y2 har brug for separate linjer, selv når de deler et lager.

### Udgivet udgivelse

Indeholder de installerbare ZIP-aktiver. En enkelt udgivelse kan indeholde pakkerne Y1 Type A, Y1 Type B og Y2 sammen.

### Updater CE installation

Bruger den valgte model til at vælge den matchende pakke og den modelspecifikke blinksti. Brugeren skal ikke gætte et filnavn.

## Udgiv et projekt i fem trin
  - Fork Updater CE-lageret. Lav din egen gaffel af [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), og klon derefter din gaffel lokalt.
  - Forbered et offentligt firmwarelager. Sørg for, at lageret er offentligt, og at dets udgivelse indeholder de korrekte ZIP-aktiver. Du kan sætte `rom.zip`, `rom_type_b.zip`, og `rom_y2.zip` på samme udgivelse, når de tilhører samme version.
  - Rediger manifestet. Åbn `slidia_manifest.xml` i roden af din Updater CE-gaffel. Tilføj en linje for hver model, som udgivelsen understøtter (Y1 og Y2 er det fælles par). Den `repo` værdien er depotets `owner/repository`; `url` er den offentlige projektside.
  - Test kataloget. Kør Updater fra den redigerede kasse. Vælg Y1, og bekræft, at projektet viser aktiverne Y1. Vælg Y2, og bekræft, at det viser Y2-udgivelsen. Tjek Type A og Type B separat, når begge er udgivet.
  - Åbn en pull-anmodning. Skub manifestændringen til din gaffel, og åbn en pull-anmodning mod upstream Updater CE-lageret. Inkluder projektlinket, understøttede modeller, frigivelsesmærke, aktivnavne og de enheder, du har testet.

## Generer dine manifestlinjer

Udfyld depotet og marker hver model, som udgivelsen understøtter. Generatoren skriver en `<package>` linje pr. model og inkluderer kun de attributter, du angiver, så resultatet matcher det aktuelle `slidia_manifest.xml` format. Hver attribut, Updater CE læser, er tilgængelig nedenfor - de valgfrie er under Flere muligheder.Repository URLDet offentlige GitHub arkiv. Generatoren udtrækker `owner/repository` fra URL'en.SoftwarenavnVist i appen og webstedskataloget.Projekt URLMenneskevendt side for projektet eller dets udgivelsesbemærkninger.MærkeRyd dette for at bruge modellens standardmærke. SR1, Q3, Q5 og Q3e er Timmkoo modeller.Enheder (en linje hver)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAndre modellerFor en model, der ikke er nævnt ovenfor. Kendte modeller beholder deres katalogstavning.Flag`do_not_keep_data` — Tilbyd aldrig Keep Data til denne firmwareBygget fra original software — tilføjer `derivative="y1-community/y1-stock-rom"`

Keep Data tilbydes kun, når den indgående firmware og den installerede firmware er den samme eller deler en `derivative` rod. Brug kun flaget, når brugerdata reelt ikke kan overføres.Flere muligheder: ikon, kunst, frigivelsesaktiver, efterinstallation og spejle

#### Ikon og kunstværkIkon filVælg det billede, du vil forpligte til depotet. Dette viser den og bygger dens rå URL; den uploader ikke noget.Ikonsti i repositorySti til det forpligtede billede i forhold til lagerroden.Ikon grenIkon URLEn direkte billed-URL. Når den er tom, bruger appen udgivelsens `updater.png` eller et genereret ikon.Forhåndsvisning af valgt ikon

URL til ikon i mørk tilstandValgfrit mørkt tema-ikon. `image_dark` er et accepteret alias.Lys kunstværk URLSekundært kunstværk, prøvet efter udgivelsesbilledet og `icon`.URL til mørkt kunstværk

#### Frigiv aktiverFrigiv aktivnavnÉt navn for hver valgt model. Lad være tom til brug `rom.zip` på Y1 og `rom_<model>.zip` andre steder.AktivmønsterGlob bruges, når udgivelsens lynlåse ikke er navngivet `rom*.zip`.Type A aktivGlob for Y1 Type A-pakken, når dens navn ikke siger det.Type B aktivGlob for Y1 Type B-pakken, når dens navn ikke siger det.Minimum appversionSkjul indgangen fra ældre Updater CE builds.

#### Links, spejle og Keep Data-familienSiden efter installationÅbnet efter en vellykket installation.Anden side efter installationValgfrit andet trin til en flersidet opsætningsvejledning.Bærbare lynlåsspejleKommasepareret `*-mirror` repositories, der bygger Portable Flashing Zip-pakker.DerivatlagerFirmwaren, som denne udgivelse er bygget af. Relaterede firmwares deler en datapartition, hvilket Keep Data kontrollerer.InfolagerApp-repo, hvis udgivelser beskriver apps i denne firmware. Det har også brug for en side efter installation.APK depotApp-repo, hvis APK appen downloader og installerer efter firmwaren.

#### Katalog ekstramaterialeSneglStabil identifikator for links og gemte installationsposter. Modellen tilføjes automatisk, når der vælges flere modeller.Beskrivelse`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Kopier linjer

Indlæser det seneste manifest...Se forhåndsvisning af det seneste manifest med dine linjer tilføjet

Generatoren hentede strømmen `slidia_manifest.xml` fra dette lager og indsatte dine genererede linjer lige før `</slidia>`.

En linje er ikke nok til et delt lager. Hvis Y2-linjen mangler, vil Y2-brugere ikke få en model-matchet post, selv når `rom_y2.zip` findes i projektets udgivelse. Det samme gælder for alle andre modeller, som din udgivelse understøtter.

### Hver egenskab, som manifestet læser

Dette er de attributter, som nuværende Updater CE-bygninger forstår. Generatoren skriver kun dem du udfylder; appen falder tilbage til fornuftige standardindstillinger for resten.slidia_manifest.xml-pakkeattributter og deres betydning``````````````````````````````````````````````````````````````````````````````````````````````

| Attribut | Tiltrængt | Hvad den gør |
| --- | --- | --- |
| name | Ja | Softwarenavn vist i kataloget og på installationskort. |
| repo | Ja | owner/repo. Appen læser dette lagers GitHub udgivelser. |
| device | Ja | Målmodel, store bogstaver (Y1, Y2, G1, Q3e, …). Behold én post pr. model. |
| url | Anbefales | Projektside eller release notes åbnet fra kataloget. |
| type, handler | Ja i praksis | type="img" og handler="Custom Firmware". Andre typer og ikke-firmwarehandlere springes over. |
| brand | Valgfrit | Katalog mærke (Innioasis, Timmkoo). Empty bruger modellens standardmærke. |
| package_name | Valgfrit | Frigiv aktiv filnavn. Standard til rom.zip på Y1 og rom_<model>.zip på andre modeller. |
| asset_pattern | Valgfrit | Skift-ufølsom glob til udgivelser, hvis firmware-zips ikke er navngivet rom*.zip (f.eks my-firmware-*.zip). |
| type_a_asset, type_b_asset | Valgfrit | Globs, der identificerer Y1 Type A og Type B zips, når deres filnavne ikke indeholder de sædvanlige markører. |
| icon | Valgfrit | Logo URL. Brugt efter udgivelsens egen updater.png / updater.jpg, og som reserve for hver udgivelse. |
| icon_dark | Valgfrit | Mørkt tema logo. image_dark er et accepteret alias. |
| image | Valgfrit | Sekundært lys kunstværk, prøvet efter icon. |
| post_install, post_install2 | Valgfrit | Side(r) åbnet efter en vellykket installation. Den anden dækker en vejledning med flere trin. |
| portable_zips | Valgfrit | Kommasepareret *-mirror reposer, der udgiver klar til at køre bærbare pakker. |
| derivative | Valgfrit | Repository firmwaren er bygget fra. Firmware med samme afledte rod kan beholde brugerdata. |
| info_repo | Valgfrit | Applager, hvis udgivelser beskriver, hvad firmwaren implementerer. Kræver post_install eller post_install2. |
| apk_repo | Valgfrit | Applager, hvis APK appen installerer efter firmwaren. |
| min_version | Valgfrit | Skjul indgangen, når Updater CE er ældre end denne version. |
| do_not_keep_data | Valgfrit | true (også 1 / yes) blokerer Behold data fuldstændigt for denne firmware. |
| slug | Valgfrit | Stabil identifikator for links og gemte installationsposter. Genereret ud fra navnet og modellen, når den er tom. |
| description | Valgfrit | Kort katalogbeskrivelse. Det kan være attributværdien eller elementets tekst. |

Ældre navne læses stadig for kompatibilitet: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` og `image_dark`. Nye poster skal bruge de nuværende navne ovenfor.

### Indsend linjerne som en pull-anmodning
  - Kopier de genererede linjer ovenfor. De matcher allerede det seneste manifestformat.
  - Rediger `slidia_manifest.xml` i depotet. Brug redigeringslinket nedenfor; lagerværten opretter automatisk en gaffel og en gren til dig.
  - Indsæt linjerne lige før `</slidia>`, bevare de eksisterende poster uændrede.
  - Forpligt dig til en ny afdeling (f.eks `add-your-firmware`), åbn derefter en pull-anmodning mod Updater CE-lageret.
  - I PR skal medtages projektlinket, understøttede modeller, release-tag, aktivnavne og de enheder, du testede.
[Rediger Updater CE-manifestet](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Se det seneste manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Hold modelnavnene med store bogstaver, brug den nøjagtige URL på dit offentlige lager, og behold `type="img"` og `handler="Custom Firmware"` for en firmware-indgang.

## Gør udgivelsen nem at verificere

Giv udgivelsen et tydeligt mærke og udgivelsesnote. Tagget er nyttigt for folk, men ZIP-aktivnavnene er, hvad Updater CE bruger til at identificere installationspakkerne.

### Frigiv tjekliste
  - Offentliggør udgivelsen offentligt.
  - Vedhæft ZIP-filerne som udgivelsesaktiver.
  - Angiv den understøttede model og Type A eller Type B i bemærkningerne.
  - Angiv alle nødvendige præparater eller kendte grænser.

### En udgivelse, tre aktiver

En delt udgivelse kan indeholde `rom.zip`, `rom_type_b.zip`, og `rom_y2.zip`. Updater klassificerer dem separat og vælger fra model- og hardwarefiltre.

### Undlad at samle gæt

Medtag ikke en Y1-pakke under Y2-filnavnet, eller tilføj ikke-testede scatter-, preloader- eller partitionsdata bare for at få et aktiv til at dukke op.

## Hvorfor modelindtastningerne betyder noget under blink

Manifestet er ikke kun en downloadmenu. Efter ekstraktion bruger Updater CE den løste model til at forberede den matchende installationssti. Y1 og Y2 har forskellige platformsfiler, forudindlæsere, scatter-konfiguration og enhedslayout.
  - Y1: opdateringsprogrammet forbereder Y1-stien og bruger enhedens navngivne partitioner, når MTKClient bruges.
  - Y2: opdateringsprogrammet forbereder Y2-stien og bruger Y2 MT6582-konfigurationen. Fuld gendannelse kan bruge fysiske adresser fra de modelkorrekte scatter-data.
  - Support på tværs af platforme: Updater CE håndterer native flashing direkte på tværs af Windows, Linux og macOS (understøtter både Intel og Apple Silicon Macs) uden ekstra blinkende værktøjer.
Bidragydere skal levere korrekte firmwarefiler, ikke flash-offsets. Rediger ikke scatter-adresser, forudindlæsere, DA-filer eller partitionskommandoer for at omgå en dårlig pakke. Ret frigivelsesaktivet og test på den tilsigtede model.

## Før du anmoder om en fletning
  - Valider XML med en XML-parser. Et manglende tilbud eller afslutning `/>` kan skjule hver post efter den.
  - Start opdateringsprogrammet fra din kassen, så det indlæser det lokale manifest før fjernopdateringen.
  - Kontroller Y1 og Y2 uafhængigt. Bekræft, at projektet kun vises, hvor dets pakke understøttes.
  - Tjek udgivelseslisten for `rom.zip`, `rom_type_b.zip`, og `rom_y2.zip` efter behov.
  - Test den faktiske installation på den tilsigtede enhed med et pålideligt USB datakabel og en genopretningsplan for tilbagevenden til original software.
  - I pull-anmodningen skal du forklare, hvad du testede. Beskriv ikke en ikke-testet model som understøttet.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

For en lokal kontrol, kør den kommando fra lagerroden. Det verificerer kun XML-syntaks; det beviser ikke, at en udgivelse indeholder gyldig firmware, eller at en enhed er sikker at flashe.

## Nyttige projektlinks[Gaffelopdatering CE](https://github.com/y1-community/Innioasis-Updater/fork)[Se manifestet](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Noter om fællesskabsbidrag](support_devs_da.html)[Fejlfinding](troubleshooting_da.html)

## Modding færdigheder for AI-agenter

Depotets `skills/` directory er en kildebaseret videnbase for agenter, der arbejder med Y1 og Y2 hardware, firmware, temaer og apps. Hver færdighed navngiver projektfilerne, dens krav kommer fra, så en agent kan tjekke en kendsgerning, før han ændrer en enhed.Start her

### [Færdighedsindeks og sikkerhedsregler](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Hvordan man indlæser en færdighed, hvilken model en kendsgerning gælder for, og de partitioner, som ingen pakke skal skrive.Hardware

### [Y1 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, hjulet som nøglebegivenheder, 480x360 display, FM/lydstier, lagring og Type A/B partitionskortet.Hardware

### [Y2 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582-kort, enhedstræ, GC9503V/ST7701S-paneler, PMIC/DAC-skinner, skillevægge og boot-imaget.Firmware

### [Firmware-pakker](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomi, scatter-filer, klasse A-opdateringskontrakter og udgivelsestjeklisten.Temaer

### [Tema- og hudforfattelse](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json temaer, Rockbox WPS/SBS, Reborn skins og Y2Player skin format v2.Alle færdigheder

### [Gennemse færdighedsmappen](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, lager Android ROM'er, Y2Linux, Android apps, launchers, release notes og webstedsudgivelse.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
