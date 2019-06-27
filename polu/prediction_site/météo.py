"""Here we call
weather, wind and pressure functions
for site web"""


import requests
import datetime
import urllib.request
from bs4 import *

from .CONFIG import CLE_OPEN
from .CONFIG import WEATHER_PATH
from .CONFIG import PRESSURE_PATH


def recuperation_donnée_météo(lieu):
    """We recuperate weather with API"""
    
    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    r = requests.get(localisation)
    data=r.json()


    méteo = data['weather'][0]['main']

    if méteo == "Rain" or\
       méteo == 'Thunderstorm':
        return 'pluie'
    
    elif méteo == "Clouds" or\
         méteo == 'Mist' or\
         méteo == 'Haze':
        return 'nuageux'
    
    elif méteo == "Clear":
        return 'beau_temps'

def vent(lieu):
    """We recuperate wind with API"""
    
    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
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
    """We recuperate pressure with API"""

    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    r = requests.get(localisation)
    data=r.json()
    
    date = datetime.datetime.now()
    mois = date.month

    pression = data['main']['pressure']

    
    if pression >= 1030:
        return 'forte'

    elif pression <= 1013:
        return 'faible'

    else:
        return 'normale'

    



































