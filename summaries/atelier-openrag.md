# AlpOSS 2026 - Donnez une voix à vos documents avec OpenRAG

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Andrzej Neugebauer (Linagora) |
| **Organisation** | Linagora |
| **Format** | Atelier |
| **Durée** | ~1h (15:40–16:40) |
| **Présent** | ❌ Non |

## À propos de l'intervenant

Andrzej Neugebauer est AI Program Director chez Linagora, éditeur français de logiciels open source. Il est impliqué dans les projets d'IA souveraine portés par Linagora, notamment autour de LUCIE (modèle de langage open source francophone développé avec la communauté OpenLLM France/Europe) et d'OpenRAG. Il intervient régulièrement dans des conférences et forums autour des enjeux de l'IA ouverte et de la souveraineté numérique.

## Résumé

Cet atelier pratique présente **OpenRAG**, la solution RAG (*Retrieval-Augmented Generation*) open source développée par Linagora, sous licence AGPL-3.0. Les participants apprennent à ingérer leurs propres documents (PDF, DOCX, audio, images…) dans OpenRAG afin de les interroger en langage naturel via un modèle de langage.

OpenRAG se distingue par son caractère modulaire, léger et extensible : il supporte plusieurs LLM (Mistral, GPT-4, Claude…), propose une API compatible OpenAI, et peut s'intégrer à des outils existants comme LangChain, OpenWebUI ou N8N. L'ingestion est parallélisée via Ray pour gérer de grands volumes de documents. Le parsing avancé (Docling, Marker) gère les OCR, les mises en page complexes, les tableaux et les images.

L'atelier vise à permettre aux participants de déployer leur propre instance OpenRAG localement et de créer un premier pipeline RAG fonctionnel.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **OpenRAG** — Stack RAG open source (AGPL-3.0) de Linagora, modulaire et souverain, déployable on-premise ou sur Kubernetes
- **Ray** — Framework de calcul distribué pour paralléliser l'ingestion et l'embedding de documents
- **Docling / Marker** — Parseurs avancés de PDF avec support OCR, tableaux, mise en page complexe
- **BM25 + recherche sémantique** — Hybridation des modes de recherche pour améliorer la précision des réponses
- **API OpenAI-compatible** — Permet l'intégration dans des pipelines existants sans modification
- **LangChain / OpenWebUI / N8N** — Exemples d'outils compatibles pour orchestrer ou exposer le RAG
- **Kubernetes** — Cible de déploiement pour les charges de production distribuées

## Points marquants

- OpenRAG est 100 % open source (AGPL-3.0), souverain by design : les données et les modèles restent sous contrôle de l'organisation
- Supporte une grande variété de formats : PDF, DOCX, PPTX, audio (WAV, MP3, MP4…), images (PNG, JPEG, SVG)
- Compatibilité native avec l'API OpenAI : intégration sans friction dans les infrastructures existantes
- Conçu pour l'expérimentation avancée de techniques RAG (reformulation de requêtes, chunking contextuel, métadonnées enrichies)
- Linagora est également à l'origine de LUCIE, premier modèle de langage génératif 100 % open source pour l'Europe francophone

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Andrzej Neugebauer (Linagora)
- Page officielle : [https://pretalx.com/alposs-2026/talk/7SSRKX/](https://pretalx.com/alposs-2026/talk/7SSRKX/)
