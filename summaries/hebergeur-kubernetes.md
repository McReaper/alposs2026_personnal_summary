# AlpOSS 2026 - Construire un hébergeur sur Kubernetes : Porté par l'Opensource, le YAML et un peu d'espoir

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Arthur MEYER (Agora Calycé) |
| **Organisation** | Agora Calycé |
| **Durée** | 15 min (créneau 14:45–15:00) |
| **Présent** | ❌ Non |

## À propos de l'intervenant

Arthur Meyer est CTO chez Agora Calycé, hébergeur français spécialisé dans les environnements cloud complexes (IaaS, PaaS). Avec une expertise étendue dans les écosystèmes cloud-native — réseaux, stockage, orchestration de conteneurs, développement — il intervient quotidiennement sur des projets d'infrastructure critiques. Fervent défenseur de l'open source, il contribue régulièrement à des projets Kubernetes et Cloud Native, et a participé à KubeCon North America 2025 à Atlanta. Agora Calycé dispose de quatre datacenters en France et propose notamment une distribution Kubernetes certifiée open source : Agorakube.

## Résumé

⚠️ Informations limitées — résumé basé sur les informations publiques disponibles, l'abstract pretalx n'étant pas accessible directement.

Le talk raconte le retour d'expérience d'Agora Calycé dans la construction d'une offre d'hébergement managé entièrement bâtie sur Kubernetes. Arthur Meyer partage les défis, les choix techniques et les leçons apprises lorsqu'on décide de faire de Kubernetes non plus un simple outil d'orchestration de conteneurs, mais la fondation complète d'un hébergeur : provisionnement, réseaux, stockage, monitoring, gestion multi-tenant.

Le titre — "Porté par l'Opensource, le YAML et un peu d'espoir" — signale un ton volontairement décalé et honnête : construire un hébergeur sur Kubernetes, c'est miser sur l'écosystème CNCF et une quantité industrielle de manifestes YAML, tout en composant avec la complexité inhérente à ces technologies.

La conférence aborde probablement : les choix d'outillage open source (Helm, Flux/ArgoCD, Cilium, Longhorn, etc.), la gestion du multi-tenant en contexte hébergeur, les opérateurs Kubernetes custom, et les enjeux d'exploitation en production d'une telle stack. Agora Calycé capitalise sur son projet open source Agorakube (distribution Kubernetes certifiée CNCF) comme brique de base.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Kubernetes** — orchestrateur de conteneurs, socle de toute l'infrastructure hébergeur
- **Agorakube** — distribution Kubernetes certifiée CNCF, open source, développée par Agora Calycé
- **Helm** — gestionnaire de packages Kubernetes (charts)
- **YAML** — format déclaratif omniprésent dans l'écosystème Kubernetes (manifestes, configs)
- **CNCF (Cloud Native Computing Foundation)** — fondation open source dont Kubernetes est le projet phare
- **GitOps** — pratique d'infrastructure as code pilotée par Git (ArgoCD, Flux)
- **Cilium** — plugin réseau CNI open source pour Kubernetes (eBPF)
- **Longhorn / Rook-Ceph** — solutions de stockage distribué open source pour Kubernetes

## Points marquants

> *Faits étonnants, atypiques ou d'actualité*

- Agora Calycé est un hébergeur français indépendant qui a choisi de construire toute sa plateforme sur Kubernetes open source, face à la domination des hyperscalers (AWS, Azure, GCP)
- Le projet Agorakube est une distribution Kubernetes certifiée par la CNCF, développée en open source — concurrente directe des distributions propriétaires comme Rancher ou OpenShift
- Utiliser Kubernetes comme fondation d'un hébergeur (et non juste pour orchestrer des apps) est une approche architecturale avancée et encore peu répandue chez les hébergeurs européens
- Le titre humoristique ("un peu d'espoir") reflète honnêtement la complexité et la charge opérationnelle de l'écosystème Kubernetes en production
- Agora Calycé a participé à KubeCon North America 2025 — présence dans les événements majeurs de la communauté CNCF mondiale

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Arthur MEYER (Agora Calycé)
- Page pretalx : https://pretalx.com/alposs-2026/talk/TRXQSU/
