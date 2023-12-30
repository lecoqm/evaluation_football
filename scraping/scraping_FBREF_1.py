import bs4
import lxml
import json
import urllib
from urllib import request
import time

##########
# Modify:
# The url are exported in a json file
file="/home/onyxia/work/evaluation_football/liste_url.json"   # Path of the json file where the data will be exported
url_first = 'https://fbref.com/fr/matchs/2023-05-28' # url of the first date  2022-08-04
url_end = 'https://fbref.com/fr/matchs/2023-05-29'  # url of the last date (not scrapped)
league = 'Premier League">'   # Use the name in the html code
##########


def scraping(url, url_end, league):
    """This function scraps the reference of each matchs,
    the reference will after be use to find the page of
    the match and to scrap the information of the match."""
    print(url)
    Refs_Matchs = []
    request_text = request.urlopen(url).read() 
    page = bs4.BeautifulSoup(request_text, 'lxml')
    L1=page.find_all('div',class_ = 'table_wrapper')
    L2=[]
    for e in L1:
        L2.append(e.find('span').text)
    if league in L2:
        urls_matchs=L1[L2.index(league)].find_all('td',attrs={'data-stat' : 'match_report'})
        for e in urls_matchs:
            Refs_Matchs.append(e.find('a')['href'].split('/')[3])   # Take the reference of the match, it is enough to find the page of the match
    # go to the next page
    url='https://fbref.com'+page.find('a',class_ = 'button2 next')['href']
    if url!=url_end:
        time.sleep(7)
        scraping(url, url_end, league)
    print(Refs_Matchs)
    return Refs_Matchs


# We parse all the page between two dates and scrap the urls
# of all the matches in a league
Refs_Matchs = scraping(url_first, url_end, league)
print(Refs_Matchs)
#with open(file, "w") as f:
#    json.dump(Refs_Matchs, f)