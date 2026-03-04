# AlpOSS 2026 - Logiciel libre et standards pour les noms de domaines

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Arthur Vuillard |
| **Organisation** | LeBureau.coop |
| **Durée** | 15:55 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Arthur Vuillard est gérant de deux coopératives : l'Agebank (connue pour DuPython, formation et services Python) et LeBureau.coop, une coopérative spécialisée dans la vente de noms de domaine avec l'ambition de devenir bureau d'enregistrement. Militant du logiciel libre et de l'économie sociale et solidaire, il s'intéresse aux enjeux de souveraineté numérique dans l'infrastructure Internet, notamment autour du DNS et des standards ouverts.

## Résumé

Arthur Vuillard ouvre sa présentation avec l'histoire fictive de Fiona, cliente d'un bureau d'enregistrement qu'il nomme "Bouddha", pour illustrer un phénomène réel : la **mérdification** (*enshittification*), concept popularisé par Cory Doctorow. De 2013 à aujourd'hui, le prix du renouvellement annuel d'un nom de domaine est passé de 12 euros à plus du double, après le rachat de l'entreprise par un fonds d'investissement.

Il identifie deux mécanismes d'enfermement propres aux bureaux d'enregistrement : l'**hébergement DNS propriétaire** (dont l'interface web se dégrade dans le temps) et les **API spécifiques** qui créent une dépendance forte. Il donne l'exemple de Certbot : le standard DNS Update (RFC 2136) était disponible dès juin 2017, mais le plugin pour Bouddha n'a été développé par une bénévole qu'en février 2019, bloquant deux ans les clientes souhaitant automatiser leurs certificats TLS wildcard.

Pour s'émanciper de cet enfermement, Arthur présente deux bibliothèques d'abstraction DNS : **Lexicon** et **OctoDNS**, qui permettent de gérer le DNS indépendamment du fournisseur. Il mentionne également le standard **EPP** (côté registre) et l'absence de standard équivalent côté titulaire/bureau d'enregistrement, pointant un vide normatif.

Pour éviter la mérdification en tant que client : fuir les entreprises qui passent de main en main et choisir des structures de l'économie sociale et solidaire où la voix du client compte. En tant que fournisseur : rester à l'écoute et ne pas vendre à des acteurs désintéressés des utilisateurs.

Il conclut sur le rôle du **logiciel libre comme facteur de résilience** : LeBureau.coop développe son propre outil de gestion de noms de domaine en Python/Django sous licence AGPL, ce qui garantit la continuité de service même si la coopérative venait à disparaître.

La session se termine par des questions : le service est ouvert aux particuliers et personnes morales. La pile technique utilisée comprend Debian, Bind, PowerDNS, PowerAdmin (PHP) et un logiciel interne Django/AGPL.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **DNS Update (RFC 2136)** — Standard IETF pour la mise à jour dynamique des enregistrements DNS ; pertinent pour l'automatisation des challenges ACME/Let's Encrypt (certificats TLS wildcard) en environnement client
- **Certbot / Let's Encrypt** — Solution de génération automatique de certificats TLS gratuits ; incontournable pour toute infrastructure web moderne
- **Lexicon** — Bibliothèque Python d'abstraction multi-fournisseurs pour la gestion DNS ; utile pour éviter le vendor lock-in dans les pipelines CI/CD ou IaC
- **OctoDNS** — Outil de gestion DNS-as-code compatible de nombreux providers ; adapté aux contextes d'infrastructure multi-cloud ou de migration sans interruption
- **EPP (Extensible Provisioning Protocol)** — Standard de communication entre bureaux d'enregistrement et registres ; pertinent pour les DSI gérant un parc de domaines important
- **PowerDNS** — Serveur DNS open source haute performance ; alternative souveraine à des solutions propriétaires ou cloud-dépendantes
- **Bind** — Serveur DNS de référence sous Unix/Linux ; utilisé dans de nombreuses infrastructures publiques et privées
- **PowerAdmin** — Interface web open source (PHP) d'administration pour PowerDNS
- **Django / Python (AGPL)** — Stack utilisée par LeBureau.coop pour son logiciel de gestion de domaines ; illustre l'approche de souveraineté par le logiciel libre

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- Le prix d'un nom de domaine chez le bureau d'enregistrement fictif "Bouddha" a **plus que doublé en deux ans** après un rachat par un fonds d'investissement — illustration concrète de l'*enshittification* décrite par Cory Doctorow
- La notion de **mérdification** (*enshittification*) est présentée en quatre étapes : service bon marché → capture des données → captivité des utilisateurs → hausse des prix et baisse de qualité ; un modèle de prédation numérique qui touche maintenant l'infrastructure critique comme le DNS
- Le plugin Certbot pour le bureau d'enregistrement en question a été développé **par une seule bénévole**, deux ans après la disponibilité du standard dans Certbot — soulignant la fragilité des écosystèmes propriétaires face aux standards ouverts
- **Absence de standard ouvert** côté titulaire/bureau d'enregistrement pour l'approvisionnement de noms de domaine : c'est un angle mort réglementaire que la communauté open source n'a pas encore comblé
- LeBureau.coop est une **coopérative** qui ambitionne de devenir bureau d'enregistrement accrédité — un modèle alternatif rare dans un secteur dominé par des acteurs commerciaux
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Arthur Vuillard (LeBureau.coop)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
