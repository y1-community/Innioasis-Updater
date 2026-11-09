---
title: "Jak obnovit nespouštěcí MediaTek přehrávač po selhání klienta MTK · Innioasis Komunita"
description: "Podrobný průvodce odblokováním a obnovením nespouštěcích Innioasis Y1, Y2, G1, Timmkoo a MediaTek přehrávačů po přerušení MTKclient na Linuxu nebo macOS."
language: "cs"
source: "https://innioasis.app/recover-non-booting-device_cs.html"
---

# Jak obnovit nespouštěcí MediaTek přehrávač po selhání klienta MTK · Innioasis Komunita

Odstraňování problémů a obnova zařízení

# Obnova nespouštěcího zařízení po blikání klienta MTK

Pokud se vaše zařízení Innioasis Y1, Y2 nebo MediaTek nezapne nebo zobrazuje černou obrazovku po blikání pomocí MTKclient na macOS nebo Linux, nepropadejte panice. Hardwarová bootROM (BROM) je trvalá a nelze ji zničit.

## Proč se MTKclient může zastavit nebo zanechat černou obrazovku

MTKclient spoléhá na softwarové exploity (kamakiri / amonet), aby obešel DA autentizaci a nezpracovanou USB komunikaci přes libusb. Na systémech macOS a Linux ARM64:
  - USB latence handshake nebo časové limity portů na macOS mohou zastavit vkládání dat DA uprostřed přenosu.
  - Chybějící nebo neúplné hlavičky oddílů ponechávají bootloader (preloader / lk) ve stavu, kdy nereaguje.
  - Přehrávač se zdá být zcela mrtvý – žádná LED, žádná ikona nabíjení, žádné podsvícení obrazovky.

I v tomto stavu se čipová sada MediaTek vrátí zpět Režim BROM (USB VID 0e8d, PID 0003), připraveno k oficiálnímu obnovení nízké úrovně.

## Definitivní metoda obnovy: SP Flash Tool Engine v Updater CE

Nejbezpečnějším a nejspolehlivějším způsobem, jak obnovit zděného hráče, je použití Aktualizátor CE nakonfigurován s úředníkem SP Flash Tool backend.

### Přesné kroky v Updater CE:
  - Otevřít Aktualizátor CE.
  - Klikněte Nastavení v levém postranním navigačním panelu.
  - Přejděte dolů do části Upřesnit a povolte Zobrazit Pokročilá nastavení.
  - Pod Metoda instalace (nebo Flashing Engine pro instalační program MediaTek), vyhledejte Flash metoda rozevírací seznam.
  - Změňte výběr z Auto (doporučeno) nebo MTKClient do SP Flash Tool.
  - Potvrďte výzvu a vraťte se do hlavního instalačního postupu.

## Požadavky na architekturu platformy a OS pro SP Flash Tool

MediaTek úředník `SP Flash Tool` binární je kompilován nativně jako an x86_64 Binární ELF pro Linux a a PE32+ spustitelný pro Windows x64.Důležitá poznámka k hardwaru pro uživatele macOS a ARM64 Linux:
 Protože MediaTek nezkompiluje SP Flash Tool pro macOS (Darwin) nebo Linux ARM64 (aarch64), uživatelé macOS a uživatelé Linuxu ARM64 (jako je Raspberry Pi nebo Apple Silicon se systémem Asahi Linux) musí svůj přehrávač připojit k: 
  - An x64 počítač se systémem Windows (Windows 10/11 64-bit), popř
  - An x86_64 počítač se systémem Linux (Ubuntu, Debian, Fedora, Arch 64-bit).

## Proces odblokování hardwaru krok za krokem
  - Odpojit přehrávač: Úplně odpojte kabel USB od přehrávače a počítače.
  - Tvrdé vypnutí: Podržte tlačítko Napájení (nebo Napájení + Snížení hlasitosti) po dobu 15 sekund, abyste se ujistili, že je čipset zcela vypnutý a neuvízl ve smyčce s nízkou spotřebou energie USB.
  - Spusťte Updater CE v režimu SP Flash Tool: Vyberte model vašeho zařízení (např. Innioasis Y1 nebo Innioasis Y2) a vyberte si Původní software obnovit skladové oddíly.
  - Zahájení instalace / obnovení: Klikněte Nainstalovat / Obnovit v Updater CE. Počkejte, až se zobrazí výzva ke stavu Čekání na hráče...
  - Vložte USB kabel ke spuštění BROM: Když je zařízení vypnuté, zapojte kabel USB přímo do portu USB na vysokorychlostní základní desce (vyhněte se nenapájeným rozbočovačům USB).
  - Systém detekuje port MediaTek VCOM, nasadí agenta stahování (DA), přepíše tabulky oddílů a obnoví všechny obrazy firmwaru čistě.

## Permutace podle modelu a operačního systému

| Model | Neúspěšná platforma | Doporučené nastavení obnovení | Motor a režim |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Počítač se systémem Windows x64 / Linux x86_64 | SP Flash Tool + Y1 Sklad ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 nebo Windows x64 PC | SP Flash Tool + DA komunity |
| Innioasis Y2 | macOS (klient MTK se zastavil) | Počítač se systémem Windows x64 / Linux x86_64 | SP Flash Tool + Y2 Scatter Recovery |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 PC s ovladači VCOM | SP Flash Tool + Firmware z výroby |
| Mechen H1 / Timmkoo A5 | Jakákoli platforma | Windows x64 nebo Linux x86_64 PC | SP Flash Tool + Scatter soubor |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
