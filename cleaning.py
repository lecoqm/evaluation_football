import pandas as pd
import numpy as np

data_pl = pd.read_csv("/home/onyxia/work/evaluation_football/data/data_premierleague_2022_2023_V2.csv")
data_pl["home"] = np.where(data_pl["id_team_A"] == data_pl["team tag"], True, False)

# eliminate Goal Keepers
data_pl = data_pl.loc[data_pl['Emplacement'] != 'GK']
data_pl = data_pl.reset_index(drop=True)

def points_gagnes(row):
    if row["id_team_A"] == row["team tag"]:
        if row["score_team_A"] > row["score_team_B"]:
            return 3
        elif row["score_team_A"] == row["score_team_B"]:
            return 1
        else: 
            return 0
    else:
        if row["score_team_B"] > row["score_team_A"]:
            return 3
        elif row["score_team_B"] == row["score_team_A"]:
            return 1
        else:
            return 0

def positions(position):
    """
    This function is used to replace the position of each players by a simpler one.
    The only position left are : "Attaquant", "Défenseur" and "Milieu".
    """
    position = position[:2]
    if position in ['FW','LW','RW']:
        return 'Attaquant'
    elif position in ['DF','FB','LB','RB','CB','WB']:
        return 'Défenseur'
    elif position in ['MF','AM','DM','CM','LM','RM','WM']:
        return 'Milieu'

data_pl['Emplacement'] = data_pl['Emplacement'].apply(positions)

data_pl['pts_gagnes'] = data_pl.apply(points_gagnes, axis=1)
data_pl['pts_apportes'] = data_pl['pts_gagnes'] * data_pl["Minutes"] / 90

data_pl.to_csv("/home/onyxia/work/evaluation_football/data/df_PL.csv")