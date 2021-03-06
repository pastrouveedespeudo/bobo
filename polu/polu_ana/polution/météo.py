import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops



def recuperation_donnée_météo(lieu, METEO, VENT, PRESSION):

    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
    r = requests.get(localisation)
    data=r.json()


    méteo = data['weather'][0]['main']
    print(méteo)
    if méteo == "Rain" or méteo == 'Thunderstorm':
        METEO['pluie'] +=1
    elif méteo == "Clouds" or méteo == 'Mist' or méteo == 'Haze':
        METEO['nuageux'] +=1
    elif méteo == "Clear":
        METEO['beau_temps'] +=1


    try:
        vent_degres = data['wind']['deg']
    except:
        pass

    
    vent = data['wind']['speed']


    if vent <= 3 :
        VENT['faible'] += 1
        
    elif vent <= 6 and vent > 3:
        VENT['moyen fort'] += 1

    elif vent <= 8 and vent > 6:
        VENT['fort'] += 1

    elif vent >= 8:
        VENT['tres fort'] += 1


    date = datetime.datetime.now()
    mois = date.month

    pression = data['main']['pressure']

    
    if pression >= 1030:#anti
        PRESSION['forte'] += 1

    elif pression <= 1013:
        PRESSION['faible'] += 1#depression

    else:
        PRESSION['normale'] += 1

    



































