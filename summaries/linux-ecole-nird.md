# AlpOSS 2026 - Linux à l'école ? Enfin un espoir avec la démarche NIRD !

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Bertrand Chartier et Marius Monnier |
| **Organisation** | Académie de Grenoble / Lycée Marie Curie (Échirolles) |
| **Durée** | 28:33 |
| **Présent** | ✅ Oui |

## À propos des intervenants

**Bertrand Chartier** est enseignant à Montélimar et chargé de mission au sein de la délégation académique au numérique (DAN) de l'académie de Grenoble, où il travaille sur les plateformes en ligne et les communs numériques éducatifs. Il est l'un des promoteurs de la démarche NIRD au niveau académique et contribue à la diffusion nationale du mouvement.

**Marius Monnier** est enseignant d'informatique (NSI — Numérique et Sciences Informatiques) au lycée Marie Curie d'Échirolles. Il a déployé une salle Linux sous Debian dans son établissement et contribue techniquement au développement de la distribution NIRD. Il intervient du côté pratique et technique de la démarche.

## Résumé

Cette présentation dure près de 30 minutes et inclut une session de questions-réponses nourrie. Elle se déroule en deux temps : Bertrand Chartier expose la démarche NIRD dans son ensemble, puis Marius Monnier entre dans les détails techniques et les réalisations locales.

**Bertrand Chartier — La démarche NIRD : contexte et modèle.**

NIRD signifie **Numérique Inclusif, Responsable et Durable**. L'acronyme résume une vision pédagogique : le but n'est pas simplement d'installer Linux, mais de transmettre aux élèves une culture numérique alignée avec les valeurs d'inclusion, de protection des données personnelles et de pérennité des usages. Bertrand remercie ironiquement Microsoft pour les incompatibilités de Windows 11, qui ont déclenché une dynamique de questionnement dans les établissements scolaires.

Le modèle s'inspire du **lycée Carnot (Nord-Pas-de-Calais)**, établissement pionnier qui a initié la démarche : des élèves ont reconditionnés des ordinateurs voués à la destruction, les ont équipés de la distribution **Primetux** (distribution Linux légère spécialement conçue pour les écoles), et sont allés les livrer dans des écoles primaires — en vélo électrique avec une remorque pouvant transporter 50 machines. Ce lycée a reçu un prix national en 2023 pour cette initiative. La dimension sociale et développement durable est centrale : les élèves formés deviennent des ressources pour le territoire local, que ce soit pour maintenir des parcs informatiques de collectivités ou pour créer des emplois dans des PME locales.

La démarche NIRD fonctionne sur un **cercle vertueux** : les enseignants forment les élèves, qui reconditionnent des ordinateurs destinés à la poubelle, lesquels sont redistribués aux familles dans le besoin, aux mairies, aux associations. Les collectivités économisent sur leur parc et peuvent investir dans l'économie locale (contrats de maintenance avec des jeunes formés). La ville de Blois en est un exemple concret : 400 ordinateurs et 400 tablettes reconditionnés pour toutes les écoles de la ville.

Aujourd'hui, la démarche rassemble plusieurs dizaines d'établissements dans toute la France, et même au-delà des frontières. Dans l'académie de Grenoble, plus de 15 établissements ont rejoint le mouvement. La région Auvergne-Rhône-Alpes met à disposition des **Masters Linux** dans les lycées, facilitant le déploiement de stations Linux en remplacement des stations Windows. Le déploiement repose sur le logiciel **FOG** (déploiement d'image réseau) et est opéré par **Atos**, le prestataire régional des lycées.

**Marius Monnier — Le côté technique au lycée Marie Curie.**

Marius prend la parole pour décrire ce qui a été mis en place au lycée Marie Curie d'Échirolles. Trois facteurs favorables expliquent l'avance de l'académie de Grenoble : (1) la matière **NSI** (enseignée dans 49 lycées sur ~100 dans la région) impose dans ses référentiels l'utilisation d'un système d'exploitation libre ; (2) le déploiement Linux est facilité par la solution régionale Ubuntu + FOG d'Atos ; (3) la DAN de l'académie communique activement sur les libertés numériques et pousse la démarche NIRD.

Au lycée Marie Curie, une salle entière est déployée sous **Debian** — non pas la solution régionale Ubuntu, jugée trop lente (1 min 40 s au démarrage), mais une solution personnelle qui démarre en 20 secondes. Cette salle est entièrement intégrée au réseau du lycée (authentification SSO LDAP, pas de compte séparé pour les élèves). Dans les autres salles, la solution régionale Ubuntu est déployée pour limiter le "bus factor" (éviter la dépendance à une seule personne). Les élèves utilisent librement LibreOffice et d'autres logiciels libres sans s'en rendre compte, le passage à Linux étant totalement transparent.

La **distribution NIRD** est évoquée comme projet collectif national : initiée par le lycée Carnot après une cyberattaque (besoin d'une distribution live utilisable hors ligne), elle est aujourd'hui en version bêta (0.1-0.2). L'objectif à moyen terme est d'en faire un dépôt de paquets indépendant, permettant à n'importe qui d'enrichir sa distribution Linux via le dépôt NIRD. La distribution est hébergée sur la **Forge des communs numériques éducatifs** (forge.apps.education.fr/nird/distribution-nird). Le collectif cherche des retours d'expérience, des contributeurs extérieurs à l'éducation nationale, et du soutien pour le reconditionnement et la redistribution des machines.

**Questions-réponses** : les échanges abordent l'intégration du libre dans les référentiels officiels (le terme « système d'exploitation libre » est noir sur blanc dans le programme NSI), les différences entre distribution NIRD et Primetux, les projets existants proches (Abuledu, Sambaedu, EUOS), les besoins de financement nuls (tout est bénévole), et la demande croissante de contributions depuis une vidéo de présentation (dizaines de demandes par jour). Une maman en salle témoigne de l'absence totale de sensibilisation au libre pour sa fille en terminale, soulignant le fossé entre les référentiels officiels et la réalité du terrain.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Linux Mint / Debian / Ubuntu** — Distributions Linux déployées en environnement scolaire. Retour d'expérience direct sur la gestion de parcs Linux en établissements publics, déploiement à grande échelle via image réseau.
- **FOG Project** — Logiciel open source de déploiement d'images disque par le réseau (clone réseau). Utilisé par Atos pour déployer les images Linux dans les lycées régionaux. Outil de référence pour les ESN en charge de déploiements massifs de postes de travail.
- **Primetux** — Distribution Linux légère conçue spécialement pour les écoles primaires, fonctionnant offline avec des logiciels pédagogiques préinstallés. Pertinente pour les missions d'équipement de collectivités ou d'associations en matériel reconditionné.
- **Distribution NIRD** — Surcouche Linux Mint / Debian en cours de développement, pensée pour le déploiement live offline en environnement éducatif. À surveiller pour les ESN intéressées par les communs numériques et les marchés Education.
- **Forge des communs numériques éducatifs** — Forge GitLab hébergée par l'État (forge.apps.education.fr), espace de collaboration pour les projets numériques éducatifs. Exemple d'infrastructure souveraine d'hébergement de code public.
- **LDAP / SSO** — Intégration annuaire et authentification unique pour les stations Linux, compatibles avec l'infrastructure existante du lycée (Active Directory ou équivalent). Compétence clé pour les ESN intégrant des postes Linux dans des parcs mixtes.
- **LibreOffice** — Suite bureautique libre déployée sur toutes les stations Linux des établissements. Cas concret d'usage en remplacement de Microsoft Office en environnement éducatif tertiaire (incluant des filières bureautiques).
- **Sambaedu** — Serveur d'intégration Linux/Windows pour les établissements scolaires (évoqué dans les questions). Alternative à Active Directory pour les ESN accompagnant le secteur public éducatif.
- **Mastodon / Tchap** — Outils de communication utilisés par le collectif NIRD : Mastodon pour le grand public, Tchap (messagerie instantanée de l'État) pour les agents de la fonction publique. Pertinent pour les ESN travaillant avec l'administration.

## Points marquants

- **Windows 11 et la fin des ordinateurs low-cost comme déclencheur** : l'incompatibilité de Windows 11 avec du matériel encore fonctionnel a poussé les lycées à reconsidérer l'alternative Linux, offrant un timing idéal à la démarche NIRD.
- **Un lycée du Nord-Pas-de-Calais livre des ordis en vélo électrique** : les élèves du lycée Carnot livrent des ordinateurs reconditionnés dans des écoles avec une remorque de 50 machines — même sous la pluie. Prix national en 2023.
- **La cyberattaque à l'origine de NIRD** : la distribution a été créée en urgence après une cyberattaque qui a déconnecté le lycée Carnot du réseau. Les enseignants avaient 3 jours pour remettre les ordinateurs en état de fonctionnement.
- **Debian vs Ubuntu : 20 secondes vs 1 min 40 s** au démarrage — Marius Monnier a déployé sa propre image Debian pour gagner en performance, au lieu de la solution régionale officielle Ubuntu.
- **Le terme "logiciel libre" est dans les référentiels NSI** : l'obligation d'utiliser un système d'exploitation libre est inscrite noir sur blanc dans le programme NSI. C'est cet argument qui a convaincu la région Auvergne-Rhône-Alpes de déployer des masters Linux.
- **Dizaines de demandes par jour** après une vidéo de présentation : le collectif NIRD croule sous les demandes de contribution depuis la mise en ligne d'une vidéo explicative, signe d'un intérêt massif mais d'une capacité d'accueil limitée.
- **Le fossé programme/réalité** : une maman en salle témoigne que sa fille en terminale n'a jamais eu de cours sur le logiciel libre, malgré les référentiels officiels — situation comparée à l'éducation à la sexualité, théoriquement au programme mais rarement appliquée.
- **Atos comme opérateur Linux régional** : le fait que le prestataire régional des lycées (Atos) soit désormais un acteur du déploiement Linux à grande échelle est un signal fort de la maturité de cet écosystème.

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Bertrand Chartier (Académie de Grenoble), Marius Monnier (Lycée Marie Curie, Échirolles)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
