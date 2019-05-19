from django.shortcuts import render
import requests
import urllib.request
import datetime
from bs4 import *

from .donnée_site.pollution import taux_particule
from .donnée_site.pollution import temps_ville
from .donnée_site.pollution import climat_ville
from .donnée_site.pollution import saison
from .donnée_site.pollution import traffique
from .donnée_site.pollution import habitude
from .donnée_site.pollution import ville_pollué_classement
from .donnée_site.pollution import region_industrielle


def home(request):
    return render(request, 'home.html')


def polution(request):

    return render(request, 'polution.html')



def charger(request):
    return render(request, 'charger.html')

def donnée(request):

    data_lyon = taux_particule('lyon')
    data_paris = taux_particule('paris')
    data_marseille = taux_particule('marseille')
    print(data_lyon, data_paris, data_marseille)


    météo_lyon = temps_ville('lyon', 'météo')
    vent_lyon = temps_ville('lyon', 'vent')

    météo_paris = temps_ville('paris', 'météo')
    vent_paris = temps_ville('paris', 'vent')

    météo_marseille = temps_ville('marseille', 'météo')
    vent_marseille = temps_ville('marseille', 'vent')

    température_lyon = climat_ville('lyon')
    température_paris = climat_ville('paris')
    température_marseille = climat_ville('marseille')

    saison_actuelle =  saison()

    traffique_lyon = traffique('lyon')
    départ_routier_lyon = traffique_lyon[0] 
    heure_pointe_lyon = traffique_lyon[1] 
    regulier_jour_lyon = traffique_lyon[2] 
    non_pointe_lyon = traffique_lyon[3] 


    traffique_paris = traffique('paris')
    départ_routier_paris = traffique_paris[0] 
    heure_pointe_paris = traffique_paris[1] 
    regulier_jour_paris = traffique_paris[2] 
    non_pointe_paris = traffique_paris[3] 


    
    traffique_marseille = traffique('marseille')
    départ_routier_marseille = traffique_marseille[0] 
    heure_pointe_marseille = traffique_marseille[1] 
    regulier_jour_marseille = traffique_marseille[2] 
    non_pointe_marseille = traffique_marseille[3] 

    jour = habitude()

    classement_lyon = ville_pollué_classement('lyon')
    classement_paris = ville_pollué_classement('paris')
    classement_marseille = ville_pollué_classement('marseille')

    pole_lyon = region_industrielle('lyon')
    pole_paris = region_industrielle('paris')
    pole_marseille = region_industrielle('marseille')

    pression_lyon = pression_ville('lyon')
    pression_paris = pression_ville('paris')
    pression_marseille = pression_ville('marseille')


    return render(request, 'donnée.html', {'lyon':data_lyon,
                                           'paris':data_paris,
                                           'marseille':data_marseille,
                                           'météo_lyon':météo_lyon,
                                           'météo_marseille':météo_marseille,
                                           'météo_paris':météo_paris,
                                           'vent_lyon':vent_lyon,
                                           'vent_paris':vent_paris,
                                           'vent_marseille':vent_marseille,
                                           'température_lyon':round(température_lyon),
                                           'température_paris':round(température_paris),
                                           'température_marseille':round(température_marseille),
                                           'saison_actuelle':saison_actuelle,
                                           'départ_routier_lyon':départ_routier_lyon,
                                           'heure_pointe_lyon':heure_pointe_lyon,
                                           'regulier_jour_lyon':regulier_jour_lyon,
                                           'non_pointe_lyon':non_pointe_lyon,
                                           'départ_routier_paris':départ_routier_paris,
                                           'heure_pointe_paris':heure_pointe_paris,
                                           'regulier_jour_marseille':regulier_jour_marseille,
                                           'non_pointe_marseille':non_pointe_marseille,
                                           'départ_routier_paris':départ_routier_paris,
                                           'heure_pointe_paris':heure_pointe_paris,
                                           'regulier_jour_paris':regulier_jour_paris,
                                           'non_pointe_paris':non_pointe_paris,
                                           'weekend':jour[0],
                                           'jour_semaine':jour[1],
                                           'classement_lyon':classement_lyon,
                                           'classement_paris':classement_paris,
                                           'classement_marseille':classement_marseille,
                                           'pole_lyon':pole_lyon,
                                           'pole_paris':pole_paris,
                                           'pole_marseille':pole_marseille,
                                           'pression_lyon':pression_lyon,
                                           'pression_paris':pression_paris,
                                           'pression_marseille':,pression_marseille})


    return render(request, 'donnée.html')





















def machine_a_o(request):
    return render(request, 'machine a o.html')

def prediction(request):
    return render(request, 'prediction.html')



def polution_lyon(request):


    a = heure()
    b = temps("lyon")
    c = particule("lyon")
    

    return render(request, 'polution_lyon.html', {'heure':a[0],'minute':a[1], 'temps':b, 'pollution':c})



def polution_marseille(request):

    a = heure()
    b = temps("marseille")
    c = particule("marseille")

    
    return render(request, 'polution_marseille.html', {'heure':a[0],'minute':a[1], 'temps':b, 'pollution':c})

def polution_paris(request):

    a = heure()
    b = temps("paris")
    c = particule("paris")
    
    return render(request, 'polution_paris.html', {'heure':a[0],'minute':a[1], 'temps':b, 'pollution':c})


def graphique(request):
    return render(request, 'graphique.html')




def heure():

    date = datetime.datetime.now()

    heure = date.hour
    minute = date.minute

    return heure, minute





def temps(lieu):

    clé = '5a72ceae1feda40543d5844b2e04a205'
        
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)

    r = requests.get(localisation)

    data=r.json()
    
    méteo = data['weather'][0]['main']

    if méteo == "Clear":
        méteo = "Beau"

    elif méteo == "Clouds":
        méteo = "Nuageux"
    return méteo


def particule(lieu):


    path = "https://air.plumelabs.com/fr/live/{}".format(lieu)

    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    liste = []
    propriete = soup.find_all("div")
    for i in propriete:
        liste.append(i.get_text())

    phrase_clé = "a atteint un niveau élevé de pollution. Supérieur à la limite maximum pour 24h établie par l'OMS"
    
    recherche_taux = str(liste).find(str(phrase_clé))
    liste_epluché = liste[20:21]
    polution = liste_epluché[0][31:34]

    return polution
    



















