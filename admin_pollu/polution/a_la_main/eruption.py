import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *



def eruption():

        
    date = datetime.datetime.now()
    
    
    mois = date.month
    année = date.year

    
    mois = str(mois)
    année = str(année)



    dico = {'1':'January', '2':'February', '3':'March','4':'April','5':'May','6':'June',
            '7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

    le_mois = ''

    for cle, valeur in dico.items():
        if str(mois) == cle:
            le_mois = valeur


    


    
    

    path = "https://www.volcanodiscovery.com/fr/volcanoes/today.html"

    r = requests.get(path)

    page = r.content

    soup = BeautifulSoup(page, "html.parser")

    
    propriete = soup.find_all("div", {"class":"ln"})

    liste = []

    liste.append(str(propriete))


    #print(liste)

    liste2 = []

    for i in range(7):

        jour = date.day
        jour = str(jour-i)

        a_chercher = jour +' '+le_mois + ' ' + année
        a_chercher1 = le_mois + ' ' + jour + ' ' + année

        
        a_chercher2 = jour+'-'+mois+'-'+année
        a_chercher3 = jour+'-'+le_mois+'-'+année
        a_chercher4 = le_mois + ' ' + jour + ', ' + année


        a = str(liste).find(str(a_chercher))
        b = str(liste).find(str(a_chercher1))
        c = str(liste).find(str(a_chercher2))
        d = str(liste).find(str(a_chercher3))
        e = str(liste).find(str(a_chercher4))

        if a >= 0 or b >= 0 or c >=0 or d >= 0 or e >=0:
            jour = str(jour) + ' ' + mois
            liste2.append(jour)



    print(liste2)    

    














eruption()












