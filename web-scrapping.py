import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scrapping(country, position):
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
                'Name': re.sub('\\n', '', trr[1].text.upper())[:-3]
            }
        except:
            return None
        
    ranking_fifa = pd.DataFrame(list(filter(lambda x: x, map(lambda t: rankingFifa(t), scrapping(url)))))