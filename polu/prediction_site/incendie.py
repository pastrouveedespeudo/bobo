import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
import datetime

PATH_LYON = 'https://www.lyoncapitale.fr/?s=incendie'
PATH_MARSEILLE = 'https://www.20minutes.fr/search?q=incendie+marseille'
PATH_PARIS = 'https://www.20minutes.fr/search?q=incendie+paris'


def incendie(ville):

    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year


    dico = {'1':'janvier','2':'fevrier','3':'mars','4':'avril',
            '5':'mai','6':'juin','7':'juillet','8':'août',
            '9':'septembre','10':'octobre','11':'novembre','12':'decembre'}


    for cle, valeur in dico.items():
        if str(mois) == cle:
            mois = valeur


    
    ville = ville.lower()

    if ville == 'lyon':
        path = PATH_LYON
        r = requests.get(path)


        page = r.content
        soup = BeautifulSoup(page, "html.parser")

        propriete = soup.find_all("div")

        liste = []

        liste.append(str(propriete))
        daate = str(jour) + ' ' + str(mois) + ' ' + str(année)

        a = str(liste).find(str(daate))

    elif ville == 'paris':
        path = PATH_PARIS
    elif ville == 'marseille':
        path = PATH_MARSEILLE
    
    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div")

    liste = []
    liste.append(str(propriete))

    a = str(liste).find('incendie')

    liste = liste[0][a-1000:a+1000]

    mois_chi = date.month

    c = 0
    for i in str(mois_chi):
        c+=1

    if c == 1:
        daate1 = str(année) + '-0' + str(mois_chi)+'-'+str(jour)
        daate3 = str(jour) + '-0' + str(mois_chi)+'-'+str(année)
    else:
        daate1 = str(année) + '-' + str(mois_chi)+'-'+str(jour)
        daate3 = str(jour) + '-' + str(mois_chi)+'-'+str(année)
        
    daate = str(jour) + ' ' + str(mois) + ' ' + str(année)
    

    b = str(liste).find(daate)
    c = str(liste).find(daate1)
    d = str(liste).find(daate3)

    if b >= 0 or c >= 0 or d >=0:
        return 'oui'
    









































