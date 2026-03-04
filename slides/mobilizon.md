# Sortez vos événements des réseaux sociaux grâce à Mobilizon

## Intervenant
Alexandra Cadet · Kaihuri

## Société
Kaihuri est une structure impliquée dans l'écosystème du logiciel libre, qui accompagne les organisations souhaitant déployer des alternatives open source aux plateformes centralisées. Elle contribue notamment à la promotion et au déploiement de Mobilizon, la plateforme décentralisée de gestion d'événements développée par Framasoft. Kaihuri aide les communautés, associations et collectivités à mettre en place leurs propres instances et à adopter le Fediverse comme infrastructure de communication souveraine.

## Résumé
Mobilizon est une alternative open source et décentralisée à Facebook Events, développée par Framasoft et financée par le fonds européen NGI. Chaque organisation peut héberger sa propre instance ou rejoindre une instance thématique existante, et les événements publiés sont interopérables avec le Fediverse (Mastodon, etc.) via ActivityPub. Un plugin WordPress permet d'afficher automatiquement les événements d'un groupe Mobilizon sur un site tiers, sans intervention manuelle. L'outil cible associations, collectivités et universités souhaitant garder la maîtrise de leurs données d'agenda.

## Points marquants
- Mobilizon reprend les groupes/événements de Facebook, pas les profils.
- Chaque instance est autonome et fédérée avec les autres.
- Un BDE universitaire a déployé sa propre instance en production.
- Les événements open data peuvent alimenter une instance Mobilizon.

## Technologies
- **Mobilizon** — Plateforme libre décentralisée de gestion d'événements et de groupes (AGPLv3). Auto-hébergeable, développée par Framasoft, financée par le programme européen NGI. Pertinent pour les ESN accompagnant des associations, collectivités ou établissements souhaitant maîtriser leurs données d'agenda.
- **ActivityPub / Fediverse** — Protocole fédéré de communication (standard W3C). Permet à Mobilizon d'interopérer nativement avec Mastodon et l'ensemble du réseau social décentralisé. Enjeu de souveraineté numérique croissant dans le secteur public européen.
- **Flux ICS (iCalendar)** — Format standard d'échange de données de calendrier, exposé nativement par chaque page Mobilizon. Permet la synchronisation avec tout client agenda (Thunderbird, Nextcloud Calendar, Google Calendar, etc.).
- **Plugin WordPress / Mobilizon** — Extension permettant l'affichage dynamique et automatique des événements d'un groupe Mobilizon sur un site WordPress, sans synchronisation manuelle ni développement spécifique.
