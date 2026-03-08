# Construire un hébergeur sur Kubernetes : Porté par l'Opensource, le YAML et un peu d'espoir

## Intervenant
Arthur Meyer · Agora Calycé

## Société
Agora Calycé (groupe E'nergys) est un hébergeur français indépendant spécialisé dans les environnements cloud complexes (IaaS, PaaS). Face au rachat de VMware par Broadcom en 2023, la société a lancé le projet Superphénix — une plateforme cloud complète construite sur Kubernetes et des outils 100 % open source, mise en production en janvier 2026 par une équipe de 4 personnes. Superphénix (SPX) sera publié en open source d'ici 2027.

## Résumé
En réponse au rachat de VMware par Broadcom, Agora Calycé a construit en 2 ans une plateforme cloud complète (IaaS + Kubernetes as a Service) en s'appuyant exclusivement sur Kubernetes et l'écosystème open source — KubeVirt pour la virtualisation, Kube-OVN pour le réseau, Rook/Ceph pour le stockage, Argo et Helm pour l'automatisation. Superphénix est en production depuis janvier 2026.

## Points marquants
- Le rachat Broadcom/VMware comme déclencheur.
  En novembre 2023, le rachat de VMware par Broadcom a conduit Agora Calycé à lancer le projet Superphénix en janvier 2024 : construire une alternative souveraine complète, sans dépendance éditeur, en 2 ans avec une équipe de 4 personnes.
- Kubernetes comme fondation d'un hébergeur complet, pas juste un orchestrateur.
  Kubernetes sert ici de socle pour la virtualisation (VMs), le stockage distribué, le réseau multi-tenant et la facturation — bien au-delà de son usage applicatif habituel. Choix retenu face à OpenStack, Proxmox et Nutanix pour son extensibilité et son écosystème 100 % open source.
- KubeVirt transforme Kubernetes en hyperviseur.
  KubeVirt permet de gérer des VMs comme des ressources Kubernetes natives, aux côtés des conteneurs — sans changer d'outil ni de paradigme opérationnel.
- 2 ans de développement, des dizaines de contributions open source.
  Superphénix n'est pas un assemblage clé-en-main : 2 ans de développement, des contributions actives aux projets upstream et une maintenance continue — avec une équipe de 4 personnes.
- SPX open sourcé d'ici 2027.
  La plateforme Superphénix sera publiée en open source d'ici 2027 — un engagement de contribution à l'écosystème dont elle est entièrement issue.

## Technologies
- **Kubernetes** — Orchestrateur de conteneurs open source (CNCF), fondation complète de Superphénix : virtualisation, réseau, stockage, automatisation. Retenu pour son extensibilité maximale et son écosystème 100 % open source, face à OpenStack, Proxmox et Nutanix.
- **KubeVirt** — Extension Kubernetes permettant de gérer des machines virtuelles comme des ressources K8s natives. Socle de la couche hyperviseur de Superphénix.
- **Kube-OVN** — Plugin réseau SDN (Software-Defined Networking) pour Kubernetes, basé sur OVN (Open Virtual Network). Gère l'isolation multi-tenant via un réseau overlay GENEVE, avec NAT gateway par tenant.
- **Rook / Ceph** — Rook est un opérateur Kubernetes qui pilote Ceph, système de stockage distribué open source. Ensemble, ils fournissent le stockage bloc et objet souverain de Superphénix sur des nœuds de stockage dédiés.
- **Argo (ArgoCD)** — Outil GitOps pour Kubernetes : l'état de la plateforme est défini dans Git et réconcilié en continu. Utilisé pour l'automatisation et le self-service de Superphénix.
- **Helm** — Gestionnaire de packages Kubernetes (charts). Assure l'extensibilité de la plateforme : chaque service supplémentaire (GitLab, Harbor, DBaaS…) s'ajoute comme un chart Helm.
- **Talos Linux** — Distribution Linux minimaliste et immuable, conçue spécifiquement pour faire tourner Kubernetes. Utilisée sur les nœuds de virtualisation et de stockage de Superphénix.
- **Superphénix (SPX)** — Plateforme cloud complète développée par Agora Calycé : IaaS (VMs, disques, réseau), Kubernetes as a Service, console web et GitOps. Open sourcé d'ici 2027.
