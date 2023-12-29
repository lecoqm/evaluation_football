# Projet python 2A
César Fabiani - Mathis Lecoq

_Ce projet est réalisé dans le cadre du cours de Python de Lino Galiana pour l'année 2023-2024._

Le but de ce projet est d'essayer d'importer des méthodes d'évaluation d'un joueur au baseball au football. Pour cela nous avons créé un joueur "moyen" que nous avons comparé avec chaque joueur, puis nous avons utilisé des données plus précises concernant chaque action lors d'un match (passes, tirs, tacles, etc) pour affiner le résultat. Vous pouvez trouvez le notebook rassemblant l'ensemble de notre projet ici : [notebook](https://github.com/lecoqm/evaluation_football/blob/main/notebook.ipynb).

Ce README contient un résumé des éléments présents dans le notebook.

## Récapitulatif des éléments présents dans le Git

- **`data`** contient toutes les bases de données scrappées brutes et netoyées
- **`scraping`** contient les programmes ayant servis à scrapper les sites

## Etape 1 : Extraction des données

Les données ont été récoltées sur les matchs de Premier League pour la saison 2022-2023 sur le site [**FB**REF](https://fbref.com/fr/). Ce dernier possède de nombreuses données pour chaqu'un des joueurs pour chaque match. 