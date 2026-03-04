# PostgreSQL sur Kubernetes avec CloudNativePG - N'oubliez pas d'embarquer votre DBA PostgreSQL !

## Intervenant
Pierrick Chovelon · Dalibo

## Société
Dalibo est une société française de services exclusivement dédiée à PostgreSQL : support, audit, formation et conseil. Elle est la référence nationale pour les missions DBA PostgreSQL en environnements critiques. Dalibo organise chaque année les PGSessions, conférences techniques PostgreSQL, et maintient un blog de référence sur l'écosystème PostgreSQL en français. Ses consultants contribuent activement aux projets communautaires autour de PostgreSQL et CloudNativePG.

## Résumé
CloudNativePG (CNPG) est l'opérateur Kubernetes de référence pour PostgreSQL : il couvre déploiement, réplication streaming, haute disponibilité, failover automatique et sauvegardes PITR sur object storage. Le message central du talk est que l'opérateur automatise des tâches complexes mais ne remplace pas l'expertise DBA — les choix de configuration (synchrone vs asynchrone, politique WAL, stratégie de failover) restent critiques. Comprendre ce que fait CNPG "sous le capot" est indispensable pour éviter les incidents en production.

## Points marquants
- CNPG : seul opérateur PostgreSQL "graduated" à la CNCF
- Failover basé sur quorum, stable depuis 2025
- L'opérateur automatise, mais ne remplace pas le DBA
- PITR natif via archivage WAL sur S3/Azure Blob/GCS

## Technologies
- **CloudNativePG (CNPG)** — Opérateur Kubernetes open source pour PostgreSQL (Apache 2.0), projet "graduated" à la CNCF. Gère l'intégralité du cycle de vie d'un cluster PostgreSQL : déploiement, réplication streaming, HA, failover automatique basé sur quorum, sauvegardes continues et PITR. Référence de facto pour opérer PostgreSQL en environnement cloud native.
- **PostgreSQL** — SGBDR open source (licence BSD) sur lequel repose entièrement CloudNativePG. Sa réplication streaming native et ses mécanismes WAL sont les fondations techniques de l'opérateur. Maîtriser PostgreSQL reste indispensable même avec un opérateur.
- **Kubernetes** — Plateforme d'orchestration de conteneurs standard. CloudNativePG exploite les Custom Resource Definitions (CRD) et l'Operator Pattern pour gérer les clusters PostgreSQL de façon déclarative. Connaître les primitives Kubernetes aide à comprendre le comportement de l'opérateur.
- **WAL (Write-Ahead Log)** — Mécanisme interne de PostgreSQL pour la durabilité des transactions et la réplication. L'archivage continu des WAL est la clé du Point-In-Time Recovery (PITR). Concept fondamental à maîtriser pour tout DBA opérant PostgreSQL sur Kubernetes.
- **Object Storage (S3 / Azure Blob / GCS)** — Cibles de sauvegarde supportées nativement par CloudNativePG pour les backups continus et l'archivage WAL. Compatible avec des solutions on-premise souveraines comme MinIO ou OVH Object Storage.
