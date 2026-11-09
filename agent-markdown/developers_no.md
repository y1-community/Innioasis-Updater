---
title: "Utviklere | Legg til tilpasset fastvare til Innioasis Updater CE - Innioasis fastvarenedlastinger"
description: "Utviklerdokumentasjon for å legge til en tilpasset Innioasis Y1 eller Y2 fastvare til Updater CE: Fork the repository, publiser rom.zip assets, rediger slidia_manifest.xml, test og åpne en pull request."
language: "no"
source: "https://innioasis.app/developers_no.html"
---

# Utviklere | Legg til tilpasset fastvare til Innioasis Updater CE - Innioasis fastvarenedlastinger

For fastvareutviklere

# Legg til fastvaren til Updater CE.

Updater CE er fellesskapskatalogen og installasjonsprogrammet for tilpasset fastvare. Utvikl prosjektet ditt fra en base ROM, publiser det som et offentlig depot med de riktige utgivelseselementene, legg til modelloppføringene i `slidia_manifest.xml`, test modellfiltrene og åpne en pull-forespørsel. Ett depot kan betjene hver modell den støtter.[Se Updater CE-kilden](https://github.com/y1-community/Innioasis-Updater)[Bla gjennom programvarenedlastinger](firmware_no.html)

## Start fra en base ROM

Base-ROM-er gir tilpassede fastvareutviklere et rent Android-grunnlag med de trådløse radiobrikkene aktivert. På Y1 aktiverer de Wi-Fi og GPS sammen med fabrikkens Bluetooth og FM; på Y2 aktiverer de Wi-Fi, GPS og FM sammen med fabrikkens Bluetooth.Base ROM nedlastinger for tilpasset fastvareutvikling, med Android-versjonen og trådløse funksjoner som hver muliggjør[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Last ned | Enhet | Android | Trådløse funksjoner |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Legger til Wi-Fi og GPS til fabrikkens Bluetooth og FM (FM fungerer allerede på Y1 fra fabrikken). For Y1 spillere som ble levert med OS 2.0.0 eller nyere. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Legger til Wi-Fi og GPS til fabrikkens Bluetooth og FM (FM fungerer allerede på Y1 fra fabrikken). For Y1 spillere som ble levert med et OS tidligere enn 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Legger til Wi-Fi, GPS og FM til fabrikkinstallert Bluetooth. Radiobrikken Y2 er fullt aktivert, så FM er også tilgjengelig her. |

Disse bildene er standard Android-base (AOSP) med enhetens trådløse radioer aktivert, slik at en tilpasset fastvare kan legge til nettverksfunksjoner i stedet for å erstatte radiostabelen. De er det praktiske utgangspunktet for publiseringstrinnene nedenfor.

## Bruk disse navnene på utgivelseselementer

Filnavnet er en del av kompatibilitetssignalet. Hold navnene nøyaktige og plasser ZIP-filene i prosjektets utgivelsesressurser, ikke bare i kildetreet for depotet.Firmware ZIP-aktivanavn og støttede enheter``````

| Eiendel | Enhet | Maskinvare | Mening |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 enheter som ble levert med OS 2.0.0 eller nyere. |
| rom_type_b.zip | Y1 | Type B | Y1 enheter som ble levert med et OS tidligere enn 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Y2 fullinstalleringspakken. Hold den atskilt fra Y1 eiendeler. |
Ikke gi nytt navn til en pakke for å få den til å passe til en annen modell. Y1 og Y2 bruker forskjellige MediaTek plattformfiler og blinkende konfigurasjon. Publiser pakken for maskinvaren den faktisk støtter.

## Hvordan tilkoblingen fungerer

Updater CE leser manifestet som sin katalog. Hver `<package>` linje forteller den prosjektnavnet, depotet, modellen og behandleren. Når en bruker velger det prosjektet, sjekker Updater depotets publiserte utgivelser og ser etter en `rom*.zip` eiendel.

### Manifest

Navngir prosjektet og tilordner det til en modell. Y1 og Y2 trenger separate linjer, selv når de deler et depot.

### Publisert utgivelse

Inneholder de installerbare ZIP-elementene. En enkelt utgivelse kan inneholde pakkene Y1 Type A, Y1 Type B, og Y2 sammen.

### Updater CE installering

Bruker den valgte modellen til å velge matchende pakke og modellspesifikk blinkbane. Brukeren skal ikke måtte gjette et filnavn.

## Publiser et prosjekt i fem trinn
  - Fork Updater CE-depotet. Lag din egen gaffel av [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), klone deretter gaffelen lokalt.
  - Forbered et offentlig fastvarelager. Sørg for at depotet er offentlig og at utgivelsen inneholder de riktige ZIP-elementene. Du kan sette `rom.zip`, `rom_type_b.zip`, og `rom_y2.zip` på samme utgivelse når de tilhører samme versjon.
  - Rediger manifestet. Åpne `slidia_manifest.xml` i roten av din Updater CE-gaffel. Legg til én linje for hver modell utgivelsen støtter (Y1 og Y2 er det vanlige paret). Den `repo` verdien er depotets `owner/repository`; `url` er den offentlige prosjektsiden.
  - Test katalogen. Kjør Updater fra den redigerte kassen. Velg Y1 og bekreft at prosjektet viser Y1 eiendeler. Velg Y2 og bekreft at det viser Y2-utgivelsen. Sjekk Type A og Type B separat når begge er publisert.
  - Åpne en pull-forespørsel. Skyv manifestendringen til gaffelen din og åpne en pull-forespørsel mot oppstrøms Updater CE-lageret. Inkluder prosjektkoblingen, støttede modeller, utgivelsesmerke, ressursnavn og enhetene du testet.

## Generer manifestlinjene dine

Fyll ut depotet og merk av for hver modell utgivelsen støtter. Generatoren skriver en `<package>` linje per modell og inkluderer kun attributtene du angir, slik at resultatet samsvarer med gjeldende `slidia_manifest.xml` format. Hvert attributt Updater CE leser er tilgjengelig nedenfor - de valgfrie er under Flere alternativer.Repository URLDet offentlige GitHub depotet. Generatoren trekker ut `owner/repository` fra URL-en.ProgramvarenavnVist i appen og nettstedskatalogen.Prosjekt-URLMenneskevendt side for prosjektet eller dets utgivelsesnotater.MerkeFjern dette for å bruke modellens standardmerke. SR1, Q3, Q5 og Q3e er Timmkoo modeller.Enheter (en linje hver)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAndre modellerFor en modell som ikke er oppført ovenfor. Kjente modeller beholder stavemåten i katalogen.Flagg`do_not_keep_data` — aldri tilby Keep Data for denne fastvarenBygget fra original programvare — legger til `derivative="y1-community/y1-stock-rom"`

Keep Data tilbys kun når den innkommende fastvaren og den installerte fastvaren er den samme eller deler en `derivative` rot. Bruk flagget kun når brukerdata virkelig ikke kan overføres.Flere alternativer: ikon, kunstverk, utgivelseselementer, etterinstallering og speil

#### Ikon og kunstverkIkon filVelg bildet du vil forplikte til depotet. Dette forhåndsviser den og bygger dens rå URL; den laster ikke opp noe.Ikonbane i depotetBanen til det forpliktede bildet, i forhold til depotroten.Ikon grenIkon URLEn direkte bilde-URL. Når den er tom, bruker appen utgivelsens `updater.png` eller et generert ikon.Forhåndsvisning av valgt ikon

Mørk modus-ikon URLValgfritt mørkt tema-ikon. `image_dark` er et akseptert alias.Lett kunstverk URLSekundært kunstverk, prøvd etter utgivelsesbildet og `icon`.URL til mørk kunst

#### Frigjør eiendelerUtgivelseselementnavnEtt navn for hver valgt modell. La stå tomt for bruk `rom.zip` på Y1 og `rom_<model>.zip` andre steder.EiendelsmønsterGlob brukes når utgivelsens glidelåser ikke er navngitt `rom*.zip`.Type A eiendelGlob for Y1 Type A-pakken når navnet ikke sier det.Type B eiendelGlob for Y1 Type B-pakken når navnet ikke sier det.Minimum appversjonSkjul oppføringen fra eldre Updater CE-bygg.

#### Lenker, speil og Keep Data-familieSiden etter installasjonÅpnet etter vellykket installasjon.Andre side etter installasjonValgfritt andre trinn for en flersidig oppsettveiledning.Bærbare glidelåsspeilKommaseparert `*-mirror` repositories som bygger Portable Flashing Zip-pakker.DerivatlagerFastvaren denne utgivelsen er bygget fra. Relaterte fastvare deler en datapartisjon, som er det Keep Data sjekker.InfolagerApp-repo hvis utgivelser beskriver appene i denne fastvaren. Den trenger også en side etter installasjon.APK depotApp-repo hvis APK appen laster ned og installerer etter fastvaren.

#### Katalog ekstrautstyrSneglStabil identifikator for koblinger og lagrede installasjonsposter. Modellen legges til automatisk når flere modeller velges.Beskrivelse`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Kopier linjer

Laster det siste manifestet …Forhåndsvis det siste manifestet med linjene dine lagt til

Generatoren hentet strømmen `slidia_manifest.xml` fra dette depotet og satte inn dine genererte linjer rett før `</slidia>`.

Én linje er ikke nok for et delt depot. Hvis Y2-linjen mangler, vil ikke Y2-brukere få en modelltilpasset oppføring selv når `rom_y2.zip` finnes i prosjektets utgivelse. Det samme gjelder for alle andre modeller utgivelsen din støtter.

### Hvert attributt manifestet leser

Dette er attributtene som nåværende Updater CE-bygg forstår. Generatoren skriver kun de du fyller inn; appen faller tilbake til fornuftige standardverdier for resten.slidia_manifest.xml-pakkeattributter og deres betydning``````````````````````````````````````````````````````````````````````````````````````````````

| Attributt | Trengs | Hva den gjør |
| --- | --- | --- |
| name | Ja | Programvarenavn vist i katalogen og på installasjonskort. |
| repo | Ja | owner/repo. Appen leser det depotets GitHub utgivelser. |
| device | Ja | Målmodell, store bokstaver (Y1, Y2, G1, Q3e, …). Behold én oppføring per modell. |
| url | Anbefalt | Prosjektside eller utgivelsesnotater åpnet fra katalogen. |
| type, handler | Ja i praksis | type="img" og handler="Custom Firmware". Andre typer og ikke-fastvarebehandlere hoppes over. |
| brand | Valgfritt | Katalog merke (Innioasis, Timmkoo). Empty bruker modellens standardmerke. |
| package_name | Valgfritt | Frigi filnavnet på ressursen. Standard til rom.zip på Y1 og rom_<model>.zip på andre modeller. |
| asset_pattern | Valgfritt | Glob som ikke skiller mellom store og små bokstaver for utgivelser hvis fastvare-zips ikke er navngitt rom*.zip (for eksempel my-firmware-*.zip). |
| type_a_asset, type_b_asset | Valgfritt | Globs som identifiserer zip-ene Y1 Type A og Type B når filnavnene deres ikke inneholder de vanlige markørene. |
| icon | Valgfritt | Logo URL. Brukt etter utgivelsens egen updater.png / updater.jpg, og som reserve for hver utgivelse. |
| icon_dark | Valgfritt | Logo med mørkt tema. image_dark er et akseptert alias. |
| image | Valgfritt | Sekundært lys kunstverk, prøvd etter icon. |
| post_install, post_install2 | Valgfritt | Siden(er) åpnet etter vellykket installasjon. Den andre dekker en flertrinnsguide. |
| portable_zips | Valgfritt | Kommaseparert *-mirror repos som publiserer klare til å kjøre bærbare pakker. |
| derivative | Valgfritt | Repository firmwaren er bygget fra. Fastvare med samme avledede rot kan beholde brukerdata. |
| info_repo | Valgfritt | Applager hvis utgivelser beskriver hva fastvaren distribuerer. Krever post_install eller post_install2. |
| apk_repo | Valgfritt | Applager hvis APK appen installeres etter fastvaren. |
| min_version | Valgfritt | Skjul oppføringen når Updater CE er eldre enn denne versjonen. |
| do_not_keep_data | Valgfritt | true (også 1 / yes) blokkerer Behold data fullstendig for denne fastvaren. |
| slug | Valgfritt | Stabil identifikator for koblinger og lagrede installasjonsposter. Generert fra navnet og modellen når den er tom. |
| description | Valgfritt | Kort katalogbeskrivelse. Det kan være attributtverdien eller elementets tekst. |

Eldre navn leses fortsatt for kompatibilitet: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` og `image_dark`. Nye oppføringer bør bruke de gjeldende navnene ovenfor.

### Send inn linjene som en pull-forespørsel
  - Kopier de genererte linjene ovenfor. De samsvarer allerede med det nyeste manifestformatet.
  - Rediger `slidia_manifest.xml` i depotet. Bruk redigeringslenken nedenfor; depotverten oppretter automatisk en gaffel og en gren for deg.
  - Lim inn linjene rett før `</slidia>`, holde de eksisterende oppføringene uendret.
  - Forplikte seg til en ny filial (for eksempel `add-your-firmware`), åpne deretter en pull-forespørsel mot Updater CE-depotet.
  - I PR, inkluderer prosjektkoblingen, støttede modeller, utgivelsestag, aktivanavn og enhetene du testet.
[Rediger Updater CE-manifestet](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Se siste manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Behold modellnavnene med store bokstaver, bruk den nøyaktige URL-en til det offentlige depotet ditt, og behold `type="img"` og `handler="Custom Firmware"` for en fastvareoppføring.

## Gjør utgivelsen enkel å verifisere

Gi utgivelsen en tydelig kode og utgivelsesnotat. Taggen er nyttig for folk, men ZIP-aktivanavnene er det Updater CE bruker for å identifisere installasjonspakkene.

### Slipp sjekkliste
  - Publiser utgivelsen offentlig.
  - Legg ved ZIP-filene som utgivelseselementer.
  - Oppgi den støttede modellen og Type A eller Type B i merknadene.
  - List opp eventuelle nødvendige forberedelser eller kjente grenser.

### En utgivelse, tre eiendeler

En delt utgivelse kan inneholde `rom.zip`, `rom_type_b.zip`, og `rom_y2.zip`. Updater klassifiserer dem separat og velger fra modell- og maskinvarefiltre.

### Ikke sett sammen gjetninger

Ikke inkluder en Y1-pakke under Y2-filnavnet, eller legg til ikke-testet scatter-, forhåndslaster- eller partisjonsdata bare for å få en ressurs til å vises.

## Hvorfor modelloppføringene betyr noe under blinking

Manifestet er ikke bare en nedlastingsmeny. Etter utvinning bruker Updater CE den løste modellen for å klargjøre den matchende installasjonsbanen. Y1 og Y2 har forskjellige plattformfiler, forhåndslastere, spredningskonfigurasjon og enhetsoppsett.
  - Y1: oppdateringsprogrammet forbereder Y1-banen og bruker enhetens navngitte partisjoner når MTKClient brukes.
  - Y2: oppdateringsprogrammet forbereder Y2-banen og bruker Y2 MT6582-konfigurasjonen. Full gjenoppretting kan bruke fysiske adresser fra modellriktige spredningsdata.
  - Støtte på tvers av plattformer: Updater CE håndterer native flashing direkte på tvers av Windows, Linux og macOS (støtter både Intel og Apple Silicon Macs) uten ekstra blinkende verktøy.
Bidragsytere bør oppgi korrekte fastvarefiler, ikke flash-forskyvninger. Ikke rediger scatter-adresser, forhåndslastere, DA-filer eller partisjonskommandoer for å omgå en dårlig pakke. Fiks utgivelseselementet og test på den tiltenkte modellen.

## Før du ber om en sammenslåing
  - Valider XML med en XML-parser. Et manglende tilbud eller avslutning `/>` kan skjule hver oppføring etter den.
  - Start oppdateringsprogrammet fra kassen slik at det laster det lokale manifestet før den eksterne oppdateringen.
  - Sjekk Y1 og Y2 uavhengig. Bekreft at prosjektet bare vises der pakken støttes.
  - Sjekk utgivelseslisten for `rom.zip`, `rom_type_b.zip`, og `rom_y2.zip` som aktuelt.
  - Test selve installasjonen på den tiltenkte enheten, med en pålitelig USB datakabel og en gjenopprettingsplan for retur til original programvare.
  - Forklar hva du testet i pull-forespørselen. Ikke beskriv en uprøvd modell som støttet.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

For en lokal sjekk, kjør den kommandoen fra depotroten. Den verifiserer kun XML-syntaks; det beviser ikke at en utgivelse inneholder gyldig fastvare eller at en enhet er trygg å flashe.

## Nyttige prosjektlenker[Gaffeloppdatering CE](https://github.com/y1-community/Innioasis-Updater/fork)[Se manifestet](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Notater om samfunnsbidrag](support_devs_no.html)[Feilsøking](troubleshooting_no.html)

## Moddingsferdigheter for AI-agenter

Depotets `skills/` katalogen er en kildebasert kunnskapsbase for agenter som jobber med Y1 og Y2 maskinvare, fastvare, temaer og apper. Hver ferdighet navngir prosjektfilene kravene kommer fra, slik at en agent kan sjekke et faktum før du endrer en enhet.Start her

### [Ferdighetsindeks og sikkerhetsregler](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Hvordan laste en ferdighet, hvilken modell et faktum gjelder for, og partisjonene som ingen pakke skal skrive.Maskinvare

### [Y1 maskinvare](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, hjulet som nøkkelhendelser, 480x360 skjerm, FM/lydbaner, lagring og partisjonskartet Type A/B.Maskinvare

### [Y2 maskinvare](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582-kort, enhetstre, GC9503V/ST7701S-paneler, PMIC/DAC-skinner, partisjoner og oppstartsbildet.Fastvare

### [Firmware-pakker](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomi, scatter-filer, klasse A-oppdateringskontrakter og utgivelsessjekklisten.Temaer

### [Tema- og hudforfatting](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json-temaer, Rockbox WPS/SBS, Reborn skins og Y2Player skin format v2.Alle ferdigheter

### [Bla gjennom ferdighetsmappen](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, lager Android-ROM, Y2Linux, Android-apper, lanseringer, utgivelsesnotater og nettstedspublisering.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
