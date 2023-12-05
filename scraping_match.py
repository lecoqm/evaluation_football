import bs4
import lxml
import pandas
import urllib

from urllib import request


#Pour l'instant un test de la récupération des infos d'un match
#Ici, ça ne récupère que les infos de la première équipe, et on a les noms des catégories
url_Brighton = "https://fbref.com/fr/matchs/56a137f7/Brighton-and-Hove-Albion-Luton-Town-12-Aout-2023-Premier-League"

def scrap_match(url) : 
    request_text = request.urlopen(url).read()

    page = bs4.BeautifulSoup(request_text, "lxml")
    print(page.find("title").text.strip())

    tableau_resume = page.find(id = "div_stats_d07537b9_summary")
    table_tbody = tableau_resume.find("tbody")
    rows = table_tbody.find_all('tr')
    for ele in rows[0] : 
        print(ele.text.strip())

    for i in range(len(rows)):
        cols = [ele.text.strip() for ele in rows[i]]
        print(cols)

    dico_joueur = dict()
    for i in range(len(rows)):
        cols = [ele.text.strip() for ele in rows[i]]
    if len(cols) > 0 : 
        dico_joueur[cols[0]] = cols[1:]
#dico_joueur

    dico_joueurs = pandas.DataFrame.from_dict(dico_joueur,orient='index')
    return dico_joueurs

scrap_match(url_Brighton)

#Il faut créer les bonnes variables âges
#Il faut ajouter l'ID du joueur
#Il faut donner la ref du match
#Il faut donner les autres catégories

