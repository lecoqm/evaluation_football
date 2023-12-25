import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##########
# Modify:
# The data come from a json file
file = "json"  # Chose the path of the json file which will be analized
##########

df = pd.read_json(file)

# number of players
nb_players = len(set(df['Joueur']))

#number of matches
nb_match = len(set(df['Match']))

# number of matches played by each players
Nb_Match = []
for e in set(df['Joueur'].tolist()):
    nb_match.append(len(set(df['Joueur'].loc[df.Joueur==e])))
nb_match.sort()
plt.boxplot(Nb_Match)
plt.show()

