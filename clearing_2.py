import pandas as pd

path = '/home/onyxia/work/evaluation_football/data/tm.csv'
df = pd.read_csv(path)

df = df.loc[df['0'] != '-']
df = df.reset_index(drop=True)

def str_to_float(str):
    """
    This function convert a string to a float.
    """
    L = str.split()
    L[0] = L[0].replace(",",".")
    if L[1]=='K':
        return float(L[0])*1000
    elif L[1]=='mio.':
        return float(L[0])*1000000
    else :
        return None


df['0'] = df['0'].apply(str_to_float)

df.to_csv("/home/onyxia/work/evaluation_football/data/df_tm.csv")