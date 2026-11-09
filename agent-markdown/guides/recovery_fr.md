---
title: "Innioasis Y1 et Y2 Guide de récupération | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel"
description: "Guide de récupération pour les lecteurs Innioasis Y1 et Y2 qui ne s&#39;allument pas ou dont la molette de défilement a cessé de fonctionner après une mise à jour. Étapes de réinitialisation et du micrologiciel."
language: "fr"
source: "https://innioasis.app/guides/recovery_fr.html"
---

# Innioasis Y1 et Y2 Guide de récupération | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel

Récupération du joueur · Y1 et Y2

# Innioasis Y1 et Y2 guide de récupération

Ne s'allume pas, la roue ne fonctionne pas ou une installation s'est arrêtée à mi-chemin. Commencez par le symptôme, puis suivez les étapes dans l’ordre au lieu de passer directement à un flash manuel.[Obtenir Updater CE](../guide_fr.html#platform)[Téléchargements de micrologiciels](../firmware_fr.html)[Dépannage](../troubleshooting_fr.html)

Commencez par Innioasis Updater

## L'installation guidée corrige la plupart de ces problèmes

Le programme de mise à jour le fait en un seul passage. Choisissez le logiciel, suivez les étapes à l'écran et vous avez terminé. Il vous indique également quand un correctif ou une nouvelle version arrive.

## Commencez par le symptôme

Ces guides couvrent les deux échecs que les gens rencontrent le plus souvent après une mise à jour ou un flash. Choisissez celui qui correspond à ce que vous voyez, puis parcourez-le dans l'ordre.

### La molette de défilement ne fonctionne pas

La roue tourne mais le joueur l'ignore, ou elle s'arrête juste après une mise à jour.

[Y1 guide de la molette de défilement](y1-scroll-wheel-not-working_fr.html) · [Y2 guide de la molette de défilement](y2-scroll-wheel-not-working_fr.html)

### Le lecteur ne s'allume pas

Un écran noir, un voyant de charge vide ou un logo qui apparaît et disparaît.

[Y1 guide d'alimentation](y1-wont-turn-on_fr.html) · [Y2 guide d'alimentation](y2-wont-turn-on_fr.html)

### Installation arrêtée à mi-chemin

Le programme de mise à jour a échoué avant ou après l'invite USB, ou la liste des versions semble incorrecte.

[Guide de dépannage](../troubleshooting_fr.html)

### Besoin des fichiers

Logiciel original et packages personnalisés pour chaque modèle.

[Téléchargements de micrologiciels](../firmware_fr.html)

## Les packages Y1 et Y2 ne sont pas interchangeablesNe faites jamais de flash croisé sur un modèle. Un Y1 `rom.zip` n'est pas un package Y2, et un Y2 `rom_y2.zip` ne fonctionnera pas sur un Y1. Flasher le mauvais modèle est l'une des raisons les plus courantes pour lesquelles un joueur se retrouve avec des commandes mortes ou une boucle de démarrage.

Vérifiez le modèle imprimé sur le lecteur, puis faites-le correspondre dans Updater CE avant de choisir une version.

## Restaurez d'abord le logiciel d'origine correspondant

Avant tout outil manuel, remettez le micrologiciel d'origine du modèle correct sur le lecteur. Cela corrige la plupart des échecs de roue et de démarrage liés à la mise à jour.

Y1: sélectionnez Y1, choisissez Logiciel d'origine, choisissez une version stable Y1, puis exécutez Installer/Restaurer. [Guide de restauration complet de Y1](restore-original-y1_fr.html).

Y2: sélectionnez Y2, choisissez Logiciel d'origine, choisissez une version stable Y2, puis exécutez Installer/Restaurer. [Guide de restauration complet de Y2](restore-original-y2_fr.html).

Éteignez le lecteur et connectez le câble de données USB uniquement lorsque le programme de mise à jour le demande. Laissez-le connecté jusqu'au message de réussite.

## Récupération manuelle fournie avec Updater CE

Lorsque le programme de mise à jour ne peut pas terminer le travail, la même installation inclut les outils manuels. [SP Flash Tool](../sp-flash-tool_fr.html) est fourni sur les machines Windows et Linux x86, et la route MTKClient couvre macOS. Les deux nécessitent un progiciel correspondant au modèle, disponible sur le [Téléchargements de micrologiciels](../firmware_fr.html) page.

Utilisez le guide pour votre plateforme et gardez le lecteur chargé. Si aucun outil ne détecte le lecteur, le problème est probablement dû au matériel plutôt qu'au micrologiciel.

## Que faut-il inclure lorsque vous demandez de l'aide
  - Le modèle — Y1 ou Y2 — imprimé sur le lecteur.
  - Ce que fait l'écran : rien, un logo, une boucle de démarrage ou l'écran d'accueil.
  - Si un ordinateur détecte le lecteur comme un périphérique MediaTek.
  - Le message exact du programme de mise à jour et le package que vous avez sélectionné.
  - Ce que vous avez déjà essayé, y compris n'importe quel outil manuel.

Ne publiez pas de jetons privés ou de fichiers système sans rapport. Le [communauté Discord](https://discord.gg/zHrT2zrcek) et [r/innioasis](https://reddit.com/r/innioasis) sont les endroits les plus rapides pour comparer des notes.

## Innioasis FAQ sur la récupération

### Comment réparer un lecteur Innioasis qui ne s'allume pas ?

Chargez-le pendant 30 minutes avec un câble de données connu, forcez un redémarrage en maintenant l'alimentation pendant 15 secondes, puis vérifiez si un ordinateur le détecte. Si tel est le cas, restaurez le logiciel d'origine correspondant au modèle ; sinon, utilisez les outils de récupération manuelle inclus avec Updater CE.

### Pourquoi ma molette de défilement Y1 ou Y2 ne fonctionne-t-elle pas ?

Si la roue s'arrête après une mise à jour, il s'agit généralement d'une incompatibilité de firmware. Réinstallez le logiciel d'origine correspondant au modèle et testez à nouveau. Si la roue est morte dans chaque firmware, traitez-la comme un défaut matériel.

### Où puis-je télécharger le firmware pour la récupération ?

La page de téléchargement du micrologiciel sur innioasis.app/firmware.html héberge des packages originaux et personnalisés pour chaque modèle. Choisissez toujours le package Y1 ou Y2 qui correspond au joueur.

### Quels outils de récupération sont inclus avec Updater CE ?

Updater CE inclut SP Flash Tool sur Windows et Linux, ainsi que la route MTKClient incluant macOS, pour une récupération manuelle lorsque l'installation normale ne peut pas se terminer.

## Correctifs associés
  - [La molette de défilement Y1 ne fonctionne pas](y1-scroll-wheel-not-working_fr.html) - la molette cliquable ne répond pas après une mise à jour
  - [La molette de défilement Y2 ne fonctionne pas](y2-scroll-wheel-not-working_fr.html) — les mêmes contrôles pour le Y2
  - [Y1 ne s'allume pas](y1-wont-turn-on_fr.html) — chargement, redémarrage et récupération manuelle
  - [Y2 ne s'allume pas](y2-wont-turn-on_fr.html) — les mêmes contrôles pour le Y2
  - [SP Flash Tool guide](../sp-flash-tool_fr.html) — flashage manuel sous Windows et Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
