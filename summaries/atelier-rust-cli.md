# AlpOSS 2026 - Découvrir Rust en 2h : construire un petit projet de CLI de A à Z

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | René Ribaud (Red Hat), Cyril Marin |
| **Organisation** | Red Hat |
| **Format** | Atelier |
| **Durée** | ~2h (15:40–17:40) |
| **Présent** | ❌ Non |

## À propos des intervenants

René Ribaud travaille chez Red Hat et est un développeur Rust expérimenté, connu dans la communauté sous le pseudonyme `uggla` (GitHub/DEV.to). Il a publié plusieurs tutoriels pratiques sur la création d'outils CLI en Rust, dont la série *"Ferris fetches Go gopher postcards"* et *"Ferris hunts errors"* sur DEV Community. Il est convaincu que le développement de programmes CLI est l'une des meilleures portes d'entrée pour apprendre Rust concrètement.

Cyril Marin co-anime l'atelier aux côtés de René Ribaud. ⚠️ Informations limitées sur son profil public.

## Résumé

Cet atelier de 2 heures est une initiation complète au langage Rust à travers la construction d'un outil en ligne de commande (CLI) de zéro. Les participants partent d'un projet vierge et arrivent à un programme fonctionnel, ce qui leur permet de toucher aux concepts fondamentaux du langage dans un contexte concret. L'atelier couvre les bases de Rust : le système d'ownership et de borrowing, le typage statique fort, la gestion des erreurs idiomatique, et l'organisation du code en modules. L'outillage Rust (Cargo, le gestionnaire de paquets et de build) est utilisé tout au long pour illustrer la maturité de l'écosystème. Le format est hands-on : chaque participant code sur sa machine et progresse étape par étape.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Rust** — Langage système open source (Mozilla/Rust Foundation) offrant sûreté mémoire sans garbage collector, très utilisé en sécurité et systèmes embarqués
- **Cargo** — Gestionnaire de paquets et outil de build officiel de Rust (compilation, tests, dépendances)
- **CLI (Command Line Interface)** — Paradigme de développement d'outils en ligne de commande, support natif dans Rust via des crates comme `clap`
- **clap** — Crate Rust populaire pour le parsing d'arguments CLI (très probablement utilisé dans l'atelier)
- **Red Hat Developer Toolset** — Distribution de Rust supportée dans RHEL pour les environnements entreprise

## Points marquants

- Rust est régulièrement élu langage "le plus apprécié" dans les sondages Stack Overflow depuis plusieurs années consécutives
- La sûreté mémoire garantie à la compilation fait de Rust un langage stratégique pour la cybersécurité (NSA, CISA et l'ENISA recommandent son adoption)
- Red Hat intègre Rust dans ses produits (coreutils, systemd components) — un signal fort pour les ESN travaillant avec des stacks Linux entreprise
- Un atelier de 2h est suffisant pour produire un vrai outil fonctionnel : faible barrière à l'entrée malgré la réputation austère du langage
- L'approche CLI-first est pédagogiquement efficace : pas de framework web ni d'interface graphique, le focus reste sur le langage lui-même

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : René Ribaud (Red Hat), Cyril Marin
- Page officielle : [https://pretalx.com/alposs-2026/talk/MCVPPT/](https://pretalx.com/alposs-2026/talk/MCVPPT/)
