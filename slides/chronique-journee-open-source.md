# Chronique d'une journée dans le monde de l'Open Source

## Intervenant
Jérémy Tuloup · QuantStack

## Société
QuantStack est un studio open source parisien spécialisé dans l'écosystème scientifique et data, principalement autour de Jupyter. La société emploie des ingénieurs qui sont simultanément des mainteneurs actifs de projets open source majeurs (JupyterLab, JupyterLite, Voilà, xeus). Ce modèle de "studio open source" où le travail de maintenance communautaire est directement le produit livré est rare et constitue un exemple de business model durable autour de l'open source. QuantStack intervient pour des clients institutionnels et industriels nécessitant des environnements de calcul scientifique reproductibles et auditables.

## Résumé
Jérémy Tuloup retrace une journée type de mainteneur open source : CI cassée sans raison apparente, dépilage de notifications GitHub, réunions sans consensus, gestion des releases avec leurs tokens, secrets et changelogs. Les attaques de supply chain sur NPM sont devenues un risque opérationnel réel, forçant des patches en urgence. En 2026, le flux de PRs générées par IA déplace le bottleneck de la production de code vers la review humaine, dont la qualité est très inégale. Le facteur humain — désaccords, abandons, perte de financement — reste plus difficile à gérer que le technique.

## Points marquants
- La review de PRs IA est le nouveau bottleneck des mainteneurs.
- Attaques supply chain NPM : patches urgents désormais courants.
- GitHub en panne arrête des milliers de projets mondiaux.
- Une typo YAML a invalidé tout un pipeline de publication NPM.

## Technologies
- **JupyterLab / JupyterLite** — Environnements de notebooks interactifs, standards en data science et ML. JupyterLite fait tourner Jupyter entièrement dans le navigateur via WebAssembly, sans serveur backend — rupture architecturale majeure pour le déploiement d'environnements de calcul légers.
- **GitHub Actions** — Système de CI/CD intégré à GitHub. La dépendance à une plateforme centralisée crée un risque systémique : quand GitHub est indisponible, l'ensemble des pipelines s'arrête. Illustre la nécessité de plans de continuité même pour des outils d'infrastructure.
- **NPM / Trusted Publishers** — Registre JavaScript et mécanisme d'authentification OIDC pour la publication de paquets (sans tokens API longue durée). Pertinent pour les équipes DevSecOps cherchant à sécuriser leur chaîne de publication.
- **PyPI** — Registre Python, même enjeux de sécurité de la supply chain que NPM. La gestion des permissions de publication est un vecteur d'attaque documenté et actif.
- **Supply chain attacks** — Compromission de paquets open source populaires affectant les dépendances en cascade. Point de vigilance SSI critique pour toute organisation utilisant des dépendances open source sans audit régulier.
- **SemVer (Semantic Versioning)** — Convention de versionnage. Jérémy rappelle que le SemVer est un contrat moral, pas une garantie technique : des cassures d'API arrivent sur des versions mineures ou patch.
