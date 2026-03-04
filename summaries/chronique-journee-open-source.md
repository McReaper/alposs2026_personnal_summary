# AlpOSS 2026 - Chronique d'une journée dans le monde de l'Open Source

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Jérémy Tuloup |
| **Organisation** | QuantStack |
| **Durée** | 6:42 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Jérémy Tuloup est ingénieur logiciel chez **QuantStack**, studio open source parisien spécialisé dans l'écosystème scientifique et data (notamment l'écosystème Jupyter). Depuis environ sept ans, il est **mainteneur principal** sur plusieurs projets Jupyter : **JupyterLab**, **Jupyter Notebook**, **JupyterLite** (Jupyter dans le navigateur, sans serveur, basé sur WebAssembly). Il a débuté comme utilisateur de notebooks et est progressivement devenu mainteneur à temps plein — une trajectoire représentative de nombreux contributeurs actifs dans l'open source. Il est reconnu dans la communauté Python/Jupyter pour ses contributions sur les frontends Jupyter et l'outillage JavaScript/TypeScript associé.

## Résumé

En six minutes, Jérémy Tuloup offre une chronique fictive mais réaliste d'une journée type dans la vie d'un mainteneur open source. La forme est légère et humoristique, le fond est dense et instructif pour qui veut comprendre les coulisses de la maintenance de projets libres.

**Matin : le chaos ordinaire**
La journée commence par un café, puis par le dépouillement des notifications GitHub accumulées (nuit, semaine, vacances). On tente de coder, on pousse un changement — et la CI plante. Raison inconnue. On fouille d'autres dépôts, on découvre qu'un paquet est manquant, qu'une issue a déjà été ouverte par quelqu'un d'autre. On crée une branche locale de contournement, on pousse plusieurs fois en attendant que la CI passe. Résultat : « Je suis venu pour faire une feature, je suis resté parce que la CI était cassée. »

**Après-midi : le réel travail... entre deux réunions**
Un bloc de quelques heures de développement effectif s'intercale entre deux meetings. Le premier est interne : une discussion sur l'amélioration du launcher de JupyterLab (trop d'informations, interface brouillonne). Tout le monde est d'accord sur le problème, personne n'est d'accord sur la solution. Le statu quo s'impose. Ce type de discussion revient régulièrement pendant des mois, voire des années.

**La supply chain et les releases**
Jérémy aborde la gestion des dépendances : le versionnage sémantique n'est pas une garantie — des cassures arrivent sur des versions mineures ou patch. Il mentionne les attaques de supply chain récentes sur NPM (paquets JavaScript ciblés et compromis, affectant de nombreux dépôts). En tant que mainteneur, il faut être prêt à sortir des patches en urgence.

La gestion des releases implique : tokens d'accès, permissions, secrets, changelogs, tags, coordination multi-personnes. Il illustre avec un bug amusant : dans la configuration des **trusted publishers NPM** (nouveau mécanisme évitant la gestion de tokens API), un R majuscule au lieu d'un R minuscule dans un fichier YAML a invalidé toute la configuration — source de perte de temps absurde.

**L'IA s'invite**
En 2026, le flux de pull requests inclut de plus en plus de contributions générées ou assistées par IA. Le bottleneck se déplace : ce n'est plus la production de code, mais la **review**. La qualité est très inégale selon les modèles. La question « est-ce que je parle à un humain ou à un humain qui fait proxy avec un LLM ? » est désormais posée à chaque PR.

**La communauté et le facteur humain**
Des réunions communautaires hebdomadaires avec des contributeurs externes qui ne sont pas des collègues. Des désaccords sur la direction technique, des intérêts divergents, des gens qui partent, qui abandonnent, qui perdent leur financement. Pour Jérémy, le facteur humain est la partie la plus difficile — plus que le technique.

**En dehors des heures de travail**
Le triage des issues déborde sur le temps libre. Des fonctionnalités « que j'ai vraiment besoin d'utiliser » sont développées le soir ou pas du tout, faute de financement. La chaîne YouTube (référence humoristique à la procrastination) l'emporte parfois.

Il conclut : certains mainteneurs sont payés (son cas), beaucoup ne le sont pas. Tous accumulent une dette de burnout potentiel.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **JupyterLab / Jupyter Notebook** — Environnements de développement interactif (notebooks) utilisés massivement en data science, ML et recherche. Standard de l'industrie pour les missions d'analyse de données et de prototypage IA. À connaître pour les ESN intervenant sur des projets data/ML.
- **JupyterLite** — Version de Jupyter fonctionnant entièrement dans le navigateur (WebAssembly/Pyodide), sans serveur backend. Innovation majeure pour le déploiement d'environnements de calcul légers, pertinent pour des démonstrations ou formations sans infrastructure.
- **GitHub Actions (CI/CD)** — Système d'intégration et de déploiement continu. Jérémy illustre les limites de la dépendance à une plateforme centralisée : quand GitHub est down, tout s'arrête.
- **NPM / Trusted Publishers** — Registre JavaScript et nouveau mécanisme d'authentification OIDC pour les publications de paquets (évite les tokens API longue durée). Pertinent pour les équipes DevSecOps cherchant à sécuriser leur chaîne de publication.
- **PyPI (Python Package Index)** — Registre Python, mentionné en parallèle de NPM pour la gestion des publications et des tokens. Même enjeux de sécurité de la supply chain.
- **Supply chain attacks (attaques NPM)** — Compromission de paquets JavaScript populaires, affectant massivement l'écosystème. Point de vigilance SSI critique pour toute organisation utilisant des dépendances open source.
- **LLM / IA générative dans la contribution open source** — L'impact des IA sur les flux de contribution est déjà mesurable en 2026 : augmentation du volume de PR, baisse de la qualité moyenne, déplacement du bottleneck vers la review humaine. Sujet clé pour les ESN qui gèrent des projets open source.
- **Semantic versioning (SemVer)** — Convention de versionnage. Jérémy rappelle que le SemVer n'est qu'un contrat moral entre mainteneurs, pas une garantie technique — les cassures sur versions mineures sont réelles.

## Points marquants

- En 2026, la question de savoir si un contributeur open source est un humain ou un proxy LLM est posée sans ironie lors de la review de pull requests — un basculement majeur dans la dynamique des communautés open source.
- GitHub en panne = production à l'arrêt pour des milliers de projets open source mondiaux. La centralisation sur une seule plateforme (même si elle dispose d'une API standard Git) reste un risque systémique sous-estimé.
- Une typo (R majuscule vs R minuscule) dans un fichier de configuration CI a invalidé un mécanisme de publication de paquet NPM — illustration que la complexité des pipelines de release est devenue une source de bugs à part entière.
- Des attaques de supply chain récentes ont compromis des paquets NPM connus et populaires, affectant de nombreux projets en cascade. La sécurité de la chaîne d'approvisionnement logicielle est désormais un enjeu opérationnel pour tous les mainteneurs.
- JupyterLite (Jupyter dans le navigateur via WebAssembly) représente une rupture architecturale : plus besoin de serveur Python pour exécuter du code — un changement de paradigme pour la distribution d'environnements de calcul.
- Un mainteneur principal sur un projet utilisé par des millions de personnes peut très bien travailler le soir sur son temps libre sur des fonctionnalités faute de financement dédié : la fragilité structurelle de l'open source en un seul exemple.

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Jérémy Tuloup (QuantStack)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
