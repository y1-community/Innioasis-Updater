---
title: "Thèmes Rockbox-Y1&nbsp;: transfert de thèmes avec Updater CE, 240p vs 360p et application d'un thème"
description: "Comment transférer des thèmes vers le Innioasis Y1 avec Updater CE (push automatique lorsqu&#39;il est disponible ou transfert guidé étape par étape après un flash MTKClient sur macOS et Linux), plus compatibilité 240p vs 360p et application d&#39;un thème."
language: "fr"
source: "https://innioasis.app/rockbox-y1-themes_fr.html"
---

# Thèmes Rockbox-Y1&nbsp;: transfert de thèmes avec Updater CE, 240p vs 360p et application d'un thème

[← Rockbox-Y1 centre](rockbox-y1/)

Rockbox-Y1 · thèmes & Updater CE

# Thèmes Rockbox-Y1 : transfert avec Updater CE, choisissez le build, puis le look

Updater CE gère les thèmes et les polices Rockbox-Y1 pour vous, en les transférant automatiquement vers le Y1 chaque fois que cela est possible et en vous guidant tout au long du transfert étape par étape lorsqu'il ne peut pas se produire sans surveillance (par exemple, juste après l'installation du micrologiciel MTKClient sur macOS ou Linux).[Obtenez Rockbox et Updater CE](guides/rockbox-y1.html)[Parcourir les thèmes de la communauté](https://themes.innioasis.app/)[240p contre 360p](rockbox-y1/resolution.html)

## Transférer des thèmes vers le Y1 avec Updater CE

Rockbox stocke son micrologiciel dans le flash interne du Y1, tandis que les thèmes, les polices et les paramètres utilisateur résident dans le stockage caché. `.rockbox` dossier sur la mémoire du lecteur (carte MicroSD). Parce que flasher un ROM et copier des fichiers vers le stockage utilisent deux connexions différentes, Programme de mise à jour CE s'adapte automatiquement à votre système d'exploitation et à votre méthode d'installation :
  - Transfert automatique lorsque Updater CE peut atteindre le joueur : Lorsque vous installez une version 360p Rockbox-Y1 (ou activez la synchronisation automatique du thème dans Paramètres), Updater CE télécharge et fusionne le thème 360p et le pack de polices sélectionnés en arrière-plan. Dès que le Y1 est accessible via BAD (Android Debug Bridge) ou monté en tant que USB lecteur avec un `.rockbox` dossier, Updater CE transfère les thèmes et les polices directement vers le lecteur pour vous sans aucune extraction manuelle du zip requise.
  - Transfert guidé étape par étape lorsqu'il ne peut pas se produire sans surveillance (par exemple, MTKClient sur macOS et Linux) : Lorsque vous faites clignoter Rockbox à l'aide d'un MTKClient méthode d'installation sur macOS ou Linux, le flash se produit pendant que le Y1 est éteint en mode Preloader/BROM de bas niveau - avant que Rockbox ait démarré pour la première fois pour créer `.rockbox` et avant que le stockage du lecteur ne soit monté sur votre ordinateur. Chaque fois que Updater CE ne peut pas terminer le transfert sans surveillance pendant le flash, il ouvre automatiquement le assistant de thèmes et de polices post-installation et vous guide tout au long de sa réalisation : 
    - Démarrez Rockbox en premier : Updater CE vous invite à déconnecter le câble USB si nécessaire et à allumer le Y1 afin que Rockbox démarre une fois et initialise le `.rockbox` dossier sur la carte.
    - Reconnectez-vous via USB : Rebranchez le Y1 sur votre Mac ou PC Linux. Si ADB est disponible, Updater CE détecte le lecteur démarré et pousse automatiquement les packs de thèmes et de polices.
    - Ou utilisez le mode de stockage USB avec le sélecteur de dossier guidé : Si ADB n'est pas actif ou si vous préférez le transfert de stockage direct, Updater CE vous guide pour entrer dans le mode de stockage USB sur le Y1, cliquez sur Sélectionnez le dossier .rockbox, révéler les dossiers cachés (Cmd+Shift+. dans la boîte de dialogue de fichier macOS ou Ctrl+H sous Linux) et sélectionnez `.rockbox` sur le lecteur Y1 — puis Updater CE fusionne tous les thèmes et polices pour vous.

  - Ajoutez ou actualisez des thèmes à tout moment sur demande : Vous pouvez exécuter le même transfert automatisé ou guidé à tout moment sans reflasher le micrologiciel : ouvrez Updater CE et choisissez Paramètres → Installer Rockbox Thèmes 360p (Cmd+T sur macOS, Ctrl+T sous Windows et Linux), ou faites glisser un thème individuel `.zip` packs sur Updater CE Dépôt intelligent fenêtre.

## 240p, 360p et pourquoi l'étiquette est sur la version

Les versions de communauté Y1 sont publiées avec une étiquette de résolution et les collections de thèmes portent la même étiquette. Les versions 240p ont la compatibilité la plus large avec les anciens packs de thèmes ; Les versions 360p sont conçues pour le nouveau chemin de thème Y1. Installer l’un et appliquer l’autre n’est pas dangereux : cela semble simplement faux, avec du texte tronqué, des éléments manquants ou une interface illisible.

Si vous n'avez pas encore de préférence de thème, prenez la version stable la plus récente et son thème par défaut, puis choisissez les thèmes qui correspondent à son étiquette. Le [page de résolution](rockbox-y1/resolution.html) va plus profondément; la règle générale est simple : l’étiquette de construction et l’étiquette de thème doivent être d’accord.

## Où vivent les thèmes

Les thèmes sont des fichiers sur la carte MicroSD, à l'intérieur du `.rockbox` dossier - le même dossier qui contient les paramètres et les caches. Le firmware lui-même est sur flash interne, donc l'ajout, la modification ou la suppression d'un thème ne nécessite jamais de reflasher.
  - Copiez le propre dossier du thème dans `.rockbox/themes` sur la carte.
  - Choisissez-le ensuite dans les paramètres du thème du lecteur et redémarrez pour le voir appliqué.
  - Conservez une copie d'un thème que vous aimez avant de mettre à jour la version : il s'agit d'un fichier, pas d'une installation.

Activez d'abord les fichiers cachés si vous ne voyez pas le dossier : macOS Cmd+Shift+., Affichage Windows → Éléments masqués, Linux Ctrl+H.

## Appliquer un thème, dans l'ordre
  - Installez et démarrez Rockbox-Y1 d'abord ; un thème a besoin d’une version en cours d’exécution.
  - Copiez le dossier du thème dans `.rockbox/themes` sur la carte.
  - Ouvrez les paramètres du thème et sélectionnez le thème.
  - Redémarrez pour que toute l’interface – pas seulement le menu – le récupère.
  - S'il semble cassé, sélectionnez un autre thème ; les fichiers sont toujours là si vous souhaitez réessayer plus tard.

## Annuler un thème qui a cassé l'interface

Si le lecteur démarre sur quelque chose d'inutilisable, vous n'avez pas besoin de réinstaller le firmware. Renommer ou supprimer le `.rockbox` dossier sur la carte et démarrez le lecteur : le build recrée le dossier avec les paramètres par défaut et un thème par défaut. Votre musique est intacte et vous pouvez copier les thèmes que vous souhaitez par la suite.[Le dossier .rockbox](rockbox-y1/sd-card.html)[Premier démarrage](rockbox-y1/first-start.html)[Mise à jour de la version](rockbox-y1/update.html)

## Les questions que les gens posentPourquoi Updater CE me guide-t-il dans le transfert de thèmes après une installation de MTKClient sur macOS ou Linux ?

MTKClient fait clignoter le Rockbox ROM sur le stockage interne pendant que votre Y1 est éteint en mode Preloader/BROM de bas niveau, avant que Rockbox n'ait démarré pour initialiser le `.rockbox` dossier et avant que la carte MicroSD ne soit montée sur votre ordinateur. Chaque fois que Updater CE peut atteindre directement le lecteur démarré (via ADB ou un lecteur USB monté), il transfère automatiquement les thèmes ; lorsqu'il ne peut pas le faire sans surveillance pendant le flash, il ouvre l'étape guidée des thèmes et des polices juste après le flash pour vous aider à allumer le Y1 et à terminer le transfert via ADB ou le mode de stockage USB.Un thème Y2 fonctionnera-t-il sur le Y1 ?

Non. Les ports sont séparés et la prise en charge des thèmes sur Y2 suit ses versions bêta. Voir [Rockbox-Y2 thèmes](rockbox-y2-themes_fr.html).Les thèmes survivent-ils à une mise à jour ?

Généralement oui, car ils vivent sur la carte et le flash écrit le ROM. Si une nouvelle version modifie le chemin du thème, réappliquez un thème qui correspond à son étiquette.Pourquoi le thème n’est-il appliqué qu’à moitié ?

Un redémarrage le résout normalement. Sinon, les fichiers du thème sont incomplets : recopiez son dossier plutôt que de modifier des fichiers individuels.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
