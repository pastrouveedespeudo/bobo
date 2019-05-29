import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color



PATH_PARIS = 'https://weather.com/fr-FR/forecast/allergy/l/1975528fb7e3553b7eacfe7ac89b421986bb9949c2506b144b4e228d57da124b'
PATH_LYON = 'https://weather.com/fr-FR/forecast/allergy/l/7615c204059d6d10382d733bf8dc1718bcac1e82e2f2cf66e6842581ca9360c2'
PATH_MARSEILLE = 'https://weather.com/fr-FR/forecast/allergy/l/97adc36f89aa35486ece34380b006f2c946ef82fad53a58954c33e39e23948fe'


def polenne(ville):

    ville = ville.lower()

    if ville == 'lyon':
        path = PATH_LYON

    elif ville == 'paris':
        path = PATH_PARIS
        
    elif ville == 'marseille':
        path = PATH_MARSEILLE
    

    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div")

    liste = []
    liste.append(str(propriete))
    a = str(liste).find('Confort de respiration:')

    liste = liste[0][a:a+200]

    mot = ''
    compa = '<div class="styles__allergyMsg__qual__yaxvL" classname="styles__allergyMsg__qual__yaxvL"'

    liste2 = []


    for i in liste:
        if i == '>':
            if mot == compa:
                mot = ''
                a = True
            else:
                mot =  ''

        elif a == True:
            if i == '<':
                a = False
            liste2.append(i)
        else:
            mot += i
        
    print("".join(liste2[:-1]))


polenne('lyon')

























