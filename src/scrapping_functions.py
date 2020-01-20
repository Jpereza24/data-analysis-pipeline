import requests
from bs4 import BeautifulSoup
import re

def scrapping(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    fifa = soup.select('tbody')[0].find_all('tr')
    return fifa

def rankingFifa(t):
    trr= t.find_all('td')
    try:
        return {
            "Position": trr[0].text,
            "Country": re.sub('\\n', '',trr[1].text.upper().strip())[:-3]
        }
    except:
        return None