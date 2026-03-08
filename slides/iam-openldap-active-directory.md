# Des outils IAM Open Source pour OpenLDAP et Active Directory, votre RSSI vous dira merci !

## Intervenant
Clément Oudot · Worteks

## Société
Worteks est une société de services spécialisée dans l'intégration et le support de solutions open source d'infrastructure, notamment IAM (Identity and Access Management). Elle accompagne entreprises et collectivités dans la sortie des solutions propriétaires (VMware, Office 365, Okta, Entra ID) au profit de l'open source. Worteks est l'un des principaux contributeurs et mainteneurs de LemonLDAP::NG, le portail SSO open source français de référence, ainsi que de la suite LDAP Toolbox (LSC, Service Desk, White Pages, Self Service Password). Elle opère des annuaires allant de quelques entrées à plusieurs centaines de millions.

## Résumé
LDAP Toolbox est une suite open source de gestion des identités (authentification unique, synchronisation, réinitialisation de mot de passe) comme alternative libre à Okta ou Microsoft Entra. La migration peut être progressive : les comptes sont synchronisés depuis un annuaire open source vers l'Active Directory existant, sans coupure brutale.

## Points marquants
- Active Directory encode ses dates en intervalles de 100 nanosecondes depuis 1601.
  L'epoch de référence est le 1er janvier 1601, héritage des systèmes Microsoft historiques. Tout outil s'interfaçant avec l'AD doit implémenter cette conversion, source fréquente de bugs lors de l'intégration.
- OpenLDAP peut devenir la source de vérité d'un Active Directory, sans big bang.
  Via LSC (LDAP Synchronization Connector), les changements sont poussés de OpenLDAP vers l'AD automatiquement. L'AD reste en place pour les outils Microsoft, mais n'est plus la source primaire des identités pour les applications tierces.
- Un client a découvert 2 000 comptes expirés dans son AD grâce à Service Desk.
  L'outil LDAP Toolbox Service Desk affiche un tableau de bord des comptes expirés, bloqués ou orphelins, sans accès direct au serveur Windows. Cette hygiène de gestion des identités est directement liée à la surface d'attaque SSI.
- La ville d'Échirolles utilise LDAP Service Desk et a cofinancé son développement.
  La collectivité hôte d'AlpOSS est elle-même cliente et contributrice financière de la suite LDAP Toolbox de Worteks — un exemple concret de collectivité locale qui finance l'open source qu'elle utilise.

## Technologies
- **OpenLDAP** — Implémentation LDAP open source de référence (licence OpenLDAP Public License) ; haute disponibilité, multi-maître, extensible via modules (politique de mots de passe, groupes dynamiques, réplication syncprov) ; base de toute architecture IAM souveraine.
- **LemonLDAP::NG** — Portail SSO open source français (Perl/JavaScript, licence GPL) ; supporte CAS, SAML 2.0, OpenID Connect et MFA ; alternative directe à Okta, Azure AD B2C et Keycloak ; déployé dans de nombreuses collectivités et administrations françaises.
- **LSC (LDAP Synchronization Connector)** — Outil de synchronisation d'identités open source (Java, GPL) ; connecteurs LDAP, SQL, CSV, REST ; indispensable pour le provisioning automatique et la migration d'annuaires, y compris OpenLDAP vers AD.
- **LDAP Toolbox - Self Service Password** — Application PHP open source de gestion autonome des mots de passe ; compatible AD et OpenLDAP ; réduit significativement le volume de tickets helpdesk de premier niveau.
- **LDAP Toolbox - Service Desk** — Interface web PHP pour le support niveau 1 : gestion des comptes, tableau de bord des comptes expirés ou bloqués ; compatible AD et OpenLDAP ; supprime la nécessité d'accès direct au serveur Windows.
- **SAML 2.0 / OpenID Connect / CAS** — Protocoles de fédération d'identités et SSO web ; bases de toute architecture IAM moderne interopérable entre applications hétérogènes.
