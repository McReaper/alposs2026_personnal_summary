# AlpOSS 2026 - Radios libres ?

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Martin Kirchgessner |
| **Organisation** | Radio Campus Grenoble |
| **Durée** | 17:25 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Martin Kirchgessner est développeur de formation et de métier, et bénévole à Radio Campus Grenoble depuis une douzaine d'années. À l'intersection des deux mondes — radio associative et logiciel libre —, il s'occupe des questions informatiques de l'association et a développé l'automate de diffusion maison de Radio Campus Grenoble, qu'il a récemment repackagé comme un logiciel libre à part entière (avec son propre site .org). Il a également croisé d'autres radios associatives et connaît bien l'écosystème technique et réglementaire du secteur.

## Résumé

Martin Kirchgessner clôt la journée AlpOSS 2026 avec une présentation sur les radios associatives et leur rapport au logiciel libre.

Il retrace d'abord l'**histoire des radios françaises** depuis le début des années 70 : monopole de l'ORTF, dissolution en 1974, création de Radio France, puis concurrence des radios périphériques (RMC, RTL sur grandes ondes) et des premières radios pirates FM. C'est la fin du monopole d'État sous Mitterrand (début des années 80) qui libère les fréquences, entraînant la création du CSA en 1989 (devenu ARCOM en 2022) et du **FSER** (Fonds de Soutien à l'Expression Radiophonique) dès 1982, toujours actif aujourd'hui.

Le **FSER** est au cœur du modèle économique des radios associatives (catégorie A de l'ARCOM) : subvention du ministère de la Culture, conditionnée à moins de 20% de revenus publicitaires. Le ministère finance ainsi **700 radios** dans tout le pays, dont neuf à Grenoble. Un financement public massif pour un secteur qui ne dit pas toujours son nom associatif.

Martin souligne les **affinités naturelles** entre radios associatives et monde du libre : bénévolat, diffusion gratuite, esprit DIY, éducation populaire. Mais aussi les distances : ce ne sont pas les mêmes métiers (journalisme/musique vs développement), pas les mêmes temporalités, et les radios sont ancrées localement.

Il décrit les **défis numériques actuels** des radios : DAB+ (démarré à Grenoble en 2021), podcasting, réseaux sociaux, diffusion mobile, live sur Twitch… Un écosystème fragmenté où le média dominant glisse vers la vidéo. Aucune certitude sur l'avenir.

Puis il imagine **créer une radio associative en 2026 avec des logiciels libres** :
- Studio sous **Linux** (support carte son excellent)
- Edition audio : **Audacity**, **Mixxx**, **Ardour**, **VLC**
- Automate de diffusion : **Liquidsoap** (script de flux audio/vidéo, développé par des Français, écrit en OCaml, utilisé jusqu'à Radio France), ou le logiciel maison de Radio Campus Grenoble
- Diffusion web : **Icecast** (flux HTTP)
- DAB : **Open Digital Radio** (suite open source pour le multiplexage)
- Podcast : **Castopod**, plugins WordPress
- Archivage obligatoire : 30 jours d'historique (exigence réglementaire) — réalisable en libre facilement

La principale barrière à l'entrée n'est pas technique mais **réglementaire et physique** : la bande FM est saturée, l'ARCOM n'attribue plus de fréquences, et les points hauts de la vallée grenobloise sont monopolisés par les télécoms.

Il conclut avec une note d'espoir : face à l'"enshittification" d'Internet, la radio reste anonyme, locale et humaine. La panne électrique espagnole de 2025 — où seule la radio nationale émettait encore — rappelle sa valeur de résilience.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Liquidsoap** — Langage de script pour la génération de flux audio/vidéo en continu ; open source, maintenu par des Français (OCaml), utilisé de la radio associative à Radio France ; pertinent pour tout projet de streaming ou de diffusion automatisée
- **Icecast** — Serveur de streaming audio open source (HTTP) ; standard de fait pour la webradio, léger et compatible avec la majorité des lecteurs ; utilisable en infrastructure de diffusion interne
- **Audacity** — Éditeur audio multiplateforme open source ; outil de base pour la production audio, podcasting, post-production légère
- **Mixxx** — Logiciel de DJing/mixage open source ; développé initialement pour les discothèques, adapté aux studios radio
- **Ardour** — DAW (Digital Audio Workstation) open source professionnel ; pour le montage et la production audio avancée
- **Open Digital Radio** — Suite open source pour la diffusion DAB/DAB+ ; alternative souveraine aux solutions propriétaires de multiplexage numérique
- **Castopod** — Plateforme de podcasting open source (auto-hébergée) ; alternative à Spotify/Apple Podcasts pour diffuser des épisodes sur ses propres serveurs avec support ActivityPub (Fediverse)
- **Linux (support audio ALSA/JACK)** — Les studios radio peuvent fonctionner entièrement sous Linux avec un excellent support matériel pour les cartes son
- **DAB+ (Digital Audio Broadcast)** — Standard de diffusion radio numérique terrestre ; technologie de transition entre FM et Internet, avec des enjeux de gouvernance fréquentielle (ARCOM)

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- **Liquidsoap est écrit en OCaml** — Un langage fonctionnel rarement cité dans des contextes pratiques ; le fait qu'il soit utilisé jusqu'à Radio France pour sa robustesse est remarquable
- **700 radios associatives financées par l'État** en France via le FSER : c'est un service public de la diversité culturelle qui ne dit pas son nom, financé à plus de 80% par de l'argent public pour la plupart des radios
- Radio Campus Grenoble existe depuis **1994 et compte 5000 épisodes de podcasts en ligne** représentant 500 Go de données — le défi d'hébergement est réel et concret
- La **panne électrique en Espagne en 2025** : seule la radio nationale émettait encore, entraînant un regain d'intérêt pour les achats de récepteurs radio — argument de résilience des infrastructures analogiques face au tout-numérique
- Les récepteurs FM ont **disparu des smartphones** — une régression technologique qui pousse les radios à se battre pour exister sur Internet, où elles n'ont aucun avantage comparatif face aux géants du streaming
- L'ARCOM impose des **contraintes absurdes en DAB+** : couvrir jusqu'à Voiron depuis Grenoble, partager une fréquence avec des radios commerciales nationales aux intérêts divergents — un exemple de politique réglementaire mal adaptée aux réalités du terrain associatif
- Martin a développé seul l'automate de Radio Campus Grenoble et l'a rendu open source **"digne de ce nom"** après bientôt cinq ans d'usage interne — un exemple authentique de contribution communautaire issue de la pratique

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Martin Kirchgessner (Radio Campus Grenoble)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
