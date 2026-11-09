---
title: "Problemi di avvio delle app Windows 10/11 e soluzione alternativa al controllo intelligente delle app - Innioasis Aggiornamento"
description: "Se Windows 10/11 o Smart App Control ti impediscono di avviare l&#39;app, segui la soluzione alternativa qui."
language: "it"
source: "https://innioasis.app/notices/2026-11-07-codesigning_it.html"
---

# Problemi di avvio delle app Windows 10/11 e soluzione alternativa al controllo intelligente delle app - Innioasis Aggiornamento

Dal 25-10-2026 · al 31-12-2026 · Modelli: Y1,Y2

# Problemi di avvio delle app di Windows 10/11 e soluzione alternativa al controllo intelligente delle app

Se Windows 10/11 o Smart App Control ti impediscono di avviare l'app, segui la soluzione alternativa qui.

Dal 25-10-2026 · al 31-12-2026 · Modelli: Y1,Y2

Sono state inviate a Microsoft segnalazioni di falsi positivi per `installer.exe` e `InnioasisUpdater.exe` e hai eseguito l'azione, ma se Windows Endpoint Protection o Smart App Control stanno ancora bloccando l'applicazione sul tuo computer, utilizza questa soluzione alternativa:

### Soluzione temporanea: disattivare il controllo intelligente delle app
  - Apri Windows Impostazioni (premere `Win + I`).
  - Vai a Privacy e sicurezza > Sicurezza di Windows > Controllo di app e browser.
  - Sotto Controllo intelligente delle app, fare clic Impostazioni di controllo intelligente delle app.
  - Imposta Controllo app intelligente su Spento. Ciò consente immediatamente l'apertura e l'esecuzione dell'app.

Se Windows o Edge ti impediscono di scaricare Updater CE, fai clic su più opzioni (…) Poi Mantenere > Mostra di più > Tienilo comunque.

### Riattivazione del controllo intelligente delle app

Una volta terminato l'aggiornamento delle definizioni dei falsi positivi sul computer, puoi riattivare Smart App Control tramite il registro di Windows:
  - Premere Tasto Windows + R, tipo `regedit`e premi Invio per aprire l'editor del Registro di sistema come amministratore.
  - Vai a: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (O `Policies`).
  - Individuare `VerifiedAndReputablePolicyState` nel riquadro di destra.
  - Fare doppio clic `VerifiedAndReputablePolicyState` e modificarne i dati valore in:

  - `1` = Attivo (imposto)
  - `2` = Modalità di valutazione

  - Fare clic su OK, chiudere l'editor del Registro di sistema e riavviare il computer.

[Consulta il report installer.exe a Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Consulta il report InnioasisUpdater.exe a Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Apri la pagina collegata](https://innioasis.app/notices.html)

[← Tutti gli avvisi](index_it.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
