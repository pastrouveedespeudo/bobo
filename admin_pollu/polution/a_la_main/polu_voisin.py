import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color

from boussole import *


#https://www.lachainemeteo.com/meteo-royaume-uni/ville-548409/previsions-meteo-london-colney-aujourdhui
ville_haut_gauche = ['london', 'plymouth', 'cardiff', 'swansea', 'antwerp',
                     'leeds', 'liverpool']

num_ville = [2, 40, 5746, 76, 9832, 6, 89]


#https://www.lachainemeteo.com/meteo-belgique/golf-3490/previsions-meteo-duisburg-military-golf-club-aujourdhui
ville_haut_droite = ['koln', 'duisburg', 'frankfurt',
                       'antwerp', 'bruxelles',
                     'liege', 'antwerp']
num_ville1 = [225775, 3490, 9832, 6487,6557,9832]


#https://www.lachainemeteo.com/meteo-pays-bas/ville-3732/previsions-meteo-amsterdam-aujourdhui
ville_haut_droite2 = ['amsterdam', 'rotterdam']
num_ville2 = [3732, 776]

#https://www.lachainemeteo.com/meteo-suisse/village-874436/previsions-meteo-aachen-aujourdhui

ville_haut_droite3 = ['aachen','bern', 'zurich']
num_ville3 = [874436, 44, 2097]


#https://www.lachainemeteo.com/meteo-france/ville-312/previsions-meteo-lille-aujourdhui
ville_haut_droite4 = ['lille', 'mulhouse', 'strasbourg' ]
num_ville4 = [312, 18193, 309]

bas_droite = ['nice']#
num_ville= [6590]



#https://www.lachainemeteo.com/meteo-allemagne/ville-33772/previsions-meteo-frankfurt-%28oder%29-aujourdhui
ville_haut_droite5 = ['mainz', 'frankfurt', 'freiburg']
num_ville5 = [2425,33772, 2598553]



#https://www.lachainemeteo.com/meteo-italie/ville-443727/previsions-meteo-baselga-del-bondone-aujourdhui
ville_bas_droite = ['basel', 'torino']
num_ville5 = [443727,2558109, ]




#https://www.lachainemeteo.com/meteo-espagne/village-1498961/previsions-meteo-cartagena-aujourdhui
ville_bas_gauche = ['cartagena','barcelone','vigo',
                    'san-sebastian',
                    'bilbao','santander','gijon','oviedo','la-coruna']
num_ville5 = [1498961,2558109,1519,1045, 2896, 356, 266, 5217,5217,4099]


#https://www.lachainemeteo.com/meteo-france/ville-312/previsions-meteo-lille-aujourdhui
ville_bas_gauche =['perpignan'

num_ville_5 = [6510]


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





def vent_voisin(nombre, ville):
    
    path = "https://www.lachainemeteo.com/meteo-royaume-uni/ville-{}/previsions-meteo-{}-aujourdhui".format(nombre, ville)

    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'splitData'})
    
    liste = str(propriete)
    
    a = str(liste).find('<i alt="Vent NW" class="icon icon-DirectionArrowNW scaleWindOrange"></i>')
    code = liste[a:a+200]

    print(code)



    c = str(code).find('Nord-Nord-Est')
    
    if c >= 0:
        print(c,'c')
        return 'Nord-Nord-Est'

    d = str(code).find('Nord-Est')
    
    if d >= 0:
        print(d, 'd')
        return 'Nord-Est'

    e = str(code).find('Est-Nord-Est')
    
    if e >= 0:
        print(e, 'e')
        return 'Est-Nord-Est'

    g = str(code).find('Est-Sud-Est')
    
    if g >= 0:
        print(g,'g')
        return 'Est-Sud-Est'

    h = str(code).find('Sud-Est')
    
    if h >= 0:
        print(h,'h')
        return 'Sud-Est'

    i = str(code).find('Sud-Sud-Est')
    
    if i >= 0:
        print(i,'i')
        return 'Sud-Sud-Est'

    k = str(code).find('Sud-Sud-Ouest')
    if k >= 0:
        print(k,'i')
        return 'Sud-Sud-Ouest'

    l = str(code).find('Sud-Ouest')
    
    if l >= 0:
        print(l,'l')
        return 'Sud-Ouest'

    m = str(code).find('Ouest-Sud-Ouest')
    
    if m >= 0:
        print(m,'m')
        return 'Ouest-Sud-Ouest'

    o = str(code).find('Ouest-Nord-Ouest')
    
    if o >= 0:
        print(o,'o')
        return 'Ouest-Nord-Ouest'

    p = str(code).find('Nord-Ouest')
    
    if p >= 0:
        print(p,'p')
        return 'Nord-Ouest'

    q = str(code).find('Nord-Nord-Ouest')
    
    if q >= 0:
        print(q,'q')
        return 'Nord-Nord-Ouest'



    b = str(code).find('Nord')
    
    if b >= 0:
        print(b,'b')
        return 'Nord'

    f = str(code).find('Est')
    
    if f >= 0:
        print(f, 'f')
        return 'Est'

    j = str(code).find('Sud')
    
    if j >= 0:
        print(j,'j')
        return 'Sud'

    n = str(code).find('Ouest')
    
    if n >= 0:
        print(n,'n')
        return 'Ouest'

 
    


vent = vent_voisin(2, 'london')
print(vent)



    

##for i in ville_haut_gauche:
##    print(i)
##    voisin(i)
##    vent_voisin(i)
##
##for i in ville_haut_droite:
##    print(i)
##    voisin(i)
##    vent_voisin(i)
##
##for i in ville_bas_droite:
##    print(i)
##    voisin(i)
##    vent_voisin(i)
##    
##for i in ville_bas_gauche:
##    print(i)
##    voisin(i)
##    vent_voisin(i)
##















