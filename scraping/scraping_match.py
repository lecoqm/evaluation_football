

import bs4
import lxml
import pandas as pd
import urllib

from urllib import request



#Les différentes tables de statistiques
#Elles sont cachées sur le site mais disponibles dans le code html
list_table = ["summary","passing","passing_types","defense","possession","misc"]


def scrap_match(url,table_list):
    """
        Retourne le dataframe des statistiques d'un match (pour toutes les tables de statistiques dans table_list)

    """

    #On récupère le text de la page
    request_text = request.urlopen(url).read() 
    page = bs4.BeautifulSoup(request_text, "lxml")

    def scrap_table(table):
        """
            Cette fonction récupère le dataframe d'une des tables de statistiques
        """
 
        #On trouve les id des deux équipes des deux équipes
        List_link = []
        scorebox = page.find("div", {"class": "scorebox"})
        strong_scorebox = scorebox.find_all('strong', {'class': None})
        for tag in strong_scorebox :
            team = tag.find("a")
            if team :
                link = team.get('href') #On récupère les urls des pages des deux équipes
                List_link.append(link)

        Tag_team = []
        for link in List_link[:len(List_link)-1]: #Il y a un troisième élément indésirable
            elements = link.split('/')
            Tag_team.append(elements[3]) #On recupère le tag de l'équipe

        #On récupère le score du match dans une liste dans le même ordre que les tag d'équipes
        all_score = scorebox.find_all('div',{"class": "score"})
        match_score = [int(score.text) for score in all_score]
        #On récupère la table pour chacune des deux équipes
        final_table = pd.DataFrame()

        for tag in Tag_team : 
            idtable = "div_stats_" + tag + "_" + table #l'id de la table utilise le tag de la team
            tableau_resume = page.find(id = idtable)
            table_tbody = tableau_resume.find("tbody")
            rows = table_tbody.find_all('tr')

            dico_joueur = dict()
            for i in range(len(rows)):
                tag_player = rows[i].find("th")['data-append-csv']
                cols = [ele.text.strip() for ele in rows[i]] #on récupère sur chaque ligne toutes les stats
                cols.insert(0,tag_player)
                if len(cols) > 0 : 
                    dico_joueur[cols[0]] = cols[1:]
        
            #On recupère le nom de chaque colonne
            header = tableau_resume.find("thead")
            var = header.find_all('tr')
            var2 = var[1].find_all("th")
            var_list = [(var2[i]['aria-label']) for i in range(len(var2))]

            #On concatène les tables des deux équipes
        
            table_tag = (pd.DataFrame.from_dict(dico_joueur,orient='index'))
            table_tag.columns = var_list
            table_tag['team tag'] = tag
            table_tag['match tag'] = url.split('/')[5]
            table_tag['player tag'] = table_tag.index.tolist() #Add the player tag
            final_table = pd.concat([final_table,table_tag], ignore_index = False)
    
        #On ajoute le score de chaque équipe
        final_table['id_team_A'] = Tag_team[0]
        final_table['score_team_A'] = match_score[0]
        final_table['id_team_B'] = Tag_team[1]
        final_table['score_team_B'] = match_score[1]

        return final_table

    #On recupère la première table
    match_table = scrap_table(table_list[0])

    #on ajoute ensuite toutes les autres tables avec des merge   
    for table in range(1,len(table_list)):
        type_table = scrap_table(table_list[table])
        suffix = ['score_team_A', 'id_team_B', 'Âge', 
                    'match tag', 'id_team_A', 'Emplacement', 
                    'Nation', 'Minutes', 'player tag', 
                    'score_team_B', 'Numéro de maillot', "team tag"] # les colonnes qui se répètent de table en table
        type_table = type_table.drop(columns=suffix)
        match_table = pd.merge(match_table, type_table, on = "Joueur")
    return match_table

#Test possible
#url_Brighton = "https://fbref.com/fr/matchs/56a137f7/Brighton-and-Hove-Albion-Luton-Town-12-Aout-2023-Premier-League"
#ttt = scrap_match(url_Brighton,list_table)
#print(ttt)