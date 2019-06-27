import requests
import urllib.request
from bs4 import *
import datetime

from .CONFIG import CLE_OPEN
from .CONFIG import PATH_TEMP
from .CONFIG import PATH_WEATHER
from .CONFIG import PATH_WIND
from .CONFIG import PATH_PRESSURE

def recuperation_donnée_météo(lieu):


    localisation = PATH_WEATHER.format(lieu, CLE_OPEN)
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

    localisation = PATH_WIND.format(lieu, CLE_OPEN)
    r = requests.get(localisation)
    data=r.json()

    
    try:
        vent_degres = data['wind']['deg']
    except:
        pass

    vent = data['wind']['speed']

    if vent <= 3 :
        return 'faible'
        
    elif vent <= 6 and\
         vent > 3:
        return 'moyen fort'

    elif vent <= 8 and\
         vent > 6:
        return 'fort'

    elif vent >= 8:
        return 'tres fort'



def pression(lieu):

    localisation = PATH_PRESSURE.format(lieu, CLE_OPEN)
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




































