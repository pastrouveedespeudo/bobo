import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *


def recup_balise():

    dol = cours_dollar()
    
    
    path = "https://prixdubaril.com/"

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'carburant_red'})

    a = str(propriete).find('Gas')
    b = str(propriete).find('Gas+')
    c = str(propriete).find('Gazole')
    d = str(propriete).find('Gazole+')
    

    gas = False
    gasplus = False
    
    if a or c >= 0:
        gas = True
    elif b or d >=0:
        gasplus = True


    

    if gas == True and gasplus == True and dol  == 'dollard baisse  ':
        return 'tres fort'

    elif gas == True and gasplus == False and dol == 'dollard augmente':
        return 'moyen'

    elif gas == False and gasplus == True and dol == 'dollard augmente':
        return 'moyen'


    elif gas == False and gasplus == False and dol == 'dollard augmente':
        return 'bas'


    elif gas == True and gasplus == False and dol == 'dollard baisse  ':
        return 'fort'

    elif gas == False and gasplus == True and dol == 'dollard baisse  ':
        return 'fort'


    
def cours_dollar():
    
    path = "https://prixdubaril.com/"

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("span")


    liste = []
    liste.append(str(propriete))


    dollar = liste[0][520:525]
    
    if dollar[0] == '+':
        return 'dollard augmente'
    else:
       return 'dollard baisse  '





#print(recup_balise())












