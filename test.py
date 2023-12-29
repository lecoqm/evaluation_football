import pandas as pd
import numpy as np

data_pl = pd.read_csv("/home/onyxia/work/evaluation_football/data/data_premierleague_2022_2023_V1.csv")
data_pl["home"] = np.where(data_pl["id_team_A"] == data_pl["team tag"], True, False)


def positions(position):
    L=[]
    position = position[:2]
    L.append(position)
    print(set(L))
    """
    if 'Attaquant' in position:
        return 'Attaquant'
    elif 'Défenseur' in position:
        return 'Défenseur'
    elif 'Milieu' in position:
        return 'Milieu'
    else:
        return 'Autre'
    """

#data_pl['Emplacement'] = data_pl['Emplacement'].apply(positions)
L=[]
for e in data_pl.itertuples():
    L.append(e.Emplacement[:2])
print(set(L))