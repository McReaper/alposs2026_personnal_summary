# Logiciel libre et standards pour les noms de domaines

## Intervenant
Arthur Vuillard · LeBureau.coop

## Société
LeBureau.coop est une coopérative spécialisée dans la vente de noms de domaine avec l'ambition de devenir bureau d'enregistrement accrédité — un modèle alternatif rare dans un secteur dominé par des acteurs commerciaux. Arthur Vuillard en est le gérant, également à la tête de l'Agebank (DuPython, formation et services Python). Militant du logiciel libre et de l'économie sociale et solidaire, il développe le logiciel de gestion de domaines de la coopérative en Python/Django sous licence AGPL, garantissant la continuité de service même si la structure disparaissait.

## Résumé
Les registrars pratiquent l'enfermement via des API propriétaires et des interfaces dégradées ; Lexicon et OctoDNS permettent de gérer le DNS indépendamment du fournisseur. Il n'existe pas de standard ouvert côté titulaire — angle mort que la communauté n'a pas encore comblé.

## Points marquants
- Prix d'un domaine plus que doublé après rachat par un fonds.
- L'enshittification : bon marché, capture, captivité, hausse des prix.
- Absence de standard ouvert côté titulaire : angle mort réglementaire.
- Logiciel AGPL = continuité de service si la coopérative disparaît.

## Technologies
- **Lexicon** — Bibliothèque Python d'abstraction multi-fournisseurs pour la gestion DNS ; permet d'éviter le vendor lock-in dans les pipelines CI/CD ou IaC ; utile pour automatiser les challenges ACME/Let's Encrypt avec n'importe quel registrar.
- **OctoDNS** — Outil de gestion DNS-as-code compatible de nombreux providers ; adapté aux contextes d'infrastructure multi-cloud ou de migration DNS sans interruption de service.
- **PowerDNS** — Serveur DNS open source haute performance ; alternative souveraine à des solutions propriétaires ou cloud-dépendantes ; utilisé en production par LeBureau.coop avec PowerAdmin comme interface web.
- **DNS Update (RFC 2136)** — Standard IETF pour la mise à jour dynamique des enregistrements DNS ; pertinent pour l'automatisation des challenges ACME/Let's Encrypt (certificats TLS wildcard) ; deux ans se sont écoulés avant qu'un plugin Certbot soit disponible pour le registrar étudié.
- **Certbot / Let's Encrypt** — Solution de génération automatique de certificats TLS gratuits ; incontournable pour toute infrastructure web moderne ; son intégration dépend de la qualité des plugins tiers des registrars.
- **Django / Python (AGPL)** — Stack utilisée par LeBureau.coop pour son logiciel de gestion de domaines ; la licence AGPL garantit que le code reste libre même en cas de fork ou de vente de la structure.
