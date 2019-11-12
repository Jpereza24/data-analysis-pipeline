import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scrapping(c1, c2):
    url = "https://www.fifa.com/fifa-world-ranking/ranking-table/men/"
    def scrapping(url):
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.select('tbody')[0].find_all('tr')
        return result
    
    def rankingFifa(t):
        trr = t.find_all('td')
        try:
            return {
                'Position': trr[0].text,
                'Country': re.sub('\\n', '', trr[1].text.upper().strip())[:-3]
            }
        except:
            return None
        
    rfifa = pd.DataFrame(list(filter(lambda x: x, map(lambda t: rankingFifa(t), scrapping(url)))))
    p1 = list(rfifa.loc[rfifa['Country']== c1, 'Position'])
    p1 = p1[0]
    p2 = list(rfifa.loc[rfifa['Country']== c2, 'Position'])
    p2 = p2[0]
    return '{} have the {}th position and {} have the {}th in the current Ranking FIFA.'.format(c1, p1,c2,p2)

