# AlpOSS 2026 - Vers une messagerie instantanée libre, décentralisée et souveraine : quel Tchap pour les collectivités ?

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Matthieu Faure (ADULLACT), Erik Da Silva (Arawa), Philippe Le Brouster (Échirolles), Stéphane Vangheluwe (SITIV) |
| **Organisation** | ADULLACT / Arawa / Ville d'Échirolles / SITIV |
| **Durée** | 19:20 |
| **Présent** | ✅ Oui |

## À propos des intervenants

- **Matthieu Faure** — Représentant de l'ADULLACT (Association des Développeurs et des Utilisateurs de Logiciels Libres pour les Administrations et les Collectivités Territoriales). Il coordonne le projet et présente la vision d'ensemble et les enjeux politiques. Membre de l'ADULLACT depuis 20 ans.
- **Erik Da Silva** — Société Arawa, intégrateur de solutions libres (notamment Nextcloud et Matrix/Element). Arawa héberge le Nextcloud et le BigBlueButton de l'ADULLACT. Prend en charge la partie technique et opérationnelle du projet.
- **Philippe Le Brouster** — DSI de la Ville d'Échirolles (ville hôte d'AlpOSS). Présent sur scène comme représentant de la collectivité partenaire du projet.
- **Stéphane Vangheluwe** — Directeur d'un OPSN (Opérateur Public de Services Numériques), représentant de Déclic (fédération regroupant 80 OPSN sur le territoire). Apporte la dimension organisationnelle et territoriale du déploiement.

## Résumé

Le modérateur introduit la session : quatre personnes pour trois noms affichés sur le diapositive. Matthieu Faure prend la parole en premier pour cadrer le sujet.

---

### Matthieu Faure (ADULLACT) — Cadre du projet et enjeux politiques

Matthieu pose le contexte : Tchap est la messagerie instantanée de l'État français. Après des "yo-yo" institutionnels (périmètre tantôt étendu aux collectivités, tantôt restreint à l'administration centrale), la situation est claire : Tchap ne concerne que les agents de l'administration centrale de l'État. Les collectivités ne sont pas couvertes.

La réponse des collectivités : "elles se prennent par la main" et montent leur propre projet, basé sur la même brique technologique — Matrix/Element — mais déployée de façon autonome. L'outil retenu pour ce réseau de collectivités est **Element** (nom du client) ou **Matrix** (nom provisoire du projet), avec comme principe une instance par structure et une fédération entre les instances.

Il souligne la situation paradoxale : des utilisateurs sur WhatsApp, Telegram ou Signal "ne peuvent pas forcément discuter entre eux, et aucune de ces trois messageries n'est libre" (Signal faisant l'objet d'un débat à l'apéro, selon Matthieu). L'objectif du projet est de permettre aux collectivités de discuter entre elles, en interne et d'une collectivité à l'autre, via une infrastructure souveraine.

Sur le plan politique, Matthieu conclut en évoquant l'exemple du procureur de la Cour Pénale Internationale dont le mail a été bloqué — "symptomatique du monde dans lequel nous vivons" et qui a "radicalement changé depuis le début de l'année." Il pose la question : si demain matin vous n'avez plus accès à votre mail, que faites-vous ? Et si Google décide que les notions d'éthique "entravent son business" ? La souveraineté numérique n'est plus abstraite. L'ADULLACT s'engage à lutter contre les portes dérobées et à afficher clairement ses valeurs.

---

### Erik Da Silva (Arawa) — Architecture technique et rôle de l'intégrateur

Erik présente brièvement le rôle d'Arawa dans le projet. Techniquement, la plateforme repose sur une VM avec plusieurs conteneurs : Synapse (serveur Matrix), Element (client web) et le Matrix Authentication Service. La personnalisation inclut un logo propre au réseau et la synchronisation des comptes via QR code.

Il insiste sur le modèle de support : Arawa s'attache à construire un partenariat avec l'éditeur (Element la société) pour définir un modèle de support de niveau 2 et niveau 3 à destination des collectivités, sur une version open source d'Element et de Synapse.

Concernant la contribution : Arawa est "en étroite discussion avec Element l'entreprise" car l'ADULLACT considère important de "faire tourner la machine économique" — la contribution prendra probablement la forme d'argent plutôt que de code.

---

### Stéphane Vangheluwe (SITIV / Déclic) — Organisation territoriale et confiance

Stéphane dirige un OPSN et est membre de Déclic, fédération de 80 OPSN sur le territoire français. Il recentre le propos sur la dimension organisationnelle : le défi n'est pas seulement technique, c'est de construire un **réseau de confiance territorial**.

Il cite la suite collaborative "Territoire Numérique Ouvert" portée par la NCT (Nantes/Lyon/SITYVONNE) comme exemple de projet similaire. La confiance repose sur une **identité de confiance** — qu'on ne souhaite pas confier à Microsoft ou Google — labellisée via ProConnect (l'identité numérique de l'État). Il souligne qu'avec 30 000 collectivités en France (contre "dix ministères" pour l'État), l'organisation territoriale est un défi majeur : "il faut pas qu'il y ait des zones blanches."

Le rôle de la fédération Déclic : accompagner les collectivités pour la sécurisation, la dématérialisation et la collaboration souveraine. L'objectif est que "plus de 50 % des collectivités représentées par les Déclic soient desservies" par ce réseau.

---

### Questions de la salle

**Sur la fédération ouverte vs fermée et le fork de Tchap** : un intervenant note que Tchap a forké le client Element et le serveur Synapse, ce qui le rend non fédéré avec le reste de l'écosystème Matrix. Est-ce que le projet des collectivités fera de même ? Matthieu répond : le réseau des collectivités sera **fermé** (pour établir la confiance, on ne peut pas laisser n'importe qui rejoindre), mais des passerelles avec Tchap (État) sont en discussion avec la DINUM. La cible à terme : "faire de Tchap le Tchap de la fonction publique." Erik précise que des enjeux de sécurité côté État rendent la fédération ouverte impossible à court terme.

**Sur la distribution et le packaging** : un enseignant-chercheur de l'UGA demande si les solutions seront packageées pour les distributions Linux, smartphones, F-Droid. Stéphane répond : le métier de l'ADULLACT et des OPSN c'est de "diffuser ces solutions et les mettre à disposition", pas de produire du logiciel directement. Erik complète : l'enjeu est de rester au plus proche des packagings existants et de contribuer à leur évolution si nécessaire.

**Sur le "Chat Control"** (projet européen de surveillance des messageries) : Matthieu répond directement — "c'est une lutte." L'ADULLACT s'oppose aux portes dérobées, "absolument pas" question de les accepter dans ce projet.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Matrix (protocole)** — Protocole de communication décentralisé, fédéré et chiffré de bout en bout. Standard ouvert. Base technique de Tchap et d'Element. Réseau distribué : pas de point central, une instance par structure, fédération entre instances. Seule messagerie permettant simultanément : réseau distribué + chiffrement E2EE + multiplateforme + logiciel libre.
- **Element** — Client Matrix open source (anciennement Riot). Nom du client retenu pour le projet des collectivités. Disponible sur toutes plateformes. La société Element (New Vector) est l'éditeur commercial.
- **Synapse** — Serveur de référence du protocole Matrix. Déployé via conteneurs Docker dans l'infrastructure Arawa. Possibilité de fork par Tchap (État) qui a créé ses propres branches.
- **Matrix Authentication Service** — Composant Matrix gérant l'authentification, déployé dans la stack Arawa.
- **Tchap** — Messagerie instantanée de l'État français basée sur Matrix/Element, opérée par la DINUM. Réservée aux agents de l'administration centrale. Non fédérée avec le reste de l'écosystème Matrix (fork de Synapse). Des discussions sont en cours pour créer des passerelles avec le réseau des collectivités.
- **ProConnect** — Solution d'identité numérique de l'État (anciennement AgentConnect). Mentionnée comme l'outil de confiance pour labelliser les identités dans le réseau des collectivités, sans dépendre de Microsoft ou Google.
- **Nextcloud / BigBlueButton** — Solutions complémentaires déployées par Arawa pour l'ADULLACT. Contexte : Arawa est intégrateur multi-produits open source pour les collectivités.
- **Déclic** — Fédération de 80 OPSN (Opérateurs Publics de Services Numériques) sur le territoire français. Rôle d'accompagnement et d'organisation pour le déploiement du réseau de messagerie entre collectivités.

## Points marquants

- Tchap ne couvre pas les collectivités territoriales en 2026 — les 30 000 collectivités françaises sont donc livrées à WhatsApp, Telegram ou Teams pour leur messagerie instantanée professionnelle. Ce projet comble ce vide.
- Le chiffrement de bout en bout de Matrix signifie que même les administrateurs de l'instance ne peuvent pas lire les contenus — distinction cruciale par rapport à des solutions comme Teams ou Exchange où l'administrateur a accès à tout.
- Tchap a forké Element et Synapse, ce qui le coupe du reste de l'écosystème Matrix — une faiblesse explicitement nommée. Le projet des collectivités cherche à éviter cette erreur.
- La référence au procureur de la Cour Pénale Internationale dont le mail a été bloqué (par les États-Unis) est utilisée comme argument politique concret : le blocage de communications peut être un "acte de guerre" et illustre la dépendance aux GAFAM.
- "Chat Control" — le projet européen de surveillance des messageries chiffrées — est directement évoqué comme menace à contrer. L'ADULLACT s'y oppose frontalement.
- Le réseau sera **fermé** (uniquement les collectivités membres) mais avec des passerelles envisagées vers Tchap (État) — un équilibre délicat entre confiance fermée et interopérabilité ouverte.
- Stéphane Vangheluwe signale le risque des forks trop divergents : "quand on a un peu trop de forks, j'en parle par expérience, on a du mal à parler avec les autres."
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Matthieu Faure (ADULLACT), Erik Da Silva (Arawa), Philippe Le Brouster (Échirolles), Stéphane Vangheluwe (SITIV)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
