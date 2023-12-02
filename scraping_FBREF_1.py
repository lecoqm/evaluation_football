import bs4
import lxml
import json
import urllib

from urllib import request

def scraping(url, url_end, league):
    # scrap the urls
    request_text = request.urlopen(url).read() 
    page = bs4.BeautifulSoup(request_text, 'lxml')
    L1=page.find_all('div',class_ = 'table_wrapper')
    L2=[]
    for e in L1:
        L2.append(e.find('span').text)
    if league in L2:
        urls_matchs=L1[L2.index(league)].find_all('td',attrs={'data-stat' : 'match_report'})
        for e in urls_matchs:
            Urls_Matchs.append(e.find('a')['href'])
    # go to the next page
    url='https://fbref.com'+page.find('a',class_ = 'button2 next')['href']
    if url!=url_end:
        scraping(url, url_end, league)

# We parse all the page between two dates and scrap the urls
# of all the matches in a league
Urls_Matchs=[]
url_first = 'https://fbref.com/fr/matchs/2022-10-01' # url of the first date
url_end = 'https://fbref.com/fr/matchs/2022-10-02'  # url of the last date (not scrapped)
league = 'Premier League">'

scraping(url_first, url_end, league)

# The url are exported in a json file
file="liste_url.json"

with open(file, "w") as f:
    json.dump(Urls_Matchs, f)