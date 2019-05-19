import os
import cv2
import json
import pyglet
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops





def recuperation_donnée(lieu, CLIMAT):

    
    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)

    r = requests.get(localisation)

    data=r.json()

    température = data['main']['temp']
    température = température - 273.15

    
    #print(str(round(température)) + ' Celsius')

    if température < 0:
        CLIMAT['> 0']+=1
    elif température >= 0 and température <= 10:
        CLIMAT['0_10']+=1
    elif température >= 10 and température <= 20:
        CLIMAT['11_20']+=1
    elif température >= 20 and température <= 30:
        CLIMAT['21_30']+=1
    elif température >= 30 and température <= 40:
        CLIMAT['31_40']+=1
    elif température >= 40:
        CLIMAT['41>']+=1

def saison(SAISON):
    
    date = datetime.datetime.now()
    mois = date.month
    jour = date.day

   
    
    if mois == 12 or mois == 1\
       or mois == 2:
        SAISON['hiver'] += 1 #pollution au bois

    elif mois == 3 or mois == 4\
         or mois == 5:
        SAISON['primtemps'] += 1

    elif mois == 6 or mois == 7\
         or mois == 8\
         or mois == 9:
        SAISON['été'] += 1 

    elif mois == 10 or mois == 11\
         or mois == 12:
        SAISON['automne'] += 1





