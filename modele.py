import pandas as pd
import numpy as np

data_pl = pd.read_csv("/home/onyxia/work/evaluation_football/df_PL.csv")

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


x = data_pl['Buts'].values.reshape(-1,1)
y = data_pl['pts_apportes'].values.reshape(-1,1)

def reg_simple(x,y):
    reg = linear_model.LinearRegression()
    reg.fit(x, y)
    y_pred = reg.predict(x)

    slope = reg.coef_[0]
    mse = mean_squared_error(y,y_pred)
    r2 = r2_score(y,y_pred)
    
    return slope, mse, r2

print(reg_simple(x,y))