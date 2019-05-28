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
     
        vent = vent_voisin(str(liste1[c]), i, nom_liste)
        liste2.append((i, vent))
        
        c+=1



    return liste2



def apport_pollu_vent(vent, liste_dir):

    for i in liste_dir:
        if vent == i:
            return True


def traitement_liste(liste, liste_ville):

    liste1 = []

    for i in liste:
        a = apport_pollu_vent(i[1], liste_ville)
        if a == True:
            liste1.append(i[0])

    return liste1



def traitement_liste_France(liste, liste_ville):

    liste1 = []

    for i in liste:
 
        if i[0] == i: 
            a = apport_pollu_vent(i[1], direction_ville4)
            if a == True:
                liste1.append(i[0])
            
        else:
            a = apport_pollu_vent(i[1], direction_ville44)
            
            if a == True:
                liste1.append(i[0])

    return liste1


    
def apport_pollu():

    liste = []
    
    a = traitement_ville(ville_haut_droite, num_ville1, 'ville_haut_droite')
    aa = traitement_liste(a, direction_ville1)
    
    
    b = traitement_ville(ville_haut_gauche, num_ville, 'ville_haut_gauche')
    bb = traitement_liste(b, direction_ville)


    c = traitement_ville(ville_haut_droite2, num_ville2, 'ville_haut_droite2')
    cc = traitement_liste(c, direction_ville2)

    
    d =traitement_ville(ville_haut_droite3, num_ville3, 'ville_haut_droite3')
    dd = traitement_liste(d, direction_ville3)

    
    e = traitement_ville(ville_haut_droite4, num_ville4, 'ville_haut_droite4')
    ee = traitement_liste_France(e, direction_ville4)
    
    
    f =traitement_ville(bas_droite6, num_ville6, 'bas_droite6')
    ff = traitement_liste(f, direction_ville6)

    
    g =traitement_ville(ville_bas_gauche9, num_ville9, 'ville_bas_gauche9')
    gg = traitement_liste(g, direction_ville9)
    
    h =traitement_ville(ville_haut_droite5, num_ville5, 'ville_haut_droite5')
    hh = traitement_liste(h, direction_ville5)
    
    i =traitement_ville(ville_bas_gauche8, num_ville8, 'ville_bas_gauche8')
    ii = traitement_liste(i, direction_ville8)
    
    j =traitement_ville(ville_bas_droite7, num_ville7, 'ville_bas_droite7')
    jj = traitement_liste(j, direction_ville7)


    liste.extend((aa,bb,cc,dd,ee,ff,gg,ii,jj))
    print(liste)
    return liste


apport_pollu()















































