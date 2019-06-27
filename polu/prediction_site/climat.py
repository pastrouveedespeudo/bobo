"""This is file for prediction site web
We'll mesure temperature and the current season"""

import requests
import datetime
import urllib.request
from bs4 import *

from .CONFIG import *



def recuperation_donnée_température(lieu):
    """We recuperate the temperature"""
    
    localisation = PATH_TEMP.format(lieu,CLE_OPEN)

    requests_html = requests.get(localisation)

    data = requests_html.json()

    température = data['main']['temp']
    température = température - 273.15

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
    """We recuperate the season"""

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





