# AlpOSS 2026 - Sécurisez vos données avec les clés de sécurité OpenPGP (YubiKey, NitroKey).

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Jean-Jacques Brucker (foopgp) et Sébastien Picardeau (piseb) |
| **Organisation** | foopgp / piseb |
| **Format** | Atelier |
| **Durée** | ~1h (10:30–11:30) |
| **Présent** | ❌ Non |

## À propos des intervenants

**Jean-Jacques Brucker** est développeur au sein de l'association **foopgp** (Friends of OpenPGP), dont il est l'un des membres fondateurs actifs. Il est l'auteur de **pgpid**, un outil open source (hébergé sur Codeberg) permettant de générer des secrets OpenPGP sur plusieurs QR codes (schéma de partage de secret physique) puis de les transférer vers une smartcard OpenPGP (YubiKey, NitroKey…). Il contribue régulièrement à la documentation et aux articles techniques de foopgp sur les standards OpenPGP et l'identité numérique.

**Sébastien Picardeau** intervient sous le pseudonyme/organisation **piseb**. ⚠️ Les informations publiques disponibles sur cet intervenant sont limitées.

## Résumé

Cet atelier pratique aborde la sécurisation des données personnelles et professionnelles à l'aide des **clés de sécurité matérielles** compatibles OpenPGP, en particulier la **YubiKey** et la **NitroKey**.

Les participants apprennent les principes fondamentaux de la cryptographie OpenPGP appliquée à la signature, au chiffrement et à l'authentification, puis découvrent comment stocker leurs clés privées sur un token matériel afin que celles-ci ne quittent jamais le périphérique. L'atelier couvre probablement le processus complet : génération des clés (maître + sous-clés), sauvegarde physique sécurisée (via l'outil pgpid de foopgp, basé sur des QR codes et un schéma de partage de secret), et transfert vers la smartcard.

⚠️ Informations limitées : le descriptif officiel de l'atelier n'a pas pu être récupéré directement depuis la page pretalx. Le contenu ci-dessus est reconstruit à partir des activités connues de foopgp et des outils développés par Jean-Jacques Brucker.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **OpenPGP (RFC 4880)** — Standard de chiffrement et signature asymétrique ; base de la cryptographie utilisée dans cet atelier
- **GnuPG (GPG)** — Implémentation libre d'OpenPGP, utilisée pour la gestion des clés et les opérations cryptographiques
- **YubiKey** — Token matériel (Yubico) supportant l'applet OpenPGP ; les clés privées ne quittent jamais le périphérique
- **NitroKey** — Alternative open source matérielle à la YubiKey, supportant OpenPGP ; particulièrement appréciée dans les contextes souverains
- **pgpid (foopgp)** — Outil open source générant les secrets OpenPGP sur plusieurs QR codes (partage de secret physique), puis les transférant vers une smartcard
- **Codeberg** — Forge open source hébergeant le dépôt foopgp/pgpid

## Points marquants

- La protection matérielle garantit que la clé privée ne peut pas être extraite même si l'ordinateur hôte est compromis : argument fort pour les contextes SSI sensibles
- foopgp milite pour la démocratisation d'OpenPGP : l'association vise à rendre ces technologies accessibles au-delà des cercles d'experts
- L'outil pgpid apporte une approche originale de la sauvegarde de clés : partage de secret physique sur QR codes imprimables, compatible avec une gestion hors ligne
- YubiKey et NitroKey couvrent des besoins complémentaires : NitroKey est entièrement open source (hardware et firmware), ce qui peut être déterminant pour des organisations attachées à la transparence
- Pertinent pour les ESN/SSI intervenant sur des projets nécessitant signature de commits, chiffrement de fichiers sensibles ou authentification SSH renforcée

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Jean-Jacques Brucker (foopgp), Sébastien Picardeau (piseb)
- Page officielle : [https://pretalx.com/alposs-2026/talk/KTNMTA/](https://pretalx.com/alposs-2026/talk/KTNMTA/)
