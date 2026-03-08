# Comment répondre aux enjeux de la gestion de services IT dans les entités publiques ?

## Intervenant
Luca Chevrier · Combodo

## Société
Combodo est un éditeur open source grenoblois fondé par les créateurs d'iTop. La société accompagne des organisations publiques et privées — collectivités, ministères, hôpitaux, universités — dans la structuration de leur gestion informatique. Son modèle repose sur le support, l'hébergement et les services autour d'iTop, entièrement open source et auto-hébergeable.

## Résumé
iTop est un logiciel open source qui permet à une équipe informatique de gérer ses tickets, son inventaire de matériel et de logiciels, et ses procédures d'intervention — le tout dans une seule interface web, sans Excel ni boîte mail partagée. Déployé au CISIRH (ministère) et à l'Éducation Nationale. Alternative directe à ServiceNow, sans abonnement cloud ni dépendance éditeur.

## Points marquants
- Excel et les boîtes mail partagées ne sont pas une gestion IT.
  Dans beaucoup d'entités publiques, les demandes d'assistance, les pannes et les inventaires de matériel se gèrent encore dans des fichiers Excel ou par email. iTop remplace tout ça par un outil structuré : qui a signalé quoi, qui traite, quel matériel est concerné, quelle est la priorité.
- Sans inventaire du SI, une cyberattaque devient incontrôlable.
  Lors d'un incident cyber sur une collectivité, la première question est : quels serveurs et logiciels sont touchés ? Sans inventaire centralisé, personne ne sait. iTop intègre nativement cet inventaire — on sait exactement ce qui tourne, où, et avec quelles dépendances.
- Le CISIRH et l'Éducation Nationale l'ont déployé.
  Le CISIRH est le service informatique des ressources humaines des ministères français. L'Éducation Nationale est l'un des périmètres les plus étendus de l'administration. Ces deux références valident la capacité d'iTop à tenir à grande échelle.
- Auto-hébergé, souverain, sans abonnement.
  iTop se déploie sur l'infrastructure de l'entité, les données ne quittent pas le SI. Pas d'abonnement SaaS, pas de vendor lock-in — à l'opposé de ServiceNow, qui facture par utilisateur et héberge les données aux États-Unis.
- Fait à Grenoble.
  Combodo a été fondée par les créateurs du projet iTop et concentre son activité sur le secteur public et les collectivités — proximité directe avec l'écosystème AlpOSS et les clients potentiels d'une ESN.

## Technologies
- **iTop** — Logiciel web open source (AGPL) qui centralise la gestion informatique d'une organisation : tickets d'incidents et de demandes, inventaire du parc matériel et logiciel, procédures de changement. Alternative open source à ServiceNow ou Jira Service Management. Auto-hébergeable, sans abonnement.
- **iTop Hub** — Marketplace d'extensions communautaires pour iTop : connecteurs, automatisations, modules métier prêts à l'emploi sans développement lourd.
- **CMDB (Configuration Management Database)** — Inventaire centralisé de tout le système informatique d'une organisation : serveurs, logiciels, contrats, dépendances entre services. Indispensable pour répondre à un incident cyber ou planifier une migration.
- **ITIL** — Référentiel international de bonnes pratiques pour les équipes informatiques : comment structurer les tickets, les changements, les incidents. iTop en implémente les processus nativement.
- **PHP / MySQL** — Stack technique d'iTop, open source et éprouvée. Facile à auto-héberger sur n'importe quelle infrastructure sans licence propriétaire.
