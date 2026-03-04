# AlpOSS 2026 - Partagez votre RAG sans partager vos données : l'IA mutualisée et souveraine

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Benjamin Bellamy et Andrzej Neugebauer |
| **Organisation** | Linagora |
| **Durée** | 16:55 |
| **Présent** | ❌ Non |

## À propos des intervenants

**Benjamin Bellamy** est responsable du développement commercial des offres IA chez Linagora. Linagora est une entreprise française spécialisée dans les logiciels libres pour les entreprises et administrations, connue notamment pour TWake (messagerie collaborative open source) et son engagement fort pour la souveraineté numérique.

**Andrzej Neugebauer** est responsable de l'offre LinaGraph au sein de Linagora, côté technique. Il est notamment en charge du développement d'OpenRAG, la solution RAG souveraine et open source de Linagora.

Ensemble, ils forment le binôme commercial/technique présentant la vision et l'implémentation d'une IA mutualisée et souveraine pour les organisations.

## Résumé

Benjamin Bellamy et Andrzej Neugebauer (Linagora) présentent alternativement leur approche de l'IA souveraine à travers le prisme du **RAG (Retrieval Augmented Generation)**.

Benjamin introduit d'abord les bases des **LLM (Large Language Models)** : ce sont des modèles probabilistes qui prédisent le mot suivant à partir de données d'entraînement — pas de compréhension, pas d'intention, que des statistiques. Il insiste sur le caractère politique de l'IA : le choix des données d'entraînement reflète une vision du monde. Un corpus biaisé (auteurs exclusivement masculins, hémisphère nord, cisgenres) produit une IA biaisée — ce n'est pas un bug, c'est une conception.

Le problème central des LLM seuls : l'**hallucination** — des réponses plausibles mais potentiellement fausses, sans traçabilité. C'est pourquoi le RAG est présenté comme la solution d'industrialisation :

1. L'utilisateur pose une question
2. La question est **vectorisée**
3. Les morceaux de documents sémantiquement proches sont récupérés dans une **base de connaissances**
4. Ces morceaux sont injectés dans le **prompt du LLM** (augmentation)
5. Le LLM génère une réponse ancrée dans les documents, avec **citation des sources**

Andrzej détaille ensuite **OpenRAG**, la solution 100% open source de Linagora :
- **Agnosticisme LLM** : compatible avec tout modèle (open source, open weight ou propriétaire)
- **Pipeline multimodale** : traite PDF, audio, DOCX, images
- **Scalabilité** : basée sur la base vectorielle **Milvus** et le framework de distribution **Ray**
- **Compatibilité OpenAI** : les API sont 100% compatibles OpenAI, facilitant l'intégration dans n'importe quel DSI (WebUI, N8N, LibreOffice, Thunderbird...)
- **Partitionnement étanche** : cloisonnement strict des données par organisation/service, garantissant qu'aucune fuite de données ne se produit entre partitions
- **Pipeline d'évaluation semi-automatique** pour mesurer la qualité en production

La démo montre concrètement des partitions étanches dédiées à des communes (Échirolles, Fontaine) : la même question sur la localisation de la mairie retourne des réponses différentes et sourcées selon la partition active. La solution est intégrée à LibreOffice et Thunderbird via l'API OpenAI.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **RAG (Retrieval Augmented Generation)** — Architecture de référence pour industrialiser l'IA générative en entreprise ; permet de brancher un LLM sur une base documentaire interne tout en gardant le contrôle des données
- **OpenRAG (Linagora)** — Solution RAG 100% open source, souveraine, agnostique LLM ; alternative aux offres Azure OpenAI ou AWS Bedrock pour les organisations souhaitant garder leurs données on-premise
- **Milvus** — Base de données vectorielle open source, hautement scalable ; alternative souveraine à Pinecone ou Weaviate Cloud pour le stockage des embeddings
- **Ray** — Framework Python de calcul distribué ; permet de scaler horizontalement et verticalement des pipelines ML/IA intensives
- **Multi-Query Retrieval (MQR)** — Technique avancée de retrieval améliorant la qualité des réponses RAG ; pertinente pour les projets d'IA en production
- **Embeddings / Rankers open source** — Composants clés de la pipeline RAG pour la vectorisation et le classement des documents ; Linagora sélectionne les meilleurs modèles open source
- **API OpenAI (standard de facto)** — Format d'API devenu standard d'interopérabilité ; la compatibilité OpenAI d'OpenRAG facilite l'intégration sans refonte des outils existants
- **N8N** — Outil d'automatisation de workflows open source ; cité comme exemple d'intégration avec OpenRAG via l'API compatible OpenAI
- **LLM open weight** — Modèles de langage dont les poids sont publiés (ex. Llama, Mistral) ; permettent un déploiement on-premise souverain sans envoyer de données à des tiers
- **NLP (Natural Language Processing)** — Domaine technique de base de tout système RAG ; compétence critique pour les équipes IA en ESN

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- **"L'IA est très, très politique"** : Benjamin Bellamy affirme sans détour que le choix des datasets d'entraînement reflète une vision du monde — un propos rarement tenu avec autant de franchise dans un cadre commercial
- Les LLM **ne comprennent pas ce qu'ils disent** : ils construisent des phrases probables, pas des idées — une démystification pédagogique claire, à rebours du marketing habituel autour de l'IA
- OpenRAG est qualifié de **"vrai open source"**, par opposition à l'open core (noyau libre, fonctionnalités avancées payantes) : code source intégralement public, sans feature premium cachée
- La solution est déjà **intégrée à LibreOffice et Thunderbird** via l'API compatible OpenAI — preuve d'une interopérabilité concrète avec la suite bureautique libre la plus répandue
- Le **RAG leakage** (fuite de données entre partitions) est identifié comme un risque majeur des solutions RAG mal architecturées ; Linagora revendique un partitionnement étanche comme différenciateur
- Un POC RAG peut se faire en **demi-journée**, mais une solution industrielle scalable est un tout autre défi — mise en garde pertinente face aux promesses marketing des intégrateurs
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Benjamin Bellamy et Andrzej Neugebauer (Linagora)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
