---
title: "SP Flash Tool pour Innioasis et Timmkoo joueurs"
description: "Recherchez SP Flash Tool fourni avec Innioasis Updater sur Windows et Linux, extrayez rom.zip ou rom_y2.zip et flashez un Innioasis Y1 ou Y2 avec le fichier scatter correspondant."
language: "fr"
source: "https://innioasis.app/sp-flash-tool_fr.html"
---

# SP Flash Tool pour Innioasis et Timmkoo joueurs

Clignotement manuel

# Outil Flash pour les joueurs Innioasis et Timmkoo

SP Flash Tool vient à l'intérieur de Innioasis Updater sur [Windows](drivers_fr.html#windows) et [Linux](drivers_fr.html#linux). Vous l'avez déjà. Ce guide montre la manière sûre de l'utiliser sur un Innioasis Y1 ou Y2, ainsi que la route de mise à jour pour les joueurs Timmkoo.[Revenir au guide du programme de mise à jour](guide_fr.html)[Téléchargements de micrologiciels](firmware_fr.html)[Dépannage](troubleshooting_fr.html)

Commencez par Innioasis Updater

## Le programme de mise à jour fait tout le travail en un seul passage

Le programme de mise à jour effectue la plupart des installations en une seule passe. Choisissez le logiciel, suivez les étapes et vous avez terminé. Il vous indique également quand un correctif ou une nouvelle version arrive. SP Flash Tool se trouve dans la boîte à outils du programme de mise à jour pour les rares cas où le programme de mise à jour ne peut pas terminer. Les étapes ci-dessous constituent l’exception.

## A quoi sert cet outil

Le programme de mise à jour fait clignoter le lecteur pour vous. SP Flash Tool est le même moteur, sans les garde-corps. Utilisez-le lorsque le programme de mise à jour ne démarre pas, lorsque le lecteur ne se connecte pas ou lorsque vous connaissez votre chemin dans un fichier scatter.Essayez d'abord le programme de mise à jour. Pour la plupart des installations et des récupérations, le guide [Itinéraire du programme de mise à jour](guide_fr.html) est le choix le plus sûr. Utilisez SP Flash Tool lorsque vous savez pourquoi vous en avez besoin et gardez à portée de main une batterie chargée et un câble de données USB.

## Outil Flash pour Innioasis joueurs

Innioasis Updater est l'outil flash pour les joueurs de Innioasis. Il installe les logiciels officiels, met à jour et restaure les packages via le flux correspondant au modèle, et conserve votre musique et vos paramètres.

### Innioasis Y1 outil Flash

Choisissez la version Y1 dans Updater, puis connectez le lecteur éteint lorsque l'application le demande. Les mêmes packages Y1 fonctionnent avec SP Flash Tool lorsque vous avez besoin de l'itinéraire manuel.

### Innioasis Y2 outil Flash

Choisissez une version répertoriée pour Y2. Les packages Y2 ne sont pas interchangeables avec les packages Y1, vérifiez donc le modèle avant de commencer.

## Outil Flash pour Timmkoo joueurs

Timmkoo les joueurs utilisent le même flux d'installation du programme de mise à jour. Il lit directement les packages ZIP et RAR de Timmkoo, vous n'avez donc pas besoin d'un outil Flash séparé ou d'un fichier scatter.

### Timmkoo Q5 outil flash

Sélectionnez le modèle Q5 dans Updater, choisissez le package Timmkoo, puis exécutez Install/Restore et connectez le lecteur à l'invite.

### Outil Flash Timmkoo Q3 et Q3E

L'entrée Q3 couvre à la fois les Q3 et les Q3E. Le programme de mise à jour sélectionne les fichiers correspondants dans le package publié par le projet.

### Timmkoo A5 outil Flash

Sélectionnez le modèle A5 avant de choisir un package, puis suivez la même invite d'installation.

## Où le met le programme de mise à jour

SP Flash Tool est livré avec le dossier d'installation du programme de mise à jour, et non sous forme de téléchargement séparé. Ouvrez-le à partir de là lorsque vous en avez besoin.

### Windows

Ouvrez le dossier d'installation du programme de mise à jour et exécutez `flash_tool.exe`. Le dossier se trouve généralement sous `%LOCALAPPDATA%\Innioasis Updater`. Un dossier Toolkit avec un raccourci SP Flash Tool est inclus sur certaines configurations.

### Linux

Exécutez le package `flash_tool` binaire dans le dossier de l'application Updater sur x86 / x86_64. L'installateur du projet prépare les autorisations USB avec les règles udev, de sorte que le lecteur devrait apparaître une fois connecté.

### macOS

SP Flash Tool n'est pas fourni sur macOS. Le programme de mise à jour utilise à la place la route MTKClient. Utilisez le [installation guidée](guide_fr.html) sur un Mac et conservez SP Flash Tool pour une machine Windows ou Linux.

L'outil est livré avec l'agent de téléchargement MediaTek et une configuration spécifique au modèle, vous n'avez donc pas besoin de collecter des fichiers DA ou scatter ailleurs.

## Préparez le firmware
  - Récupérez la version que vous souhaitez [Téléchargements de micrologiciels](firmware_fr.html). Choisir `rom.zip` pour un Y1 ou `rom_y2.zip` pour un Y2.
  - Extrayez le ZIP dans son propre dossier. Windows peut utiliser Extraire tout. Sous Linux, utilisez votre gestionnaire d'archives ou `unzip` dans une borne.
  - Vérifiez que le fichier scatter se trouve dans le dossier extrait. On le nomme généralement `MT6572_Android_scatter.txt` pour Y1 packages et `MT6582_Android_scatter_def.txt` pour les packages Y2, bien qu'une version puisse lui donner le nom de son projet.
Gardez les modèles séparés. Le scatter Y1 décrit un appareil MT6572 et le scatter Y2 décrit un appareil MT6582. C'est en clignotant avec le mauvais que les joueurs se retrouvent bloqués. Si la dispersion à l'intérieur du ZIP ne correspond pas à votre modèle, arrêtez-vous et utilisez plutôt un package répertorié pour votre modèle.

## Chargez le scatter et le flash
  - Ouvrez SP Flash Tool à partir du dossier d'installation du programme de mise à jour.
  - Dans l'onglet Télécharger, cliquez sur Choisissez à côté de Fichier de chargement dispersé et sélectionnez le fichier dispersé dans le dossier extrait. La liste des partitions se remplira.
  - Laissez le mode flash activé Téléchargement uniquement à moins que vous ne procédiez délibérément à une récupération complète, ce qui nécessite Mise à niveau du micrologiciel.
  - Cliquez Télécharger. L'outil attendra le joueur.
  - Éteignez complètement le lecteur, puis connectez le câble de données USB. Posez le lecteur et ne le déplacez pas.
  - Attendez la coche verte. Ensuite seulement, débranchez le câble et démarrez le lecteur.

Conservez les mêmes règles de câble et de synchronisation USB que pour l'itinéraire guidé : un câble de données, pas de hub et connectez-vous uniquement lorsque l'outil est prêt.

## S'il ne clignote pas
  - Vérifiez que le scatter et le ZIP correspondent au modèle imprimé sur le lecteur.
  - Vérifiez que le lecteur est complètement éteint avant de le connecter.
  - Sous Windows, confirmez le pilote MediaTek installé avec la configuration du programme de mise à jour ; sous Linux, confirmez les règles udev du programme d'installation du projet.
  - Rebranchez le câble uniquement lorsque l'outil est en attente. Une course portuaire peut nécessiter un débranchement complet et un nouveau Télécharger cliquez.

Pour tout ce qui va au-delà, ouvrez [dépannage](troubleshooting_fr.html). Et rappelez-vous : le programme de mise à jour reste la voie normale, et [Y1](guides/restore-original-y1.html) et [Y2](guides/restore-original-y2.html) Les guides de restauration l'utilisent également.

## Était-ce utile ?

Votre réponse contribue à améliorer ce guide.Oui, je l'ai trouvé utilePas encore[Faites-nous savoir comment nous pouvons nous améliorer](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
