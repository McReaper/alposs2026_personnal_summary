# Partagez votre RAG sans partager vos données : l'IA mutualisée et souveraine

## Intervenant
Benjamin Bellamy · Linagora
Andrzej Neugebauer · Linagora

## Société
Linagora est un éditeur et société de services français spécialisé dans les logiciels libres et l'open source. La société développe des solutions souveraines dans les domaines de la messagerie collaborative (LinShare, LinTo) et de l'intelligence artificielle (OpenRAG, LUCIE). Elle opère en France et à l'international, avec un positionnement fort sur la souveraineté numérique et le cloud souverain pour les entreprises et les institutions publiques.

## Résumé
OpenRAG est un framework RAG open source (AGPL-3.0) conçu pour être mutualisé entre plusieurs organisations sans mélanger leurs données. Chaque tenant dispose d'une base documentaire isolée sur une infrastructure partagée (LLM, vectorstore, pipelines). La solution est déployable on-premise ou en cloud souverain, avec une compatibilité API OpenAI pour l'intégration dans des stacks existantes.

## Points marquants
- RAG mutualisé : infra partagée, données cloisonnées par tenant
- Isolation vectorielle par organisation via Milvus
- Agnostique LLM, compatible API OpenAI
- LUCIE : LLM open source francophone communautaire

## Technologies
- **OpenRAG** — Framework RAG open source développé par Linagora (AGPL-3.0). Architecture modulaire permettant la mutualisation multi-organisations avec isolation stricte des données par tenant. Alternative souveraine aux stacks RAG propriétaires (Azure OpenAI, Google Vertex AI).
- **Milvus** — Base de données vectorielle open source utilisée pour la recherche sémantique. Supporte l'isolation des collections par tenant, ce qui est le mécanisme clé de la séparation des données dans OpenRAG.
- **Ray** — Framework de calcul distribué Python pour la scalabilité des pipelines IA. Utilisé dans OpenRAG pour paralléliser les traitements documentaires à grande échelle.
- **Marker** — Outil open source de parsing de documents : PDF, OCR, tableaux, images. Constitue la couche d'ingestion documentaire multimodale d'OpenRAG.
- **LUCIE** — Modèle de langage open source compact ciblant la langue française, développé dans le cadre de la communauté OpenLLM France/Europe. Exemple de LLM souverain utilisable avec OpenRAG sans dépendance à un fournisseur étranger.
