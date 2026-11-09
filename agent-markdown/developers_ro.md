---
title: "Dezvoltatori | Adăugați firmware personalizat la Innioasis Updater CE - Innioasis Descărcări de firmware"
description: "Documentația dezvoltatorului pentru adăugarea unui firmware personalizat Innioasis Y1 sau Y2 la Updater CE: forkează depozitul, publică rom.zip materiale, editează slidia_manifest.xml, testează și deschide o cerere de extragere."
language: "ro"
source: "https://innioasis.app/developers_ro.html"
---

# Dezvoltatori | Adăugați firmware personalizat la Innioasis Updater CE - Innioasis Descărcări de firmware

Pentru dezvoltatorii de firmware

# Adăugați firmware-ul la Updater CE.

Updater CE este catalogul comunității și programul de instalare pentru firmware personalizat. Dezvoltați-vă proiectul dintr-o bază ROM, publicați-l ca depozit public cu elementele de lansare corecte, adăugați intrările modelului la `slidia_manifest.xml`, testați filtrele de model și deschideți o cerere de extragere. Un singur depozit poate servi fiecare model pe care îl acceptă.[Vizualizați sursa Updater CE](https://github.com/y1-community/Innioasis-Updater)[Răsfoiți Descărcări de software](firmware_ro.html)

## Începeți de la o bază ROM

ROM-urile de bază oferă dezvoltatorilor de firmware personalizat o bază curată pentru Android, cu cipurile radio wireless activate. Pe Y1 activează Wi-Fi și GPS împreună cu Bluetooth și FM din fabrică; pe Y2 activează Wi-Fi, GPS și FM împreună cu Bluetooth-ul din fabrică.Descărcări de bază ROM pentru dezvoltarea firmware-ului personalizat, cu versiunea Android și funcțiile wireless pe care fiecare le permite[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Descarcă | Dispozitiv | Android | Caracteristici wireless |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Adaugă Wi-Fi și GPS în fabrică Bluetooth și FM (FM funcționează deja pe Y1 din fabrică). Pentru Y1 jucători livrați cu OS 2.0.0 sau o versiune ulterioară. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Adaugă Wi-Fi și GPS în fabrică Bluetooth și FM (FM funcționează deja pe Y1 din fabrică). Pentru Y1 jucători care au fost livrate cu un sistem de operare anterior versiunii 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Adaugă Wi-Fi, GPS și FM la Bluetooth din fabrică. Cipul radio Y2 este complet activat, așa că FM este disponibil și aici. |

Aceste imagini sunt baza stoc Android (AOSP) cu dispozitivele radio wireless activate, astfel încât un firmware personalizat poate adăuga funcții de rețea în loc să înlocuiască stack-ul radio. Ele reprezintă punctul de plecare practic pentru etapele de publicare de mai jos.

## Folosiți aceste nume de materiale de lansare

Numele fișierului face parte din semnalul de compatibilitate. Păstrați numele exacte și puneți fișierele ZIP în elementele de lansare ale proiectului, nu numai în arborele sursă al depozitului.Firmware ZIP nume de active și dispozitive acceptate``````

| Atu | Dispozitiv | Hardware | Înțeles |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 dispozitive livrate cu OS 2.0.0 sau o versiune ulterioară. |
| rom_type_b.zip | Y1 | Type B | Y1 dispozitive care au fost livrate cu un sistem de operare anterior versiunii 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Pachetul de instalare completă Y2. Păstrați-l separat de Y1 elemente. |
Nu redenumiți un pachet pentru a se potrivi cu alt model. Y1 și Y2 folosesc fișiere de platformă MediaTek diferite și configurații intermitente. Publicați pachetul pentru hardware-ul pe care îl acceptă de fapt.

## Cum funcționează conexiunea

Updater CE citește manifestul ca catalog. Fiecare `<package>` line îi spune numele proiectului, depozitul, modelul și handlerul. Când un utilizator alege acel proiect, Updater verifică versiunile publicate ale depozitului și caută un `rom*.zip` activ.

### Manifesta

Denumește proiectul și îl mapează la un model. Y1 și Y2 au nevoie de linii separate, chiar și atunci când partajează un depozit.

### Lansare publicată

Conține elementele ZIP instalabile. O singură versiune poate conține pachetele Y1 Type A, Y1 Type B și Y2 împreună.

### Instalare Updater CE

Utilizează modelul selectat pentru a alege pachetul potrivit și calea intermitentă specifică modelului. Utilizatorul nu trebuie să ghicească un nume de fișier.

## Publicați un proiect în cinci pași
  - Bifurcați depozitul Updater CE. Creează-ți propria furcă de [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), apoi clonează-ți furculița local.
  - Pregătiți un depozit public de firmware. Asigurați-vă că depozitul este public și că ediția sa conține elementele ZIP corecte. Poți pune `rom.zip`, `rom_type_b.zip`, și `rom_y2.zip` pe aceeași versiune când aparțin aceleiași versiuni.
  - Editați manifestul. Deschide `slidia_manifest.xml` în rădăcina furcii dvs. Updater CE. Adăugați o linie pentru fiecare model pe care suportă versiunea (Y1 și Y2 sunt perechea comună). The `repo` valoarea este a depozitului `owner/repository`; `url` este pagina publică a proiectului.
  - Testează catalogul. Rulați Updater din casă editată. Selectați Y1 și confirmați că proiectul arată activele Y1. Selectați Y2 și confirmați că afișează versiunea Y2. Bifați Type A și Type B separat când ambele sunt publicate.
  - Deschideți o cerere de tragere. Împingeți modificarea manifestului în fork și deschideți o cerere de extragere împotriva depozitului Updater CE din amonte. Includeți linkul proiectului, modelele acceptate, eticheta de lansare, numele materialelor și dispozitivele pe care le-ați testat.

## Generați-vă liniile manifeste

Completați depozitul și bifați fiecare model pe care îl acceptă versiunea. Generatorul scrie unul `<package>` linie per model și include numai atributele pe care le setați, astfel încât rezultatul se potrivește cu cel curent `slidia_manifest.xml` format. Fiecare atribut pe care Updater CE îl citește este disponibil mai jos - cele opționale sunt sub Mai multe opțiuni.Adresa URL a depozituluiDepozitul public GitHub. Generatorul extrage `owner/repository` de la adresa URL.Nume softwareAfișat în aplicație și în catalogul site-ului.Adresa URL a proiectuluiPagina cu fața umană pentru proiect sau notele de lansare ale acestuia.MarcaȘtergeți această opțiune pentru a utiliza marca implicită a modelului. SR1, Q3, Q5 și Q3e sunt modele Timmkoo.Dispozitive (o linie fiecare)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAlte modelePentru un model care nu este listat mai sus. Modelele cunoscute își păstrează ortografia catalogului.Steaguri`do_not_keep_data` — nu oferiți niciodată Keep Data pentru acest firmwareConstruit din software original - adaugă `derivative="y1-community/y1-stock-rom"`

Keep Data este oferit numai atunci când firmware-ul primit și firmware-ul instalat sunt identice sau partajează a `derivative` rădăcină. Utilizați steag numai atunci când datele utilizatorului nu pot fi transferate cu adevărat.Mai multe opțiuni: pictogramă, ilustrație, materiale de lansare, post-instalare și oglinzi

#### Icoana și opera de artăFișier pictogramăAlegeți imaginea pe care o veți trimite în depozit. Acesta îl previzualizează și își construiește URL-ul brut; nu incarca nimic.Calea pictogramei în depozitCalea către imaginea comisă, relativ la rădăcina depozitului.Ramura pictogrameiAdresa URL a pictogrameiO adresă URL directă a imaginii. Când este goală, aplicația folosește versiunea `updater.png` sau o pictogramă generată.Previzualizarea pictogramei selectate

Adresa URL a pictogramei în modul întunecatPictogramă opțională cu temă întunecată. `image_dark` este un alias acceptat.Adresa URL a lucrării de artă ușoarăOpera de artă secundară, încercată după imaginea de lansare și `icon`.Adresa URL întunecată a lucrării de artă

#### Eliberați activeEliberați numele materialuluiUn nume pentru fiecare model selectat. Lăsați gol pentru utilizare `rom.zip` pe Y1 și `rom_<model>.zip` altundeva.Modelul de activeGlob folosit atunci când zipurile versiunii nu sunt denumite `rom*.zip`.Type A materialGlob pentru pachetul Y1 Type A când numele său nu spune acest lucru.Type B materialGlob pentru pachetul Y1 Type B când numele său nu spune acest lucru.Versiunea minimă a aplicațieiAscundeți intrarea din versiunile mai vechi de Updater CE.

#### Linkuri, oglinzi și familia Keep DataPagina de post-instalareDeschis după o instalare cu succes.A doua pagină post-instalareAl doilea pas opțional pentru un ghid de configurare cu mai multe pagini.Oglinzi portabile cu fermoarSeparate prin virgulă `*-mirror` depozite care construiesc pachete Portable Flashing Zip.Depozitul de derivateFirmware-ul din care este construită această versiune. Firmware-urile înrudite partajează o partiție de date, care este ceea ce verifică Keep Data.Depozitul de informațiiRepo de aplicații ale căror versiuni descriu aplicațiile din acest firmware. De asemenea, are nevoie de o pagină post-instalare.APK depozitRepoziție de aplicație a cărei APK aplicația se descarcă și se instalează după firmware.

#### Suplimente de catalogLimacIdentificator stabil pentru link-uri și înregistrări de instalare salvate. Modelul este atașat automat atunci când sunt selectate mai multe modele.Descriere`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Copiați linii

Se încarcă cel mai recent manifest...Previzualizează cel mai recent manifest cu rândurile tale adăugate

Generatorul a preluat curentul `slidia_manifest.xml` din acest depozit și a inserat liniile dvs. generate chiar înainte `</slidia>`.

O singură linie nu este suficientă pentru un depozit partajat. Dacă linia Y2 lipsește, utilizatorii Y2 nu vor primi o intrare potrivită cu modelul chiar și atunci când `rom_y2.zip` există în lansarea proiectului. Același lucru este valabil pentru orice alt model pe care îl acceptă versiunea dvs.

### Fiecare atribut pe care îl citește manifestul

Acestea sunt atributele pe care le înțeleg actualul Updater CE. Generatorul le scrie doar pe cele pe care le completați; aplicația revine la valori implicite sensibile pentru restul.Atributele pachetului slidia_manifest.xml și semnificația acestora``````````````````````````````````````````````````````````````````````````````````````````````

| Atribut | Necesar | Ce face |
| --- | --- | --- |
| name | Da | Numele software-ului este afișat în catalog și pe cardurile de instalare. |
| repo | Da | owner/repo. Aplicația citește versiunile GitHub ale acelui depozit. |
| device | Da | Model țintă, majuscule (Y1, Y2, G1, Q3e, …). Păstrați o înregistrare pentru fiecare model. |
| url | Recomandat | Pagina de proiect sau note de lansare deschise din catalog. |
| type, handler | Da in practica | type="img" şi handler="Custom Firmware". Alte tipuri și manipulari non-firmware sunt ignorate. |
| brand | Opțional | Marca de catalog (Innioasis, Timmkoo). Empty folosește marca implicită a modelului. |
| package_name | Opțional | Eliberați numele fișierului materialului. Implicit la rom.zip pe Y1 și rom_<model>.zip pe alte modele. |
| asset_pattern | Opțional | Glob fără majuscule și minuscule pentru versiunile ale căror zip-uri de firmware nu sunt denumite rom*.zip (de exemplu my-firmware-*.zip). |
| type_a_asset, type_b_asset | Opțional | Glob-uri care identifică zipurile Y1 Type A și Type B atunci când numele fișierelor lor nu conțin marcajele obișnuite. |
| icon | Opțional | Adresa URL a siglei. Folosit după lansarea proprie updater.png / updater.jpg, și ca alternativă pentru fiecare lansare. |
| icon_dark | Opțional | Logo cu temă întunecată. image_dark este un alias acceptat. |
| image | Opțional | Lucrări de artă luminoase secundare, încercate după icon. |
| post_install, post_install2 | Opțional | Paginile deschise după o instalare reușită. Al doilea acoperă un ghid în mai mulți pași. |
| portable_zips | Opțional | Separate prin virgulă *-mirror repos-uri care publică pachete portabile gata de rulare. |
| derivative | Opțional | Depozitul din care este construit firmware-ul. Firmware-ul cu aceeași rădăcină derivată poate păstra datele utilizatorului. |
| info_repo | Opțional | Depozitul de aplicații ale cărui versiuni descriu ce implementează firmware-ul. Necesită post_install sau post_install2. |
| apk_repo | Opțional | Depozitul de aplicații al cărui APK se instalează aplicația după firmware. |
| min_version | Opțional | Ascundeți intrarea când Updater CE este mai veche decât această versiune. |
| do_not_keep_data | Opțional | true (de asemenea 1 / yes) blochează complet Keep Data pentru acest firmware. |
| slug | Opțional | Identificator stabil pentru link-uri și înregistrări de instalare salvate. Generat din nume și model atunci când sunt goale. |
| description | Opțional | Scurtă descriere a catalogului. Poate fi valoarea atributului sau textul elementului. |

Numele moștenite sunt încă citite pentru compatibilitate: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` şi `image_dark`. Noile intrări ar trebui să utilizeze numele curente de mai sus.

### Trimiteți liniile ca cerere de tragere
  - Copiați liniile generate mai sus. Se potrivesc deja cu cel mai recent format de manifest.
  - Editați `slidia_manifest.xml` în depozit. Utilizați linkul de editare de mai jos; gazda depozitului creează automat o furcă și o ramură pentru tine.
  - Lipiți liniile chiar înainte `</slidia>`, păstrând neschimbate înregistrările existente.
  - Angajați-vă într-o nouă filială (de exemplu `add-your-firmware`), apoi deschideți o cerere de extragere împotriva depozitului Updater CE.
  - În PR, includeți linkul proiectului, modelele acceptate, eticheta de lansare, numele materialelor și dispozitivele pe care le-ați testat.
[Editați manifestul Updater CE](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Vezi cel mai recent manifest](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Păstrați numele modelelor cu majuscule, utilizați adresa URL exactă a depozitului dvs. public și păstrați `type="img"` şi `handler="Custom Firmware"` pentru o intrare de firmware.

## Faceți eliberarea ușor de verificat

Dați lansării o etichetă clară și o notă de lansare. Eticheta este utilă oamenilor, dar numele materialelor ZIP sunt cele pe care Updater CE le folosește pentru a identifica pachetele de instalare.

### Eliberați lista de verificare
  - Publicați ediția public.
  - Atașați fișierele ZIP ca materiale de lansare.
  - Indicați modelul acceptat și Type A sau Type B în note.
  - Enumerați orice preparat necesar sau limitele cunoscute.

### O lansare, trei active

O versiune partajată poate conține `rom.zip`, `rom_type_b.zip`, și `rom_y2.zip`. Updater le clasifică separat și alege dintre filtrele model și hardware.

### Nu combina ghiciri

Nu includeți un pachet Y1 sub numele de fișier Y2 și nu adăugați date de dispersie, preîncărcare sau partiție netestate doar pentru a face să apară un material.

## De ce contează intrările de model în timpul intermitentului

Manifestul nu este doar un meniu de descărcare. După extragere, Updater CE utilizează modelul rezolvat pentru a pregăti calea de instalare potrivită. Y1 și Y2 au fișiere de platformă diferite, preîncărcare, configurație scatter și aspect al dispozitivului.
  - Y1: actualizatorul pregătește calea Y1 și folosește partițiile numite ale dispozitivului când este utilizat MTKClient.
  - Y2: actualizatorul pregătește calea Y2 și utilizează configurația Y2 MT6582. Recuperarea completă poate folosi adrese fizice din datele de împrăștiere corecte la model.
  - Asistență pe mai multe platforme: Updater CE gestionează intermiterea nativă direct pe Windows, Linux și macOS (care acceptă atât Intel, cât și Apple Silicon Mac) fără instrumente suplimentare de flashing.
Colaboratorii ar trebui să furnizeze fișiere firmware corecte, nu compensații flash. Nu editați adrese scatter, preîncărcătoare, fișiere DA sau comenzi de partiție pentru a evita un pachet prost. Remediați activul de lansare și testați pe modelul dorit.

## Înainte de a solicita o fuziune
  - Validați XML cu un parser XML. Un citat lipsă sau o închidere `/>` poate ascunde fiecare intrare după ea.
  - Lansați actualizatorul de la finalizarea comenzii, astfel încât să încarce manifestul local înainte de reîmprospătarea de la distanță.
  - Bifați Y1 și Y2 independent. Confirmați că proiectul apare numai acolo unde pachetul său este acceptat.
  - Verificați lista de lansări pentru `rom.zip`, `rom_type_b.zip`, și `rom_y2.zip` după caz.
  - Testați instalarea efectivă pe dispozitivul dorit, cu un cablu de date USB fiabil și un plan de recuperare pentru revenirea la software-ul original.
  - În cererea de extragere, explicați ce ați testat. Nu descrieți un model netestat ca fiind acceptat.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Pentru o verificare locală, executați comanda de la rădăcina depozitului. Verifică numai sintaxa XML; nu dovedește că o versiune conține firmware valid sau că un dispozitiv este sigur pentru flash.

## Linkuri utile pentru proiecte[Fork Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Vezi manifestul](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Note de contribuție comunitară](support_devs_ro.html)[Depanare](troubleshooting_ro.html)

## Abilități de modificare pentru agenții AI

Depozitul `skills/` directorul este o bază de cunoștințe bazată pe sursă pentru agenții care lucrează pe hardware, firmware, teme și aplicații Y1 și Y2. Fiecare abilitate denumește fișierele de proiect din care provin revendicările sale, astfel încât un agent poate verifica un fapt înainte de a schimba un dispozitiv.Începeți de aici

### [Indicele de aptitudini și regulile de siguranță](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Cum să încărcați o abilitate, la ce model se aplică un fapt și partițiile pe care niciun pachet nu ar trebui să scrie.Hardware

### [Y1 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, roata ca evenimente cheie, afișaj 480x360, căi FM/audio, stocare și harta partiției Type A/B.Hardware

### [Y2 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Placă MT6582, arborele dispozitivelor, panourile GC9503V/ST7701S, șine PMIC/DAC, partiții și imaginea de pornire.Firmware

### [Pachete de firmware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomie, fișiere scatter, contracte de actualizare de clasa A și lista de verificare a lansării.Teme

### [Crearea temei și a skinului](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 teme config.json, Rockbox WPS/SBS, Reborn skin și Y2Player format de skin v2.Toate aptitudinile

### [Răsfoiți folderul abilități](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, ROM-uri Android stoc, Y2Linux, aplicații Android, lansatoare, note de lansare și publicare pe site.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
