"""Here we define for site web
the numbers of particle,
ranking pollute in France and industrail poles"""

import requests
import datetime
import urllib.request
from bs4 import *


from .CONFIG import PATH_PARTICLE_RATE

def particule2(lieu):
    """we search particule rate from plumelabs"""

    nb = []
    liste = []

    path = PATH_PARTICLE_RATE.format(lieu)
    request = requests.get(path)
    page = request.content
    soup_html = BeautifulSoup(page, "html.parser")
    Property = soup_html.find_all("div", {'class':'report__pi-number'})

    for i in Property:
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
    polution = nb

    return polution


    
def france(place):


    liste = ["lyon", "marseille","paris","roubaix"]


    counter = 0
    for i in liste:

        if place == place[0]:
            return 'un'
            break

        elif place == place[1]:
            return 'deux'
            break

        elif place == place[2]:
            return 'trois'
            break

        elif place == place[3]:
            return 'quattre'
            break
        else:
            return 'non'
            break
           
        counter += 1
    



def industrie(place):


    if place == 'lyon':
        return 'oui'
    elif place == 'paris':
        return 'non'
    elif place == 'marseille':
        return 'oui'
    



