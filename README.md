# Projet python 2A - Transposition du Wins Above Replacement au football européen pour évaluer la performance des joueurs

César Fabiani - Mathis Lecoq

_Ce projet est réalisé dans le cadre du cours de Python de Lino Galiana pour l'année 2023-2024._
 
### Introduction


**Notre objectif** : 

Notre objectif est d'essayer de transposer dans le cadre du football européen la variable de Wins Above Replacement (WAR), très populaire dans les sports américains, surtout le baseball. Cette statistique de WAR donne la performance d'un joueur sous la forme d'un nombre de victoires que le joueur apporte à son équipe par rapport à un joueur de niveau "replacement", c'est-à-dire un joueur faible que toutes les équipes peuvent obtenir.

Cette performance est individuelle et le plus possible indépendante de la performance du reste de l'équipe. L'idée est d'obtenir une évaluation de la performance d'un joueur la plus objective possible en corrigeant le fait qu'il appartienne à une plus ou moins bonne équipe. On mesure son apport personnel en terme de victoires. Cette statistique est aussi indépendante du contexte (car le contexte dépend du reste de l'équipe) : un but vaut autant qu'il soit marqué à un moment décisif du match, qu'à un moment où le sort de la partie est déjà presque certainement connu. C'est sur ces principes que la WAR a été créée aux Etats-Unis pour le baseball et le hockey sur glace.

**Notre démarche** 

Pour la recréer dans le cadre du football européen, nous allons devoir récupérer les données nécessaires à la création d'une telle statistique, les explorer pour voir comment recréer la statistique WAR, mettre en œuvre la stratégie choisie et observer la performance des joueurs ainsi obtenue. On proposera à la fin du notebook une petite application de cette statistique dans le cadre du management d'une équipe et nous aurons besoin pour cela de la valeur marchande des joueurs.
Comme dans le football on compte le nombre de points et pas de victoires (une victoire donne 3 points, un nul 1 et une défaite 0), on nommera plutôt la statistique créée PAR (Points Above Replacement).
La démarche de création du PAR est explicitée dans le corps de ce notebook au cours de l’analyse, mais elle s’inspire fondamentalement de la méthode développée par le site Fan Graph pour le baseball (https://library.fangraphs.com/war/war-position-players/). 
Bien sûr, tout l’enjeu est de la réadapté au football et de voir si elle fonctionne pour ce sport.
De plus il existe, à notre connaissance, une seule vraie tentative de recréation de la WAR au football et elle est le fait d’un américain (https://www.americansocceranalysis.com/home/2019/1/11/points-above-replacement) . Mais ce dernier utilise des données de position (avec l’endroit où se situent la balle et les joueurs à chaque instant) et sa méthode n’est donc pas du tout applicable à notre situation. Ces données sont payantes, très difficiles à exploiter et nous souhaitons créer un outil plus accessible. 


**L'objectif de ce projet est de construire le framework de la transposition de la WAR du baseball au football, de construire une base de données adaptée et d'évaluer la pertinence du modèle créé.**


Vous pouvez trouvez le notebook rassemblant l'ensemble de notre projet ici : [notebook](https://github.com/lecoqm/evaluation_football/blob/main/main.ipynb).

## Récapitulatif des éléments présents dans le Git

- **`data`** contient toutes les bases de données scrappées brutes et netoyées
- **`scraping`** contient les programmes ayant servis à scrapper les sites
- **`main`** notre notebook rassemblant l'ensemble de notre travail et nos résultats

## Un mot sur notre motivation

Cette dernière partie du read.me revient sur les motivations derrière le choix de ce projet. Elle permet de comprendre dans quelle contexte s'inscrit notre démarche.


Si les statistiques avancées sont devenues très populaires dans le sport américain, cette enthousiasme n'a pas traversé l'Atlantique pour deux raisons.

Tout d'abord il existe une réticence des européens à voir le sport être quantifié, ce qui enleverait la beauté du jeu aux yeux de certains. De plus, là où le baseball est un sport facilement à séquencer, quantifier et analyse, cela est beaucoup plus difficile (et intéressant !) pour le football où le jeu est plus dynamique.

Néanmoins, les choses changent dans le football et les Expected Goals, statistiques avancées utilisant les positionnements des joueurs sur le terrain gagnent en popularité et ouvrent la porte à de nouvelles opportunités pour le traitement statistique du football. C'est ici que s'inscrit notre démarche.