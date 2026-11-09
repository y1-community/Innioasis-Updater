---
title: "Innioasis Y1 e Y2 USB driver | Driver Windows e permessi Linux - Innioasis Aggiornamento"
description: "Configura il tuo computer per Innioasis Updater: driver Windows MediaTek e autorizzazioni Linux USB, oltre a correzioni di cavi e tempistiche."
language: "it"
source: "https://innioasis.app/drivers_it.html"
---

# Innioasis Y1 e Y2 USB driver | Driver Windows e permessi Linux - Innioasis Aggiornamento

Configurazione del computer

# Prepara il computer prima del lettore.

La maggior parte dei problemi di connessione derivano dal driver, dalle autorizzazioni, dal cavo o dai tempi. Windows richiede l'installazione del driver MediaTek. Linux ha bisogno delle giuste autorizzazioni USB. Trova la tua piattaforma qui sotto.[Ottieni Updater CE](guide_it.html#platform)[Risoluzione dei problemi](troubleshooting_it.html)

## Windows
  - Scarica il programma di installazione del driver MediaTek di seguito.
  - Esegui il programma di installazione e consenti a Windows di installare il driver.
  - Riavviare il computer.
  - Aprire Updater CE e attendere la richiesta di connessione prima di collegare il lettore spento.

Alcuni sistemi Windows bloccano il driver tramite l'isolamento del core (integrità della memoria). Se Updater CE non riesce ancora a vedere il lettore dopo il riavvio, disattivare l'integrità della memoria in Sicurezza di Windows, riavviare e reinstallare il driver. Riattiva l'impostazione al termine, se il sistema lo consente.

Windows non avvia l'app? Se Sicurezza di Windows o Controllo intelligente delle app impediscono l'apertura di Updater CE, aprilo Impostazioni (premere Win + I) → Privacy e sicurezza → Windows Security → Controllo di app e browser → Impostazioni di controllo intelligente delle app e impostarlo su Spento. Controllo app intelligente sta attualmente influenzando applicazioni diffuse come Epic Overlay Service (utilizzato da Fortnite) — Updater CE è sicuro e verificato. Per riattivarlo in seguito, imposta `VerifiedAndReputablePolicyState` a `1` (Attivo) o `2` (Modalità di valutazione) sotto `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` nell'editor del Registro di sistema.[Scarica il driver di Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Torna alla guida principale](guide_it.html#windows) · [Download di software](firmware_it.html)

## Autorizzazioni Linux USB.

Linux ha bisogno che il tuo account utente possa comunicare con il chip MediaTek USB all'interno del lettore. Updater CE di solito risolve questo problema durante l'installazione e la stessa autorizzazione copre SP Flash Tool, quindi consideralo come un passaggio di correzione piuttosto che come una fase normale.
  - Esegui Updater CE come utente normale, non come root. Il programma di installazione richiede l'accesso come amministratore solo quando ne ha bisogno.
  - Controlla che il giocatore sia visibile. Spegni il lettore, collega il cavo ed esegui il comando lsusb in un terminale. Un lettore connesso viene visualizzato come dispositivo MediaTek con l'ID fornitore 0e8d.
`lsusb`
  - Se appare in lsusb ma Innioasis Updater CE o SP Flash Tool dice che l'autorizzazione è stata negata o non è possibile aprire la porta, l'utente non ha accesso al dispositivo USB. La stessa regola udev copre entrambi gli strumenti, quindi aggiungine una che consenta al gruppo di utenti di leggerla.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Salva quella riga in un nuovo file chiamato /etc/udev/rules.d/51-innioasis.rules, quindi esegui:`sudo udevadm control --reload && sudo udevadm trigger`
  - Scollega completamente il lettore, ricollegalo e riprova l'installazione.
  - Se SP Flash Tool segnala un'autorizzazione seriale o una competizione tra porte, scollega completamente e riconnetti solo quando richiesto.
Non improvvisare gli offset del flash.Se passi a uno strumento di ripristino manuale, utilizza i file e la configurazione specifica del modello forniti con il progetto.

[Torna alla guida principale](guide_it.html#linux) · [Download di software](firmware_it.html) · [SP Flash Tool guida](sp-flash-tool_it.html)

## Cavo e temporizzazione
  - Utilizzare un cavo dati USB noto.
  - Evitare gli hub durante la risoluzione dei problemi.
  - Spegnere completamente il modello corretto.
  - Connettiti solo quando richiesto.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
