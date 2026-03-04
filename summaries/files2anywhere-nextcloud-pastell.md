# AlpOSS 2026 - Files2Anywhere : la brique qui connecte Nextcloud et Pastell pour vos processus métiers

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Philippe SCOFFONI (Opendsi) |
| **Organisation** | Opendsi (devenu Easya Solutions) |
| **Durée** | 15 min (11:55–12:10) |
| **Présent** | ❌ Non |

## À propos de l'intervenant

Philippe Scoffoni est fondateur et dirigeant d'**Opendsi** (rebaptisé Easya Solutions), une société spécialisée dans l'intégration de solutions libres et souveraines pour les organisations publiques et privées. Il est expert reconnu dans l'écosystème open source français, notamment sur les briques **Nextcloud**, **Dolibarr ERP/CRM** et **Metabase**.

Il tient également un blog personnel de référence sur le logiciel libre et le numérique ([philippe.scoffoni.net](https://philippe.scoffoni.net/)) et est actif sur les réseaux sociaux professionnels sur ces sujets.

Il préside **PlossRA** (Professionnels du Logiciel Libre en Auvergne-Rhône-Alpes), l'association régionale des entreprises du numérique libre, ce qui l'ancre fortement dans l'écosystème grenoblois et rhônalpin — contexte naturel d'AlpOSS.

## Résumé

Ce talk présente **Files2Anywhere**, un connecteur open source développé par Opendsi pour relier **Nextcloud** (stockage et partage de fichiers) et **Pastell** (orchestrateur de dématérialisation des collectivités territoriales), dans le but d'automatiser et fluidifier les processus métiers documentaires des administrations locales.

**Contexte du besoin :**
Les collectivités territoriales utilisent fréquemment Pastell (édité par Libriciel SCOP) pour orchestrer leurs flux dématérialisés : signature électronique, télétransmission au contrôle de légalité (préfecture), archivage. De leur côté, beaucoup ont déployé Nextcloud comme espace de stockage collaboratif. Files2Anywhere est la brique d'interopérabilité qui fait le lien entre ces deux mondes.

**Ce que permet Files2Anywhere :**
- Connecter Nextcloud à Pastell pour déclencher automatiquement des workflows de dématérialisation depuis des fichiers stockés dans Nextcloud
- Simplifier le partage de documents entre agents, services et partenaires externes
- Automatiser des processus métiers (validation, signature, télétransmission) sans ressaisie ni transfert manuel
- Garantir la sécurité et la conformité des échanges (données publiques, données personnelles)
- Renforcer la souveraineté sur les données : tout le stack est open source et peut être hébergé en interne ou chez un hébergeur souverain

**Portée :** Ce type de connecteur s'adresse prioritairement aux collectivités (communes, intercommunalités, départements) mais la logique de connecteur Nextcloud-workflow est transposable dans d'autres contextes (ESN, administrations d'État).

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Files2Anywhere** — connecteur open source développé par Opendsi, reliant Nextcloud et Pastell pour l'automatisation des processus documentaires
- **Nextcloud** — plateforme open source de stockage, partage et collaboration documentaire (alternative souveraine à SharePoint/Google Drive)
- **Pastell** — orchestrateur open source de processus dématérialisés pour les administrations (édité par Libriciel SCOP), gérant la signature électronique, la télétransmission et l'archivage
- **iParapheur** — parapheur électronique open source de Libriciel, souvent couplé à Pastell pour la signature dans les collectivités
- **Dolibarr ERP/CRM** — ERP open source également intégré par Opendsi/Easya Solutions

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- Files2Anywhere illustre une tendance de fond : la constitution d'un **stack souverain complet** pour les collectivités, en assemblant des briques open source éprouvées plutôt qu'en déployant des solutions monolithiques propriétaires
- Pastell (Libriciel) est un acteur méconnu hors secteur public mais très largement déployé dans les collectivités françaises pour la dématérialisation réglementaire — un marché de niche mais stratégique
- L'approche "connecteur" (vs intégration native) est un modèle architectural pragmatique : elle permet de faire coexister des outils déjà déployés sans les remplacer
- Philippe Scoffoni préside PlossRA, ce qui positionne ce talk aussi comme un témoignage de l'écosystème local des prestataires open source en Auvergne-Rhône-Alpes
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Philippe SCOFFONI (Opendsi)
- Page pretalx : https://pretalx.com/alposs-2026/talk/9Q3N89/
