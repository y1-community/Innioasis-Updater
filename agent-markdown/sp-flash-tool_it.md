---
title: "SP Flash Tool per Innioasis e Timmkoo giocatori"
description: "Trova SP Flash Tool in bundle con Innioasis Updater su Windows e Linux, estrai rom.zip o rom_y2.zip e esegui il flashing di un Innioasis Y1 o Y2 con il file scatter corrispondente."
language: "it"
source: "https://innioasis.app/sp-flash-tool_it.html"
---

# SP Flash Tool per Innioasis e Timmkoo giocatori

Lampeggio manuale

# Strumento Flash per Innioasis e Timmkoo giocatori

SP Flash Tool entra in Innioasis Aggiornamento attivo [Windows](drivers_it.html#windows) e [Linux](drivers_it.html#linux). Ce l'hai già. Questa guida mostra il modo sicuro per utilizzarlo su un Innioasis Y1 o Y2 e il percorso di aggiornamento per Timmkoo giocatori.[Ritorna alla guida dell'Aggiornamento](guide_it.html)[Download del firmware](firmware_it.html)[Risoluzione dei problemi](troubleshooting_it.html)

Inizia con Innioasis Updater

## Updater fa l'intero lavoro in un unico passaggio

Updater esegue la maggior parte delle installazioni in un unico passaggio. Scegli il software, segui i passaggi e il gioco è fatto. Ti dice anche quando arriva una correzione o una nuova versione. SP Flash Tool è all'interno del Toolkit di Updater per i rari casi in cui Updater non riesce a terminare. I passaggi seguenti rappresentano un'eccezione.

## A cosa serve questo strumento

Updater esegue il flashing del lettore per te. SP Flash Tool è lo stesso motore, senza guard rail. Usalo quando l'Updater non si avvia, quando il lettore non si connette o quando sai come aggirare un file scatter.Prova prima l'Updater. Per la maggior parte delle installazioni e dei ripristini, il file guidato [Percorso di aggiornamento](guide_it.html) è la scelta più sicura. Utilizza SP Flash Tool quando sai perché ti serve e tieni a portata di mano una batteria carica e un cavo dati USB.

## Strumento Flash per Innioasis giocatori

Innioasis Updater è lo strumento flash per Innioasis giocatori. Installa il software ufficiale, aggiorna e ripristina i pacchetti attraverso il flusso corrispondente al modello e conserva la musica e le impostazioni.

### Innioasis Y1 strumento flash

Scegli la versione Y1 in Updater, quindi collega il lettore spento quando richiesto dall'app. Gli stessi pacchetti Y1 funzionano con SP Flash Tool quando è necessario il percorso manuale.

### Innioasis Y2 strumento flash

Scegli una versione elencata per Y2. I pacchetti Y2 non sono intercambiabili con i pacchetti Y1, quindi controlla il modello prima di iniziare.

## Strumento Flash per Timmkoo giocatori

Timmkoo i giocatori utilizzano lo stesso flusso di installazione dell'aggiornamento. Legge direttamente i pacchetti ZIP e RAR di Timmkoo, quindi non è necessario uno strumento flash separato o un file scatter.

### Timmkoo Q5 strumento flash

Seleziona il modello Q5 in Updater, scegli il pacchetto Timmkoo, quindi esegui Installa/Ripristina e collega il lettore quando richiesto.

### Timmkoo Q3 e Q3E strumento flash

La voce Q3 copre allo stesso modo Q3 e Q3E. Updater seleziona i file corrispondenti dal pacchetto pubblicato dal progetto.

### Timmkoo A5 strumento flash

Seleziona il modello A5 prima di scegliere un pacchetto, quindi segui la stessa richiesta di installazione.

## Dove lo mette Updater

SP Flash Tool viene fornito con la cartella di installazione dell'Updater, non come download separato. Aprilo da lì quando ne hai bisogno.

### Windows

Apri la cartella di installazione dell'Updater ed esegui `flash_tool.exe`. La cartella è solitamente sotto `%LOCALAPPDATA%\Innioasis Updater`. In alcune configurazioni è inclusa una cartella Toolkit con un collegamento SP Flash Tool.

### Linux

Esegui il bundle `flash_tool` binario all'interno della cartella dell'app Updater su x86 / x86_64. Il programma di installazione del progetto prepara i permessi USB con le regole udev, quindi il lettore dovrebbe apparire una volta connesso.

### macOS

SP Flash Tool non è incluso in macOS. L'Updater utilizza invece il percorso MTKClient lì. Usa il [installazione guidata](guide_it.html) su un Mac e mantieni SP Flash Tool per un computer Windows o Linux.

Lo strumento viene fornito con l'agente di download MediaTek e una configurazione specifica del modello, quindi non è necessario raccogliere DA o sparpagliare file da altrove.

## Preparare il firmware
  - Prendi la versione che desideri [Download del firmware](firmware_it.html). Scegliere `rom.zip` per un Y1 o `rom_y2.zip` per un Y2.
  - Estrai lo ZIP nella sua cartella. Windows può utilizzare Estrai tutto. Su Linux, usa il tuo gestore archivi o `unzip` in un terminale.
  - Controlla che il file scatter sia nella cartella estratta. Di solito è nominato `MT6572_Android_scatter.txt` per Y1 pacchetti e `MT6582_Android_scatter_def.txt` per Y2 pacchetti, sebbene una versione possa chiamarlo con il nome del suo progetto.
Mantieni i modelli separati. Lo scatter Y1 descrive un dispositivo MT6572 e lo scatter Y2 descrive un dispositivo MT6582. Lampeggiare con quello sbagliato è il modo in cui i giocatori vengono bloccati. Se la dispersione all'interno del ZIP non corrisponde al tuo modello, fermati e utilizza invece un pacchetto elencato per il tuo modello.

## Carica lo scatter e il flash
  - Apri SP Flash Tool dalla cartella di installazione dell'Updater.
  - Nella scheda Download, fare clic su Scegli accanto a File di caricamento scatter e seleziona il file scatter dalla cartella estratta. L'elenco delle partizioni verrà compilato.
  - Lasciare attiva la modalità flash Solo download a meno che tu non stia deliberatamente eseguendo un recupero completo, che è necessario Aggiornamento del firmware.
  - Fare clic Scarica. Lo strumento attenderà il giocatore.
  - Spegnere completamente il lettore, quindi collegare il cavo dati USB. Metti giù il lettore e non spostarlo.
  - Attendi il segno di spunta verde. Solo allora scollegare il cavo e avviare il lettore.

Mantieni le stesse USB regole relative ai cavi e ai tempi del percorso guidato: un cavo dati, nessun hub e connettiti solo quando lo strumento è pronto.

## Se non lampeggia
  - Controlla che lo scatter e il CAP corrispondano al modello stampato sul giocatore.
  - Verificare che il lettore sia completamente spento prima di collegarlo.
  - Su Windows, verificare il driver MediaTek installato con l'installazione dell'Updater; su Linux, confermare le regole udev dal programma di installazione del progetto.
  - Ricollegare il cavo solo quando lo strumento è in attesa. Una corsa in porto può richiedere una disconnessione completa e una rinfrescata Scarica clic.

Per qualsiasi cosa oltre a questo, apri [risoluzione dei problemi](troubleshooting_it.html). E ricorda: Updater è ancora il percorso normale e [Y1](guides/restore-original-y1.html) e [Y2](guides/restore-original-y2.html) anche le guide di ripristino lo usano.

## È stato utile?

La tua risposta aiuta a migliorare questa guida.Sì, l'ho trovato utileNon ancora[Facci sapere come possiamo migliorare](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
