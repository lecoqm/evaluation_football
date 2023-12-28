import pandas as pd
import numpy as np

data_pl = pd.read_csv("/home/onyxia/work/evaluation_football/data_premierleague_2022_2023_V1.csv")
data_pl["home"] = np.where(data_pl["id_team_A"] == data_pl["team tag"], True, False)

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


data_pl['pts_gagnes'] = data_pl.apply(points_gagnes, axis=1)
data_pl['pts_apportes'] = data_pl['pts_gagnes'] * data_pl["Minutes"] / 90

data_pl.to_csv("/home/onyxia/work/evaluation_football/df_PL.csv")