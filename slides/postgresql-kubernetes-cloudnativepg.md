# PostgreSQL sur Kubernetes avec CloudNativePG - N'oubliez pas d'embarquer votre DBA PostgreSQL !

## Intervenant
Pierrick Chovelon · Dalibo

## Société
Dalibo est une société française de services exclusivement dédiée à PostgreSQL : support, audit, formation et conseil. Elle est la référence nationale pour les missions DBA PostgreSQL en environnements critiques. Dalibo organise chaque année les PGSessions, conférences techniques PostgreSQL, et maintient un blog de référence sur l'écosystème PostgreSQL en français. Ses consultants contribuent activement aux projets communautaires autour de PostgreSQL et CloudNativePG.

## Résumé
CloudNativePG est un outil open source qui pilote automatiquement PostgreSQL dans Kubernetes : démarrage, copies de secours, bascule en cas de panne, sauvegardes. Mais il ne remplace pas un expert base de données — les mauvais réglages restent dangereux, même avec l'automatisation.

## Points marquants
- CloudNativePG est l'outil de référence pour faire tourner PostgreSQL dans Kubernetes.
  C'est le seul dans sa catégorie à avoir obtenu le label "graduated" de la CNCF — l'organisme qui certifie la maturité des projets cloud-native (Kubernetes, Prometheus…). Concrètement : il est assez stable pour la production.
- Automatiser PostgreSQL ne dispense pas de le comprendre.
  L'outil gère tout seul des tâches complexes, mais les décisions de configuration restent humaines : est-ce qu'on accepte de perdre quelques secondes de données en cas de panne, ou on veut zéro perte ? Quelle durée de sauvegarde on conserve ? Mal configuré, l'outil peut silencieusement perdre des données.
- En cas de panne du serveur principal, la bascule vers un serveur de secours est automatique.
  CloudNativePG choisit le serveur de secours le plus à jour et le promeut. Depuis 2025, ce choix repose sur un système de vote entre serveurs pour éviter qu'ils se contredisent — un problème classique dans les bases distribuées.
- On peut restaurer la base à n'importe quel instant dans le passé.
  CloudNativePG envoie en continu le journal des transactions (le WAL) vers un stockage cloud (S3, MinIO…). En cas de catastrophe, on peut rejouer ce journal jusqu'à la seconde exacte avant l'incident — sans outil supplémentaire.
- Dalibo publie depuis janvier 2025 une série d'articles de référence sur CloudNativePG.
  Cette documentation technique en français, rédigée par Pierrick Chovelon, est l'une des sources les plus complètes disponibles sur le fonctionnement interne de l'outil.

## Technologies
- **CloudNativePG (CNPG)** — Outil open source (Apache 2.0) qui pilote PostgreSQL dans Kubernetes : démarrage, réplication, bascule automatique en cas de panne, sauvegardes et restauration à un instant précis. Label "graduated" de la CNCF, signe de maturité industrielle. Référence pour opérer PostgreSQL en environnement cloud.
- **PostgreSQL** — Base de données relationnelle open source (licence BSD), la plus utilisée dans le monde open source. CloudNativePG ne fonctionne qu'avec PostgreSQL — et en exploite les mécanismes internes. Le maîtriser reste indispensable même avec l'outil.
- **Kubernetes** — Plateforme standard pour orchestrer des conteneurs. CloudNativePG s'y intègre nativement et se configure comme n'importe quelle autre ressource Kubernetes, en YAML déclaratif.
- **WAL (journal des transactions)** — PostgreSQL écrit chaque modification dans un journal avant de la valider. Ce journal sert à la réplication vers les serveurs de secours et aux sauvegardes continues. C'est lui qui permet de "rembobiner" la base jusqu'à un instant précis.
- **Object Storage (S3 / MinIO / OVH…)** — Stockage de fichiers en cloud, utilisé par CloudNativePG pour archiver les sauvegardes en continu. Compatible avec des solutions souveraines hébergées en France.
