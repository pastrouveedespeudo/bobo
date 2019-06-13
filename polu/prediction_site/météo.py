import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops



def recuperation_donnée_météo(lieu):

    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
    r = requests.get(localisation)
    data=r.json()


    méteo = data['weather'][0]['main']

    if méteo == "Rain" or méteo == 'Thunderstorm':
        return 'pluie'
    elif méteo == "Clouds" or méteo == 'Mist' or méteo == 'Haze':
        return 'nuageux'
    elif méteo == "Clear":
        return 'beau_temps'

def vent(lieu):

    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
    r = requests.get(localisation)
    data=r.json()

    
    try:
        vent_degres = data['wind']['deg']
    except:
        pass

    
    vent = data['wind']['speed']


    if vent <= 3 :
        return 'faible'
        
    elif vent <= 6 and vent > 3:
        return 'moyen fort'

    elif vent <= 8 and vent > 6:
        return 'fort'

    elif vent >= 8:
        return 'tres fort'

def pression(lieu):

    
    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
    r = requests.get(localisation)
    data=r.json()
    
    date = datetime.datetime.now()
    mois = date.month

    pression = data['main']['pressure']

    
    if pression >= 1030:#anti
        return 'forte'

    elif pression <= 1013:
        return 'faible'#depression

    else:
        return 'normale'

    



































