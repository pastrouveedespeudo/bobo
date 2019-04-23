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

METEO = {'beau_temps':0,
         'nuageux':0,
         'pluie':0,
}

PRESSION = {'forte':0,
            'faible':0,
            'normale':0,
}

VENT = {'tres fort':0,
        'fort':0,
        'moyen fort':0,
        'faible':0, 
}



class météo:

    def recuperation_donnée(self, lieu):
        self.lieu = lieu

        clé = '5a72ceae1feda40543d5844b2e04a205'
        
        localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(self.lieu,clé)
        r = requests.get(localisation)
        data=r.json()


        méteo = data['weather'][0]['main']

        if méteo == "Rain":
            METEO['pluie'] +=1
        elif méteo == "Clouds":
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

        elif vent <= 12 and vent > 8:
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






if __name__ == "__main__":

    meteo = météo()
    meteo.recuperation_donnée('Paris')


    print(PRESSION, METEO, VENT)
































