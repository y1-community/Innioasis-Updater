---
title: "Développeurs | Ajouter un micrologiciel personnalisé aux téléchargements de micrologiciels Innioasis Updater CE - Innioasis"
description: "Documentation du développeur pour ajouter un micrologiciel Innioasis Y1 ou Y2 personnalisé à Updater CE : forkez le référentiel, publiez les ressources rom.zip, modifiez slidia_manifest.xml, testez et ouvrez une demande d&#39;extraction."
language: "fr"
source: "https://innioasis.app/developers_fr.html"
---

# Développeurs | Ajouter un micrologiciel personnalisé aux téléchargements de micrologiciels Innioasis Updater CE - Innioasis

Pour les développeurs de firmware

# Ajoutez votre micrologiciel à Updater CE.

Updater CE est le catalogue communautaire et le programme d'installation du micrologiciel personnalisé. Développez votre projet à partir d'une base ROM, publiez-le en tant que référentiel public avec les ressources de version appropriées, ajoutez les entrées de modèle à `slidia_manifest.xml`, testez les filtres du modèle et ouvrez une pull request. Un référentiel peut servir tous les modèles qu'il prend en charge.[Afficher la source Updater CE](https://github.com/y1-community/Innioasis-Updater)[Parcourir les téléchargements de logiciels](firmware_fr.html)

## Partir d'une base ROM

Les ROM de base offrent aux développeurs de micrologiciels personnalisés une base Android propre avec les puces radio sans fil activées. Sur le Y1, ils activent le Wi-Fi et le GPS aux côtés du Bluetooth et de la FM d'usine ; sur le Y2, ils activent le Wi-Fi, le GPS et la FM aux côtés du Bluetooth d'usine.Téléchargements de base ROM pour le développement de micrologiciels personnalisés, avec la version Android et les fonctionnalités sans fil que chacun permet[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Télécharger | Appareil | Android | Fonctionnalités sans fil |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Ajoute le Wi-Fi et le GPS au Bluetooth et à la FM d'usine (FM fonctionne déjà sur le Y1 de l'usine). Pour les lecteurs Y1 livrés avec OS 2.0.0 ou version ultérieure. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Ajoute le Wi-Fi et le GPS au Bluetooth et à la FM d'usine (FM fonctionne déjà sur le Y1 de l'usine). Pour les lecteurs Y1 livrés avec un système d'exploitation antérieur à 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Ajoute le Wi-Fi, le GPS et la FM au Bluetooth d'usine. La puce radio Y2 est entièrement activée, donc la FM est également disponible ici. |

Ces images représentent la base Android d'origine (AOSP) avec les radios sans fil de l'appareil activées, de sorte qu'un micrologiciel personnalisé peut ajouter des fonctionnalités réseau au lieu de remplacer la pile radio. Ils constituent le point de départ pratique des étapes de publication ci-dessous.

## Utilisez ces noms d'éléments de version

Le nom de fichier fait partie du signal de compatibilité. Gardez les noms exacts et placez les fichiers ZIP dans les ressources de version du projet, pas seulement dans l'arborescence des sources du référentiel.Noms des actifs ZIP du micrologiciel et appareils pris en charge``````

| Actif | Appareil | Matériel | Signification |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 appareils livrés avec OS 2.0.0 ou version ultérieure. |
| rom_type_b.zip | Y1 | Type B | Y1 appareils livrés avec un système d'exploitation antérieur à 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Le package d'installation complète Y2. Gardez-le séparé des actifs de Y1. |
Ne renommez pas un package pour l’adapter à un autre modèle. Y1 et Y2 utilisent des fichiers de plate-forme MediaTek et une configuration clignotante différents. Publiez le package pour le matériel qu’il prend réellement en charge.

## Comment fonctionne la connexion

Updater CE lit le manifeste comme son catalogue. Chaque `<package>` La ligne lui indique le nom du projet, le référentiel, le modèle et le gestionnaire. Lorsqu'un utilisateur choisit ce projet, Updater vérifie les versions publiées du référentiel et recherche un `rom*.zip` actif.

### Manifeste

Nomme le projet et le mappe à un modèle. Y1 et Y2 nécessitent des lignes distinctes, même lorsqu'ils partagent un référentiel.

### Version publiée

Contient les ressources ZIP installables. Une seule version peut contenir les packages Y1 Type A, Y1 Type B et Y2 ensemble.

### Updater CE installer

Utilise le modèle sélectionné pour choisir le package correspondant et le chemin de clignotement spécifique au modèle. L'utilisateur ne devrait pas avoir à deviner le nom d'un fichier.

## Publier un projet en cinq étapes
  - Forkez le référentiel Updater CE. Créez votre propre fourchette de [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), puis clonez votre fork localement.
  - Préparez un référentiel public de micrologiciels. Assurez-vous que le référentiel est public et que sa version contient les ressources ZIP appropriées. Vous pouvez mettre `rom.zip`, `rom_type_b.zip`, et `rom_y2.zip` sur la même release lorsqu'ils appartiennent à la même version.
  - Modifiez le manifeste. Ouvert `slidia_manifest.xml` à la racine de votre fourchette Updater CE. Ajoutez une ligne pour chaque modèle pris en charge par la version (Y1 et Y2 sont la paire commune). Le `repo` la valeur est celle du référentiel `owner/repository`; `url` est la page publique du projet.
  - Testez le catalogue. Exécutez Updater à partir de la caisse modifiée. Sélectionnez Y1 et confirmez que le projet affiche les actifs Y1. Sélectionnez Y2 et confirmez qu'il affiche la version Y2. Cochez Type A et Type B séparément lorsque les deux sont publiés.
  - Ouvrez une pull request. Envoyez la modification du manifeste vers votre fork et ouvrez une demande d'extraction sur le référentiel Updater CE en amont. Incluez le lien du projet, les modèles pris en charge, la balise de version, les noms des actifs et les appareils que vous avez testés.

## Générez vos lignes de manifeste

Remplissez le référentiel et cochez chaque modèle pris en charge par la version. Le générateur en écrit un `<package>` ligne par modèle et inclut uniquement les attributs que vous avez définis, de sorte que le résultat correspond au courant `slidia_manifest.xml` format. Chaque attribut Updater CE lu est disponible ci-dessous — les facultatifs sont sous Plus d'options.URL du référentielLe référentiel public GitHub. Le générateur extrait `owner/repository` à partir de l'URL.Nom du logicielAffiché dans l'application et le catalogue du site.URL du projetPage destinée aux humains pour le projet ou ses notes de version.MarqueDécochez cette option pour utiliser la marque par défaut du modèle. SR1, Q3, Q5 et Q3e sont des modèles Timmkoo.Appareils (une ligne chacun)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eAutres modèlesPour un modèle qui n'est pas répertorié ci-dessus. Les modèles connus conservent l'orthographe de leur catalogue.Drapeaux`do_not_keep_data` - ne proposez jamais Keep Data pour ce firmwareConstruit à partir du logiciel original — ajoute `derivative="y1-community/y1-stock-rom"`

Keep Data n'est proposé que lorsque le firmware entrant et le firmware installé sont identiques ou partagent un `derivative` racine. Utilisez l'indicateur uniquement lorsque les données utilisateur ne peuvent réellement pas être transférées.Plus d'options : icône, illustration, ressources de version, post-installation et miroirs

#### Icône et oeuvre d'artFichier d'icôneChoisissez l'image que vous allez valider dans le référentiel. Cela le prévisualise et construit son URL brute ; il ne télécharge rien.Chemin de l'icône dans le référentielChemin d'accès à l'image validée, par rapport à la racine du référentiel.Branche d'icôneURL de l'icôneUne URL d’image directe. Lorsqu'elle est vide, l'application utilise la version `updater.png` ou une icône générée.Aperçu de l'icône sélectionnée

URL de l'icône du mode sombreIcône de thème sombre en option. `image_dark` est un pseudonyme accepté.URL de l'illustration lumineuseIllustration secondaire, essayée après la sortie de l'image et `icon`.URL de l'illustration sombre

#### Libérer des ressourcesNom de l'élément de versionUn nom pour chaque modèle sélectionné. Laisser vide pour pouvoir l'utiliser `rom.zip` le Y1 et `rom_<model>.zip` autre part.Modèle d'actifGlob utilisé lorsque les zips de la version ne sont pas nommés `rom*.zip`.Type A élémentGlob pour le package Y1 Type A lorsque son nom ne le dit pas.Type B élémentGlob pour le package Y1 Type B lorsque son nom ne le dit pas.Version minimale de l'applicationMasquez l’entrée des anciennes versions de Updater CE.

#### Liens, miroirs et famille Keep DataPage de post-installationOuvert après une installation réussie.Deuxième page post-installationDeuxième étape facultative pour un guide de configuration de plusieurs pages.Miroirs zippés portablesSéparés par des virgules `*-mirror` référentiels qui créent des packages Portable Flashing Zip.Dépôt dérivéLe firmware à partir duquel cette version est construite. Les firmwares associés partagent une partition de données, ce que Keep Data vérifie.Référentiel d'informationsDépôt d'applications dont les versions décrivent les applications de ce firmware. Il a également besoin d'une page post-installation.APK dépôtDépôt d'application dont APK l'application télécharge et installe après le firmware.

#### Extras du catalogueLimaceIdentifiant stable pour les liens et les enregistrements d'installation enregistrés. Le modèle est ajouté automatiquement lorsque plusieurs modèles sont sélectionnés.Descriptif`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Copier des lignes

Chargement du dernier manifeste…Prévisualisez le dernier manifeste avec vos lignes ajoutées

Le générateur récupérait le courant `slidia_manifest.xml` depuis ce référentiel et inséré vos lignes générées juste avant `</slidia>`.

Une ligne ne suffit pas pour un référentiel partagé. Si la ligne Y2 est manquante, les utilisateurs Y2 n'obtiendront pas d'entrée correspondant au modèle même si `rom_y2.zip` existe dans la version du projet. La même chose est vraie pour tous les autres modèles pris en charge par votre version.

### Chaque attribut lu par le manifeste

Ce sont les attributs que les builds actuels de Updater CE comprennent. Le générateur écrit uniquement ceux que vous remplissez ; l'application revient à des valeurs par défaut raisonnables pour le reste.Attributs du package slidia_manifest.xml et leur signification``````````````````````````````````````````````````````````````````````````````````````````````

| Attribut | Nécessaire | Ce que ça fait |
| --- | --- | --- |
| name | Oui | Nom du logiciel indiqué dans le catalogue et sur les cartes d'installation. |
| repo | Oui | owner/repo. L'application lit les versions GitHub de ce référentiel. |
| device | Oui | Modèle cible, majuscule (Y1, Y2, G1, Q3e,…). Gardez une entrée par modèle. |
| url | Recommandé | Page du projet ou notes de version ouvertes à partir du catalogue. |
| type, handler | Oui en pratique | type="img" et handler="Custom Firmware". Les autres types et gestionnaires non micrologiciels sont ignorés. |
| brand | Facultatif | Marque du catalogue (Innioasis, Timmkoo). Empty utilise la marque par défaut du modèle. |
| package_name | Facultatif | Libérer le nom du fichier de ressource. La valeur par défaut est rom.zip le Y1 et rom_<model>.zip sur d'autres modèles. |
| asset_pattern | Facultatif | Globe insensible à la casse pour les versions dont les zips du micrologiciel ne sont pas nommés rom*.zip (Par exemple my-firmware-*.zip). |
| type_a_asset, type_b_asset | Facultatif | Globs qui identifient les zips Y1 Type A et Type B lorsque leurs noms de fichiers ne contiennent pas les marqueurs habituels. |
| icon | Facultatif | URL du logo. Utilisé après la propre version updater.png / updater.jpg, et comme solution de secours pour chaque version. |
| icon_dark | Facultatif | Logo sur le thème sombre. image_dark est un pseudonyme accepté. |
| image | Facultatif | Illustration de lumière secondaire, essayée après icon. |
| post_install, post_install2 | Facultatif | Page(s) ouverte(s) après une installation réussie. Le second couvre un guide en plusieurs étapes. |
| portable_zips | Facultatif | Séparés par des virgules *-mirror les dépôts qui publient des packages portables prêts à être exécutés. |
| derivative | Facultatif | Référentiel à partir duquel le firmware est construit. Un micrologiciel avec la même racine dérivée peut conserver les données utilisateur. |
| info_repo | Facultatif | Référentiel d'applications dont les versions décrivent ce que le firmware déploie. Nécessite post_install ou post_install2. |
| apk_repo | Facultatif | Référentiel d'applications dont APK l'application installe après le firmware. |
| min_version | Facultatif | Masquez l'entrée lorsque Updater CE est plus ancien que cette version. |
| do_not_keep_data | Facultatif | true (aussi 1 / yes) bloque complètement Keep Data pour ce firmware. |
| slug | Facultatif | Identifiant stable pour les liens et les enregistrements d'installation enregistrés. Généré à partir du nom et du modèle lorsqu'il est vide. |
| description | Facultatif | Brève description du catalogue. Il peut s'agir de la valeur de l'attribut ou du texte de l'élément. |

Les anciens noms sont toujours lus pour des raisons de compatibilité : `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` et `image_dark`. Les nouvelles entrées doivent utiliser les noms actuels ci-dessus.

### Soumettez les lignes sous forme de pull request
  - Copiez les lignes générées ci-dessus. Ils correspondent déjà au dernier format de manifeste.
  - Modifier `slidia_manifest.xml` dans le référentiel. Utilisez le lien de modification ci-dessous ; l'hôte du référentiel crée automatiquement un fork et une branche pour vous.
  - Collez les lignes juste avant `</slidia>`, en gardant les entrées existantes inchangées.
  - S'engager dans une nouvelle branche (Par exemple `add-your-firmware`), puis ouvrez une pull request sur le référentiel Updater CE.
  - Dans le PR, incluez le lien du projet, les modèles pris en charge, la balise de version, les noms des actifs et les appareils que vous avez testés.
[Modifier le manifeste Updater CE](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Voir le dernier manifeste](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Gardez les noms de modèles en majuscules, utilisez l'URL exacte de votre référentiel public et conservez `type="img"` et `handler="Custom Firmware"` pour une entrée de firmware.

## Rendre la version facile à vérifier

Donnez à la version une étiquette claire et une note de version. La balise est utile aux gens, mais les noms des actifs ZIP sont ce que Updater CE utilise pour identifier les packages d'installation.

### Liste de contrôle de sortie
  - Publier le communiqué publiquement.
  - Joignez les fichiers ZIP en tant qu'actifs de version.
  - Indiquez le modèle pris en charge et Type A ou Type B dans les notes.
  - Énumérez toute préparation requise ou limites connues.

### Une version, trois atouts

Une version partagée peut contenir `rom.zip`, `rom_type_b.zip`, et `rom_y2.zip`. Updater les classe séparément et choisit parmi les filtres de modèle et de matériel.

### Ne regroupez pas les suppositions

N'incluez pas de package Y1 sous le nom de fichier Y2, et n'ajoutez pas de données scatter, préchargement ou partition non testées simplement pour faire apparaître un actif.

## Pourquoi les entrées de modèle sont importantes pendant le flashage

Le manifeste n'est pas seulement un menu de téléchargement. Après l'extraction, Updater CE utilise le modèle résolu pour préparer le chemin d'installation correspondant. Y1 et Y2 ont des fichiers de plate-forme, des préchargeurs, une configuration scatter et des dispositions de périphérique différents.
  - Y1: le programme de mise à jour prépare le chemin Y1 et utilise les partitions nommées du périphérique lorsque MTKClient est utilisé.
  - Y2: le programme de mise à jour prépare le chemin Y2 et utilise la configuration Y2 MT6582. La récupération complète peut utiliser les adresses physiques des données de dispersion correctes du modèle.
  - Prise en charge multiplateforme : Updater CE gère le flash natif directement sur Windows, Linux et macOS (prenant en charge les Mac Intel et Apple Silicon) sans outils de flash supplémentaires.
Les contributeurs doivent fournir des fichiers de firmware corrects, et non des décalages flash. Ne modifiez pas les adresses scatter, les préchargeurs, les fichiers DA ou les commandes de partition pour contourner un package défectueux. Corrigez l’actif de version et testez sur le modèle prévu.

## Avant de demander une fusion
  - Validez le XML avec un analyseur XML. Une citation ou une clôture manquante `/>` peut masquer chaque entrée après.
  - Lancez le programme de mise à jour depuis votre caisse afin qu'il charge le manifeste local avant l'actualisation à distance.
  - Vérifiez Y1 et Y2 indépendamment. Confirmez que le projet apparaît uniquement là où son package est pris en charge.
  - Consultez la liste des versions pour `rom.zip`, `rom_type_b.zip`, et `rom_y2.zip` le cas échéant.
  - Testez l'installation réelle sur l'appareil prévu, avec un câble de données USB fiable et un plan de récupération pour revenir au logiciel d'origine.
  - Dans la pull request, expliquez ce que vous avez testé. Ne décrivez pas un modèle non testé comme pris en charge.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Pour une vérification locale, exécutez cette commande à partir de la racine du référentiel. Il vérifie uniquement la syntaxe XML ; cela ne prouve pas qu'une version contient un micrologiciel valide ou qu'un périphérique peut flasher en toute sécurité.

## Liens utiles vers le projet[Fourchette Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Voir le manifeste](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Notes de contribution communautaire](support_devs_fr.html)[Dépannage](troubleshooting_fr.html)

## Compétences de modding pour les agents IA

Le référentiel `skills/` L'annuaire est une base de connaissances basée sur la source pour les agents travaillant sur le matériel, le micrologiciel, les thèmes et les applications Y1 et Y2. Chaque compétence nomme les fichiers de projet d'où proviennent ses revendications, afin qu'un agent puisse vérifier un fait avant de changer d'appareil.Commencez ici

### [Index des compétences et règles de sécurité](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Comment charger une compétence, à quel modèle un fait s'applique et aux partitions qu'aucun paquet ne doit écrire.Matériel

### [Y1 matériel](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, la roue comme événements clés, affichage 480x360, chemins FM/audio, stockage et carte de partition Type A/B.Matériel

### [Y2 matériel](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Carte MT6582, arborescence des périphériques, panneaux GC9503V/ST7701S, rails PMIC/DAC, partitions et image de démarrage.Micrologiciel

### [Paquets de micrologiciels](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomie, fichiers scatter, contrats de mise à jour de classe A et liste de contrôle de publication.Thèmes

### [Création de thèmes et de skins](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 thèmes config.json, Rockbox WPS/SBS, Reborn skins et Y2Player format de skin v2.Toutes les compétences

### [Parcourez le dossier des compétences](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, ROM Android en stock, Y2Linux, applications Android, lanceurs, notes de version et publication de sites.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
