---
title: "Ripristina il software originale su Innioasis G3 - passo dopo passo"
description: "Come ripristinare il software originale ufficiale su un Innioasis G3 con Innioasis Updater CE o SP Flash Tool, utilizzando il pacchetto verificato rom_g3.zip."
language: "it"
source: "https://innioasis.app/guides/restore-original-g3_it.html"
---

# Ripristina il software originale su Innioasis G3 - passo dopo passo

Guida al ripristino · Innioasis G3

# Ripristina il software originale su Innioasis G3

Un netto ritorno al software con cui è stato fornito il lettore. Usalo dopo un aggiornamento non riuscito, prima di vendere il lettore o ogni volta che un sistema personalizzato non fa per te.[Ottieni Updater CE](../guide_it.html#platform)[G3 download](../firmware_it.html?model=G3)[G3 manuale](../manuals/g3.html)

Guida all'installazione per il tuo computer

## Ripristina il software originale sul tuo G3 con il tuo computer

Scegli la guida per il computer che stai utilizzando. Ogni versione ha la configurazione della piattaforma, Updater CE passaggi e il modo per tornare allo stock.[Guida Windows](/install/original-g3-windows.html)[guida macOS](/install/original-g3-mac.html)[Guida Linux](/install/original-g3-linux.html)

[Tutte le guide Innioasis G3.](/install/g3.html) · [Tutte le guide al software originale](/install/original-software.html)

## Di cosa hai bisogno
  - Un computer Windows, macOS o Linux. Updater CE funziona su tutti e tre.
  - Il cavo dati USB fornito con il lettore. I cavi di sola ricarica non funzioneranno.
  - Il funzionario `rom_g3.zip` pacchetto, che Updater scarica per te, o una copia dal file [G3 archivio](../firmware_it.html?model=G3) se preferisci flashare a mano.
  - Carica nel lettore. Un ripristino che perde potenza è l'unico modo comune per peggiorare una brutta situazione.

Questo sostituisce il sistema e cancella la memoria interna. Copiare prima musica, registrazioni e foto su un computer.

## Itinerario A: Updater CE (consigliato)
  - Installare [Innioasis Programma di aggiornamento CE](../guide_it.html#platform) e aprirlo.
  - Impostato Modello del dispositivo a G3. Il modello deve corrispondere esattamente al giocatore.
  - Scegli Software originale nell'elenco del software.
  - Scegli una versione. La build stabile più recente è l'impostazione predefinita sicura.
  - Premere Installa / Ripristina e attendi che il pacchetto venga scaricato ed estratto.
  - Spegnere completamente il lettore, quindi collegare il cavo USB solo quando richiesto dall'Updater.
  - Non toccare il lettore o il cavo fino al messaggio di successo. Disconnetti e avvia il lettore.
Non scegliere mai un modello diverso per "farlo funzionare". Un G3 necessita di un pacchetto G3. Mescolare i modelli è il modo in cui i giocatori finiscono per aver bisogno di un ripristino manuale.

## Itinerario B: SP Flash Tool (manuale)

Utilizzalo quando un computer non può eseguire Updater CE o quando hai già il pacchetto e preferisci lo strumento classico.
  - Scaricamento `rom_g3.zip` dal [G3 archivio](../firmware_it.html?model=G3) e decomprimilo.
  - Mantieni il file scatter accanto alle immagini. Non rinominare o spostare le immagini.
  - Apri SP Flash Tool, scegli Solo downloade caricare il file scatter.
  - Spegnere il lettore, premere Scaricamento, quindi collegare il cavo.
  - Attendi il segno verde di successo prima di disconnetterti.

Il [SP Flash Tool guida](../sp-flash-tool_it.html) tratta i driver e le istruzioni di Windows in modo più dettagliato. Su Linux e macOS, Updater CE è il percorso più semplice perché offre la propria gestione USB.

## Dopo il ripristino
  - Scollegare il lettore e lasciarlo avviare da solo.
  - Scegli la tua lingua e imposta l'orologio.
  - Riconnettiti al Wi-Fi o al Bluetooth se li usi.
  - Copia la tua musica. Il [guida al trasferimento](../manuals/transfer-music.html) ha i nomi delle cartelle.

Se il lettore si avvia ma lo schermo, il volante o i pulsanti continuano a funzionare in modo anomalo, il ripristino ha funzionato; questa è una questione hardware o di configurazione, non software. Il [guida alla risoluzione dei problemi](../troubleshooting_it.html) è la prossima fermata.

## Se non funziona

### Il programma di aggiornamento non vede mai il lettore

Cambia il cavo, poi la porta USB. Evita gli hub. Su Windows, installare il driver MediaTek dal file [pagina del conducente](../drivers_it.html).

### Il flash si ferma presto

Riconnetti, carica il lettore e ricomincia. Non passare al pacchetto di un modello diverso.

### Il giocatore rimane nero

Carica per un'ora, quindi mantieni la carica per dieci secondi. Se è ancora morto, leggi il [guida al recupero](../guides/recovery_it.html) prima di riprovare.

## Domande che le persone fanno

### La mia musica verrà eliminata?

Sì, la memoria interna viene cancellata. I file su una scheda microSD di solito sopravvivono, ma prima copiali in un posto sicuro.

### Posso tornare a Rockbox in seguito?

SÌ. Il ripristino del software originale non è una porta a senso unico; la pagina del software personalizzato per il tuo modello può installarlo nuovamente.

### Ho bisogno dell'impostazione Type A/Type B?

Solo l'Y1 ha questa scelta e solo per il software originale. Ogni altro modello utilizza un unico pacchetto.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
