import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scrapping(country):
    url = "https://www.fifa.com/fifa-world-ranking/ranking-table/men/"
    def scrapping(url):
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        fifa = soup.select('tbody')[0].find_all('tr')
        return fifa
    
    def rankingFifa(t):
        trr = t.find_all('td')
        try:
            return {
                'Position': trr[0].text,
                'Name': re.sub('\\n', '', trr[1].text.upper().strip())[:-3]
            }
        except:
            return None
        
    rfifa = pd.DataFrame(list(filter(lambda x: x, map(lambda t: rankingFifa(t), scrapping(url)))))
    position = rfifa.loc[rfifa['Country']== country, 'Position'].iloc[0]
    return '{} have the {} position in the current Ranking FIFA'.format(country, position)

