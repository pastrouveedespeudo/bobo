import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color

from boussole import *


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





    

















