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

from polu_voisin import *

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
            code = liste[aa:aa+200]
        
        
        
    
    c = str(code).find('Nord-Nord-Est')
    if c >= 0:
        DIR = vent_m_s(path)
        return 'Nord-Nord-Est', DIR

    d = str(code).find('Nord-Est')
    
    if d >= 0:
        DIR = vent_m_s(path)
        return 'Nord-Est', DIR

    e = str(code).find('Est-Nord-Est')
    
    if e >= 0:
        DIR = vent_m_s(path)
        return 'Est-Nord-Est', DIR

    g = str(code).find('Est-Sud-Est')
    
    if g >= 0:
        DIR = vent_m_s(path)
        return 'Est-Sud-Est', DIR

    h = str(code).find('Sud-Est')
    
    if h >= 0:
        DIR = vent_m_s(path)
        return 'Sud-Est', DIR

    i = str(code).find('Sud-Sud-Est')
    
    if i >= 0:
        DIR = vent_m_s(path)
        return 'Sud-Sud-Est', DIR

    k = str(code).find('Sud-Sud-Ouest')
    if k >= 0:
        DIR = vent_m_s(path)
        return 'Sud-Sud-Ouest', DIR

    l = str(code).find('Sud-Ouest')
    
    if l >= 0:
        DIR = vent_m_s(path)
        return 'Sud-Ouest', DIR

    m = str(code).find('Ouest-Sud-Ouest')
    
    if m >= 0:
        DIR = vent_m_s(path)
        return 'Ouest-Sud-Ouest', DIR

    o = str(code).find('Ouest-Nord-Ouest')
    
    if o >= 0:
        DIR = vent_m_s(path)
        return 'Ouest-Nord-Ouest', DIR

    p = str(code).find('Nord-Ouest')
    
    if p >= 0:
        DIR = vent_m_s(path)
        return 'Nord-Ouest', DIR

    q = str(code).find('Nord-Nord-Ouest')
    
    if q >= 0:
        DIR = vent_m_s(path)
        return 'Nord-Nord-Ouest', DIR


    b = str(code).find('Nord')
    
    if b >= 0:
        DIR = vent_m_s(path)
        return 'Nord', DIR

    f = str(code).find('Est')
    
    if f >= 0:
        DIR = vent_m_s(path)
        return 'Est', DIR

    j = str(code).find('Sud')
    
    if j >= 0:
        DIR = vent_m_s(path)
        return 'Sud', DIR

    n = str(code).find('Ouest')
    
    if n >= 0:
        DIR = vent_m_s(path)
        return 'Ouest', DIR

 
    
def traitement_ville(liste, liste1, nom_liste):


    liste2 = []

    c = 0
    for i in liste:
  
        vent = vent_voisin(str(liste1[c]), i, nom_liste)
       
        liste2.append([i, vent[0], vent[1]])
        
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
            liste1.append([i[0], i[1], i[2]])

    return liste1



def traitement_liste_France(liste, liste_ville):

    liste1 = []

    for i in liste:

        if i[0] == i: 
            a = apport_pollu_vent(i[1], direction_ville4)
            if a == True:
                liste1.append([i[0], i[1]])
            
        else:
            a = apport_pollu_vent(i[1], direction_ville44)
            
            if a == True:
                liste1.append([i[0], i[1]])

    return liste1


def vent_m_s(path):

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("span")
    liste = []
    liste.append(propriete)

 

    nb = ''
    stop = ''
    c = 0
    for i in liste[0]:
        nb = ''
        for j in i:
   
            try:
                j = int(j)
                if j == int(j):
                    nb += str(j)
                    stop = True     
            except:
                pass
        c+=1
        if stop == True:
            break

        
    
    return nb

    
def apport_pollu():

    liste = []
    
    a = traitement_ville(ville_haut_droite, num_ville1, 'ville_haut_droite')
    aa = traitement_liste(a, direction_ville1)
    aaa = voisinage(aa)

    print(aaa)
    print('\n')

    b = traitement_ville(ville_haut_gauche, num_ville, 'ville_haut_gauche')
    bb = traitement_liste(b, direction_ville)
    bbb = voisinage(bb)

    print(bbb)
    print('\n')

    c = traitement_ville(ville_haut_droite2, num_ville2, 'ville_haut_droite2')
    cc = traitement_liste(c, direction_ville2)
    ccc = voisinage(cc)

    print(ccc)
    print('\n')
    
    d =traitement_ville(ville_haut_droite3, num_ville3, 'ville_haut_droite3')
    dd = traitement_liste(d, direction_ville3)
    ddd = voisinage(dd)

    print(ddd)
    print('\n')
    
    e = traitement_ville(ville_haut_droite4, num_ville4, 'ville_haut_droite4')
    print(e)
    ee = traitement_liste_France(e, direction_ville4)
    eee = voisinage(ee)

    print(eee)
    print('\n')
    
    f =traitement_ville(bas_droite6, num_ville6, 'bas_droite6')
    ff = traitement_liste(f, direction_ville6)
    fff = voisinage(ff)

    print(fff)
    print('\n')
    
    g =traitement_ville(ville_bas_gauche9, num_ville9, 'ville_bas_gauche9')
    gg = traitement_liste(g, direction_ville9)
    ggg = voisinage(gg)

    print(ggg)
    print('\n')


    h =traitement_ville(ville_haut_droite5, num_ville5, 'ville_haut_droite5')
    hh = traitement_liste(h, direction_ville5)
    hhh = voisinage(hh)

    print(hhh)
    print('\n')

    i = traitement_ville(ville_bas_gauche8, num_ville8, 'ville_bas_gauche8')
    ii = traitement_liste(i, direction_ville8)
    iii = voisinage(ii)

    print(iii)
    print('\n')


    j =traitement_ville(ville_bas_droite7, num_ville7, 'ville_bas_droite7')
    jj = traitement_liste(j, direction_ville7)
    jjj = voisinage(jj)

    print(jjj)
    print('\n')

    liste.extend([aaa, bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj])
    print(liste)






    
    return liste


apport_pollu()














































