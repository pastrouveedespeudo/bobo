"""BS4, requests, datatime 16/04/2019"""




import requests

import urllib.request
from bs4 import *



from .CONFIG import PATH_PARIS_POLENNE
from .CONFIG import PATH_LYON_POLENNE
from .CONFIG import PATH_MARSEILLE_POLENNE
from .CONFIG import COMPA_POELENNE


def path_function(city):
    """Here we define the path"""
    
    city = city.lower()

    path = ''
    
    if city == 'lyon':
        path = PATH_LYON_POLENNE

    elif city == 'paris':
        path = PATH_PARIS_POLENNE
        
    elif city == 'marseille':
        path = PATH_MARSEILLE_POLENNE

    return path 


def soup_function(city):
    """Soup and BS4 call"""
    
    #path_function()
    path = path_function(city)

    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    Property = soup_html.find_all("div")


    liste = []
    liste.append(str(Property))
    
    finding = str(liste).find('Confort de respiration:')
    liste = liste[0][finding:finding + 200]

    return liste

def polenne(city):
    """we are looking for the rate of polenne"""

    #soup_function()
    liste = soup_function(city)

    word = ''
    liste2 = []
    oContinuer = ''
    
    for i in liste:
        if i == '>':
            if word == COMPA_POELENNE:
                word = ''
                oContinuer = True
            else:
                word =  ''

        elif oContinuer == True:
            if i == '<':
                oContinuer = False
            liste2.append(i)
        else:
            word += i

    return "".join(liste2[:-1])




























