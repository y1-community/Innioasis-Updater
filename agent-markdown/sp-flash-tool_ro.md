---
title: "SP Flash Tool pentru Innioasis și Timmkoo jucători"
description: "Găsiți SP Flash Tool împreună cu Innioasis Updater pe Windows și Linux, extrageți rom.zip sau rom_y2.zip și flashați un Innioasis Y1 sau Y2 cu fișierul scatter potrivit."
language: "ro"
source: "https://innioasis.app/sp-flash-tool_ro.html"
---

# SP Flash Tool pentru Innioasis și Timmkoo jucători

Clipire manuală

# Flash Tool pentru Innioasis și Timmkoo jucători

SP Flash Tool vine în Innioasis Updater activat [Windows](drivers_ro.html#windows) şi [Linux](drivers_ro.html#linux). O ai deja. Acest ghid arată modalitatea sigură de a-l folosi pe un Innioasis Y1 sau Y2 și ruta de actualizare pentru Timmkoo jucători.[Reveniți la ghidul de actualizare](guide_ro.html)[Descărcări de firmware](firmware_ro.html)[Depanare](troubleshooting_ro.html)

Începe cu Innioasis Updater

## Updater face toată treaba într-o singură trecere

Updater face majoritatea instalărilor într-o singură trecere. Alegeți software-ul, urmați pașii și ați terminat. De asemenea, vă spune când ajunge o remediere sau o nouă versiune. SP Flash Tool se află în setul de instrumente Updater pentru cazurile rare, Updater nu poate finaliza. Pașii de mai jos sunt o excepție.

## Pentru ce este acest instrument

Updater afișează playerul pentru dvs. SP Flash Tool este același motor, fără balustrade. Folosiți-l atunci când Updater nu pornește, când playerul nu se va conecta sau când vă cunoașteți cum să vă descurcați într-un fișier scatter.Încercați mai întâi Updater. Pentru cele mai multe instalări și cele mai multe recuperări, ghidat [Ruta de actualizare](guide_ro.html) este alegerea mai sigură. Folosiți SP Flash Tool când știți de ce aveți nevoie de el și păstrați o baterie încărcată plus un cablu de date USB gata.

## Instrument flash pentru Innioasis jucători

Innioasis Updater este instrumentul flash pentru Innioasis jucători. Instalează software-ul oficial, actualizează și restaurează pachetele prin fluxul potrivit modelului și vă păstrează muzica și setările.

### Innioasis Y1 instrument flash

Alegeți versiunea Y1 în Updater, apoi conectați playerul oprit când aplicația vă solicită. Aceleași pachete Y1 funcționează cu SP Flash Tool atunci când aveți nevoie de ruta manuală.

### Innioasis Y2 instrument flash

Alegeți o versiune listată pentru Y2. Pachetele Y2 nu sunt interschimbabile cu pachetele Y1, așa că verificați modelul înainte de a începe.

## Instrument flash pentru Timmkoo jucători

Timmkoo jucători folosesc același flux de instalare a programului de actualizare. Citește direct pachetele ZIP și RAR ale lui Timmkoo, deci nu aveți nevoie de un instrument flash separat sau de fișier scatter.

### Timmkoo Q5 instrument flash

Selectați modelul Q5 în Updater, alegeți pachetul Timmkoo, apoi rulați Instalare/Restaurare și conectați playerul la solicitare.

### Timmkoo Q3 și Q3E instrument flash

Intrarea Q3 acoperă Q3 și Q3E deopotrivă. Updater alege fișierele care se potrivesc din pachetul pe care îl publică proiectul.

### Timmkoo A5 instrument flash

Selectați modelul A5 înainte de a alege un pachet, apoi urmați același prompt de instalare.

## Unde îl pune Updater

SP Flash Tool este livrat cu folderul de instalare a programului de actualizare, nu ca o descărcare separată. Deschide-l de acolo când ai nevoie.

### Windows

Deschideți folderul de instalare Updater și rulați `flash_tool.exe`. Dosarul este de obicei sub `%LOCALAPPDATA%\Innioasis Updater`. Un folder Toolkit cu o comandă rapidă SP Flash Tool este inclus în unele setări.

### Linux

Rulați pachetul `flash_tool` binar în dosarul aplicației Updater pe x86 / x86_64. Programul de instalare a proiectului pregătește USB permisiuni cu reguli udev, astfel încât jucătorul ar trebui să apară atunci când este conectat.

### macOS

SP Flash Tool nu este inclus pe macOS. Updater folosește în schimb ruta MTKClient acolo. Utilizați [instalare ghidată](guide_ro.html) pe un Mac și păstrați SP Flash Tool pentru o mașină Windows sau Linux.

Instrumentul este livrat cu agentul de descărcare MediaTek și configurația specifică modelului, astfel încât nu trebuie să colectați fișiere DA sau să împrăștiați din altă parte.

## Pregătiți firmware-ul
  - Luați eliberarea de la care doriți [Descărcări de firmware](firmware_ro.html). Alege `rom.zip` pentru un Y1 sau `rom_y2.zip` pentru un Y2.
  - Extrageți fișierul ZIP în propriul folder. Windows poate folosi Extract All. Pe Linux, utilizați managerul de arhive sau `unzip` într-un terminal.
  - Verificați dacă fișierul scatter se află în folderul extras. De obicei este numit `MT6572_Android_scatter.txt` pentru Y1 pachete și `MT6582_Android_scatter_def.txt` pentru Y2 pachete, deși o ediție îl poate denumi după proiectul său.
Păstrați modelele separate. Scatter-ul Y1 descrie un dispozitiv MT6572, iar Y2 scatter descrie un dispozitiv MT6582. Intermiterea cu cea greșită este modul în care jucătorii sunt blocați. Dacă împrăștierea din interiorul ZIP nu se potrivește cu modelul dvs., opriți-vă și utilizați în schimb un pachet listat pentru modelul dvs.

## Încărcați scatter și flash
  - Deschideți SP Flash Tool din folderul de instalare a programului de actualizare.
  - În fila Descărcare, faceți clic Alege lângă Scatter-loading File și selectați fișierul scatter din folderul extras. Lista de partiții se va completa.
  - Lăsați modul bliț activat Doar descărcare cu excepția cazului în care faceți în mod deliberat o recuperare completă, ceea ce are nevoie Actualizare firmware.
  - Faceți clic Descarcă. Instrumentul va aștepta jucătorul.
  - Opriți complet playerul, apoi conectați cablul de date USB. Pune playerul jos și nu-l mișca.
  - Așteptați bifa verde. Abia apoi deconectați cablul și porniți playerul.

Păstrați același cablu USB și reguli de sincronizare ca și traseul ghidat: un cablu de date, fără hub și conectați-vă numai când instrumentul este gata.

## Dacă nu clipește
  - Verificați dacă scatter-ul și ZIP se potrivesc cu modelul imprimat pe player.
  - Confirmați că playerul este complet oprit înainte de a vă conecta.
  - Pe Windows, confirmați driverul MediaTek instalat cu configurarea Updater; pe Linux, confirmați regulile udev din programul de instalare a proiectului.
  - Reconectați cablul numai când unealta așteaptă. O cursă portuară poate avea nevoie de o deconectare completă și un proaspăt Descarcă faceți clic.

Pentru orice dincolo de asta, deschide [depanare](troubleshooting_ro.html). Și amintiți-vă: Updater este încă ruta normală și [Y1](guides/restore-original-y1.html) şi [Y2](guides/restore-original-y2.html) Ghidurile de restaurare folosesc și el.

## A fost util?

Răspunsul tău ajută la îmbunătățirea acestui ghid.Da, mi s-a părut utilNu încă[Spune-ne cum ne putem îmbunătăți](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
