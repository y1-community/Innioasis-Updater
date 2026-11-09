---
title: "Innioasis Y1 și Y2 USB drivere | Driver Windows și permisiuni Linux - Innioasis Updater"
description: "Configurați computerul pentru Innioasis Updater: driverul Windows MediaTek și permisiunile Linux USB - plus remedieri de cablu și sincronizare."
language: "ro"
source: "https://innioasis.app/drivers_ro.html"
---

# Innioasis Y1 și Y2 USB drivere | Driver Windows și permisiuni Linux - Innioasis Updater

Configurare computer

# Pregătiți computerul înaintea playerului.

Cele mai multe probleme de conectare provin de la driver, permisiuni, cablu sau sincronizare. Windows are nevoie de driverul MediaTek instalat. Linux are nevoie de permisiunile USB potrivite. Găsiți platforma dvs. mai jos.[Obține Updater CE](guide_ro.html#platform)[Depanare](troubleshooting_ro.html)

## Windows
  - Descărcați programul de instalare a driverului MediaTek de mai jos.
  - Rulați programul de instalare și permiteți Windows să instaleze driverul.
  - Reporniți computerul.
  - Deschideți Updater CE și așteptați solicitarea de conectare înainte de a conecta playerul oprit.

Unele sisteme Windows blochează driverul prin izolarea Core (Integritatea memoriei). Dacă Updater CE tot nu poate vedea playerul după o repornire, dezactivați Integritatea memoriei în Windows Security, reporniți și reinstalați driverul. Reactivați setarea când ați terminat, dacă sistemul dvs. permite acest lucru.

Windows nu va lansa aplicația? Dacă Windows Security sau Smart App Control oprește deschiderea Updater CE, deschideți Setări (apăsați Win + I) → Confidențialitate și securitate → Windows Security → Controlul aplicației și browserului → Setări Smart App Control și setați-l la Oprit. Smart App Control afectează în prezent aplicațiile populare, cum ar fi Epic Overlay Service (utilizat de Fortnite) - Updater CE este sigur și verificat pentru utilizare. Pentru a reactiva mai târziu, setați `VerifiedAndReputablePolicyState` la `1` (Activat) sau `2` (Modul de evaluare) sub `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` în Editorul Registrului.[Descărcați driverul Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Înapoi la ghidul principal](guide_ro.html#windows) · [Descărcări de software](firmware_ro.html)

## Permisiuni Linux USB.

Linux are nevoie ca contul dvs. de utilizator să aibă permisiunea de a vorbi cu cipul MediaTek USB din interiorul playerului. Updater CE rezolvă de obicei acest lucru în timpul instalării și aceeași permisiune acoperă SP Flash Tool, așa că tratați acest lucru ca un pas de remediere mai degrabă decât o etapă normală.
  - Rulați Updater CE ca utilizator normal, nu ca root. Programul de instalare solicită acces de administrator numai atunci când are nevoie de el.
  - Verificați dacă jucătorul este văzut. Opriți playerul, conectați cablul și rulați comanda lsusb într-un terminal. Un jucător conectat apare ca un dispozitiv MediaTek cu ID-ul furnizorului 0e8d.
`lsusb`
  - Dacă apare în lsusb, dar Innioasis Updater CE sau SP Flash Tool spune permisiunea refuzată sau nu poate deschide portul, utilizatorul dvs. nu are acces la dispozitivul USB. Aceeași regulă udev acoperă ambele instrumente, așa că adăugați unul care să le permită grupului de utilizatori să o citească.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Salvați acea linie într-un fișier nou numit /etc/udev/rules.d/51-innioasis.rules, apoi rulați:`sudo udevadm control --reload && sudo udevadm trigger`
  - Deconectați complet playerul, conectați-l din nou și încercați din nou instalarea.
  - Dacă SP Flash Tool raportează o permisiune serială sau o cursă de porturi, deconectați complet și reconectați numai când vi se solicită.
Nu improvizați decalaje bliț.Dacă treceți la un instrument de recuperare manuală, utilizați fișierele și configurația specifică modelului livrate împreună cu proiectul.

[Înapoi la ghidul principal](guide_ro.html#linux) · [Descărcări de software](firmware_ro.html) · [SP Flash Tool ghid](sp-flash-tool_ro.html)

## Cablu și sincronizare
  - Utilizați un cablu de date USB cunoscut.
  - Evitați hub-urile în timpul depanării.
  - Opriți complet modelul corect.
  - Conectați-vă numai la solicitare.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
