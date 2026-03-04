# AlpOSS 2026 - PostgreSQL sur Kubernetes avec CloudNativePG - N'oubliez pas d'embarquer votre DBA PostgreSQL !

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Pierrick CHOVELON (Dalibo) |
| **Organisation** | Dalibo |
| **Durée** | 15:00 |
| **Présent** | ❌ Non |

## À propos de l'intervenant

Pierrick Chovelon est consultant DBA PostgreSQL chez Dalibo, société française de services spécialisée exclusivement dans PostgreSQL (support, audit, formation, conseil). Il a rejoint l'équipe DBA de Dalibo en 2023, après avoir utilisé PostgreSQL dans des environnements variés — systèmes, bases de données, cloud et Kubernetes. Il est l'auteur d'une série d'articles de référence sur le blog Dalibo intitulée "Plongez dans le monde de CloudNativePG", publiée depuis janvier 2025 et couvrant en profondeur le fonctionnement de l'opérateur. Il a également présenté ses travaux sur CloudNativePG lors des PostgreSQL Sessions (PGSession 18) et dans des conférences internationales, dont une à KubeCon avec Gabriele Bartolini (contributeur majeur de CloudNativePG).

## Résumé

Le titre de cette présentation — "N'oubliez pas d'embarquer votre DBA PostgreSQL !" — dit beaucoup de son propos : Kubernetes facilite le déploiement d'applications, mais la gestion d'une base de données relationnelle en production ne s'improvise pas, même derrière un opérateur.

Pierrick Chovelon présente CloudNativePG (CNPG), l'opérateur Kubernetes open source de référence pour PostgreSQL. Initialement créé par EnterpriseDB (EDB), CloudNativePG est aujourd'hui un projet porté par une communauté très active sous licence Apache 2.0. Il couvre l'intégralité du cycle de vie d'un cluster PostgreSQL dans Kubernetes : déploiement, réplication streaming, haute disponibilité, sauvegardes, mises à jour.

La présentation expose les capacités concrètes de l'opérateur : failover automatique intelligent avec promotion du réplica le plus à jour, switchover planifié, réplication synchrone configurable pour le zéro perte de données, sauvegardes continues sur object storage (S3, Azure Blob, GCS) avec archivage WAL et Point-In-Time Recovery (PITR). Ces mécanismes s'appuient directement sur les fonctionnalités natives de PostgreSQL, que Pierrick détaille à travers le prisme d'un DBA — et non d'un administrateur Kubernetes.

Le message central est pédagogique : adopter CloudNativePG ne dispense pas de comprendre PostgreSQL. L'opérateur automatise des tâches d'exploitation complexes, mais les décisions de configuration (réplication synchrone vs asynchrone, politique de rétention des WAL, stratégie de failover basée sur quorum) restent des choix qui requièrent une expertise DBA. La présentation fournit les clés pour comprendre ce que fait l'opérateur "sous le capot" et éviter les pièges classiques d'une adoption trop naïve.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **CloudNativePG (CNPG)** — Opérateur Kubernetes open source pour PostgreSQL (licence Apache 2.0) ; gestion complète du cycle de vie : déploiement, HA, réplication streaming, failover automatique, sauvegardes PITR ; référence de facto pour les équipes DevOps souhaitant opérer PostgreSQL en environnement cloud native
- **PostgreSQL** — SGBDR open source de référence (licence PostgreSQL, type BSD) ; le seul SGBD supporté par CloudNativePG ; sa réplication streaming native et ses capacités WAL sont les fondations sur lesquelles s'appuie l'opérateur
- **Kubernetes** — Plateforme d'orchestration de conteneurs standard de l'industrie ; CloudNativePG s'appuie sur ses primitives (Custom Resource Definitions, Operators Pattern) pour gérer les clusters PostgreSQL de manière déclarative
- **Object Storage (S3 / Azure Blob / GCS)** — Cibles de sauvegarde supportées par CloudNativePG pour les backups continus et l'archivage WAL ; pertinent pour les architectures cloud hybride souverain (ex : MinIO on-premise, OVH Object Storage)
- **WAL (Write-Ahead Log)** — Mécanisme interne de PostgreSQL pour la durabilité des transactions et la réplication ; l'archivage WAL est la clé du PITR (Point-In-Time Recovery) ; concept fondamental à maîtriser pour tout DBA opérant PostgreSQL sur Kubernetes
- **Dalibo** — Société française de services exclusivement dédiée à PostgreSQL ; formation, support, audit, conseil ; référence nationale pour les missions DBA PostgreSQL

## Points marquants

- CloudNativePG est le seul opérateur Kubernetes pour PostgreSQL à avoir atteint le statut de projet "graduated" au sein de la CNCF (Cloud Native Computing Foundation), ce qui témoigne de sa maturité et de l'adoption massive dans l'industrie
- Le titre de la présentation formule une critique implicite à l'adresse des équipes DevOps/SRE : automatiser PostgreSQL avec un opérateur ne supprime pas le besoin d'expertise DBA — une erreur fréquente qui génère des incidents graves en production
- Dalibo a publié depuis janvier 2025 une série de 10+ articles de fond sur CloudNativePG, faisant de Pierrick Chovelon l'une des voix françaises les plus documentées sur ce sujet
- Le failover basé sur quorum de CloudNativePG (passé stable en 2025) permet des décisions de promotion de réplica plus sûres dans les environnements multi-AZ — une évolution critique pour les déploiements à haute disponibilité
- PGSession 18, la conférence PostgreSQL annuelle organisée par Dalibo, s'est tenue fin février 2026 et a mis CloudNativePG au coeur de plusieurs sessions

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Pierrick CHOVELON (Dalibo)
- Page pretalx : [https://pretalx.com/alposs-2026/talk/BMQBBM/](https://pretalx.com/alposs-2026/talk/BMQBBM/)
