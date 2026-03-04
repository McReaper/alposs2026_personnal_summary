# AlpOSS 2026 - Démo en direct+Atelier: Une infra JupyterHub opérationnelle avec contenus en 1h grâce à WoD

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Bruno Cornec (Hyper-Linux.org) et Frédéric Passeron (HPE) |
| **Organisation** | Hyper-Linux.org / Hewlett Packard Enterprise (HPE) |
| **Format** | Démo en direct + Atelier |
| **Durée** | ~1h (09:30–10:30) |
| **Présent** | ❌ Non |

## À propos des intervenants

**Bruno Cornec** est un expert Linux et open source qui administre des systèmes Unix depuis 1987 et Linux depuis 1993. Ancien Open Source & Linux Technology Strategist chez HPE, il est aujourd'hui actif via Hyper-Linux.org. Il a contribué à de nombreux projets open source (MondoRescue, Mageia, FOSSology, python-redfish) et est l'un des mainteneurs principaux du projet Workshops-on-Demand. La version 1.0.2 de WoD a été publiée le 19 février 2026, deux jours après AlpOSS 2026.

**Frédéric Passeron** est Solution Architect dans le programme HPE Developer Community, basé à Grenoble. Il est co-créateur des Workshops-on-Demand chez HPE et a rédigé la série d'articles documentant l'open sourcing complet du projet. Il est l'un des principaux contributeurs à l'infrastructure JupyterHub de WoD.

## Résumé

Cet atelier combine une démonstration en direct et une mise en pratique autour de **WoD (Workshops-on-Demand)**, la plateforme open source d'HPE permettant de déployer une infrastructure JupyterHub complète — avec contenus (notebooks) — en environ une heure.

Les participants assistent au déploiement pas à pas d'un environnement WoD fonctionnel, comprenant les trois machines de l'infrastructure (frontend, API/base de données, backend JupyterHub), puis peuvent reproduire tout ou partie de la procédure. L'objectif est de repartir avec la capacité de proposer des ateliers techniques à la demande basés sur Jupyter Notebooks dans leur propre organisation.

WoD est entièrement open source depuis 2025 (5 dépôts publics sur GitHub), déployé via des scripts shell et des playbooks Ansible, et construit sur des technologies éprouvées (JupyterHub, PostgreSQL, Procmail, Fail2ban).

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **WoD (Workshops-on-Demand)** — Plateforme open source HPE pour délivrer des ateliers techniques à la demande via JupyterHub ; stable depuis la v1.0.2
- **JupyterHub** — Serveur multi-utilisateurs pour Jupyter Notebooks, colonne vertébrale de l'infrastructure WoD
- **Jupyter Notebooks** — Format de supports interactifs combinant code, texte et visualisations ; base des contenus pédagogiques
- **Ansible** — Outil d'automatisation utilisé pour les playbooks de déploiement de l'infrastructure WoD
- **PostgreSQL** — Base de données relationnelle utilisée par le service API de WoD (wod-api-db)
- **Fail2ban** — Protection contre les attaques par force brute sur le backend JupyterHub
- **GitHub / Workshops-on-Demand org** — Hébergement des 5 dépôts open source du projet

## Points marquants

- Infrastructure en 3 machines distinctes (frontend web, API+BDD, backend JupyterHub) : architecture claire et reproductible
- Déploiement complet en ~1 heure selon les auteurs — pertinent pour les organisations souhaitant monter des formations techniques rapidement
- 100 % open source depuis 2025, après avoir été développé en interne chez HPE depuis 2020
- Né pendant la pandémie pour remplacer les ateliers en présentiel, WoD est aujourd'hui utilisé hors contexte événementiel
- Frédéric Passeron est basé à Grenoble, ce qui ancre le projet dans l'écosystème local AlpOSS

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Bruno Cornec (Hyper-Linux.org), Frédéric Passeron (HPE)
- Page officielle : [https://pretalx.com/alposs-2026/talk/X9XHGW/](https://pretalx.com/alposs-2026/talk/X9XHGW/)
