---
title: "Cum se instalează Rockbox pe programul de actualizare Innioasis Y1 sau Y2 - Innioasis"
description: "Instalați Rockbox pe un Innioasis Y1 sau Y2 cu Updater: teme, versiuni stabile, note Type A și Type B și cum să restaurați software-ul original după."
language: "ro"
source: "https://innioasis.app/rockbox_ro.html"
---

# Cum se instalează Rockbox pe programul de actualizare Innioasis Y1 sau Y2 - Innioasis

Rockbox referință

# Obținerea Rockbox pe Y1 sau Y2

Rockbox modifică software-ul playerului și deschide o interfață mai profundă pentru redare muzicală, comenzi de redare, sortare și opțiuni de temă. Instalarea este ghidată, dar Y1 și Y2 sunt călătorii separate.[Rockbox pe Y1](guides/rockbox-y1.html)[Rockbox pe Y2](guides/rockbox-y2.html)[De ce Rockbox?](rockbox-benefits_ro.html)

## Ce se schimbă instalarea

Rockbox este un software personalizat. Nu vă elimină capacitatea de a reveni la interfața stoc atunci când pachetul de software original corespunzător este disponibil. Poate îmbunătăți navigarea și personalizarea muzicii, dar funcțiile, rezoluția, durata de viață a bateriei și compatibilitatea temelor depind de construcție.Nu amestecați modele. Selectați Y1 pentru un jucător Y1 și Y2 pentru un jucător Y2. Un nume de lansare cu aspect similar nu este o dovadă suficientă că un pachet este compatibil.

## Urmăriți videoclipul

Videoclip de Frawgeeys. Afișează ruta Innioasis Updater; utilizați pașii scrisi specifici modelului de mai jos pentru Y1 sau Y2.

Video de la [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (spaniolă), afișând Rockbox pe un Y1. Utilizați pașii specifici modelului de mai jos pentru playerul dvs.

## Ruta de actualizare partajată
  - Instalați Updater și nu conectați nimic până când vă întreabă.
  - Alegeți modelul imprimat pe player în Model dispozitiv.
  - Alege Rockbox în Software.
  - Alegeți o versiune stabilă, cu excepția cazului în care testați în mod deliberat o versiune de noapte.
  - Faceți clic Instalează / Restaurează, apoi urmați promptul de oprire și de conectare USB.
  - Deconectați-vă numai după mesajul de succes.

## 240p, 360p și teme

Colecțiile de teme mai vechi Rockbox pot fi create pentru 240p. Y1 versiunile comunității folosesc și etichete de compatibilitate 360p. Citiți notele de lansare și sursa temei înainte de a alege o versiune. Este posibil ca o temă creată pentru o rezoluție sau o familie de software să nu funcționeze pe alta.[Răsfoiți temele comunității](https://themes.innioasis.app/?lang=ro)[Instrumente tematice](https://themes.innioasis.app/?lang=ro)

## Revenind la software-ul original

Alege din nou același model, selectează Software original, alegeți o versiune stabilă și utilizați Instalează / Restaurează. Dacă eșecul a avut loc înainte de promptul USB, verificați computerul și fișierele extrase. Dacă playerul a fost detectat, dar blițul a eșuat, începeți cu [depanare](troubleshooting_ro.html).[Y1 restaurați](guides/restore-original-y1.html)[Y2 restaurați](guides/restore-original-y2.html)

## Întrebări frecventeAm reinstalat Rockbox și nu a rezolvat nimic.

Reinstalarea Rockbox scrie aceeași versiune peste aceleași fișiere, așa că nu poate reseta lucrurile pe care Rockbox le păstrează pe MicroSD. Dacă problema este o setare, o temă, o listă de redare sau o bază de date deteriorate care se află pe card, reinstalarea nu o va șterge. Resetarea de încredere este ștergerea `.rockbox` folderul din MicroSD — Rockbox creează unul nou la următoarea pornire.
  - Opriți complet playerul și scoateți cardul MicroSD sau conectați playerul ca unitate USB.
  - Afișați fișierele ascunse pe computer, astfel încât folderul să fie vizibil. Cum să afișați fișierele ascunseAfișați fișierele cu puncte pe computerWindows: în File Explorer deschideți Vedeți tab și bifează Articole ascunse.macOS: în apăsarea Finder Cmd+Shift+. pentru a comuta fișierele ascunse.Linux · Fișiere GNOME: apăsați Ctrl+H, sau deschideți meniul și alegeți Afișați fișierele ascunse.Linux · KDE Dolphin: apăsați Ctrl+H, sau utilizați Vizualizare → Afișare fișiere ascunse.
  - Ștergeți `.rockbox` folder din rădăcina cardului.
  - Reintroduceți cardul și porniți jucătorul. Rockbox recreează folderul cu valorile implicite.
  - Reaplicați tema și setările. Dacă problema revine doar după o anumită temă, acea temă este cauza.

Ștergerea `.rockbox` nu dezinstalează Rockbox și nu îți atinge muzica — folderul conține setări, teme și cache și este reconstruit automat. Dacă doriți să vă păstrați temele, copiați folderul din `.rockbox` înainte de a-l șterge sau redenumiți folderul în `.rockbox-old` mai întâi.De ce nu pot vedea folderul .rockbox pe MicroSD meu?

Folderele al căror nume începe cu un punct sunt ascunse implicit pe majoritatea computerelor. Nu trebuie să-l vedeți pentru a instala Rockbox — Updater gestionează fișierele. Dacă depanați și doriți să o ștergeți, activați mai întâi fișierele ascunse. Cum să afișați fișierele ascunseAfișați fișierele cu puncte pe computerWindows: în File Explorer deschideți Vedeți tab și bifează Articole ascunse.macOS: în apăsarea Finder Cmd+Shift+. pentru a comuta fișierele ascunse.Linux · Fișiere GNOME: apăsați Ctrl+H, sau deschideți meniul și alegeți Afișați fișierele ascunse.Linux · KDE Dolphin: apăsați Ctrl+H, sau utilizați Vizualizare → Afișare fișiere ascunse.Ștergerea .rockbox îmi va reseta tema și setările?

da — `.rockbox` deține setările lui Rockbox, tema, listele de redare și baza de date stocată în cache. Ștergerea lui readuce Rockbox la o stare implicită curată. Faceți o copie de rezervă a întregului folder (sau redenumiți-l în `.rockbox-old`) dacă doriți înapoi, porniți playerul și Rockbox creează un dosar nou.

## Mai multe ghiduri Rockbox-Y1 și Rockbox-Y2.

Explorați ghidurile pas cu pas pentru instalarea, descărcarea, tematică, restaurarea și depanarea Rockbox pe ambele modele:[Rockbox-Y1 hub](rockbox-y1/)[Hub Rockbox-Y2](rockbox-y2/)[Rockbox descărcări ROM](rockbox-rom-download_ro.html)[Rockbox pentru Y1](rockbox-for-y1_ro.html)[Rockbox pentru Y2](rockbox-for-y2_ro.html)[Rockbox-Y1 vs Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 teme](rockbox-y1-themes.html)[Rockbox-Teme Y2](rockbox-y2-themes.html)

## A fost utilă această referință?

Răspunsul tău ajută la îmbunătățirea acestui ghid.DaNu încă[Spune-ne cum ne putem îmbunătăți](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
