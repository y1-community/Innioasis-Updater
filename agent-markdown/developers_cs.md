---
title: "Vývojáři | Přidejte vlastní firmware do Innioasis Updater CE - Innioasis Firmware Downloads"
description: "Vývojářská dokumentace pro přidání vlastního Innioasis Y1 nebo Y2 firmwaru do Updater CE: rozvětvete repozitář, publikujte rom.zip položky, upravte soubor slidia_manifest.xml, otestujte a otevřete požadavek na stažení."
language: "cs"
source: "https://innioasis.app/developers_cs.html"
---

# Vývojáři | Přidejte vlastní firmware do Innioasis Updater CE - Innioasis Firmware Downloads

Pro vývojáře firmwaru

# Přidejte svůj firmware do Updater CE.

Updater CE je komunitní katalog a instalační program pro vlastní firmware. Vyvíjejte svůj projekt ze základny ROM, publikujte jej jako veřejné úložiště se správnými prostředky vydání, přidejte položky modelu do `slidia_manifest.xml`, otestujte filtry modelu a otevřete požadavek na stažení. Jedno úložiště může obsluhovat každý model, který podporuje.[Zobrazit zdroj Updater CE](https://github.com/y1-community/Innioasis-Updater)[Procházet software ke stažení](firmware_cs.html)

## Začít od základny ROM

Základní paměti ROM poskytují vývojářům vlastního firmwaru čistý základ pro Android s povolenými bezdrátovými rádiovými čipy. Na Y1 umožňují Wi-Fi a GPS spolu s továrním Bluetooth a FM; na Y2 umožňují Wi-Fi, GPS a FM spolu s továrním Bluetooth.Základní ROM stahování pro vlastní vývoj firmwaru s verzí Androidu a bezdrátovými funkcemi, které každý umožňuje[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Stáhnout | Zařízení | Android | Bezdrátové funkce |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Přidá Wi-Fi a GPS k továrnímu Bluetooth a FM (FM již funguje na Y1 z výroby). Pro Y1 přehrávače dodávané s OS 2.0.0 nebo novějším. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Přidá Wi-Fi a GPS k továrnímu Bluetooth a FM (FM již funguje na Y1 z výroby). Pro Y1 přehrávače, které byly dodány s OS starším než 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Přidá Wi-Fi, GPS a FM k továrnímu Bluetooth. Rádiový čip Y2 je plně povolen, takže FM je k dispozici i zde. |

Tyto obrázky jsou základním systémem Android (AOSP) s povolenými bezdrátovými rádii zařízení, takže vlastní firmware může přidat síťové funkce namísto výměny rádiového zásobníku. Jsou praktickým výchozím bodem pro níže uvedené kroky publikování.

## Použijte tyto názvy aktiv vydání

Název souboru je součástí signálu kompatibility. Udržujte přesné názvy a umístěte soubory ZIP do prostředků vydání projektu, nikoli pouze do stromu zdroje úložiště.Firmware ZIP názvy aktiv a podporovaná zařízení``````

| Aktiva | Zařízení | Železářské zboží | Význam |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 zařízení dodávaná s OS 2.0.0 nebo novějším. |
| rom_type_b.zip | Y1 | Type B | Y1 zařízení dodávaná s operačním systémem starším než 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Balíček plné instalace Y2. Udržujte jej odděleně od Y1 aktiv. |
Nepřejmenovávejte balíček, aby vyhovoval jinému modelu. Y1 a Y2 používají různé soubory platformy MediaTek a flashovou konfiguraci. Zveřejněte balíček pro hardware, který skutečně podporuje.

## Jak funguje připojení

Updater CE čte manifest jako svůj katalog. Každý `<package>` řádek mu říká název projektu, úložiště, model a handler. Když uživatel zvolí tento projekt, Updater zkontroluje publikovaná vydání úložiště a vyhledá a `rom*.zip` aktiva.

### Manifest

Pojmenuje projekt a namapuje jej na model. Y1 a Y2 potřebují samostatné řádky, i když sdílejí úložiště.

### Zveřejněné vydání

Obsahuje instalovatelné zdroje ZIP. Jedno vydání může obsahovat balíčky Y1 Type A, Y1 Type B a Y2 společně.

### Instalace aktualizace CE

Použije vybraný model k výběru odpovídajícího balíčku a trasy blikání specifického pro model. Uživatel by neměl hádat název souboru.

## Publikování projektu v pěti krocích
  - Rozvětvete úložiště Updater CE. Vytvořte si vlastní vidličku [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater)a poté lokálně naklonujte vidlici.
  - Připravte si veřejné úložiště firmwaru. Ujistěte se, že je úložiště veřejné a jeho vydání obsahuje správné zdroje ZIP. Můžete dát `rom.zip`, `rom_type_b.zip`a `rom_y2.zip` na stejném vydání, pokud patří ke stejné verzi.
  - Upravte manifest. Otevřít `slidia_manifest.xml` v kořenovém adresáři vaší vidlice Updater CE. Přidejte jeden řádek pro každý model, který verze podporuje (Y1 a Y2 jsou společný pár). The `repo` hodnota je úložiště `owner/repository`; `url` je veřejná stránka projektu.
  - Vyzkoušejte katalog. Spusťte Updater z upravené pokladny. Vyberte Y1 a potvrďte, že projekt zobrazuje aktiva Y1. Vyberte Y2 a potvrďte, že se zobrazí uvolnění Y2. Když jsou obě publikovány, zaškrtněte samostatně Type A a Type B.
  - Otevřete žádost o stažení. Odešlete změnu manifestu do své vidlice a otevřete žádost o stažení proti upstream úložišti Updater CE. Zahrňte odkaz na projekt, podporované modely, značku vydání, názvy prostředků a zařízení, která jste testovali.

## Vygenerujte řádky manifestu

Vyplňte úložiště a zaškrtněte každý model, který vydání podporuje. Generátor píše jeden `<package>` řádek na model a zahrnuje pouze atributy, které jste nastavili, takže výsledek odpovídá aktuálnímu `slidia_manifest.xml` formát. Každý atribut, který Updater CE čte, je dostupný níže – volitelné jsou níže Více možností.Adresa URL úložištěVeřejné GitHub úložiště. Generátor extrahuje `owner/repository` z adresy URL.Název softwaruZobrazeno v aplikaci a katalogu stránek.Adresa URL projektuLidská stránka projektu nebo jeho poznámky k vydání.ZnačkaZrušte toto zaškrtnutí, chcete-li použít výchozí značku modelu. SR1, Q3, Q5 a Q3e jsou Timmkoo modely.Zařízení (každý jeden řádek)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eJiné modelyPro model, který není uveden výše. Známé modely zachovávají svůj katalogový pravopis.Vlajky`do_not_keep_data` — nikdy nenabízejte Keep Data pro tento firmwarePostaveno z původního softwaru – dodává `derivative="y1-community/y1-stock-rom"`

Keep Data se nabízí pouze v případě, že příchozí firmware a nainstalovaný firmware jsou stejné nebo sdílejí a `derivative` kořen. Příznak použijte pouze v případě, že uživatelská data skutečně nelze přenést.Další možnosti: ikona, kresba, vydání aktiv, po instalaci a zrcadlení

#### Ikona a umělecká dílaSoubor ikonyVyberte obrázek, který odevzdáte do úložiště. Tím se zobrazí jeho náhled a vytvoří se jeho nezpracovaná adresa URL; nic nenahrává.Cesta ikony v úložištiCesta k potvrzenému obrazu vzhledem ke kořenovému adresáři úložiště.Ikona větevAdresa URL ikonyPřímá adresa URL obrázku. Když je prázdný, aplikace použije vydání `updater.png` nebo vygenerovaná ikona.Náhled vybrané ikony

Adresa URL ikony tmavého režimuVolitelná ikona tmavého motivu. `image_dark` je akceptovaný alias.Adresa URL světelného uměleckého dílaSekundární předloha, vyzkoušená po vydání obrázku a `icon`.Adresa URL tmavé kresby

#### Uvolněte aktivaUvolnit název dílaJedno jméno pro každý vybraný model. Nechte prázdné k použití `rom.zip` dne Y1 a `rom_<model>.zip` jinde.Vzor aktivGlob se používá, když zipy vydání nejsou pojmenovány `rom*.zip`.Type A aktivaGlob pro balíček Y1 Type A, pokud to jeho název neříká.Type B aktivaGlob pro balíček Y1 Type B, pokud to jeho název neříká.Minimální verze aplikaceSkryjte záznam ze starších sestavení Updater CE.

#### Linky, zrcadla a rodina Keep DataStránka po instalaciOtevřeno po úspěšné instalaci.Druhá stránka po instalaciVolitelný druhý krok pro vícestránkový průvodce nastavením.Přenosná zrcadla na zipOddělené čárkou `*-mirror` repozitáře, které vytvářejí balíčky Portable Flashing Zip.Derivační úložištěFirmware, ze kterého je toto vydání sestaveno. Související firmwary sdílejí datový oddíl, což Keep Data kontroluje.Úložiště informacíÚložiště aplikací, jehož vydání popisují aplikace v tomto firmwaru. Potřebuje také stránku po instalaci.APK úložištěÚložiště aplikace, jehož APK aplikace stáhne a nainstaluje po firmwaru.

#### Katalogové doplňkySlimákStabilní identifikátor pro odkazy a uložené záznamy o instalaci. Model se automaticky přidá, když je vybráno několik modelů.Popis`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Kopírovat řádky

Načítání nejnovějšího manifestu…Prohlédněte si nejnovější manifest s přidanými řádky

Generátor nabral proud `slidia_manifest.xml` z tohoto úložiště a vložili vygenerované řádky těsně předtím `</slidia>`.

Jeden řádek pro sdílené úložiště nestačí. Pokud řádek Y2 chybí, uživatelé Y2 neobdrží záznam odpovídající modelu, i když `rom_y2.zip` existuje ve verzi projektu. Totéž platí pro každý další model, který vaše vydání podporuje.

### Každý atribut, který manifest čte

To jsou atributy, kterým rozumí současná sestavení Updater CE. Generátor zapisuje pouze ty, které vyplníte; u zbytku se aplikace vrátí k rozumným výchozím nastavením.atributy balíčku slide_manifest.xml a jejich význam``````````````````````````````````````````````````````````````````````````````````````````````

| Atribut | Potřebné | Co to dělá |
| --- | --- | --- |
| name | Ano | Název softwaru uvedený v katalogu a na instalačních kartách. |
| repo | Ano | owner/repo. Aplikace čte vydání GitHub daného úložiště. |
| device | Ano | Cílový model, velká písmena (Y1, Y2, G1, Q3e, …). U každého modelu si ponechte jeden záznam. |
| url | Doporučeno | Stránka projektu nebo poznámky k verzi otevřeny z katalogu. |
| type, handler | V praxi ano | type="img" a handler="Custom Firmware". Ostatní typy a nefirmwarové obslužné programy jsou přeskočeny. |
| brand | Volitelné | Katalogová značka (Innioasis, Timmkoo). Prázdný používá výchozí značku modelu. |
| package_name | Volitelné | Uvolněte název souboru podkladu. Výchozí na rom.zip dne Y1 a rom_<model>.zip na jiných modelech. |
| asset_pattern | Volitelné | U verzí, jejichž zipy firmwaru nejsou pojmenovány, se nerozlišují malá a velká písmena rom*.zip (například my-firmware-*.zip). |
| type_a_asset, type_b_asset | Volitelné | Globy, které identifikují Y1 Type A a Type B zipy, když jejich názvy souborů neobsahují obvyklé značky. |
| icon | Volitelné | Adresa URL loga. Použito po vlastním vydání updater.png / updater.jpga jako záložní pro každé vydání. |
| icon_dark | Volitelné | Logo s tmavým motivem. image_dark je akceptovaný alias. |
| image | Volitelné | Sekundární světelné umělecké dílo, vyzkoušeno icon. |
| post_install, post_install2 | Volitelné | Stránky se otevřely po úspěšné instalaci. Druhý obsahuje vícekrokového průvodce. |
| portable_zips | Volitelné | Oddělené čárkou *-mirror repozitáře, které publikují přenosné balíčky připravené ke spuštění. |
| derivative | Volitelné | Úložiště, ze kterého je sestaven firmware. Firmware se stejným odvozeným kořenem může uchovávat uživatelská data. |
| info_repo | Volitelné | Úložiště aplikací, jehož verze popisují, co firmware nasazuje. Vyžaduje post_install nebo post_install2. |
| apk_repo | Volitelné | Úložiště aplikací, jehož APK aplikace nainstaluje po firmwaru. |
| min_version | Volitelné | Skrýt záznam, když je Updater CE starší než tato verze. |
| do_not_keep_data | Volitelné | true (také 1 / yes) pro tento firmware zcela blokuje Keep Data. |
| slug | Volitelné | Stabilní identifikátor pro odkazy a uložené záznamy o instalaci. Vygenerováno z názvu a modelu, když je prázdné. |
| description | Volitelné | Krátký popis katalogu. Může to být hodnota atributu nebo text prvku. |

Kvůli kompatibilitě se stále čtou starší názvy: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` a `image_dark`. Nové položky by měly používat aktuální názvy výše.

### Odešlete řádky jako požadavek na stažení
  - Zkopírujte vygenerované řádky výše. Již odpovídají nejnovějšímu formátu manifestu.
  - Upravit `slidia_manifest.xml` v úložišti. Použijte níže uvedený odkaz pro úpravy; hostitel úložiště pro vás automaticky vytvoří větev a větev.
  - Vložte řádky těsně předtím `</slidia>`, zachování stávajících položek beze změny.
  - Zavázat se k nové pobočce (například `add-your-firmware`), poté otevřete požadavek na stažení proti úložišti Updater CE.
  - V PR zahrňte odkaz na projekt, podporované modely, značku vydání, názvy prostředků a zařízení, která jste testovali.
[Upravte manifest Updater CE](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Podívejte se na nejnovější manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Ponechte názvy modelů velkými písmeny, použijte přesnou adresu URL svého veřejného úložiště a ponechte `type="img"` a `handler="Custom Firmware"` pro záznam firmwaru.

## Usnadněte ověření vydání

Dejte vydání jasný štítek a poznámku k vydání. Značka je pro lidi užitečná, ale k identifikaci instalačních balíčků používá Updater CE názvy aktiv ZIP.

### Kontrolní seznam vydání
  - Publikovat vydání veřejně.
  - Připojte soubory ZIP jako podklady k vydání.
  - Do poznámek uveďte podporovaný model a Type A nebo Type B.
  - Uveďte všechny požadované přípravky nebo známé limity.

### Jedno vydání, tři aktiva

Sdílené vydání může obsahovat `rom.zip`, `rom_type_b.zip`a `rom_y2.zip`. Updater je klasifikuje samostatně a vybírá z modelových a hardwarových filtrů.

### Nesdružujte odhady

Nezahrnujte balíček Y1 pod název souboru Y2 ani nepřidávejte nevyzkoušená data rozptylu, předběžného načítání nebo oddílu jen proto, aby se aktiva objevila.

## Proč záleží na zadání modelu během blikání

Manifest není jen nabídka stahování. Po extrakci Updater CE použije vyřešený model k přípravě odpovídající instalační cesty. Y1 a Y2 mají různé soubory platformy, preloadery, konfiguraci rozptylu a rozložení zařízení.
  - Y1: aktualizátor připraví cestu Y1 a při použití MTKClient použije pojmenované oddíly zařízení.
  - Y2: aktualizátor připraví cestu Y2 a použije konfiguraci Y2 MT6582. Úplná obnova může používat fyzické adresy z modelově správných rozptylových dat.
  - Podpora napříč platformami: Updater CE zvládá nativní flashování přímo ve Windows, Linuxu a macOS (podporuje Intel i Apple Silicon Mac) bez dalších flashovacích nástrojů.
Přispěvatelé by měli poskytovat správné soubory firmwaru, nikoli offsety flash. Neupravujte rozptylové adresy, preloadery, soubory DA nebo příkazy oddílů, abyste obešli špatný balíček. Opravte aktivum vydání a otestujte jej na zamýšleném modelu.

## Než požádáte o sloučení
  - Ověřte XML pomocí analyzátoru XML. Chybějící citace nebo uzávěrka `/>` může skrýt každý záznam po něm.
  - Spusťte aktualizátor z pokladny, aby před vzdálenou aktualizací načetl místní manifest.
  - Nezávisle zkontrolujte Y1 a Y2. Potvrďte, že se projekt zobrazuje pouze tam, kde je podporován jeho balíček.
  - Podívejte se na seznam vydání `rom.zip`, `rom_type_b.zip`a `rom_y2.zip` podle potřeby.
  - Otestujte skutečnou instalaci na zamýšleném zařízení pomocí spolehlivého datového kabelu USB a plánu obnovy pro návrat k původnímu softwaru.
  - V žádosti o stažení vysvětlete, co jste testovali. Nepopisujte netestovaný model jako podporovaný.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Pro místní kontrolu spusťte tento příkaz z kořenového adresáře úložiště. Ověřuje pouze syntaxi XML; neprokazuje, že vydání obsahuje platný firmware nebo že je zařízení bezpečné pro flashování.

## Užitečné odkazy na projekty[Fork Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Viz manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Poznámky k příspěvku komunity](support_devs_cs.html)[Řešení problémů](troubleshooting_cs.html)

## Modovací dovednosti pro agenty AI

Úložiště `skills/` adresář je znalostní báze založená na zdroji pro agenty pracující na Y1 a Y2 hardwaru, firmwaru, motivech a aplikacích. Každá dovednost pojmenovává soubory projektu, ze kterých pocházejí její nároky, takže agent si může ověřit fakt před změnou zařízení.Začněte zde

### [Index dovedností a pravidla bezpečnosti](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Jak načíst dovednost, na který model se daná skutečnost vztahuje a na oblasti, které by žádný balíček neměl zapisovat.Železářské zboží

### [Y1 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, kolo jako klíčové události, displej 480x360, FM/audio cesty, úložiště a mapa oddílu Type A/B.Železářské zboží

### [Y2 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Deska MT6582, strom zařízení, panely GC9503V/ST7701S, kolejnice PMIC/DAC, oddíly a zaváděcí obraz.Firmware

### [Firmwarové balíčky](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomie, rozptylové soubory, smlouvy o aktualizaci třídy A a kontrolní seznam vydání.Témata

### [Tvorba motivu a vzhledu](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 témata config.json, Rockbox WPS/SBS, Reborn vzhledy a Y2Player formát vzhledu v2.Všechny dovednosti

### [Procházejte složku dovedností](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, zásoby Android ROM, Y2Linux, aplikace pro Android, spouštěče, poznámky k vydání a publikování stránek.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
