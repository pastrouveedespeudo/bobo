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


def vent_voisin(nombre, ville, situ):

  
    if situ == 'ville_haut_gauche':
        path = "https://www.lachainemeteo.com/meteo-royaume-uni/ville-{}/previsions-meteo-{}-aujourdhui"
        
    elif situ == 'ville_haut_droite':
        path = 'https://www.lachainemeteo.com/meteo-belgique/golf-{}/previsions-meteo-{}-aujourdhui'

    elif situ == 'ville_haut_droite2':
        path = 'https://www.lachainemeteo.com/meteo-pays-bas/ville-{}/previsions-meteo-{}-aujourdhui'

    elif situ == 'ville_haut_droite3':
        path = 'https://www.lachainemeteo.com/meteo-suisse/village-{}/previsions-meteo-{}-aujourdhui'

    elif situ == 'ville_haut_droite4' or situ == 'bas_droite6' or situ == 'ville_bas_gauche9':
        path = 'https://www.lachainemeteo.com/meteo-france/ville-{}/previsions-meteo-{}-aujourdhui'

    elif situ == 'ville_haut_droite5':
        path = 'https://www.lachainemeteo.com/meteo-allemagne/ville-{}/previsions-meteo-{}-%28oder%29-aujourdhui'

    elif situ == 'ville_bas_gauche8':
        path = 'https://www.lachainemeteo.com/meteo-espagne/ville-{}/previsions-meteo-{}-aujourdhui'
        
    elif situ == 'ville_bas_droite7':
        path = 'https://www.lachainemeteo.com/meteo-italie/ville-{}/previsions-meteo-{}-aujourdhui'


    path = path.format(nombre, ville)

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'splitData'})

    liste = str(propriete)

    a = str(liste).find('scaleWindOrange"></i>')
    b = str(liste).find('scaleWindRed"></i>')
    aa = str(liste).find('scaleWindYellow"></i>')
    
    if a >= 0:
        code = liste[a:a+200]
    elif b >= 0:
        code = liste[b:b+200]
    elif aa >= 0:
        code = liste[aa:aa+200]
    else:
        code = 'None'
    
    #print(a,b,aa)

    if code == 'None':
        path = 'https://www.lachainemeteo.com/meteo-allemagne/village-{}/previsions-meteo-{}-%28oder%29-aujourdhui'
        path = path.format(nombre, ville)
        r = requests.get(path)

        page = r.content
        soup = BeautifulSoup(page, "html.parser")

        propriete = soup.find_all("div", {'class':'splitData'})

        liste = str(propriete)

        a = str(liste).find('scaleWindOrange"></i>')
        b = str(liste).find('scaleWindRed"></i>')
        aa = str(liste).find('scaleWindYellow"></i>')
        
        if a >= 0:
            code = liste[a:a+200]
        elif b >= 0:
            code = liste[b:b+200]
        elif aa >= 0:
            code = liste[c:c+200]






    
    c = str(code).find('Nord-Nord-Est')
    
    if c >= 0:
        return 'Nord-Nord-Est'

    d = str(code).find('Nord-Est')
    
    if d >= 0:
        return 'Nord-Est'

    e = str(code).find('Est-Nord-Est')
    
    if e >= 0:
        return 'Est-Nord-Est'

    g = str(code).find('Est-Sud-Est')
    
    if g >= 0:
        return 'Est-Sud-Est'

    h = str(code).find('Sud-Est')
    
    if h >= 0:
        return 'Sud-Est'

    i = str(code).find('Sud-Sud-Est')
    
    if i >= 0:
        return 'Sud-Sud-Est'

    k = str(code).find('Sud-Sud-Ouest')
    if k >= 0:
        return 'Sud-Sud-Ouest'

    l = str(code).find('Sud-Ouest')
    
    if l >= 0:
        return 'Sud-Ouest'

    m = str(code).find('Ouest-Sud-Ouest')
    
    if m >= 0:
        return 'Ouest-Sud-Ouest'

    o = str(code).find('Ouest-Nord-Ouest')
    
    if o >= 0:
        return 'Ouest-Nord-Ouest'

    p = str(code).find('Nord-Ouest')
    
    if p >= 0:
        return 'Nord-Ouest'

    q = str(code).find('Nord-Nord-Ouest')
    
    if q >= 0:
        return 'Nord-Nord-Ouest'


    b = str(code).find('Nord')
    
    if b >= 0:
        return 'Nord'

    f = str(code).find('Est')
    
    if f >= 0:
        return 'Est'

    j = str(code).find('Sud')
    
    if j >= 0:
        return 'Sud'

    n = str(code).find('Ouest')
    
    if n >= 0:
        return 'Ouest'

 
    
def traitement_ville(liste, liste1, nom_liste):


    liste2 = []

    c = 0
    for i in liste:
        print(i)
        vent = vent_voisin(str(liste1[c]), i, nom_liste)
        print(vent)
        liste2.append((i, vent))
        
        c+=1
        
    return liste2

    
def apport_pollu():
    
    a = traitement_ville(ville_haut_droite, num_ville1, 'ville_haut_droite')
    b = traitement_ville(ville_haut_gauche, num_ville, 'ville_haut_gauche')
    c = traitement_ville(ville_haut_droite2, num_ville2, 'ville_haut_droite2')
    d =traitement_ville(ville_haut_droite3, num_ville3, 'ville_haut_droite3')
    e =traitement_ville(ville_haut_droite4, num_ville4, 'ville_haut_droite4')
    f =traitement_ville(bas_droite6, num_ville6, 'bas_droite6')
    g =traitement_ville(ville_bas_gauche9, num_ville9, 'ville_bas_gauche9')
    h =traitement_ville(ville_haut_droite5, num_ville5, 'ville_haut_droite5')
    i =traitement_ville(ville_bas_gauche8, num_ville8, 'ville_bas_gauche8')
    j =traitement_ville(ville_bas_droite7, num_ville7, 'ville_bas_droite7')
    
































apport_pollu()















































