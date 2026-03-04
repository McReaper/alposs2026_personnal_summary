# AlpOSS 2026 - Partagez votre RAG sans partager vos données : l'IA mutualisée et souveraine

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Benjamin BELLAMY (Linagora), Andrzej NEUGEBAUER (Linagora) |
| **Organisation** | Linagora |
| **Durée** | 15 min (11:10–11:25) |
| **Présent** | ❌ Non |

## À propos des intervenants

**Benjamin BELLAMY** est Business Development Manager pour les solutions IA et Community Management chez Linagora. Il est impliqué dans la promotion et la diffusion des solutions d'IA open source de Linagora, notamment OpenRAG, auprès des communautés et des clients.

**Andrzej NEUGEBAUER** est AI Program Director chez Linagora et créateur d'OpenRAG, le framework RAG souverain et open source de Linagora. Fort de plus de 15 ans d'expérience, il accompagne entreprises et institutions dans leur transformation par l'IA. Il a notamment contribué au développement de LUCIE, modèle de langage compact, souverain et éthique pour la francophonie, avec la communauté OpenLLM France/Europe.

## Résumé

Ce talk présente OpenRAG, la solution de Retrieval-Augmented Generation (RAG) développée par Linagora, sous l'angle de la mutualisation souveraine. L'enjeu central : comment plusieurs organisations peuvent-elles partager une même infrastructure RAG sans pour autant exposer leurs données respectives ?

OpenRAG propose une architecture mutualisée permettant à plusieurs entités de bénéficier d'une infrastructure commune (modèles, pipelines de traitement documentaire, moteur de recherche vectorielle) tout en maintenant une séparation stricte entre les bases documentaires de chaque organisation. La solution repose sur une approche "privacy by design" et est entièrement open source (licence AGPL-3.0).

Parmi les caractéristiques techniques mises en avant :
- Agnosticisme LLM : compatibilité avec différents modèles de langage
- Parsing multimodal des documents (PDF, images, tableaux) via Marker
- Recherche vectorielle avec isolation par tenant via Milvus
- Scalabilité via Ray
- Compatibilité API OpenAI

Le positionnement est clairement orienté souveraineté numérique : une alternative open source aux stacks RAG propriétaires, déployable on-premise ou en cloud souverain.

> Note : Un autre talk sur une thématique RAG souverain (par des intervenants Scaleway) est présent dans les summaries. Celui-ci est spécifiquement porté par Linagora et met l'accent sur la mutualisation multi-organisations.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **OpenRAG** — framework RAG open source, modulaire et extensible, développé par Linagora (AGPL-3.0)
- **Milvus** — base de données vectorielle open source, utilisée pour la recherche sémantique avec isolation par tenant
- **Ray** — framework de calcul distribué pour la scalabilité des pipelines IA
- **Marker** — outil open source de parsing de documents (PDF, OCR, tableaux, images)
- **LUCIE** — LLM open source souverain pour la francophonie (OpenLLM France/Europe)
- **API OpenAI** — compatibilité API pour intégration avec des outils existants

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- La mutualisation RAG multi-organisations est un angle rarement abordé : partager l'infrastructure sans partager les données est un défi technique et organisationnel non trivial
- Linagora positionne OpenRAG comme une alternative souveraine aux solutions propriétaires (Azure OpenAI, Google Vertex AI...) déployable en environnement maîtrisé
- L'isolation des données par Milvus permet une segmentation fine par utilisateur, équipe ou organisation — un argument fort pour les marchés publics et les données sensibles
- LUCIE, le LLM francophone cité en contexte, est issu d'une démarche communautaire (OpenLLM France/Europe) — l'un des rares LLM open source ciblant la langue française
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Benjamin BELLAMY (Linagora), Andrzej NEUGEBAUER (Linagora)
- Page pretalx : https://pretalx.com/alposs-2026/talk/AZEW8Z/
