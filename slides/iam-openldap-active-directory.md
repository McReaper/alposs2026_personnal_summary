# Des outils IAM Open Source pour OpenLDAP et Active Directory, votre RSSI vous dira merci !

## Intervenant
Clément Oudot · Worteks

## Société
Worteks est une société de services spécialisée dans l'intégration et le support de solutions open source d'infrastructure, notamment IAM (Identity and Access Management). Elle accompagne entreprises et collectivités dans la sortie des solutions propriétaires (VMware, Office 365, Okta, Entra ID) au profit de l'open source. Worteks est l'un des principaux contributeurs et mainteneurs de LemonLDAP::NG, le portail SSO open source français de référence, ainsi que de la suite LDAP Toolbox (LSC, Service Desk, White Pages, Self Service Password). Elle opère des annuaires allant de quelques entrées à plusieurs centaines de millions.

## Résumé
Clément Oudot présente un tour d'horizon pragmatique des outils IAM open source pour gérer des annuaires OpenLDAP et Active Directory. La suite LDAP Toolbox couvre tous les besoins : SSO, synchronisation d'identités, gestion autonome des mots de passe, support niveau 1. Une stratégie de migration progressive permet de rendre Active Directory dépendant d'OpenLDAP comme source de vérité, sans big bang. La ville d'Échirolles, hôte de l'événement, utilise elle-même ces outils et en a cofinancé le développement.

## Points marquants
- Active Directory encode ses dates depuis le 1er janvier 1601.
- OpenLDAP peut devenir la source de vérité sur l'AD.
- 2000 comptes expirés découverts via Service Desk chez un client.
- Les tribunaux reconnaissent l'open source : Orange condamné à 1 M€.

## Technologies
- **OpenLDAP** — Implémentation LDAP open source de référence (licence OpenLDAP Public License) ; haute disponibilité, multi-maître, extensible via modules (politique de mots de passe, groupes dynamiques, réplication syncprov) ; base de toute architecture IAM souveraine.
- **LemonLDAP::NG** — Portail SSO open source français (Perl/JavaScript, licence GPL) ; supporte CAS, SAML 2.0, OpenID Connect et MFA ; alternative directe à Okta, Azure AD B2C et Keycloak ; déployé dans de nombreuses collectivités et administrations françaises.
- **LSC (LDAP Synchronization Connector)** — Outil de synchronisation d'identités open source (Java, GPL) ; connecteurs LDAP, SQL, CSV, REST ; indispensable pour le provisioning automatique et la migration d'annuaires, y compris OpenLDAP vers AD.
- **LDAP Toolbox - Self Service Password** — Application PHP open source de gestion autonome des mots de passe ; compatible AD et OpenLDAP ; réduit significativement le volume de tickets helpdesk de premier niveau.
- **LDAP Toolbox - Service Desk** — Interface web PHP pour le support niveau 1 : gestion des comptes, tableau de bord des comptes expirés ou bloqués ; compatible AD et OpenLDAP ; supprime la nécessité d'accès direct au serveur Windows.
- **SAML 2.0 / OpenID Connect / CAS** — Protocoles de fédération d'identités et SSO web ; bases de toute architecture IAM moderne interopérable entre applications hétérogènes.
