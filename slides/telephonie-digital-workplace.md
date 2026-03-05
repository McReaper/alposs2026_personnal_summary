# De l'outil isolé au composant central : la téléphonie dans la Digital Workplace

## Intervenant
Jehan Monnier et Pauline Perconte · Belledonne Communications

## Société
Belledonne Communications est une société grenobloise éditrice du projet open source Linphone, client et serveur SIP développé depuis 2001 et disponible sous double licence GPLv3 et commerciale. C'est l'un des acteurs de référence de la communication temps réel open source en Europe, avec une expertise approfondie sur les protocoles SIP, WebRTC et les architectures de téléphonie d'entreprise. Belledonne a participé à l'AMI France 2030 sur les suites souveraines collaboratives, contribuant la brique téléphonie au consortium Hexagone aux côtés de Bluemind, XWiki et Interstice. Ses clients sont principalement des entreprises et des collectivités cherchant à sortir de la dépendance à Microsoft Teams ou Cisco.

## Résumé
Belledonne présente Linphone (SIP open source, 2001) comme alternative souveraine à Teams Phone, intégrable à un Active Directory existant sans migration brutale. Face à la domination de Microsoft (45 % du marché, Cloud Act), la suite Hexagone regroupe quatre éditeurs open source français pour couvrir l'ensemble d'une Digital Workplace.

## Points marquants
- Microsoft détient 45 % du marché des Digital Workplaces, soit 7 entreprises sur 10.
  Ce monopole de fait rend impossible l'audit du code, crée une dépendance unilatérale aux hausses de prix et de licence, et expose les données au Cloud Act américain.
- Le Cloud Act a permis la coupure unilatérale des accès de Karim Khan en 2025.
  Le procureur de la Cour pénale internationale a vu ses accès Microsoft coupés suite à un litige avec l'administration Trump. Cet exemple illustre concrètement le risque de dépendance à un éditeur soumis à la juridiction américaine.
- Linphone remplace Microsoft Teams Phone sans migration brutale.
  Linphone se connecte à un Active Directory existant via un proxy OpenID Connect, sans toucher l'infrastructure en place. Le projet est en développement actif depuis 2001 et couvre téléphonie SIP, messagerie instantanée et visioconférence.
- La suite Hexagone associe quatre éditeurs open source français issus de l'AMI France 2030.
  Le consortium réunit Linphone (Belledonne), Bluemind (messagerie), XWiki (wiki) et Interstice (partage documentaire), hébergés chez Hotscale. Il a notamment répondu à l'appel d'offre Canopé de l'Éducation nationale.
- Aucun acteur européen ne peut proposer seul une Digital Workplace complète.
  La fragmentation de l'offre européenne impose des consortiums d'éditeurs open source complémentaires, là où Microsoft fournit une intégration verticale unique. L'interopérabilité repose sur des standards ouverts : SIP, WebRTC, OpenID Connect, LDAP/CardDAV.

## Technologies
- **Linphone** — Client et serveur SIP open source (GPLv3/commercial) développé depuis 2001 par Belledonne Communications. Alternative directe à Microsoft Teams Phone et Cisco, couvrant téléphonie SIP, messagerie instantanée et visioconférence. Intégrable à un Active Directory existant via proxy OpenID Connect.
- **Protocole SIP** — Standard de téléphonie IP le plus répandu, base de toute architecture de téléphonie d'entreprise moderne. Assure l'interopérabilité avec les opérateurs PSTN via SIP Trunk et entre systèmes hétérogènes.
- **WebRTC** — Standard W3C/IETF pour la communication temps réel dans le navigateur. Permet un client léger sans installation, pertinent pour les architectures zero-client et les accès BYOD sécurisés.
- **OpenID Connect / OIDC** — Protocole d'authentification fédérée (couche au-dessus d'OAuth 2.0), brique centrale du SSO dans les Digital Workplaces open source. Compatible avec Keycloak, LemonLDAP et Dex.
- **Suite Hexagone** — Consortium open source français (Linphone + Bluemind + XWiki + Interstice + Hotscale) issu de l'AMI France 2030. Exemple concret de Digital Workplace souveraine intégrée, répondant à l'appel d'offre Canopé de l'Éducation nationale.
- **Cloud Act** — Loi américaine permettant aux autorités US d'accéder aux données hébergées par des entreprises américaines, y compris en dehors des États-Unis. Argument central pour justifier la migration vers des solutions à hébergement maîtrisé.
