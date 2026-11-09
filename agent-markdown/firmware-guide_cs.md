---
title: "Průvodce instalací firmwaru a obnovením zásob | Innioasis Updater CE - Innioasis Stažení firmwaru"
description: "Nainstalujte vlastní firmware nebo obnovte oficiální tovární firmware na Innioasis Y1, Y2, G1, G3, G5, R1, PR1 a Timmkoo Q5, Q3 pomocí Innioasis Updater CE."
language: "cs"
source: "https://innioasis.app/firmware-guide_cs.html"
---

# Průvodce instalací firmwaru a obnovením zásob | Innioasis Updater CE - Innioasis Stažení firmwaru

Průvodce instalací firmwaru a obnovou zásob

# Nainstalujte nebo obnovte firmware na vašem zařízení

Vyberte model vytištěný na přehrávači. Poté postupujte podle kroků v Updater CE. O zbytek se postará.[Získat Updater CE](guide_cs.html#platform)[Procházet archiv firmwaru](firmware_cs.html)[Řešení problémů](troubleshooting_cs.html)

Vyberte model vytištěný na přehrávači a požadovaný software a otevřete tuto příručku. [Procházejte software a firmware podle modelu](firmware_cs.html).

## 

[Získat Updater CE](guide_cs.html#download-updater)[Kompletní písemný tutoriál](guide_cs.html)

## Získejte Innioasis Updater CE

Zde je místo, kde začít, pokud ještě nemáte Updater CE.Získejte to na Updater CEs řízenou instalací

### Windows

Stáhněte si instalační program, otevřete jej a postupujte podle pokynů k nastavení.[Stáhněte a nainstalujte ovladač](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Stáhněte si aplikaci a ovladače](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Blokován Edge?](#)

Pokud vám systém Windows zabrání spouštění aplikace nebo ji nelze spustit, otevřete Nastavení, klikněte na Soukromí a zabezpečení → Zabezpečení Windows → Ovládání aplikací a prohlížeče a vypněte Smart App Control. [Windows nespustí aplikaci? Pomoc](#smart-app-control)

Po instalaci budete muset restartovat počítač, aby fungoval.

### macOS

Stáhněte si aplikaci a přesuňte ji do sekce Aplikace. Pokud to macOS zablokuje, otevřete Nastavení systému, poté Soukromí a zabezpečení a klikněte na Přesto otevřít. [Jak to funguje](https://support.apple.com/en-gb/102445#openanyway)[Stáhnout Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Stáhněte si AppImage pro systémy Intel a AMD, udělejte jej spustitelný a spusťte jej.[Stáhněte si AppImage pro Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Poznámky k nastavení Linuxu](drivers_cs.html#linux)Jiná platforma?

Potřebujete delší poznámky k nastavení počítače? Otevřete [Windows](drivers_cs.html#windows) nebo [Linux](drivers_cs.html#linux) průvodce nastavením.

## Vraťme se k původnímu softwaru

Chcete-li se vrátit, vyberte svůj model, vyberte si Původní software, pak běžte Nainstalovat / Obnovit. To je vše. Updater za vás nahradí systémový software.[Průvodce obnovením Y1](guides/restore-original-y1.html)[Průvodce obnovením Y2](guides/restore-original-y2.html)

## Softwarové průvodce podle modelu

Vyberte svůj model a otevřete průvodce pro váš software.

### Innioasis Y1

Software pro Y1:

### Innioasis Y2

Software pro Y2:

Poznámka ke dvěma nástrojům

## Který nástroj bych měl použít?

Innioasis Updater CE je nejbezpečnější způsob aktualizace přehrávače. Udržuje vaši hudbu, videa a párování Bluetooth. Oznámí vám, kdy jsou aktualizace připraveny. Běží na Windows, MacOS a Linux. Innioasis Universal Flash Tool vymaže váš přehrávač a funguje na menším počtu počítačů.[Otevřít úplné srovnání](updater-comparison_cs.html)

### Windows nespustí aplikaci? Jak vypnout Smart App Control

Windows Defender SmartScreen nebo Smart App Control mohou blokovat nově stažené komunitní aplikace dříve, než se rozšíří reputace signatur. Smart App Control v současné době ovlivňuje oblíbené aplikace, jako je Epic Overlay Service (používaná Fortnite) – Updater CE je bezpečný a ověřený pro použití. Vypnutí Smart App Control umožní Updater CE normálně otevřít a spustit.
  - Otevřít Nastavení na vašem počítači se systémem Windows (stiskněte Win + I).
  - Klikněte Soukromí a zabezpečení v levém postranním panelu a poté klikněte Windows Security.
  - Klikněte Ovládání aplikací a prohlížeče.
  - Pod Inteligentní ovládání aplikací, klikněte Nastavení Smart App Control.
  - Nastavte přepínač na Vypnuto aby bylo možné spustit Updater CE.

Blokován Edge? Pokud Microsoft Edge blokuje stahování samotné, klikněte na tlačítko Další možnosti (…) → Nechat → Zobrazit více → Stejně si ponechat.

Později znovu povolte Smart App Control: Když budete chtít Smart App Control znovu zapnout, můžete jej znovu povolit prostřednictvím registru Windows pod `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` nastavením `VerifiedAndReputablePolicyState` do `1` (Zapnuto) nebo `2` (Režim hodnocení) a restartování.Zavřít nápovědu

## Bylo to užitečné?

Vaše odpověď pomáhá zlepšit tuto příručku.Ano, přišlo mi to užitečnéJeště ne[Dejte nám vědět, jak se můžeme zlepšit](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
