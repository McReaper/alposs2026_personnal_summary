# Vers une messagerie instantanée libre, décentralisée et souveraine : quel Tchap pour les collectivités ?

## Intervenant
Matthieu Faure · ADULLACT / Erik Da Silva · Arawa / Philippe Le Brouster · Ville d'Échirolles / Stéphane Vangheluwe · SITIV

## Société
L'ADULLACT est l'association nationale des développeurs et utilisateurs de logiciels libres pour les administrations et collectivités territoriales, active depuis plus de 20 ans. Arawa est un intégrateur de solutions libres (Nextcloud, Matrix/Element, BigBlueButton) spécialisé dans les collectivités. Le SITIV est un OPSN (Opérateur Public de Services Numériques) membre de Déclic, fédération regroupant 80 OPSN sur le territoire français. Ce projet réunit ces acteurs pour déployer une messagerie instantanée souveraine couvrant les 30 000 collectivités françaises exclues du périmètre de Tchap État.

## Résumé
Tchap, la messagerie de l'État basée sur Matrix/Element, ne couvre pas les collectivités territoriales. Ce projet porté par l'ADULLACT, Arawa et la fédération Déclic vise à déployer une infrastructure Matrix fédérée, une instance par collectivité, pour permettre des échanges chiffrés de bout en bout entre agents publics locaux. Le réseau sera fermé aux seules collectivités membres, avec des passerelles envisagées vers Tchap État. L'identité des agents sera labellisée via ProConnect pour éviter toute dépendance à Microsoft ou Google.

## Points marquants
- Tchap exclut les 30 000 collectivités françaises en 2026.
- Matrix garantit le chiffrement E2EE, même pour les admins.
- Tchap État a forké Synapse : il n'est plus fédéré avec Matrix.
- Le réseau collectivités sera fermé, avec passerelles vers l'État.

## Technologies
- **Matrix (protocole)** — Protocole de communication décentralisé, fédéré et chiffré de bout en bout (standard ouvert). Base technique de Tchap et d'Element. Permet un réseau distribué sans point central, une instance par structure et une fédération entre instances. Seule messagerie combinant réseau distribué + E2EE + multiplateforme + logiciel libre.
- **Element** — Client Matrix open source (anciennement Riot), disponible sur toutes plateformes. Retenu comme client pour le projet des collectivités. La société Element (New Vector) est l'éditeur commercial qui assure le support de niveau 2 et 3 pour Arawa.
- **Synapse** — Serveur de référence du protocole Matrix, déployé via conteneurs Docker dans l'infrastructure Arawa. Tchap État en a réalisé un fork, le coupant du reste de l'écosystème Matrix — une limite explicitement identifiée.
- **ProConnect** — Solution d'identité numérique de l'État (ex-AgentConnect). Utilisée pour labelliser les identités des agents dans le réseau des collectivités, sans dépendre de fournisseurs d'identité privés (Microsoft, Google).
- **Nextcloud / BigBlueButton** — Solutions complémentaires déployées par Arawa pour l'ADULLACT. Illustrent la capacité d'Arawa à proposer une suite collaborative complète et souveraine pour les collectivités.
