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

    print(nb)


def voisinage():

    
    for i in ville_haut_droite:
        print(i)
        
        if i == 'duisburg-military-golf-club':
            voisin('duisburg')
        elif i == 'antwerp-golf-school':
            voisin('antwerp')
        elif i == 'antwerp-golf-school':
            voisin('antwerp')
        else:
            voisin(i)

    for i in ville_haut_gauche:
        print(i)
        voisin(i)

    for i in ville_haut_droite2:
        print(i)
        voisin(i)

    for i in ville_haut_droite3:
        print(i)
        voisin(i)
        
    for i in ville_haut_droite4:
        print(i)
        voisin(i)

    for i in bas_droite6:
        print(i)
        voisin(i)
        
    for i in ville_bas_gauche9:
        print(i)
        voisin(i)
        
    for i in ville_haut_droite5:
        print(i)
        voisin(i)
        
    for i in ville_bas_gauche8:
        print(i)
        if i == 'barcelone':
            voisin('barcelona')
        else:
            voisin(i)
        
    for i in ville_bas_droite7:
        print(i)
        if i == 'baselga-del-bondone':
            voisin('basel')
        else:
            voisin(i)

    

voisinage()

















