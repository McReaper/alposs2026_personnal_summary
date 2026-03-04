# Partagez votre RAG sans partager vos données : l'IA mutualisée et souveraine

## Intervenant
Benjamin Bellamy · Linagora

## Société
Linagora est une ESN française spécialisée en logiciels libres pour entreprises et administrations. Connue pour TWake (messagerie collaborative open source) et son engagement pour la souveraineté numérique. Intervient sur des projets RAG/IA on-premise pour DSI publiques et privées.

## Résumé
OpenRAG de Linagora adresse le problème de fond des LLM : l'hallucination, faute d'ancrage documentaire. Via une pipeline RAG multi-tenant, chaque organisation interroge un LLM commun sur ses propres documents, sans jamais exposer ses données aux autres tenants. L'API est 100 % compatible OpenAI, ce qui facilite l'intégration dans les stacks existants. Un POC se monte en demi-journée ; une solution industrielle scalable, c'est un tout autre chantier.

## Points marquants
- RAG leakage : fuite entre partitions = risque majeur des solutions mal architecturées
- Partitionnement étanche validé en production (communes Échirolles / Fontaine)
- Intégré nativement dans LibreOffice et Thunderbird via API OpenAI
- POC en demi-journée, mais industrialisation = projet à part entière

## Technologies
- **OpenRAG** — Framework RAG open source (AGPL-3.0), multi-tenant, agnostique LLM. Déployable on-premise ou cloud souverain. Alternative directe à Azure OpenAI Service et AWS Bedrock.
- **Milvus** — Base de données vectorielle open source, hautement scalable. Alternative souveraine à Pinecone ou Weaviate Cloud.
- **Ray** — Framework Python de calcul distribué pour scaler les pipelines ML/IA intensifs.
- **API OpenAI (standard)** — Format d'interopérabilité devenu standard de facto ; la compatibilité d'OpenRAG évite toute refonte des outils existants.
- **LLM open weight** — Modèles dont les poids sont publiés (Llama, Mistral) ; permettent un déploiement on-premise sans envoyer de données à des tiers.
