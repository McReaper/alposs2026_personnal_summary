# AlpOSS 2026 - Déploiement de la messagerie OpenXchange au SITPI : RETEX de la migration de la ville de Claix

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Fayçal Braiki (SITPI), Christophe Ninucci (DINUM), Yoann Dupont (Alma), Baptiste Danielewicz (Ville de Claix), Nicolas Ecarnot (SITPI) |
| **Organisation** | SITPI, DINUM, Alma, Ville de Claix |
| **Durée** | 20:08 |
| **Présent** | ✅ Oui |

## À propos des intervenants

**Fayçal Braiki** est directeur du SITPI (Syndicat Intercommunal des Technologies et des Plateformes d'Information), structure de mutualisation des systèmes d'information regroupant dix communes de l'agglomération grenobloise, représentant environ 140 000 habitants. Il pilote la stratégie de souveraineté numérique du syndicat et conduit les projets de migration vers des solutions libres.

**Christophe Ninucci** est directeur de projet messagerie à la DINUM (Direction Interministérielle du Numérique). Il pilote le déploiement d'OpenXchange pour les administrations publiques françaises et contribue activement au dépôt open source de l'outillage de déploiement (DevOps, Ansible, OpenTofu).

**Yoann Dupont** est consultant chez Alma, prestataire spécialisé dans l'accompagnement des collectivités pour la migration vers OpenXchange. Il a géré la partie technique de la migration des données (IMAP, CalDAV, CardDAV).

**Baptiste Danielewicz** est le DSI (ou représentant SI) de la Ville de Claix, commune membre du SITPI, qui a conduit la migration des 200 comptes de messagerie de sa collectivité vers OpenXchange.

## Résumé

La présentation se déroule sous forme de RETEX à plusieurs voix, avec une succession de cinq intervenants couvrant chacun un aspect du projet.

**Fayçal Braiki (SITPI)** ouvre la présentation en rappelant le contexte : la fin annoncée du support Microsoft Exchange a déclenché une réflexion collective au sein du SITPI dès 2024. Un groupe de travail inter-communes a été constitué, avec une nouveauté méthodologique importante : la participation des utilisateurs finaux au benchmark, et non pas seulement des DSI. Six solutions ont été évaluées sur une heure de démonstration chacune, où 90 à 95 % du temps était consacré à l'ergonomie utilisateur. OpenXchange, soutenu par la DINUM, a été retenu car il a été plébiscité en premier choix par les utilisateurs pour son interface. Au moment du lancement, l'écosystème de prestataires autour d'OpenXchange était quasi inexistant ; Alma était l'un des premiers acteurs à proposer cet accompagnement.

**Christophe Ninucci (DINUM)** présente les forces fonctionnelles d'OpenXchange : webmail sans installation, gestion fine des mails (filtres, catégories, indexation), agenda partagé, contacts collaboratifs. Il décrit l'outillage DevOps développé par la DINUM : **OpenTofu** (fork libre de Terraform) pour le provisioning d'infrastructure multi-provider, et **Ansible** pour la configuration et la maintenance en conditions opérationnelles (MCO). L'ensemble est publié en licence GPLv3 sur un dépôt public. Il précise que l'objectif est de simplifier l'exploitation d'une plateforme mail complexe (Postfix, etc.) pour des équipes dont ce n'est pas la spécialité principale.

**Yoann Dupont (Alma)** prend ensuite la parole pour détailler la migration technique depuis Exchange. Il évoque deux grandes phases : (1) comprendre l'usage Exchange existant pour le reproduire fidèlement sur OpenXchange, en collaboration avec la Ville de Claix et la DINUM ; (2) la migration effective des données via des outils de synchronisation IMAP et des protocoles standards CalDAV/CardDAV pour les calendriers et contacts. Le provisioning a été réalisé manuellement (sans OpenTofu) via Ansible seul.

**Baptiste Danielewicz (Ville de Claix)** détaille l'approche conduite côté collectivité. La migration des 200 comptes de messagerie s'est globalement bien passée. La migration des événements de calendrier a été plus laborieuse mais s'est terminée positivement, notamment grâce à Carbonio (fork de Zimbra basé sur des formats ouverts) comme pivot. La migration des smartphones a été traitée comme un sous-projet indépendant, avec un calendrier et une gestion d'astreinte dédiés. La solution retenue est un écosystème 100 % libre : **F-Droid** comme magasin d'applications Android, **DAVx5** pour la synchronisation CalDAV/CardDAV, **Fossify Calendar** pour le calendrier, et **K-9 Mail** pour la messagerie. La bascule a eu lieu un mardi soir pour une mise en production le mercredi — stratégie délibérée évitant le vendredi (*Never on Friday*).

**En conclusion**, Baptiste insiste sur les clés du succès : démarche inclusive (utilisateurs autour de la table dès le départ), accent assumé sur la souveraineté numérique, adhésion des élus, et analyse partagée des besoins. L'objectif secondaire affiché est de sortir d'Office et de passer intégralement sur une suite bureautique libre. D'autres communes du SITPI rejoindront la plateforme mi-2026.

Lors des questions, un participant belge demande si l'infrastructure pourrait monter à 150 000 enseignants et 1,5 million d'élèves. Christophe Ninucci répond que la DINUM vise des infrastructures à 100 000 comptes mais n'est pas encore mature pour un déploiement à plusieurs millions.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **OpenXchange** — Suite de messagerie et collaboration open source d'origine allemande. Solution souveraine et on-premise, alternative à Microsoft Exchange/Outlook. Pertinent pour les intégrateurs travaillant avec les collectivités ou le secteur public.
- **OpenTofu** — Fork libre de Terraform (Infrastructure as Code). Utilisé par la DINUM pour le provisioning multi-provider. Incontournable pour toute ESN pratiquant le DevOps ou la gestion d'infrastructures cloud/hybrides.
- **Ansible** — Outil d'automatisation de configuration de référence. Utilisé pour le déploiement, la configuration et le MCO de la plateforme OpenXchange. Standard de facto pour les ESN en charge de l'exploitation d'infras Linux.
- **Carbonio** — Fork de Zimbra basé sur des formats ouverts (Zextras). Utilisé comme pivot de migration. À connaître pour les missions de migration de messagerie en environnement public ou PME.
- **CalDAV / CardDAV** — Protocoles standardisés de synchronisation de calendriers et contacts. Clé de voûte de l'interopérabilité entre Exchange et OpenXchange.
- **F-Droid** — Magasin d'applications Android 100 % libre. Alternative au Google Play Store pour les déploiements mobiles souverains, pertinent pour les SSI gérant des flottes Android durcies.
- **DAVx5** — Client de synchronisation CalDAV/CardDAV pour Android. Intégration mobile essentielle dans un écosystème sans Google.
- **Fossify Calendar / K-9 Mail** — Applications Android libres de calendrier et messagerie. Alternatives open source aux applications Google natives, pertinentes pour les politiques BYOD souveraines.
- **Postfix** — MTA (Mail Transfer Agent) Unix historique, composant de la pile serveur OpenXchange. Maîtrise requise pour les architectes messagerie.
- **GPLv3** — Licence copyleft forte utilisée pour le dépôt DevOps DINUM. Implique des obligations de redistribution à prendre en compte lors d'intégrations ou de forks.

## Points marquants

- **Microsoft comme déclencheur involontaire** : Baptiste Danielewicz remercie ironiquement Microsoft pour sa stratégie tarifaire et marketing « un peu boiteuse » — c'est la fin du support Exchange qui a contraint la collectivité à se tourner vers le logiciel libre.
- **Écosystème de prestataires quasi inexistant au départ** : lors du lancement du projet, Alma était l'un des seuls acteurs capables d'accompagner une collectivité française sur OpenXchange. La situation a évolué depuis.
- **Démarche inclusive comme clé du succès** : impliquer les agents utilisateurs finaux (et pas seulement les DSI) dans le benchmark est présenté comme le facteur n°1 de réussite, y compris pour l'adhésion des élus.
- **100 % webmail** : le passage à OpenXchange a aussi permis de supprimer tous les clients lourds de messagerie. La collectivité est désormais intégralement en webmail.
- **Scalabilité en question** : la DINUM ne se juge pas encore prête pour un déploiement à l'échelle de millions d'utilisateurs (ex : système éducatif belge), cible intermédiaire à ~100 000 comptes.
- **"Never on Friday"** : la migration a été délibérément planifiée un mercredi pour limiter les impacts, principe partagé par toute l'équipe projet.
- **Contribution reversée à la DINUM** : le SITPI et Alma ont pu contribuer au dépôt public DINUM, illustrant le cycle vertueux du logiciel libre dans la sphère publique.

## Mes notes

*(à compléter)*

## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Fayçal Braiki (SITPI), Christophe Ninucci (DINUM), Yoann Dupont (Alma), Baptiste Danielewicz (Ville de Claix), Nicolas Ecarnot (SITPI)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
