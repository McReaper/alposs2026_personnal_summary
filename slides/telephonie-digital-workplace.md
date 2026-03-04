# De l'outil isolé au composant central : la téléphonie dans la Digital Workplace

## Intervenant
Jehan Monnier et Pauline Perconte · Belledonne Communications

## Société
Belledonne Communications est une société grenobloise éditrice du projet open source Linphone, client et serveur SIP développé depuis 2001 et disponible sous double licence GPLv3 et commerciale. C'est l'un des acteurs de référence de la communication temps réel open source en Europe, avec une expertise approfondie sur les protocoles SIP, WebRTC et les architectures de téléphonie d'entreprise. Belledonne a participé à l'AMI France 2030 sur les suites souveraines collaboratives, contribuant la brique téléphonie au consortium Hexagone aux côtés de Bluemind, XWiki et Interstice. Ses clients sont principalement des entreprises et des collectivités cherchant à sortir de la dépendance à Microsoft Teams ou Cisco.

## Résumé
Microsoft détient 45 % du marché des Digital Workplaces et le Cloud Act américain permet aux autorités US d'accéder aux données hébergées par des éditeurs américains — l'affaire Karim Khan, dont les accès ont été coupés unilatéralement, l'illustre concrètement. Belledonne Communications intègre Linphone (SIP open source depuis 2001) dans des suites collaboratives via des standards ouverts : SIP, WebRTC, OpenID Connect, LDAP/CardDAV. La suite Hexagone, issue de l'AMI France 2030, associe Linphone, Bluemind, XWiki et Interstice pour offrir une alternative souveraine à M365. Linphone peut remplacer Teams Phone en drop-in, sans migration brutale, via un proxy OpenID Connect vers Active Directory.

## Points marquants
- Microsoft détient 45 % du marché des Digital Workplaces.
- Le Cloud Act permet la coupure unilatérale d'accès (cas Karim Khan).
- Linphone remplace Teams Phone sans migration brutale.
- Aucun acteur européen ne propose seul une intégration verticale complète.

## Technologies
- **Linphone** — Client et serveur SIP open source (GPLv3/commercial) développé depuis 2001 par Belledonne Communications. Alternative directe à Microsoft Teams Phone et Cisco, couvrant téléphonie SIP, messagerie instantanée et visioconférence. Intégrable à un Active Directory existant via proxy OpenID Connect.
- **Protocole SIP** — Standard de téléphonie IP le plus répandu, base de toute architecture de téléphonie d'entreprise moderne. Assure l'interopérabilité avec les opérateurs PSTN via SIP Trunk et entre systèmes hétérogènes.
- **WebRTC** — Standard W3C/IETF pour la communication temps réel dans le navigateur. Permet un client léger sans installation, pertinent pour les architectures zero-client et les accès BYOD sécurisés.
- **OpenID Connect / OIDC** — Protocole d'authentification fédérée (couche au-dessus d'OAuth 2.0), brique centrale du SSO dans les Digital Workplaces open source. Compatible avec Keycloak, LemonLDAP et Dex.
- **Suite Hexagone** — Consortium open source français (Linphone + Bluemind + XWiki + Interstice + Hotscale) issu de l'AMI France 2030. Exemple concret de Digital Workplace souveraine intégrée, répondant à l'appel d'offre Canopé de l'Éducation nationale.
- **Cloud Act** — Loi américaine permettant aux autorités US d'accéder aux données hébergées par des entreprises américaines, y compris en dehors des États-Unis. Argument central pour justifier la migration vers des solutions à hébergement maîtrisé.
