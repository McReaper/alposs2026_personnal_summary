# AlpOSS 2026 - Choisir un logiciel libre au-delà de la licence

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Michaël Scherer |
| **Organisation** | Red Hat |
| **Durée** | 19:33 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Michaël Scherer est administrateur système au sein de l'**Open Source Program Office (OSPO)** de **Red Hat**, l'un des principaux éditeurs de logiciels open source au monde (RHEL, Fedora, CentOS Stream, OpenShift). Son rôle couvre la gestion de communautés, l'organisation d'événements, les relations avec les fondations open source, et la fourniture d'infrastructures pour les projets (notamment des instances Pretalx pour la gestion de CFP). Contributeur de longue date à l'écosystème libre (ex-packager pour Mandriva), il intervient régulièrement dans des conférences francophones et européennes sur des sujets liés à l'administration système et à la gouvernance open source.

## Résumé

Michaël Scherer aborde un sujet qu'il juge insuffisamment traité dans les événements open source : comment choisir un logiciel libre en allant au-delà du simple critère de la licence ? La présentation est volontairement centrée sur le contexte serveur (son domaine d'expertise en tant qu'adminsys) et sur la question de la maintenance à long terme.

**Qui développe le logiciel ?**
Premier axe : analyser la structure de développement. Il distingue quatre cas :
- *Une seule grande entreprise* : risque de changement de licence vers le propriétaire pour monétiser (exemple : Elasticsearch, devenu non-libre) ou de contribution désintéressée (exemple : OVH sur OpenStack).
- *Plusieurs grandes entreprises* : modèle plus équilibré, type CNCF/Kubernetes, mais bureaucratique.
- *Un petit groupe* : risque de disputes et de forks (exemple : les multiples forks de Conduit, serveur Matrix, issus de disputes entre contributeurs issus de la culture IRC).
- *Une seule personne* : risque de burn-out, d'un enfant, ou de partir chez Apple et de perdre le droit de contribuer à son propre projet (cas réel avec Abbey World).

Il insiste sur l'importance d'éviter les projets portés par des personnes ou groupes conflictuels (risque de « australisation »), et recommande d'attendre la stabilisation lors d'un fork avant de choisir son camp.

**Comment est-il financé ?**
Deuxième axe : la pérennité financière. Il passe en revue : startup avec du cash (fragile), subventions NLnet/NGI (soumises au calendrier), vendeurs de logiciels (risque de bascule propriétaire, exemple : Minio archivé la semaine précédente), vendeurs d'hébergement (exemple vertueux : OVH qui finance des développeurs OpenStack), et logiciels académiques ou d'État (moins courants aujourd'hui).

**Autres critères techniques**
Il aborde ensuite : le cycle de release et la durée de support des versions (PostgreSQL vs projets à release bi-hebdomadaire), la facilité de mise à jour (regrets sur les migrations PostgreSQL vs MySQL), l'industrialisation de l'installation (Matomo, dont le wizard PHP rend l'automatisation difficile avec Kubernetes/OpenShift), la gestion des dépendances (exemple complexe d'un logiciel de bibliothèque en Perl avec Elasticsearch, Z39.50 et MySQL), le packaging (RPM, Debian, qualité des images Docker/OCI), le langage de programmation (impact sur le debugging, la sécurité — il cite Rust), et la licence elle-même (exemple : BookWire, perçu comme libre mais ne l'étant pas).

Il termine sur les CLA (Contributor License Agreements) : distinction entre le bon CLA (FSF, qui redistribue les droits aux contributeurs) et le mauvais CLA (certains acteurs qui captent les droits sans contrepartie).

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Red Hat Enterprise Linux (RHEL) / Fedora / CentOS Stream** — Distributions Linux de référence en entreprise. Red Hat fixe les standards de packaging RPM et de support à long terme. Incontournable pour les missions d'infrastructure.
- **OpenShift** — Distribution Kubernetes entreprise de Red Hat. Mentionné comme solution d'industrialisation. Forte demande en intégration et déploiement (DevOps, Platform Engineering).
- **Kubernetes / CNCF** — Standard de l'orchestration de conteneurs. Exemple de gouvernance multi-acteurs, pertinent pour évaluer la pérennité des projets cloud-native.
- **Elasticsearch / OpenSearch** — Moteur de recherche et d'indexation. Mentionné pour son changement de licence (de libre à propriétaire), suivi d'un fork (OpenSearch par AWS). Cas d'école du risque de bascule propriétaire.
- **PostgreSQL** — SGBD relationnel open source de référence. Cité pour son excellent cycle de support long terme mais ses migrations de version complexes.
- **MySQL / MariaDB** — SGBD alternatif, cité pour ses mises à jour plus simples. Comparaison directe avec PostgreSQL sur la praticité des migrations.
- **Matrix / Synapse / Conduit / Conduwuit** — Protocole de messagerie fédérée et ses implémentations serveur. Exemple de fragmentation communautaire par forks successifs. Pertinent pour les ESN proposant des solutions de messagerie souveraine.
- **Minio** — Stockage objet compatible S3, open source. Alerte : vient d'archiver sa version libre (semaine de la conférence). Les forks deviennent nécessaires.
- **Docker / conteneurs OCI** — Technologie de conteneurisation. Scherer soulève les questions de qualité et de maintenance des images (qui les maintient ? sur quelle base ?).
- **Rust** — Langage de programmation système, cité pour sa sécurité mémoire intrinsèque. Pertinent pour les missions SSI (développement sécurisé, réduction de la surface d'attaque).
- **Matomo** — Outil d'analyse web open source (alternative à Google Analytics). Cité comme exemple de logiciel difficile à industrialiser/automatiser (wizard PHP incompatible avec Kubernetes).
- **CLA (Contributor License Agreement)** — Mécanisme juridique de gestion des droits de contribution. Distinction critique entre CLA FSF (équitable) et CLA « aspirateur de droits » pratiqué par certains acteurs commerciaux.
- **Pretalx** — Outil de gestion de CFP (Call For Papers) pour conférences. Mentionné comme infrastructure gérée par l'OSPO de Red Hat.

## Points marquants

- Un développeur principal d'Abbey World, parti travailler chez Apple, n'avait plus le droit de contribuer à son propre projet open source — les clauses de non-concurrence d'Apple sont particulièrement restrictives sur l'open source.
- Minio, outil de stockage objet très populaire (compatible S3), a archivé sa version libre la semaine précédant la conférence : un signal d'alarme pour tous ceux qui l'utilisent sans plan de contingence.
- La Mandriva Mandrake 7 qui effaçait les disques durs : une cicatrice collective de la communauté Linux encore évoquée 20 ans après, preuve de la longue mémoire de l'écosystème.
- En 2026, la question de savoir si une pull request a été rédigée par un humain ou générée par IA est déjà posée dans le monde de l'open source — avec des impacts réels sur la charge de review des mainteneurs.
- BookWire est mentionné comme un logiciel perçu comme libre par la communauté mais qui ne l'est en réalité pas — un piège fréquent pour les structures qui s'y fient sans vérification juridique.
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Michaël Scherer (Red Hat)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
