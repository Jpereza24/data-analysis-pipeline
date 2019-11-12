import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import argparse
import src.cleaning as cl
import src.webscrapping as wb

def parse():    
    parser = argparse.ArgumentParser(description='Give you back the position of two countries in the current ranking FIFA compared to its results in the last 30 years.')
    parser.add_argument('--c1', help='Insert the name of the first country in English and capital letters')
    parser.add_argument('--c2', help='Insert the name of the second country in English and capital letters')
    args = parser.parse_args()
    return args

def main():
    args = parse()
    last30years = cl.database(args.c1, args.c2)
    print(last30years)
    fifar = wb.web_scrapping(args.c1, args.c2)
    print(fifar)
    
if __name__ == '__main__':
    main()