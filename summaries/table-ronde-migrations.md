# AlpOSS 2026 - Table ronde : migrations vers l'open source

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Marie-Jo Kopp Castinel (OpenGo), Damien Accorsi (Algoo), Baptiste Danielewicz (Ville de Claix), Nicolas Benoît (CGT Isère) |
| **Organisation** | OpenGo / Algoo / Ville de Claix / CGT Isère |
| **Durée** | 43:58 |
| **Présent** | ✅ Oui |

## À propos des intervenants

- **Nicolas Vivant** (animateur) — Représentant de la Ville d'Échirolles (ville hôte d'AlpOSS), il anime la table ronde. Il a un rôle dans la stratégie numérique de la collectivité, fortement engagée dans l'open source depuis la signature de la charte des logiciels libres en 2014.
- **Nicolas Benoît** — Secrétaire général de l'Union Départementale CGT Isère. Représente une organisation syndicale ayant engagé une migration complète vers Linux, Thunderbird et Tracim, avec des motivations à la fois politiques (opposition aux GAFAM) et de souveraineté des données.
- **Damien Accorsi** — PDG d'Algoo (Moirans), société éditrice de Tracim (plateforme collaborative open source). 25-26 ans de prosélytisme pour le logiciel libre. A accompagné la CGT Isère dans sa migration vers Linux, première migration de ce type pour Algoo à cette échelle.
- **Marie-Jo Kopp Castinel** — PDG d'OpenGo, spécialiste du poste de travail et des migrations bureautiques depuis LibreOffice/OpenOffice (version 2). Accompagne les migrations bureautiques et messagerie dans de nombreuses collectivités isèroises (Saint-Martin-d'Uriage, Voreppe, etc.) ainsi que le Conseil Départemental de l'Aude (4 500 agents).
- **Baptiste Danielewicz** — Responsable informatique de la Ville de Claix (environ 8 000 habitants). A piloté la migration de la messagerie Microsoft Exchange vers Open-Xchange (packagé par Ladinium) via le syndicat intercommunal SITPI, avec une démarche centrée utilisateurs.

## Résumé

Nicolas Vivant ouvre la table ronde en posant le cadre : rares sont les organisations qui naissent avec de l'open source dans leur infrastructure. La table réunit un client (CGT Isère), deux prestataires (Algoo, OpenGo) et une collectivité (Ville de Claix) pour des retours d'expérience concrets.

---

### Nicolas Benoît (CGT Isère) — La migration syndicale vers Linux

La CGT Isère a migré vers Linux (depuis Windows), Thunderbird (depuis Outlook), Tracim (partage de données sur NAS) et un nouveau système de suivi des formations. Les motivations sont multiples : problèmes avec les prestataires précédents, manque de maîtrise de la messagerie, opposition politique aux GAFAM, et exigence de souveraineté des données stockées en France.

L'alternative était simple : rester chez Microsoft (coûteux) ou "faire la bascule dans un environnement du libre peu connu, propre à l'imaginaire et angoissant car souvent lié au monde de la programmation." La migration a concerné une quinzaine de personnes sur deux structures (l'UD CGT et la section météorologie). Le projet s'est déroulé sur environ six mois (contractualisation en décembre, déploiement complet prévu en juin). Nicolas souligne que sans le soutien d'Algoo et l'expérience de la Ville d'Échirolles comme référence, la migration n'aurait probablement pas eu lieu.

---

### Damien Accorsi (Algoo) — La perspective du prestataire

Algoo avait déjà accompagné des migrations, mais sur de très petites structures (3-4 postes dans des mairies). La CGT Isère représentait un challenge plus important. Damien reconnaît que la migration a été "un succès" et qu'elle a ouvert une nouvelle corde à l'arc d'Algoo : un forum d'entraide pour les organisations souhaitant migrer vers Linux est en cours de lancement.

Il insiste sur l'importance de la phase d'accompagnement, qu'il considère comme un "surcoût" à court terme mais une économie sur le long terme. Sa conviction : les logiciels libres ne sont pas "fondamentalement meilleurs" fonctionnellement, mais présentent des avantages différents, et ce qui importe c'est que les utilisateurs sachent ce qu'ils perdent et ce qu'ils gagnent. Toute la migration CGT a été réalisée en une seule fois (pas de mode dégradé possible avec Linux), après une validation préalable sur un poste pilote.

---

### Marie-Jo Kopp Castinel (OpenGo) — L'accompagnement bureautique à grande échelle

OpenGo accompagne des migrations bureautiques vers LibreOffice depuis l'époque d'OpenOffice version 2, dans de nombreuses collectivités isèroises. Marie-Jo détaille le cas du Conseil Départemental de l'Aude (environ 2 800 utilisateurs effectifs sur 4 500 agents), une migration qu'elle accompagne depuis mai 2025 vers LibreOffice et Zimbra (via Bisym).

Le succès de cette migration repose sur un triptyque indispensable : **direction, DSI et volonté politique**. Le DGS de l'Aude arrivait d'une collectivité déjà sous LibreOffice, ce qui a facilité la décision. La migration a été progressive : d'abord LibreOffice, puis la messagerie (Zimbra), les deux simultanément étant une "catastrophe" à éviter. La formation a pris la forme d'e-learning via Chamilo (LMS libre) pour aller vite à cette échelle. Les directeurs ont été migrés en premier — l'exemplarité de la hiérarchie est présentée comme essentielle.

Marie-Jo tranche clairement sur LibreOffice vs OnlyOffice : LibreOffice est "une solution aboutie", OnlyOffice est "plus joli" mais présente encore des soucis de compatibilité et des fonctionnalités manquantes. Le choix du DSI de l'Aude : il voulait "une solution bureautique" et ne voulait "pas entendre parler d'OnlyOffice."

---

### Baptiste Danielewicz (Ville de Claix) — La migration messagerie pilotée par les utilisateurs

Claix était depuis plus de vingt ans sur Microsoft Exchange. Lorsque Microsoft a annoncé la fin du mode de licence perpétuelle, la ville a décidé de se réinterroger. La commande de la direction : conserver une messagerie on-premises et souveraine.

La méthode : un groupe projet de **vingt utilisateurs** représentatifs de tous les services et tous les profils (assistantes de direction, personnel d'accueil, cadres, membres du CODIR, novices et experts) a été constitué. Ces utilisateurs ont d'abord listé leurs besoins et leurs usages actuels — ce document a servi de fil conducteur pour les démonstrations. Les candidats ont présenté leur solution sur la base d'un filage de démonstration utilisateur (90 % du temps), pas de back-office. Un objectif explicite de Baptiste : sortir d'Outlook (client lourd) vers un webmail à 100 %, premier pas vers une sortie du Pack Office.

La solution retenue : Open-Xchange, dans sa version packagée par Ladinium et hébergée par le syndicat intercommunal SITPI. Migration réalisée en octobre 2025. Résultat : 120 utilisateurs actifs, ~200 boîtes. Les référents utilisateurs formés en amont ont porté le message vers leurs collègues — "le projet n'appartient pas à la DSI, il appartient aux utilisateurs."

Son conseil : employer la même démarche, quelle que soit la solution retenue. Impliquer les utilisateurs est "une grande partie de la réussite."

---

### Échanges avec la salle

Un intervenant anonyme pose la question philosophique : si "rien n'a changé" pour les utilisateurs, la dimension politique et éthique du logiciel libre ne passe-t-elle pas à la trappe ? Damien répond que c'est normal — la plupart des utilisateurs voient l'informatique comme un outil, pas un enjeu politique. Les instances dirigeantes portent ces enjeux, pas nécessairement chaque agent.

Pierre Miriot, adjoint numérique à Grenoble, témoigne : la ville a basculé 1 600 PC des écoles en libre intégral, mais l'Éducation Nationale ne formant pas ses personnels, la ville a dû assurer la formation elle-même, étalée sur cinq ans. Il note que la "rapacité des GAFAM" — notamment le passage à la licence d'abonnement de Microsoft — aide désormais à décider, et espère que cela enclenchera une autre vitesse pour la métropole de Grenoble.

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **Linux (postes de travail)** — Migration complète de postes Windows vers Linux à la CGT Isère. Algoo accompagne ce type de migration pour des petites et moyennes structures. Forum d'entraide en cours de lancement par Algoo.
- **Thunderbird** — Client de messagerie libre utilisé en remplacement d'Outlook dans la migration CGT. Compatible avec les échanges de calendrier (CalDAV) et les contacts (CardDAV).
- **Tracim (Algoo)** — Plateforme collaborative open source développée à Moirans (Isère). Utilisée pour le partage documentaire sur NAS à la CGT Isère. Alternative open source à Confluence/SharePoint.
- **LibreOffice** — Suite bureautique libre, choisie par OpenGo pour accompagner les migrations bureautiques. Présenté comme "une solution aboutie", avec désormais un environnement à onglets comparable à Microsoft Office.
- **OnlyOffice** — Suite bureautique libre alternative à LibreOffice. Présentée comme "plus jolie" et ressemblant à Microsoft Office, mais avec des soucis de compatibilité et des fonctionnalités encore manquantes selon Marie-Jo. La ville de Lyon y travaille.
- **Open-Xchange (OX App Suite)** — Suite collaborative open source (messagerie, agenda, contacts). Retenue par la Ville de Claix dans sa version packagée par Ladinium, hébergée par le SITPI. Alternative à Microsoft Exchange pour les collectivités.
- **Microsoft Exchange / Outlook** — Solution historique remplacée à Claix. La fin du mode de licence perpétuelle annoncée par Microsoft est présentée comme le déclencheur direct de nombreuses migrations.
- **Zimbra / Bisym** — Solution de messagerie open source accompagnée par OpenGo dans la migration du Conseil Départemental de l'Aude (vers Zimbra via Bisym).
- **Chamilo (LMS)** — Plateforme e-learning libre utilisée pour la formation à distance des 2 800 utilisateurs du Département de l'Aude (via un partenaire d'Amiens). Pertinent pour les ESN proposant des formations à grande échelle.
- **SITPI** — Syndicat intercommunal de traitement de l'informatique (région grenobloise). Héberge et opère l'instance Open-Xchange de la Ville de Claix. Modèle de mutualisation réplicable.

## Points marquants

- La CGT Isère, organisation syndicale opposée aux GAFAM par conviction politique, avait pourtant ses données chez Microsoft jusqu'à la migration — et assume publiquement cette contradiction passée.
- La fin du mode de licence perpétuelle Microsoft Office est citée comme le déclencheur principal de plusieurs migrations en cours (Claix, Aude, Grenoble). Les collectivités n'ont plus le choix financier.
- Le triptyque **direction + DSI + volonté politique** est présenté par Marie-Jo comme une condition sine qua non des migrations réussies. Sans ce triptyque, elle prévient : "vous allez avoir des retours en arrière."
- À la Ville de Claix, des migrations Exchange vers Open-Xchange en France, "j'en connaissais pas avant que le SITPI le fasse" — une migration pionnière en France pour une collectivité de cette taille.
- La première direction à désinstaller Microsoft Office au Département de l'Aude est... les Finances. "On passe à LibreOffice point."
- Pierre Miriot (adjoint numérique Grenoble) évoque la "rapacité des GAFAM" comme argument politique permettant désormais de convaincre les élus. Il cite le cas du procureur de la Cour Pénale Internationale dont le mail a été bloqué comme symptôme du monde dans lequel on vit.
- La durée de la table ronde (44 minutes) reflète la densité du sujet — et l'intérêt croissant pour des retours d'expérience concrets, avec des noms, des chiffres et des durées de projets réels.
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Marie-Jo Kopp Castinel (OpenGo), Damien Accorsi (Algoo), Baptiste Danielewicz (Ville de Claix), Nicolas Benoît (CGT Isère) — Animation : Nicolas Vivant (Ville d'Échirolles)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
