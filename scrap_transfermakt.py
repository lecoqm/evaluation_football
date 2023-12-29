import bs4
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import urllib

import requests



headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})
Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})
Age = pageSoup.find_all("td", {"class": "zentriert"})


def scrap_team_value(url):

    #On récupère le text de la page
    request_text = requests.get(url, headers = headers) 
    page = BeautifulSoup(request_text.content, 'html.parser')

    dico_value = dict()
    table = page.find(id = "yw1")
    table_values = table.find("tbody")
    names_values = table_values.find_all('td',{"class": "hauptlink"})
    List_names_values = [ele.text.strip() for ele in names_values]
    List_names = [List_names_values[2*i] for i in range(int(len(List_names_values)/2))]
    List_values = [List_names_values[2*i + 1] for i in range(int(len(List_names_values)/2))]
    attributes = table_values.find_all('td',{"class": "zentriert"})
    List_attributes = [ele.text.strip() for ele in attributes]
    List_age = [List_attributes[4*i+1] for i in range(int(len(List_attributes)/4))]

    length = len(List_age)

    for i in range(length):
        dico_value[List_names[i]] = [List_values[i],List_age[i]]

    return dico_value

print(scrap_team_value("https://www.transfermarkt.fr/manchester-city/startseite/verein/281/saison_id/2022"))