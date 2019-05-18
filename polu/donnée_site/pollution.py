import requests
import urllib.request
from bs4 import *

def taux_particule(lieu):
    
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
    polution = nb

    print(polution)
    return polution



def temps_ville(lieu, donnée):
    
    clé = '5a72ceae1feda40543d5844b2e04a205'

    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
    r = requests.get(localisation)
    data=r.json()

    if donnée == 'vent':
        vent = data['wind']['speed']
        return vent
    
    elif donnée == 'météo':
        méteo = data['weather'][0]['main']
        return  méteo

    

    






























