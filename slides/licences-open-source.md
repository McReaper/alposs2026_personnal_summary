# Licences open source : peut-on vraiment les faire respecter ?

## Intervenant
Josquin Louvier · Champollion Avocats (Grenoble)

## Société
Champollion Avocats est un cabinet grenoblois spécialisé en droit du numérique et propriété intellectuelle. Il intervient en conseil et en contentieux pour des acteurs de l'open source, des éditeurs logiciels et des entreprises du numérique. Josquin Louvier accompagne notamment des éditeurs open source dans la structuration de leur modèle de licence et dans la défense de leurs droits en justice. Il intervient régulièrement dans les événements de l'écosystème libre pour vulgariser les enjeux juridiques des licences open source auprès d'un public technique.

## Résumé
La Cour de cassation a tranché : violer une licence open source est de la contrefaçon, pas un manquement contractuel — ce qui ouvre saisie-contrefaçon et mesures provisoires. Orange a été condamné à près d'un million d'euros pour violation de la GPL, record français en matière de contrefaçon logicielle.

## Points marquants
- Cinq décisions de tribunaux français en 40 ans sur les licences open source.
  Le contentieux propriétaire représente plusieurs dizaines de décisions sur la même période. Ce paradoxe révèle non pas une faiblesse juridique de l'open source, mais une difficulté d'appréhension initiale des licences par les juridictions françaises.
- Orange condamné à près d'un million d'euros pour violation de la GPL.
  Orange avait intégré LASSO (logiciel d'authentification sous GPL v2) dans le portail monservicepublic.fr sans respecter les trois conditions copyleft : redistribution sous la même licence, fourniture des codes sources, et préservation des mentions de copyright. C'est à ce jour la plus forte condamnation pour contrefaçon de logiciel prononcée en France.
- Violer une licence open source constitue de la contrefaçon, pas un manquement contractuel.
  La Cour de cassation a tranché ce point fondamental dans l'affaire Orange c/ Entre Ouverts. Ce statut ouvre l'accès à des recours bien plus puissants : saisie-contrefaçon, mesures provisoires d'interdiction, et indemnisation plus généreuse.
- Orange savait qu'il violait la GPL avant de le faire.
  L'éditeur Entre Ouverts avait été contacté en amont pour négocier une licence propriétaire de LASSO ; les discussions n'avaient pas abouti. Ce contexte a aggravé la responsabilité d'Orange et renforcé la condamnation.
- La clause de rétablissement AGPL v3 laisse 30 jours pour corriger.
  Après notification d'un manquement, l'auteur dispose d'une fenêtre de 30 jours pour rectifier sans perdre le droit de distribuer. Dans l'affaire Bluemind/Inaagora (Cour d'appel de Bordeaux, 2025), la correction n'est intervenue qu'après plus de deux mois, entraînant la résiliation de la licence et le retour à l'état de contrefaçon.

## Technologies
- **GPL v2 / GPL v3** — Licences copyleft fortes ; obligations clés : redistribution des sources et maintien de la même licence pour les œuvres dérivées ; Kaizen intégrant des composants GPL dans les livrables de ses clients doit être vigilante sur le respect des conditions de redistribution.
- **AGPL v3 (Affero GPL)** — Variante de la GPL étendue au SaaS : l'obligation de redistribution des sources s'applique même à l'usage réseau, pas seulement à la distribution ; particulièrement critique pour Kaizen hébergeant des logiciels GPL pour le compte de clients.
- **Double licensing** — Modèle permettant à un éditeur de distribuer son logiciel à la fois sous licence open source et sous licence propriétaire ; Kaizen doit comprendre ce modèle pour négocier les licences de ses composants tiers.
- **Saisie-contrefaçon** — Procédure judiciaire française permettant de récupérer des preuves (codes sources, etc.) chez un tiers ; rendue accessible aux titulaires de droits open source grâce à l'arrêt de la Cour de cassation dans l'affaire Orange c/ Entre Ouverts.
