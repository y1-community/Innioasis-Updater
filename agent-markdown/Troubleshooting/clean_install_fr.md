---
title: "Correction de l'assistance Innioasis Updater et Y1 avec une nouvelle installation - Innioasis Updater"
description: "Installation propre étape par étape pour Innioasis Updater et l&#39;assistant Y1 : supprimez les fichiers restants, réinstallez et revenez au micrologiciel clignotant."
language: "fr"
source: "https://innioasis.app/Troubleshooting/clean_install_fr.html"
---

# Correction de l'assistance Innioasis Updater et Y1 avec une nouvelle installation - Innioasis Updater

## Confirmez que vous avez besoin d'une nouvelle installation

Une réinstallation manuelle est recommandée lorsque vous constatez l'un des symptômes suivants :
  - Le lancement du programme de mise à jour prend quelques minutes ou se bloque lors de la recherche de mises à jour.
  - Les mises à jour cessent d'arriver même si des versions plus récentes existent.
  - Les mises à jour du micrologiciel de l'appareil ne parviennent pas à être téléchargées ou appliquées même si elles sont disponibles.
  - Vous avez ignoré plusieurs versions et n’avez pas utilisé le programme de mise à jour depuis longtemps.

## Windows : effectuez une réinstallation propre

Utilisez le programme d'installation officiel de Windows pour actualiser le programme de mise à jour sur Windows 10 ou Windows 11 (64 bits). Cela remplace entièrement les anciennes versions et restaure le canal de mise à jour automatique.

Avant d'exécuter le programme d'installation, ouvrez Paramètres › Applications › Applications installées (ou l'héritage Ajout/Suppression de programmes panneau) et désinstallez toute copie existante de Innioasis Updater. Démarrer Clean évite les conflits de fichiers.[ Téléchargez le programme d'installation propre pour Windows ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)Étape 1

### Téléchargez le dernier programme d'installation

Enregistrez le programme d'installation dans votre dossier Téléchargements. Fermez Innioasis Updater s'il est en cours d'exécution.Étape 2

### Supprimer toute installation existante

Ouvert Paramètres › Applications › Applications installées (ou l'héritage Panneau de configuration › Ajout/Suppression de programmes) et désinstallez Innioasis Updater pour que la réinstallation démarre à partir d'une table rase.Étape 3

### Installer et relancer

Exécutez le programme d’installation que vous avez téléchargé : Windows vous demandera l’autorisation. Une fois l'installation terminée, lancez Innioasis Updater ; il devrait maintenant détecter automatiquement la version 1.8.2.8 et récupérer à nouveau les mises à jour.

 Cela corrige également les démarrages lents et permet à Updater de récupérer à nouveau les versions du micrologiciel directement auprès des développeurs. 

## macOS : actualisez avec le programme d'installation DMG

Le programme d'installation de macOS efface les anciens fichiers et installe la version 1.8.2.8.[ Télécharger Innioasis Updater DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - Ouvrez le DMG téléchargé et développez la fenêtre du Finder pour voir le Réinstaller option.
  - Exécutez la commande Réinstaller pour actualiser la copie existante de Updater. Cela supprime les anciens fichiers d'assistance susceptibles de bloquer de nouvelles fonctionnalités.
  - Lancez à nouveau Innioasis Updater depuis Applications. Confirmez la version des listes du panneau À propos 1.8.2.8.
 Si vous voyez « Innioasis Updater ne peut pas être ouvert » après la réinstallation, accédez à Paramètres système › Confidentialité et sécurité et choisissez Ouvrir quand même pour approuver l'application. 

## Après la mise à jour vers 1.8.2.8

Une fois que vous utilisez la dernière version, vous accédez aux fonctionnalités ci-dessous. Ceux-ci ne sont disponibles que sur les versions actuelles.
  - Installations en un clic pour le micrologiciel original, les versions communautaires et les versions Rockbox téléchargées directement à partir des versions des développeurs.
  - Étapes guidées claires qui vous indiquent quand connecter le lecteur et quand il peut être débranché en toute sécurité.
  - Améliorations générales de la stabilité et temps de lancement considérablement plus rapides sur les deux plates-formes.

 Besoin d'aide pour vérifier votre version ? Ouvrez Innioasis Updater, choisissez Aide › À propos, et confirmez que la construction s'affiche 1.8.2.8. 

## Vous avez encore besoin d'aide ?

Si la nouvelle installation échoue, capturez tous les messages d'erreur et contactez les canaux d'assistance de la communauté Innioasis. Incluez la version de votre système d'exploitation, la version du programme de mise à jour (si disponible) et les étapes que vous avez déjà essayées.

En gardant votre installation à jour, vous garantissez de toujours recevoir les derniers progiciels et outils au fur et à mesure de leur déploiement.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
