---
title: "Sviluppatori | Aggiungi firmware personalizzato a Innioasis Updater CE - Innioasis Download firmware"
description: "Documentazione per gli sviluppatori per aggiungere un firmware Innioasis Y1 o Y2 personalizzato a Updater CE: eseguire il fork del repository, pubblicare rom.zip risorse, modificare slidia_manifest.xml, testare e aprire una richiesta pull."
language: "it"
source: "https://innioasis.app/developers_it.html"
---

# Sviluppatori | Aggiungi firmware personalizzato a Innioasis Updater CE - Innioasis Download firmware

Per gli sviluppatori di firmware

# Aggiungi il tuo firmware a Updater CE.

Updater CE è il catalogo della community e il programma di installazione per il firmware personalizzato. Sviluppa il tuo progetto da una base ROM, pubblicalo come repository pubblico con le risorse di rilascio corrette, aggiungi le voci del modello a `slidia_manifest.xml`, testare i filtri del modello e aprire una richiesta pull. Un repository può servire ogni modello che supporta.[Visualizza il sorgente Updater CE](https://github.com/y1-community/Innioasis-Updater)[Sfoglia i download di software](firmware_it.html)

## Inizia da una base ROM

Le ROM di base offrono agli sviluppatori di firmware personalizzati una base Android pulita con i chip radio wireless abilitati. Sul Y1 abilitano Wi-Fi e GPS insieme a Bluetooth e FM di fabbrica; sul Y2 abilitano Wi-Fi, GPS e FM insieme al Bluetooth di fabbrica.Download di base ROM per lo sviluppo di firmware personalizzato, con la versione Android e le funzionalità wireless abilitate da ciascuno[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Scarica | Dispositivo | Android | Funzionalità senza fili |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Aggiunge Wi-Fi e GPS al Bluetooth e FM di fabbrica (FM funziona già sul Y1 di fabbrica). Per Y1 giocatori forniti con sistema operativo 2.0.0 o successivo. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Aggiunge Wi-Fi e GPS al Bluetooth e FM di fabbrica (FM funziona già sul Y1 di fabbrica). Per Y1 giocatori forniti con un sistema operativo precedente alla 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Aggiunge Wi-Fi, GPS e FM al Bluetooth di fabbrica. Il chip radio Y2 è completamente abilitato, quindi FM è disponibile anche qui. |

Queste immagini sono la base Android di serie (AOSP) con le radio wireless del dispositivo abilitate, quindi un firmware personalizzato può aggiungere funzionalità di rete invece di sostituire lo stack radio. Costituiscono il punto di partenza pratico per le fasi di pubblicazione riportate di seguito.

## Utilizza questi nomi di risorse di rilascio

Il nome del file fa parte del segnale di compatibilità. Mantieni i nomi esatti e inserisci i file ZIP nelle risorse di rilascio del progetto, non solo nell'albero dei sorgenti del repository.Nomi delle risorse ZIP firmware e dispositivi supportati``````

| Risorsa | Dispositivo | Hardware | Senso |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 dispositivi forniti con sistema operativo 2.0.0 o versione successiva. |
| rom_type_b.zip | Y1 | Type B | Y1 dispositivi forniti con un sistema operativo precedente alla 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Il pacchetto di installazione completa Y2. Tienilo separato dalle Y1 risorse. |
Non rinominare un pacchetto per adattarlo a un altro modello. Y1 e Y2 utilizzano file di piattaforma MediaTek e configurazioni flash diversi. Pubblica il pacchetto per l'hardware che supporta effettivamente.

## Come funziona la connessione

Updater CE legge il manifest come catalogo. Ogni `<package>` la riga indica il nome del progetto, il repository, il modello e il gestore. Quando un utente sceglie quel progetto, Updater controlla le versioni pubblicate del repository e cerca un file `rom*.zip` risorsa.

### Manifesto

Assegna un nome al progetto e lo mappa a un modello. Y1 e Y2 necessitano di righe separate, anche quando condividono un repository.

### Rilascio pubblicato

Contiene le risorse ZIP installabili. Una singola versione può contenere insieme i pacchetti Y1 Type A, Y1 Type B e Y2.

### Installazione dell'aggiornamento CE

Utilizza il modello selezionato per scegliere il pacchetto corrispondente e il percorso lampeggiante specifico del modello. L'utente non dovrebbe dover indovinare il nome di un file.

## Pubblica un progetto in cinque passaggi
  - Effettua il fork del repository Updater CE. Crea la tua forchetta di [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), quindi clona il fork localmente.
  - Preparare un repository firmware pubblico. Assicurati che il repository sia pubblico e che la sua versione contenga le risorse ZIP corrette. Puoi mettere `rom.zip`, `rom_type_b.zip`, e `rom_y2.zip` sulla stessa versione quando appartengono alla stessa versione.
  - Modifica il manifesto. Aperto `slidia_manifest.xml` nella radice del fork Updater CE. Aggiungere una riga per ciascun modello supportato dalla versione (Y1 e Y2 sono la coppia comune). IL `repo` il valore è quello del repository `owner/repository`; `url` è la pagina pubblica del progetto.
  - Prova il catalogo. Esegui Updater dal checkout modificato. Seleziona Y1 e conferma che il progetto mostra le Y1 risorse. Selezionare Y2 e confermare che venga visualizzata la versione Y2. Controllare Type A e Type B separatamente quando entrambi vengono pubblicati.
  - Apri una richiesta pull. Invia la modifica del manifest al fork e apri una richiesta pull rispetto al repository Updater CE upstream. Includi il collegamento del progetto, i modelli supportati, il tag di rilascio, i nomi delle risorse e i dispositivi che hai testato.

## Genera le tue linee manifest

Compila il repository e seleziona ogni modello supportato dalla versione. Il generatore ne scrive uno `<package>` linea per modello e include solo gli attributi impostati, quindi il risultato corrisponde a quello corrente `slidia_manifest.xml` formato. Tutti gli attributi letti da Updater CE sono disponibili di seguito: quelli facoltativi sono sotto Più opzioni.URL dell'archivioIl repository pubblico GitHub. Il generatore estrae `owner/repository` dall'URL.Nome del softwareMostrato nell'app e nel catalogo del sito.URL del progettoPagina rivolta alle persone per il progetto o le relative note di rilascio.MarcaDeselezionarlo per utilizzare la marca predefinita del modello. SR1, Q3, Q5 e Q3e sono Timmkoo modelli.Dispositivi (una linea ciascuno)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAltri modelliPer un modello non elencato sopra. I modelli noti mantengono l'ortografia del catalogo.Bandiere`do_not_keep_data` - non offrire mai Keep Data per questo firmwareCostruito dal software originale - aggiunge `derivative="y1-community/y1-stock-rom"`

Keep Data viene offerto solo quando il firmware in arrivo e il firmware installato sono uguali o condividono a `derivative` radice. Utilizza il flag solo quando i dati utente non possono davvero essere trasferiti.Altre opzioni: icona, grafica, risorse di rilascio, post-installazione e mirror

#### Icona e opera d'arteArchivio di iconeScegli l'immagine che impegnerai nel repository. Questo ne visualizza l'anteprima e crea il suo URL non elaborato; non carica nulla.Percorso dell'icona nel repositoryPercorso dell'immagine impegnata, relativo alla radice del repository.Ramo di iconeURL dell'iconaUn URL di immagine diretto. Quando è vuota, l'app utilizza la versione `updater.png` o un'icona generata.Anteprima dell'icona selezionata

URL dell'icona della modalità oscuraIcona opzionale del tema scuro. `image_dark` è un alias accettato.URL dell'opera d'arte leggeraGrafica secondaria, provata dopo l'immagine di rilascio e `icon`.URL dell'opera d'arte scura

#### Rilasciare risorseRilascia il nome della risorsaUn nome per ogni modello selezionato. Lasciare vuoto per l'uso `rom.zip` su Y1 e `rom_<model>.zip` altrove.Modello di assetGlob utilizzato quando i zip della versione non hanno un nome `rom*.zip`.Type A risorsaGlob per il pacchetto Y1 Type A quando il suo nome non lo dice.Type B risorsaGlob per il pacchetto Y1 Type B quando il suo nome non lo dice.Versione minima dell'appNascondi la voce dalle build precedenti di Updater CE.

#### Collegamenti, mirror e la famiglia Keep DataPagina di post-installazioneAperto dopo un'installazione riuscita.Seconda pagina post-installazioneSecondo passaggio facoltativo per una guida alla configurazione di più pagine.Specchietti con cerniera portatiliSeparati da virgole `*-mirror` repository che creano pacchetti Portable Flashing Zip.Deposito di derivatiIl firmware da cui è creata questa versione. I firmware correlati condividono una partizione dati, che è ciò che Keep Data controlla.Deposito di informazioniRepo di app le cui versioni descrivono le app in questo firmware. Ha bisogno anche di una pagina post-installazione.APK archivioRepo dell'app di cui APK l'app viene scaricata e installata dopo il firmware.

#### Extra del catalogoLumacaIdentificatore stabile per collegamenti e record di installazione salvati. Il modello viene aggiunto automaticamente quando vengono selezionati più modelli.Descrizione`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Copia righe

Caricamento dell'ultimo manifest…Visualizza l'anteprima dell'ultimo manifest con le tue righe aggiunte

Il generatore prelevava la corrente `slidia_manifest.xml` da questo repository e hai inserito le righe generate poco prima `</slidia>`.

Una riga non è sufficiente per un repository condiviso. Se manca la riga Y2, gli utenti Y2 non riceveranno una voce corrispondente al modello anche quando `rom_y2.zip` esiste nella versione del progetto. Lo stesso vale per ogni altro modello supportato dalla tua versione.

### Ogni attributo letto dal manifest

Questi sono gli attributi che le attuali build di Updater CE comprendono. Il generatore scrive solo quelli che inserisci; per il resto l'app torna a impostazioni predefinite ragionevoli.Attributi del pacchetto slideia_manifest.xml e loro significato``````````````````````````````````````````````````````````````````````````````````````````````

| Attributo | Necessario | Cosa fa |
| --- | --- | --- |
| name | Sì | Nome del software riportato nel catalogo e sulle schede di installazione. |
| repo | Sì | owner/repo. L'app legge le versioni GitHub del repository. |
| device | Sì | Modello di destinazione, maiuscolo (Y1, Y2, G1, Q3e,…). Conserva una voce per modello. |
| url | Raccomandato | Pagina del progetto o note di rilascio aperte dal catalogo. |
| type, handler | Sì, in pratica | type="img" e handler="Custom Firmware". Altri tipi e gestori non firmware vengono ignorati. |
| brand | Facoltativo | Marchio del catalogo (Innioasis, Timmkoo). Vuoto utilizza la marca predefinita del modello. |
| package_name | Facoltativo | Rilascia il nome del file della risorsa. Il valore predefinito è rom.zip su Y1 e rom_<model>.zip su altri modelli. |
| asset_pattern | Facoltativo | Glob senza distinzione tra maiuscole e minuscole per versioni i cui zip firmware non sono nominati rom*.zip (Per esempio my-firmware-*.zip). |
| type_a_asset, type_b_asset | Facoltativo | Glob che identificano gli zip Y1 Type A e Type B quando i nomi dei file non contengono i soliti marcatori. |
| icon | Facoltativo | URL del logo. Utilizzato dopo il rilascio updater.png / updater.jpge come fallback per ogni versione. |
| icon_dark | Facoltativo | Logo a tema scuro. image_dark è un alias accettato. |
| image | Facoltativo | Grafica con luce secondaria, provata dopo icon. |
| post_install, post_install2 | Facoltativo | Pagine aperte dopo un'installazione riuscita. Il secondo copre una guida in più passaggi. |
| portable_zips | Facoltativo | Separati da virgole *-mirror repository che pubblicano pacchetti portatili pronti per l'esecuzione. |
| derivative | Facoltativo | Repository da cui è creato il firmware. Il firmware con la stessa radice derivata può conservare i dati dell'utente. |
| info_repo | Facoltativo | Repository di app le cui versioni descrivono cosa distribuisce il firmware. Richiede post_install o post_install2. |
| apk_repo | Facoltativo | Repository dell'app di cui APK l'app viene installata dopo il firmware. |
| min_version | Facoltativo | Nascondi la voce quando Updater CE è precedente a questa versione. |
| do_not_keep_data | Facoltativo | true (Anche 1 / yes) blocca completamente Keep Data per questo firmware. |
| slug | Facoltativo | Identificatore stabile per collegamenti e record di installazione salvati. Generato dal nome e dal modello quando vuoto. |
| description | Facoltativo | Breve descrizione del catalogo. Può essere il valore dell'attributo o il testo dell'elemento. |

I nomi legacy vengono ancora letti per compatibilità: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` e `image_dark`. Le nuove voci dovrebbero utilizzare i nomi attuali sopra.

### Invia le righe come richiesta pull
  - Copia le righe generate sopra. Corrispondono già al formato manifest più recente.
  - Modificare `slidia_manifest.xml` nel deposito. Utilizza il link di modifica qui sotto; l'host del repository crea automaticamente un fork e un ramo.
  - Incolla le linee appena prima `</slidia>`, mantenendo invariate le voci esistenti.
  - Impegnarsi in una nuova filiale (Per esempio `add-your-firmware`), quindi aprire una richiesta pull sul repository Updater CE.
  - Nel PR, includere il collegamento del progetto, i modelli supportati, il tag di rilascio, i nomi delle risorse e i dispositivi testati.
[Modifica il manifesto di Updater CE](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Visualizza l'ultimo manifesto](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Mantieni i nomi dei modelli in maiuscolo, utilizza l'URL esatto del tuo repository pubblico e mantieni `type="img"` e `handler="Custom Firmware"` per una voce del firmware.

## Rendi la versione facile da verificare

Assegna alla pubblicazione un tag chiaro e una nota di rilascio. Il tag è utile alle persone, ma i nomi delle risorse ZIP sono ciò che Updater CE utilizza per identificare i pacchetti di installazione.

### Lista di controllo del rilascio
  - Pubblicare pubblicamente il comunicato.
  - Allega i file ZIP come risorse di rilascio.
  - Indicare il modello supportato e Type A o Type B nelle note.
  - Elencare eventuali preparazioni richieste o limiti noti.

### Una versione, tre risorse

Una versione condivisa può contenere `rom.zip`, `rom_type_b.zip`, e `rom_y2.zip`. Updater li classifica separatamente e sceglie tra il modello e i filtri hardware.

### Non raggruppare ipotesi

Non includere un pacchetto Y1 sotto il nome file Y2 e non aggiungere dati scatter, preloader o partizioni non testati solo per far apparire una risorsa.

## Perché le voci del modello sono importanti durante il flashing

Il manifest non è solo un menu di download. Dopo l'estrazione, Updater CE utilizza il modello risolto per preparare il percorso di installazione corrispondente. Y1 e Y2 hanno file di piattaforma, precaricatori, configurazioni scatter e layout dei dispositivi diversi.
  - Y1: il programma di aggiornamento prepara il percorso Y1 e utilizza le partizioni denominate del dispositivo quando viene utilizzato MTKClient.
  - Y2: il programma di aggiornamento prepara il percorso Y2 e utilizza la configurazione Y2 MT6582. Il ripristino completo può utilizzare gli indirizzi fisici dai dati di dispersione corretti dal modello.
  - Supporto multipiattaforma: Updater CE gestisce il flashing nativo direttamente su Windows, Linux e macOS (supportando sia i Mac Intel che Apple Silicon) senza strumenti di flashing aggiuntivi.
I contributori devono fornire file firmware corretti, non offset flash. Non modificare indirizzi scatter, precaricatori, file DA o comandi di partizione per aggirare un pacchetto danneggiato. Correggere l'asset di rilascio ed eseguire il test sul modello previsto.

## Prima di richiedere un'unione
  - Convalidare l'XML con un parser XML. Una citazione mancante o di chiusura `/>` può nascondere ogni voce successiva.
  - Avvia il programma di aggiornamento dal checkout in modo che carichi il manifest locale prima dell'aggiornamento remoto.
  - Controllare Y1 e Y2 in modo indipendente. Confermare che il progetto venga visualizzato solo dove il relativo pacchetto è supportato.
  - Controlla l'elenco delle versioni `rom.zip`, `rom_type_b.zip`, e `rom_y2.zip` come applicabile.
  - Testa l'effettiva installazione sul dispositivo previsto, con un cavo dati USB affidabile e un piano di ripristino per tornare al software originale.
  - Nella richiesta pull, spiega cosa hai testato. Non descrivere un modello non testato come supportato.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Per un controllo locale, esegui il comando dalla root del repository. Verifica solo la sintassi XML; non dimostra che una versione contenga firmware valido o che sia sicuro eseguire il flashing di un dispositivo.

## Link utili al progetto[Aggiornamento forcelle CE](https://github.com/y1-community/Innioasis-Updater/fork)[Vedi il manifesto](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Note sul contributo comunitario](support_devs_it.html)[Risoluzione dei problemi](troubleshooting_it.html)

## Abilità di modding per gli agenti IA

Quello del deposito `skills/` La directory è una base di conoscenza basata sull'origine per gli agenti che lavorano su hardware, firmware, temi e app Y1 e Y2. Ciascuna competenza nomina i file di progetto da cui provengono le sue richieste, in modo che un agente possa verificare un fatto prima di modificare un dispositivo.Inizia qui

### [Indice di competenze e norme di sicurezza](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Come caricare una competenza, a quale modello si applica un fatto e le partizioni che nessun pacchetto dovrebbe scrivere.Hardware

### [Y1hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, la ruota come eventi chiave, display 480x360, percorsi FM/audio, memoria e mappa delle partizioni Type A/B.Hardware

### [Y2 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Scheda MT6582, struttura dei dispositivi, pannelli GC9503V/ST7701S, binari PMIC/DAC, partizioni e immagine di avvio.Firmware

### [Pacchetti firmware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomia, file scatter, contratti di aggiornamento di Classe A e lista di controllo del rilascio.Temi

### [Creazione di temi e skin](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 temi config.json, Rockbox WPS/SBS, Reborn skin e Y2Player formato skin v2.Tutte le abilità

### [Sfoglia la cartella delle competenze](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, ROM Android di serie, Y2Linux, app Android, launcher, note di rilascio e pubblicazione di siti.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
