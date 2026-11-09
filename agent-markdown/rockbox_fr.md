---
title: "Comment installer Rockbox sur votre Innioasis Y1 ou Y2 - Innioasis Updater"
description: "Installez Rockbox sur un Innioasis Y1 ou Y2 avec Updater : thèmes, versions stables, notes Type A et Type B, et comment restaurer le logiciel d&#39;origine après."
language: "fr"
source: "https://innioasis.app/rockbox_fr.html"
---

# Comment installer Rockbox sur votre Innioasis Y1 ou Y2 - Innioasis Updater

Rockbox référence

# Obtenir Rockbox sur votre Y1 ou Y2

Rockbox modifie le logiciel du lecteur et ouvre une interface de lecteur de musique plus profonde, des commandes de lecture, des options de tri et de thème. L'installation est guidée, mais Y1 et Y2 sont des parcours distincts.[Rockbox sur Y1](guides/rockbox-y1.html)[Rockbox sur Y2](guides/rockbox-y2.html)[Pourquoi Rockbox ?](rockbox-benefits_fr.html)

## Ce que l'installation change

Rockbox est un logiciel personnalisé. Cela ne supprime pas votre possibilité de revenir à l'interface d'origine lorsque le package logiciel d'origine correspondant est disponible. Il peut améliorer la navigation et la personnalisation de la musique, mais les fonctionnalités, la résolution, la durée de vie de la batterie et la compatibilité des thèmes dépendent de la version.Ne mélangez pas les modèles. Sélectionnez Y1 pour un lecteur Y1 et Y2 pour un lecteur Y2. Un nom de version similaire ne constitue pas une preuve suffisante de la compatibilité d'un package.

## Regardez la vidéo

Vidéo de Frawgeeys. Il montre l'itinéraire Innioasis Updater ; utilisez les étapes écrites spécifiques au modèle ci-dessous pour votre Y1 ou Y2.

Vidéo par [Place Cristian](https://www.youtube.com/@CristianPlaza) (Espagnol), affichant Rockbox sur un Y1. Utilisez les étapes spécifiques au modèle ci-dessous pour votre lecteur.

## La route partagée du programme de mise à jour
  - Installez Updater et ne connectez rien jusqu'à ce qu'il vous le demande.
  - Choisissez le modèle imprimé sur le lecteur en Modèle d'appareil.
  - Choisissez Rockbox dans Logiciel.
  - Choisissez une version stable, sauf si vous testez délibérément une version nocturne.
  - Cliquez Installer / Restaurer, puis suivez l'invite de mise hors tension et de connexion USB.
  - Déconnectez-vous uniquement après le message de réussite.

## 240p, 360p et thèmes

Les anciennes collections de thèmes Rockbox peuvent être créées pour 240p. Les builds de la communauté Y1 utilisent également des étiquettes de compatibilité 360p. Lisez les notes de version et la source du thème avant de choisir une version. Un thème conçu pour une résolution ou une famille de logiciels peut ne pas fonctionner sur une autre.[Parcourir les thèmes de la communauté](https://themes.innioasis.app/?lang=fr)[Outils thématiques](https://themes.innioasis.app/?lang=fr)

## Revenir au logiciel d'origine

Choisissez à nouveau le même modèle, sélectionnez Logiciel d'origine, choisissez une version stable et utilisez Installer / Restaurer. Si l'échec s'est produit avant l'invite USB, vérifiez l'ordinateur et les fichiers extraits. Si le lecteur a été détecté mais que le flash a échoué, commencez par [dépannage](troubleshooting_fr.html).[Y1 restaurer](guides/restore-original-y1.html)[Y2 restaurer](guides/restore-original-y2.html)

## FAQJ'ai réinstallé Rockbox et cela n'a rien résolu.

La réinstallation de Rockbox écrit la même version sur les mêmes fichiers, elle ne peut donc pas réinitialiser les éléments que Rockbox conserve sur MicroSD. Si le problème concerne un paramètre, un thème, une liste de lecture ou une base de données défectueux qui réside sur la carte, la réinstallation ne le résoudra pas. La réinitialisation fiable supprime le `.rockbox` dossier du MicroSD — Rockbox en crée un nouveau au prochain démarrage.
  - Éteignez complètement le lecteur et retirez la carte MicroSD, ou connectez le lecteur en tant que lecteur USB.
  - Affichez les fichiers cachés sur votre ordinateur pour que le dossier soit visible. Comment afficher les fichiers cachésAfficher les fichiers dot sur votre ordinateurWindows: dans l'Explorateur de fichiers, ouvrez le Voir tabulation et coche Objets cachés.macOS: dans le Finder, appuyez sur Cmd+Shift+. pour basculer les fichiers cachés.Linux · Fichiers GNOME : appuyez sur Ctrl+H, ou ouvrez le menu et choisissez Afficher les fichiers cachés.Linux · Dauphin KDE : appuyez sur Ctrl+H, ou utiliser Affichage → Afficher les fichiers cachés.
  - Supprimer le `.rockbox` dossier à partir de la racine de la carte.
  - Réinsérez la carte et démarrez le lecteur. Rockbox recrée le dossier avec les valeurs par défaut.
  - Réappliquez votre thème et vos paramètres. Si le problème ne réapparaît qu’après un thème spécifique, ce thème en est la cause.

Suppression `.rockbox` ne désinstalle pas Rockbox et ne touche pas votre musique - le dossier contient les paramètres, les thèmes et les caches et est reconstruit automatiquement. Si vous souhaitez conserver vos thèmes, copiez le dossier hors de `.rockbox` avant de le supprimer, ou renommez le dossier en `.rockbox-old` d'abord.Pourquoi ne puis-je pas voir le dossier .rockbox sur mon MicroSD ?

Les dossiers dont le nom commence par un point sont masqués par défaut sur la plupart des ordinateurs. Vous n'avez pas besoin de le voir pour installer Rockbox — Updater gère les fichiers. Si vous effectuez un dépannage et souhaitez le supprimer, activez d'abord les fichiers cachés. Comment afficher les fichiers cachésAfficher les fichiers dot sur votre ordinateurWindows: dans l'Explorateur de fichiers, ouvrez le Voir tabulation et coche Objets cachés.macOS: dans le Finder, appuyez sur Cmd+Shift+. pour basculer les fichiers cachés.Linux · Fichiers GNOME : appuyez sur Ctrl+H, ou ouvrez le menu et choisissez Afficher les fichiers cachés.Linux · Dauphin KDE : appuyez sur Ctrl+H, ou utiliser Affichage → Afficher les fichiers cachés.La suppression de .rockbox réinitialisera-t-elle mon thème et mes paramètres ?

Oui - `.rockbox` contient les paramètres, le thème, les listes de lecture et la base de données mise en cache de Rockbox. Le supprimer ramène Rockbox à un état par défaut propre. Sauvegardez l'intégralité du dossier (ou renommez-le en `.rockbox-old`) si vous souhaitez en récupérer une partie, démarrez le lecteur et Rockbox crée un nouveau dossier.

## Plus de guides Rockbox-Y1 et Rockbox-Y2

Découvrez les guides étape par étape pour l'installation, le téléchargement, la création de thèmes, la restauration et le dépannage Rockbox sur les deux modèles :[Rockbox-Concentrateur Y1](rockbox-y1/)[Rockbox-Concentrateur Y2](rockbox-y2/)[Rockbox Téléchargements de ROM](rockbox-rom-download_fr.html)[Rockbox pour l'année 1](rockbox-for-y1_fr.html)[Rockbox pour l'an 2](rockbox-for-y2_fr.html)[Rockbox-Y1 contre Y2](rockbox-y1-vs-y2.html)[Rockbox-Thèmes Y1](rockbox-y1-themes.html)[Rockbox-Thèmes Y2](rockbox-y2-themes.html)

## Cette référence a-t-elle été utile ?

Votre réponse contribue à améliorer ce guide.OuiPas encore[Faites-nous savoir comment nous pouvons nous améliorer](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
