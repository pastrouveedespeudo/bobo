import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
import datetime

def periode_angrais():

    mois_angrais = [5,6]


    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    for i in mois_angrais:
        if mois == i:
            return 'oui'
            break






