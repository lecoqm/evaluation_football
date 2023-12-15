

import bs4
import lxml
import pandas as pd
import urllib

from urllib import request


#Pour l'instant un test de la récupération des infos d'un match
#Ici, ça ne récupère que les infos de la première équipe, et on a les noms des catégories
url_Brighton = "https://fbref.com/fr/matchs/56a137f7/Brighton-and-Hove-Albion-Luton-Town-12-Aout-2023-Premier-League"


#Les différentes tables de statistiques
#Elles sont cachées sur le site mais disponibles dans le code html
list_table = ["summary","passing","passing_types","defense","possession","misc"]

#Scrap les informations d'une des tables qui nous intéressent
def scrap_table(url,table):

    #On récupère le text de la page
    request_text = request.urlopen(url).read() 
    page = bs4.BeautifulSoup(request_text, "lxml")
    #print(page.find("title").text.strip())

    
    #On trouve les id des deux équipes des deux équipes
    List_link = []
    scorebox = page.find("div", {"class": "scorebox"})
    strong_scorebox = scorebox.find_all('strong', {'class': None})
    for tag in strong_scorebox :
        team = tag.find("a")
        if team :
            link = team.get('href')
            List_link.append(link)

    Tag_team = []
    for link in List_link[:len(List_link)-1]: #Il y a un troisième élément indésirable
        elements = link.split('/')
        Tag_team.append(elements[3])
        
    #On récupère la table pour chacune des deux équipes
    final_table = pd.DataFrame()

    for tag in Tag_team : 
        idtable = "div_stats_" + tag + "_" + table
        #print(idtable)
        tableau_resume = page.find(id = idtable)
        table_tbody = tableau_resume.find("tbody")
        rows = table_tbody.find_all('tr')

        dico_joueur = dict()
        for i in range(len(rows)):
            tag_player = rows[i].find("th")['data-append-csv']
            cols = [ele.text.strip() for ele in rows[i]]
            cols.insert(0,tag_player)
            if len(cols) > 0 : 
                dico_joueur[cols[0]] = cols[1:]
        
        
        header = tableau_resume.find("thead")
        var = header.find_all('tr')
        var2 = var[1].find_all("th")
        var_list = [(var2[i]['aria-label']) for i in range(len(var2))]

        #On fusionne les tables
        
        table_tag = (pd.DataFrame.from_dict(dico_joueur,orient='index'))
        table_tag.columns = var_list
        table_tag['match tag'] = tag
        table_tag['player tag'] = table_tag.index.tolist()
        #Add the player tag
        final_table = pd.concat([final_table,table_tag], ignore_index = False)
    
    #Il faut ajouter le nom des joueurs et leur tag
    #Il faut ajouter le titre des colonnes
    #Il faut récupérer les légendes
    return final_table

tt = scrap_table(url_Brighton,"passing_types")
#print(tt)

def scrap_match(url,table_list):

    match_table = scrap_table(url,table_list[0])

    for table in range(1,len(table_list)):
        type_table = scrap_table(url,table_list[table])
        match_table = pd.merge(match_table, type_table)
    return match_table

ttt = scrap_match(url_Brighton,list_table)
print(ttt)


#Il faut créer les bonnes variables âges
#Il faut ajouter l'ID du joueur
#Il faut donner la ref du match
#Il faut donner les autres catégories

