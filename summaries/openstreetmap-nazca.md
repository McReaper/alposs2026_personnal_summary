# AlpOSS 2026 - OpenStreetMap, Wikipedia, Commons, Wikidata et les figures de Nazca

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Guillaume Allègre |
| **Organisation** | Wikimédia France / OpenStreetMap |
| **Durée** | 20:59 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Guillaume Allègre est informaticien professionnel qui contribue bénévolement à l'écosystème des communs numériques : Wikipédia, Wikimedia Commons, Wikidata et OpenStreetMap. Libriste convaincu, il s'investit à la fois pour l'aspect communautaire et partage du savoir, et pour les aspects techniques pointus de ces projets. Il intervient à AlpOSS à titre personnel, en tant que militant et contributeur, et anime également un atelier sur les coulisses de Wikipédia lors de l'événement.

## Résumé

Guillaume Allègre présente un panorama technique de quatre projets libres complémentaires — Wikipédia, Wikimedia Commons, Wikidata et OpenStreetMap — en mettant l'accent sur leurs rouages techniques et leurs interactions.

**Wikipédia** fête ses 25 ans en 2026 (édition anglophone en janvier, francophone trois mois plus tard). Son moteur est **MediaWiki**, développé depuis 2000 en PHP/SQL.

**Wikimedia Commons** est l'instance centralisée hébergeant les médias de toutes les Wikipédia linguistiques (photos, cartes, sons, vidéos et formats de données avancés). Il dépasse le simple stockage d'images statiques en supportant des formats interactifs comme les cartes GeoJSON embarquées.

**Wikidata** (lancé en 2013) est la base de données structurées de l'écosystème, issue du besoin de centraliser les liens interlangues. Elle fonctionne sur le modèle du **web sémantique** : chaque entité a un identifiant unique et pérenne (ex. Q211134 pour Échirolles), associé à des déclarations (objet–propriété–valeur). L'interrogation se fait via **SPARQL** grâce au Wikidata Query Service.

**OpenStreetMap** est la carte du monde collaborative (fondée sur PostgreSQL/PostGIS), avec une architecture de données en deux niveaux : géométries simples (points, lignes, polygones) enrichies d'attributs sémantiques (tags). L'API **Overpass** permet d'interroger la base en temps réel via l'assistant **Overpass Turbo**. Le format **GeoJSON** et la bibliothèque JavaScript **Leaflet** permettent d'intégrer ces données dans des interfaces web légères.

Guillaume illustre l'interaction entre ces projets avec deux exemples grenoblois : les remparts romains de Cularo/Grenoble visibles dans Wikipédia via une carte dynamique GeoJSON intégrée à Wikimedia Commons, et les remparts actuels d'Avignon dont le tracé est directement issu d'OpenStreetMap et affiché dans Commons via la balise `MapFrame`.

Il conclut sur les actualités 2026 : Wikimania (congrès mondial Wikimédia) et State of the Map (congrès mondial OpenStreetMap) se tiennent tous les deux à Paris cette année — une coïncidence remarquable.

*Note : les figures de Nazca mentionnées dans le titre n'ont pas été développées faute de temps.*

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Wikidata / SPARQL** — Base de données sémantiques libre et son langage d'interrogation ; exploitable pour des projets de knowledge graph, de data enrichissement ou d'intégration de données ouvertes dans des SI
- **Wikidata Query Service** — Interface d'interrogation SPARQL en ligne ; modèle à suivre pour exposer des données structurées à des tiers sans développement client
- **OpenStreetMap (OSS)** — Base cartographique mondiale libre (ODbL) ; alternative souveraine à Google Maps pour des applications métier, des SIG internes ou des services géolocalisés
- **Overpass API / Overpass Turbo** — API d'interrogation géospatiale en temps réel sur les données OSM ; utile pour des requêtes ponctuelles sans avoir à héberger un dump complet
- **PostgreSQL / PostGIS** — Socle de la stack cartographique OSM ; extension géospatiale incontournable pour toute application SIG hébergée en interne
- **GeoJSON** — Format standard d'échange de données géographiques en JSON ; très utilisé dans les API REST géospatiales et les front-ends web cartographiques
- **Leaflet** — Bibliothèque JavaScript légère pour l'affichage de cartes interactives ; alternative open source à Google Maps JS ou Mapbox GL
- **MediaWiki** — Moteur wiki open source (PHP/SQL) sur lequel repose tout l'écosystème Wikimédia ; déployable en interne pour des bases de connaissances d'équipe

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- **2026 : double anniversaire parisien** — Wikimania et State of the Map 2026 se tiennent tous les deux à Paris la même année, une coïncidence rarissime pour la communauté des communs numériques
- **25 ans de Wikipédia** en 2026 : projet lancé en janvier 2001, il reste le 5e site le plus visité au monde, géré sans publicité par une fondation à but non lucratif
- L'identifiant Wikidata d'Échirolles (ville hôte d'AlpOSS) est **Q211134** — tout lieu, concept ou personne notable possède un identifiant unique et pérenne dans cette base mondiale
- La complexité de gestion des liens interlangues entre N langues générait un coût en O(N²) avant la création de Wikidata en 2013 — un problème d'ingénierie massif résolu par la centralisation sémantique
- Les données OpenStreetMap sont **licenciées ODbL** : même un logiciel propriétaire peut les consommer, mais toute redistribution des données dérivées doit rester libre — un modèle de licence copyleft adapté aux données

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Guillaume Allègre (Wikimédia France / OpenStreetMap)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
