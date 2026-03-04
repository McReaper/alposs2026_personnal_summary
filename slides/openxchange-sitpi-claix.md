# Déploiement de la messagerie OpenXchange au SITPI : RETEX de la migration de la ville de Claix

## Intervenant
Fayçal Braiki, Christophe Ninucci, Yoann Dupont, Baptiste Danielewicz, Nicolas Ecarnot · SITPI / DINUM / Alma / Ville de Claix

## Société
Le SITPI (Syndicat Intercommunal des Technologies et des Plateformes d'Information) est une structure de mutualisation des systèmes d'information regroupant dix communes de l'agglomération grenobloise, représentant environ 140 000 habitants. Il pilote la stratégie de souveraineté numérique du syndicat et conduit les projets de migration vers des solutions libres. La DINUM (Direction Interministérielle du Numérique) développe et publie sous GPLv3 l'outillage DevOps (OpenTofu, Ansible) pour faciliter le déploiement d'OpenXchange dans les administrations françaises. Alma est un prestataire spécialisé dans l'accompagnement des collectivités pour la migration vers OpenXchange, l'un des premiers acteurs à proposer ce service en France.

## Résumé
Le SITPI présente le retour d'expérience de la migration de la ville de Claix (200 comptes) depuis Microsoft Exchange vers OpenXchange. La démarche a impliqué les utilisateurs finaux dès le benchmark, ce qui a été présenté comme le facteur clé de succès. La migration mobile a mobilisé un écosystème 100 % libre (F-Droid, DAVx5, K-9 Mail). La DINUM publie l'outillage DevOps sous GPLv3 pour que d'autres collectivités puissent répliquer le déploiement.

## Points marquants
- Les utilisateurs finaux ont choisi OpenXchange, pas les DSI.
- Migration planifiée un mercredi : "Never on Friday".
- Pile mobile 100 % libre : F-Droid, DAVx5, K-9 Mail.
- DINUM pas encore prête pour des millions d'utilisateurs.

## Technologies
- **OpenXchange** — Suite de messagerie et collaboration open source d'origine allemande ; alternative souveraine on-premise à Microsoft Exchange/Outlook ; interface webmail sans client lourd ; pertinent pour les ESN travaillant avec les collectivités ou le secteur public.
- **OpenTofu** — Fork libre de Terraform (Infrastructure as Code) utilisé par la DINUM pour le provisioning multi-provider ; incontournable pour toute ESN pratiquant le DevOps ou la gestion d'infrastructures cloud/hybrides.
- **Ansible** — Outil d'automatisation de configuration de référence ; utilisé pour le déploiement, la configuration et la MCO de la plateforme OpenXchange ; standard de facto pour les ESN exploitant des infras Linux.
- **CalDAV / CardDAV** — Protocoles standardisés de synchronisation de calendriers et contacts ; clé de voûte de l'interopérabilité entre Exchange et OpenXchange pour la migration des données.
- **DAVx5** — Client de synchronisation CalDAV/CardDAV pour Android ; intégration mobile essentielle dans un écosystème sans Google ; couplé à F-Droid et K-9 Mail pour une flotte souveraine.
- **Carbonio** — Fork de Zimbra basé sur des formats ouverts (Zextras) ; utilisé comme pivot de migration pour les événements de calendrier entre Exchange et OpenXchange.
