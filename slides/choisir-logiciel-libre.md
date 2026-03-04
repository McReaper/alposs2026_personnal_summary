# Choisir un logiciel libre au-delà de la licence

## Intervenant
Michaël Scherer · Red Hat

## Société
Red Hat est l'un des principaux éditeurs mondiaux de logiciels open source, éditeur de RHEL, Fedora, CentOS Stream et OpenShift. Filiale d'IBM depuis 2019, Red Hat dispose d'un Open Source Program Office (OSPO) dédié à la gestion des relations avec les communautés open source, les fondations et les événements. La société fixe les standards de packaging RPM et de support long terme pour les distributions Linux d'entreprise, et contribue massivement à des projets comme le noyau Linux, Kubernetes et Ansible. C'est un acteur incontournable pour toute ESN intervenant sur des environnements d'infrastructure Linux ou cloud-native.

## Résumé
Choisir un logiciel libre ne se limite pas à vérifier sa licence : il faut analyser qui le développe (une seule entreprise, un consortium, un individu), comment il est financé, et sa robustesse opérationnelle à long terme. Minio, très populaire comme stockage objet compatible S3, a archivé sa version libre la semaine même de la conférence — illustration directe du risque de bascule propriétaire. Les CLA méritent une attention particulière : certains captent les droits des contributeurs sans contrepartie, d'autres (FSF) les redistribuent équitablement. En 2026, la question de savoir si une pull request est générée par IA pèse déjà sur la charge de review des mainteneurs.

## Points marquants
- Minio a archivé sa version libre la semaine de la conférence.
- Un CLA peut capter vos droits sans aucune contrepartie.
- Les PRs générées par IA déplacent le bottleneck vers la review humaine.
- BookWire perçu comme libre ne l'est en réalité pas.

## Technologies
- **OpenShift** — Distribution Kubernetes entreprise de Red Hat. Solution d'industrialisation des déploiements conteneurisés, avec support long terme et outillage DevOps intégré. Forte demande en intégration et Platform Engineering.
- **PostgreSQL** — SGBD relationnel open source de référence. Cité pour son excellent cycle de support long terme (5 ans par version majeure) mais ses migrations de version complexes. À privilégier pour les projets nécessitant une durée de vie étendue.
- **Elasticsearch / OpenSearch** — Moteur de recherche et d'indexation. Elasticsearch a changé de licence (libre vers propriétaire), provoquant le fork OpenSearch par AWS. Cas d'école du risque de bascule propriétaire à anticiper dans les choix d'architecture.
- **Matrix / Conduit / Conduwuit** — Protocole de messagerie fédérée et ses implémentations serveur. Exemple de fragmentation communautaire par forks successifs suite à des disputes entre contributeurs. Pertinent pour les ESN proposant des solutions de messagerie souveraine.
- **Minio** — Stockage objet compatible S3, open source. A archivé sa version libre lors de la semaine de la conférence — signal d'alarme pour les déploiements sans plan de contingence.
- **Rust** — Langage de programmation système cité pour sa sécurité mémoire intrinsèque. Pertinent pour les missions SSI et le développement sécurisé à faible surface d'attaque.
