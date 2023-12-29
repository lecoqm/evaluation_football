import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##########
# Modify:
# The data come from a json file
file = "/home/onyxia/work/evaluation_football/data/df_PL.csv"  # Chose the path of the json file which will be analized
##########

df = pd.read_csv(file)

# number of players
nb_players = len(set(df['Joueur']))
print(nb_players)

statistiques = ['Buts','Passes décisives_x','Total des tirs ','Shots on Target','Cartons jaunes_x','Cartons rouges_x','Touches_x','Tacles_x','Interceptions_x','Balles contrées_x','Actions menant à un tir','Actions menant à un but','Passes réussies_x','Passes tentées_x','% de passes réussies_x','Passes progressives_x','Balle au pied_x','Possessions progressives_x','Dribbles tentés_x','Dribbles réussis_x','Distance totale des passes',"Distance parcourue vers l'attaque avec les passes",'Passes réussies (Court)','Passes tentées (Court)','% de passes réussies (Court)','Passes réussies (Moyen)','Passes tentées (Moyen)','% de passes réussies (Moyen)','Passes réussies (Long)','Passes tentées (Long)','% de passes réussies (Long)','Passes clés','Passes dans le dernier tiers du terrain','Passes dans la surface de réparation','Centres dans la surface de réparation','Passes tentées','Live-ball Passes','Dead-ball Passes','Passe en profondeur','Transversales','Centres_x','Throw-ins Taken','Passes réussies','Passes hors-jeux','Passes bloquées_x','Tacles réussis_x','Tacles (ZDéf)','Tacles (MilTer)','Tacles (ZOff)','Dribbleurs taclés','Dribbles mis en échec','% of Dribblers Tackled','Tacles manqués','Tirs bloqués','Tcl+Int','Dégagements','Erreurs','Touches (SurfRépDéf)','Touches (ZDéf)','Touches (MilTer)','Touches (ZOff)','Touches (SurfRépOff)','Touches (Ballon vivant)','% de dribbles réussis','Nombre de fois où le joueur a été taclé','Pourcentage de tacles subis lors des tentatives de franchissement','Distance totale parcourue avec le ballon',"Distance parcourue vers l'attaque en portant la balle","Chevauchées dans le dernier tiers","Chevauchées dans la surface de réparation","Mauvais contrôle","Perte de balle","Passes reçues","Passes progressives reçues","Deuxième carton jaune","Fautes commises","Fautes provoquées","Hors-jeux","Interceptions","Pénaltys concédés","But contre son camp","Récupérations de balle","Aerials Won","Aerials Lost","% of Aerials Won"]

variances = pd.DataFrame(index=statistiques, columns=df['Emplacement'].unique())

for position in df['Emplacement'].unique():
    for stat in statistiques:
        variance = df[df['Emplacement'] == position][stat].var(ddof=0)
        variances.at[stat, position] = variance

variances.to_csv("/home/onyxia/work/evaluation_football/data/variances.csv")