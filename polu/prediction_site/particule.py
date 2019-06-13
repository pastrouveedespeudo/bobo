import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops





def particule2(lieu):

    liste = []
    nb = []

    path = "https://air.plumelabs.com/fr/live/{}".format(lieu)

    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'report__pi-number'})
    for i in propriete:
        liste.append(i.get_text())
    for i in liste:
        for j in i:
            try:
                j = int(j)
                if j == int(j):
                    nb.append(str(j))
            except:
                pass

    
    nb = ''.join(nb)
    nb = int(nb)

    phrase_clé = "a atteint un niveau élevé de pollution. Supérieur à la limite maximum pour 24h établie par l'OMS"

    polution = nb
    #polution = int(polution)

    return nb


    
def france(lieu):


    liste = ["lyon", "marseille","paris","roubaix"]


    c = 0
    for i in liste:

        if lieu == liste[0]:
            return 'un'
            break

        elif lieu == liste[1]:
            return 'deux'
            break

        elif lieu == liste[2]:
            return 'trois'
            break

        elif lieu == liste[3]:
            return 'quattre'
            break
        else:
            return 'non'
            break
            

            
        c+=1
    


def industrie(lieu):


##
##    path = "https://fr.wikipedia.org/wiki/{}".format(lieu) 
##
##    r = requests.get(path)
##
##    page = r.content
##    soup = BeautifulSoup(page, "html.parser")
##    propriete = soup.find('table',attrs={"class":u"infobox_v2"})
##    propriete = str(propriete)
##
##    try:
##        code_postal = propriete[5649:5654]
##        code_postal = int(code_postal)
##        
##    except:
##        pass
##
##    liste = []
##
##    path = "http://www.cartesfrance.fr/recherche/?q={}".format(code_postal)
##
##    r = requests.get(path)
##
##    page = r.content
##    soup = BeautifulSoup(page, "html.parser")
##    
##    propriete = soup.find_all('Département')
##
##
##
##
##    pole_poluant = {'1':'Nord',
##                    '2':'Bouches-du-Rhône',
##                    '3':'Moselle',
##                    '4':'Seine-Maritime',
##                    '5':'Loire-Atlantique',
##                    '6':'Haute-Normandie',
##                    '7':'Meurthe-et-Moselle',
##                    '8':'Seine-Maritime',
##                    '9':'Rhône'
##
##                    }
    if lieu == 'lyon':
        return 'oui'
    elif lieu == 'paris':
        return 'non'
    elif lieu == 'marseille':
        return 'oui'
    
##    for i in pole_poluant.keys():
##        a = str(soup).find(str(pole_poluant[i]))
##        print(a,pole_poluant[i])


##
##    if a > 0:
##        return 'oui'
##
##    else:
##        return 'non'
        














