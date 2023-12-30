import bs4
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import urllib
import time

import requests


#On définit un headers nécessaire
headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


def scrap_team_value(url):
    """
    Récupère les valeurs de tous les joueurs d'une équipe
        """

    #On récupère le text de la page
    request_text = requests.get(url, headers = headers) 
    page = BeautifulSoup(request_text.content, 'html.parser')

    #On recupère les données sous forme d'un dictionnaire avec en clés, les noms et en valeur les valeurs des joueurs
    dico_value = dict()
    table = page.find(id="yw1")
    table_values = table.find("tbody")
    names_values = table_values.find_all('td', {"class": "hauptlink"})
    List_names_values = [ele.text.strip() for ele in names_values] #On a une liste de la forme Joueur A, valeur A, joueur B, valeur B
    List_names = [List_names_values[2*i] for i in range(int(len(List_names_values)/2))]
    List_values = [List_names_values[2*i + 1] for i in range(int(len(List_names_values)/2))]

    #On rajoute l'âge du joueur dans l'idée d'un merge futur
    attributes = table_values.find_all('td', {"class": "zentriert"})
    List_attributes = [ele.text.strip() for ele in attributes]
    List_age = [List_attributes[4*i+1] for i in range(int(len(List_attributes)/4))]

    length = len(List_age)

    for i in range(length):
        dico_value[List_names[i]] = [List_values[i],List_age[i]]

    return dico_value

#print(scrap_team_value("https://www.transfermarkt.fr/manchester-city/startseite/verein/281/saison_id/2022"))


def scrap_value_league(url) :
    """
    Pour une ligue donnée sur une année donnée (correspond à une url), renvoie la valeur de tous
    les joueurs de toutes les équipes de la ligue
    """

    request_text = requests.get(url, headers=headers) 
    page = BeautifulSoup(request_text.content, 'html.parser')

    #On récupère la liste des équipes
    List_url_team  = []
    table = page.find(id="yw1")
    table_values = table.find("tbody")
    List_link = table_values.find_all('td',{"class": "zentriert no-border-rechts"})
    for e in List_link:
            List_url_team.append("https://www.transfermarkt.fr" + e.find('a')['href'])
    #print(List_url_team)
    value_league = pd.DataFrame()

    #On itère sur chaque équipe pour récupèrer les données et concaténer 
    for team in List_url_team :
        print(team)
        time.sleep(3)
        dict_team = scrap_team_value(team)
        df_team = pd.DataFrame.from_dict(dict_team,orient='index')
        value_league = pd.concat([value_league,df_team], ignore_index = False)

    return value_league

#Test
#Ci dessous, cela lance le scrap de toute la premier league anglaise sur la saison 2022-2023
#TM= scrap_value_league("https://www.transfermarkt.fr/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2022")
#TM.to_csv("/home/onyxia/work/evaluation_football/tm.csv")

