import json
import bs4
import lxml
import pandas as pd
import urllib
import time

from urllib import request
from scraping_match import scrap_match
#Scrap tous les match d'une ligue donnée pour une année donnée

list_table = ["summary","passing","passing_types","defense","possession","misc"]

def scrap_ligue(file):
    # On récupère les matchs à scraper
    json_file = open(file)
    match_list = json.load(json_file)
    df_league = pd.DataFrame()
    print(match_list)

    for tag in match_list:
        print(tag)
        # time.sleep nécesaire pour éviter de se faire bloquer
        time.sleep(5)
        url_match = 'https://fbref.com/fr/matchs/' + tag
        # On récupère les éléments présents dans le tableau récapitulatif du match
        match_table = scrap_match(url_match,list_table)
        df_league = pd.concat([df_league,match_table], ignore_index = False)
    
    return df_league

# Test, attention prend une quarantaine de minutes

#PL_2022_2023 = scrap_ligue("/home/onyxia/work/evaluation_football/liste_url.json")
#PL_2022_2023.to_csv("/home/onyxia/work/evaluation_football/data_premierleague_2022_2023_V3.csv")


