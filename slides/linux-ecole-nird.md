# Linux à l'école ? Enfin un espoir avec la démarche NIRD !

## Intervenant
Bertrand Chartier et Marius Monnier · Académie de Grenoble / Lycée Marie Curie (Échirolles)

## Société
Bertrand Chartier est chargé de mission à la délégation académique au numérique (DAN) de l'académie de Grenoble, promoteur de la démarche NIRD au niveau académique. Marius Monnier est enseignant NSI (Numérique et Sciences Informatiques) au lycée Marie Curie d'Échirolles, où il a déployé une salle Linux Debian intégrée au réseau du lycée via SSO LDAP. Tous deux contribuent bénévolement à la distribution NIRD, hébergée sur la Forge des communs numériques éducatifs (forge.apps.education.fr).

## Résumé
NIRD déploie Linux dans les lycées sur matériel reconditionné redistribué aux familles, avec authentification centralisée intégrée au réseau pédagogique existant. La distribution est en bêta et cherche des contributeurs extérieurs à l'Éducation nationale.

## Points marquants
- Windows 11 a poussé les lycées vers Linux, timing idéal.
- Debian démarre en 20 s vs 1 min 40 s pour Ubuntu (Atos).
- "Logiciel libre" est inscrit noir sur blanc dans les référentiels NSI.
- La cyberattaque au lycée Carnot a déclenché la création de NIRD.

## Technologies
- **Distribution NIRD** — Surcouche Linux Mint/Debian en cours de développement (v0.1-0.2, bêta), conçue pour le déploiement live offline en environnement éducatif ; hébergée sur la Forge des communs numériques éducatifs ; à surveiller pour les ESN intéressées par les communs numériques et les marchés Éducation.
- **FOG Project** — Logiciel open source de déploiement d'images disque par le réseau (clone réseau) ; utilisé par Atos pour déployer les images Linux dans les lycées régionaux ; outil de référence pour les ESN en charge de déploiements massifs de postes de travail.
- **Primetux** — Distribution Linux légère conçue pour les écoles primaires, fonctionnant offline avec des logiciels pédagogiques préinstallés ; pertinente pour les missions d'équipement de collectivités ou d'associations en matériel reconditionné.
- **Debian / Ubuntu** — Distributions Linux déployées en environnement scolaire ; retour d'expérience direct sur la gestion de parcs Linux en établissements publics ; Debian privilégiée ici pour ses performances au démarrage.
- **LDAP / SSO** — Intégration annuaire et authentification unique pour les stations Linux, compatibles avec l'infrastructure existante du lycée ; compétence clé pour les ESN intégrant des postes Linux dans des parcs mixtes.
- **Forge des communs numériques éducatifs** — Instance GitLab hébergée par l'État (forge.apps.education.fr) pour les projets numériques éducatifs ; exemple d'infrastructure souveraine d'hébergement de code public.
