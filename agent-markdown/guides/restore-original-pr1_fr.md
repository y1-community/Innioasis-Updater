---
title: "Restaurer le logiciel d'origine sur Innioasis PR1 - étape par étape"
description: "Comment restaurer le logiciel original officiel sur un Innioasis PR1 avec Innioasis Updater CE ou SP Flash Tool, à l&#39;aide du package vérifié rom_pr1.zip."
language: "fr"
source: "https://innioasis.app/guides/restore-original-pr1_fr.html"
---

# Restaurer le logiciel d'origine sur Innioasis PR1 - étape par étape

Guide de restauration · Innioasis PR1

# Restaurer le logiciel d'origine sur Innioasis PR1

Un retour net au logiciel avec lequel le lecteur a été livré. Utilisez-le après un échec de mise à jour, avant de vendre le lecteur ou chaque fois qu'un système personnalisé ne vous convient pas.[Obtenir Updater CE](../guide_fr.html#platform)[PR1 téléchargements](../firmware_fr.html?model=PR1)[PR1 manuel](../manuals/pr1.html)

Guide d'installation pour votre ordinateur

## Restaurez le logiciel d'origine sur votre PR1 avec votre ordinateur

Choisissez le guide correspondant à l'ordinateur que vous utilisez. Chaque version comprend la configuration de la plate-forme, Updater CE étapes et le chemin de retour au stock.[Guide Windows](/install/original-pr1-windows.html)[Guide macOS](/install/original-pr1-mac.html)[Guide Linux](/install/original-pr1-linux.html)

[Tous les guides Innioasis PR1](/install/pr1.html) · [Tous les guides de logiciels originaux](/install/original-software.html)

## Ce dont vous avez besoin
  - Un ordinateur Windows, macOS ou Linux. Updater CE s'exécute sur les trois.
  - Le câble de données USB fourni avec le lecteur. Les câbles de charge uniquement ne fonctionneront pas.
  - Le fonctionnaire `rom_pr1.zip` package, que le programme de mise à jour télécharge pour vous, ou une copie du [PR1 archives](../firmware_fr.html?model=PR1) si vous préférez flasher à la main.
  - Chargez dans le lecteur. Une restauration qui perd de la puissance est le seul moyen courant d’aggraver une mauvaise situation.

Cela remplace le système et efface le stockage interne. Copiez d'abord la musique, les enregistrements et les photos sur un ordinateur.

## Itinéraire A : Updater CE (recommandé)
  - Installer [Innioasis Programme de mise à jour CE](../guide_fr.html#platform) et ouvrez-le.
  - Ensemble Modèle d'appareil à PR1. Le modèle doit correspondre exactement au joueur.
  - Choisissez Logiciel d'origine dans la liste des logiciels.
  - Choisissez une version. La version stable la plus récente est la valeur par défaut sûre.
  - Presse Installer / Restaurer et attendez que le package soit téléchargé et extrait.
  - Éteignez complètement le lecteur, puis connectez le câble USB uniquement lorsque le programme de mise à jour le demande.
  - Ne touchez pas le lecteur ou le câble jusqu'au message de réussite. Déconnectez et démarrez le lecteur.
Ne choisissez jamais un modèle différent pour « le faire fonctionner ». Un PR1 a besoin d'un package PR1. C’est en mélangeant des modèles que les joueurs finissent par avoir besoin d’une récupération manuelle.

## Itinéraire B : SP Flash Tool (manuel)

Utilisez-le lorsqu'un ordinateur ne peut pas exécuter Updater CE, ou lorsque vous disposez déjà du package et préférez l'outil classique.
  - Télécharger `rom_pr1.zip` de la [PR1 archives](../firmware_fr.html?model=PR1) et décompressez-le.
  - Conservez le fichier scatter à côté des images. Ne renommez pas et ne déplacez pas les images.
  - Ouvrez SP Flash Tool, choisissez Téléchargement uniquement, et chargez le fichier scatter.
  - Éteignez le lecteur, appuyez sur Télécharger, puis connectez le câble.
  - Attendez la marque verte de réussite avant de vous déconnecter.

Le [SP Flash Tool guide](../sp-flash-tool_fr.html) couvre les pilotes et les invites Windows plus en détail. Sous Linux et macOS, Updater CE est la solution la plus simple car elle apporte sa propre gestion USB.

## Après la restauration
  - Déconnectez le lecteur et laissez-le démarrer tout seul.
  - Choisissez votre langue et réglez l'horloge.
  - Reconnectez-vous au Wi-Fi ou au Bluetooth si vous les utilisez.
  - Copiez votre musique. Le [guide de transfert](../manuals/transfer-music.html) a les noms de dossiers.

Si le lecteur démarre mais que l'écran, la molette ou les boutons se comportent toujours mal, la restauration a fonctionné ; c'est une question de matériel ou de configuration, pas de logiciel. Le [guide de dépannage](../troubleshooting_fr.html) est le prochain arrêt.

## Si ça ne marche pas

### Le programme de mise à jour ne voit jamais le joueur

Changez le câble, puis le port USB. Évitez les hubs. Sous Windows, installez le pilote MediaTek à partir du [page du pilote](../drivers_fr.html).

### Le flash s'arrête tôt

Reconnectez-vous, chargez le lecteur et recommencez. Ne passez pas au package d’un autre modèle.

### Le joueur reste noir

Chargez pendant une heure, puis maintenez l'alimentation pendant dix secondes. S'il est toujours mort, lisez le [guide de récupération](../guides/recovery_fr.html) avant de réessayer.

## Les questions que les gens posent

### Est-ce que cela supprimera ma musique ?

Oui, la mémoire interne est effacée. Les fichiers sur une carte microSD survivent généralement, mais copiez-les d'abord dans un endroit sûr.

### Puis-je revenir à Rockbox par la suite ?

Oui. La restauration du logiciel d'origine n'est pas une porte à sens unique ; la page du logiciel personnalisé pour votre modèle peut l'installer à nouveau.

### Ai-je besoin du paramètre Type A / Type B ?

Seul le Y1 a ce choix, et uniquement pour les logiciels originaux. Tous les autres modèles utilisent un seul package.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
