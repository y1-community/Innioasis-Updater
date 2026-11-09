---
title: "Utvecklare | Lägg till anpassad firmware till Innioasis Updater CE - Innioasis Firmware-nedladdningar"
description: "Utvecklardokumentation för att lägga till en anpassad Innioasis Y1 eller Y2 firmware till Updater CE: dela arkivet, publicera rom.zip tillgångar, redigera slidia_manifest.xml, testa och öppna en pull-begäran."
language: "sv"
source: "https://innioasis.app/developers_sv.html"
---

# Utvecklare | Lägg till anpassad firmware till Innioasis Updater CE - Innioasis Firmware-nedladdningar

För firmware-utvecklare

# Lägg till din firmware till Updater CE.

Updater CE är gemenskapskatalogen och installationsprogrammet för anpassad firmware. Utveckla ditt projekt från en bas ROM, publicera det som ett offentligt arkiv med rätt utgivningstillgångar, lägg till modellposterna i `slidia_manifest.xml`, testa modellfiltren och öppna en pull-begäran. Ett arkiv kan tjäna alla modeller som det stöder.[Se Updater CE-källan](https://github.com/y1-community/Innioasis-Updater)[Bläddra bland nedladdningar av programvara](firmware_sv.html)

## Börja från en bas ROM

Bas-ROM ger utvecklare av anpassad firmware en ren Android-grund med de trådlösa radiochips aktiverade. På Y1 aktiverar de Wi-Fi och GPS tillsammans med fabriken Bluetooth och FM; på Y2 aktiverar de Wi-Fi, GPS och FM tillsammans med fabrikens Bluetooth.Bas ROM nedladdningar för anpassad firmwareutveckling, med Android-versionen och trådlösa funktioner som var och en möjliggör[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Ladda ner | Enhet | Android | Trådlösa funktioner |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Lägger till Wi-Fi och GPS till fabrikens Bluetooth och FM (FM fungerar redan på Y1 från fabriken). För Y1 spelare som levererades med OS 2.0.0 eller senare. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Lägger till Wi-Fi och GPS till fabrikens Bluetooth och FM (FM fungerar redan på Y1 från fabriken). För Y1 spelare som levererades med ett tidigare operativsystem än 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Lägger till Wi-Fi, GPS och FM till Bluetooth från fabriken. Radiochippet Y2 är fullt aktiverat, så FM är tillgängligt även här. |

Dessa bilder är standard Android-basen (AOSP) med enhetens trådlösa radioapparater aktiverade, så en anpassad firmware kan lägga till nätverksfunktioner istället för att ersätta radiostacken. De är den praktiska utgångspunkten för publiceringsstegen nedan.

## Använd dessa releasetillgångars namn

Filnamnet är en del av kompatibilitetssignalen. Håll namnen exakta och placera ZIP-filerna i projektets releasetillgångar, inte bara i arkivets källträd.Firmware ZIP-tillgångsnamn och enheter som stöds``````

| Tillgång | Enhet | Hårdvara | Mening |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 enheter som levererades med OS 2.0.0 eller senare. |
| rom_type_b.zip | Y1 | Type B | Y1 enheter som levererades med ett tidigare operativsystem än 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Fullinstallationspaketet Y2. Håll den åtskild från Y1 tillgångar. |
Byt inte namn på ett paket för att det ska passa en annan modell. Y1 och Y2 använder olika MediaTek plattformsfiler och blinkande konfiguration. Publicera paketet för den hårdvara som det faktiskt stöder.

## Hur anslutningen fungerar

Updater CE läser manifestet som sin katalog. Varje `<package>` linje berättar projektets namn, arkiv, modell och hanterare. När en användare väljer det projektet kontrollerar Updater förvarets publicerade utgåvor och letar efter en `rom*.zip` tillgång.

### Manifestera

Namner projektet och mappar det till en modell. Y1 och Y2 behöver separata rader, även när de delar ett arkiv.

### Publicerad release

Innehåller de installerade ZIP-tillgångarna. En enda version kan innehålla paketen Y1 Type A, Y1 Type B och Y2 tillsammans.

### Updater CE installation

Använder den valda modellen för att välja matchande paket och modellspecifik blinkningsbana. Användaren ska inte behöva gissa ett filnamn.

## Publicera ett projekt i fem steg
  - Dela upp Updater CE-förrådet. Skapa din egen gaffel av [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), klona sedan din gaffel lokalt.
  - Förbered ett offentligt firmwareförråd. Se till att förvaret är offentligt och att dess release innehåller rätt ZIP-tillgångar. Du kan lägga `rom.zip`, `rom_type_b.zip`, och `rom_y2.zip` på samma utgåva när de tillhör samma version.
  - Redigera manifestet. Öppna `slidia_manifest.xml` i roten på din Updater CE-gaffel. Lägg till en rad för varje modell som releasen stöder (Y1 och Y2 är det gemensamma paret). Den `repo` värdet är förvarets `owner/repository`; `url` är den offentliga projektsidan.
  - Testa katalogen. Kör Updater från den redigerade kassan. Välj Y1 och bekräfta att projektet visar Y1 tillgångar. Välj Y2 och bekräfta att det visar Y2-releasen. Kontrollera Type A och Type B separat när båda är publicerade.
  - Öppna en pull-begäran. Tryck på manifeständringen till din gaffel och öppna en pull-begäran mot uppströms Updater CE-förvaret. Inkludera projektlänken, modeller som stöds, releasetagg, tillgångsnamn och enheterna du testade.

## Skapa dina manifestlinjer

Fyll i arkivet och markera varje modell som versionen stöder. Generatorn skriver en `<package>` rad per modell och inkluderar bara de attribut du ställer in, så resultatet matchar det aktuella `slidia_manifest.xml` formatera. Varje attribut Updater CE läser är tillgängligt nedan — de valfria finns under Fler alternativ.Repository URLDet offentliga GitHub arkivet. Generatorn extraherar `owner/repository` från URL:en.Programvarans namnVisas i appen och sajtkatalogen.Projektets URLMänniskovänd sida för projektet eller dess versionskommentarer.VarumärkeAvmarkera detta för att använda modellens standardmärke. SR1, Q3, Q5 och Q3e är Timmkoo modeller.Enheter (en rad vardera)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAndra modellerFör en modell som inte är listad ovan. Kända modeller behåller sin katalogstavning.Flaggor`do_not_keep_data` — Erbjud aldrig Keep Data för denna firmwareByggd av originalprogramvara — tillägger `derivative="y1-community/y1-stock-rom"`

Keep Data erbjuds endast när den inkommande firmware och den installerade firmware är samma eller delar en `derivative` rot. Använd flaggan endast när användardata verkligen inte kan överföras.Fler alternativ: ikon, konstverk, releasetillgångar, efterinstallation och speglar

#### Ikon och konstverkIkon filVälj den bild du vill lägga till förvaret. Detta förhandsgranskar den och bygger dess råa URL; den laddar inte upp någonting.Ikonsökväg i förvaretSökväg till den engagerade bilden, i förhållande till förvarsroten.Ikon grenIkon URLEn direkt bild-URL. När den är tom använder appen utgåvans `updater.png` eller en genererad ikon.Förhandsgranskning av vald ikon

URL för ikon för mörkt lägeValfri ikon för mörkt tema. `image_dark` är ett accepterat alias.Lätt konstverk URLSekundärt konstverk, provat efter releasebilden och `icon`.URL för mörk konst

#### Släpp tillgångarSläpp tillgångens namnEtt namn för varje vald modell. Lämna tomt för användning `rom.zip` på Y1 och `rom_<model>.zip` någon annanstans.TillgångsmönsterGlob används när releasens blixtlås inte är namngivna `rom*.zip`.Type A tillgångGlob för paketet Y1 Type A när dess namn inte säger det.Type B tillgångGlob för paketet Y1 Type B när dess namn inte säger det.Minsta appversionDölj posten från äldre Updater CE-byggen.

#### Länkar, speglar och Keep Data-familjenSida efter installationÖppnas efter en lyckad installation.Andra sidan efter installationenValfritt andra steg för en flersidig installationsguide.Bärbara speglar med dragkedjaKommaseparerad `*-mirror` arkiv som bygger Portable Flashing Zip-paket.DerivatförrådDen firmware som den här versionen är byggd av. Relaterade firmware delar en datapartition, vilket är vad Keep Data kontrollerar.InfoförrådApp-repo vars utgåvor beskriver apparna i denna firmware. Den behöver också en sida efter installationen.APK arkivApprepo vars APK appen laddar ner och installerar efter firmware.

#### Katalog extramaterialSnigelStabil identifierare för länkar och sparade installationsposter. Modellen läggs till automatiskt när flera modeller väljs.Beskrivning`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Kopiera rader

Laddar det senaste manifestet...Förhandsgranska det senaste manifestet med dina rader tillagda

Generatorn hämtade strömmen `slidia_manifest.xml` från detta förråd och infogade dina genererade rader precis innan `</slidia>`.

En rad räcker inte för ett delat arkiv. Om raden Y2 saknas, kommer Y2 användare inte att få en modellmatchad post även när `rom_y2.zip` finns i projektets release. Detsamma gäller för alla andra modeller som din version stöder.

### Varje attribut som manifestet läser

Det här är attributen som nuvarande Updater CE-byggen förstår. Generatorn skriver bara de du fyller i; appen faller tillbaka till förnuftiga standardinställningar för resten.slidia_manifest.xml-paketattribut och deras betydelse``````````````````````````````````````````````````````````````````````````````````````````````

| Attribut | Behövs | Vad den gör |
| --- | --- | --- |
| name | Ja | Programvarunamnet visas i katalogen och på installationskorten. |
| repo | Ja | owner/repo. Appen läser förvarets GitHub utgåvor. |
| device | Ja | Målmodell, versaler (Y1, Y2, G1, Q3e, …). Behåll en post per modell. |
| url | Rekommenderas | Projektsida eller release notes öppnas från katalogen. |
| type, handler | Ja i praktiken | type="img" och handler="Custom Firmware". Andra typer och icke-firmwarehanterare hoppas över. |
| brand | Valfritt | Katalogmärke (Innioasis, Timmkoo). Empty använder modellens standardmärke. |
| package_name | Valfritt | Släpp tillgångens filnamn. Standard till rom.zip på Y1 och rom_<model>.zip på andra modeller. |
| asset_pattern | Valfritt | Skift-okänslig glob för releaser vars firmware zips inte är namngivna rom*.zip (till exempel my-firmware-*.zip). |
| type_a_asset, type_b_asset | Valfritt | Globs som identifierar zippen Y1 Type A och Type B när deras filnamn inte innehåller de vanliga markörerna. |
| icon | Valfritt | Logotyp URL. Används efter utgivningens egna updater.png / updater.jpg, och som reserv för varje utgåva. |
| icon_dark | Valfritt | Logotyp i mörkt tema. image_dark är ett accepterat alias. |
| image | Valfritt | Sekundärt ljuskonstverk, provat efter icon. |
| post_install, post_install2 | Valfritt | Sida(r) öppnas efter en lyckad installation. Den andra täcker en flerstegsguide. |
| portable_zips | Valfritt | Kommaseparerad *-mirror repor som publicerar färdiga bärbara paket. |
| derivative | Valfritt | Lagret som den fasta programvaran är byggd från. Firmware med samma derivatrot kan behålla användardata. |
| info_repo | Valfritt | Applager vars versioner beskriver vad den fasta programvaran distribuerar. Kräver post_install eller post_install2. |
| apk_repo | Valfritt | Applager vars APK appen installeras efter den fasta programvaran. |
| min_version | Valfritt | Dölj posten när Updater CE är äldre än den här versionen. |
| do_not_keep_data | Valfritt | true (även 1 / yes) blockerar Behåll data helt för denna firmware. |
| slug | Valfritt | Stabil identifierare för länkar och sparade installationsposter. Genereras från namn och modell när de är tomma. |
| description | Valfritt | Kort katalogbeskrivning. Det kan vara attributvärdet eller elementets text. |

Äldre namn läses fortfarande för kompatibilitet: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` och `image_dark`. Nya poster bör använda de nuvarande namnen ovan.

### Skicka in raderna som en pull-förfrågan
  - Kopiera de genererade raderna ovan. De matchar redan det senaste manifestformatet.
  - Redigera `slidia_manifest.xml` i förvaret. Använd redigeringslänken nedan; förvarsvärden skapar automatiskt en gaffel och en gren åt dig.
  - Klistra in raderna precis innan `</slidia>`, att behålla de befintliga posterna oförändrade.
  - Engagera sig för en ny filial (till exempel `add-your-firmware`), öppna sedan en pull-begäran mot Updater CE-förvaret.
  - I PR, inkludera projektlänken, modeller som stöds, releasetagg, tillgångsnamn och enheterna du testade.
[Redigera Updater CE-manifestet](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Se det senaste manifestet](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Behåll modellnamnen med versaler, använd den exakta webbadressen till ditt offentliga arkiv och behåll `type="img"` och `handler="Custom Firmware"` för en firmware-post.

## Gör releasen lätt att verifiera

Ge releasen en tydlig tagg och release note. Taggen är användbar för människor, men ZIP-tillgångsnamnen är vad Updater CE använder för att identifiera installationspaketen.

### Släpp checklista
  - Publicera utgåvan offentligt.
  - Bifoga ZIP-filerna som releasetillgångar.
  - Ange vilken modell som stöds och Type A eller Type B i anteckningarna.
  - Lista alla nödvändiga förberedelser eller kända gränser.

### En release, tre tillgångar

En delad version kan innehålla `rom.zip`, `rom_type_b.zip`, och `rom_y2.zip`. Updater klassificerar dem separat och väljer bland modell- och maskinvarufiltren.

### Bunta inte gissningar

Inkludera inte ett Y1-paket under filnamnet Y2 eller lägg till oprövad scatter-, preloader- eller partitionsdata bara för att få en tillgång att visas.

## Varför modellposterna spelar roll under blinkning

Manifestet är inte bara en nedladdningsmeny. Efter extraktion använder Updater CE den lösta modellen för att förbereda den matchande installationssökvägen. Y1 och Y2 har olika plattformsfiler, förladdare, scatter-konfiguration och enhetslayouter.
  - Y1: Uppdateraren förbereder Y1-sökvägen och använder enhetens namngivna partitioner när MTKClient används.
  - Y2: Uppdateraren förbereder Y2-sökvägen och använder Y2 MT6582-konfigurationen. Full återställning kan använda fysiska adresser från modellkorrekta spridningsdata.
  - Cross-Platform Support: Updater CE hanterar inbyggd flashning direkt över Windows, Linux och macOS (stöder både Intel och Apple Silicon Mac) utan extra blinkande verktyg.
Bidragsgivare bör tillhandahålla korrekta firmware-filer, inte flash-offset. Redigera inte spridningsadresser, förladdare, DA-filer eller partitionskommandon för att komma runt ett dåligt paket. Fixa releasetillgången och testa den avsedda modellen.

## Innan du begär en sammanslagning
  - Validera XML med en XML-tolkare. En saknad offert eller stängning `/>` kan dölja varje post efter den.
  - Starta uppdateringsprogrammet från din kassa så att det laddar det lokala manifestet innan fjärruppdateringen.
  - Kontrollera Y1 och Y2 oberoende av varandra. Bekräfta att projektet endast visas där dess paket stöds.
  - Kontrollera releaselistan för `rom.zip`, `rom_type_b.zip`, och `rom_y2.zip` som tillämpligt.
  - Testa själva installationen på den avsedda enheten, med en pålitlig USB datakabel och en återställningsplan för återgång till originalprogramvaran.
  - Förklara vad du testade i pull-begäran. Beskriv inte en oprövad modell som stöds.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

För en lokal kontroll, kör det kommandot från förvarets rot. Den verifierar endast XML-syntax; det bevisar inte att en utgåva innehåller giltig firmware eller att en enhet är säker att flasha.

## Användbara projektlänkar[Gaffeluppdatering CE](https://github.com/y1-community/Innioasis-Updater/fork)[Se manifestet](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Noteringar om gemenskapens bidrag](support_devs_sv.html)[Felsökning](troubleshooting_sv.html)

## Modding färdigheter för AI-agenter

Förvarets `skills/` katalogen är en källgrundad kunskapsbas för agenter som arbetar med Y1 och Y2 hårdvara, fast programvara, teman och appar. Varje färdighet namnger projektfilerna som deras anspråk kommer ifrån, så en agent kan kontrollera ett faktum innan du ändrar en enhet.Börja här

### [Färdighetsindex och säkerhetsregler](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Hur man laddar en färdighet, vilken modell ett faktum gäller, och de partitioner som inget paket ska skriva.Hårdvara

### [Y1 hårdvara](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, hjulet som nyckelhändelser, 480x360 skärm, FM/ljudbanor, lagring och partitionskartan Type A/B.Hårdvara

### [Y2 hårdvara](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582-kort, enhetsträd, GC9503V/ST7701S-paneler, PMIC/DAC-skenor, partitioner och startbilden.Firmware

### [Firmware-paket](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomi, scatter-filer, klass A-uppdateringskontrakt och releasechecklistan.teman

### [Tema- och hudförfattarskap](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json-teman, Rockbox WPS/SBS, Reborn skal och Y2Player skalformat v2.Alla färdigheter

### [Bläddra i färdighetsmappen](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, Android-ROM i lager, Y2Linux, Android-appar, startprogram, versionsinformation och webbplatspublicering.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
