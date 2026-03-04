# AlpOSS 2026 - De l'outil isolé au composant central : la téléphonie dans la Digital Workplace

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Jehan Monnier et Pauline Perconte |
| **Organisation** | Belledonne Communications |
| **Durée** | 20:18 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

**Jehan Monnier** est co-fondateur de Belledonne Communications, société grenobloise éditrice du projet open source Linphone (rebaptisé "l'info" dans la transcription). Issu du monde de la téléphonie sur IP, il est l'un des acteurs de référence de la communication temps réel open source basée sur le protocole SIP en Europe. Il développe Linphone depuis 2001 et pilote les travaux d'intégration de la téléphonie dans les environnements numériques de travail souverains.

**Pauline Perconte** est chargée de communication et marketing chez Belledonne Communications. Elle co-anime cette présentation avec une approche orientée cas d'usage et adoption utilisateur.

## Résumé

Pauline Perconte et Jehan Monnier présentent la démarche de Belledonne Communications pour sortir la téléphonie de son isolement historique et en faire un composant central des environnements numériques de travail (Digital Workplace) open source.

**Contexte — le problème du vendor lock-in :** La présentation commence par un état des lieux du marché des Digital Workplaces. Microsoft détient 45 % des parts de marché (7 entreprises sur 10) avec Teams/M365. Ce monopole de fait pose plusieurs problèmes : impossibilité d'auditer ou corriger le code, dépendance unilatérale à l'éditeur (hausses de prix, changements de licence), et surtout une problématique de souveraineté numérique liée au Cloud Act américain. L'exemple du procureur de la Cour pénale internationale Karim Khan, dont les accès Microsoft ont été coupés suite à un litige avec l'administration Trump, illustre concrètement ce risque.

**La réponse open source :** Les intervenants exposent les avantages structurels de l'open source dans ce contexte : indépendance vis-à-vis de l'éditeur, possibilité de changer d'intégrateur sans changer d'outil, code auditable, hébergement maîtrisé, pas d'arrêt unilatéral des services.

**La téléphonie comme brique d'intégration :** Belledonne Communications, dont le projet phare est Linphone (logiciel SIP open source lancé en 2001), travaille à intégrer la téléphonie dans les suites collaboratives. L'approche repose sur des standards ouverts : SIP pour la téléphonie, LDAP/CardDAV pour les annuaires, OpenID Connect pour le SSO, WebRTC pour l'accès navigateur. L'objectif est qu'un utilisateur puisse passer un appel directement depuis sa suite collaborative (messagerie, annuaire, calendrier) sans changer d'outil.

Trois niveaux d'intégration sont présentés :
1. Bouton d'appel dans la fiche contact (URI handler vers le client lourd ou client léger WebRTC)
2. Dialer intégré pour composer un numéro externe
3. Historique des appels synchronisé avec l'annuaire et les fiches contacts

**France 2030 et l'appel à manifestation d'intérêt :** En 2023, Belledonne a répondu à l'appel à manifestation d'intérêt France 2030 sur les "suites souveraines collaboratives" en apportant la brique téléphonie. Résultat : la **suite Hexagone**, fruit d'un consortium open source associant Bluemind (messagerie), XWiki (wiki/documentation), Interstice (partage documentaire), le tout hébergé chez Hotscale. L'appel d'offre Canopé (centrale d'achat éducation nationale) est également cité comme vecteur de structuration du marché.

En Q&A, Jehan Monnier confirme que Linphone couvre téléphonie SIP, messagerie instantanée et visioconférence — périmètre comparable à Microsoft Teams — et peut s'intégrer à Active Directory via un proxy OpenID Connect.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Linphone (Belledonne Communications)** — Client et serveur SIP open source (licence GPLv3/commercial), depuis 2001 ; alternative directe à Microsoft Teams Phone et Cisco ; pertinent pour toute mission de téléphonie souveraine en entreprise ou collectivité
- **Protocole SIP** — Standard de téléphonie IP le plus répandu ; base de toute architecture de téléphonie d'entreprise moderne ; interopérabilité avec les opérateurs PSTN via SIP Trunk
- **WebRTC** — Standard W3C/IETF pour la communication temps réel dans le navigateur ; permet un client léger sans installation ; pertinent pour les architectures zero-client et les accès BYOD sécurisés
- **OpenID Connect / OIDC** — Protocole d'authentification fédérée (couche au-dessus d'OAuth 2.0) ; brique centrale du SSO dans les Digital Workplaces open source ; compatible avec KeyCloak, LemonLDAP, Dex
- **LDAP / CardDAV** — Standards d'annuaire et de carnet d'adresses ; assurent l'interopérabilité entre téléphonie, messagerie et suite bureautique
- **Suite Hexagone** — Consortium open source français (Linphone + Bluemind + XWiki + Interstice + Hotscale) issu de l'AMI France 2030 ; exemple concret de Digital Workplace souveraine et intégrée
- **Bluemind** — Solution open source de messagerie et calendrier d'entreprise ; intégrée à la suite Hexagone
- **XWiki** — Plateforme wiki open source d'entreprise ; intégrée à la suite Hexagone
- **Cloud Act** — Loi américaine permettant aux autorités US d'accéder aux données hébergées par des entreprises américaines y compris en dehors des USA ; argument central de la souveraineté numérique

## Points marquants

- Microsoft détient **45 % du marché des Digital Workplaces** (environ 7 entreprises sur 10) — un monopole de facto qui crée une dépendance structurelle
- L'affaire Karim Khan (procureur de la CPI) dont les accès Microsoft ont été **coupés unilatéralement** par l'administration Trump est citée comme cas concret du risque lié au Cloud Act — fait survenu en 2025
- Le projet Linphone a été lancé en **2001**, soit 23 ans avant cette conférence — l'un des plus anciens projets open source de communication temps réel encore actif et en développement
- L'appel à manifestation d'intérêt **France 2030** sur les suites souveraines collaboratives a structuré un écosystème de partenariats entre éditeurs open source français qui ne se connaissaient pas tous auparavant
- La téléphonie open source (Linphone) peut remplacer Microsoft Teams Phone **en drop-in**, en se connectant à un Active Directory existant via un proxy OpenID Connect — aucune migration brutale requise
- Il n'existe pas d'acteur européen capable de proposer une **intégration verticale complète** d'une Digital Workplace (comme Microsoft le fait) — d'où la nécessité de consortiums d'éditeurs open source complémentaires

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Jehan Monnier et Pauline Perconte (Belledonne Communications)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
