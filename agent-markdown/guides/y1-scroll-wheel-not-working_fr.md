---
title: "Innioasis Y1 La molette de défilement ne fonctionne pas après la mise à jour | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel"
description: "Innioasis Y1 la molette de défilement ou la molette cliquable ne fonctionnent pas après une mise à jour ? Réinstallez le logiciel d&#39;origine Y1, vérifiez l&#39;anneau et séparez le micrologiciel des défauts matériels."
language: "fr"
source: "https://innioasis.app/guides/y1-scroll-wheel-not-working_fr.html"
---

# Innioasis Y1 La molette de défilement ne fonctionne pas après la mise à jour | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel

Récupération du joueur · Innioasis Y1

# Innioasis Y1 la molette de défilement ne fonctionne pas après une mise à jour

La molette tourne mais rien ne bouge, ou la molette cliquable a cessé de répondre juste après un flash. Voici comment séparer une erreur de micrologiciel d'une erreur matérielle et que faire en premier.[Obtenir Updater CE](../guide_fr.html#platform)[Y1 téléchargements de logiciels](../firmware_fr.html?model=Y1&software=original-y1)[Guide de récupération](recovery_fr.html)

## Déterminez si la roue ou le firmware est en cause

Sur un Y1, la roue est une entrée physique, mais le micrologiciel décide de l'effet de chaque tour et clic. Si la roue s'est arrêtée au moment où vous avez mis à jour ou flashé le lecteur, la cause probable est un logiciel et non une pièce cassée. S'il ignore tous les logiciels que vous essayez (stock, Rockbox ou un écran de récupération), traitez-le comme du matériel.
  - Fonctionne dans un logiciel, mort dans un autre : défaut du micrologiciel.
  - Mort sur tous les écrans, y compris la récupération : roue, ruban ou planche.
  - Une seule direction manque : généralement des débris sous la bague ou de l'usure.
  - La roue tourne mais rien ne ressort : le lecteur peut être gelé – forcez d’abord un redémarrage.

## Vérifications rapides avant de réinstaller le firmware
  - Maintenez le bouton d'alimentation enfoncé pendant environ 15 secondes pour forcer l'arrêt du lecteur, puis démarrez-le normalement.
  - Testez la molette sur l'écran d'accueil, dans Paramètres et dans le lecteur de musique.
  - Appuyez sur les boutons physiques. Si la puissance et le retour répondent mais que la roue ne le fait pas, la faute vient de la roue elle-même.
  - Chargez le lecteur pendant 30 minutes avec un câble de données connu : une batterie faible peut rendre les entrées erratiques.
  - Si vous avez installé Rockbox ou une autre version personnalisée, revenez au logiciel d'origine et testez à nouveau.

## Réinstallez le firmware Y1 correspondant à votre lecteur

Étant donné que la roue est pilotée par le micrologiciel, un échec lié à la mise à jour est corrigé en remettant le logiciel d'origine Y1 correct sur le lecteur. N'utilisez pas de package Y2 et ne choisissez pas une version "assez proche" - les packages Y1 sont construits pour le matériel Y1, et une construction Y2 sur un Y1 peut laisser les contrôles mal mappés.
  - Ouvert [Programme de mise à jour CE](../guide_fr.html#platform) sur votre ordinateur.
  - Ensemble Modèle d'appareil à Y1.
  - Choisissez Logiciel d'origine dans Logiciel et choisissez une version stable Y1 - le package manuel est `rom.zip`.
  - Cliquez Installer / Restaurer et laissez le paquet extraire.
  - Éteignez complètement le Y1, connectez le câble de données USB uniquement lorsque le programme de mise à jour le demande et laissez-le jusqu'au message de réussite.
Faites correspondre le modèle et la version. Si la liste des versions ressemble à Y2 logiciel, arrêtez et resélectionnez Y1. Les étapes complètes sont dans le [Guide de restauration Y1](restore-original-y1_fr.html).

## Vérifiez l'anneau de roue pour déceler des débris ou des dommages

Si la roue est rigide, colle ou ne tombe en panne que dans une direction, des peluches et des graviers peuvent se trouver entre l'anneau et le boîtier. Éteignez le lecteur et essuyez autour de l'anneau avec un chiffon en microfibre sec. Ne faites pas couler de nettoyants ou d'alcool dans l'espace et ne soulevez pas l'anneau.

Si l'anneau est desserré, fissuré ou ne clique plus, le joueur a besoin d'une réparation. La réinstallation du micrologiciel ne réparera pas une roue endommagée, un ruban déconnecté ou un liquide endommagé.

## Si le joueur ne démarre pas non plus

Un échec de mise à jour peut empêcher le démarrage du Y1, ce qui ressemble à un problème de roue car rien ne répond. Travailler à travers le [Y1 n'active pas le guide](y1-wont-turn-on_fr.html) pour les étapes de charge, de redémarrage forcé et de récupération manuelle.

## Innioasis Y1 FAQ sur la molette de défilement

### Pourquoi ma molette de défilement Innioasis Y1 a-t-elle cessé de fonctionner après une mise à jour ?

Une mise à jour peut laisser le pilote de roue déphasé par rapport au reste du firmware, surtout si le flash a été interrompu ou si un package Y2 a été utilisé. Réinstallez la version Y1 du logiciel d'origine pour votre modèle et testez la roue sur l'écran d'accueil d'origine.

### Comment puis-je savoir si la molette cliquable Y1 est cassée ou si le micrologiciel est défectueux ?

Testez la roue dans plusieurs logiciels. Si cela fonctionne dans le logiciel d'origine mais pas dans Rockbox, il s'agit d'un problème de mappage du micrologiciel. S'il ne fait rien sur aucun écran, y compris un menu de récupération, suspectez la roue, son ruban ou le tableau.

### La restauration du logiciel d'origine corrigera-t-elle la molette de défilement Y1 ?

Il corrige les échecs causés par une mise à jour ou un package incompatible, et c'est la première chose à essayer. Il ne réparera pas une roue physiquement endommagée, un ruban lâche ou un dommage liquide.

### Puis-je utiliser un progiciel Y2 pour résoudre un problème de roue Y1 ?

Non. Les packages Y1 et Y2 ne sont pas interchangeables, et flasher le mauvais modèle peut aggraver les commandes. Faites correspondre le modèle et la version avant d'exécuter l'installation/restauration.

## Correctifs associés
  - [La molette de défilement Y2 ne fonctionne pas](y2-scroll-wheel-not-working_fr.html) — les mêmes contrôles pour le Y2
  - [Y1 ne s'allume pas](y1-wont-turn-on_fr.html) - récupération de l'alimentation et du démarrage
  - [Innioasis guide de récupération](recovery_fr.html) - tous les guides de symptômes en un seul endroit
  - [Dépannage d'une installation](../troubleshooting_fr.html) — à quoi ressemble un flash défaillant
  - [Restaurer Y1 logiciel d'origine](restore-original-y1_fr.html) - la procédure pas à pas de restauration complète

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
