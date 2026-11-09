---
title: "Innioasis Y2 Ne s'allume pas | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel"
description: "Innioasis Y2 ne s&#39;allume pas ou ne se charge pas ? Forcez un redémarrage, vérifiez si un ordinateur le voit, puis restaurez le micrologiciel Y2 ou utilisez la récupération manuelle SP Flash Tool."
language: "fr"
source: "https://innioasis.app/guides/y2-wont-turn-on_fr.html"
---

# Innioasis Y2 Ne s'allume pas | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel

Récupération du joueur · Innioasis Y2

# Innioasis Y2 ne s'allume pas

Un écran noir ne signifie pas toujours un joueur mort. Effectuez la charge, un redémarrage forcé et la détection sur un ordinateur avant d'essayer un flash manuel.[Obtenir Updater CE](../guide_fr.html#platform)[Téléchargements de micrologiciels](../firmware_fr.html)[Guide de récupération](recovery_fr.html)

## Chargez correctement le Y2 avant toute autre chose

La plupart des rapports « Y2 ne s'allume pas » indiquent une batterie déchargée, un câble de charge uniquement ou un chargeur qui ne peut pas fournir suffisamment de courant. Un Y2 profondément vidé peut prendre 20 à 30 minutes sous tension avant que l'écran n'affiche quoi que ce soit.
  - Utilisez un USB connu données câble, pas un câble de charge uniquement.
  - Essayez un chargeur mural, puis directement le port USB d'un ordinateur, pas un hub.
  - Laissez-le connecté pendant 30 à 60 minutes et surveillez une icône de chargement ou un rétroéclairage.
  - Essayez un deuxième câble et un deuxième chargeur avant de continuer.

## Forcer un redémarrage

Maintenez le bouton d'alimentation enfoncé pendant environ 15 secondes, relâchez-le, attendez cinq secondes, puis appuyez une fois sur le bouton d'alimentation. Cela supprime un démarrage bloqué et peut être répété en toute sécurité.

Si l'écran affiche le logo puis devient noir, le lecteur démarre et échoue – passez à la restauration du micrologiciel ci-dessous. Si rien ne se passe, laissez-le en charge et réessayez après une demi-heure.

## Vérifiez si un ordinateur peut voir le lecteur

Connectez le Y2 éteint avec un câble de données et ouvrez le Gestionnaire de périphériques sous Windows, `lsusb` sous Linux, ou MTKClient sous macOS. Un lecteur fonctionnel apparaît sous la forme d'un appareil MediaTek avec un identifiant de fournisseur. `0e8d`. S'il apparaît, le matériel est suffisamment vivant pour reflasher même lorsque l'écran reste sombre.

Si rien n'apparaît, installez d'abord le pilote MediaTek sous Windows — le [guide du conducteur](../drivers_fr.html) couvre les autorisations Windows et Linux.

## Restaurer le firmware d'origine Y2

Si le lecteur est détecté mais ne démarre pas, réinstallez le logiciel d'origine Y2. Utilisez uniquement un package Y2 ; une build Y1 ne démarrera pas sur le matériel Y2.
  - Ouvert [Programme de mise à jour CE](../guide_fr.html#platform) sur votre ordinateur.
  - Ensemble Modèle d'appareil à Y2.
  - Choisissez Logiciel d'origine dans Logiciel et choisissez une version stable Y2 - le package manuel est `rom_y2.zip`.
  - Cliquez Installer / Restaurer et laissez le paquet extraire.
  - Éteignez complètement le Y2, connectez le câble de données USB uniquement lorsque le programme de mise à jour le demande et laissez-le jusqu'au message de réussite.
Gardez la puissance stable. Un flash qui perd en puissance peut rendre le lecteur inutilisable. Chargez-le d'abord et connectez-le directement à l'ordinateur.

## Récupération manuelle lorsque le programme de mise à jour ne peut pas voir le lecteur

Updater CE inclut des outils de récupération manuelle pour les cas où l'installation guidée ne peut pas se terminer. [SP Flash Tool](../sp-flash-tool_fr.html) est fourni sur Windows et Linux x86, et la route MTKClient couvre macOS. Les deux nécessitent un progiciel correspondant au modèle du [Téléchargements de micrologiciels](../firmware_fr.html) page.

Suivez le guide des outils de votre plateforme plutôt que d'improviser des fichiers scatter ou des décalages. Si le lecteur n'est détecté par aucun outil, le problème vient probablement de la batterie, du port de charge ou de la carte.

## S'il ne démarre toujours pas

Stop flashing and treat it as hardware. Do not open the case or press on the battery. Demandez à la communauté avec le modèle, ce que fait l'écran, si un ordinateur le détecte et quels packages vous avez essayés - le [Discord communauté](https://discord.gg/zHrT2zrcek) peut aider à identifier un itinéraire de service.

Une restauration de stock remplace le système, alors sauvegardez tout ce qui est stocké dans la mémoire interne du lecteur avant de flasher. La musique sur une carte MicroSD n'est pas affectée par la restauration.

## Innioasis Y2 FAQ sur l'alimentation

### Pourquoi mon Innioasis Y2 ne s'allume-t-il pas ?

Les causes habituelles sont une batterie complètement déchargée, un câble de charge uniquement ou un chargeur faible, un crash du micrologiciel qui arrête le démarrage ou un défaut matériel. Chargez-le pendant 30 minutes avec un câble de données connu avant de supposer que le lecteur est mort.

### Comment forcer le redémarrage d'un Innioasis Y2 ?

Maintenez le bouton d'alimentation enfoncé pendant environ 15 secondes, relâchez-le, attendez cinq secondes, puis appuyez une fois sur le bouton d'alimentation. Si rien n'apparaît, laissez-le en charge et réessayez après 30 minutes.

### Puis-je récupérer un Y2 qui ne s'allume pas ?

Souvent oui. Si un ordinateur détecte toujours le périphérique MediaTek, réinstallez le package logiciel d'origine Y2 avec Updater CE. S'il n'est pas détecté, utilisez la récupération SP Flash Tool ou MTKClient incluse avec Updater CE et un fichier de micrologiciel Y2 correspondant au modèle.

### Un Y2 doit-il être chargé avant de clignoter ?

Oui. Un flash qui perd en puissance peut rendre le lecteur inutilisable. Chargez-le d'abord et connectez-le directement à l'ordinateur plutôt que via un hub.

## Correctifs associés
  - [Y1 ne s'allume pas](y1-wont-turn-on_fr.html) — les mêmes contrôles pour le Y1
  - [La molette de défilement Y2 ne fonctionne pas](y2-scroll-wheel-not-working_fr.html) - s'il démarre mais que la roue ne démarre pas
  - [Innioasis guide de récupération](recovery_fr.html) - tous les guides de symptômes en un seul endroit
  - [SP Flash Tool guide](../sp-flash-tool_fr.html) — flashage manuel sous Windows et Linux
  - [Dépannage d'une installation](../troubleshooting_fr.html) — à quoi ressemble un flash défaillant

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
