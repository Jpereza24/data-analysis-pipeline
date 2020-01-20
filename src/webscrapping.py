import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from src import scrapping_functions as sf

def web_scrapping(c1, c2):
    url = "https://www.fifa.com/fifa-world-ranking/ranking-table/men/"
        
    rfifa = pd.DataFrame(list(filter(lambda x: x, map(lambda t: sf.rankingFifa(t), sf.scrapping(url)))))
    p1 = list(rfifa.loc[rfifa['Country']== c1, 'Position'])
    p1 = p1[0]
    p2 = list(rfifa.loc[rfifa['Country']== c2, 'Position'])
    p2 = p2[0]
    return '{} have the {}th position and {} have the {}th in the current Ranking FIFA.'.format(c1, p1,c2,p2)

