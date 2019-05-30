import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops





def recuperation_donnée_température(lieu):

    
    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)

    r = requests.get(localisation)

    data=r.json()

    température = data['main']['temp']
    température = température - 273.15

    
    #print(str(round(température)) + ' Celsius')

    if température < 0:
        return '> 0'
    elif température >= 0 and température <= 10:
        return '0_10'
    elif température >= 10 and température <= 20:
        return '11_20'
    elif température >= 20 and température <= 30:
        return '21_30'
    elif température >= 30 and température <= 40:
        return '31_40'
    elif température >= 40:
        return '41>'

def saison():
    
    date = datetime.datetime.now()
    mois = date.month
    jour = date.day

   
    
    if mois == 12 or mois == 1\
       or mois == 2:
        return 'hiver'

    elif mois == 3 or mois == 4\
         or mois == 5:
        return 'primtemps'

    elif mois == 6 or mois == 7\
         or mois == 8\
         or mois == 9:
        return 'été'

    elif mois == 10 or mois == 11\
         or mois == 12:
        return 'automne'





