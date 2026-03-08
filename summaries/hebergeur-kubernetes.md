# AlpOSS 2026 - Construire un hébergeur sur Kubernetes : Porté par l'Opensource, le YAML et un peu d'espoir

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Arthur MEYER (Agora Calycé) |
| **Organisation** | Agora Calycé (groupe E'nergys) |
| **Durée** | 15 min (créneau 14:45–15:00) |
| **Présent** | ❌ Non |

## À propos de l'intervenant

Arthur Meyer est CTO chez Agora Calycé, hébergeur français membre du groupe E'nergys, spécialisé dans les environnements cloud complexes (IaaS, PaaS). Il a piloté le projet Superphénix de janvier 2024 à sa mise en production en janvier 2026, avec une équipe de 4 personnes. Fervent défenseur de l'open source, il s'est engagé à publier Superphénix (SPX) en open source d'ici 2027.

## Résumé

Ce talk raconte l'histoire du projet **Superphénix** : comment le rachat de VMware par Broadcom en novembre 2023 a conduit Agora Calycé à construire de zéro une plateforme cloud complète, souveraine, basée exclusivement sur Kubernetes et l'écosystème open source.

En deux ans, avec 4 personnes, l'équipe a construit une offre IaaS complète (VMs, disques, réseau) et un Kubernetes as a Service, en assemblant des briques open source : **KubeVirt** pour transformer Kubernetes en hyperviseur, **Kube-OVN** pour le réseau SDN multi-tenant, **Rook/Ceph** pour le stockage distribué, **Argo** pour le GitOps et **Helm** pour l'extensibilité. Le tout tourne sur **Talos Linux**, une distribution Linux minimaliste conçue pour Kubernetes.

La présentation est structurée comme un récit en étapes ("Étape 1 : transformer K8s en hyperviseur", "Étape 2 : faire tout le reste"...) avec un ton volontairement décalé — mèmes Yu-Gi-Oh, chouette difficile à dessiner — pour illustrer honnêtement la complexité de l'entreprise.

Superphénix est en production depuis janvier 2026. Il propose aujourd'hui une console web & GitOps, IaaS (VMs/disques/réseau) et Kubernetes as a Service. Des services SaaS (GitLab, Harbor), DBaaS (PostgreSQL, MongoDB) et GPU sont prévus prochainement. Le code sera open sourcé sous le nom SPX d'ici 2027.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Kubernetes** — Orchestrateur de conteneurs open source (CNCF), utilisé comme fondation complète de l'hébergeur : virtualisation, réseau, stockage, facturation. Retenu face à OpenStack, Proxmox et Nutanix pour son extensibilité et son caractère 100 % open source.
- **KubeVirt** — Extension Kubernetes permettant de gérer des VMs comme des ressources K8s natives. Socle de la couche hyperviseur de Superphénix.
- **Kube-OVN** — Plugin réseau SDN pour Kubernetes, basé sur OVN (Open Virtual Network). Gère l'isolation multi-tenant via un overlay réseau GENEVE, avec NAT gateway par tenant.
- **Rook** — Opérateur Kubernetes qui pilote Ceph. Orchestre le stockage distribué depuis Kubernetes.
- **Ceph** — Système de stockage distribué open source. Fournit le stockage bloc et objet souverain de Superphénix.
- **Argo (ArgoCD)** — Outil GitOps : l'état de la plateforme est défini dans Git et réconcilié en continu. Pilote l'automatisation et le self-service.
- **Helm** — Gestionnaire de packages Kubernetes (charts). Permet d'étendre la plateforme service par service (GitLab, Harbor, DBaaS…).
- **Talos Linux** — Distribution Linux immuable et minimaliste, conçue pour Kubernetes. Utilisée sur les nœuds de virtualisation et de stockage.
- **Superphénix (SPX)** — Plateforme cloud complète développée par Agora Calycé, open sourcée d'ici 2027.

## Points marquants

- **Le rachat Broadcom/VMware comme déclencheur direct** : en novembre 2023, Broadcom rachète VMware. Agora Calycé lance immédiatement le projet Superphénix pour s'affranchir de toute dépendance éditeur — un cas concret d'impact des consolidations du marché sur les hébergeurs indépendants.
- **Une plateforme cloud complète construite par 4 personnes en 2 ans** : de janvier 2024 à janvier 2026, en production. Ce rythme démontre la maturité de l'écosystème open source Kubernetes pour des usages avancés.
- **Kubernetes comme hyperviseur, pas comme orchestrateur d'apps** : KubeVirt permet de faire tourner des VMs dans Kubernetes, unifiant la gestion conteneurs et VMs sur une seule plateforme. Approche architecturale encore peu répandue chez les hébergeurs européens.
- **Engagement open source d'ici 2027** : SPX (Superphénix) sera publié en open source — contribution de retour à l'écosystème dont il est entièrement issu.
- **2 ans de développement, des dizaines de contributions upstream** : pas un simple assemblage de briques existantes, mais une contribution active aux projets open source utilisés.

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Arthur MEYER (Agora Calycé)
- Page pretalx : https://pretalx.com/alposs-2026/talk/TRXQSU/
- Slides PDF : disponibles sur pretalx (8,9 Mo)
