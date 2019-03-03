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



def polution_lyon(request):


    a = heure()

    clé = '5a72ceae1feda40543d5844b2e04a205'
        
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format("lyon",clé)

    r = requests.get(localisation)

    data=r.json()
    print(data)
    méteo = data['weather'][0]['main']

    if méteo == "Clear":
        méteo = "Beau"


    path = "https://air.plumelabs.com/fr/live/lyon"

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
    polution = liste_epluché[0][31:33]
    


    return render(request, 'polution_lyon.html', {'heure':a[0],'minute':a[1], 'temps':méteo, 'pollution':polution})



def polution_marseille(request):
    return render(request, 'polution_marseille.html')

def polution_paris(request):
    return render(request, 'polution_paris.html')



def heure():

    date = datetime.datetime.now()

    heure = date.hour
    minute = date.minute

    return heure, minute
