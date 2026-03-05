# OpenStreetMap, Wikipedia, Commons, Wikidata et les figures de Nazca

## Intervenant
Guillaume Allègre · Wikimédia France / OpenStreetMap

## Société
Guillaume Allègre est informaticien professionnel qui contribue bénévolement à l'écosystème des communs numériques : Wikipédia, Wikimedia Commons, Wikidata et OpenStreetMap. Libriste convaincu, il s'investit à la fois sur les aspects communautaires et techniques de ces projets. Il intervient à AlpOSS à titre personnel, en tant que militant et contributeur, et anime également un atelier sur les coulisses de Wikipédia lors de l'événement.

## Résumé
Wikipédia, Wikidata, Wikimedia Commons et OpenStreetMap sont quatre communs numériques distincts — données encyclopédiques, sémantiques, médias et cartographiques — mais techniquement interconnectés. Cette articulation permet d'afficher des cartes dynamiques OpenStreetMap directement dans les articles Wikipédia.

## Points marquants
- Wikimania et State of the Map 2026 tous les deux à Paris.
- Wikidata résout un problème de liens interlangues en O(N²).
- Données OSM sous ODbL : redistribution dérivée doit rester libre.
- 25 ans de Wikipédia en 2026, 5e site le plus visité au monde.

## Technologies
- **OpenStreetMap / PostGIS** — Base cartographique mondiale libre (ODbL) adossée à PostgreSQL/PostGIS ; alternative souveraine à Google Maps pour des applications métier, des SIG internes ou des services géolocalisés ; les données sont librement consommables y compris dans des logiciels propriétaires.
- **Overpass API / Overpass Turbo** — API d'interrogation géospatiale en temps réel sur les données OSM ; utile pour des requêtes ponctuelles sans héberger un dump complet ; Overpass Turbo fournit une interface web pour tester les requêtes.
- **Wikidata / SPARQL** — Base de données sémantiques libre (modèle web sémantique, identifiants pérennes) et son langage d'interrogation ; exploitable pour des projets de knowledge graph, d'enrichissement de données ou d'intégration de données ouvertes dans des SI.
- **GeoJSON** — Format standard d'échange de données géographiques en JSON ; très utilisé dans les API REST géospatiales et les front-ends web cartographiques ; support natif dans Wikimedia Commons via la balise MapFrame.
- **Leaflet** — Bibliothèque JavaScript légère pour l'affichage de cartes interactives ; alternative open source à Google Maps JS ou Mapbox GL ; intégrée dans l'écosystème Wikimédia pour les cartes dynamiques.
- **MediaWiki** — Moteur wiki open source (PHP/SQL) sur lequel repose tout l'écosystème Wikimédia depuis 2000 ; déployable en interne pour des bases de connaissances d'équipe.
