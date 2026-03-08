# Déploiement de la messagerie OpenXchange au SITPI : RETEX de la migration de la ville de Claix

## Intervenant
Fayçal Braiki, Christophe Ninucci, Yoann Dupont, Baptiste Danielewicz, Nicolas Ecarnot · SITPI / DINUM / Alma / Ville de Claix

## Société
Le SITPI (Syndicat Intercommunal des Technologies et des Plateformes d'Information) est une structure de mutualisation des systèmes d'information regroupant dix communes de l'agglomération grenobloise, représentant environ 140 000 habitants. Il pilote la stratégie de souveraineté numérique du syndicat et conduit les projets de migration vers des solutions libres. La DINUM (Direction Interministérielle du Numérique) développe et publie sous GPLv3 l'outillage DevOps (OpenTofu, Ansible) pour faciliter le déploiement d'OpenXchange dans les administrations françaises. Alma est un prestataire spécialisé dans l'accompagnement des collectivités pour la migration vers OpenXchange, l'un des premiers acteurs à proposer ce service en France.

## Résumé
Le SITPI a migré 200 comptes de Microsoft Exchange vers OpenXchange en impliquant les agents dès le benchmark — facteur clé du succès. La DINUM publie l'outillage DevOps (OpenTofu + Ansible) sous GPLv3 pour que d'autres collectivités puissent répliquer le déploiement.

## Points marquants
- Les utilisateurs finaux ont plébiscité OpenXchange, pas les DSI.
  Six solutions ont été benchmarkées sur une heure de démo chacune ; 90 à 95 % du temps était consacré à l'ergonomie utilisateur, pas au back-office. OpenXchange a été choisi en premier par les agents d'une vingtaine représentant cinq à six communes du SITPI.
- Microsoft a involontairement déclenché la migration vers le libre.
  La fin annoncée du mode de licence perpétuelle Microsoft Exchange a contraint le SITPI à se réinterroger dès 2024. Baptiste Danielewicz remercie explicitement Microsoft pour sa "stratégie marketing un peu boiteuse" comme déclencheur de la démarche.
- La migration mobile a été traitée comme un sous-projet indépendant.
  Les smartphones ont été migrés vers un écosystème 100 % libre : F-Droid (magasin d'applications), DAVx5 (synchronisation CalDAV/CardDAV), Fossify Calendar et K-9 Mail. La bascule a eu lieu un mardi soir pour une mise en production le mercredi — stratégie délibérée ("Never on Friday").
- L'outillage DevOps de la DINUM est publié en GPLv3 et réutilisable.
  OpenTofu (fork libre de Terraform) et Ansible permettent de déployer et maintenir une instance OpenXchange. Le SITPI et Alma ont pu contribuer au dépôt public, illustrant le cycle vertueux du logiciel libre dans la sphère publique.
- La DINUM cible 100 000 comptes mais n'est pas prête pour des millions.
  Interrogée sur un déploiement à l'échelle du système éducatif belge (150 000 enseignants, 1,5 million d'élèves), la DINUM indique qu'elle n'est pas encore assez mature pour des infrastructures à plusieurs millions d'utilisateurs.

## Technologies
- **OpenXchange** — Suite de messagerie et collaboration open source d'origine allemande ; alternative souveraine on-premise à Microsoft Exchange/Outlook ; interface webmail sans client lourd ; pertinent pour une ESN travaillant avec les collectivités ou le secteur public.
- **OpenTofu** — Fork libre de Terraform (Infrastructure as Code) utilisé par la DINUM pour le provisioning multi-provider ; incontournable pour une ESN pratiquant le DevOps ou la gestion d'infrastructures cloud/hybrides.
- **Ansible** — Outil d'automatisation de configuration de référence ; utilisé pour le déploiement, la configuration et la MCO de la plateforme OpenXchange ; standard de facto pour une ESN exploitant des infras Linux.
- **CalDAV / CardDAV** — Protocoles standardisés de synchronisation de calendriers et contacts ; clé de voûte de l'interopérabilité entre Exchange et OpenXchange pour la migration des données.
- **DAVx5** — Client de synchronisation CalDAV/CardDAV pour Android ; intégration mobile essentielle dans un écosystème sans Google ; couplé à F-Droid et K-9 Mail pour une flotte souveraine.
- **Carbonio** — Fork de Zimbra basé sur des formats ouverts (Zextras) ; utilisé comme pivot de migration pour les événements de calendrier entre Exchange et OpenXchange.
