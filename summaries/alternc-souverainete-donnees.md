# AlpOSS 2026 - AlternC : Une solution pour gérer la souveraineté de ses données

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Camille LAFITTE (Webelys) |
| **Organisation** | Webelys |
| **Durée** | 15:00 |
| **Présent** | ❌ Non |

## À propos de l'intervenant

Camille Lafitte est développeur et militant du logiciel libre, fondateur et gérant de Webelys, hébergeur alternatif basé à Valaurie (Drôme). Il est l'un des principaux contributeurs et animateurs du projet AlternC depuis de nombreuses années : il participe à la maintenance du code, à l'animation de la communauté et au développement de l'écosystème. Webelys est l'un des rares hébergeurs professionnels à utiliser AlternC en production et à contribuer activement à son développement. Camille Lafitte est une figure reconnue de l'hébergement associatif et alternatif dans la communauté francophone du libre. Il a présenté AlternC à plusieurs éditions de l'AlpOSS, dont la version 3.5 en 2025.

## Résumé

⚠️ Informations limitées — résumé basé sur l'abstract pretalx et les informations disponibles publiquement sur AlternC et Webelys.

AlternC est un ensemble de logiciels libres (licence GPLv2+) conçu pour la gestion d'hébergements mutualisés. Né en 2000 après la fermeture de l'hébergeur gratuit Altern.org, le projet a pour vocation originelle de garantir l'indépendance et la liberté d'expression des internautes en favorisant l'hébergement alternatif — notamment associatif.

Dans cette présentation, Camille Lafitte expose comment AlternC constitue une réponse concrète à la question de la souveraineté des données. Le logiciel propose un panneau de contrôle web permettant à tout utilisateur, y compris sans compétences techniques, de gérer ses domaines, adresses e-mail, comptes FTP, statistiques de fréquentation et autres services d'hébergement. Cette interface volontairement accessible est complétée d'options avancées pour les utilisateurs expérimentés.

La présentation couvre probablement l'état actuel du projet (version 3.5, sortie début 2025), les avancées techniques récentes — notamment le remplacement de Courier par Dovecot pour le stockage des mails, et l'isolation des sites hébergés via des utilisateurs Unix distincts avec le module ITK d'Apache — ainsi que les perspectives d'évolution du projet. Webelys opère AlternC en production et contribue directement à son développement, aux côtés d'acteurs comme Octopuce, Neuronnexion, Globenet et l'Autre Net.

L'angle souveraineté est central : AlternC permet à des structures (associations, petites entreprises, hébergeurs militants) de proposer un hébergement maîtrisé, dont le code source est entièrement auditable et dont les données restent sous le contrôle de l'hébergeur et de ses utilisateurs, sans dépendance à un acteur commercial tiers.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **AlternC** — Panel d'administration d'hébergement mutualisé libre (GPLv2+) ; gestion de domaines, e-mails, FTP, statistiques ; alternative souveraine aux solutions propriétaires d'hébergement mutualisé ; utilisable par des hébergeurs alternatifs ou des collectivités voulant maîtriser leur infrastructure
- **Dovecot** — Serveur IMAP/POP3 open source haute performance ; utilisé dans AlternC comme backend de stockage des boîtes mail en remplacement de Courier ; référence pour les architectes messagerie
- **Apache HTTP Server (module ITK)** — Serveur web open source ; le module ITK permet d'isoler chaque site hébergé sous un utilisateur Unix distinct, renforçant la sécurité en cas de compromission d'un compte
- **GPLv2+** — Licence copyleft du projet AlternC ; garantit la liberté d'audit, de modification et de redistribution du code ; à intégrer dans les analyses de conformité licences des ESN

## Points marquants

- AlternC est né en 2000 en réaction directe à la fermeture d'Altern.org, dont la disparition avait mis hors ligne des milliers de sites d'associations et de particuliers — une leçon toujours actuelle sur la dépendance aux hébergeurs commerciaux
- Le projet est maintenu depuis plus de 25 ans exclusivement par des contributeurs bénévoles et des hébergeurs alternatifs, sans financement d'un grand éditeur logiciel
- La version 3.5, sortie début 2025, témoigne de la vitalité du projet malgré sa discrétion médiatique
- Webelys est l'un des seuls hébergeurs professionnels (non associatifs) à utiliser et cofinancer AlternC, illustrant qu'un modèle économique viable est possible autour du logiciel libre d'hébergement
- L'approche "interface non technique en premier" d'AlternC est une décision de conception délibérée, souvent oubliée dans les projets d'infrastructure : la souveraineté n'est réelle que si l'outil est utilisable sans compétence spécialisée

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Camille LAFITTE (Webelys)
- Page pretalx : [https://pretalx.com/alposs-2026/talk/WEDJJQ/](https://pretalx.com/alposs-2026/talk/WEDJJQ/)
