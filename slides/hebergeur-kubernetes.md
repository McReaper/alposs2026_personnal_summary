# Construire un hébergeur sur Kubernetes : Porté par l'Opensource, le YAML et un peu d'espoir

## Intervenant
Arthur Meyer · Agora Calycé

## Société
Agora Calycé est un hébergeur français indépendant spécialisé dans les environnements cloud complexes (IaaS, PaaS), disposant de quatre datacenters en France. La société a développé Agorakube, une distribution Kubernetes certifiée CNCF entièrement open source, positionnée comme alternative aux distributions propriétaires (Rancher, OpenShift). Elle participe activement à la communauté CNCF mondiale, notamment via sa présence à KubeCon North America 2025 à Atlanta. Son CTO Arthur Meyer cumule expertise réseau, stockage, orchestration de conteneurs et développement cloud-native.

## Résumé
Agora Calycé a construit toute son offre d'hébergement managé sur Kubernetes — non pas comme outil d'orchestration d'applications, mais comme fondation complète de la plateforme hébergeur. Le talk couvre les choix d'outillage open source (CNCF stack), la gestion du multi-tenant, les opérateurs Kubernetes custom et les enjeux d'exploitation en production. Agorakube, leur distribution Kubernetes certifiée CNCF, sert de brique de base. Le titre décalé ("un peu d'espoir") reflète honnêtement la complexité opérationnelle de cette approche.

## Points marquants
- Agora Calycé a bâti toute sa plateforme d'hébergement sur Kubernetes, pas seulement ses applications.
  Kubernetes est utilisé ici comme fondation complète — provisionnement, réseaux, stockage, monitoring, multi-tenant — ce qui va bien au-delà de l'usage standard d'orchestration d'applications, encore peu répandu chez les hébergeurs européens.
- Agorakube est une distribution Kubernetes certifiée CNCF, entièrement open source.
  Développée par Agora Calycé, elle constitue une alternative auditable aux distributions propriétaires comme Red Hat OpenShift ou SUSE Rancher, avec une certification CNCF qui atteste de la conformité aux standards de l'industrie.
- La gestion du multi-tenant sur Kubernetes en contexte hébergeur pose des défis spécifiques.
  Isoler les clients, gérer les quotas de ressources et sécuriser les flux réseau entre tenants nécessite une maîtrise avancée des primitives Kubernetes et de la stack réseau (Cilium/eBPF).
- Agora Calycé s'appuie sur une stack de stockage distribué open source sans dépendance cloud.
  Longhorn et Rook-Ceph permettent de gérer des volumes persistants sur l'infrastructure propre de l'hébergeur, condition nécessaire pour proposer une offre souveraine indépendante des hyperscalers AWS, Azure et GCP.
- Agora Calycé a participé à KubeCon North America 2025 à Atlanta.
  Cette présence dans l'événement majeur de la communauté CNCF mondiale place l'hébergeur français dans le circuit des contributeurs actifs de l'écosystème Kubernetes.

## Technologies
- **Kubernetes** — Orchestrateur de conteneurs open source (CNCF), socle de toute l'infrastructure d'Agora Calycé. Utilisé ici non comme outil applicatif mais comme fondation d'un hébergeur complet : provisionnement, réseaux, stockage, monitoring, multi-tenant. Maîtrise indispensable pour tout consultant cloud-native.
- **Agorakube** — Distribution Kubernetes certifiée CNCF développée par Agora Calycé, entièrement open source. Alternative aux distributions propriétaires (Red Hat OpenShift, SUSE Rancher). Pertinent pour les ESN cherchant une base K8s souveraine et auditable pour leurs clients.
- **Helm** — Gestionnaire de packages Kubernetes (charts). Standard de facto pour le déploiement d'applications sur K8s ; incontournable pour tout projet cloud-native en ESN.
- **GitOps (ArgoCD / Flux)** — Pratique d'infrastructure as code pilotée par Git : l'état du cluster est défini dans des dépôts Git et réconcilié en continu. Apporte traçabilité, rollback et auditabilité — particulièrement pertinent pour les contextes réglementés.
- **Cilium** — Plugin réseau CNI open source pour Kubernetes, basé sur eBPF. Offre des capacités avancées de sécurité réseau, d'observabilité et de performance. Standard montant pour les clusters K8s en production.
- **Longhorn / Rook-Ceph** — Solutions de stockage distribué open source pour Kubernetes. Permettent de gérer des volumes persistants sans dépendre d'un cloud provider propriétaire — clé pour un hébergeur souverain.
- **CNCF (Cloud Native Computing Foundation)** — Fondation open source Linux hébergeant Kubernetes et l'ensemble de l'écosystème cloud-native (Prometheus, Envoy, Cilium, Helm…). La certification CNCF d'Agorakube atteste de la conformité aux standards de l'industrie.
