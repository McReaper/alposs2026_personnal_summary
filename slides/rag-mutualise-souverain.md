# Partagez votre RAG sans partager vos données : l'IA mutualisée et souveraine

## Intervenant
Benjamin Bellamy · Linagora

## Société
Linagora est une ESN française spécialisée en logiciels libres pour entreprises et administrations. Connue pour TWake (messagerie collaborative open source) et son engagement pour la souveraineté numérique. Intervient sur des projets RAG/IA on-premise pour DSI publiques et privées.

## Résumé
OpenRAG de Linagora adresse le problème de fond des LLM : l'hallucination, faute d'ancrage documentaire. Via une pipeline RAG multi-tenant, chaque organisation interroge un LLM commun sur ses propres documents, sans jamais exposer ses données aux autres tenants. L'API est 100 % compatible OpenAI, ce qui facilite l'intégration dans les stacks existants. Un POC se monte en demi-journée ; une solution industrielle scalable, c'est un tout autre chantier.

## Points marquants
- Les LLM ne comprennent pas ce qu'ils disent : ce sont des modèles probabilistes.
  Un LLM prédit le mot suivant à partir de statistiques sur ses données d'entraînement. Il n'a pas d'intention, pas de compréhension, et peut produire des réponses plausibles mais fausses — c'est le problème de l'hallucination que le RAG vise à réduire.
- L'IA est très politique : les biais viennent des données d'entraînement.
  Si le corpus d'entraînement est constitué exclusivement d'auteurs masculins, blancs, cisgenres de l'hémisphère nord, l'IA reproduira ces biais. Ce n'est pas un bug, c'est une conséquence directe de la conception du dataset.
- Le RAG leakage est le risque principal des solutions multi-tenant mal architecturées.
  OpenRAG garantit un partitionnement étanche par organisation : une même question posée sur la partition d'Échirolles et sur celle de Fontaine retourne des réponses différentes et sourcées, sans aucune fuite entre les deux contextes.
- OpenRAG est compatible avec l'API OpenAI et s'intègre dans LibreOffice et Thunderbird.
  La compatibilité 100 % OpenAI permet de brancher OpenRAG sur n'importe quel outil existant (WebUI, N8N, LibreOffice, Thunderbird) sans refonte de la stack. Le code source est intégralement public — pas d'open core, pas de fonctionnalités premium cachées.
- Un POC RAG se monte en demi-journée, mais une solution industrielle est un autre défi.
  Linagora identifie cinq défis majeurs pour industrialiser : partitionnement étanche, indexation scalable (Milvus + Ray), qualité de pipeline (MQR, contextualisation), intégration avec monitoring, et pipeline d'évaluation semi-automatique en production.

## Technologies
- **OpenRAG** — Framework RAG open source (AGPL-3.0), multi-tenant, agnostique LLM. Déployable on-premise ou cloud souverain. Alternative directe à Azure OpenAI Service et AWS Bedrock.
- **Milvus** — Base de données vectorielle open source, hautement scalable. Alternative souveraine à Pinecone ou Weaviate Cloud.
- **Ray** — Framework Python de calcul distribué pour scaler les pipelines ML/IA intensifs.
- **API OpenAI (standard)** — Format d'interopérabilité devenu standard de facto ; la compatibilité d'OpenRAG évite toute refonte des outils existants.
- **LLM open weight** — Modèles dont les poids sont publiés (Llama, Mistral) ; permettent un déploiement on-premise sans envoyer de données à des tiers.
