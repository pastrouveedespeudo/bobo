"""BS4, requests, datatime 16/04/2019"""

import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color


#Path to site of polenne
PATH_PARIS = 'https://weather.com/fr-FR/forecast/allergy/l/1975528fb7e3553b7eacfe7ac89b421986bb9949c2506b144b4e228d57da124b'
PATH_LYON = 'https://weather.com/fr-FR/forecast/allergy/l/7615c204059d6d10382d733bf8dc1718bcac1e82e2f2cf66e6842581ca9360c2'
PATH_MARSEILLE = 'https://weather.com/fr-FR/forecast/allergy/l/97adc36f89aa35486ece34380b006f2c946ef82fad53a58954c33e39e23948fe'


def polenne(city):

    city = city.lower()

    #according to the city we grant the path
    if city == 'lyon':
        path = PATH_LYON

    elif city == 'paris':
        path = PATH_PARIS
        
    elif city == 'marseille':
        path = PATH_MARSEILLE
    
    #BS4 stuff, we recup all div from the
    #HTML page.
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find_all("div")

    #We searching "Confort de respiration"
    #And take the finding to finding + 200
    
    liste = []
    liste.append(str(Property))
    a = str(liste).find('Confort de respiration:')
    liste = liste[0][a:a+200]

    word = ''
    compa = '<div class="styles__allergyMsg__qual__yaxvL" classname="styles__allergyMsg__qual__yaxvL"'

    liste2 = []

    #Our searched word is just after the compa variable into liste
    #so, we increment mot,
    #if i == > or < (tag) we verify if mot == compa
    #if yes we defining a to True.
    #If a == True, we add to liste2 the world searched.
    
    for i in liste:
        if i == '>':
            if word == compa:
                word = ''
                a = True
            else:
                word =  ''

        elif a == True:
            if i == '<':
                a = False
            liste2.append(i)
        else:
            word += i

    return "".join(liste2[:-1])























