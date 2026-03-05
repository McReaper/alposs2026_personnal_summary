# Vers une messagerie instantanée libre, décentralisée et souveraine : quel Tchap pour les collectivités ?

## Intervenant
Matthieu Faure · ADULLACT / Erik Da Silva · Arawa / Philippe Le Brouster · Ville d'Échirolles / Stéphane Vangheluwe · SITIV

## Société
L'ADULLACT est l'association nationale des développeurs et utilisateurs de logiciels libres pour les administrations et collectivités territoriales, active depuis plus de 20 ans. Arawa est un intégrateur de solutions libres (Nextcloud, Matrix/Element, BigBlueButton) spécialisé dans les collectivités. Le SITIV est un OPSN (Opérateur Public de Services Numériques) membre de Déclic, fédération regroupant 80 OPSN sur le territoire français. Ce projet réunit ces acteurs pour déployer une messagerie instantanée souveraine couvrant les 30 000 collectivités françaises exclues du périmètre de Tchap État.

## Résumé
Les 30 000 collectivités françaises sont exclues de Tchap (la messagerie sécurisée de l'État) et recourent à WhatsApp ou Teams faute d'alternative. Ce projet déploie une messagerie chiffrée de bout en bout pour agents publics locaux, une instance par collectivité, avec authentification via le système d'identité national ProConnect.

## Points marquants
- Tchap couvre uniquement l'administration centrale de l'État, pas les collectivités.
  Après plusieurs changements de périmètre, la situation en 2026 est claire : les 30 000 collectivités françaises ne sont pas couvertes par Tchap et recourent à WhatsApp, Telegram ou Teams pour leur messagerie instantanée professionnelle. Ce projet comble ce vide.
- Matrix est la seule messagerie combinant réseau distribué, E2EE, multiplateforme et logiciel libre.
  Le chiffrement de bout en bout signifie que même les administrateurs de l'instance ne peuvent pas lire les contenus — contrairement à Teams ou Exchange où l'administrateur a accès à tout. La nature open source permet de vérifier que les processus de chiffrement sont bien respectés.
- Tchap État a forké Element et Synapse, se coupant de l'écosystème Matrix.
  Ce fork a été réalisé pour des raisons de sécurité permettant de gérer des niveaux de communication élevés côté État. Le projet des collectivités cherche à éviter cette erreur et reste au plus proche des packagings existants.
- Le réseau sera fermé aux collectivités membres, avec des passerelles envisagées vers Tchap État.
  La fermeture est nécessaire pour établir la confiance : on ne peut pas laisser n'importe qui rejoindre le réseau. Des discussions sont en cours avec la DINUM pour créer des passerelles, avec pour objectif à terme de "faire de Tchap le Tchap de la fonction publique."
- L'identité des agents sera labellisée via ProConnect, sans dépendance à Microsoft ou Google.
  La fédération Déclic (80 OPSN sur le territoire) pilote l'organisation territoriale pour que plus de 50 % des collectivités représentées soient desservies, en s'assurant qu'il n'y ait pas de zones blanches entre communes voisines.

## Technologies
- **Matrix (protocole)** — Protocole de communication décentralisé, fédéré et chiffré de bout en bout (standard ouvert). Base technique de Tchap et d'Element. Permet un réseau distribué sans point central, une instance par structure et une fédération entre instances. Seule messagerie combinant réseau distribué + E2EE + multiplateforme + logiciel libre.
- **Element** — Client Matrix open source (anciennement Riot), disponible sur toutes plateformes. Retenu comme client pour le projet des collectivités. La société Element (New Vector) est l'éditeur commercial qui assure le support de niveau 2 et 3 pour Arawa.
- **Synapse** — Serveur de référence du protocole Matrix, déployé via conteneurs Docker dans l'infrastructure Arawa. Tchap État en a réalisé un fork, le coupant du reste de l'écosystème Matrix — une limite explicitement identifiée.
- **ProConnect** — Solution d'identité numérique de l'État (ex-AgentConnect). Utilisée pour labelliser les identités des agents dans le réseau des collectivités, sans dépendre de fournisseurs d'identité privés (Microsoft, Google).
- **Nextcloud / BigBlueButton** — Solutions complémentaires déployées par Arawa pour l'ADULLACT. Illustrent la capacité d'Arawa à proposer une suite collaborative complète et souveraine pour les collectivités.
