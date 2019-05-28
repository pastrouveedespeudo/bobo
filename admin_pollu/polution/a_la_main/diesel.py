import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *


def recup_balise():

    
    path = "https://prixdubaril.com/"

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'carburant_red'})

    a = str(propriete).find('Gas')
    b = str(propriete).find('Gas+')
    c = str(propriete).find('Gazole')
    d = str(propriete).find('Gazole+')
    

    gas = ''
    gasplus = ''
    
    if a or c >= 0:
        gas = True
    elif b or d >=0:
        gasplus = True


    return gas, gasplus



def cours_dollar():
    
    path = "https://prixdubaril.com/"

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("span")


    liste = []
    liste.append(str(propriete))


    print('dolar', liste[0][520:525])
    dollar = liste[0][520:525]
    
    if dollar[0] == '+':
        print('non baisse')
    else:
        print('baisse')



recup_balise()
cours_dollar()














