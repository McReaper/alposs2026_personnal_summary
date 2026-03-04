# Chronique d'une journée dans le monde de l'Open Source

## Intervenant
Jérémy Tuloup · QuantStack

## Société
QuantStack est un studio open source parisien spécialisé dans l'écosystème scientifique et data, principalement autour de Jupyter. La société emploie des ingénieurs qui sont simultanément des mainteneurs actifs de projets open source majeurs (JupyterLab, JupyterLite, Voilà, xeus). Ce modèle de "studio open source" où le travail de maintenance communautaire est directement le produit livré est rare et constitue un exemple de business model durable autour de l'open source. QuantStack intervient pour des clients institutionnels et industriels nécessitant des environnements de calcul scientifique reproductibles et auditables.

## Résumé
Jérémy Tuloup retrace une journée type de mainteneur open source : CI cassée sans raison apparente, dépilage de notifications GitHub, réunions sans consensus, gestion des releases avec leurs tokens, secrets et changelogs. Les attaques de supply chain sur NPM sont devenues un risque opérationnel réel, forçant des patches en urgence. En 2026, le flux de PRs générées par IA déplace le bottleneck de la production de code vers la review humaine, dont la qualité est très inégale. Le facteur humain — désaccords, abandons, perte de financement — reste plus difficile à gérer que le technique.

## Points marquants
- En 2026, les LLM déplacent le goulot d'étranglement de la production vers la review.
  Le volume de pull requests a augmenté, mais leur qualité est très inégale selon les modèles utilisés. Les mainteneurs ne peuvent pas toujours savoir si un contributeur est un humain ou un proxy LLM, ce qui alourdit le travail de review.
- Des attaques supply chain ont compromis des paquets NPM connus.
  Des paquets JavaScript populaires ont été ciblés et compromis, affectant de nombreux dépôts en cascade. Les mainteneurs doivent être prêts à publier des patches correc­tifs en urgence, sans délai.
- Quand GitHub est en panne, des milliers de projets s'arrêtent simultanément.
  La centralisation de la CI/CD sur GitHub Actions crée un risque systémique : l'indisponibilité de la plateforme bloque l'ensemble des pipelines de l'écosystème, y compris les projets critiques.
- Une majuscule dans un fichier YAML a invalidé une publication NPM entière.
  Dans la configuration des Trusted Publishers NPM (mécanisme sans token API), un "R" majuscule au lieu d'un "r" minuscule a rendu la configuration inopérante. Illustration que la complexité des pipelines de release est devenue une source de bugs à part entière.
- Le facteur humain est plus difficile à gérer que les problèmes techniques.
  Désaccords sur la direction du projet, contributeurs qui partent ou perdent leur financement, intérêts divergents entre mainteneurs — ces situations reviennent sur des mois ou des années et ne se résolvent pas avec un patch.

## Technologies
- **JupyterLab / JupyterLite** — Environnements de notebooks interactifs, standards en data science et ML. JupyterLite fait tourner Jupyter entièrement dans le navigateur via WebAssembly, sans serveur backend — rupture architecturale majeure pour le déploiement d'environnements de calcul légers.
- **GitHub Actions** — Système de CI/CD intégré à GitHub. La dépendance à une plateforme centralisée crée un risque systémique : quand GitHub est indisponible, l'ensemble des pipelines s'arrête. Illustre la nécessité de plans de continuité même pour des outils d'infrastructure.
- **NPM / Trusted Publishers** — Registre JavaScript et mécanisme d'authentification OIDC pour la publication de paquets (sans tokens API longue durée). Pertinent pour les équipes DevSecOps cherchant à sécuriser leur chaîne de publication.
- **PyPI** — Registre Python, même enjeux de sécurité de la supply chain que NPM. La gestion des permissions de publication est un vecteur d'attaque documenté et actif.
- **Supply chain attacks** — Compromission de paquets open source populaires affectant les dépendances en cascade. Point de vigilance SSI critique pour toute organisation utilisant des dépendances open source sans audit régulier.
- **SemVer (Semantic Versioning)** — Convention de versionnage. Jérémy rappelle que le SemVer est un contrat moral, pas une garantie technique : des cassures d'API arrivent sur des versions mineures ou patch.
