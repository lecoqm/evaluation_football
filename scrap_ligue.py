import json
import bs4
import lxml
import pandas as pd
import urllib
import time

from urllib import request
from scraping_match import scrap_table
from scraping_match import scrap_match
#Scrap tous les match d'une ligue donnée pour une année donnée

list_table = ["summary","passing","passing_types","defense","possession","misc"]

def scrap_ligue(file):
    json_file = open(file)
    match_list = json.load(json_file)
    df_league = pd.DataFrame()
    print(match_list)

    for tag in match_list :
        print(tag)
        time.sleep(36)
        url_match = 'https://fbref.com/fr/matchs/' + tag
        match_table = scrap_match(url_match,list_table)
        pd.concat([df_league,match_table], ignore_index = False)
    
    return df_league

 
scrap_ligue("/home/onyxia/work/evaluation_football/liste_url.json")
print(scrap_ligue)
