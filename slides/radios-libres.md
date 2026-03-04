# Radios libres ?

## Intervenant
Martin Kirchgessner · Radio Campus Grenoble

## Société
Radio Campus Grenoble est une radio associative grenobloise (catégorie A ARCOM) fondée en 1994, émettant en FM et en streaming, avec plus de 5 000 épisodes de podcasts archivés. Elle est financée par le FSER (Fonds de Soutien à l'Expression Radiophonique), dispositif public finançant 700 radios associatives en France via le ministère de la Culture. Martin Kirchgessner y est bénévole depuis douze ans et assure les responsabilités informatiques de l'association, dont le développement d'un automate de diffusion maison rendu open source après cinq ans d'usage interne.

## Résumé
Martin Kirchgessner dresse un panorama des radios associatives françaises et de leur rapport au logiciel libre : historique du secteur depuis la fin du monopole ORTF, modèle économique du FSER, et stack technique libre complète pour créer une radio en 2026. La chaîne outillée avec du libre est mature — Linux, Audacity, Liquidsoap, Icecast, Castopod — mais la barrière d'entrée reste réglementaire : la bande FM est saturée et l'ARCOM n'attribue plus de fréquences. Face à l'"enshittification" d'Internet et à la disparition des récepteurs FM des smartphones, la radio reste un medium de résilience, comme l'a montré la panne électrique espagnole de 2025.

## Points marquants
- 700 radios associatives financées par l'État via le FSER.
- La bande FM est saturée : plus de fréquences disponibles.
- Liquidsoap, écrit en OCaml, tourne jusqu'à Radio France.
- La panne espagnole 2025 : seule la radio nationale émettait.

## Technologies
- **Liquidsoap** — Langage de script pour la génération de flux audio/vidéo en continu. Open source, maintenu par des développeurs français, écrit en OCaml. Utilisé de la radio associative jusqu'à Radio France pour sa robustesse en production 24/7.
- **Icecast** — Serveur de streaming audio open source (HTTP). Standard de fait pour la webradio, léger et compatible avec la majorité des lecteurs multimédia. Utilisable comme infrastructure de diffusion interne ou publique.
- **Audacity** — Éditeur audio multiplateforme open source. Outil de base pour la production audio, le podcasting et la post-production légère.
- **Castopod** — Plateforme de podcasting open source auto-hébergeable. Alternative souveraine à Spotify/Apple Podcasts, avec support natif du protocole ActivityPub pour la diffusion dans le Fediverse.
- **Open Digital Radio** — Suite open source pour la diffusion DAB/DAB+. Alternative aux solutions propriétaires de multiplexage numérique terrestre, utilisée par des radios associatives voulant émettre en numérique.
