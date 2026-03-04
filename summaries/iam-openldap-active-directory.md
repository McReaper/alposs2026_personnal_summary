# AlpOSS 2026 - Des outils IAM Open Source pour OpenLDAP et Active Directory, votre RSSI vous dira merci !

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Clément Oudot |
| **Organisation** | Worteks |
| **Durée** | 20:43 |
| **Présent** | ✅ Oui |

## À propos de l'intervenant

Clément Oudot est expert IAM (Identity and Access Management) open source et directeur technique chez Worteks, société de services spécialisée dans l'intégration et le support de solutions open source d'infrastructure. Il est l'un des principaux contributeurs et mainteneurs de LemonLDAP::NG, le portail web SSO open source français de référence, ainsi que de plusieurs outils de la suite LDAP Toolbox (LSC, Service Desk, White Pages). Worteks accompagne les entreprises et collectivités dans la sortie des solutions propriétaires (VMware, Office 365, Okta, Entra ID) au profit de l'open source. Clément Oudot est connu dans la communauté pour allier expertise technique pointue et sens de la pédagogie — il n'hésite pas à débuter ses conférences en chanson.

## Résumé

Clément Oudot présente un tour d'horizon complet et pragmatique des outils IAM open source permettant de gérer des annuaires OpenLDAP et Active Directory, avec un fil conducteur : rendre ces environnements interopérables, sécurisés et auditables pour satisfaire les exigences d'un RSSI.

**Introduction à LDAP et ses acteurs :**
LDAP (Lightweight Directory Access Protocol), normalisé par l'IETF dans des dizaines de RFC, est l'équivalent de SQL pour les annuaires d'identités. Deux implémentations majeures coexistent :

- **OpenLDAP** : implémentation de référence, open source, hautement configurable, modulaire (politique de mots de passe, groupes dynamiques, clusters multi-maîtres). Worteks l'opère sur des annuaires allant de quelques entrées à plusieurs centaines de millions.
- **Active Directory** : annuaire Microsoft non standard (NTP, DNS, Kerberos + LDAP "propriétarisé"). Ses subtilités techniques posent des problèmes concrets : stockage de mots de passe non standard (inaccessible en lecture), pagination forcée à 1000 entrées (les clients non conformes ne récupèrent pas toutes les données), gestion des ranges sur les groupes à grande échelle, et un format de date absurde (intervalles de 100 nanosecondes depuis le 1er janvier 1601).

**Les outils de la suite Worteks/LDAP Toolbox :**

1. **LemonLDAP::NG** — Portail web SSO open source implémentant CAS, SAML 2.0 et OpenID Connect. Gère l'authentification multi-facteurs, les groupes récursifs AD, et la fédération d'identités. Compatible OpenLDAP et Active Directory nativement. Cas d'usage : portail d'entreprise pour authentification unique de toutes les applications.

2. **LSC (LDAP Synchronization Connector)** — Outil de synchronisation d'identités sans interface graphique, permettant de connecter n'importe quelle source (base de données RH, CSV, LDAP) à n'importe quelle destination (OpenLDAP, AD). Cas typique : approvisionnement automatique des comptes AD depuis une base RH, ou synchronisation OpenLDAP ↔ AD pour une migration progressive. Permet de rendre l'AD dépendant d'OpenLDAP comme source de vérité.

3. **LDAP Toolbox - Self Service Password** — Interface web de gestion autonome des mots de passe (changement, réinitialisation par mail/SMS) compatible OpenLDAP et AD. Évite le bricolage maison et répond à un besoin universel en helpdesk.

4. **LDAP Toolbox - White Pages** — Annuaire interne web avec affichage des fiches collaborateurs (photo, groupes, adresse géolocalisée sur carte). Permet de publier de façon contrôlée certaines données de l'annuaire auprès des utilisateurs.

5. **LDAP Toolbox - Service Desk** — Interface web de support niveau 1 pour gérer les comptes (statut, blocage, expiration) dans OpenLDAP ou AD. Supprime la nécessité de se connecter directement au serveur Windows. Tableau de bord des comptes expirés, désactivés, ou orphelins. Utilisé par la **ville d'Échirolles** (lieu de l'événement) sur son Active Directory, avec participation au financement de la R&D.

**Stratégie de sortie de Microsoft :** En Q&A, Clément Oudot décrit une stratégie de migration progressive : maintenir l'AD/Entra ID pour les outils Microsoft, déployer OpenLDAP + LemonLDAP::NG pour le reste, synchroniser les identités via LSC, puis migrer progressivement. Cette approche évite la "big bang migration" et réduit la dépendance à l'écosystème Microsoft pour les applications tierces.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **OpenLDAP** — Implémentation LDAP open source de référence (licence OpenLDAP Public License) ; haute disponibilité, multi-maître, extensible via modules (politique de mots de passe, groupes dynamiques, syncprov pour la réplication) ; pertinent pour toute architecture IAM souveraine
- **LemonLDAP::NG** — Portail SSO open source français (Perl/JavaScript, licence GPL) ; supporte CAS, SAML 2.0, OpenID Connect, MFA ; alternative directe à Okta, Azure AD B2C, Keycloak ; déployé dans de nombreuses collectivités et administrations françaises
- **LSC (LDAP Synchronization Connector)** — Outil de synchronisation d'identités open source (Java, licence GPL) ; connecteurs LDAP, SQL, CSV, REST ; indispensable pour les projets de provisioning automatique et de migration d'annuaires
- **LDAP Toolbox - Self Service Password** — Application PHP open source de gestion autonome des mots de passe ; compatible AD et OpenLDAP ; réduction du volume de tickets helpdesk de premier niveau
- **LDAP Toolbox - White Pages** — Application PHP open source d'annuaire interne ; affichage contrôlé des données collaborateurs incluant cartographie
- **LDAP Toolbox - Service Desk** — Application PHP open source d'administration LDAP pour le support niveau 1 ; tableau de bord des comptes expirés/bloqués ; compatible AD et OpenLDAP
- **Active Directory (Microsoft)** — Annuaire Microsoft propriétaire basé sur LDAP non standard ; omniprésent en entreprise ; les outils Worteks permettent de s'en affranchir progressivement ou d'en améliorer la gestion
- **Entra ID (ex Azure AD)** — Version cloud de l'Active Directory Microsoft ; la stratégie recommandée est la fédération avec un annuaire open source pour limiter la dépendance
- **SAML 2.0 / OpenID Connect / CAS** — Protocoles de fédération d'identités et SSO web ; bases de toute architecture IAM moderne interopérable
- **389 Directory Server (389DS) / FreeIPA** — Alternative open source à OpenLDAP portée par Red Hat ; FreeIPA propose une interface intégrée sur 389DS pour l'authentification centralisée Linux/Unix ; cité en Q&A comme outil complémentaire

## Points marquants

- La ville d'**Échirolles** (qui accueille AlpOSS) utilise elle-même LDAP Service Desk de Worteks sur son Active Directory et a **cofinancé des développements** sur ce logiciel — un exemple direct d'une collectivité locale contributrice à l'open source
- Active Directory encode ses dates en **intervalles de 100 nanosecondes depuis le 1er janvier 1601** — une bizarrerie technique historique qui oblige à des conversions dans tout outil s'interfaçant avec l'AD
- Certains clients de Worteks ont découvert via Service Desk qu'ils avaient **2000 comptes expirés** dans leur AD — illustration d'une hygiène de gestion des identités souvent négligée en entreprise, directement problématique d'un point de vue SSI
- Il est possible de **rendre Active Directory totalement dépendant d'OpenLDAP** : OpenLDAP devient la source de vérité et LSC pousse les changements vers l'AD — sans jamais toucher directement l'AD
- Clément Oudot a **chanté une chanson** pour introduire son talk sur LDAP — moment d'humour rare dans une conférence technique pointue
- LemonLDAP::NG implémente la **récursivité des groupes AD** avec gestion des cycles (groupe A membre de groupe B, groupe B membre de groupe A) — un bug classique qui plantait les serveurs en production avant la correction

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Clément Oudot (Worteks)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
