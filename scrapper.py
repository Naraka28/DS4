"""
Web scrapper
"""
import requests
from bs4 import BeautifulSoup

def scrap(URL:str):
    page=requests.get(URL)
    return page
