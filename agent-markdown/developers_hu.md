---
title: "Fejlesztők | Adjon hozzá egyéni firmware-t a Innioasis Updater CE-hez – Innioasis Firmware letöltések"
description: "Fejlesztői dokumentáció egyéni Innioasis Y1 vagy Y2 firmware hozzáadásához az Updater CE-hez: forgassa el a tárat, tegye közzé rom.zip eszközöket, szerkessze a slidia_manifest.xml fájlt, tesztelje és nyissa meg a lekérést."
language: "hu"
source: "https://innioasis.app/developers_hu.html"
---

# Fejlesztők | Adjon hozzá egyéni firmware-t a Innioasis Updater CE-hez – Innioasis Firmware letöltések

Firmware fejlesztőknek

# Adja hozzá firmware-jét az Updater CE-hez.

Az Updater CE az egyéni firmware közösségi katalógusa és telepítője. Fejlessze projektjét ROM alapból, tegye közzé nyilvános adattárként a megfelelő kiadási eszközökkel, adja hozzá a modellbejegyzéseket a `slidia_manifest.xml`, tesztelje a modellszűrőket, és nyissa meg a lehívási kérelmet. Egy adattár kiszolgálhat minden általa támogatott modellt.[Tekintse meg az Updater CE forrását](https://github.com/y1-community/Innioasis-Updater)[Böngésszen a szoftverletöltések között](firmware_hu.html)

## Kezdje egy alapról ROM

Az alap ROM-ok az egyéni firmware-fejlesztőknek tiszta Android-alapot biztosítanak a vezeték nélküli rádióchipek engedélyezésével. A Y1-on engedélyezik a Wi-Fi-t és a GPS-t a gyári Bluetooth és FM mellett; a Y2-on a gyári Bluetooth mellett engedélyezik a Wi-Fi-t, a GPS-t és az FM-et.Az egyéni firmware-fejlesztéshez szükséges alapletöltések ROM Android-verziója és a vezeték nélküli funkciók mindegyike lehetővé teszi[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Letöltés | Eszköz | Android | Vezeték nélküli funkciók |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Hozzáadja a Wi-Fi-t és a GPS-t a gyári Bluetooth-hoz és FM-hez (az FM gyárilag működik a Y1-on). Az OS 2.0.0 vagy újabb verzióval szállított Y1 lejátszókhoz. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Hozzáadja a Wi-Fi-t és a GPS-t a gyári Bluetooth-hoz és FM-hez (az FM gyárilag működik a Y1-on). Y1 lejátszókhoz, amelyeket 2.0.0-nál korábbi operációs rendszerrel szállítottak. |
| rom_y2.zip | Y2 | Android 4.4.2 | Hozzáadja a Wi-Fi-t, a GPS-t és az FM-et a gyári Bluetooth-hoz. A Y2 rádióchip teljesen engedélyezett, így az FM itt is elérhető. |

Ezek a képek az Android alapja (AOSP), amelyen az eszköz vezeték nélküli rádiói is engedélyezettek, így az egyéni firmware a rádióverem cseréje helyett hálózati funkciókat adhat hozzá. Ezek jelentik az alábbi közzétételi lépések gyakorlati kiindulópontját.

## Használja ezeket a kiadási elemneveket

A fájlnév a kompatibilitási jel része. Tartsa pontosan a neveket, és helyezze el a ZIP-fájlokat a projekt kiadási eszközei között, ne csak a lerakat forrásfájában.Firmware ZIP eszköznevek és támogatott eszközök``````

| Eszköz | Eszköz | Hardver | Jelentése |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 olyan eszközök, amelyeket OS 2.0.0 vagy újabb verzióval szállítottak. |
| rom_type_b.zip | Y1 | Type B | Y1 olyan eszköz, amelyet 2.0.0-nál korábbi operációs rendszerrel szállítottak. |
| rom_y2.zip | Y2 | Y2 | A Y2 teljes telepítési csomag. Tartsa elkülönítve Y1 eszközöktől. |
Ne nevezzen át egy csomagot, hogy egy másik modellhez illeszkedjen. A Y1 és a Y2 különböző MediaTek platformfájlokat és villogó konfigurációt használ. Tegye közzé a ténylegesen támogatott hardver csomagját.

## Hogyan működik a kapcsolat

Az Updater CE a jegyzéket katalógusaként olvassa be. Mindegyik `<package>` sor közli vele a projekt nevét, tárolóját, modelljét és kezelőjét. Amikor egy felhasználó ezt a projektet választja, az Updater ellenőrzi a lerakat közzétett kiadásait, és megkeresi a `rom*.zip` eszköz.

### Nyilvánvaló

Elnevezi a projektet, és leképezi egy modellre. A Y1-nak és Y2-nek külön sorra van szüksége, még akkor is, ha egy adattáron osztoznak.

### Megjelent kiadás

Tartalmazza a telepíthető ZIP eszközöket. Egyetlen kiadás tartalmazhatja a Y1 Type A, Y1 Type B és Y2 csomagokat együtt.

### Frissítő CE telepítés

A kiválasztott modellt használja a megfelelő csomag és a modellspecifikus villogási útvonal kiválasztásához. A felhasználónak nem kell fájlnevet kitalálnia.

## Tegyen közzé egy projektet öt lépésben
  - Forgassa el az Updater CE adattárat. Készítse el saját villáját [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), majd klónozzuk helyileg a villát.
  - Készítsen nyilvános firmware-tárat. Győződjön meg arról, hogy a tár nyilvános, és a kiadása tartalmazza a megfelelő ZIP-elemeket. Felteheted `rom.zip`, `rom_type_b.zip`, és `rom_y2.zip` ugyanazon a kiadáson, ha ugyanahhoz a verzióhoz tartoznak.
  - Szerkessze a jegyzéket. Nyissa meg `slidia_manifest.xml` az Updater CE villájának gyökerében. Adjon hozzá egy sort minden egyes modellhez, amelyet a kiadás támogat (Y1 és Y2 a közös pár). A `repo` az érték az adattáré `owner/repository`; `url` a projekt nyilvános oldala.
  - Tesztelje a katalógust. Futtassa az Updater programot a szerkesztett pénztárból. Válassza a Y1 lehetőséget, és ellenőrizze, hogy a projekt megjeleníti az Y1 eszközöket. Válassza a Y2 lehetőséget, és erősítse meg, hogy megjelenik a Y2 kiadás. Ha mindkettő megjelent, ellenőrizze külön a Type A-et és a Type B-ot.
  - Nyisson meg egy lehívási kérelmet. Tolja el a jegyzékmódosítást a villájára, és nyissa meg a lekérési kérelmet az upstream Updater CE-lerakatára vonatkozóan. Adja meg a projekt hivatkozását, a támogatott modelleket, a kiadási címkét, az eszközneveket és a tesztelt eszközöket.

## Készítse elő manifeszt sorait

Töltse ki a tárat, és jelölje be a kiadás által támogatott minden modellt. A generátor ír egyet `<package>` sort modellenként, és csak az Ön által beállított attribútumokat tartalmazza, így az eredmény megegyezik az aktuális értékkel `slidia_manifest.xml` formátum. Az Updater CE által beolvasott összes attribútum elérhető alább – az opcionálisak alatt találhatók További lehetőségek.Adattár URL-jeA nyilvános GitHub adattár. A generátor kivonat `owner/repository` az URL-ből.SzoftvernévMegjelenik az alkalmazásban és a webhely katalógusában.Projekt URLEmberekre néző oldal a projekthez vagy a kiadási megjegyzésekhez.MárkaTörölje ezt a modell alapértelmezett márkájának használatához. SR1, Q3, Q5 és Q3e Timmkoo modellek.Eszközök (egy-egy sor)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eEgyéb modellekA fenti listán nem szereplő modellhez. Az ismert modellek megtartják katalógusuk helyesírását.Zászlók`do_not_keep_data` – soha ne kínáljon Keep Datat ehhez a firmware-hezEredeti szoftverből épült – teszi hozzá `derivative="y1-community/y1-stock-rom"`

A Keep Data szolgáltatást csak akkor ajánljuk fel, ha a bejövő firmware és a telepített firmware megegyezik, vagy megosztja a `derivative` gyökér. Csak akkor használja a jelzőt, ha a felhasználói adatok valóban nem vihetők át.További lehetőségek: ikon, grafika, kiadási eszközök, telepítés utáni és tükrök

#### Ikon és műalkotásIkon fájlVálassza ki azt a képet, amelyet az adattárba helyez. Ez megtekinti az előnézetet, és létrehozza a nyers URL-t; nem tölt fel semmit.Ikon elérési útja az adattárbanA véglegesített kép elérési útja a tároló gyökérhez viszonyítva.Ikon ágIkon URLA kép közvetlen URL-je. Ha üres, az alkalmazás a kiadást használja `updater.png` vagy egy generált ikon.A kiválasztott ikon előnézete

Sötét mód ikon URL-jeOpcionális sötét témájú ikon. `image_dark` egy elfogadott álnév.Könnyű műalkotás URL-jeMásodlagos műalkotás, kipróbálva a kiadás után kép és `icon`.Sötét grafika URL-je

#### Eszközök felszabadításaTartalomnév kiadásaMinden kiválasztott modellhez egy név. Hagyja üresen a használathoz `rom.zip` Y1 és `rom_<model>.zip` máshol.Eszköz mintaGlob akkor használatos, ha a kiadás zipjei nincsenek megnevezve `rom*.zip`.Type A eszközGlob a Y1 Type A csomaghoz, ha a neve nem ezt mondja.Type B eszközGlob a Y1 Type B csomaghoz, ha a neve nem ezt mondja.Az alkalmazás minimális verziójaA bejegyzés elrejtése a régebbi Updater CE buildekből.

#### Linkek, tükrök és Keep Data családTelepítés utáni oldalSikeres telepítés után megnyílt.Második telepítés utáni oldalVálasztható második lépés a többoldalas beállítási útmutatóhoz.Hordozható cipzáras tükrökVesszővel elválasztva `*-mirror` Portable Flashing Zip csomagokat építő adattárak.Származékos adattárA firmware, amelyből ez a kiadás épül. A kapcsolódó firmware-ek megosztanak egy adatpartíciót, amelyet a Keep Data ellenőrzi.InfotárAlkalmazástár, amelynek kiadásai leírják az ebben a firmware-ben lévő alkalmazásokat. Telepítés utáni oldal is kell hozzá.APK adattárApp repo, amelynek APK az alkalmazás letölti és telepíti a firmware után.

#### Katalógus extrákMeztelen csigaStabil azonosító a hivatkozásokhoz és a mentett telepítési rekordokhoz. A modell automatikusan hozzáfűződik, ha több modellt választ ki.Leírás`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Vonalak másolása

A legújabb jegyzék betöltése…Tekintse meg a legújabb jegyzék előnézetét a soraival együtt

A generátor levette az áramot `slidia_manifest.xml` ebből a tárolóból, és közvetlenül előtte szúrta be a generált sorokat `</slidia>`.

Egy sor nem elég egy megosztott tárolóhoz. Ha a Y2 sor hiányzik, a Y2 felhasználók akkor sem kapnak modellegyező bejegyzést, ha `rom_y2.zip` létezik a projekt kiadásában. Ugyanez igaz minden más modellre, amelyet a kiadása támogat.

### A jegyzék minden attribútuma beolvas

Ezeket az attribútumokat a jelenlegi Updater CE buildek megértik. A generátor csak azokat írja, amelyeket Ön kitölt; az alkalmazás a többinél visszaáll az ésszerű alapértelmezett értékekre.slidia_manifest.xml csomagattribútumok és jelentésük``````````````````````````````````````````````````````````````````````````````````````````````

| Attribútum | Szükséges | Mit csinál |
| --- | --- | --- |
| name | Igen | A katalógusban és a telepítési kártyákon látható szoftvernév. |
| repo | Igen | owner/repo. Az alkalmazás beolvassa az adattár GitHub kiadásait. |
| device | Igen | Célmodell, nagybetűs (Y1, Y2, G1, Q3e, …). Modellenként egy bejegyzés maradjon. |
| url | Ajánlott | A katalógusból megnyitott projektoldal vagy kiadási megjegyzések. |
| type, handler | A gyakorlatban igen | type="img" és handler="Custom Firmware". Más típusok és nem firmware-kezelők kimaradnak. |
| brand | Választható | Katalógus márka (Innioasis, Timmkoo). Az Empty a modell alapértelmezett márkáját használja. |
| package_name | Választható | Tartalomfájlnév kiadása. Alapértelmezés szerint rom.zip Y1 és rom_<model>.zip más modelleken. |
| asset_pattern | Választható | A kis- és nagybetűk nem megkülönböztetik az olyan kiadásokat, amelyek firmware-zipjei nincsenek megnevezve rom*.zip (például my-firmware-*.zip). |
| type_a_asset, type_b_asset | Választható | Globák, amelyek azonosítják a Y1 Type A és Type B zipeket, ha a fájlneveik nem tartalmazzák a szokásos jelölőket. |
| icon | Választható | Logo URL. A saját megjelenése után használták updater.png / updater.jpg, és minden kiadás tartalékaként. |
| icon_dark | Választható | Sötét témájú logó. image_dark egy elfogadott álnév. |
| image | Választható | Másodlagos könnyű alkotás, utána próbált icon. |
| post_install, post_install2 | Választható | Sikeres telepítés után megnyitott oldal(ok). A második egy többlépcsős útmutatót takar. |
| portable_zips | Választható | Vesszővel elválasztva *-mirror repók, amelyek futtatásra kész hordozható csomagokat tesznek közzé. |
| derivative | Választható | Repository, amelyből a firmware épül. Az azonos származékos gyökérrel rendelkező firmware tárolhatja a felhasználói adatokat. |
| info_repo | Választható | Alkalmazástár, amelynek kiadásai leírják, hogy mit telepít a firmware. Megköveteli post_install vagy post_install2. |
| apk_repo | Választható | Alkalmazástár, amelynek APK a firmware után telepíti az alkalmazást. |
| min_version | Választható | A bejegyzés elrejtése, ha az Updater CE régebbi ennél a verziónál. |
| do_not_keep_data | Választható | true (szintén 1 / yes) blokkolja az adatok teljes megőrzését ehhez a firmware-hez. |
| slug | Választható | Stabil azonosító a hivatkozásokhoz és a mentett telepítési rekordokhoz. Üres állapotban a név és a modell alapján generálódik. |
| description | Választható | Rövid katalógus leírás. Ez lehet az attribútum értéke vagy az elem szövege. |

A kompatibilitás érdekében a régi neveket továbbra is olvassák: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` és `image_dark`. Az új bejegyzéseknél a fenti jelenlegi neveket kell használni.

### Küldje el a sorokat lehívási kérelemként
  - Másolja ki a fenti generált sorokat. Már megfelelnek a legújabb jegyzékformátumnak.
  - Szerkesztés `slidia_manifest.xml` az adattárban. Használja az alábbi szerkesztési linket; a tároló gazdagép automatikusan létrehoz egy elágazást és egy elágazást.
  - Illessze be a vonalakat közvetlenül előtte `</slidia>`, a meglévő bejegyzések változatlan megőrzése.
  - Köteleződjön el egy új ágon (például `add-your-firmware`), majd nyissa meg a lehívási kérelmet az Updater CE lerakatában.
  - A PR-ben szerepeljen a projekt hivatkozását, a támogatott modelleket, a kiadási címkét, az eszközneveket és a tesztelt eszközöket.
[Szerkessze az Updater CE jegyzékét](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Tekintse meg a legújabb manifestet](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Tartsa a modellneveket nagybetűkkel, használja a nyilvános tárhely pontos URL-címét, és tartsa meg `type="img"` és `handler="Custom Firmware"` firmware bejegyzéshez.

## Tegye könnyen ellenőrizhetővé a kiadást

Adjon a kiadásnak egyértelmű címkét és kiadási megjegyzést. A címke hasznos az emberek számára, de az Updater CE a ZIP-eszközneveket használja a telepítőcsomagok azonosítására.

### Feloldási ellenőrzőlista
  - Tegye közzé a kiadást nyilvánosan.
  - Csatolja a ZIP-fájlokat kiadási eszközökként.
  - Adja meg a támogatott modellt és Type A vagy Type B a megjegyzésekben.
  - Sorolja fel a szükséges előkészületeket vagy ismert határértékeket.

### Egy kiadás, három eszköz

A megosztott kiadás tartalmazhat `rom.zip`, `rom_type_b.zip`, és `rom_y2.zip`. Az Updater külön osztályozza őket, és a modell- és hardverszűrők közül választ.

### Ne kapcsolja össze a találgatásokat

Ne adjon meg Y1 csomagot a Y2 fájlnév alatt, és ne adjon hozzá nem tesztelt szóró-, előbetöltő- vagy partíciós adatokat csak azért, hogy egy eszköz megjelenjen.

## Miért számítanak a modellbejegyzések villogás közben?

A jegyzék nem csak egy letöltési menü. A kibontás után az Updater CE a feloldott modellt használja a megfelelő telepítési útvonal előkészítéséhez. A Y1 és Y2 különböző platformfájlokkal, előtöltőkkel, szórt konfigurációval és eszközelrendezéssel rendelkezik.
  - Y1: a frissítő előkészíti a Y1 elérési utat, és az eszköz elnevezett partícióit használja az MTKClient használatakor.
  - Y2: a frissítő előkészíti a Y2 elérési utat és az Y2 MT6582 konfigurációt használja. A teljes helyreállítás fizikai címeket használhat a modellnek megfelelő szórt adatokból.
  - Platformok közötti támogatás: Az Updater CE közvetlenül kezeli a natív flashinget Windowson, Linuxon és macOS-en (mind az Intel, mind az Apple Silicon Mac-eket támogatja), további flash-eszközök nélkül.
A közreműködőknek megfelelő firmware fájlokat kell megadniuk, nem flash offseteket. Ne szerkessze a szórt címeket, előbetöltőket, DA fájlokat vagy partíciós parancsokat a rossz csomagok megkerülésére. Javítsa ki a kiadási eszközt, és tesztelje a kívánt modellt.

## Mielőtt egyesítést kérne
  - Érvényesítse az XML-t egy XML-elemzővel. Hiányzó idézet vagy zárás `/>` minden bejegyzést elrejthet utána.
  - Indítsa el a frissítőt a pénztárból, hogy a távoli frissítés előtt betöltse a helyi jegyzéket.
  - Ellenőrizze egymástól függetlenül a Y1 és Y2 elemet. Győződjön meg arról, hogy a projekt csak ott jelenik meg, ahol a csomagja támogatott.
  - Ellenőrizze a kiadási listát `rom.zip`, `rom_type_b.zip`, és `rom_y2.zip` értelemszerűen.
  - Tesztelje a tényleges telepítést a tervezett eszközön egy megbízható USB adatkábellel és egy helyreállítási tervvel az eredeti szoftverhez való visszatéréshez.
  - A lehívási kérelemben magyarázza el, mit tesztelt. Ne írjon le nem tesztelt modellt támogatottként.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Helyi ellenőrzéshez futtassa a parancsot a lerakat gyökérből. Csak az XML szintaxist ellenőrzi; nem bizonyítja, hogy egy kiadás érvényes firmware-t tartalmaz, vagy hogy egy eszköz biztonságosan villoghat.

## Hasznos projekt linkek[Fork Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Lásd a manifestet](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[közösségi hozzájárulással kapcsolatos megjegyzések](support_devs_hu.html)[Hibaelhárítás](troubleshooting_hu.html)

## Moding készségek AI ügynökök számára

Az adattáré `skills/` A könyvtár egy forrásalapú tudásbázis a Y1 és Y2 hardveren, firmware-en, témákon és alkalmazásokon dolgozó ügynökök számára. Minden képesség elnevezi azokat a projektfájlokat, amelyekből a követelései származnak, így az ügynök ellenőrizheti a tényt, mielőtt eszközt cserél.Kezdje itt

### [Képességmutató és biztonsági szabályok](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Hogyan töltsünk be egy képességet, melyik modellre vonatkozik egy tény, és milyen partíciókat nem írhat a csomag.Hardver

### [Y1 hardver](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, a kerék, mint legfontosabb események, 480x360-as kijelző, FM/audio útvonalak, tárhely és a Type A/B partíciótérkép.Hardver

### [Y2 hardver](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582 kártya, eszközfa, GC9503V/ST7701S panelek, PMIC/DAC sínek, partíciók és a rendszerindító kép.Firmware

### [Firmware csomagok](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatómia, szórt fájlok, A osztályú frissítési szerződések és a kiadási ellenőrzőlista.Témák

### [Téma és skin szerzői](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json témák, Rockbox WPS/SBS, Reborn felszínek és Y2Player skin formátum v2.Minden készség

### [Böngésszen a készségek mappájában](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, készlet Android ROM-ok, Y2Linux, Android-alkalmazások, indítók, kibocsátási megjegyzések és webhelyek közzététele.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
