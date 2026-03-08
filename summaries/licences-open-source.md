# AlpOSS 2026 - Licences open source : peut-on vraiment les faire respecter ?

> AlpOSS 2026 — 17 février 2026, Grenoble

## Informations

| | |
|---|---|
| **Intervenant(s)** | Josquin Louvier |
| **Organisation** | Champollion Avocats (Grenoble) |
| **Durée** | 19:59 |
| **Présent** | ❌ Non |

## À propos de l'intervenant

**Josquin Louvier** est avocat associé au cabinet grenoblois **Champollion Avocats**, spécialisé en droit du numérique et propriété intellectuelle. Le cabinet intervient en conseil et en contentieux pour des acteurs de l'open source, des éditeurs logiciels et des entreprises du numérique. Josquin Louvier accompagne notamment des éditeurs open source dans la structuration de leur modèle de licence et dans la défense de leurs droits en justice. Il intervient régulièrement dans des événements de l'écosystème libre pour vulgariser les enjeux juridiques des licences open source auprès d'un public technique.

## Résumé

Cette conférence propose un panorama structuré de la jurisprudence française sur les licences open source, en s'appuyant sur les quatre décisions publiées à ce jour.

**Introduction : un constat paradoxal.** Les licences open source existent depuis environ 40 ans (le manifeste de Richard Stallman date de 1985). Elles sont aujourd'hui largement répandues dans l'édition logicielle. Pourtant, le contentieux judiciaire sur ces licences est extrêmement rare : seulement **cinq décisions de tribunaux français depuis 2007**, dont quatre publiées. À titre de comparaison, le contentieux sur les licences propriétaires ou la contrefaçon classique de logiciels représente plusieurs dizaines de décisions sur la même période.

**Rappels fondamentaux.** Josquin Louvier rappelle qu'un logiciel libre n'est pas « libre de droit » : il a un auteur, des contributeurs, et est soumis à une licence qui confère des droits précis à l'utilisateur. Sortir du périmètre de ces droits constitue un usage illicite et potentiellement un acte de contrefaçon. Les quatre libertés du manifeste (exécuter, étudier, modifier, diffuser) ont des équivalents directs en droit d'auteur français. Il soulève également les difficultés d'appréhension de ces licences par les juridictions françaises : rédigées en anglais, sur des bases de droit américain, avec des clauses d'exclusion de garantie potentiellement invalides en droit français (clauses abusives pour un consommateur, problème d'obligation essentielle entre professionnels).

**Décision 1 — Tribunal d'Instance de Paris, mars 2007 (affaire Baguera/JetLight).** Un logiciel de formation du CNRS/UJF intégrait JetLight de l'Université de Stanford sous GPL v2, livré sans la licence ni les mentions de copyright. La société Educafix, ne pouvant exploiter le logiciel sous licence propriétaire, a assigné en nullité pour dol. La nullité a été rejetée mais le contrat a été résolu pour manquement contractuel, le tribunal reconnaissant implicitement l'effet contaminant de la GPL. Décision jugée peu convaincante dans sa motivation mais pionnière.

**Décision 2 — 2009 (affaire AFPA/Educafix/VNC).** L'AFPA avait passé un marché pour une solution logicielle de formation. Le prestataire Educafix avait livré un produit intégrant VNC (GPL) en supprimant les mentions de copyright et le texte de la licence. L'AFPA a prononcé la résiliation du marché. La cour d'appel a confirmé la résolution au tort du fournisseur sur trois motifs : suppression du texte de la licence, remplacement des mentions de copyright, et absence de remise des codes sources au client. Le non-respect d'une licence open source est ici reconnu comme un **manquement contractuel grave justifiant la résolution du contrat**.

**Décision 3 — Affaire Orange / Entre Ouverts (saga 2009-2023, Cour de cassation).** C'est la plus importante et la plus emblématique. En 2009, Orange avait remporté le marché du portail monservicepublic.fr et intégré sans autorisation le logiciel d'authentification unique LASSO (sous GPL v2) de l'éditeur Entre Ouverts, en supprimant toutes les mentions de licence et de copyright, sans fournir les codes sources. Trois manquements à la GPL retenus : (1) redistribution payante d'une version dérivée (à plus de 50 %) sans respecter les conditions copyleft ; (2) non-fourniture des codes sources ; (3) redistribution sous une licence différente de la licence d'origine. Après un long contentieux incluant plusieurs degrés de juridiction, la Cour de cassation a tranché un point de droit fondamental : **un éditeur de logiciel libre peut agir en contrefaçon** (et non pas seulement en responsabilité contractuelle) en cas de non-respect de sa licence open source. Cela lui donne accès aux mécanismes de saisie-contrefaçon, aux mesures provisoires d'interdiction, et à une indemnisation plus généreuse. Au final, Orange a été condamné à **près d'un million d'euros** de dommages et intérêts (manque à gagner, bénéfices du contrefacteur, préjudice moral, parasitisme). C'est à ce jour **la plus forte condamnation jamais prononcée en France dans une affaire de contrefaçon de logiciel**, et elle concerne un non-respect de licence open source.

**Décision 4 — Cour d'appel de Bordeaux, 2025 (affaire Bluemind / Inaagora).** Plus récente, cette affaire oppose deux éditeurs partenaires du salon (présentée avec réserve). Inaagora avait acquis la société Alias Source, dont des anciens dirigeants ont fondé Bluemind avec des composants similaires sous licence AGPL v3. Le manquement retenu porte uniquement sur la **suppression des mentions de copyright** (droit à la paternité). Point juridique notable : la clause de **rétablissement automatique** de la licence AGPL v3 (cure period de 30 jours) — si le manquement est notifié et non corrigé dans les 30 jours, la licence est résiliée et la distribution constitue à nouveau une contrefaçon. En l'occurrence, la correction n'est intervenue qu'après plus de deux mois, entraînant la résiliation de la licence. Les dommages accordés restent modestes, mais la décision confirme la solidité de la jurisprudence.

**Conclusion.** Les licences open source sont désormais bien appréhendées par les tribunaux français. Les titulaires de droits qui choisissent l'open source bénéficient d'une protection comparable, voire supérieure, à celle des éditeurs propriétaires. Les juridictions sont devenues, selon l'orateur, « un outil de promotion du logiciel libre ».

## Technologies & outils mentionnés

> *Pertinents pour une ESN/SSI*

- **GPL v2 / GPL v3** — Licences copyleft fortes. Obligations clés : redistribution des sources, maintien de la même licence pour les œuvres dérivées. Toute ESN intégrant des composants GPL dans un produit commercialisé doit être vigilante sur le respect des conditions de redistribution, sous peine de contrefaçon.
- **AGPL v3 (Affero GPL)** — Variante de la GPL étendue au SaaS : l'obligation de redistribution des sources s'applique même à l'usage en réseau (pas seulement à la distribution). Particulièrement critique pour les ESN hébergeant des logiciels GPL pour le compte de clients.
- **LASSO** — Solution d'authentification unique (SSO) sous GPL v2 / double licence. Cas d'école pour comprendre le modèle de double licensing (open source + propriétaire) et ses implications contractuelles.
- **VNC (Virtual Network Computing)** — Logiciel de prise de contrôle à distance sous GPL. Composant fréquemment intégré dans des solutions SI ; sa licence GPL impose des obligations de redistribution à surveiller.
- **Clause de rétablissement (Cure Period)** — Mécanisme présent dans la GPL v3 et l'AGPL v3 : en cas de manquement notifié, 30 jours pour corriger sans perdre le droit de distribuer. Passé ce délai, contrefaçon. À intégrer dans les procédures de conformité (licence compliance) des ESN.
- **Saisie-contrefaçon** — Procédure judiciaire française permettant de récupérer des preuves (codes sources, etc.) chez un tiers. Rendue accessible aux titulaires de droits open source grâce à l'arrêt de la Cour de cassation dans l'affaire Orange.
- **Double licensing** — Modèle permettant à un éditeur de distribuer son logiciel à la fois sous licence open source et sous licence propriétaire. Modèle commercial que les ESN doivent comprendre pour négocier les licences de leurs composants tiers.

## Points marquants

- **Seulement 5 décisions de tribunaux français en 40 ans** sur les licences open source, alors que le contentieux propriétaire est bien plus fourni. Paradoxe révélateur : l'open source est omniprésent mais rarement défendu en justice.
- **Orange condamné à près d'un million d'euros** pour non-respect de la GPL — la plus forte condamnation pour contrefaçon de logiciel en France, et elle concerne une licence open source. Un signal fort envoyé aux grandes entreprises.
- **La Cour de cassation a tranché un débat fondamental** : le non-respect d'une licence open source est bien de la contrefaçon (et non seulement un manquement contractuel), ouvrant l'accès à des recours plus puissants.
- **Les tribunaux comme "outil de promotion du libre"** : formule finale de l'intervenant, qui inverse l'intuition commune selon laquelle l'open source serait moins bien protégé juridiquement que le propriétaire.
- **Orange était parfaitement conscient du problème** : l'éditeur avait contacté Entre Ouverts en amont pour négocier une licence propriétaire, discussions qui n'avaient pas abouti. Cet élément a aggravé sa responsabilité.
- **La clause de non-garantie questionnable en droit français** : les licences open source comportent généralement une exclusion totale de garantie, ce qui pourrait être contesté devant les tribunaux français, notamment pour des consommateurs.
## Crédits

- Conférence : [AlpOSS 2026](https://alposs.fr/)
- Intervenant(s) : Josquin Louvier (Champollion Avocats)
- Replay : [video.echirolles.fr](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk?playlistPosition=1)
