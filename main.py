import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import argparse
import src.cleaning as cl
import src.webscrapping as wb

def parse():    
    parser = argparse.ArgumentParser(description='Give you back the position of a country in the current ranking FIFA compared to its results in the last 30 years.')
    parser.add_argument('--country', help='Insert the name of the country in English and capital letters')
    args = parser.parse_args()
    return args

def main():
    args = parse()
    last30years = cl.database(args.country)
    print(last30years)
    fifar = wb.web_scrapping(args.country)
    print(fifar)
    
if __name__ == '__main__':
    main()