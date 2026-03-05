# PostgreSQL sur Kubernetes avec CloudNativePG - N'oubliez pas d'embarquer votre DBA PostgreSQL !

## Intervenant
Pierrick Chovelon · Dalibo

## Société
Dalibo est une société française de services exclusivement dédiée à PostgreSQL : support, audit, formation et conseil. Elle est la référence nationale pour les missions DBA PostgreSQL en environnements critiques. Dalibo organise chaque année les PGSessions, conférences techniques PostgreSQL, et maintient un blog de référence sur l'écosystème PostgreSQL en français. Ses consultants contribuent activement aux projets communautaires autour de PostgreSQL et CloudNativePG.

## Résumé
CloudNativePG automatise déploiement, HA, failover et PITR pour PostgreSQL sur Kubernetes, mais ne remplace pas l'expertise DBA. Les choix de configuration WAL, réplication et failover restent critiques et nécessitent de comprendre ce que l'opérateur fait sous le capot.

## Points marquants
- CloudNativePG est le seul opérateur PostgreSQL certifié "graduated" à la CNCF.
  Ce statut, atteint en 2025, atteste d'une maturité industrielle reconnue par la communauté cloud-native mondiale et distingue CNPG de tous les autres opérateurs PostgreSQL pour Kubernetes.
- Un opérateur automatise l'exploitation PostgreSQL, mais pas les décisions DBA.
  Les choix de configuration — réplication synchrone ou asynchrone, politique de rétention des WAL, stratégie de failover — requièrent une expertise PostgreSQL que l'opérateur ne peut pas remplacer. Une adoption naïve génère des incidents graves en production.
- Le failover basé sur quorum, passé stable en 2025, réduit les risques de split-brain.
  Ce mécanisme permet de promouvoir le réplica le plus à jour dans les environnements multi-AZ, en évitant les promotions incorrectes qui causent des pertes de données.
- CNPG intègre nativement le PITR via archivage continu des WAL sur object storage.
  Les sauvegardes sont envoyées en continu sur S3, Azure Blob ou GCS (compatible MinIO on-premise), permettant une restauration à n'importe quel point dans le temps sans outil tiers.
- Dalibo publie depuis janvier 2025 une série d'articles de référence sur CloudNativePG.
  Cette documentation technique en français, rédigée par Pierrick Chovelon, est l'une des sources les plus complètes disponibles sur le fonctionnement interne de l'opérateur.

## Technologies
- **CloudNativePG (CNPG)** — Opérateur Kubernetes open source pour PostgreSQL (Apache 2.0), projet "graduated" à la CNCF. Gère l'intégralité du cycle de vie d'un cluster PostgreSQL : déploiement, réplication streaming, HA, failover automatique basé sur quorum, sauvegardes continues et PITR. Référence de facto pour opérer PostgreSQL en environnement cloud native.
- **PostgreSQL** — SGBDR open source (licence BSD) sur lequel repose entièrement CloudNativePG. Sa réplication streaming native et ses mécanismes WAL sont les fondations techniques de l'opérateur. Maîtriser PostgreSQL reste indispensable même avec un opérateur.
- **Kubernetes** — Plateforme d'orchestration de conteneurs standard. CloudNativePG exploite les Custom Resource Definitions (CRD) et l'Operator Pattern pour gérer les clusters PostgreSQL de façon déclarative. Connaître les primitives Kubernetes aide à comprendre le comportement de l'opérateur.
- **WAL (Write-Ahead Log)** — Mécanisme interne de PostgreSQL pour la durabilité des transactions et la réplication. L'archivage continu des WAL est la clé du Point-In-Time Recovery (PITR). Concept fondamental à maîtriser pour tout DBA opérant PostgreSQL sur Kubernetes.
- **Object Storage (S3 / Azure Blob / GCS)** — Cibles de sauvegarde supportées nativement par CloudNativePG pour les backups continus et l'archivage WAL. Compatible avec des solutions on-premise souveraines comme MinIO ou OVH Object Storage.
