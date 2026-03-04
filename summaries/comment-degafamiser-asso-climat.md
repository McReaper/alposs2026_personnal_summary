# AlpOSS 2026 - Comment déGAFAMiser une asso climat ?

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Gauthier Fanucci |
| **Organisation** | Alternatiba |
| **Durée** | 6:26 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Gauthier Fanucci est responsable informatique (et militant libriste auto-proclamé « casse-pieds de services ») au sein d'Alternatiba, mouvement citoyen pour le climat et la justice sociale actif depuis le début des années 2010. Il gère l'infrastructure numérique de l'association avec un autre responsable IT, tous deux engagés dans la transition vers des logiciels libres. Il présente depuis un fauteuil roulant, une béquille à la main, signe de son engagement bénévole malgré un accident.

## Résumé

Gauthier Fanucci ouvre la conférence en posant le paradoxe fondamental des mouvements militants : être convaincu que les GAFAM sont nuisibles (pour la vie privée, l'environnement, l'indépendance technologique) tout en utilisant leurs outils au quotidien, faute d'alternatives suffisamment ergonomiques.

Alternatiba (une centaine de groupes locaux en France, connu pour ses villages des alternatives, ses tours à vélo quadruplet et ses marches pour le climat de 2018-2019) a décidé d'avancer « un octet à la fois », en reprenant le slogan de Framasoft. Plutôt que de tout migrer d'un coup, l'association a identifié sa priorité numéro un : la protection des données personnelles de ses militants (numéros de téléphone, coordonnées) qui étaient stockées dans Google Sheets.

Grâce au mécénat de compétences de la coopérative Télescope, Alternatiba a déployé un système d'information fondé sur deux logiciels libres : **Baserow** (base de données no-code, hébergée en propre) et **N8N** (automatisation de workflows). Ce système permet désormais des formulaires, des envois de mails automatiques, des statistiques et des cartographies, le tout maîtrisé en interne.

Pour les services qu'ils n'hébergent pas eux-mêmes, Alternatiba s'appuie sur des « hébergeurs éthiques » — définis avec humour par le critère de la « distance d'une bière » : peut-on aller boire un coup avec son hébergeur ? Framasoft passe le test, Google non. Les mails ont été migrés d'OVH vers Grésille. La prochaine étape est la migration de Google Drive vers Nextcloud.

Gauthier conclut en présentant une campagne en cours de lancement : une mobilisation large contre l'obsolescence programmée imposée par Microsoft avec la fin du support de Windows 10, visant à transformer l'indignation des utilisateurs en levier pour la promotion du logiciel libre. Il appelle associations, collectivités, entreprises et particuliers à rejoindre cette campagne.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Baserow** — Base de données no-code open source, alternative à Airtable/Google Sheets. Intéressant pour les ESN cherchant à proposer des solutions de gestion de données souveraines à leurs clients associatifs ou PME.
- **N8N** — Outil d'automatisation de workflows (ETL léger, intégrations API). Concurrent open source de Zapier/Make, auto-hébergeable. Très pertinent pour des missions d'intégration ou de RPA chez des clients souhaitant sortir des outils SaaS propriétaires.
- **Nextcloud** — Suite collaborative open source (Drive, Agenda, Documents). Standard de fait pour la souveraineté des données en entreprise et collectivités. Forte demande en déploiement et MCO.
- **Framasoft / les Chatons** — Réseau d'hébergeurs éthiques proposant des alternatives libres aux GAFAM. Cadre de référence pour identifier des partenaires d'hébergement conformes RGPD.
- **Grésille** — Hébergeur de messagerie éthique francophone. Exemple d'alternative à OVH ou Gmail pour des structures sensibles à la souveraineté des données.

## Points marquants

- Alternatiba utilise encore Google Drive en 2026, malgré ses positions militantes contre les GAFAM : le parfait exemple que même les associations les plus engagées subissent la dette technique propriétaire.
- Le critère de sélection d'un hébergeur : « Est-ce que je peux aller boire un coup avec lui ? » — une formulation qui résume brillamment le besoin de proximité et de confiance dans la chaîne numérique.
- La campagne contre la fin du support Windows 10 est présentée comme un levier d'entrée pour le grand public vers le logiciel libre, en capitalisant sur l'indignation liée à l'obsolescence forcée de millions d'ordinateurs encore fonctionnels.
- Le mécénat de compétences (ici par la coopérative Télescope) est présenté comme un modèle viable pour financer la transition numérique des associations, à l'heure où les subventions publiques diminuent.
- Les subventions pour les associations sont en baisse : un contexte qui renforce l'attrait des solutions libres auto-hébergées, moins coûteuses à long terme.
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Gauthier Fanucci (Alternatiba)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
