---
title: "Kehittäjät | Lisää mukautettu laiteohjelmisto Innioasis Updater CE:hen - Innioasis Firmware Downloads"
description: "Kehittäjädokumentaatio mukautetun Innioasis Y1- tai Y2-laiteohjelmiston lisäämiseksi Updater CE:hen: haaroittele arkisto, julkaise rom.zip resurssit, muokkaa slidia_manifest.xml-tiedostoa, testaa ja avaa vetopyyntö."
language: "fi"
source: "https://innioasis.app/developers_fi.html"
---

# Kehittäjät | Lisää mukautettu laiteohjelmisto Innioasis Updater CE:hen - Innioasis Firmware Downloads

Laiteohjelmistokehittäjille

# Lisää laiteohjelmisto Updater CE:hen.

Updater CE on mukautetun laiteohjelmiston yhteisön luettelo ja asennusohjelma. Kehitä projektisi alustasta ROM, julkaise se julkisena tietovarastona oikeilla julkaisuresursseilla, lisää mallimerkinnät `slidia_manifest.xml`, testaa mallisuodattimet ja avaa vetopyyntö. Yksi arkisto voi palvella jokaista tukemaansa mallia.[Katso Updater CE -lähde](https://github.com/y1-community/Innioasis-Updater)[Selaa ohjelmistolatauksia](firmware_fi.html)

## Aloita alustasta ROM

PerusROM-levyt antavat mukautetuille laiteohjelmistokehittäjille puhtaan Android-perustan langattoman radiosirun ollessa käytössä. Y1:ssa ne mahdollistavat Wi-Fi:n ja GPS:n tehtaan Bluetoothin ja FM:n rinnalla; Y2:ssa ne mahdollistavat Wi-Fin, GPS:n ja FM:n tehdas Bluetoothin rinnalla.Peruslataukset ROM mukautetun laiteohjelmiston kehittämiseen, joissa Android-versio ja langattomat ominaisuudet ovat kukin mahdollistavat[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Lataa | Laite | Android | Langattomat ominaisuudet |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Lisää Wi-Fin ja GPS:n tehdasasetuksiin Bluetoothin ja FM:n kanssa (FM toimii jo tehtaalla Y1:ssa). Y1 pelaajille, joiden mukana toimitettiin OS 2.0.0 tai uudempi. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Lisää Wi-Fin ja GPS:n tehdasasetuksiin Bluetoothin ja FM:n kanssa (FM toimii jo tehtaalla Y1:ssa). Y1 pelaajille, joiden käyttöjärjestelmä on vanhempi kuin 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Lisää Wi-Fin, GPS:n ja FM:n tehtaan Bluetoothiin. Y2 radiosiru on täysin käytössä, joten FM on saatavilla myös täällä. |

Nämä kuvat ovat Android-pohjaisia ​​(AOSP) -laitteita, joissa laitteen langattomat radiot ovat käytössä, joten mukautettu laiteohjelmisto voi lisätä verkkoominaisuuksia radiopinon korvaamisen sijaan. Ne ovat käytännön lähtökohta alla oleville julkaisuvaiheille.

## Käytä näitä julkaisukohteiden nimiä

Tiedostonimi on osa yhteensopivuussignaalia. Pidä nimet tarkasti ja laita ZIP-tiedostot projektin julkaisuresursseihin, ei vain arkiston lähdepuuhun.Firmware ZIP-resurssien nimet ja tuetut laitteet``````

| Omaisuus | Laite | Laitteisto | Merkitys |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 laitteita, joiden mukana toimitettiin OS 2.0.0 tai uudempi. |
| rom_type_b.zip | Y1 | Type B | Y1 laitteita, joiden käyttöjärjestelmä on vanhempi kuin 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Täysi asennuspaketti Y2. Pidä se erillään Y1 sisällöstä. |
Älä nimeä pakettia uudelleen, jotta se sopisi toiseen malliin. Y1 ja Y2 käyttävät erilaisia ​​MediaTek alustatiedostoja ja vilkkuvia määrityksiä. Julkaise paketti sille laitteistolle, jota se todella tukee.

## Miten yhteys toimii

Updater CE lukee manifestin luettelokseen. Jokainen `<package>` rivi kertoo projektin nimen, arkiston, mallin ja käsittelijän. Kun käyttäjä valitsee kyseisen projektin, Updater tarkistaa arkiston julkaistut julkaisut ja etsii a `rom*.zip` omaisuus.

### Selvä

Nimeää projektin ja kartoittaa sen malliksi. Y1 ja Y2 tarvitsevat erilliset rivit, vaikka niillä olisi yhteinen tietovarasto.

### Julkaistu julkaisu

Sisältää asennettavat ZIP-materiaalit. Yksi julkaisu voi sisältää paketit Y1 Type A, Y1 Type B ja Y2 yhdessä.

### Updater CE asennus

Käyttää valittua mallia valitsemaan vastaavan paketin ja mallikohtaisen vilkkupolun. Käyttäjän ei pitäisi joutua arvaamaan tiedostonimeä.

## Julkaise projekti viidessä vaiheessa
  - Haarukka Updater CE -arkisto. Luo oma haarukkasi [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), kloonaa sitten haarukkasi paikallisesti.
  - Valmistele julkinen laiteohjelmistovarasto. Varmista, että arkisto on julkinen ja että sen julkaisu sisältää oikeat ZIP-sisällöt. Voit laittaa `rom.zip`, `rom_type_b.zip`, ja `rom_y2.zip` samassa julkaisussa, kun ne kuuluvat samaan versioon.
  - Muokkaa luetteloa. Avaa `slidia_manifest.xml` Updater CE -haarukan juuressa. Lisää yksi rivi jokaiselle mallille, jota julkaisu tukee (Y1 ja Y2 ovat yhteinen pari). The `repo` arvo on arkiston `owner/repository`; `url` on projektin julkinen sivu.
  - Testaa luetteloa. Suorita Updater muokatusta kassalta. Valitse Y1 ja vahvista, että projekti näyttää Y1 resurssit. Valitse Y2 ja vahvista, että se näyttää Y2-vapautuksen. Tarkista Type A ja Type B erikseen, kun molemmat on julkaistu.
  - Avaa vetopyyntö. Työnnä luettelomuutos haarukkaan ja avaa vetopyyntö ylävirran Updater CE -tietovarastoa vastaan. Liitä mukaan projektilinkki, tuetut mallit, julkaisutunniste, resurssien nimet ja testaamasi laitteet.

## Luo manifestirivit

Täytä arkisto ja valitse jokainen malli, jota julkaisu tukee. Generaattori kirjoittaa yhden `<package>` riviä mallia kohti ja sisältää vain asettamasi attribuutit, joten tulos vastaa nykyistä `slidia_manifest.xml` muoto. Jokainen Updater CE:n lukema attribuutti on saatavilla alla – valinnaiset ovat alla Lisää vaihtoehtoja.Tietovaraston URL-osoiteJulkinen GitHub arkisto. Generaattori purkaa `owner/repository` URL-osoitteesta.Ohjelmiston nimiNäkyy sovelluksessa ja sivustoluettelossa.Projektin URL-osoiteIhmisille suunnattu sivu projektille tai sen julkaisutiedotteille.TuotemerkkiPoista tämä, jos haluat käyttää mallin oletusmerkkiä. SR1, Q3, Q5 ja Q3e ovat Timmkoo malleja.Laitteet (yksi rivi kukin)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eMuut mallitMallille, jota ei ole mainittu yllä. Tunnetut mallit säilyttävät luettelonsa oikeinkirjoituksen.Liput`do_not_keep_data` – Älä koskaan tarjoa Keep Dataa tälle laiteohjelmistolleRakennettu alkuperäisestä ohjelmistosta - lisää `derivative="y1-community/y1-stock-rom"`

Keep Data on tarjolla vain, kun saapuva laiteohjelmisto ja asennettu laiteohjelmisto ovat samat tai jakavat a `derivative` juuri. Käytä lippua vain, kun käyttäjätietoja ei todellakaan voi siirtää.Lisää vaihtoehtoja: kuvake, kuvitus, julkaisumateriaali, asennuksen jälkeen ja peilit

#### Ikoni ja taideteosIkonitiedostoValitse kuva, jonka siirrät arkistoon. Tämä esikatselee sitä ja muodostaa sen raaka-URL-osoitteen; se ei lataa mitään.Kuvakepolku arkistossaPolku sitoutuneeseen kuvaan suhteessa arkiston juureen.Ikoni haaraKuvakkeen URL-osoiteSuora kuvan URL-osoite. Kun sovellus on tyhjä, se käyttää julkaisua `updater.png` tai luotu kuvake.Valitun kuvakkeen esikatselu

Tumman tilan kuvakkeen URL-osoiteValinnainen tumman teeman kuvake. `image_dark` on hyväksytty alias.Kevyen taiteen URL-osoiteToissijainen taideteos, kokeiltu julkaisun jälkeen kuva ja `icon`.Tumman kuvituksen URL-osoite

#### Vapauta omaisuusVapauta sisällön nimiYksi nimi jokaiselle valitulle mallille. Jätä tyhjäksi käytettäväksi `rom.zip` Y1 ja `rom_<model>.zip` muualla.KohdekuvioGlobia käytetään, kun julkaisun vetoketjuja ei ole nimetty `rom*.zip`.Type A omaisuusGlobaali paketille Y1 Type A, kun sen nimi ei sano niin.Type B omaisuusGlobaali paketille Y1 Type B, kun sen nimi ei sano niin.Sovelluksen vähimmäisversioPiilota merkintä vanhemmista Updater CE -versioista.

#### Linkit, peilit ja Keep Data -perheAsennuksen jälkeinen sivuAvattu onnistuneen asennuksen jälkeen.Toinen asennuksen jälkeinen sivuValinnainen toinen vaihe monisivuiselle asennusoppaalle.Kannettavat vetoketjulliset peilitPilkuilla erotettuna `*-mirror` arkistot, jotka rakentavat kannettavia Flashing Zip -paketteja.JohdannaisvarastoLaiteohjelmisto, josta tämä julkaisu on rakennettu. Aiheeseen liittyvät laiteohjelmistot jakavat tietoosion, jonka Keep Data tarkistaa.TietovarastoSovellusvarasto, jonka julkaisut kuvaavat tämän laiteohjelmiston sovelluksia. Se tarvitsee myös asennuksen jälkeisen sivun.APK arkistoSovellusrepo, jonka APK sovellus lataa ja asentaa laiteohjelmiston jälkeen.

#### Katalogin lisäosatEtanaLinkkien ja tallennettujen asennustietueiden vakaa tunniste. Malli liitetään automaattisesti, kun useita malleja valitaan.Kuvaus`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Kopioi rivit

Ladataan viimeisintä luetteloa…Esikatsele viimeisintä luetteloa, johon on lisätty rivit

Generaattori haki virran `slidia_manifest.xml` tästä arkistosta ja lisäsi luodut rivisi juuri ennen `</slidia>`.

Yksi rivi ei riitä jaettuun arkistoon. Jos rivi Y2 puuttuu, Y2-käyttäjät eivät saa mallivastaavaa merkintää, vaikka `rom_y2.zip` on olemassa projektin julkaisussa. Sama pätee kaikkiin muihin julkaisusi tukemiin malleihin.

### Jokainen luettelon attribuutti lukee

Nämä ovat attribuutit, jotka nykyiset Updater CE:n koontiversiot ymmärtävät. Generaattori kirjoittaa vain ne, jotka täytät; sovellus palaa järkeviin oletusasetuksiin muilta osin.slidia_manifest.xml-paketin attribuutit ja niiden merkitys``````````````````````````````````````````````````````````````````````````````````````````````

| Attribuutti | Tarvitaan | Mitä se tekee |
| --- | --- | --- |
| name | Kyllä | Ohjelmiston nimi luettelossa ja asennuskorteissa. |
| repo | Kyllä | owner/repo. Sovellus lukee kyseisen arkiston GitHub julkaisut. |
| device | Kyllä | Kohdemalli, isot kirjaimet (Y1, Y2, G1, Q3e, …). Säilytä yksi merkintä mallia kohti. |
| url | Suositeltava | Projektisivu tai julkaisutiedot avattu luettelosta. |
| type, handler | Kyllä käytännössä | type="img" ja handler="Custom Firmware". Muut tyypit ja muut kuin laiteohjelmiston käsittelijät ohitetaan. |
| brand | Valinnainen | Tuotemerkki (Innioasis, Timmkoo). Tyhjä käyttää mallin oletusmerkkiä. |
| package_name | Valinnainen | Vapauta sisällön tiedostonimi. Oletuksena rom.zip Y1 ja rom_<model>.zip muissa malleissa. |
| asset_pattern | Valinnainen | Kirjainkoolla ei ole merkitystä julkaisuille, joiden laiteohjelmiston zip-tiedostoja ei ole nimetty rom*.zip (esimerkiksi my-firmware-*.zip). |
| type_a_asset, type_b_asset | Valinnainen | Maapallot, jotka tunnistavat Y1 Type A ja Type B zipsin, kun niiden tiedostonimet eivät sisällä tavallisia merkkejä. |
| icon | Valinnainen | Logon URL-osoite. Käytetty oman julkaisun jälkeen updater.png / updater.jpg, ja jokaisen julkaisun varavaihtoehtona. |
| icon_dark | Valinnainen | Tumman teeman logo. image_dark on hyväksytty alias. |
| image | Valinnainen | Toissijainen valotaide, kokeiltu jälkeenpäin icon. |
| post_install, post_install2 | Valinnainen | Sivu(t) avattu onnistuneen asennuksen jälkeen. Toinen kattaa monivaiheisen oppaan. |
| portable_zips | Valinnainen | Pilkuilla erotettuna *-mirror repot, jotka julkaisevat valmiita kannettavia paketteja. |
| derivative | Valinnainen | Arkisto, josta laiteohjelmisto on rakennettu. Laiteohjelmisto, jolla on sama johdannaisjuuri, voi säilyttää käyttäjätiedot. |
| info_repo | Valinnainen | Sovellusarkisto, jonka julkaisut kuvaavat, mitä laiteohjelmisto ottaa käyttöön. Vaatii post_install tai post_install2. |
| apk_repo | Valinnainen | Sovellusarkisto, jonka APK sovellus asentaa laiteohjelmiston jälkeen. |
| min_version | Valinnainen | Piilota merkintä, kun Updater CE on tätä versiota vanhempi. |
| do_not_keep_data | Valinnainen | true (myös 1 / yes) estää tämän laiteohjelmiston tietojen säilyttämisen kokonaan. |
| slug | Valinnainen | Linkkien ja tallennettujen asennustietueiden vakaa tunniste. Luodaan nimestä ja mallista tyhjänä. |
| description | Valinnainen | Lyhyt luettelokuvaus. Se voi olla attribuutin arvo tai elementin teksti. |

Vanhat nimet luetaan edelleen yhteensopivuuden vuoksi: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` ja `image_dark`. Uusien merkintöjen tulee käyttää yllä olevia nykyisiä nimiä.

### Lähetä rivit vetopyyntönä
  - Kopioi yllä luodut rivit. Ne vastaavat jo viimeisintä luettelomuotoa.
  - Muokkaa `slidia_manifest.xml` arkistossa. Käytä alla olevaa muokkauslinkkiä; arkiston isäntä luo haarukan ja haaran sinulle automaattisesti.
  - Liitä rivit juuri ennen `</slidia>`, pitää nykyiset merkinnät ennallaan.
  - Sitoudu uuteen haaraan (esimerkiksi `add-your-firmware`), avaa sitten noutopyyntö Updater CE -tietovarastoa vastaan.
  - Sisällytä PR:ään projektilinkki, tuetut mallit, julkaisutunniste, resurssien nimet ja testaamasi laitteet.
[Muokkaa Updater CE -luetteloa](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Katso uusin manifesti](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Pidä mallien nimet isoilla kirjaimilla, käytä julkisen arkistosi tarkkaa URL-osoitetta ja säilytä `type="img"` ja `handler="Custom Firmware"` laiteohjelmiston merkintää varten.

## Tee julkaisusta helppo tarkistaa

Anna julkaisulle selkeä tunniste ja julkaisuilmoitus. Tunniste on hyödyllinen ihmisille, mutta ZIP-resurssien nimiä Updater CE käyttää asennuspakettien tunnistamiseen.

### Vapauta tarkistuslista
  - Julkaise julkaisu julkisesti.
  - Liitä ZIP-tiedostot julkaisuresursseina.
  - Ilmoita tuettu malli ja Type A tai Type B huomautuksissa.
  - Luettele kaikki vaaditut valmisteet tai tunnetut rajat.

### Yksi julkaisu, kolme omaisuutta

Jaettu julkaisu voi sisältää `rom.zip`, `rom_type_b.zip`, ja `rom_y2.zip`. Updater luokittelee ne erikseen ja valitsee malli- ja laitteistosuodattimista.

### Älä niputa arvauksia

Älä sisällytä Y1-pakettia Y2-tiedostonimen alle tai lisää testaamattomia haja-, esilataus- tai osiotietoja vain saadaksesi resurssin näkyviin.

## Miksi mallimerkinnöillä on merkitystä vilkkumisen aikana

Luettelo ei ole vain latausvalikko. Purkamisen jälkeen Updater CE käyttää ratkaistua mallia vastaavan asennuspolun valmistelemiseen. Y1:lla ja Y2:lla on erilaiset alustatiedostot, esilataajat, hajontakonfiguraatiot ja laiteasettelut.
  - Y1: päivitysohjelma valmistelee Y1-polun ja käyttää laitteen nimettyjä osioita, kun MTKClient on käytössä.
  - Y2: päivitysohjelma valmistelee Y2-polun ja käyttää Y2 MT6582-kokoonpanoa. Täysi palautus voi käyttää fyysisiä osoitteita mallinmukaisista sirontatiedoista.
  - Monialustainen tuki: Updater CE käsittelee alkuperäisen flash-toiminnon suoraan Windowsissa, Linuxissa ja macOS:ssä (tukee sekä Intel- että Apple Silicon Mac -tietokoneita) ilman ylimääräisiä flash-työkaluja.
Osallistujien tulee toimittaa oikeat laiteohjelmistotiedostot, ei flash-offsetit. Älä muokkaa haja-osoitteita, esilataajia, DA-tiedostoja tai osiokomentoja kiertääksesi huonon paketin. Korjaa vapautusväline ja testaa aiotulla mallilla.

## Ennen kuin pyydät yhdistämistä
  - Vahvista XML XML-jäsentimillä. Puuttuva lainaus tai sulkeminen `/>` voi piilottaa jokaisen merkinnän sen jälkeen.
  - Käynnistä päivitysohjelma kassalta, jotta se lataa paikallisen luettelon ennen etäpäivitystä.
  - Tarkista Y1 ja Y2 erikseen. Varmista, että projekti näkyy vain siellä, missä sen pakettia tuetaan.
  - Tarkista julkaisuluettelo `rom.zip`, `rom_type_b.zip`, ja `rom_y2.zip` soveltuvin osin.
  - Testaa varsinaista asennusta tarkoitetulle laitteelle luotettavalla USB-datakaapelilla ja palautussuunnitelmalla alkuperäiseen ohjelmistoon paluuta varten.
  - Selitä vetopyynnössä, mitä testasit. Älä kuvaile testaamatonta mallia tuetuksi.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Paikallista tarkistusta varten suorita kyseinen komento arkiston juuresta. Se vahvistaa vain XML-syntaksin; se ei todista, että julkaisu sisältää kelvollisen laiteohjelmiston tai että laite on turvallinen flash-muistiin.

## Hyödyllisiä linkkejä projekteihin[Fork Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Katso manifesti](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[huomautukset yhteisön rahoitusosuudesta](support_devs_fi.html)[Vianetsintä](troubleshooting_fi.html)

## Tekoälyagenttien taitojen muokkaaminen

Arkiston `skills/` hakemisto on lähdepohjainen tietokanta agenteille, jotka työskentelevät Y1- ja Y2-laitteistojen, laiteohjelmistojen, teemojen ja sovellusten parissa. Jokainen taito nimeää projektitiedostot, joista sen väitteet tulevat, joten agentti voi tarkistaa tosiasian ennen laitteen vaihtamista.Aloita tästä

### [Taitoindeksi ja turvallisuussäännöt](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Kuinka ladata taito, mitä mallia fakta koskee ja osiot, joita paketin ei pitäisi kirjoittaa.Laitteisto

### [Y1 laitteisto](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, pyörä keskeisinä tapahtumina, 480 x 360 näyttö, FM/äänipolut, tallennustila ja Type A/B-osiokartta.Laitteisto

### [Y2 laitteisto](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582-kortti, laitepuu, GC9503V/ST7701S-paneelit, PMIC/DAC-kiskot, osiot ja käynnistyskuva.Laiteohjelmisto

### [Laiteohjelmistopaketit](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomia, scatter-tiedostot, luokan A päivityssopimukset ja julkaisun tarkistuslista.Teemat

### [Teeman ja ihon kirjoittaminen](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json-teemat, Rockbox WPS/SBS, Reborn skinit ja Y2Player skin-muoto v2.Kaikki taidot

### [Selaa osaamiskansiota](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, varastossa olevat Android-ROM-levyt, Y2Linux, Android-sovellukset, käynnistysohjelmat, julkaisutiedot ja sivuston julkaisu.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
