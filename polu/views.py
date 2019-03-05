from django.shortcuts import render
import requests
import urllib.request
import datetime
from bs4 import *


def home(request):
    return render(request, 'home.html')


def polution(request):
    return render(request, 'polution.html')

def charger(request):
    return render(request, 'charger.html')

def donnée(request):
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
    



















