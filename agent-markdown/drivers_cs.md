---
title: "Innioasis Y1 a Y2 USB řidiči | Ovladač Windows a oprávnění pro Linux - Innioasis Updater"
description: "Nastavte svůj počítač pro Innioasis Updater: Ovladač Windows MediaTek a oprávnění Linux USB – plus opravy kabelu a časování."
language: "cs"
source: "https://innioasis.app/drivers_cs.html"
---

# Innioasis Y1 a Y2 USB řidiči | Ovladač Windows a oprávnění pro Linux - Innioasis Updater

Nastavení počítače

# Před přehrávačem připravte počítač.

Většina problémů s připojením pochází z ovladače, oprávnění, kabelu nebo načasování. Windows potřebuje nainstalovaný ovladač MediaTek. Linux potřebuje správná USB oprávnění. Níže najděte svou platformu.[Získat Updater CE](guide_cs.html#platform)[Řešení problémů](troubleshooting_cs.html)

## Windows
  - Níže si stáhněte instalační program ovladače MediaTek.
  - Spusťte instalační program a nechte Windows nainstalovat ovladač.
  - Restartujte počítač.
  - Před připojením vypnutého přehrávače otevřete Updater CE a počkejte na výzvu k připojení.

Některé systémy Windows blokují ovladač prostřednictvím izolace jádra (integrita paměti). Pokud Updater CE nevidí přehrávač ani po restartu, vypněte integritu paměti v Zabezpečení systému Windows, restartujte a znovu nainstalujte ovladač. Po dokončení nastavení znovu zapněte, pokud to váš systém umožňuje.

Windows nespustí aplikaci? Pokud zabezpečení Windows nebo Smart App Control zastaví otevření Updater CE, otevřete Nastavení (stiskněte Win + I) → Soukromí a zabezpečení → Windows Security → Ovládání aplikací a prohlížeče → Nastavení Smart App Control a nastavte jej na Vypnuto. Smart App Control v současné době ovlivňuje oblíbené aplikace, jako je Epic Overlay Service (používaná Fortnite) – Updater CE je bezpečný a ověřený pro použití. Chcete-li později znovu aktivovat, nastavte `VerifiedAndReputablePolicyState` do `1` (Zapnuto) nebo `2` (Režim hodnocení) pod `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` v Editoru registru.[Stáhněte si ovladač pro Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Zpět k hlavnímu průvodci](guide_cs.html#windows) · [Software ke stažení](firmware_cs.html)

## Oprávnění Linux USB

Linux potřebuje, aby váš uživatelský účet mohl komunikovat s čipem MediaTek USB uvnitř přehrávače. Updater CE to obvykle vyřeší během instalace a stejné oprávnění se vztahuje na SP Flash Tool, takže to považujte spíše za krok opravy než za normální fázi.
  - Spusťte Updater CE jako normální uživatel, ne jako root. Instalační program požádá o přístup správce pouze tehdy, když jej potřebuje.
  - Zkontrolujte, zda je přehrávač vůbec vidět. Vypněte přehrávač, připojte kabel a spusťte příkaz lsusb v terminálu. Připojený přehrávač se zobrazí jako zařízení MediaTek s ID dodavatele 0e8d.
`lsusb`
  - Pokud se objeví v lsusb, ale Innioasis Updater CE nebo SP Flash Tool říká, že oprávnění bylo odepřeno nebo nemůže otevřít port, váš uživatel nemá přístup k zařízení USB. Stejné pravidlo udev pokrývá oba nástroje, takže přidejte jeden, který umožní skupině uživatelů jej číst.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Uložte tento řádek do nového souboru s názvem /etc/udev/rules.d/51-innioasis.rules a poté spusťte:`sudo udevadm control --reload && sudo udevadm trigger`
  - Přehrávač zcela odpojte, znovu zapojte a zkuste znovu nainstalovat.
  - Pokud SP Flash Tool hlásí sériové oprávnění nebo závodění portů, odpojte jej úplně a znovu připojte, až budete vyzváni.
Neimprovizujte offsety blesku.Pokud přejdete na nástroj ruční obnovy, použijte soubory a konfiguraci specifickou pro model dodané s projektem.

[Zpět k hlavnímu průvodci](guide_cs.html#linux) · [Software ke stažení](firmware_cs.html) · [SP Flash Tool průvodce](sp-flash-tool_cs.html)

## Kabel a časování
  - Použijte známý datový kabel USB.
  - Při odstraňování problémů se vyhněte rozbočovačům.
  - Úplně vypněte správný model.
  - Připojte se pouze na výzvu.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
