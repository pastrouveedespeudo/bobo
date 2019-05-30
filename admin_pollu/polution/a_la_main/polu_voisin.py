import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color

from boussole import *
from conteneur_ville import *

#en gros chaque jour tu updates ca dans une database

#et ensuite par le vent tu mattes

def voisin(ville):

    liste1 = []
    nb = []
    path = "https://air.plumelabs.com/fr/live/{}".format(ville)

    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'report__pi-number'})
    for i in propriete:
        liste1.append(i.get_text())
    
    for i in liste1:
        for j in i:
            try:
                j = int(j)
                if j == int(j):
                    nb.append(str(j))
            except:
                pass

    
    nb = ''.join(nb)
    nb = int(nb)


    return nb

def voisinage(liste):

    c = 0
    for i in liste:
    
        if i[0] == 'duisburg-military-golf-club':
            a = voisin('duisburg')
            liste[c].append(a)
            
        elif i[0] == 'antwerp-golf-school':
            a = voisin('antwerp')
            liste[c].append(a)
            
        elif i[0] == 'antwerp-golf-school':
            a = voisin('antwerp')
            liste[c].append(a)
            
        elif i[0] == 'barcelone':
            a = voisin('barcelona')
            liste[c].append(a)

        elif i[0] == 'baselga-del-bondone':
            a = voisin('basel')
            liste[c].append(a)

        else:
            a = voisin(i[0])
            liste[c].append(a)
    

        c+=1

    return liste















