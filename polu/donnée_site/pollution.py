import requests
import urllib.request
from bs4 import *
import datetime


CLE = '5a72ceae1feda40543d5844b2e04a205'


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
    
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,CLE)
    r = requests.get(localisation)
    data=r.json()

    if donnée == 'vent':
        vent = data['wind']['speed']
        return vent
    
    elif donnée == 'météo':
        méteo = data['weather'][0]['main']

        data = ''
        
        if méteo == 'Clouds' or méteo == 'Mist':
            data = 'Nuageux'
        elif méteo == 'Rain' or méteo == 'Thunderstorm'\
             or méteo == 'Haze':
            data = 'Pluie'
        elif méteo == 'Clear':
            data = 'Beau temps'

        
        return  data

def climat_ville(lieu):
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,CLE)
    r = requests.get(localisation)
    data=r.json()

    température = data['main']['temp']
    température = température - 273.15

    return température

        
def saison():

    date = datetime.datetime.now()
    mois = date.month
    jour = date.day

   
    
    if mois == 12 or mois == 1\
       or mois == 2:
        return 'hiver'

    elif mois == 3 or mois == 4\
         or mois == 5:
        return 'primtemps'

    elif mois == 6 or mois == 7\
         or mois == 8\
         or mois == 9:
        return 'été'

    elif mois == 10 or mois == 11\
         or mois == 12:
        return 'automne'

def traffique(lieu):
    
    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute



    heure_pointe_semaine = [7,8,9,16,17,18,19]

    départ_routier = [(2,1), (5,1), (9,2), (16,2), (22,2),(23,2),
                      (1,3),(2,3),(8,3),(9,3),
                      (19,4),(22,4),(26,4),(27,4),(28,4),
                      (4,5),(5,5),(29,5),(30,5),
                      (5,6),(6,6),(7,6),(10,6),(28,6),
                      (5,7),(6,7),(7,7),(12,7),(13,7),(14,7),(19,7),(20,7),(21,7),(26,7),(27,7),(28,7),
                      (2,8),(3,8),(4,8),(9,8),(10,8),(11,8),(16,8),(17,8),(18,8),(19,8),(23,8),(24,8),(25,8),(30,8),(31,8),
                      (1,9),
                      (18,10),(25,10),(26,10),(31,10),
                      (3,11),(8,11),(11,11),
                      (20,12),(21,12),(22,12),(24,12),(27,12),(28,12)
        ]


    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""

    
    for i in départ_routier:
        if (jour, mois) == i :
            dep = 'Oui'

        elif (jour, mois) != i :
            normale = 'Oui'
            dep = 'Non'
            

    for i in heure_pointe_semaine:

        if i == heure:
            pointe = 'Oui'
            non_pointe = 'Non'
            break
        

    if pointe == '':
        pointe = 'Non'
        non_pointe = 'Oui'


    print('dep', dep)#TRAFIQUE['depart_routier'] += 1
    print('pointe', pointe)#HEURE['heure_pointe'] += 1
    print('normlame', normale)#regulier jour
    print('non pointe', non_pointe)#HEURE['non_heure_pointe jour'] += 1


    return dep, pointe, normale, non_pointe



















