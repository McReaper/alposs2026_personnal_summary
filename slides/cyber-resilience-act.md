# Cyber Resilience Act et open source

## Intervenant
Marta Rybczynska · Ygreky

## Société
Ygreky est une structure spécialisée en cybersécurité des systèmes embarqués et en conformité réglementaire européenne. Marta Rybczynska y mène des travaux de standardisation liés au Cyber Resilience Act, en participant activement aux travaux des organismes de normalisation ETSI et CEN/CENELEC. Elle contribue par ailleurs au noyau Linux et au projet Yocto, ce qui lui confère une double expertise technique et réglementaire rare dans l'écosystème open source embarqué. Ygreky intervient pour des fabricants de produits connectés souhaitant mettre en conformité leur chaîne logicielle avec le CRA.

## Résumé
Le Cyber Resilience Act est publié au Journal officiel de l'UE et entre en vigueur progressivement jusqu'en décembre 2027, avec une première échéance dès septembre 2026 : la notification obligatoire des vulnérabilités activement exploitées. Les simples contributeurs open source sont explicitement exemptés ; les obligations incombent aux fabricants qui monétisent, qui doivent notamment fournir 5 ans de mises à jour de sécurité gratuites et notifier les projets upstream des failles découvertes. Entre 70 et 90 % des composants d'un produit commercial étant open source, la production de S-BOM devient incontournable. L'analyse des risques est l'unique fondement juridique des mesures de sécurité à mettre en place.

## Points marquants
- Le CRA est en vigueur ; première échéance dès septembre 2026.
  La notification obligatoire des vulnérabilités activement exploitées s'applique à tous les produits concernés dès septembre 2026, y compris les versions déjà en marché. L'entrée en vigueur complète est prévue pour décembre 2027.
- Les simples contributeurs open source sont explicitement exemptés de toute obligation.
  Cette exemption n'était pas acquise dans les premières versions du texte. Seuls les fabricants (ceux qui monétisent) et les intendants de logiciels ouverts (personnes morales supportant un projet) ont des obligations.
- Les fabricants sont tenus de notifier les projets upstream des failles découvertes.
  Si un fabricant découvre une faille dans une dépendance open source, il doit la signaler au projet upstream. Le projet n'a aucune obligation d'agir en retour, mais il recevra les rapports et patches des acteurs commerciaux.
- 5 ans de mises à jour de sécurité gratuites sont obligatoires pour les fabricants.
  Les fabricants ne peuvent pas vendre un produit au-delà de la fin de cette période d'assistance sans justification. La durée doit être alignée sur la durée de vie prévue du produit, que le fabricant doit communiquer.
- Entre 70 et 90 % des composants d'un produit commercial sont open source.
  Ce chiffre rend la production d'un S-BOM (Software Bill of Materials) incontournable. La génération est particulièrement complexe dans les architectures conteneurisées, où la combinaison de plusieurs S-BOM issus de microservices distincts n'est pas triviale.

## Technologies
- **S-BOM (Software Bill of Materials)** — Inventaire exhaustif des composants logiciels d'un produit, rendu obligatoire par le CRA pour tous les fabricants. La génération de S-BOM est complexe dans les environnements conteneurisés à cause de la multiplication des composants et de la difficulté de combiner plusieurs S-BOM issus de microservices distincts.
- **Projet Yocto** — Framework open source de construction de distributions Linux embarquées. Directement concerné par le CRA car intégré dans de nombreux produits matériels connectés. L'intervenante y contribue et travaille sur les processus de sécurité associés.
- **Noyau Linux** — Composant open source central dans les systèmes embarqués. Les fabricants qui l'intègrent doivent analyser ses risques et notifier le projet upstream en cas de faille découverte dans leur produit.
- **OpenSSF (Open Source Security Foundation)** — Groupe de travail produisant des guides pour aider les projets open source à répondre aux exigences de sécurité du CRA. Ressource de référence pour les équipes DevSecOps cherchant à se conformer.
- **ETSI / CEN/CENELEC** — Organismes de normalisation européens produisant les standards techniques associés au CRA. Les entreprises souhaitant influencer ces normes peuvent y participer directement.
- **Conteneurisation (Docker/OCI)** — Facilite la génération de S-BOM par analyse des images livrées, mais complexifie leur gestion en raison de l'explosion du nombre de composants dans les architectures microservices.
