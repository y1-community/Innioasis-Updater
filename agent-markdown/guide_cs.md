---
title: "Začínáme s Innioasis Updater CE | Nainstalujte nebo obnovte firmware na libovolném přehrávači Innioasis nebo Timmkoo - Innioasis Updater"
description: "Stáhněte si Innioasis Updater CE pro Windows, macOS nebo Linux a poté nainstalujte nebo obnovte firmware na libovolném přehrávači Innioasis nebo Timmkoo v několika krocích s průvodcem."
language: "cs"
source: "https://innioasis.app/guide_cs.html"
---

# Začínáme s Innioasis Updater CE | Nainstalujte nebo obnovte firmware na libovolném přehrávači Innioasis nebo Timmkoo - Innioasis Updater

Rychlý start

# Začínáme s Innioasis Updater CE

Funguje se všemi audio přehrávači Innioasis a Timmkoo. Nainstalujte do počítače Innioasis Updater CE, vyberte model a požadovaný software a postupujte podle pokynů.

## 

[Získat Updater CE](guide_cs.html#download-updater)[Kompletní písemný tutoriál](guide_cs.html)

## Získejte Innioasis Updater CE

Innioasis Updater CE je aplikace, která instaluje oficiální aktualizace a komunitní software do vašeho přehrávače. Uchovává vaši hudbu a nastavení a běží na Windows, MacOS a Linux.

### Windows

Stáhněte si instalační program, spusťte jej a po dokončení restartujte počítač.[Získejte ovladače](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Stáhnout Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

Pokud vám systém Windows zabrání spouštění aplikace nebo ji nelze spustit, otevřete Nastavení, klikněte na Soukromí a zabezpečení → Zabezpečení Windows → Ovládání aplikací a prohlížeče a vypněte Smart App Control. Smart App Control v současnosti ovlivňuje oblíbené aplikace, jako je Epic Overlay Service (používaná Fortnite) – Updater CE je bezpečný a ověřený pro použití. [Windows nespustí aplikaci? Pomoc](#smart-app-control)

Po instalaci restartujte počítač. Pomoc pro řidiče je v [Poznámky k nastavení systému Windows](drivers_cs.html#windows).

### macOS[Stáhnout Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Pokud vám váš Mac zabrání v prvním spuštění aplikace, otevřete Nastavení systému, klikněte na Soukromí a zabezpečení, přejděte dolů na Zabezpečení a klikněte na [Přesto otevřít](https://support.apple.com/en-gb/102445#openanyway). Můžete také kliknout se stisknutou klávesou Ctrl (nebo pravým tlačítkem) na aplikaci ve Finderu a zvolit Otevřít.

Funguje na počítačích Intel a Apple Silicon Mac s macOS Monterey a novějšími.

### Linux

Stáhněte si AppImage pro systémy Intel a AMD, udělejte jej spustitelný a spusťte jej.[Stáhněte si AppImage pro Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Poznámky k nastavení Linuxu](drivers_cs.html#linux)Jiná platforma?

Potřebujete svůj přehrávač, datový kabel USB, který přenáší data (kabel pouze pro nabíjení nelze nainstalovat) a několik minut. Nechte kabel připojený, dokud Updater CE neoznámí, že je hotovo.

## Vyberte si svůj model a software
  - Model zařízení: vyberte model vytištěný na přehrávači, Y1 nebo Y2. Software vytvořený pro jeden model nelze nainstalovat na druhý.
  - Software a vydání: vyberte Original Software, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player nebo Koensayr, pokud je uveden pro váš model, a poté vyberte verzi. Stabilní je bezpečná volba.
  - Instalace: klikněte Nainstalovat / Obnovit, úplně vypněte přehrávač a připojte kabel USB pouze tehdy, když Updater CE požádá.
  - Dokončit: ponechte přehrávač a kabel v klidu, dokud se nezobrazí zpráva o úspěchu, poté odpojte a spusťte přehrávač.

Y1 hráči, kteří byli dodáni s originálním softwarem před verzí 2.0.0, potřebují Zařízení Type B. Všichni ostatní si ponechají výchozí Type A.Pokyny pro připojení aktualizace pro připojení vypnutého přehrávačePostupujte podle živé výzvy Updater CE pro váš model.

## Vraťme se k původnímu softwaru

Vlastní software je reverzibilní. V Updater CE vyberte svůj model, vyberte Původní software, vyberte stabilní vydání a poté spusťte Nainstalovat / Obnovit stejným způsobem. Není co ručně mazat.[Průvodce obnovením Y1](guides/restore-original-y1.html)[Průvodce obnovením Y2](guides/restore-original-y2.html)

Pokud se blesk zastaví před výzvou USB, zkontrolujte nejprve kabel, nastavení platformy a model. Viz [odstraňování problémů](troubleshooting_cs.html) pro opravy, [Y1 a Y2 průvodce obnovením](guides/recovery.html) pro poruchy napájení a kol a [SP Flash Tool](sp-flash-tool_cs.html) pro pokročilé zotavení.

## Softwarové průvodce podle modelu

Otevřete průvodce pro váš model a software, který jste si vybrali.

### Innioasis Y1

Software pro Y1:

### Innioasis Y2

Software pro Y2:

## Který nástroj bych měl použít?

Tato příručka používá Innioasis Updater 2.5.1, také nazývaný Updater CE. Udržuje vaše skladby, videa a párování Bluetooth v bezpečí. Oznámí vám, kdy jsou aktualizace připraveny. Innioasis Universal Flash Tool vymaže váš přehrávač a vyžaduje ruční kroky. [Porovnejte nástroje →](updater-comparison_cs.html)

## Windows nespustí aplikaci? Řešení Smart App Control

Windows Defender SmartScreen nebo Smart App Control mohou blokovat nově stažené komunitní aplikace dříve, než se rozšíří reputace signatur. Smart App Control v současné době ovlivňuje oblíbené aplikace, jako je Epic Overlay Service (používaná Fortnite) – Updater CE je bezpečný a ověřený pro použití. Vypnutí Smart App Control umožní Updater CE normálně otevřít a spustit.
  - Otevřít Nastavení na vašem počítači se systémem Windows (stiskněte Win + I).
  - Klikněte Soukromí a zabezpečení v levém postranním panelu a poté klikněte Windows Security.
  - Klikněte Ovládání aplikací a prohlížeče.
  - Pod Inteligentní ovládání aplikací, klikněte Nastavení Smart App Control.
  - Nastavte přepínač na Vypnuto aby bylo možné spustit Updater CE.

Staženo přes Edge? Pokud Edge blokuje stahování samotné, klikněte na tlačítko Další možnosti (…) → Nechat → Zobrazit více → Stejně si ponechat.

Později znovu povolte Smart App Control: Když budete chtít Smart App Control znovu zapnout, můžete jej znovu povolit prostřednictvím registru Windows pod `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` nastavením `VerifiedAndReputablePolicyState` do `1` (Zapnuto) nebo `2` (Režim hodnocení) a restartování.

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
