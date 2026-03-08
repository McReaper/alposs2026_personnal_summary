# Choisir un logiciel libre au-delà de la licence

## Intervenant
Michaël Scherer · Red Hat

## Société
Red Hat est l'un des principaux éditeurs mondiaux de logiciels open source, éditeur de RHEL, Fedora, CentOS Stream et OpenShift. Filiale d'IBM depuis 2019, Red Hat dispose d'un Open Source Program Office (OSPO) dédié à la gestion des relations avec les communautés open source, les fondations et les événements. La société fixe les standards de packaging RPM et de support long terme pour les distributions Linux d'entreprise, et contribue massivement à des projets comme le noyau Linux, Kubernetes et Ansible. C'est un acteur incontournable pour Kaizen, intervenant sur des environnements d'infrastructure Linux ou cloud-native.

## Résumé
La licence ne suffit pas : il faut évaluer le modèle de gouvernance, le financement et les CLA avant d'intégrer un composant open source. Minio a archivé sa version libre la semaine précédant la conférence — cas d'école du risque de bascule propriétaire à anticiper en architecture.

## Points marquants
- Minio, stockage objet compatible S3, a archivé sa version libre.
  L'archivage est survenu la semaine précédant la conférence. Minio avait d'abord laissé la version libre "vivoter" tout en développant une version propriétaire ; le fork devient désormais la seule issue pour les équipes qui l'utilisent sans plan de contingence.
- Un développeur parti chez Apple ne pouvait plus contribuer à son propre projet.
  Cas documenté avec Abbey World : en signant chez Apple, le développeur principal n'avait plus le droit de contribuer au logiciel qu'il avait créé. Les clauses de non-concurrence d'Apple sont particulièrement restrictives vis-à-vis de l'open source.
- Un mauvais CLA capture tous vos droits sans aucune contrepartie.
  Le Contributor License Agreement de la FSF redistribue les droits aux contributeurs ; celui pratiqué par certains éditeurs commerciaux les capte sans retour. La distinction est critique avant toute contribution à un projet porté par une entreprise.
- BookWire est perçu comme un logiciel libre, mais ne l'est pas juridiquement.
  Ce cas illustre le risque de se fier à la réputation communautaire sans vérification de la licence. Une structure qui déploie BookWire en croyant respecter une obligation de recours au libre s'expose à un risque juridique réel.

## Technologies
- **OpenShift** — Distribution Kubernetes entreprise de Red Hat. Solution d'industrialisation des déploiements conteneurisés, avec support long terme et outillage DevOps intégré. Forte demande en intégration et Platform Engineering.
- **PostgreSQL** — SGBD relationnel open source de référence. Cité pour son excellent cycle de support long terme (5 ans par version majeure) mais ses migrations de version complexes. À privilégier pour les projets nécessitant une durée de vie étendue.
- **Elasticsearch / OpenSearch** — Moteur de recherche et d'indexation. Elasticsearch a changé de licence (libre vers propriétaire), provoquant le fork OpenSearch par AWS. Cas d'école du risque de bascule propriétaire à anticiper dans les choix d'architecture.
- **Matrix / Conduit / Conduwuit** — Protocole de messagerie fédérée et ses implémentations serveur. Exemple de fragmentation communautaire par forks successifs suite à des disputes entre contributeurs. Pertinent pour Kaizen proposant des solutions de messagerie souveraine.
- **Minio** — Stockage objet compatible S3, open source. A archivé sa version libre la semaine précédant la conférence — signal d'alarme pour les déploiements sans plan de contingence.
- **Rust** — Langage de programmation système cité pour sa sécurité mémoire intrinsèque. Pertinent pour les missions SSI et le développement sécurisé à faible surface d'attaque.
