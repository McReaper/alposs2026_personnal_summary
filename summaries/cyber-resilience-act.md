# AlpOSS 2026 - Cyber Resilience Act et open source

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Marta Rybczynska |
| **Organisation** | Ygreky |
| **Durée** | 19:45 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Marta Rybczynska est spécialiste en cybersécurité embarquée. Elle contribue activement au noyau Linux et au projet Yocto, et s'implique fortement dans les processus de sécurité. Ces trois dernières années, elle s'est concentrée sur la standardisation autour du Cyber Resilience Act. Elle est également active dans les organismes de normalisation européens (ETSI, CEN/CENELEC) et communique régulièrement sur les enjeux réglementaires liés à l'open source et à la sécurité des produits connectés.

## Résumé

Le Cyber Resilience Act (CRA) est une réglementation européenne désormais publiée au Journal officiel de l'UE, avec une entrée en vigueur complète prévue pour décembre 2027. Une première échéance importante arrive dès septembre 2026 : la notification obligatoire des vulnérabilités activement exploitées dans tous les produits concernés.

Le CRA cible tous les **produits comportant des éléments numériques** — logiciels et matériels connectés ou connectables — distribués ou vendus dans l'Union Européenne, quelle que soit l'origine du fabricant. Sont inclus : logiciels installés sur postes utilisateurs, objets domotiques, applications dont les traitements se font sur serveur distant. Sont exclus : sites web, secteur automobile (couvert par une autre réglementation), et projets de loisir non commerciaux.

Les produits sont classés en plusieurs catégories. Pour 90 % d'entre eux, une auto-évaluation suffit. Les produits "importants" (classe 1 et 2) incluent navigateurs web, boot managers, interfaces réseau, distributions Linux, routeurs, objets connectés. Les produits "critiques" couvrent notamment les cartes à puce et équipements de sécurité matérielle.

Concernant l'open source, la bonne nouvelle est claire : les **simples contributeurs** à des projets open source n'ont aucune obligation. Les obligations incombent aux **fabricants** (ceux qui monétisent) et, dans une moindre mesure, aux **intendants de logiciels ouverts** (personnes morales supportant un projet sans le monétiser). Les fabricants doivent notamment : effectuer l'analyse des risques de leurs produits en incluant toutes leurs dépendances open source, fournir des mises à jour de sécurité gratuites pendant une période d'assistance par défaut de 5 ans, notifier les projets upstream en cas de découverte de faille, et communiquer sur les correctifs publiés.

L'analyse des risques est au cœur du dispositif : c'est elle — et elle seule — qui détermine les mesures de sécurité à mettre en place. Entre 70 et 90 % des composants utilisés dans les produits étant open source, la production d'un inventaire exhaustif (S-BOM) devient incontournable. La rétroactivité est limitée : les exigences de sécurité ne s'appliquent pas aux produits déjà en marché, sauf en cas de mise à jour fonctionnelle majeure. En revanche, la notification des vulnérabilités exploitées s'applique à tous les produits dès septembre 2026.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **S-BOM (Software Bill of Materials)** — Inventaire exhaustif des composants logiciels d'un produit. Rendu indispensable par le CRA : les fabricants doivent documenter toutes leurs dépendances, y compris open source. La génération de S-BOM est particulièrement complexe dans les environnements conteneurisés (multiplication des composants, difficulté de combiner plusieurs S-BOM).
- **Projet Yocto** — Framework de construction de distributions Linux embarquées. Directement concerné par le CRA car utilisé dans de nombreux produits embarqués. L'intervenante y contribue activement.
- **Noyau Linux** — Composant open source central dans les systèmes embarqués et distributions. Les fabricants qui l'intègrent ont l'obligation d'analyser ses risques et de notifier les failles découvertes au projet upstream.
- **OpenSSF (Open Source Security Foundation)** — Groupe de travail produisant des guides et ressources pour aider les projets open source à répondre aux exigences de sécurité du CRA. Ressource de référence pour les équipes DevSecOps.
- **Open Regulatory Compliance (groupe Linux Foundation)** — Groupe de travail dédié à la conformité réglementaire dans l'écosystème open source, notamment face au CRA. Propose des conseils sur la gestion des cas concrets.
- **ETSI (European Telecommunications Standards Institute)** — Organisme de normalisation européen produisant les standards techniques liés au CRA. Les entreprises souhaitant influencer ces standards peuvent y participer.
- **CEN/CENELEC** — Organismes de normalisation européens également impliqués dans la rédaction des normes techniques associées au CRA (mentionnés sous l'abréviation "Sincénec" dans la transcription).
- **Conteneurisation (Docker/OCI)** — Facilite la génération de S-BOM par analyse des images livrées, mais complexifie leur gestion (explosion du nombre de composants, difficultés de combiner plusieurs S-BOM issus de microservices distincts).

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- Le CRA est déjà publié au Journal officiel de l'UE — il ne s'agit plus d'un projet de loi mais d'une réglementation en vigueur, avec une première échéance dès **septembre 2026** pour la notification obligatoire des vulnérabilités activement exploitées.
- Les **simples contributeurs open source** sont explicitement exemptés de toute obligation — une protection qui n'était pas acquise lors des premières versions du texte, selon l'intervenante.
- Les fabricants ont l'obligation légale de **notifier les projets open source upstream** lorsqu'ils découvrent une faille dans une dépendance — les projets vont donc recevoir des rapports (et des patches) de la part d'acteurs commerciaux, sans être contraints d'agir pour autant.
- La **période d'assistance par défaut est de 5 ans** avec mises à jour de sécurité gratuites obligatoires — les fabricants **n'ont pas le droit de vendre un produit après la fin de cette période** sans justification.
- Le CRA s'applique à **toute entreprise vendant à un client européen**, y compris une entreprise américaine vendant directement à une société française — le critère est le destinataire, pas l'origine du fabricant.
- Entre **70 et 90 % des composants** d'un produit commercial typique sont open source — ce qui rend l'analyse des dépendances et la production de S-BOM particulièrement lourde pour les fabricants.
- La loi inclut une **définition officielle de "système d'exploitation"** dans son règlement d'exécution — pour ceux qui se poseraient la question, la réponse est désormais dans un texte juridique européen.
- Les **mises à jour automatiques** doivent être présentes dans les produits concernés, mais avec une **option de désactivation obligatoire** laissée à l'utilisateur.
- L'**analyse des risques est l'unique fondement juridique des mesures de sécurité** — et la seule défense des fabricants en cas de litige : certains fournisseurs prétendent à tort qu'une fonctionnalité X est obligatoire, alors que seule l'analyse des risques propre au produit le détermine.
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Marta Rybczynska (Ygreky)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
