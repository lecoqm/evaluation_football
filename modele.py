import pandas as pd
import numpy as np

data_pl = pd.read_csv("/home/onyxia/work/evaluation_football/df_PL.csv")

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def buts_equipe(row):
    if row["id_team_A"] == row["team tag"]:
        return row['score_team_A']
    else:
        return row['score_team_B']

data_pl['buts_equipes'] = data_pl.apply(buts_equipe, axis=1)

data_pl_2 = data_pl[data_pl['Emplacement'] == 'FW']
data_pl_2['home_num'] = np.where(data_pl_2['home'] == True, 1,0)

#print(data_pl_2.columns[:10])
#print(data_pl_2.columns[10:20])
x = data_pl_2[data_pl_2.columns[8:20]]
#x = data_pl_2[['home_num','Minutes']]
y = data_pl_2['buts_equipes'].values.reshape(-1,1)

def reg_simple(x,y):
    reg = linear_model.LinearRegression()
    reg.fit(x, y)
    y_pred = reg.predict(x)

    slope = reg.coef_[0]
    mse = mean_squared_error(y,y_pred)
    r2 = r2_score(y,y_pred)
    
    return slope, mse, r2

print(reg_simple(x,y))

