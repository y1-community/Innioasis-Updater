---
title: "Ghid de instalare a firmware-ului și restaurare stoc | Innioasis Updater CE - Innioasis Descărcări de firmware"
description: "Instalați firmware personalizat sau restaurați firmware-ul oficial din fabrică pe Innioasis Y1, Y2, G1, G3, G5, R1, PR1 și Timmkoo Q5, Q3 cu Innioasis Updater CE."
language: "ro"
source: "https://innioasis.app/firmware-guide_ro.html"
---

# Ghid de instalare a firmware-ului și restaurare stoc | Innioasis Updater CE - Innioasis Descărcări de firmware

Ghid de instalare a firmware-ului și restaurare stoc

# Instalați sau restaurați firmware-ul pe dispozitivul dvs

Alegeți modelul imprimat pe player. Apoi urmați pașii din Updater CE. Se ocupă de restul.[Obține Updater CE](guide_ro.html#platform)[Răsfoiți Arhiva Firmware](firmware_ro.html)[Depanare](troubleshooting_ro.html)

Alegeți modelul imprimat pe player și software-ul dorit, apoi deschideți acest ghid. [Răsfoiți software-ul și firmware-ul stoc după model](firmware_ro.html).

## 

[Obține Updater CE](guide_ro.html#download-updater)[Tutorial scris complet](guide_ro.html)

## Obțineți Innioasis Updater CE

Iată de unde să începeți dacă nu aveți deja Updater CE.Obțineți-l pe Updater CEcu instalare ghidată

### Windows

Descărcați programul de instalare, deschideți-l și urmați instrucțiunile de configurare.[Descărcați și instalați driverul](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Descărcați aplicația și driverele](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Blocat de Edge?](#)

Dacă Windows vă împiedică să rulați aplicația sau nu o lansează, deschideți Setări, faceți clic pe Confidențialitate și securitate → Securitate Windows → Control aplicație și browser și dezactivați Controlul aplicației inteligente. [Windows nu va lansa aplicația? Ajutor](#smart-app-control)

Va trebui să reporniți computerul după instalare pentru ca acesta să funcționeze.

### macOS

Descărcați aplicația și mutați-o în Aplicații. Dacă macOS îl blochează, deschide Setări sistem, apoi Confidențialitate și securitate și dă clic pe Deschide oricum. [Cum funcționează asta](https://support.apple.com/en-gb/102445#openanyway)[Descărcați Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Descărcați AppImage pentru sistemele Intel și AMD, faceți-l executabil și rulați-l.[Descărcați AppImage pentru Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Note de configurare Linux](drivers_ro.html#linux)O altă platformă?

Aveți nevoie de note mai lungi de configurare a computerului? Deschideți [Windows](drivers_ro.html#windows) sau [Linux](drivers_ro.html#linux) ghid de configurare.

## Revenind la software-ul original

Pentru a reveni, alege-ți modelul, alege Software original, apoi fugi Instalează / Restaurează. Asta este tot. Updater înlocuiește software-ul de sistem pentru dvs.[Ghid de restaurare Y1](guides/restore-original-y1.html)[Ghid de restaurare Y2](guides/restore-original-y2.html)

## Ghiduri software după model

Alegeți modelul dvs., apoi deschideți ghidul software-ului dvs.

### Innioasis Y1

Software pentru Y1:

### Innioasis Y2

Software pentru Y2:

O notă despre cele două instrumente

## Ce instrument ar trebui să folosesc?

Innioasis Updater CE este cel mai sigur mod de a vă actualiza playerul. Vă păstrează muzica, videoclipurile și împerecherile Bluetooth. Vă spune când actualizările sunt gata. Funcționează pe Windows, macOS și Linux. Innioasis Universal Flash Tool șterge playerul și funcționează pe mai puține computere.[Deschideți comparația completă](updater-comparison_ro.html)

### Windows nu va lansa aplicația? Cum să dezactivezi Smart App Control

Windows Defender SmartScreen sau Smart App Control pot bloca aplicațiile comunitare recent descărcate înainte ca reputația semnăturii să se propage. Smart App Control afectează în prezent aplicațiile populare, cum ar fi Epic Overlay Service (utilizat de Fortnite) - Updater CE este sigur și verificat pentru utilizare. Dezactivarea Smart App Control permite ca Updater CE să se deschidă și să ruleze normal.
  - Deschide Setări pe computerul dvs. cu Windows (apăsați Win + I).
  - Faceți clic Confidențialitate și securitate în bara laterală din stânga, apoi faceți clic Windows Security.
  - Faceți clic Controlul aplicației și browserului.
  - Sub Control inteligent al aplicației, faceți clic Setări Smart App Control.
  - Setați comutatorul la Oprit pentru a permite lansarea Updater CE.

Blocat de Edge? Dacă Microsoft Edge blochează descărcarea în sine, faceți clic pe butonul Mai multe opțiuni (…) → Păstrează → Arată mai multe → Păstrați oricum.

Reactivarea Smart App Control mai târziu: Când doriți să reactivați Smart App Control, îl puteți reactiva prin Registrul Windows de sub `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` prin setare `VerifiedAndReputablePolicyState` la `1` (Activat) sau `2` (Mod de evaluare) și repornire.Ajutor aproape

## A fost util?

Răspunsul tău ajută la îmbunătățirea acestui ghid.Da, mi s-a părut utilNu încă[Spune-ne cum ne putem îmbunătăți](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
