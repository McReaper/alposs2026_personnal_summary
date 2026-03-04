# AlpOSS 2026 - Linux sur les Mac : état des lieux du support matériel (Intel 2017-2020 et Apple Silicon)

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Walid Nouh |
| **Organisation** | Podcast Projets Libres / LinuxFr.org |
| **Durée** | 15 min (11:25–11:40) |
| **Présent** | ❌ Non |

## À propos de l'intervenant

Walid Nouh est un passionné de logiciel libre depuis l'an 2000, date à laquelle il a découvert le logiciel libre en terminant ses études d'informatique. Il a travaillé professionnellement comme développeur core de logiciels libres pendant 15 ans, ainsi que comme consultant.

Il est le créateur et animateur du podcast **Projets Libres !**, dédié à la découverte du logiciel libre sous toutes ses facettes : acteurs, modèles économiques, communautés. Le podcast est devenu le podcast officiel de **LinuxFr.org**, la référence francophone de l'information sur le logiciel libre.

Son profil GitHub ([wawax](https://github.com/wawax)) et son site Flickr témoignent d'une activité longue dans la communauté du libre. Il a également contribué à des conférences comme le Capitole du Libre.

## Résumé

⚠️ Informations limitées — résumé basé uniquement sur les informations disponibles via les sources publiques AlpOSS 2026.

Ce talk propose un état des lieux du support matériel de Linux sur les Mac, en distinguant deux générations de machines :

**Mac Intel (2017–2020) :** Ces machines embarquent souvent la puce de sécurité T2 (Apple T2), qui complexifie l'installation de Linux (Secure Boot propriétaire, contrôle du démarrage). Des solutions existent cependant pour y installer Linux, avec des degrés variables de support des périphériques (Wi-Fi, Touch Bar, suspension...).

**Apple Silicon (M1, M2, M3...) :** Depuis la transition d'Apple vers ses propres puces ARM (2020), Linux supporte progressivement ces architectures via le projet **Asahi Linux**, qui reverse-engineer le matériel Apple pour en assurer le support dans le noyau Linux mainline. En 2026, le support est partiel : le GPU, certains périphériques audio ou la gestion de l'énergie restent des sujets ouverts, notamment sur M3.

Ce talk vise probablement à faire le point sur l'état réel du support en 2026, les machines compatibles, les distributions utilisables, et les cas d'usage envisageables (reconditionner d'anciens Mac Intel sous Linux, utiliser Apple Silicon avec Linux).

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Asahi Linux** — projet de portage de Linux sur Apple Silicon (ARM), seule initiative majeure à reverser les drivers Apple vers le noyau mainline
- **Linux kernel** — noyau Linux, dont le support ARM/Apple Silicon progresse dans les versions récentes
- **Apple T2** — puce de sécurité présente dans les Mac Intel 2017–2020, impactant l'installation de Linux (Secure Boot propriétaire)
- **Apple Silicon (M1/M2/M3)** — architecture ARM propriétaire d'Apple, sujet central du portage Linux

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- Apple met fin au support logiciel de ses Mac Intel en 2025-2026, ce qui crée un stock important de machines puissantes potentiellement reconditionnables sous Linux — un enjeu écologique et budgétaire réel
- Asahi Linux est l'un des rares projets à reverse-engineer du matériel propriétaire aussi complexe et à contribuer ses drivers directement dans le noyau Linux mainline
- En janvier 2026, Asahi Linux annonçait un portage fonctionnel (mais encore limité) sur M3 — la progression est rapide mais le support GPU reste absent
- Le sujet intéresse directement les DSI et responsables IT qui cherchent à prolonger la vie de parcs de Mac en fin de support Apple
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Walid Nouh
- Page pretalx : https://pretalx.com/alposs-2026/talk/CMABAD/
